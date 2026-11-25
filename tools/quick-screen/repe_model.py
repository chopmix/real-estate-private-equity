#!/usr/bin/env python3
"""Build a live-formula underwriting workbook from a deal JSON.

Usage: python3 repe_model.py <deal.json> <out.xlsx>

Every calculated cell is an Excel formula. Only the Inputs sheet holds typed
values (blue font). No macros, external links, circular references or data
tables. Layout follows repe-core/references/excel-standard.md.
"""
import os
import re
import sys

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter as CL
    from openpyxl.workbook.defined_name import DefinedName
    from openpyxl.worksheet.datavalidation import DataValidation
except ImportError:
    sys.exit("openpyxl is required: pip install openpyxl")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from repe_calc import load_deal  # input normalization only; math lives in the formulas

# ---------------------------------------------------------------- styles
BLUE, BLACK, GREEN = "0000FF", "000000", "008000"
USD = '$#,##0_);($#,##0)'
PSF = '$#,##0.00_);($#,##0.00)'
PCT1 = '0.0%'
PCT2 = '0.00%'
MULT = '0.00"x"'
NUM = '#,##0'
NUM1 = '#,##0.0'
HDR_FILL = PatternFill("solid", fgColor="1F3864")
SEC_FILL = PatternFill("solid", fgColor="D9E1F2")
CHK_FILL = PatternFill("solid", fgColor="E2EFDA")
LINK_RE = re.compile(r"^=(?:'?[A-Za-z ]+'?!\$?[A-Z]{1,3}\$?\d+|[A-Za-z_][A-Za-z0-9_]*)$")
CREDIT = "Model standard: Real Estate Private Equity plugin by Chi Hathiramani, CH Consulting (chiraghathiramani.com)"
YR = range(12)          # year 0 .. year 11 in columns C .. N


def ycol(t):
    return CL(3 + t)


class Sheet:
    """Small writer that applies the color code automatically."""

    def __init__(self, wb, title, widths=None):
        self.ws = wb.create_sheet(title)
        self.name = title
        self.ws.column_dimensions["A"].width = 44
        for i in range(2, 30):
            self.ws.column_dimensions[CL(i)].width = 14
        for k, v in (widths or {}).items():
            self.ws.column_dimensions[k].width = v

    def put(self, ref, value, fmt=None, typed=False, bold=False):
        c = self.ws[ref]
        c.value = value
        if typed:
            color = BLUE
        elif isinstance(value, str) and value.startswith("="):
            color = GREEN if LINK_RE.match(value) else BLACK
        else:
            color = BLACK
        c.font = Font(color=color, bold=bold)
        if fmt:
            c.number_format = fmt
        return c

    def label(self, row, text, col="A", bold=False, fill=None):
        c = self.ws[f"{col}{row}"]
        c.value = text
        c.font = Font(bold=bold, color="FFFFFF" if fill is HDR_FILL else BLACK)
        if fill:
            c.fill = fill
        return c

    def title(self, text, sub=None):
        self.label(1, text, bold=True)
        self.ws["A1"].font = Font(bold=True, size=14)
        if sub:
            self.label(2, sub)

    def section(self, row, text, last_col=14):
        for i in range(1, last_col + 1):
            self.ws.cell(row=row, column=i).fill = SEC_FILL
        self.label(row, text, bold=True)

    def year_header(self, row=4, flags=True, col0=3, hold="Hold"):
        """Year numbers, in-hold flag and sale-year flag, all formulas."""
        self.label(row, "Year", bold=True, fill=HDR_FILL)
        for t in YR:
            c = CL(col0 + t)
            self.put(f"{c}{row}", "=0" if t == 0 else f"={CL(col0 + t - 1)}{row}+1", "0", bold=True)
            self.ws[f"{c}{row}"].fill = HDR_FILL
            self.ws[f"{c}{row}"].font = Font(color="FFFFFF", bold=True)
        if flags:
            self.label(row + 1, "In hold (1 = yes)")
            self.label(row + 2, "Sale year (1 = yes)")
            for t in YR:
                c = CL(col0 + t)
                self.put(f"{c}{row + 1}", f"=IF(AND({c}${row}>=1,{c}${row}<={hold}),1,0)", "0")
                self.put(f"{c}{row + 2}", f"=IF({c}${row}={hold},1,0)", "0")
        self.ws.freeze_panes = self.ws.cell(row=row + 1, column=col0)

    def yrow(self, row, label, fn, fmt=USD, years=YR, bold=False):
        """Write one annual row. fn(t, col, prev_col) returns a formula or None."""
        self.label(row, label, bold=bold)
        for t in years:
            f = fn(t, ycol(t), ycol(t - 1) if t > 0 else None)
            if f is not None:
                self.put(f"{ycol(t)}{row}", f, fmt, bold=bold)
        return row


class Builder:
    def __init__(self, d):
        self.d = d
        self.raw = d["raw"]
        self.wb = Workbook()
        self.wb.remove(self.wb.active)
        self.r = {}       # remembered row numbers
        # create sheets in the standard order
        order = ["Summary", "Inputs", "Revenue", "CashFlow", "Debt", "Returns",
                 "Waterfall", "Sensitivity", "Checks", "Sources"]
        self.s = {n: Sheet(self.wb, n) for n in order}

    # -------------------------------------------------------------- names
    def name(self, nm, sheet, ref):
        col, row = re.match(r"([A-Z]+)(\d+)", ref).groups()
        self.wb.defined_names[nm] = DefinedName(nm, attr_text=f"{sheet}!${col}${row}")

    def name_range(self, nm, sheet, c1, c2, row):
        self.wb.defined_names[nm] = DefinedName(nm, attr_text=f"{sheet}!${c1}${row}:${c2}${row}")

    def tag(self, key):
        tags = self.d["source_tags"]
        if key in tags:
            return tags[key]
        present = any(isinstance(v, dict) and key in v for v in self.raw.values()) or key in self.raw
        return "[User]" if present else "[Assumed]"

    # -------------------------------------------------------------- inputs
    def build_inputs(self):
        d, S = self.d, self.s["Inputs"]
        ws = S.ws
        S.title("Inputs", "Blue = typed input. Black = formula. Change values here only.")
        for i, h in enumerate(["Input", "Value", "Unit", "Source", "Note", "Base", "Upside", "Downside"]):
            S.label(4, h, col=CL(1 + i), bold=True, fill=HDR_FILL)
        ws.column_dimensions["E"].width = 36
        row = [5]

        def add(nm, label, value, unit="", fmt=None, key=None, note="", typed=True):
            r = row[0]
            S.label(r, label)
            if isinstance(value, list):           # scenario driver
                for i, v in enumerate(value):
                    S.put(f"{CL(6 + i)}{r}", v, fmt, typed=True)
                S.put(f"B{r}", f"=CHOOSE(ScenIdx,F{r},G{r},H{r})", fmt)
                note = note or "Scenario driver: value follows the scenario switch"
            else:
                S.put(f"B{r}", value, fmt, typed=typed)
            S.label(r, unit, col="C")
            S.label(r, self.tag(key) if key else "[User]", col="D")
            S.label(r, note, col="E")
            if nm:
                self.name(nm, "Inputs", f"B{r}")
            row[0] += 1
            return r

        def sec(text):
            row[0] += 1
            S.section(row[0], text, 8)
            row[0] += 1

        sec("General")
        add("DealName", "Deal name", d["deal_name"], key="deal_name")
        add("PropertyType", "Property type", d["property_type"], key="property_type")
        add("Engine", "Revenue engine", d["engine"], key="engine", note="unit, lease or operating")
        r = add("Scenario", "Scenario switch", d["scenario"], key="scenario", note="Base, Upside or Downside")
        for i, n in enumerate(["Base", "Upside", "Downside"]):
            S.put(f"{CL(6 + i)}{r}", n, typed=True)
        self.r["scen_row"] = r
        dv = DataValidation(type="list", formula1='"Base,Upside,Downside"', allow_blank=False)
        ws.add_data_validation(dv)
        dv.add(f"B{r}")
        add("ScenIdx", "Scenario index", f"=MATCH(Scenario,F{r}:H{r},0)", typed=False,
            note="Formula: position of the scenario in the list")
        add("Hold", "Hold period", d["hold"], "years", "0", key="hold_years", note="1 to 10; sale at end of hold on next-year NOI")

        sec("Acquisition")
        add("PurchasePrice", "Purchase price", d["price"], "$", USD, "purchase_price")
        add("ClosingPct", "Closing costs", d["closing_pct"], "% of price", PCT2, "closing_cost_pct")
        add("UpfrontCapex", "Upfront capital funded at close", d["upfront_capex"], "$", USD, "upfront_capex")
        add("TrailingNOI", "Trailing 12-month NOI (Year 0)", d["trailing_noi"], "$", USD, "trailing_noi")

        sec("Scenario drivers")
        add("RentGrowth", "Rent / rate growth", d["rent_growth"], "% per year", PCT2, "rent_growth")
        add("ExpenseGrowth", "Expense growth", d["expense_growth"], "% per year", PCT2, "expense_growth")
        add("ExitCap", "Exit cap rate", d["exit_cap"], "%", PCT2, "exit_cap")
        if d["engine"] == "operating":
            add("OccAdj", "Occupancy adjustment", d["vacancy"], "points", PCT2, "occupancy_adjustment",
                "Added to the occupancy schedule each year")
        elif d["engine"] == "unit":
            add("Vacancy", "Physical vacancy", d["vacancy"], "% of rent", PCT2, "vacancy")
        else:
            add("Vacancy", "General vacancy and credit loss", d["vacancy"], "% of revenue", PCT2, "vacancy")
        add("SaleCostPct", "Sale costs", d["sale_cost_pct"], "% of value", PCT2, "sale_cost_pct")

        sec("Revenue engine: " + d["engine"])
        if d["engine"] == "unit":
            add("ConcessionPct", "Concessions", d["concessions_pct"], "% of rent", PCT2, "concessions_pct")
            add("BadDebtPct", "Bad debt", d["bad_debt_pct"], "% of rent", PCT2, "bad_debt_pct")
            add("OtherIncome", "Other income, Year 1", d["other_income"], "$", USD, "other_income")
            add("LTLBurn", "Loss to lease burn-off", d["ltl_burnoff"], "years", "0.0", "loss_to_lease_burnoff_years")
        elif d["engine"] == "lease":
            add("OtherIncome", "Other income, Year 1", d["other_income"], "$", USD, "other_income")
        else:
            add("Keys", "Units or keys", d["keys"], "count", NUM, "keys")
            add("RateY1", "Rate per occupied unit, Year 1", d["rate"], "$", PSF, "rate")
            add("RatePeriods", "Rate periods per year", d["rate_periods"], "365 = daily, 12 = monthly", "0", "rate_basis")
            add("OtherRevPct", "Other revenue", d["other_rev_pct"], "% of unit revenue", PCT2, "other_revenue_pct")
            add("DeptPct", "Departmental expenses", d["dept_pct"], "% of revenue", PCT2, "departmental_expense_pct")
            add("UndistPct", "Undistributed expenses", d["undist_pct"], "% of revenue", PCT2, "undistributed_expense_pct")
            add("FFEPct", "FF&E reserve", d["ffe_pct"], "% of revenue", PCT2, "ffe_reserve_pct")

        sec("Operating expenses")
        add("MgmtFeePct", "Management fee", d["mgmt_fee_pct"], "% of EGI", PCT2, "management_fee_pct")
        add("TaxReassess", "Reassess property tax at purchase (1 = yes)", d["tax_reassess"], "1 / 0", "0", "reassess")
        add("CurrentTax", "Current property tax, Year 1", d["current_tax"], "$", USD, "current_tax")
        add("AssessRatio", "Assessment ratio", d["assess_ratio"], "% of price", PCT2, "assessment_ratio")
        add("TaxRate", "Tax rate", d["tax_rate"], "% of assessed value", "0.000%", "tax_rate")
        add("Insurance", "Insurance, Year 1", d["insurance"], "$", USD, "insurance")
        if d["engine"] != "operating":
            add("Reserves", "Replacement reserves, Year 1", d["reserves"], "$", USD, "replacement_reserves",
                "Below NOI; grows with expenses")

        sec("Debt")
        add("DebtMode", "Loan mode", d["debt_mode"], "Sized / Stated", None, "mode")
        add("StatedLoan", "Stated loan amount", d["stated_loan"], "$", USD, "stated_amount", "Used only in Stated mode")
        add("MaxLTV", "Maximum LTV", d["max_ltv"], "%", PCT1, "max_ltv")
        add("MinDSCR", "Minimum DSCR", d["min_dscr"], "x", MULT, "min_dscr")
        add("MinDY", "Minimum debt yield", d["min_dy"], "%", PCT2, "min_debt_yield")
        add("LoanRate", "Interest rate", d["loan_rate"], "% per year", PCT2, "rate")
        add("IOYears", "Interest-only years", d["io_years"], "years", "0", "io_years")
        add("AmortYears", "Amortization", d["amort_years"], "years (0 = full IO)", "0", "amort_years")
        add("LoanFeePct", "Loan fee", d["loan_fee_pct"], "% of loan", PCT2, "loan_fee_pct")

        sec("Waterfall")
        add("InvShare", "Investor share of equity", d["inv_share"], "%", PCT1, "investor_share",
            "Sponsor co-invest is the remainder")
        add("PrefRate", "Preferred return (compounds annually)", d["pref"], "%", PCT2, "pref_rate")
        for i, (h, p) in enumerate(d["tiers"], start=1):
            add(f"Hurdle{i}", f"Tier {i} hurdle (investor IRR)", h, "%", PCT2, "tiers")
            add(f"Promote{i}", f"Tier {i} promote, below hurdle {i}", p, "% of tier cash", PCT1, "tiers")
        add("FinalPromote", "Promote above the last hurdle", d["final_promote"], "% of cash", PCT1, "final_promote")
        add("AcqFeePct", "Acquisition fee", d["acq_fee_pct"], "% of price", PCT2, "acquisition_fee_pct")
        add("AMFeePct", "Asset management fee", d["am_fee_pct"], "% of equity per year", PCT2, "asset_management_fee_pct")
        add("DispFeePct", "Disposition fee", d["disp_fee_pct"], "% of sale price", PCT2, "disposition_fee_pct")

        sec("Hurdle and sensitivity steps")
        add("HurdleIRR", "Firm levered IRR hurdle", d["hurdle_irr"], "%", PCT2, "hurdle_irr")
        add("CapStep", "Exit cap step", d["cap_step"], "%", PCT2, "exit_cap_step")
        add("NOIStep", "NOI versus plan step", d["noi_step"], "%", PCT1, "noi_step")
        add("PriceStep", "Price step (grid)", d["price_step"], "%", PCT1, "price_step")
        add("RateStep", "Interest rate step", d["rate_step"], "%", PCT2, "rate_step")
        add("LadderLow", "Price ladder start", d["ladder_low"], "% of price", PCT1, "ladder_low")
        add("LadderStep", "Price ladder step", d["ladder_step"], "% of price", PCT1, "ladder_step")
        add("CheckTolRate", "Check tolerance on rates", 0.000001, "decimal", "0.000000", "check_tolerance",
            "Used by the Checks sheet for rate tie-outs")

        # ---- tables
        def table(title, headers, rows, fmts, src_key):
            sec(title)
            hr = row[0]
            for i, h in enumerate(headers):
                S.label(hr, h, col=CL(1 + i), bold=True, fill=HDR_FILL)
            row[0] += 1
            first = row[0]
            for rec in rows:
                for i, (v, f) in enumerate(zip(rec[:-1], fmts)):
                    if v is None:
                        continue
                    if i == 0:
                        S.put(f"A{row[0]}", v, typed=True)
                    else:
                        S.put(f"{CL(1 + i)}{row[0]}", v, f, typed=True)
                S.label(row[0], rec[-1], col=CL(len(headers)))
                row[0] += 1
            return first

        if d["engine"] == "unit":
            self.r["mix"] = table(
                "Unit mix (rents per unit per month)",
                ["Unit type", "Units", "SF per unit", "In-place rent", "Market rent", "Renovation premium",
                 "Renovations per year", "Cost per unit", "Source"],
                [[u["type"], u["count"], u["sf"], u["in_place_rent"], u["market_rent"], u["renovation_premium"],
                  u["renovations_per_year"], u["renovation_cost_per_unit"], u["source"]] for u in d["unit_mix"]],
                [None, NUM, NUM, USD, USD, USD, NUM1, USD], "unit_mix")
        elif d["engine"] == "lease":
            self.r["ten"] = table(
                "Tenant table (rents and costs per SF per year)",
                ["Tenant", "SF", "Rent PSF", "Annual bump", "Expiry year", "Renewal probability",
                 "Downtime months", "Market rent PSF", "TI new PSF", "TI renewal PSF", "LC new PSF",
                 "LC renewal PSF", "Recovery PSF", "Source"],
                [[t["name"], t["sf"], t["rent_psf"], t["bump"], t["expiry"], t["renew_prob"], t["downtime"],
                  t["market_psf"], t["ti_new"], t["ti_ren"], t["lc_new"], t["lc_ren"], t["recovery_psf"],
                  t["source"]] for t in d["tenants"]],
                [None, NUM, PSF, PCT1, "0", PCT1, "0.0", PSF, PSF, PSF, PSF, PSF, PSF], "tenants")
            if d["vacant_suites"]:
                self.r["vac"] = table(
                    "Vacant suites (lease-up)",
                    ["Suite", "SF", "Market rent PSF", "Lease-up year", "Annual bump", "TI new PSF",
                     "LC new PSF", "Recovery PSF", "Source"],
                    [[v["name"], v["sf"], v["market_psf"], v["lease_up"], v["bump"], v["ti_new"], v["lc_new"],
                      v["recovery_psf"], v["source"]] for v in d["vacant_suites"]],
                    [None, NUM, PSF, "0", PCT1, PSF, PSF, PSF], "vacant_suites")
        self.r["exp"] = table(
            "Expense line items (Year 1; blank growth uses expense growth)",
            ["Expense", "Year 1 amount", "Growth", "Source"],
            [[i["name"], i["amount"], i["growth"], i["source"]] for i in d["expense_items"]],
            [None, USD, PCT2], "items")

        # ---- annual vectors (columns C..N = years 0..11, same as other sheets)
        sec("Annual inputs (columns are years 0 to 11)")
        hr = row[0]
        S.label(hr, "Year", bold=True, fill=HDR_FILL)
        for t in YR:
            S.put(f"{ycol(t)}{hr}", t, "0", typed=True)
        row[0] += 1
        self.r["capex_in"] = row[0]
        S.label(row[0], "Capital expenditure schedule ($)")
        for t in range(1, 12):
            S.put(f"{ycol(t)}{row[0]}", d["capex"][t - 1], USD, typed=True)
        row[0] += 1
        if d["engine"] == "operating":
            self.r["occ_in"] = row[0]
            S.label(row[0], "Occupancy schedule (before scenario adjustment)")
            for t in range(1, 12):
                S.put(f"{ycol(t)}{row[0]}", d["occupancy"][t - 1], PCT1, typed=True)
            row[0] += 1
        ws.freeze_panes = "B5"

    # -------------------------------------------------------------- revenue
    def build_revenue(self):
        d, S = self.d, self.s["Revenue"]
        S.title("Revenue", f"Engine: {d['engine']}. Annual, year-end. Deductions shown negative.")
        S.year_header()
        r = 8
        Y = range(1, 12)
        I = lambda col, row: f"Inputs!${col}${row}"
        gf = lambda c: f"(1+RentGrowth)^({c}$4-1)"
        if d["engine"] == "unit":
            gpr_rows, ltl_rows, cap_rows = [], [], []
            for k, u in enumerate(d["unit_mix"]):
                ir = self.r["mix"] + k
                S.section(r, u["type"])
                r += 1
                mkt = S.yrow(r, "Market rent per unit per month", lambda t, c, p: f"={I('E', ir)}*{gf(c)}", USD, Y)
                cum = S.yrow(r + 1, "Renovated units, cumulative",
                             lambda t, c, p: "=0" if t == 0 else f"=MIN({I('B', ir)},{I('G', ir)}*{c}$4)", NUM1)
                avg = S.yrow(r + 2, "Renovated units, average in year",
                             lambda t, c, p: f"=({p}{r + 1}+{c}{r + 1})/2", NUM1, Y)
                S.yrow(r + 3, "Gross potential rent (market plus premium)",
                       lambda t, c, p: f"=12*({I('B', ir)}*{c}{mkt}+{c}{avg}*{I('F', ir)}*{gf(c)})", USD, Y)
                S.yrow(r + 4, "Loss to lease (classic units)",
                       lambda t, c, p: f"=-12*({I('B', ir)}-{c}{avg})*({I('E', ir)}-{I('D', ir)})*{gf(c)}"
                                       f"*MAX(0,1-({c}$4-1)/MAX(1,LTLBurn))", USD, Y)
                S.yrow(r + 5, "Renovation capital",
                       lambda t, c, p: f"=({c}{cum}-{p}{cum})*{I('H', ir)}", USD, Y)
                gpr_rows.append(r + 3)
                ltl_rows.append(r + 4)
                cap_rows.append(r + 5)
                r += 7
            S.section(r, "Property revenue")
            r += 1
            sm = lambda rows: (lambda t, c, p: "=" + "+".join(f"{c}{x}" for x in rows))
            gpr = S.yrow(r, "Gross potential rent", sm(gpr_rows), USD, Y)
            ltl = S.yrow(r + 1, "Loss to lease", sm(ltl_rows), USD, Y)
            net = S.yrow(r + 2, "Net potential rent", lambda t, c, p: f"={c}{gpr}+{c}{ltl}", USD, Y)
            S.yrow(r + 3, "Vacancy", lambda t, c, p: f"=-{c}{net}*Vacancy", USD, Y)
            S.yrow(r + 4, "Concessions", lambda t, c, p: f"=-{c}{net}*ConcessionPct", USD, Y)
            S.yrow(r + 5, "Bad debt", lambda t, c, p: f"=-{c}{net}*BadDebtPct", USD, Y)
            S.yrow(r + 6, "Other income", lambda t, c, p: f"=OtherIncome*{gf(c)}", USD, Y)
            self.r["egi"] = S.yrow(r + 7, "Effective gross income", lambda t, c, p: f"=SUM({c}{net}:{c}{r + 6})", USD, Y, True)
            self.r["occ"] = S.yrow(r + 8, "Occupancy", lambda t, c, p: "=1-Vacancy", PCT1, Y)
            self.r["engcap"] = S.yrow(r + 9, "Renovation capital (to CashFlow)", sm(cap_rows), USD, Y)
            self.r["engopex"] = None
        elif d["engine"] == "lease":
            pot, vac, occ, rec, tilc = [], [], [], [], []
            for k, tn in enumerate(d["tenants"]):
                ir = self.r["ten"] + k
                E, B, F, G, H = (I(x, ir) for x in "EBFGH")
                bump = I("D", ir)
                S.section(r, tn["name"])
                r += 1
                S.yrow(r, "In-place rent", lambda t, c, p: f"=IF({c}$4<={E},{I('C', ir)}*{B}*(1+{bump})^({c}$4-1),0)", USD, Y)
                S.yrow(r + 1, "Rollover rent at market (potential)",
                       lambda t, c, p: f"=IF({c}$4>{E},{H}*(1+RentGrowth)^{E}*{B}*(1+{bump})^({c}$4-{E}-1),0)", USD, Y)
                S.yrow(r + 2, "Downtime vacancy (probability weighted)",
                       lambda t, c, p: f"=-IF({c}$4={E}+1,{H}*(1+RentGrowth)^{E}*{B}*(1-{F})*{G}/12,0)", USD, Y)
                S.yrow(r + 3, "Occupied SF (equivalent)", lambda t, c, p: f"=IF({c}$4={E}+1,{B}*(1-(1-{F})*{G}/12),{B})", NUM, Y)
                S.yrow(r + 4, "Recoveries",
                       lambda t, c, p: f"={I('M', ir)}*(1+ExpenseGrowth)^({c}$4-1)*{c}{r + 3}", USD, Y)
                S.yrow(r + 5, "TI and leasing commissions",
                       lambda t, c, p: f"=IF({c}$4={E}+1,{B}*({F}*({I('J', ir)}+{I('L', ir)})+(1-{F})*({I('I', ir)}+{I('K', ir)}))"
                                       f"*(1+ExpenseGrowth)^{E},0)", USD, Y)
                pot += [r, r + 1]
                vac.append(r + 2)
                occ.append(r + 3)
                rec.append(r + 4)
                tilc.append(r + 5)
                r += 7
            for k, v in enumerate(d["vacant_suites"]):
                ir = self.r["vac"] + k
                B, C, L, H = I("B", ir), I("C", ir), I("D", ir), I("H", ir)
                S.section(r, v["name"])
                r += 1
                S.yrow(r, "Potential rent at market",
                       lambda t, c, p: f"=IF({c}$4<{L},{C}*{B}*(1+RentGrowth)^({c}$4-1),"
                                       f"{C}*{B}*(1+RentGrowth)^({L}-1)*(1+{I('E', ir)})^({c}$4-{L}))", USD, Y)
                S.yrow(r + 1, "Lease-up vacancy", lambda t, c, p: f"=-IF({c}$4<{L},{C}*{B}*(1+RentGrowth)^({c}$4-1),0)", USD, Y)
                S.yrow(r + 2, "Occupied SF", lambda t, c, p: f"=IF({c}$4>={L},{B},0)", NUM, Y)
                S.yrow(r + 3, "Recoveries", lambda t, c, p: f"={H}*(1+ExpenseGrowth)^({c}$4-1)*{c}{r + 2}", USD, Y)
                S.yrow(r + 4, "TI and leasing commissions",
                       lambda t, c, p: f"=IF({c}$4={L},{B}*({I('F', ir)}+{I('G', ir)})*(1+ExpenseGrowth)^({L}-1),0)", USD, Y)
                pot.append(r)
                vac.append(r + 1)
                occ.append(r + 2)
                rec.append(r + 3)
                tilc.append(r + 4)
                r += 6
            S.section(r, "Property revenue")
            r += 1
            sm = lambda rows: (lambda t, c, p: "=" + "+".join(f"{c}{x}" for x in rows))
            S.yrow(r, "Potential base rent", sm(pot), USD, Y)
            S.yrow(r + 1, "Downtime and lease-up vacancy", sm(vac), USD, Y)
            S.yrow(r + 2, "Base rent", lambda t, c, p: f"={c}{r}+{c}{r + 1}", USD, Y)
            S.yrow(r + 3, "Expense recoveries", sm(rec), USD, Y)
            S.yrow(r + 4, "Gross revenue", lambda t, c, p: f"={c}{r + 2}+{c}{r + 3}", USD, Y)
            S.yrow(r + 5, "General vacancy and credit loss", lambda t, c, p: f"=-{c}{r + 4}*Vacancy", USD, Y)
            S.yrow(r + 6, "Other income", lambda t, c, p: f"=OtherIncome*{gf(c)}", USD, Y)
            self.r["egi"] = S.yrow(r + 7, "Effective gross income", lambda t, c, p: f"={c}{r + 4}+{c}{r + 5}+{c}{r + 6}", USD, Y, True)
            S.yrow(r + 8, "Occupied SF", sm(occ), NUM, Y)
            sfs = [f"Inputs!$B${self.r['ten'] + k}" for k in range(len(d["tenants"]))]
            sfs += [f"Inputs!$B${self.r['vac'] + k}" for k in range(len(d["vacant_suites"]))]
            S.label(r + 9, "Total rentable SF")
            S.put(f"C{r + 9}", "=" + "+".join(sfs), NUM)
            self.r["occ"] = S.yrow(r + 10, "Occupancy (after general vacancy)",
                                   lambda t, c, p: f"={c}{r + 8}/$C${r + 9}*(1-Vacancy)", PCT1, Y)
            self.r["engcap"] = S.yrow(r + 11, "TI and leasing commissions (to CashFlow)", sm(tilc), USD, Y)
            self.r["engopex"] = None
        else:
            oc = self.r["occ_in"]
            self.r["occ"] = S.yrow(r, "Occupancy", lambda t, c, p: f"=MIN(1,MAX(0,Inputs!{c}{oc}+OccAdj))", PCT1, Y)
            S.yrow(r + 1, "Rate per occupied unit", lambda t, c, p: f"=RateY1*{gf(c)}", PSF, Y)
            S.yrow(r + 2, "Revenue per available unit", lambda t, c, p: f"={c}{r}*{c}{r + 1}", PSF, Y)
            S.yrow(r + 3, "Unit revenue", lambda t, c, p: f"=Keys*{c}{r}*{c}{r + 1}*RatePeriods", USD, Y)
            S.yrow(r + 4, "Other revenue", lambda t, c, p: f"={c}{r + 3}*OtherRevPct", USD, Y)
            self.r["egi"] = S.yrow(r + 5, "Total revenue", lambda t, c, p: f"={c}{r + 3}+{c}{r + 4}", USD, Y, True)
            S.yrow(r + 6, "Departmental expenses", lambda t, c, p: f"={c}{r + 5}*DeptPct", USD, Y)
            S.yrow(r + 7, "Undistributed expenses", lambda t, c, p: f"={c}{r + 5}*UndistPct", USD, Y)
            self.r["dept"], self.r["undist"] = r + 6, r + 7
            S.yrow(r + 8, "Gross operating profit", lambda t, c, p: f"={c}{r + 5}-{c}{r + 6}-{c}{r + 7}", USD, Y)
            S.yrow(r + 9, "GOP margin", lambda t, c, p: f"=IF({c}{r + 5}=0,0,{c}{r + 8}/{c}{r + 5})", PCT1, Y)
            self.r["ffe"] = S.yrow(r + 10, "FF&E reserve (to CashFlow)", lambda t, c, p: f"={c}{r + 5}*FFEPct", USD, Y)
            self.r["engcap"] = None

    # -------------------------------------------------------------- cash flow
    def build_cashflow(self):
        d, S = self.d, self.s["CashFlow"]
        S.title("CashFlow", "Annual operating cash flow through NOI and cash flow before debt.")
        S.year_header()
        Y = range(1, 12)
        r = 8
        egi = S.yrow(r, "Effective gross income", lambda t, c, p: f"=Revenue!{c}{self.r['egi']}", USD, Y, True)
        r += 2
        S.section(r, "Operating expenses")
        r += 1
        first = r
        if d["engine"] == "operating":
            S.yrow(r, "Departmental expenses", lambda t, c, p: f"=Revenue!{c}{self.r['dept']}", USD, Y)
            S.yrow(r + 1, "Undistributed expenses", lambda t, c, p: f"=Revenue!{c}{self.r['undist']}", USD, Y)
            r += 2
        for k, it in enumerate(d["expense_items"]):
            ir = self.r["exp"] + k
            S.yrow(r, it["name"], lambda t, c, p: f"=Inputs!$B${ir}*(1+IF(Inputs!$C${ir}=\"\",ExpenseGrowth,Inputs!$C${ir}))^({c}$4-1)", USD, Y)
            r += 1
        S.yrow(r, "Management fee", lambda t, c, p: f"={c}{egi}*MgmtFeePct", USD, Y)
        tax = S.yrow(r + 1, "Property tax",
                     lambda t, c, p: f"=IF(TaxReassess=1,PurchasePrice*AssessRatio*TaxRate,CurrentTax)*(1+ExpenseGrowth)^({c}$4-1)", USD, Y)
        S.yrow(r + 2, "Insurance", lambda t, c, p: f"=Insurance*(1+ExpenseGrowth)^({c}$4-1)", USD, Y)
        opex = S.yrow(r + 3, "Total operating expenses", lambda t, c, p: f"=SUM({c}{first}:{c}{r + 2})", USD, Y, True)
        r += 5
        noi = S.yrow(r, "Net operating income", lambda t, c, p: "=TrailingNOI" if t == 0 else f"={c}{egi}-{c}{opex}", USD, YR, True)
        S.yrow(r + 1, "NOI margin", lambda t, c, p: f"=IF({c}{egi}=0,0,{c}{noi}/{c}{egi})", PCT1, Y)
        r += 3
        if d["engine"] == "operating":
            res = S.yrow(r, "FF&E reserve", lambda t, c, p: f"=Revenue!{c}{self.r['ffe']}", USD, Y)
        else:
            res = S.yrow(r, "Replacement reserves", lambda t, c, p: f"=Reserves*(1+ExpenseGrowth)^({c}$4-1)", USD, Y)
        cpx = S.yrow(r + 1, "Capital expenditure schedule", lambda t, c, p: f"=Inputs!{c}{self.r['capex_in']}", USD, Y)
        if self.r["engcap"]:
            lbl = "Renovation capital" if d["engine"] == "unit" else "TI and leasing commissions"
            eng = S.yrow(r + 2, lbl, lambda t, c, p: f"=Revenue!{c}{self.r['engcap']}", USD, Y)
        else:
            eng = S.yrow(r + 2, "Engine capital (none for this engine)", lambda t, c, p: "=0", USD, Y)
        cfbd = S.yrow(r + 3, "Cash flow before debt", lambda t, c, p: f"={c}{noi}-{c}{res}-{c}{cpx}-{c}{eng}", USD, Y, True)
        r += 5
        S.section(r, "Memo")
        S.yrow(r + 1, "Occupancy", lambda t, c, p: f"=Revenue!{c}{self.r['occ']}", PCT1, Y)
        tpd = S.yrow(r + 2, "Property tax per dollar of price (sensitivity)",
                     lambda t, c, p: f"=IF(TaxReassess=1,{c}{tax}/PurchasePrice,0)", "0.00000", Y)
        self.r.update(cf_noi=noi, cf_res=res, cf_capex=cpx, cf_eng=eng, cf_cfbd=cfbd, cf_occ=r + 1, cf_tpd=tpd, cf_egi=egi)
        self.name_range("out_NOI", "CashFlow", "C", "N", noi)

    # -------------------------------------------------------------- debt
    def build_debt(self):
        S = self.s["Debt"]
        R = self.r
        S.title("Debt", "Loan sized to the lowest of LTV, DSCR and debt yield, or a stated amount.")
        S.year_header()
        r = 8
        S.section(r, "Loan sizing")
        rows = [
            ("Lender NOI, Year 1 (after reserves)", f"=CashFlow!D{R['cf_noi']}-CashFlow!D{R['cf_res']}", USD),
            ("Loan constant (amortizing payment basis)", "=IF(AmortYears>0,PMT(LoanRate,AmortYears,-1),LoanRate)", "0.0000%"),
            ("LTV test", "=PurchasePrice*MaxLTV", USD),
            ("DSCR test", f"=C{r + 1}/(MinDSCR*C{r + 2})", USD),
            ("Debt yield test", f"=C{r + 1}/MinDY", USD),
            ("Maximum loan (lowest test)", f"=MIN(C{r + 3}:C{r + 5})", USD),
            ("Binding test", f'=IF(DebtMode="Stated","Stated amount",IF(C{r + 3}=C{r + 6},"LTV",IF(C{r + 4}=C{r + 6},"DSCR","Debt yield")))', None),
            ("Loan amount", f'=IF(DebtMode="Stated",StatedLoan,C{r + 6})', USD),
            ("Loan fee", f"=C{r + 8}*LoanFeePct", USD),
            ("Annual amortizing payment", f"=IF(AmortYears>0,PMT(LoanRate,AmortYears,-C{r + 8}),0)", USD),
        ]
        for i, (lbl, f, fmt) in enumerate(rows, start=1):
            S.label(r + i, lbl)
            S.put(f"C{r + i}", f, fmt, bold=(lbl == "Loan amount"))
        R.update(d_size=r + 6, d_bind=r + 7, d_loan=r + 8, d_fee=r + 9, d_pay=r + 10, d_lnoi=r + 1)
        self.name("out_LoanAmount", "Debt", f"C{r + 8}")
        self.name("out_Binding", "Debt", f"C{r + 7}")
        r += 13
        S.section(r, "Balance roll")
        r += 1
        o, dr, it, pr, po, cl, ds = range(r, r + 7)
        S.yrow(o, "Opening balance", lambda t, c, p: "=0" if t == 0 else f"={p}{cl}")
        S.yrow(dr, "Loan funding", lambda t, c, p: f"=$C${R['d_loan']}" if t == 0 else "=0")
        S.yrow(it, "Interest", lambda t, c, p: "=0" if t == 0 else f"={c}{o}*LoanRate*{c}$5")
        S.yrow(pr, "Scheduled principal",
               lambda t, c, p: "=0" if t == 0 else f"=IF(AND({c}$4>IOYears,AmortYears>0),MIN({c}{o},$C${R['d_pay']}-{c}{o}*LoanRate),0)*{c}$5")
        S.yrow(po, "Payoff at sale", lambda t, c, p: "=0" if t == 0 else f"=IF({c}$4=Hold,{c}{o}-{c}{pr},0)")
        S.yrow(cl, "Closing balance", lambda t, c, p: f"={c}{o}+{c}{dr}-{c}{pr}-{c}{po}", USD, YR, True)
        S.yrow(ds, "Debt service", lambda t, c, p: f"={c}{it}+{c}{pr}", USD, YR, True)
        R.update(d_open=o, d_draw=dr, d_prin=pr, d_payoff=po, d_close=cl, d_ds=ds)
        self.name_range("out_DebtService", "Debt", "C", "N", ds)
        r = ds + 2
        S.section(r, "Credit metrics")
        S.yrow(r + 1, "DSCR (NOI / debt service)",
               lambda t, c, p: f"=IF({c}{ds}=0,0,CashFlow!{c}{R['cf_noi']}/{c}{ds})", MULT, range(1, 12))
        S.yrow(r + 2, "Debt yield (NOI / opening balance)",
               lambda t, c, p: f"=IF({c}{o}=0,0,CashFlow!{c}{R['cf_noi']}/{c}{o})", PCT2, range(1, 12))
        S.label(r + 3, "LTV at close")
        S.put(f"C{r + 3}", f"=C{R['d_loan']}/PurchasePrice", PCT1)
        R["d_dscr"] = r + 1

    # -------------------------------------------------------------- returns
    def build_returns(self):
        S, R = self.s["Returns"], self.r
        S.title("Returns", "Annual year-end cash flows. IRR uses Excel IRR on years 0 to 11.")
        S.year_header()
        r = 8
        S.section(r, "Sources and uses")
        su = [("Purchase price", "=PurchasePrice"), ("Closing costs", "=PurchasePrice*ClosingPct"),
              ("Upfront capital", "=UpfrontCapex"), ("Loan fee", f"=Debt!C{R['d_fee']}"),
              ("Total uses", f"=SUM(C{r + 1}:C{r + 4})"), ("Loan", f"=Debt!C{R['d_loan']}"),
              ("Equity", f"=C{r + 5}-C{r + 6}"), ("Total sources", f"=C{r + 6}+C{r + 7}")]
        for i, (lbl, f) in enumerate(su, start=1):
            S.label(r + i, lbl, bold=lbl.startswith("Total"))
            S.put(f"C{r + i}", f, USD, bold=lbl.startswith("Total"))
        R.update(rt_close=r + 2, rt_uses=r + 5, rt_loan=r + 6, rt_eq=r + 7, rt_src=r + 8)
        r += 10
        S.section(r, "Sale")
        sale = [("Exit-year NOI (year after sale)", f"=INDEX(CashFlow!D{R['cf_noi']}:N{R['cf_noi']},Hold+1)", USD),
                ("Exit cap rate", "=ExitCap", PCT2),
                ("Exit value", f"=C{r + 1}/C{r + 2}", USD),
                ("Sale costs", f"=C{r + 3}*SaleCostPct", USD),
                ("Net sale before debt", f"=C{r + 3}-C{r + 4}", USD),
                ("Loan payoff", f"=SUM(Debt!C{R['d_payoff']}:N{R['d_payoff']})", USD),
                ("Net sale proceeds to equity", f"=C{r + 5}-C{r + 6}", USD)]
        for i, (lbl, f, fmt) in enumerate(sale, start=1):
            S.label(r + i, lbl)
            S.put(f"C{r + i}", f, fmt)
        R.update(rt_xnoi=r + 1, rt_xval=r + 3, rt_nsu=r + 5, rt_nsl=r + 7)
        self.name("out_ExitValue", "Returns", f"C{r + 3}")
        r += 9
        S.section(r, "Cash flows")
        Y = range(1, 12)
        cf = S.yrow(r + 1, "Cash flow before debt (in hold)", lambda t, c, p: f"=CashFlow!{c}{R['cf_cfbd']}*{c}$5", USD, Y)
        ds = S.yrow(r + 2, "Debt service", lambda t, c, p: f"=Debt!{c}{R['d_ds']}", USD, Y)
        un = S.yrow(r + 3, "Unlevered cash flow",
                    lambda t, c, p: f"=-(PurchasePrice+$C${R['rt_close']}+UpfrontCapex)" if t == 0
                    else f"={c}{cf}+{c}$6*$C${R['rt_nsu']}", USD, YR, True)
        lv = S.yrow(r + 4, "Levered cash flow",
                    lambda t, c, p: f"=-$C${R['rt_eq']}" if t == 0
                    else f"={c}{cf}-{c}{ds}+{c}$6*$C${R['rt_nsl']}", USD, YR, True)
        coc = S.yrow(r + 5, "Cash on cash", lambda t, c, p: f"=IF({c}$5=1,({c}{cf}-{c}{ds})/$C${R['rt_eq']},0)", PCT1, Y)
        R.update(rt_cf=cf, rt_un=un, rt_lv=lv)
        r += 7
        S.section(r, "Return metrics")
        rng = lambda x: f"C{x}:N{x}"
        noi = R["cf_noi"]
        cap_hold = (f"SUMPRODUCT(CashFlow!D{R['cf_capex']}:N{R['cf_capex']},D$5:N$5)"
                    f"+SUMPRODUCT(CashFlow!D{R['cf_eng']}:N{R['cf_eng']},D$5:N$5)")
        m = [("Unlevered IRR", f"=IRR({rng(un)})", PCT2, "out_UnlevIRR"),
             ("Levered IRR", f"=IRR({rng(lv)})", PCT2, "out_LevIRR"),
             ("Unlevered multiple", f'=SUMIF({rng(un)},">0")/-SUMIF({rng(un)},"<0")', MULT, None),
             ("Equity multiple", f'=SUMIF({rng(lv)},">0")/-SUMIF({rng(lv)},"<0")', MULT, "out_EM"),
             ("Unlevered profit", f"=SUM({rng(un)})", USD, None),
             ("Levered profit", f"=SUM({rng(lv)})", USD, None),
             ("Going-in cap rate (Year 1 NOI / price)", f"=CashFlow!D{noi}/PurchasePrice", PCT2, None),
             ("In-place cap rate (trailing NOI / price)", "=TrailingNOI/PurchasePrice", PCT2, None),
             ("Cash on cash, Year 1", f"=D{coc}", PCT1, "out_CoC1"),
             ("Average cash on cash over hold", f"=SUM(D{coc}:N{coc})/Hold", PCT1, None),
             ("Total project cost (price, closing, capital in hold)",
              f"=PurchasePrice+$C${R['rt_close']}+UpfrontCapex+{cap_hold}", USD, None),
             ("Yield on cost (final hold-year NOI / total cost)", f"=INDEX(CashFlow!D{noi}:N{noi},Hold)/C{r + 11}", PCT2, None),
             ("Price per unit or SF", "=PurchasePrice/" + self.size_ref(), USD, None)]
        for i, (lbl, f, fmt, nm) in enumerate(m, start=1):
            S.label(r + i, lbl)
            S.put(f"C{r + i}", f, fmt, bold=nm in ("out_LevIRR", "out_EM"))
            if nm:
                self.name(nm, "Returns", f"C{r + i}")
        R.update(rt_unirr=r + 1, rt_lvirr=r + 2, rt_em=r + 4, rt_uprof=r + 5, rt_lprof=r + 6, rt_gic=r + 7,
                 rt_coc1=r + 9, rt_yoc=r + 12, rt_ppu=r + 13)
        r += 15
        S.section(r, "Returns attribution (levered profit)")
        a = [("NOI growth (valued at going-in cap)", f"=($C${R['rt_xnoi']}-CashFlow!D{noi})/$C${R['rt_gic']}"),
             ("Cap rate movement", f"=$C${R['rt_xnoi']}/ExitCap-$C${R['rt_xnoi']}/$C${R['rt_gic']}"),
             ("Cash flow during hold", f"=SUM(D{cf}:N{cf})"),
             ("Transaction costs and upfront capital", f"=$C${R['rt_uprof']}-SUM(C{r + 1}:C{r + 3})"),
             ("Leverage and amortization", f"=$C${R['rt_lprof']}-$C${R['rt_uprof']}"),
             ("Total levered profit", f"=SUM(C{r + 1}:C{r + 5})")]
        for i, (lbl, f) in enumerate(a, start=1):
            S.label(r + i, lbl, bold=lbl.startswith("Total"))
            S.put(f"C{r + i}", f, USD)
        S.label(r + 7, "Cap rate flag")
        S.put(f"C{r + 7}", f'=IF(AND($C${R["rt_lprof"]}>0,2*C{r + 2}>$C${R["rt_lprof"]}),'
                           f'"Flag: cap rate movement supplies most of the profit","OK")')
        R.update(rt_att_total=r + 6, rt_capflag=r + 7)

    def size_ref(self):
        d = self.d
        if d["engine"] == "unit":
            return f"SUM(Inputs!B{self.r['mix']}:B{self.r['mix'] + len(d['unit_mix']) - 1})"
        if d["engine"] == "lease":
            return "Revenue!C" + str(self.r["occ"] - 1)
        return "Keys"

    # -------------------------------------------------------------- waterfall
    def build_waterfall(self):
        d, S, R = self.d, self.s["Waterfall"], self.r
        S.title("Waterfall", "Annual. Hurdles measured on investor IRR with hurdle balance accounts. "
                             "Pref compounds annually on unreturned capital.")
        S.year_header()
        Y = range(1, 12)
        r = 8
        lev = S.yrow(r, "Levered cash flow (property level)", lambda t, c, p: f"=Returns!{c}{R['rt_lv']}", USD, YR)
        acq = S.yrow(r + 1, "Acquisition fee (funded at close)", lambda t, c, p: "=AcqFeePct*PurchasePrice" if t == 0 else "=0")
        am = S.yrow(r + 2, "Asset management fee", lambda t, c, p: "=0" if t == 0 else f"={c}$5*AMFeePct*Returns!$C${R['rt_eq']}")
        dsp = S.yrow(r + 3, "Disposition fee", lambda t, c, p: "=0" if t == 0 else f"={c}$6*DispFeePct*Returns!$C${R['rt_xval']}")
        cash = S.yrow(r + 4, "Cash after fees", lambda t, c, p: f"={c}{lev}-{c}{acq}-{c}{am}-{c}{dsp}", USD, YR, True)
        con = S.yrow(r + 5, "Equity contributions", lambda t, c, p: f"=-{c}{cash}" if t == 0 else f"=MAX(0,-{c}{cash})")
        dist = S.yrow(r + 6, "Cash available for distribution", lambda t, c, p: "=0" if t == 0 else f"=MAX(0,{c}{cash})", USD, YR, True)
        ic = S.yrow(r + 7, "Investor contributions", lambda t, c, p: f"={c}{con}*InvShare")
        sc = S.yrow(r + 8, "Sponsor co-invest contributions", lambda t, c, p: f"={c}{con}*(1-InvShare)")
        r += 10
        n = len(d["tiers"])
        rates = ["PrefRate"] + [f"Hurdle{k}" for k in range(1, n + 1)]
        promos = ["0"] + [f"Promote{k}" for k in range(1, n + 1)]
        # hurdle accounts: start rows; end rows filled after investor total is known
        pre, end = [], []
        S.section(r, "Hurdle accounts (investor)")
        r += 1
        for k in range(n + 1):
            lbl = "Pref account (capital plus pref)" if k == 0 else f"Hurdle {k} account"
            pre.append(r)
            end.append(r + 1)
            r += 2
        r += 1
        S.section(r, "Distribution bands")
        r += 1
        X, INV, PRO = [], [], []
        for k in range(n + 1):
            share = "InvShare" if k == 0 else f"(InvShare*(1-{promos[k]}))"
            lbl = "Band 0: pref and return of capital (pro rata)" if k == 0 else \
                f"Band {k}: to hurdle {k} (promote {promos[k]})"
            prior_x = "".join(f"-{{c}}{x}" for x in X)
            prior_i = "".join(f"-{{c}}{x}" for x in INV)
            if k == 0:
                fx = lambda t, c, p, pr=pre[0]: f"=MIN({c}{dist},{c}{pr}/InvShare)"
            else:
                fx = (lambda t, c, p, pr=pre[k], px=prior_x, pi=prior_i, sh=share:
                      f"=MAX(0,MIN({c}{dist}{px.format(c=c)},MAX(0,{c}{pr}{pi.format(c=c)})/{sh}))")
            S.yrow(r, lbl, fx)
            if k == 0:
                S.put(f"A{r}", '="Band 0: pref at "&TEXT(PrefRate,"0.00%")&" and return of capital (pro rata)"')
            else:
                S.put(f"A{r}", f'="Band {k}: to hurdle {k} at "&TEXT(Hurdle{k},"0.00%")&", promote "&TEXT(Promote{k},"0.0%")')
            S.yrow(r + 1, "  to investor", lambda t, c, p, x=r, sh=share: f"={c}{x}*{sh}")
            S.yrow(r + 2, "  promote to sponsor", lambda t, c, p, x=r, pm=promos[k]: f"={c}{x}*{pm}")
            X.append(r)
            INV.append(r + 1)
            PRO.append(r + 2)
            r += 3
        S.yrow(r, f"Final band: above last hurdle (promote FinalPromote)",
               lambda t, c, p: f"={c}{dist}" + "".join(f"-{c}{x}" for x in X))
        S.put(f"A{r}", '="Final band: above last hurdle, promote "&TEXT(FinalPromote,"0.0%")')
        S.yrow(r + 1, "  to investor", lambda t, c, p, x=r: f"={c}{x}*(1-FinalPromote)*InvShare")
        S.yrow(r + 2, "  promote to sponsor", lambda t, c, p, x=r: f"={c}{x}*FinalPromote")
        INV.append(r + 1)
        PRO.append(r + 2)
        r += 4
        inv = S.yrow(r, "Total to investor", lambda t, c, p: "=" + "+".join(f"{c}{x}" for x in INV), USD, YR, True)
        spo = S.yrow(r + 1, "Total to sponsor (co-invest share and promote)", lambda t, c, p: f"={c}{dist}-{c}{inv}", USD, YR, True)
        prm = S.yrow(r + 2, "  of which promote", lambda t, c, p: "=" + "+".join(f"{c}{x}" for x in PRO))
        tot = S.yrow(r + 3, "Total distributed", lambda t, c, p: f"={c}{inv}+{c}{spo}")
        chk = S.yrow(r + 4, "Difference from cash available", lambda t, c, p: f"={c}{tot}-{c}{dist}")
        # now the hurdle account rows
        for k in range(n + 1):
            S.put(f"A{pre[k]}", ('="Pref account at "&TEXT(PrefRate,"0.00%")' if k == 0 else
                                 f'="Hurdle {k} account at "&TEXT(Hurdle{k},"0.00%")') + '&": start of year plus accrual"')
            S.label(end[k], "  end of year balance")
            for t in YR:
                c = ycol(t)
                f = f"={c}{ic}" if t == 0 else f"=({ycol(t - 1)}{end[k]}*(1+{rates[k]})+{c}{ic})*({c}$4<=Hold)"
                S.put(f"{c}{pre[k]}", f, USD)
                S.put(f"{c}{end[k]}", f"=MAX(0,{c}{pre[k]}-{c}{inv})*({c}$4<=Hold)", USD)
        r += 6
        S.section(r, "Investor capital account (band 0 split: pref first, then capital)")
        due, pp, cr, uc, pb, cc, cum, ex = range(r + 1, r + 9)
        S.yrow(due, "Pref due", lambda t, c, p: "=0" if t == 0 else f"=({p}{pb}+({p}{uc}+{p}{pb})*PrefRate)*({c}$4<=Hold)")
        S.yrow(pp, "Pref paid", lambda t, c, p: f"=MIN({c}{INV[0]},{c}{due})")
        S.yrow(cr, "Capital returned", lambda t, c, p: f"={c}{INV[0]}-{c}{pp}")
        S.yrow(uc, "Unreturned capital, end of year", lambda t, c, p: (f"={c}{ic}-{c}{cr}" if t == 0 else f"={p}{uc}+{c}{ic}-{c}{cr}"))
        S.yrow(pb, "Accrued unpaid pref, end of year", lambda t, c, p: f"={c}{due}-{c}{pp}")
        S.yrow(cc, "Cumulative investor contributions", lambda t, c, p: f"={c}{ic}" if t == 0 else f"={p}{cc}+{c}{ic}")
        S.yrow(cum, "Cumulative capital returned", lambda t, c, p: f"={c}{cr}" if t == 0 else f"={p}{cum}+{c}{cr}")
        S.yrow(ex, "Capital returned in excess of contributed", lambda t, c, p: f"=MAX(0,{c}{cum}-{c}{cc})")
        r = ex + 2
        S.section(r, "Investor and sponsor returns")
        ncf = S.yrow(r + 1, "Investor net cash flow", lambda t, c, p: f"={c}{inv}-{c}{ic}", USD, YR, True)
        gcf = S.yrow(r + 2, "Investor gross cash flow (pro rata, before fees and promote)", lambda t, c, p: f"={c}{lev}*InvShare")
        scf = S.yrow(r + 3, "Sponsor net cash flow (co-invest and promote)", lambda t, c, p: f"={c}{spo}-{c}{sc}")
        r += 5
        rng = lambda x: f"C{x}:N{x}"
        m = [("Investor gross IRR", f"=IRR({rng(gcf)})", PCT2, None),
             ("Investor gross multiple", f'=SUMIF({rng(gcf)},">0")/-SUMIF({rng(gcf)},"<0")', MULT, None),
             ("Investor net IRR", f"=IRR({rng(ncf)})", PCT2, "out_InvNetIRR"),
             ("Investor net multiple", f"=SUM({rng(inv)})/SUM({rng(ic)})", MULT, "out_InvNetEM"),
             ("Gross to net IRR spread", f"=C{r + 1}-C{r + 3}", PCT2, None),
             ("Sponsor promote, total", f"=SUM({rng(prm)})", USD, "out_Promote"),
             ("Sponsor fees, total", f"=SUM({rng(acq)})+SUM({rng(am)})+SUM({rng(dsp)})", USD, None),
             ("Sponsor co-invest profit and promote", f"=SUM({rng(scf)})", USD, None),
             ("Sponsor total economics (fees, promote, co-invest profit)", f"=C{r + 7}+C{r + 8}", USD, None)]
        for i, (lbl, f, fmt, nm) in enumerate(m, start=1):
            S.label(r + i, lbl)
            S.put(f"C{r + i}", f, fmt, bold=bool(nm))
            if nm:
                self.name(nm, "Waterfall", f"C{r + i}")
        R.update(w_chk=chk, w_ex=ex, w_dist=dist, w_tot=tot, w_netirr=r + 3, w_netem=r + 4, w_prom=r + 6,
                 w_fees=r + 7, w_gross=r + 1, w_con=con)

    # -------------------------------------------------------------- sensitivity
    def build_sensitivity(self):
        S, R = self.s["Sensitivity"], self.r
        ws = S.ws
        S.title("Sensitivity", "Live scenario rows, no data tables. Levered cash flows are linear in each driver, "
                               "so each row adjusts the base row by formula.")
        # columns: A label, B exit cap, C NOI factor, D price change, E rate change, F IRR, G..R years 0..11
        Ycol = lambda t: CL(7 + t)
        S.year_header(row=4, col0=7)
        r = 8
        S.label(r, "Base levered cash flow")
        S.label(r + 1, "NOI")
        S.label(r + 2, "Property tax per dollar of price")
        S.label(r + 3, "Opening loan balance")
        for t in YR:
            c, rc = Ycol(t), ycol(t)
            S.put(f"{c}{r}", f"=Returns!{rc}{R['rt_lv']}", USD)
            S.put(f"{c}{r + 1}", f"=CashFlow!{rc}{R['cf_noi']}" if t else "=0", USD)
            S.put(f"{c}{r + 2}", f"=CashFlow!{rc}{R['cf_tpd']}" if t else "=0", "0.00000")
            S.put(f"{c}{r + 3}", f"=Debt!{rc}{R['d_open']}", USD)
        S.label(r + 5, "Exit-year NOI")
        S.put(f"B{r + 5}", f"=Returns!C{R['rt_xnoi']}", USD)
        S.label(r + 6, "Exit-year tax per dollar of price")
        S.put(f"B{r + 6}", f"=INDEX(CashFlow!D{R['cf_tpd']}:N{R['cf_tpd']},Hold+1)", "0.00000")
        xnoi, xtpd = f"$B${r + 5}", f"$B${r + 6}"
        S.label(r + 7, "Interest rate rows change interest on the base balance only. Exact for interest-only years; "
                       "for amortizing years principal is held at base, an approximation. Loan amount stays at base.")
        r += 9
        for i, h in enumerate(["Scenario", "Exit cap", "NOI vs plan", "Price change", "Rate change", "Levered IRR"]):
            S.label(r, h, col=CL(1 + i), bold=True, fill=HDR_FILL)
        for t in YR:
            S.label(r, f"Year {t}", col=Ycol(t), bold=True, fill=HDR_FILL)
        r += 1
        rows = []

        def off(k, name):
            """Grid offset k steps from base, written without stray literals."""
            return {-2: f"-2*{name}", -1: f"-{name}", 0: "", 1: f"+{name}", 2: f"+2*{name}"}[k]

        def scen(label, cap, f, dp, dr):
            nonlocal r
            S.label(r, label)
            S.put(f"B{r}", cap, PCT2)
            S.put(f"C{r}", f, PCT1)
            S.put(f"D{r}", dp, PCT1)
            S.put(f"E{r}", dr, PCT2)
            for t in YR:
                c = Ycol(t)
                if t == 0:
                    fx = f"={c}$8-$D{r}*PurchasePrice*(1+ClosingPct)"
                else:
                    fx = (f"={c}$8+{c}$5*(($C{r}-1)*{c}$9-$D{r}*PurchasePrice*{c}$10-$E{r}*{c}$11)"
                          f"+{c}$6*(1-SaleCostPct)*(($C{r}*{xnoi}-$D{r}*PurchasePrice*{xtpd})/$B{r}-{xnoi}/ExitCap)")
                S.put(f"{c}{r}", fx, USD)
            S.put(f"F{r}", f"=IFERROR(IRR({Ycol(0)}{r}:{Ycol(11)}{r}),-1)", PCT2, bold=True)
            rows.append(r)
            r += 1
            return r - 1

        base = scen("Base (ties to Returns)", "=ExitCap", "=1", "=0", "=0")
        R["s_base"] = base
        self.name("out_SensBase", "Sensitivity", f"F{base}")
        g1 = [[scen(f"Grid 1 r{i + 1} c{j + 1}", f"=ExitCap{off(j - 2, 'CapStep')}", f"=1{off(i - 2, 'NOIStep')}", "=0", "=0")
               for j in range(5)] for i in range(5)]
        g2 = [[scen(f"Grid 2 r{i + 1} c{j + 1}", f"=ExitCap{off(j - 2, 'CapStep')}", "=1", f"=0{off(i - 2, 'PriceStep')}", "=0")
               for j in range(5)] for i in range(5)]
        rr = [scen(f"Rate r{i + 1}", "=ExitCap", "=1", "=0", f"=0{off(i - 2, 'RateStep')}") for i in range(5)]
        ld = []
        for i in range(9):   # each ladder step builds on the one before
            ld.append(scen(f"Ladder {i + 1}", "=ExitCap", "=1", "=LadderLow" if i == 0 else f"=D{ld[-1]}+LadderStep", "=0"))

        # ---- display grids to the right (columns T onward)
        gc = 20
        ws.column_dimensions[CL(gc)].width = 30

        def grid(top, title, rowlbl, rowfmt, cells, rowsrc):
            S.label(top, title, col=CL(gc), bold=True)
            S.label(top + 1, rowlbl + " \\ Exit cap", col=CL(gc), bold=True)
            for j in range(5):
                S.put(f"{CL(gc + 1 + j)}{top + 1}", f"=B{cells[0][j]}", PCT2, bold=True)
            for i in range(5):
                S.put(f"{CL(gc)}{top + 2 + i}", f"={rowsrc}{cells[i][0]}", rowfmt, bold=True)
                for j in range(5):
                    S.put(f"{CL(gc + 1 + j)}{top + 2 + i}", f"=F{cells[i][j]}", PCT2)
            return top + 8

        t = grid(4, "Levered IRR: exit cap x NOI versus plan", "NOI vs plan", PCT1, g1, "C")
        t = grid(t, "Levered IRR: exit cap x purchase price change", "Price change", PCT1, g2, "D")
        S.label(t, "Levered IRR by interest rate change", col=CL(gc), bold=True)
        for i, x in enumerate(rr):
            S.put(f"{CL(gc)}{t + 1 + i}", f"=E{x}", PCT2)
            S.put(f"{CL(gc + 1)}{t + 1 + i}", f"=F{x}", PCT2)
        t += 8
        # ---- price ladder and maximum bid
        S.label(t, "Price ladder and maximum bid", col=CL(gc), bold=True)
        for j, h in enumerate(["Price change", "Price", "Levered IRR", "Crossing value"]):
            S.label(t + 1, h, col=CL(gc + j), bold=True, fill=HDR_FILL)
        lr = []
        for i, x in enumerate(ld):
            rw = t + 2 + i
            S.put(f"{CL(gc)}{rw}", f"=D{x}", PCT1)
            S.put(f"{CL(gc + 1)}{rw}", f"=PurchasePrice*(1+D{x})", USD)
            S.put(f"{CL(gc + 2)}{rw}", f"=F{x}", PCT2)
            lr.append(rw)
        P, Q = CL(gc + 1), CL(gc + 2)
        for i in range(8):
            a, b = lr[i], lr[i + 1]
            S.put(f"{CL(gc + 3)}{a}", f"=IF(AND({Q}{a}>=HurdleIRR,{Q}{b}<HurdleIRR),"
                                      f"{P}{a}+(HurdleIRR-{Q}{a})/({Q}{b}-{Q}{a})*({P}{b}-{P}{a}),0)", USD)
        f0, f8 = lr[0], lr[-1]
        m = t + 12
        S.label(m, "Firm hurdle IRR", col=CL(gc))
        S.put(f"{P}{m}", "=HurdleIRR", PCT2)
        S.label(m + 1, "Maximum bid at hurdle", col=CL(gc), bold=True)
        S.put(f"{P}{m + 1}", f"=IF({Q}{f8}>=HurdleIRR,{P}{f8},IF({Q}{f0}<HurdleIRR,{P}{f0},"
                             f"SUM({CL(gc + 3)}{f0}:{CL(gc + 3)}{lr[7]})))", USD, bold=True)
        S.label(m + 2, "Maximum bid status", col=CL(gc))
        S.put(f"{P}{m + 2}", f'=IF({Q}{f8}>=HurdleIRR,"Hurdle met at top of ladder; bid may be higher",'
                             f'IF({Q}{f0}<HurdleIRR,"Hurdle not met at bottom of ladder","Interpolated within ladder"))')
        S.label(m + 3, "Maximum bid versus asking price", col=CL(gc))
        S.put(f"{P}{m + 3}", f"={P}{m + 1}/PurchasePrice-1", PCT1)
        self.name("out_MaxBid", "Sensitivity", f"{P}{m + 1}")
        R.update(s_maxbid=f"{P}{m + 1}", s_status=f"{P}{m + 2}", s_disc=f"{P}{m + 3}")

    # -------------------------------------------------------------- checks
    def build_checks(self):
        S, R = self.s["Checks"], self.r
        S.title("Checks", "Each check returns OK or ERROR. Tolerance: $1 on amounts.")
        S.ws.column_dimensions["B"].width = 18
        S.ws.column_dimensions["C"].width = 10
        S.label(3, "Master check", bold=True)
        for i, h in enumerate(["Check", "Value", "Status", "Passes when"]):
            S.label(5, h, col=CL(1 + i), bold=True, fill=HDR_FILL)
        S.ws.column_dimensions["D"].width = 60
        cf = lambda x: f"C{x}:N{x}"
        checks = [
            ("Sources and uses", f"=Returns!C{R['rt_src']}-Returns!C{R['rt_uses']}", "ABS", "Total sources equal total uses"),
            ("Loan balance roll",
             f"=SUMPRODUCT(ABS(Debt!{cf(R['d_open'])}+Debt!{cf(R['d_draw'])}-Debt!{cf(R['d_prin'])}"
             f"-Debt!{cf(R['d_payoff'])}-Debt!{cf(R['d_close'])}))", "ABS",
             "Opening plus draws minus principal and payoff equals closing, every year"),
            ("Loan repaid at sale", f"=INDEX(Debt!D{R['d_close']}:N{R['d_close']},Hold)", "ABS",
             "Balance is zero after the sale year"),
            ("Loan sizing", f"=MAX(0,Debt!C{R['d_loan']}-Debt!C{R['d_size']})", "ABS",
             "Loan amount does not exceed the binding test"),
            ("Distributions", f"=SUMPRODUCT(ABS(Waterfall!{cf(R['w_chk'])}))", "ABS",
             "Waterfall distributions equal cash available each year"),
            ("Capital accounts", f"=MAX(Waterfall!{cf(R['w_ex'])})", "ABS",
             "Capital returned never exceeds capital contributed"),
            ("NOI tie", f"=CashFlow!C{R['cf_noi']}-TrailingNOI", "ABS", "Year 0 NOI matches trailing NOI on Inputs"),
            ("Occupancy bounds", f"=IF(AND(MIN(CashFlow!D{R['cf_occ']}:N{R['cf_occ']})>=0,"
                                 f"MAX(CashFlow!D{R['cf_occ']}:N{R['cf_occ']})<=1),0,1)", "ABS",
             "Occupancy stays between 0 and 100 percent"),
            ("Scenario", "=IF(ISNUMBER(ScenIdx),0,1)", "ABS", "Scenario cell holds Base, Upside or Downside"),
            ("Sensitivity base ties", f"=ABS(Sensitivity!F{R['s_base']}-Returns!C{R['rt_lvirr']})", "RATE",
             "Base scenario row IRR equals the Returns levered IRR"),
            ("Attribution ties", f"=Returns!C{R['rt_att_total']}-Returns!C{R['rt_lprof']}", "ABS",
             "Attribution sums to levered profit"),
        ]
        r = 6
        for lbl, f, kind, note in checks:
            S.label(r, lbl)
            S.put(f"B{r}", f, "0.000000" if kind == "RATE" else '#,##0.00')
            tol = "CheckTolRate" if kind == "RATE" else "1"
            S.put(f"C{r}", f'=IF(ISERROR(B{r}),"ERROR",IF(ABS(B{r})<={tol},"OK","ERROR"))', bold=True)
            S.label(r, note, col="D")
            r += 1
        S.put("C3", f'=IF(COUNTIF(C6:C{r - 1},"ERROR")=0,"OK","ERROR")', bold=True)
        S.ws["C3"].fill = CHK_FILL
        self.name("out_Master", "Checks", "C3")

    # -------------------------------------------------------------- summary and sources
    def build_summary(self):
        S, R = self.s["Summary"], self.r
        S.title("Quick screening model", "Annual first-look model. Use a full model for bids, financing and committee.")
        S.ws.column_dimensions["B"].width = 22
        rows = [
            ("Deal", "=DealName", None), ("Property type", "=PropertyType", None), ("Engine", "=Engine", None),
            ("Scenario", "=Scenario", None), ("Hold (years)", "=Hold", "0"), ("Model check status", "=Checks!C3", None),
            None,
            ("Purchase price", "=PurchasePrice", USD), ("Price per unit or SF", f"=Returns!C{R['rt_ppu']}", USD),
            ("Year 1 NOI", f"=CashFlow!D{R['cf_noi']}", USD),
            ("In-place cap rate", "=TrailingNOI/PurchasePrice", PCT2),
            ("Going-in cap rate", f"=Returns!C{R['rt_gic']}", PCT2),
            ("Exit cap rate", "=ExitCap", PCT2), ("Exit value", f"=Returns!C{R['rt_xval']}", USD),
            None,
            ("Loan amount", f"=Debt!C{R['d_loan']}", USD), ("Binding sizing test", f"=Debt!C{R['d_bind']}", None),
            ("LTV at close", f"=Debt!C{R['d_loan']}/PurchasePrice", PCT1),
            ("DSCR, Year 1", f"=Debt!D{R['d_dscr']}", MULT),
            ("Equity required", f"=Returns!C{R['rt_eq']}", USD),
            ("Peak equity (including capital calls)", f"=SUM(Waterfall!C{R['w_con']}:N{R['w_con']})", USD),
            None,
            ("Unlevered IRR", f"=Returns!C{R['rt_unirr']}", PCT2), ("Levered IRR", f"=Returns!C{R['rt_lvirr']}", PCT2),
            ("Equity multiple", f"=Returns!C{R['rt_em']}", MULT), ("Cash on cash, Year 1", f"=Returns!C{R['rt_coc1']}", PCT1),
            ("Yield on cost", f"=Returns!C{R['rt_yoc']}", PCT2),
            ("Levered IRR versus hurdle", f'=IF(Returns!C{R["rt_lvirr"]}>=HurdleIRR,"Meets hurdle","Below hurdle")', None),
            ("Cap rate flag", f"=Returns!C{R['rt_capflag']}", None),
            None,
            ("Investor gross IRR", f"=Waterfall!C{R['w_gross']}", PCT2),
            ("Investor net IRR", f"=Waterfall!C{R['w_netirr']}", PCT2),
            ("Investor net multiple", f"=Waterfall!C{R['w_netem']}", MULT),
            ("Sponsor promote", f"=Waterfall!C{R['w_prom']}", USD),
            ("Sponsor fees", f"=Waterfall!C{R['w_fees']}", USD),
            None,
            ("Firm hurdle IRR", "=HurdleIRR", PCT2),
            ("Maximum bid at hurdle", f"=Sensitivity!{R['s_maxbid']}", USD),
            ("Maximum bid versus asking", f"=Sensitivity!{R['s_disc']}", PCT1),
            ("Maximum bid status", f"=Sensitivity!{R['s_status']}", None),
        ]
        r = 4
        for x in rows:
            if x is None:
                r += 1
                continue
            S.label(r, x[0])
            S.put(f"B{r}", x[1], x[2], bold=x[0] in ("Levered IRR", "Model check status", "Maximum bid at hurdle"))
            if x[0] == "Peak equity (including capital calls)":
                self.name("out_PeakEquity", "Summary", f"B{r}")
            if x[0] == "Cash on cash, Year 1":
                S.put(f"C{r}", f'=IF(B{r}<0,"Negative: Year 1 capital (renovation, capex, TI and LC) is paid from '
                               f'cash flow; any shortfall is funded by capital calls","")')
            if x[0] == "Model check status":
                S.ws[f"B{r}"].fill = CHK_FILL
            r += 1

    def build_sources(self):
        S = self.s["Sources"]
        S.title("Sources", "Documents and public sources used, with dates.")
        for i, h in enumerate(["Document or source", "Tag", "Date", "Note"]):
            S.label(4, h, col=CL(1 + i), bold=True, fill=HDR_FILL)
        S.ws.column_dimensions["D"].width = 40
        r = 5
        for src in self.d["sources"]:
            S.label(r, str(src.get("document", "")))
            S.label(r, str(src.get("type", "")), col="B")
            S.label(r, str(src.get("date", "")), col="C")
            S.label(r, str(src.get("note", "")), col="D")
            r += 1
        S.label(r + 1, CREDIT)

    def build(self, out):
        self.build_inputs()
        self.build_revenue()
        self.build_cashflow()
        self.build_debt()
        self.build_returns()
        self.build_waterfall()
        self.build_sensitivity()
        self.build_checks()
        self.build_summary()
        self.build_sources()
        for ws in self.wb.worksheets:
            ws.sheet_view.showGridLines = False
            for row in ws.iter_rows():
                for c in row:
                    if c.column == 1:
                        c.alignment = Alignment(wrap_text=False)
        self.wb.active = 0
        self.wb.calculation.fullCalcOnLoad = True
        self.wb.save(out)


def build(deal_path, out_path):
    d = load_deal(deal_path)
    Builder(d).build(out_path)
    return out_path


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python3 repe_model.py <deal.json> <out.xlsx>")
        sys.exit(2)
    build(sys.argv[1], sys.argv[2])
    print("Workbook written: " + sys.argv[2])
