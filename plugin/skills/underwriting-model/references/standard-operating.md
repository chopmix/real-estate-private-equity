# Engine standard: operating-business properties

For hotels, seniors housing and self-storage. Read with `model-standard.md`. These assets earn income from running a business inside the building, so the model is part real estate and part operating company. These are the practices an experienced underwriter of operating assets expects. How the workbook implements them is open.

## Periods

- **Use monthly periods.** Seasonality, ramp-up and renovation displacement move cash and coverage month to month. Annual totals hide the months when coverage is thin and the reserve or the sponsor has to fund the gap.

## Revenue

- **Build revenue from drivers.** Hotels: occupancy, average daily rate and RevPAR by segment, plus food and beverage and other departments. Seniors housing: occupancy and monthly rate by care level, plus care fees and entrance or community fees. Storage: occupancy, rate by unit size and climate control, plus fees and insurance or protection income.
- **Respect the mix.** Segment, unit size and care level each move at their own pace. A blended rate hides shifts in mix that change margin.
- **Show seasonality** in the drivers, drawn from the property's own monthly history where it exists.
- **Ramp new or repositioned assets.** Occupancy and rate build over a stated period. Do not start at stabilized levels.
- **Seniors housing: care levels and payor mix.** Price each level of care separately. Separate private pay from government programs and insurance, with each payor's rate and collection risk. Changes in reimbursement rules are a flag for counsel.
- **Storage: street rate and in-place rate differ.** New customers move in at street rates, often discounted. Existing customers receive periodic rate increases. Model both, with move-out sensitivity to increases, and track the gap between in-place and street rates.

## Expenses

- **Departmental expenses follow their department.** Rooms, food and beverage, care, and other departments carry their own cost and margin.
- **Undistributed expenses sit below departmental profit**: administration, sales and marketing, maintenance, utilities, and technology. Then fixed charges: property tax, insurance and ground rent.
- **Separate fixed from variable costs.** Model labor by staffing levels where possible. Flow-through, the share of a revenue change that reaches profit, should look reasonable both when revenue rises and when it falls. A model that keeps margin flat in a downturn is wrong.
- **Wage pressure deserves its own driver** in labor-heavy assets such as seniors housing and full-service hotels.

## Fees, reserves and capital

- **Management fees come from the contract**: base fee on revenue, incentive fee on profit above a threshold, and any centralized service charges. Read termination terms and the cost to replace the manager.
- **Franchise and brand fees** follow the license: royalty, marketing and reservation fees, loyalty program charges.
- **The FF&E reserve is a real cost.** Deduct it in the cash flow as a share of revenue, or as the management or franchise agreement requires. Show NOI before and after it.
- **Property improvement plans are capital, with displacement.** Budget the plan, time it, and take rooms or units out of service while the work happens. A brand or license transfer can trigger one.

## Operator and license risk

- **Value depends on the operator.** Record the operator, the agreement's term, fees and termination rights. Test the cost and disruption of a change.
- **Licenses and approvals can be lost.** Seniors housing depends on state licensing. Hotels depend on the flag. Name what happens to revenue if either goes away, and flag the regulatory points for counsel.
- **Leased structures differ.** Where an operator leases the property, model the lease, the rent coverage at the operator level, and the operator's credit.

## Debt

- **Lenders size on trailing cash flow** after management fees and the FF&E reserve, often with an imputed management fee where the actual one is lower. Model the lender's view of cash flow.
- **Test coverage on a trailing basis every month** and show the weakest months. Seasonal dips can trip a cash management trigger even when the annual result looks safe.
- **Seasonal working capital** and any seasonality reserve the lender requires belong in sources and uses.

## Exit and returns

- **Capitalize forward NOI after the FF&E reserve and a market management fee**, as buyers of operating assets underwrite.
- **Reflect any capital the next buyer will need**, such as a property improvement plan due soon after the sale.
- **Returns follow `standard-unit.md`**: date-based IRR, equity multiple, cash on cash on operating cash only, and a waterfall matched to the operating agreement.

## Checks specific to this engine

| Check | Passes when |
|-------|-------------|
| Driver tie | Revenue equals occupancy times rate times available units or rooms, by segment or level |
| Trailing tie | Year-zero monthly revenue and expenses equal the trailing operating statements |
| Seasonality | Modeled monthly pattern matches history, or the change is explained |
| Flow-through | Profit change over revenue change is reasonable in both up and down cases |
| Fees | Management, incentive and franchise fees match the contracts |
| Reserve | FF&E reserve is deducted every period and appears before value and coverage |
| Coverage | Trailing coverage is tested each month, and the weakest month is shown |
| Storage rates | In-place and street rates are tracked separately with a move-out effect on increases |
