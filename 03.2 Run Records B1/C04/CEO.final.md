CEO FINAL DECISION RECORD: C04 (Mon 16 Nov 2026, 18:00 HKT, H+10). Lan Tidal Bank, CMT chair.

All actions are simulated, for the facilitator to log. I received sealed answers for all six units. The facilitator handoffs went to LC (Q02a, Q02b and the C01 dispatch record) and to COM (Q03b and the status of later statements). SEC had none.

Before relying on them, I checked these sources myself:
- R01 s.22(1)–(3), PDF pp.33–34, and s.28 with Sch.6 (checked in C01).
- R07 1.3.3, p.5 ("periodic progress reports upon being notified until the final resolution of the crisis") and 4.3.2, p.11.
- R09 5.1.2, p.19, and fn 26, p.33.
- R05 p.2 (gain or regain access) and p.3.
- R02 7.2.4(a), p.34.
- R06 s.1.3, p.3.
- PH01 v1.0 in full.

**CEO record entries, 18:00**
1. **Board chair notices.** No supplied record shows my PH01 s.15.1 Board-chair calls (decided for 10:00 and 13:00) were made. I log them as "not evidenced". I phone the Board chair by 18:15 and cover:
   - the Severity 1 declaration, the extortion demand and the 80 confirmed exposures;
   - the expected 50% tolerance point at about 20:00 (earlier if the disruption began before 08:00), and the likely 100% point at about 08:00 Tue (PH01 s.4.3);
   - a request to pre-book a Board Risk Committee meeting for Tue morning. PH01 s.15.2 requires it to meet within 12 hours of 100%.

   I phone again at 20:00 with the activation and pilot status.
2. **Insurer.** The CFO confirms by 22:00 that the cyber insurer has been notified (PH01 s.12.4; limit 08:00 Tue).

==================================================================
**UNIT C04-Q10a: whether to use the secondary process, and payment priority**

- **Original answer reference:** sealed SEC answer for C04, "UNIT Q10a", conditional clearance C1–C7 and actions P1–P6.
- **Decision:** CONFIRM.

**Reason**
- **Clearance logic.** Recommending use, subject to SEC's written clearance, applies PH01 s.8.2 ("shares no hosts, accounts, keys or network path with any affected system"). The clearance has a default of HOLD (s.2.3) and also depends on the C03 closure test (C6), so the same credential cannot reach recovery.
- **Work that does not wait.** The register build and payroll call-backs start now, without waiting for clearance. Verification, not capacity, is the night-time bottleneck.
- **Worklist copy.** The gateway queue is only a hashed worklist copy, never the authority to pay. This is correct because the attacker issued commands on the gateway.
- **Pilot and order.** A pilot of at most 20 instructions (s.8.3), then processing in s.8.4 order, with a 10% urgent lane.
- **Authority line.** Clearance is SEC's; activation is mine (s.3). The fallback if clearance is refused is Board escalation, not proceeding anyway (s.4.3, s.15.2).
- **External support.** R06 s.1.3, p.3, requires that "disruptions to an AI's critical operations must not exceed its 'tolerance for disruption'". R07 4.3.2, p.11 (verified) allows "record reconstruction and verification, establishment of new controls".

**Final action and condition**
- C1–C7 and P1–P6 exactly as written.
- My activation rule as chair:
  - At about 19:15, I activate if SEC's written clearance is logged by 19:00, after consulting the Head of Payments Ops.
  - I record the BCP activation in the decision log with the time and the operation (PH01 s.4.4), and LC is told at once.
  - If SEC logs a HOLD, there is no activation. SEC re-checks every hour, and the tolerance consequence goes to the Board chair and the Risk Committee.

**Accountable owner**
- Clearance: SEC.
- Activation and BCP declaration: CEO, as CMT chair.
- Release of the worklist copy: SEC and LC jointly, with the forensic lead consulted. I direct LC to co-sign at 18:30.
- Register, operation and release: Payments Ops.
- Stop authority: SEC or the Head of Payments Ops (s.8.7).

**HKT time, deadline or trigger**

| Step | Time |
|---|---|
| Checks, register build and payroll call-backs | from 18:00 |
| Worklist copy released | 18:30 |
| Clearance or HOLD logged | 19:00 |
| Activation | about 19:15 |
| Pilot | about 19:15–20:15 |
| Full operation | from about 20:15 |
| Reconciliation | hourly |
| 50% of tolerance | about 20:00 |
| 100% of tolerance | about 08:00 Tue |

**Recipient and channel**
- Changes are made on the secondary-process hosts, firewalls and keys, and in the instruction register.
- Clearance, activation and gate results go in the decision log and the BCP activation entry.
- Communication is in the CMT room or on a phone bridge, never by corporate email unless email has been logged safe.

**Final external basis**
SEC Q10a "BASIS: EXTERNAL" items 1–5 are adopted unchanged:
- R06 s.1.3, p.3 (verified) and s.3.4, p.6.
- R07 definitions, p.3; 4.3.2, p.11 (verified); 3.2.2, p.8; 1.3.3, p.5 (verified).
- R02 7.2.4(a), p.34 (verified: "continue essential operation during disruptions").
- R05, p.1.

SEC's "no direct rule located" search record for the clearance criteria and the order within the queue is adopted.

Added for LC's register: R01 s.22(1) and (2)(c)–(d), pp.33–34 (verified). If the secondary process becomes "essential to the core function", the regulating authority must be notified "within 1 month". This is not urgent tonight; it goes into the PH01 s.18.4 register.

**Final internal basis**
Internal bank procedure, PH01 v1.0:
- s.3 (activation row);
- s.8.2–8.5 and s.8.7;
- s.2.3, s.4.3, s.4.4, s.6.1, s.9.1 and s.15.2.

No conflict found.

**Dispatch instruction**
- EXECUTE NOW: P1 and the C1–C7 checks.
- SCHEDULE: P2 at 18:30 (needs LC's co-signature); P3 at 19:00.
- HOLD activation (P4) until SEC's written clearance is logged.
- P5 runs only after activation. P6 runs only after a pilot with no unexplained difference.

==================================================================
**UNIT C04-Q10b: control for retried and duplicate payments**

- **Original answer reference:** sealed SEC answer for C04, "UNIT Q10b", D1–D9.
- **Decision:** CONFIRM.

**Reason**
The control applies PH01 s.8.6 in full and adds checks suited to the attack:
- **D1:** a single register, with each instruction released once only under a unique ID.
- **D4 (two checks before release):**
  - (a) the customer's intent, confirmed only by a bank-initiated call-back to a number on file;
  - (b) the status, confirmed from the ledger and an independent receiving-side record.

  If either check is incomplete, the instruction is held.
- **D2:** the customer's authenticated channel record is the source of truth, because gateway records may contain attacker commands.
- **D3:** "same amount, different beneficiary" is flagged for Fraud as a possible redirection scam.
- **D4(a) extra check:** a verification question not based on the exposed data, for the C03 exposed group.
- **D5:** in-flight items are treated as "status unknown" and held.
- **D6:** maker-checker release.
- **D7:** hourly reconciliation that stops all releases on any unexplained difference.
- **External support:** R09 5.1.2, p.19 (verified): "reconcile data file balances after transaction updates and to check the integrity of data transmitted between different systems".

**Final action and condition:** D1–D9 exactly as written. The control is in force before the pilot.

**Accountable owner**
- Register and release: Head of Payments Ops.
- Integrity conditions and stop authority: SEC.
- Flagged items: Fraud.
- Worklist copy: the custodian and LC.

**HKT time, deadline or trigger**
- In force before the pilot, at about 19:15.
- Reconciliation every hour of operation.
- Any trigger in D8 stops releases at once.

**Recipient and channel**
- The instruction register and the secondary-process controls.
- Customer call-backs go only to numbers on file.
- Counterparties are contacted only by verified call-back (PH01 s.14.2).

**Final external basis:** SEC Q10b "BASIS: EXTERNAL" items 1–3 are adopted:
- R09 5.1.2, p.19 (verified);
- R07 4.3.2, p.11 (verified);
- R05 p.1 and R09 8.2.1.

SEC's "no direct rule located" record for duplicates is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0, s.8.5, s.8.6, s.8.7, s.10.5 and s.14.2. No conflict found.

**Dispatch instruction:**
- EXECUTE NOW: build the register and put the control in force.
- No release from the secondary process happens until the control is in force and activation has occurred.

==================================================================
**UNIT C04-Q11a: review of the Commissioner (Cap. 653 s.28) record and next action**

- **Original answer reference:** sealed LC answer for C04, "UNIT Q11a", actions (a)–(f).
- **Decision:** CONFIRM.

**Reason**
LC's reading of the handoff is accurate:
- **Phone call by 08:30.** It was within the 12-hour limit of s.28(2)(a) and covered what s.28(2)(b)(ii) requires.
- **Annex E at 11:00.** It meets the 48-hour limit of s.28(3) (Sch.6 item 2).
- **Gaps.** Neither the call nor the filing has a receipt, a reference number or a call time on record. The C03 supplementary information was not sent.

LC's plan secures evidence before the 20:00 outer limit:
- it retrieves the bank's own records;
- it gets the Commissioner's confirmation by 18:45;
- at a 19:00 checkpoint it re-submits Annex E by 19:30 if needed, and falls back to a fresh phone notification before 20:00.

This applies PH01 s.5.5 ("LC saves the system's submission receipt ... If no receipt is shown, LC asks the recipient for one").

On the supplement:
- It goes by 19:30 under PH01 s.5.9 and R02 7.3.7(a).
- The miss is logged honestly.
- If SEC confirms the workspace is a separate critical computer system (CCS), the conditional new Annex E correctly applies s.28 to that CCS, with an outer limit of 24:00.

**Final action and condition:** (a)–(f) exactly as written. A BCP activation (Q10a) goes to the Commissioner as a further supplement at once (R02 7.3.4(c)).

**Accountable owner**
- Accountable: LC.
- Executing: a designated LC officer.
- SEC confirms the workspace's CCS status by 19:00.
- I am informed. No internal approval holds any filing (PH01 s.2.4).

**HKT time, deadline or trigger**

| Step | Time |
|---|---|
| Own evidence retrieved | 18:15 |
| Commissioner confirms | 18:45 |
| Checkpoint | 19:00 |
| Re-submission (if needed) and supplement | 19:30 |
| Statutory outer limit | 20:00 |
| Annex E for the workspace (if it is a separate CCS) | by 19:30; statutory limit 24:00 |
| Annex F | target 27 Nov; statutory limit 30 Nov |

**Recipient and channel**
- Commissioner of Critical Infrastructure (Computer-system Security).
- Confirmation by the verified CI telephone route.
- Annex E and supplements through the designated secured channel. The standby device is the fallback.

**Final external basis:** LC Q11a "Basis: external" is adopted:
- R01 s.28(2)(a), (2)(b)(ii), (3), (5) and Sch.6 items 1–3, pp.44 and 97 (verified in C01);
- R02 7.3.6(b), p.36, and 7.3.7(a), p.37 (verified).

LC's search record on "supplementary" is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0, s.5.5, s.5.9, s.2.3 and s.2.4. No conflict found; the gap was in carrying the procedure out.

**Dispatch instruction**
- EXECUTE NOW: (a).
- SCHEDULE: (b) at 18:45; (c) at 19:00, with re-submission only if receipt is unconfirmed; (d) at 19:30.
- The workspace Annex E runs only if SEC confirms it is a separate CCS.
- (e) is logged now; (f) is scheduled.

==================================================================
**UNIT C04-Q11b: review of the HKMA record and supervisory contact now**

- **Original answer reference:** sealed LC answer for C04, "UNIT Q11b".
- **Decision:** CONFIRM.

**Reason**
LC's review matches the handoff:
- reports and updates were made, but there are no receipts or HKMA reference;
- the route of the 10:00 written summary is unverified;
- the 09:00 statement is uncertain;
- no BCP activation has been recorded.

An 18:30 follow-up call ahead of the 20:30 scheduled update is justified. The tolerance is at risk, activation is imminent, customers are having trouble reaching the bank, and the record gaps need closing. R05 p.3 supports this: "The HKMA should be kept informed during the process".

The call also corrects the record on the 09:00 statement, checks the PCPD status (filing at once if there is no dispatch record) and arranges an immediate call on activation (R07 1.3.3). That is complete.

One point of record: the clearance-time figure given in item 3 is taken from SEC and Payments Ops. At 360 an hour after the 10% urgent lane, the queue takes about 11.7 hours from full operation, so it clears no earlier than about 08:00 Tue. This only fills a record field and changes no action, time or recipient.

**Final action and condition:** as written:
- the 18:30 call (items 1–6);
- a consolidated written update by 19:30 by the HKMA-confirmed route, never corporate email unless email has been logged safe;
- a phone call and written note at once on activation;
- updates at 20:30, 00:30 and 04:30, then 08:00 and 18:00, and at once on a status change, a statement, or 50% or 100% of tolerance.

The PCPD check means: LC confirms the PCPD dispatch record by 18:20. If there is none, LC faxes or hand-delivers the form by 18:45 and tells the HKMA the true status.

**Accountable owner**
- Accountable and executing: LC.
- Figures: Payments Ops and SEC.
- Public material and the 09:00 release status: COM, by 18:20.
- I am informed.

**HKT time, deadline or trigger:** call by 18:30; written update by 19:30; immediate call on activation (about 19:15); 20:30 and the times after it as above.

**Recipient and channel:** the HKMA banking supervision contact (from the printed Regulator Contact Register) by telephone; written follow-up by the route the HKMA confirms.

**Final external basis:** LC Q11b "Basis: external" is adopted:
- R05 pp.2–3 (scan-checked);
- R07 1.3.3, p.5 (verified, including "periodic progress reports");
- R09 8.2.5;
- R06 p.3.

LC's "no direct rule located" record on telling the HKMA of a tolerance breach is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0, s.5.8, s.4.4, s.4.3, s.5.7 and s.1.3. No conflict found.

**Dispatch instruction**
- EXECUTE NOW: the call by 18:30.
- SCHEDULE: the 19:30 written update and the 20:30 update.
- The activation call is triggered by Q10a P4.
- The PCPD filing is conditional on there being no dispatch record by 18:20.

==================================================================
**UNIT C04-Q12a: public service-status update**

- **Original answer reference:** sealed COM answer for C04, "Q12 a", conditions U1–U6 and the draft update.
- **Decision:** OVERRIDE.

**Reason**
COM's approach is kept: a self-contained update at 19:00 that does not depend on the uncertain 09:00 and 13:00 texts; an extra update at once on activation; then 22:00 and 07:00.

Three accuracy fixes:
1. **Capacity line.** Activation cannot happen before about 19:15 (Q10a), so U1 will fail at 18:45. COM's U2 line "We can currently process up to [400] checked payments an hour" would then be false in the 19:00 text. The capacity line is now tied to U1.
2. **Queue figure.** The figure includes retried instructions (SEC Q10b). The public text must not suggest that 4,200 separate payments will all be made.
3. **Branch hours.** These are now my decision (Q12b), listed only once confirmed live under U6.

Adding a condition that changes what is published counts as an OVERRIDE.

**Final action and condition**
COM's draft and U1–U6 stand, with these changes:
- **If U1 is not met:** "We are preparing a safe alternative way to process waiting payments. Once it starts it can handle up to [400] checked payments an hour, and we will tell you as soon as it starts."
- **If U1 is met:** COM's [NEW] activation lines and "We can currently process up to [400] checked payments an hour".
- **Queue line (if U2 is met):** "About [4,200] payment instructions are waiting, including some repeated instructions; each payment will be made only once."
- **No completion time** unless Payments Ops confirms it from the register (PH01 s.11.4).
- **Help routes:** "Getting help" lists only routes Operations has confirmed live (U6). That includes the branch hours I decided under Q12b.
- **Everything else as written:** the retry and duplicate wording, the data lines under U4, the ransom line only under U5, fees and losses, and the next update times.
- **Activation:** if activation happens after 19:00, an extra update goes at once with the U1-met lines.

**Accountable owner**
- COM drafts and publishes.
- I approve (the COO is alternate after 15 minutes).
- LC clears. SEC and Operations fact-check.
- Figures: Payments Ops.

**HKT time, deadline or trigger**

| Step | Time |
|---|---|
| Channel audit | 18:05 |
| Verifications | 18:45 |
| Approval | 18:50 |
| Publish | 19:00 |
| Extra update | at once on activation |
| Next scheduled updates | 22:00, then 07:00 Tue |
| Unscheduled update | at once on any service change |

**Recipient and channel**
- Public: website status page, press release, official social media, app banner (only if SEC has logged it trusted), IVR and branch notices.
- Staff: script v4.
- HKMA: a copy goes from COM to LC to the HKMA, with a receipt requested.

**Final external basis**
- COM Q12a "Basis: external" is adopted:
  - R05 p.2 (verified: "gain or regain access to the relevant banking services or to protect their interests");
  - R05 p.3;
  - R09 8.2.2 and fn 26, p.33 (verified: "any estimated service resumption time");
  - R07 1.3.3 and 4.7.1.
- On the corrections: R09 8.2.2, p.33, requires messages that are "consistent and up-to-date". Stating a capacity as current before activation would breach that.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.11.2 ("Each update states what is confirmed, what is being verified, what customers can do and when the next update is due");
- s.11.4 (figures only from an owner's record);
- s.8.4, s.8.6(a), s.13.1, s.13.2 and s.5.8.

No conflict found.

**Dispatch instruction**
- SCHEDULE: publish at 19:00. This depends on U1–U6 by 18:45 and my approval at 18:50.
- The service lines are never held; unverified lines take their defaults.
- The activation update is triggered by Q10a P4.

==================================================================
**UNIT C04-Q12b: reaching customers who cannot use the usual channels**

- **Original answer reference:** sealed COM answer for C04, "Q12 b", items 1–6 and conditions R1–R3.
- **Decision:** OVERRIDE.

**Reason**
COM's design is kept:
- outbound contact first;
- an IVR call-back option using existing numbers, with no new number or link;
- calls returned only to the number on file;
- branch-phone overflow diverted;
- a priority order for call-backs;
- the 24-hour fraud line;
- the 10% urgent lane and the FAQ.

Three changes:
1. **SMS wording.** The SMS says "We will call you ... only if we need to confirm a duplicate". That is inaccurate. PH01 s.8.5 requires call-back confirmation of every payroll batch, and SEC D2 may also trigger calls. Customers told "only for duplicates" could treat a genuine bank call as a scam, or a scam call as genuine.
2. **SMS audience.** COM drew the audience from the instruction register, which is built from the gateway worklist copy. That copy may contain attacker-created instructions (SEC Q10b D2). Telling a customer "your payment is waiting" for an instruction they never made would mislead them.
3. **Branch and contact-centre hours.** These were left to me and the Head of Operations, and I decide them here.

**Final action and condition**
1. **SMS alert, audience approved by me now (condition R1).**
   - Audience: customers whose queued instruction Payments Ops has matched to their authenticated channel record (D2).
   - Unmatched instructions get no SMS and go to Fraud and SEC for review.
   - Tranches: the first at activation or 19:15, then as matching completes.
   - Text: "Lan Tidal Bank: Your payment of [date] is waiting to be processed. Please do not resubmit it. We may call you on the number in our records to confirm it before we pay it. We will never ask for your password, PIN or one-time password, or ask you to make a new transfer. Fees caused by the disruption are waived."
   - No link and no amount.
2. **Call-back service live by 18:30, provided SEC clears R2.** If R2 is not met, the default is call-back requests through branches and relationship managers only. The rest as written:
   - priority order (payroll and items due today or tomorrow, then the 80 exposed customers, then hardship cases, then everyone else);
   - urgent call-backs by 22:00, all others within 24 hours;
   - a case reference for every request;
   - contact details changed during the incident checked by Fraud.
3. **Hours (CEO decision).**
   - All eight branches stay open until at least 20:00 tonight, or later where a later closing time was set under my C02 decision.
   - Branches open at 08:00 on Tue 17 Nov.
   - The contact centre stays open until at least 24:00 tonight and reopens at 07:00 Tue.
   - The fraud line stays open at all times.
   - Back-office staff are moved into the call-back team, using script v4.
   - Operations confirms each item live before COM announces it (U6).
4. **As written:** the urgent referral log feeding the 40-an-hour lane, payment-made SMS from Payments Ops, relationship-manager calls combined with the duplicate check (one consolidated contact, PH01 s.10.6), the static FAQ, and hourly contact-centre reports to the CMT.

**Accountable owner**
- SMS audience: CEO, after consulting LC, SEC and the DPO.
- Wording, scripts and FAQ: COM, with LC clearing.
- IVR, diversion, staffing and hours: the Head of Operations and the contact-centre head.
- Matching, referrals and payment SMS: the Head of Payments Ops.
- Contact-detail checks: Fraud.
- R2 and R3 trust checks: SEC.

**HKT time, deadline or trigger**

| Step | Time |
|---|---|
| IVR call-back and branch-phone diversion | 18:30 (after R2) |
| Script v4 | 18:45 |
| Routes announced in the update | 19:00 |
| SMS tranche 1 | at activation or 19:15, then further tranches |
| Urgent call-backs complete | 22:00 |
| Contact centre open until | at least 24:00 |
| Branches open | 08:00 Tue |

**Recipient and channel**
- Customers: SMS with no link; outbound calls to numbers on file; the IVR option on existing published numbers; branches; relationship managers; the app secure inbox only if SEC logs it trusted (R3).

**Final external basis**
- COM Q12b "Basis: external" is adopted:
  - R05 p.3 (scan-checked: "customer service hotlines and extended office hours of branch services");
  - R09 fn 24, p.32, and 4.4.2, p.17;
  - R07 5.1.4 (by analogy);
  - R14b p.8;
  - R02 7.2.3(e).
- On the audience fix: R09 5.1.2, p.19 (verified), on checking "the integrity of data transmitted between different systems". Customer messages must rest on verified instruction data.
- COM's "no direct rule located" record on call-back targets, branch hours and call-back queue order is adopted. The hours are professional judgment, sized to doubled call volumes and the overnight payroll processing.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.13.6, s.8.4, s.8.5 ("Payroll batches are confirmed with the SME's authorised contact by call-back to a number already on file");
- s.10.2, s.10.5, s.10.6 and s.3 (customer-notice audience row).

No conflict found.

**Dispatch instruction**
- EXECUTE NOW: the IVR and diversion once R2 is cleared, plus staffing and hours.
- SCHEDULE: the SMS tranches. They depend on D2 matching and on activation (or 19:15).
- The secure-inbox route stays on HOLD unless R3 is cleared.

==================================================================
**ORDER OF DEPENDENT ACTIONS (HKT)**

1. **18:00–18:15**
   - SEC starts the C1–C7 checks.
   - Payments Ops starts the register and payroll call-backs.
   - LC retrieves the Commissioner and HKMA evidence.
   - COM audits the channels (18:05).
   - I phone the Board chair (18:15).
2. **By 18:20**
   - COM confirms to LC whether the 09:00 statement was released.
   - LC checks the PCPD dispatch record. If there is none, the PCPD form goes by fax or hand by 18:45.
3. **18:30**
   - SEC and LC jointly release the worklist copy. This allows D2 matching and the SMS audience.
   - LC makes the HKMA call (Q11b).
   - The IVR call-back option goes live after SEC's R2 check.
4. **18:45–18:50**
   - LC gets confirmation from the Commissioner (Q11a b).
   - U1–U6 and R1–R3 are verified.
   - Script v4 is issued.
   - I approve the update and the SMS audience; LC clears them.
5. **19:00**
   - SEC logs its clearance or a HOLD (Q10a P3).
   - The public update is published with the "not yet started" wording, and a copy goes to the HKMA through LC.
   - LC's Commissioner checkpoint.
   - SEC confirms whether the workspace is a separate CCS.
6. **About 19:15 (only if clearance is logged)**
   - I activate the secondary process and declare BCP activation.
   - LC is told at once and phones the HKMA at once (R07 1.3.3).
   - COM issues an extra public update.
   - SMS tranche 1 goes.
   - The pilot of at most 20 instructions starts, with the Q10b control in force.
7. **19:30**
   - LC sends the Commissioner supplement, including activation if it has happened.
   - LC re-submits Annex E and files the workspace Annex E, only if needed.
   - LC sends the consolidated written update to the HKMA.
8. **20:00**
   - The s.28 outer limit. The evidence of notification is secured, or the fallback phone notification is made before this time.
   - 50% of tolerance: I phone the Board chair.
   - Branches stay open until at least 20:00.
9. **About 20:15:** if the pilot reconciles, full operation starts, with hourly reconciliation and the stop triggers live.
10. **20:30 to 24:00**
    - HKMA update with the pilot result (20:30).
    - Public update, urgent call-backs complete, LC's posture note (C02) and my scope decision (C03), all at 22:00.
    - The contact centre stays open until at least 24:00.
11. **Overnight to Tue 08:00**
    - HKMA updates at 00:30 and 04:30.
    - The attacker's deadline passes at 02:00. If data is published, the C03 widening triggers apply.
    - Public update at 07:00.
    - At about 08:00, 100% of tolerance: I convene the Board or its Risk Committee (meeting within 12 hours).
    - Branches open at 08:00.
    - HKMA update at 08:00.
    - The CFO's insurer notice must be confirmed by 08:00.
12. **Within 1 month:** LC assesses the secondary-process activation and each change to a CCS for notice under R01 s.22 (PH01 s.18.4).

No files were created.