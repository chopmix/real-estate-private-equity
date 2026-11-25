---
name: market-intelligence
description: Researches the submarket and the specific property behind a deal, from broker reports, local press, public records and online reviews. Produces a market and property brief with sale and rent comps, a red flag list and questions for the site visit. Use when screening a deal, preparing underwriting assumptions, or checking an asset before a tour. Triggers on "what's happening in this submarket", "pull comps", "research this property", "any red flags on the owner", or "market brief".
---

# Market Intelligence

## Workflow

### Step 1: Load Standards and Define the Scope

Load the `repe-core` skill and follow `references/standards.md`.
Identify the property type and read its playbook in `references/playbooks/`.

Then confirm:

- Property address, type and size
- Submarket boundary (the one brokers and lenders use, not just the city)
- Owner entity, major tenants or operator, and current lender if known
- Any broker reports or comp data the user already holds (these count as user data)

### Step 2: Part 1 - Read the Submarket

| Item | Current | Trend | Source and date |
|------|---------|-------|-----------------|
| Market rent | | | |
| Vacancy or occupancy | | | |
| Net absorption | | | |
| Supply under construction | | | |
| Supply planned or permitted | | | |
| Recent trades and cap rates | | | |
| Major employers and recent moves | | | |
| Population and job growth | | | |

- Compare broker reports with each other and with public data. Label forecasts as broker opinion.
- Note new supply within the property's direct competitive set, not just the submarket total.

### Step 3: Part 2 - Build the Property File

| Item | Finding | Source and date |
|------|---------|-----------------|
| News on the asset | | |
| Owner track record and other holdings | | |
| Major tenant or operator news | | |
| Sale history (dates and prices) | | |
| Loan history (lender, amount, maturity) | | |
| Code violations and open permits | | |
| Litigation, liens and lis pendens | | |
| Online reviews (score trend and recurring themes) | | |

Let the playbook set the emphasis. Reviews carry weight for residential, hotels, seniors housing and storage. Tenant news and credit carry weight for office, industrial and retail.

### Step 4: Build Comp Tables

Sale comps:

| Property | Date | Price | Per unit or SF | Cap rate | Buyer type | Source |
|----------|------|-------|----------------|----------|------------|--------|

Rent comps:

| Property | Distance | Vintage | Rent | Per SF | Occupancy | Concessions | Source and date |
|----------|----------|---------|------|--------|-----------|-------------|-----------------|

- Use comps from the subject's competitive set and quality. Note the adjustment needed for each.
- State the rent and exit cap rate the comps support, for use in `underwriting-model`.

### Step 5: Output

Market and property brief, two to three pages, using `references/brief-template.md`:

- Summary of what the market supports: rent, occupancy, exit cap rate
- Comp tables with source and date
- Red flag list, each with its evidence and severity
- Questions for the site visit, passed to `site-visit-prep`
- What could not be found, and what the user should supply
- Decision record per the standards

## Important Notes

- Supply kills rent growth faster than demand builds it. Count every competing project within the subject's draw, including those not yet broken ground.
- Broker reports aim to sell. Use their data, discount their forecasts, and cross-check against public records.
- Sale comps age quickly when rates move. A trade before a rate change says little about today's pricing.
- Review trends matter more than the score. A falling score after a management change tells you what you are buying.
- Code cases and permit history often reveal deferred maintenance before the property condition report does.
- Say plainly what could not be verified. A blank in the brief is better than an assumption presented as research.
