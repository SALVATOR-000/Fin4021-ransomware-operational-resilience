SEC RESPONSE - C03 (Mon 16 Nov 2026, 12:00 HKT, H+4) - Unit Q07 a and b. Locked before colleagues' answers.

Internal bank procedure (PH01): N/A for both units. PH01 is not in my allowed manifest, so no internal basis and no conflict check is possible.

Fact status I am working from
- Confirmed by the card: the sample matches bank records; independent time-stamped logs confirm unauthorised export of a file with 80 customers' names, Hong Kong identity card numbers and telephone numbers; the same workspace holds records for up to 18,000 customers; a vendor support credential was used in the relevant session; mobile transfer submission is still interrupted.
- Unverified or unknown: export of the wider set; whether the wider records hold more fields than the three confirmed; whether the revoked credential still has live sessions or tokens; how the credential was obtained; whether other credentials or sessions touched the workspace; whether vendor session records requested under C02 (due 12:00) have arrived.

---

Q07a - Establishing the scope of exfiltration, and what would change the estimate

Decision. SEC issues a three-tier scope statement and revises it only on evidence:
- Confirmed exported: 80 customers (name, identity card number, telephone number). This is the floor; it cannot go down.
- Accessible, export unverified: up to 18,000 customers in the same workspace. SEC reports this as neither "exported" nor "safe".
- Unknown: any data outside the workspace that the credential or session could reach.
The estimate stays provisional until Q07b confirms the access window is closed.

Simulated actions for the log (five workstreams, run in parallel)
1. Session reconstruction. Rebuild a timeline of every session by the vendor credential and anything derived from it: logons, commands, files opened, archives created, export actions. Sources: bank-side privileged access and remote access logs, workspace file and database audit logs, forensic images from C01, and the vendor's session records from C02.
2. Outbound volume test. From independent network records (firewall, proxy, traffic flow, DNS, data-loss tooling), total the bytes sent to external destinations during the access window. Compare with the size of the 80-record file and the smallest compressed size of the wider set.
3. Workspace inventory. The data owner lists every file and table in the workspace, the fields in each, and the count of unique individuals, separating bank customers from payroll payees. "Up to 18,000" becomes an exact list held by internal reference.
4. Window and coverage. Fix the first and last use of the credential and its tokens, and mark every period where logging is missing or came only from compromised hosts.
5. Other routes. Check for other accounts or sessions that reached the workspace, and for capture through the remote session itself (screen display, clipboard, the remote tool's file transfer), which bank network records would not show. The attacker's screenshot makes on-screen capture a live possibility.

Evidence that would change the estimate (professional judgment)

| Direction | Evidence |
|---|---|
| Up | File or database audit entries showing the wider files were read, queried or copied in the session |
| Up | Archive or staging files, or deleted traces of them, containing wider records |
| Up | Outbound volume at or above the size of the wider set, or further export events |
| Up | Vendor session records or recordings showing bulk display, clipboard use or file transfer of wider data |
| Up | A new attacker sample or publication with records outside the 80 that match bank records (validated by the C02 method; SEC does not solicit samples) |
| Up | Other credentials, sessions or tokens found to have reached the workspace, or any activity after the revocation |
| Cannot exclude | Logging gaps inside the access window: the affected records stay in the "unverified" tier and SEC tells LC export cannot be ruled out |
| Bounds the estimate | Complete independent logs for the whole window showing only the 80-record file left, outbound volume too small for more, audit entries showing wider files unopened, and bank and vendor records that reconcile |

Absence of traces in logs taken from compromised hosts is not treated as evidence that nothing more was taken.

Accountable owner: SEC. Executing parties: bank forensic staff and the external forensic firm, Security Operations Centre, network operations, the workspace data owner, and the vendor for its records.

Time and triggers (judgment targets): scope statement v1 at 12:30 HKT; v2 at 15:00 after the outbound volume and audit analysis; v3 at 18:00 after the vendor material due under C02; then daily. Any "up" evidence goes to LC, the privacy officer and the incident commander within 30 minutes, without waiting for the next version.

Destination and channel: scope statement (counts, fields, confidence, evidence references, no personal data) to the incident commander, LC and the privacy officer over the out-of-band bridge and restricted incident workspace. COM receives approved figures only.

Basis
- R16b, HKMA circular "Customer Data Protection", PDF p.2, heading "Controls for handling incidents involving loss or leakage of customer data": procedures should cover "ascertaining the nature of the incidents, the causes of the incidents and identity of customers affected". HKMA supervisory circular to all authorized institutions; it applies because customer data has leaked. It leaves the method to the bank.
- R11, PCPD Guidance, PDF p.4, Step 1: questions to address include "What kind of personal data was involved?" and "How many data subjects might be affected?". PDF p.6, Step 5: "A comprehensive record of the incident is therefore required, which should include all facts relating to the breach". Non-binding PCPD guidance; a data breach is now confirmed for 80 individuals.
- R11, PDF p.8: "A notification should generally be given as soon as practicable after becoming aware of the incident, regardless of the progress of any internal investigation." This is why SEC issues provisional tiers now and does not ask LC to wait for a final figure.
- R02, OCCICS Code of Practice (Generic), s.7.2.3(a)(v)(3), PDF p.32: "Investigating the cause and impact of the incident;", and Annex F item C(3), PDF p.45: "Data Impact (if any sensitive information was compromised, altered or lost):". The scope finding feeds the written report. Authority and scope as in my C01 answer.
- R03, HKMA Sectoral Code, s.6.2.23(d), PDF p.18: "Retained logs should contain sufficient information to support after-the-fact investigation of computer-system security incident(s)". R08, SPM TM-G-1, s.3.4.1, PDF p.15: "the logs should be securely protected from manipulation". These support relying on independent logs over host logs. Whether the bank's logs meet this is being tested in workstream 4.
- R16b Annex D, PDF p.5: "proper and timely follow-up actions should be taken upon the detection to ascertain whether leakage of consumer data has actually happened". Written for detection of unusual transmissions; I use it as a general principle.

No direct rule located in assigned sources for the scoping method, the three tiers, volume comparison, or review times. Files: all. Terms: regex "number of (data subjects|individuals|customers) affected|approximate number|extent of"; regex "exfiltrat|leak|dark web|screenshot|sample"; "session"; "token". These are professional judgment.

---

Q07b - Vendor credential, active sessions and related tokens

Decision. Treat the vendor credential as compromised and its revocation as incomplete until tested. Capture the live session and token state as evidence, then terminate every session, invalidate every token and key tied to that identity, rotate secrets the session could have read, and prove closure by test. No vendor access is reinstated without SEC sign-off.

Simulated actions for the log

| Step | Operator | What is changed | Precondition | Validation |
|---|---|---|---|---|
| 1 | Security Operations Centre | Nothing: export of current session tables, token and key inventory, and authentication logs for the identity | Capped at 10 minutes; hashed into the evidence register | Export complete |
| 2 | Identity and privileged access admins | All sessions for the identity terminated on each layer: remote access gateway, jump host, directory, workspace, gateway application, databases, remote support tool | Step 1 done or timed out | Zero sessions for the identity on each layer |
| 3 | Identity admins, platform owners | Refresh and access tokens, API keys, SSH keys, certificates, remembered-device and multi-factor registrations revoked. Where a single token cannot be revoked, the signing secret is rotated or the scope is signed out | Emergency change record; prior state saved | A replayed token and a logon with the old credential both fail |
| 4 | Identity admins, network operations | Account disabled, not deleted. All other accounts of this vendor disabled across all bank systems pending review. Vendor remote path blocked at the perimeter | Information owner approves, or endorses afterwards | Access attempt alerts in place |
| 5 | Platform owners, IT Operations | Rotation of service passwords, keys and shared administrator secrets readable from the session, in a planned order with rollback | Dependency check against services still running | Each dependent service retested after rotation |
| 6 | Forensic staff | Removal of persistence created in the session: new accounts, added keys, scheduled tasks, multi-factor enrolments, access grants, rule changes | Each item recorded as evidence first | Re-scan clean |
| 7 | Vendor, on SEC instruction via the C02 channel | Vendor preserves first, then ends its own sessions to the bank, rotates its bank-related credentials and quarantines the workstation concerned | Preservation confirmed | Written confirmation |

Stop triggers
- Any successful use of the identity or its tokens after Step 3: treat as active intrusion, block at network level, tell the incident commander at once, and restart Step 1.
- A rotation breaks a working service (mobile balance viewing, branches): fix forward with the new secret; the old secret is not restored. Service impact goes to CMT.
- Attacker sessions are not left open to protect availability or recovery work.

Reinstatement conditions for vendor access (judgment): cause of the credential compromise known; individual named accounts; multi-factor authentication; time-limited access through the privileged access system with session recording; information owner approval; LC confirmation of contract terms. Until then, any vendor support needed for recovery is on site, supervised, on a bank-issued temporary account.

Accountable owner: SEC. Executing parties: as in the table.

Time (judgment targets): Step 1 12:00-12:10 HKT; Steps 2-4 complete by 12:20; replay and logon tests by 12:30, with the closure time reported to the incident commander and LC; rechecks at 13:30 and 16:30; rotation plan by 14:00 and rotation complete by 18:00. If a token type cannot be force-invalidated, closure is its revocation time plus its maximum lifetime, stated explicitly. Monitoring for attempted use runs for 30 days.

Destination and channel: identity, privileged access and perimeter systems, by emergency change record and the out-of-band bridge; each action entered in the incident log. The vendor is instructed through the verified contact used in C02.

Basis
- R10, Cap. 486, Schedule 1, Principle 4(1), PDF p.169: personal data held by a data user is to be "protected against unauthorized or accidental access, processing, erasure, loss or use". Binding statute. It applies because the workspace holds records of up to 18,000 customers and a session with access may still be live.
- R03 s.6.2.13(b), PDF p.14: "a Designated AI should ensure that all passwords are promptly changed if they have been or are suspected of being compromised". Sectoral code under Cap. 653 s.8; applies to credentials of the designated gateway. It names passwords only; extending it to sessions, tokens and keys is my judgment.
- R03 s.6.2.11(a), PDF p.14, refers to SPM TM-G-1 s.3.2.3. R08 s.3.2.3, PDF pp.12-13: "Extra care should be exercised when controlling the use of and access to privileged and emergency IDs", including "change of privileged and emergency IDs' passwords immediately upon return by the requesters". Whether the vendor credential was privileged is not stated; I treat it as such because it reached the gateway.
- R02 s.6.2.10(e), PDF p.14: "All user privileges and data access rights should be revoked when no longer required." and s.6.2.18(b), PDF p.17: "revoking authority and access rights when they are no longer needed". Generic-code text used as principle; R03 s.6.2.10 and s.6.2.18 point to C-RAF, which is not in my manifest.
- R11, PDF p.5, Step 2: "Changing users' passwords and system configurations to block any (further) unauthorised access". R16a, PCPD form annex, PDF p.4: "Change login details for the compromised device / software / database / system". Non-binding PCPD material; applies now that a breach is confirmed.
- R16b Annex C(vii), PDF p.5: remote access by service providers "should be subject to robust authentication (e.g. two-factor authentication)". Supports the reinstatement conditions.
- R08 s.4.3.2-4.3.3, PDF pp.19-20 (quoted in C01): emergency changes approved, logged and backed up. Governs Steps 2-6.
- R02 Annex F item D(1), PDF p.45: "Compromised accounts have been removed or isolated". The action and its time are reportable.

No direct rule located in assigned sources for terminating sessions, revoking tokens or keys, replay testing, rotation order, closure timing or reinstatement conditions. Files: all. Terms: "session" (relevant hits only R02 pp.17 and 19, and R09 pp.14 and 20 on customer e-banking sessions); "token" (R08 p.12; R09 pp.16 and 18, customer authentication tokens); regex "revok|revoc|credential" (R02 pp.14, 17, 22; R16b p.4). These are professional judgment: disabling an account does not by itself end sessions or tokens already issued, so closure has to be tested.

---

Facts SEC passes to the incident team (12:30 statement, then at each version or trigger)

| Fact | Status at 12:00 | Used by |
|---|---|---|
| 80 customers' names, identity card numbers and telephone numbers exported | Confirmed | LC (Q08), COM (Q09) |
| Up to 18,000 customers' records in the same workspace | Confirmed present; export unverified; cannot be excluded | LC, COM |
| Fields held for the wider set | Unknown until inventory, 15:00 | LC |
| Data outside the workspace reached | Unknown | LC |
| Vendor support credential used in the relevant session | Confirmed | LC |
| How the credential was obtained; any vendor staff involvement | Unknown; no inference drawn | LC, COM |
| Access window closed | Not confirmed; closure time due 12:30 | LC, CMT |
| Events that would enlarge the affected group | The "up" rows in the Q07a table | LC (Q08b) |
| Mobile transfer submission | Still interrupted; the credential work does not restore it; SEC gives no restoration time | COM, CMT |

Caution for wording, as a fact constraint only: SEC evidence supports "80 confirmed so far". It does not support "only 80" or "no other data affected".

Limitations: text search and page reads only. Not available to me: C-RAF, the HKMA third-party circular of 21 December 2023 cited by R03, the vendor contract, and the bank's own plans.