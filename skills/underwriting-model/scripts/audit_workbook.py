#!/usr/bin/env python3
"""Audit any Excel workbook, whatever its layout.

Usage:
  python3 audit_workbook.py <workbook.xlsx> [--inputs "Inputs,Assumptions"]
      [--irr "Returns!C40:O40=Returns!C45"] [--xirr "CF!C10:Z10@CF!C5:Z5=Summary!B12"]
      [--equal "Returns!B12=Returns!B15"] [--checks "Checks!C3"] [--json]

--irr, --xirr, --equal and --checks may be repeated or comma separated.
Tests: recalculation, error values, typed numbers in calculation areas, literals
inside formulas, structure (links, macros, data tables, hidden sheets, circular
references), row consistency, independent recompute, and check cells.
Each test reads PASS, FAIL, REVIEW (needs judgment) or SKIP. Exit 1 on any FAIL.
Standard library plus openpyxl. LibreOffice (soffice) is optional.
"""
import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

try:
    from openpyxl import load_workbook
    from openpyxl.utils import column_index_from_string, get_column_letter, range_boundaries
except ImportError:
    sys.exit("openpyxl is required: pip install openpyxl")

ERRORS = ("#REF!", "#DIV/0!", "#VALUE!", "#NAME?", "#N/A", "#NUM!", "#NULL!")
OK_LITERALS = {0, 1, 2, 4, 7, 12, 24, 52, 100, 360, 365, 1000}
RATE_TOL, AMT_TOL = 0.0005, 1.0
LIMIT = 20
REF_RE = re.compile(r"(?<![A-Za-z0-9_.$])(?:(?:'[^']+'|[A-Za-z0-9_.]+)!)?(\$?)([A-Z]{1,3})(\$?)(\d+)(?![A-Za-z0-9_(])")
STR_RE = re.compile(r'"[^"]*"')


# ---------------------------------------------------------------- helpers

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
    out = tempfile.mkdtemp(prefix="audit_recalc_")
    profile = tempfile.mkdtemp(prefix="audit_lo_profile_")
    cmd = [soffice, "-env:UserInstallation=file://" + profile, "--headless", "--calc",
           "--convert-to", "xlsx", "--outdir", out, os.path.abspath(path)]
    try:
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=240, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return None
    res = os.path.join(out, os.path.splitext(os.path.basename(path))[0] + ".xlsx")
    return res if os.path.exists(res) else None


def split_ref(ref):
    """'Sheet'!A1:B2 -> (sheet, 'A1:B2')."""
    sheet, rng = ref.rsplit("!", 1)
    return sheet.strip("'"), rng.replace("$", "")


def cell_values(wb, ref):
    sheet, rng = split_ref(ref)
    ws = wb[sheet]
    if ":" in rng:
        return [c.value for row in ws[rng] for c in row]
    return ws[rng].value


def is_num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def irr(cfs):
    def npv(r):
        return sum(c / (1 + r) ** i for i, c in enumerate(cfs))
    lo, hi = -0.99, 10.0
    flo, fhi = npv(lo), npv(hi)
    if flo * fhi > 0:
        return None
    for _ in range(300):
        mid = (lo + hi) / 2
        fm = npv(mid)
        if flo * fm <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def to_date(v):
    if isinstance(v, datetime.datetime):
        return v.date()
    if isinstance(v, datetime.date):
        return v
    if is_num(v):
        return datetime.date(1899, 12, 30) + datetime.timedelta(days=float(v))
    return None


def xirr(cfs, dates):
    d0 = dates[0]

    def npv(r):
        return sum(c / (1 + r) ** ((d - d0).days / 365.0) for c, d in zip(cfs, dates))
    lo, hi = -0.99, 10.0
    flo, fhi = npv(lo), npv(hi)
    if flo * fhi > 0:
        return None
    for _ in range(300):
        mid = (lo + hi) / 2
        fm = npv(mid)
        if flo * fm <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def is_rate_cell(wb_f, ref, v):
    sheet, rng = split_ref(ref)
    fmt = wb_f[sheet][rng].number_format or ""
    if "%" in fmt or "x" in fmt.lower():
        return True
    return is_num(v) and abs(v) < 10 and fmt in ("General", "0.00", "0.0000")


def pattern(formula, row, col):
    """R1C1-style pattern: references become offsets from the cell (absolute parts kept)."""
    f = STR_RE.sub('""', formula)

    def sub(m):
        cabs, c, rabs, r = m.groups()
        prefix = m.group(0)[:m.start(1) - m.start(0)]
        cc = column_index_from_string(c)
        cpart = "C%d" % cc if cabs else "C[%d]" % (cc - col)
        rpart = "R%s" % r if rabs else "R[%d]" % (int(r) - row)
        return prefix + rpart + cpart
    return REF_RE.sub(sub, f)


def literals(formula):
    """Numeric literals left in a formula after removing strings, references and names."""
    f = STR_RE.sub("", formula)
    f = re.sub(r"'[^']+'!", "", f)
    f = REF_RE.sub("", f)
    f = re.sub(r"[A-Za-z_][A-Za-z0-9_.]*", "", f)
    out = []
    for m in re.finditer(r"(?<![\d.])(\d+\.?\d*(?:[eE][-+]?\d+)?)(%?)", f):
        v = float(m.group(1)) / (100 if m.group(2) else 1)
        if v not in OK_LITERALS:
            out.append(m.group(0))
    return out


def header_row(cells):
    """True when numeric cells in a row look like years or periods (1, 2, 3 or 2026, 2027)."""
    nums = [v for _, v in cells if is_num(v)]
    if len(nums) < 3 or not all(float(v).is_integer() for v in nums):
        return False
    steps = {nums[i + 1] - nums[i] for i in range(len(nums) - 1)}
    return steps == {1}


# ---------------------------------------------------------------- audit

def audit(path, inputs=None, irrs=(), xirrs=(), equals=(), checks=()):
    res = {"file": os.path.basename(path), "tests": {}, "details": {}}
    T, D = res["tests"], res["details"]
    wb_f = load_workbook(path)

    # a. recalculation
    soffice = find_soffice()
    vals_path = recalc(path, soffice) if soffice else None
    if vals_path:
        T["Recalculation"] = "PASS"
        D["Recalculation"] = ["Recalculated with LibreOffice"]
    else:
        T["Recalculation"] = "SKIP"
        D["Recalculation"] = ["LibreOffice not found or failed; using values cached in the file"]
        vals_path = path
    wb_v = load_workbook(vals_path, data_only=True)

    # input sheets
    if inputs:
        input_sheets = {s.strip().lower() for s in inputs.split(",") if s.strip()}
    else:
        input_sheets = {ws.title.lower() for ws in wb_f.worksheets
                        if "input" in ws.title.lower() or "assumption" in ws.title.lower()}
    D["Input sheets"] = sorted(input_sheets) or ["none detected"]

    # b. error values
    errs = []
    for ws in wb_v.worksheets:
        for row in ws.iter_rows():
            for c in row:
                v = c.value
                if isinstance(v, str) and (v in ERRORS or v.startswith("Err:") or v.startswith("#NAME")):
                    errs.append("%s!%s %s" % (ws.title, c.coordinate, v))
    T["Error values"] = "FAIL" if errs else "PASS"
    D["Error values"] = ["%d error cells" % len(errs)] + errs[:LIMIT]

    # c, d, f: scan formulas sheet
    typed, flags, lits, incons = [], [], [], []
    for ws in wb_f.worksheets:
        calc_sheet = ws.title.lower() not in input_sheets
        for row in ws.iter_rows():
            cells = [(c, c.value) for c in row if c.value is not None]
            if not cells:
                continue
            hdr = header_row(cells)
            seq = []    # (col, kind, pattern) for row consistency
            for c, v in cells:
                if isinstance(v, str) and v.startswith("="):
                    for lit in literals(v):
                        lits.append("%s!%s %s" % (ws.title, c.coordinate, v[:80]))
                        break
                    seq.append((c.column, "f", pattern(v, c.row, c.column), c.coordinate))
                elif is_num(v):
                    seq.append((c.column, "n", None, c.coordinate))
                    if calc_sheet and not hdr and c.column > 1:
                        item = "%s!%s = %s" % (ws.title, c.coordinate, v)
                        (flags if v in (0, 1) else typed).append(item)
            if calc_sheet:
                incons.extend(row_outliers(ws.title, seq))
    T["Typed numbers"] = "REVIEW" if typed else "PASS"
    D["Typed numbers"] = ["%d typed numbers outside input sheets; %d 0/1 flags (lower severity)"
                          % (len(typed), len(flags))] + typed[:LIMIT] + flags[:max(0, LIMIT - len(typed))]
    T["Formula literals"] = "REVIEW" if lits else "PASS"
    D["Formula literals"] = ["%d formulas hold numeric literals" % len(lits)] + lits[:LIMIT]
    T["Row consistency"] = "REVIEW" if incons else "PASS"
    D["Row consistency"] = ["%d cells break the pattern of their neighbors" % len(incons)] + incons[:LIMIT]

    # e. structure
    fails, reviews = [], []
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        if any(n.startswith("xl/externalLinks/") for n in names):
            fails.append("External links present")
        if any(n.endswith("vbaProject.bin") for n in names):
            fails.append("Macros present (vbaProject.bin)")
        wbxml = z.read("xl/workbook.xml").decode("utf-8", "ignore") if "xl/workbook.xml" in names else ""
        if re.search(r'iterate="(1|true)"', wbxml):
            reviews.append("Iterative calculation is on: a common cover for circular references")
        for n in names:
            if n.startswith("xl/worksheets/") and n.endswith(".xml"):
                if 't="dataTable"' in z.read(n).decode("utf-8", "ignore"):
                    fails.append("Data table in " + n)
    for ws in wb_f.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("=") and re.search(r"\[\d+\]|TABLE\(", c.value):
                    fails.append("External link or data table formula: %s!%s" % (ws.title, c.coordinate))
    circ = [e for e in errs if "Err:522" in e or "Err:523" in e]
    if circ:
        fails.append("Circular reference symptoms: %d cells (Err:522/523)" % len(circ))
    hidden = [ws.title for ws in wb_f.worksheets if ws.sheet_state != "visible"]
    if hidden:
        reviews.append("Hidden sheets: " + ", ".join(hidden))
    T["Structure"] = "FAIL" if fails else ("REVIEW" if reviews else "PASS")
    D["Structure"] = (fails + reviews)[:LIMIT] or ["No links, macros, data tables, hidden sheets or circular symptoms"]

    # g. independent recompute
    rec, rfail = [], False
    for spec in irrs:
        try:
            rng, cell = spec.split("=")
            cfs = [v if is_num(v) else 0.0 for v in cell_values(wb_v, rng)]
            mine, theirs = irr(cfs), cell_values(wb_v, cell)
            ok = mine is not None and is_num(theirs) and abs(mine - theirs) <= RATE_TOL
            rec.append("IRR %s: workbook %s, recomputed %s %s" % (cell, _f(theirs), _f(mine), "OK" if ok else "MISMATCH"))
        except Exception as exc:
            ok = False
            rec.append("IRR %s: could not evaluate (%s)" % (spec, exc))
        rfail |= not ok
    for spec in xirrs:
        try:
            left, cell = spec.split("=")
            rng, drng = left.split("@")
            cv, dv = cell_values(wb_v, rng), cell_values(wb_v, drng)
            pairs = [(c, to_date(d)) for c, d in zip(cv, dv) if is_num(c) and to_date(d)]
            mine = xirr([p[0] for p in pairs], [p[1] for p in pairs]) if pairs else None
            theirs = cell_values(wb_v, cell)
            ok = mine is not None and is_num(theirs) and abs(mine - theirs) <= RATE_TOL
            rec.append("XIRR %s: workbook %s, recomputed %s %s" % (cell, _f(theirs), _f(mine), "OK" if ok else "MISMATCH"))
        except Exception as exc:
            ok = False
            rec.append("XIRR %s: could not evaluate (%s)" % (spec, exc))
        rfail |= not ok
    for spec in equals:
        try:
            a, b = spec.split("=")
            va, vb = cell_values(wb_v, a), cell_values(wb_v, b)
            if is_num(va) and is_num(vb):
                tol = RATE_TOL if is_rate_cell(wb_f, a, va) else AMT_TOL
                ok = abs(va - vb) <= tol
            else:
                ok = va == vb and va is not None
            rec.append("Equal %s = %s: %s vs %s %s" % (a, b, _f(va), _f(vb), "OK" if ok else "MISMATCH"))
        except Exception as exc:
            ok = False
            rec.append("Equal %s: could not evaluate (%s)" % (spec, exc))
        rfail |= not ok
    if rec:
        T["Recompute"] = "FAIL" if rfail else "PASS"
        D["Recompute"] = rec
    else:
        T["Recompute"] = "SKIP"
        D["Recompute"] = ["No --irr, --xirr or --equal given"]

    # h. check cells
    chk, cfail = [], False
    for ref in checks:
        try:
            v = cell_values(wb_v, ref)
        except Exception as exc:
            v = "unreadable (%s)" % exc
        ok = (isinstance(v, str) and v.strip().upper() in ("OK", "TRUE", "PASS")) or v is True or (is_num(v) and v == 0)
        cfail |= not ok
        chk.append("%s reads %s %s" % (ref, v, "OK" if ok else "FAIL"))
    if chk:
        T["Check cells"] = "FAIL" if cfail else "PASS"
        D["Check cells"] = chk
    else:
        T["Check cells"] = "SKIP"
        D["Check cells"] = ["No --checks given"]

    st = list(T.values())
    res["overall"] = "FAIL" if "FAIL" in st else ("REVIEW" if "REVIEW" in st else "PASS")
    return res


def row_outliers(sheet, seq):
    """Flag a cell whose formula pattern (or typed number) differs while its neighbors agree."""
    out = []
    for i in range(1, len(seq)):
        col, kind, pat, coord = seq[i]
        left = seq[i - 1]
        right = seq[i + 1] if i + 1 < len(seq) else None
        left2 = seq[i - 2] if i >= 2 else None
        key = lambda s: (s[1], s[2])
        adjacent = lambda a, b: b[0] - a[0] == 1
        right2 = seq[i + 2] if i + 2 < len(seq) else None
        if right and adjacent(left, seq[i]) and adjacent(seq[i], right):
            third = (left2 and adjacent(left2, left) and key(left2) == key(left)) or \
                    (right2 and adjacent(right, right2) and key(right2) == key(right))
            if third and key(left) == key(right) and left[1] == "f" and key(seq[i]) != key(left):
                out.append("%s!%s differs from its neighbors" % (sheet, coord))
        elif right is None and left2 and adjacent(left2, left) and adjacent(left, seq[i]):
            if key(left2) == key(left) and left[1] == "f" and key(seq[i]) != key(left):
                out.append("%s!%s (last period) differs from the cells before it" % (sheet, coord))
    return out


def _f(v):
    if is_num(v):
        return "%.6f" % v if abs(v) < 100 else "{:,.2f}".format(v)
    return str(v)


def _multi(vals):
    out = []
    for v in vals or []:
        out += [x.strip() for x in v.split(",") if x.strip()]
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="Audit any Excel workbook, whatever its layout.")
    ap.add_argument("workbook")
    ap.add_argument("--inputs", help='Input sheet names, comma separated, e.g. "Inputs,Assumptions"')
    ap.add_argument("--irr", action="append", help="CashFlowRange=ReportedIRRCell")
    ap.add_argument("--xirr", action="append", help="CashFlowRange@DateRange=ReportedXIRRCell")
    ap.add_argument("--equal", action="append", help="CellA=CellB")
    ap.add_argument("--checks", action="append", help="Check cells that should read OK")
    ap.add_argument("--json", action="store_true", help="Print the report as JSON")
    a = ap.parse_args(argv)
    res = audit(a.workbook, a.inputs, _multi(a.irr), _multi(a.xirr), _multi(a.equal), _multi(a.checks))
    if a.json:
        print(json.dumps(res, indent=2))
    else:
        print("Workbook audit: %s" % res["file"])
        print("Input sheets: %s" % ", ".join(res["details"]["Input sheets"]))
        for name, status in res["tests"].items():
            print("\n[%s] %s" % (status, name))
            for line in res["details"][name]:
                print("    " + line)
        print("\nSummary")
        for name, status in res["tests"].items():
            print("  %-18s %s" % (name, status))
        print("OVERALL: %s" % res["overall"])
    return 1 if res["overall"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
