# Metrics and formulas

Definitions used across the plugin. The workbook implements each one as a live formula.

## Income

| Metric | Formula |
|--------|---------|
| Gross potential rent (GPR) | Sum of market rent on all space, occupied or not |
| Loss to lease | GPR minus in-place contract rent on occupied space |
| Vacancy and credit loss | Physical vacancy plus concessions plus bad debt |
| Effective gross income (EGI) | GPR less loss to lease, vacancy, concessions and bad debt, plus other income and recoveries |
| Operating expenses | Controllable plus non-controllable (taxes, insurance), including management fee |
| Net operating income (NOI) | EGI minus operating expenses. Before reserves, capital, debt service and income tax |
| NOI after reserves | NOI minus replacement reserves |
| Cash flow before debt | NOI minus capital expenditures, tenant improvements and leasing commissions |

Management fee is a percent of EGI. Replacement reserves sit below NOI. On a sale, model property tax on the reassessed value where the jurisdiction reassesses.

## Value and yield

| Metric | Formula |
|--------|---------|
| Going-in cap rate | Year 1 NOI / purchase price |
| In-place cap rate | Trailing 12-month NOI, adjusted for known changes, / purchase price |
| Yield on cost | Stabilized NOI / total project cost |
| Exit value | NOI for the year after sale / exit cap rate |
| Net sale proceeds | Exit value less sale costs less loan balance |
| Price per unit or SF | Purchase price / units or rentable SF |
| Replacement cost check | Purchase price per unit or SF compared with cost to build new |

## Debt

| Metric | Formula |
|--------|---------|
| Loan to value (LTV) | Loan amount / value |
| Loan to cost (LTC) | Loan amount / total project cost |
| Debt service coverage (DSCR) | NOI / annual debt service |
| Debt yield | NOI / loan amount |
| Loan constant | Annual debt service / loan amount |
| Maximum loan | The lowest of the LTV, DSCR and debt yield tests |
| Positive leverage | Going-in cap rate greater than the loan constant |

State which test binds. Use lender NOI (after reserves and a market management fee) for sizing when the lender requires it.

## Returns

| Metric | Formula |
|--------|---------|
| Unlevered IRR | IRR of total cost out, cash flow before debt in, net sale value in |
| Levered IRR | IRR of equity out, cash flow after debt in, net sale proceeds in |
| Equity multiple | Total distributions / total equity invested |
| Cash on cash | Annual cash flow after debt / equity invested |
| Profit | Total distributions minus total equity invested |
| Maximum bid | Highest price at which levered IRR meets the firm's hurdle |

Annual models use IRR on year-end cash flows. Dated cash flows use XIRR. Say which.

## Returns attribution

Split levered profit into four sources:

1. NOI growth: change in NOI valued at the going-in cap rate
2. Cap rate movement: exit NOI valued at exit cap minus exit NOI valued at going-in cap
3. Cash flow during the hold
4. Leverage and amortization: the difference between levered and unlevered profit

If cap rate compression supplies most of the profit, flag it.

## Waterfall

| Term | Definition |
|------|------------|
| Preferred return | Return on unreturned capital at the stated rate, simple or compounding as the agreement says, paid before any promote |
| Return of capital | Contributed capital returned before promote tiers |
| Hurdle | The IRR (or multiple) an investor must reach before the next split applies |
| Promote | Share of profit paid to the sponsor above its pro rata share |
| Catch-up | Tier in which the sponsor receives a larger share until it reaches its target share of profit |
| Gross to net | Investor return after fees and promote. Always show both |

Distributions in every period must equal cash available. Each tier fills before the next starts.

## Lease metrics (commercial)

| Metric | Formula |
|--------|---------|
| WALT | Remaining lease term weighted by rent (state if weighted by SF instead) |
| Rollover exposure | Share of rent expiring in each year |
| Net effective rent | Present value of rent less free rent, TI and commissions, expressed per SF per year |
| Mark to market | Market rent / in-place rent minus 1 |
| Occupancy cost | Tenant rent and charges / tenant sales (retail) |

## Operating business metrics

| Metric | Formula |
|--------|---------|
| RevPAR (hotels) | Occupancy x average daily rate |
| GOP margin (hotels) | Gross operating profit / total revenue |
| FF&E reserve | Percent of revenue set aside for furniture, fixtures and equipment |
| Revenue per occupied unit (seniors) | Total resident revenue / occupied units |
| Economic occupancy (storage) | Collected rent / rent at street rates on all units |

## For-sale and development

| Metric | Formula |
|--------|---------|
| Absorption | Units or lots sold per period |
| Profit margin | (Net sale revenue minus total cost) / net sale revenue |
| Return on cost | Profit / total cost |
| Cost to complete | Remaining budget plus known overruns minus committed funding |
| Contingency remaining | Contingency budget minus contingency used, compared with percent complete |
