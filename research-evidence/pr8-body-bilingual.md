## Summary

Assemble M0.2 discovery evidence for independent restaurants and cafes in Spain: market and competitor research, a 50-review ledger, an interview guide, three explicitly fictional scenarios, a legal register, and a provisional Gate 1 recommendation. Add seven separately collected module reports and an English-edited methodological framework with direct links to its principal references.

The module reports are research inputs, not verified product requirements. Several claims lack direct source URLs and need item-level verification before use in the M0.2 synthesis. The methodological framework is broader than the restaurant product; its Spanish source remains outside the repository. Gate 1 and commercial demand remain unvalidated.

Relates to #2. Keep the issue open until the owner records the Gate 1 decision.

The Storefront + Digital Menu master report is also included in its exact Spanish source version and a complete English translation: 59 products across three regions, 23 numbered sections, and five appendices. The source-language copy is included at the owner’s explicit request.

## Type of change

- [ ] Feature
- [ ] Fix
- [x] Documentation / research
- [ ] Refactor
- [ ] Build / CI / tooling

## How it was verified

- Recounted the existing 50 review IDs and source locators; reconciled theme, sentiment, and year totals.
- Checked the published 2025 DIRCE series and recalculated the employee-stratum sums.
- Confirmed all three interview scenarios are marked fictional and excluded from demand evidence.
- Confirmed seven module reports, English filenames, and no personal workspace files in the commit.
- Checked local links, 39 defined reference links in the methodological framework, and absence of unresolved citation tokens.
- Ran `git diff --cached --check`; verified the commit author is Yahya and has no trailers.

Application tests and accessibility checks begin in M1; this PR contains documentation only. See `docs/research/verification.md` for the earlier discovery evidence checks.

- Verified the bilingual master report: 87 headings, 403 table rows, 213 URL occurrences in identical order, all numeric values, unchanged codes in the 20/19/20 product matrices, and a byte-identical Spanish source.

## Definition of Done

- [ ] Acceptance criteria of the linked issue are met (Gate 1 pending)
- [ ] Tests added/updated and passing (from M1)
- [ ] Accessibility checks pass (from M1)
- [x] Security and privacy impact considered
- [x] Documentation updated (ADR / SRS / glossary / README)
- [x] `CHANGELOG.md` updated if relevant

## Notes for the reviewer

Read `docs/research/README.md` first. The module reports in `result-research/` need source verification and synthesis before product scope is approved. ADR-0006 remains proposed. The English framework replaces opaque source markers with a readable reference list, but the supplied report's citations could not be mapped one-to-one to URLs; check time-sensitive numbers and legal or funding claims against the current primary sources.

This PR is stacked on #7 (`docs/m0-kickoff`). Review #7 first. After its squash merge, transplant the research commits onto the resulting `main`, retarget this PR, and confirm its diff contains only M0.2 changes.
