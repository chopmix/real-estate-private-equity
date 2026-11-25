---
name: deal-screening
description: Screens offering memoranda, broker packages and listing batches against the firm's buy box. Scores every deal in a quick scan, then runs a deep screen on those above the threshold, with a maximum bid for the hurdle and a Pursue, Watch or Pass verdict. Produces a one-page screening memo and a deal log row. Use when triaging new deals or deciding whether to take a first call. Triggers on "screen this deal", "review this OM", "should we look at this", "score these listings", or "what's our max bid".
---

# Deal Screening

## Workflow

### Step 1: Load Standards and Gather Materials

Load the `repe-core` skill and follow `references/standards.md`.
Identify the property type and read its playbook in `references/playbooks/`.

Then collect:

- Offering memorandum, teaser, flyer or listing batch
- Rent roll and T-12 if provided
- The firm's buy box, screening weights and deep screen threshold from `buy-box.md`

### Step 2: Quick Scan Every Deal

Score each deal from a starting point of 5 using the buy box screening weights. A breach of any hard limit is an automatic Pass.

- Write one line per deal in the quick scan format in `references/deal-log-schema.md`.
- Stop here for deals below the threshold. Log them with the reason.

### Step 3: Deep Screen - Extract Facts and Test

For deals at or above the threshold, extract the facts.

| Fact | Value | Source |
|------|-------|--------|
| Property and address | | |
| Property type and subtype | | |
| Size (units, SF, keys or beds) | | |
| Vintage and last renovation | | |
| Asking price | | |
| Price per unit or SF | | |
| In-place NOI and cap rate | | |
| Occupancy (physical and economic) | | |
| Seller and motive | | |
| Broker and process (call for offers date) | | |

Test against the buy box.

| Test | Target | Actual | Pass/Fail |
|------|--------|--------|-----------|
| Market and submarket | | | |
| Property type and class | | | |
| Deal size and equity check | | | |
| Going-in cap rate | | | |
| Price vs replacement cost | | | |
| Yield on cost | | | |
| Debt sizing (binding test) | | | |
| Levered IRR vs hurdle | | | |

### Step 4: Back-of-Envelope Returns and Maximum Bid

Hand the facts to the `underwriting-model` skill and use its quick screen path. It returns:

- Going-in and stabilized yield, loan sized to the binding test, levered IRR and multiple at the asking price
- Maximum bid that meets the firm's hurdle, and the discount from ask in dollars and percent

Optional investor-fit lens, when the user asks: stabilized cash yield, depreciable basis, and cost segregation potential. Flag all tax points for a CPA.

### Step 5: Assess

| Item | Content |
|------|---------|
| Verdict and conviction | Pursue, Watch or Pass, 1 to 10 |
| Data quality | Good, Fair or Poor, with what is missing |
| Bull case | 2 to 3 bullets |
| Bear case | 2 to 3 bullets |
| First-call questions | 3 to 5 questions for the broker or seller |
| Next steps | Owner and date for each |

### Step 6: Output

- One-page screening memo for each deep-screened deal, suitable for a partner or a quick committee read.
- Quick scan list for the full batch, ranked by score.
- One deal log row per deal, passes included, using `references/deal-log-schema.md`, then the decision record.

## Important Notes

- The broker's pro forma is the seller's case. Screen on in-place NOI with taxes reassessed at the purchase price, then look at upside.
- When the maximum bid sits far below ask, say so plainly. A Pass with a number attached is useful when the deal comes back.
- A cap rate is only as good as the NOI under it. Check for missing reserves, a below-market management fee and one-time income.
- Seller motive and process tell you how much room there is on price. Ask before spending model time.
- Log every pass with its reason. The log becomes the firm's evidence of discipline and a record of what traded where.
- Speed matters. A quick scan should take minutes, and a deep screen should not become underwriting.
