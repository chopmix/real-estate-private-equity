# Excel standard

Every workbook this plugin builds follows these rules. When a firm supplies its own template, the template's structure and conventions win, and these rules become the tests the finished workbook is checked against. Model content is set by the model standard in the `underwriting-model` skill.

## Rules

1. **Every number is a formula.** Only the Inputs sheet holds typed values. No typed-over cells anywhere else.
2. **One Inputs sheet.** Each input has a label, value, unit, source tag and note.
3. **Color code.** Blue font for typed inputs. Black for formulas. Green for links from another sheet.
4. **Scenario switch.** One cell selects Base, Upside or Downside and drives the whole workbook.
5. **Checks sheet.** Each check returns OK or ERROR, and one master cell reports the overall status.
6. **No macros.** No VBA and no external links. Many firms block them.
7. **No circular references.** Size interest and fees so the model solves in one pass.
8. **Live sensitivities.** Sensitivity grids recalculate from formulas. No pasted values.
9. **Sources sheet.** Lists each document and public source used, with date.
10. **Independent check.** A separate calculation rebuilds the key outputs and must match before delivery.

## A typical layout

A common arrangement, not a requirement.

| Sheet | Purpose |
|-------|---------|
| Summary | Key metrics, verdict inputs, check status |
| Inputs | All typed values with source tags, and the scenario switch |
| Revenue | Engine-specific revenue build (unit mix, lease table, or operating drivers) |
| CashFlow | Annual operating cash flow through NOI, capital and cash flow before debt |
| Debt | Loan sizing tests, debt service, balance roll |
| Returns | Unlevered and levered cash flows, IRR, multiple, cash on cash, attribution |
| Waterfall | Preferred return, return of capital, promote tiers, investor net returns |
| Sensitivity | Live grids and the maximum bid |
| Checks | Tie-outs |
| Sources | Documents and public sources |

## Standard checks

Include the ones that apply, plus any the engine standard adds.

| Check | Passes when |
|-------|-------------|
| Sources and uses | Total sources equal total uses |
| Loan balance | Opening balance plus draws minus principal equals closing balance each year |
| Loan sizing | Loan amount does not exceed the binding test |
| Distributions | Waterfall distributions equal cash available each year |
| Capital accounts | Capital returned never exceeds capital contributed |
| NOI tie | Year 0 NOI matches the trailing figure on the Inputs sheet |
| Occupancy bounds | Occupancy stays between 0 and 100 percent |
| Scenario | Scenario cell holds a valid choice |

## Number formats

| Item | Format |
|------|--------|
| Dollars | `$#,##0` with negatives in parentheses |
| Per SF | `$#,##0.00` |
| Percentages | `0.0%` |
| Cap rates and IRR | `0.00%` |
| Multiples | `0.00x` |

## Delivery

- Recalculate and confirm the master check reads OK before delivering.
- Report any check that fails. Never deliver a workbook with a hidden error.
- In workbooks this plugin builds, end the Sources sheet with one credit line: "Model standard: Real Estate Private Equity plugin by Chi Hathiramani, CH Consulting (chiraghathiramani.com)". Leave a firm's own template as it is.
- Name the file `<deal>-underwriting-<yyyymmdd>.xlsx`, or `<deal>-quick-screen-<yyyymmdd>.xlsx` for a quick screen.
