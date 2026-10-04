## Summary

Record the owner's first-launch capability commitment and prepare complete-scope M1 no-code briefs. ADR-0008 records D1 approval and the owner's D2 amendment: personal comparison, video, declared nutrition, offline consultation, change comparison, in-venue displays and six connection capabilities enter the launch; only standalone audio and 3D are deferred.

Contributes to #3 and #6; coordinates #15. These outcomes stay open for remaining preparation dependencies and actual closure evidence.

## Type of change

- [ ] Feature
- [ ] Fix
- [x] Documentation / research
- [ ] Refactor
- [ ] Build / CI / tooling

## How it was verified

- All 72 source table rows mapped once with original line references; accepted launch scope separate from proposed detailed rules.
- Counts reconcile: 36 Included, 30 Configurable and 6 Connection-dependent. B3.11 is split into launch video and deferred audio/3D subparts without inflating the parent count.
- Journey coverage 72/72; new public/operator criteria for saved choices/video, nutrition, offline/reconnect, display output, observed change comparison and supported connection states.
- Ten PR Markdown files and 59 local link targets checked; table widths, staged whitespace and attribution scan pass. Original functional/research sources unchanged.
- Commits use Yahya <yaboula@alumno.upv.es>, empty trailers verified after each commit. Linked GitHub/Linear tracking updated without backlog migration.

## Definition of Done

- [ ] Acceptance criteria of the linked issue are met: scope accepted; remaining clarification/target/access/device/content dependencies and full M0 closure remain open
- [x] Risk-appropriate checks pass (construction CI from M3): documentation checks passed
- [x] Relevant accessibility checks pass (design from M1; implementation from M3): no interface changed; video/output/prototype checks retained
- [x] Security and privacy impact considered: connection authorisation/data boundaries and honest nutrition/offline/measurement behaviours retained; no collection implemented
- [x] Documentation updated (ADR / SRS / glossary / README): ADR/index, matrix, journeys, briefs, executive framework and roadmap aligned
- [x] `CHANGELOG.md` updated if relevant

## Notes for the reviewer

Scope acceptance comes from the explicit owner response on 1 October 2026; PR integration does not establish implementation or M0 completion. Detailed D3 service/pricing obligations remain pending evidence. Actual connection targets/access are launch dependencies, not automatic deferrals; future-module execution is not silently absorbed.

Two separate prose-only ideas (free-form owner editor and individualised recommender) were omitted from the enumerated D2 question and are explicitly pending clarification. Independent review, prototypes, real participants, active integrations and commercial validation are not claimed completed.

Stacked on `docs/m0-execution-brief` / #18. Review order #7 -> #8 -> #16 -> #18 -> this PR. After earlier squash merges transplant only dependent commits, retarget and verify. No merge performed. No committed dates or budget assumptions.