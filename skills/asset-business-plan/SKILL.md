---
name: asset-business-plan
description: Build the ownership business plan for one asset after closing or at a plan reset. Sets the in-place baseline, sizes each value lever, bridges NOI from in-place to stabilized, lays out the first 100 days and the capital program, and sets KPIs with hold, sell or refinance triggers. Use when taking over an asset, rebasing a plan, or preparing an annual plan. Triggers on "build the business plan", "100-day plan", "NOI bridge to stabilization", "capital plan for this asset", or "reset the plan".
---

# Asset Business Plan

## Workflow

### Step 1: Gather Inputs and Set the Baseline

Load the `repe-core` skill and follow `references/standards.md`.
Identify the property type and read its playbook in `references/playbooks/`.

- Inputs: acquisition model, latest T-12 and rent roll, property condition report, loan documents, IC memo, management agreement.
- If the rent roll and T-12 have not been normalized, run `rent-roll-t12-analysis` first.

| Baseline item | In place | Underwriting | Source |
|---------------|----------|--------------|--------|
| NOI (trailing 12 months) | | | |
| Occupancy, physical and economic | | | |
| Average rent vs market | | | |
| Operating expense ratio | | | |
| Deferred and near-term capital needs | | | |
| Debt: balance, rate, maturity, IO period, covenants | | | |

### Step 2: Size the Levers

Draw the lever list from the playbook. Size each one on its own before combining.

| Lever | Category | Annual NOI effect | Capital required | Start | Stabilized by | Owner | Confidence |
|-------|----------|-------------------|------------------|-------|---------------|-------|------------|
| | Revenue | | | | | | |
| | Expense | | | | | | |
| | Capital program | | | | | | |
| | Lease-up | | | | | | |
| | Repositioning | | | | | | |

- Support each revenue lever with market evidence from `market-intelligence` or the rent roll.
- Rate confidence High, Medium or Low, and say what would raise it.

### Step 3: Build the NOI Bridge

Walk NOI from in-place to stabilized, one lever per bar.

- Start at in-place NOI. Add each lever in the order it lands.
- Deduct known headwinds: property tax reassessment, insurance renewal, payroll, expiring abatements.
- Show the stabilized NOI, the yield on total cost, and the year it is reached.
- Hand the levers, timing and capital budget to `underwriting-model` to run the plan case and compare it with underwriting.

### Step 4: Lay Out the First 100 Days and the Capital Program

| Window | Actions | Owner | Done when |
|--------|---------|-------|-----------|
| Days 1 to 30 | Transition: bank accounts, insurance, vendor contracts, staffing, reporting setup | | |
| Days 31 to 60 | Quick wins: fees, collections, expense rebids, pricing | | |
| Days 61 to 100 | Capital program launch, leasing plan, first reforecast | | |

- Capital budget by project: scope, cost, contingency, start, finish, NOI it supports, funding source and status.
- Sequence projects that protect income (life safety, roofs, systems) ahead of projects that grow it.

### Step 5: Set KPIs and Review Triggers

| KPI | Target | Measured | Trigger | Action if tripped |
|-----|--------|----------|---------|-------------------|
| NOI vs plan | | Monthly | | |
| Occupancy | | Monthly | | |
| Rent or rate growth | | Quarterly | | |
| Capital spend vs budget | | Monthly | | |
| DSCR and debt yield | | Quarterly | | |

- Name the condition that prompts a hold, sell or refinance review (for example plan NOI reached early, or a lever failing by a set date).

### Step 6: Output

- Business plan document: baseline, levers, NOI bridge, 100-day plan, capital budget, KPIs and triggers, risks.
- Plan inputs for the workbook, in the format `underwriting-model` expects.
- Decision record per the standards.

## Important Notes

- Most plans miss on timing, not on the size of the lever. Put a date and an owner on every line or it will slip.
- Property tax and insurance resets after a sale can erase a year of revenue gains. Check them before promising NOI growth.
- Expense savings without a named vendor, contract or headcount change are hopes. Leave them out of the base case.
- Budget contingency on the capital program and hold it at the asset, not inside each project.
- Compare the plan with what underwriting promised investors. Explain any gap now, before the first quarterly report does.
- A lever that depends on a market rent the asset has never achieved needs proof from comparable leases, not a broker survey.
