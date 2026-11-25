---
name: underwriting-model
description: Produces an institutional-grade real estate underwriting model in Excel. Fills the firm's own template or builds a live-formula workbook to the plugin's model standard, then audits it. Covers the revenue build, debt sizing, returns, waterfall inputs, sensitivities and maximum bid, with a quick screening model for first looks. Use when a deal needs returns, a loan size or a bid price. Triggers on "underwrite this deal", "build the model", "fill in our model", "size the debt", "max bid", or "audit this model".
---

# Underwriting Model

## Workflow

### Step 1: Load Standards and Pick the Path

Load the `repe-core` skill and follow `references/standards.md`.
Identify the property type and read its playbook in `references/playbooks/`.

| Path | Use when | What happens |
|------|----------|--------------|
| Firm template | The user provides or has a model template | Fill it. Keep its structure and conventions |
| Build to standard | No template, and the decision needs a full model | Build a workbook that meets the model standard |
| Quick screen | First look, triage or maximum bid | Build a compact annual workbook to the quick screen standard |

Check for a template first. If none is attached, ask once whether the firm has one.

### Step 2: Read the Model Standard

Read `references/model-standard.md`, then the engine standard for the property type.

| Engine | Property types | Standard |
|--------|----------------|----------|
| Unit-based | Multifamily, student, single-family rental, manufactured, affordable | `references/standard-unit.md` |
| Lease-by-lease | Office, medical office, industrial, retail, net lease, life science, data centers | `references/standard-lease.md` |
| Operating | Hotels, seniors housing, self-storage | `references/standard-operating.md` |
| Development | Ground-up and heavy redevelopment | `references/standard-development.md` |
| For-sale | Condos, townhomes, lots | `references/standard-for-sale.md` |

The standards describe outcomes and tests. The method is yours to choose.

### Step 3: Produce the Model

**Firm template**
- Work on a copy. Never restructure, rename or rebuild the template.
- Map the deal's inputs into the template's input cells. Complete missing formulas in the template's own style.
- Where the template differs from the model standard, keep the template and note the difference for the reviewer.

**Build to standard**
- Build the workbook with live formulas, following the Excel standard in `repe-core`.
- Use monthly periods when timing drives value. Build revenue at the level income is earned.
- Include every item under "Required content" in the model standard that the decision needs.

**Quick screen**
- Follow `references/quick-screen-standard.md`. Save as `<deal>-quick-screen-<yyyymmdd>.xlsx`.
- Fill gaps from the buy box and tag each one `[Assumed]`.

For raw documents, run `rent-roll-t12-analysis` first. Use placeholders for tenant names.

### Step 4: Audit the Workbook

Run the mechanical audit in `references/audit-checklist.md` on any workbook, including a firm's own: error values, typed-over formulas, ties, check cells and an independent recompute of the headline returns.

Then apply the judgment tests from the model standard:

| Test | Question |
|------|----------|
| Flex | Do price, growth, exit cap and rate changes move outputs the right way, by a sensible amount? |
| Reconcile | Does in-place income tie to the rent roll and trailing statement? |
| Reasonable | Do growth, margins and exit pricing fit the evidence? |
| Downside | Does the downside still cover debt service and extension tests? |

Fix what fails and audit again. Report anything that still fails or needs review.

### Step 5: Answer the Six Questions

| Question | Answer from the model |
|----------|-----------------------|
| What is it worth to us? | Maximum price at the hurdle, versus ask |
| How much debt can it carry? | Loan amount and the binding test |
| What do we earn? | Unlevered, levered and investor net returns |
| What has to go right? | Top drivers and returns attribution |
| What if it does not? | Downside case and breakevens |
| How much cash, and when? | Peak equity and capital calls |

For the investor split, load `jv-waterfall`.

### Step 6: Output

- The workbook, with a note on which path produced it and the audit result.
- A one-page returns summary answering the six questions, base and downside.
- Every `[Assumed]` input, and every difference between a firm template and the model standard.

## Important Notes

- A firm's own model carries its history and its investors' expectations. Fill it and test it. Do not improve it uninvited.
- The standard sets what a good model proves, not how it is laid out. Choose the simplest build that proves it.
- A quick screen is annual and built for speed. Never present its result as a bid or a committee number.
- When exit cap rate movement supplies most of the profit, say so plainly. The deal then depends on the market more than on the plan.
- A model that ties can still be wrong. The reasonableness and downside tests matter more than the mechanical ones.
- If the workbook cannot be recalculated in this environment, say so and ask the user to open it in Excel and confirm the checks.
