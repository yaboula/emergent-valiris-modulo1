# ORILLA 1.0 — published content handoff

4 October 2026 · G2.04 · Refs [M1 #5](https://github.com/yaboula/valiris-restaurants/issues/5) · **Useful preliminary content; applied cross-review pending.**

## Exact version for consumption

Use **`5bd3184ca48be8d579e3f82d3361dbf5de0ed228`** for both case and copy, without taking one from another revision. This commit was pushed to `origin/docs/m1-g2-04-orilla-content`; `git ls-remote` and GitHub's PR head both returned that exact SHA before this evidence-only handoff was added.

| Source / version | Frozen Git blob | Use |
| --- | --- | --- |
| [ORILLA case](../../docs/design/orilla-case.md) / ORI-CASE-1.0 | `bade7126a2d4222227095a1f8e9fa6ae85c5c687` | Single restaurant reality; identity/story/people/room, MENU/DISH/P/variant/FOOD/VISIT/SCENARIO/ASSET records. |
| [Situated copy](../../docs/design/m1-storefront-content-and-copy.md) / ORI-COPY-1.0 | `bfc11eba8d86c2192e0c4fef766bf2728d7d15cf` | H01–H04/M01/D01, 83 copy IDs including 30 state records, same-source phone proposals and XR01/discovery questions. |

Each consumer cites content SHA, case/copy version, block/state and exact affected IDs. A response identifies location, factual source, purpose, effect and recommendation. G2.04 consolidates case/copy; G2.02 retains architecture consolidation; G1 resolves material discrepancies. A later handoff evidence commit may advance the PR head but must retain these two blobs for this version. New factual changes need a new identified content delivery and dependent-language/resource review.

## Git and draft review

- Draft [PR #35](https://github.com/yaboula/valiris-restaurants/pull/35): `docs(M1): develop ORILLA case and situated Storefront copy`.
- Own branch/worktree: `docs/m1-g2-04-orilla-content`, `D:/the next level/valiris-restaurants-worktrees/g2-04-orilla-content`.
- Published operating baseline: `6046327ee9216e26ed56aeac81c346f7299735d8` on `docs/m1-g1-orilla-architecture-handoff` / dependency [#34](https://github.com/yaboula/valiris-restaurants/pull/34). The PR targets that branch; main is not the execution baseline.
- Frozen architecture: `ff8fc061dfb4e63461ee2b77b5a18f02108edb6b` / [#33](https://github.com/yaboula/valiris-restaurants/pull/33). Inherited shared/specialist dependencies remain #32/#31; earlier selected sources and the independent #30 review keep their existing roles.
- Commit author and committer: Yahya `<yaboula@epsa.upv.es>`. English documentation/commit/PR, Spanish proposed content; no trailers.
- Only the two content documents and `research-evidence/g2-04-storefront/` are included. Temporary PR-body file remains ignored under `.cache/g2-04/`. Shared checkout, architecture, contracts, ADRs, criteria and other specialists' evidence remain intact.

PR creation readback confirmed **OPEN / draft**, correct base/head and seven owned files at the frozen content commit. The PR was attached to this Codex chat. Final evidence publication is checked by readback and a clean local status after its own push; the immutable content SHA above remains the review source.

## Verified and pending

The [checks report](checks.json) records passing bounded documentary checks: 11 dishes, 13 price/format offers, four categories, 12 example food records, 83 unique situated-copy IDs, 11 scenario branches, clock boundaries, source relationships and preservation of 44 input/ADR/graphic records. The [author review](author-review.md) records 18 editorial contrasts. Markdown links/table shapes and `git diff --cached --check` also pass. Running the helper again after evidence changes updates its link count without changing case/copy facts.

CR01–CR07 have author responses and XR01 has proposed resolutions. **No applied SEO/GEO review/XR02 or G2.02 adoption has been received.** G1 can dispatch this source to SEO and G2.02/G2.07 for early PC composition with that explicit partial status; no chat was messaged and no specialist was assumed active. Phone variants await deliberate adaptation after PC, with potential feedback to PC.

G2.05 language review, composed UI/behaviour/actual accessibility, productive resources/rights, G4 independent application review and participant evidence are pending. All restaurant facts are fiction and all food declarations are unverified examples. Author checks do not replace any of those reviews. M1/#5 and #15 remain open; no merge, live website, listing, purchase or product implementation was performed.
