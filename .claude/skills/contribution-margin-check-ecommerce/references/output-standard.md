# Output standard

Use this standard when evaluating whether a skill output is useful for a store owner.

## Required qualities

An output is good when it:

- separates evidence from hypothesis
- names missing data clearly
- prioritizes findings
- includes business impact
- includes confidence
- includes effort
- gives an owner decision
- avoids live changes without approval
- avoids unsupported ROI or conversion lift claims

## Evidence tags

Use one or more:

- `export`
- `screenshot`
- `url`
- `review_cluster`
- `support_ticket`
- `return_reason`
- `policy`
- `feed_diagnostics`
- `margin_csv`
- `inventory_export`
- `hypothesis`
- `needs_data`

Added with skills 11-20:

- `cogs_export` - product cost file, ideally landed cost
- `payout_report` - payment provider settlement or payout statement
- `shipping_invoice` - carrier invoice including surcharges
- `cohort_export` - customer-level order history usable for cohorts
- `subscription_export` - subscriber list with cycle and status
- `chargeback_export` - disputes with reason codes and outcomes
- `site_search_export` - internal search queries and results
- `structured_data` - markup a machine reads from the page
- `promo_calendar` - dated record of past and planned promotions

## Decision fields

Every finding a skill returns carries all five of these, whatever the skill.
Individual skills state only their own ranking rule, because that is the part
that differs; this table is the part that does not.

| Field | Values |
|---|---|
| Severity | `low`, `medium`, `high`, `critical` |
| Confidence | `low`, `medium`, `high` |
| Business impact | `revenue`, `margin`, `cashflow`, `retention`, `conversion`, `support_load`, `risk` |
| Effort | `XS`, `S`, `M`, `L` |
| Owner decision | `do_now`, `test`, `investigate`, `monitor`, `ignore`, `approval_needed` |

## Decision summary template

```md
## Decision Summary

| Finding | Evidence | Severity | Confidence | Business impact | Effort | Owner decision |
|---|---|---|---|---|---|---|
| [finding] | [tag] | [value] | [value] | [value] | [value] | [value] |

## What not to do yet

- [live/costly/public action that should wait for approval or better data]

## Missing data

- [data needed to improve confidence]
```

## Common failure modes

Fail the output if it:

- treats ROAS as profit without margin data
- recommends increasing spend without stock and margin context
- recommends discounts as the first solution without evidence
- invents testimonials, product claims, or benchmark numbers
- treats screenshots as proof of impact
- hides missing data
- presents projected savings as guaranteed savings
- recommends live changes without approval
- projects an LTV or cohort curve past the data it has
- compares segments without stating how small the segments are
- reports one churn number without splitting voluntary from involuntary
- promises visibility, ranking, or inclusion on any AI or marketplace surface
- marks a launch layer ready when nobody verified it
