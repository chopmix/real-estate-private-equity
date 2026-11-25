# Playbook: Net Lease

Engine: `lease` (lease-by-lease). Read with `metrics-and-formulas.md` and `standards.md`.

## 1. What it is

| Subtype | Description | Main risk |
|---------|-------------|-----------|
| Corporate single-tenant | Office, industrial or retail leased to one company | Tenant credit, residual value |
| Government-leased (GSA and other agencies) | Federal, state or local agency tenant | Lease actions, termination rights, building specificity |
| Franchise / operator | Restaurants, services, convenience, run by operators | Operator credit, unit economics |
| Sale-leaseback | Seller becomes tenant on a new long lease | Rent vs market, tenant health |
| Ground lease | Land only, tenant owns improvements | Reversion, leasehold financing |

## 2. How income is produced

- One lease, or a few. Value comes from lease term plus tenant credit.
- Structures: absolute NNN (tenant pays all, including roof and structure), NNN with landlord structure duty, and modified gross. Read who bears roof, structure and capital.
- Fixed bumps are common. Some leases have flat rent for long periods.
- Government leases often have firm terms followed by soft terms. Only the firm term is secure income.
- Government leases may be full service, with the landlord paying operating costs. Do not assume NNN.
- Rent may reset at renewal to fair market value. That is a rollover event, not a given.

## 3. Key metrics

| Metric | How to compute | Why it matters |
|--------|----------------|----------------|
| Remaining firm term | Years until the first right to terminate | Secured income |
| WALT | Remaining term weighted by rent | Portfolio view |
| Tenant credit | Rating, financials, guarantor strength | Probability rent is paid |
| Rent coverage | Store or unit EBITDAR / rent | Probability the tenant keeps the site |
| Mark to market | Market rent / in-place rent minus 1 | Renewal and re-leasing risk |
| Residual value | Value at lease end, based on market rent and use | Exit risk |
| Rent per SF vs market | In-place rent / market rent | Over-rented sites fail first |
| Going-in cap vs credit | Cap rate relative to similar credit and term | Pricing check |

## 4. Revenue drivers

- Contract rent and bumps.
- Renewal option exercise, and rent at renewal.
- Landlord-paid costs on gross or modified structures.
- Re-leasing assumptions after expiry: downtime, TI, commissions.
- Early termination fees.

## 5. Expense drivers

- Property tax. Under NNN the tenant pays. Model reassessment on sale for credit risk of the pass-through.
- Insurance, tenant-paid but verify coverage and landlord additional insured status.
- Roof, structure and parking: landlord or tenant, per lease.
- Management and asset management cost.
- Government leases with full service pay landlord operating costs: utilities, janitorial, security.
- Non-recoverable leakage after expiry.
- Reserves below NOI, scaled to landlord obligations.

## 6. Capital needs

- Landlord roof and structure work where the lease allows.
- TI for renewal or new tenant. Larger when the space is specialized.
- Leasing commission at renewal and new lease.
- Downtime carry: taxes, insurance and utilities during vacancy.
- Re-tenanting capital after expiry. Price it at purchase.

## 7. Debt and lender view

- Lenders: life companies, banks, CMBS, specialty net lease lenders.
- Credit and term drive proceeds. Strong credit with long term gets high leverage.
- DSCR and debt yield bind when term is short or credit is weak.
- Loan terms often must not outlast the firm lease term.
- Lenders may require a tail: loan matures well before lease expiry or reserves build.
- Rule of thumb, verify locally: lenders want term past loan maturity, or a sweep in the last years.

## 8. Screening quick tests

| Test | Pass looks like |
|------|-----------------|
| Firm term vs hold | Firm term covers the hold, or exit value is secured |
| Credit | Tenant or guarantor supports rent with margin |
| Rent vs market | In-place rent at or below market |
| Residual value | Land plus building worth enough if tenant leaves |
| Rent coverage | Operators have healthy coverage |
| Price vs credit | Cap rate fits credit and term |

## 9. Diligence additions

- Read the lease for: termination rights, purchase options, ROFR, repair duties, casualty, condemnation, SNDA and assignment.
- Government leases: the lease form, termination for convenience clause, appropriation language, and the agency's space plans.
- Estoppel and, where relevant, a landlord SNDA.
- Tenant financial statements, parent guarantees and credit ratings.
- Unit-level sales for operator tenants and rent coverage.
- Property condition and roof report even where the tenant pays, since the asset returns to you.
- Zoning and use rights. Check whether a new user could be permitted.
- Alternative use and re-leasing study.

## 10. Red flags

- Short remaining firm term with an over-market rent.
- Weak or unrated tenant with no guarantee.
- Termination right close in time, or termination for convenience in a government lease.
- Specialized building with no alternate user.
- Landlord obligations hidden in an otherwise net lease.
- Location in a declining trade area or one with a rival tenant site.
- Rent coverage thin at the site.
- Tenant in a distressed sector, or in talks of sale or merger.
- Price based on a cap rate for a different credit.

## 11. Value levers

- Extend term early in return for modest concessions.
- Buy with a long firm term and strong credit, then hold.
- Convert full service to NNN where agencies allow it.
- Sell into strong demand for credit tenants.
- Re-tenant above market with a different user.

## 12. Local intelligence

- Tenant news first: credit rating actions, restructurings, store closures, relocations, mergers and layoffs.
- Government lease actions: agency consolidations, space reductions, budget decisions and lease notices.
- Operator unit trends: closing lists and franchise disputes.
- New supply: competing sites and alternative buildings.
- Sublease listings and dark site listings by the same tenant.

## 13. Model inputs to capture

| Input | Notes |
|-------|-------|
| Tenant, guarantor, SF | One row per lease |
| Lease start, firm term end, soft term end | Include notice dates |
| Options and rent at renewal | Fixed, fair market or CPI |
| Base rent per SF and bumps | Steps and dates |
| Lease structure | Absolute NNN, NNN, modified gross, full service |
| Market rent per SF | For residual and re-leasing |
| Renewal probability | Credit and fit based |
| Downtime months | After expiry |
| TI per SF | New vs renewal |
| Leasing commission | New vs renewal |
| Landlord-paid costs | Roof, structure, services |
| Opex and recoveries | Tax, insurance, services |
| Tax reassessment | Year and value after sale |
| Reserves per SF | Landlord obligations |
| Residual cap rate | Higher than going-in |

## 14. Site visit and management questions

- Walk the site. Is the building maintained as the lease requires?
- Ask the tenant how critical the site is to their business.
- Ask about plans to relocate, consolidate or expand.
- Check roof, parking, signage and drainage.
- For government tenants: ask the property manager about agency staffing and space use.
- Ask about unpaid rent, disputes and repair requests.
