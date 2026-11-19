SEC (Information Security Lead): locked response for C06, Tuesday 17 Nov 2026, 20:00 HKT (H+36)

Assigned units: Q16a and Q16b only. I have taken the facilitator's handoff on the status of my Q13a and Q13b items into account.

Records that do not exist yet, and how I treat them:
- The handoff confirms that no card records the I1–I8 / S1–S7 results, the PH01 9.2 data preconditions, the RC1–RC8 results, or SEC's C04 clearance of the alternate process.
- I do not treat any of those as passed.
- No conflict was found between PH01 and any applicable external requirement for these units.

---------------------------------------------------------------
UNIT Q16a: Staged production recovery, hold, or a narrower service mode; the authorisation gate

DECISION
1. HOLD staged production recovery of the recovered image. No PH01 9.4 stage, including the 20-instruction pilot, may touch a live payment interface.
   - The lab test reconciled 118 of 120 instructions, and the 2 mismatches are unexplained. Under PH01 9.2, one unexplained difference is a FAIL.
   - 120 instructions is a sample. Even 120 out of 120 would be recorded only as a sample, not as a pass of the whole set.
   - So the first PH01 9.3 gate item (offline pass) is not met. No gate item may be waived (PH01 s.3).
2. A narrower recovered-system mode, such as Board-narrowed "payroll only", is also NOT available now.
   - PH01 9.3 lets the Board narrow the scope, but the narrower scope must still pass every applicable gate item.
   - While the cause of the mismatches is unknown, they cannot be shown to lie outside any narrower scope.
3. The only narrower service mode SEC will support tonight is the PH01 s.8 alternate process, payroll first (PH01 8.4). It is CONDITIONAL on SEC's clearance under PH01 8.2 being logged now:
   - checks C1–C7 from C04, with evidence;
   - a reconciliation check confirming that its own reconciliation ties (PH01 8.7).
   Condition in the PH01 2.3 four-item format:
   - Verifier: SEC.
   - Latest time: 21:00 HKT (judgment).
   - Default if not verified: HOLD. This is a security condition, so it can never default to going ahead.
   - Close-out: logged.
   If cleared, the chair activates (or confirms the earlier activation) and declares BCP activation (PH01 4.4); LC is told at once. Activation is the chair's decision (PH01 s.3), not SEC's.

ACTIONS (simulated, for the log)

H1, 20:00: decision log.
- Record "recovered image: offline FAIL (sample test 118/120, 2 unexplained); production HOLD".
- Record that it is unverified whether the image is the candidate (1) build that passed I1–I8 and S1–S7. If it is not, it is not an eligible candidate (PH01 9.1).

H2, 20:00 to 20:30: preserve evidence.
- Preserve the test record, the image hash, and the full trace of both mismatched instructions (inputs, candidate output, ledger, simulated acknowledgements) in the evidence register.
- Check whether the test record shows de-sensitisation and the information owner's prior approval (PH01 9.2; R08 4.2.4).
- If either is missing: log it as a breach of the test-data rule, tell LC and the DPO, and quarantine that data set. The FAIL result stands either way.

H3, 20:30: protect the live register.
- If the two mismatched items correspond to real queued instructions (re-identified through the custodian's tokenisation key), Payments Ops marks them "status unknown, held" in the live instruction register (PH01 8.6).
- This prevents the alternate process paying them wrongly or twice.

H4, by 23:00: preliminary root cause to the chair (judgment). For each mismatch, classify the cause as one of:
- (a) data in the backup or image corrupted or tampered with: the integrity check fails, so test the next-earlier immutable point, still candidate (1). The standby only if candidate (1) fails;
- (b) an error in reconstructing events since the backup, or a static-data difference;
- (c) a test-harness or tokenisation mapping error: fix it, document it, then rerun.
- Whatever the cause, a FULL-set rerun of RC1–RC8 is required, followed by a new pass through PH01 9.3. The 118/120 result stays on record as a fail.

H5. "No recurring encryption activity during the test window" is recorded as a limited observation. It does not replace the indicator scan (I4) or the separation checks (S1–S7).

AUTHORISATION GATE (PH01 9.3)
Production use of the recovered system needs ALL of the following, each logged with evidence and signer:
- (1) an offline pass under 9.2 on the full set, with the data preconditions logged;
- (2) integrity and separation checks I1–I8 and S1–S7 passed;
- (3) rollback rehearsed to the target set in 9.5 (Q16b);
- (4) the reconciliation plan for changes since the backup, and the live test plan, ready;
- (5) business acceptance by the payments information owner;
- (6) LC's confirmation of regulatory steps, including the Cap. 653 s.22 deployment record;
- (7) the CMT chair's (Chief Executive's) authorisation.
Then the PH01 9.4 stages, each advanced by the chair after the previous stage has run clean for the period set in the change record. Judgment for those periods:
- Stage 1: 20 instructions reconciled end to end.
- Stage 2: at least four consecutive clean hourly reconciliations before stage 3.
Passing a target time never releases the gate. Reports to regulators continue whatever the gate's state (PH01 2.4).

OWNER
- Gate evidence for items 1–3, plus the hold and the stop: SEC.
- Execution: Payments Ops and the IT Ops recovery team.
- Production authorisation: the CMT chair, after the full gate.
- The Board may narrow the scope but cannot waive any item.

TIMES
- 20:00: HOLD logged.
- 20:30: evidence and register flags.
- 21:00: alternate-process clearance, or HOLD.
- 23:00: preliminary root cause.
- Rerun and gate review only after the cause is explained.

DESTINATION / CHANNEL
- Decision log, test record, evidence register, instruction register.
- The CMT room or phone bridge, through the chair to the Board.

BASIS: EXTERNAL
1. R08, SPM TM-G-1, s.4.2.4, PDF p18.
   - Quote: "A formal acceptance process should be established to ensure that only properly tested and approved systems are promoted to the production environment."
   - Authority: HKMA supervisory policy module.
   - Why it applies: a candidate that failed reconciliation is not "properly tested".
2. R09, SPM TM-E-1, s.5.1.2, PDF p19: "reconcile data file balances after transaction updates and to check the integrity of data transmitted between different systems". Unexplained mismatches mean integrity is unverified.
3. R05, HKMA circular of 22 Jun 2010, PDF p1 (checked against the scan): "The top priority should be to safeguard the interests of customers". A system with unexplained mismatches risks wrong or duplicate payments. Payroll should therefore move only through a verified route.
4. R07, SPM TM-G-2, s.4.3.2, PDF p11: the full recovery phase "is as difficult and critical to the business as the process to activate the BCP".
5. R06, SPM OR-2, s.1.3 (PDF p3) and s.3.4 (PDF p6): the tolerance has now been exceeded. The Board "bears ultimate responsibility" for appropriate action. This calls for Board escalation (LC's Q17b), not for releasing an unsafe system.
6. For LC: R01 Cap. 653 s.22 and R03 s.6.1.1, PDF p11. Any later deployment of the rebuilt system to production is logged with its deployment time.

NO DIRECT RULE LOCATED externally for the pass mark or the gate items.
- Terms searched: "reconcil", "rollback", "rolling-back", "restor".
- Only PH01 9.2, 9.3 and 9.5 set them. The staging periods and the root-cause classes are professional judgment.

BASIS: INTERNAL (Internal bank procedure: PH01, v1.0, effective 1 Oct 2026)
- s.9.2: "One unexplained difference is a fail. A sample result is recorded as a sample, not as a pass of the whole set."
- s.9.3: "Missing any item means hold ... The Board may narrow the scope of recovery ... the narrower scope must still pass every item above that applies to it."
- s.3: "No gate condition may be waived."
- Also s.8.2, s.8.4, s.8.6, s.2.3, s.4.4 and s.9.1.

CONFLICT CHECK
- None found.

---------------------------------------------------------------
UNIT Q16b: Stop and rollback criteria for any production activity authorised

A. ALTERNATE PROCESS (the narrow mode, if cleared tonight)

Stop at once. SEC or the Head of Payments Ops may stop without prior approval and then tells the chair (PH01 8.7). Stop on any of:
- one unexplained difference in the hourly reconciliation (released count and value against ledger debits and receiving-side acknowledgements);
- any duplicate, replayed or wrong payment;
- any security indicator (list C below). This also suspends SEC's clearance.
Separately, an instruction whose status cannot be established is held on its own (PH01 8.6).

Rollback:
- All releases are suspended. There is no further fallback.
- In-flight items are classified settled, not settled or unknown from independent records. Unknown items are held.
- Restart needs the difference explained and logged. After a security indicator, SEC must re-clear (C1–C7 re-run for the affected element) and the chair must decide.

B. RECOVERED SYSTEM (only after the full gate)

Stop at once (PH01 9.5) on any of:
- a security indicator (list C);
- one unexplained reconciliation difference;
- any duplicate, replayed or wrong payment;
- an instruction whose status cannot be established.
Stop authority: SEC, the Head of Payments Ops, or the IT Ops duty manager, without prior approval.

Rollback:
- The IT Ops duty manager disconnects the recovered system from the payment interfaces. Target: within 15 minutes of the stop order (judgment). The time is rehearsed and recorded as gate item 3.
- SEC confirms the disconnection from traffic-flow logs.
- Service returns to the alternate process only if that process holds a current clearance and its reconciliation ties. Otherwise ALL releases are suspended.
- In-flight items are classified settled, not settled or unknown from independent records; unknown items are held.
- The recovered system's state and logs are preserved as evidence.
- Restart needs a NEW full pass through PH01 9.3.
- LC is told at once (a change in service status, PH01 5.8). COM updates the public status (PH01 11.2).

C. SECURITY INDICATORS (SEC's definition, judgment), applying to both A and B:
- Any match against the forensic firm's indicator list on the recovered or alternate hosts.
- Any authentication attempt using the revoked vendor credentials or tokens.
- Any connection to or from the isolated segment, the workspace, or known attacker infrastructure.
- Any unexpected admin account, privilege change or scheduled job.
- Encryption-like file activity (mass renames, high-entropy writes).
- Endpoint detection or logging switched off.
- Any payment message not traceable to a processing ID in the instruction register.
- Any new attacker contact claiming access to the recovery environment.

OWNER
- Definition of the criteria and of security stops: SEC.
- Reconciliation and holds: the Head of Payments Ops.
- Disconnection: the IT Ops duty manager.
- The chair is informed after every stop and decides restart after a security stop.

TIMES
- Reconciliation every hour of operation, plus a continuous check that no processing ID is released twice.
- Stop: immediate.
- Disconnection target: 15 minutes.

BASIS: EXTERNAL
1. R08, SPM TM-G-1, s.4.3.1, PDF p19: change management must include "a process for rolling-back changes to re-instate the original programs, system configuration or data in the event of production release problems" and "a post implementation verification of the changes made".
2. R09, SPM TM-E-1, s.5.1.2, PDF p19, as above.
3. R05, PDF p1, and R09 s.8.2.1, PDF p32: protect customers' interests.
4. For LC: R07, SPM TM-G-2, s.1.3.3, PDF p5: "periodic progress reports" to the HKMA after BCP activation.

NO DIRECT RULE LOCATED externally for the stop thresholds, the disconnection time or the indicator list.
- Terms searched: "rollback", "rolling-back", "stop", "reconcil".
- The 15-minute target and list C are professional judgment. The thresholds come from PH01.

BASIS: INTERNAL (PH01 v1.0)
- s.9.5: "Releases from the recovered system stop at once on any of: a security indicator from the incident; one unexplained reconciliation difference; any duplicate, replayed or wrong payment; an instruction whose status cannot be established ... Rollback disconnects the recovered system from payment interfaces ... Restart needs a new pass through 9.3."
- Also s.8.6 and s.8.7.

CONFLICT CHECK
- None found.

---------------------------------------------------------------
FACTS SEC PASSES TO THE INCIDENT TEAM

To the chair and the Board (through LC's Q17b):
- The recovery candidate failed offline testing. Production is held. The root cause is due by 23:00.
- The tolerance has been exceeded since about 08:00 today.
- The Board may narrow the scope, but cannot waive any gate item.
- Tonight's service depends on the alternate-process clearance due at 21:00.

To LC:
- Service status for the HKMA and Commissioner updates: still not available, or provided by the alternate process if cleared (R02 Annex F, section D.2).
- A possible breach of the test-data rule, if the H2 records are missing.

SEC's co-decision position on the forensic firm's request. Under PH01 s.3, sharing data with a third party needs LC and SEC jointly, with the DPO consulted, so SEC gives its position for LC's Q17a:
- No transfer of the full diagnostic image by default (PH01 16.2).
- The firm's staff may examine the full image inside the bank's laboratory, or receive a minimised, masked extract.
- A full copy leaves the bank only with LC's and SEC's written approval, for a stated need that cannot be met in the lab, under the PH01 s.16 agreement terms, and recorded in the data release record.

To Payments Ops and COM:
- The two mismatched items are held.
- Counterparty requests are answered only after a verified call-back (PH01 14.2), with status taken from the register.
- Missed payroll cut-offs are covered by PH01 13.2 (reimbursement on claim). Payroll stays first in the queue (PH01 8.4).

---------------------------------------------------------------
LOG-READY ACTIONS (HKT, status)
- 20:00: Recovered image offline FAIL; production HOLD (executed).
- 20:00 to 20:30: Test record, image hash and mismatch traces preserved; data preconditions checked (scheduled).
- 20:30: Mismatched items held in the live register if they map to real instructions (scheduled).
- 21:00: Alternate-process clearance under PH01 8.2, or HOLD (scheduled; default HOLD).
- 23:00: Preliminary root cause to the chair (scheduled).
- Full-set RC1–RC8 rerun: held until the cause is explained.
- PH01 9.3 gate: held.
- Continuous: stops under A and B (trigger).