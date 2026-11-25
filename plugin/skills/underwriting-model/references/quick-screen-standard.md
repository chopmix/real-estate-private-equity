# Quick screen standard

A quick screen answers one question fast: is this deal worth real underwriting, and at what price? It is annual, compact and built in minutes. It is never a bid or a committee number.

## What it must show

| Output | Notes |
|--------|-------|
| Price, price per unit or SF, in-place and going-in cap rate | In-place on trailing NOI. Going-in on Year 1 NOI after tax reassessment |
| Loan amount and the binding test | Lowest of LTV, DSCR and debt yield from the buy box |
| Equity required and peak equity | Include closing costs, loan fee and upfront capital |
| Unlevered and levered IRR, equity multiple, Year 1 cash on cash | Annual, year-end cash flows |
| Yield on cost | Stabilized NOI over total cost |
| Maximum bid at the firm's hurdle | With the discount or premium to ask |
| Returns attribution and a cap rate flag | Flag when exit pricing supplies most of the profit |
| Two sensitivity grids | Exit cap rate against NOI versus plan, and exit cap rate against price |

## Inputs

Keep the list short. Take what the documents give and fill the rest from the buy box, tagging each fill `[Assumed]`.

| Group | Inputs |
|-------|--------|
| Deal | Property type, size, price, closing costs, hold period |
| Income | Trailing NOI, or rent and occupancy with an expense ratio. Rent growth, expense growth |
| Plan | Upfront capital, renovation or lease-up effect on NOI, stabilized year |
| Tax | Reassessed property tax where the jurisdiction resets on sale |
| Debt | LTV, DSCR and debt yield limits, rate, interest-only years, amortization, loan fee |
| Exit | Exit cap rate, sale costs |
| Hurdle | The firm's levered IRR hurdle |

## How to build it

The method is open. These practices keep it trustworthy.

- One small workbook with live formulas. Inputs on one sheet, calculations elsewhere, a checks area.
- Use the revenue engine that fits: unit mix, tenant table, or operating drivers. Keep it to the few lines that move the answer.
- Value the exit on the NOI of the year after sale.
- Size the loan to the lowest test and say which one binds.
- Build the sensitivity grids from formulas so they recalculate. Each grid cell can use its own row of cash flows, since levered cash flow responds simply to exit cap rate, NOI level and price.
- Find the maximum bid from a ladder of prices around ask, reading across to the price where levered IRR equals the hurdle. Hold the loan at its base dollar amount and say so, since a lender may cut proceeds at a lower price.
- Include a Base and a Downside case.

## Checks

| Check | Passes when |
|-------|-------------|
| Sources and uses | Totals match |
| Loan sizing | Loan does not exceed the binding test |
| Loan balance | Balance rolls each year |
| NOI tie | Year 0 NOI matches the trailing figure supplied |
| Independent recompute | Levered IRR and multiple recalculated outside the workbook match it |

## How to report it

- Label the workbook and the summary "Quick screen".
- Lead with the maximum bid against ask and the verdict inputs for `deal-screening`.
- List every `[Assumed]` input.
- State what a full model would add: monthly timing, lease-by-lease or unit-level detail, the real debt structure and the waterfall.
