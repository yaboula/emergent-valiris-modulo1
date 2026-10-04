---
status: proposed
date: 2026-10-02
deciders: Product owner
---

# ADR-0011: Prefer shared item content with explicit contextual maintenance

## Context and problem statement

The accepted launch includes bulk editing, reuse and independent copies (B4.04), contextual prices/conditions and reviewed publication. Maintaining the same product in several menus requires a visible distinction between common factual content and each menu's applicable offering. Automatic cloning increases repeated factual maintenance; automatic shared publication risks unintended scope and private-draft leakage.

On 2 October the owner explicitly selected **shared content as the principal reuse option, with independent copies available**, then authorised the content-preparation design plan. This ADR remains **proposed** in draft PR #21 under the repository review/integration process; the selected direction is recorded, while detailed ownership, transaction, permission and recovery contracts still require G3/M2 review. No accepted historical ADR is changed.

## Decision drivers

- Keep everyday factual maintenance autonomous for both template and studio-designed venues without forcing advanced controls on Café Linde.
- Preserve item/variant/portion/context, price/unit/conditions, current validity and separate live availability.
- Show every affected shared use, dependency and private/public consequence before action.
- Retain known food declarations, explicitly pending information and affected translations/nutrition/diet.
- Provide understandable copies and recovery without accidental publication, silent overwrites or expired-service revival.

## Considered options

1. Prefer a common item ficha with explicitly contextual placements; offer independent copies deliberately.
2. Prefer independent item copies in each menu; offer shared reuse as an additional choice.
3. Automatically match/reuse and propagate changes to every destination without scope review.

## Decision outcome

Chosen direction: **Option 1**, selected by the owner. The [descriptive design](../design/m1-content-preparation.md) proposes the following behaviour, not an implemented data schema:

- Common identity/recipe facts and their dependent food/diet/nutrition/translation review belong to an identified shared source within one restaurant. Placement-specific format/amounts, supplements/conditions, validity, section/order and availability retain their explicit menu/context scope; they are not copied per interface language.
- Reuse creates a private reviewed placement proposal. Import/matching and menu duplication show source identities, relationship choice and contextual fields; no automatic publication, deletion or name-based identity merge.
- Publishing a common factual change requires one coherent reviewed group of all affected applicable published uses and current factual fallback/pending states. A denied/conflicting required use blocks that common group; unrelated drafts stay private, and expired uses are never reactivated. This enforcement/atomicity proposal needs technical review.
- Contextual price/availability operations name their item/context/service and have separate editorial and urgent modes. Outcome and recovery are recorded by original operation/action/group/base revision; unknown is not success or permission to blindly retry.
- An independent copy has a new identity, retained source references and explicit factual applicability review. It does not receive later source changes or automatically inherit confirmed stock, schedules, reviewer certification, rights or public validity. Detaching a placement is itself a reviewed private change; it cannot bypass permissions or known recipe facts.

### Consequences

- Diner: consistent contextual offers and maintained factual limits; review delay or explicit withholding/fallback can reduce immediate content availability. No safety guarantee is inferred.
- Restaurant: less repeated maintenance is the intended benefit, not a measured result. Staff must recognise common versus contextual changes and review their scope; independent copies create a separate maintenance obligation.
- Valiris: shared-source/placement identities, dependency visibility, permission scope, coherent operation groups and reliable correlation/recovery require engineering/service work. No provider, implementation cost, effort saving or margin is established.
- Core/M2: review the field-ownership boundary, variant/portion dependencies, versioning, scheduled targets, per-action/per-use authority, source rights/retention and partial/unknown operation results. No database/API/model choice is approved here.

### Confirmation

Author checks: CP-S01–CP-S04, CP-B01–CP-B04 and PC14–PC23 in the descriptive package, alongside affected J3/J4/J5/J6/J7 mappings and earlier V/Q regressions. These are documentary checks.

Before affected closure, independent G4 reviews understanding and critical scope; G3 evaluates enforcement/atomicity/concurrency and actual operation contracts; G5 supplies authorised material and real restaurant facts. Real interaction, staff tasks, publication, failure/recovery and output checks remain required. No specialists are asserted available or consulted.

## Pros and cons of the options

### Option 1 — Shared principal option

- Supports common factual maintenance and explicit contextual differences.
- Requires visible dependencies and coherent review across affected uses; an unresolved required use can block common publication.

### Option 2 — Independent copies principal option

- Offers straightforward local divergence and simpler individual update scope.
- Repeated facts, recipe changes and translations can drift; sharing needs additional identity reconciliation. Still available deliberately under the selected direction.

### Option 3 — Automatic propagation

- Appears to remove review steps.
- Can merge different dishes by name, copy wrong prices/context, overwrite private work or publish unintended changes. Rejected as inconsistent with the accepted scope's review and permission rules.

## More information

- [Launch commitment](0008-first-launch-capability-commitment.md), [studio design and autonomy](0009-studio-design-and-registered-diner-personalisation.md), [account/diet/display directions](0010-diner-account-and-display-recovery.md).
- [Capability matrix](../product/m0-capability-matrix.md), [criteria](../product/m0-journeys-and-criteria.md), [M1 briefs](../product/m1-design-briefs.md), [M2 dependency in roadmap](../project/roadmap.md).
- Revisit the detailed proposal if actual recipe/context, permissions, source ownership or technical evaluation shows an incompatible use. G1 consolidates consequences; material changes to the selected direction require an explicit owner decision, not silent conversion to copies or scope deferral.
