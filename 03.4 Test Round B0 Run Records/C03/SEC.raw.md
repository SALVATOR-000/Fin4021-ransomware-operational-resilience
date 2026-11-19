SEC (Information Security Lead): locked response to C03 (Monday 16 Nov 2026, 12:00 HKT, H+4). This answers only Q07a and Q07b. No facilitator handoff to SEC.

Facts as given at C03:
- **Confirmed:** forensic analysts matched the sample to bank records. Independent, time-stamped logs show an unauthorised export of one file holding 80 customers' names, HKID numbers and telephone numbers. A vendor support credential was used in that session.
- **Unverified:** whether the wider workspace set was exported. That set is up to 18,000 customers.
- **Open risk:** a credential that has been revoked may still have live sessions or tokens.
- **Service status:** mobile transfer submission is still interrupted.

The facilitator needs to confirm one time: when "first confirmation of exposure" happened, either at 12:00 or at an earlier time the analysts logged. Every PH01 10.4(b) timing below runs from that point.

All actions below are simulated, for the facilitator to log.

== Q07a: How to establish the scope of the exfiltration, and what evidence would change the estimate ==

**Decision.** From 12:00 I report the estimate in tiers. Each tier is reviewed and changed only when there is evidence:

| Tier | Size | Status |
|---|---|---|
| T1 Confirmed export | 80 customers | From the logged export |
| T2 Evidence of access or staging | Starts at 0 | Grows only on evidence |
| T3 Reachable, export not shown | Up to 18,000 in the same workspace | Possible, not shown |
| T4 Other stores reachable by the credential | To be determined | Being mapped |

I will not describe T3 as "not exported". Until log coverage is complete, it is "cannot yet be excluded".

**Action (forensic analysts and the retained forensic firm on verified copies; firm sees masked data only):**

1. **Session reconstruction, from 12:00.** Build one timeline, using the PH01 6.4 offset rules, for every session that used the vendor credential, starting from its first use (not only today). Sources:
   - PAM session recordings
   - VPN and identity-provider logs
   - workspace file and database access logs
   - EDR process and file events (archive creation, compression, staging)
   - DNS, proxy and firewall egress records with byte counts
2. **Volume test.** Compare outbound byte counts for each session and destination with:
   - the size of the 80-record file, and
   - the size the 18,000-record set would have once compressed.
   Egress well above the 80-record file size with no explanation pushes the estimate up.
3. **Access test.** Use read-level logs, if the workspace has them, to list which records or files the sessions opened, queried or copied. Each customer is recorded by internal ID only, not by copying the data out.
4. **Reach mapping (T4).** List every share, database and system the vendor credential and its group memberships could reach, and check each for the same indicators.
5. **Coverage check.** For each log source, record:
   - the period it covers and any gaps
   - its integrity (hash, immutable store)
   - whether it logs reads or only writes.
   Any gap that overlaps attacker activity is reported as a limit on how far the scope can be narrowed. It is not reported as a negative finding.
6. **Vendor records.** Reconcile the vendor's session logs (requested under C02) against the bank's own PAM and firewall logs. Until they are reconciled, they remain the vendor's account.
7. **Data minimisation.** The 18,000 records are not extracted in bulk for analysis. Analysts work with record IDs and hashes on the offline lab copy.

**Evidence that would increase the estimate (move customers into T1/T2 or widen T4):**
- egress volume larger than the 80-record export
- staging or archive files containing the wider set
- read or query logs touching records beyond the 80
- other sessions using the vendor credential (now or earlier) that reached the workspace
- the attacker publishing or offering rows outside the 80
- reports of misuse or fraud from affected customers or the Fraud team
- a successful post-revocation session (see Q07b) that touched data
- log gaps that overlap attacker sessions (these widen what cannot be excluded)

**Evidence that would reduce or close the estimate:** complete, integrity-checked logs at read level covering the whole period the credential was usable, which show only the one export, with total egress matching that export and no other reachable stores accessed.

**Owner.** Accountable: SEC. Executing: SEC forensic analysts, with the retained forensic firm on masked data. The DPO is told about each tier change.

**Timing.**
- An immediate note to LC, the DPO and the CMT chair that T1 = 80 is confirmed. This is needed for LC's HKMA update and for the Q08 decisions.
- Tier updates in each hourly SEC status report.
- A written scope paper for the DPO/LC review under PH01 10.4(b), well before first confirmation + 12h. If confirmation was 12:00, that review is due by 24:00 HKT. My target for the paper is 20:00 HKT (professional judgment, so the review has time to act).
- Any upward change is escalated at once.

**Recipient and channel.** Evidence register and decision log. Verbal briefing to the CMT chair, LC and DPO in the CMT room. Written scope paper on paper or the secure lab system. Corporate email is not used unless it has been logged as safe.

**Basis (external):**
- R11, PCPD Guidance on Data Breach Handling (June 2023), PDF p.4, "Step 1: Immediate gathering of essential information": the data user "shall promptly gather all relevant information of the data breach", including "How many data subjects might be affected?".
  - PDF p.5, Step 3, lists factors including "The amount of personal data involved".
  - Authority: PCPD regulatory guidance. It applies because a personal-data breach is now confirmed for 80 customers. Method and timing are left to judgment.
- R16b, HKMA circular "Customer Data Protection" (14 Oct 2014), PDF p.2, "Controls for handling incidents involving loss or leakage of customer data": procedures include "ascertaining the nature of the incidents, the causes of the incidents and identity of customers affected".
- R02, OCCICS Code of Practice s.7.2.3(a)(v)(3), PDF p.32: "Investigating the cause and impact of the incident".
- R03, HKMA Sectoral Code s.6.2.23(d), PDF p.18: logs "should contain sufficient information to support after-the-fact investigation". Any shortfall found in the coverage check is also a finding against this requirement.

**Basis (internal bank procedure, PH01 v1.0):**
- s.10.4(c): scope is set by "evidence that their records were accessed or copied; publication or offer of the data; reports of misuse; the sensitivity of the data types; and whether their records were held in the same place as confirmed records". "An unverified claim, or the size of the data store, does not by itself make everyone in the store a notification batch."
  - Application: the 18,000 share a location with the confirmed 80, and HKID data is sensitive. Those facts are inputs for the DPO/LC/CMT scope decision; the decision is theirs.
- s.10.4(b): 12-hour review "with SEC's evidence".
- s.6.4 (clocks), s.6.7(d) (reconciling supplier records), s.16.2 (masked data to the firm).
- Conflict check: none found.

== Q07b: Handling the vendor credential, active sessions and tokens ==

**Decision.** Revoking the password alone is not closure. The access window is treated as open until the PH01 7.4 closure test passes. All revocation and closure steps go ahead now; none of them is held.

**Action (IAM and Network execute under an emergency change record; the evidence custodian witnesses):**

1. **12:00–12:10: capture, capped at 10 minutes.** Snapshot the live session and token state for every vendor identity:
   - PAM active sessions
   - VPN concentrator sessions
   - identity-provider refresh and access tokens and OAuth grants
   - application session tables on the workspace and gateway
   - Kerberos tickets on reachable hosts.
   Stop trigger: if live data transfer is seen, terminate immediately without waiting for the capture to finish.
2. **By 12:15: terminate and revoke at every layer.**
   - end all sessions in PAM, VPN, the identity provider and applications
   - revoke refresh and access tokens and OAuth consents
   - revoke API keys, SSH keys and client certificates issued to the vendor
   - if the credential is a directory account, reset the password twice and purge its tickets.
   - Judgment, not a required step: if evidence of ticket forgery appears, a planned double krbtgt reset needs a separate change and a decision by the Head of IT Operations.
3. **Disable all other accounts of the same vendor** and block the vendor's source addresses and remote path at the perimeter. If this was done at C02, re-verify it and log the result.
4. **Rotate secrets readable through the vendor access:** service-account passwords, keys and configuration secrets on hosts the credential reached.
   - Precondition: the custodian has captured the current state first.
   - Hosts under evidence hold are not rebuilt.
   - Rotation is done through the credential stores, logged, and each rotation is validated.
5. **Persistence sweep.** Look for accounts, keys, scheduled tasks, services or MFA devices created or changed by the vendor credential. Capture each item, then disable or remove it under change control.
6. **By 12:30: closure test (PH01 7.4).**
   - From an isolated test host, an SEC operator with a witness replays a captured token and attempts a logon with the old credential.
   - Both must fail. Record the result and time.
   - If either succeeds: the window stays open, I re-block at the network layer at once, tell the CMT chair and LC, and extend Q07a's period of interest up to the present.
7. **Monitoring.** Alert on any use of the vendor identifiers, source IPs or captured token IDs. Any hit is a stop trigger and is escalated at once.
8. **Reinstatement is held.** Vendor access returns only after:
   - the cause is known
   - the access meets the PH01 7.2 standard (named accounts, MFA, time-limited, recorded)
   - the secrets are rotated
   - I give written sign-off, the CMT chair decides, and LC is consulted on the contract terms.
   Until then, any vendor support for recovery goes only through bank-operated, supervised sessions.

**Owner.**
- SEC decides and is accountable.
- IAM, Network and IT Operations execute.
- The Head of IT Operations is consulted if disabling an account or rotating a secret would affect a service that is working now.
- The vendor relationship owner tells the vendor through the contract contact with a call-back, giving no technical detail beyond what is needed.

**Timing.** Capture 12:00–12:10. Revocation by 12:15. Closure test logged by 12:30. Status in the 13:00 SEC report.

**Recipient and channel.** Emergency change record, decision log and evidence register. Briefing to the CMT chair and LC. LC can use the result for the containment items of the Cap. 653 report: R02, PDF p.45, "Damage Containment: ☐ Compromised accounts have been removed or isolated".

**Basis (external):**
- R11, PDF p.5, Step 2 "Containing the data breach": "Changing users' passwords and system configurations to block any (further) unauthorised access" and "Removing the access rights of users suspected to have committed or contributed to the data breach".
  - Applies because the credential was used in a confirmed data export. The technical steps are left to judgment.
- R10, PDPO Sch.1 DPP4(1), PDF p.169: "All practicable steps shall be taken to ensure that any personal data ... is protected against unauthorized or accidental access". Statutory. Live sessions are a continuing risk of unauthorised access to the 18,000 records.
- R08, SPM TM-G-1 s.3.2.3, PDF p.12: "Extra care should be exercised when controlling the use of and access to privileged and emergency IDs". A vendor support account is privileged.
- R03, HKMA Sectoral Code s.6.2.25(a), PDF p.19: manage supply-chain risk for critical computer systems.

**Basis (internal bank procedure, PH01 v1.0):**
- s.7.3: "SEC captures session and token state (10 minutes at most), then terminates all sessions, revokes tokens and keys, and disables the account and every other account of the same vendor."
- s.7.4 "Closure test": "A credential is closed only when a replayed token and a logon with the old credential both fail ... Until then the access window is treated as open."
- s.7.5: reinstatement conditions.
- s.3: the CMT chair reinstates vendor access on SEC's written sign-off.
- Conflict check: none found. The order "capture first, terminate at once if transfer is active" is consistent with R02 s.7.2.3(f), which gives priority to swift containment.

== Facts passed to the incident team ==
1. **To LC and the DPO (for Q08):**
   - Confirmed: 80 customers, with data types name, HKID and telephone, and the time the export was logged.
   - The wider set of up to 18,000 is possible but not shown; T2 is currently 0.
   - The closure-test result and time, and whether the access window is closed or still open.
   - The time of first confirmation, which starts the 12-hour review clock.
   - LC should also update the HKMA on confirmed data exposure, a PH01 5.8 trigger.
2. **To COM (for Q09):**
   - Confirmed and safe to state: 80 customers, and the data types.
   - Not to be stated as fact: "18,000 affected", or "no wider data taken".
   - Do not name the vendor, the system or the attacker.
   - Customers should watch for calls impersonating the bank. HKID and telephone numbers make social-engineering calls easier; this is my professional judgment.
3. **To Fraud and Payments:** the 80 customer IDs, for increased monitoring and checks on contact-detail changes (PH01 10.5).
4. **To the CMT chair:**
   - Mobile transfer submission is still interrupted. Payment recovery remains on hold under 8.2 and 9.3.
   - The 24-hour tolerance runs out at 08:00 HKT on 17 Nov; the 50% point (20:00 HKT) is when the chair must notify the Board chair.