# Engine standard: lease-based commercial properties

For office, medical office, industrial, retail, net lease, life science and data centers. Read with `model-standard.md`. These are the practices an experienced commercial underwriter expects. How the workbook implements them is open.

## Revenue

- **Model every lease on its own terms.** Each lease carries its own start, expiry, area, base rent, bump schedule (fixed, percentage or index-linked), free rent, and options. Rent comes from the leases. An average rent per square foot hides the plan.
- **Free rent and abatements are dated.** Show them in the months they occur. Contract rent and cash rent differ until they burn off, and lenders and buyers will both ask which one the model is showing.
- **Read the options and use them deliberately.** Renewal options at a fixed rate or a share of market rent change what happens at expiry. Expansion, contraction and purchase options belong in the model if they could be exercised during the hold.
- **Termination rights are a rollover date.** Where a tenant can leave early by paying a fee, test the case where it does, and record the fee as one-time income.
- **Tenant credit drives risk.** Record each major tenant's credit, guarantor and security deposit or letter of credit. Concentration in one tenant or one industry is a finding in its own right.

## Rollover

- **Every expiry is a decision tree.** Weight renewal and new-tenant outcomes by a renewal probability, or model the cases separately when one tenant moves the result. State the probability and the reason for it.
- **New tenants cost more than renewals.** Downtime, free rent, tenant improvements and leasing commissions differ between the two. Carry separate assumptions for each, and blend them by the renewal probability.
- **Re-lease at market rent at that future date**, grown from today's market rent, with the market lease term and bump structure. The new lease then rolls again if it expires inside the hold or the exit year.
- **Follow space through more than one rollover.** Short leases and long holds produce second and third expiries. Each carries its own downtime and leasing cost.
- **Vacant space leases up on a schedule**, with absorption timing, market terms and full leasing costs. Do not assume it fills at closing.
- **Show rollover exposure by year**, by rent and by area, with the weighted average lease term at entry and at exit.

## Recoveries and other income

- **Rebuild recoveries from the leases.** Gross, modified gross, base year, expense stop and triple net leases each recover differently. Apply each lease's structure, its pro rata share, any gross-up for occupancy, and any caps on controllable expenses or administrative fees.
- **Reset base years at rollover.** A new lease brings a new base year or stop, which usually cuts recoveries for a time.
- **Tie recoveries to the expense lines that are recoverable.** If expenses rise, recoveries rise only as far as the leases allow. The owner keeps the leakage.
- **Retail needs more.** Model percentage rent from tenant sales above each breakpoint, and test co-tenancy and kick-out clauses that let tenants pay less or leave if an anchor goes dark. Track occupancy cost for tenants with sales reporting.
- **Parking, storage, signage, power and other income** are underwritten from contracts and history. Data center power and cooling pass-throughs follow the contract terms.

## Vacancy and credit loss

- **Add a general vacancy and credit loss on top of scheduled rollover.** Rollover downtime covers known expiries. A general allowance covers the unknown: defaults, early exits and collection loss. Do not double count, and do not apply the allowance to space already modeled as vacant.
- **Exempt or reduce the allowance for credit tenants on long leases** only when the evidence supports it, and say why.

## Expenses and capital

- **Expenses follow the same discipline as `standard-unit.md`**: reassessed property tax, insurance on its own line, a market management fee, and normalized trailing figures.
- **Tenant improvements and leasing commissions sit below NOI**, timed with each lease. They are the largest capital cost in most office and retail deals.
- **Carry building capital and a reserve** for roofs, structure, systems and parking, below NOI. Life science and data center buildings carry heavy systems that wear on their own schedule.

## Debt

- **Size on the lender's NOI**, which may mark leases to market, strip out tenants near expiry, or apply the lender's own vacancy.
- **Model cash management triggers.** Coverage or debt yield tests, a major tenant giving notice, going dark or filing for bankruptcy can trap cash or sweep it to a leasing reserve. Test when each trigger could fire, especially in the years of heavy rollover.
- **Model required leasing reserves** funded at closing or monthly, and show when they can be drawn.
- **Line up debt maturity against rollover.** A loan that matures in a heavy rollover year is a refinance risk to name.

## Exit

- **Value the forward NOI a buyer will underwrite.** Capitalize the year after the sale. Then adjust for what that buyer will see: near-term expiries, below-market or above-market leases, free rent still to burn off, and leasing cost still to spend.
- **When rollover falls just after the exit**, deduct the expected leasing cost and downtime from value, or use a discounted cash flow for the exit, and state which.
- **Single-tenant and net lease assets carry residual value risk.** Value depends on remaining term and tenant credit. Model a case where the tenant does not renew: dark value, re-tenanting cost and time, or alternative use.

## Returns

- **Returns follow `standard-unit.md`**: date-based IRR, equity multiple, cash on cash on operating cash only, and a waterfall matched to the operating agreement.
- **Show returns with and without the key tenant renewing** when one lease drives the result.

## Checks specific to this engine

| Check | Passes when |
|-------|-------------|
| Rent roll tie | Modeled in-place rent and area equal the rent roll at the start date |
| Area | Leased plus vacant area equals rentable area every period |
| Lease abstracts | Bumps, free rent, options and recovery terms match the leases or abstracts |
| Recovery logic | Recoveries never exceed recoverable expenses, and base years reset at rollover |
| Leasing cost | Tenant improvements and commissions appear in the month each new or renewal lease starts |
| Rollover | Every lease expiring in the hold or exit year has a modeled outcome |
| Credit loss | General vacancy is not applied to space already modeled as vacant |
| Exit | Exit NOI reflects near-term rollover and mark to market, or the adjustment is shown |
