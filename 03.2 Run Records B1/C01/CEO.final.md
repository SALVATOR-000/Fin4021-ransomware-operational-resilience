CEO FINAL DECISION RECORD for C01 (Mon 16 Nov 2026, 08:00 HKT, H+0). Lan Tidal Bank, CMT chair.

All actions are simulated, for the facilitator to log. The dispatch log was empty at release. No facilitator handoffs went to any role. All three sealed answers were received; none is missing.

Before writing this record I checked the main citations myself:
- R05 pp.1–3 against the scan images.
- R01 s.28, PDF pp.43–44, and Sch. 6, p.97.
- R02 7.2.3, pp.32–33, and 7.3.2–7.3.7, pp.35–37.
- R03 1.1.3, p.3, and 6.2.23(c), p.18.
- R09 8.2.1–8.2.5, pp.32–33.
- R04 para 2.4, p.4, and R07 1.3.3, p.5.
- PH01 v1.0 in full.

**CEO record entry, 08:00.** As CMT chair I declare Severity 1 at 08:00 HKT. The trigger is PH01 v1.0 s.4.1: "a critical operation is disrupted". PH01 does not say who declares, and the chair fills that gap. The CMT is convened for 08:30 (PH01 s.2.1). Every PH01 clock that runs "from declaration" runs from 08:00. Logging this only fills a record field that SEC, LC and COM had assumed, so it changes no unit.

==================================================================
**UNIT C01-Q01a: what to isolate first, and keeping available services running**

**Original answer reference:** Sealed SEC answer, C01, "UNIT Q01a", actions A1–A10.

**Decision: OVERRIDE** (narrow; A1–A10 otherwise unchanged).

**Reason**
- A1–A10 are adopted as written:
  - network-layer isolation of the gateway segment only, with hosts left powered on;
  - pre-change capture capped at 10 minutes, and skipped if spread is active;
  - credential actions and the closure test;
  - the failover HOLD until a 12:00 condition, logged with the four PH01 s.2.3 items;
  - the 08:30 terminal and email logs, the hourly status reports and the s.22 change register.
- These steps match PH01 s.7.1 and s.6.2, R05 p.1 and R02 7.2.3(f).
- The one change is in A5. SEC did not decide whether to pause mobile transfer submission; it referred the question to the CMT chair as "consider pausing mobile transfer submission at the application layer while balance view stays on".
- I now decide that question, adding a condition, a time and a hold default. That changes execution, so the unit is marked OVERRIDE.

**Final action and condition**
1. A1–A10 exactly as in SEC's sealed Q01a.
2. New action A5-bis (CEO decision):
   - **(a) 08:20.** The Head of Payments Operations confirms and logs whether mobile or internet banking still accepts outbound domestic transfer or payroll instructions.
   - **(b) If it does,** only those submission functions are disabled at the application layer by 08:40, and a static in-app notice with no link is shown. The notice reads: "Outgoing transfers and payroll submission are temporarily unavailable. Please do not resubmit. Your balances remain viewable." COM owns the notice and LC clears it at the 08:30 CMT. Login and balance view stay on.
   - **(c) PH01 s.2.3 condition** (four items):
     - Verifier: SEC.
     - Latest time: 08:40.
     - What is verified: the change is outside the gateway segment and does not touch the login or balance-view paths. SEC checks this against the dependency map and the A6 synthetic checks.
     - Default if not verified: HOLD the pause, so that the 8-hour balance-access tolerance is never put at risk, and rely on COM's "do not resubmit" messages.
     - Close-out: a log entry.
     - After the change, a synthetic login and balance check runs. If it fails, the change is reverted at once and SEC phones the chair.
   - **(d)** Any instruction accepted since the disruption began is held as "status unknown" (PH01 s.8.6) and goes into COM's A2 list.
   - **(e)** If the channel already rejects instructions, nothing is done and the result is logged.

**Accountable owner**
- A1–A10: SEC. Executed by the IT Operations network, firewall and identity engineers. The Head of IT Operations is consulted.
- A5-bis: the CEO as CMT chair. Executed by the Head of Payments Operations through the digital-channel and IT Operations engineers. SEC verifies.

**HKT time, deadline or trigger**
- Isolation by 08:10 (target), 08:15 at the latest. Immediately if spread is active.
- Validation 08:15–08:30.
- A8 logs at 08:30.
- A9 status reports at 09:00, then hourly.
- A7 failover condition by 12:00.
- A5-bis: confirmation at 08:20, change by 08:40.
- Isolation is widened only when spread is observed.

**Recipient and channel**
- Changes are made on the gateway segment-boundary firewalls and routers, the privileged-access system and identity provider, the replication links, the backup scheduler, and the mobile/internet banking application configuration (A5-bis).
- Instructions are given in person in the CMT room or on a phone bridge, never by corporate email. They are recorded in the decision log and the emergency change record.

**Final external basis**
- Unchanged and adequate: SEC Q01a, "BASIS: EXTERNAL" items 1–5. I confirmed R05 p.1 against the scan, R02 7.2.3(a)(v)(1) and (f) at pp.32–33, and R01 s.27(5) at p.43.
- For A5-bis:
  - R05 (HKMA circular, 22 Jun 2010), PDF p.1, heading "Immediate incident response", paragraph 1, checked against the scan: "The top priority should be to safeguard the interests of customers who have been or may be affected by the incident." This applies because a submission screen that accepts instructions which cannot be processed creates instructions of unknown status and a risk of duplicates.
  - R09 (SPM TM-E-1 V.4), s.8.2.1, PDF p.32. This covers "service interruptions" affecting e-banking services.
  - R06 (SPM OR-2), s.1.3, PDF p.3: "disruptions to an AI's critical operations must not exceed its 'tolerance for disruption'". This is the reason the default protects balance view.
- No direct rule located in assigned sources for pausing a front-end submission function during a back-end outage:
  - "suspend" in R09: hits at 4.4.3 (account suspension for fraud) and 8.1.4 (suspending suspicious transactions), neither on point.
  - "unavailab" in all files: PH01, R03, R07, R08, none on point.
  - "duplicate" in all files: PH01 and R07 only.
  - "mobile transfer submission" in all files: PH01 only.
- Professional judgment: the pause cuts the number of unknown-status and duplicate payments at no cost to any working service.

**Final internal basis** (Internal bank procedure: PH01 v1.0, effective 1 Oct 2026)
- SEC Q01a, "BASIS: INTERNAL", adopted: s.3, s.7.1, s.6.2, s.7.3–7.4, s.6.1, s.2.3, s.5.6–5.7, s.2.5 and s.18.4.
- For A5-bis:
  - s.9.4, stage "(3) mobile transfer submission reopened with limits". This assumes submission is closed while the disruption lasts.
  - s.8.6: "Items in flight at the failure are held as status unknown until an independent record shows they did not settle."
  - s.7.1: "Services still working are kept running".
- No conflict with any external requirement.

**Dispatch instruction**
- EXECUTE NOW: A1–A4, A6 and A10.
- SCHEDULE: A8 at 08:30; A9 at 09:00 and then hourly.
- HOLD: any failover until SEC logs the A7 condition. The default is hold or an approved alternate process, never go ahead.
- A5-bis: EXECUTE by 08:40 only if both (a) and (c) are met. Otherwise HOLD, or NO ACTION if the channel already rejects instructions.

==================================================================
**UNIT C01-Q01b: evidence to secure before changes, and custody**

**Original answer reference:** Sealed SEC answer, C01, "UNIT Q01b", B1–B9.

**Decision: CONFIRM**

**Reason**
- **Evidence hold and custodian:** the hold, the independent custodian and the Annex B register meet PH01 s.6.1, s.6.3 and Annex B.
- **Capture sequence:** volatile capture is capped at 10 minutes, and containment goes first if spread is active. This applies R02 7.2.3(f): an incident that has "impacted business operations" is prioritised, and "Otherwise, more time should be allocated to evidence collection".
- **Logs:** log immutability follows R03 6.2.23(c) (verified, p.18).
- **Production and offline scope:** offline backups are recorded but never mounted on the affected network.
- **Supplier requests:** drafts are due within one hour, by 09:00 (PH01 s.6.7(a)).
- **No hold on reporting:** nothing in the evidence work delays an external report.
- **Dependency:** the forensic call-in at 08:15 (PH01 s.6.5) relies on the Severity 1 declaration, which I made at 08:00.

**Final action and condition:** as written in B1–B9. Third-party data sharing requires LC and SEC jointly, with the DPO consulted. By default only masked, minimised data is shared (PH01 s.16.2).

**Accountable owner**
- Accountable: SEC.
- Executed by the evidence custodian, SEC analysts and the forensic firm.
- LC issues the written legal hold at 08:00 (PH01 s.17.1). I direct this as a dependency; it does not change Q02.
- The vendor relationship owner sends any supplier request.

**HKT time, deadline or trigger**
- Hold and register: 08:00.
- Volatile capture: 08:00–08:10, or skipped if spread is active.
- Log exports and images: from about 08:15.
- Supplier drafts: by 09:00, if a supplier is in scope.
- Standby snapshot: by 12:00.

**Recipient and channel:** the write-once evidence store, the evidence register and the decision log. The forensic firm is reached by phone through its contract contact. Nothing goes by corporate email until SEC logs it safe.

**Final external basis:** SEC Q01b, "BASIS: EXTERNAL" items 1–5, adopted unchanged:
- R02 7.2.3(a)(v)(2), p.32: "Digital evidence handling, including identification, collection, acquisition, preservation of evidence and chain of custody".
- R02 7.2.3(f) and (h), p.33.
- R03 6.2.23(c), p.18.
- R01 s.36(2)(b), p.52, as a general principle (I verified "to preserve the state of the system").
- R11 Step 2, conditional only.
- SEC's search record for the custody fields is adopted unchanged.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.6.1–6.7, s.16.2, s.17.1, s.3 and Annex B, as in SEC Q01b "BASIS: INTERNAL". No conflict.

**Dispatch instruction**
- EXECUTE NOW: B1–B3, B8 and B9.
- SCHEDULE: B4–B6 from 08:15.
- B7: SCHEDULE by 09:00, conditional on the third-party register showing a supplier in scope.

==================================================================
**UNIT C01-Q02a: initial HKMA reporting**

**Original answer reference:** Sealed LC answer, C01, "UNIT Q02a".

**Decision: CONFIRM**

**Reason**
- A telephone report to the HKMA supervisory contact (from the printed RCR) by 08:30, on the facts held, with unverified items marked, and not waiting for containment or CMT sign-off.
- This meets R05 p.2: "notify the HKMA immediately and provide it with whatever information is available at the time" and "should not wait until it has rectified the problem". I checked both against the scan.
- It also meets PH01 s.2.4. The four-hourly update cadence and the immediate-update triggers match PH01 s.5.8.
- No conflict with any other role. LC tells the HKMA about COM's planned statement, which is the same point COM asked for.

**Final action and condition:** as written:
- the call with items 1–7;
- questions to the HKMA on its reference number, follow-up format and update frequency;
- a written summary by 10:00 by the route the HKMA names;
- updates about 12:30, 16:30, 20:30, 00:30 and 04:30, then 08:00 and 18:00 daily;
- an update at once on any of: BCP activation, data exposure, an extortion demand, a change in service status (this includes any A5-bis pause), or a public statement.

**Accountable owner:** LC, who makes the call personally. SEC supplies facts in parallel. The chair is informed; chair approval is not a precondition.

**HKT time, deadline or trigger:** trigger is awareness at 08:00. The call is completed by 08:30 at the latest (professional judgment applying R05's "immediately"). Written summary by 10:00.

**Recipient and channel:** HKMA banking supervision contact by telephone, using the RCR. Written follow-up by the HKMA-confirmed route, never corporate email until SEC logs it safe. Every contact is recorded under PH01 s.5.5.

**Final external basis:** LC Q02a, "External basis", adopted:
- R05, PDF p.2, heading "Reporting incident to the HKMA", paragraph 1; and p.3, heading "Handling of customers' and media's enquiry", paragraph 1. All verified against the scan.
- R09 s.8.2.5, p.33 (verified).
- R04 para 2.4, p.4 (verified).
- R08 s.3.3.3.
- R07 s.1.3.3, p.5 (verified; conditional).
- LC's no-rule search record on the channel, form and a numeric time limit is adopted unchanged.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.5.1, s.5.2, s.2.4 and s.5.8, as in LC Q02a. No conflict.

**Dispatch instruction**
- EXECUTE NOW: the call.
- SCHEDULE: the written summary by 10:00 and the four-hourly updates. Immediate updates fire on their triggers.
- No dependency holds the call.

==================================================================
**UNIT C01-Q02b: Cap. 653 s.28 notification**

**Original answer reference:** Sealed LC answer, C01, "UNIT Q02b".

**Decision: CONFIRM**

**Reason**
- **Trigger:** unauthorised commands encrypting a designated CCS and disrupting a core function meet s.28(1) and the "actual adverse effect" test in R02 7.3.2. This is the Sch. 6 item 1(a) 12-hour category: "has disrupted, is disrupting ... the core function ... 12 hours after the CI operator ... becomes aware" (verified, R01 p.97). Awareness is 08:00 (R02 7.3.5).
- **Route:** phone notification on the verified CI route is permitted by R02 7.3.6(b) and R01 s.28(2)(b)(ii), as long as it gives the nature of the incident and identifies the CCS (verified, p.44).
- **Follow-on filings:** the Annex E route sequence when the terminal is down (released terminal, then the standby device, then a Commissioner-confirmed route) applies PH01 s.5.6 and R02 1.1.6. Annex E is due 48 hours after the call (Sch. 6 item 2) and Annex F 14 days after awareness (item 3). Both are correct.
- **Deadline reading:** LC reads PH01 s.2.4's "30 minutes before" as a last resort only, with s.28(2)(a)'s "as soon as practicable" governing. I adopt that reading.

**Final action and condition:** as written:
- phone notification by a designated LC officer, in parallel with the HKMA call, with nature, CCS, summary, awareness time and contact details;
- obtain a reference number and the Commissioner's accepted alternative written route;
- Annex E by the compliant route;
- Annex F;
- fallback to any route giving the nature and identifying the CCS if the phone route fails;
- conditions C-1 to C-4 as logged.

**Accountable owner**
- Accountable: LC. Executed by a designated LC officer.
- Who clears the conditions:
  - SEC: terminal release by 08:30.
  - Compliance: the standby device.
  - The Commissioner's office: any alternative written route.

**HKT time, deadline or trigger**
- Phone call by 08:30, and never later than 09:00. Statutory outer limit 20:00, Mon 16 Nov. If SEC's timeline shows earlier certainty, the limit moves earlier (C-4).
- Annex E: internal target 20:00, 16 Nov; statutory limit 48 hours after the call (about 08:30, Wed 18 Nov).
- Annex F: internal target 27 Nov; statutory limit 30 Nov 2026.

**Recipient and channel:** the Commissioner of Critical Infrastructure (Computer-system Security), not the MA (R01 s.6, p.15, verified):
- the notification by phone on the verified CI route;
- Annex E and Annex F through a designated secured channel, as listed above.

**Final external basis:** LC Q02b, "External basis", adopted. Verified: R01 s.28(1)–(6), pp.43–44; Sch. 6 items 1–3, p.97; R02 7.3.2, 7.3.4–7.3.7, pp.35–37; R02 1.1.6, p.4; R03 1.1.3, p.3. LC's no-rule search record is adopted unchanged.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.5.2, s.5.3, s.5.6, s.2.4 and s.1.4, as in LC Q02b. No conflict.

**Dispatch instruction**
- EXECUTE NOW: the phone notification.
- SCHEDULE: Annex E (target 20:00, 16 Nov) and Annex F (target 27 Nov).
- Annex E depends on the C-1 route decision at 08:30. The phone notification has no dependency.

==================================================================
**UNIT C01-Q03a: alerting affected and likely affected customers**

**Original answer reference:** Sealed COM answer, C01, "Q03 a".

**Decision: CONFIRM**

**Reason**
- **Effective means:** COM alerts proactively by calls and by SMS and push with no link, and keeps letters for later. This meets R05 p.1 ("proactively notify ... through the most effective means ... whether the bank would reimburse any losses", checked against the scan) and R09 8.2.2.
- **Within PH01:** COM resolved the letter-default tension inside PH01 s.10.2.
- **Priority order:** payroll first by value date, not by customer size, mirrors PH01 s.8.4.
- **Conditions:** C1–C5 carry all four PH01 s.2.3 items, and the security conditions default to "do not use that channel", which is correct.
- **Fees and losses:** the fee waiver and the claims route match PH01 s.13.1, 13.2 and 13.6.
- **A5-bis:** any app pause needs no change to COM's text. It is covered by "currently disrupted" and enters through the C2 fact-check at 08:40.

**Final action and condition:** as written:
- Groups A1, A2 and B, channels and draft wording;
- frontline script and IVR at 08:45;
- delivery register under PH01 s.10.3;
- conditions C1–C5.

I will approve the audience as chair at the 08:30 CMT after consulting LC, SEC and the DPO (PH01 s.3).

**Accountable owner**
- COM drafts and sends.
- The CEO (CMT chair) approves the audience.
- LC clears the text.
- SEC and Operations confirm the facts.
- Executed by the contact centre and SMS/push team, the relationship-manager and payments call teams, Payments Operations (lists) and the Fraud team (changed contact details).

**HKT time, deadline or trigger**
| Time | Action |
|---|---|
| 08:30 | Audience approved |
| 08:40 | Facts confirmed (C2) |
| 08:45 | Channel trust logged (C1); frontline script and IVR live |
| 08:50 | LC clears the text (C4) |
| 09:00 | A1 calls and SMS/push start |
| 09:30 | Group B SME tranche |
| 10:00–11:00 | Group B retail tranches |
| By 11:00 | A1 customers with payroll due today called |
| By 15:00 | A1 customers with payroll due tomorrow called |
| List + 1 hour | A2 alerts sent |

**Recipient and channel:**
- Group A1 by personal call (with the call-back offer) plus SMS and push, no link.
- Group A2 by SMS and push, plus a call for SME and time-critical items.
- Group B by SMS and push, no link.
- Staff by mobile broadcast and phone cascade, not corporate email.

**Final external basis:** COM "Basis" items 1–4, adopted:
- R05 p.1 "Customer notifications", p.2 "Public announcement" and p.3 "Handling of customers' and media's enquiry", all checked against the scan.
- R09 8.2.2, p.33, and footnote 26 (verified).
- R06 8.3, R07 4.7.2 and R02 7.2.3(a)(iv) and (e) as general principles.
- COM's no-rule search record on numeric timing is adopted. The times are professional judgment.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.3, s.10.1–10.3, s.10.5–10.6, s.13.1–13.2 and s.2.3, as in COM's "Internal bank procedure" list. No conflict beyond the letter-default point COM resolved under s.1.3.

**Dispatch instruction**
- SCHEDULE, in the order above.
- Dependencies:
  - Sends depend on the 08:30 audience approval, C2 at 08:40 and C4 at 08:50.
  - Each SMS, push or app channel depends on C1 at 08:45. If C1 is not met, that channel is not used and the others proceed.
  - A2 depends on the Payments Operations list (C5 default applies at 09:30).

==================================================================
**UNIT C01-Q03b: public holding statement**

**Original answer reference:** Sealed COM answer, C01, "Q03 b".

**Decision: CONFIRM**

**Reason**
- **Trigger:**
  - R05 p.2(a) and (b) are met: a critical channel is disrupted, recovery is uncertain, and a large number of customers may be affected.
  - R09 8.2.3 expects a release "shortly after the commencement of any disruption". I verified this at p.33. Failover is unverified, so the bank has no "reasonable confidence" of near-term resumption.
- **Timing and cadence:** a target of 09:00 (latest 09:30) and a next update by 13:00 meet that standard and sit within PH01 s.11.2.
- **Wording:**
  - The draft names no system, attacker, vendor or designation (PH01 s.11.3).
  - The "authorities informed" line depends on LC logging the HKMA call.
  - The copy goes to the HKMA through LC at release (R05 p.3; PH01 s.5.8).
- **Approval, spokesperson and naming the cause:** I accept COM's chair-approval route and the chair-only spokesperson. I also accept the "cyber security incident" wording unless LC logs a prejudice concern by 08:50 (R05 p.2 weighing).

**Final action and condition:** as written:
- a bilingual statement (English and Traditional Chinese) on the website status page, press release, official social media, app banner (if C1 is met), branch notices and IVR;
- the fixed media lines;
- the "[We have informed the relevant authorities.]" line included only if LC has logged the Q02a call;
- the balance-view line conditional on SEC confirming by 08:40;
- release conditions linked to Q01a and Q02a as written.

**Accountable owner**
- The CEO (CMT chair) approves and is the sole spokesperson. The COO approves if I am unreachable for 15 minutes.
- LC clears; SEC and Operations fact-check.
- COM executes and keeps the communications log.

**HKT time, deadline or trigger:** release at 09:00 (target), 09:30 at the latest. Next update by 13:00, then at least every six hours between 07:00 and 22:00, and at once on any change in service status.

**Recipient and channel**
- The public and media through the channels listed above.
- A copy goes COM → LC → HKMA at release, by the HKMA-confirmed route and not corporate email.
- COM logs the form and date for Annex F Part E (R02 p.46, verified).

**Final external basis:** COM "Basis" adopted:
- R05 p.2 "Public announcement" (scan-checked).
- R09 8.2.2–8.2.3, p.33, and footnote 25.
- R02 Annex F Part E, p.46.
- COM's no-rule search record on numeric timing and on naming the cause is adopted. Both are professional judgment.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.3 ("Approve public statements and replies to media | CMT chair; alternate COO if the chair is unreachable for 15 minutes"), s.11.1–11.4 and s.5.8. No conflict. The first release time comes from the external standard (PH01 s.1.4).

**Dispatch instruction**
- SCHEDULE: 09:00 (latest 09:30).
- Release depends on C2 (08:40), C1 (08:45, for the app banner only) and LC clearance (08:50).
- The authorities line depends on the Q02a call log. The statement is never held for HKMA approval.

==================================================================
**CROSS-ROLE CONFLICT RESOLUTION**
1. **Who declares Severity 1:** PH01 is silent. I declared at 08:00 as chair, and every role's assumption holds.
2. **Written legal hold:** SEC asked for it (B1) but LC's answer did not list it. I direct LC to issue it at 08:00 (PH01 s.17.1), by hand or phone cascade, not email. This does not change Q02a or Q02b.
3. **Mobile transfer submission:** decided under the Q01a override. It flows into COM's C2 fact-check and LC's "change in service status" trigger without changing their text.
4. **No other conflicts:** none found among SEC, LC and COM, or between PH01 and the external requirements. The terminal and email logs at 08:30, the no-email rule, the HKMA copy route and the balance-view dependency are consistent across all three answers.

**ORDER OF DEPENDENT ACTIONS (HKT)**
1. **08:00.** CEO declares Severity 1 and convenes the CMT for 08:30. SEC places the evidence hold and names the custodian. LC issues the legal hold and opens the deadline tracker. Compliance tests the standby device.
2. **08:00–08:15.** Pre-change capture (skipped if spread is active), then isolation and credential actions. These steps depend on each other and must happen in this order.
3. **By 08:30, in parallel and not dependent on steps 2 or 4.** LC calls the HKMA (Q02a). An LC officer calls the Commissioner (Q02b).
4. **Validation and CMT decisions.**
   - 08:15: forensic firm called in (depends on step 1).
   - 08:15–08:30: validation.
   - 08:20: Payments Operations confirms whether the app still accepts outbound instructions.
   - 08:30 CMT: I approve the customer audience and LC clears the in-app notice.
   - By 08:40: A5-bis executes if SEC verifies it.
5. **08:30 logs.** SEC logs the terminal release and email safety (feeds the Annex E route and all written channels). The second LC officer checks the tracker.
6. **08:40–08:50.** Facts confirmed (C2), channel trust logged (C1), frontline script and IVR live at 08:45, LC clears the text (C4).
7. **09:00.** Holding statement released; the authorities line goes in only if step 3 is logged. A1 calls and SMS start. SEC's first status report. Supplier request drafts due.
8. **At release.** The statement copy goes to the HKMA through LC, with an immediate HKMA update (PH01 s.5.8).
9. **09:30–11:00.** Group B tranches. Written HKMA summary by 10:00. CEO tells the Board chair by 10:00 (PH01 s.15.1).
10. **12:00 to Wed 18 Nov.**
    - 12:00: standby condition (default hold).
    - 12:30: HKMA update. 13:00: public update.
    - By 20:00, 16 Nov: s.28 outer limit (already met by step 3) and the Annex E internal target. 50% of the transfer tolerance is reached by 20:00 at the latest (earlier if the disruption began before 08:00); CEO tells the Board chair (PH01 s.4.3).
    - By 08:00, Tue 17 Nov: 100% of the tolerance; Board or Risk Committee convened (PH01 s.4.3 and s.15.2). CFO notifies the cyber insurer (PH01 s.12.4).
    - About 08:30, Wed 18 Nov: Annex E statutory limit. Then Annex F: target 27 Nov, statutory limit 30 Nov.
11. **Any failover or alternate processing.** It needs SEC's written clearance (PH01 s.8.2), then my activation and BCP declaration (PH01 s.4.4). LC then informs the HKMA promptly (R07 1.3.3; PH01 s.5.8).

No files were created.