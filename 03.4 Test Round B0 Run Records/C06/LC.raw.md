LC answer for C06 (Tuesday 17 Nov 2026, 20:00 HKT, H+36). This covers Q17a and Q17b only and was locked before I saw colleagues' answers. The facilitator gave LC no handoff for this card.

Facts I am relying on:
- The recovery image passed 118 of 120 instructions in the laboratory test. The 2 mismatches are unexplained.
- The lab saw no encryption activity during its test window.
- Some SMEs have missed payroll cut-offs.
- The forensic firm has asked for a copy of a diagnostic image that contains customer data.
- Two counterparties have asked for a status update.

Unknown at this card, because no handoff records it:
- whether the secondary process was activated at C04;
- whether the Board or its Risk Committee has met;
- the running remediation total.

---

## Q17a – Forensic firm request for the diagnostic image

**Decision: no full copy leaves the bank now.** I am offering a narrower route instead and holding the full copy.

1. **Default, approved now.** The firm gets a minimised extract, prepared by SEC from a verified copy, with customer personal data masked or tokenised. The extract contains:
   - system and process artefacts, malware and IOC material, logs and timelines;
   - file and record metadata;
   - hashes of data files, with no content.
   If the firm needs the full image, it examines it only inside the bank's laboratory. Bank staff supervise, sessions are logged, and nothing is exported.
2. **Full copy outside the bank: HOLD.** It is allowed only if all of the following are met:
   - (i) The firm states in writing the specific analysis that cannot be done on masked data or in the bank's lab.
   - (ii) LC and SEC both approve in writing, and the DPO is consulted.
   - (iii) LC confirms that the MSA's data terms meet every PH01 s.16.1 item. The card does not show I have checked this, so LC re-checks it against the signed MSA by 22:00. The items are: use limited to the incident and the bank's instructions; confidentiality; processing in Hong Kong; no sub-contracting or onward disclosure without consent; immediate reporting of any loss; bank audit rights; return or destruction with a certificate.
   - (iv) The copy is encrypted, carried on bank-issued media collected and delivered by the evidence custodian, and the transfer is logged on the custody record (PH01 s.6.3, Annex B).
   - (v) The copy is returned or destroyed within 30 days of the end of the engagement or of LC's request, with a destruction certificate, unless LC directs preservation under the legal hold (PH01 s.17.2).
   - **Condition record.** Verifier: LC with SEC. Latest time: 22:00 HKT on 17 Nov for item (iii); on receipt of the firm's request for (i). Default if not verified: hold the full copy and continue with the masked extract and in-lab access. This is not a "go ahead" default, because data and security conditions stay in force (PH01 s.2.3).
3. The original image stays under the legal hold. The firm is reminded in writing that the legal hold covers its copies (PH01 s.17.1).

**Owners.** LC and SEC decide jointly; the DPO is consulted (PH01 s.3, "Share incident data with a forensic firm or other third party"). SEC prepares the extract. The evidence custodian handles the transfer. The vendor or forensic relationship owner sends the written terms.

**Timing.** The masked extract is ready by 23:00 HKT on 17 Nov, or at the time SEC sets after verifying the extract. Full-copy decision is held as set out above.

**Recipient and channel.** The retained Hong Kong forensic firm's engagement lead. Data goes on encrypted media or by bank-hosted encrypted transfer, never by ordinary email (PH01 s.6.7(b) applied by analogy). A data release record and custody log are kept.

**Basis.**
- **R10, Cap. 486 PDPO (statute).**
  - Schedule 1, DPP 4(1), PDF p.169: data must be protected "against unauthorized or accidental access, processing, erasure, loss or use having particular regard to— (a) the kind of data and the harm that could result". The image holds HKID-level data, and 320 customers' records are already public, so the harm from a second exposure is high.
  - DPP 4(2), PDF pp.169-170: "if a data user engages a data processor ... the data user must adopt contractual or other means to prevent unauthorized or accidental access, processing, erasure, loss or use of the data transferred to the data processor".
  - DPP 2(3), PDF p.167: the data user "must adopt contractual or other means to prevent any personal data transferred to the data processor from being kept longer than is necessary".
  - Application: the firm processes on the bank's behalf, so it is a data processor. The MSA terms are the "contractual means". Minimising and masking reduce the DPP 4(1) risk.
- **R12, HKMA SPM SA-2 Outsourcing V.1 (non-statutory guideline; cover: "A non-statutory guideline issued by the MA as a guidance note"), s.2.5.2, PDF p.6.** Safeguards include "undertakings by the service provider that the company and its staff will abide by confidentiality rules" and "access rights to AIs' data delegated to authorized employees of the service provider on a need basis". Footnote 1 notes the common-law duty that AIs should "not divulge such information to any person without the customer's consent". In my professional judgment, that duty is met by a need-based, masked disclosure to the bank's own agent under contract.
- **R16b, HKMA circular Customer Data Protection (14 Oct 2014), PDF p.4, Annex B:** policies "including those to be followed by the relevant service providers, should also be in line with PDPO".
- **Left to judgment:** what counts as "necessary" analysis, and how far masking can go before the forensic value is lost. SEC and the firm decide this case by case, and LC records the reasons.

**Internal bank procedure (PH01 v1.0).**
- s.16.1: "Data goes to a forensic firm or other third party only under a signed agreement that limits use to the incident ... keeps processing in Hong Kong, forbids sub-contracting ... requires return or destruction with a certificate."
- s.16.2: "By default the firm receives a minimised data set with customer personal data masked. Full images are examined only inside the bank's laboratory. A full copy leaves the bank only with LC's and SEC's written approval."
- s.6.5: the MSA "already contains the data terms in section 16". LC still re-checks the signed text before any full copy, because this is a verification step, not a conflict.
- No conflict with the external sources.

---

## Q17b – Escalation to the Board

**Decision: escalate now.** The Board or its Risk Committee meeting is overdue or due now, and the CMT chair convenes it at once.
- **Trigger.** The Board-approved tolerance for "Outbound domestic transfers and SME payroll submission" is 24 hours (PH01 s.4.2). Measured from the 08:00 HKT awareness on 16 Nov, that was 100% at 08:00 HKT on 17 Nov. The disruption is now about 36 hours, or about 150%.
- **Deadline.** PH01 s.15.2 requires a meeting "within 12 hours of: 100% of a tolerance reached". The latest time is **20:00 HKT on 17 Nov, which is now**.
- **Missing fact.** I cannot confirm whether the Board was convened. If no meeting is recorded, LC logs the internal deadline as missed and the CMT reconvenes at once (PH01 s.18.5). The meeting is held tonight by call, target **21:30 HKT**.
- If disruption began before 08:00, the tolerance was reached earlier. SEC confirms the start time.

**Owners.** The CMT chair (Chief Executive) convenes and presents. LC writes the legal and regulatory section of the paper and the separate privileged legal advice section. The CFO provides the remediation total. SEC and the Head of Payments Operations provide the recovery and queue facts.

**Channel.** Board or Risk Committee meeting by secure call, with the Board paper set out under PH01 s.15.3, and a Board minute.

**Contents of the Board paper** (PH01 s.15.3):
1. **Disruption against tolerance.**
   - Transfers and payroll are about 36 hours into a 24-hour tolerance, so the tolerance is breached.
   - Queue status and payroll cut-offs missed.
   - Throughput of the alternate process, if it was activated. Its status is unknown at this card and must be confirmed.
   - Balances view is within its 8-hour tolerance, since balances remain viewable.
2. **Recovery position: for information and possible decision.**
   - The candidate failed the offline pass mark (118/120, with 2 unexplained differences). Production use is held unless SEC finds otherwise (Q16).
   - The Board may narrow the recovery scope, for example to payroll only, but cannot waive any gate item. A narrower scope must still pass every applicable check in PH01 s.9.3.
   - **Decision sought:** whether to ask management to pursue a narrower payroll-first scope, subject to the full gate.
3. **Customer remediation.**
   - SME missed-payroll charges are reimbursable under PH01 s.13.2.
   - Identity monitoring for the 320 confirmed customers under s.13.5.
   - **Decision sought:** if the CFO projects the incident total will exceed HKD 5 million (s.13.7), approve a revised total so that payments are not delayed. Claims continue to be registered in the meantime.
4. **Data position.**
   - 320 records confirmed exposed and publicly mirrored.
   - The 18,000-record claim is unverified.
   - A fake verification page is active.
   - Notification status of each customer group.
   - The forensic firm's data request and the Q17a decision. This is for information only; the decision belongs to LC and SEC, not the Board.
5. **Payment posture.** Unchanged: no payment, no preparatory steps, no attacker contact, and no commitment recorded. No Board decision is sought or recommended.
6. **Authorities engaged and deadlines.**
   - Commissioner: s.28 notification. The specified-form filing was decided at C04; LC confirms its receipt. Written report by **30 Nov 2026** (R01 Sch.6 item 3).
   - HKMA: ongoing updates. Tolerance breach, recovery hold and Board meeting reported in the next update.
   - PCPD: voluntary notification and update to 320.
   - Police: CSTCB case, s.25A disclosure, and referral of the mirror and fake page.
   - Insurer: notified by the CFO.
   - Any regulator request received is itself a Board trigger (PH01 s.15.2).
7. **Privileged section.** Legal exposure on the missed payroll and the tolerance breach; regulatory risk; Cap. 653 compliance evidence.

**Basis.**
- **R06, HKMA SPM OR-2 Operational Resilience V.1** (cover: "A non-statutory guideline issued by the MA as a guidance note").
  - s.3.4, PDF p.6: "The Board bears ultimate responsibility for ensuring that an AI remains operationally resilient. This would require the Board to ensure appropriate action is taken by senior management to address any deficiencies identified in an AI's ability to remain within its tolerance for disruption."
  - s.3.3: the Board "is responsible for approving the tolerance for disruption".
  - Application: a breach of a Board-approved tolerance is exactly the deficiency the Board must oversee.
- **R07, HKMA SPM TM-G-2 V.2 (non-statutory guideline), s.2.1.1, PDF p.5:** "The Board of Directors and senior management of AIs have the ultimate responsibility for business continuity planning and the effectiveness of their BCP."
- **No direct external rule located** for a specific board-meeting deadline. I searched R06 for "tolerance for disruption" and read p.6. The 12-hour timing comes from PH01 only.

**Internal bank procedure (PH01 v1.0).**
- s.4.3: "When it reaches 100%, the CMT chair convenes the Board or its Risk Committee (section 15)."
- s.15.2: "The Board or its Risk Committee meets within 12 hours of: 100% of a tolerance reached; any decision reserved to the Board".
- s.15.3: "The Board paper states: the disruption against tolerance; data position; payment posture; authorities engaged and deadlines; decisions required. Legal advice is in a separate privileged section."
- s.9.3: "No gate condition may be waived" (s.3); "The Board may narrow the scope of recovery".
- s.13.7: the Board approves any incident total above HKD 5 million.
- No conflict with the external sources.

**Related external update (for coordination, not assigned).** LC tells the HKMA by phone at the 20:00 or 24:00 scheduled update about the tolerance breach, the recovery hold and the Board meeting (PH01 s.5.8, "a change in service status"). This sits within R05's "kept informed" expectation (PDF p.3).

---

**Simulated actions to log (HKT, 17 Nov):**
- 20:05: decision log entry for the forensic data decision (masked extract approved, full copy held) and for the Board escalation.
- 20:10: CMT chair convenes the Board or Risk Committee for 21:30.
- 21:00: Board paper issued.
- 22:00: LC check of MSA terms against s.16.1.
- 23:00: masked extract transferred by the custodian, with custody and data-release records.
- Next scheduled HKMA update includes the tolerance breach.