# Authoring standard

Every skill in this plugin follows this standard. The goal is the clean, succinct style of Anthropic's financial-services skills: short, scannable, and specific.

## Shape of a SKILL.md

```
---
name: <folder-name>
description: <what it does>. <What it produces>. Use when <situations>. Triggers on "<phrase>", "<phrase>", or "<phrase>".
---

# <Title>

## Workflow

### Step 1: <Verb phrase>
...
### Step N: Output

## Important Notes
- 4 to 7 short bullets
```

Guide to outcomes. Describe what good looks like, the tests that prove it, and the judgment calls. Leave the method to Claude. Models keep improving, so a skill that dictates every step ages badly, and one that sets the standard does not.

Rules:

- 60 to 120 lines per SKILL.md. Hard cap 130. If it runs long, move detail to `references/` in the same skill folder and name the file in the step that needs it.
- Description is one paragraph, under 600 characters, written as the situations a user is in. Include 4 to 6 trigger phrases in quotes.
- 4 to 6 workflow steps. Each step is a short lead line, then bullets or one table. No paragraphs longer than two sentences.
- Use tables for extracted facts, pass/fail tests, scenarios and output layouts. Leave value cells blank.
- The last step is always "Output" and names the deliverable (one-page memo, Excel workbook, tracker rows).
- "Important Notes" holds judgment: what experienced people watch for. No restating of steps.
- Plain English. Imperative voice. No management-framework jargon. No em dashes. ASCII characters only (straight quotes, hyphens).
- No dated market statistics. A rule of thumb is allowed only when labeled "rule of thumb, verify locally".

## Step 1 of every skill

Step 1 always opens with the same two lines, then the skill's own input list:

```
Load the `repe-core` skill and follow `references/standards.md`.
Identify the property type and read its playbook in `references/playbooks/`.
```

Skills that do not depend on property type (for example `decision-brief`) drop the second line.

## Standards every skill inherits (from repe-core)

Do not restate these in each skill. Refer to them.

- Data order: user data, then connected sources, then public sources.
- Every figure carries a source tag: `[User]`, `[Connected]`, `[Public]` or `[Assumed]`.
- Cash and capital carry a status: Actual, Committed, Expected or Assumed.
- Conflicts between sources are shown, with the one used.
- Math comes from the workbook or a script, never from free text.
- Excel outputs are live formulas. Underwriting workbooks come from the `underwriting-model` skill.
- Screens end in a verdict: Pursue, Watch or Pass, with a 1 to 10 conviction score.
- Each run ends with a dated decision record and, where relevant, a deal log row.
- Personal data in source documents is read, never stored or sent anywhere.
- Outputs are drafts for professional review. Legal and tax points are flagged for counsel or a CPA.

## Reference files

- Live in `skills/<skill>/references/`. Markdown only. Under 200 lines each.
- Templates use blank tables and bracketed placeholders, never real names or numbers.
- Property-type knowledge belongs in the playbooks in `repe-core`, not in individual skills.

## Commands

One file per skill in `commands/`, same pattern as Anthropic's:

```
---
description: <one line, under 80 characters>
argument-hint: "[what to pass]"
---

Load the `<skill>` skill and <one sentence on the job>.

If <input> is provided, use it. Otherwise ask the user for <what is needed>.
```

## What never goes in the repo

- Client names, real deals, real people, or real financials. Examples are synthetic.
- Binary files (xlsx, pdf, zip). Workbooks are generated at run time.
- Secrets, credentials, or network calls in scripts.
