CEO FINAL DECISION RECORD: C06 (Tue 17 Nov 2026, 20:00 HKT, H+36). Lan Tidal Bank, CMT chair.

All actions are simulated, for the facilitator to log. I received sealed answers from SEC (Q16a, Q16b), LC (Q17a, Q17b) and COM (Q18a, Q18b). The only facilitator handoff went to SEC (Q13a and Q13b); LC and COM had none.

I re-checked the following before relying on them:
- R08 4.2.4 (p.18) and 4.3.1 (p.19, "a process for rolling-back changes to re-instate the original programs").
- R06 3.4 (p.6, "The Board bears ultimate responsibility").
- R10 DPP2(3) (p.167) and DPP4(2) (p.169).
- R12 2.5.2 (p.6, "segregation or compartmentalisation").
- R07 4.7.1–4.7.2 (pp.13–14).
- R05 pp.1–3 (scan-checked at C01).
- PH01 v1.0.

**CEO record entries, 20:00**
1. **Production recovery.** The recovered image is recorded as an offline FAIL: 118 of 120 instructions reconciled, with 2 unexplained mismatches. I authorise no production stage and no narrower recovered-system mode tonight. The basis is PH01 s.9.2 ("One unexplained difference is a fail") and s.9.3 ("Missing any item means hold"). No gate item may be waived (s.3).
2. **Board meeting.** No card shows that the 19:00 Board Risk Committee I convened at C05 took place, so its status is unverified. I convene the Board Risk Committee by phone or video for 21:30. If the 19:00 meeting was held, this is an urgent update meeting. If it was not, the decision log records that the PH01 s.15.2 limit (20:00) was missed.
3. **Clearance rule.** My C05 standing rule continues: every LC clearance is given live at a fixed time, with the second LC officer as backup, and is logged at once.

==================================================================
**UNIT C06-Q16a: staged recovery, hold or narrower mode, and the gate**

**Original answer reference:** sealed SEC answer for C06, "UNIT Q16a": decisions 1–3, actions H1–H5 and the PH01 s.9.3 authorisation gate.

**Decision: OVERRIDE** (narrow addition; SEC's hold and gate are kept).

**Reason**
- SEC's three decisions are adopted:
  - Production of the recovered image is held.
  - A Board-narrowed recovered mode is also unavailable, because a narrower scope "must still pass every item" (PH01 s.9.3) and the cause of the mismatches is unknown.
  - The only narrower service mode is the PH01 s.8 alternate process, payroll first. It runs only on SEC's written clearance, due by 21:00 with a HOLD default.
- External support: R08 4.2.4 (p.18) says "only properly tested and approved systems are promoted to the production environment".
- **Gap I am closing:** SEC's answer does not cover 20:00–21:00 if the alternate process is already releasing. The handoff says SEC's C04 clearance "cannot be verified". PH01 s.9.3 allows service to continue on the alternate process only "if it holds a current security clearance under 8.2 and its own reconciliation ties". PH01 s.2.3 sets a security default of hold. A release route with no evidenced clearance therefore pauses until SEC logs one.
- This new condition changes execution, so the unit is marked OVERRIDE.

**Final action and condition**
1. **SEC actions H1–H5 and the seven-item gate, exactly as written:**
   - log FAIL and HOLD;
   - preserve the test record, image hash and mismatch traces, and check the test-data preconditions;
   - mark mismatched items that map to real instructions as "status unknown, held";
   - deliver a preliminary root cause by 23:00;
   - require a full-set rerun of RC1–RC8 and a new pass through s.9.3 before any production use.
2. **Added: alternate-process status check.**
   - By 20:15 the Head of Payments Ops reports whether the alternate process is currently releasing. SEC reports whether a PH01 s.8.2 clearance is on the log.
   - If it is releasing and no clearance is logged, new releases pause at once. In-flight items are classified (settled, not settled or unknown) and unknown items are held under PH01 s.8.6. The hourly reconciliation is run immediately.
   - LC is told at once. This is a change in service status (PH01 s.5.8).
3. **21:00 outcome:**
   - **If SEC logs clearance by 21:00** (checks C1–C7 plus reconciliation ties): at about 21:15 I activate the alternate process, or confirm the earlier activation, after consulting the Head of Payments Ops. It runs payroll first under PH01 s.8.4. I declare or confirm BCP activation (PH01 s.4.4). LC is told at once and informs the HKMA promptly (R07 1.3.3).
   - **If SEC logs HOLD:** all releases stay suspended. The Board is told at 21:30.

**Accountable owner**
- SEC: hold, gate evidence items 1–3, clearance and stop authority.
- Execution: Payments Ops and the IT Ops recovery team.
- CEO: decides activation and production. The Board may narrow scope but cannot waive any gate item.

**HKT time, deadline or trigger**

| Time | Item |
|---|---|
| 20:00 | HOLD logged |
| 20:15 | Status report on the alternate process; pause if uncleared |
| 20:30 | Evidence preserved; register flags set |
| 21:00 | SEC clearance or HOLD |
| ~21:15 | Activation or confirmation, if cleared |
| 23:00 | Preliminary root cause |
| After a logged full-set pass only | Rerun and gate review |

**Recipient and channel:** decision log, test record, evidence register and instruction register. Communication is in the CMT room or on a phone bridge. Results go to the Board through me.

**Final external basis**
- SEC Q16a "BASIS: EXTERNAL" items 1–6 are adopted unchanged:
  - R08 4.2.4, p.18 (verified);
  - R09 5.1.2, p.19;
  - R05 p.1;
  - R07 4.3.2, p.11;
  - R06 1.3 and 3.4, pp.3 and 6 (verified);
  - R01 s.22 and R03 6.1.1.
- For the added pause: R05 p.1 (scan-checked), "The top priority should be to safeguard the interests of customers". Releases through a route with no evidenced security clearance risk wrong payments.
- SEC's "no direct rule located" search record is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.9.2, s.9.3, s.3 ("No gate condition may be waived");
- s.8.2, s.8.4, s.8.6, s.2.3, s.4.4, s.9.1, s.5.8.

No conflict found.

**Dispatch instruction**
- EXECUTE NOW: H1, the 20:15 status check, and the pause if releases are running without a logged clearance.
- SCHEDULE: H2/H3 at 20:30, the clearance decision at 21:00, H4 at 23:00.
- HOLD: any production stage and any narrower recovered mode until the full s.9.3 gate is passed.
- Activation at ~21:15 depends on SEC's logged clearance.

==================================================================
**UNIT C06-Q16b: stop and rollback criteria**

**Original answer reference:** sealed SEC answer for C06, "UNIT Q16b", sections A, B and C.

**Decision: CONFIRM**

**Reason**
- **Section A (alternate process).** Stops at once, without prior approval, on:
  - one unexplained reconciliation difference;
  - any duplicate, replayed or wrong payment;
  - any security indicator.

  On a stop, all releases are suspended, in-flight items are classified and unknown items are held. This applies PH01 s.8.6–8.7.
- **Section B (recovered system).** Applies PH01 s.9.5 verbatim. Rollback means disconnection from the payment interfaces within a rehearsed target of 15 minutes. Service falls back to the alternate process only if its clearance is current and its reconciliation ties; otherwise all releases are suspended. Restart needs a new pass through s.9.3.
- **Section C (security indicators).** Includes any payment message that cannot be traced to a processing ID.
- External support: R08 4.3.1 (p.19, verified) requires "a process for rolling-back changes" and "a post implementation verification".

**Final action and condition:** A, B and C exactly as written. After any stop I am informed. I decide restart after a security stop, and restart also requires SEC to re-clear.

**Accountable owner**
- SEC: the criteria and security stops.
- Head of Payments Ops: reconciliation and holds.
- IT Ops duty manager: disconnection.
- CEO: restart after a security stop.

**HKT time, deadline or trigger**
- Hourly reconciliation, plus a continuous check against duplicate processing IDs.
- Stops take effect immediately.
- Disconnection within 15 minutes, rehearsed as gate item 3.

**Recipient and channel**
- The alternate-process and recovered-system interfaces, the instruction register and the decision log.
- LC is told at once on any stop, and COM issues the Version R update.

**Final external basis:** SEC Q16b "BASIS: EXTERNAL" items 1–4 are adopted (R08 4.3.1, p.19, verified; R09 5.1.2; R05 p.1; R09 8.2.1; R07 1.3.3). SEC's "no direct rule located" record is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.9.5, s.8.6 and s.8.7. No conflict found.

**Dispatch instruction**
- EXECUTE NOW: the section A criteria apply to any alternate-process release from this moment.
- Section B criteria: HOLD, since no recovered-system production is authorised. They take effect only after the gate.

==================================================================
**UNIT C06-Q17a: forensic firm request for the diagnostic image**

**Original answer reference:** sealed LC answer for C06, "UNIT Q17a".

**Decision: CONFIRM**

**Reason**
- No full copy leaves the bank. The firm gets a minimised extract with customer identifiers masked, or examines the full image inside the bank's laboratory. This is the PH01 s.16.2 default.
- SEC's co-decision position (SEC Q16, facts to LC) agrees, so the joint LC and SEC decision required by PH01 s.3 is met. The DPO is consulted.
- The conditions satisfy DPP4(2) (p.169) and DPP2(3) (p.167, "from being kept longer than is necessary"):
  - a written need statement;
  - a check of the actual contract terms against PH01 s.16.1;
  - DPO-checked masking;
  - encrypted transfer by bank route only;
  - named analysts;
  - legal hold;
  - return or destruction with a certificate.
- Segregation follows R12 2.5.2 (p.6, verified).

**Final action and condition:** conditions 1–7 exactly as written.

**Accountable owner**
- LC and SEC jointly, consulting the DPO and the forensic lead.
- SEC's forensic lead prepares the extract.
- The evidence custodian transfers it.

**HKT time, deadline or trigger**

| Time | Item |
|---|---|
| 20:15 | Decision logged |
| 20:45 | Reply to the firm |
| 21:00 | Firm's need statement due; LC contract check |
| 00:30 Wed | Masked extract (target) |
| Now | In-lab access can start |

**Recipient and channel:** the firm's engagement lead.
- The reply goes by call-back to a number on file, then in writing by a route that does not depend on corporate email.
- Data goes only by bank-hosted encrypted transfer, or on bank-issued encrypted media collected by the custodian.

**Final external basis:** LC Q17a "Basis: external" is adopted:
- R10 DPP4(2), DPP2(3)–(4), DPP3 (pp.167–169; DPP2(3) and DPP4(2) verified);
- R12 2.5.2, p.6 (verified);
- R16b Annexes D and E;
- R08 4.2.4, as a general principle.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.16.1, s.16.2, s.6.3, s.6.5, s.6.6, s.17.1, s.17.2 and s.3. No conflict found.

**Dispatch instruction**
- EXECUTE NOW: log the decision and reply to the firm.
- SCHEDULE: the extract, which depends on the need statement, the contract check and the DPO's masking check.
- HOLD: any full-copy transfer.

==================================================================
**UNIT C06-Q17b: escalation to the Board**

**Original answer reference:** sealed LC answer for C06, "UNIT Q17b".

**Decision: CONFIRM**

**Reason**
- The tolerance was reached at about 08:00 and is now about 150%.
- PH01 s.15.2 requires a meeting within 12 hours of reaching 100%, and no meeting is evidenced.
- LC's branch is right: convene now, targeting 21:30. If the 19:00 meeting was held, this becomes an update meeting; if not, the missed limit is logged.
- The agenda separates items to note from decisions:
  - **Decisions:** recovery scope, with LC's advice that no gate can be waived; a revised remediation total under s.13.7 if the projection exceeds HKD 5 million; reaffirming the no-payment policy.
  - **To note:** data, authorities and third parties.
- Legal advice goes in a separate privileged section (PH01 s.15.3).
- External support: R06 3.4 (p.6, verified), "The Board bears ultimate responsibility for ensuring that an AI remains operationally resilient".

**Final action and condition:** items 1–8 exactly as written. I add the 21:00 alternate-process outcome and SEC's 23:00 root-cause timing as facts in item 2. This only fills record fields.

**Accountable owner**
- CEO: convenes and chairs the escalation, consulting LC.
- LC: legal and authorities sections, and privileged advice, by 21:00.
- CFO: remediation total and insurer position.
- SEC and Payments Ops: recovery facts.

**HKT time, deadline or trigger**
- Meeting notice: 20:15.
- Paper sections: 21:00.
- Meeting: 21:30.
- Board minute: at the meeting.
- HKMA told in its next update that tolerance is exceeded and the Board is engaged.

**Recipient and channel:** Board or Risk Committee members by phone or video. The paper goes by hand, or by an encrypted Board route only if SEC has logged it safe.

**Final external basis:** LC Q17b "Basis: external" is adopted:
- R06 3.2 (pp.5–6), 3.4 (p.6, verified) and p.3;
- R07 2.1.1, p.5.

LC's "no direct rule located" record on external Board timing is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.4.3, s.15.2, s.15.3, s.9.2, s.9.3, s.13.7 and s.12.1. No conflict found.

**Dispatch instruction**
- EXECUTE NOW: send the convening notice.
- SCHEDULE: the paper at 21:00 and the meeting at 21:30. Item 2 depends on the 21:00 clearance outcome.

==================================================================
**UNIT C06-Q18a: customer status update**

**Original answer reference:** sealed COM answer for C06, "Q18 a": Version H and conditions V1–V4.

**Decision: OVERRIDE**

**Reason**
- The approved position is COM's Version H (hold). Versions N and S are not usable tonight.
- Three changes:
  1. **New "paused" line.** COM's V2 recognises a "paused" status but its text has lines only for running and not running. My Q16a pause needs its own accurate line.
  2. **Clearance default.** No default is set if LC's clearance is not logged. That gap held statements at C01–C03. My C05 fixed-slot rule applies: LC clears at 20:45; if no clearance is logged by 20:55, I direct release of the verified-facts version, with LC's review running in parallel. Basis: R09 8.2.2 (p.33), messages must be "consistent and up-to-date"; PH01 s.1.3.
  3. **Extra update.** An update goes at once on the 21:00/21:15 alternate-process outcome and on the Board's decision.
- These change execution, so the unit is marked OVERRIDE.

**Final action and condition**
- Version H as written, published at 21:00. It includes:
  - the hold explanation, with no test figures;
  - the SME payroll apology;
  - the fee waiver and direct-loss claims, with "told when to expect a decision";
  - the payroll-delay confirmation letter on request, wording cleared by LC;
  - the data lines (V4) and the scam warning;
  - next update by 07:00.
- The V2 alternate-process line is one of three:
  - **Running with logged clearance:** COM's running line.
  - **Paused:** "Payments through our alternative process are paused while we complete a security check. Each payment will be made only once; we will tell you as soon as they restart."
  - **Never activated or HOLD:** COM's "remain on hold" line.
- Fixed lines as written: no 118/120 figures, no "attack is over", no restoration time, and nothing about the vendor, system or designation.
- **Clearance:** LC clears at 20:45, with the second LC officer as backup. Default at 20:55 as described in the Reason.
- **Further updates at once on:**
  - activation or confirmation at ~21:15, or a HOLD;
  - the Board decision;
  - any stop (Version R).

**Accountable owner**
- CEO approves (COO as alternate after 15 minutes).
- LC clears. SEC and Operations fact-check.
- COM publishes.
- Payments Ops supplies figures (V3).

**HKT time, deadline or trigger**
- V1–V4 verified: 20:45.
- Clearance default: 20:55.
- Publish: 21:00.
- Extra updates: at once on the triggers above.
- Next scheduled: 07:00 Wed.

**Recipient and channel**
- Public: website status page, press release, text-only social posts, app banner (if trusted), IVR and branch notices.
- Staff: script v6.
- HKMA: copy via COM to LC at release, with a receipt requested (PH01 s.5.5, s.5.8).

**Final external basis**
- COM Q18a "Basis" is adopted:
  - R05 pp.1–3 (scan-checked);
  - R09 8.2.2, p.33, and footnote 26.
- For the changes: R09 8.2.2, p.33, "consistent and up-to-date messages". COM's professional-judgment record on the confirmation letter is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.9.2, s.9.3, s.11.2, s.11.3, s.11.4;
- s.13.1, s.13.2, s.13.6, s.13.7;
- s.1.3, s.2.3, s.5.8.

The s.2.3 clearance-hold conflict is resolved as at C05.

**Dispatch instruction**
- SCHEDULE: publish at 21:00. This depends on V1 (my HOLD decision, logged now), V2 (the 20:15 status report) and clearance or the 20:55 default.
- Extra updates are triggered by Q16a and Q17b outcomes.

==================================================================
**UNIT C06-Q18b: counterparties with unsettled instructions**

**Original answer reference:** sealed COM answer for C06, "Q18 b".

**Decision: CONFIRM**

**Reason**
- **Scope.** All counterparties holding unsettled items are notified, not only the two that asked. This applies PH01 s.14.3: "a verified call and a written notice the same day, then updates at 08:00, 13:00 and 18:00". It also applies R05 p.2: "notify other affected AIs (so that they can in turn notify their affected customers) as soon as practicable".
- **Verification.** Every incoming request is verified by call-back before any reply (s.14.2). Counterparties are asked to check their own receiving-side records, which supply the independent record that PH01 s.8.6(b) needs for unknown items.
- **Data minimisation.** Notices carry references, amounts and value dates only.
- **Security.** Nothing is acted on through routes the counterparty supplied in its request, and there is a warning against unverified instructions.
- **LC review.** It runs alongside and does not hold this operational message, which is consistent with my clearance rule.

**Final action and condition**
- Exactly as written.
- The core message's alternate-process line uses the same V2 status as Q18a (running, paused, or on hold).
- The two Q16a mismatched items, if they map to real instructions, are shown as "unknown – held".

**Accountable owner**
- Head of Payments Ops: contact (PH01 s.14.1).
- COM: wording.
- LC: parallel review.
- The named Payments Ops duty manager makes the calls.

**HKT time, deadline or trigger**

| Time | Item |
|---|---|
| 21:00 | Counterparty list and item statuses ready |
| 21:30 | Verified calls to the two counterparties that asked |
| 23:00 | Calls to the other counterparties |
| 23:30 | All written notices sent |
| 18 Nov onward | Updates at 08:00, 13:00, 18:00 until every item is settled or returned |
| 08:00 | Calls to any desk unreachable tonight |

**Recipient and channel:** counterparty operations desks.
- A verified call to a number on file.
- A written notice through the bank's established secure interbank operations channel, or by courier.
- Not ordinary email unless SEC has logged it safe.

**Final external basis:** COM Q18b "Basis" is adopted:
- R05 pp.1–2 (scan-checked);
- R07 4.7.1, p.13 ("counterparties, business partners", verified) and 4.7.2, p.14;
- R09 8.2.2.

COM's "no direct rule located" record on notice content and channel is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.14.1–14.3 and s.8.6(b). No conflict found.

**Dispatch instruction**
- SCHEDULE as in the timetable above.
- Notice content depends on the V2 status (Q16a, from 20:15) and the H3 flags (20:30).

==================================================================
**ORDER OF DEPENDENT ACTIONS (HKT)**
1. **20:00.** SEC logs FAIL and HOLD (H1); I log no production and no narrower recovered mode.
2. **20:15.**
   - Alternate-process status and clearance-log report; pause at once if releasing without a logged clearance. LC is told.
   - Forensic-firm decision logged (Q17a).
   - Board meeting notice for 21:30 (Q17b).
3. **20:30.** SEC preserves the test evidence and checks the data preconditions. Mismatched items are flagged and held in the live register. This feeds the counterparty statuses.
4. **20:45.**
   - V1–V4 closed; LC clearance slot.
   - Reply to the forensic firm.
5. **20:55.** Clearance default, if no clearance has been logged.
6. **21:00.**
   - Version H published; HKMA copy via LC; staff script v6.
   - SEC logs clearance or HOLD.
   - Firm need statement and contract check due.
   - Counterparty list ready.
   - Board paper sections ready.
7. **~21:15 (only if cleared).**
   - I activate or confirm the alternate process and declare BCP activation.
   - LC informs the HKMA at once.
   - COM issues an extra update.
   - Counterparty notices reflect the new status.
8. **21:30.**
   - Board Risk Committee meets.
   - Verified calls to the two counterparties that asked.
   - After the meeting: Board minute, COM update on any Board decision, HKMA told the tolerance is exceeded and the Board is engaged.
9. **23:00–00:30.**
   - SEC preliminary root cause (23:00); full-set rerun only once the cause is explained.
   - Calls to other counterparties (23:00); written notices (23:30).
   - Masked extract for the firm (00:30).
10. **Wed 18 Nov.**
    - Customer update at 07:00.
    - Counterparty and HKMA updates at 08:00, 13:00 and 18:00 for counterparties; HKMA at 08:00 and 18:00.
11. **Standing holds.**
    - Production of the recovered system until a full-set pass and every s.9.3 item is logged.
    - Full-image transfer to the forensic firm.
    - Payment to the attacker.

No files were created.