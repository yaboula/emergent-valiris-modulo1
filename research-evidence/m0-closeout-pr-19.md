## Summary

Prepare the accepted Storefront + Digital Menu launch commitment and M0 closeout for owner review/integration. ADR-0008 records the 72 source capabilities with only standalone audio and 3D deferred; ADR-0009 confirms studio page design, autonomous restaurant content updates and optional registered-diner personalisation.

The closeout record audits existing exit criteria, records actual resources and gives each outstanding design/technical/access/participant/commercial need a responsible contribution and later checkpoint. It includes complete-scope M1 public/management briefs and the dependent integration sequence. M0 remains formally open until review/integration and outcome closure.

Closes #3. Closes #6. Coordinates #15 and hands over to #5/#4.

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
- Thirteen PR Markdown files / 87 local link targets, table widths, staged whitespace and attribution checked. Original functional/research sources and accepted ADR-0008 unchanged.
- Commit identity Yahya <yaboula@alumno.upv.es> and empty trailers verified after each commit. GitHub/Linear carry-over aligned without a duplicate backlog.

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

Stacked on `docs/m0-execution-brief` / #18. Owner review/squash order #7 -> #8 -> #16 -> #18 -> #19. After each earlier squash, transplant only dependent changes, retarget and verify the next diff. No merge or milestone closure performed; no dates/costs invented.
