# Playbook: Multifamily

Engine: `unit`. Income comes from many short leases on apartment units, so the model is a unit mix with a renovation program, not a tenant roll.

## 1. What it is

| Subtype | Description | Underwriting focus |
|---------|-------------|--------------------|
| Garden | Low-rise, surface parking, often 1960s to 2000s | Renovation premium, deferred capital, tax reassessment |
| Mid-rise and high-rise | Elevator buildings, structured parking | Operating cost per unit, concessions, lease-up risk |
| Townhome and walk-up | Small buildings, often older | Plumbing and electrical age, unit-level capital |
| Lease-up (new build) | Newly delivered, not stabilized | Absorption pace, concession burn, cost to stabilize |
| Value-add | Class B or C with renovation upside | Premium achieved, pace, tenant turnover |
| Mixed use | Apartments over ground-floor retail | Retail rollover, split lender view |

## 2. How income is produced

- Rent from 6 to 15 month leases, billed monthly. Rolling expirations let rent reset to market within a year.
- Other income: fees, utility reimbursement (RUBS), parking, pet, storage, laundry, cable or internet bulk deals.
- Income is cash collected from many small payers. Credit risk is diffuse, so collections quality matters more than tenant credit.
- Engine inputs: unit types, counts, SF, in-place and market rent, renovation premium and pace.

## 3. Key metrics

| Metric | How to compute | Why it matters |
|--------|----------------|----------------|
| Economic occupancy | Collected rent / GPR | Physical occupancy hides concessions and bad debt |
| Loss to lease | GPR less in-place rent on occupied units | Shows mark-to-market upside or overstated market rents |
| Renovation premium | Renovated rent less unrenovated rent, same unit type | Core of the value-add return |
| Return on renovation cost | Annual premium / cost per unit | Test each unit scope on its own |
| Turnover rate | Move-outs / total units, trailing 12 months | Drives downtime, make-ready cost and pace |
| Expense per unit | Operating expenses / units, by line | Compare with comps and the T-12 trend |
| Controllable expense ratio | Controllable lines / EGI | Shows management efficiency |
| Price per unit and per SF | Price / units or SF | Compare with replacement cost |
| Renewal conversion | Renewals / expiring leases | Retention against renewal rent growth |

## 4. Revenue drivers

- Market rent growth, tied to jobs, household formation and new supply.
- Renovation premium and the pace at which units turn and get renovated.
- Concessions and how fast they burn off or build up.
- Renewal versus new-lease rent spread.
- Other income programs (RUBS, fees, parking, bulk internet) and legal limits on each.
- Occupancy, bad debt and eviction timelines in the jurisdiction.

## 5. Expense drivers

- Property tax: model reassessment on the purchase price where the jurisdiction reassesses on sale. Check appeal history and the millage trend.
- Insurance: age, roof, wiring, coastal or hail exposure, and claims history. Quotes beat trailing actuals.
- Payroll: onsite staff count versus unit count. Check whether the T-12 runs short-staffed.
- Utilities: how much is billed back versus owner-paid. Check vacant-unit and common-area load.
- Repairs, turnover and make-ready, contract services, marketing, administrative.
- Management fee: model market fee on EGI even if the seller self-manages.

## 6. Capital needs

- Replacement reserves per unit, above the lender minimum if the asset is old.
- Unit renovation scope, by unit type, with cost and downtime.
- Building systems: roofs, HVAC, plumbing risers, boilers, elevators, parking and paving, balconies.
- Amenity upgrades, tested against the rent they actually support.
- Life-safety and code items, including fire alarm and sprinkler status.

## 7. Debt and lender view

- Lenders: agency (Fannie Mae, Freddie Mac), HUD/FHA, banks, debt funds, life companies, CMBS. See program-overlays.md.
- Usually binding test: DSCR for stabilized assets with agency debt. Debt yield binds for banks and debt funds on value-add.
- Lender NOI uses a market management fee, reserves and often a vacancy floor.
- Structural quirks: interest-only periods, supplemental loans, floating rate caps, earn-outs tied to renovation, replacement reserve and repair escrows, prepayment cost.

## 8. Screening quick tests

- Price per unit against replacement cost per unit.
- Going-in cap against the loan constant. Flag negative leverage.
- Renovation premium against the premium already achieved on the property or a comp.
- Yield on cost after renovation against exit cap plus a spread of your choice.
- Rent growth needed to hit the hurdle. Fail the deal if growth above trend is required.
- Reassessed tax on the purchase price against the T-12 tax.

## 9. Diligence additions

- Unit-level rent roll, with lease start, expiry, concessions, deposits and delinquency.
- Matching rent roll to bank deposits for a sample of months.
- Physical inspection of a sample of units, including unrenovated and down units.
- Renovation proof: leases on renovated units, dates, and time to lease.
- Utility bills and RUBS recovery. Check legality and tenant pushback.
- Property condition report plus own engineer review for roofs, plumbing and structure.
- Insurance quote and loss runs. Tax bills, appeals and reassessment rules.
- Service contracts, especially termination terms and bulk internet agreements.
- Fire marshal, code violation and open permit searches.

## 10. Red flags

- Rent roll does not tie to deposits or the T-12.
- Many units "down" for long periods, or model units used for marketing.
- Concessions recorded as lower rent, hiding true market rent.
- Delinquency above normal with weak eviction follow-through.
- Seller rent comps are all new product against an older asset.
- Deferred capital kept off the capital plan (roofs, risers, paving).
- Expense lines far below comps, especially payroll, insurance and repairs.
- Heavy turnover with falling review scores and rising complaints.
- Large new supply delivering within 3 miles during the hold.
- Renovation premium shown only on a handful of units.

## 11. Value levers

- Renovate units at a tested premium and pace.
- Fix management, collections and turnover time.
- Add or correct other income (RUBS, fees, parking, pet, internet).
- Reduce expense: insurance marketplace, tax appeal, utility retrofits, bulk contracts.
- Reposition or rebrand a property with a weak reputation.
- Lease-up and concession management on new product.
- Refinance into agency or HUD debt after stabilization.
- Buy below replacement cost with a plan to hold through cycles.

## 12. Local intelligence

- Online reviews: read for patterns in maintenance response, management behavior, safety, pests and noise. Track score trends over 24 months. Do not name staff or reviewers.
- New supply: city permit filings, planning agendas, and developer announcements within the submarket.
- Employer news: hiring, layoffs, relocations and major expansions near the property.
- Public data: Census and BLS for jobs and households, county tax records, code enforcement, crime maps.
- Broker market reports are opinion. Cross-check with property-level listings and concessions advertised.
- Walk the competing set and note advertised concessions and rents.

## 13. Model inputs to capture

- Unit types: count, average SF, in-place rent, market rent, by type.
- Renovation program: units per year, cost per unit, premium, downtime months.
- Vacancy, concessions, bad debt, by year. Renewal rate and turnover.
- Other income by line, with a note on what is legal and recurring.
- Expense lines: taxes, insurance, payroll, utilities, repairs and maintenance, turnover, contract services, marketing, administrative, management fee.
- Tax reassessment value, millage rate and growth cap.
- Replacement reserves per unit. Capital plan by year.
- Rent and expense growth, by year. Exit cap rate and sale costs.
- Debt terms: rate or index plus spread, IO months, amortization, fees, escrows.

## 14. Site visit and management questions

- Walk every building and a sample of units, including down and unrenovated units.
- Ask how many units are down and why.
- Ask the time from move-out to lease on renovated and unrenovated units.
- What are the top five resident complaints?
- What is the eviction process and average time?
- Which vendors are on contract and what are the termination terms?
- What did the last renovated units lease for, and when?
- How are prices set, and who approves concessions?
- Which capital items has the owner deferred?
- Review the shopping of competing properties and compare amenities and service levels.
- Ask staff how long they have been there and what they would fix first.
