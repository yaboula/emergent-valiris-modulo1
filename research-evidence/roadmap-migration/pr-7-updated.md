> Current planning (1 October 2026): the owner adopted a first-product M0–M7 roadmap. Historical phase names and schedules below describe this earlier delivery, not the current launch commitment. See issue #9 and its roadmap-alignment PR. No PR has been merged.

## Summary

M0.1 kick-off: working agreements and foundational decisions, so that every later change follows the same workflow.

Closes #1

## Type of change

- [x] Documentation / research

## What is included

- **Project charter** (docs/project/charter.md): purpose, honesty statement (studio-owned product, simulated client), quality bar, principles, how each official standard is tailored, roles and gates, initial risk register.
- **Roadmap** (docs/project/roadmap.md): incremental releases v0.0 to v1.0 and M0 phases with gates.
- **Glossary** (docs/glossary.md): ubiquitous language EN/ES with the platform/vertical/module layer of each term.
- **ADRs**:
  - 0001 record architecture decisions (MADR 4)
  - 0002 keep the Valiris studio brand, **accepted risk** after finding VALIRIS SAS (Paris, hospitality AI messaging), with mitigations
  - 0003 product name "Valiris Restaurants" and naming conventions
  - 0004 private repository + proprietary license until v1.0
  - 0005 English repository, Spanish-first internationalised UI

Already done outside this PR: labels (.github/labels.json, synced), milestones M0 to M8, issues #2 to #6 for the remaining M0 phases.

## How it was verified

- Markdown reviewed for internal links and consistency with the roadmap and the glossary.

## Definition of Done

- [x] Acceptance criteria of the linked issue are met
- [ ] Relevant verification complete (construction CI from current M3)
- [ ] Relevant accessibility checks (design in M1; implementation from M3)
- [x] Security and privacy impact considered (brand/legal risk documented)
- [x] Documentation updated
- [x] `CHANGELOG.md` updated

## Notes for the reviewer

- Please confirm ADR-0002 (brand risk) explicitly; it is the only decision with a known external risk.
- ADR-0005 sets English as the repository language; switching to Spanish later is possible, but costly.
