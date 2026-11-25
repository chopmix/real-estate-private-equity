---
name: jv-waterfall
description: Models how deal cash splits between investors and the sponsor: preferred return, return of capital, hurdles and promote, catch-up, sponsor co-invest and fees, with gross and net investor returns. Works in the firm's own model or builds to the plugin's waterfall standard, then tests the result. Use when structuring or reviewing a joint venture, comparing sponsor terms, or explaining what the sponsor earns. Triggers on "model the waterfall", "promote", "LP net returns", "what does the GP make", or "pref and hurdles".
---

# JV Waterfall

## Workflow

### Step 1: Load Standards and Read the Agreement

Load the `repe-core` skill and follow `references/standards.md`.

Read the operating agreement, term sheet or offering summary. The document governs. Extract:

| Term | Value | Source |
|------|-------|--------|
| Investor and sponsor equity shares | | |
| Preferred return, compounding and accrual start | | |
| Return of capital order | | |
| Hurdles (IRR or multiple) and promote at each tier | | |
| Catch-up, clawback, lookback | | |
| Operating cash vs capital event distributions | | |
| Fees and the base each is charged on | | |
| Capital calls after closing and default remedies | | |

- Mark any term not found as `[Assumed]` and name the missing document.
- Flag ambiguous or unusual terms for counsel. Do not resolve them by guessing.

### Step 2: Read the Waterfall Standard

Read `references/waterfall-standard.md`. It sets what a correct waterfall proves. The method is open.

### Step 3: Produce the Waterfall

| Path | Use when | What happens |
|------|----------|--------------|
| Firm template | The firm's model already has a waterfall | Map the terms in. Keep its structure |
| Build to standard | No template, or the terms do not fit one | Build the waterfall with live formulas, at the timing the agreement tests |
| Quick screen | First look at sponsor economics | Use the quick screening model in `underwriting-model` |

- Property cash flows come from the `underwriting-model` skill. Build or load them first.
- The quick screening model handles a preferred return, return of capital and up to three IRR hurdles, annually. For catch-up, clawback, multiple classes or monthly tests, build to standard.

### Step 4: Test the Split

| Test | Passes when |
|------|-------------|
| Distributions | Investor plus sponsor equals cash available every period |
| Capital accounts | Capital returned never exceeds capital contributed |
| Hurdle logic | When a tier is exactly filled, investor IRR equals that hurdle |
| Gross to net | Net return is below gross by fees plus promote, and the bridge adds up |
| Agreement match | Compounding, hurdle definition and fee bases match the document |

Run the workbook audit in `underwriting-model` and recompute investor IRR independently.

### Step 5: Read the Economics

| Item | Investor | Sponsor |
|------|----------|---------|
| Capital contributed | | |
| Distributions | | |
| IRR, gross and net | | |
| Equity multiple, gross and net | | |
| Promote | | |
| Fees | | |

- Show sponsor pay in the base and downside cases. Fees persist when promote disappears.
- When comparing structures, hold the property cash flows fixed and change only the terms.

### Step 6: Output

- The waterfall in the workbook, with the test results.
- A one-page summary: terms table, economics table, base and downside.
- Every `[Assumed]` term and every point flagged for counsel.

## Important Notes

- Fees are paid whether or not the deal performs. Promote is paid only on performance. Show both so the reader sees which drives sponsor pay.
- The co-invest share earns its pro rata share in every tier. Do not count it as promote.
- Small differences in compounding and timing move promote by real money. Model what the agreement says, not the common convention.
- Capital called after closing accrues the preferred return from the date it arrives.
- The operating agreement governs. This model is a draft for review by counsel and the accountants.
