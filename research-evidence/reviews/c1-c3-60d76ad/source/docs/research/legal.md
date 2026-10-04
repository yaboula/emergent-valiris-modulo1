> Historical discovery context (September 2026). The [current first-product roadmap](../project/roadmap.md) supersedes the former M0 subphases, Gate 1/2 and seven-module v1 timetable. Findings remain research inputs; old milestone references are historical, not launch commitments. No commercial validation is established.

# Legal and provider-policy constraints

Checked: 2026-09-28. This is an engineering constraint register, not a legal opinion or a compliance certification. Product proposals below must become traceable requirements in M0.3 and be reviewed before real guest data, live charges or promotional messages are enabled.

## Privacy and communications

| ID | Source constraint | Proposed product implication | Verification / owner |
| --- | --- | --- | --- |
| L-01 | GDPR Articles 5, 6, 7, 13 and 25: lawful basis, purpose limitation, minimisation, transparent information and privacy by design | Document basis by purpose. Necessary booking processing need not rely on marketing consent. Keep optional promotions separate and unchecked. Store consent purpose/channel, wording version, timestamp and withdrawal. | M0.3 consent flows; M1 tests; product owner |
| L-02 | GDPR Articles 15–22, 28, 32–35 and 44 onward: rights, processor contracts, security, incidents, risk assessment and transfers | Map restaurant/controller and Valiris/processor roles per activity; Valiris may separately control its own account/billing data. Plan scoped export/deletion, retention, subprocessors and transfer assessment. Document the breach-notification workflow and whether a DPIA is required. | M0.4 data inventory/security design; before production |
| L-03 | LOPDGDD Articles 5, 7 and 32 cover confidentiality, children's consent and blocking of data | Staff access must be limited. Define minors' participation before collecting loyalty data. Erasure must account for justified statutory blocking; do not promise immediate deletion of every record. | M0.3 privacy requirements; production review |
| L-04 | LSSI Articles 20–22 constrain electronic promotions and require an effective opt-out; Article 21(2) contains a limited prior-customer exception | The existing v1 direction uses explicit promotional opt-in. This is a deliberately narrower product policy, not a claim that the law has no exception. Recheck suppression immediately before sending, including retries. A booking does not itself enable reactivation campaigns. | M6 campaign/suppression tests |
| L-05 | LSSI Articles 10, 22(2), 27–28 cover identification, applicable cookies, contracting information and confirmation | Publish legal/privacy information and clear booking/payment terms. Avoid nonessential tracking by default; any optional trackers require classification and a suitable consent mechanism. | M2/M3 guest-flow review |

Sources: [GDPR](https://www.boe.es/doue/2016/119/L00001-00088.pdf), [consolidated LOPDGDD](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673), [consolidated LSSI](https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758). Role allocation and implementation details above are engineering proposals; they require an actual data-flow assessment.

Allergy notes tied to an identifiable guest may reveal health data under GDPR Article 9. Proposed minimisation: avoid persistent allergy profiles, request only what the reservation needs, restrict access/retention and assess the legal basis for any exceptional collection. Dish allergen information is a different data category.

## Food information

**L-06.** Regulation 1169/2011, Articles 9(1)(c), 21 and 44 and Annex II, requires applicable allergen information, including for non-prepacked food. Annex II's fourteen categories are gluten-containing cereals, crustaceans, eggs, fish, peanuts, soybeans, milk, specified nuts, celery, mustard, sesame, sulphur dioxide/sulphites above the specified threshold, lupin and molluscs. Definitions, named subtypes and exceptions matter; a checkbox taxonomy does not replace recipe knowledge. [EU regulation and amendment history](https://www.boe.es/buscar/doc.php?id=DOUE-L-2011-82311).

**L-07.** Spain's RD 126/2015 Article 6 permits oral allergen information under conditions including an accessible written/electronic record and the required customer notice. It does not require a QR menu or every allergen icon on every printed dish. [Consolidated Spanish rule](https://www.boe.es/buscar/act.php?id=BOE-A-2015-2293).

Proposed M2 controls: owner-reviewed dish/variant records; distinguish unknown, declared present and reviewed absence; prevent an unknown record from appearing allergen-free; show words as well as icons; keep record changes attributable; offer a staff-assisted route. Software cannot establish that a kitchen is free of cross-contact. The conversational product must never infer ingredient safety or invent an allergen answer. Review the consolidated EU annex before implementation, including subsequent exemptions.

## Public reviews

**L-08.** Google prohibits incentives in exchange for reviews and discouraging negative reviews or selectively asking for positive ones. [Google Maps fake-engagement policy](https://support.google.com/contributionpolicy/answer/7400114).

Proposed M4 controls: apply the same review-invitation eligibility to comparable completed visits regardless of feedback score; preserve the Google link on every feedback path; no rewards for posting; no staff review quotas or demands for particular review content. Loyalty rewards attach to eligible visits, independently of reviews. Keep reply suggestions under owner approval and do not publish private guest details in a public reply. Tests must cover low ratings and the negative-feedback path.

## WhatsApp and conversational features

**L-09.** The Business Messaging Policy inspected here was updated **2026-09-23**. It requires recipient permission, respecting opt-outs, approved templates for business-initiated messages, and templates outside the rolling 24-hour window from the guest's last message. Automation must provide a clear escalation route. It also restricts regulated goods, including alcohol, subject to specified exceptions. [Current messaging policy](https://whatsappbusiness.com/policy/).

Proposed M7 controls: record purpose/channel permission; calculate the window from inbound guest messages, not outgoing sends; keep template category/status and delivery failures observable; disable campaigns when approval/permission is missing; provide human contact; never request full card details in chat. Apply channel restrictions to beverage recommendations and promotions rather than treating restaurant menus as automatically exempt. Template approval, fees and recipient quality limits need a provider check at implementation.

**Provider prerequisite:** an indexed official version of the Business Solution Terms, modified **2026-03-06**, restricts AI technology offered as the primary functionality, contains regional exceptions, permits AI providers as contracted service providers subject to conditions, and restricts reuse of messaging data for model training. This supports investigating an ancillary restaurant-service workflow; it does not grant approval for Valiris. Direct retrieval redirected to a login page, so the latest consolidated terms remain unverified. Confirm eligibility, provider contracts and data-use settings before M7 live use. [Indexed official version](https://www.whatsapp.com/legal/business-solution-terms?lang=ur), [current entry point](https://www.whatsapp.com/legal/business-solution-terms).

**L-10.** The AI Act's Article 50 addresses informing people that they are interacting with an AI system. Proposed flow: explicit disclosure on the first conversational interaction and a human escalation option; confirm applicable roles and dates before production. [Consolidated AI Act retrieved, Articles 50 and 113](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A02024R1689-20260727).

## Deposits and card guarantees

**L-11.** PSD2 Article 97 and its authentication rules require SCA in applicable situations and define exemptions; the application must not decide that a small charge is automatically exempt. Let the payment provider handle authentication and issuer outcomes. [PSD2 official publication](https://www.boe.es/doue/2015/337/L00035-00127.pdf), [authentication RTS](https://www.boe.es/doue/2018/069/L00023-00043.pdf). Recheck the applicable consolidated rules and Spanish implementation before live payments.

**L-12.** Stripe SetupIntents collect credentials for later payments without taking an immediate payment; successful setup is not a guarantee of a future charge. [Stripe SetupIntents](https://docs.stripe.com/api/setup_intents).

Proposed M3 controls: distinguish deposit taken, saved payment method and temporary authorisation hold; disclose the amount/trigger, cancellation deadline and refund conditions before acceptance; retain the accepted terms version. Use provider-hosted/tokenised collection, signed webhook verification and idempotent settlement. Test authentication-required, declined later charge, cancelled/expired hold, refund and duplicate webhook outcomes. Never store PAN/CVC or treat a redirect as payment completion. Restaurant merchant onboarding and the money flow require an M0.4 payment ADR; no model has been selected by this research.

## Gate implications

The essential constraints are implementable design inputs, not proof of compliance. M0.3 must map L-01–12 to requirements and acceptance criteria; M0.4 must resolve retention, provider/data-region choices, tenant isolation and payment responsibilities. M2/M3/M6/M7 must recheck the relevant law and provider rules before live activation. No campaign, provider account or real charge was created during this research.
