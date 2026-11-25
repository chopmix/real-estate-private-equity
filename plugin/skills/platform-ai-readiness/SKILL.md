---
name: platform-ai-readiness
description: Assess where AI can help a real estate investment firm most, function by function and across its assets. Maps current processes and data, sizes quick wins by effort, value and risk, and ranks the uses that repeat across the portfolio. Produces a ranked action list with an owner and first step for each. Use when a firm asks where to start with AI, plans its AI budget, or wants to speed up reporting and decisions. Triggers on "where should we use AI", "AI readiness", "AI opportunities across the firm", "which AI projects first", or "AI roadmap".
---

# Platform AI Readiness

## Workflow

### Step 1: Gather Inputs

Load the `repe-core` skill and follow `references/standards.md`.

- Inputs: organization chart or team list, systems in use (accounting, property management, CRM, document storage, models), recurring reports, the asset list, and current AI use.
- Ask what decisions are slowest today and which reports take the most staff time.
- Note any policy on data, vendors or client confidentiality that limits AI use.

### Step 2: Map Each Function

| Function | Current process | Data available and where it lives | Time spent per cycle | Pain point |
|----------|-----------------|-----------------------------------|----------------------|------------|
| Acquisitions | | | | |
| Asset management | | | | |
| Property operations | | | | |
| Finance and accounting | | | | |
| Investor relations | | | | |
| Development and construction | | | | |

- Interview or read the process as it runs, not as the policy manual describes it.
- Mark data quality Good, Fair or Poor. Poor data limits what AI can do first.

### Step 3: Find the Uses

| Function | Use | Clarity or automation | Quick win | Effort | Value | Risk | Repeats across assets |
|----------|-----|-----------------------|-----------|--------|-------|------|-----------------------|
| | | | Yes or No | Low, Medium, High | Low, Medium, High | Low, Medium, High | Yes or No |

- Clarity uses come first: summaries, variance explanations, screening, briefs and answers drawn from the firm's own documents.
- Automation comes second: data entry, report assembly, reconciliations, routing.
- Point to skills in this plugin where they fit, such as `deal-screening`, `asset-management-review` and `decision-brief`.

### Step 4: Rank Across the Firm

- Score each use on value, effort and risk. Favor high value, low effort, low risk.
- Move uses that repeat across many assets up the list. One process fixed once pays many times.
- Hold back uses that need clean data the firm does not yet have, and name the data fix that unlocks them.
- Keep a human review step on anything that reaches investors, lenders or a signed document.

### Step 5: Output

- Ranked action list:

| Rank | Use | Function | First step | Owner | Done when | Value measure |
|------|-----|----------|------------|-------|-----------|---------------|
| | | | | | | |

- One-page summary: the top three uses, the data fixes needed, and the risks to manage.
- Decision record per the standards.

## Important Notes

- The first value is clarity and faster decisions. Automation follows once people trust the outputs.
- Start where the data already exists and the decision is frequent. Monthly asset reviews and deal screens are common first wins.
- Measure value in hours saved and days cut from a decision, not in tools deployed.
- Confidential deal and investor data needs a clear policy on which tools may see it. Settle that before the first pilot.
- One named owner per use. Shared ownership of an AI pilot means no ownership.
- A use that works on one asset should be tested on a second before it is called a platform capability.
