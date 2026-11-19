LC response, C06 Q17 — locked at 20:00 HKT, Tuesday 17 November 2026 (H+36), before colleagues' answers.

The forensic firm gets a narrower, masked data set tonight, not a copy of the full diagnostic image. Access to the full image is given only inside a bank-controlled environment, once the firm shows it is needed. The Board is briefed tonight and asked for four decisions, the first being whether production recovery may proceed with two unexplained mismatches.

Internal bank procedure: N/A for both units. PH01 is not in my allowed manifest (search "PH01": 0 hits).

## Q17a — Forensic firm's request for the diagnostic image

**Decision and action.** A staged release.
1. Now: a minimised data set. It holds the system artefacts the firm needs (logs, configuration, process records and the two mismatched instructions), with customer personal data masked or tokenised.
2. If the firm shows in writing that the full image is necessary: its named analysts examine the image inside the bank's offline laboratory. The image stays in the bank's custody.
3. A full copy leaves the bank only if step 2 is technically unworkable, with my written approval and SEC's sign-off, and with the Police informed if the image is among the evidence referred.

**Conditions before any transfer.**
- A signed engagement or addendum covering:
  - use only for this incident and only on the bank's instructions;
  - confidentiality undertakings by the firm and its staff;
  - compliance with the privacy and critical-infrastructure statutes;
  - no sub-contracting without consent;
  - immediate reporting of any loss or unauthorised access;
  - an audit right for the bank;
  - Hong Kong law.
- A written statement of need from the firm: which artefacts, for what question, and which data fields.
- SEC confirms the released item is a hash-verified copy; the original stays under the evidence hold, with a custody entry.
- Management approval of the extract is recorded.

**Conditions on transfer.**
- Strong encryption on registered media, hand-delivered by bank staff against a signed receipt; keys sent separately.
- No email and no internet file-sharing service.
- An inventory check after delivery.

**Conditions on use.**
- Processing and storage in Hong Kong only, in an isolated environment, by named analysts, with an access log.
- No onward disclosure to anyone, including the support vendor, insurers or affiliates, without the bank's written consent.
- Any demand from an authority is referred to the bank first, unless the law forbids that.
- Deletion or return on completion or on request, with a destruction certificate.
- Findings are reported to LC and SEC only.

**Missing facts and conditional action.** I do not know the firm's engagement terms, why it wants the image, or how many customers' data the image holds. If the engagement lacks the terms above, nothing is released until the addendum is signed.

**Owner and executing party.** LC is accountable for the release decision and the conditions. SEC prepares, hashes and delivers the data set. The firm's engagement lead signs.

**Timing (judgment).** Minimised data set released by 22:00 HKT tonight if the conditions are met, so the mismatch analysis is not delayed. Supervised access to the full image is available from 08:00 HKT on Wednesday 18 November, if justified.

**Recipient and channel.** The retained Hong Kong forensic firm, by hand delivery of encrypted media or by supervised access in the bank's laboratory.

**Basis and application.**
- R10, Cap. 486 Personal Data (Privacy) Ordinance (statute), Schedule 1.
  - Principle 2(4) (p.168): a data processor "processes personal data on behalf of another person". The firm is one.
  - Principle 4(2) (pp.169–170): the bank "must adopt contractual or other means to prevent unauthorized or accidental access, processing, erasure, loss or use of the data transferred to the data processor".
  - Principle 2(3) (p.167): contractual or other means "to prevent any personal data transferred to the data processor from being kept longer than is necessary".
  - Principle 3(1) (p.168): personal data "shall not, without the prescribed consent of the data subject, be used for a new purpose". Judgment: investigating a security incident is directly related to the purpose for which the data is held. s.58(2) (p.119) also exempts use for crime detection where applying the principle would be likely to prejudice it.
- R16b, HKMA circular "Customer Data Protection" (14 October 2014), Annex (supervisory circular).
  - Section C (p.4): rights to "transmit customer data to external parties should be granted on a need-to-have basis only".
  - Section C (p.4): massive download tools "can be used only upon proper approval from the management".
  - Section I (p.8): service providers that "store, transport or have access to customer data" must comply with the bank's data security policies.
  - Section G (p.7): "Adequate reconciliation or inventory check should be performed as soon as practicable during and after the relocation or transportation".
- R12 SPM SA-2 para 2.5.2 (p.6, non-statutory guideline): safeguards include "access rights to AIs' data delegated to authorized employees of the service provider on a need basis". Applied by analogy; whether this engagement is "outsourcing" is a judgment.
- R02 Code of Practice (Generic) (code of practice).
  - para 7.2.3(h) (p.33): "The CI operator should engage capable incident response and forensic examination personnel".
  - para 7.2.3(a)(v)(2) (p.32): evidence handling includes "chain of custody".
  - para 6.2.22(f) (p.19): "Sensitive digital data should be removed or masked if it is used in the testing environment." General reference only: for these obligations the bank follows the sectoral code.
- R03, HKMA Sectoral Code para 6.2.25(a) (p.19) governs supplier risk for the bank, but it points to a 21 December 2023 circular and an assessment matrix that are not in my manifest.
- No direct rule located in assigned sources on giving a forensic firm a full image as against an extract. The staged approach is professional judgment.

## Q17b — Escalation to the Board

**Decision and action.** I escalate tonight. The Board chair is telephoned by 20:30 HKT. A written paper follows by 21:30 HKT. The Board, or its delegated committee, meets by 22:00 HKT, and in any event before any production recovery step that needs its decision.

**For the Board to note.**
- The core function has been disrupted for 36 hours and the original gateway is still impaired.
- Some SMEs report missed payroll cut-offs. Two counterparties are asking about unsettled instructions.
- Whether the Board-approved tolerance for disruption has been breached. I do not have that figure; management must state it.
- Recovery evidence: the offline test reconciled 118 of 120 instructions. Two mismatches are unexplained. No recurring encryption was seen, but only within the test window.
- Data: 320 customers' records are verified as public. The claim of up to 18,000 is unverified. A fake verification page is targeting customers.
- Ransom: no payment and no contact. The attacker's deadline has passed.
- Authorities engaged: the HKMA, the Commissioner of Critical Infrastructure, the Privacy Commissioner and the Police. The statutory written report is due by 30 November 2026 and asks whether the Board was informed.
- Legal exposure: customer and counterparty claims, the vendor relationship, and possible regulatory investigations.
- The forensic data-sharing conditions in Q17a.

**Decisions for the Board.**
1. Recovery risk: approve, or expressly delegate with conditions, the gate for returning payment processing to production while the two mismatches are unexplained. SEC's Q16 defines the gate. My advice is that this risk acceptance sits with the Board; a hold or a narrower service mode sits with management.
2. Ransom: minute the "do not pay" posture. Earlier Board confirmation could not be verified.
3. Customer remediation: approve the principle and a budget for reimbursing losses from missed payroll cut-offs and failed or duplicated transfers, so customers can be told how to claim.
4. Oversight: set a crisis committee and a reporting rhythm until closure, direct remedial priorities if the tolerance is breached, and commission an independent root-cause review that covers the vendor.

**Missing fact.** I do not know whether the bank or a parent is listed. If either is, a market disclosure assessment is needed; that is outside my sources.

**Owner and executing party.** LC decides the content and drafts the legal and regulatory sections. The Chief Executive presents and is accountable for management's reporting. The company secretary convenes (judgment).

**Recipient and channel.** The Board chair and directors, or the delegated committee, by a telephone or video bridge and a written paper on a channel SEC confirms is safe. Legal advice goes in a separate privileged section (judgment).

**Basis and application.**
- R06 SPM OR-2 (non-statutory guideline).
  - para 3.2 (pp.5–6): "senior management should provide regular and timely reports to the Board on the ongoing operational resilience of the AI's business units, particularly when significant deficiencies could affect the delivery of the AI's critical operations".
  - para 3.4 (p.6): the Board must "ensure appropriate action is taken by senior management to address any deficiencies identified in an AI's ability to remain within its tolerance for disruption".
  - para 3.3 (p.6): "The Board is responsible for approving the tolerance for disruption".
- R07 SPM TM-G-2 para 2.1.1 (p.5, non-statutory guideline): "The Board of Directors and senior management of AIs have the ultimate responsibility for business continuity planning and the effectiveness of their BCP."
- R08 SPM TM-G-1 (non-statutory guideline).
  - para 2.2.3 (p.8): reporting "where appropriate to the Board or its designated committee" on "any material IT-related issues".
  - para 2.3.4 (p.9): risk acceptance needs "approval of the risk acknowledgement from the owner of the risk and senior management". That is the minimum level. Taking the recovery decision to the Board is my judgment, given a core function of designated infrastructure.
- R02 Annex F, section E.1 (p.46, code of practice): the written report asks whether the incident was communicated to "The Board of Directors / Senior management".
- R05, HKMA circular (22 June 2010), p.1, "Customer notifications" (checked against the scan): customers should be told "whether the bank would reimburse any losses incurred by them and if so, how they can apply for compensation". That requires a decision on remediation.
- R13, HKMA circular (1 June 2026), p.2: "The Board and senior management should continue to lead by example".
- No direct rule located in assigned sources fixing when or what to escalate to the Board during an incident. The timing and the list of decisions are professional judgment.

## Search record and limits

- All documents, regex "forensic|diagnostic|anonymis|pseudonymis|masking|mask": 6 hits (R02 pp.19, 33; R11 p.5; R16b p.4).
- R02, regex "supplier|service provider|third part": 37 hits. R03, regex "Supply Chain|non-disclosure|external service provider": 7 hits.
- All documents, regex "report(s|ed|ing)? to the Board|escalat": 12 hits; relevant ones at R06 p.5, R07 p.6, R08 p.20, R14b pp.6–9.
- R14b, "Board": 4 hits.
- Not in the manifest: the forensic firm's engagement terms, the December 2023 HKMA third-party circular, the bank's tolerance for disruption, and listing rules.

## Simulated actions for the facilitator to log

1. 20:10 — LC sends the release conditions to the forensic firm and asks for its statement of need.
2. 20:30 — LC and the Chief Executive telephone the Board chair.
3. By 21:30 — Board paper circulated.
4. By 22:00 — Board or committee meeting held; decisions minuted.
5. By 22:00 — SEC releases the minimised data set, if the conditions are signed.
6. Next HKMA update — LC reports the Board's decisions.