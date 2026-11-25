---
name: ic-memo
description: Assembles the investment committee memo for a real estate deal from the screening, rent roll analysis, market brief, underwriting model, waterfall and diligence tracker. States the verdict against the buy box, shows gross and net returns, sensitivities and a downside case, and lists what is still open. Produces an IC memo and a decision record. Use when a deal is ready for committee approval. Triggers on "write the IC memo", "investment committee memo", "prepare this for committee", "approval memo", or "write up the deal".
---

# Investment Committee Memo

## Workflow

### Step 1: Load Standards and Gather Inputs

Load the `repe-core` skill and follow `references/standards.md`.
Identify the property type and read its playbook in `references/playbooks/`.

Then collect the latest version of each input and list what is missing.

| Input | From | Version and date | Status |
|-------|------|------------------|--------|
| Screening memo | `deal-screening` | | |
| Rent roll and T-12 analysis | `rent-roll-t12-analysis` | | |
| Market and property brief | `market-intelligence` | | |
| Underwriting workbook | `underwriting-model` | | |
| Waterfall and net returns | `jv-waterfall` | | |
| Diligence status | `dd-checklist` | | |
| Lender term sheet | User | | |

If the workbook or waterfall is missing or stale, run `underwriting-model` or `jv-waterfall` before drafting.

### Step 2: Draft the Memo

Follow `references/memo-template.md`.

| Section | Content |
|---------|---------|
| 1. Recommendation and terms | Verdict, price, equity, debt, key terms, approval sought |
| 2. Property and business plan | What it is, what we will do, timing and cost |
| 3. Market | What the market supports, supply, comps |
| 4. Financial analysis | In-place to stabilized NOI bridge, assumptions vs comps |
| 5. Capital structure and returns | Sources and uses, debt terms, gross and net returns |
| 6. Risks and mitigants | Ranked by effect on value |
| 7. Diligence status | Red flags, open items, critical dates |
| 8. Exit | Timing, buyer pool, exit cap rate basis |
| 9. Open items | Owner and date for each |

### Step 3: Tie Every Number to the Workbook

- Pull each figure from the workbook or waterfall by sheet and cell. No number is typed from memory or recomputed in text.
- Show both gross (property and deal level) and net (investor after fees and promote) returns.
- Include the sensitivity grids from the workbook: exit cap rate, rent growth, and the playbook's key driver.
- Include a downside case with its assumptions stated, and show whether the loan stays within covenants.
- Show returns attribution and flag it if cap rate compression supplies most of the profit.

### Step 4: State the Verdict Against the Buy Box

| Test | Buy box | This deal | Within limits |
|------|---------|-----------|---------------|
| Levered IRR | | | |
| Equity multiple | | | |
| Stabilized cash on cash | | | |
| Yield on cost | | | |
| Maximum LTV or LTC | | | |
| Minimum DSCR and debt yield | | | |

- Name every exception to the buy box and the reason the deal team supports it.
- Give the verdict (Pursue, Watch or Pass) and conviction score. The committee makes the decision.

### Step 5: Output

- IC memo document, with an executive summary on the first page.
- Appendix listing input documents with dates, and the workbook file name and version.
- Decision record per the standards, with the Reviewer field left blank for committee sign-off.

## Important Notes

- The first page carries the decision. A committee member who reads only that page should know the ask, the return, the main risk and what is still open.
- Show the downside honestly. A memo that only shows the base case invites the committee to build its own, usually harsher.
- Net returns are what investors receive. Gross returns alone overstate the deal.
- Rank risks by what they would do to value, and pair each with a mitigant that is real: a reserve, a structure or a price.
- Open diligence items belong in the memo, not in a side conversation. Approval subject to named conditions is a clean outcome.
- Keep the memo the same shape for every deal. Consistency lets the committee compare deals and shows investors a disciplined process.
