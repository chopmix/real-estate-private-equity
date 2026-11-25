# Deal input schema

One JSON file per deal. `repe_model.py` builds the workbook from it and `repe_calc.py` recalculates it. Fields marked Req are required. Anything left out takes the default and is tagged `[Assumed]` on the Inputs sheet. Scenario drivers take one number or `[base, upside, downside]`. Years count from 1 (first year of ownership). Rates are decimals (0.05 = 5%).

## Top level

| Field | Type | Req | Default | Meaning |
|-------|------|-----|---------|---------|
| deal_name | text | | Deal | Name shown on Summary |
| property_type | text | | | Playbook name, for example multifamily, office, hotel |
| engine | text | Req | | `unit`, `lease` or `operating` |
| scenario | text | | Base | Base, Upside or Downside |
| hold_years | integer | | 5 | 1 to 10. Sale at end of hold on next-year NOI |
| source_tags | object | | | Field name to tag, for example `{"exit_cap": "[Assumed]"}`. Fields given without a tag are `[User]` |
| sources | list | | | `{document, type, date, note}` rows for the Sources sheet |

## acquisition

| Field | Type | Req | Default | Meaning |
|-------|------|-----|---------|---------|
| purchase_price | $ | Req | | Contract price |
| closing_cost_pct | rate | | 0 | Closing costs as share of price |
| upfront_capex | $ | | 0 | Capital funded with equity at close |
| trailing_noi | $ | | 0 | Trailing 12-month NOI. Shown as Year 0 and tied in Checks |

## assumptions

| Field | Type | Req | Default | Meaning |
|-------|------|-----|---------|---------|
| rent_growth | scenario | | 0.03 | Annual growth of rents, market rents and rates |
| expense_growth | scenario | | 0.03 | Annual growth of expenses, taxes, insurance, recoveries, TI and LC |
| exit_cap | scenario | Req | | Cap rate on next-year NOI at sale |
| vacancy | scenario | | 0.05 | unit: physical vacancy. lease: general vacancy and credit loss |
| occupancy_adjustment | scenario | | 0 | operating only: points added to the occupancy schedule |
| sale_cost_pct | rate | | 0.02 | Sale costs as share of exit value |

## unit (engine `unit`)

| Field | Type | Req | Default | Meaning |
|-------|------|-----|---------|---------|
| unit_mix[].type | text | | Unit | Unit type label |
| unit_mix[].count | number | Req | | Units of this type |
| unit_mix[].sf | number | | 0 | SF per unit (reference only) |
| unit_mix[].in_place_rent | $/month | Req | | Average contract rent per unit, Year 1 |
| unit_mix[].market_rent | $/month | Req | | Market rent per unit, Year 1 |
| unit_mix[].renovation_premium | $/month | | 0 | Premium over market after renovation |
| unit_mix[].renovations_per_year | number | | 0 | Units renovated per year until all are done |
| unit_mix[].renovation_cost_per_unit | $ | | 0 | Paid in the year of renovation |
| unit_mix[].source | tag | | [User] | Source tag for the row |
| concessions_pct | rate | | 0 | Share of net potential rent |
| bad_debt_pct | rate | | 0 | Share of net potential rent |
| other_income | $ | | 0 | Year 1 other income, grows with rents |
| loss_to_lease_burnoff_years | number | | 1 | Years for classic rents to reach market |

## lease (engine `lease`)

| Field | Type | Req | Default | Meaning |
|-------|------|-----|---------|---------|
| tenants[].name | text | | Tenant | Label only. Use a placeholder, not the real tenant name, in shared files |
| tenants[].sf | number | Req | | Leased SF |
| tenants[].rent_psf | $/SF/yr | Req | | Contract rent, Year 1 |
| tenants[].annual_bump | rate | | 0 | Annual increase, also used on the rollover lease |
| tenants[].expiry_year | integer | Req | | Lease ends at the end of this year. 12 or more means no rollover in the model |
| tenants[].renewal_probability | rate | | 0.6 | Weight on renewal versus a new tenant |
| tenants[].downtime_months | number | | 6 | Months vacant if a new tenant is needed (max 12) |
| tenants[].market_rent_psf | $/SF/yr | Req | | Market rent, Year 1 |
| tenants[].ti_new_psf, ti_renewal_psf | $/SF | | 0 | Tenant improvements, in Year 1 dollars |
| tenants[].lc_new_psf, lc_renewal_psf | $/SF | | 0 | Leasing commissions, in Year 1 dollars |
| tenants[].recovery_psf | $/SF/yr | | 0 | Expense recoveries, Year 1 |
| vacant_suites[].name, sf | text, number | sf Req | | Vacant space to lease up |
| vacant_suites[].market_rent_psf | $/SF/yr | Req | | Market rent, Year 1 |
| vacant_suites[].lease_up_year | integer | | 1 | First year of rent |
| vacant_suites[].annual_bump | rate | | 0 | Annual increase after lease-up |
| vacant_suites[].ti_new_psf, lc_new_psf, recovery_psf | $/SF | | 0 | As for tenants |
| other_income | $ | | 0 | Year 1 parking and other income, grows with rents |

## operating (engine `operating`)

| Field | Type | Req | Default | Meaning |
|-------|------|-----|---------|---------|
| keys | number | Req | | Rooms, beds or units |
| rate | $ | Req | | Rate per occupied unit per day or month, Year 1 |
| rate_basis | text | | day | `day` (x365) or `month` (x12) |
| occupancy | list | Req | | Occupancy by year from Year 1. The last value repeats |
| other_revenue_pct | rate | | 0 | Other revenue as share of unit revenue |
| departmental_expense_pct | rate | | 0 | Share of total revenue |
| undistributed_expense_pct | rate | | 0 | Share of total revenue |
| ffe_reserve_pct | rate | | 0.04 | FF&E reserve, share of total revenue, below NOI |

## expenses

| Field | Type | Req | Default | Meaning |
|-------|------|-----|---------|---------|
| items[].name, amount | text, $ | Req | | Year 1 expense line |
| items[].growth | rate | | expense growth | Own growth rate for the line |
| management_fee_pct | rate | | 0.03 | Share of EGI |
| property_tax.reassess | true/false | | false | Reset tax to price x assessment ratio x tax rate |
| property_tax.current_tax | $ | | 0 | Year 1 tax when not reassessed |
| property_tax.assessment_ratio | rate | | 1.0 | Assessed value as share of price |
| property_tax.tax_rate | rate | | 0 | Tax as share of assessed value |
| insurance | $ | | 0 | Year 1, grows with expenses |
| replacement_reserves | $ | | 0 | Year 1, below NOI (unit and lease engines) |
| capex_schedule | list of $ | | zeros | Capital by year from Year 1, paid from cash flow |

## debt

| Field | Type | Req | Default | Meaning |
|-------|------|-----|---------|---------|
| mode | text | | sized | `sized` (lowest test) or `stated` |
| stated_amount | $ | | 0 | Loan amount in stated mode |
| max_ltv | rate | | 0.65 | LTV test on price |
| min_dscr | number | | 1.25 | DSCR test on Year 1 NOI after reserves, amortizing constant |
| min_debt_yield | rate | | 0.08 | Debt yield test on Year 1 NOI after reserves |
| rate | rate | | 0.06 | Fixed annual interest rate |
| io_years | integer | | 0 | Interest-only years |
| amort_years | integer | | 30 | Amortization. 0 means interest only throughout |
| loan_fee_pct | rate | | 0.01 | Share of loan, funded at close |

## waterfall

| Field | Type | Req | Default | Meaning |
|-------|------|-----|---------|---------|
| investor_share | rate | | 0.9 | Investor share of equity. Sponsor co-invests the rest |
| pref_rate | rate | | 0.08 | Preferred return, compounding annually on unreturned capital |
| tiers[] | list | | none | Up to three `{hurdle, promote}`. Promote applies to cash between the prior hurdle and this one |
| final_promote | rate | | 0.2 | Promote above the last hurdle (or above the pref if no tiers) |
| acquisition_fee_pct | rate | | 0 | Share of price, funded by equity at close |
| asset_management_fee_pct | rate | | 0 | Share of property equity, per hold year |
| disposition_fee_pct | rate | | 0 | Share of exit value |

## returns and sensitivity

| Field | Type | Req | Default | Meaning |
|-------|------|-----|---------|---------|
| returns.hurdle_irr | rate | | 0.15 | Firm levered IRR hurdle for the maximum bid |
| sensitivity.exit_cap_step | rate | | 0.0025 | Grid step for exit cap |
| sensitivity.noi_step | rate | | 0.05 | Grid step for NOI versus plan |
| sensitivity.price_step | rate | | 0.05 | Grid step for purchase price |
| sensitivity.rate_step | rate | | 0.005 | Step for interest rate rows |
| sensitivity.ladder_low | rate | | -0.15 | First price ladder step versus price |
| sensitivity.ladder_step | rate | | 0.025 | Ladder step (nine steps) |
