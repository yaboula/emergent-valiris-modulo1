# C1-C3 focused independent correction recheck

Reviewed 2 October 2026. Responsibility: G4 independent Quality. Consolidation: G1. Correction ownership: G2 Product Designer.

## Verdict

**G4-01/P2 is resolved at the documentary specification level on immutable commit `c4f219cf5f06a3fe55b1d4e2040c6f6f45c584df`.** The corrected contract now distinguishes locally entered content, confirmed saved draft revision, unknown save result and a competing saved revision before publication review. The four required contrasts remain coherent across the referenced recovery cards. This does not prove implementation correctness.

The separate X05 clarification is also resolved: unknown food records explicitly form a labelled group inside the filtered result, while a positive declared milk record remains excluded even when other information is incomplete. The previous report did not classify this clarification as a second demonstrated defect.

No contradictory route requiring the original finding to remain open was identified in this bounded rereading. This finding closure does not close C1-C3 as a complete product deliverable, the content-preparation block, draft PR #21 or M1/#5.

## Baseline and scope

Sources: `D:\the next level\research-evidence\reviews\c1-c3-c4f219c\source`, the frozen GitHub PR #21 draft/head supplied for this recheck. Line numbers below refer to that snapshot, not the concurrently edited working checkout.

- `docs/design/m1-connected-journey.md`, SHA-256 `8C661B05629BC6858DEE275456BF50E7E24E279EB642D558C9A4CBB9650DDBD9`.
- `docs/design/m1-content-preparation.md`, SHA-256 `49048796905BCAF44EB9E415F0B3C987B6687B61F8170EFAE8BF8EE0441EBCC5`.
- Original independent finding retained at `D:\the next level\research-evidence\reviews\c1-c3-60d76ad\g4-review.md`, against baseline `60d76ad602d83ca70124eeac4e1fab20329255d1`.

Read the corrected O02/O03/O05, X05, CP-X01/CP-X02/CP-X03, DS01-DS04 and strictly necessary CP-R01/CP-R02/CP-R03 references. Rechecked source R04/R05, J4.4 and J2.4. CP and ADR-0011 appeared after the original review; their presence supplies referenced recovery contracts, not a full review of their new capabilities. Neither ADR-0011 nor J10-J15 as a whole is certified by this recheck. Author expectations were compared with actual written destinations; their "consistent" labels were not treated as proof.

## G4-01 correction evidence

| Original missing contract | Current exact evidence | Independent documentary conclusion |
| --- | --- | --- |
| Lost draft-save result lacked a draft-specific recovery outcome | Connected line 230 names the original save operation, local 2,00 EUR, confirmed DR1 and recovered DR2; routes to CP-X02 rather than editorial publication. Content-preparation lines 313-319 distinguish original operation, confirmed/not-applied/conflict/denied/unknown, forbid inferring success from equal values and keep uncheckable results unknown. | Saved, unknown and not-applied are no longer conflated. O02 supplies the draft-save-specific found-result continuation even though CP-X02 is a generic register. |
| Competing saved private revision was not distinguished from current public price | Connected line 232 compares actual last-confirmed DR1/DR2, current saved DR3 at 2,10 EUR and local 2,00 EUR. CP-X01 lines 303-309 compares base/current/proposal, preserves unrelated work and requires a freshly reviewed choice, not an automatic winner. | Private-draft conflict can now be reviewed without presuming the current public price changed. |
| Which confirmed proposal O03/O05 reviews was unclear | Connected line 240 identifies the confirmed saved revision and labels any local preview unconfirmed; lines 250-252 revalidate reviewed source/version/permission and return an uncertain/competing save to recovery before publication. CP-R01 lines 125-131 distinguishes current/public/private bases and saves only authorised corrected content; CP-R03 lines 145-151 reserves actual publication for O05. | Draft save, local preview and authorised publication stay separate. Revalidation handles a newer source discovered after recovery. |
| Saving then leaving could silently discard an uncertain proposal | Connected line 232 remains in recovery or explicitly closes with unresolved status and permitted retention/clearing. | No silent assumption that unknown means saved, failed or safely disposable. The eventual retention mechanism remains pending. |
| Revoked access could be incorrectly retained to inspect/retry | Connected line 232 and CP-X03 lines 323-329 distinguish lost edit permission from lost venue/read access; hide private venue content, provide only permitted alternatives and leave inaccessible status unknown. | Recoverability does not invent continued reading/editing rights or claim a failed operation merely because access was revoked. |

## Required four contrasts

Each contrast resets to public coffee 1,90 EUR, local 2,00 EUR, confirmed private DR1 at 1,90 EUR and unrelated private croissant description, as stated in content-preparation line 454. DR2/DR3/DR4 are fictional proposal revisions, not executed persistence results.

1. **DS01 — save committed, response lost (line 458):** O02/CP-X02 correlates the original save, identifies confirmed DR2 at 2,00 EUR and reviews that revision in O03. O05 rechecks source/permission before publication. A later saved change cannot be silently ignored: O03/O05 source reconciliation sends it back to conflict review. Public coffee and croissant remain unchanged until a separate known authorised publication.
2. **DS02 — confirmed not applied (line 459):** only a known not-applied outcome uses this route; local 2,00 EUR remains distinct from last saved DR1. The latest permitted base is compared before explicit resave/refetch of a confirmed revision. Unknown cannot be treated as not-applied to justify blind retry. No publication or croissant insertion is inferred.
3. **DS03 — competing saved 2,10 EUR (line 460):** show DR1, current DR3 and local proposal separately; deliberately adopt current or review/save a new confirmed DR4. The chosen confirmed revision is reviewed again before O05. This preserves unrelated work and does not prescribe a whole-draft overwrite.
4. **DS04 — edit/venue access revoked (line 461):** read the draft only with remaining actual read authority; no resave/publication through revoked edit rights. With lost venue access, remove private source/proposal from view and use authorised workspace/access recovery. CP-X02/CP-X03 leave the result unknown if it cannot lawfully be inspected; public/private operation outcomes are not guessed.

**Result:** all four expected written distinctions are supplied. The assertions checked are state/route consistency, not operation execution, data retention or concurrency enforcement.

## X05 filtered-result clarification

Connected line 340 explicitly places **"Informacion incompleta: consulta al personal"** in a separately labelled group *within the filtered view*. **Ver carta completa** preserves full-menu discovery. Cheese with positive declared milk is excluded even if its remaining record is incomplete; unknowns are neither hidden nor mixed into an asserted safe group. This resolves the placement ambiguity noted against old line 330 and matches `m0-journeys-and-criteria.md` J2.4 line 60. This does not prove diners understand the wording or certify food safety.

## Limits and handover

- No rendered UI, functional prototype, server operation, physical output or real participant was tested. No visual/accessibility/security/compliance result is implied.
- M2/#4 still needs operation correlation, saved-source/version enforcement, concurrent writes, permission checks, persistence/local-retention/clearing and retry guarantees. A coherent written route is not a working guarantee.
- Other first-review limits remain: real food/translation/source material, FR/DE representative food notices, visual/print/interaction evidence, scoped technical review and remaining accepted design paths. This recheck does not remove those dependencies.
- The entire CP package, ADR-0011 and J10-J15 require their own assigned reviews. No full regression certificate or milestone closure is issued.
- G1 may record G4-01 as **resolved documentary finding at c4f219c**, retain the original report and this dated evidence, and continue the existing M1 assignment. G2 owns further design; G3 specifies implementation contracts. No new founder scope approval is required to record this correction.

Only this report was written. No repository/Git state, G2 source, HANDOFF, tracker or external communication was modified by this recheck.