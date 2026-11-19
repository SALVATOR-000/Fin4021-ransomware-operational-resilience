LC SUBMISSION – C06 (Tue 17 Nov 2026, 20:00 HKT, H+36) – Units Q17a and Q17b
Locked before I see colleagues' answers. All actions are simulated, for the facilitator to log. There was no facilitator handoff to LC for this card.

C06 facts:
- An offline lab test of a recovery image reconciled 118 of 120 instructions. The 2 mismatches are unexplained.
- No recurring encryption activity was seen during the test window.
- Some SMEs report missed payroll cut-offs.
- The retained Hong Kong forensic firm asks for a copy of a diagnostic image that contains customer data.
- Two counterparties are asking about unsettled instructions.

Missing facts:
- What exactly the firm needs the image for.
- What customer data the image holds: retail, SME, how many records.
- Whether a Board or Risk Committee meeting has already been held. No card or handoff records one.
- The CFO's running remediation total.

==================================================
UNIT Q17a – Forensic firm request for the diagnostic image
==================================================
Decision
- No copy of the full image leaves the bank now.
- The firm receives a narrower data set: the system artefacts it needs, with all customer personal data masked. This is the default under PH01 16.2.
- If the firm shows that its work needs the unmasked image, it examines it inside the bank's laboratory only.
- LC and SEC give no written approval for a full copy to leave the bank at this point. We would consider one only if all three are shown:
  - (i) the work cannot be done in the lab;
  - (ii) the data has been minimised as far as possible;
  - (iii) every condition below is met.

Conditions for transfer and use
1. Need statement. By 21:00 HKT the firm states in writing:
   - the analysis it needs;
   - why masked data or in-lab work would not do;
   - the named analysts.
2. Contract check. By 21:00 LC checks the master services agreement itself. Under PH01 6.5 it already contains the section 16 terms, but LC confirms rather than assumes. The terms required:
   - use only for this incident and on the bank's instructions;
   - confidentiality;
   - processing in Hong Kong;
   - no sub-contracting or onward disclosure without consent;
   - immediate reporting of any loss;
   - bank audit rights;
   - return or destruction with a certificate.
   If any term is missing, nothing is transferred until LC has a signed addendum.
3. Minimisation.
   - SEC's forensic lead prepares the extract (logs, binaries, configuration, metadata).
   - Customer identifiers (names, HKID numbers, phone numbers, account data) are masked or tokenised.
   - The DPO checks the masking before release.
   - A SHA-256 manifest goes with it.
   - Target: ready by 00:30 HKT 18 Nov, subject to SEC capacity. In-lab access can start at once.
4. Transfer.
   - Only by a bank-hosted encrypted transfer, or on bank-issued encrypted media collected by the evidence custodian.
   - Never by email, the firm's own file-sharing, or any internet storage.
   - Transfer record: from, to, time, purpose, signatures (PH01 6.3).
   - Original evidence stays with the custodian; the firm works on verified copies.
5. Use and access.
   - Named analysts only, on a need-to-know basis.
   - Kept separate from the firm's other clients' data.
   - Attacker material is not uploaded to any outside service (PH01 6.6).
   - Any request to the firm from a third party or authority goes to LC.
6. Retention.
   - The firm's copies are under LC's legal hold (PH01 17.1).
   - When the engagement ends, or at LC's request, they are returned or destroyed within 30 days with a certificate, unless LC directs preservation (PH01 17.2).
7. Records: evidence register, data release record, and decision log.

Owners and timing
- Decision: LC and SEC jointly (PH01 s.3), with the DPO and the forensic lead consulted.
- Decision logged by 20:15 HKT.
- Reply to the firm by 20:45, by call-back to a number on file, then in writing by a route that does not depend on corporate email unless SEC has logged email as safe.

Recipient and channel
- The retained Hong Kong forensic firm's engagement lead.
- Data only by the transfer methods in condition 4.

Basis: external
- R10, Cap. 486 Personal Data (Privacy) Ordinance. Status: statute.
  - DPP4(2), PDF p.169: a data user engaging a data processor "must adopt contractual or other means to prevent unauthorized or accidental access, processing, erasure, loss or use of the data transferred".
  - DPP2(3), PDF p.167: contractual or other means to prevent transferred data "from being kept longer than is necessary".
  - DPP2(4), PDF p.168: a data processor is a person who "processes personal data on behalf of another person".
  - DPP3, PDF p.168: personal data "shall not, without the prescribed consent of the data subject, be used for a new purpose".
  - Professional judgment: investigating a breach of the same data is arguably a directly related purpose. Masking removes most of the question.
- R12, SPM SA-2 Outsourcing. Status: non-statutory guideline; applied by analogy to a service engagement.
  - 2.5.2, PDF p.6: safeguards include confidentiality undertakings, "segregation or compartmentalisation" of data, and access "on a need basis".
  - Footnote 1: the common-law duty of confidentiality covers corporate customers too, so SME data in the image is also protected.
- R16b, HKMA circular "Customer Data Protection". Status: supervisory circular.
  - Annex D, PDF p.5: controls against transmission of customer data through internet storage services.
  - Annex E, PDF p.6: "strong data encryption" on portable media, and records of their use.
- R08, SPM TM-G-1. Status: non-statutory guideline. 4.2.4, PDF p.18: production data should be "de-sensitised (i.e. not disclosing personal or sensitive information)". This is about testing, so I use it only as a general principle.

Internal bank procedure (PH01 v1.0)
- 16.2: "By default the firm receives a minimised data set with customer personal data masked. Full images are examined only inside the bank's laboratory. A full copy leaves the bank only with LC's and SEC's written approval."
- Also relied on: 16.1 contract terms, 6.5 the master services agreement, 6.3 custody, 17.1 and 17.2 legal hold and retention, and s.3.
- Conflict check: none. PH01 is stricter than the external sources and consistent with them.

==================================================
UNIT Q17b – Escalation to the Board
==================================================
Decision: escalate to the Board now.
- The 24-hour tolerance for outbound domestic transfers and SME payroll was reached at about 08:00 HKT 17 Nov. It is now about 150%.
- PH01 15.2 requires the Board or its Risk Committee to meet within 12 hours of reaching 100%. That window closes now, at 20:00 HKT.
- No card or handoff records a meeting. LC therefore advises the CEO (CMT chair) to convene the Board or Risk Committee at once, by telephone or video, targeting 21:30 HKT tonight.
- If a meeting was already held, this becomes an urgent update meeting with the decisions below. If none was held, the decision log records that the 12-hour limit was missed.

Board paper: LC drafts the legal and authorities sections by 21:00. Legal advice goes in a separate privileged section (PH01 15.3).

Items for the Board
For the Board to note:
1. Disruption against tolerance.
   - Outbound transfers and SME payroll have been down for 36 hours or more against a 24-hour tolerance.
   - Mobile transfer submission is still interrupted.
   - SMEs report missed payroll cut-offs. Call volumes are high and some customers cannot reach the bank.
   - Under OR-2 the Board "bears ultimate responsibility for ensuring that an AI remains operationally resilient".
2. Recovery position.
   - The candidate failed offline testing: under PH01 9.2, "One unexplained difference is a fail", and there are two.
   - It cannot go to production until the mismatches are explained and it passes again. SEC's Q16 recommendation is attached.
   - The status of the alternate payment process is the CEO's decision on SEC's clearance (PH01 8.2), reported to the Board for information.

Decisions for the Board:
3. Scope of recovery. The Board may narrow the scope, for example to payroll only (PH01 9.3), and must minute any change.
   - LC's legal advice: the Board cannot waive any gate.
   - A narrower scope must pass every check in 9.3 that applies to it.
   - The failed candidate cannot be used for any scope until its own pass is achieved.
4. Customer remediation.
   - Under PH01 13.2, SME late-payment charges and other documented direct losses are reimbursed on claim.
   - The CFO reports the running total.
   - If the projection is likely to exceed the HKD 5 million incident total, LC recommends the Board approve a revised total in advance, so SME claims are not stalled. Only the Board or Risk Committee can do this (PH01 13.7).
   - While a revised total is awaited, claims continue to be registered and acknowledged.
5. Payment posture. The Board is asked to reaffirm the no-payment policy.
   - No payment has been made and no departure is proposed.
   - Gates (a)–(g) remain unconfirmed.

For the Board to note:
6. Data and authorities.
   - 320 records confirmed and published; 18,000 unverified.
   - A fake verification page is active and has been referred to the Police.
   - Customer notification status.
   - Deadlines: Cap. 653 Annex F, statutory 30 Nov (internal target 27 Nov); HKMA updates at 08:00 and 18:00 daily; PCPD updates; Police referral.
   - The insurer's position.
7. Third parties.
   - The vendor credential compromise: reinstatement only on the PH01 7.5 gates; contract position.
   - The forensic firm decision under Q17a.
8. Privileged section (legal exposure):
   - Cap. 653 s.28 compliance and the evidence gaps closed at C04;
   - possible regulatory directions;
   - PDPO DPP4 exposure and any PCPD investigation;
   - customer and counterparty claims;
   - the HKMA supervisory response.

Owners and channels
- CEO: convenes the meeting and decides any escalation (PH01 s.3), with LC consulted.
- LC: drafts the legal and authorities sections and the privileged advice.
- CFO: remediation total and insurer.
- SEC and Payments Operations: recovery facts.
- Board paper by hand, or by an encrypted Board route if SEC has logged it safe.
- Meeting by telephone or video, with a Board minute.
- Professional judgment: tell the HKMA in its next update that the tolerance has been exceeded and the Board is engaged.

Basis: external
- R06, SPM OR-2. Status: non-statutory guideline.
  - 3.2, PDF pp.5–6: senior management should provide "regular and timely reports to the Board ... particularly when significant deficiencies could affect the delivery of the AI's critical operations".
  - 3.4, PDF p.6: "The Board bears ultimate responsibility for ensuring that an AI remains operationally resilient".
  - PDF p.3: disruptions "must not exceed" the tolerance for disruption.
- R07, SPM TM-G-2. Status: non-statutory guideline. 2.1.1, PDF p.5: the Board and senior management "have the ultimate responsibility for business continuity planning and the effectiveness of their BCP".
- No direct rule located that sets a timeframe for Board escalation in the external sources. Searched "Board" and "tolerance" in R06, R07, R13 and R14b. The timing comes from PH01.

Internal bank procedure (PH01 v1.0)
- 4.3: "When it reaches 100%, the CMT chair convenes the Board or its Risk Committee".
- 15.2: meets "within 12 hours of: 100% of a tolerance reached; any decision reserved to the Board; a request from a regulator".
- 15.3: Board paper contents; "Legal advice is in a separate privileged section."
- Also relied on: 9.2, 9.3, 13.7 and 12.1.
- Conflict check: none.

No files were created.