---
name: asset-management-review
description: Review a monthly or quarterly property package for one asset. Compares actuals with budget, underwriting and the business plan, explains each variance, tracks leasing, delinquency and capital projects, and tests debt covenants. Produces an asset scorecard, a variance table and an issues list. Use when the property manager's package arrives or before an asset review meeting. Triggers on "review the monthly package", "budget vs actual", "how is this asset performing", "covenant check", or "quarterly asset review".
---

# Asset Management Review

## Workflow

### Step 1: Ingest the Property Package

Load the `repe-core` skill and follow `references/standards.md`.
Identify the property type and read its playbook in `references/playbooks/`.

- Inputs: income statement with budget, balance sheet, rent roll, leasing report, aged delinquency, capital project report, bank and reserve statements, loan compliance certificate.
- Pull the approved budget, the underwriting case and the business plan. Ask for any that are missing.
- Note the period, the accounting basis (cash or accrual) and any restatement of prior months.

### Step 2: Explain Budget vs Actual

| Line | Actual | Budget | Variance | Variance % | Timing or permanent | Price or volume | Explanation |
|------|--------|--------|----------|------------|---------------------|-----------------|-------------|
| | | | | | | | |

- Explain every line above the firm's materiality threshold, or 5 percent and a set dollar amount if none is set `[Assumed]`.
- Timing: the spend or income moves to another month. Permanent: it will not reverse this year.
- Price: rate, rent or unit cost differs. Volume: occupancy, units, hours or quantity differs. Split mixed variances.
- Reforecast the year when permanent variances add up past the threshold.

### Step 3: Compare with Underwriting and the Business Plan

| Measure | Actual | Business plan | Underwriting | Comment |
|---------|--------|---------------|--------------|---------|
| NOI, trailing 12 months | | | | |
| Occupancy | | | | |
| Average rent or rate | | | | |
| Capital spent to date | | | | |
| Plan levers delivered | | | | |

- Mark each business plan lever On track, Late or At risk, with the reason.

### Step 4: Review Operations and Capital

- Leasing and occupancy: trend over at least six periods, leases signed and lost, pipeline, expirations in the next 12 months.
- Delinquency: aging buckets, write-offs, payment plans, trend.
- Capital projects: budget, committed, spent, percent complete, schedule against plan, change orders.
- Local watch from `market-intelligence`: review score trend, new competing supply, tenant news.

### Step 5: Test the Debt

| Test | Actual | Covenant or trigger | Headroom | Next test date |
|------|--------|---------------------|----------|----------------|
| DSCR | | | | |
| Debt yield | | | | |
| Cash management trigger | | | | |
| Rate cap expiry and strike | | | | |
| Loan maturity and extension tests | | | | |

- Compute covenants the way the loan agreement defines them, not the way the package reports them.
- Flag any test within one bad quarter of tripping. Hand to `financing-decisions` if a cure, extension or refinance is in view.

### Step 6: Output

- Asset scorecard: one page, status by area (NOI, leasing, collections, capital, debt), verdict and conviction score.
- Variance table from Step 2.
- Issues list: issue, impact, action, owner, date.
- Questions for the property manager and a decision record per the standards.

## Important Notes

- A favorable expense variance is often a deferred repair or an unpaid invoice. Check accruals before calling it a saving.
- Timing variances that repeat three months running are permanent. Treat them that way.
- Occupancy can rise while economic occupancy falls. Read concessions and bad debt next to the occupancy line.
- Covenant definitions differ from GAAP and from the property manager's NOI. Use the loan agreement's terms.
- Rate cap replacement and reserve deposits can surprise cash. Check the cap expiry date every review.
- Ask for the property manager's explanation first, then test it against the general ledger detail.
