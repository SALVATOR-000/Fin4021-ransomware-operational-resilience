CEO FINAL DECISION RECORD: C07 (Wed 18 Nov 2026, 12:00 HKT, H+52). Lan Tidal Bank, CMT chair.

All actions are simulated, for the facilitator to log. I received sealed answers for all six units: SEC (Q19a, Q19b), LC (Q20a, Q20b) and COM (Q21a, Q21b).

Handoffs received:
- SEC: Q01a, Q01b, Q07a, Q07b, Q16a, Q16b and the current execution state.
- LC: Q02b, Q11a and the notification record.
- COM: Q09a and Q15a.

Sources I checked myself for this card:
- R02 Annex F, pp.43–46; 7.3.2, p.35 ("detected and timely removed or quarantined").
- R01 s.65(1), p.82 ("all reasonable precautions and exercised all due diligence"); s.28 and Sch.6 (checked at C01).
- R10 DPP2(1), p.166.
- R09 4.4.4, p.18 ("acts fraudulently or with gross negligence").
- Citations checked on earlier cards: R11, R16b, R03 6.2.23.
- PH01 v1.0.

**CEO RECORD ENTRIES, 12:00**
1. **Alternate-process state is still unknown.** Across C04 and C06, no card records whether it was cleared, activated, paused or released any payment. I direct the Head of Payments Ops to report its state in writing by 12:30: activated or not, releases by count and value, whether reconciliation ties, and whether SEC's clearance is logged.
   - The report goes to SEC (Q19b N3), to LC (Annex F D2 and the HKMA update) and to me.
   - If it is releasing with no logged clearance, releases pause under my C06 order.
2. **Workspace status.** SEC confirms in writing by 12:30 whether the data workspace is a separate critical computer system (CCS). LC's Q20a(d) depends on this, and the question has been unresolved since C04.
3. **The 31 scam reports.** LC adds them to the Police referral (minimised; joint LC and SEC release; DPO consulted) and to the next PCPD and HKMA updates (PH01 s.5.8, s.5.9; R11 p.8).

==================================================================
**UNIT C07-Q19a: reviewable technical timeline with clock offsets and uncertainties**

**Original answer reference:** sealed SEC answer for C07, "UNIT Q19a", steps T1–T5.

**Decision:** CONFIRM.

**Reason:**
- **Source handling:**
  - Every row traces to a hashed source registered with the Annex B fields.
  - Vendor-service records are labelled "supplier's account – unreconciled" (PH01 s.6.7(d)).
  - The chain from vendor to forensic partner to bank is recorded, and the manifest hash is confirmed by call-back.
- **Clock handling:**
  - Offsets are measured from anchor events for each source and period. Time zones are stated, so UTC is not misread as HKT. Drift is interpolated between anchors.
  - Each row carries the original timestamp, offset, normalised HKT, uncertainty and a tag.
  - Conservative rules apply: an unanchored source gets at least ±4 minutes, and two rows' uncertainties are added together. Events inside that combined uncertainty are logged as "order undetermined" (PH01 s.6.4).
- **Priorities:** the questions that depend on ordering are answered first. These include the backup timing (C05 I1), whether containment failed, and the Annex F fields B5–B6.
- **Review and versioning:** an independent reviewer checks every ordering-critical row. Revisions are added with a change log, never overwritten.
- **Statutory fit:** this supports R02 7.2.3(a)(v)(3)–(4), p.32, and R03 6.2.23(d), p.18. It also feeds LC's Annex F (Q20b).

**Final action and condition:** T1–T5 exactly as written.

**Accountable owner:**
- SEC is accountable.
- Executed by SEC analysts, the forensic firm and the custodian, with an independent reviewer. The vendor relationship owner does the hash call-back.
- LC decides any external use, and sharing with a third party is decided jointly by LC and SEC with the DPO consulted (PH01 s.3).

**HKT time, deadline or trigger:**

| Step | Time |
|---|---|
| Intake | by 13:00 |
| Offsets | by 15:00 |
| Version 1.0 | by 18:00 |
| Independent review | by 20:00 |
| Later versions | on new evidence, each sent to LC as supplementary material |

**Recipient and channel:** the evidence register, the write-once evidence store and the versioned workbook. Delivery to LC is by hand or through the evidence store; corporate email only if it has been logged safe.

**Final external basis:**
- SEC Q19a "BASIS: EXTERNAL" items 1–5 are adopted unchanged: R02 7.2.3(a)(v)(3)–(4), p.32; R03 6.2.23(d), p.18; R02 6.2.23(g), p.20 (supporting only); R02 Annex F B5–B6, p.44 (verified); R01 Sch.6 item 3; R11 p.6, Step 5.
- SEC's "no direct rule located" record ("uncertaint", "time source", "clock", "offset") is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.6.4, s.6.3, s.6.7(d), Annex B, s.5.9. No conflict.

**Dispatch instruction:**
- EXECUTE NOW: T1.
- SCHEDULE: offsets at 15:00, v1.0 at 18:00, review at 20:00.

==================================================================
**UNIT C07-Q19b: monitoring and containment in light of the new indicator**

**Original answer reference:** sealed SEC answer for C07, "UNIT Q19b", steps N1–N8 and the triggers.

**Decision:** CONFIRM.

**Reason:**
- **Overall position:** raise monitoring, keep all containment and add targeted containment.
  - Until the evidence says otherwise, the indicator is treated as related to the original compromise.
  - Nothing in the recorded recovery state can safely be reduced: the gateway is isolated, the recovered image failed, the standby is held, vendor access is revoked, and mobile transfer submission is held (PH01 s.18.3).
- **Steps in order:**
  - capture before any change (s.6.2);
  - check that the quarantine is holding;
  - sweep the whole bank, including the alternate process. A hit there is a security stop, and SEC grants no new clearance until the sweep is clean;
  - re-run the closure test, because no result is recorded and the access window therefore stays open (s.7.4);
  - classify the indicator by 14:00, so LC can judge whether it is a new incident.
- **Customer-side monitoring:** login anomalies and transaction monitoring for the 320 customers, which fits the 31 scam reports (R09 8.1.4).
- **Reducing later:** monitoring can only be reduced against evidence-based criteria, with a 72-hour quiet period.

**Final action and condition:** N1–N8 and the triggers exactly as written. Under my C06 order, if the alternate process is releasing with no logged clearance, it pauses at once.

**Accountable owner:**
- SEC decides isolation, monitoring and security stops (PH01 s.3, s.7.1).
- Executed by security operations, IT Ops network and identity engineers, the forensic firm and Fraud.
- I am told of every widening.

**HKT time, deadline or trigger:**

| Step | Time |
|---|---|
| Capture | 12:10 |
| Quarantine check | 12:30 |
| Sweep and closure test | 13:00 |
| Classification to LC | 14:00 |
| Status reports | hourly (containment not confirmed, s.2.5) |
| Earliest reduction review | only once the N8 criteria are met |

Widening is triggered by any hit outside the quarantined host, or any use of a revoked credential.

**Recipient and channel:** the endpoint detection platform, the monitoring system, the perimeter firewalls and the identity provider. Changes are recorded in the decision log, emergency change record and evidence register. Coordination is through the CMT room or phone bridge.

**Final external basis:**
- SEC Q19b "BASIS: EXTERNAL" items 1–4 are adopted unchanged: R03 6.2.26(a)–(b), p.19; R05 p.1 (checked against the scan); R02 7.2.3(a)(v)(1), p.32; R09 8.1.4, p.32; R01 s.36(2)(c), p.52.
- SEC's "no direct rule located" record on reducing monitoring is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.7.1, s.6.2, s.7.3, s.7.4, s.2.5, s.18.3, s.18.5. No conflict.

**Dispatch instruction:**
- EXECUTE NOW: N1, N6 and N7.
- SCHEDULE: N2 at 12:30, N3 and N4 at 13:00, N5 at 14:00.
- HOLD: any reduction, under N8.

==================================================================
**UNIT C07-Q20a: status of the specified-form follow-up, the clock and immediate action**

**Original answer reference:** sealed LC answer for C07, "UNIT Q20a", findings 1–4 and actions (a)–(e).

**Decision:** CONFIRM.

**Reason:**
LC's reading of the notification record is correct:
- **s.28(1)–(2) notification:** made by telephone by 08:30 on 16 Nov. It was not in the specified form, but it stated the nature of the incident and identified the CCS, inside the 12-hour limit.
- **s.28(3) specified-form written record:** required, because the first notification was by telephone. Under Sch.6 item 2 the clock ran 48 hours from the call and expired no later than 08:30 on 18 Nov.
- **Annex E:** dispatched through the secure channel by 11:00 on 16 Nov. On the record the obligation is satisfied, neither outstanding nor late.
- **The gap is proof, not dispatch:** no receipt or reference number is recorded, and neither is the outcome of the 18:45 confirmation call.

LC's actions protect the s.65(1) defence (p.82, verified), which needs evidence that the bank "took all reasonable precautions and exercised all due diligence":
- preserve the dispatch logs;
- obtain the Commissioner's confirmation;
- re-submit openly if the Commissioner has no record.

On the other two questions:
- **Workspace as a separate CCS:** LC's conditional analysis is correct. If it is a separate CCS, the bank is either inside the Annex E window, which closes at 19:30 today, or already late, and either way files now.
- **New indicator:** on current facts it is not a new notifiable incident. R02 7.3.2, p.35, excludes "a computer-system security threat that is detected and timely removed or quarantined". If SEC finds an actual adverse effect on a CCS, a new clock runs. That ties to the SEC Q19b classification at 14:00.

**Final action and condition:** (a)–(e) exactly as written. SEC's written CCS-status confirmation is due by 12:30 (CEO entry 2). The 18:00 supplement on the new indicator includes SEC's 14:00 classification.

**Accountable owner:**
- LC is accountable; a designated LC officer executes.
- SEC confirms the workspace status and the indicator facts.
- I am informed. No internal approval holds any filing (PH01 s.2.4).

**HKT time, deadline or trigger:**

| Step | Time |
|---|---|
| Proof preserved | 12:45 |
| Call to the Commissioner's office | 13:00 |
| Re-submission if the Commissioner has no record | 14:00 |
| Re-submission anyway, as a labelled duplicate, if there is no answer | 15:00 |
| Workspace Annex E | 13:00 if late; 14:00 if inside the window (window closes 19:30) |
| Indicator supplement | 18:00 |
| A new s.28 clock (12 or 48 hours) | only if SEC finds an actual adverse effect on a CCS |

**Recipient and channel:** the Commissioner of Critical Infrastructure (Computer-system Security). Confirmation by the verified CI telephone route. Annex E and supplements through the designated secured channel, with the standby device as fallback.

**Final external basis:**
- LC Q20a "Basis: external" is adopted:
  - R01 s.28(3), (5)–(6), p.44 (verified at C01);
  - R01 Sch.6 items 1–2, p.97;
  - R01 s.65(1), pp.81–82 (verified);
  - R01 s.7(1)(b), p.16;
  - R02 7.3.2, p.35 (verified);
  - R02 7.3.5 and 7.3.6(b), p.36.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.5.5 ("If no receipt is shown, LC asks the recipient for one"), s.2.4, s.5.9. No conflict found; the gap was in carrying out s.5.5.

**Dispatch instruction:**
- EXECUTE NOW: (a) and (b).
- (c) is conditional on the Commissioner's answer, with a 15:00 fallback.
- (d) depends on SEC's 12:30 confirmation.
- SCHEDULE: (e) at 18:00.

==================================================================
**UNIT C07-Q20b: the s.28(4) written report (Annex F)**

**Original answer reference:** sealed LC answer for C07, "UNIT Q20b".

**Decision:** CONFIRM.

**Reason:**
- **The report is complete in scope:**
  - It is submitted on the information available, with unverified items marked and later facts sent as supplementary material (R02 7.3.7(a)).
  - It does not wait for root cause or attribution.
  - LC's section map matches Annex F as published (pp.43–46, verified): A2 with physical location; B1–B8 including the earliest and awareness times; C1–C7 including the HK$ estimate and duration; D1–D5 including CCS status; E1–E2 including the Police case reference and media dates; F, the reporting entity.
- **Owners and inputs:** each section has a named owner, assigned by 17:00, and the Q19a timeline is built in.
- **Exclusions:** no personal data and no privileged advice.
- **Deadlines:**
  - Statutory limit: 30 Nov (Sch.6 item 3).
  - Internal target: 17:00 on 27 Nov, which leaves a margin because the Cap. 1 day-counting rules are not in the manifest.
  - PH01 s.2.4 sends the report regardless of any open internal item.

**Final action and condition:** as written. Two record fills:
- The D2 operation status comes from the Payments Ops report due at 12:30 (CEO entry 1).
- The E1 Police case reference is obtained by LC from the CSTCB.

**Accountable owner:**
- LC is accountable and is the reporting entity in section F. A designated LC officer leads drafting.
- Section owners: SEC and the forensic lead; Payments Ops and IT Ops; the DPO; Fraud with COM; the CFO.
- I review in parallel and cannot delay submission.

**HKT time, deadline or trigger:**

| Step | Time |
|---|---|
| Section owners assigned | 17:00 today |
| Section drafts | 18:00, 20 Nov |
| Consolidated v1 | 23 Nov |
| Sign-offs | 25 Nov |
| Submission and receipt | by 17:00, 27 Nov (statutory limit 30 Nov) |
| Supplements | as facts emerge |

**Recipient and channel:** the Commissioner of Critical Infrastructure (Computer-system Security), through the designated secured channel. Fallbacks: the standby device, then the route the Commissioner confirms (PH01 s.5.6). The HKMA is told after submission.

**Final external basis:**
- LC Q20b "Basis: external" is adopted: R01 s.28(4)–(5), p.44; R01 Sch.6 item 3, p.97; R02 7.3.7(a), p.37; R02 Annex F, pp.43–46 (verified).
- LC's search record on the Cap. 1 day count is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.5.1, s.5.2, s.5.5, s.5.6, s.6.4, s.6.7(d), s.18.4, s.2.4. No conflict.

**Dispatch instruction:**
- SCHEDULE: assignments at 17:00 today, then the milestones above.
- Submission is never held by an internal item.

==================================================================
**UNIT C07-Q21a: routing scam and remediation cases, and what can be promised**

**Original answer reference:** sealed COM answer for C07, "Q21 a".

**Decision:** CONFIRM.

**Reason:**
- **One intake, existing channels:**
  - A single case register.
  - Intake only through existing channels: the 24/7 fraud line, branches, relationship managers and call-back. No new numbers, links or online forms while the fake page is live.
  - Every case gets a case reference (PH01 s.13.6) and protective action at first contact (R09 4.4.3, 8.1.4).
- **Triage:**
  - Six categories, each with an owner.
  - A case unclear between A (unauthorised transaction) and B (scam payment the customer made) is treated as A. This protects the R09 4.4.4 position (p.18, verified): unless the customer "acts fraudulently or with gross negligence", they should not bear the direct loss.
  - The frontline never decides gross negligence.
- **What staff may promise:** exactly matches PH01 s.13.1–13.7.
  - No promise of reimbursement for scam payments the customer made (s.13.4).
  - No claim that a scam is linked to the leak until that is verified.
  - Approval limits under s.13.7. Amounts above HKD 50,000 per customer come to me.
- **Cross-match:** matching the 31 reports against the workspace feeds the PH01 s.10.4(c) "reports of misuse" factor.
- **Interim instruction:** the 12:30 interim instruction carries only PH01 fixed positions and routing. Under my C02 rule that version may go while LC's 12:45 clearance of script v7 runs in the fixed slot.

**Final action and condition:**
- Exactly as written.
- Scam details from case intake are passed to SEC's evidence process (SEC Q19b N6).
- Any match outside the 320 goes straight to the DPO and LC. I decide scope under s.10.4(d).

**Accountable owner:**
- COM: routing and scripts. LC clears, with the second LC officer as backup.
- Cases A–D: Head of Fraud, with LC.
- Case E: Head of Payments Ops.
- Case F and anything above HKD 50,000: me.
- CFO: running total.
- Cross-match: Fraud with the DPO.

**HKT time, deadline or trigger:**

| Step | Time |
|---|---|
| Interim instruction | 12:30 |
| LC clears script v7 | 12:45 |
| Cross-match result | 15:00 |
| All 31 cases owned and contacted | 17:00 |
| Acknowledgement letter | within 1 business day |
| First case update | within 2 business days |
| Fraud-line line in the public update | next public update |

**Recipient and channel:** customers through the existing fraud line, branches, relationship managers and call-back to numbers on file. Cases are logged in the case register, cross-referenced to the notification register.

**Final external basis:**
- COM Q21a "Basis: external" is adopted: R09 4.4.2, p.17; R09 4.4.3–4.4.4, p.18 (4.4.4 verified); R09 8.1.4, p.32; R05 p.1 (checked against the scan); R11 p.4.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.13.1–13.7, s.10.4(c)–(d), s.11.5, s.2.2. No conflict.

**Dispatch instruction:**
- EXECUTE NOW: the 12:30 interim instruction.
- SCHEDULE: script v7 at 12:45, which depends on clearance or the fixed-position default; the cross-match at 15:00; case owners by 17:00.

==================================================================
**UNIT C07-Q21b: correcting the notification list and sending follow-ups without duplicates**

**Original answer reference:** sealed COM answer for C07, "Q21 b", steps 1–5.

**Decision:** OVERRIDE (timing and priority for the 12; COM's method is kept).

**Reason:**
- **COM's method is right and is kept:**
  - Stop the old details.
  - Take corrections only from verified bank records, with Fraud checking any change made after the incident began. This applies PH01 s.10.5 and DPP2(1), p.166 (verified): "All practicable steps shall be taken to ensure that— (a) personal data is accurate having regard to the purpose".
  - Rebuild the register only from delivery evidence. A status of "executed in simulation" is not delivery (s.10.3).
  - Send one message per customer, chosen by what was evidenced as delivered (s.10.6).
  - Assess the misdirection risk.
- **The problem: the 12 are the most exposed group.** Every notice to them since 16–17 Nov went to wrong contact details. Their data is published and scams are active.
  - Under COM's plan they wait until 15:30, behind a register rebuild that they do not need: they are misdirected by definition.
  - Their audience is already approved, because they are within the 320 batches approved at C05.
  - R11 p.8 says notice must go "in sufficient time for its benefits to be maximised, in particular to reduce the risk of harm". R16b p.3 says notify affected customers "as soon as practicable".
- **The change:** the 12 move ahead, and LC's clearance moves earlier. This changes timing, so the unit is marked OVERRIDE.

**Final action and condition:**
1. **Steps 1–3 and 5 exactly as written,** with one addition: Fraud clears each of the 12 corrections as a priority, target 13:30, latest 14:30.
2. **Text clearance moved to 13:15.** LC clears both the consolidated notice (V3) and the short follow-up text at 13:15, in the fixed slot with the second LC officer as backup.
   - If no clearance is logged by 13:30, the C05 default applies: I direct release of the minimum notice (SEC-verified facts plus protective advice) while LC reviews.
3. **The 12 (priority batch C07-P12).**
   - Each customer receives V3 as soon as Fraud clears that correction and the text is cleared, from about 13:30: a call to the corrected number with a call-back offer, then a no-link SMS only if the call is unanswered.
   - Courier letters to the corrected addresses go by 16:00.
   - If Fraud cannot clear a correction by 14:30, that customer gets a relationship-manager or branch contact instead (COM's default).
   - Fraud checks the 12 against the scam case list before calling. If a customer has an open case, the case owner delivers V3.
4. **Everyone else as COM wrote:**
   - Register rebuilt 13:00–15:00.
   - I approve the class audiences at 15:00.
   - Calls from 15:30 and letters by 18:00.
   - One message per customer: V3 for those with no evidence or V1 only; a short letter for those with evidenced delivery of V2; content through the case owner for open cases.
   - Visits on 19 Nov for anyone not reached.

**Accountable owner:**
- COM keeps the register and sends.
- I approve the audiences.
- LC clears, with the second LC officer as backup.
- SEC and Operations confirm where the corrections came from; Fraud clears the corrections.
- The DPO and LC assess the misdirection.
- Executed by the notification team and the courier.

**HKT time, deadline or trigger:**

| Step | Time |
|---|---|
| Old details stopped | 12:15 |
| Text clearance (default point 13:30) | 13:15 |
| Fraud clears the 12 | 13:30 target, 14:30 latest |
| Calls to the 12 | from about 13:30 |
| Letters to the 12 | by 16:00 |
| Register rebuild | 13:00–15:00 |
| Class audiences approved | 15:00 |
| Calls to everyone else | from 15:30 |
| Letters to everyone else | by 18:00 |
| Figures to LC | 18:00 |
| Visits | 19 Nov |

**Recipient and channel:** the 320 individuals by call (with call-back offer), no-link SMS only if a call goes unanswered, and courier letter. Secure inbox only if trusted. No email. No HKID numbers in any message.

**Final external basis:**
- COM Q21b "Basis: external" is adopted: R10 DPP2(1)(a)–(b), pp.166–167 (verified); R11 pp.1–2 and 8; R09 4.2.3, p.16 (by analogy).
- New support for the priority:
  - R11 p.8 (verified at C03), "in sufficient time for its benefits to be maximised, in particular to reduce the risk of harm";
  - R16b p.3 (verified), "notify the affected customers as soon as practicable".
- COM's "no direct rule located" record on de-duplication is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.10.3, s.10.5, s.10.6, s.3, s.17.2. The s.2.3 hold conflict is resolved by the C05 fixed slot and default under s.1.3.

**Dispatch instruction:**
- EXECUTE NOW: step 1 (12:15).
- SCHEDULE: clearance at 13:15; C07-P12 from about 13:30, per customer once Fraud clears the correction; the rest from 15:30.
- Dependencies: the rest wait on the register rebuild and my 15:00 approval.

==================================================================
**ORDER OF DEPENDENT ACTIONS (HKT)**

1. **12:00–12:15.**
   - SEC: intake and hashing (T1); host capture (N1).
   - COM: stop the 12 old contact details.
   - All containment kept and monitoring raised.
2. **12:30.**
   - Payments Ops reports the alternate-process state; pause it if it is releasing without a logged clearance.
   - SEC confirms the workspace's CCS status. This feeds Q20a(d) and Annex F.
   - SEC checks the quarantine.
   - COM issues the interim case instruction.
3. **12:45–13:00.**
   - LC preserves the dispatch proof and clears script v7.
   - At 13:00: LC calls the Commissioner's office; SEC runs the bank-wide sweep and re-runs the closure test; the register rebuild starts.
   - The workspace Annex E goes by 13:00 if late.
4. **13:15–13:30.**
   - LC clears V3 and the follow-up text; default point 13:30.
   - Fraud clears the 12 corrections, and calls to the 12 begin.
5. **14:00.**
   - SEC classifies the indicator and passes it to LC. If it shows an actual adverse effect on a CCS, a new s.28 clock starts.
   - Annex E is re-submitted if the Commissioner has no record.
   - The workspace Annex E goes by 14:00 if it is inside the window.
6. **15:00.**
   - Fraud reports the cross-match. Any match outside the 320 goes to the DPO and LC, and I decide scope.
   - The register rebuild completes, and I approve the class audiences.
   - SEC measures clock offsets.
   - LC re-submits as a labelled duplicate if the Commissioner has not answered.
7. **15:30–18:00.**
   - Calls to the other classes.
   - Letters to the 12 by 16:00.
   - All 31 cases have owners by 17:00.
   - Annex F section owners are assigned by 17:00.
8. **18:00.**
   - Timeline v1.0.
   - LC's indicator supplement to the Commissioner.
   - All letters sent and register figures to LC.
   - HKMA update, including the 31 scam reports, the indicator, the alternate-process state and the tolerance.
   - PCPD supplementary information, including any finding on the misdirection.
9. **20:00.** Independent review of the timeline.
10. **19 Nov to 30 Nov.**
    - Visits on 19 Nov.
    - Annex F milestones, with submission by 17:00 on 27 Nov (statutory limit 30 Nov).
11. **Standing holds.**
    - Gateway isolation and evidence hold.
    - Vendor access revoked.
    - Standby and recovered image held.
    - Mobile transfer submission held.
    - No reduction in monitoring until the N8 criteria are met.
    - No promise of reimbursement for scam payments customers made.

No files were created.