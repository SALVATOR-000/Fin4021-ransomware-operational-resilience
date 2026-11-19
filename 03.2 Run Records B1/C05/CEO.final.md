CEO FINAL DECISION RECORD: C05 (Tue 17 Nov 2026, 08:00 HKT, H+24). Lan Tidal Bank, CMT chair.

All actions below are simulated, for the facilitator to log. I received sealed answers from SEC, LC and COM for all six units. Facilitator handoffs went to LC (Q05a and Q05b) and COM (Q08b and Q09a); SEC had none.

Sources I checked myself:
- R09 4.3.1–4.3.2 and fn 12, PDF pp.16–17.
- R10 s.58(1)(a) and (2), pp.117–119.
- R03 6.2.20(b)(i), p.17.
- R02 p.18.
- R08 4.2.4, p.18.
- Citations already checked on earlier cards, including R11 pp.4–8, R16b pp.2–3, R16c s.25A and R05 pp.1–3.
- PH01 v1.0.

**CEO record entries at 08:00**

1. **Lapse: the 80 customers were never verifiably notified.** The handoffs show no evidenced call, SMS or letter to batch C03-B1. COM's default when LC clearance is not logged was "hold and escalate", and no clearance was logged. This is the third card on which a missing LC clearance has silently held a customer or public action (C01 Q03b, C02 script v2, C03 Q09a).
   - I log it as a lapse against R16b p.3, which asks banks to "notify the affected customers as soon as practicable".
   - LC reports the true notification status in its HKMA and PCPD updates.
2. **New clearance rule, from now on.** Every LC clearance is given live in the CMT room at a fixed time. The second LC officer is the backup. The decision-log keeper records it at that moment, and I check the log at each clearance time.
3. **Tolerance breach and Board.** The 24-hour tolerance for transfers and payroll is at 100%: it was reached by 08:00 at the latest, earlier if the disruption began before 08:00.
   - PH01 s.4.3 requires me to convene the Board; I convene the Board Risk Committee for 19:00 today. PH01 s.15.2 sets the latest time at 20:00.
   - The Board paper is circulated at 18:30 and follows PH01 s.15.3.
   - Contributions: SEC gives recovery status by 18:00. LC writes the posture and authorities sections, with legal advice in a separate privileged section. COM gives notification status. The CFO gives the remediation running total under s.13.7.
   - Decisions the Board will be asked for:
     - note the payment posture;
     - possibly narrow the recovery scope, for example to payroll only (PH01 s.9.3);
     - revise the incident total if monitoring and loss costs require it.
   - I phone the Board chair at 08:15 about the mirror, the fake page and the meeting.

==================================================================
**UNIT C05-Q13a: recovery candidate, integrity and separation**

- **Original answer reference:** sealed SEC answer for C05, "UNIT Q13a". This covers the candidate choice, R0, integrity checks I1–I8 and separation checks S1–S7.
- **Decision:** CONFIRM.

**Reason**
- **Candidate order.** SEC tests candidate (1) first: a new build from trusted media, using only data from the immutable backup, in an isolated environment. The standby is tried only if (1) fails, and the gateway is never repaired in place. That is exactly PH01 s.9.1.
- **Backup timing (I1).** An undetermined order of events is not treated as "pre-incident". This applies PH01 s.6.4 correctly, because the attacker may have been present before the first evidence of activity.
- **What comes from the backup (I5).** Only data is restored. Binaries come from trusted media obtained through a channel that does not depend on the compromised vendor.
- **Separation.** New keys, rebuilt accounts and no vendor path (S1–S7, I7). This keeps the new build away from the compromise.
- **Default if checks fail.** The default is HOLD, or the next-earlier immutable restore point (PH01 s.2.3). Meanwhile service continues only on the alternate process, and only if its clearance is current and its reconciliation ties (PH01 s.9.3).
- **External support.** R03 6.2.20(b)(i), p.17 (verified), on a backup "physically disconnected from the CCS". R08 4.2.4, p.18 (verified), on separate test environments.

**Final action and condition**
- Candidate choice, R0, I1–I8, S1–S7 and the four-item condition exactly as written.
- I direct LC to co-sign the R0 backup working-copy release at 08:30. PH01 s.3 makes evidence release a joint SEC and LC decision.
- Recovery status goes into the 18:30 Board paper.

**Accountable owner**
- SEC is accountable for integrity and separation, which is one item of the PH01 s.9.3 gate.
- Build: IT Ops recovery team. Indicator scan: forensic firm. Copy: evidence custodian.
- Consulted: Head of Payments Ops.
- Production decision: me, after the gate. The Board may narrow the scope.

**HKT time, deadline or trigger**

| Step | Time |
|---|---|
| R0 working copy released | 08:30 |
| Checks I1–I4 and S1–S7 | 09:00–12:00 |
| Backup suitability condition (default HOLD) | 12:00 |
| Build (I5–I8) | 12:00–16:00 |
| Recovery input to the Board paper | 18:00 |

Every step is gate-based. Passing a time never releases the gate.

**Recipient and channel**
- Work is done in the isolated recovery environment. It is recorded in the change record and the evidence register.
- Decisions go in the decision log, made in the CMT room or on the phone bridge.

**Final external basis**
- SEC Q13a "BASIS: EXTERNAL" items 1–7, adopted:
  - R03 6.2.20(b)(i), p.17 (verified: "a backup copy that is physically disconnected from the CCS");
  - R04 4.3, p.8;
  - R08 4.2.4, p.18 (verified);
  - R07 4.6.2 and 4.3.3;
  - R01 Sch.3 Pt 2 item 5;
  - R14b p.5;
  - R03 6.1.1, p.11.
- SEC's "no direct rule located" search record is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.9.1, s.9.3, s.6.1, s.2.3, s.7.5, s.18.4 and s.3.
- No conflict found.

**Dispatch instruction**
- EXECUTE NOW: choose candidate (1); hold the standby and the original gateway.
- SCHEDULE: R0 at 08:30 (needs LC's co-signature); checks from 09:00.
- HOLD: any production use, until the PH01 s.9.3 gate is passed.

==================================================================
**UNIT C05-Q13b: offline reconciliation before production**

- **Original answer reference:** sealed SEC answer for C05, "UNIT Q13b": preconditions (i) and (ii), checks RC1–RC8, the pass mark and the gate.
- **Decision:** CONFIRM.

**Reason**
- **Before any production data is used.** SEC records de-sensitisation and the information owner's prior approval in the test record. This is R08 4.2.4, p.18 (verified): "Production data should not be used in development or acceptance testing unless the data has been de-sensitised ... and prior approval from the information owner has been obtained". It also matches PH01 s.9.2.
- **Tokenisation.** Deterministic tokenisation keeps records joinable while protecting personal data (DPP4(1)).
- **Coverage of the checks.**
  - Restore completeness and a point-in-time match.
  - Classification of everything since the backup, with unknown items held.
  - Tie-out against what the alternate process has released, to prevent paying twice at cutover.
  - Duplicate and replay rejection, and static data checks.
  - A harness-only end-to-end run and payroll totals.
- **Pass mark.** Zero unexplained differences on the full set; a sample is recorded only as a sample. This is PH01 s.9.2 verbatim. Production still needs every item of the s.9.3 gate, then the s.9.4 stages.

**Final action and condition:** as written.

**Accountable owner**
- SEC: check design, test record and pass/fail.
- Execution: Payments Ops and the IT Ops recovery team.
- Data approval: the payments information owner.
- Production: me, after the gate.

**HKT time, deadline or trigger**
- Approval and de-sensitised data ready by 15:00.
- RC1–RC8 from 16:00 to 22:00.
- The gate review is held only after a logged pass.

**Recipient and channel:** the isolated recovery environment, the test harness and the test record. Nothing touches a live payment network.

**Final external basis:**
- SEC Q13b "BASIS: EXTERNAL" items 1–5, adopted: R08 4.2.4, p.18 (verified); R03 6.2.22(c), p.17; R09 5.1.2, p.19 (verified at C04); R07 4.3.2, p.11 (verified at C04); R14b p.2; R10 DPP4(1).
- SEC's "no direct rule located" record is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.9.2 ("One unexplained difference is a fail. A sample result is recorded as a sample, not as a pass of the whole set"), s.8.6 and s.9.3–9.5.
- No conflict found.

**Dispatch instruction**
- SCHEDULE: preconditions by 15:00; RC1–RC8 from 16:00.
- HOLD: testing with any data set that lacks either precondition entry, and the gate review until a pass is logged.

==================================================================
**UNIT C05-Q14a: payment posture and recorded commitments**

- **Original answer reference:** sealed LC answer for C05, "UNIT Q14a".
- **Decision:** CONFIRM.

**Reason**
- **Posture kept.** The no-payment, no-contact posture stays (PH01 s.12.1). Gates (a)–(g) are all still unconfirmed and no departure has been put to the Board.
- **Why it stays.** Publication of 320 records shows that payment would not buy confidentiality. The immutable backup gives a recovery path that does not depend on the attacker.
- **Commitments to the attacker.** The handoff records none. LC correctly sends no "we will not pay" message, because that would itself be contact barred by s.12.3.
- **Internal commitments stay in force:**
  - the Treasury hold;
  - the no-reply instruction;
  - the "verified present fact" rule for public lines on payment.
- **Gaps LC closes:**
  - The posture notes recorded no content, so LC reissues a written note by 10:00.
  - Insurer receipt: the CFO obtains the insurer's written acknowledgement and position by 10:00.
  - The Cap. 455 disclosure cannot be verified. SEC and LC check the demand for a payment destination by 09:00. If one is named and no disclosure is logged, LC makes a late disclosure now and logs the reason. This applies R16c s.25A(1), p.83, "as soon as it is reasonable".
- **Board.** Revised review triggers are added, and the Board notes the posture at 19:00.

**Final action and condition:** items 1–5 exactly as written. I hold the posture day to day and present it at the 19:00 Board Risk Committee.

**Accountable owner**
- Board: the policy and any departure from it.
- CEO: the posture day to day, and convening the Board.
- LC: the recommendation, the gates, the note and any disclosure.
- CFO and Treasury: the hold and the insurer.
- SEC: the demand evidence check.

**HKT time, deadline or trigger**

| Step | Time |
|---|---|
| Decision logged | 08:15 |
| Demand check | 09:00 |
| Posture note and insurer position | 10:00 |
| Board Risk Committee | 19:00 (limit 20:00) |
| Posture reviews | 08:00 and 18:00 daily, and at once on any listed trigger |

**Recipient and channel**
- Decision log.
- Treasury in writing through the CFO.
- If a disclosure is triggered, a police officer through the internal disclosure procedure.
- The Board paper through me.

**Final external basis:**
- LC Q14a "Basis: external", adopted: R16c s.25A(1), (2)(a) and (5), pp.83–84 (verified at C02); R16d s.8(a), p.20 (verified at C02).
- LC's "no direct rule located" record on an HKMA ransom position is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.12.1, s.12.2, s.12.3, s.11.3 and s.15.2–15.3.
- The s.12.2 disclosure gap noted at C02 is still resolved in favour of Cap. 455.

**Dispatch instruction**
- EXECUTE NOW: log the decision.
- SCHEDULE: the 09:00 check and the 10:00 note.
- HOLD: every payment step until the Board decides.
- NO ACTION: towards the attacker.

==================================================================
**UNIT C05-Q14b: law enforcement referral and accompanying evidence**

- **Original answer reference:** sealed LC answer for C05, "UNIT Q14b".
- **Decision:** OVERRIDE (narrow: timing and clearance of the platform report only).

**Reason**
- **Adopted from LC:**
  - an updated, formal CSTCB referral with its own reference, because 16 Nov has no case reference on record;
  - the phone call by 08:30 and the written referral with evidence by 12:00;
  - evidence tiers A, B and C;
  - the PH01 s.16.1 reading: Police disclosure goes under a covering letter and is recorded under PH01 s.1.3. R09 4.3.2 requires a Police report and R10 s.58(2) covers the crime exemption.
- **Conflict with COM.** COM files the platform impersonation report at 08:15 (Q15b). LC starts all removal requests "From 08:30" with "LC clears the legal wording". The difference matters because the phishing page is live. R09 4.3.2, p.17 (verified), says "AIs should make attempts to remove the fake or suspicious items where practicable", and fn 12 stresses speed.
- **Resolution.**
  - The platform's standard impersonation report is a factual report with no customer data and no bespoke legal wording. COM files it at 08:15.
  - The host, registrar and mirror removal requests use LC-cleared wording at 08:30, as LC wrote.

**Final action and condition**
1. **By 08:30**, LC phones CSTCB. LC reports the fake page and the mirror as urgent, confirms or obtains the case reference, and asks for the Police view on takedowns and warning wording. The contact is recorded under PH01 s.5.5.
2. **Takedowns.**
   - 08:15: COM files the platform impersonation report through the official account's reporting tool.
   - 08:30: SEC sends the host, registrar and mirror requests with LC-cleared wording.
   - Staff never visit the links; SEC captures them under PH01 s.6.6.
3. **By 12:00**, the written referral goes with the evidence package.
   - Tier A: no personal data.
   - Tier B: minimised personal data, preferably on Police request.
   - Tier C: withheld (privileged advice, originals, the full workspace).
   - Release is decided by LC and SEC jointly, with the DPO consulted. The custodian delivers it on encrypted media or by bank-hosted transfer, with a SHA-256 manifest. It is logged in the evidence register and the data release record.
4. **HKMA.** LC reports the scam to the HKMA immediately after COM's press release (R09 fn 12).

**Accountable owner**
- LC decides the referral; I am informed.
- LC and SEC release the evidence jointly, consulting the DPO and the forensic lead.
- The custodian delivers it.
- COM files the platform report.

**HKT time, deadline or trigger**

| Step | Time |
|---|---|
| Platform report | 08:15 |
| Phone call; host, registrar and mirror requests | 08:30 |
| Written referral and evidence | 12:00 |
| HKMA report | immediately after the 09:00 press release |

**Recipient and channel**
- Police CSTCB: telephone, then a written referral with the encrypted package.
- The platform: its reporting tool.
- Hosts and registrars: written requests.
- HKMA: its confirmed route.

**Final external basis**
- LC Q14b "Basis: external", adopted:
  - R09 4.3.2, p.17 (verified, "report the matter to the Hong Kong Police Force");
  - R04 2.4 and fn 1, p.4;
  - R11 pp.4 and 7;
  - R10 s.58(2), p.119 (verified: exempt from DPP3 where use is for crime purposes and applying DPP3 "would be likely to prejudice" them);
  - R16c s.25A(3)(a), p.83.
- New basis for the platform-report timing: R09 4.3.2, p.17, and fn 12 (verified: "as soon as practicable after they become aware of the scams").

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.3 (Police row; third-party data row), s.6.3, s.6.6 and s.1.3.
- Conflict: s.16.1 conflicts with the external requirement. It is resolved as LC proposed and recorded in the decision log.

**Dispatch instruction**
- EXECUTE NOW: the platform report (08:15) and the Police call (08:30).
- SCHEDULE: host, registrar and mirror requests at 08:30 (they depend on LC's wording); the written referral by 12:00 (it depends on the joint LC/SEC release and the DPO consultation).

==================================================================
**UNIT C05-Q15a: notifying newly verified affected customers**

- **Original answer reference:** sealed COM answer for C05, "Q15 a": batches C05-B2 and C03-B1, conditions M1–M5 and the proposed action under "Conflict".
- **Decision:** CONFIRM.

**Reason**
- **Batch B2.** COM's independent recommendation to send today from 09:00 is adopted. B2 is the 240 customers in the mirror who are not among the 80, plus any B1a individual SEC confirms by 08:45.
- **Batch B1 (the original 80).** No delivery is evidenced, so each gets one consolidated notice covering the original facts and the publication. This applies PH01 s.10.6: "A customer with no evidenced delivery gets one consolidated notice".
- **Why the notice is justified now.** The data is public, HKID numbers are sensitive and a scam is running. This meets R11 p.8 ("as soon as practicable ... regardless of the progress of any internal investigation") and R16b p.3.
- **The clearance conflict.**
  - COM identified it correctly. PH01 s.2.3 lets LC's text clearance hold a notice with no time limit, which defeats the external "as soon as practicable" standard. PH01 s.1.3 says the external requirement prevails.
  - I select COM's stated branch. LC clears in a fixed slot at 08:45, with the second LC officer as backup.
  - If no clearance is logged by 09:00, COM records the conflict and tells me and LC. I then direct release of the minimum notice (SEC-verified facts plus protective advice), with LC's review running alongside.
- **Rest of the workspace.** COM proposed a re-review: DPO and LC at 08:30, my decision by 10:00. This is adopted as written.

**Final action and condition**
- As written: batches, channels, core notice, call script, no-link SMS, conditions M1–M5 and the timing.
- I approve the B1 and B2 audience at 08:30, after consulting LC, SEC and the DPO.
- Any Police request about timing is logged and considered by LC and me. No delay is planned, because the data is already public.
- At 10:00 I decide the rest of the workspace by applying the decision rule adopted at C03, LC trigger (v): if SEC cannot bound the export, the batch widens to every record that session could reach.
  - SEC reports by 09:30 whether the 240 appear in the export logs.
  - If they do not, and SEC cannot identify a bounded path, the remaining records become a precautionary batch, C05-B3. They are told their information "may have been accessed; not confirmed", by letter and no-link SMS, using COM's ready template within two hours.
  - Any monitoring offer beyond PH01 s.13.5 goes to the 19:00 Board, because of the cost limit in s.13.7.

**Accountable owner**
- COM sends and keeps the register.
- I approve the audience and sign.
- LC clears, with the second LC officer as backup.
- SEC confirms the fields for each customer. Fraud and Operations confirm their own facts.
- Executed by the notification team (16 callers), Fraud, Operations and the courier.

**HKT time, deadline or trigger**

| Step | Time |
|---|---|
| Register check | 08:05 |
| Audience approved; scope re-review begins | 08:30 |
| LC clearance slot; SEC confirms the 320 list and fields | 08:45 |
| Default point if no clearance is logged | 09:00 |
| Calls start | 09:00 |
| My decision on the rest of the workspace | 10:00 |
| First attempts done; SMS to those not reached | 12:00 |
| Register summaries to LC | 13:00 and 18:00 |
| Letters for all 320 with the courier | 14:00 |
| Second call attempt | 17:00 |
| Visits to anyone not reached | 18 Nov |

**Recipient and channel:** the 320 individuals.
- Personal call with a call-back offer.
- No-link SMS to those not reached.
- Courier letter.
- Secure inbox only if SEC logs it trusted.
- No email and no HKID numbers.

**Final external basis:** COM Q15a "Basis: external", adopted:
- R11 pp.4, 5, 7 and 8 (verified);
- R16b pp.2–3 (verified);
- R05 p.1 (scan-checked).

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.10.3, s.10.4(a), (c) and (d), s.10.5, s.10.6, s.13.5 and s.3.
- Conflict: s.2.3, with no time limit on the hold, against R11 p.8 and R16b p.3. It is resolved under s.1.3 as above and recorded in the decision log.

**Dispatch instruction**
- SCHEDULE: calls at 09:00.
- Dependencies: audience approval (08:30), clearance or the 09:00 default, M3 field confirmation, and the M5 contact check for each customer.
- B3 runs only on my 10:00 decision.

==================================================================
**UNIT C05-Q15b: warning about the fake verification page**

- **Original answer reference:** sealed COM answer for C05, "Q15 b".
- **Decision:** OVERRIDE.

**Reason**
- **Adopted from COM:**
  - The page is described by its pattern only. The URL, QR code, handle and mirror location are never published; naming the platform is acceptable.
  - The bank states its "we never ask" rules.
  - The warning goes at 09:00 on every channel.
  - A no-link SMS and push alert go to all customers.
  - The scam is reported to the HKMA immediately after the press release.
  - The 320 data line is confirmed from SEC's record (PH01 s.11.4).
- **Change 1: a clearance default.** COM's Q15b has no default if LC's clearance is not logged. That gap held the C01–C03 statements. R09 fn 12 expects scam press releases "as soon as practicable". I add the same fixed-slot default as Q15a.
- **Change 2: removal-request timing.** The host and registrar requests move from 08:15 to 08:30, with LC wording, to match the Q14b resolution.

**Final action and condition**
- COM's actions and texts as written, including the public update, the SMS and push alert, and staff script v5.
- **Takedowns.** The platform impersonation report goes at 08:15. The host, registrar and mirror requests go at 08:30 with LC wording.
- **Approval and clearance.**
  - I approve the update and the all-customer SMS and push audience at 08:30.
  - LC clears live between 08:30 and 08:45, with the second LC officer as backup. SEC fact-checks.
  - If no clearance is logged by 08:55, I direct release at 09:00 of only the scam warning and the data line, using SEC-verified facts and PH01 fixed positions. LC reviews in parallel and any correction goes in the 13:00 update. The conflict is recorded under PH01 s.1.3.
- **Lines included only if logged:** "reported to the platform and the Police".

**Accountable owner**
- COM publishes.
- I approve (the COO is alternate after 15 minutes).
- LC clears; SEC fact-checks.
- SEC captures the page and blocks it in bank channels.
- COM's social team monitors and never engages the fake account.
- LC reports to the HKMA.

**HKT time, deadline or trigger**

| Step | Time |
|---|---|
| Capture | 08:05 |
| Platform report | 08:15 |
| Approval and removal requests | 08:30 |
| Clearance | by 08:45 |
| Default point if no clearance is logged | 08:55 |
| Publish | 09:00 |
| HKMA report | immediately after release |
| All-customer SMS and push | 09:30–11:00, in tranches |
| Next update | 13:00 |

**Recipient and channel**
- Public: website status-page banner, press release, a pinned text-only social post, app banner and in-app notice (if trusted), IVR and branch notices.
- All retail and SME customers: no-link SMS and push.
- Staff: script v5.
- HKMA: through LC.

**Final external basis**
- COM Q15b "Basis: external", adopted:
  - R09 4.3.1, p.16 (verified: "prominently displayed ... through multiple effective channels");
  - R09 4.3.2, p.17, and fn 12 (verified);
  - R09 4.4.2–4.4.3.
- New basis for the default: R09 fn 12, p.17 (verified): "AIs are expected to issue their press releases as soon as practicable after they become aware of the scams".
- COM's "no direct rule located" record on publishing identifiers is adopted. The pattern-only warning is professional judgment.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.10.2, s.6.6, s.3, s.11.3, s.11.4, s.5.8 and s.1.3.
- The s.2.3 hold conflict is resolved as in Q15a.

**Dispatch instruction**
- EXECUTE NOW: the capture and the platform report.
- SCHEDULE: removal requests at 08:30; publication at 09:00 (it depends on approval and on clearance or the 08:55 default); SMS tranches from 09:30.

==================================================================
**ORDER OF DEPENDENT ACTIONS (HKT)**

1. **08:00–08:05**
   - SEC selects candidate (1) and holds the standby and the gateway.
   - SEC captures the page and the mirror.
   - COM checks the register.
   - LC gives the HKMA an update at once on the publication and the 240 (PH01 s.5.8).
2. **08:15**
   - I log the posture, phone the Board chair and convene the 19:00 Board Risk Committee.
   - COM files the platform impersonation report.
   - SEC and LC begin checking the demand for a payment destination.
3. **08:30**
   - LC phones the Police (CSTCB).
   - LC-worded removal requests go to the host, registrar and mirror.
   - SEC and LC co-sign the backup working copy (Q13a R0).
   - I approve all audiences and the public update.
   - The DPO and LC begin the scope re-review.
4. **08:45:** LC clearance slot, with the second LC officer as backup. SEC confirms the 320 list and each customer's fields.
5. **08:55–09:00:** if no clearance has been logged, I direct release of the minimum texts (conflict recorded under PH01 s.1.3).
6. **09:00**
   - Public warning and data update.
   - Calls to batches B1 and B2 start.
   - Staff script v5.
   - The demand-check result: a Cap. 455 disclosure if a payment destination is named.
7. **Immediately after release:** LC reports the scam to the HKMA.
8. **09:00–12:00**
   - SEC runs checks I1–I4 and S1–S7.
   - 09:30: SEC reports on the export logs, feeding my 10:00 scope decision (B3 if the export cannot be bounded).
   - 09:30–11:00: all-customer SMS.
   - 10:00: LC's posture note and the insurer's position.
9. **12:00**
   - Written Police referral and evidence package.
   - LC's PCPD update, giving the true notification status.
   - Backup suitability condition.
   - First call attempts complete.
   - LC sends the Commissioner supplementary information today.
10. **12:00–22:00**
    - Build (12:00–16:00).
    - Public update and register summary (13:00).
    - Letters with the courier (14:00).
    - Test preconditions (15:00).
    - RC1–RC8 (16:00–22:00).
    - Second call attempt (17:00).
    - SEC recovery input (18:00).
    - Board paper (18:30).
    - Board Risk Committee (19:00, limit 20:00).
11. **Standing holds**
    - Production stays held until the PH01 s.9.3 gate is passed.
    - The payment path stays held unless the Board decides otherwise.
    - No contact with the attacker.

No files were created.