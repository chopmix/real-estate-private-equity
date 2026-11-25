# Engine standard: development and heavy redevelopment

For ground-up construction and redevelopment large enough that the asset produces little or no income during the work. Read with `model-standard.md`, and with the engine standard for the stabilized asset (`standard-unit.md`, `standard-lease.md` or `standard-operating.md`). For-sale projects use `standard-for-sale.md`. These are the practices an experienced development underwriter expects. How the workbook implements them is open.

## Periods and schedule

- **Use monthly periods** from land closing through stabilization or sale.
- **Build the schedule in phases**: entitlement and design, pre-construction, construction, lease-up, and stabilization. Each phase has a start, a duration and the event that ends it.
- **Drive cost and revenue timing from the schedule.** Moving a date moves every cash flow tied to it, without rewriting formulas.

## Budget

- **Budget by category**: land and closing costs, hard costs, soft costs (design, permits, fees, legal, insurance, taxes during construction, marketing), financing costs, contingency and developer fee.
- **Source each line.** A contractor's bid or guaranteed maximum price, a cost estimate, or an assumption. Show which, and what is excluded from any contract.
- **Spend each category on a curve** that fits it. Land closes up front. Hard costs follow a construction curve. Some soft costs front-load, others trail.
- **Carry hard and soft contingency separately**, sized to how complete the design and pricing are. Add cost escalation for work not yet bought out.
- **Developer fee is a cost of the project.** State its base, timing and whether any of it is deferred or subordinated.

## Funding

- **Model the order of funding.** Equity usually goes in first, up to the required amount, then the construction loan funds the rest. Mezzanine or preferred equity sits between, with its own terms.
- **Accrue interest on the drawn balance**, at the floating rate with any floor and hedge cost. Interest is part of project cost.
- **Interest creates a loop**: interest depends on the loan balance, which depends on cost, which includes interest. Solve it transparently: a tested iterative calculation, a closed-form estimate, or a funded interest reserve sized with a stated method. Show that the loop converges and that the method is switchable.
- **Size the interest reserve** to carry the loan through construction and lease-up until income covers interest, and test it against a delay.
- **Size the construction loan to cost** and also to the stabilized value and coverage the lender will test. Show which test binds.
- **Record guarantees**: completion, carry or interest, and repayment, with who gives them and when they burn off. Flag guarantee terms for counsel.

## Lease-up and stabilization

- **Model absorption** at a stated pace by unit type or space, starting at certificate of occupancy or delivery of each phase.
- **Include concessions, leasing costs and marketing** during lease-up. Early leases often price below the stabilized rent.
- **Operating expenses start before income.** Staff, utilities, insurance and taxes begin as space delivers.
- **Define stabilization** as a measurable test, such as occupancy held for a stated period, and use the same definition for the takeout, the sale and any promote.

## Exit and takeout

- **Model the takeout or sale at stabilization.** Size a permanent loan on stabilized NOI at a stressed rate, or value the sale on forward stabilized NOI.
- **Compare yield on cost with the market cap rate.** The spread between them is the reward for development risk. A thin spread is a finding, whatever the IRR says.
- **Do not assume cap rate compression** at completion without evidence.

## Tracking and sensitivities

- **Track cost to complete** for projects underway: budget, committed, spent, remaining, contingency remaining compared with percent complete.
- **Sensitize the four drivers that break developments**: hard cost, schedule delay, rent or price, and exit cap rate. Show combined cases, such as a delay that also pushes the exit into a weaker market.
- **Show breakevens**: the cost overrun and the delay that erase the profit, and the rent that still covers the takeout loan.

## Returns

- **Report project-level and equity returns** on dated cash flows, with peak equity, the time to peak and the time to return capital.
- **Returns follow `standard-unit.md`** for definitions and the waterfall.

## Checks specific to this engine

| Check | Passes when |
|-------|-------------|
| Budget tie | Sum of monthly spend by category equals the budget by category |
| Funding tie | Equity plus loan draws plus other sources equal cost every month |
| Funding order | Loan draws begin only after the required equity is in |
| Interest | Interest equals rate times drawn balance each month, and the loop converges |
| Loan limit | Draws never exceed the commitment, and the binding sizing test is shown |
| Reserve | Interest reserve does not run out before income covers interest, in base and delay cases |
| Stabilization | One definition is used for takeout, sale and promote |
| Spread | Yield on cost and the market cap rate are both shown, with the spread |
