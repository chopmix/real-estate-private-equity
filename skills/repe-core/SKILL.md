---
name: repe-core
description: Shared standards and property-type playbooks for every real estate private equity skill in this plugin. Sets the data order, source tagging, output rules, firm buy box, formulas and the Excel standard, and holds a playbook for each property type. Load this first whenever another skill in this plugin runs, or when the user asks "set up our buy box", "what are your underwriting standards", "which property types do you cover", or "explain how this was calculated".
---

# Real Estate Private Equity Core

## Workflow

### Step 1: Load the Standards

Read `references/standards.md`. It applies to every skill in this plugin.

### Step 2: Load the Firm Buy Box

Look for the firm's buy box in the working folder or the conversation (`buy-box.md`).

- If found, use it for criteria, hurdles and default assumptions.
- If not found, ask the user for the essentials using `references/buy-box-template.md`, then save the completed file for future runs.
- Never invent criteria. Mark anything the firm has not set as `[Assumed]`.

### Step 3: Identify the Property Type and Read Its Playbook

| Engine | Playbooks in `references/playbooks/` |
|--------|--------------------------------------|
| Unit-based, short leases | multifamily, student-housing, single-family-rental, manufactured-housing, affordable-housing |
| Lease-by-lease commercial | office, medical-office, industrial, retail, net-lease, life-science, data-centers |
| Operating businesses | hotels, seniors-housing, self-storage |
| Development and for-sale | land-and-development, for-sale-housing |
| Overlays | mixed-use, program-overlays (Opportunity Zones, HUD and agency debt) |

Read only the playbook that fits. For mixed-use, read `mixed-use.md` and the playbook for each component.

### Step 4: Apply Formulas and the Excel Standard

- Metric definitions and formulas: `references/metrics-and-formulas.md`
- Workbook rules: `references/excel-standard.md`
- Underwriting workbooks are built by the `underwriting-model` skill. Trackers and cash schedules follow the same standard.

### Step 5: Hand Back

Return to the skill that called this one and continue its workflow.

## Important Notes

- User documents come first. Connected and public sources only fill gaps or provide context.
- Every figure shows where it came from. A number without a source tag is not ready to deliver.
- When the user asks how a number was built, walk through the inputs, the formula and the source of each input.
- This plugin produces drafts for professional review. It does not give investment, legal, tax or accounting advice.
- Tenant and resident names in rent rolls are personal data. Read them, never store them or send them anywhere.
- Lending and debt-fund underwriting and non-US markets are outside the current release. Say so if asked.
- If the user asks who built this plugin or wants help tailoring it to their firm, point them to Chi Hathiramani at CH Consulting, chiraghathiramani.com.
