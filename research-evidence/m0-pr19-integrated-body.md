## Summary

Integrate the accepted Storefront + Digital Menu launch commitment and M0 closeout. ADR-0008 records the 72 source capabilities with only standalone audio and 3D deferred; ADR-0009 confirms studio page design, autonomous restaurant content updates and optional registered-diner personalisation.

The closeout record audits existing exit criteria, records actual resources and gives each outstanding design/technical/access/participant/commercial need a responsible contribution and later checkpoint. It includes complete-scope M1 public/management briefs and the dependent integration sequence. All five M0 PRs are now merged, the six M0 outcomes are closed, milestone M0 is closed and Linear YAH-5 is Done.

Closes #3.
Closes #6.

Carry-over: M1 design (#5), M2 preparation (#4), and parallel commercial work (#15) remain open.

## Type of change

- [ ] Feature
- [ ] Fix
- [x] Documentation / research
- [ ] Refactor
- [ ] Build / CI / tooling

## How it was verified

- 72 exact unique source parent IDs/line references; accepted 36 Included / 30 Configurable / 6 Connection-dependent counts.
- Separate audio/3D deferrals and supplementary S1 excluded builder/S2 accepted personalisation; 72/72 parent journey coverage plus J15.1–J15.6/R17.
- Author exit audit against current roadmap, executive brief and existing #3/#6 criteria; resources and unresolved later checkpoints explicit, no independent review claimed.
- Thirteen PR Markdown files / 88 local link targets, table widths, staged whitespace and attribution checked. Original functional/research sources and accepted ADR-0008 unchanged.
- Local commit identity Yahya <yaboula@epsa.upv.es> and empty trailers verified; GitHub squash uses YAHYA ABOULAFIYA with the same verified email. Historical commits retain their originally approved identity. GitHub/Linear carry-over aligned without a duplicate backlog.

## Definition of Done

- [x] Acceptance criteria of the linked issue are met: preparation evidence ready for owner review/integration; formal M0 closure follows all integrated outcomes
- [x] Risk-appropriate checks pass (construction CI from M3): documentation checks passed
- [x] Relevant accessibility checks pass (design from M1; implementation from M3): no interface changed; actual prototype/implementation reviews remain their milestone work
- [x] Security and privacy impact considered: guest/staff identity, private session/offline isolation, account controls and connection boundaries documented; no collection implemented
- [x] Documentation updated (ADR / SRS / glossary / README): matrix, journeys, briefs, closeout, executive framework, roadmap, planning transition, ADR/index and vocabulary aligned
- [x] `CHANGELOG.md` updated if relevant

## Notes for the reviewer

Start with `docs/project/m0-closeout.md`. D1/D2/D4/D5 are resolved; no repeat scope questionnaire. M0 identifies accountable dependencies; it does not require completion of the later prototypes, account algorithms/providers, supported connections, independent design reviews or real pilot. Missing later access does not waive the accepted launch commitment. D3 terms/spending remain concrete owner decisions when evidence exists.

No implementation, recommendation effectiveness, commercial validation or completed independent review claimed. #15 continues in parallel through M7; its full tracker completion belongs there rather than keeping M0 open until launch.

Based on main after #7/#8/#16/#18 were reviewed and squash-integrated. Each dependent branch was transplanted from its original parent boundary, pushed with an explicit lease, retargeted and checked. The owner delegated authorised review/merge; protections remain active. PR #19 completes the M0 package. Formal milestone/Linear closure was verified after integration and outcome closure; no dates/costs invented.
