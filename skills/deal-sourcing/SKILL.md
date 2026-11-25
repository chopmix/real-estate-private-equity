---
name: deal-sourcing
description: Finds acquisition opportunities that fit the firm's buy box, either by building an outbound owner and broker target list from public triggers or by turning connected listing and broker emails into a daily inbound digest. Produces a ranked target list or digest, draft outreach for review, and deal log rows. Use when building a pipeline, working a target market, or clearing listing alerts. Triggers on "find us deals", "build a target list", "who owns these properties", "go through my listing emails", or "source off-market deals".
---

# Deal Sourcing

## Workflow

### Step 1: Load Standards and Set the Mode

Load the `repe-core` skill and follow `references/standards.md`.
Identify the property type and read its playbook in `references/playbooks/`.

Then confirm:

- **Mode**: Outbound (find owners to approach) or Inbound (process listings already received)
- **Buy box**: Markets, property types, size, vintage and risk profile from `buy-box.md`
- **Scope**: Submarkets or ZIP codes, number of targets wanted, time window for inbound mail
- **Where the deal log and CRM live**, so prior contact can be checked

### Step 2: Outbound - Build the Target Universe

Pull candidate properties inside the buy box from tax rolls, deed records and connected data, then score each against public triggers.

| Trigger | Where to look | Why it matters |
|---------|---------------|----------------|
| Loan maturity within 24 months | Recorded mortgages, CMBS data, connected debt data | Owner must refinance or sell |
| Long hold (rule of thumb 7+ years, verify locally) | Deed transfer date | Owner has gains and may be ready |
| Ownership change at the entity level | Secretary of state filings, estate records | New decision maker |
| Permits filed or stalled | City permit portal | Capital plan in motion or stuck |
| Distress signals | Tax delinquency, liens, lis pendens, code cases | Motivated seller |
| Rising vacancy or poor reviews | Listing sites, review sites | Operating fatigue |

- Resolve each owning entity to a decision maker and a mailing address where the record allows.
- Note the listing broker or local broker most active in the submarket for each target.

### Step 3: Inbound - Extract Listings

Read listing-platform alerts and broker emails the user has connected, within the stated window.

| Field | Content |
|-------|---------|
| Property and address | |
| Type and size (units or SF) | |
| Asking price and price per unit or SF | |
| Stated NOI and cap rate | |
| Occupancy | |
| Broker and firm | |
| Call for offers date | |
| Source email and date | |

- Drop duplicates across platforms and brokers. Keep the earliest source.
- Drop anything outside a hard limit in the buy box, with the reason.
- Pass the remaining listings to `deal-screening` as a batch for quick scan scores.

### Step 4: Check Prior Contact and Draft Outreach

- Search the deal log and CRM for each property, owner and broker. Record last contact, outcome and who owns the relationship.
- Skip owners marked do-not-contact or already in active talks with a colleague.
- Draft outreach for the top targets: three to five sentences, the specific reason for reaching out (the trigger), what the firm buys, and a clear ask for a call.
- Drafts go to the user for review. Never send, schedule or post anything.

### Step 5: Output

| Mode | Deliverable |
|------|-------------|
| Outbound | Ranked target list: property, owner, decision maker, trigger, score, prior contact, broker, draft outreach |
| Inbound | Daily digest: listings ranked by quick scan score, with call for offers dates and those dropped with reasons |

Add one deal log row per new property using the schema in `deal-screening/references/deal-log-schema.md`, then the decision record from the standards.

## Important Notes

- One strong trigger beats three weak ones. A maturing loan on a long-held asset is worth more than a list of every old deed.
- The tax roll mailing address is often a management company or attorney. Confirm the decision maker before drafting outreach.
- Outreach that names the property and the reason lands. Generic "we are active buyers" letters get filed.
- Inbound volume hides the good deals in plain sight. Rank by fit, not by arrival time, and track call for offers dates so nothing expires unread.
- Respect relationships. If a broker brought the firm a deal, do not go around them to the owner.
- Owner names and contact details are personal data. Keep them in the user's workspace and follow local rules on unsolicited contact.
