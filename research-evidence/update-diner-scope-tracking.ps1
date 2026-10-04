$ErrorActionPreference = 'Stop'
$repoPath = 'D:\the next level\valiris-restaurants'
$evidencePath = 'D:\the next level\research-evidence'
$issueUpdates = @{
    3 = @'
## Current execution — 1 October 2026

Combined G1 Direction/Product responsibility consolidates scope and design; independent Quality remains. ADR-0008 records D1 approval and D2 expansion, deferring only standalone audio and 3D. ADR-0009 resolves supplementary D4/D5: restaurants update content, Valiris controls page design, and personalised recommendations enter the launch for authenticated registered diners. Ordinary menu consultation remains account-free.

Current matrix on `docs/m0-launch-commitment` / PR #19: all 72 source rows accepted for launch, 36 Included, 30 Configurable and 6 Connection-dependent. Supplementary S1 excludes a free-form restaurant builder; S2 accepts registered-diner personalisation without changing the parent count. J1–J15, R01–R17 and M1 briefs include necessary account/access/preferences/recommendation states. Guest identity remains distinct from staff membership and future campaign customers.

Scope clarification is complete. Actual connection targets/access, representative device/content, account/personalisation rules and independent reviews remain preparation dependencies; M2 selects sufficient data/access/authentication rules without a presumed provider or algorithm. This issue stays open until its full criteria are met; scope acceptance is not implementation, validation or M0 closure. Continue linked execution in YAH-5 without duplicating the backlog.
'@
    6 = @'
## Current execution — 1 October 2026

The executive brief and combined G1 launch package reflect owner-accepted D1/D2 through ADR-0008, with only standalone audio and 3D deferred. ADR-0009 resolves D4/D5: autonomous restaurant content updates, studio page design and launch personalisation for authenticated registered diners, with ordinary account-free consultation.

Public/operator/buyer criteria and M1 briefs cover the complete accepted scope, including J15 account/preferences/recommendation states and necessary Core preparation. The two prose-only scope questions are resolved. Remaining preparation includes actual target/access/device/content dependencies and sufficient account/personalisation rules; independent review and real-participant evidence remain separate.

Do not close M0 from scope acceptance alone. Outcomes/dependencies govern execution without dates; concrete spending and D3 service terms await reviewable proposals/evidence. PR #19 carries the aligned package; linked scope issue #3 and Linear YAH-5 remain open/in progress.
'@
    15 = @'
## Coordination update — 1 October 2026

Combined G1 coordinates the accepted launch scope and commercial/service implications. ADR-0008 accepts D1 and expanded D2 coverage, with only standalone audio and 3D deferred. Include video/nutrition/offline/display/comparison and connected delivery work in content intake, maintenance and offer preparation.

ADR-0009 confirms autonomous restaurant content updates while Valiris retains template/bespoke page design; exclude a free-form restaurant builder. Personalised recommendations are launch scope for authenticated registered diners, with public consultation remaining account-free. Account/profile work affects delivery and operating effort; no effectiveness or working-account claim is established by the decision.

Final packages/prices, support/revisions and domain/exit terms require delivery evidence and explicit obligations; scope approval does not establish active integrations, content rights, profitability or sales outcomes. Valiris website discovery remains distinct from restaurant SEO; no dates or tariffs added. PR #19 records current scope and briefs.
'@
}
foreach ($issueNumber in @(3,6,15)) {
    $issue = (& gh -R yaboula/valiris-restaurants issue view $issueNumber --json body | ConvertFrom-Json)
    if ($LASTEXITCODE -ne 0) { throw "Read issue $issueNumber" }
    $heading = if ($issueNumber -eq 15) { '## Coordination update — 1 October 2026' } else { '## Current execution — 1 October 2026' }
    if (-not $issue.body.Contains($heading)) { throw "Missing section $issueNumber" }
    $prefix = $issue.body.Substring(0, $issue.body.IndexOf($heading)).TrimEnd()
    $bodyPath = Join-Path $evidencePath "diner-scope-issue-$issueNumber.md"
    [System.IO.File]::WriteAllText($bodyPath, "$prefix`n`n$($issueUpdates[$issueNumber])`n", [System.Text.UTF8Encoding]::new($false))
    & gh -R yaboula/valiris-restaurants issue edit $issueNumber --body-file $bodyPath
    if ($LASTEXITCODE -ne 0) { throw "Update issue $issueNumber" }
}
$prBody = @'
## Summary

Record the owner's first-launch capability commitment and prepare complete-scope M1 no-code briefs. ADR-0008 accepts the 72 reference rows with only standalone audio and 3D deferred. ADR-0009 adds personalised recommendations for authenticated registered diners, keeps ordinary consultation account-free, and confirms studio page design with autonomous restaurant content updates.

Contributes to #3 and #6; coordinates #15. These outcomes stay open for actual preparation dependencies and closure evidence.

## Type of change

- [ ] Feature
- [ ] Fix
- [x] Documentation / research
- [ ] Refactor
- [ ] Build / CI / tooling

## How it was verified

- All 72 source table rows mapped once with exact original line references: 36 Included, 30 Configurable and 6 Connection-dependent, accepted scope separate from proposed detailed rules.
- Audio/3D deferred subparts and supplementary S1 excluded builder/S2 accepted personalisation remain separate from the 72-parent count. Journey coverage is 72/72 plus J15.1–J15.6/R17 account/preferences/recommendation criteria.
- Eleven PR Markdown files and 69 local targets checked; consistent table widths, staged whitespace and attribution scan pass. Original functional/research sources unchanged; accepted ADR-0008 preserved by the supplementary ADR.
- Commits use Yahya <yaboula@alumno.upv.es>, empty trailers verified after each commit. Linked GitHub/Linear tracking updated without backlog migration.

## Definition of Done

- [ ] Acceptance criteria of the linked issue are met: scope resolved; actual target/access/device/content dependencies and full M0 closure remain open
- [x] Risk-appropriate checks pass (construction CI from M3): documentation checks passed
- [x] Relevant accessibility checks pass (design from M1; implementation from M3): no interface changed; video/output/prototype review criteria retained
- [x] Security and privacy impact considered: guest/staff identity, private profile/session/offline isolation, account controls and connection boundaries documented; no collection implemented
- [x] Documentation updated (ADR / SRS / glossary / README): ADR/index, matrix, journeys, briefs, executive framework, roadmap and vocabulary aligned
- [x] `CHANGELOG.md` updated if relevant

## Notes for the reviewer

Scope acceptance comes from explicit owner responses on 1 October 2026. D1/D2/D4/D5 are resolved; no repeat scope approval is required. PR integration does not establish implementation or M0 completion. D3 service/pricing obligations remain pending evidence. Actual connection targets/access are launch dependencies, not automatic deferrals; future-module execution is not silently absorbed.

Registered-diner personalisation adds genuine identity/profile/access work. Recommendation inputs/rules, account scope across venues, authentication method and retention/deletion effects require M1/M2 preparation; no provider or algorithm selected. Independent reviews, prototypes, real participants, active integrations and commercial validation are not claimed completed.

Stacked on `docs/m0-execution-brief` / #18. Review order #7 -> #8 -> #16 -> #18 -> this PR. After earlier squash merges transplant only dependent commits, retarget and verify. No merge performed. No committed dates or budget assumptions.
'@
$prBodyPath = Join-Path $evidencePath 'diner-scope-pr-19.md'
[System.IO.File]::WriteAllText($prBodyPath, "$prBody`n", [System.Text.UTF8Encoding]::new($false))
& gh -R yaboula/valiris-restaurants pr edit 19 --body-file $prBodyPath
if ($LASTEXITCODE -ne 0) { throw 'PR update' }
