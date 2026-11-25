# Build spec

Real estate private equity plugin for Claude. Published by Chi Hathiramani, CH Consulting (Chirag Hathiramani Real Estate Consulting). Apache 2.0. Fully public.

## Decisions

| Decision | Answer |
|----------|--------|
| Audience | Client-ready, fully public, for owner-operators, fund managers, developers, allocators and family offices |
| Property types | All major types through three income engines plus development and for-sale |
| Excel | Live formulas, no macros, audited before delivery. Firm templates are filled, never replaced |
| Modeling | Standards and best practices guide to the outcome. The method is left to Claude |
| Data | User data, then connected sources, then public sources. Every figure tagged |
| Style | Matches Anthropic's financial-services skills: short, numbered steps, tables, brief notes |
| Out of scope for now | Lending and debt-fund underwriting, non-US markets, company-wide consolidation |
| Shared knowledge | Lives in the `repe-core` skill. Every other skill loads it first |

## Releases

| Release | Module | Skills |
|---------|--------|--------|
| 1 | Core | repe-core |
| 1 | Deals | deal-sourcing, deal-screening, rent-roll-t12-analysis, market-intelligence, underwriting-model, jv-waterfall, dd-checklist, site-visit-prep, ic-memo |
| 1 | Ownership | asset-business-plan, asset-management-review, platform-ai-readiness |
| 1 | Capital and oversight | liquidity-and-capital-needs, financing-decisions, decision-brief |
| 2 | Fund and investor | track-record, valuation-memo, lp-reporting, ddq-response, allocation-memo, manager-economics |
| 2 | Distress | workout-analysis, rescue-capital |
| 2 | Execution | capital-raise-package, sponsor-monitoring, construction-monitoring, leasing-decisions, offer-and-closing, property-tax-review |
| 3 | Later | disposition, hold-sell-refi, development-feasibility, continuation-vehicles |

## Skill briefs (Release 1)

Each brief lists what the skill must cover. Write to `docs/authoring-standard.md`.

### deal-sourcing
- Two modes. Outbound: build an owner and broker target list from the buy box using public triggers (loan maturities, long holds, tax-roll ownership, permits, distress signals). Inbound: read listing-platform and broker emails the user has connected, extract each listing, and pass it to `deal-screening` as a batch.
- Check the firm's deal log and CRM for prior contact before outreach.
- Draft short, specific outreach for the user to review. Never send.
- Output: ranked target list or daily inbound digest, plus deal log rows.

### deal-screening
- Two tiers. Quick scan scores every deal 1 to 10 using the buy box weights. Deep screen only for deals at or above the firm's threshold.
- Extract facts table: property, type, size, price, price per unit or SF, in-place NOI and cap rate, occupancy, vintage, seller motive, broker.
- Tests table against buy box: target, actual, pass or fail.
- Back-of-envelope returns and maximum bid for the hurdle, with the discount from ask. Hand to `underwriting-model` in quick mode.
- Verdict Pursue, Watch or Pass, conviction score, data quality grade, bull case, bear case, first-call questions, next steps.
- Optional investor-fit lens: cash yield, depreciation and cost segregation potential, flagged for CPA.
- Output: one-page screening memo and a deal log row. Reference file: deal log schema and quick scan format.

### rent-roll-t12-analysis
- Normalize the rent roll and trailing 12-month statement into the standard layout for the property type's engine.
- Unit-based: unit mix, in-place vs market rent, loss to lease, lease expirations, concessions, delinquency, renovated vs classic.
- Commercial: lease table, WALT, rollover by year, mark to market, tenant concentration, recoveries, options, co-tenancy.
- Operating: revenue per available unit trend, departmental margins, seasonality.
- T-12: trend by line, one-time items, normalize management fee, reserves, payroll, insurance, and property tax after reassessment.
- Reconcile the rent roll to T-12 collections. Flag gaps.
- Output: analysis memo with findings, adjusted NOI bridge (reported to underwritten), and the model input file for `underwriting-model`. Tenant names stay in the user's file only.

### market-intelligence
- Part 1, submarket read: rent, vacancy and absorption trends, supply pipeline, recent trades, employers, from broker reports, local press and public records.
- Part 2, property file: news on the asset, owner and major tenants, sale and loan history, code violations, litigation, online reviews.
- Playbook decides emphasis: reviews for residential, hotels, seniors and storage. Tenant news for office, industrial and retail.
- Sale and rent comp tables with source and date.
- Follow public research rules in standards. State what could not be found.
- Output: market and property brief with a red flag list and questions for the site visit.

### dd-checklist
- Scope by property type, deal type (acquisition, recapitalization, development), and debt.
- Workstreams: title and survey, environmental, property condition, zoning and entitlements, leases and estoppels, financial, tax, insurance, service contracts, legal and entity, loan documents, property-type additions from the playbook.
- Status tracking: requested, received, reviewed, issue, cleared. Owner and due date per item.
- Red flag summary with severity and effect on price or terms. Critical dates: diligence expiry, deposit hard date, closing.
- Output: tracker workbook rows and a one-page status summary. Reference file: checklist by workstream.

### site-visit-prep
- Prepare for a property tour, property manager interview, broker call, lender call or seller meeting.
- Question lists by audience, drawn from the playbook and open items from screening, market-intelligence and the checklist.
- Things to observe on site: deferred maintenance, unit or suite condition, competing properties, traffic and access.
- Red flags to probe and the evidence that would close each.
- Output: a two-page prep sheet and a blank notes template for the visit.

### ic-memo
- Gather outputs from screening, rent-roll-t12-analysis, market-intelligence, underwriting-model, jv-waterfall and dd-checklist. List what is missing.
- Structure: recommendation and terms, property and business plan, market, financial analysis, capital structure and returns (gross and net), risks and mitigants, diligence status, exit, open items.
- Every number traces to the workbook. Sensitivities and downside case included.
- States the verdict against the buy box. The committee makes the decision.
- Output: IC memo document plus decision record. Reference file: memo template.

### asset-business-plan
- Baseline: in-place NOI, occupancy, rents vs market, capital needs, debt terms.
- Levers by playbook: revenue, expense, capital program, lease-up, repositioning.
- NOI bridge from in-place to stabilized, with each lever sized, timed and owned.
- First 100 days after takeover. Capital budget and schedule.
- KPIs with targets and the trigger that prompts a hold, sell or refinance review.
- Output: business plan document and plan inputs for the workbook.

### asset-management-review
- Ingest the monthly or quarterly property package (financials, rent roll, leasing, delinquency, capital).
- Budget vs actual by line with variance explained as timing or permanent, and price or volume.
- Actual vs underwriting and vs business plan.
- Leasing and occupancy trend, delinquency, capital project status.
- Debt: DSCR, debt yield, covenant headroom, cash management triggers, rate cap expiry, maturity.
- Local watch: reviews, new supply, tenant news (from market-intelligence).
- Output: asset scorecard, variance table, issues with owner and date.

### liquidity-and-capital-needs
- For one asset, project or vehicle. Not company-wide consolidation.
- 13-week cash forecast: opening cash, receipts, operating payments, debt service, capital, taxes, insurance, distributions.
- Sources and uses reconciliation for a project: invoice-level uses, draws available, equity received.
- Label every inflow Actual, Committed, Expected or Assumed. Only Actual and Committed count toward coverage.
- Funding gap by date, the first shortfall, and options: defer, draw, raise, bridge, sell. Show the cost and risk of each.
- Output: cash schedule workbook rows, a one-page funding summary, and decisions needed with owner and date.

### financing-decisions
- Compare lender term sheets on one basis: proceeds, rate and index, spread, floor, term, interest-only period, amortization, fees, prepayment, recourse and guarantees, covenants, reserves, cash management, conditions, timing and certainty of close.
- All-in cost and annual debt service for each, and the effect on cash on cash and levered IRR via `underwriting-model`.
- Refinance analysis: payoff and prepayment cost, new proceeds, cash out or cash in, break-even hold.
- A term sheet is not a commitment. List conditions that must clear.
- Output: comparison table, recommendation against the firm's leverage limits, questions for each lender.

### decision-brief
- Turn a tracker, emails, meeting notes or transcripts the user provides into a weekly brief for a principal.
- Lead with decisions needed: issue, what changed, recommendation, strongest alternative, owner, date, evidence link.
- Separate confirmed facts from estimates. Label cash by status.
- Advice ledger: what was flagged, what was recommended, the decision, the result.
- Open items table: matter, position, next result, owner.
- Output: a brief of two pages or less. Reference file: brief template.

### platform-ai-readiness
- Scan the firm's functions (acquisitions, asset management, property operations, finance, investor relations, development) and its assets for the highest-value AI uses.
- Per function: current process, data available, quick win, effort, value, risk.
- Rank across the firm. Find the ones that repeat across assets.
- Focus on clarity and faster decisions first, then automation.
- Output: ranked action list with owner and first step.

## Playbook template

Each playbook in `skills/repe-core/references/playbooks/` uses these sections, 90 to 150 lines:

1. What it is (subtypes in one table)
2. How income is produced (which engine, lease structure)
3. Key metrics (table: metric, how to compute, why it matters)
4. Revenue drivers
5. Expense drivers (include property tax and insurance)
6. Capital needs
7. Debt and lender view (who lends, which sizing test usually binds, structural quirks)
8. Screening quick tests
9. Diligence additions (beyond the standard checklist)
10. Red flags
11. Value levers
12. Local intelligence (which public sources and signals matter)
13. Model inputs to capture
14. Site visit and management questions

No dated market statistics. Rules of thumb only when labeled "rule of thumb, verify locally".

## Modeling approach

Models keep improving, so the plugin sets the standard and checks the result. It does not hard-wire one way to build a model. This follows the pattern in Anthropic's own modeling skills.

| Layer | Where | Role |
|-------|-------|------|
| Model standard | `skills/underwriting-model/references/` | What an institutional-grade model must prove, by engine. Outcomes and tests, not a layout |
| Firm template path | `underwriting-model` skill | Fill the firm's own model and test it against the standard |
| Auditor | `scripts/audit_workbook.py` | Mechanical tests on any workbook: errors, typed-over formulas, ties, independent return recompute |
| Quick screening model | `scripts/repe_model.py` | Annual first-look workbook for screens and maximum bids. Not a full model |

Engine standards: unit-based, lease-by-lease, operating, development, for-sale, plus a waterfall standard in `jv-waterfall`.

## Publishing

- Plugin folder is the repository root. Text files only. No binaries.
- Plugin name `real-estate-private-equity`, mirroring Anthropic's `private-equity`. The name is permanent once submitted. If review holds it as too generic, the fallback is `ch-real-estate-private-equity`.
- Submit from the CH Consulting Claude account at claude.ai/directory/manage.
