SEC (Information Security Lead): locked response for C08, Thursday 19 Nov 2026, 08:00 HKT (H+72)

Assigned units: Q22a and Q22b only. I have taken the facilitator's handoff for Q16a, Q16b and Q19b into account.

Live status, from the facilitator's decision record:
- No recovered-system production is authorised.
- Whether the alternate process released any payments cannot be verified.
- None of the N2–N5 results, the closure-test re-run, or the N8 reduction criteria is recorded.

Today's test results:
- The second test (240 of 240 reconciled) and the six hours without alarms describe the offline test environment only. They do not certify live operation.
- No conflict was found between PH01 and any applicable external requirement for these units.

---------------------------------------------------------------
UNIT Q22a: Which restrictions to keep or release, and what to hand to the standing operations team

DECISION
- No restriction is released at this card. None of the release conditions is recorded as met, and under PH01 18.3 restrictions stay in force after handover until their release condition is met and the PH01 s.3 decision-maker has logged the release.
- The 240/240 result is recorded as a SAMPLE, not as a pass of the whole set (PH01 9.2). The first gate item (offline pass) is therefore still unmet.
- One step forward is authorised: a FULL-set offline rerun of RC1–RC8 on the candidate (1) build. It touches no live interface. Its preconditions:
  - the root cause of the 118/120 failure has been documented;
  - the PH01 9.2 data preconditions (de-sensitisation, information owner's approval) are logged;
  - the build is confirmed as candidate (1), with checks I1–I8 and S1–S7 logged.
- Containment is still NOT confirmed, so status reports stay hourly (PH01 2.5). The duty passes to the receiving owner.

RESTRICTIONS KEPT
For each: the release condition, then who decides the release.

1. Gateway isolation and evidence hold.
   - Release when: an approved rebuild decision is made and the evidence is imaged and recorded.
   - Decided by: SEC for the isolation; SEC and LC jointly for the evidence.
2. Recovered system production HOLD.
   - Release when: a full-set offline pass under PH01 9.2, the first failure explained, and all seven PH01 9.3 items logged.
   - Decided by: the CMT chair, after the gate. The Board may narrow the scope but cannot waive any item.
3. Standby on hold.
   - Release when: candidate (1) has failed and the same checks are passed.
   - Decided by: SEC.
4. Vendor access revoked.
   - Release when: all PH01 7.5 conditions are met (see Q22b).
   - Decided by: the CMT chair, on SEC's written sign-off.
5. Mobile transfer submission held.
   - Release when: PH01 9.4 stage 3, after stages 1 and 2 have run clean.
   - Decided by: the CMT chair.
6. Alternate process: treated as NOT cleared, because no SEC clearance under PH01 8.2 is recorded.
   - Release when: SEC's written clearance (C1–C7 plus reconciliation ties) is logged after a clean N3 sweep and a passed closure test. If it is releasing without a logged clearance, it pauses (the C06 order).
   - Decided by: the CMT chair, on SEC's clearance.
7. Raised monitoring (N6), the quarantined host (kept powered on), and the perimeter blocks.
   - Release (reduce) when: all N8 criteria are met. Six hours with no offline alarms is not 72 hours with no indicator across the bank.
   - Decided by: SEC, with the chair informed.
8. Corporate email and the filing terminal.
   - Default: treated as not safe until SEC logs them as safe (PH01 5.6, 5.7).
   - Decided by: SEC.
9. Technical suspension of log rotation and backup recycling.
   - Release when: LC lifts the legal hold (PH01 17.1).
   - Decided by: LC.

HANDOVER (PH01 18.1–18.2)
The CMT hands over only items that have a named receiving owner who has signed acceptance of a specific list. Owners are given by role; names come from the CMT roster.
- Standing security operations manager: N6 monitoring and detection rules; the quarantined host; perimeter blocks; hourly status reports to SEC until containment is confirmed, then every four hours; the N8 reduction review.
- Head of IT Operations: gateway isolation infrastructure; the recovery build; the clock-synchronisation fix; changes to the privileged-access system.
- Identity engineering lead: re-run and log the closure test on every path (overdue, due by 12:00 today); token and session lifecycle fixes.
- Evidence custodian (an SEC designate): the evidence register, all holds and transfers, and the hashes of the partner deliveries.
- Head of Payments Ops: the alternate-process state record (due by 10:00 today); the instruction register; items held as unknown status, including the two first-test mismatches if they map to real instructions; hourly reconciliation.
- Forensic firm engagement owner (within SEC): indicator classification (N5, result outstanding); timeline versions; reconciling the vendor-service records.
- Vendor relationship owner, with the Chief Risk Officer and LC: the vendor preservation request and its production (sending not verified); contract terms.
- DPO, with LC: data-related items. This includes testing whether the 31 scam reports use data from the 320 file.
- SEC (Head of Information Security): keeps all PH01 s.3 decision rights and signs any closure or release. Handover transfers the execution, not the authority (judgment).

PAGE 1 OF THE HANDOVER PACK: "NOT EVIDENCED" (PH01 18.2). Each item transfers as OPEN, not done.
- C01: validation results (A6); whether mobile submission was disabled under A5-bis; the 08:30 terminal and email logs; the content of the standby snapshot.
- C02: whether the vendor preservation request was sent, and anything the vendor produced.
- C03: closure-test result; access-window end; the 15:00 and 20:00 scope results; secret rotation; persistence sweep.
- C04 and C06: SEC's clearance or hold of the alternate process; any releases and their reconciliation; the 20:15 status.
- C05: suitability of the backup (I1–I4) and checks I5–I8 / S1–S7.
- C06: the test-data preconditions for the first test (H2); the H3 flags; the content of the root cause.
- C07: N2–N5 results; the independent review of the timeline.
- C08: whether the 240-instruction test ran on the candidate (1) build, and whether its data preconditions were logged.

OWNER
- Accountable: SEC.
- Receiving owners as listed above.
- LC takes the register of external deadlines (PH01 18.4).

TIMES
- Handover pack signed before the CMT stands down.
- Alternate-process record by 10:00 today.
- Closure test and N2–N5 results by 12:00 today.
- Full-set rerun after the root cause is documented.

DESTINATION / CHANNEL
- The handover pack, with signed acceptances.
- Decision log, evidence register, instruction register.
- The CMT reconvenes at once on any security trigger, missed external deadline or new data exposure (PH01 18.5).

BASIS: EXTERNAL
1. R08, SPM TM-G-1, s.4.2.4, PDF p18: "only properly tested and approved systems are promoted to the production environment". A sample is not a full test, so the production hold stays.
2. R03, HKMA Sectoral Code for Designated AIs, s.6.2.26(a)–(b), PDF p19: detect incidents affecting the critical computer systems, monitor threat intelligence, "and take appropriate actions". This keeps monitoring raised while the indicator is unclassified.
3. R06, SPM OR-2, s.8.3–8.4, PDF p13. The incident management programme covers the "full life-cycle of any incidents" and is "supported by an inventory of internal and third party resources". This supports a role-by-role handover.
4. R02, OCCICS Code of Practice v1.0, s.7.2.3(c), PDF p33: ensure team members "are familiar with both their own roles and responsibilities and those of other team members". This supports named owners with signed acceptance.
5. R07, SPM TM-G-2, s.4.3.2, PDF p11: the full recovery phase "is as difficult and critical to the business as the process to activate the BCP".

NO DIRECT RULE LOCATED externally for handover mechanics.
- Term "handover": hits only PH01.
- Other terms searched: "stand-down", "monitor".

BASIS: INTERNAL (Internal bank procedure: PH01, v1.0, effective 1 Oct 2026)
- s.18.1: "The CMT hands over to standing teams only when each open item has a named receiving owner who has signed acceptance of a specific list."
- s.18.2: "Each handover pack starts with a page listing what is not evidenced. Items without evidence transfer as open, not done."
- s.18.3: "Restrictions stay in force after handover until their release condition is met and the decision-maker in section 3 has logged the release."
- s.9.2: "A sample result is recorded as a sample, not as a pass of the whole set."
- Also s.2.5 and s.18.5.

CONFLICT CHECK
- None found.

---------------------------------------------------------------
UNIT Q22b: Root-cause remediation, and the evidence needed to close the vendor-credential issue

ROOT-CAUSE REMEDIATION
Each item has an owner, an independent check by SEC, and a place in the standing risk register. Every change to a critical computer system is logged with its deployment date for LC under Cap. 653 s.22 (PH01 18.4).

- RC-A, vendor access model. Owner: Head of IT Ops, with SEC.
  - Enforce PH01 7.2: individual named accounts, multi-factor authentication, time-limited sessions through the privileged-access system, recorded sessions. No shared accounts.
  - Whether the compromised account was shared is still unverified.
- RC-B, session and token lifecycle. Owner: identity engineering lead.
  - Revocation must reach every path: identity-provider sessions, refresh tokens, server-side application sessions, maximum session lifetimes. C03 showed that a revoked credential could keep live sessions.
- RC-C, segmentation and egress. Owner: Head of IT Ops.
  - The vendor path lands only on jump hosts, with no route to customer-data stores.
  - Outbound controls and data-loss-prevention alerts on the workspace.
- RC-D, data minimisation. Owner: the data owner, with the DPO and SEC.
  - Remove or mask customer identity data in support workspaces.
  - Access only where needed (R16b Annex C).
- RC-E, detection. Owner: security operations manager.
  - Alerts on vendor-account behaviour, bulk exports and out-of-window logons.
- RC-F, recovery reconciliation. Owners: IT Ops recovery lead and Head of Payments Ops.
  - Document the cause of the 118/120 failure.
  - Run a full-set RC1–RC8 rerun.
- RC-G, supplier contract terms. Owners: vendor relationship owner, the Chief Risk Officer and LC.
  - Log retention, audit and production rights, incident cooperation, security requirements.
- RC-H, clock synchronisation. Owner: Head of IT Ops.
  - All critical-system components synchronised to the primary time source (PH01 6.4). Clocks differed by up to four minutes on this incident.
- RC-I, secrets. Owner: identity engineering lead.
  - Rotate everything the old access could read (PH01 7.5).
  - Where a supplier uses a password as the only factor, change it after every use.

Due dates (judgment):
- Remediation plan with owners and dates by 26 Nov.
- Technical root-cause draft to LC by 25 Nov. It feeds the Annex F written report, which LC files about 30 Nov (14 days after awareness on 16 Nov).
- Post-incident review completed by 16 Dec.

EVIDENCE TO CLOSE THE VENDOR-CREDENTIAL ISSUE
SEC signs the closure in writing. Each item is logged with its evidence ID. Closing the issue is NOT reinstatement.
- V1, inventory: a complete list of the vendor's accounts, keys, certificates, tokens and API credentials on every system: identity provider, VPN, privileged access, gateway, workspace, directory, alternate process and recovery environment. It must be reconciled with the vendor's own account records (PH01 6.7(d)), with no unreconciled entry left.
- V2: disablement, revocation and key-removal records, with timestamps, for every item in V1.
- V3: closure test passed on EVERY path. A replayed token and a logon with the old credential both fail, witnessed, with result and time logged (PH01 7.4). It is repeated after any change to identity configuration. This is currently NOT recorded.
- V4: no use since closure. Monitoring records for at least 72 hours show no successful use, and any attempts are logged and attributed.
- V5: a clean persistence sweep: no accounts, keys, multi-factor devices or scheduled tasks created by or for the vendor identity.
- V6: secrets rotated. The list of everything readable by the old access, with rotation evidence.
- V7, cause established: how the credential was obtained or misused, shown from the bank's logs reconciled with the vendor's records. Plus the vendor's examination of the endpoint used, the individuals identified, and the vendor's own remediation evidence.
- V8, supplier evidence chain:
  - the LC-cleared preservation request is on file and acknowledged by call-back;
  - production arrived through a PH01 6.7(b) channel with a SHA-256 manifest;
  - custody is recorded in the register;
  - the partner-delivered vendor records are reconciled.
- V9, independent check: internal audit or the forensic firm reviews items V1–V8 before SEC signs (judgment).
- Reinstatement is a separate decision under PH01 7.5: the cause is known, access meets 7.2, secrets are rotated, and SEC signs off in writing; then the chair decides. Until then access stays revoked.

OWNER
- Closure sign-off: SEC.
- Evidence: identity engineering lead, security operations manager, custodian, forensic firm.
- Vendor items: vendor relationship owner, with LC on contract terms.
- Reinstatement: the CMT chair.

TIMES
- V3 by 12:00 today; then V4's 72-hour run.
- V1, V2, V5 and V6 by 20 Nov 18:00.
- V7 and V8 by 25 Nov.
- Closure decision after V9.
All are judgment targets. No item closes because its time has passed (PH01 2.3).

BASIS: EXTERNAL
1. R06, SPM OR-2, s.8.3, PDF p13: incident management includes "Root cause analysis of incidents to help with the prevention or minimisation of recurrence."
2. R02, OCCICS Code of Practice v1.0, s.7.2.3(i), PDF p33: the post-incident review covers "(i) Facts and causes of the incident; (ii) Gaps in the existing governance, risk management and compliance contributed to the incident ... (iv) Improvement actions recommended."
3. R02 Annex F, PDF p43–44: the written report needs the "Initial Attack Vector / Point of Intrusion", the "Root Cause Analysis Summary", and "Whether the root cause was identified in previous security assessment or audit". V7 supplies these for LC.
4. R03, HKMA Sectoral Code, s.6.2.13(b), PDF p14: "all passwords are promptly changed if they have been or are suspected of being compromised", and a single-factor supplier password is "changed after every use".
5. R16b, HKMA circular "Customer Data Protection", Annex C(vii), PDF p5: remote access by service providers "should be subject to robust authentication". This is a precondition for RC-A and any reinstatement.
6. R01, Cap. 653, Schedule 3 Part 1 item 3(h), PDF p92 (statute): policies for "managing contracts and other communications with suppliers". This underpins RC-G.
7. R10, PDPO DPP4(1)(d) (PDF p169), "the integrity, prudence and competence of persons having access to the data", and DPP4(2) (PDF p169–170), contractual means for data processors. These underpin RC-D and RC-G.
8. For LC: R01 s.22 (remediation changes to critical systems) and s.27(4) (submit a revised emergency response plan within one month, if PH01 forms part of it and is revised).

NO DIRECT RULE LOCATED externally for the contents of the closure evidence pack.
- Terms searched: "token", "revok", "session", "root cause".
- Only PH01 7.4 and 7.5 address it. Items V1–V9 are professional judgment.

BASIS: INTERNAL (PH01 v1.0)
- s.7.4: "A credential is closed only when a replayed token and a logon with the old credential both fail, and the result and time are logged. Until then the access window is treated as open."
- s.7.5: "Vendor access is reinstated only when: the cause of the compromise is known; the access meets 7.2; secrets readable by the old access are rotated; and SEC signs off in writing."
- s.6.7(d): supplier records are "the supplier's account until SEC has reconciled them".
- Also s.7.2, s.3 (vendor-reinstatement row) and s.18.4.

CONFLICT CHECK
- None found.

---------------------------------------------------------------
FACTS SEC PASSES TO THE INCIDENT TEAM

To LC:
- The production hold continues; the 240/240 result is a sample.
- The closure test and N2–N5 results are open.
- The technical root-cause draft arrives by 25 Nov for the Annex F written report.
- Changes deployed to critical systems are logged for s.22.

To COM: the recovered system is not authorised for production. Any closing update would breach PH01 11.5, because SEC has not confirmed a stable production service.

To the chair: no restriction has been released; the handover pack and its "not evidenced" page need signed acceptance before the CMT stands down.

---------------------------------------------------------------
LOG-READY ACTIONS (HKT, status)
- 08:00: All restrictions retained; 240/240 recorded as a sample (executed).
- 08:00: Full-set offline rerun authorised, subject to its preconditions (scheduled).
- 10:00: Alternate-process state record (scheduled).
- 12:00: Closure test re-run and N2–N5 results (scheduled; overdue).
- Before stand-down: handover pack and signed acceptances (scheduled).
- 20 Nov 18:00: V1, V2, V5, V6 (scheduled).
- 25 Nov: V7, V8 and the root-cause draft to LC (scheduled).
- 26 Nov: remediation plan (scheduled).
- 16 Dec: post-incident review (scheduled).
- Vendor reinstatement: held.
- Reductions: held.