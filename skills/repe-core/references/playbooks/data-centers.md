# Playbook: Data Centers

Engine: `lease` (lease-by-lease). Read with `metrics-and-formulas.md` and `standards.md`.

## 1. What it is

| Subtype | Description | Main risk |
|---------|-------------|-----------|
| Hyperscale / wholesale | Large powered halls leased to a few large tenants | Tenant concentration, power delivery |
| Retail colocation | Cabinets and cages for many customers | Churn, power cost, cooling |
| Edge | Smaller sites near users | Small scale, tenant quality |
| Powered shell | Building plus utility power, tenant builds the interior | Tenant credit, delivery timing |
| Build-to-suit / development | Built for a named tenant | Construction, power, lease terms |

## 2. How income is produced

- Lease by lease, priced by power (kilowatts or megawatts) as much as by SF.
- Structures: NNN with power passed through, or fixed rate per kW. Know who pays power and who bears cost overruns.
- Long terms with fixed bumps for hyperscale. Retail colocation uses shorter terms and rate cards.
- Rent may ramp as the tenant takes more capacity (phased ramp schedules).
- Cross-connect and interconnection revenue in colocation.
- Power is often resold with a margin or passed at cost. Check the contract.

## 3. Key metrics

| Metric | How to compute | Why it matters |
|--------|----------------|----------------|
| WALT | Remaining term weighted by rent | Lock-in |
| Rollover by year | Rent expiring each year / total rent | Re-leasing risk |
| Rent per kW | Monthly rent / contracted kW | Fair comparison across sites |
| Contracted vs available power | Contracted kW / critical load capacity | Leased capacity vs headroom |
| Utilization | Used kW / contracted kW | Tenant ramp status |
| Tenant concentration | Top tenant share of rent | Exit risk |
| Power usage effectiveness | Total facility power / IT power | Efficiency and cost |
| Net effective rent | PV of rent less free rent, TI, commissions | Compare deals |
| Mark to market | Market rent / in-place rent minus 1 | Resets at renewal |

## 4. Revenue drivers

- Contract rent per kW and fixed bumps.
- Ramp schedules and take-up of reserved capacity.
- Power pass-through and margin.
- Cross-connect, remote hands and managed services.
- Rollover: renewal probability and downtime. Switching cost makes tenants sticky.
- Expansion rights and reserved capacity fees.

## 5. Expense drivers

- Power is the largest cost. Understand utility tariff, contract and pass-through.
- Property tax, including sales-tax abatements on equipment that may expire.
- Insurance, with higher property and business interruption cover.
- Maintenance contracts: generators, UPS, chillers.
- Staffing, security and compliance.
- Management fee as a percent of EGI.
- Reserves below NOI for electrical and mechanical systems.

## 6. Capital needs

- Fit-out of halls: electrical, cooling and racks, often phased with leasing.
- Tenant allowances or landlord-funded interior in some structures.
- Generator, UPS and cooling replacement cycles.
- Utility interconnection and substation costs.
- Expansion of capacity for committed tenants.

## 7. Debt and lender view

- Lenders: banks, life companies, debt funds, construction lenders and ABS-style programs for stabilized assets.
- Tenant credit and lease term drive proceeds. Development debt depends on power and pre-leasing.
- Debt yield and DSCR usually bind on stabilized assets.
- Construction loans need power delivery date, budget control and cost-to-complete tests.
- Rule of thumb, verify locally: lenders lend on contracted rent, not capacity that is not leased.
- Watch tenant termination rights tied to delivery delay.

## 8. Screening quick tests

| Test | Pass looks like |
|------|-----------------|
| Power | Secured utility capacity and delivery date |
| Tenant credit | Strong tenant or guarantor on long term |
| WALT vs hold | Term supports hold or re-leasing is plausible |
| Rent per kW vs market | In-place at or below market |
| Cost to complete | Budget funded with contingency |
| Alternate use | Value if tenant leaves is supportable |

## 9. Diligence additions

- Utility agreements: capacity, interconnection, delivery schedule and tariff.
- Lease terms: delivery delay remedies, uptime service levels, power pass-through, termination and expansion.
- Tenant financials, guarantees and credit rating.
- Engineering review: electrical single points of failure, redundancy tier, cooling and generator fuel.
- Environmental and noise permits for generators.
- Water rights and cooling design.
- Tax abatements and their conditions.
- Construction contracts, equipment lead times and warranties.

## 10. Red flags

- Power not yet secured or delivery date slipping.
- One tenant with most of the capacity.
- Lease allows termination for missed delivery.
- Tenants paying below-market power with no pass-through.
- Old facility unable to meet modern density.
- Local opposition or moratoria on data centers.
- Tax abatement ending soon.

## 11. Value levers

- Secure additional power and expansion rights.
- Lease up reserved capacity.
- Renew and extend tenants early.
- Raise rents to market on rollover.
- Upgrade cooling and density.

## 12. Local intelligence

- Tenant news first: credit events, layoffs, capacity cuts, relocations and funding changes.
- Utility actions: interconnection queues, tariff cases and capacity announcements.
- Government actions: moratoria, zoning, tax incentive changes and energy policy.
- New supply: announced campuses, land purchases and pre-leasing nearby.
- Sublease or returned capacity from tenants.

## 13. Model inputs to capture

| Input | Notes |
|-------|-------|
| Tenant, hall, SF, contracted kW | One row per lease |
| Lease start, expiry, options | Include ramp dates |
| Rent per kW or per SF and bumps | Fixed or CPI |
| Lease structure | NNN with power pass-through, fixed rate |
| Ramp schedule | kW by period |
| Market rent per kW | For rollover |
| Renewal probability | Tenant-level |
| Downtime months | After expiry |
| Free rent months | New vs renewal |
| TI per SF or per kW | New vs renewal |
| Leasing commission | New vs renewal |
| Power cost and pass-through | Rate and margin |
| Opex lines | Power, maintenance, tax, insurance, staff, management |
| Tax reassessment and abatements | Year and value |
| Reserves per kW | Electrical and mechanical |

## 14. Site visit and management questions

- Tour halls, electrical rooms and generator yards.
- Ask when power was last at limit and what outages occurred.
- Ask which tenants plan to expand and which to leave.
- Ask about utility timelines and upgrade needs.
- Check cooling, fuel storage and security.
- Ask how much capacity is committed but unused.
