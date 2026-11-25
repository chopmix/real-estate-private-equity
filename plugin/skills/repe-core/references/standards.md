# Standards

These rules apply to every skill in this plugin.

## 1. Data order

1. **User data.** Rent rolls, T-12s, offering memoranda, leases, loan documents, models and reports the user provides.
2. **Connected sources.** Property management, accounting, market data, CRM or document systems the user has connected.
3. **Public sources.** Census, BLS, county tax and deed records, SEC filings, FDIC data, broker market reports, local press, reviews.

A report the user uploads counts as user data, whatever its origin.

## 2. Source tags

Tag every figure where it first appears.

| Tag | Meaning |
|-----|---------|
| `[User]` | From a document or statement the user supplied |
| `[Connected]` | From a system the user connected |
| `[Public]` | From a public source, with link and date |
| `[Assumed]` | A default or estimate. State the basis |

When two sources disagree, show both and say which one was used and why.

## 3. Status labels for cash and capital

| Label | Meaning |
|-------|---------|
| Actual | Received or paid, confirmed by a statement |
| Committed | Signed and enforceable, not yet funded |
| Expected | Forecast with a named source and date |
| Assumed | Placeholder with no confirmation |

Never count Expected or Assumed cash as available. A term sheet is not a commitment. A subscription is not a wire.

## 4. Math

- Calculations come from the workbook or a script, never from free text.
- Simple arithmetic may be shown in a memo when both inputs are visible.
- State every assumption that drives a return.

## 5. Verdicts

Screens and reviews end with a verdict and a conviction score.

| Score | Verdict | Meaning |
|-------|---------|---------|
| 8 to 10 | Pursue | Clear path to the firm's hurdle |
| 5 to 7 | Watch | Possible, with named gaps to close |
| 1 to 4 | Pass | Does not fit. One-line reason |

Also grade data quality: Good, Fair or Poor.

## 6. Decision record

End every run with a dated record. It doubles as evidence of the firm's investment process for investor due diligence.

| Field | Content |
|-------|---------|
| Date | Run date |
| Deal or asset | Name and type |
| Skill | Which skill ran |
| Inputs | Documents used, with dates |
| Result | Verdict or key output |
| Open items | What is missing, who owns it |
| Reviewer | Left blank for the human who signs off |

Screens also add one row to the firm's deal log, including passes and the reason.

## 7. Public research rules

- Every finding is dated and linked. Flag anything older than 12 months as stale.
- Broker reports are marketing as well as research. Label forecasts as broker opinion.
- Summarize and attribute. Do not copy report text.
- If nothing is found or a source needs a login, say so and ask the user to supply it.
- Read online reviews as patterns and score trends. Never name staff or reviewers.

## 8. Privacy and confidentiality

- Read personal data in source documents only as needed. Do not store it or send it anywhere.
- Keep each firm's buy box, deal log and outputs in the user's own workspace.
- Do not carry one deal's confidential facts into another deal's output.

## 9. Professional review

- Outputs are drafts for a qualified professional to review and sign.
- Flag legal points for counsel and tax points for a CPA. Do not state conclusions on either.
- Do not make an investment recommendation. Present the analysis, the verdict against the firm's own criteria, and the open risks.

## 10. Run discipline

- Screen first, go deep second. Spend effort only on deals that clear the first pass.
- Cap public research at three searches per topic unless the user asks for more.
- Write "Not disclosed" for missing data. Never fill a gap silently.
- If a source fails to load, note it and continue.

## 11. Explain mode

When the user asks how something was calculated, or asks to learn, show the inputs, the formula from `metrics-and-formulas.md`, the source of each input, and one sentence on why the metric matters.
