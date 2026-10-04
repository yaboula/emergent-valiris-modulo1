## Summary

Replace the seven-module/17-week execution plan with the owner-supplied first-product roadmap. v1.0 now delivers Storefront + Digital Menu, necessary Core and onboarding/design/support; future modules have no committed order or date. M0–M2 prepare, M3–M5 construct, M6 pilots with real participants, and M7 launches and operates.

Closes #9

## Type of change

- [x] Documentation / research

## What is included

- English roadmap, ADR-0007, aligned charter, README, contribution rules, documentation index, glossary and PR checklist.
- Historical roadmap snapshot and research applicability notices; original module reports, bilingual master research, functional proposal and HTML remain unchanged.
- Retire ADR-0006's unaccepted gate proposal; update only obsolete milestone triggers in ADR-0004/0005.
- Align GitHub M0–M7 milestones, move existing tasks to their current outcomes, close superseded M8, and add implementation/pilot/launch and parallel commercial tasks (#10–#15). Preserve tracker snapshots outside the repository.

## How it was verified

- Reviewed all nine supplied roadmap sections, the M0–M7 outcomes/exits, parallel commercial work, quality, versions, capacity-based estimates and future-module conditions against the English roadmap.
- Checked 30 changed/new Markdown files and 121 local file links; no missing targets.
- Confirmed 11 supplied source files remain unchanged and the historical roadmap matches its prior Git version.
- Checked whitespace, repository boundaries and absence of attribution/context material in the new planning files.
- Verified current GitHub issue/milestone assignments, unset due dates, retired M8 and open PR status.

Application tests are not applicable to this documentation-only change. Design accessibility review begins in M1; construction CI and implementation checks begin in M3.

## Definition of Done

- [x] Acceptance criteria of the linked issue are met
- [x] Risk-appropriate checks pass (documentation verification; construction CI from M3)
- [x] Relevant accessibility checks considered (no interface change)
- [x] Security and privacy impact considered (existing obligations preserved)
- [x] Documentation updated
- [x] `CHANGELOG.md` updated

## Notes for the reviewer

Review the current roadmap and ADR-0007 first. This PR changes planning, not the product's implemented state: the capability commitment matrix, new synthesis and prototypes are still pending. Source personal coordination references remain outside Git under the workspace agreement.

Stacked on #8 (`docs/m0-discovery`), which is stacked on #7. Review order: #7, #8, this PR. After each earlier squash merge, transplant only the dependent commits, retarget, and verify the remaining diff. No PR has been merged; merges remain the owner's responsibility.
