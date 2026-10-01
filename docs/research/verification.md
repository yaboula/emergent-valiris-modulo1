> Historical discovery context (September 2026). The [current first-product roadmap](../project/roadmap.md) supersedes the former M0 subphases, Gate 1/2 and seven-module v1 timetable. Findings remain research inputs; old milestone references are historical, not launch commitments. No commercial validation is established.

# M0.2 verification record

Review date: 2026-09-28. Scope: documentation and research evidence. This record describes document verification; it does not certify providers, legal compliance or product performance.

## Evidence checks

- The ledger contains exactly 50 rows with sequential RM-001–050 IDs and unique source locators: 20 TheFork Manager, 20 CoverManager and 10 Loopy Loyalty.
- All 40 Apple locators, dates, star ratings and app versions match the retrieved public feeds. Capterra entries were checked against individually readable review passages; the method discloses indexed retrieval, selection bias and incentive labels.
- Recounted primary themes, text sentiments and review years match [review-mining.md](review-mining.md). One theme per record prevents double counting; positive and mixed reports remain in the sample.
- The ten DIRCE series match 2025 national enterprise counts, all legal forms, CNAE-2009 groups 561/563. The two derived 0–9 employee totals were recomputed. No count is represented as a validated buyer population.
- All three simulated profiles state that no interview took place and that their responses and numbers are fictional. They are excluded from the evidence sample.
- Public-source claims are separated from interpretations and proposed controls. Unknown tariffs, untested capabilities, historical complaints and incomplete policy retrieval remain explicit.

## Document checks

- Repository Markdown links to local files and heading fragments resolve; table column counts are consistent.
- `git diff --check` reports no whitespace errors.
- The documentation index, ADR index, glossary, repository introduction and changelog reflect the research. Accepted ADR-0001–0005 are unchanged.
- Repository contents exclude raw working feeds, personal files and session-management files. Commit identity follows the contribution agreement.

Application tests, accessibility automation and preview deployment start in M1 under `CONTRIBUTING.md`; M0.2 introduces no application code. No successful payment, campaign, external integration or measured business outcome is claimed.

## Review still required

**Gate 1 is pending, not passed.** [ADR-0006](../adr/0006-discovery-evidence-boundary.md) remains proposed. The product owner must review the evidence boundary and record the actual decision in [synthesis.md](synthesis.md#gate-1-review-record). Issue #2 cannot be marked done beforehand.

The research PR depends on M0.1 PR #7. After the owner squash-merges that PR, update the research branch onto the resulting `main` commit and retarget it before merging; preserve the research changes and verify the resulting diff. No PR has been merged by this work.
