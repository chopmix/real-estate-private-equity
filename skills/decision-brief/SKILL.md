---
name: decision-brief
description: Turn a tracker, email threads, meeting notes or transcripts into a weekly brief of two pages or less for a principal. Leads with the decisions needed, each with a recommendation, the strongest alternative, an owner, a date and evidence, then the advice ledger and open items. Use when a principal needs to act on the week's matters without reading everything. Triggers on "weekly brief", "what decisions do I need to make", "summarize this week for the principal", "decision memo from these notes", or "brief me".
---

# Decision Brief

## Workflow

### Step 1: Gather the Sources

Load the `repe-core` skill and follow `references/standards.md`.

- Inputs: the user's tracker, email threads, meeting notes, transcripts and any prior brief.
- Note the period covered and the date of each source.
- Ask who the principal is and what they decide on, so the brief stays within their remit.

### Step 2: Sort Facts from Estimates

| Item | Confirmed fact or estimate | Source and date | Cash status if money |
|------|----------------------------|-----------------|----------------------|
| | | | |

- A fact is in a signed document, a statement or a recorded decision. Everything else is an estimate, and says whose.
- Label cash Actual, Committed, Expected or Assumed.
- Where sources disagree, show both and name the one relied on.

### Step 3: Frame the Decisions Needed

For each decision, in order of deadline and consequence:

| Field | Content |
|-------|---------|
| Issue | One sentence |
| What changed | Since the last brief |
| Recommendation | One sentence, with the reason |
| Strongest alternative | The best case against the recommendation |
| Owner | One name |
| Decide by | Date, and what happens if it slips |
| Evidence | Link or document reference |

- No decision goes in without an owner, a date and evidence. If one is missing, list it as an open item instead.
- Hand calculations to `underwriting-model` and cash questions to `liquidity-and-capital-needs`.

### Step 4: Update the Advice Ledger and Open Items

- Advice ledger: what was flagged, what was recommended, the decision made, the result so far.
- Open items: matter, current position, next expected result, owner.
- Close items that are done. Carry the rest forward with their original date.

### Step 5: Draft the Brief

Use `references/brief-template.md`.

- Page one: decisions needed. Page two: ledger, open items, and anything for information only.
- Write so the principal can decide from the brief alone. Detail lives in the linked evidence.

### Step 6: Output

- Decision brief of two pages or less.
- Decision record per the standards, listing the sources used.

## Important Notes

- A decision without an owner and a date is a discussion. Do not dress it up as a decision.
- State the strongest alternative fairly. A brief that argues only one side loses the principal's trust.
- Keep confirmed facts apart from estimates on the page. Mixing them is how wrong numbers reach investors.
- The advice ledger protects everyone. It shows what was raised, when, and what was chosen.
- Leave out matters that need no action this week. Short briefs get read.
- Names and personal details from emails and transcripts stay in the user's workspace.
