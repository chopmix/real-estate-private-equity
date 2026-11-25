# Workbook audit checklist

Run this on any workbook before it is delivered: one Claude built, or a firm's own template. It covers the mechanical tests. The judgment tests are in `model-standard.md`.

The method is open. Open the file with whatever tools are available, write a short script if that is fastest, and recalculate the workbook first when the environment allows it. Report what was checked and what could not be.

## Mechanical tests

| Test | What to look for | Result |
|------|------------------|--------|
| Recalculation | The workbook recalculates and the values are current | SKIP if it cannot be recalculated here. Say so |
| Error values | Any `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A` or `#NUM!` | FAIL if any exist. List the cells |
| Typed numbers in calculations | Numeric constants in cells outside the input sheets, ignoring period headers and 0 or 1 flags | REVIEW. List the first 20 |
| Numbers inside formulas | Literals such as `=B5*1.03` that hide an assumption | REVIEW. List the first 20 with the formula |
| Row consistency | A row whose formulas change pattern partway across the periods, a common sign of an overwritten cell | REVIEW. List the rows |
| Structure | External links, macros, data tables, hidden sheets, circular references | REVIEW, or FAIL for links that do not resolve |
| Ties | Sources equal uses. Debt balances roll. Distributions equal cash available. Capital returned does not exceed capital contributed | FAIL if any tie is off by more than a dollar |
| Check cells | Every check the model carries reads OK | FAIL if any reads otherwise |
| Independent recompute | IRR, multiple and net proceeds recalculated outside the workbook from its own cash flow rows | FAIL if rates differ by more than 0.0005 or amounts by more than a dollar |

## Independent recompute

1. Read the cash flow row behind each headline return: unlevered, levered and investor net.
2. Recalculate the return outside the workbook. Use date-based IRR when the cash flows carry dates.
3. Compare with the reported cell.
4. Recalculate the equity multiple as total distributions over total equity invested.

A match shows the return formula reads the right cells. It does not show the cash flows themselves are right. That is what the reconcile and reasonableness tests are for.

## Results

| Result | Meaning | Action |
|--------|---------|--------|
| PASS | The test found nothing | Proceed |
| REVIEW | Findings that need judgment | Explain each, or fix it |
| FAIL | The workbook is wrong or cannot be trusted as it stands | Fix and audit again |
| SKIP | The test could not run here | Say why, and tell the user how to run it |

## Reporting

Deliver a short audit note with the workbook.

| Item | Content |
|------|---------|
| Workbook and date | File name and when it was audited |
| Result by test | PASS, REVIEW, FAIL or SKIP |
| Findings | Cell references and one line each |
| Judgment tests | Flex, reconcile, reasonable, downside: result and reasoning |
| Not checked | Anything the audit could not cover |

In a firm's own template, report findings. Do not fix them without being asked.
