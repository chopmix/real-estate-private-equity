# Deal log schema

One row per deal seen, passes included. Keep the log in the location named in `buy-box.md`. Add columns if the firm needs them, but do not remove these.

## Columns

| Column | Content |
|--------|---------|
| Log ID | [YYYY-MM-DD]-[sequence] |
| Date received | [date] |
| Source | [Broker, listing platform, direct owner, referral] |
| Source contact | [Broker or contact firm] |
| Property name | [name] |
| Address | [street, city, state] |
| Market and submarket | [market] / [submarket] |
| Property type and subtype | [type] / [subtype] |
| Size | [units, SF, keys or beds] |
| Vintage | [year built / year renovated] |
| Asking price | [$] |
| Price per unit or SF | [$] |
| In-place NOI | [$] [source tag] |
| In-place cap rate | [%] |
| Occupancy | [%] |
| Seller motive | [stated or inferred, or Not disclosed] |
| Call for offers date | [date] |
| Quick scan score | [1 to 10] |
| Deep screen | [Yes / No] |
| Maximum bid | [$] or [n/a] |
| Discount from ask | [%] or [n/a] |
| Verdict | [Pursue / Watch / Pass] |
| Reason | [one line] |
| Data quality | [Good / Fair / Poor] |
| Prior contact | [date and outcome, or None] |
| Owner | [deal team member] |
| Next step and date | [action] by [date] |
| Outcome | [Bid, LOI, Closed, Lost, Dead] and [final price if known] |

## Quick scan one-line format

One line per deal, ranked by score.

```
[Score]/10 | [Verdict] | [Property], [City] | [Type], [Size] | Ask [$] ([$ per unit or SF]) | Cap [%] on [in-place or pro forma] | [Top reason for the score] | [Key gap or hard-limit breach]
```

Example layout with placeholders:

```
[7]/10 | Watch | [Property name], [City] | [Type], [Units] units | Ask [$] ([$]/unit) | Cap [%] on in-place | [Below replacement cost] | [T-12 not provided]
```

## Rules

- Record the score as first given. If a later screen changes it, add a new row or note the change, so the log shows how views evolved.
- A hard-limit breach shows as Pass with the limit named in Reason.
- Never put tenant or resident names in the log.
