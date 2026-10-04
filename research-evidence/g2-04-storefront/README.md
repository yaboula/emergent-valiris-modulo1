# G2.04 — ORILLA content delivery 1.0

4 October 2026 · Author evidence under [M1 #5](https://github.com/yaboula/valiris-restaurants/issues/5) · **Useful preliminary content; partial pending applied SEO/GEO review.** G1 remains sole PM. This request was supplied by the founder in the current chat; the older prepared/not-sent metadata describes contract preparation, not this execution. No other specialist was activated or contacted.

## Deliverables and versions

| Artifact | Version and use |
| --- | --- |
| [Single case](../../docs/design/orilla-case.md) | ORI-CASE-1.0: developed origin/people/place, 11 dish identities, 13 contextual format offers, four categories, two aubergine variants, visit facts, example food records and frozen scenarios. Sole maintained factual fixture. |
| [Situated content/copy](../../docs/design/m1-storefront-content-and-copy.md) | ORI-COPY-1.0: usable H01–H04/M01/D01 copy, source/maintenance mappings, 30 state strings/patterns, label resolutions, proposed phone openings and discovery/resource questions. Spanish proposals in English documentation. |
| [Author contrasts](author-review.md) | Editorial coherence, negative cases, limits and corrections; no independent or real-use evidence. |
| [Verifier](verify.py), [checks](checks.json), [source manifest](source-manifest.json) | Bounded integrity/amount/recipe/clock/reference checks, owned-path boundary and original-source preservation. Documentation helper only, no application implementation. |

The **published content commit and PR** are recorded in the [delivery handoff](delivery.md). That commit contains both case and copy: specialists should adopt it together, cite IDs/revisions and return recommendations against that exact SHA. Evidence added afterwards does not introduce another case version. The branch is `docs/m1-g2-04-orilla-content`; isolated checkout is `D:/the next level/valiris-restaurants-worktrees/g2-04-orilla-content`.

## Baseline, dependency and reading scope

Before editing, repository root, clean state, own branch/HEAD and worktrees were verified. G1 source worktree remained on its own branch. GitHub PR #34 and `git ls-remote` both established the same published operational baseline: **`6046327ee9216e26ed56aeac81c346f7299735d8`** on `docs/m1-g1-orilla-architecture-handoff`. New worktree/branch started there; no substitution of main. The app worktree tool returned “Not a git repository” for the chat root, so Git created the required isolated worktree in the identified repository.

Direct stack dependency is **#34**, itself based on architecture **#33**, which depends on shared contracts **#32**, specialist contracts **#31** and prior #29/#28 inputs. Independent conceptual review #30 is a separate reviewed source, not a commit to merge silently into this branch. G1 controls the wider integration order, including the shared product #21 and parallel #22 history. The new PR targets #34's branch; it contains only G2.04 routes. No milestone/issue-closing directive or merge is requested.

Sources were read for this delivery, completing applicable content after truncated outputs. Whole document text: AGENTS, CONTRIBUTING, operating index, common brief/context/protocol, current G2.04/SEO contracts, working agreement, roadmap, functional definition, M1 briefs, IA v0.2, CR/XR, G1 architecture receipt, PV/J1–J2, C1–C3 connected package, coverage/evidence, brand foundation/refinement and exact selection. For the large connected/coverage ledgers, display-link labels were retained while long link targets were suppressed for bounded semantic reading; original files remained intact. HANDOFF's full 554-line text was read, including the operational entry, review continuity and preserved historical appendix; long display-link targets were suppressed in the later reading chunks. Superseded stack/calendar/gates and external-evidence instructions remain history, not current execution authority. Completing that historical reading changed no case/copy fact or decision. Original J1/J2 criteria and cross-rules plus relevant ADR-0005/0009/0011 were read; no new exhaustive audit of every earlier state package is claimed. The G4 selected-direction report was consulted from its exact Git commit `2b2a4a3bf5506c94b95d9b177f6006946200df24`; its application limits remain.

The input/source manifest pins Git references and hashes. C1–C3 informed behaviour, not ORILLA amounts/stories. No external local-cultural assertion, legal advice, technical SEO rule, live menu evidence, new benchmark or image inspection was used to invent credibility. Selected graphic concepts are referenced through their versioned guide; this content delivery does not claim a new visual review of their raster assets.

## Received requests and authored responses

**Received:** G2.02's versioned CR01–CR07/XR01 at frozen architecture `ff8fc061dfb4e63461ee2b77b5a18f02108edb6b`, made available through the founder's assignment and repository. These are source requests, not messages received directly from another chat. The title's IA v0.1 residue is known in G1's receipt; source remains untouched.

| Request | Authored response / exact record and placement | Resolution and residual review |
| --- | --- | --- |
| CR01 | Case §§2–3: STORY-01, PEOPLE-01/02, CONCEPT; copy H01/H02/H03 | Specific sibling/table/portion origin, linked to food and room. Content supplied; G2.02 adoption and UI review pending. |
| CR02 | EXPERIENCE-01–04 + VISIT-03; H03/H04 | Light room, individual/shared occasions, audible-room limit, group/access conditions. Authored hypotheses, no researched audience or premise. Adoption pending. |
| CR03 | MENU-01/C01–C04, DISH-01–11, P01–P13, FOOD rows; H02/M01/D01 | Actual compact menu, complete names/descriptions/amounts/units and long aubergine name; source only in case. Categories/jump labels proposed, not imposed on IA. |
| CR04 | D02/V01/V02/P02/P03; D10/P11/P12; D04/P05; SCENARIO-00–04/07 | Meaningful portions/recipe/wine formats and rice minimum. D08/P09 temporary override, restoration, next-service unknown and withdrawal differ. One menu/room; no fake terrace or daily menu. |
| CR05 | VISIT-01–03 + SCENARIO-04/06/09; H04 and S01–S12 | Local/kitchen/service clocks, scoped exception and unknowns; no real address/contact/channel. No implied booking or global access certification. |
| CR06 | FOOD-01–11, FOOD-02-V02, DIET-01, CHANGE-01; D01/S21–S25 | Explicit assumptions/positive examples plus pending fields; variant yogurt removal never proves absence. Private sesame revision retains earlier positives, price/status and unaffected V02. All unverified; G2.05/real source review absent. |
| CR07 | ASSET-01–04; copy §6 | Brand illustration versus conceptual dish/fictional room; recipe/portion/version linkage, misleading-inference limits and text-only fallback. No production commissioned. |
| XR01 | Copy §5 plus H02/H03/H04/M01/D01 | Retain La cocina/Ver carta/Conocer ORILLA; propose Nuestra mesa and consistent Horarios y visita. Plain category jump variants share existing IDs. G2.02 adoption/comprehension review pending. |

“Response supplied” means G2.04 has produced reviewable content. It does **not** mean G2.02 marked its own request resolved/adopted or a recipient reviewed it. This record does not modify their frozen request/status file.

## Cross-review received versus pending

| Contributor / source | Actually received / affected closure |
| --- | --- |
| G1 architecture review on ff8fc06 | Existing bounded receipt read: structure usable for content/preliminary exploration. It does not review this new case/copy. |
| G4 conceptual review on e7065aa, report 2b2a4a3 | Existing bounded conceptual outcome; no mandatory material correction in that scope. No review of new content, UI or applied accessibility. |
| G2.02 adoption | Not received. Prepared CR/XR response identifies new source for their next version; IA frozen. |
| SEO/GEO applied review / XR02 | **Not received.** Five source-linked editorial questions and metadata candidates prepared in copy §7. G1 coordinates availability/dispatch; SEO uses the exact published delivery SHA in its own routes. This missing contribution makes the package partial at joint-content acceptance. UI may explore with that label. |
| G2.05 | Not received. ES author copy plus three unreviewed orientative EN notices; no four-language content or linguistic approval. |
| G2.07 / G2.03 | Not received. PC first/phone later, proposed length variants and actual origins/states require composition/behaviour review. No render, click/focus/device or prototype evidence. |
| G2.06 / G2.08 | Not received for these situated requests. Direction preserved; productive sources/rights/resources pending. |
| G4 application / participants | Not received; author documentary checks cannot substitute for independent application review, accessibility or real use. |

No contact, chat messaging, delegation, site publication, purchase, product code/configuration, issue closure or merge occurred. Commit/push/draft PR are this assignment's authorised delivery actions. 72-capability scope, separate S1/S2, public anonymous reading, registered/authenticated personalisation and deferred standalone audio/3D are preserved. No new material founder question blocks the independent first content version.

## Editorial method provenance

Primary: **ux-writing-content-design (Hueyexe)**, read from the installed SKILL.md. Applied task → entry/action/feedback/return → situated state pattern, four editorial passes, calm uncertainty and whole-string localization. Secondary: **rampstack-content-and-copy (Rampstack)**, read from the installed SKILL.md. Applied reader/goal/working voice, structure before prose, specifics that earn space and pre-publication editing. Neither method is evidence of actual comprehension. Generic CMS front matter, slogan lengths or SEO metrics were not imposed on a product-content contract. Skill paths/content hashes are pinned by the verifier for provenance; no skill was installed or changed.

## Next usable review

G1 can hand this identified version to G2.02/G2.07 immediately for representative PC composition, identifying missing SEO/GEO cross-review. SEO returns XR02 and findings by block/source/objective/effect; G2.04 accepts/rejects/changes them in its own next version. G2.02 adopts case/copy IDs and label resolutions in its own branch, G2.03 checks origins/state recovery, and G2.07 returns PC then phone findings before length variants are accepted. New recipe/amount/hour changes invalidate only dependent text/languages/resources. No second menu, dossier or PM is created.
