SEC (Information Security Lead): locked response for C08, Thursday 19 Nov 2026, 08:00 HKT (H+72). I answer only Q22a and Q22b. My execution-state baseline is the facilitator's handoff for Q16a, Q16b and Q19b.

**Facts as given**
- A second offline test reconciled all 240 *sampled* instructions. It ran on a rebuilt access environment.
- The offline environment has had no new alarms for six hours. These results describe the test environment only. They say nothing about production or about containment.

**Not recorded on any card, so they cannot be verified:**
- secondary-process clearance (17 Nov 21:00) and any re-clearance;
- Q19b indicator classification and the 14:00 sweep results;
- vendor credential closure test result;
- root cause of the C06 mismatches;
- a full-set re-test;
- the Q13a separation, backup and test-data records.

All actions below are simulated, for the facilitator to log.

== Q22a: Restrictions to keep or release, and the handover to standing operations ==

**Decision: nothing is released at H+72. Every restriction stays in force after handover until its release condition is met and the decision-maker under PH01 s.3 logs the release.**

| Restriction | Keep or release | Release condition |
|---|---|---|
| 1. Original gateway: network quarantine and evidence hold | KEEP | No restore to production, ever (s.9.1). Evidence release item by item, jointly by SEC and LC, after consulting the forensic lead. Disposal only under the s.17 legal hold rules. |
| 2. Recovered system: production HOLD | KEEP | See below. |
| 3. Secondary process | HOLD, unless SEC's written s.8.2 re-clearance and a clean Q19b sweep are logged | If it is running under a logged clearance, the Q16b stop and reconciliation controls continue. |
| 4. Raised monitoring: indicator detection and blocking in EDR, SIEM, DNS and proxy; heightened alerting on vendor identifiers and captured tokens | KEEP | Release (back to baseline) only after containment is confirmed by evidence: the Q19b indicator is classified, sweeps are clean, the closure test has passed, and a quiet period runs in production (my judgment: 14 days). SEC logs the release. |
| 5. SEC reports to the CEO | Hourly until containment is confirmed, then four-hourly | — |
| 6. Vendor access: revoked, perimeter block in place | KEEP | Reinstatement only under s.7.5: CEO decision on SEC's written sign-off, LC consulted. |
| 7. Front-end service message rejecting or queuing transfer submissions | KEEP | Until a cleared production path exists. Changes coordinated with Payments and COM. |
| 8. Q16b stop and rollback criteria | KEEP as standing controls | — |

**Why the recovered system stays on HOLD (item 2):**
- "All 240 sampled" is recorded as a sample result, not a pass of the whole set (s.9.2).
- The second test used a rebuilt access environment. That exact configuration has to be the one proposed for production, shown by its build record and hashes.
- The C06 mismatches still have no logged root cause.
- No s.9.3 gate item is evidenced.

Release of item 2 needs every s.9.3 item logged with evidence and signer, then the CEO's authorisation. No item can be waived.

**Handover actions**

1. **Pack structure.** Each handover pack starts with a "not evidenced" page. Every unevidenced item moves across as open, not done. My list of unevidenced items:
   - closure test result;
   - secondary clearance decisions due 16 Nov 19:00 and 17 Nov 21:00, and any re-clearance;
   - Q19b classification and sweep;
   - Q07a tier results and the content of the scope paper;
   - 16 Nov 08:30 filing-terminal and email logs;
   - 09:00 supplier requests and LC clearance;
   - Q13a separation, backup timing and immutability, and test-data records;
   - whether the backup is the STDB;
   - root cause of the 2 mismatches;
   - full-set re-test;
   - delivery channel for the forensic partner's records;
   - timeline v1 and its review status.
2. **Receiving owners.** Each signs acceptance of a specific list:
   - **SOC manager:** monitoring rules, the indicator hunt, escalation triggers.
   - **Head of IT Operations:** quarantine, the isolated recovery environment, the candidate build and its re-test, the change records.
   - **Head of Payments Operations:** instruction register, held and unknown-status items, secondary-process controls.
   - **Evidence custodian:** evidence register and chain of custody.
   - **IAM lead:** vendor accounts, tokens, keys and rotation evidence.
   - **Vendor relationship owner:** supplier preservation and production requests.
   - **LC:** facts for the deadline register.

   SEC remains the security sign-off authority for clearances, the closure test and the release of monitoring.
3. **Changes to pass to LC.** I give LC the list of changes deployed to the critical computer systems (CCS) during the incident, each with its deployment date, so LC can decide whether any must be notified:
   - network quarantine rules;
   - account disablement;
   - rotation of secrets and keys;
   - detection rules;
   - any re-keying.
4. **Facts to LC for HKMA progress reports.** Containment is unconfirmed. Production is on HOLD. The secondary process status is as recorded.
5. **Reconvening.** The CMT is reconvened at once on any security trigger, including an indicator outside quarantine, use of the vendor credential, or a new data exposure.

**Owner, timing, destination**
- Accountable: SEC. Executing: the receiving owners above. Release decisions remain with the s.3 decision-makers.
- Timing: handover packs signed by 18:00 HKT on 19 Nov (my judgment). Restrictions stay until their logged releases.
- Destination: handover packs; decision log entries with status "held"; evidence register; signed acceptance sheets; summary briefing to the CEO.

**Basis: external**
- R08, SPM TM-G-1 s.4.2.4, PDF p.18: "only properly tested and approved systems are promoted to the production environment." A sample pass in a test environment does not meet this for production.
- R07, SPM TM-G-2 s.1.3.3, PDF p.5: "The HKMA should also receive periodic progress reports upon being notified until the final resolution of the crisis." This supports keeping SEC's facts flowing to LC after handover.
- R03, HKMA Sectoral Code s.6.2.26(a), PDF p.19: designated AIs should "implement measures to detect computer-system security incidents affecting CCSs". This supports keeping raised detection while containment is unconfirmed.
- R05, PDF p.1, "Immediate incident response": contain and safeguard customers' interests.
- How long monitoring stays raised is my professional judgment.

**Basis: internal (Internal bank procedure, PH01 v1.0)**
- s.18.1: "only when each open item has a named receiving owner who has signed acceptance of a specific list."
- s.18.2: "Items without evidence transfer as open, not done."
- s.18.3: "Restrictions stay in force after handover until their release condition is met and the decision-maker in section 3 has logged the release."
- s.18.4: changes deployed to a CCS are separate items, and LC decides notification (Cap. 653 s.22; HKMA Code s.6.1).
- Also s.18.5, s.9.2 ("A sample result is recorded as a sample"), s.9.3, s.2.5, s.7.5.
- Conflict check: none found.

== Q22b: Root-cause remediation and the evidence to close the vendor credential issue ==

**Decision.** Remediation is assigned through a written treatment plan. Each finding has a named owner, a due date and monitoring. Two milestones are closed separately:
- **(A) Credential closed** (s.7.4): the old access no longer works.
- **(B) Vendor access issue closed** (s.7.5): cause known, and any future access meets the s.7.2 standard.

Closing (A) does not close (B).

**Remediation items**

| # | Item | Owner | Target |
|---|---|---|---|
| 1 | **Credential misuse root cause.** How the vendor support credential was obtained and used: vendor-side compromise, theft, shared account, MFA bypass or token reuse. Was the account compliant with s.7.2 (named, MFA, time-limited through PAM, recorded)? Uses the vendor's reconciled records and the Q19a timeline. | SEC, with the vendor relationship owner and the CRO (third-party register) | Interim finding 3 Dec 2026 |
| 2 | **Privileged and remote-access controls.** Every vendor and admin path to CCS goes through PAM, with named accounts, MFA, time limits and session recording. Shared accounts removed. Token lifetimes and revocation reach tested at every layer. | IAM lead and Head of IT Operations | 31 Dec 2026 |
| 3 | **Segmentation and gateway hardening,** including whatever the rebuilt access environment used in test 2 showed. | Head of IT Operations, SEC verifying | 31 Dec 2026 |
| 4 | **Logging and clocks.** Close the log-coverage gaps; fix the up-to-4-minute clock drift against the primary time source. | Head of IT Operations and SOC | 4 Dec 2026 |
| 5 | **Backup and STDB.** Confirm STDB status and dwell-time-safe retention for the gateway. | Head of IT Operations | 31 Dec 2026 |
| 6 | **Detection gaps** behind the delayed detection of the export and the new indicator. | SOC manager | 4 Dec 2026 |
| 7 | **Post-incident risk assessment** of the gateway CCS (vulnerability assessment and penetration test), with a treatment plan. | SEC | Plan by 31 Dec 2026 |
| 8 | **Post-incident review,** including the playbook gaps found: no security stop for the alternate process in s.8.7; no defined start for the four hours in s.6.7(c). | SEC, for CEO approval | Draft 18 Dec 2026 |

All dates are my professional judgment, set on a risk basis. LC is told of any change that needs notification.

**Evidence required to close (A), the credential**
1. A closure test (s.7.4) logged with the time, operator and witness: a replay of a captured token *and* a logon with the old credential both fail. If it is not already on record, it is re-run on 19 Nov by 10:00 HKT. If either attempt succeeds, the access window is treated as open, Q07a is extended to the present, and the CMT is reconvened.
2. IdP, PAM, directory and VPN exports showing every account, token, key and certificate of the vendor disabled or revoked.
3. Evidence of the perimeter block on the vendor path.
4. Rotation records for every secret readable through the old access.
5. A timeline (Q19a) showing no use after revocation beyond its uncertainty band.
6. The Q19b indicator classified, and either shown to be unrelated to the vendor credential or resolved.

**Additional evidence to close (B), the vendor access issue**
1. Root cause established, with the vendor's records received by an approved channel, hash-checked, and reconciled with the bank's logs (s.6.7(b) and (d)).
2. The vendor's remediation confirmed in writing.
3. Any proposed new access designed to s.7.2 and tested.
4. SEC's written sign-off, then the CEO's reinstatement decision, with LC consulted on contract terms. Until then, reinstatement is on HOLD.

**Owner, timing, destination**
- Accountable: SEC. Executing: as assigned above.
- Timing: closure test by 10:00 HKT on 19 Nov; remediation dates as above.
- Destination: treatment plan register, decision log, evidence register; status reported to the CEO and Board; facts to LC.

**Basis: external**
- R03, HKMA Sectoral Code s.6.3.7(c), PDF p.20: the report should include a "Treatment plan for each finding, with timeline and responsible party for executing and monitoring the implementation of the plan."
- R02, OCCICS Code of Practice s.7.2.3(i), PDF p.33: the post-incident review covers "Facts and causes of the incident", gaps, effectiveness, and "Improvement actions recommended."
- R13, HKMA circular of 1 Jun 2026, PDF p.3: "There should also be a clear risk-based framework for determining the timeline and priority of remediations."
- R03 s.6.2.25(a), PDF p.19: manage supply-chain risks of CCS.
- R08, TM-G-1 s.3.2.3, PDF p.12: "Extra care should be exercised when controlling the use of and access to privileged and emergency IDs."
- R11, PCPD Guidance, PDF p.5, Step 2: "Removing the access rights of users suspected to have committed or contributed to the data breach."
- Dates and the A/B split are my professional judgment.

**Basis: internal (Internal bank procedure, PH01 v1.0)**
- s.7.4: "A credential is closed only when a replayed token and a logon with the old credential both fail, and the result and time are logged. Until then the access window is treated as open."
- s.7.5: "Vendor access is reinstated only when: the cause of the compromise is known; the access meets 7.2; secrets readable by the old access are rotated; and SEC signs off in writing."
- s.7.2: vendor access standard.
- s.6.7(d): supplier records reconciled.
- s.3: reinstatement by the CMT chair on SEC's written sign-off.
- Conflict check: none found.

== Facts I am passing to the incident team ==
1. **To LC (Q23).** The CCS change list with dates. The records SEC holds under preservation: original gateway images, evidence register, timeline, vendor records, the quarantined host. The third-party copies held by the forensic firm and the forensic partner, for return or destruction once their engagements end. Production remains on HOLD.
2. **To COM (Q24).** Do not publish a closing update. The s.11.5 conditions are not met: there is no production service that SEC has confirmed stable. Payment service is not restored and its status is as recorded.
3. **To the CEO and Board.** Containment confirmation is still open. The recovered-system gate is unmet. The secondary process's status cannot be verified from the record. The remediation plan owners and dates are above.