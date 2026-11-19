SEC RESPONSE - C01 (Mon 16 Nov 2026, 08:00 HKT, H+0) - Unit Q01 a and b. Locked before colleagues' answers.

Internal bank procedure (PH01): N/A for both units. PH01 is not in my allowed manifest (search "PH01": 0 hits), so no internal basis and no conflict check is possible.

Fact status I am working from
- Confirmed by the card: unauthorised commands encrypted payment gateway components (a designated critical computer system, CCS); outbound domestic transfers and payroll submission are disrupted; mobile balance viewing works; branches are open; dispatch log is empty.
- Unverified or unknown: whether encryption is still spreading; entry point and accounts used; whether mobile, branch or core systems share credentials, management tooling or middleware with the gateway; whether data left the bank; whether backups and the standby gateway are clean (failover is unverified); whether the secure-filing terminal outage is related; whether the gateway is vendor-managed; content of the bank's own emergency response plan.

---

Q01a - What to isolate first, without disabling available services

Decision. Isolate the payment gateway CCS at the network layer first: the segment hosting the encrypted components, plus the route the unauthorised commands used (privileged and service accounts, and admin or remote access paths into the gateway). No bank-wide shutdown and no power-off of affected hosts. Hold on failover and on any restore.

Simulated actions for the log (role names other than SEC are assumed, since PH01 is absent):

| Step | Operator | What is changed | Precondition | Validation |
|---|---|---|---|---|
| 1 | Network Operations | Deny-all at the gateway segment boundary (firewalls, ACLs) towards core, mobile, branch and backup networks; close gateway connections to external payment and payroll interfaces; allow only a path to a clean forensic collector | Device configs and rule bases exported first; emergency change record opened; gateway information owner approves, or endorses afterwards if unreachable | Boundary logs show no permitted flows out of the segment |
| 2 | Identity/privileged access admins | Suspend (not delete) accounts able to issue commands on the gateway; revoke sessions, tokens and keys; block remote and vendor admin access | Account and session state exported first; work from a clean admin workstation | No new privileged logons to the gateway |
| 3 | Backup/storage team | Suspend backup and replication jobs from the gateway to standby and backup stores | Confirm which copy is offline or immutable | Job logs show no writes after the hold |
| 4 | IT Operations (hold) | Standby gateway is not activated | Released only when SEC confirms no shared credentials, no replicated encrypted data and no indicators of compromise, and IT has tested it in isolation | Recorded SEC release |
| 5 | Security Operations Centre | Heightened monitoring of mobile, core, branch and directory systems using indicators from the gateway | None | Half-hourly report |

How available services are protected (professional judgment). Outbound transfers and payroll are already down, so isolating the gateway removes no service known to be working at this card. Mobile balance viewing and branches stay up on two conditions: no indicator of compromise on those systems, and the dependency map shows they do not need the gateway segment. Each link is checked against the network diagram before it is cut, and after Step 1 a mobile balance test and one branch teller confirmation are run.

Stop and escalation triggers
- Encryption or unauthorised commands seen outside the gateway segment: extend isolation to that segment. If that would disable a live customer service, SEC acts at once only when destructive activity is active and informs the crisis management team (CMT) immediately; otherwise CMT decides.
- An isolation rule unexpectedly breaks mobile balance viewing or a branch function: roll back that rule only, using the saved configuration, if the flow is verified benign; otherwise keep it and escalate.
- Any sign of unauthorised payment instructions: tell the incident commander and LC immediately.

Accountable owner: SEC. Executing parties: as in the table. CMT ratifies, and decides any step that removes a working customer service.

Time (judgment targets; no fixed time limit for containment was located): start 08:00 HKT; Step 1 in place by 08:10; validation by 08:20; report to CMT by 08:30; re-validate every 30 minutes.

Destination and channel: gateway boundary devices and the identity/privileged access systems, instructed by emergency change record and an out-of-band phone bridge, with each instruction entered in the incident log (entry 1 opens the empty log). Status goes to the incident commander/CMT, LC, COM and IT Operations.

Basis
- R05, HKMA circular "Incident response and management procedures", PDF p.1, heading "Immediate incident response", sole paragraph (checked against the scan): "The AI concerned should immediately analyse the cause of the incident and as soon as practicable rectify or contain the problem." Authority: HKMA supervisory circular to all authorized institutions. Applies because the bank is a licensed bank and a critical payment service is disrupted. It leaves what to contain and how to judgment.
- R02, OCCICS Code of Practice (Generic), s.7.2.3(a)(v)(1), PDF p.32: playbooks for "Containing the incident to prevent further harm;". Authority: code issued under Cap. 653 s.8; not subsidiary legislation (R02 s.1.1.4, p.4). It reaches designated banks through R03 s.1.1.3, p.3: "A Designated AI should refer to guidance published by the Commissioner in relation to category 3 obligations, which can be found in section 7 of the Code of Practice (Generic)". I infer R03 applies because the bank is a licensed bank with CI operator designation; the card does not name the designating authority.
- R01, Cap. 653, s.27(5), PDF p.43: "A CI operator must implement an emergency response plan." Binding statute. Missing fact: the bank's plan is not in my sources. Conditional action: if the plan's containment playbook differs from the steps above, follow the plan and log the deviation.
- R08, SPM TM-G-1, s.4.3.2, PDF p.19: "Emergency changes should be approved by the information owner (for application system or production data related changes) and other relevant parties at the time of change." and s.4.3.3, PDF p.20: "Emergency changes should be logged and backed up". HKMA supervisory guidance; it governs how the isolation changes are approved, recorded and made reversible.
- R07, SPM TM-G-2, s.4.2.2, PDF pp.9-10: crisis process for "dealing with and containing an emergency to avoid spillover effects to the business as a whole", with the CMT "to make quick decisions on the appropriate responses for action (i.e. staff safety, incident containment and specific crisis management procedures)". Supports targeted containment and CMT ratification.
- R09, SPM TM-E-1, s.8.2.1, PDF p.32: "The top priority should be to protect the interests of customers who have been or may be affected by the incident." And s.9.4.1, PDF p.35: "It is important that the actual effectiveness of the resilience of the system should be properly verified and tested." General principles supporting keeping mobile service up and holding unverified failover.
- R03, HKMA Sectoral Code, s.6.2.13(b), PDF p.14: "a Designated AI should ensure that all passwords are promptly changed if they have been or are suspected of being compromised". Missing fact: which credentials. Suspend now; reset once scope is known.
- R02 s.6.2.20(c), PDF p.18: "An immutable copy or a copy that is physically disconnected from a CCS should be stored to avoid corruption of backup data if the CCS is compromised." Supports Step 3. Missing fact: whether that copy exists and is intact.
- Conditional only (personal data involvement unknown): R16a, PCPD form annex, PDF p.4, "Cyberattack - Immediate Remedial Measures": "Disconnect the compromised device from the Internet and any network to which it is linked". Non-binding PCPD tips.

No direct rule located in assigned sources for which component to isolate first, the order of steps, network isolation versus power-off, or the timing targets. Those are professional judgment: network isolation stops spread while keeping host memory and disks intact for Q01b.

---

Q01b - Evidence to secure before systems are changed, and custody record

Decision. An evidence hold on the gateway CCS takes effect at 08:00 HKT. No reboot, power-off, clean-up, patch, decryption attempt, rebuild, restore or failover of affected components until SEC records an evidence release for that item. Network isolation in Q01a is not held, because it changes boundary devices, not the affected hosts.

Evidence to secure, most perishable first (order is professional judgment):
1. Before Step 1: running configuration, rule base and session tables of each boundary device to be changed.
2. Live state of encrypted gateway hosts and the admin or jump hosts used: memory images, processes, network connections, logged-on sessions, scheduled tasks; hypervisor snapshots with memory where virtual.
3. Logs, exported to an isolated store with rotation and purge suspended: gateway application and transaction logs, operating system and security logs, privileged access records and session recordings, authentication, endpoint detection, central log platform, firewall, proxy, DNS, remote access, database audit and backup system logs.
4. The unauthorised commands themselves: command lines, scripts, timestamps, source account and source host; any malware files; samples of encrypted files; any ransom note (none is reported at this card).
5. Payment state: last successful outbound message, and queued or pending transfer and payroll files, for later reconciliation.
6. Disk images or storage-level snapshots of every encrypted component, before any rebuild or restore.
7. Each host's clock offset against the bank's primary time source; console photographs; data centre access records; notes of who observed what and when, including the 08:00 confirmation.
8. The secure-filing terminal: preserved untouched until SEC establishes whether its outage is related.

Scope of production and offline evidence (judgment). Production evidence is the live state of compromised hosts. It shows what is there now, but the attacker may have altered or deleted on-host logs, so it does not by itself prove what did not happen, for example that no data left. Offline evidence (central log copies, offline or immutable backups, forensic images) is more reliable but only up to its capture time. A clean offline backup does not show the standby gateway or production is clean, and an offline test does not validate production failover. Backup sets are preserved as evidence, their rotation is suspended, and they are examined only in an isolated environment.

Custody record. One evidence register plus a chain-of-custody form per item, recording:
- Unique evidence ID, description, source system (hostname, asset ID, location).
- Acquisition date and time in HKT, clock offset, acquirer and witness, tool and version.
- SHA-256 hash taken at acquisition and re-verified on every copy.
- Storage location: sealed tamper-evident bag in a locked safe for media; access-controlled write-once repository for digital items.
- Every transfer (from, to, time, purpose, signatures) and every access.
Analysis is done on verified working copies only; masters stay sealed. The evidence custodian is an SEC designate who is not an administrator of the affected systems. Any change that collection tools make on a host is noted. Every action and decision is also entered in the incident log.

Accountable owner: SEC. Executing parties: bank forensic staff and Security Operations Centre; platform, network, database and backup administrators acting only on SEC instruction; an external forensic firm if one is retained (unknown; if none, SEC asks the incident commander for emergency engagement by 08:30).

Time and triggers (judgment):
- 08:00: hold issued, register opened.
- 08:00-08:10: items 1 and 2, capped at 10 minutes. If encryption is seen still spreading, Step 1 goes ahead immediately and memory is captured afterwards on the isolated hosts.
- By 09:00: log exports complete or running; first custody status to the incident commander.
- Observable trigger: no recovery change proceeds without a recorded SEC evidence release.

Destination and channel: the evidence repository, safe and register. The hold notice goes to IT Operations, administrators, the backup team, the Security Operations Centre and any gateway service provider, by out-of-band bridge and a written notice entered in the incident log.

Basis
- R02 s.7.2.3(a)(v)(2), PDF p.32: playbooks for "Digital evidence handling, including identification, collection, acquisition, preservation of evidence and chain of custody;" and (4): "Recording the incident response process, including details of the incident, actions taken and decisions made;". Authority and scope as for Q01a. It names the subjects but leaves methods to the operator.
- R02 s.7.2.3(f), PDF p.33: "When balancing the need for timely system recovery and digital evidence handling, the CI operator should prioritize incidents which had impacted business operations, require swift damage containment or need immediate system recovery. Otherwise, more time should be allocated to evidence collection." Business operations are affected here, so pre-isolation capture is capped and containment is not delayed.
- R02 s.7.2.3(h), PDF p.33: "The CI operator should engage capable incident response and forensic examination personnel to assist with digital evidence collection and incident investigation."
- R01 s.27(5), PDF p.43 (quoted above), with Schedule 3 Part 2 item 4, PDF p.93: "The procedures for investigating the cause and assessing the impact of computer-system security incidents." Missing fact: the bank's plan; follow it where it specifies evidence steps.
- R03 s.6.2.23(c), PDF p.18: "Such logs should be secured so that they cannot be deleted or altered, and can be read only by authorised persons." and (d): "Retained logs should contain sufficient information to support after-the-fact investigation of computer-system security incident(s)". Supports the log export and purge suspension.
- R08 s.4.3.3, PDF p.20 (quoted above): supports capturing device configurations before each change.
- Context, not a current duty: R01 s.36(2)(b), PDF p.52, an authorised officer may by written notice require the operator "to preserve the state of the system;", and s.35(1)(a), PDF p.50, may require documents. No notice has been received; preserving evidence keeps the bank able to comply.
- General principles: R06 SPM OR-2 s.8.3, PDF p.13, "Root cause analysis of incidents to help with the prevention or minimisation of recurrence."; R02 s.6.2.23(g), PDF p.20, clock synchronisation "to enable accurate log-event correlation across the systems".
- Conditional (personal data involvement unknown): R11, PCPD Guidance, PDF p.5, Step 2 list: "Keeping a proper record of the compromised system for further investigation". Non-binding.

No direct rule located in assigned sources for memory or disk imaging, hashing, order of collection, custody form fields, two-person handling, or custodian independence. These are professional judgment, chosen so the evidence can support root-cause findings and withstand regulatory or police scrutiny.

---

Facts SEC passes to the incident team (first fact sheet by 08:30 HKT, then every 30 minutes)

| Fact | Status at 08:00 | Used by |
|---|---|---|
| Unauthorised commands were run on the designated payment gateway and components are encrypted | Confirmed | LC: R01 s.2, PDF p.10, "any other act done, without lawful authority" with "an actual adverse effect" |
| Domestic transfer and payroll processing (core function) is disrupted | Confirmed | LC, COM |
| Time the bank became aware | 08:00 HKT 16 Nov 2026 per card | LC |
| Earliest identifiable time of the incident | Unknown, pending log review | LC (R02 Annex E item B3, PDF p.42) |
| Nature | Unauthorised access confirmed; "ransomware" unverified (encryption seen, no demand reported) | LC, COM |
| Entry point, accounts used, root cause | Unknown | LC |
| Data compromise or leakage | Unknown; no evidence either way | LC, COM |
| Mobile balance viewing and branches | Working; not yet verified clean | COM, CMT |
| Failover and backups | Unverified; on hold | CMT, COM (no restoration time can be given) |
| Secure-filing terminal | Unavailable; relation to incident unknown | LC (channel choice is LC's decision) |
| Containment steps and times | Reported as executed | LC (R02 Annex F part D, PDF p.45: "Affected systems or network segments have been isolated") |

For LC's telephone notification, SEC supplies the three items in R02 s.7.3.6(b), PDF p.36: "Nature of the computer-system security incident;", "CCSs involved; and", "Brief incident summary." Whether and when to notify is LC's unit (Q02), not decided here.

---

Search record and limitations
- Tools: text search and page reads only. R05 is a scan; the quotation was checked against the page 1 image.
- Terms searched across all documents: "isolat"; "containment"; "evidence"; "custody"; "forensic"; "preserv"; "ransom"; "audit trail"; "emergency change"; "PH01"; regex "hash|write.?block|memory dump|volatile|snapshot|disk image|forensic image" (one irrelevant hit, R09 p.38); regex "quarantin|disconnect|segregat|segment"; regex "failover|fail-over|fallback|alternate site"; regex "record.?keeping|keep(ing)? (a )?(proper )?records?|actions taken and decisions made"; regex "law enforcement|Police".
- Terms searched in single documents: "incident" in R03, R04, R06, R07, R08, R09; "log" in R02; "emergency response plan", "computer-system security incident" and "Schedule 6" in R01.
- "custody" and "forensic" returned relevant hits only in R02 pp.32-33.
- Not available to me: the bank's emergency response plan, and the C-RAF and HKAB STDB Guideline that R03 refers to.