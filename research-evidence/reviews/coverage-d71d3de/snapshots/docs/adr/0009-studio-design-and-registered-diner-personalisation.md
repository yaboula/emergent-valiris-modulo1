---
status: accepted
date: 2026-10-01
deciders: Product owner
---

# ADR-0009: Keep studio design and personalise for registered diners

## Context and problem statement

ADR-0008 accepted the 72 reference capability rows and left two prose-only ideas for clarification: a free-form restaurant page editor and an individualised recommender. The owner has now confirmed autonomous content updates, rejected restaurant-authored page design, and accepted personalised recommendations for diners with a registered account.

## Decision drivers

- Preserve the agreed template and paid bespoke studio-design model.
- Give restaurants autonomous everyday content maintenance.
- Provide personalised recommendations to authenticated registered diners while keeping ordinary public consultation accessible without an account.
- Add only account/profile responsibilities needed by this committed product need; retain honest food-information and publication boundaries.

## Considered options

1. Restaurant free-form page design versus studio-controlled design with autonomous content updates.
2. Venue-selected recommendations only, anonymous individual profiling, or personalised recommendations for registered diners.

## Decision outcome

Chosen options: **studio-controlled design with autonomous content updates, and launch personalised recommendations for registered diners**, accepted by explicit owner direction on 1 October 2026.

- Restaurant operators maintain prices, text, photos, availability and permitted content/brand controls. Templates and bespoke composition/design remain Valiris responsibilities; a free-form restaurant page builder is excluded.
- Personalised recommendations require a registered diner account and an authenticated session. Ordinary browsing, declared venue recommendations and the already accepted local comparison list remain account-free.
- Include the necessary registration/sign-in, account recovery, session/sign-out, preference management and account-control journeys in M1; sufficient identity/profile and authorised-data rules belong to M2.
- Initial recommendation inputs, algorithm, account scope across venues, authentication method/providers and retention/deletion rules are proposed design/technical questions, not settled by this decision. Prefer explicit guest-supplied preferences for the first design rather than inventing behavioural history.
- Empty preferences, unavailable recommendation service or no matching current items have understandable fallback states. Recommendations respect current published context/price/availability and never guarantee allergen safety or nutritional suitability.
- Recommendation/account access does not authorise promotional messages, implicit future loyalty/booking modules or sharing private profiles with restaurants. Data flows and privacy/security requirements need targeted review in M2.

### Consequences

- Good: content autonomy and studio design stay coherent; personalisation has an explicit account boundary.
- Accepted trade-off: registered-diner identity, profiles and personalised states add real design, data and security work. No dates, provider, cost, benefit or implementation are assumed.
- Additional responsibility: guest accounts and restaurant staff access must remain distinguishable, and private state must not leak across users, venues or signed-out/offline sessions.

### Confirmation

Keep the original 72-row ledger intact. Record the excluded editor and accepted registered-diner recommendation separately with source-prose references. Review anonymous, registration, signed-in empty/usable preference, no-match/error, sign-out and recovery cases, plus operator content autonomy in template/bespoke paths. Actual implementation, independent review and real tests remain pending.

## Pros and cons of the options

- Free-form restaurant design adds composition and maintenance responsibilities and was rejected by the owner; autonomous content updates retain the chosen studio model.
- Venue-only recommendations remain useful but do not satisfy the accepted personalised-account capability. Anonymous profiling was not chosen; authenticated personalisation has an explicit access boundary and added account/profile work.

## More information

This supplements [ADR-0008](0008-first-launch-capability-commitment.md) without rewriting its historical accepted content. See the [capability commitment](../product/m0-capability-matrix.md), [journeys/criteria](../product/m0-journeys-and-criteria.md), [M1 briefs](../product/m1-design-briefs.md) and [PR #19](https://github.com/yaboula/valiris-restaurants/pull/19). Decision accepted; PR integration pending.
