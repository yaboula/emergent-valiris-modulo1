## Summary

Turn the Storefront + Digital Menu definition into a reviewable first-launch proposal and actionable M1 no-code design briefs. Cover all 72 source capabilities with separate treatment/approval status, public/operator/buyer journeys and critical-state criteria, and public/management design assignments with targeted specialist questions.

Contributes to #3 and #6; coordinates the parallel line in #15. These outcomes stay open pending the actual owner decisions and closure evidence.

## Type of change

- [ ] Feature
- [ ] Fix
- [x] Documentation / research
- [ ] Refactor
- [ ] Build / CI / tooling

## How it was verified

- Matched all 72 unique capability IDs and original source line references; no source row omitted or duplicated. Every detailed approval remains proposed.
- Reconciled treatment counts: 36 included, 24 configurable within launch, 6 connection-dependent, 5 later, 1 pending. Two additional prose opportunities are separately identified rather than added to the table count.
- Checked the journey coverage map against all 72 source rows; included/configurable behaviours have public/operator/service criteria, with critical publication, context, translation, food-information, print and continuity states retained.
- Checked seven Markdown files, consistent table widths and 33 local link targets. Staged whitespace check passed. Original research/functional sources are unchanged.
- Verified commit author Yahya <yaboula@alumno.upv.es>, empty trailers and clean attribution scan.
- Checked current GitHub #3/#6/#15 and Linear YAH-5 before updating only execution responsibility/content. No backlog migration or duplicate task was created.

## Definition of Done

- [ ] Acceptance criteria of the linked issue are met: proposed documents delivered; launch approval and full M0 closure remain pending
- [x] Risk-appropriate checks pass (construction CI from M3): documentation checks passed
- [x] Relevant accessibility checks pass (design from M1; implementation from M3): no interface changed; prototype/implementation review requirements retained
- [x] Security and privacy impact considered: no personal-data collection or permissions implementation added; later checks specified
- [x] Documentation updated (ADR / SRS / glossary / README): brief, product package, index and glossary; no stack or architecture choice made
- [x] `CHANGELOG.md` updated if relevant

## Notes for the reviewer

Owner instruction combines executive and Product execution/consolidation for this assignment. Update the existing executive brief narrowly; independent Quality and other specialist responsibilities remain. No committed dates or budget assumptions.

D1 requests review of the 60 included/configurable first-commercial rows. D2 requests review of opportunity/display/connection boundaries. D3 retains detailed service/pricing/support/domain obligations until concrete evidence supports the terms. No approval is inferred from document delivery or PR integration.

Independent specialist review, no-code prototypes, real participants, implementation, active integrations and commercial validation have not occurred in this change. Consultations are prepared, not represented as answered.

Stacked on `docs/m0-execution-brief` / #18. Review order #7 -> #8 -> #16 -> #18 -> this PR. After earlier squash merges, transplant only dependent commits, retarget and verify the diff. No merge is performed.