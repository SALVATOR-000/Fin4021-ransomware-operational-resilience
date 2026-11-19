SEC (Information Security Lead) response to C06, locked. Tuesday 17 Nov 2026, 20:00 HKT (H+36). Units covered: Q16a and Q16b only. I have taken the facilitator's handoff on Q13a/Q13b as the record. All actions below are simulated, for the facilitator to log.

**Facts at this card**
- Confirmed from C06:
  - A pre-arranged offline lab test on "a recovery image" reconciled 118 of 120 instructions. The 2 mismatches are unexplained.
  - No recurring encryption activity was seen in the lab's test window.
- Not verifiable from the record (per the handoff):
  - Whether that image is the Q13a candidate-1 build.
  - Whether separation validation, the backup timing and integrity checks, and the test-data records (de-sensitisation and owner approval) were completed.
  - Whether the secondary process holds a current SEC clearance under PH01 s.8.2. My C04 clearance decision is not recorded on any card.
- Context: the disruption is about 36 hours old, well past the 24-hour tolerance. SMEs are reporting missed payroll cut-offs.

== Q16a: Start staged recovery, hold, or narrower mode, and the authorisation gate ==

**Decision**
1. **Recovered system: HOLD.** No staged production recovery and no production pilot from the recovered image, including a payroll-only scope.
   - The offline test failed. The pass mark is zero unexplained differences and there are 2.
   - 120 instructions is a sample, so even a clean result would not have been a pass of the whole set.
   - The other gate items are unverified.
   - A narrower scope set by the Board does not help: it must still pass every gate item that applies to it, and the offline pass is missing.
2. **Narrower service mode: conditional. The secondary (alternate) process may run for SME payroll first, but only if it holds a current SEC clearance under s.8.2.** Because that clearance is not on record:
   - I carry out or re-confirm the clearance now. The written result is due by 21:00 HKT.
   - It checks that the secondary process shares no hosts, accounts, keys or network path with any affected system, the candidate image or the lab environment.
   - It also covers: the incident's indicators of compromise, the vendor-account exclusion, the status of the credential closure test, and key separation.
   - I attach the evidence for each check.
   - If clearance is given: the Chief Executive (CMT chair) may activate or continue the process. This counts as BCP activation. LC is told so the HKMA can be informed. A pilot of up to 20 instructions comes first if this is a first activation. Priority order follows s.8.4 (payroll, earliest value date first). Duplicate and status checks follow s.8.6. Reconciliation is hourly, with a stop rule.
   - If clearance is refused or cannot be completed by 21:00: the default is hold. This is a security condition, so it never defaults to going ahead. All releases stay suspended and the Chief Executive and Board are told the same night.
   - Condition record (s.2.3): verifier SEC; latest time 21:00 HKT; default hold; close-out entry required.
3. **Fixing the failed test (no production effect):**
   - Prove the image's identity: compare its SHA-256 and build record with the Q13a candidate.
   - Root-cause each mismatch. Likely causes are tampered static or instruction data in the backup, timing at the delta cut-off, a duplicate or replay, or a fault in the test harness.
   - Any mismatch involving beneficiary, amount or account changes goes to Fraud as suspected tampering.
   - Retrieve and log the missing Q13a records: separation, backup timing against the dwell period, and the test-data entries.
   - After a fix, re-run the full reconciliation set, not only the 2 items.
   - A new pass under s.9.2 is required, followed by every s.9.3 item.
   - "No recurring encryption in the test window" is lab-scope evidence only. It does not show that the image is free of dormant persistence, and it says nothing about the production environment.

**Authorisation gate for any later production use (PH01 s.9.3)**
All of the following must be logged with evidence and signer:
- offline pass on the full set;
- integrity and separation checks passed;
- rollback rehearsed to the defined target;
- delta reconciliation plan and live test plan ready;
- business acceptance by the payments information owner;
- LC confirmation of regulatory steps;
- authorisation by the Chief Executive (CMT chair).

No item may be waived. The Board may narrow the scope, but only through a Board minute.

**Owner and executing parties**
- Owner and accountable for the security recommendation and clearance: SEC.
- Head of IT Operations: rebuild and root cause.
- Head of Payments Operations: reconciliation and secondary-process operation.
- Production authorisation: Chief Executive alone, after the gate.

**Times**
- Clearance decision on the secondary process: 21:00 HKT.
- Root-cause interim: next SEC status report.
- Full-set re-test: when the fix is ready. This is a professional-judgment target, not a time-driven release.

**Recipients and channels**
- Decision log entry: recovered system HOLD, status "held".
- Written clearance or refusal to the Chief Executive.
- Briefing pack to the Board or Risk Committee, which is engaged because tolerance has been exceeded (PH01 s.4.3).
- Facts to LC for the HKMA update (change in service status, BCP).
- Facts to COM for Q18. Do not announce a recovery date.

**Basis: external**
- **R08, SPM TM-G-1, s.4.2.4, PDF p.18:** "A formal acceptance process should be established to ensure that only properly tested and approved systems are promoted to the production environment."
  - Authority: HKMA supervisory guidance. The recovered gateway is a system being promoted to production. A failed reconciliation means it is not "properly tested". The pass threshold is left to the bank; PH01 sets it at zero.
- **R03, HKMA Sectoral Code, s.6.2.22(c), PDF p.17:** "Data used for testing should be carefully selected, protected and controlled".
  - Applies to the designated critical computer system (CCS). The test-data records for this lab test are unverified.
- **R07, SPM TM-G-2, s.1.3.3, PDF p.5:** "AIs should inform the HKMA promptly if their BCP is activated."
  - Applies to any use of the secondary process. LC acts on it.
- **R05, HKMA circular of 22 Jun 2010, p.1, "Immediate incident response":** "The top priority should be to safeguard the interests of customers who have been or may be affected by the incident."
  - Supports an alternate route for payroll that is cleared and controlled, rather than an untested system. Releasing wrong or duplicate payments would harm customers further.
- **R06, SPM OR-2, s.3.4, PDF p.6:** prioritise the "critical operation that would more sooner breach its tolerance". Treated as a general principle supporting payroll-first.

**Basis: internal (Internal bank procedure, PH01 v1.0)**
- **s.9.2:** "One unexplained difference is a fail. A sample result is recorded as a sample, not as a pass of the whole set."
- **s.9.3:** "Missing any item means hold: releases from the recovered system stay suspended, or service continues on the alternate process if it holds a current security clearance under 8.2 and its own reconciliation ties."
- **s.3 (Authority matrix), "Return a recovered system to production":** decided by the CMT chair after the gate in 9.3. "No gate condition may be waived."
- **s.8.2:** activation only "after SEC's written clearance".
- **s.2.3:** security conditions default to hold.
- **Conflict check:** none. PH01 and R08 s.4.2.4 point the same way.

== Q16b: Stop and rollback criteria for any authorised production activity ==

**Decision.** The criteria below apply now to the secondary process, if it is cleared, and later to any staged recovery.

**Stop triggers.** Any one is enough. Releases stop at once with no prior approval needed. SEC, the Head of Payments Operations or the IT Operations duty manager may call the stop, then tell the Chief Executive.
1. Any security indicator from the incident, including:
   - encryption activity or ransomware artefacts;
   - a hit on the incident's indicators of compromise;
   - any use of the vendor identifiers or captured tokens;
   - an unexpected outbound connection or admin logon;
   - a change to a configuration or key outside the change record.
2. One unexplained reconciliation difference: count or value of releases against ledger debits and receiving-side acknowledgements, checked hourly (and at the end of each pilot or stage).
3. Any duplicate, replayed or wrong payment, including a payee or amount that differs from the original authenticated instruction.
4. Any instruction whose status cannot be established.
5. A counterparty or clearing report of a rejected, unmatched or duplicate message that cannot be explained.
6. Loss of monitoring or logging on the live path. If the system cannot be seen, it does not run.

**Rollback (recovered system)**
- IT Operations, on the stop call, disconnects the recovered system from the payment interfaces at the network layer and preserves its state. No power-off.
- The evidence custodian captures logs and the queue state.
- Service returns to the secondary process only if it holds a current s.8.2 clearance and its own reconciliation ties. Otherwise all releases are suspended.
- In-flight items are classified as settled, not settled or unknown, using independent ledger and clearing records. Unknown items are held.
- Restart needs a fresh pass through the full s.9.3 gate, with the stop cause explained and logged.

**Stop (secondary process)**
- The stop halts all releases.
- The instruction register is frozen.
- Resumption needs the difference explained and logged, under s.8.7. Where the stop was a security indicator, SEC must also re-confirm clearance.

**Rehearsal precondition**
- Before any recovered-system stage, the rollback is rehearsed to the defined target and logged. This is a gate item.
- If no cleared secondary process exists, the rehearsed target is "suspend all releases".

**Owner and executing parties**
- Accountable for criteria and security triggers: SEC.
- Head of Payments Operations: reconciliation triggers.
- IT Operations duty manager: disconnection.
- Chief Executive: informed at once and decides any restart through the gate.

**Times**
- Criteria apply from the first release.
- Reconciliation every hour.
- The stop is immediate on any trigger, with a decision-log entry within minutes.

**Recipients and channels**
- Change record, decision log, instruction register, evidence register.
- Immediate notice to the Chief Executive.
- Facts to LC: a change in service status triggers an HKMA update.
- Facts to COM and Payments Operations for counterparty status (Q18b).

**Basis: external**
- **R08, s.4.3.1, PDF p.19:** change management includes "a process for rolling-back changes to re-instate the original programs, system configuration or data in the event of production release problems".
- **R14b, HKMA good-practices annex, s.A.1, PDF p.1:** "controlled auto-retry logic (e.g. duplication checks when re-attempting transactions)". Good-practice support for trigger 3.
- **R05, p.1:** safeguard affected customers' interests.

**Basis: internal (Internal bank procedure, PH01 v1.0)**
- **s.9.5:** "Releases from the recovered system stop at once on any of: a security indicator from the incident; one unexplained reconciliation difference; any duplicate, replayed or wrong payment; an instruction whose status cannot be established." Also: "Rollback disconnects the recovered system from payment interfaces." And: "Restart needs a new pass through 9.3."
- **s.8.7:** "Any unexplained difference stops all releases until it is explained and logged."
- **s.8.6:** unknown items are held.
- Triggers 5 and 6 are my professional-judgment additions. They are consistent with s.9.5.
- **Conflict check:** none.

== Facts I am passing to the incident team ==
1. **Chief Executive and Board:**
   - Recovered system on HOLD (failed offline test: 2 unexplained of 120, and the 120 is a sample only).
   - Clearance decision on the secondary process due 21:00.
   - Tolerance exceeded.
   - No recovery date can be given.
   - Board scope-narrowing would not bypass the failed test.
2. **LC:**
   - Service status unchanged, with the recovered system held.
   - Whether the secondary process is or will be active (BCP and HKMA update).
   - On Q17a: the diagnostic image contains customer data. A full copy leaves the bank only with LC and SEC written approval. The firm gets a masked minimum set by default and examines full images inside the bank's lab.
   - SEC recommends: give a masked or minimised extract scoped to the two mismatches and the indicators of compromise. Offer in-lab access for anything more.
3. **COM and Payments Operations (Q18):**
   - Unsettled instructions remain held as "status unknown" until independent records confirm them.
   - Any counterparty status update must say only what the register confirms.
   - Duplicate protection is in force.
4. **Fraud:** if root cause shows tampering, the two mismatched instructions and their account identifiers go to Fraud.