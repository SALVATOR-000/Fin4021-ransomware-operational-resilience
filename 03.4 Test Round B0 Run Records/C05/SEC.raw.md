SEC (Information Security Lead): locked response for C05 (Tuesday 17 Nov 2026, 08:00 HKT, H+24). This covers only Q13a and Q13b. No facilitator handoff was addressed to SEC.

Facts as given at this card:
- A pre-incident immutable backup exists. Whether it is suitable for restoring payment processing is unverified.
- The original gateway is still impaired and under evidence hold.
- A public mirror matches 320 customer records. The 18,000 claim is still unverified.
- The 24-hour tolerance for transfers and payroll ran out at 08:00 HKT today.
- I do not know whether the secondary process from C04 holds a current security clearance. The facilitator should confirm, because it decides the rollback target in Q13b.

All actions below are simulated, for the facilitator to log.

== Q13a: Recovery candidate, integrity checks and separation checks ==

**Decision.** I will test candidate 1: a new gateway build from trusted media, loaded with data from the pre-incident immutable backup, inside an isolated recovery environment.
- The standby system is candidate 2. It is tested only if candidate 1 fails, under the same checks.
- The original gateway is not repaired in place. It stays held as evidence.
- Nothing from the candidate reaches production until the PH01 9.3 gate is passed (Q13b and below).

**Action**
Executed by IT Operations recovery engineers. SEC verifies each step, and the evidence custodian witnesses.

1. **Build the isolated recovery environment, from 08:30.**
   - New hosts.
   - A separate identity store with newly issued named admin accounts and MFA.
   - No vendor accounts and no reuse of any credential from the affected estate.
   - No network route to production, to the quarantined gateway segment, or to the internet. Management only through a dedicated jump host.
   - EDR and logging running from the first boot.
2. **Separation validation, before any data is loaded.** Log each of these:
   - Firewall and routing rules have been reviewed.
   - An active reachability test from the recovery environment to the production and quarantine ranges fails in both directions.
   - The account and group inventory shows no shared principals.
   - The key and certificate inventory shows no material shared with the gateway. All payment, TLS and API keys and certificates are newly issued. Payment keys are re-keyed with the clearing counterparties through Payments Operations.
3. **Software integrity.**
   - Application and OS binaries come only from trusted media, meaning the original procurement or escrow copies, with signature and hash checked against the publisher's values.
   - Those values are obtained by a route independent of the vendor's support channel, because a vendor support credential was misused.
   - Configuration is rebuilt from the version-controlled baseline. Every difference from the last approved configuration is reviewed.
   - No binaries, scripts, scheduled jobs or credentials are taken from the backup. The backup supplies data only.
4. **Backup integrity.**
   a. **Timing.** Compare the backup timestamp with the earliest attacker indicator in the C03 forensic timeline, including the first use of the vendor credential.
      - Stop trigger: if the backup is not clearly earlier than the earliest indicator, or the start of the dwell period is unknown, the backup is not treated as clean. It needs the deeper scan in 4(c), and any restored executable objects are rebuilt from the baseline.
   b. **Immutability.** Check the vault's lock and audit logs for any deletion, retention change or access attempt since the backup was written. Check the backup catalogue checksums against the stored data.
   c. **Content scan.** Restore to a copy, never the original backup set, mounted read-only.
      - Run an indicator and malware scan.
      - Review database stored procedures, triggers and job definitions.
      - Compare static payment data (beneficiaries, payroll templates, routing tables, limits) with independent records.
   d. **Evidence.** The original backup set stays preserved and is entered in the evidence register with its SHA-256. Restores run from a hashed working copy.
5. **Personal data in testing.**
   - Production data or extracts are used in testing only after SEC records two things: that the data has been de-sensitised and the de-sensitisation checked, and that the payments information owner gave prior approval.
   - Judgment: tokenise names, HKID numbers and telephone numbers consistently, so reconciliation still works on tokens.
   - If either record is missing, that data set is not used and the test is held.
   - The recovery environment holds customer data that is already partly exposed, so access is limited to named recovery staff.

**Owner and execution**
- SEC is accountable for the security verification and the integrity and separation sign-offs.
- The Head of IT Operations leads the build.
- The payments information owner approves use of test data.
- The evidence custodian handles the backup copy.

**Timing (HKT, targets set by professional judgment, not gates)**
- Separation validation by 12:00.
- Backup timing and integrity result by 14:00.
- Interim status in each SEC report, which goes four-hourly once containment is confirmed and hourly until then.
- Missing a target only delays progress. It never releases a check (PH01 2.3).

**Recipient and channel**
- Recovery test record, emergency change record and evidence register.
- Decision log entries for each sign-off.
- Verbal briefing to the CMT chair and the Head of Payments Operations.

**Basis: external**
- **R02, OCCICS Code of Practice, s.6.2.20(c), PDF p.18:** "An immutable copy or a copy that is physically disconnected from a CCS should be stored to avoid corruption of backup data if the CCS is compromised."
  - Authority: a Code under Cap. 653 s.8, and the reference baseline for designated operators.
  - It supports restoring from the immutable copy. It does not prove the copy is clean, so the timing and content checks are my judgment.
- **R03, HKMA Sectoral Code, s.6.2.20(b)(i), PDF p.17:** the designated AI should "implement a secure tertiary data backup (STDB)".
  - If the immutable backup is the STDB, the HKAB STDB principles apply. The facilitator should confirm which backup this is.
- **R03 s.6.2.22(c), PDF p.17:** "Data used for testing should be carefully selected, protected and controlled", with reference to TM-G-1 s.4.2.4.
- **R08, SPM TM-G-1, s.4.2.4, PDF p.18:**
  - "System and user acceptance testing should be carried out in an environment separated from the production environment."
  - "Production data should not be used in development or acceptance testing unless the data has been de-sensitised ... and prior approval from the information owner has been obtained."
  - It applies directly to offline testing of the candidate.
- **R14b, HKMA good-practices annex, s.B.6, PDF p.5:** examples include "setting up dedicated environments and utilities for recovery". Good-practice support only.

**Basis: internal bank procedure (PH01 v1.0)**
- **s.9.1 "Candidate order":** "(1) A new build from trusted media with data from the immutable backup, in an isolated recovery environment; (2) the standby system, only if (1) fails, under the same checks. An affected system is never repaired in place for return to service."
- **s.9.2:** de-sensitisation and prior approval of the information owner, otherwise "that data set is not used and testing with it is held".
- **s.6.1:** the original gateway stays under hold.
- **s.7.5:** no vendor access to the recovery environment without reinstatement.
- **Conflict check:** none found. PH01 9.2 adopts R08 4.2.4.

== Q13b: Offline reconciliation checks before the candidate can be considered for production ==

**Decision.** The candidate passes offline testing only if the full reconciliation shows no unexplained difference.
- One unexplained difference is a fail.
- A sample result is recorded as a sample, not as a pass of the whole set.
- A pass is necessary but not sufficient. Production use still needs every PH01 9.3 gate item, and only the CMT chair can authorise it.

**Checks** (run in the recovery environment on de-sensitised or tokenised data, under Q13a item 5)
1. **Baseline at the backup point.** The candidate's restored state (instruction tables, queues, static data) must agree with independent records at the same cut-off:
   - the core ledger end-of-day position
   - clearing and settlement statements.
   Count and value must tie in total and by account class.
2. **Delta since the backup point.** Every instruction created after the backup point is rebuilt from independent sources:
   - core ledger postings
   - clearing and receiving-side records
   - the C04 secondary-process instruction register and its unique processing IDs
   - SME original uploads.
   Each is classified as settled, not settled or unknown. The candidate's loaded state must:
   - mark every item settled by the secondary process or by clearing as settled, so nothing is sent twice at cutover;
   - hold every unknown item;
   - queue only verified, not-settled items, in PH01 8.4 priority order.
3. **Duplicate and replay rejection.** Inject test copies of known retried and duplicate instructions, and replay an old message. The candidate must reject each and log it.
4. **Static data integrity.** Beneficiary lists, payroll templates, routing and BIC tables, limits and fee tables must match the pre-incident baseline plus authorised changes only. Any unexplained change is a fail and goes to Fraud.
5. **Message integrity.** Formats, signatures and new keys are tested end to end against a clearing test or simulator only, never the live system.
6. **Count and value tie-out.** For the full test set: totals in equal totals out, with every item accounted for.
7. **Recording.** Each check is logged with evidence and signer: SEC for security and integrity, Payments Operations for reconciliation.

**Other gate items to prepare in parallel (PH01 9.3)**
These are outside my decision, but they are dependencies:
- integrity and separation checks passed (Q13a)
- rollback rehearsed. The target is the secondary process if it holds a current clearance and its reconciliation ties; otherwise releases are suspended.
- a delta reconciliation plan and live test plan
- business acceptance by the payments information owner
- LC's confirmation of the regulatory steps
- the CMT chair's authorisation.

Any missing item means hold. The Board, now engaged because 100% of tolerance is reached (PH01 4.3), may narrow the scope, for example to payroll only. The narrower scope still has to pass every applicable check.

**Stop triggers after any later go-live**
Any of the following stops releases at once, with no prior approval needed from SEC, the Head of Payments Operations or the IT Operations duty manager:
- an incident indicator
- one unexplained difference
- a duplicate, replayed or wrong payment
- an instruction whose status cannot be established.

**Owner and execution**
- SEC is accountable for the integrity and security checks and sign-off.
- The Head of Payments Operations runs the reconciliation and signs business results.
- The CMT chair alone authorises production.

**Timing.** Professional-judgment target: offline reconciliation result by 20:00 HKT on 17 Nov. It is reported when complete and is never shortened to meet a time.

**Recipient and channel.** Recovery test record and decision log. The gate pack goes to the CMT chair, and to the Board or Risk Committee if it is convened.

**Basis: external**
- **R08, SPM TM-G-1, s.4.2.4, PDF p.18:** "A formal acceptance process should be established to ensure that only properly tested and approved systems are promoted to the production environment."
- **R08 s.4.3.1, PDF p.19:** change management should include "a process for rolling-back changes" and "a post implementation verification of the changes made".
- **R07, SPM TM-G-2, s.4.3.2, PDF p.11:** alternate processing "may entail record reconstruction and verification". This supports the delta rebuild from independent records.
- **R14b, PDF p.1, s.A.1:** "controlled auto-retry logic (e.g. duplication checks when re-attempting transactions)". Good practice behind check 3.
- How strict the pass mark is, is left to the bank. PH01 sets zero tolerance.

**Basis: internal bank procedure (PH01 v1.0)**
- **s.9.2:** "A candidate passes offline testing only if reconciliation shows no unexplained difference. One unexplained difference is a fail. A sample result is recorded as a sample, not as a pass of the whole set."
- **s.9.3 "Gate":** "Missing any item means hold."
- **s.9.4:** staged go-live starting with a pilot of 20 instructions.
- **s.9.5:** stop and rollback.
- **s.8.6:** unknown status is held.
- **Conflict check:** none found.

== Facts passed to the incident team ==
1. **CMT chair and Board**
   - Which candidate is chosen and the planned check times.
   - The result of the backup timing check against the dwell period.
   - Tolerance was breached at 08:00, so the Board or Risk Committee must be convened (PH01 4.3).
   - The scope-narrowing option (payroll first).
2. **LC** (for the HKMA and Commissioner updates)
   - Recovery approach and status.
   - BCP and secondary-process status.
   - Confirmed exposure has grown from 80 to 320. This is a confirmation of data exposure that triggers an HKMA update (PH01 5.8) and the 10.4(b) review clock.
   - The 18,000 figure is still unverified.
3. **DPO, COM and LC**
   - The public mirror is captured into evidence by the monitoring provider or the forensic firm. Bank staff do not browse to it (PH01 6.6).
   - The mirrored record set is compared by internal ID only.
   - Any rows beyond the 320 are reported at once.
4. **COM and LC (fake verification page)**
   - SEC supplies the indicators: domain, URL and account handle, captured into evidence without bank staff visiting the page.
   - These support takedown and the customer warnings, which COM and LC decide.
   - SEC adds the indicators to the bank's blocking and fraud monitoring.
5. **Payments Operations.** The secondary-process register must stay authoritative for "settled" status so the candidate does not pay anything twice at cutover.