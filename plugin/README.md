# Real Estate Private Equity for Claude

For acquisitions, asset management and capital teams at real estate investment firms. Screen a deal in minutes, underwrite it in your own model, run diligence, write the IC memo and keep every asset on plan. It covers every major property type and fits owner-operators, fund managers, developers, allocators and family offices.

Created by Chi Hathiramani, CH Consulting. See [About and contact](#about-and-contact).

> Nothing here is investment, legal, tax or accounting advice. The plugin drafts analyst work product for review by a qualified professional. It does not make investment recommendations, send messages, move money or sign anything. You are responsible for verifying outputs.

## What it does

| Module | Skill | What you get |
|--------|-------|--------------|
| Core | `repe-core` | Shared standards, firm buy box, formulas, Excel standard, property-type playbooks |
| Deals | `deal-sourcing` | Target lists and a daily digest of inbound listings |
| Deals | `deal-screening` | One-page screen with verdict, conviction score and maximum bid |
| Deals | `rent-roll-t12-analysis` | Normalized rent roll and trailing financials, adjusted NOI |
| Deals | `market-intelligence` | Submarket read and a property file from public sources |
| Deals | `underwriting-model` | Institutional model in your template or built to standard, audited. Quick screen for first looks |
| Deals | `jv-waterfall` | Preferred return, hurdles, promote, investor net returns |
| Deals | `dd-checklist` | Diligence tracker by workstream with red flags |
| Deals | `site-visit-prep` | Questions and observation list for tours and calls |
| Deals | `ic-memo` | Investment committee memo tied to the model |
| Ownership | `asset-business-plan` | NOI bridge, capital plan, first 100 days |
| Ownership | `asset-management-review` | Budget vs actual, leasing, covenants, issues |
| Ownership | `platform-ai-readiness` | Ranked AI opportunities across the firm |
| Capital | `liquidity-and-capital-needs` | 13-week cash, sources and uses, funding gap |
| Capital | `financing-decisions` | Lender term sheet comparison and refinance analysis |
| Oversight | `decision-brief` | Weekly brief of decisions with owner, date and evidence |

## Property types

One set of skills covers all of them. Each skill reads the playbook for the property in front of it.

- Unit-based: multifamily, student housing, single-family rental and build-to-rent, manufactured housing, affordable housing
- Lease-by-lease: office, medical office, industrial, retail, net lease, life science, data centers
- Operating businesses: hotels, seniors housing, self-storage
- Development and for-sale: land and development, for-sale housing, mixed-use
- Overlays: Opportunity Zones, HUD and agency debt

## Use it

1. Ask Claude to set up your buy box. It saves your criteria, hurdles and default assumptions for every later run.
2. Attach a document and ask in plain words: "screen this deal", "analyze this rent roll", "build the model", "write the IC memo", "review this month's package".
3. In Claude Code and Cowork you can also use slash commands such as `/real-estate-private-equity:screen-deal` and `/real-estate-private-equity:underwrite`.

## Examples

Three requests that show the core of the plugin:

1. Attach an offering memorandum and say: "Screen this deal against our buy box and give me a maximum bid."
2. Attach a rent roll and a trailing 12-month statement and say: "Analyze these and show me the adjusted NOI."
3. Attach your firm's model and the deal documents and say: "Fill in our underwriting model for this deal and audit it."

## How it works

- **Your data first.** Skills work from the documents you provide, then systems you have connected, then public sources. Every figure is tagged with where it came from.
- **Your model first.** If your firm has its own underwriting template, Claude fills it and keeps its structure. If not, Claude builds a live-formula workbook to the plugin's model standard.
- **Standards, not scripts.** The model standard sets what an institutional-grade model must prove for each property type, and leaves the method open so results improve as Claude does.
- **Audited.** Claude checks any workbook for errors, typed-over formulas and ties, and recomputes headline returns independently before delivery.
- **Quick screen.** A compact annual model gives a first look and a maximum bid in minutes. It is a screen, not a full model.
- **A record of every decision.** Each run ends with a dated record, and screens add a row to your deal log.

## Author credit in workbooks

When the plugin builds a new workbook, it adds one credit line at the end of the Sources sheet: "Model standard: Real Estate Private Equity plugin by Chi Hathiramani, CH Consulting (chiraghathiramani.com)". This is the only place the plugin adds the author's name to your work. You are free to delete it. The plugin adds no credit to your firm's own template, your memos, your investor materials or any other output.

## Data handling

- The plugin has no servers and no connectors of its own. It sends nothing to CH Consulting or any third party.
- The plugin contains only instructions and reference files. It ships no code. When a task needs a calculation or a workbook, Claude writes and runs what it needs inside your own Claude workspace.
- Public research uses Claude's own web search when your Claude setup allows it. Without web access the skills still run and say what they could not check.
- Rent rolls and similar documents can contain personal data. The skills read it to do the analysis and do not store it or send it anywhere.
- Your buy box, deal log and outputs stay in your own workspace.

## Troubleshooting

- **A skill does not start.** Name the task in plain words, such as "screen this deal", or ask Claude which skills it has from this plugin.
- **Claude asks for your criteria every time.** Ask it to set up your buy box once. It saves the file and reads it on later runs.
- **A workbook shows a failed check.** Ask Claude to audit the workbook and list what failed and where.
- **Public research is missing.** Web access may be off in your Claude settings. The skills say what they could not check.

## Limits

- A quick screen is annual. Full models, including monthly, development and for-sale, are built to the model standard or in your own template.
- Real estate lending and debt-fund underwriting are not covered yet.
- United States conventions.

## Roadmap

Fund and investor reporting, track record, valuation memos and due diligence questionnaire responses; workout and rescue capital analysis; capital raise packages; sponsor monitoring; construction monitoring; leasing decisions; disposition.

## Feedback and requests

I built this for teams like yours, and I want it to keep getting better. If you spot an error, see something missing, or want a skill or a property type added, send me a note. I read every message and I'm glad to make changes.

- Email: chi@chiraghathiramani.com
- Website: https://chiraghathiramani.com
- Or open an issue on the GitHub repository

Chi Hathiramani

## About and contact

Built and maintained by Chi Hathiramani (Chirag Hathiramani), founder of CH Consulting (Chirag Hathiramani Real Estate Consulting), a strategic advisor to real estate investment firms with about 20 years of principal-side experience.

- Contact: Chi Hathiramani
- Website: https://chiraghathiramani.com
- Email: chi@chiraghathiramani.com

Questions about setup or how a skill works are welcome.

## Privacy and security

See `PRIVACY.md`. To report a security concern, email chi@chiraghathiramani.com.

## License

Apache 2.0. See `LICENSE` and `NOTICE`. Examples are synthetic and describe no real property, firm or person.
