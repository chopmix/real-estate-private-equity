# Model standard

What an institutional-grade real estate model must achieve. This standard describes outcomes and the tests that prove them. It does not prescribe a layout or a method. Build the model the best way available, then show that it meets the standard.

## 1. Questions the model must answer

| Question | Evidence in the model |
|----------|-----------------------|
| What is it worth to us? | Maximum price at the firm's hurdle, and the discount or premium to ask |
| How much debt can it carry? | Each sizing test, the one that binds, and coverage through the hold |
| What do we earn? | Unlevered and levered returns, and investor returns before and after fees and promote |
| What has to go right? | The few drivers that produce most of the profit, and a returns attribution |
| What if it does not? | A downside case, sensitivities, and breakeven points |
| How much cash, and when? | Sources and uses, peak equity, capital calls, and distributions by period |

A model that cannot answer all six is not finished, however detailed it is.

## 2. Principles

- **Traceable.** Every output traces to inputs, and every input shows its source tag. A reviewer can follow any number in a few clicks.
- **Flexible.** Assumptions change in one place. No formula needs rewriting to test a different price, rate, timing or structure.
- **Honest about timing.** Use monthly periods whenever timing drives value: renovations, lease-up, rollover, construction, floating-rate debt or a short hold. Annual periods are acceptable for a stabilized first look. Use date-based returns when cash flows are dated.
- **Built at the level income is earned.** Unit types for residential, leases for commercial, operating drivers for hotels, seniors housing and storage. Blended shortcuts hide the plan.
- **Consistent.** One definition per metric, from `repe-core/references/metrics-and-formulas.md`. One formula across a row.
- **Self-checking.** The model proves that it ties, and says so in one place.
- **Proportionate.** Match the detail to the decision. A screen needs less than a committee model. Do not build what the decision does not need.

## 3. Required content

Whatever the layout, a full model contains:

- Inputs, separated from calculations, each with a source tag
- Revenue build at the level income is earned, in place and projected
- Expenses by line, with property tax reassessed where the jurisdiction reassesses on sale
- Capital plan: renovations, tenant improvements, commissions, reserves, with timing
- Debt: sizing tests, structure, floating rate and hedge cost, interest-only period, extension tests, covenants tested each period
- Sources and uses, including closing costs, fees, reserves and working capital
- Unlevered and levered cash flows and returns
- Waterfall from property cash flow to investor net returns
- At least a base and a downside case
- Sensitivities on the two or three drivers that matter most for this deal
- Breakevens: occupancy and rent that cover debt service, and the exit cap rate that returns capital
- Returns attribution
- Checks, and a log of source documents

The engine standards in this folder add what each property type requires.

## 4. Three ways to produce a model

| Path | Use when | Rule |
|------|----------|------|
| Firm template | The firm has its own model | Use it. Keep its structure and conventions. Map inputs in, complete it, and test it against this standard |
| Build to standard | No template, and the decision needs a full model | Build a workbook that meets this standard and the engine standard. The method is open |
| Quick screen | First look, triage, or maximum bid | Build to `quick-screen-standard.md`. Annual, fast, and labeled as a screen |

When a firm's convention differs from this standard, the firm's convention wins. Record the difference as an observation for the reviewer. Do not change the template to fit.

## 5. Tests a finished model must pass

| Test | Passes when |
|------|-------------|
| Ties | Sources equal uses. Debt balances roll. Distributions equal cash available. Capital returned never exceeds capital contributed |
| Clean | No error values, no external links, no macros, no unexplained typed numbers inside calculations |
| Independent recompute | Headline returns recalculated outside the workbook match it |
| Flex | Changing price, rent growth, exit cap rate and interest rate moves every output in the right direction, by a sensible amount |
| Reconciles to the documents | In-place income and expenses tie to the rent roll and trailing statement, or the gap is explained |
| Reasonable | Growth, margins, expense ratios and exit pricing sit within what the evidence supports, or the exception is argued |
| Downside | The downside case still covers debt service and passes extension tests, or the shortfall is sized |
| Reviewable | A person who did not build it can find the inputs, follow the logic, and see the checks |

`audit-checklist.md` covers the mechanical tests. The reasonableness and downside tests need judgment.

## 6. Where models go wrong

- The broker's pro forma is carried into the base case without challenge.
- Blended rents or blended growth hide a plan that depends on a few unit types or tenants.
- Property tax and insurance are held flat or grown at general inflation.
- Reserves sit above NOI, or are left out, so the cap rate and the loan size are both overstated.
- The exit is valued on the sale year's NOI instead of the following year's.
- Exit cap rate compression supplies most of the profit.
- Floating-rate debt is modeled at today's rate with no hedge cost and no stress.
- Extension options are assumed without testing the covenants that gate them.
- The waterfall's compounding, hurdle definition or fee base does not match the operating agreement.
- Annual periods are used on a short hold with heavy early capital, which misstates the returns.
- A typed number sits where a formula should be.

## 7. Reporting the result

Deliver the workbook with a short statement of how it was produced (which path), which tests passed, which need a reviewer's judgment, and every `[Assumed]` input. Never present a model as final. It is a draft for a qualified professional to review.
