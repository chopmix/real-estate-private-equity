---
name: financing-decisions
description: Compare lender term sheets and refinance options for one asset on a single basis. Lines up proceeds, pricing, structure, recourse, covenants and conditions, computes all-in cost and debt service, and runs the effect on returns. Produces a comparison table, a recommendation against the firm's leverage limits, and questions for each lender. Use when quotes come in, a loan nears maturity, or a refinance is on the table. Triggers on "compare these term sheets", "which loan should we take", "refinance analysis", "lender quotes", or "should we refi".
---

# Financing Decisions

## Workflow

### Step 1: Gather the Quotes and the Context

Load the `repe-core` skill and follow `references/standards.md`.
Identify the property type and read its playbook in `references/playbooks/`.

- Inputs: each term sheet or quote, the current loan documents and payoff letter, latest T-12 and rent roll, business plan, and the firm's leverage limits from the buy box.
- Record what the firm needs from the loan: proceeds, flexibility to sell or refinance, funding for capital or lease-up, hold period.
- Note the date of each quote and when it expires.

### Step 2: Line Up the Terms

Use the layout in `references/term-sheet-comparison.md`. One column per lender.

- Proceeds and the sizing test that binds (LTV, DSCR, debt yield or LTC).
- Pricing: index, spread, floor, rate cap or swap cost, fees in and out.
- Structure: term, extensions and their tests, interest-only period, amortization, prepayment.
- Credit: recourse, guarantees, carve-outs, covenants, reserves, cash management.
- Execution: conditions, third-party reports, timing, lender track record on closing.
- Write "Not quoted" where a lender is silent. Silence is a question, not a yes.

### Step 3: Compute Cost and Effect on Returns

- All-in cost per loan: rate plus fees and required hedging, spread over the expected hold.
- Annual debt service, DSCR and debt yield in year one and at stabilization.
- Hand each structure to `underwriting-model` to run cash on cash, levered IRR and multiple under the base and downside cases.

### Step 4: Run the Refinance Case (if refinancing)

| Item | Amount | Source |
|------|--------|--------|
| Current loan payoff | | |
| Prepayment cost (yield maintenance, defeasance or penalty) | | |
| Closing costs on new loan | | |
| New loan proceeds | | |
| Cash out or cash in | | |
| Change in annual debt service | | |
| Break-even hold to recover costs | | |

- Compare refinancing now with waiting, extending or selling.

### Step 5: Test Against Limits and Recommend

- Check each option against the firm's leverage limits, recourse policy and hedge policy.
- Rank by fit with the business plan, then certainty of close, then cost.
- List the conditions that must clear before any term sheet becomes a commitment.
- Flag recourse, guarantee and carve-out language for counsel.

### Step 6: Output

- Comparison table with a recommendation and the strongest alternative.
- Questions for each lender, tied to gaps or soft terms in their quote.
- Conditions to close with owner and date, and a decision record per the standards.

## Important Notes

- The headline rate is rarely the deciding term. Amortization, recourse, conditions and certainty of close often matter more.
- A term sheet is not a commitment. Proceeds shrink and conditions grow between quote and closing. Keep a second lender warm.
- Read the extension tests. A three-year loan with tests the asset cannot meet is a two-year loan.
- Cash management triggers and reserve sweeps can stop distributions long before a covenant default. Price that in.
- Prepayment terms decide whether the firm can sell when the plan says to. Match them to the business plan exit.
- A lender who has closed similar loans in this market is worth a modest premium over one who has not.
