---
name: liquidity-and-capital-needs
description: Forecast cash and capital needs for one asset, project or vehicle. Builds a 13-week cash forecast or a project sources and uses reconciliation, labels every inflow by status, finds the first shortfall, and weighs the options to close it. Use when cash is tight, a draw or capital call is pending, a project is over budget, or a lender or investor asks about liquidity. Triggers on "13-week cash forecast", "do we have enough cash", "sources and uses", "funding gap", or "when do we run out of cash".
---

# Liquidity and Capital Needs

## Workflow

### Step 1: Set the Scope and Gather Inputs

Load the `repe-core` skill and follow `references/standards.md`.
Identify the property type and read its playbook in `references/playbooks/`.

- Confirm the scope: one asset, one project or one vehicle. Company-wide consolidation is out of scope.
- Inputs: bank and reserve statements, AP aging, invoices, budget, loan agreement and draw history, equity commitments and wire confirmations, insurance and tax bills, distribution policy.
- Record the minimum cash balance the lender or operating agreement requires.

### Step 2: Build the Cash Schedule

Use the layout in `references/cash-schedule-layout.md`.

- Operating asset: 13 weeks of opening cash, receipts, operating payments, debt service, capital, taxes, insurance and distributions.
- Project: sources and uses at invoice level, draws available under the loan, equity received, and cost to complete.
- Build it as a workbook that follows the Excel standard in `repe-core`: typed values on one inputs sheet, formulas everywhere else, and a check that the weekly balances roll.

### Step 3: Label Every Inflow

| Inflow | Amount | Date | Status | Evidence |
|--------|--------|------|--------|----------|
| | | | Actual, Committed, Expected or Assumed | |

- Only Actual and Committed cash counts toward coverage.
- A term sheet is not a commitment. A subscription is not a wire. A draw request is not a funded draw.
- A loan advance is Committed only if its conditions are met or within the borrower's control.

### Step 4: Find the Gap

| Week or milestone | Covered cash | Required cash and minimum balance | Surplus or shortfall | Cumulative |
|-------------------|--------------|-----------------------------------|----------------------|------------|
| | | | | |

- Name the date of the first shortfall and its size.
- Show the gap twice: on covered cash only, and including Expected inflows. The difference is the risk.

### Step 5: Weigh the Options

| Option | Cash raised or saved | Available by | Cost | Risk | Approvals needed |
|--------|----------------------|--------------|------|------|------------------|
| Defer payments or scope | | | | | |
| Draw on loan or reserves | | | | | |
| Raise equity or capital call | | | | | |
| Bridge or rescue capital | | | | | |
| Sell an asset or interest | | | | | |

- Rank options by how certain and how fast, then by cost.
- Hand lender options to `financing-decisions`.

### Step 6: Output

- Cash schedule workbook.
- One-page funding summary: covered cash, first shortfall date and size, recommended path, fallback.
- Decisions needed, each with owner and date, plus a decision record per the standards.

## Important Notes

- The first shortfall matters more than the total gap. Liquidity problems are about dates.
- Lenders take weeks to fund draws. Use the actual funding lag from the draw history, not the loan agreement's target.
- Retainage, lien waivers and change orders hide cost to complete. Reconcile the contractor's schedule of values to invoices.
- Reserves held by the lender are not free cash. Check the release conditions before counting them.
- Tell investors and lenders early. A shortfall raised with options gets better terms than one raised at the deadline.
- Deferring capital spend saves cash now and can cost NOI later. Note what each deferral puts at risk.
