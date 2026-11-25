---
name: rent-roll-t12-analysis
description: Normalizes a rent roll and trailing 12-month operating statement into the standard layout for the property's income engine, finds the gaps between reported and underwritable NOI, and builds the input file for the model. Produces an analysis memo, an adjusted NOI bridge, and model inputs. Use when a seller's financials arrive or before underwriting. Triggers on "analyze this rent roll", "review the T-12", "normalize the financials", "what's the real NOI", or "loss to lease".
---

# Rent Roll and T-12 Analysis

## Workflow

### Step 1: Load Standards and Gather Files

Load the `repe-core` skill and follow `references/standards.md`.
Identify the property type and read its playbook in `references/playbooks/`.

Then collect:

- Rent roll with its as-of date
- T-12 by month, plus prior year and budget if available
- Delinquency or aged receivables report, concession detail, other income detail
- Current tax bill and insurance premium

Tenant and resident names stay in the user's file. Work with unit or suite numbers only.

### Step 2: Normalize the Rent Roll by Engine

| Engine | Build |
|--------|-------|
| Unit-based | Unit mix by type, in-place vs market rent, loss to lease, lease expirations by month, concessions, delinquency, renovated vs classic premium |
| Commercial | Lease table, WALT, rollover by year, mark to market, tenant concentration (top 5 share of rent), recoveries vs expenses, renewal and expansion options, co-tenancy and kick-out clauses |
| Operating | Revenue per available unit trend by month, occupancy and rate split, departmental margins, seasonality |

- Flag vacant units carried at rent, rents above market by more than the playbook tolerance, and leases with dates that do not match.
- For commercial, read lease abstracts or leases for options and clauses. The rent roll alone will miss them.

### Step 3: Review the T-12

- Trend each line by month. Flag spikes, gaps and lines that move with no driver.
- Identify one-time items (insurance proceeds, lease termination fees, catch-up tax bills) and remove them.
- Normalize to what a new owner will pay:

| Line | Reported | Normalized | Basis |
|------|----------|------------|-------|
| Management fee | | | Market percent of EGI |
| Payroll | | | Staffing plan for the size and type |
| Insurance | | | Current quote or premium |
| Property tax | | | Reassessed at purchase price where the jurisdiction reassesses |
| Repairs and turnover | | | Trend, not the best month |
| Replacement reserves | | | Buy box or lender requirement |

### Step 4: Reconcile Rent Roll to Collections

- Compare annualized rent roll income with T-12 rental collections. Explain the gap: vacancy, concessions, bad debt, timing or rent roll error.
- Compare the last three months of collections with the rent roll. A rising gap means delinquency or concessions are growing.
- Tie other income and recoveries to their detail. Flag any line with no support.

### Step 5: Build the NOI Bridge

| Step | Amount | Source |
|------|--------|--------|
| Seller reported NOI | | |
| Remove one-time income | | |
| Normalize vacancy and credit loss | | |
| Normalize management fee | | |
| Reassess property tax | | |
| Update insurance | | |
| Other normalizations | | |
| Underwritten in-place NOI | | |

Hand the normalized rent roll, expenses and bridge to `underwriting-model` as its deal input file.

### Step 6: Output

- Analysis memo of two pages or less: key findings, data gaps, and questions for the seller.
- Adjusted NOI bridge from reported to underwritten, every line tagged.
- Model input file for `underwriting-model`.
- Decision record per the standards.

## Important Notes

- The rent roll and T-12 are prepared by the seller to support the price. Test every line before accepting it.
- Collections tell the truth that the rent roll may not. When they disagree, trust collections and ask why.
- Property tax reassessment is often the single largest change to NOI after a sale. Never carry the seller's tax bill forward without checking the jurisdiction's rules.
- A last-90-days annualized figure flatters a property in lease-up and hides seasonality. Use it only with the trailing 12 beside it.
- Concessions buried in rent or in marketing expense make in-place rent look higher than it is. Look for them in both places.
- In commercial deals, one tenant's option or co-tenancy clause can matter more than the whole rollover schedule.
