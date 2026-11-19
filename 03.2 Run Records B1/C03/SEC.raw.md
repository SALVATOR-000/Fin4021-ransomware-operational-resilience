SEC (Information Security Lead): locked response for C03, Monday 16 Nov 2026, 12:00 HKT (H+4)

Assigned units: Q07a and Q07b only. The C01 and C02 reports were handed back earlier. No facilitator handoff was addressed to SEC for C03.

The two units depend on each other:
- The exposure window cannot close until the vendor credential is proven closed (Q07b). Until then the scope estimate in Q07a stays open-ended.
- My C02 revocation is not closure. The card says active sessions or tokens may survive, so under PH01 7.4 the window is treated as open.
- No conflict was found between PH01 and any applicable external requirement for these units.

Facts not known at this card:
- The workspace's location: inside or outside the gateway segment isolated at C01.
- Whether the export happened before or after the C01 isolation (about 08:10) and the C02 revocation (09:30).
- The exact number of records and individuals in the workspace, and which fields each record holds.
- Whether the vendor credential is a shared account.
- Whether the workspace is part of the critical computer system.
- The bank's "material volume" threshold in its business continuity plan.

---------------------------------------------------------------
UNIT Q07a: How to establish the scope of exfiltration, and what evidence would change the estimate

DECISION AND ACTION (simulated, for the log)

S1, 12:00. Log the exact time the forensic analysts confirmed the exposure. This starts the PH01 10.4(b) clock: a scope review no later than 12 hours later, so by 24:00 if confirmation was at 12:00.
By 12:15, confirmed facts go to LC, the Data Protection Officer (DPO) and the CMT chair, in person or by phone plus a decision-log entry:
- 80 customers' names, Hong Kong identity card numbers and telephone numbers were exported.
- The export timestamp.
- A vendor support credential was used in that session.
- The wider set of up to 18,000 is unverified.
None of LC's reports wait for the scoping work (PH01 2.4).

S2, 12:00 to 12:30. Check that the workspace is contained.
- If it sits outside the isolated segment, or can be reached by any open path, isolate it at the network layer. Preserve its state, and block at the perimeter the outbound destinations seen in the export logs.
- If a working service uses the workspace, consult the chair. Active exfiltration risk means containment goes first (PH01 7.1 and 6.2).
- Stop trigger: an export timestamp after 08:10 or 09:30 means containment failed. Re-contain and tell the chair at once.

S3, by 13:00. Fix the access window.
- Start: the earliest evidence of attacker or vendor-credential activity in the identity provider, VPN, privileged-access and gateway logs.
- End: the time the Q07b closure test passes on every access path. Until then the end stays "open".
- Every timeline entry carries its clock offset and uncertainty. Events closer together than their combined uncertainty are logged as "order undetermined" (PH01 6.4).

S4, by 15:00. Define the population from an offline copy.
- Use a backup or snapshot of the workspace from just before the first attacker access. It is a verified copy, used only in the bank's lab (PH01 6.3, 16.2).
- Record the exact number of records and of unique individuals, the fields in each record, and whether each person is a customer.
- Identifiers are tokenised for analysis. This replaces "up to 18,000" with exact figures.

S5, 15:00 to 20:00. Evidence sweep across the whole window and every way data could leave:
- (a) File and object access logs, database query logs (rows returned), and export or download logs for the workspace.
- (b) Staging artefacts: archives, temporary files, tools and scripts, found through endpoint telemetry and disk images.
- (c) Outbound bytes per destination (firewall, proxy, traffic-flow and data-loss-prevention logs), compared with the size of the 80-record file and of the full set.
- (d) The bank's own privileged-access session recording, and the vendor's transfer records (from C02). Vendor records count only as the vendor's own account until reconciled with bank logs (PH01 6.7(d)).
- (e) The screenshot rows compared with the 80 exported rows.
- (f) Log coverage and integrity: gaps, clock anomalies, audit-policy changes, protection tools switched off.
- (g) External signs:
  - publication or offer of the data, watched by the forensic firm without visiting attacker links (PH01 6.6);
  - misuse reports from branches and the contact centre, for example callers quoting identity card numbers, routed to SEC as evidence;
  - any further attacker material, received into evidence only.

S6. Classify every record and every individual into one of four groups, each with evidence references:
- CONFIRMED EXPORTED: the 80.
- EVIDENCE OF ACCESS: read, queried, staged, or appearing in attacker material beyond the 80.
- POSSIBLE: in the workspace with no evidence of access, but log coverage is incomplete.
- EXCLUDED: only where independent, integrity-checked logs cover the whole window and every exit path and show no access.
For LC and the DPO, SEC also records that the possible group was "held in the same place as confirmed records" (a PH01 10.4(c) factor).

S7, reporting.
- Preliminary at 15:00: the window, the population, and any early findings.
- Full scope package by 20:00, for the DPO and LC review due by 24:00 (PH01 10.4(b)).
- Then on every new piece of evidence (PH01 10.4(d)), and in SEC's hourly status reports (PH01 2.5).
- The estimate is always given as the four groups with counts and confidence. It is never extrapolated from the 80 or taken from the attacker's claim.
- Counts of records and of individuals are reported separately, because the PCPD guidance asks for both.

EVIDENCE THAT WOULD CHANGE THE ESTIMATE

Would increase it:
- Outbound volume in the window larger than the 80-record file.
- Further read, query or export entries for other records.
- A staged archive holding more records.
- Rows in the screenshot, or in later attacker material, that are not among the 80.
- Vendor-side transfer records showing workspace data leaving.
- Any use of the credential or a token after revocation. This extends the window (see Q07b).
- Publication or offer of the data, or misuse reports from customers outside the 80.
- The same credential reaching other data stores.

Would block any exclusion:
- Log gaps or tampering within the window. Records affected stay "possible"; they do not become "confirmed".

Would narrow it (moving records from "possible" to "excluded"):
- Complete, independent, integrity-checked logs on every exit path for the whole window, showing only the one export.
- Outbound bytes that match that one file (plus protocol overhead).
- A session recording showing that the attacker's actions were limited.
- Reconciled vendor records that agree.
- A passed closure test that fixes the end of the window.

Would NOT change it:
- The attacker's claim on its own.
- The size of the store on its own (PH01 10.4(c)).
- Vendor assurances that have not been reconciled.
- Absence of findings where logs are incomplete.

OWNER
- Accountable for the evidence and the estimate: SEC.
- Execution: SEC analysts and the retained forensic firm, with the evidence custodian; the data owner supplies the population count.
- Review: the DPO and LC. The CMT chair decides the notification scope (PH01 10.4(b)).

TIMES
- 12:15: confirmed facts out.
- 12:30: containment check.
- 13:00: window fixed.
- 15:00: preliminary report.
- 20:00: full scope package.
- The chair's review is due by 24:00.

BASIS: EXTERNAL (direct rules)
1. R11, PCPD Guidance on Data Breach Handling, June 2023. Authority: PCPD guidance, not law. Why it applies: there is now an actual breach involving the 80.
   - PDF p4, Step 1: "How many data subjects might be affected?"
   - PDF p7: a notification may include "The categories and approximate number of data subjects involved" and "The categories and approximate number of personal data records involved".
   - PDF p8: "After the full details of the incident are revealed, all information should be submitted to the PCPD and other law enforcement agencies without delay." The scope therefore goes forward as supplementary facts and does not hold the first report.
2. R16b, HKMA circular "Customer Data Protection", 14 Oct 2014, PDF p2.
   - Quote: procedures include "ascertaining the nature of the incidents, the causes of the incidents and identity of customers affected".
   - Authority: HKMA circular. Why it applies: this is a confirmed privacy incident.
3. R03, HKMA Sectoral Code for Designated AIs, s.6.2.23(b) and (d), PDF p18.
   - Logs must record "(iii) Access attempts to critical files" and "(vi) Modifications to audit policies".
   - "Retained logs should contain sufficient information to support after-the-fact investigation".
   - Authority: the HKMA's category 2 code. It applies directly to the gateway's logs. For the workspace it applies only if the workspace is part of the critical computer system, which is unknown; otherwise it is a supporting principle.
4. R10, Cap. 486 PDPO, Schedule 1, Data Protection Principle 4(1)(a), PDF p169. The bank must protect data having "particular regard to— (a) the kind of data and the harm that could result".
   - Names plus identity card numbers plus phone numbers carry an identity-theft risk (R11 p5).
   - So copies made for analysis are minimised and tokenised.
5. For LC:
   - R02, OCCICS Code of Practice v1.0, s.7.3.4(d), PDF p36: a serious incident includes "leakage of material volume of customer data, where 'material' is defined by the CI operator in the business continuity management plan". LC applies the bank's threshold to SEC's counts.
   - R16a, PCPD Data Breach Notification Form, PDF p2, needs "Number of individuals affected*", "Types of personal data involved*", and "Did you engage a service provider / contractor". SEC supplies these facts.

NO DIRECT RULE LOCATED in the assigned sources for the scoping method (the four groups, byte reconciliation, the rule for exclusion).
- Files searched: PH01 and R01–R16d.
- Terms: "exfiltrat" (hits only R02 p35 and R11 p2, both definitional), "material volume", "sample", "evidence", "session".
- S2–S7 are professional judgment.

BASIS: INTERNAL (Internal bank procedure: PH01, v1.0, effective 1 Oct 2026)
- s.10.4(a): customers with "evidence that their data was accessed, copied or misused, are notified as soon as practicable".
- s.10.4(b): "No later than 12 hours after the first confirmation of exposure, the DPO and LC review, with SEC's evidence, whether the scope should be widened."
- s.10.4(c): scope "is set by evidence and risk ... An unverified claim, or the size of the data store, does not by itself make everyone in the store a notification batch."
- Also s.6.4, s.6.7(d), s.16.2, s.17.2 and s.2.4.
- By analogy, s.9.2: "A sample result is recorded as a sample".

CONFLICT CHECK
- None found.
- PH01 10.4 is consistent with R11 p8 and R16b p2–3, and notification decisions stay with LC, the DPO and the chair.

---------------------------------------------------------------
UNIT Q07b: How to handle the vendor credential, active sessions and related tokens

DECISION AND ACTION (simulated)

K1, 12:00. Log the access window as OPEN (PH01 7.4). The C02 revocation is recorded as "not closed, closure test not passed".

K2, 12:00 to 12:10. List and capture every live session or token tied to the vendor's identities, on every path (10 minutes at most, PH01 7.3, witnessed into evidence):
- identity-provider and single-sign-on sessions and refresh tokens;
- VPN or remote-gateway sessions;
- privileged-access sessions;
- gateway and workspace application sessions;
- directory tickets;
- SSH keys, API keys and certificates.
For each, record the user, source, and last activity.
Override: if a live session is moving data, cut it at once without capture (PH01 6.2).

K3, by 12:15. Terminate and revoke.
- Terminate all those sessions and revoke all tokens and grants.
- Invalidate application sessions on the server side.
- Reset the credentials so existing tickets cannot be renewed, and force expiry where the platform allows.
- Remove keys and confirm every vendor account is disabled.
- Block the vendor's remote path, its source IP addresses and the export destinations at the perimeter.
- If the evidence shows privileged directory rights, a directory-wide credential reset goes to the chair as a decision, because it could break mobile and branch services (PH01 s.3).

K4, by 12:30. Closure test (PH01 7.4), on each path separately.
- Run from a controlled SEC test host with a witness, against a harmless endpoint.
- Replay a captured token, and attempt a logon with the old credential.
- Both must fail. Log the result and time for each path.
- If either succeeds: that path stays open, repeat K3 for it, and tell the chair. The Q07a window stays open.

K5, by 14:00. Rotate every secret the old access could read:
- passwords and keys in workspace or gateway configurations;
- shared admin credentials and service-account credentials;
- payment-interface keys.
Where a rotation touches a working service (mobile balance view, branches), stage it with IT Operations and keep a fallback. Consult the chair if a working service would be lost.

K6, by 16:00. Persistence sweep.
- Look for accounts created, privileges changed, keys added, multi-factor devices enrolled, and scheduled tasks set up by or for the vendor identity during the window.
- Capture each as evidence, then remove it.

K7, continuous. Detection rules fire on any attempted use of the old credential, its tokens, or the vendor or attacker IP addresses.
- A successful use is a stop trigger: re-contain, tell the chair at once, and extend the Q07a window.
- Failed attempts are logged as evidence that the attacker is still trying, and passed to LC.

K8, vendor. Through the vendor relationship owner, using a call-back to the number on file, never the vendor's own remote path. The vendor must confirm:
- that it has disabled the credential on its own side;
- the individual(s) and device used in the session;
- that the device is preserved (C02);
- that it holds no other credential for the bank.
If the vendor does not confirm, escalate under PH01 6.7(c).

K9, HOLD. Vendor access stays off. It can be reinstated only under PH01 7.5, which requires all of:
- the cause is known;
- access meets 7.2 (named individual accounts, multi-factor, time-limited, through the privileged-access system and recorded);
- secrets readable by the old access have been rotated;
- SEC signs off in writing; the chair then decides (PH01 s.3).
Two further holds until the closure test has passed on every path:
- SEC gives no written clearance for the alternate payment process (PH01 8.2) and no sign-off on any recovery gate (PH01 9.3). Both also need confirmation that no vendor account or key is shared with them.
- Mobile transfer submission, still interrupted, gets no security clearance to reopen.

OWNER
- Decides: SEC (PH01 7.3, s.3).
- Execution under emergency change: identity administrators, privileged-access administrators, network/perimeter engineers, and application administrators. The custodian witnesses the captures.
- The chair is consulted if a working service would be lost, and decides any reinstatement.
- The vendor relationship owner handles contact with the vendor.
- Each change to the critical computer system is logged with its deployment time for LC's Cap. 653 s.22 assessment.

TIMES
- 12:10: capture.
- 12:15: revocation.
- 12:30: closure test.
- 14:00: secret rotation.
- 16:00: persistence sweep.
- Continuous: detection.

BASIS: EXTERNAL (direct rules)
1. R03, HKMA Sectoral Code for Designated AIs, s.6.2.13(b), PDF p14.
   - Quote: "all passwords are promptly changed if they have been or are suspected of being compromised".
   - Authority: the HKMA's category 2 code. Why it applies: the vendor credential's compromise is confirmed, and it reached the gateway, a critical computer system.
2. R11, PCPD Guidance, PDF p5, Step 2: "Changing users' passwords and system configurations to block any (further) unauthorised access" and "Removing the access rights of users suspected to have committed or contributed to the data breach". Why it applies: an actual breach is confirmed.
3. R16a, PCPD Data Breach Notification Form, Annex, PDF p4, under Cyberattack, Immediate Remedial Measures: "Change login details for the compromised device / software / database / system".
4. R10, PDPO DPP4(1), PDF p169: "All practicable steps shall be taken". Sessions or tokens still alive mean continuing exposure.
5. R05, HKMA circular "Incident response and management procedures", PDF p1 (checked against the scan in C01): "as soon as practicable rectify or contain the problem".
6. R16b, Annex C(vii), PDF p5: remote access by service providers "should be subject to robust authentication (e.g. two-factor authentication)". This is a precondition for any reinstatement.
7. For LC's reports: R02 Annex F, section D.1, PDF p45, has the tick box "Compromised accounts have been removed or isolated". It may be ticked only after the closure test passes.

NO DIRECT RULE LOCATED in an external source for token replay or closure testing.
- Files searched: all allowed files.
- Terms: "token", "session", "revok".
- Only PH01 7.3 and 7.4 address it; the external hits are unrelated.

BASIS: INTERNAL (PH01 v1.0)
- s.7.3: "SEC captures session and token state (10 minutes at most), then terminates all sessions, revokes tokens and keys, and disables the account and every other account of the same vendor. The vendor's remote path is blocked at the perimeter."
- s.7.4: "A credential is closed only when a replayed token and a logon with the old credential both fail, and the result and time are logged. Until then the access window is treated as open."
- s.7.5 sets the reinstatement conditions; s.7.2 sets the access standard.
- Also s.3 (vendor-reinstatement row), s.6.2, s.8.2 and s.9.3.

CONFLICT CHECK
- None found.

---------------------------------------------------------------
FACTS SEC PASSES TO THE INCIDENT TEAM

To LC, by 12:15 (for the PCPD form, the HKMA "at once" update on confirmed data exposure under PH01 5.8, the CI notification and the Police):
- Data types: name, Hong Kong identity card number, telephone number.
- Confirmed: 80 individuals.
- Possible: up to 18,000, unverified; exact count by 15:00.
- Hong Kong residents: likely, because identity card numbers are involved; to be confirmed.
- Date of the breach: the export timestamp.
- Cause: cyberattack using a vendor support credential.
- Closure status of that credential.
- The bank's "material volume" threshold (R02 7.3.4(d)) is LC's to apply.

To the DPO and the CMT chair:
- The 80 fall under PH01 10.4(a) now.
- SEC's scope package arrives by 20:00 for the review due by 24:00.
- The "possible" group may include people who are not customers.

To COM, for fact-checking:
- Verified: data of 80 customers exported.
- The wider set is "being investigated". Give no figure beyond the verified count (PH01 11.4).
- Do not name the vendor or the system (PH01 11.3).

To the contact centre and branches: send any report of a call quoting customer identity details to SEC as evidence.

To Payments Ops: the alternate process must be checked for any vendor account or key it shares.

---------------------------------------------------------------
LOG-READY ACTIONS (HKT, status)
- 12:00: Exposure confirmation time logged; access window logged as open (executed).
- 12:10: Sessions and tokens captured (executed, or skipped if data is moving).
- 12:15: Sessions terminated, tokens revoked, perimeter blocked (executed).
- 12:15: Confirmed facts to LC, DPO and chair (executed).
- 12:30: Closure test on each path (scheduled).
- 12:30: Workspace containment check (scheduled).
- 13:00: Access window fixed, end provisional (scheduled).
- 14:00: Secret rotation (scheduled).
- 15:00: Population count and preliminary scope report (scheduled).
- 16:00: Persistence sweep (scheduled).
- 20:00: Full scope package (scheduled).
- Vendor reinstatement: held.
- Alternate-process and recovery clearances: held until the closure test passes.
- Continuous: re-contain and extend the window on any use of the old credential or tokens (trigger).