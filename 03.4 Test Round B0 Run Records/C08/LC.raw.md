LC answer to C08 (Thursday 19 Nov 2026, 08:00 HKT, H+72). This covers my units Q23a and Q23b only. I locked it before seeing colleagues' answers and based it on the C08 handoff record. Where the handoff says an item "cannot be verified", I treat it as open, not done (PH01 s.18.2).

---

## Q23a – Compliance actions that stay open after handover, and who receives the register

**Decision**
- LC stays accountable. LC takes over the register of external deadlines and commitments item by item (PH01 s.18.4).
- Day-to-day holder: a named Compliance officer (Deputy Head of Compliance, regulatory reporting). This person signs acceptance of the specific item list.
- A second LC officer checks each item.
- The handover pack opens with a page listing everything not evidenced (PH01 s.18.2). Every item without a receipt or acknowledgement moves across as OPEN.
- Each item is chased on its own due date, and the whole register is reviewed weekly until all statutory reports are filed.

**Timing**
- Do before handover: the two "now" items below (HKMA 08:00 update, Commissioner confirmation).
- Register handover with signed acceptance: by 17:00 HKT, 19 Nov.
- First weekly review: 26 Nov. That is before the 27 Nov Annex F filing target.

**Destination**
- The register is delivered in print and electronically on a channel SEC has logged as safe.
- A copy goes to the CMT chair and the Chief Risk Officer.

**Open items** (owner / deadline or trigger / recipient and channel / basis)

1. **Commissioner: proof of the s.28 notification and record. Open, possibly late.**
   - Owner: LC duty officer.
   - By 10:00 HKT today:
     - Call the Commissioner's office to get the outcome of the 18 Nov 13:00 confirmation request: references, the logged time of the 16 Nov call, receipt of the Annex E, and whether the number used is the designated one.
     - If the Annex E receipt still cannot be confirmed, re-file the Annex E through the designated secure channel as a disclosed re-submission.
     - Record the possible missed deadline under s.28(3), and tell the CMT chair and the HKMA (PH01 s.18.5).
   - Basis: R01 s.28(2)–(3), Sch.6 item 2.
2. **Commissioner: written report (Annex F). Open.**
   - Inputs due 23 Nov 17:00; draft 24 Nov; check 25–26 Nov; file 27 Nov 17:00.
   - Statutory latest date: 30 Nov 2026.
   - Channel: designated secure channel. A copy goes to the HKMA.
   - After filing, send further facts as supplementary material.
   - Basis: R01 s.28(4), Sch.6 item 3 ("14 days after the date on which the CI operator concerned becomes aware"); R02 s.7.3.7.
3. **Commissioner: the new indicator from 18 Nov. Open; whether it is a new incident is not verified.**
   - SEC must give a written conclusion on whether it is related and whether the host is a critical computer system (CCS).
   - If it is related: report it as supplementary information.
   - If it is a new incident on a CCS: a new s.28 clock runs from the time of reasonable certainty — 12 hours if the core function is affected, otherwise 48 hours (R02 s.7.3.5; R01 Sch.6 item 1).
4. **MA: Cap. 653 s.22 material-change notifications. New open item.**
   - LC decides each change one by one (PH01 s.18.4). Recipient is the MA (the regulating authority for category 2 obligations), in the form and way the MA has specified (R03 s.6.1.3).
   - Deadline: "within 1 month after the date on which the event occurs" (R01 s.22(1), PDF p.33). The date of the event is the production deployment (R03 s.6.1.1).
   - Changes recorded in the handoff:
     - 16 Nov: gateway segment quarantine and flow blocking; vendor lockout; vendor path blocked at the perimeter; tokens, keys and certificates revoked; secrets rotated. **Due by 16 Dec 2026.**
     - 18 Nov: new detection rules (EDR/SIEM/DNS/proxy). **Due by 18 Dec 2026, if they are on or for a CCS.**
     - Secondary process: activation cannot be verified. **Conditional.** If it was activated and is essential to the core function, s.22(2)(c)/(d) may apply, with one month from activation.
     - Future return to production of the rebuilt gateway or access environment: one month from each deployment phase.
   - Professional judgment: changes that alter security configuration "affect the computer-system security" of the CCS (s.22(3)(a)(i), PDF p.34). I recommend notifying, using the collective option in R03 s.6.1.1 where it fits.
   - Detail left to judgment: R03 s.6.1.2 limits reportable changes to those with "high security risk implications", identified through risk assessment. SEC supplies that assessment by 30 Nov.
5. **HKMA. Open.**
   - The 08:00 update for 19 Nov is pending: make it now. Content: handover, open items, the second offline test result (test environment only), and live status as recorded.
   - Still to obtain: acknowledgements, and confirmation of the written route.
   - Clarify the status of BCP activation reporting and the Board outcome, and resend copies of the public updates decided at C03/C04 once COM has verified they were released.
   - Continue updates at 08:00 and 18:00 until the HKMA agrees otherwise. Report any missed Commissioner deadline.
   - Basis: R05 p.2–3 (supervisory circular), R07 s.1.3.3 (non-statutory guideline), PH01 s.5.8.
6. **PCPD. Open.**
   - Send an update notification covering:
     - notification completion figures for the 320;
     - outcomes of the Group B scope reviews;
     - the decision on the 31 scam reports;
     - the 18,000-record claim, still unverified.
   - Assess whether the 12 corrected contacts mean earlier notices went to wrong recipients. If they did, that is a further disclosure, and the PCPD update and those customers must be told.
   - Owners: DPO prepares, LC files.
   - Deadline: as soon as practicable, target by 25 Nov, and again on any change of scope.
   - Channel: R16a form by fax or in person.
   - Basis: R11 p.8 ("After the full details of the incident are revealed, all information should be submitted to the PCPD ... without delay"); R16b p.3.
7. **Police. Open.**
   - Obtain the reference number, the Police view, and any response under Cap. 455 s.25A.
   - Record any release of customer data, or that none was made.
   - Hand over further evidence on request.
   - Keep the tipping-off control on all communications (R16c s.25A(5)).
8. **Payment posture.** The Treasury hold and the no-contact instruction stay in force until the CMT chair or Board logs a release (PH01 s.18.3). The Board alone decides any departure.
9. **Vendor and contract.**
   - Escalate the preservation and production status and the contract terms (PH01 s.6.7(c)).
   - Any vendor access reinstatement needs LC to review the contract terms and SEC's written sign-off (s.7.5).
10. **Customer remediation (legal side).**
    - LC confirms the wording for unauthorised-transaction and scam cases (PH01 s.13.3–13.4).
    - The Board decides a revised total if the incident total goes above HKD 5 million (s.13.7).
11. **Forensic firm.** Return or destruction of the masked extract, as set out in Q23b.
12. **Insurer.** CFO to obtain the acknowledgement and the insurer's position.

**Internal bank procedure (PH01 v1.0)**
- s.18.1: handover only when "each open item has a named receiving owner who has signed acceptance of a specific list."
- s.18.2: "Items without evidence transfer as open, not done."
- s.18.4: "At handover LC takes over the register of external deadlines and commitments item by item ... Each change deployed to a critical computer system during the incident is entered as a separate item ... applying Cap. 653 section 22 and the HKMA Code of Practice for Designated AIs section 6.1."
- No conflict with external requirements.

---

## Q23b – Records under preservation, and conditions for review and disposal

**Decision**
- The legal hold issued at declaration stays in force for every system and custodian in scope (PH01 s.17.1). That includes the forensic firm and the vendor.
- Log rotation and backup recycling stay stopped on in-scope systems (the Q01b change) until LC lifts the hold in writing.
- No disposal of any kind until the release conditions below are met. Release needs LC's written confirmation plus the record owner's approval, and destruction must be secure and certified (PH01 s.17.3).

**Preserved records and their conditions**

| Record | Review | Disposal / release condition |
|---|---|---|
| Original forensic images, gateway / identity-provider / vendor-access logs, and attacker material (demands, screenshot, mirror and fake-page captures) with the evidence register and custody records (owner: SEC custodian) | One month after declaration (16 Dec 2026), then quarterly | Only when LC confirms no investigation, proceeding or inquiry needs them: the Police case is closed, the Commissioner raises no further requirement after Annex F, the HKMA and PCPD have closed their follow-up, and no civil claim is pending. The legal hold must be lifted. CCS logs are never released before at least 6 months (R03 s.6.2.23(c)). Where analysis continues, masked extracts replace the originals. |
| Decision log, CMT and Board papers (owner: CMT secretary) | Three months after closure, then yearly | Seven years after closure, if nothing is pending and LC approves |
| Notification evidence: filings, receipts, call logs, deadline tracker, Regulator Contact Register entries (owner: LC) | Three months after closure, then yearly | Seven years after closure, on the same conditions. This includes the evidence for item 1 of Q23a. |
| Supplier-produced records (owner: vendor relationship owner and SEC) | Under the legal hold | Same release condition as the originals |
| Third-party copies: the forensic firm's masked extract, any vendor copies, insurer copies | At the end of each engagement and whenever LC asks | Returned or destroyed within 30 days of the engagement ending or LC's request, with a certificate. LC directs the forensic firm to keep its copy while the Police case and the Annex F follow-up are open. |
| Working copies of customer data: notification lists, the corrected file for 12 contacts, case lists for the 31 scam reports and remediation (owners: COM, DPO, Head of Fraud) | Monthly | Keep in minimised form only while the cases, the 12-month identity monitoring and complaints need them. Erase when each task ends, unless LC directs preservation. |

**External basis**
- **Statute, PDPO (R10), Schedule 1 DPP 2(2), PDF p.167:** "personal data is not kept longer than is necessary for the fulfillment of the purpose". This limits retention of customer data to legal and investigative need.
- **Statute, PDPO, DPP 2(3):** "contractual or other means to prevent any personal data transferred to the data processor from being kept longer than is necessary". This applies to the forensic firm and vendor copies.
- **Statutory sector code under Cap. 653 s.8 (R03, HKMA Sectoral Code), s.6.2.23(c), PDF p.18:** "The logs should be retained for a minimum period of 6 months. Such logs should be secured so that they cannot be deleted or altered".
- **Privacy guidance (R11, PCPD), Step 5, PDF p.6:** "A comprehensive record of the incident is therefore required".
- **Non-statutory guideline (R12, SPM SA-2), s.2.5.4:** customer data must be "either retrieved from the service provider or destroyed".
- **Statute, Cap. 653 (R01), s.28(4):** reports still owed and possible supplementary material. This supports preserving the evidence until the Commissioner's process ends.
- **No direct rule located** in the assigned sources for an incident-record retention period such as seven years. Searched all manifest files with the regex "(retain|preserve|keep).{0,40}(record|document|log)". The seven-year period is internal (PH01 s.17.2) and is professional judgment.

**Internal bank procedure (PH01 v1.0)**
- s.17.1: the legal hold "overrides routine deletion, log rotation and backup recycling for systems in scope."
- s.17.2: the table, including "not before any minimum retention an applicable external document sets for that record".
- s.17.3: "Records are released for disposal only on LC's written confirmation and the record owner's approval, and are destroyed securely with a certificate."
- s.18.3: restrictions stay "until their release condition is met and the decision-maker in section 3 has logged the release."
- No conflict with external requirements. PH01 s.17.2 itself defers to the external 6-month minimum and to the PDPO.

---

## Simulated actions for the facilitator to log (HKT, 19 Nov)

| Time | Action |
|---|---|
| 08:15 | HKMA update |
| 10:00 | Commissioner confirmation; conditional Annex E re-filing and missed-deadline disclosure |
| 12:00 | s.22 change list entered in the register, with SEC's risk assessment due 30 Nov |
| 15:00 | Legal hold reconfirmed in writing to custodians, vendor and forensic firm |
| 17:00 | Register handed over with signed acceptance and the "not evidenced" page |

Upcoming dates: weekly review 26 Nov; Annex F filing 27 Nov (statutory latest 30 Nov); s.22 notifications by 16 and 18 Dec 2026; first review of the originals 16 Dec 2026.