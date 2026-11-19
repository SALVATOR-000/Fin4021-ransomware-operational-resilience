CEO FINAL DECISION RECORD: C08, Thursday 19 November 2026, 08:00 HKT (H+72). Lan Tidal Bank, CMT chair.

All actions are simulated, for the facilitator to log.

Inputs for this card:
- **Sealed answers:** SEC (Q22a, Q22b), LC (Q23a, Q23b) and COM (Q24a, Q24b). None is missing.
- **Handoffs:** SEC received Q16a, Q16b and Q19b. LC received Q11b, Q08a/b, Q14b, Q20a/b, the production-change list and the notification record. COM received Q03b/Q12a/Q18a, Q21a and Q21b.

Sources I re-checked myself for this card:
- R01 s.22(1)–(3), pp.33–34, and s.27(4), p.43.
- R10 DPP2(2), p.167 ("not kept longer than is necessary"), and s.26, p.58.
- R06 8.3, p.13 ("Root cause analysis of incidents").
- R02 Annex F, pp.43–46, and 7.3.7(a), p.37.
- PH01 v1.0, sections 9.2, 11.5 and 18.

**CEO RECORD ENTRIES, 08:00**
1. **The CMT does not stand down.** The exercise window is closing, but the incident is not:
   - Outbound transfers and payroll are still disrupted, well past the 24-hour tolerance.
   - Containment is not confirmed: the indicator classification and closure-test results are not recorded.
   - PH01 s.11.5 closing conditions are unmet.

   Decision: execution of the listed items passes to signed receiving owners at 12:00 (PH01 s.18.1). The CMT stays convened, sitting at 08:00 and 18:00 daily. It reconvenes at once on any PH01 s.18.5 trigger. Full stand-down needs all of the following to be logged:
   - production restored through the s.9.3 gate;
   - SEC confirms containment;
   - every item has a signed owner.
2. **The 240/240 test is recorded as a sample, not a pass (PH01 s.9.2).** I authorise no production stage.
3. **Board.** I give the Board a written status by 18:00 today. It covers tolerance, the recovery hold, data, authorities and open liabilities. The Board meeting called for 21:30 on 17 Nov has no record, so its status goes on the "not evidenced" page. LC supplies the privileged section (PH01 s.15.3).

==================================================================
**UNIT C08-Q22a: restrictions to keep or release, and handover to standing operations**

**Original answer reference:** sealed SEC answer for C08, "UNIT Q22a". This covers the decision, restrictions 1–9, the handover list and the "not evidenced" page.

**Decision:** CONFIRM.

**Reason**
- No restriction is released. None of their release conditions is recorded as met, and PH01 s.18.3 keeps every restriction in force until the s.3 decision-maker logs its release.
- 240/240 is correctly treated as a sample (PH01 s.9.2), so the first gate item is unmet. External support: R08 4.2.4, p.18, "only properly tested and approved systems are promoted".
- The only step forward is a full-set offline rerun, with no live interface, behind its preconditions:
  - the first failure explained;
  - the data preconditions logged;
  - the candidate (1) build confirmed.
- The alternate process is treated as not cleared, because no PH01 s.8.2 clearance is recorded. This is consistent with my C06 order.
- Each restriction carries its release condition and decision-maker.
- The handover names an owner by role for each item and keeps decision rights with SEC.
- The "not evidenced" page lists every unrecorded result from C01 to C08, so those items transfer as open (PH01 s.18.2).

**Final action and condition**
- As written.
- The alternate-process state record from the Head of Payments Ops is due 10:00. It also feeds COM's 13:00 update (Q24a W2) and LC's HKMA correction (Q23a B3).

**Accountable owner**
- SEC is accountable and keeps all PH01 s.3 decision rights.
- Receiving owners, by role:
  - security operations manager;
  - Head of IT Ops;
  - identity engineering lead;
  - evidence custodian;
  - Head of Payments Ops;
  - forensic engagement owner;
  - vendor relationship owner with the CRO and LC;
  - DPO with LC.

**HKT time, deadline or trigger**

| Time | Item |
|---|---|
| 08:00 | All restrictions retained |
| 10:00 | Alternate-process state record due |
| 12:00 | Closure test and N2–N5 results due (overdue); signed acceptances due |
| Status reports | Hourly until containment is confirmed (PH01 s.2.5) |
| Full-set rerun | Only after the root cause is documented |

**Recipient and channel**
- The handover pack with signed acceptances.
- The decision log, evidence register and instruction register.
- The CMT room or phone bridge.

**Final external basis**
- SEC Q22a "BASIS: EXTERNAL" items 1–5 are adopted:
  - R08 4.2.4, p.18 (verified);
  - R03 6.2.26(a)–(b), p.19;
  - R06 8.3–8.4, p.13;
  - R02 7.2.3(c), p.33;
  - R07 4.3.2, p.11.
- SEC's search record for "handover" is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.18.1–18.3, s.18.5, s.9.2, s.2.5 and s.3. No conflict.

**Dispatch instruction**
- EXECUTE NOW: retain all restrictions.
- SCHEDULE: the 10:00 record; the 12:00 results and acceptances.
- HOLD:
  - every release;
  - production;
  - reopening of mobile submission;
  - vendor reinstatement;
  - any reduction in monitoring.
- The full-set rerun is held until its preconditions are logged.

==================================================================
**UNIT C08-Q22b: root-cause remediation and closure evidence for the vendor credential**

**Original answer reference:** sealed SEC answer for C08, "UNIT Q22b". This covers RC-A to RC-I, the due dates and V1–V9.

**Decision:** OVERRIDE. This is a narrow change to one due date.

**Reason**
- **Kept as written:**
  - Remediation items RC-A to RC-I, each with an owner, an independent check, a risk-register entry and an s.22 log.
  - The closure evidence V1–V9, including:
    - a reconciled inventory;
    - a closure test passed on every path (PH01 s.7.4);
    - 72 hours with no use;
    - a clean persistence sweep;
    - rotated secrets;
    - the cause established;
    - the supplier evidence chain under s.6.7;
    - independent review before SEC signs.
  - Closure is kept separate from reinstatement under PH01 s.7.5.
- **The conflict being fixed:**
  - SEC's due date for the technical root-cause draft to LC is 25 Nov.
  - The Annex F schedule confirmed at C07 (Q20b) needs SEC's section drafts (B1–B8, including B4 "Root Cause Analysis Summary") by 18:00 on 20 Nov and consolidated v1 on 23 Nov. Sign-offs are on 25 Nov, submission is by 27 Nov, and the statutory limit is 30 Nov (R01 Sch.6 item 3).
  - A root-cause draft arriving on sign-off day leaves no time for review.
  - R02 Annex F, p.43, requires all fields "as far as practicable based on the information available". R02 7.3.7(a), p.37, allows later facts "as supplementary material". So the draft should come earlier, and anything found later is supplemented.
- Changing a due date changes execution, so this is an OVERRIDE.

**Final action and condition**
- RC-A to RC-I and V1–V9 as written.
- Revised due dates:
  - SEC delivers the Annex F B1–B8 and D drafts by 18:00 on 20 Nov, with unverified items marked.
  - The technical root-cause draft goes to LC by 12:00 on 23 Nov, ready for v1.
  - V7 (cause established, vendor-dependent) stays at 25 Nov. Any later finding goes to the Commissioner as supplementary material.
- No item closes because its date has passed (PH01 s.2.3).

**Accountable owner**
- SEC: closure sign-off and remediation oversight.
- Item owners as listed: Head of IT Ops, identity engineering lead, security operations manager, data owner with the DPO, the recovery lead with the Head of Payments Ops, and the vendor relationship owner with the CRO and LC.
- The CEO decides any reinstatement.

**HKT time, deadline or trigger**

| Date / time | Item |
|---|---|
| 12:00 today | V3 (closure test); the 72-hour V4 window then runs |
| 18:00, 20 Nov | V1, V2, V5, V6, and the Annex F B and D drafts |
| 12:00, 23 Nov | Root-cause draft |
| 25 Nov | V7, V8 |
| 26 Nov | Remediation plan |
| After V9 | Closure decision |
| 16 Dec | Post-incident review |

**Recipient and channel:** LC (Annex F), the risk register, the evidence register, the change records (s.22 log) and the decision log.

**Final external basis**
- SEC Q22b "BASIS: EXTERNAL" items 1–8 are adopted:
  - R06 8.3, p.13 (verified: "Root cause analysis of incidents to help with the prevention or minimisation of recurrence");
  - R02 7.2.3(i), p.33;
  - R02 Annex F, pp.43–44;
  - R03 6.2.13(b), p.14;
  - R16b Annex C(vii);
  - R01 Sch.3 Pt 1 item 3(h);
  - R10 DPP4(1)(d) and DPP4(2);
  - R01 s.22 and s.27(4).
- New basis for the timing change:
  - R02 Annex F, p.43 (verified): "All fields should be completed as far as practicable based on the information available".
  - R02 7.3.7(a), p.37 (verified): additional information goes "as supplementary material".

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.7.2, s.7.4, s.7.5, s.6.7(d), s.3 (reinstatement row), s.18.4 and s.2.3. No conflict.

**Dispatch instruction**
- SCHEDULE: as listed above.
- HOLD: vendor reinstatement until the PH01 s.7.5 conditions are met and I decide.
- Dependency: Annex F v1 depends on the 20 Nov drafts and the 23 Nov root-cause draft.

==================================================================
**UNIT C08-Q23a: compliance actions open after handover, and who receives the register**

**Original answer reference:** sealed LC answer for C08, "UNIT Q23a", items A1–G2.

**Decision:** OVERRIDE. One item is added to the register.

**Reason**
- **Kept as written:**
  - LC takes the register item by item (PH01 s.18.4).
  - A designated officer keeps it, and a second officer checks the dates.
  - Every item needs a signed owner (s.18.1).
  - Every unrecorded receipt, reference and "cannot be verified" item goes on page 1 as open (s.18.2).
- **The open items are complete except for one gap:**
  - A: Commissioner items — Annex F due 30 Nov; proof of receipt; the workspace's CCS status; indicator classification.
  - A5: s.22 material-change notices go to the MA, not the Commissioner. This is verified at R01 s.22(1), p.33: "the regulating authority that regulates the operator ... within 1 month after the date on which the event occurs". The 16 Nov batch is due 16 Dec, with an internal target of 9 Dec.
  - B: HKMA. This includes the overdue 08:00 update by 08:30 and the record correction on the alternate process.
  - C: PCPD, including the misdirection assessment.
  - D: Police and Cap. 455.
  - E–G: customers, third parties and governance.
- **The gap:**
  - SEC flagged it to LC (Q22b, basis item 8). It is not in LC's register.
  - R01 s.27(4), p.43 (verified): "If there is any revision to an emergency response plan after it is submitted, the CI operator must submit the revised plan to the Commissioner within 1 month after the date on which the revision is made." Failing to do so is an offence under s.27(7).
  - The post-incident review (16 Dec) is likely to revise PH01. It is unverified whether PH01 is part of the plan submitted under s.27.
  - This is a statutory, conditional commitment, so it belongs on the register. Adding it changes execution, which makes this an OVERRIDE.

**Final action and condition**
- Items A1–G2 exactly as written.
- New item A6, conditional:
  - By 26 Nov, LC confirms in writing whether PH01, or any document revised after the post-incident review, forms part of the emergency response plan submitted under s.27(1).
  - If it does, then:
    - every revision gets an LC register entry with its revision date;
    - the revised plan goes to the Commissioner within 1 month of that date;
    - the revision is endorsed by the Board or senior management before submission (R02 7.2.2, p.32).
  - If it does not, LC logs "not part of the plan" with the reason.
- I direct LC to cover the Board's 21:30 meeting on 17 Nov (no record exists) under G1.

**Accountable owner**
- LC receives and owns the register. A designated LC officer keeps it, and a second LC officer checks it.
- Item owners as listed: SEC, Payments Ops, COM, the DPO, the CFO, and the vendor relationship owner.
- The CEO owns G1.

**HKT time, deadline or trigger**

| Date / time | Item |
|---|---|
| 08:30 today | HKMA update (B1) |
| 10:00 today | SEC confirms the workspace's CCS status (A3) |
| 12:00 today | Commissioner receipt request (A2); handover signed |
| 18:00 today | Misdirection assessment (C2) |
| 20 Nov | Police written referral (D2) |
| 26 Nov | s.22 change list (A5); A6 confirmation |
| 27 Nov (statutory 30 Nov) | Annex F |
| 9 Dec (statutory 16 Dec) | s.22 notices for the 16 Nov batch; the 18 Nov batch by 18 Dec |
| Ongoing | A6 revised plan within 1 month of each revision; weekly review of the whole register |

**Recipient and channel**
- Commissioner: designated secured channel or verified CI telephone route.
- MA/HKMA: telephone, and its confirmed route and specified form.
- PCPD: fax or by hand.
- Police CSTCB.
- The register itself is held in the LC duty pack.

**Final external basis**
- LC Q23a "Basis" is adopted:
  - R01 s.22(1) and (3)(a), pp.33–34 (verified);
  - R01 s.28(4) and Sch.6 item 3;
  - R03 6.1.1 and 6.1.3, p.11;
  - R07 1.3.3, R05, R16b, R11, R16c s.25A and R09 4.3.2, as cited at C02–C07.
- Added for A6:
  - R01 s.27(4), p.43 (verified, quoted above) and s.27(7);
  - R02 7.2.2, p.32 (verified at C01): plan changes "are endorsed by the Board ... or the senior management".

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.18.1, s.18.2, s.18.4, s.18.5, s.5.3 and s.5.8. No conflict.

**Dispatch instruction**
- EXECUTE NOW: B1 and the register takeover.
- SCHEDULE: all other items on their own due dates.
- A6 depends on LC's 26 Nov confirmation and on any revision of PH01.

==================================================================
**UNIT C08-Q23b: records under preservation, review and disposal**

**Original answer reference:** sealed LC answer for C08, "UNIT Q23b".

**Decision:** CONFIRM.

**Reason**
- The legal hold stays and is re-issued at handover to all custodians, the vendor and the forensic firm (PH01 s.17.1).
- Nothing is disposed of.
- Each record class has its own review point and retention period, matching the PH01 s.17.2 table.
- Original logs from critical systems are never destroyed before the 6-month minimum: no earlier than 16 May 2027 (R03 6.2.23(c), p.18, verified at C01).
- Disposal needs all six conditions:
  - no inquiry, proceeding or claim pending or expected;
  - LC lifts the hold in writing;
  - every external minimum has passed;
  - the record owner approves;
  - destruction is certified;
  - third parties certify their own destruction.
- Personal data is minimised at each review, so the 7-year periods stay consistent with DPP2(2), p.167 (verified: "not kept longer than is necessary") and s.26, p.58 (verified: erasure "unless ... prohibited under any law").
- LC correctly flags the one point needing alignment: the fixed 7-year periods against DPP2(2). LC resolves it within PH01.

**Final action and condition:** as written.

**Accountable owner**
- LC: the hold and any release.
- Record owners: approval of disposal.
- Evidence custodian: originals.
- DPO: consulted on personal-data retention.

**HKT time, deadline or trigger**

| Date / time | Item |
|---|---|
| 12:00 today | Hold re-issued |
| 16 Dec 2026, then quarterly | Review of original images and logs |
| 3 months after closure, then yearly | Review of the decision log and notification evidence |
| Not before 16 May 2027 | Earliest destruction of critical-system logs |
| Not before the 7-year point after closure | Earliest destruction of the decision log and notification evidence, subject to conditions (i)–(vi) |

**Recipient and channel:** custodians, the vendor and the forensic firm, by written hold notice through a route that does not depend on corporate email. Record stores: the write-once evidence store and the restricted register store.

**Final external basis:** LC Q23b "Basis: external" is adopted:
- R03 6.2.23(c), p.18; R02 6.2.23(c), p.20;
- R01 s.34–35, p.50;
- R10 DPP2(2)–(3), p.167 (verified), and s.26(1), p.58 (verified);
- R11 pp.3 and 6;
- R12 2.5.4.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.17.1–17.3 and s.18.3. No conflict; the DPP2(2) alignment is handled by minimisation at review.

**Dispatch instruction**
- EXECUTE NOW: re-issue the hold by 12:00.
- SCHEDULE: reviews on the dates above.
- HOLD: all disposal until conditions (i)–(vi) are met.

==================================================================
**UNIT C08-Q24a: closing status update, or continued updates**

**Original answer reference:** sealed COM answer for C08, "Q24 a", Version H3 and conditions W1–W5.

**Decision:** OVERRIDE. The W2 default wording changes.

**Reason**
- **Kept as written:**
  - No closing update. The PH01 s.11.5 conditions are unmet: no production service, queued instructions not settled, no evidence of delivery, regulators not confirmed.
  - A self-contained 09:00 update, then 13:00 and 19:00, then the s.11.2 cadence.
  - An apology if the 18 Nov 13:00 and 19:00 updates are confirmed missing.
  - The 240/240 result described as a test result only (s.9.2).
  - Version P only after a gate pass.
  - The W5 clearance default from my C05 rule.
- **The flaw in W2:**
  - COM's W2 default, used if the alternate-process status is not verified by 08:45, is "Queued payments remain on hold".
  - That status has been unverifiable since C04. SEC's state record is not due until 10:00.
  - If the process has been releasing, the line would be false. Customers told their payments are on hold might pay by other means and create duplicates.
  - PH01 s.11.2 requires each update to say "what is being verified". An unverified status must go there, not be stated as fact.
- Changing a default changes execution, so this is an OVERRIDE.

**Final action and condition**
- Version H3 and W1, W3–W5 as written.
- New W2 default, used if Payments Ops has not verified the status by 08:45: "We are confirming the status of queued payments and will tell you in our 13:00 update. Each payment will be made only once. Please do not resubmit."
- The 13:00 update states the status from the Head of Payments Ops' 10:00 record (Q22a).

**Accountable owner**
- COM drafts and publishes.
- I approve (the COO is alternate after 15 minutes).
- LC clears, with the second LC officer as backup.
- SEC and Operations fact-check.
- The Head of Payments Ops supplies W2.

**HKT time, deadline or trigger**

| Time | Item |
|---|---|
| 08:05 | Channel and archive check |
| 08:30 | Approval |
| 08:45 | Clearance and fact-check |
| 09:00 | W5 default point; publish |
| 13:00, 19:00 | Next updates |
| After that | The s.11.2 cadence, plus at once on any change of service |

A closing update is issued only when every s.11.5 condition is evidenced and I approve it.

**Recipient and channel**
- Public: website status page, press release, text-only official social media, app banner (if SEC has logged it trusted), IVR, branch notices and staff scripts.
- HKMA: copy via COM → LC → HKMA, with a receipt requested.

**Final external basis**
- COM Q24a "Basis: external" is adopted: R09 8.2.2, p.33; R05 p.3 (scan-checked); R07 1.3.3, p.5; R06 8.3, p.13.
- For the W2 change: R09 8.2.2, p.33 (verified at C01), "consistent and up-to-date messages ... on a timely basis". Stating an unverified status as fact would breach this.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.11.5, s.11.2 ("what is confirmed, what is being verified"), s.11.4, s.9.2, s.1.3 and s.5.8. No conflict.

**Dispatch instruction**
- SCHEDULE: publish at 09:00. This depends on W1–W4 at 08:45 and on clearance or the 09:00 default.
- HOLD: the closing update.
- The 13:00 W2 line depends on the 10:00 Payments Ops record.

==================================================================
**UNIT C08-Q24b: hand-off of unresolved customer cases and follow-up messaging**

**Original answer reference:** sealed COM answer for C08, "Q24 b", handover items 1–12 and the standing rules.

**Decision:** CONFIRM.

**Reason**
- Items are handed over one by one under PH01 s.18. The handover meeting runs 10:00–11:00 and signed acceptances are due at 12:00.
- The pack opens with the "not evidenced" page. COM keeps any item that has no signed owner.
- Each of the 12 items has an owner, a status, a next action and a trigger. The list covers:
  - notification register: rows close only on evidenced delivery (s.10.3);
  - misdirection assessment for the 12 contacts;
  - workspace scope, reviewed every 24 hours, with the reasons for not notifying logged (R16b p.2);
  - case register and approval limits (s.13.7);
  - cross-match;
  - monitoring enrolment;
  - public updates;
  - counterparties (s.14.3);
  - scripts;
  - media and takedowns;
  - payroll-delay letters;
  - the communications log for LC.
- The standing messaging rules carry forward unchanged:
  - one message per customer (s.10.6);
  - no links;
  - call-back offered;
  - no email;
  - no HKID numbers.
- COM's handover matches SEC's Q22a and LC's Q23a: the same 12:00 signature time and consistent owners.

**Final action and condition:** as written. The CMT stays convened (CEO entry 1), so any unsigned item stays with the CMT.

**Accountable owner**
- COM is accountable for the handover.
- Receiving owners:
  - Head of Customer Service;
  - DPO and LC;
  - Head of Fraud;
  - Head of Payments Ops;
  - CFO;
  - COM standing duty manager;
  - relationship-manager heads;
  - LC.
- The CEO approves audiences and public updates and remains the only spokesperson.

**HKT time, deadline or trigger**

| Date / time | Item |
|---|---|
| 10:00–11:00 | Handover meeting |
| 12:00 | Signed acceptances |
| Today | Visits; the 31 cross-match report; script v8 |
| 18:00 today | Misdirection assessment |
| Daily | Figures to LC; counterparty updates at 08:00, 13:00 and 18:00 |
| Ongoing | Scope review every 24 hours and on new evidence; triggers as listed |

**Recipient and channel**
- Customers: call with call-back, courier letter, SMS with no link only if not reached by phone, secure inbox only if trusted.
- Counterparties: verified call plus written notice.
- Internal: handover pack, notification register, case register and communications log.

**Final external basis:** COM Q24b "Basis: external" is adopted: R11 pp.6 and 8; R16b p.2; R09 4.4.2; R02 7.2.3(a)(v)(4)–(5), p.32. COM's search record (no external rule on closing or handover of communications) is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.18.1–18.3, s.10.3, s.10.4(d), s.10.6, s.13.7 and s.11.5. No conflict.

**Dispatch instruction**
- SCHEDULE: the handover meeting at 10:00 and signatures at 12:00.
- Items without a signed owner stay with COM and the CMT.

==================================================================
**ORDER OF DEPENDENT ACTIONS (HKT)**
1. **08:00.** I record that the CMT stays convened. SEC retains all restrictions. The 240/240 result is recorded as a sample.
2. **08:05–08:45.**
   - COM checks the channels and archive.
   - By 08:30: LC makes the overdue HKMA update; I approve the 09:00 text.
   - By 08:45: LC clears the text and W1–W4 are verified, using the new W2 default if Payments Ops has not verified the status.
3. **09:00.** Public update published. A copy goes to the HKMA through LC.
4. **10:00.**
   - Payments Ops delivers the alternate-process state record. It feeds LC B3 (HKMA correction) and the 13:00 W2 line.
   - SEC confirms the workspace's CCS status (A3). If late, a workspace Annex E follows.
   - The handover meeting starts.
5. **12:00.**
   - Signed acceptances for all three handover lists.
   - LC re-issues the legal hold.
   - Commissioner receipt request (A2).
   - Closure test (V3) and N2–N5 results. A pass starts the 72-hour V4 window.
   - Any N5 result showing an actual adverse effect on a critical system triggers LC's s.28 assessment at once.
6. **13:00 and 19:00.** Public updates. Counterparty updates at 13:00 and 18:00.
7. **18:00 today.**
   - Misdirection assessment. A finding of further disclosure triggers PCPD and customer notice.
   - Written Board status from me.
   - CMT sitting.
8. **20 Nov.** Annex F B and D drafts plus V1, V2, V5 and V6 by 18:00. Police written referral.
9. **23 Nov.** Root-cause draft at 12:00, then Annex F v1.
10. **25 Nov.** Sign-offs, V7 and V8.
11. **26 Nov.** s.22 change list, A6 confirmation, remediation plan.
12. **27 Nov.** Annex F submitted and receipt saved. Statutory limit 30 Nov.
13. **9 Dec / 16 Dec.** s.22 notices to the MA for the 16 Nov batch (statutory 16 Dec). Post-incident review on 16 Dec, possibly followed by A6 revised-plan submission within 1 month of any PH01 revision.
14. **Standing holds.**
    - Production stays held until a full-set pass and every s.9.3 item is logged.
    - Vendor reinstatement waits for the s.7.5 conditions and my decision.
    - Mobile submission stays closed until s.9.4 stage 3.
    - No monitoring reduction until the N8 criteria are met.
    - The legal hold and no disposal.
    - No closing update until s.11.5 is met.
    - No-payment and no-contact posture continues.

No files were created.