# Playbook: Life Science

Engine: `lease` (lease-by-lease). Read with `metrics-and-formulas.md` and `standards.md`.

## 1. What it is

| Subtype | Description | Main risk |
|---------|-------------|-----------|
| Lab / R&D | Laboratory buildings with wet labs, vented | Tenant funding, specialized fit-out |
| Office / lab flex | Mix of lab and office, flexible layouts | Conversion cost, tenant churn |
| Manufacturing / GMP | Production space, controlled environments | Compliance, power and process needs |
| Core and shell | Base building ready for tenant fit-out | Lease-up risk, fit-out cost |
| Campus / cluster | Several buildings in a research district | Cluster concentration |

## 2. How income is produced

- Lease by lease. Tenants range from startups to large companies, with credit that varies widely.
- Structures: NNN is common. Some leases are modified gross.
- Long terms with fixed bumps for larger tenants. Startups sign shorter terms and need security.
- Security deposits and letters of credit protect against startup failure.
- Tenants often fund their own build-out through allowances and own equipment.
- Landlords sometimes provide shared lab infrastructure and charge for use.

## 3. Key metrics

| Metric | How to compute | Why it matters |
|--------|----------------|----------------|
| WALT | Remaining term weighted by rent | Lock-in |
| Rollover by year | Rent expiring each year / total rent | Re-leasing cost is high |
| Mark to market | Market rent / in-place rent minus 1 | Rent reset potential |
| Tenant credit mix | Rent by credit class (public, funded, early stage) | Loss risk |
| Cash runway | Tenant cash / annual burn | Probability of paying |
| Lab share of SF | Lab SF / total SF | Fit with demand |
| Net effective rent | PV of rent less free rent, TI and commissions | TI is large here |
| Power and ventilation capacity | Kilowatts and air changes per SF | Functional fit |

## 4. Revenue drivers

- Contract rent and fixed bumps.
- Rollover: renewal probability, downtime, free rent and market rent. Sticky for built-out labs.
- Recoveries under NNN, including specialized services.
- Landlord-provided shared services and equipment access fees.
- Tenant failure losses, offset by deposits.

## 5. Expense drivers

- Property tax. Model reassessment on sale where the jurisdiction reassesses.
- Insurance, with higher property and pollution exposure.
- Utilities: high power, ventilation and process loads.
- Repairs: lab HVAC, exhaust, fume hoods, plumbing and waste systems.
- Management fee as a percent of EGI.
- Reserves below NOI for mechanical systems and roof.

## 6. Capital needs

- TI is large: lab fit-out, ventilation, plumbing, casework and power.
- Leasing commissions, new vs renewal.
- Spec lab suites to speed leasing.
- Building system upgrades: air handling, backup power, waste handling and loading.
- Conversion of office to lab, where possible and permitted.
- Decommissioning and restoration of lab suites at lease end.

## 7. Debt and lender view

- Lenders: banks, life companies, debt funds. Some avoid the sector for startup-heavy rent rolls.
- Debt yield and DSCR usually bind, with credit-weighted NOI.
- Lenders discount rent from early-stage tenants.
- Lenders look at funded runway, deposits and letters of credit.
- Rule of thumb, verify locally: lenders will size on credit-quality rent and ask for reserves on specialized TI.

## 8. Screening quick tests

| Test | Pass looks like |
|------|-----------------|
| Tenant credit mix | Mostly funded or public tenants, with deposits |
| WALT | Supports the hold |
| Functional fit | Floor loads, vibration, power, ventilation and loading meet users |
| Basis vs replacement cost | Below cost to build new lab space |
| Cluster strength | Near research institutions and talent |
| Conversion economics | Cost to convert fits rent |

## 9. Diligence additions

- Lease abstracts with termination, expansion, surrender and restoration duties.
- Tenant funding: cash runway, last financing, partners and grants.
- Security deposits and letter of credit terms.
- Environmental: Phase I, Phase II where use is hazardous, and decommissioning history.
- Hazardous materials permits and tenant compliance records.
- Mechanical review: air handling, exhaust, redundancy, backup power.
- Structural review: floor loads, vibration and slab capacity.
- Zoning and permitted uses for labs and manufacturing.

## 10. Red flags

- Rent roll weighted to early-stage tenants with short runway.
- Large tenant dependent on a single product or financing.
- Space that cannot meet modern lab standards.
- Unfunded restoration duties on tenant exits.
- Recent supply wave from conversions or new buildings.
- Rents set at the peak of funding cycles with no resets planned.
- High free rent or TI in recent leases to hit occupancy.
- No environmental history for prior lab tenants.

## 11. Value levers

- Early renewal and extension for stable tenants.
- Spec suites for fast leasing.
- Building upgrades to meet specification.
- Convert office to lab, if feasible.
- Provide shared services and expansion space for growing tenants.
- Improve tenant mix toward funded or public companies.

## 12. Local intelligence

- Tenant news first: financing rounds, trial results, layoffs, mergers, bankruptcy, relocations and credit events.
- Government lease actions, and research funding or grant changes.
- New supply: lab deliveries, conversions and pre-leasing.
- Sublease space, especially from tenants cutting back.
- University and institute expansions.

## 13. Model inputs to capture

| Input | Notes |
|-------|-------|
| Tenant, suite, SF, lab or office | One row per lease |
| Lease start, expiry, options | Include notice dates |
| Base rent per SF and bumps | Fixed or CPI |
| Lease structure | NNN, modified gross |
| Market rent per SF | Lab vs office |
| Renewal probability | By credit class |
| Downtime months | New vs renewal |
| Free rent months | New vs renewal |
| TI per SF | Lab vs office, new vs renewal |
| Leasing commission | New vs renewal |
| Recoveries and caps | Per SF |
| Deposits and letters of credit | Amount |
| Opex lines | Tax, insurance, power, R&M, management |
| Tax reassessment | Year and value after sale |
| Reserves per SF | Mechanical and structure |
| Restoration cost per SF | At lease end |

## 14. Site visit and management questions

- Tour labs with the tenants. Check exhaust, power, floor loads and waste handling.
- Ask which tenants are hiring, raising funds or cutting staff.
- Ask what tenants need that the building lacks.
- Look at mechanical rooms and backup power.
- Ask about restoration and decommissioning on past exits.
- Ask which competing buildings tenants toured.
