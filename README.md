# Real Estate Private Equity for Claude

Skills that take a real estate investment from first look to ownership: sourcing, screening, underwriting, diligence, investment committee, asset management and capital decisions. Built for owner-operators, fund managers, developers, allocators and family offices, across every major property type.

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

## How it works

- **Your data first.** Skills work from the documents you provide, then systems you have connected, then public sources. Every figure is tagged with where it came from.
- **Your model first.** If your firm has its own underwriting template, Claude fills it and keeps its structure. If not, Claude builds a live-formula workbook to the plugin's model standard.
- **Standards, not scripts.** The model standard sets what an institutional-grade model must prove for each property type, and leaves the method open so results improve as Claude does.
- **Audited.** An auditor checks any workbook for errors, typed-over formulas and ties, and recomputes headline returns independently.
- **Quick screen.** A bundled annual model gives a first look and a maximum bid in minutes. It is a screen, not a full model.
- **A record of every decision.** Each run ends with a dated record, and screens add a row to your deal log.

## Data handling

- The plugin has no servers and no connectors of its own. It sends nothing to CH Consulting or any third party.
- It runs Python scripts bundled in `skills/underwriting-model/scripts/` to build and check Excel workbooks. The scripts use the `openpyxl` library, make no network calls, and optionally call LibreOffice on the same machine to recalculate a workbook. If `openpyxl` is not installed, Claude installs it from the Python package index before building.
- Public research uses Claude's own web search when your Claude setup allows it. Without web access the skills still run and say what they could not check.
- Rent rolls and similar documents can contain personal data. The skills read it to do the analysis and do not store it or send it anywhere.
- Your buy box, deal log and outputs stay in your own workspace.

## Limits

- The bundled quick screening model is annual and covers income properties. Full models, including monthly, development and for-sale, are built to the model standard or in your own template.
- Real estate lending and debt-fund underwriting are not covered yet.
- United States conventions.

## Roadmap

Fund and investor reporting, track record, valuation memos and due diligence questionnaire responses; workout and rescue capital analysis; capital raise packages; sponsor monitoring; construction monitoring; leasing decisions; disposition. See `docs/build-spec.md`.

## About and contact

Built and maintained by Chi Hathiramani (Chirag Hathiramani), founder of CH Consulting (Chirag Hathiramani Real Estate Consulting), a strategic advisor to real estate investment firms with about 20 years of principal-side experience.

- Contact: Chi Hathiramani
- Website: https://chiraghathiramani.com
- Email: chi@chiraghathiramani.com

For help tailoring the plugin to your firm, setting up your buy box, or connecting your systems, get in touch.

## License

Apache 2.0. See `LICENSE` and `NOTICE`. Examples are synthetic and describe no real property, firm or person.
