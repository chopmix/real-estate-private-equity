# Engine standard: for-sale housing

For condominiums, townhomes, for-sale single-family homes and finished lots. Read with `model-standard.md`, and with `standard-development.md` for the budget, schedule and construction funding. These projects earn their profit from sales, so there is no exit cap rate. These are the practices an experienced homebuilding underwriter expects. How the workbook implements them is open.

## Pricing

- **Price by unit or by product type.** Plan, size, floor, view, lot premium and options each carry value. A single price per square foot across the project hides which units carry the margin.
- **Support base prices with comparables** of the same product and buyer, adjusted for location, finish and timing.
- **Escalate prices only with evidence.** If prices rise over the sellout, state the rate and the reason, and run a case with none.
- **Model incentives on their own line**: price reductions, closing cost help, rate buydowns, and upgrades given away. Report gross and net prices.

## Absorption and presales

- **Set a sales pace** in units per month, by product type and phase, supported by comparable projects and the depth of the buyer pool. Pace usually slows at the end of a sellout.
- **Presales come before construction for many condo projects** and may be required by the lender. Show the presale count and pace before the loan funds.
- **Sales, contracts and closings are separate events.** A contract today closes later, often after completion or certificate of occupancy. Revenue arrives at closing.
- **Allow for contract cancellations**, and model what happens to deposits when buyers walk away.

## Deposits

- **Deposits have rules.** Local law and the contracts may hold them in escrow, limit their use for construction, or require their return. Model only what the project may actually use, and when. Flag deposit rules for counsel.
- **Show deposits as a funding source** only to the extent they are released for use.

## Costs

- **Budget by phase and product**, following `standard-development.md`: land, horizontal and vertical hard costs, soft costs, financing and contingency.
- **Sales and marketing costs**: sales office or model, brokerage commissions, marketing, and closing costs paid by the seller. Commissions are paid at closing.
- **Carry costs for unsold inventory**: taxes, insurance, association dues on unsold units, and maintenance. These grow if pace slows.
- **Warranty reserves** and the cost of post-closing claims. Flag construction defect exposure for counsel.

## Phasing

- **Phase work and sales together.** Start a new phase when the prior phase hits a stated sales level, so capital is not committed ahead of demand.
- **Model phase-level profit and cash**, as well as the project total.

## Debt

- **Model the construction loan with release prices.** Each closing repays the loan by a set amount or share of price before any cash comes back to equity. Release terms often require repaying the loan faster than the sellout.
- **Show the loan paying down from closings** and the date it is fully repaid.
- **Lot and land loans** follow the same release logic where they apply.

## Returns and metrics

- **Profit margin and return on cost are the core metrics.** Profit margin is profit over net sale revenue. Return on cost is profit over total cost. Report both, by phase and in total.
- **Show peak equity, the time to peak, and the time to return all capital.**
- **Report dated IRR and equity multiple** as well, with the waterfall matched to the operating agreement.

## Downside and fallback

- **Sensitize pace, price and cost**, alone and together. A slower pace raises carry and interest at the same time price may soften.
- **Model a fallback case.** If sales stall, what does the project earn as a bulk sale of remaining units at a discount, or as a rental? For rental, apply `standard-unit.md` and check whether the loan and the condo documents allow it.
- **Show breakevens**: the price cut and the pace that erase profit, and the point where closings no longer repay the loan on time.

## Checks specific to this engine

| Check | Passes when |
|-------|-------------|
| Unit count | Sold plus unsold units equal total units every period |
| Revenue tie | Closing revenue equals units closed times net price, by product type |
| Timing | Every closing falls after the completion of its unit or phase |
| Deposits | Deposits used never exceed deposits released for use |
| Release prices | Loan repayment at each closing meets the release terms, and the loan is fully repaid |
| Carry | Carry costs on unsold units rise when pace slows |
| Metrics | Profit margin and return on cost use net revenue and total cost as defined |
| Fallback | A bulk sale or rental case is shown with its returns |
