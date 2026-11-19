C07 is decided: all six units are CONFIRM. On Q21b I take COM's stated fallback branch so customer notices are not held for an internal clearance. CEO final record for Wed 18 Nov 2026, 12:00 HKT (H+52). All actions are simulated, for the facilitator to log.

**Position from the handoffs**
- Containment, the evidence hold and the vendor revocation are in force.
- The recovered image is on HOLD.
- No card records whether the secondary process was activated.
- No card records the credential closure-test result.
- No card records any customer notice as delivered: all 80 and all 320 dispatches depended on an LC clearance that was never logged.
- No receipt from the Commissioner is verified.
- Annex F has not been dispatched.

My standing direction at 12:05: notices to customers whose data is confirmed exposed may no longer wait on an unlogged internal clearance. PH01 s.1.3 says "the external requirement prevails". R16b PDF p.3 expects notice "as soon as practicable". I record the gap in the decision log.

---
**Q19a | Original: SEC sealed answer, Q19a | CONFIRM**
- **Reason:**
  - It applies PH01 s.6.4: each entry keeps the original timestamp, the measured offset, the time converted to HKT and the uncertainty. Events closer together than their combined uncertainty are recorded as "order undetermined".
  - The offset method is chosen per source and stated.
  - The ±4-minute default is used only where nothing better is known.
  - Supplier records count as the supplier's account until reconciled (s.6.7(d)).
  - The scripts are versioned and hashed, a second person reviews independently, personal data is masked, and nothing is attributed.
  - The key questions feed the Annex F report and the backup-suitability check.
- **Final action:** as in SEC Q19a, actions 1 to 6. Version 1 also goes to LC for Annex F sections B5 to B7.
- **Owner:** SEC. SEC analysts build the timeline; the evidence custodian handles intake; the forensic firm (on masked data) or an independent analyst reviews.
- **Time:** intake and hashing 14:00; version 1 at 20:00 on 18 Nov; reviewed version 12:00 on 19 Nov.
- **Recipient and channel:** the offline lab master file and evidence register; summaries in the decision log; a printed or secure-lab copy to LC and me.
- **External basis:** SEC Q19a "Basis, external" (R02 s.7.2.3(a)(v)(2),(4); R02 s.6.2.23(g), used as a general principle; R03 s.6.2.23(d)).
- **Internal basis:** SEC Q19a "Basis, internal" (PH01 v1.0 ss.6.4, 6.3, 6.7(b),(d)). No conflict.
- **Dispatch:** EXECUTE NOW.

**Q19b | Original: SEC sealed answer, Q19b | CONFIRM**
- **Reason:**
  - An unexplained incident indicator means containment can no longer be treated as confirmed.
  - Raising monitoring and keeping every containment measure follows PH01 s.7.1 (isolate at the network layer, do not power off) and s.6.1 (capture before any change). It also meets R03 s.6.2.26(a)–(b) and R05 p.1.
  - Under s.2.5, SEC reports hourly again until containment is confirmed.
  - The stop on security indicators that I adopted at C06 Q16b applies to the secondary process.
  - The sweep is correctly extended to the recovery candidate and the backup copy.
- **Final action:** as in SEC Q19b, actions 1 to 8.
  - If any secondary releases are running, they stop now.
  - Releases resume, or the process is first activated, only after a clean sweep, SEC's re-confirmed written s.8.2 clearance and a reconciliation that ties.
- **Owner:** SEC. SOC, EDR, Network and IT Operations execute. The Head of Payments Operations stops any releases. I am told.
- **Time:** isolation check and capture 12:00–12:30; sweep results 14:00; hourly reports from 13:00.
- **Escalation trigger:** escalate at once if the indicator appears outside quarantine, the host makes any outbound connection, or the indicator links to data access.
- **Recipient and channel:** change record, evidence register, decision log; verbal briefing to me. LC is told for the HKMA update if service status changes.
- **External basis:** SEC Q19b "Basis, external" (R05 p.1; R03 s.6.2.26(a)–(b); R02 ss.6.2.23(f), 7.2.3(f); R11 Step 2).
- **Internal basis:** SEC Q19b "Basis, internal" (PH01 v1.0 ss.7.1, 6.1, 2.5, 9.5, 8.2, 7.5, plus the gap SEC noted in s.8.7). No conflict.
- **Dispatch:** EXECUTE NOW. Secondary releases are on HOLD until the sweep is clean and clearance is re-confirmed in writing. The recovered system and vendor reinstatement stay on HOLD.

**Q20a | Original: LC sealed answer, Q20a | CONFIRM**
- **Reason:**
  - The specified-form follow-up was required under R01 s.28(3), because the 09:00 call was not in the specified form.
  - On the record, Annex E was filed on the evening of 16 Nov. That is inside the 48 hours in R01 Sch.6 item 2, and also counts on its own as notice under s.28(2)(b)(i).
  - No receipt is verified, so compliance cannot be proven. The 48-hour clock ended by 09:00 on 18 Nov.
  - LC's plan is sound:
    - get the device receipt and ask the Commissioner to confirm by 13:00;
    - if receipt is unconfirmed, re-file openly by 14:00, treat it as a possible missed deadline and reconvene the CMT (s.18.5);
    - open a provisional tracker line for the new indicator, depending on SEC's certainty and on whether a critical computer system (CCS) is involved.
- **Final action:** as in LC Q20a, immediate actions 1 to 4.
- **Owner:** LC. The LC duty officer executes and a second LC officer checks. SEC supplies the device log and facts on the indicator.
- **Time:** 13:00 confirmation; re-file by 14:00 if needed.
- **Clock for any new incident:** starts when SEC logs reasonable certainty. It is 12 hours if the core function is affected, otherwise 48 hours.
- **Recipient and channel:** the Commissioner; confirmation by the verified telephone route; any re-filing through the designated secure channel. If the deadline is confirmed missed, the HKMA is told at the next update and the matter goes in the Board paper.
- **External basis:** LC Q20a "External basis" (R01 s.28(2)(b), (3), (5), Sch.6 item 2; R02 Annex E, s.7.3.5, s.7.3.6(b)). I checked R01 PDF p.44 and R02 PDF p.42 at C04.
- **Internal basis:** LC Q20a "Internal bank procedure" (PH01 v1.0 ss.5.5, 18.5, 5.3). No conflict.
- **Dispatch:** EXECUTE NOW. The re-filing depends on whether receipt is confirmed by 13:00, and is not held for anything else.

**Q20b | Original: LC sealed answer, Q20b | CONFIRM**
- **Reason:**
  - The written report under R01 s.28(4) goes to the Commissioner in the Annex F format, or a sector form if the regulator contact register (RCR) lists one, through the designated secure channel.
  - It is due within 14 days of awareness (Sch.6 item 3), so by 30 Nov 2026. LC records that it could not confirm the day-counting convention and takes the conservative date.
  - The section owners, the fact-checking from records with unverified items marked, the second-officer check and the 27 Nov internal target all fit s.1.4, s.2.4 and s.5.6.
  - Customer data is minimised to counts and data types.
  - It is correctly a category 3 filing to the Commissioner, with the HKMA receiving a copy.
- **Final action:** as in LC Q20b.
  - Sections assigned on 18 Nov.
  - Inputs due 23 Nov at 17:00.
  - Draft on 24 Nov; fact-check and route test on 25–26 Nov.
  - File on 27 Nov and save the receipt.
  - 28–30 Nov is the fallback window.
  - Later facts follow as supplementary material.
- **Owner:** LC is accountable. The LC duty officer drafts. The section owners are as tabled in LC's answer. I am informed and review in parallel; I do not hold the filing.
- **Time:** 27 Nov 2026 at 17:00 internally; statutory latest 30 Nov 2026.
- **Recipient and channel:** the Commissioner, through the designated secure channel; copy to the HKMA.
- **External basis:** LC Q20b "External basis" (R01 s.28(4)–(6), Sch.6 item 3; R02 s.7.3.7(a)–(b), Annex F).
- **Internal basis:** LC Q20b "Internal bank procedure" (PH01 v1.0 ss.5.2, 5.6, 1.4, 18.4). No conflict.
- **Dispatch:** SCHEDULE. Section assignments go today and filing is on 27 Nov. The filing depends on the section inputs but is never held past 30 Nov.

**Q21a | Original: COM sealed answer, Q21a | CONFIRM**
- **Reason:**
  - Every report gets one case route with a reference number and a named owner (PH01 ss.13.6, 11.5).
  - Fraud gives immediate protection: it offers suspension and attempts recall (R09 ss.4.4.2–4.4.3).
  - Routing by type follows s.13.
  - Promises are confined to what the bank has pre-approved:
    - fees waived (s.13.1);
    - direct losses from the disruption reimbursed on claim (s.13.2);
    - identity-protection monitoring for the 320 (s.13.5).
  - There is no promise to reimburse scam losses (s.13.4).
  - The line on unauthorised transactions is used only in wording LC confirms (s.13.3; R09 s.4.4.4).
  - Approval limits follow s.13.7.
  - Scam reports from customers outside the 320 count as "reports of misuse", a trigger to review Group B scope (s.10.4(c)).
- **Final action:** as in COM Q21a items 1 to 6.
  - Route live at 12:30.
  - Script v7 by 13:30, cleared by LC.
  - By 15:00, Fraud tells the DPO, LC and SEC which of the 31 are in the 320.
  - If any are outside it, the DPO and LC review scope and I decide by 18:00.
  - LC includes the scam reports in the next HKMA update.
- **Owner:** Fraud handles intake and triage. The Head of Fraud with LC decides s.13.3 and s.13.4 cases. The Head of Payments Operations owns s.13.2. COM owns scripts. The CFO owns the running total. I approve anything above HKD 50k per customer, and the Board approves anything above the HKD 5m incident total.
- **Time:** 12:30; protection within 1 hour of a report; 13:30; 15:00; 18:00.
- **Recipient and channel:** the case register; call-back to the number on file, the number on the customer's card, a relationship manager or a branch.
- **External basis:** COM Q21a "Basis (external)" (R09 ss.4.4.2–4.4.4, 4.3.2; R05 p.1).
- **Internal basis:** COM Q21a "Basis (internal)" (PH01 v1.0 ss.13.1–13.7, 10.4(c), 11.5). No conflict.
- **Dispatch:** EXECUTE NOW. The unauthorised-transaction line depends on LC's confirmation of the wording.

**Q21b | Original: COM sealed answer, Q21b | CONFIRM (COM's stated fallback branch)**
- **Reason:**
  - Nothing proves any of the 320 has been reached. Under PH01 s.10.3 ("Approval and scheduling are not delivery") and s.10.6, each customer gets one consolidated notice from a single list keyed by customer ID.
  - The 12 corrected contacts are checked by Fraud against the bank's verified records before use (s.10.5). If a contact cannot be verified, the customer is reached through a branch or relationship manager instead.
  - Any earlier misdirected notice is assessed as a possible further disclosure.
  - COM correctly identified that an open-ended internal hold conflicts with R16b p.3 ("as soon as practicable") and R11 p.8 ("regardless of the progress of any internal investigation"). Its proposed action follows the external requirement, as PH01 s.1.3 directs.
- **I select COM's branch as written:**
  - LC clears the consolidated text by 13:30, orally if need be, and I log the clearance.
  - If LC has not cleared it by 13:30, I direct dispatch of the facts-only core text: exposure, publication, scam warning, how to get help, and contact. SEC and the DPO have already confirmed these facts.
  - The authorities line and any liability wording are left out until LC clears them.
- **Final action:** as in COM Q21b items 1 to 5.
  - Master list 13:30; Fraud check of the 12 by 14:30.
  - Calls 14:30–19:00, letters posted 18 Nov.
  - Register figures to LC by 20:00, then daily.
  - Any change to the 320 audience comes back to me for approval.
  - If the DPO and LC find a misdirected notice, LC updates the PCPD and the HKMA.
- **Owner:** I approve the audience (unchanged) and direct dispatch if needed. LC clears the text. SEC and the DPO confirm the facts. COM owns the list, the register and sending. Fraud checks contacts and makes calls with the contact centre. Operations sends letters.
- **Time:** 13:30, 14:30, 19:00, 20:00.
- **Recipient and channel:** the 320, by named-team call then letter; no SMS, push or email; up to 3 attempts, then risk-based follow-up.
- **External basis:** COM Q21b "Basis (external)" (R16b p.3; R11 pp.7–8; R09 s.4.2.3).
- **Internal basis:** COM Q21b "Basis (internal)" (PH01 v1.0 ss.10.3, 10.5, 10.6, 10.1–10.2, 1.3, 1.4).
- **Recorded conflict:** PH01 s.10.1 (LC clears) together with s.2.3 (compliance conditions default to hold) would allow an open-ended hold, contrary to R16b and R11. It is resolved under s.1.3 by the bounded fallback above, and logged for the post-incident review of PH01.
- **Dispatch:** EXECUTE NOW. Calls start at 14:30 with LC-cleared text, or with the facts-only text on my 13:30 direction. Use of the 12 corrected contacts depends on the Fraud check.

---
**Order of actions that depend on each other**
1. 12:00–12:30:
   - SEC checks the quarantine and captures the indicator.
   - Any secondary releases stop.
   - The case route goes live.
   - The timeline intake starts.
2. 13:00:
   - LC obtains the Annex E receipt and confirmation from the Commissioner.
   - SEC reports hourly from now on.
3. 13:30:
   - LC clears the customer notice, or I direct the facts-only text.
   - Master list built.
   - Script v7 issued.
4. 14:00:
   - If receipt is unconfirmed, Annex E is re-filed openly, the CMT reconvenes, and the HKMA and Board are told.
   - Sweep results. Any secondary resumption or activation depends on a clean sweep plus SEC's written re-clearance.
   - Timeline intake complete.
5. 14:30: Fraud check of the 12 contacts, then calls begin.
6. 15:00: Fraud maps the 31 scam reports against the 320. If any fall outside it, the DPO and LC review scope and I decide by 18:00.
7. 19:00 and 20:00:
   - Calls complete.
   - Register figures to LC.
   - Timeline version 1 to LC, feeding Annex F sections B5 to B7.
   - If SEC reaches certainty that the new indicator is the same incident, LC sends supplementary information. If SEC finds it is a new incident, LC files a fresh s.28 notification on its own clock.
8. 19 Nov 12:00: reviewed timeline.
9. 23–26 Nov: Annex F drafting milestones.
10. 27 Nov: Annex F filed.
11. 30 Nov: statutory latest for Annex F.