#!/usr/bin/env python3
"""Test audit_workbook.py on the multifamily quick model and on corrupted copies.

Usage: python3 tests/test_audit.py   (exits non-zero on failure)
"""
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "quick-screen")
DEAL = os.path.join(ROOT, "quick-screen", "examples", "multifamily_value_add.json")
sys.path.insert(0, SCRIPTS)

from openpyxl import load_workbook  # noqa: E402

import audit_workbook  # noqa: E402
import repe_model  # noqa: E402


def find_row(ws, label):
    for r in range(1, ws.max_row + 1):
        if ws.cell(r, 1).value == label:
            return r
    raise KeyError(label)


def run(path, irr, checks):
    return audit_workbook.audit(path, None, [irr], [], [], [checks])


def main():
    tmp = tempfile.mkdtemp(prefix="audit_test_")
    clean = os.path.join(tmp, "clean.xlsx")
    repe_model.build(DEAL, clean)
    wb = load_workbook(clean)
    ret = wb["Returns"]
    lv, lirr = find_row(ret, "Levered cash flow"), find_row(ret, "Levered IRR")
    irr = "Returns!C%d:N%d=Returns!C%d" % (lv, lv, lirr)
    checks = "Checks!C3"
    failures = []

    def expect(name, cond, res):
        print("%-60s %s" % (name, "ok" if cond else "FAILED"))
        if not cond:
            failures.append(name)
            print("    tests: %s" % res["tests"])

    # 1. Clean model: recompute and checks pass
    res = run(clean, irr, checks)
    expect("clean: recompute PASS", res["tests"]["Recompute"] == "PASS", res)
    expect("clean: check cells PASS", res["tests"]["Check cells"] == "PASS", res)
    expect("clean: no error values", res["tests"]["Error values"] == "PASS", res)
    expect("clean: no typed numbers outside Inputs", res["tests"]["Typed numbers"] == "PASS", res)

    # 2. A formula overwritten with a typed number is flagged
    over = os.path.join(tmp, "overwritten.xlsx")
    wb = load_workbook(clean)
    wb["Returns"]["F%d" % lv] = 123456.0
    wb.save(over)
    res = run(over, irr, checks)
    expect("overwrite: typed number flagged REVIEW", res["tests"]["Typed numbers"] == "REVIEW", res)
    expect("overwrite: row consistency flagged REVIEW", res["tests"]["Row consistency"] == "REVIEW", res)
    expect("overwrite: overall not PASS", res["overall"] in ("REVIEW", "FAIL"), res)

    # 3. An injected error value fails the audit
    bad = os.path.join(tmp, "error.xlsx")
    wb = load_workbook(clean)
    cf = wb["CashFlow"]
    noi = find_row(cf, "Net operating income")
    cf["E%d" % noi] = "=1/0"
    wb.save(bad)
    res = run(bad, irr, checks)
    expect("error: error values FAIL", res["tests"]["Error values"] == "FAIL", res)
    expect("error: overall FAIL", res["overall"] == "FAIL", res)

    if failures:
        print("TEST RESULT: FAIL (%d)" % len(failures))
        return 1
    print("TEST RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
