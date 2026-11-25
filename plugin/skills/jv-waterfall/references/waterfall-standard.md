# Waterfall standard

What a distribution waterfall must get right. Read with `underwriting-model/references/model-standard.md` and the waterfall terms in `repe-core/references/metrics-and-formulas.md`. These are the practices an experienced fund controller or investment committee expects. How the workbook implements them is open.

## Start with the agreement

- **Read the operating agreement first and model what it says.** The agreement governs over market convention and the term sheet. Abstract each economic term with its section reference before building.
- **Where the agreement is silent or unclear, say so.** Model the most reasonable reading, show the alternative, and flag the point for counsel.
- **Use the agreement's definitions.** Capital contributions, distributable cash, capital events and the preferred return are defined terms. Use them exactly.

## Capital accounts

- **Track contributions and distributions by member and by class**, with dates. Unreturned capital and accrued but unpaid preferred return are running balances, rolled every period.
- **Sponsor co-invest is pro rata capital.** It earns the same returns as investor capital, in the same tiers. Promote is separate and paid on top. Never blend the two.

## Preferred return

- **Match the agreement on four points**: simple or compounding, compounding frequency, the accrual start (usually each contribution's date), and the base (unreturned capital, or unreturned capital plus unpaid preferred return).
- **Pay accrued preferred return before return of capital** unless the agreement reverses the order.
- **Accrue on actual dates** when contributions and distributions are dated. Period-end approximations move the result.

## Tiers, hurdles and promote

- **Define each hurdle as the agreement does**: IRR, equity multiple, or both, and if both, whether the greater or the lesser governs.
- **Measure the hurdle on the right cash flows**: which members, which classes, and whether fees count. Use dated cash flows.
- **Fill one tier before the next begins.** Within each tier, split cash by the stated percentages until the hurdle is exactly met, then move up.
- **Model the catch-up** if there is one: the sponsor's share, the target it catches up to, and whether it applies to the preferred return alone or to all profit.
- **Model clawback and lookback provisions.** If promote paid early would exceed what the sponsor earns over the life of the deal, show the amount owed back and when it is tested. Note any tax distributions netted against it. Flag tax points for a CPA.

## Operating and capital event cash

- **Run operating cash and capital event cash through the waterfalls the agreement sets.** Many agreements pay operating cash pro rata or to preferred return only, and reserve promote for capital events. Some use one waterfall for all cash.
- **Define distributable cash**: after debt service, reserves, and fees the agreement puts ahead of distributions.

## Fees

- **List every fee with its base and timing**: acquisition, asset management, construction or development management, financing, and disposition. Asset management may be based on committed capital, invested capital, or asset value. Show which.
- **State whether each fee is paid before the waterfall** as a project expense, or from the sponsor's share. Fees paid ahead of the waterfall reduce investor returns and belong in the gross to net bridge.

## Capital calls and default

- **Model capital calls after closing** for shortfalls, capital plans or debt paydown, with each member's share.
- **Model default remedies the agreement allows**: dilution, a punitive conversion, a member loan at a penalty rate, or loss of promote. Show the effect on each member's share.

## Structures above the property

- **Model each vehicle that sits between the property and the investor**: a joint venture, a fund or feeder, a preferred equity class. Run each layer's waterfall on the cash it receives from the layer below.
- **Keep classes separate.** Preferred equity, common equity and different investor classes carry their own terms and order.

## Crystallization and removal

- **Model crystallization** if the agreement allows the promote to be valued and paid on a set date without a sale, with the valuation method stated.
- **Model the effect of sponsor removal** for cause or without cause: forfeiture or buyout of promote, and fee changes.

## Gross to net

- **Show the bridge** from property-level returns, to venture returns, to investor returns after fees and promote, in IRR and multiple. Name each step's cost.

## Checks specific to this engine

| Check | Passes when |
|-------|-------------|
| Cash tie | Total distributions equal cash available for distribution, every period |
| Capital | Capital returned to each member never exceeds capital contributed |
| Hurdles | When a tier is exactly filled, the measured IRR or multiple equals the hurdle |
| Tier order | No cash reaches a tier until every tier below it is filled |
| Pro rata | Sponsor co-invest receives the same return as investors on its capital, apart from promote |
| Accrual | Preferred return matches the agreement's compounding, frequency and start date |
| Fees | Each fee ties to its stated base, and fees ahead of the waterfall appear in the bridge |
| Agreement map | Every modeled term cites its section, and every open question is listed for counsel |
