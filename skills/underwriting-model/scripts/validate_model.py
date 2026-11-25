#!/usr/bin/env python3
"""Validate an underwriting workbook against the independent Python recalculation.

Usage: python3 validate_model.py <deal.json> <model.xlsx>

1. Recalculates the workbook with LibreOffice headless (if soffice is found).
2. Compares key outputs to repe_calc.py ($1 on amounts, 0.0005 on rates).
3. Confirms the master check reads OK and no cell shows an error.
4. Confirms no calculated sheet holds typed numbers outside Inputs.
Prints a PASS / FAIL report and exits 0 on PASS, 1 on FAIL.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

try:
    from openpyxl import load_workbook
except ImportError:
    sys.exit("openpyxl is required: pip install openpyxl")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from repe_calc import calc, load_deal

AMT_TOL, RATE_TOL = 1.0, 0.0005
REQUIRED_SHEETS = ["Summary", "Inputs", "Revenue", "CashFlow", "Debt", "Returns",
                   "Waterfall", "Sensitivity", "Checks", "Sources"]
CREDIT = "Model standard: Real Estate Private Equity plugin by Chi Hathiramani, CH Consulting (chiraghathiramani.com)"


def find_soffice():
    for name in ("soffice", "libreoffice"):
        p = shutil.which(name)
        if p:
            return p
    for p in ("/usr/bin/soffice", "/Applications/LibreOffice.app/Contents/MacOS/soffice"):
        if os.path.exists(p):
            return p
    return None


def recalc(path, soffice):
    """Open and re-save with LibreOffice so formula values are cached."""
    out = tempfile.mkdtemp(prefix="repe_recalc_")
    profile = tempfile.mkdtemp(prefix="repe_lo_profile_")
    cmd = [soffice, "-env:UserInstallation=file://" + profile, "--headless", "--calc",
           "--convert-to", "xlsx", "--outdir", out, path]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=180, check=False)
    res = os.path.join(out, os.path.basename(path))
    return res if os.path.exists(res) else None


def resolve(wb, name):
    """Return the value(s) at a defined name: a scalar or a list for a row range."""
    dn = wb.defined_names[name]
    sheet, ref = dn.attr_text.split("!")
    ref = ref.replace("$", "")
    ws = wb[sheet]
    if ":" in ref:
        return [c.value for row in ws[ref] for c in row]
    return ws[ref].value


def structural(wb_formulas):
    """Checks that need no recalculation."""
    issues = []
    names = wb_formulas.sheetnames
    if names != REQUIRED_SHEETS:
        issues.append("Sheet list or order differs from the standard: %s" % names)
    for ws in wb_formulas.worksheets:
        for row in ws.iter_rows():
            for c in row:
                v = c.value
                if ws.title != "Inputs" and isinstance(v, (int, float)) and not isinstance(v, bool):
                    issues.append("Typed number outside Inputs: %s!%s" % (ws.title, c.coordinate))
                if isinstance(v, str) and v.startswith("="):
                    if re.search(r"\[\d+\]|TABLE\(", v):
                        issues.append("External link or data table: %s!%s" % (ws.title, c.coordinate))
    if getattr(wb_formulas, "_external_links", None):
        issues.append("Workbook has external links")
    if getattr(wb_formulas, "vba_archive", None):
        issues.append("Workbook contains macros")
    src = wb_formulas["Sources"]
    texts = [c.value for row in src.iter_rows() for c in row if isinstance(c.value, str)]
    if not texts or texts[-1] != CREDIT:
        issues.append("Sources sheet does not end with the credit line")
    return issues


def compare(wb_vals, res):
    """Compare cached workbook values to the Python results."""
    rows, fails = [], 0
    pairs = [
        ("Loan amount", "out_LoanAmount", res["loan"], "amt"),
        ("Binding test", "out_Binding", res["binding"], "text"),
        ("Unlevered IRR", "out_UnlevIRR", res["unlevered_irr"], "rate"),
        ("Levered IRR", "out_LevIRR", res["levered_irr"], "rate"),
        ("Equity multiple", "out_EM", res["equity_multiple"], "rate"),
        ("Cash on cash, Year 1", "out_CoC1", res["coc_y1"], "rate"),
        ("Exit value", "out_ExitValue", res["exit_value"], "amt"),
        ("Investor net IRR", "out_InvNetIRR", res["investor_net_irr"], "rate"),
        ("Investor net multiple", "out_InvNetEM", res["investor_net_multiple"], "rate"),
        ("Sponsor promote", "out_Promote", res["sponsor_promote"], "amt"),
        ("Maximum bid", "out_MaxBid", res["max_bid"], "amt"),
        ("Peak equity", "out_PeakEquity", res["peak_equity"], "amt"),
        ("Sensitivity base IRR", "out_SensBase", res["sens_base_irr"], "rate"),
    ]
    for label, nm, py, kind in pairs:
        xl = resolve(wb_vals, nm)
        ok = _match(xl, py, kind)
        fails += 0 if ok else 1
        rows.append((label, xl, py, ok))
    for label, nm, key in (("NOI by year", "out_NOI", "noi"), ("Debt service by year", "out_DebtService", "debt_service")):
        xl = resolve(wb_vals, nm)
        py = res[key]
        ok = len(xl) == len(py) and all(_match(a or 0.0, b, "amt") for a, b in zip(xl, py))
        fails += 0 if ok else 1
        rows.append((label, "%d years" % len(xl), "max diff %.2f" % max(abs((a or 0.0) - b) for a, b in zip(xl, py)), ok))
    return rows, fails


def _match(xl, py, kind):
    if kind == "text":
        return str(xl) == str(py)
    if not isinstance(xl, (int, float)):
        return False
    tol = AMT_TOL if kind == "amt" else RATE_TOL
    return abs(xl - py) <= tol


def error_cells(wb_vals):
    bad = []
    for ws in wb_vals.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and (c.value.startswith("#") or c.value.startswith("Err:")):
                    bad.append("%s!%s=%s" % (ws.title, c.coordinate, c.value))
    return bad


def fmt(v):
    if isinstance(v, float):
        return "%.6f" % v if abs(v) < 100 else "{:,.2f}".format(v)
    return str(v)


def main(deal_path, xlsx_path):
    failed = False
    print("Validating %s" % os.path.basename(xlsx_path))
    wb_f = load_workbook(xlsx_path)
    issues = structural(wb_f)
    print("[%s] Structure: sheets, typed numbers outside Inputs, links, credit line" % ("FAIL" if issues else "PASS"))
    for i in issues[:20]:
        print("    " + i)
    failed |= bool(issues)

    soffice = find_soffice()
    if not soffice:
        print("[SKIP] Recalculation: LibreOffice (soffice) not found. Open the file in Excel, "
              "confirm Checks!C3 reads OK, and compare to repe_calc.py by hand.")
        print("RESULT: %s (structural checks only)" % ("FAIL" if failed else "PASS"))
        return 1 if failed else 0
    rc = recalc(os.path.abspath(xlsx_path), soffice)
    if not rc:
        print("[FAIL] Recalculation: LibreOffice did not produce a file")
        return 1
    wb_v = load_workbook(rc, data_only=True)
    errs = error_cells(wb_v)
    print("[%s] Error values after recalculation: %d" % ("FAIL" if errs else "PASS", len(errs)))
    for e in errs[:10]:
        print("    " + e)
    failed |= bool(errs)
    master = resolve(wb_v, "out_Master")
    print("[%s] Master check cell reads %s" % ("PASS" if master == "OK" else "FAIL", master))
    failed |= master != "OK"
    if master != "OK":
        ws = wb_v["Checks"]
        for r in range(6, ws.max_row + 1):
            if ws["C%d" % r].value == "ERROR":
                print("    ERROR: %s (value %s)" % (ws["A%d" % r].value, ws["B%d" % r].value))

    res = calc(load_deal(deal_path))
    rows, fails = compare(wb_v, res)
    print("[%s] Excel versus Python ($1 on amounts, 0.0005 on rates)" % ("FAIL" if fails else "PASS"))
    print("    %-24s %20s %20s" % ("Output", "Excel", "Python"))
    for label, xl, py, ok in rows:
        print("    %-24s %20s %20s %s" % (label, fmt(xl), fmt(py), "" if ok else "<- MISMATCH"))
    failed |= bool(fails)
    print("RESULT: %s" % ("FAIL" if failed else "PASS"))
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python3 validate_model.py <deal.json> <model.xlsx>")
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
