# Playbook: Affordable Housing

Engine: `unit`. Rents and tenant incomes are limited by program rules, so the model is a unit mix with restricted rents. Every program point here is flagged for counsel or a CPA.

## 1. What it is

| Subtype | Description | Underwriting focus |
|---------|-------------|--------------------|
| LIHTC (Low-Income Housing Tax Credit) | Credits fund construction or rehab, with rent and income limits | Compliance period, credit recapture, restricted rents |
| Section 8 project-based | Federal subsidy contract tied to the building | Contract term, renewal, rent adjustments |
| Housing choice voucher mix | Tenants hold vouchers on market-based buildings | Voucher rent limits, inspection, payment delays |
| Regulatory agreement or deed restriction | Local or state restrictions tied to financing or land | Term, rent limits, resale limits |
| Naturally occurring affordable (NOAH) | Older units that rent below market without restriction | Rent growth pressure, capital need, displacement rules |
| Mixed-income | Market and restricted units in one building | Unit allocation, compliance tracking |

## 2. How income is produced

- Rent from tenants, capped by program limits based on area median income.
- Subsidy payments from housing authorities for voucher and project-based units, usually paid monthly.
- Income is stable but capped. Growth follows published limits, not the market.
- Engine inputs: unit types, counts, SF, restricted and market rent, subsidy, income tier, pace of renovation.

## 3. Key metrics

| Metric | How to compute | Why it matters |
|--------|----------------|----------------|
| Maximum allowable rent | Program limit by unit size and income tier, less utility allowance | Cap on gross rent |
| Rent headroom | Maximum rent / in-place rent minus 1 | Shows room to raise or overpricing risk |
| Restricted share | Restricted units / total units | Drives income and exit buyer pool |
| Subsidy share of rent | Subsidy payments / total rent | Dependence on contract renewal |
| Remaining affordability term | Years left on the agreement or compliance period | Sets the hold and exit path |
| Economic occupancy | Collected rent / GPR | Delays in subsidy hit collections |
| Debt coverage including soft debt | NOI / all required debt payments | Soft debt may bind, even if deferred |
| Credit equity per unit | Tax credit equity / units | Capital stack check for new or rehab deals |
| Utility allowance gap | Allowance vs actual cost | Affects the net rent collected |

## 4. Revenue drivers

- Annual changes to income and rent limits.
- Subsidy contract rent adjustments and renewal outcomes.
- Voucher payment standards and housing authority timing.
- Occupancy, with a waitlist as a leading signal.
- Compliance with income certification, which keeps units eligible.
- Other income, limited by program rules.
- For mixed income, the market rent premium on unrestricted units.

## 5. Expense drivers

- Property tax: check exemptions or abatements tied to affordability, their term and what happens on sale. Flag for counsel or CPA.
- Insurance: standard multifamily factors, plus lender-required coverage.
- Compliance: certification staff, inspections, monitoring fees, annual reporting, third-party audits.
- Payroll, utilities, repairs and turn. Rehab units may need more repair.
- Asset management and partnership fees paid to investors or sponsors.
- Replacement reserves and operating reserves often required by investors and lenders.
- Management fee, with program limits on fee levels.

## 6. Capital needs

- Rehab scope funded at closing, with credit or soft loan proceeds.
- Accessibility upgrades, life safety and code items.
- Replacement reserves per unit, often above market minimums.
- Operating reserve and lease-up reserve.
- Energy and utility retrofits, which can also reduce expense.
- Capital at the end of the compliance period for refinance or recapitalization.

## 7. Debt and lender view

- Lenders: agency lenders (Fannie Mae, Freddie Mac), HUD/FHA, banks, state housing finance agencies, tax-exempt bond issuers. See program-overlays.md.
- Usually binding test: DSCR on restricted rents. Soft debt and residual receipts loans can bind the total debt picture.
- Quirks: subordinate loans with cash flow sweeps, use agreements, recorded restrictions that survive foreclosure, replacement reserve requirements, bond covenants.
- Lenders size on restricted rents, not market rents. Do not mix them.

## 8. Screening quick tests

- Maximum allowable rent against in-place rent and against the model rent.
- Remaining affordability term against hold period.
- Subsidy contract term and renewal history.
- Debt coverage including all soft debt and fees.
- Exit buyer pool: who buys restricted assets and at what cap rate range, from broker opinion and recent trades. Label as opinion.
- Required rehab against funding sources.
- Tax exemption status and what happens on sale.

## 9. Diligence additions

- Regulatory agreement, use restriction, extended use agreement, and any amendments. Counsel to read.
- Latest compliance audit and state agency monitoring reports.
- Tenant files: sample of income certifications, recertifications and unit eligibility.
- Rent roll showing restricted versus unrestricted units, income tier and rent.
- Utility allowance schedule and its date.
- Subsidy contracts: term, rent adjustment method, expiry and renewal rules.
- Physical inspection scores and open findings.
- Tax credit documents, partnership agreement, and investor consent requirements. CPA and counsel to review.
- Property tax exemption or abatement documents. Counsel and CPA to review.
- Any right of first refusal, purchase option, or consent right held by a nonprofit, agency, or investor.

## 10. Red flags

- Rents above the maximum allowable rent on any restricted unit.
- Missing or stale income certifications.
- Compliance findings or uncorrected inspection issues.
- Subsidy contract near expiry with no renewal plan.
- Soft debt due or accruing interest with no repayment plan.
- Partnership consent or transfer rights that block a sale or refinance.
- Tax exemption that ends or is lost on sale.
- Utility allowance out of date.
- Unit vacancy held for tenant eligibility reasons with no waitlist.
- Seller who treats the restrictions as expiring without documents to show it.

## 11. Value levers

- Fix compliance and tenant file quality to protect eligibility and credits.
- Raise rents to the maximum allowable where tenants can pay.
- Refinance existing debt where terms and use agreements allow.
- Retrofit utilities and reduce operating expense.
- Add or convert units to mixed income where permitted.
- Buy at the end of a compliance period with a plan for recapitalization.

## 12. Local intelligence

- Reviews: read for maintenance response, inspection issues, safety and management treatment of tenants. Track trends. Do not name residents or staff.
- Housing agency data: waitlists, voucher payment standards, awards of credits, and agency policy changes.
- New supply: planned affordable and market projects, including those using credits or bonds.
- Employer news: wage trends that move area median income and tenant ability to pay.
- Public data: HUD income and rent limit tables, inspection scores, county tax records, local housing plans.

## 13. Model inputs to capture

- Unit types: count, SF, income tier, maximum rent, in-place rent, market rent for unrestricted units.
- Utility allowance by unit type.
- Subsidy payments, contract term and adjustment method.
- Vacancy, concessions, bad debt, and subsidy payment delays.
- Other income allowed under program rules.
- Expense lines: taxes, insurance, compliance, payroll, utilities, repairs, administrative, management fee, asset management fees.
- Tax exemption terms and reassessment value at exit.
- Reserves: replacement and operating, per unit.
- Growth in limits by year. Exit cap and sale costs with restricted rents.
- All debt, including soft debt, accruing interest and repayment triggers.

## 14. Site visit and management questions

- Walk units and common areas. Review inspection findings.
- Show the tenant file process and who signs off on certifications.
- How many units turned over this year and how long were they vacant?
- How is the waitlist managed and how old is it?
- How are subsidy payments tracked and how late are they?
- What is the status of the last compliance audit?
- What does the utility allowance schedule look like?
- What repair items come up most often?
- Who must consent to a sale or refinance?
- What changes would you make to improve rent collection and tenant stability?
