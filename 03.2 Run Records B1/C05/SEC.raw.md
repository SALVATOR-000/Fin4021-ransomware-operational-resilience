SEC (Information Security Lead): locked response for C05, Tuesday 17 Nov 2026, 08:00 HKT (H+24)

Assigned units: Q13a and Q13b only. The C01–C04 reports were handed back earlier. No facilitator handoff was addressed to SEC for C05. The ransom-decision and customer-notification records being supplied are for LC and COM; SEC does not rely on them here.

Status at 08:00 (if the disruption began at 08:00 Monday):
- The 24-hour tolerance for transfers and payroll is now at 100%. The chair must convene the Board or its Risk Committee within 12 hours (PH01 15.2), so by 20:00.
- Every recovery item below is gate-based, not time-based. Passing a target time never releases the gate (PH01 2.3 and 9.3).

Facts not known at this card:
- The backup's timestamp compared with the earliest evidence of attacker activity (from C03).
- Whether the backup system was ever reached by the vendor credential or attacker accounts.
- Whether the C04 secondary process holds a current clearance and its reconciliation ties.
- Whether trusted installation media is available independently of the compromised support vendor.
- Whether an earlier immutable restore point exists.
- The payments information owner's approval.

No conflict was found between PH01 and any applicable external requirement for these units.

---------------------------------------------------------------
UNIT Q13a: Which recovery candidate to test, and how to verify its integrity and separation

DECISION
- Test candidate (1) under PH01 9.1: a new build from trusted media, using only DATA from the pre-incident immutable backup, in an isolated recovery environment.
- The original gateway is never repaired in place. It stays under evidence hold.
- The standby system is tested only if candidate (1) fails, and then under the same checks.

Condition in the PH01 2.3 four-item format:
- Verifier: SEC.
- Latest time: 12:00 HKT (target).
- Condition: checks I1–I4 below show the backup is suitable.
- Default if not verified: HOLD that restore point. Then test the next-earlier immutable point if one exists (still candidate (1)). Move to the standby only if candidate (1) fails.
- Meanwhile, service continues on the alternate process only if it holds a current clearance and its reconciliation ties. Otherwise releases stay suspended (PH01 9.3).
- Close-out: logged.

ACTION (simulated, for the log)

R0, 08:30: working copy of the backup.
- SEC and LC jointly approve a hashed working copy of the immutable backup, with the forensic lead consulted (PH01 s.3).
- The evidence custodian carries it into the recovery environment by a one-way transfer.
- The original backup is preserved untouched. It is offline-scope evidence of the state before the incident.

INTEGRITY CHECKS
- I1, timing: the backup's timestamp (with clock offset) must come before the earliest evidence of attacker or vendor-credential activity from C03, by a margin (judgment). The attacker may have been present earlier than the first evidence shows. If the order cannot be determined, the backup is NOT treated as pre-incident (PH01 6.4).
- I2, immutability: the retention-lock and backup-system access logs show no change or deletion attempt, and no access by the vendor credential or attacker accounts.
- I3, hashes: file hashes, counts and sizes match the catalogue recorded at backup time (C01 item O1).
- I4, scan: an offline, read-only scan for the forensic firm's indicators: file hashes, web shells, scripts, unauthorised accounts, scheduled jobs and persistence.
- I5, data only:
  - Only application data is restored.
  - The operating system, application binaries and configuration come from trusted media and the approved baseline, never from the backup.
  - Binaries are hash-checked against signed or escrowed releases.
  - The media is obtained by a verified channel that does not depend on the compromised vendor.
- I6, static data: beneficiary master, routing, limits, roles, scheduled jobs and interface endpoints are compared with the baseline and change records. Every difference must be explained.
- I7, accounts and secrets: all accounts are rebuilt. There are no vendor accounts. New credentials, multi-factor authentication, new keys and certificates are issued. The old gateway keys are treated as compromised.
- I8, entry route: the entry route is closed (C03 closure test logged) and hardening is applied before the candidate goes to the PH01 9.3 gate.

SEPARATION CHECKS
- S1: no hosts, virtualisation, storage or management plane shared with the gateway or the workspace.
- S2: no network route to the compromised environment and no internet egress, shown by firewall rules plus traffic-flow logs with zero flows. Transfers come in one way only, through the custodian.
- S3: a separate identity store with no trust to the possibly compromised directory. Administration only from clean, dedicated workstations.
- S4: no vendor remote path. Vendor access stays unreinstated (PH01 7.5).
- S5: endpoint detection and logging into an independent store, with alerts on the known indicators.
- S6: separate key and hardware-security-module partitions.
- S7: no connection to live payment networks during testing; a test harness or simulator only.

TIMES (targets)
- 08:30: backup copy released.
- 09:00 to 12:00: checks I1–I4 and S1–S7.
- 12:00 to 16:00: build (I5–I8).
- Hourly status reports.
- Input for the Board paper by 18:00.

OWNER
- Accountable for integrity and separation, which is a PH01 9.3 gate item: SEC.
- Build: the IT Ops recovery team.
- Indicator scanning: the forensic firm.
- Backup copy: the evidence custodian.
- Consulted: the Head of Payments Ops.
- Production decision: the CMT chair, after the gate (PH01 s.3). The Board may narrow the scope, for example to payroll only (PH01 9.3).

DESTINATION / CHANNEL
- Work happens in the isolated recovery environment, and is recorded in the change record and evidence register.
- Decisions go in the decision log, through the CMT room or phone bridge.

BASIS: EXTERNAL
1. R03, HKMA Sectoral Code for Designated AIs, s.6.2.20(b)(i), PDF p17.
   - Requirement: a secure tertiary data backup (STDB), and where that is not feasible, "a backup copy that is physically disconnected from the CCS".
   - Authority: the HKMA's category 2 code.
   - Why it applies: the payment gateway is a critical computer system (CCS). This makes the immutable backup the proper data source.
2. R04, SPM TM-C-1, s.4.3, PDF p8: the STDB exists "to recover and restore critical data promptly in the event that a cyberattack compromises both the production and backup environments".
3. R08, SPM TM-G-1, s.4.2.4, PDF p18: "only properly tested and approved systems are promoted to the production environment. System and user acceptance testing should be carried out in an environment separated from the production environment."
4. R07, SPM TM-G-2.
   - s.4.6.2, PDF p13: access to backup vital records "should be adequately controlled to ensure that they are reliable for business resumption purposes".
   - s.4.3.3, PDF p11: plan for "the verification of the safety and readiness of the permanent site".
5. R01, Cap. 653, Schedule 3 Part 2 item 5, PDF p93: the emergency response plan must include "A recovery plan for resuming the provision of essential services". This applies through s.27(5) if PH01 is part of that plan (unverified).
6. Supporting good practice, not mandatory (R14a p2 says AIs are "encouraged" to review it): R14b, PDF p5, "setting up dedicated environments and utilities for recovery".
7. For LC: deploying the rebuilt gateway to production is likely a s.22 change event. R03 s.6.1.1, PDF p11: the event date is "the moment when a change is deployed to production environments". It is logged as a separate item (PH01 18.4).

NO DIRECT RULE LOCATED in the assigned sources for how to check backup timing, run the indicator scan, or test separation.
- Files searched: all allowed files.
- Terms: "immutable", "restor", "backup", "isolat", "failover".
- I1–I8 and S1–S7 are professional judgment.

BASIS: INTERNAL (Internal bank procedure: PH01, v1.0, effective 1 Oct 2026)
- s.9.1: "(1) A new build from trusted media with data from the immutable backup, in an isolated recovery environment; (2) the standby system, only if (1) fails, under the same checks. An affected system is never repaired in place for return to service."
- Also s.6.1, s.2.3, s.7.5, s.9.3 (the "integrity and separation checks passed" item) and s.18.4.

CONFLICT CHECK
- None found.

---------------------------------------------------------------
UNIT Q13b: Offline transaction reconciliation checks before the candidate is considered for production

PRECONDITIONS (PH01 9.2 and R08 4.2.4)
Before any production data, or an extract of it, is used in testing, SEC records two things in the test record:
- (i) The data has been de-sensitised, and the de-sensitisation checked. Method (judgment): deterministic tokenisation of names, identity card numbers, phone numbers and account numbers, with amounts, dates and references kept as they are, so that records still join for reconciliation. The tokenisation key is held separately by the custodian.
- (ii) The payments information owner approved the use in advance.
If either entry is missing, that data set is not used and testing with it is held.

CHECKS (all on the full set, each logged with evidence, signer and time)
- RC1, restore completeness: record counts and control totals (count and value by table, batch and value date) match the backup catalogue and the ledger as at the backup time.
- RC2, point-in-time match: every instruction in the restored state at backup time is either settled (ledger debit plus settlement record) or pending. No debit without a message, and no message without a debit.
- RC3, everything since the backup: every instruction from the backup time to cutover is classified settled, not settled or unknown, using:
  - the channels' authenticated instruction logs;
  - the gateway worklist copy;
  - the C04 secondary-process register;
  - the ledger and receiving-side records.
  Unknown items are held (PH01 8.6). Any instruction in the candidate with no authenticated source is a difference.
- RC4, tie-out with the alternate process: everything the secondary process released (count and value) matches ledger debits and receiving-side acknowledgements, and is marked completed in the candidate. This prevents paying twice at cutover.
- RC5, duplicate and replay rejection: inject tokenised duplicates, retries and replayed messages. The candidate must refuse a second release of the same processing ID and flag duplicates under the C04 control.
- RC6, static data: beneficiary, routing, limit and fee data match the independent baseline. Any change during the attacker's window must be explained.
- RC7, synthetic end-to-end run in the harness: ledger debit count and value equal outbound message count and value, which equal the simulated acknowledgements. Message format and signing with the new keys are verified. Nothing reaches a live network.
- RC8, payroll: batch totals match the SMEs' authenticated submissions.

PASS MARK (PH01 9.2)
- Zero unexplained differences across the full set.
- One unexplained difference is a FAIL. The cause is investigated and the test is rerun from the start.
- A sample result is recorded as a sample, not as a pass of the whole set.
- An offline pass describes only the isolated candidate (offline scope). It does not certify production.

AFTER AN OFFLINE PASS: the PH01 9.3 gate. Every item is logged with evidence and signer:
- the offline pass;
- integrity and separation checks (Q13a);
- rollback rehearsed to the target set in 9.5;
- the reconciliation plan for changes since the backup, and the live test plan, ready;
- business acceptance by the payments information owner;
- LC's confirmation of regulatory steps;
- the chair's authorisation.
Then the staged return under PH01 9.4: a live pilot of 20 instructions, then payroll at a capped rate, and so on. The stop rules of PH01 9.5 apply throughout.

OWNER
- Check design, test record and pass/fail: SEC.
- Execution: Payments Ops and the IT Ops recovery team.
- Data approval: the payments information owner.
- Production decision: the CMT chair.

TIMES (targets)
- 15:00: approval and de-sensitised data set ready.
- 16:00 to 22:00: RC1–RC8.
- The gate review is held only after a logged pass.

BASIS: EXTERNAL
1. R08, SPM TM-G-1, s.4.2.4, PDF p18.
   - Quote: "Production data should not be used in development or acceptance testing unless the data has been de-sensitised (i.e. not disclosing personal or sensitive information) and prior approval from the information owner has been obtained."
   - It reaches the CCS through R03 s.6.2.22(c), PDF p17: "Data used for testing should be carefully selected, protected and controlled ... relevant requirements outlined in SPM TM-G-1 section 4.2.4."
   - Why it applies: this is acceptance testing of the CCS candidate.
2. R09, SPM TM-E-1, s.5.1.2, PDF p19: "reconcile data file balances after transaction updates and to check the integrity of data transmitted between different systems". It applies to the e-banking instructions moving between systems.
3. R07, SPM TM-G-2, s.4.3.2, PDF p11: alternate processing "may entail record reconstruction and verification".
4. Supporting good practice: R14b, PDF p2, "reconciliation procedures to maintain accuracy following a bypass". This supports RC4.
5. R10, PDPO DPP4(1), PDF p169: test data is protected, hence tokenisation and separate key custody.

NO DIRECT RULE LOCATED externally for the pass mark or the RC1–RC8 design.
- Term "reconcil": hits are PH01, R09 p19, R14b p2 and an unrelated R16b p7.
- RC1–RC8 are professional judgment.

BASIS: INTERNAL (PH01 v1.0)
- s.9.2: "Before production data, or an extract of it, is used in testing, SEC records in the test record that the data has been de-sensitised and the de-sensitisation checked, and that the information owner approved its use in advance ... A candidate passes offline testing only if reconciliation shows no unexplained difference. One unexplained difference is a fail. A sample result is recorded as a sample, not as a pass of the whole set."
- Also s.8.6, s.9.3, s.9.4 and s.9.5.

CONFLICT CHECK
- None found. PH01 9.2 matches R08 4.2.4.

---------------------------------------------------------------
FACTS SEC PASSES TO THE INCIDENT TEAM

To LC, the DPO and COM: the public mirror.
- It holds 320 matching records, including the 80. That makes 240 newly verified affected people, who come under PH01 10.4(a).
- Under my C03 list, publication is evidence that INCREASES the estimate.
- If the 240 do not appear in the export logs, either log coverage is incomplete or there was another way out. The "excluded" category is then withdrawn until a fresh review under PH01 10.4(d).
- The 18,000 claim remains unverified.
- LC's related steps: an HKMA update at once (PH01 5.8), and supplementary information to the PCPD (R11 p8).
- The forensic firm captures and hashes the mirror. Staff do not visit it (PH01 6.6). Any takedown request is for LC and COM.

To LC, for the Police referral (Q14b). SEC can supply an evidence package with full custody records:
- hashed export and session log extracts;
- the vendor-credential timeline;
- indicators of compromise;
- the original demand and screenshot;
- the hashed mirror capture.
Personal data in it is kept to the minimum. Release goes through PH01 s.3 (LC reports to the Police; data release needs LC and SEC jointly, with the DPO consulted).

To COM: the fake verification page.
- SEC gives its domain and indicators to IT for blocking in bank channels, and to LC and COM for takedown. The page address is never published or clicked.
- SEC watches for e-banking login anomalies, in case harvested credentials are used.

To the chair:
- The attacker's deadline has passed, so the risk of further leaks or attacks is higher. Monitoring is stepped up, and any new attacker message goes into evidence only.
- The tolerance is at 100% and the Board must meet by 20:00.
- Recovery status for the Board paper (PH01 15.3): the candidate is being tested, and production is gated.

---------------------------------------------------------------
LOG-READY ACTIONS (HKT, status)
- 08:00: Candidate (1) chosen; standby held; original gateway held (executed).
- 08:30: SEC and LC joint release of the hashed backup working copy (scheduled).
- 09:00 to 12:00: Checks I1–I4 and S1–S7 (scheduled).
- 12:00: Backup suitability condition; default HOLD (scheduled).
- 12:00 to 16:00: Build from trusted media (I5–I8) (scheduled).
- 15:00: Information owner approval and de-sensitised data set (scheduled; testing held if missing).
- 16:00 to 22:00: RC1–RC8 offline reconciliation (scheduled).
- 18:00: Recovery status for the Board paper (scheduled).
- After a logged pass: PH01 9.3 gate review (conditional).