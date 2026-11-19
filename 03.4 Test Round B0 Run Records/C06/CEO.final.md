C06 is decided: five units are CONFIRM and one is OVERRIDE. The override is Q18a: I replace one sentence in COM's customer update. That sentence says waiting payments "will not be lost", which is not a verified fact. This is the CEO final record for Tue 17 Nov 2026, 20:00 HKT (H+36). All actions are simulated, for the facilitator to log.

**What I take from the handoffs**
- The candidate-1 build started at 08:30.
- No card records the separation results, the backup checks, the test-data records or the data load.
- No card records SEC's clearance of the secondary process at C04, so I treat it as not current.
- Production use stays on HOLD.
- Whether the Board met under my C05 instruction (by 20:00) is not recorded.

**My decisions at 20:05, which set the position for every unit**
1. **Recovered system: HOLD.** The 118/120 lab result fails PH01 s.9.2: "One unexplained difference is a fail." It is also only a sample.
2. **Secondary process, payroll first:** I activate it only if SEC gives written clearance by 21:00 (PH01 s.8.2). The default is hold. If cleared, I log BCP activation and LC tells the HKMA at once.
3. **Board or Risk Committee:** meets by secure call at 21:30, unless a meeting is already recorded. LC logs any missed internal deadline.

There are no conflicts between the roles. COM's Version 1 (HOLD) matches SEC's hold and LC's Board paper.

---
**Q16a | Original: SEC sealed answer, Q16a | CONFIRM**
- **Reason:**
  - The recovered system is held for three reasons: the test failed the zero-tolerance mark, it covered only a sample, and the other s.9.3 gate items are unverified.
  - A narrower scope set by the Board cannot get around the missing offline pass (s.9.3).
  - The secondary process may run only on SEC's written s.8.2 clearance, with hold as the default (s.2.3).
  - The lab's "no recurring encryption" finding is correctly treated as limited to the lab's scope.
- **Final action:** as in SEC Q16a items 1–3.
  - Hold the recovered system.
  - SEC clears, or re-confirms clearance of, the secondary process by 21:00. If cleared, I activate it: pilot of up to 20 instructions if this is the first activation, then payroll in order of earliest value date, with the s.8.6 duplicate checks and hourly reconciliation.
  - Fix the failed test: prove the image's identity, find the root cause of both mismatches (Fraud reviews any tampering), retrieve the missing Q13a records, and re-run the full set.
  - Future production use needs the full s.9.3 gate and my authorisation.
- **Owner:** SEC. The Head of IT Operations and the Head of Payments Operations execute. I authorise.
- **Time:** hold logged 20:05. Clearance by 21:00, default hold. Re-test when the fix is ready.
- **Recipient and channel:** decision log; written clearance or refusal to me; Board pack; facts to LC (HKMA) and to COM.
- **External basis:** SEC Q16a "Basis: external" (R08 s.4.2.4; R03 s.6.2.22(c); R07 s.1.3.3; R05 p.1; R06 s.3.4).
- **Internal basis:** SEC Q16a "Basis: internal" (PH01 v1.0 ss.9.2, 9.3, 3, 8.2, 2.3). No conflict.
- **Dispatch:**
  - Recovered system: HOLD.
  - Clearance review: EXECUTE NOW.
  - Secondary-process activation: HOLD until SEC's written clearance, then SCHEDULE the pilot.

**Q16b | Original: SEC sealed answer, Q16b | CONFIRM**
- **Reason:**
  - It applies the PH01 s.9.5 and s.8.7 triggers: a security indicator, one unexplained difference, any duplicate or wrong payment, or any item whose status cannot be established.
  - Anyone named may stop without prior approval.
  - Rollback disconnects the system at the network layer, with no power-off. Service falls back to the secondary process only if it is cleared and its reconciliation ties; otherwise all releases are suspended.
  - Restart needs a new pass through s.9.3.
  - SEC added two triggers: an unexplained counterparty or clearing reject, and loss of monitoring. Both are reasonable judgment and consistent with s.9.5.
- **Final action:** as in SEC Q16b. It applies now to the secondary process, if cleared, and later to any recovery stage.
- **Owner:** SEC. The Head of Payments Operations owns the reconciliation triggers. The IT Operations duty manager disconnects. I am told at once.
- **Time:** from the first release. Reconciliation hourly. Stop immediately on any trigger.
- **Recipient and channel:** change record, decision log, instruction register, evidence register; immediate notice to me; LC (HKMA) and COM informed.
- **External basis:** SEC Q16b "Basis: external" (R08 s.4.3.1; R14b s.A.1; R05 p.1).
- **Internal basis:** SEC Q16b "Basis: internal" (PH01 v1.0 ss.9.5, 8.7, 8.6). No conflict.
- **Dispatch:** EXECUTE NOW as a standing control. It depends on the release activity it governs.

**Q17a | Original: LC sealed answer, Q17a | CONFIRM**
- **Reason:**
  - It applies the PH01 s.16.2 default: the firm gets a minimised set with personal data masked, and full images are examined only in the bank's lab.
  - A full copy needs LC's and SEC's written approval, a re-check of the s.16.1 contract terms, encrypted transfer with custody, and return or destruction (s.17.2).
  - DPP4(1), DPP4(2) and DPP2(3) (R10) make the bank responsible for its data processor. The harm from a second exposure is high because 320 records are already public.
  - Hold as the default for the full copy is correct.
- **Final action:** as in LC Q17a items 1–3.
  - Masked extract plus supervised in-lab access.
  - Full copy held: LC checks the contract terms by 22:00, and the firm must justify the need in writing.
  - The legal hold reminder goes to the firm.
- **Owner:** LC and SEC jointly, with the DPO consulted. SEC prepares the extract. The evidence custodian transfers it.
- **Time:** contract check 22:00; extract by 23:00. The full copy is held until all its conditions are met.
- **Recipient and channel:** the forensic firm's engagement lead, by encrypted media or bank-hosted encrypted transfer. A data release record and custody log are kept.
- **External basis:** LC Q17a "Basis" (R10 DPP4(1)–(2), DPP2(3); R12 s.2.5.2; R16b Annex B).
- **Internal basis:** LC Q17a "Internal bank procedure" (PH01 v1.0 ss.16.1, 16.2, 6.5, 3). No conflict.
- **Dispatch:**
  - Masked extract: SCHEDULE for 23:00, after SEC verifies it.
  - Full copy: HOLD until conditions (i)–(v) are met.

**Q17b | Original: LC sealed answer, Q17b | CONFIRM**
- **Reason:**
  - The tolerance reached 100% at 08:00, so under PH01 s.15.2 the Board must meet by 20:00. That deadline is now.
  - LC handles the unknown fact correctly: if no meeting is recorded, it logs the deadline as missed, the CMT reconvenes (s.18.5) and the meeting is held at 21:30.
  - The paper follows s.15.3. It seeks decisions only on matters that are the Board's: a narrower payroll-first scope that cannot waive any gate, and a revised remediation total if HKD 5m will be exceeded (s.13.7).
  - It gives the forensic data decision for information only, which is correct.
  - The "no direct rule located" search record for the meeting deadline is adequate.
- **Final action:** as in LC Q17b. I convene at 20:10 for 21:30. Paper out at 21:00. Board minute recorded.
- **Owner:** I convene and present. LC writes the legal sections. The CFO supplies the remediation total. SEC and Payments supply the facts.
- **Time:** 21:30 meeting; next HKMA update covers the tolerance breach, the hold and the Board meeting.
- **Recipient and channel:** Board or Risk Committee by secure call; Board minute.
- **External basis:** LC Q17b "Basis" (R06 ss.3.3–3.4; R07 s.2.1.1).
- **Internal basis:** LC Q17b "Internal bank procedure" (PH01 v1.0 ss.4.3, 15.2, 15.3, 9.3, 13.7). No conflict.
- **Dispatch:** EXECUTE NOW. The paper includes SEC's 21:00 clearance result.

**Q18a | Original: COM sealed answer, Q18a | OVERRIDE (one sentence)**
- **What stays:** Version 1 (HOLD), released by 21:00, with COM's core text, channels, approvals, the "never published" list and the next update by 07:00.
- **Reason for the change:**
  - In the branch for when the secondary process is not running, COM's Version 1 says "Waiting payments remain queued and safe. They will not be lost". That is not a verified present fact.
  - Items in flight are "held as status unknown until an independent record shows they did not settle" (PH01 s.8.6).
  - SEC treats the queue as untrusted.
  - I made the same correction at C04 Q12b. PH01 s.11.4 and R05 p.3 ("consistent and up-to-date messages") apply.
  - Clearance is not due until 21:00, so at release this is the branch in force unless an activation has been logged.
- **Replacement sentence:** "Waiting payment instructions are being held and checked so that each is processed correctly and only once. We will process them as soon as these checks allow."
- **Final action:**
  - Version 1 with the replacement sentence, released by 21:00. The "alternative process is running" branch is used only if I have logged activation.
  - Version 2 is published at once if I activate payroll-first after SEC's clearance (s.11.2 requires an update on any change in service status).
  - Version 3 is not released.
  - Relationship managers call the SMEs whose payroll was missed.
  - The bank-caused-delay letter line goes in only once LC has cleared it.
- **Owner:** I approve (COO as alternate after 15 minutes). LC clears. SEC and Payments check the facts. COM releases.
- **Time:** 21:00; Version 2 on activation; next update 07:00 on 18 Nov.
- **Recipient and channel:** as in COM Q18a "Channels"; copy to the HKMA through LC.
- **External basis:** COM Q18a "Basis (external)" (R05 pp.1–3; R09 s.8.2.2 and fn.26), plus R05 p.3 as quoted above.
- **Internal basis:** COM Q18a "Basis (internal)", plus PH01 v1.0 s.8.6 (quoted above) and s.11.4: "A figure is published only if its owner has confirmed it from a record."
- **Dispatch:** EXECUTE NOW for the 21:00 release. Version 2 is SCHEDULED, triggered by my logged activation.

**Q18b | Original: COM sealed answer, Q18b | CONFIRM**
- **Reason:**
  - It applies PH01 ss.14.1–14.3: both requesters are verified by call-back to a number already on file before any reply.
  - Every counterparty holding unsettled items gets a verified call and a written notice the same day, then updates at 08:00, 13:00 and 18:00.
  - Status is marked SETTLED, NOT SETTLED or STATUS UNKNOWN from independent records (s.8.6), and counterparties are asked for their receiving-side records.
  - Banks whose customers are affected are also told (R05 pp.1–2).
  - No customer personal data is disclosed beyond item references.
- **Final action:** as in COM Q18b.
- **Owner:** the Head of Payments Operations makes the contacts. COM controls the wording. LC clears.
- **Time:** verified calls and notices by 23:00 on 17 Nov; then 08:00, 13:00 and 18:00 daily, and at once on any change.
- **Recipient and channel:** all banks and counterparties holding unsettled items. Verified call first, then the established operational or interbank channel. Corporate email only if logged safe; otherwise a route agreed on the call.
- **External basis:** COM Q18b "Basis (external)" (R05 pp.1–2; R07 ss.4.7.1–4.7.2).
- **Internal basis:** COM Q18b "Basis (internal)" (PH01 v1.0 ss.14.1–14.3, 8.6, 5.7). No conflict.
- **Dispatch:** EXECUTE NOW. Replies depend on the call-back verification. Item status depends on the Payments Operations register.

---
**Order of actions that depend on each other**
1. 20:05: decision log entries for the recovered-system hold, the forensic data decision and the Board escalation. SEC's clearance review starts. Root-cause work and the extract are prepared.
2. 20:10: I convene the Board or Risk Committee for 21:30.
3. 21:00:
   - SEC's written clearance or refusal of the secondary process.
   - Board paper issued (it includes the clearance result).
   - Customer update released: Version 1 with the corrected sentence, unless activation has been logged.
4. If cleared:
   - I activate and log BCP.
   - LC phones the HKMA at once.
   - Pilot of up to 20 payroll instructions under the Q16b stop rules.
   - COM issues Version 2 at once.
   - The counterparty notices reflect it.
5. 21:30: Board meeting. It may narrow the scope, but no gate item can be waived. It may approve a revised remediation total.
6. 22:00: LC's contract check (only relevant to any later full-copy decision).
7. By 23:00: masked extract transferred; counterparties verified, called and given written notice.
8. 24:00: scheduled HKMA update covering the tolerance breach, the hold, the activation status and the Board outcome.
9. 07:00 on 18 Nov: next customer update. 08:00: next counterparty update.
10. Any future production use of the recovered system: a full re-test with zero unexplained differences, then every s.9.3 item, then my authorisation.