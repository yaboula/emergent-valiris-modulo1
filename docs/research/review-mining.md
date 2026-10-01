# Public competitor review mining

Collected: 2026-09-28. **50 distinct public software reviews**, classified by one primary theme, are recorded in the [review ledger](review-ledger.md). This is an exploratory, purposive sample, not a representative satisfaction survey.

## Collection and inclusion

- TheFork Manager: 20 reviews from the first 50 entries of the Spanish Apple public feed, ordered most recent first. This is the operator app, not TheFork's diner app.
- CoverManager: 20 reviews from the first 50 entries of the Spanish Apple public feed, ordered most recent first.
- Loopy Loyalty: 10 readable Capterra reviews selected for restaurant/food-and-beverage operational relevance; one general manager's sector is unspecified. Capterra's default helpful ordering and platform selection are additional biases.

For each Apple feed, inspect in returned order and retain the first 20 entries whose title or body describes a feature, task, change or purchasing condition. Exclude food/venue comments and generic praise or insults without an interpretable product theme. For Capterra, retain the ten named reviews in the ledger from individually readable indexed passages across the first two results pages; do not infer unseen review bodies. No automated randomisation, rating balancing or claim of saturation was used.

Examples excluded: TheFork IDs 14461938530 and 9364884845 describe food; 13502233474 and 9702389791 give generic praise; 9177501483 gives a generic insult. CoverManager IDs 14219607018, 13036952415 and 11896001557 lack a specific interpretable feature or task. Vendor responses and page-level pros/cons highlights are not additional reviews.

Apple IDs plus product identify unique records. Capterra uses public abbreviated reviewer name + date + product as the locator. Dates are the platform's displayed/updated dates, not verified incident dates. Preserve app version where the feed provides it. Spanish storefront does not establish reviewer nationality, venue location or operator employment. Raw feeds and working notes are kept outside the repository; the repository contains minimal locators and paraphrases, not copied review bodies or customer profiles.

Sources: [TheFork Manager Apple feed](https://itunes.apple.com/es/rss/customerreviews/page=1/id=1295795281/sortby=mostrecent/json), [CoverManager Apple feed](https://itunes.apple.com/es/rss/customerreviews/id=1289393829/sortBy=mostRecent/json), [Loopy Loyalty Capterra](https://www.capterra.com/p/160859/Loopy-Loyalty/reviews/), [second results page](https://www.capterra.com/p/160859/Loopy-Loyalty/reviews/?page=2). All accessed 2026-09-28. Public feeds and page ordering can change; IDs/date/name enable re-identification but do not guarantee continued availability.

## Coding rules

Primary theme identifies the most actionable part of the report, including benefits worth preserving. Assign one theme per row to prevent double counting; secondary complaints remain in the paraphrase where useful. Text sentiment is coded separately from stars. For example, RM-016 has five stars but describes a negative update experience. Counts include praise and mixed reports, so they are **theme mentions, not complaint counts**.

| Code | Meaning | Theme mentions / 50 |
| --- | --- | --- |
| UX | Task friction, navigation, useful interface or change adoption | 14 |
| RELIABILITY | Cannot log in/open/use app, freezes or outage | 11 |
| SYNC | Stale state, notification or refresh problems | 7 |
| COST | Contract/billing concern or perceived value | 6 |
| CUSTOMER | Customer lookup, ownership or card retrieval | 4 |
| CAPACITY | Party size and table assignment | 2 |
| SUPPORT | Response or unresolved-issue handling | 2 |
| LOYALTY | Stamp operation or guest card retrieval | 2 |
| CONTENT | Restaurant photo/content publication | 1 |
| DATA | Export/database delivery and reporting workflow | 1 |

Product totals: TheFork Manager 20, CoverManager 20, Loopy Loyalty 10. Text sentiment totals: 31 negative, 13 mixed, 6 positive. Review years: 2017 (1), 2022 (10), 2023 (2), 2024 (6), 2025 (16), 2026 (15). **31/50 date from 2025–2026**; the other 19 are historical signals. RM-041 is explicitly incentivized by Capterra; RM-042–050 are marked non-incentivized. Apple incentive status is unknown.

## Findings and counterevidence

- Booking work must remain usable under service pressure: stale state, extra steps and outages create candidate failure scenarios for tests (RM-001, 005, 007, 014, 017, 026–030).
- Useful mobile software already exists in reviewers' experience: CoverManager praise and improving versions contradict a claim that every incumbent is unusable (RM-021–023, 025, 028, 031, 038).
- Loyalty requires recovery, not just a happy-path QR scan: the useful questions concern a card not saved, a changed device and customer lookup (RM-044, 049, 050). They do not prove repeat-visit uplift.
- Vendor replies offer counterevidence: RM-042's confirmation can reportedly be disabled; RM-045's requested notifications and automation depend on settings/integrations. These are vendor explanations, not verified fixes. Reported friction does not prove an absent feature.
- Cost concerns are about perceived value and conditions as well as a monthly amount. Allegations of incorrect charging or contract disputes are unverified reports, not findings of misconduct (RM-002, 004, 025, 037, 041, 046).

## Limits and requirement handoff

Two reservation apps contribute 80% of the sample. App-store complaints overrepresent mobile failures and update incidents; several reports may concern the same release. Historical complaints may already be fixed. The ten loyalty reviews are not a Spanish-only sample. Qamarero, EterSystem and menu specialists have no counted independent reviews here. A single coding pass has no independent inter-rater check. Do not convert sample counts into market percentages, vendor rankings or claims of feature absence.

Use these records to derive provisional task-based acceptance criteria and recovery tests in M0.3/M0.4. Use simulations to probe scenarios, not to increase the review sample or its confidence. Commercial validation still requires independent conversations about recent behaviour and existing workarounds.
