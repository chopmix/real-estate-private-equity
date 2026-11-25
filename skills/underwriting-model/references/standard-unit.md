# Engine standard: unit-based properties

For multifamily, student housing, single-family rental, manufactured housing and affordable housing. Read with `model-standard.md`. These are the practices an experienced multifamily underwriter expects. How the workbook implements them is open.

## Revenue

- **Track renovated and unrenovated units separately.** Unrenovated units grow at organic rent growth. Renovated units earn market rent plus the renovation premium. A single blended rent hides whether the plan is working.
- **Build rent from the unit mix**, by unit type: count, size, in-place rent, market rent, premium and renovation pace.
- **Loss to lease moves.** It falls as renovated units lease at market and can widen when market rent grows faster than leases turn.
- **Renovation downtime is vacancy.** Units offline during renovation earn nothing. Show it apart from general vacancy.
- **Show the full path from potential rent to collected income**: loss to lease, vacancy, non-revenue units, concessions and write-offs, then utility reimbursements and other income, each on its own line.
- **Other income is underwritten, not assumed.** New fee income needs an adoption rate and a ramp.

## Expenses

- **Reassess property tax.** At purchase, where the jurisdiction reassesses, tax follows the purchase price, the assessment ratio and the tax rate. At exit, the buyer faces the same reset, which affects the price they can pay.
- **Management fee is a percent of effective gross income**, at a market rate for the property's size, even if the owner self-manages.
- **Trend insurance on its own line.** Never hold it flat or fold it into general expense growth.
- **Separate controllable from non-controllable expenses.** Payroll, repairs, marketing and administration respond to management. Taxes and insurance do not.
- **Replacement reserves sit below NOI.** They are not an operating expense, and they are always in the cash flow.
- **Normalize the trailing statement** before projecting: remove one-time items and bring payroll, contracts and utilities to a full-year run rate.

## Capital

- **Renovation budget by scope**, with cost per unit, unit count and schedule. Include exterior and common-area work, soft costs, contingency and any construction management fee.
- **Tie spend to pace.** Capital goes out as units are renovated, and premiums start after the unit re-leases.
- **Fund it explicitly**: from the loan, from equity at close, or from cash flow. Show which, and what happens if cash flow falls short.

## Debt

- **Model the loan the deal will actually have.** Bridge loans float over an index with a spread and often a floor. Include the cost of the rate cap and stress the rate.
- **Show the interest-only period and the step up** to amortizing payments when it ends.
- **Size to every test the lender applies**, on the lender's NOI, and state which test binds. Bridge lenders usually size to cost. Agency and bank lenders size to value and coverage.
- **Test extension options** against their coverage and debt yield conditions, on the business plan and on the downside.
- **Model the takeout.** A bridge plan depends on refinancing or selling into permanent debt. Size that loan on stabilized NOI at a stressed rate.

## Returns

- **Use date-based returns** (XIRR) when cash flows are dated, and monthly periods for any value-add plan.
- **Equity multiple is total distributions over total equity invested.**
- **Cash on cash is operating cash flow after debt service over equity invested.** Sale proceeds are excluded.
- **The waterfall fills one tier before the next begins.** Match the preferred return's compounding and the hurdle definitions to the operating agreement.

## Exit

- **Capitalize the year after the sale.** A five-year hold values year six NOI, after reserves when that is how buyers in the market underwrite.
- **Do not assume a lower cap rate at exit than at purchase** without evidence. Conservative practice holds it flat or widens it.
- **Deduct every sale cost**: brokerage, closing and transfer costs, and any disposition fee.

## Checks specific to this engine

| Check | Passes when |
|-------|-------------|
| Unit count | Renovated plus unrenovated units equal total units every period |
| Rent roll tie | Modeled in-place rent equals the rent roll total at the start date |
| Trailing tie | Year-zero income and expenses equal the normalized trailing statement |
| Renovation budget | Capital spent equals cost per unit times units renovated, plus other scope |
| Occupancy | Physical and economic occupancy stay within bounds and are consistent with each other |
| Premium | Achieved premium is supported by renovated comparables, not by the broker's figure |
