SEC (Information Security Lead), locked response for C04: Monday 16 Nov 2026, 18:00 HKT (H+10). This covers only Q10a and Q10b. No handoff was addressed to SEC for this card.

Facts I am working from:
- The original gateway is still impaired.
- About 4,200 instructions are queued, measured independently. They include time-sensitive SME payroll. The figure probably counts retries, so the number of unique instructions is unknown.
- The secondary process can handle up to 400 verified instructions an hour, if approved.
- Some customers retried after a timeout.
- Still unverified from earlier cards: whether the secondary process is separate from the affected estate, and whether the queued data is intact.

All actions below are simulated, for the facilitator to log.

== Q10a: Whether to use the secondary process, and in what priority order ==

**Decision.** I support using the secondary process. It goes ahead only if I give written security clearance and the CMT chair then activates it. Until clearance is given, it is on hold.

My recommendation is driven by the deadline:
- The 24-hour tolerance for transfers and payroll ends at 08:00 HKT on 17 Nov.
- 50% of tolerance is reached at 20:00 tonight. At that point the CMT chair must tell the Board chair.
- 10% of hourly capacity is kept back for branch and contact-centre urgent cases, which leaves about 360 an hour for the queue.
- At that rate, 4,200 items take about 11.7 hours. Starting around 20:00 means finishing around 07:40, with almost no margin.
- I will tell the CMT chair now that the lowest-priority tail may go past tolerance. They should prepare to convene the Board or Risk Committee under PH01 4.3. That is the chair's decision.

**Action 1: security clearance review, 18:00 to 19:00 HKT.** The work is done by SEC engineers, IT Operations and Payments Operations.

Before I sign, each item below is checked and the evidence is logged:
- (i) **No shared hosts, accounts, keys or network path with any affected system.** This is checked against the live firewall rules, routing, directory groups, privileged access entitlements, the HSM and key inventory, and certificate stores.
  - Specifically excluded: every account of the support vendor, and any account or token whose closure test from C03 has not passed.
  - If a signing key or certificate is shared with the gateway, it is rotated before use, or clearance is refused.
- (ii) **The secondary hosts are clean.** EDR scans and a sweep for the incident's indicators (file hashes, IP addresses and domains, tools, persistence artefacts) find nothing.
- (iii) **Operator access is controlled.** Operators use named accounts with MFA. Any reused credentials are rotated. No vendor remote path exists.
- (iv) **The input is not trusted just because it sat in the queue.** The queue sits on a held, compromised system and could have been changed.
  - Instructions are rebuilt from records outside the gateway, such as channel and core-ledger records of the customer's original authenticated instruction, or the SME's original upload.
  - Each one is checked against that original before release.
  - Data comes off a held system only if SEC and LC jointly log a release. The forensic lead is consulted first, and a hashed copy is preserved.
- (v) **Monitoring and alerting are live** on the secondary process, and run only through a channel that does not depend on corporate email.

**Condition** (four elements, as PH01 2.3 requires):
- Verified by: SEC.
- Latest time: 19:00 HKT.
- Default if not verified: hold. This is a security condition, so it never defaults to going ahead.
- Close-out: an entry when clearance is signed or refused.

If any item fails, I refuse clearance in writing and give the reason. The CMT chair then decides whether to escalate. I will not give a partial clearance unless the scope is defined, for example payroll only through a path that has been separately cleared.

**Action 2: pilot and release, after the chair activates.**
- Activation counts as a BCP activation. The CMT chair logs it, and LC is told at once so the HKMA can be informed.
- The pilot is no more than 20 instructions, all SME payroll. It must be reconciled end to end and logged before full operation starts. Target: pilot about 19:30, full run about 20:00.

**Priority order:**
1. SME payroll, earliest value date first.
2. Other instructions with a value date of today or the next business day.
3. Everything else, in order of submission.

Customer size never sets the order. Items released under the urgent reserve are logged with the referral source.

Professional judgment: when payroll batches have the same value date, I would put batches that are already verified and confirmed by call-back ahead of those still awaiting call-back. That keeps throughput up without changing the rule.

**Reconciliation and stop triggers:**
- Every hour, the count and value released are reconciled against ledger debits and acknowledgements from the receiving side.
- Releases stop at once, without prior approval, on any of:
  - an unexplained difference;
  - a duplicate, replayed or wrong payment;
  - an instruction whose status cannot be established;
  - an incident indicator found on the secondary path.
- SEC or the Head of Payments Operations can call the stop, and then tells the chair.

**Owner and execution:**
- SEC decides the security clearance.
- The CMT chair decides activation, after consulting the Head of Payments Operations.
- Payments Operations runs the process.
- IT Operations and SEC monitor it.

**Times (HKT):**
- Clearance decision by 19:00.
- Pilot about 19:30.
- Full run about 20:00 onward.
- Tolerance checkpoints at 20:00 (50%) and 08:00 on 17 Nov (100%).
- SEC status report every hour.

**Recipients and channels:**
- Written clearance or refusal goes to the CMT chair, entered in the decision log.
- BCP activation entry under PH01 4.4.
- Emergency change record.
- Facts passed to LC for the HKMA BCP notification, and to COM for the service status.

**Basis: external sources**
- **R07, SPM TM-G-2, s.1.3.3, p.5:** "AIs should inform the HKMA promptly if their BCP is activated."
  - Authority: HKMA statutory guideline.
  - Activating the secondary process is BCP activation, so LC must notify. That action belongs to LC; I flag the trigger.
- **R07, s.4.3.2, p.11:** the alternate processing phase "may entail record reconstruction and verification, establishment of new controls, alternate manual processes".
  - This supports rebuilding and verifying instructions rather than trusting the queue.
- **R06, SPM OR-2, s.3.4, p.6:** "an AI should prioritise a critical operation that would more sooner breach its tolerance for disruption over one that is less time sensitive".
  - Authority: HKMA guideline. It is a general principle about prioritising remediation, and I apply it here by analogy.
  - It supports prioritising by time sensitivity and value date. The exact order within the queue is left to judgment and to PH01.
- **R05, HKMA circular of 22 Jun 2010, p.1, "Immediate incident response":** "The top priority should be to safeguard the interests of customers who have been or may be affected by the incident."
- **R09, TM-E-1, s.8.2.1, p.32:** the same principle.

**Basis: internal bank procedure (PH01 v1.0)**
- **s.8.2:** "The CMT chair activates it under section 3, after SEC's written clearance that it shares no hosts, accounts, keys or network path with any affected system. Activation is a BCP activation under 4.4."
- **s.8.3:** pilot of no more than 20 instructions.
- **s.8.4:** "(1) SME payroll, earliest value date first; (2) other instructions with a value date of today or the next business day; (3) everything else in order of submission. Up to 10% of hourly capacity is kept for urgent cases ... Order is never set by customer size."
- **s.8.7:** hourly reconciliation and stop.
- **s.2.3:** conditions and the security default.
- **s.6.1 and s.3:** evidence release.
- **s.4.3:** tolerance escalation.
- **Conflict check:** none found. PH01's BCP activation entry and the LC notice are consistent with R07 s.1.3.3.

== Q10b: Control for retried payments and possible duplicates before processing ==

**Decision.** No instruction is released until it has a single entry in one instruction register and passes the checks below. Anything uncertain is held. The default is hold, never release.

**Action (Payments Operations runs it; SEC sets the integrity checks; Fraud reviews flagged items):**

1. **One register, one ID.** Every instruction goes into a single register with a unique processing ID, whatever its source: gateway queue extract, channel logs, branch, contact centre or SME resubmission. Each ID can be released once only.
2. **Duplicate matching.** Automated matching on:
   - debtor account
   - beneficiary account
   - amount
   - value date
   - customer reference or batch ID
   - submission time window (from the first timeout onward)

   Each item is then classified as one of:
   - unique;
   - suspected duplicate or retry (linked to its original);
   - in flight at the failure, status unknown.
3. **Status check, for any retry, suspected duplicate or in-flight item.**
   - The ledger and a receiving-side record that is independent of the gateway (clearing or settlement records or acknowledgements) must show whether the original was posted or settled.
   - In-flight items stay "status unknown" and are held until an independent record shows they did not settle.
4. **Intent check.**
   - The customer, or the SME's authorised contact, confirms which instruction they want paid.
   - Confirmation is by call-back to a number already on file, never one given in the call.
   - Contact details changed since the incident began are checked by Fraud before use.
   - Professional judgment: the 80 customers whose phone numbers were exfiltrated are exposed to impersonation. For them, the call-back script includes verification questions and never asks for one-time passwords or PINs.
5. **Integrity check (SEC).** Because the gateway was compromised, every instruction is compared with the customer's original authenticated instruction.
   - Any difference in beneficiary, amount or account is held and passed to Fraud as suspected tampering.
   - Payroll files are compared by hash with the SME's original upload, or confirmed line by line by call-back.
   - Beneficiaries added during the window of attacker activity get a Fraud review.
6. **Hold rule.** If either the status check or the intent check is incomplete, the item is held. Held items stay out of the release queue and are reviewed each hour. The customer is told through COM's approved channels that the payment is being verified.
7. **After release.**
   - Hourly reconciliation runs as in Q10a.
   - Any duplicate or wrong payment found stops all releases until it is explained and logged.
   - Recall or recovery of a wrong payment goes to Payments Operations and LC.

**Owner and execution:**
- Payments Operations, led by its Head, owns the register and the releases.
- SEC defines and audits the integrity checks.
- Fraud reviews flagged items.
- Branch and contact-centre staff do call-backs only from numbers on file.

**Timing:** in place before the first pilot item, about 19:30 HKT, and applied to every batch.

**Recipients and channels:**
- Instruction register, decision log and case register.
- Customers are reached by call-back to numbers on file.
- Duplicate statistics go to LC and COM so their figures are accurate.

**Basis: external sources**
- **R14b, HKMA "Good practices for operational resilience" Annex (1 Apr 2026), p.1, s.A.1 "Eliminating single points of failure", "Auto-switching capabilities" bullet:**
  - It cites "controlled auto-retry logic (e.g. duplication checks when re-attempting transactions), and timeout mechanisms, along with exceptions monitoring to allow for manual intervention".
  - Authority: HKMA good-practice annex, not a binding rule.
  - It supports duplicate checks when transactions are retried after a timeout, as here. The exact method is left to judgment.
- **R07, s.4.3.2, p.11:** "record reconstruction and verification".
- **R05, p.1, and R09, s.8.2.1:** protect the interests of affected customers. Paying twice or paying a tampered beneficiary harms them.
- **R08, TM-G-1, s.3.2.2, p.12:** stronger authentication for "payment transactions". This supports verifying each instruction against the original authenticated instruction.

**Basis: internal bank procedure (PH01 v1.0)**
- **s.8.6, "Duplicates and unknown status":**
  - "Each instruction is released once only, under a unique processing ID."
  - Two checks: "(a) intent ... by call-back to a number already on file" and "(b) status: the ledger and an independent receiving-side record".
  - "If either check is incomplete, or the status of an instruction cannot be established, the instruction is held."
- **s.8.5:** check against the original authenticated instruction, and call-back for payroll.
- **s.10.5:** contact details changed since the incident began.
- **s.8.7:** stop rule.
- **Conflict check:** none found.

== Facts passed to the incident team ==
1. **To the CMT chair:**
   - Whether clearance is signed or refused, and when.
   - Capacity arithmetic: about 360 an hour, about 11.7 hours for 4,200, so the tail is at risk of passing the 08:00 tolerance on 17 Nov.
   - The 20:00 notice to the Board chair at 50% tolerance.
2. **To LC:** BCP activation and its time once the chair logs it, so the HKMA can be informed promptly under R07 s.1.3.3 and PH01 5.8.
3. **To COM:** verified hourly figures only, from the Payments Operations register, under PH01 11.4. Retried payments will not be paid twice; customers do not need to resubmit; held items will be confirmed by call-back from a number on file. Callers must not be asked for PINs or one-time passwords.
4. **To Fraud:** the list of instructions that do not match their originals, and the 80 exposed customers, so call-backs to them are handled with extra care.