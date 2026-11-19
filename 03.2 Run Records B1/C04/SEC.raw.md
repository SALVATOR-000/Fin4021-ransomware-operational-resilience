SEC (Information Security Lead): locked response for C04, Monday 16 Nov 2026, 18:00 HKT (H+10)

Assigned units: Q10a and Q10b only. The C01–C03 reports were handed back earlier. No facilitator handoff was addressed to SEC for C04. The dispatch records being supplied from C01 are for LC's Q11; SEC does not rely on them here.

Authority for these units:
- SEC does not activate the secondary process. Under PH01 s.3 the CMT chair activates it, on SEC's written security clearance, after consulting the Head of Payments Ops.
- SEC's decision is whether to give that clearance, and on what conditions. Payments Ops owns the instruction register and releases payments.
- SEC defines the security and integrity controls and may stop releases without prior approval (PH01 8.7).

Facts not known at this card:
- Whether the C03 closure test and persistence sweep have been logged as passed.
- Whether the "secondary process" is the PH01 s.8 alternate payment process, or the standby gateway. I assume it is the s.8 process. If it is the standby gateway, it is a held system (PH01 6.1 and my C01 hold A7), it may be used only if a new build fails (PH01 9.1), and SEC gives no clearance.
- Whether the secondary process shares any host, directory, account, key or network path with the gateway.
- How many of the about 4,200 instructions are duplicates.
- Payroll value dates, and receiving-side settlement hours.
- Whether SME authorised contacts can be reached tonight.
- The exact time the disruption started.

---------------------------------------------------------------
UNIT Q10a: Whether to use the secondary process, and how to prioritise queued payments

DECISION
- SEC recommends using the secondary process.
- SEC's written clearance under PH01 8.2 is CONDITIONAL on checks C1–C7 below, logged with evidence by 19:00 HKT.
- The condition is recorded in the PH01 2.3 four-item format:
  - Verifier: SEC, consulting the Head of IT Ops.
  - Latest time: 19:00.
  - Default if not verified: HOLD. This is a security condition, so it can never default to going ahead.
  - Close-out: an entry when the checks pass or the hold is applied.
- If held, SEC re-checks hourly and tells the chair what the hold means for the tolerance.

CLEARANCE CHECKS (SEC, with IT Ops; each logged with its evidence reference)
- C1, hosts: no host, virtualisation cluster, storage or management plane is shared with the gateway or the C03 workspace.
- C2, accounts: no shared admin, service or vendor accounts. No account belonging to the vendor exists or is active on the secondary process. No account used by the attacker during its access window has any rights there.
  - If the secondary process authenticates through the same directory, and the C03 sweep found privileged directory compromise: no clearance.
- C3, keys: signing keys, certificates, hardware-security-module partitions and interface credentials are separate from the gateway's (the gateway's were suspended at C01). Any shared key is rotated before use.
- C4, network path: no route from the isolated gateway segment or the workspace. Checked by reviewing firewall rules and confirming zero traffic flows during the attacker's access window.
- C5, clean: a sweep for the forensic firm's indicators of compromise (file hashes, IP addresses, tools, persistence) comes back clean. Endpoint detection and independent logging are active.
- C6: the C03 closure test is logged as passed on every access path (PH01 7.4).
- C7: instructions come into the secondary process only as a hashed export carried by the evidence custodian. The secondary process never connects to the gateway.
- The clearance is "current" only while no security indicator appears. SEC re-confirms it in each hourly status report. Any indicator suspends it at once.

ACTION SEQUENCE (simulated, for the log)

P1, 18:00 onward, in parallel and not waiting for clearance:
- Payments Ops builds the single instruction register (Q10b).
- Payments Ops starts payroll call-backs to SME authorised contacts on numbers already on file (PH01 8.5).
- Reason: verification, not machine capacity, is likely the real bottleneck at night.

P2, 18:30: worklist copy of the gateway queue.
- The queued instructions sit on the gateway, which is under evidence hold.
- SEC and LC jointly approve a hashed, read-only copy for use as a worklist only, with the forensic lead consulted (PH01 s.3, release of held evidence). The original stays on hold.
- The copy is not the authority for any payment. Each instruction is checked against the customer's original authenticated instruction (PH01 8.5), because the attacker could issue commands on the gateway.

P3, 19:00: SEC's written clearance, or the hold, is logged.

P4, about 19:15:
- The chair decides activation and declares BCP activation in the decision log (PH01 4.4).
- LC is told at once. Activation is something LC must act on:
  - R07 1.3.3 (inform the HKMA promptly if the BCP is activated);
  - PH01 5.8;
  - R02 7.3.4(c) (BCP activation is a serious-incident criterion);
  - R01 s.22(2)(d), if the secondary process thereby becomes essential to the core function.
- SEC logs the activation and deployment times for LC's assessment.

P5, about 19:15 to 20:15: pilot of no more than 20 instructions (PH01 8.3).
- Composition (judgment): verified SME payroll items with the earliest value dates. No retries, suspected duplicates or items of unknown status.
- Each item is reconciled end to end: ledger debit, outbound message, and receiving-side acknowledgement.
- Each gate passed and the pilot result are logged with the time.
- Full operation starts only if the pilot reconciles with no unexplained difference.

P6, from about 20:15: full operation.
- Priority order (PH01 8.4):
  - (1) SME payroll, earliest value date first; ties in order of submission (judgment);
  - (2) other instructions with a value date of today or the next business day;
  - (3) everything else in order of submission.
- About 40 per hour (10% of capacity) is reserved for urgent cases referred by branches and the contact centre.
- Order is never set by customer size.
- Count, value, ledger debits and receiving-side acknowledgements are reconciled every hour (PH01 8.7).

FACTS FOR THE CHAIR (tolerance and capacity)
- About 4,200 instructions (including retries) at about 360 an hour for the queue is about 11.7 hours.
- From about 20:15, the queue clears at about 08:00 Tuesday at the earliest, with no stops and every item verifiable.
- The 24-hour tolerance runs out about 08:00 Tuesday if the disruption began at 08:00, and earlier if it began earlier.
- So the 24-hour tolerance is at risk for the tail of the queue, and for every held item.
- 50% of the tolerance falls at about 20:00, when the chair must tell the Board chair (PH01 4.3).
- 100% falls about 08:00 Tuesday, which triggers a Board or Risk Committee meeting within 12 hours (PH01 15.2).
- Payments Ops must confirm the receiving-side settlement hours. SEC has no information on them.
- Removing duplicates will shrink the queue, and the payroll call-back rate may become the real limit.

STOP TRIGGERS (SEC or the Head of Payments Ops, no prior approval needed; the chair is told afterwards)
- Any unexplained reconciliation difference.
- Any duplicate, replayed or wrong payment.
- Any security indicator on the secondary process, or any use of the old credentials. This also suspends SEC's clearance.

OWNER
- Clearance: SEC.
- Activation and BCP declaration: the CMT chair, after consulting the Head of Payments Ops.
- Operation and release: Payments Ops.
- Release of the worklist copy: SEC and LC jointly.

TIMES
- Clearance or hold by 19:00.
- Activation about 19:15.
- Pilot about 19:15 to 20:15.
- Full operation from about 20:15.
- Hourly reconciliation after that.
- 50% tolerance at about 20:00.

DESTINATION / CHANNEL
- Changes are made on the secondary-process hosts and firewalls (checks and key rotation) and in the instruction register.
- Clearance, activation and gate records go in the decision log and the BCP activation entry.
- Discussion happens in the CMT room or on a phone bridge. Nothing goes by corporate email unless email has been logged safe.

BASIS: EXTERNAL
1. R06, SPM OR-2 Operational Resilience, s.1.3, PDF p3.
   - Quote: an AI must "Continue to deliver critical operations when disruptions occur ... disruptions to an AI's critical operations must not exceed its 'tolerance for disruption'".
   - Authority: HKMA supervisory policy module.
   - Why it applies: transfers and payroll are a critical operation with a 24-hour tolerance, and that tolerance is now at risk.
2. R07, SPM TM-G-2 Business Continuity Planning.
   - PDF p3, definition: a recovery strategy includes "use of another delivery channel to provide the same operation".
   - s.4.3.2, PDF p11: the alternate processing phase "may entail record reconstruction and verification, establishment of new controls".
   - s.3.2.2, PDF p8: "The result of the time-frame assessment in the business impact analysis is the key determination factor for the recovery priority".
   - s.1.3.3, PDF p5: "AIs should inform the HKMA promptly if their BCP is activated." (for LC)
3. R02, OCCICS Code of Practice v1.0, s.7.2.4(a), PDF p34: "sustaining the CI operator's ability to continue essential operation during disruptions arising from computer-security incidents". It applies through the bank's emergency response plan (category 3).
4. R05, HKMA circular of 22 Jun 2010, PDF p1 (checked against the scan): "The top priority should be to safeguard the interests of customers". This supports moving payroll and also not releasing unverified items.
5. Supporting principle, by analogy (its own context is Board prioritisation of remediation): R06 s.3.4, PDF p6, "prioritise a critical operation that would more sooner breach its tolerance for disruption".

NO DIRECT RULE LOCATED in the assigned sources for the security-clearance criteria or the order within the queue.
- Files searched: all allowed files.
- Terms: "priorit", "payroll" (hits PH01 only), "workaround", "alternate", "failover".
- C1–C7 and the tie-break rule are professional judgment.

BASIS: INTERNAL (Internal bank procedure: PH01, v1.0, effective 1 Oct 2026)
- s.3: "Activate alternate payment processing (section 8) | CMT chair, on SEC's written security clearance".
- s.8.2: clearance "that it shares no hosts, accounts, keys or network path with any affected system".
- s.8.3: "The first batch is a pilot of at most 20 instructions, reconciled end to end before full operation."
- s.8.4: "(1) SME payroll, earliest value date first ... Up to 10% of hourly capacity is kept for urgent cases ... Order is never set by customer size."
- Also s.2.3, s.4.3, s.4.4, s.6.1, s.8.5, s.8.7, s.9.1 and s.15.2.

CONFLICT CHECK
- None found.
- If SEC withholds clearance, the hold leads to a tolerance breach. PH01 deals with that by escalating to the Board (s.4.3 and 15.2), not by going ahead. That is consistent with R06, which requires delivery within tolerance but not on an unsafe platform.

---------------------------------------------------------------
UNIT Q10b: Control for retried payments and possible duplicates before processing

DECISION: the control is in force before the pilot. Payments Ops runs it; SEC sets the integrity conditions.

D1, single register (PH01 8.6).
- One instruction register covers every source: the gateway worklist copy, e-banking channel records, branch forms, SME payroll files, and retries.
- Each instruction gets a unique processing ID and a status: queued, verified, released, settled, returned, held-duplicate, held-unknown, or held-unverified.

D2, source of truth.
- Every instruction must match the customer's original authenticated instruction in the channel's own records: e-banking authentication and audit logs, signed branch forms, or authenticated payroll submissions (PH01 8.5).
- The gateway copy is never sufficient, because the attacker could issue commands on the gateway.
- Any instruction created or changed during the attacker's window that has no matching authenticated source is held for review by Fraud and SEC.

D3, duplicate detection (judgment).
- Flag as a suspected duplicate: same debit account, same beneficiary, same amount, within the incident period, across all channels and references.
- Same debit account and amount but a different beneficiary is flagged for Fraud review, because it could be a redirection scam.

D4, before releasing any suspected duplicate or retry, two checks are made and logged (PH01 8.6):
- (a) Intent: the customer or SME authorised contact confirms which instruction they want paid, by a bank-initiated call-back to a number already on file. Inbound confirmations are never accepted.
  - Judgment: for the 80 confirmed-exposed customers, and the possible group from C03, add a verification question not based on exposed data. Any contact details changed after the incident started are checked by Fraud before use (PH01 10.5 by analogy).
- (b) Status: the ledger, and an independent receiving-side record, show whether the original was posted or settled. Payments Ops obtains receiving-side records only through counterparty contacts verified by call-back (PH01 14.2).
- If either check is incomplete, the item is held.

D5, in flight at the failure. Items in flight when the gateway failed are "status unknown" until an independent record shows they did not settle. They are never re-sent on assumption (PH01 8.6).

D6, release once only.
- The secondary process rejects any second release of the same processing ID.
- Judgment: releases use maker-checker dual control.

D7, hourly reconciliation (PH01 8.7). Released count and value are reconciled against ledger debits and receiving-side acknowledgements. Any unexplained difference stops ALL releases until it is explained and logged.

D8, stop triggers.
- Any duplicate, replayed or wrong payment; any instruction whose status cannot be established; any security indicator.
- SEC or the Head of Payments Ops stops without prior approval and then tells the chair.

D9, dependencies for others (no decision taken here).
- Mobile transfer submission stays closed. SEC gives no clearance to reopen it.
- COM should advise customers not to retry. That is COM's wording.
- Any loss from a duplicate is handled under PH01 13.2 or 13.3.

OWNER
- Register and release: the Head of Payments Ops.
- Integrity conditions and stop authority: SEC.
- Fraud reviews flagged items. The custodian and LC handle the worklist copy.

TIMES
- In force before the pilot (about 19:15).
- Reconciliation every hour of operation.

DESTINATION / CHANNEL
- The instruction register and the secondary-process controls.
- Customer call-backs go only to numbers already on file.
- Counterparty contact uses only verified call-back.

BASIS: EXTERNAL
1. R09, SPM TM-E-1 Risk Management of E-banking, s.5.1.2, PDF p19.
   - Quote: "AIs should also implement sufficient controls to maintain and verify the integrity of the information processed by their Internet banking systems ... reconcile data file balances after transaction updates and to check the integrity of data transmitted between different systems."
   - Authority: HKMA supervisory policy module.
   - Why it applies: retried and queued e-banking instructions are being moved from the gateway and the channels into the secondary process.
   - Left to judgment: the duplicate-matching rule.
2. R07, SPM TM-G-2, s.4.3.2, PDF p11: alternate processing "may entail record reconstruction and verification, establishment of new controls".
3. R05, PDF p1, and R09 s.8.2.1, PDF p32: the customer's interests are the top priority. Wrong or duplicate payments harm customers.

NO DIRECT RULE LOCATED externally for duplicate or retry controls.
- Term "duplicate": hits only PH01 and an unrelated R07 p5.
- Other terms searched: "integrity" (R08, R09), "reconcil" (R08: no hits).

BASIS: INTERNAL (PH01 v1.0)
- s.8.6: "Each instruction is released once only, under a unique processing ID. Before a suspected duplicate or a retried instruction is released, two checks are made and logged: (a) intent ... (b) status ... If either check is incomplete, or the status of an instruction cannot be established, the instruction is held. Items in flight at the failure are held as status unknown until an independent record shows they did not settle."
- s.8.7: "Any unexplained difference stops all releases until it is explained and logged."
- Also s.8.5 and s.14.2.

CONFLICT CHECK
- None found.

---------------------------------------------------------------
FACTS SEC PASSES TO THE INCIDENT TEAM
- To the chair: the tolerance and capacity forecast above; the 20:00 Board-chair notice; the 08:00 Tuesday 100% point; the clearance status at 19:00.
- To LC, at once when the chair activates: the activation time, and the deployment time of the secondary process, for HKMA, Commissioner and s.22 purposes. Held items and any duplicate incidents go into later updates.
- To Payments Ops: start payroll call-backs now; confirm settlement hours; the worklist copy is not authority for any payment.
- To COM: customers should not retry; held payments are being verified; no completion time is to be published until Payments Ops confirms it from the register (PH01 11.4).
- To COM and the contact centre: urgent-case referrals use the reserved 40-an-hour lane. Customers who cannot reach a branch need a working referral route (COM's Q12b).

---------------------------------------------------------------
LOG-READY ACTIONS (HKT, status)
- 18:00: Clearance checks C1–C7 started; register and payroll call-backs started (executed).
- 18:30: SEC and LC joint release of the worklist copy of the gateway queue (scheduled).
- 19:00: Written clearance under PH01 8.2, or HOLD in the 2.3 format (scheduled).
- About 19:15: Chair's activation and BCP declaration; LC told (decision for the chair).
- 19:15 to 20:15: Pilot of no more than 20 instructions (scheduled, conditional on clearance).
- 20:00: 50% tolerance, Board-chair notice (chair).
- 20:15 onward: Full operation with hourly reconciliation (conditional on the pilot).
- Continuous: Stop on any trigger in D8 or the Q10a list (trigger).