#!/usr/bin/env python3
"""End-to-end test: build and validate every example deal. Exits non-zero on failure.

Usage: python3 tests/test_engine.py
"""
import glob
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "skills", "underwriting-model", "scripts")
EXAMPLES = os.path.join(ROOT, "skills", "underwriting-model", "assets", "examples")
sys.path.insert(0, SCRIPTS)

import repe_model  # noqa: E402
import validate_model  # noqa: E402


def main():
    deals = sorted(glob.glob(os.path.join(EXAMPLES, "*.json")))
    if len(deals) < 3:
        print("FAIL: expected three example deals, found %d" % len(deals))
        return 1
    out_dir = tempfile.mkdtemp(prefix="repe_test_")
    failures = []
    for deal in deals:
        name = os.path.splitext(os.path.basename(deal))[0]
        out = os.path.join(out_dir, name + ".xlsx")
        try:
            repe_model.build(deal, out)
            rc = validate_model.main(deal, out)
        except Exception as exc:  # report and continue with the next deal
            print("FAIL: %s raised %r" % (name, exc))
            rc = 1
        if rc != 0:
            failures.append(name)
        print("-" * 60)
    if failures:
        print("TEST RESULT: FAIL (%s)" % ", ".join(failures))
        return 1
    print("TEST RESULT: PASS (%d deals)" % len(deals))
    return 0


if __name__ == "__main__":
    sys.exit(main())
