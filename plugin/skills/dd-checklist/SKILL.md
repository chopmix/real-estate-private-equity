---
name: dd-checklist
description: Builds and tracks the due diligence checklist for a real estate acquisition, recapitalization or development, scoped to the property type, deal type and debt. Tracks every item by status, owner and due date, escalates red flags with their effect on price or terms, and watches critical dates. Produces tracker rows and a one-page status summary. Use when a deal goes under contract or diligence needs a status check. Triggers on "dd checklist", "diligence tracker", "what's still outstanding", "build the request list", or "when does our deposit go hard".
---

# Due Diligence Checklist

## Workflow

### Step 1: Load Standards and Scope the Diligence

Load the `repe-core` skill and follow `references/standards.md`.
Identify the property type and read its playbook in `references/playbooks/`.

Then confirm:

- **Deal type**: Acquisition, recapitalization or development
- **Debt**: New loan, loan assumption, or all cash. Name the lender if known
- **Contract dates**: Effective date, diligence expiry, deposit hard date, closing date, any extension rights
- **Known concerns**: Issues from screening, `rent-roll-t12-analysis` or `market-intelligence`
- **Team**: Who owns legal, environmental, engineering, financial and insurance work

### Step 2: Build the Checklist by Workstream

Use `references/checklist-by-workstream.md` as the base, then add the playbook's diligence additions.

| Workstream | Scope driver |
|------------|--------------|
| Title and survey | All deals |
| Environmental | All deals. Phase II only if Phase I finds a recognized condition |
| Property condition | All deals. Add specialty reports (roof, structural, MEP) by type and age |
| Zoning and entitlements | All deals. Deeper for development |
| Leases and estoppels | Commercial in full. Unit-based by audit sample |
| Financial | All deals |
| Tax | All deals |
| Insurance | All deals |
| Service contracts | All deals |
| Legal and entity | All deals. Deeper for recapitalization |
| Loan documents | New loan or assumption |
| Property-type additions | From the playbook |

Drop items that do not apply and note why.

### Step 3: Track Status

Every item carries a status, an owner and a due date.

| Status | Meaning |
|--------|---------|
| Requested | Asked of the seller or a third party |
| Received | In hand, not yet reviewed |
| Reviewed | Read, no issue found |
| Issue | Problem found, logged as a red flag |
| Cleared | Issue resolved by price, terms, cure or acceptance |

Count items by status and workstream. Flag anything requested more than a week ago with no response.

### Step 4: Escalate Red Flags and Watch Dates

| Red flag | Workstream | Severity | Effect on price or terms | Proposed fix | Owner | Status |
|----------|------------|----------|--------------------------|--------------|-------|--------|

- Severity: Critical (could kill the deal), Major (price or terms), Minor (note and monitor).
- Size the price effect with `underwriting-model` where it can be modeled.

| Critical date | Date | Days remaining | What must be done by then |
|---------------|------|----------------|---------------------------|
| Diligence expiry | | | |
| Deposit hard date | | | |
| Loan commitment | | | |
| Closing | | | |

### Step 5: Output

- Tracker workbook rows: workstream, item, status, owner, due date, notes. Follow `repe-core/references/excel-standard.md` when writing to a workbook.
- One-page status summary: counts by status, critical dates, red flags by severity, and the decisions needed before the deposit goes hard.
- Decision record per the standards. Legal points flagged for counsel and tax points for a CPA.

## Important Notes

- Work backward from the deposit hard date. Anything that could kill the deal must be reviewed before that date, not just received.
- Estoppels and lease audits catch what the rent roll hides: side letters, unpaid TI, disputed charges and free rent.
- Order third-party reports on day one. Environmental and property condition reports set the pace of the whole schedule.
- A Phase I finding is a question, not an answer. Decide quickly whether to commission a Phase II or price the risk.
- Survey and title exceptions are easy to skip and hard to fix later. Read the exceptions, not just the commitment.
- Every red flag needs a fix path: price reduction, credit at closing, seller cure, escrow, or walk. Decide which before the call with the seller.
