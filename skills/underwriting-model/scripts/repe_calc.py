#!/usr/bin/env python3
"""Independent pure-Python recalculation of a deal JSON.

Mirrors the logic of the live-formula workbook built by repe_model.py so the
two can be compared by validate_model.py. Standard library only.

Usage: python3 repe_calc.py <deal.json>   (prints key outputs as JSON)
"""
import json
import sys

YEARS = 12          # model columns: year 0 .. year 11
SCENARIOS = ["Base", "Upside", "Downside"]


# ---------------------------------------------------------------- inputs

def _tri(v):
    """Scenario driver: a number or [base, upside, downside]."""
    if isinstance(v, (list, tuple)):
        if len(v) != 3:
            raise ValueError("scenario drivers need 3 values: base, upside, downside")
        return [float(x) for x in v]
    return [float(v)] * 3


def _vec(v, n=11, fill_last=False):
    """Year 1..11 vector; pads with zeros or the last value."""
    v = [float(x) for x in (v or [])][:n]
    pad = v[-1] if (fill_last and v) else 0.0
    return v + [pad] * (n - len(v))


def load_deal(path_or_dict):
    """Read and normalize a deal JSON. Shared by the builder and the calculator."""
    if isinstance(path_or_dict, dict):
        raw = path_or_dict
    else:
        with open(path_or_dict, "r", encoding="utf-8") as f:
            raw = json.load(f)
    d = {}
    d["deal_name"] = raw.get("deal_name", "Deal")
    d["property_type"] = raw.get("property_type", "")
    d["engine"] = raw["engine"]
    if d["engine"] not in ("unit", "lease", "operating"):
        raise ValueError("engine must be unit, lease or operating")
    d["scenario"] = raw.get("scenario", "Base")
    if d["scenario"] not in SCENARIOS:
        raise ValueError("scenario must be Base, Upside or Downside")
    d["hold"] = int(raw.get("hold_years", 5))
    if not 1 <= d["hold"] <= 10:
        raise ValueError("hold_years must be 1 to 10")

    a = raw["acquisition"]
    d["price"] = float(a["purchase_price"])
    d["closing_pct"] = float(a.get("closing_cost_pct", 0.0))
    d["upfront_capex"] = float(a.get("upfront_capex", 0.0))
    d["trailing_noi"] = float(a.get("trailing_noi", 0.0))

    s = raw["assumptions"]
    d["rent_growth"] = _tri(s.get("rent_growth", 0.03))
    d["expense_growth"] = _tri(s.get("expense_growth", 0.03))
    d["exit_cap"] = _tri(s["exit_cap"])
    if d["engine"] == "operating":
        d["vacancy"] = _tri(s.get("occupancy_adjustment", 0.0))
    else:
        d["vacancy"] = _tri(s.get("vacancy", 0.05))
    d["sale_cost_pct"] = float(s.get("sale_cost_pct", 0.02))

    eng = raw.get(d["engine"], {})
    if d["engine"] == "unit":
        d["unit_mix"] = [{
            "type": u.get("type", "Unit"), "count": float(u["count"]), "sf": float(u.get("sf", 0)),
            "in_place_rent": float(u["in_place_rent"]), "market_rent": float(u["market_rent"]),
            "renovation_premium": float(u.get("renovation_premium", 0)),
            "renovations_per_year": float(u.get("renovations_per_year", 0)),
            "renovation_cost_per_unit": float(u.get("renovation_cost_per_unit", 0)),
            "source": u.get("source", "[User]")} for u in eng["unit_mix"]]
        d["concessions_pct"] = float(eng.get("concessions_pct", 0))
        d["bad_debt_pct"] = float(eng.get("bad_debt_pct", 0))
        d["other_income"] = float(eng.get("other_income", 0))
        d["ltl_burnoff"] = float(eng.get("loss_to_lease_burnoff_years", 1))
    elif d["engine"] == "lease":
        d["tenants"] = [{
            "name": t.get("name", "Tenant"), "sf": float(t["sf"]), "rent_psf": float(t["rent_psf"]),
            "bump": float(t.get("annual_bump", 0)), "expiry": int(t["expiry_year"]),
            "renew_prob": float(t.get("renewal_probability", 0.6)),
            "downtime": min(12.0, float(t.get("downtime_months", 6))),
            "market_psf": float(t["market_rent_psf"]),
            "ti_new": float(t.get("ti_new_psf", 0)), "ti_ren": float(t.get("ti_renewal_psf", 0)),
            "lc_new": float(t.get("lc_new_psf", 0)), "lc_ren": float(t.get("lc_renewal_psf", 0)),
            "recovery_psf": float(t.get("recovery_psf", 0)), "source": t.get("source", "[User]")}
            for t in eng["tenants"]]
        d["vacant_suites"] = [{
            "name": v.get("name", "Vacant"), "sf": float(v["sf"]), "market_psf": float(v["market_rent_psf"]),
            "lease_up": max(1, int(v.get("lease_up_year", 1))), "bump": float(v.get("annual_bump", 0)),
            "ti_new": float(v.get("ti_new_psf", 0)), "lc_new": float(v.get("lc_new_psf", 0)),
            "recovery_psf": float(v.get("recovery_psf", 0)), "source": v.get("source", "[User]")}
            for v in eng.get("vacant_suites", [])]
        d["other_income"] = float(eng.get("other_income", 0))
    else:
        d["keys"] = float(eng["keys"])
        d["rate"] = float(eng["rate"])
        d["rate_periods"] = 365.0 if eng.get("rate_basis", "day") == "day" else 12.0
        d["occupancy"] = _vec(eng["occupancy"], fill_last=True)
        d["other_rev_pct"] = float(eng.get("other_revenue_pct", 0))
        d["dept_pct"] = float(eng.get("departmental_expense_pct", 0))
        d["undist_pct"] = float(eng.get("undistributed_expense_pct", 0))
        d["ffe_pct"] = float(eng.get("ffe_reserve_pct", 0.04))

    e = raw.get("expenses", {})
    d["expense_items"] = [{"name": i["name"], "amount": float(i["amount"]),
                           "growth": (None if i.get("growth") is None else float(i["growth"])),
                           "source": i.get("source", "[User]")} for i in e.get("items", [])]
    d["mgmt_fee_pct"] = float(e.get("management_fee_pct", 0.03))
    t = e.get("property_tax", {})
    d["tax_reassess"] = 1 if t.get("reassess", False) else 0
    d["current_tax"] = float(t.get("current_tax", 0))
    d["assess_ratio"] = float(t.get("assessment_ratio", 1.0))
    d["tax_rate"] = float(t.get("tax_rate", 0))
    d["insurance"] = float(e.get("insurance", 0))
    d["reserves"] = float(e.get("replacement_reserves", 0))
    d["capex"] = _vec(e.get("capex_schedule", []))

    b = raw.get("debt", {})
    d["debt_mode"] = "Stated" if b.get("mode", "sized") == "stated" else "Sized"
    d["stated_loan"] = float(b.get("stated_amount", 0))
    d["max_ltv"] = float(b.get("max_ltv", 0.65))
    d["min_dscr"] = float(b.get("min_dscr", 1.25))
    d["min_dy"] = float(b.get("min_debt_yield", 0.08))
    d["loan_rate"] = float(b.get("rate", 0.06))
    d["io_years"] = int(b.get("io_years", 0))
    d["amort_years"] = int(b.get("amort_years", 30))
    d["loan_fee_pct"] = float(b.get("loan_fee_pct", 0.01))

    w = raw.get("waterfall", {})
    d["inv_share"] = float(w.get("investor_share", 0.9))
    d["pref"] = float(w.get("pref_rate", 0.08))
    tiers = w.get("tiers", [])[:3]
    d["tiers"] = [(float(x["hurdle"]), float(x["promote"])) for x in tiers]
    d["final_promote"] = float(w.get("final_promote", 0.2))
    d["acq_fee_pct"] = float(w.get("acquisition_fee_pct", 0))
    d["am_fee_pct"] = float(w.get("asset_management_fee_pct", 0))
    d["disp_fee_pct"] = float(w.get("disposition_fee_pct", 0))

    d["hurdle_irr"] = float(raw.get("returns", {}).get("hurdle_irr", 0.15))
    sn = raw.get("sensitivity", {})
    d["cap_step"] = float(sn.get("exit_cap_step", 0.0025))
    d["noi_step"] = float(sn.get("noi_step", 0.05))
    d["price_step"] = float(sn.get("price_step", 0.05))
    d["rate_step"] = float(sn.get("rate_step", 0.005))
    d["ladder_low"] = float(sn.get("ladder_low", -0.15))
    d["ladder_step"] = float(sn.get("ladder_step", 0.025))
    d["source_tags"] = raw.get("source_tags", {})
    d["sources"] = raw.get("sources", [])
    d["sidx"] = SCENARIOS.index(d["scenario"])
    d["raw"] = raw
    return d


# ---------------------------------------------------------------- helpers

def irr(cfs):
    """IRR by bisection. Returns -1.0 when no sign change (as the workbook's IFERROR)."""
    def npv(r):
        return sum(c / (1 + r) ** i for i, c in enumerate(cfs))
    lo, hi = -0.99, 10.0
    flo, fhi = npv(lo), npv(hi)
    if flo * fhi > 0:
        return -1.0
    for _ in range(300):
        mid = (lo + hi) / 2
        fm = npv(mid)
        if flo * fm <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def pmt(rate, n, pv):
    if n <= 0:
        return 0.0
    if rate == 0:
        return pv / n
    return pv * rate / (1 - (1 + rate) ** -n)


def multiple(cfs):
    pos = sum(c for c in cfs if c > 0)
    neg = -sum(c for c in cfs if c < 0)
    return pos / neg if neg else 0.0


# ---------------------------------------------------------------- engines

def revenue(d):
    """Returns dict of year arrays (index 0..11). Year 0 revenue is zero."""
    k = d["sidx"]
    g, eg, vac = d["rent_growth"][k], d["expense_growth"][k], d["vacancy"][k]
    z = lambda: [0.0] * YEARS
    r = {"egi": z(), "opex_engine": z(), "reserves": z(), "capital": z(), "occupancy": z()}
    if d["engine"] == "unit":
        gpr, ltl, cap = z(), z(), z()
        burn = max(1.0, d["ltl_burnoff"])
        for u in d["unit_mix"]:
            cum_prev = 0.0
            for t in range(1, YEARS):
                gf = (1 + g) ** (t - 1)
                cum = min(u["count"], u["renovations_per_year"] * t)
                avg = (cum_prev + cum) / 2
                gpr[t] += 12 * (u["count"] * u["market_rent"] * gf + avg * u["renovation_premium"] * gf)
                gap = max(0.0, 1 - (t - 1) / burn)
                ltl[t] += 12 * (u["count"] - avg) * (u["market_rent"] - u["in_place_rent"]) * gf * gap
                cap[t] += (cum - cum_prev) * u["renovation_cost_per_unit"]
                cum_prev = cum
        for t in range(1, YEARS):
            base = gpr[t] - ltl[t]
            loss = base * (vac + d["concessions_pct"] + d["bad_debt_pct"])
            other = d["other_income"] * (1 + g) ** (t - 1)
            r["egi"][t] = base - loss + other
            r["capital"][t] = cap[t]
            r["occupancy"][t] = 1 - vac
    elif d["engine"] == "lease":
        base, rec, tilc, occ = z(), z(), z(), z()
        total_sf = sum(x["sf"] for x in d["tenants"]) + sum(x["sf"] for x in d["vacant_suites"])
        for tn in d["tenants"]:
            E, p, dm = tn["expiry"], tn["renew_prob"], tn["downtime"]
            m1 = tn["market_psf"] * (1 + g) ** E
            for t in range(1, YEARS):
                inplace = tn["rent_psf"] * tn["sf"] * (1 + tn["bump"]) ** (t - 1) if t <= E else 0.0
                post = m1 * tn["sf"] * (1 + tn["bump"]) ** (t - E - 1) if t > E else 0.0
                down = m1 * tn["sf"] * (1 - p) * dm / 12 if t == E + 1 else 0.0
                o = tn["sf"] * (1 - (1 - p) * dm / 12) if t == E + 1 else tn["sf"]
                base[t] += inplace + post - down
                occ[t] += o
                rec[t] += tn["recovery_psf"] * (1 + eg) ** (t - 1) * o
                if t == E + 1:
                    tilc[t] += tn["sf"] * (p * (tn["ti_ren"] + tn["lc_ren"]) + (1 - p) * (tn["ti_new"] + tn["lc_new"])) * (1 + eg) ** E
        for v in d["vacant_suites"]:
            L = v["lease_up"]
            for t in range(1, YEARS):
                rent = v["market_psf"] * v["sf"] * (1 + g) ** (L - 1) * (1 + v["bump"]) ** (t - L) if t >= L else 0.0
                o = v["sf"] if t >= L else 0.0
                base[t] += rent
                occ[t] += o
                rec[t] += v["recovery_psf"] * (1 + eg) ** (t - 1) * o
                if t == L:
                    tilc[t] += v["sf"] * (v["ti_new"] + v["lc_new"]) * (1 + eg) ** (L - 1)
        for t in range(1, YEARS):
            gross = base[t] + rec[t]
            other = d["other_income"] * (1 + g) ** (t - 1)
            r["egi"][t] = gross - gross * vac + other
            r["capital"][t] = tilc[t]
            r["occupancy"][t] = occ[t] / total_sf * (1 - vac)
    else:
        for t in range(1, YEARS):
            o = min(1.0, max(0.0, d["occupancy"][t - 1] + vac))
            rooms = d["keys"] * o * d["rate"] * (1 + g) ** (t - 1) * d["rate_periods"]
            total = rooms * (1 + d["other_rev_pct"])
            r["egi"][t] = total
            r["opex_engine"][t] = total * (d["dept_pct"] + d["undist_pct"])
            r["reserves"][t] = total * d["ffe_pct"]
            r["occupancy"][t] = o
    return r


def calc(d):
    k = d["sidx"]
    eg, cap0 = d["expense_growth"][k], d["exit_cap"][k]
    H = d["hold"]
    rv = revenue(d)
    inhold = [1.0 if 1 <= t <= H else 0.0 for t in range(YEARS)]
    sale = [1.0 if t == H else 0.0 for t in range(YEARS)]

    # Operating expenses and NOI
    tax1 = d["price"] * d["assess_ratio"] * d["tax_rate"] if d["tax_reassess"] else d["current_tax"]
    noi, cfbd, reserves, capital, tax, tpd = ([0.0] * YEARS for _ in range(6))
    noi[0] = d["trailing_noi"]
    for t in range(1, YEARS):
        egi = rv["egi"][t]
        items = sum(i["amount"] * (1 + (eg if i["growth"] is None else i["growth"])) ** (t - 1)
                    for i in d["expense_items"])
        tax[t] = tax1 * (1 + eg) ** (t - 1)
        tpd[t] = tax[t] / d["price"] if d["tax_reassess"] else 0.0   # tax per dollar of price
        opex = rv["opex_engine"][t] + items + d["mgmt_fee_pct"] * egi + tax[t] + d["insurance"] * (1 + eg) ** (t - 1)
        noi[t] = egi - opex
        reserves[t] = rv["reserves"][t] if d["engine"] == "operating" else d["reserves"] * (1 + eg) ** (t - 1)
        capital[t] = d["capex"][t - 1] + rv["capital"][t]
        cfbd[t] = noi[t] - reserves[t] - capital[t]

    # Debt sizing and schedule
    rate = d["loan_rate"]
    const = pmt(rate, d["amort_years"], 1.0) if d["amort_years"] > 0 else rate
    size_noi = noi[1] - reserves[1]
    tests = {"LTV": d["price"] * d["max_ltv"],
             "DSCR": size_noi / (d["min_dscr"] * const),
             "Debt yield": size_noi / d["min_dy"]}
    sized = min(tests.values())
    binding = [n for n in ("LTV", "DSCR", "Debt yield") if tests[n] == sized][0]
    loan = d["stated_loan"] if d["debt_mode"] == "Stated" else sized
    if d["debt_mode"] == "Stated":
        binding = "Stated amount"
    payment = pmt(rate, d["amort_years"], loan) if d["amort_years"] > 0 else 0.0
    opening, interest, principal, payoff, ds = ([0.0] * YEARS for _ in range(5))
    close = loan
    for t in range(1, YEARS):
        opening[t] = close
        interest[t] = opening[t] * rate * inhold[t]
        if t > d["io_years"] and d["amort_years"] > 0:
            principal[t] = min(opening[t], payment - opening[t] * rate) * inhold[t]
        payoff[t] = opening[t] - principal[t] if t == H else 0.0
        close = opening[t] - principal[t] - payoff[t]
        ds[t] = interest[t] + principal[t]

    # Sources and uses, sale, cash flows
    closing = d["price"] * d["closing_pct"]
    loan_fee = loan * d["loan_fee_pct"]
    uses = d["price"] + closing + d["upfront_capex"] + loan_fee
    equity = uses - loan
    exit_noi = noi[H + 1]
    exit_value = exit_noi / cap0
    sale_costs = exit_value * d["sale_cost_pct"]
    payoff_amt = sum(payoff)
    unlev = [0.0] * YEARS
    lev = [0.0] * YEARS
    unlev[0] = -(d["price"] + closing + d["upfront_capex"])
    lev[0] = -equity
    for t in range(1, YEARS):
        unlev[t] = inhold[t] * cfbd[t] + sale[t] * (exit_value - sale_costs)
        lev[t] = inhold[t] * (cfbd[t] - ds[t]) + sale[t] * (exit_value - sale_costs - payoff_amt)

    out = {"noi": noi, "loan": loan, "binding": binding, "debt_service": ds,
           "loan_tests": tests, "equity": equity, "exit_value": exit_value,
           "unlevered_irr": irr(unlev), "levered_irr": irr(lev),
           "equity_multiple": multiple(lev), "unlevered_multiple": multiple(unlev),
           "coc_y1": (cfbd[1] - ds[1]) / equity, "levered_cf": lev, "unlevered_cf": unlev,
           "going_in_cap": noi[1] / d["price"]}

    # Waterfall
    wf = waterfall(d, lev, equity, exit_value, inhold, sale)
    out.update(wf)

    # Sensitivity: scenario rows from base rows (linear in each driver)
    exit_tpd = tpd[H + 1]

    def scen(c, f, dpp, dr):
        dP = dpp * d["price"]
        cf = [lev[0] - dP * (1 + d["closing_pct"])]
        for t in range(1, YEARS):
            v = lev[t] + inhold[t] * ((f - 1) * noi[t] - dP * tpd[t] - dr * opening[t])
            v += sale[t] * (1 - d["sale_cost_pct"]) * ((f * exit_noi - dP * exit_tpd) / c - exit_noi / cap0)
            cf.append(v)
        return irr(cf)

    out["sens_base_irr"] = scen(cap0, 1.0, 0.0, 0.0)
    out["grid_cap_noi"] = [[scen(cap0 + (j - 2) * d["cap_step"], 1 + (i - 2) * d["noi_step"], 0, 0)
                            for j in range(5)] for i in range(5)]
    out["grid_cap_price"] = [[scen(cap0 + (j - 2) * d["cap_step"], 1.0, (i - 2) * d["price_step"], 0)
                              for j in range(5)] for i in range(5)]
    out["rate_irr"] = [scen(cap0, 1.0, 0.0, (i - 2) * d["rate_step"]) for i in range(5)]
    ladder = []
    for i in range(9):
        pct = d["ladder_low"] + i * d["ladder_step"]
        ladder.append((d["price"] * (1 + pct), scen(cap0, 1.0, pct, 0)))
    out["ladder"] = ladder
    h = d["hurdle_irr"]
    if ladder[-1][1] >= h:
        mb = ladder[-1][0]
    elif ladder[0][1] < h:
        mb = ladder[0][0]
    else:
        mb = 0.0
        for i in range(8):
            (p0, r0), (p1, r1) = ladder[i], ladder[i + 1]
            if r0 >= h and r1 < h:
                mb += p0 + (h - r0) / (r1 - r0) * (p1 - p0)
    out["max_bid"] = mb
    return out


def waterfall(d, lev, equity, exit_value, inhold, sale):
    s = d["inv_share"]
    rates = [d["pref"]] + [h for h, _ in d["tiers"]]
    promos = [0.0] + [p for _, p in d["tiers"]]
    pf = d["final_promote"]
    acq_fee = d["acq_fee_pct"] * d["price"]
    n = len(rates)
    acct = [0.0] * n
    inv_cf, inv_dist_all, inv_contrib_all, check = [], [], [], 0.0
    promote_total, fees_total = 0.0, acq_fee
    uc = pf_bal = 0.0          # unreturned capital, accrued unpaid pref
    cap_ok = True
    cum_contrib = cum_ret = peak = 0.0
    for t in range(YEARS):
        if t == 0:
            C, D = equity + acq_fee, 0.0
        else:
            am = inhold[t] * d["am_fee_pct"] * equity
            disp = sale[t] * d["disp_fee_pct"] * exit_value
            fees_total += am + disp
            cash = lev[t] - am - disp
            C, D = max(0.0, -cash), max(0.0, cash)
        peak += C
        IC = s * C
        pre = [acct[k] * (1 + rates[k]) + IC for k in range(n)]
        left, inv_paid, inv0 = D, 0.0, 0.0
        for k in range(n):
            share = s * (1 - promos[k])
            need = max(0.0, pre[k] - inv_paid) / share
            x = min(left, need)
            left -= x
            inv_paid += x * share
            promote_total += x * promos[k]
            if k == 0:
                inv0 = x * share
        inv_paid += left * (1 - pf) * s
        promote_total += left * pf
        acct = [max(0.0, pre[k] - inv_paid) if t <= d["hold"] else 0.0 for k in range(n)]
        # pref then capital split of band 0, for the capital account check
        due = (pf_bal + (uc + pf_bal) * d["pref"]) if t <= d["hold"] else 0.0
        pref_paid = min(inv0, due)
        cap_ret = inv0 - pref_paid
        uc, pf_bal = uc + IC - cap_ret, due - pref_paid
        cum_contrib += IC
        cum_ret += cap_ret
        if cum_ret > cum_contrib + 0.01:
            cap_ok = False
        inv_cf.append(inv_paid - IC)
        inv_dist_all.append(inv_paid)
        inv_contrib_all.append(IC)
    gross = [s * x for x in lev]
    return {"investor_net_irr": irr(inv_cf), "investor_net_multiple": sum(inv_dist_all) / sum(inv_contrib_all),
            "investor_gross_irr": irr(gross), "investor_gross_multiple": multiple(gross),
            "sponsor_promote": promote_total, "sponsor_fees": fees_total, "investor_cf": inv_cf,
            "capital_ok": cap_ok, "peak_equity": peak}


def key_outputs(res):
    return {k: res[k] for k in ("loan", "binding", "unlevered_irr", "levered_irr", "equity_multiple",
                                "coc_y1", "exit_value", "investor_net_irr", "investor_net_multiple",
                                "sponsor_promote", "max_bid")}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 repe_calc.py <deal.json>")
        sys.exit(2)
    r = calc(load_deal(sys.argv[1]))
    print(json.dumps({**key_outputs(r), "noi": r["noi"], "debt_service": r["debt_service"]}, indent=2))
