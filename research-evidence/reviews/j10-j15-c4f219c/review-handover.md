# J10-J15 consolidated review handback to G2

2 October 2026. G1 consolidates product review with independent G4. Baseline: `c4f219cf5f06a3fe55b1d4e2040c6f6f45c584df`, PR #21 open/draft, active M1 #5.

**Result: one required correction, G4-J15-01 / P2**, before the affected J15.3/J15.4 category-lifecycle branch is considered resolved. The 38 described states and 20 criteria were reviewed; no other reproducible written contradiction was identified in the bounded contrasts. Other authorised design work may continue.

## Required correction: unavailable saved taste category

In `docs/design/m1-extended-journeys.md`, J15-A06 line 309 flags deleted/renamed categories for review but leaves the resulting recommendation behavior unspecified. J15-P02 line 316 permits diet-only candidates when the diner deliberately has no taste selections. Retirement of the last saved category cannot silently become that voluntary empty-input choice. Q17 line 496 needs the actual category-change outcome, not only save/reset/concurrency safeguards.

Supply visible saved-reference status, reason, permitted result and exact route to review/reconfirm inputs. Recommended copy: "Una categoría de tus preferencias ya no está disponible. Revisa qué quieres elegir"; **Cambiar preferencias** -> J15-A06. While unresolved, do not silently substitute categories, broaden results or present the missing category as a deliberate reset. Preserve diet constraints, known food facts, account/venue scope and ordinary public reading/venue suggestions.

Distinguish a same-identity cosmetic rename from retirement, substitution or uncertain identity/meaning. Define any continued matching of remaining valid taste selections with the changed reference visible. A deliberately confirmed edit/reset/reconfirmation may change inputs; unsaved or unknown results may not become recommendations. G3 specifies category identity and enforcement in M2/#4; this correction is the visible design contract, not implementation or a scope change.

## Six focused contrasts to return

1. Rename with the same confirmed category identity and meaning.
2. Retire the only saved taste category, with a separately labelled conditional declared-diet branch.
3. Retire one taste while another valid selected category remains.
4. Replace it with a similarly named category under a new identity.
5. Receive an old recommendation response after retirement/current-publication change.
6. Diner deliberately removes the unavailable reference and confirms diet-only or empty-taste inputs.

For each, state preference/publication revision, visible reason, permitted candidate behavior, action/destination and known/unknown result. Keep unrelated venue preferences/private profiles unchanged. Do not fabricate actual dietary declarations, identities, measurements or backend outcomes.

## Evidence and limits

- [G1 product review](g1-review.md).
- [Independent G4 finding and criterion-by-criterion evidence](g4-review.md).
- [Document checks](document-checks.json): 38 distinct states, 20 source criteria mapped exactly once, six differentiated connection cards, 44 local link occurrences valid. Matrix remains 72 parents, 36/30/6.
- [Immutable source](../c1-c3-c4f219c/source/docs/design/m1-extended-journeys.md).

G2 returns a corrected immutable commit and six written contrasts; G4/G1 recheck the affected preference/recommendation/fallback states. No new backlog item, founder scope approval, Figma dependency, implementation, merge or M1 closure is requested. This handback is prepared in the agreed personal location; no message was sent to the separate G2 chat.

Provider/session/publication/freshness/measurement/connection contracts, real video/nutrition/diet/translation sources, six actual targets/access, devices, rendered design/accessibility/interaction and participant evidence remain pending at their existing checkpoints. CP/ADR-0011 was not reviewed as a whole. The earlier G4-01 draft-save correction remains resolved and is separate from this new finding.
