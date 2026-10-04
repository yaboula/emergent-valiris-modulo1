$ErrorActionPreference = 'Stop'
$evidencePath = 'D:\the next level\research-evidence'
$updates = @{
3 = @'
## Current execution — 1 October 2026

Launch scope is accepted through ADR-0008/0009: all 72 source rows (36 Included, 30 Configurable, six Connection-dependent), audio/3D deferred subparts, excluded restaurant page builder and registered-diner personalisation. Ordinary menu consultation remains account-free; restaurants maintain content while Valiris designs pages.

PR #19 now includes `docs/project/m0-closeout.md`: audit of existing exit criteria, actual resources, accountable carry-over/checkpoints and owner integration sequence. Matrix, J1–J15/R01–R17 and public/management M1 briefs are delivered; scope clarification is complete. Actual design/technical/access/participant evidence belongs to its affected M1–M7 checkpoint, with no silent scope reduction.

M0 preparation is ready for owner PR review/integration. PR #19 closes this outcome on integration; no completed prototype, independent review, functioning connection or commercial validation is claimed. The owner requested M0 completion before M1 execution. Review order #7 -> #8 -> #16 -> #18 -> #19, adjusting dependent changes/base after each squash. Continue linked execution in YAH-5 without a duplicate backlog.
'@
6 = @'
## Current execution — 1 October 2026

M0 preparation is ready for owner review/integration. PR #19 adds `docs/project/m0-closeout.md`, which audits all existing closure criteria and records actual capacity/tools/content/participant limits, responsible contributions, next actions and affected checkpoints. D1/D2/D4/D5 scope decisions are resolved through ADR-0008/0009; D3 awaits concrete service/offer evidence at its later checkpoint.

The public/management briefs can start M1 without reconstructing the vision. Prototypes, technical rules, integration access, independent review and real-participant evidence remain their actual M1–M7 work, not new M0 prerequisites. No accepted launch capability is removed. Dates and costs remain uncommitted.

The remaining formal M0 closure action is owner review/integration of #7 -> #8 -> #16 -> #18 -> #19, with dependent changes transplanted and the next PR retargeted after each squash. PR #19 closes #3/#6 on integration. Confirm the other M0 outcomes are integrated/closed before closing the milestone and completing YAH-5. #15 continues in parallel with full completion tracked in M7.
'@
}
foreach ($number in @(3,6)) {
    $issue = gh -R yaboula/valiris-restaurants issue view $number --json body | ConvertFrom-Json
    if ($LASTEXITCODE -ne 0) { throw "Read #$number" }
    $heading = '## Current execution — 1 October 2026'
    if (-not $issue.body.Contains($heading)) { throw "Missing section #$number" }
    $prefix = $issue.body.Substring(0,$issue.body.IndexOf($heading)).TrimEnd()
    $bodyPath = Join-Path $evidencePath "m0-closeout-issue-$number.md"
    [System.IO.File]::WriteAllText($bodyPath,"$prefix`n`n$($updates[$number])`n",[System.Text.UTF8Encoding]::new($false))
    gh -R yaboula/valiris-restaurants issue edit $number --body-file $bodyPath
    if ($LASTEXITCODE -ne 0) { throw "Edit #$number" }
}
$carryNotes = @{
2 = 'M0 closeout audit: traceable historical and latest Storefront inputs, fictional-scenario labels and evidence limits are available. PR #8 integrates this outcome without passing the retired Gate 1 or claiming demand validation. `docs/project/m0-closeout.md` in PR #19 records the owner integration sequence; synthesis rebuilding remains separate decision-specific work.'
4 = 'M0 handover is prepared in `docs/project/m0-closeout.md` / PR #19. From M1 design, resolve publication/context/recovery, six actual connection target/data/access contracts, guest versus staff identity, recommendation inputs/account scope, retention/deletion and offline/measurement rules. Preserve all accepted launch capabilities. This issue remains open; no stack/provider or technical evidence is established by M0 preparation.'
5 = 'The owner requested M0 completion before M1 execution. `docs/project/m0-closeout.md` / PR #19 records integration readiness and the handover. After M0 integration, confirm prototyping method, prepare labelled C1–C3 fixtures and produce both public/management prototypes covering J1–J15/R01–R17, including optional diner accounts/personalisation and the complete accepted scope. Return coverage, actual independent review/corrections and real-session limits. This issue remains open; no prototype or specialist activation claimed.'
15 = 'Full completion is tracked in M7 because this outcome runs in parallel through launch. Its M0 contribution is captured in the briefs and `docs/project/m0-closeout.md` / PR #19; moving the tracker milestone does not postpone execution or remove M0–M6 work. Final terms/prices/support still need delivery evidence and owner decisions; this issue stays open.'
}
foreach ($number in @(2,4,5,15)) {
    $issue = gh -R yaboula/valiris-restaurants issue view $number --json body | ConvertFrom-Json
    if ($LASTEXITCODE -ne 0) { throw "Read #$number" }
    $bodyPath = Join-Path $evidencePath "m0-closeout-issue-$number.md"
    $newBody = $issue.body.TrimEnd() + "`n`n## M0 closeout handover — 1 October 2026`n`n" + $carryNotes[$number] + "`n"
    [System.IO.File]::WriteAllText($bodyPath,$newBody,[System.Text.UTF8Encoding]::new($false))
    if ($number -eq 15) { gh -R yaboula/valiris-restaurants issue edit $number --milestone 'M7 - Launch and operation' --body-file $bodyPath }
    else { gh -R yaboula/valiris-restaurants issue edit $number --body-file $bodyPath }
    if ($LASTEXITCODE -ne 0) { throw "Edit #$number" }
}
$researchPr = gh -R yaboula/valiris-restaurants pr view 8 --json body | ConvertFrom-Json
if ($LASTEXITCODE -ne 0 -or -not $researchPr.body.Contains('Relates to #2.')) { throw 'Research link changed' }
$researchBodyPath = Join-Path $evidencePath 'm0-closeout-pr-8.md'
$researchBody = $researchPr.body.Replace('Relates to #2.','Closes #2.') + "`n`nCurrent M0 closeout: PR #19 records the exit audit and dependent integration order. Issue #2 closes on review/integration of these traceable inputs and historical limits, not commercial validation or the retired Gate 1.`n"
[System.IO.File]::WriteAllText($researchBodyPath,$researchBody,[System.Text.UTF8Encoding]::new($false))
gh -R yaboula/valiris-restaurants pr edit 8 --body-file $researchBodyPath
if ($LASTEXITCODE -ne 0) { throw 'PR #8 edit' }
$prBody = @'
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
'@
$bodyPath = Join-Path $evidencePath 'm0-closeout-pr-19.md'
[System.IO.File]::WriteAllText($bodyPath,"$prBody`n",[System.Text.UTF8Encoding]::new($false))
gh -R yaboula/valiris-restaurants pr edit 19 --title 'docs(product): prepare launch commitment and M0 closeout' --body-file $bodyPath
if ($LASTEXITCODE -ne 0) { throw 'PR #19 edit' }
