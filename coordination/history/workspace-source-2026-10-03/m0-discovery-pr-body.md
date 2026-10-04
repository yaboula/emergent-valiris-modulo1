## Summary

Complete the M0.2 discovery deliverables with Spanish market evidence, an advertised feature/pricing comparison, 50 traceable public software reviews, an original behaviour-based interview guide, three explicitly fictional scenarios, legal/provider constraints and a prioritised synthesis.

Recommend a conditional go for portfolio product definition. Commercial demand and business uplift remain unvalidated; proposed ADR-0006 makes the Gate 1 evidence boundary explicit.

Closes #2 after the owner records a passing Gate 1 decision.

## Type of change

- [ ] Feature
- [ ] Fix
- [x] Documentation / research
- [ ] Refactor
- [ ] Build / CI / tooling

## How it was verified

- Recounted 50 unique review IDs/source locators: 20 TheFork Manager, 20 CoverManager and 10 Loopy Loyalty. Theme, sentiment and year totals reconcile.
- Matched the 40 Apple records' IDs, dates, ratings and versions to the retrieved feeds; checked individual Capterra passages and preserved retrieval/selection limitations.
- Checked ten official 2025 DIRCE series and recomputed employee-stratum sums.
- Verified all three simulations are labelled fictional and excluded from demand evidence.
- Checked 29 Markdown files, 68 local links/anchors and table column consistency; `git diff --check` passed.
- Reviewed sources, privacy implications and product-policy constraints. Confirmed accepted ADR-0001–0005 are unchanged and commits have the configured author with no trailers.

Full verification record: `docs/research/verification.md`. Application tests, accessibility automation and preview deployment begin in M1; this change contains no application code.

## Definition of Done

- [ ] Acceptance criteria of the linked issue are met
- [ ] Tests added/updated and passing (from M1)
- [ ] Accessibility checks pass (from M1)
- [x] Security and privacy impact considered
- [x] Documentation updated (ADR / SRS / glossary / README)
- [x] `CHANGELOG.md` updated if relevant

## Notes for the reviewer

Start with `docs/research/synthesis.md`, then the ledger, source register and proposed ADR-0006. Research delivery is complete; Gate 1 remains pending your review, so issue #2 stays open. Record the actual decision/date/reference and accept or reject ADR-0006 before considering the gate passed.

This PR is stacked on #7 (`docs/m0-kickoff`) because the kick-off documentation is still awaiting review. Review #7 first. After its squash merge, transplant the two research commits onto the resulting `main`, retarget this PR and verify that its diff contains only research changes.

The feature bundle already has strong incumbent overlap. Differentiation through reliable mobile tasks is a hypothesis; 80% of the review sample comes from two booking apps. Fictional scenarios establish no demand. Unknown tariffs, untested capabilities and the latest WhatsApp Business Solution Terms remain explicit gaps. No provider account, campaign, payment or measured business result is introduced.
