SEC (Information Security Lead): locked response for C01, Monday 16 Nov 2026, H+0 (08:00 HKT)

Assigned units: Q01a and Q01b only.

Working assumptions (please log them):
- The PH01 Severity 1 criteria are met at 08:00, because "a critical operation is disrupted" (PH01 4.1). PH01 does not say who declares severity. SEC asks the CMT chair to log the declaration at 08:00. Every "from declaration" time below assumes 08:00; if the actual time differs, shift them by the same amount.
- No conflict was found between PH01 and any applicable external requirement for these units. One related point (the evidence hold on failover) is handled in Q01a below.

Facts not known at this card:
- The route or account used to issue the unauthorised commands.
- Whether encryption is still spreading.
- Whether any service that still works (balance view, branch functions, card authorisation, inbound credits) routes through the gateway segment.
- Whether the standby/failover shares hosts, accounts, keys, network paths or replication with the gateway. Failover capability is unverified.
- Whether any supplier supports, hosts or has remote access to the gateway.
- Why the filing terminal is unavailable.
- Whether any data was taken out.
- Whether there is an extortion demand. None is on the card.
- Card authorisation status.
- Whether PH01 is, or forms part of, the emergency response plan submitted under Cap. 653 s.27.

---------------------------------------------------------------
UNIT Q01a: What to isolate first, without disabling available services

DECISION AND ACTION (simulated, for the log)

A1, 08:00. SEC logs the isolation decision in the master decision log and opens an emergency change record (PH01 s.3).
- SEC consults the Head of IT Operations in person in the CMT room, or by phone.
- No working customer service is to be removed, so the CMT chair is informed but not asked for consent.

A2, 08:00 to 08:10. Pre-change capture, limited to 10 minutes. The evidence items (E1, E3, E2) are listed under Q01b.
- Override: if encryption or unauthorised commands are still spreading (new encrypted files, endpoint detection alerts, new command activity), skip this capture and isolate at once (PH01 6.2).

A3, isolation complete by 08:10, latest 08:15. Network-layer isolation of the payment gateway segment only. Hosts stay powered on. What is changed:
- (i) The segment-boundary firewalls get deny-all rules for traffic in and out. The one exception is a single forensic collection path controlled by SEC: one jump host, with fresh credentials not issued from the possibly affected directory, and every use witnessed.
- (ii) The gateway's links to external payment networks and clearing interfaces are blocked. Outbound service is already down, so no working service is lost. This stops any attacker-originated payment messages.
- (iii) Every administrative or management path into the gateway is blocked: jump hosts, privileged-access routes, and any vendor or remote-access route. The actual route used is unknown, so all of them are treated as "the route used" (PH01 7.1).
- (iv) Replication and synchronisation from the gateway to the standby/failover environment and to the alternate payment environment are cut.
- (v) Backup jobs that write from the gateway into the backup repositories are paused, and backup recycling is suspended (together with LC's legal hold, PH01 17.1).

A4, credentials. PH01 7.3 is triggered because unauthorised commands make a compromised credential a reasonable suspicion.
- For each account seen issuing commands on the gateway: capture its session and token state (10 minutes at most), then terminate sessions, revoke tokens and keys, and disable the account.
- If a vendor account is implicated: disable every account of that vendor, block its remote path at the perimeter, and issue a preservation request under PH01 6.7.
- Log the closure test (PH01 7.4). Until a replayed token and a logon with the old credential both fail, treat the access window as open.
- Judgment: suspend use of the gateway's payment-messaging credentials and certificates, but do not destroy them. Coordinate this with Payments Ops.
- Judgment: no directory-wide password reset at H+0. It could break service accounts that mobile and branch systems depend on. If evidence of directory compromise appears, take it to the chair as a decision that removes working services.

A5, keep running:
- Mobile balance view, branches, card authorisation (status unverified) and all segments not affected.
- Before cutting, use the dependency map (the OR-2 5.1 mapping documentation) to find any flow a working service needs through the gateway segment.
- Any such flow stays open only on the exact source, destination and port it needs, and is monitored.
- If a working service would lose a flow, consult the CMT chair before cutting it. The exception is active spread: then cut first and phone the chair at the same moment.
- Recommendation for the Payments Ops head and CMT chair to decide (judgment): consider pausing mobile transfer submission at the application layer while balance view stays on. This prevents new instructions queuing into "status unknown".

A6, validation after each change, 08:15 to 08:30. Record results in the emergency change record.
- Firewall and traffic-flow logs show no traffic crossing the boundary except the forensic path.
- Endpoint detection shows no new encryption events outside the segment.
- Synthetic checks pass for mobile login and balance view, a branch teller enquiry, and a card authorisation test.
- Stop triggers:
  - A working service fails its health check: revert that specific rule (unless it blocks active spread) and phone the chair.
  - Indicators appear outside the segment: widen isolation to that segment (containment first) and phone the chair at once.
  - Any payment message is seen leaving after isolation: escalate at once to the Payments Ops head and the chair.

A7, failover HOLD. No failover to the standby (PH01 6.1). Logged in the four-item condition format (PH01 2.3):
- Verifier: SEC.
- Latest time: 12:00 HKT (judgment; four hours, well inside the 24-hour tolerance).
- Condition: a standby snapshot is taken, and the standby is confirmed to share no hosts, accounts, keys, network path or replicated compromised state with the gateway.
- Default if not verified: hold, or switch to an approved alternate process. Never go ahead.
- Close-out: an entry is logged when verified or when the default is applied.
- Any failover is a BCP activation that the chair declares, and LC is told (PH01 4.4).

A8, 08:30 (30 minutes after declaration). SEC logs two items:
- (a) Whether the normal filing terminal can be released (PH01 5.6). Judgment: not released if it sits on the affected segment or uses affected credentials. LC then uses the verified telephone route or the standby device as PH01 5.6 allows.
- (b) Whether corporate email is safe (PH01 5.7). The default is not safe until logged otherwise.
- A8 does not hold any external report (PH01 2.4).

A9. SEC gives the chair a status report at 09:00, then hourly until containment is confirmed (PH01 2.5).

A10. Every emergency change deployed to the gateway and its network components is logged as a separate item with its deployment time, for LC's Cap. 653 s.22 assessment (PH01 18.4).

OWNER
- Accountable: SEC (PH01 s.3).
- Execution: the IT Operations network/firewall engineers and identity administrators, under emergency change on SEC's instruction.
- Consulted: Head of IT Operations, and the CMT chair if a working service is affected.

TIMES / TRIGGERS
- Isolation by 08:10 (target), latest 08:15.
- Immediately if spread is active.
- Items 08:30 (A8), 09:00 and hourly (A9), and the 12:00 standby condition (A7).
- Widening is triggered only by observed spread.

DESTINATION / CHANNEL
- Changes are made on the gateway segment-boundary firewalls and routers, the privileged-access system and identity provider, the replication links, and the backup scheduler.
- Instructions are given in person in the CMT room or on a phone bridge that does not depend on corporate email. They are recorded in the decision log and the emergency change record.

BASIS: EXTERNAL (direct rules)
1. R05, HKMA circular "Incident response and management procedures", 22 Jun 2010. PDF p1, heading "Immediate incident response". Quotation checked against the scan.
   - Quote: "The AI concerned should immediately analyse the cause of the incident and as soon as practicable rectify or contain the problem. The top priority should be to safeguard the interests of customers who have been or may be affected by the incident."
   - Authority: HKMA supervisory circular to all authorised institutions.
   - Why it applies: a disruption to transfers and payroll for 192,000 customers is a significant incident (judgment; the circular does not define the term).
   - Effect: requires containment now. Putting customers' interests first supports keeping balance view and branches running.
2. R09, SPM TM-E-1 Risk Management of E-banking, s.8.2.1, PDF p32.
   - Quote: "The top priority should be to protect the interests of customers who have been or may be affected by the incident."
   - Why it applies: it covers incidents affecting e-banking services, and mobile services are affected.
3. R02, OCCICS Code of Practice (Generic) v1.0, s.7.2.3(f), PDF p33.
   - Quote: "the CI operator should prioritize incidents which had impacted business operations, require swift damage containment or need immediate system recovery."
   - Also s.7.2.3(a)(v)(1), PDF p32: playbooks must cover "Containing the incident to prevent further harm".
   - Authority: the Commissioner's code under Cap. 653 s.8. It is not subsidiary legislation, but it is a basis for written directions (R02 1.1.4, PDF p4).
   - Why it applies: s.7 covers category 3 (incident response) obligations of all CI operators. The HKMA sectoral code covers only categories 1 and 2 (R02 1.1.3).
   - Effect: business operations are impacted, so containment comes first.
4. R01, Cap. 653, s.27(5), PDF p43.
   - Quote: "A CI operator must implement an emergency response plan."
   - Authority: statute.
   - Missing fact: whether PH01 is part of the plan submitted under s.27(1). If it is, carrying out PH01 7.1 and 6.2 is also a statutory duty.
5. R01, Cap. 653, s.22(1) and (3), PDF p33–34: a "material change" includes one that "affects— (i) the computer-system security of the critical computer system".
   - R03, HKMA Sectoral Code, s.6.1.1, PDF p11: the event date is "the moment when a change is deployed to production environments".
   - R03 s.3.1.4, PDF p7: network components "may also be regarded as components of the CCS".
   - Effect: isolation changes are logged with their deployment times. LC decides whether to notify; the limit is one month.

GENERAL PRINCIPLES (supporting)
- R06, SPM OR-2, s.1.3, PDF p3: "disruptions to an AI's critical operations must not exceed its 'tolerance for disruption'". Removing balance access needlessly would start its own 8-hour tolerance clock (PH01 4.2).
- R06, s.5.1, PDF p9: requires interdependency mapping, which is the basis for cutting flows selectively.

NO DIRECT RULE LOCATED in the assigned sources for:
- isolating selectively while keeping services that still work;
- not powering hosts off;
- the 10-minute pre-containment limit.
Files searched: PH01 and R01–R16d (all allowed). Exact terms: "isolat", "segment", "contain", "shut down", "failover", "incident response", "volatile".
R11 (PCPD Guidance, PDF p4, Step 2) lists "Shutting down or isolating the compromised/ breached system/server" only as a non-exhaustive option for a personal data breach. No breach is confirmed at C01, and R11 prefers neither option. These details are professional judgment, as stated above.

BASIS: INTERNAL (Internal bank procedure: PH01, v1.0, effective 1 Oct 2026)
- s.3, authority matrix: "Isolate a system or segment | SEC | Head of IT Operations; CMT chair if a working customer service will be removed".
- s.7.1: "SEC isolates at the network layer first: the affected segment and the route used. Hosts are not powered off. Services still working are kept running unless SEC finds active spread to them."
- s.6.2: "If destructive activity is still spreading, containment goes first".
- s.7.3 and 7.4 (credentials), s.6.1 (failover hold), s.2.3 (condition format), s.5.6 and 5.7 (30-minute logs), s.2.5 (hourly reports), s.18.4 (change register).

CONFLICT CHECK
- None found.
- One tension: the s.6.1 evidence hold on failover could delay recovery. PH01 allows release item by item, which is consistent with R05 and with R02 7.2.3(f)'s priority for recovery. So the standby is captured and assessed first (A7), with a fixed time.

---------------------------------------------------------------
UNIT Q01b: Evidence to secure before changes, and how custody is recorded

DECISION AND ACTION (simulated)

B1, 08:00. SEC places an evidence hold (PH01 6.1) on:
- the gateway components and its network devices;
- the standby/failover environment;
- the related log sources;
- the filing terminal, if it is implicated.
SEC asks LC to issue the written legal hold (PH01 17.1). SEC technically suspends log rotation and backup recycling on these systems. Logs must be kept so that they "cannot be deleted or altered" (R03 6.2.23(c)).

B2, 08:00. SEC appoints an evidence custodian: an SEC designate who does not administer the gateway. The custodian opens the evidence register with the Annex B fields plus a scope field (production or offline).

B3, 08:00 to 08:10, before any change. Only if spread is not active; otherwise these are taken right after isolation, since the hosts stay powered on. Priority order (judgment):
- E1: export of the boundary firewall and router configuration. This proves what the isolation changed and makes rollback possible.
- E3: session and token state for privileged, vendor and management accounts.
- E2: volatile state of the gateway hosts (memory, processes, network connections, logged-on users).

B4, after isolation, from about 08:15 (production scope):
- E4: native log exports.
  - Gateway application and operating-system logs.
  - Privileged-access session recordings.
  - Directory / identity-provider authentication logs.
  - Endpoint detection telemetry.
  - Firewall, proxy and traffic-flow logs.
  - Security monitoring (SIEM) extracts.
  - Job-scheduler and change records.
  - Logs of the bank's primary time source.
  These include outbound-traffic logs, which bear on whether data was taken out.
- E5: payment message queues and transaction logs, exported read-only. This preserves the in-flight instructions for the "status unknown" handling (PH01 8.6). Payments Ops must not resubmit anything from them.
- E6: disk images or hypervisor snapshots of the encrypted components.
- E7: attacker material (any notes or binaries), handled only through the evidence process and never uploaded outside (PH01 6.6).

B5, offline scope:
- O1: the catalogue and integrity metadata of the immutable backup and the secure tertiary data backup (STDB): the latest clean set IDs and times. They are recorded and protected but never mounted or restored on the affected network. Testing is later and only in an isolated environment (PH01 9.1–9.2).
- O2: snapshot and configuration of the standby, taken before any release.
- O3: verified working copies only.
Offline evidence shows the state before the incident and the recovery source. It is kept separate in the register, and it never stands in for production evidence or certifies the production state.

B6, about 08:15. SEC calls in the retained forensic firm (PH01 6.5; R02 7.2.3(h)).
- Sharing any data with the firm needs joint LC and SEC approval, with the Data Protection Officer consulted (PH01 s.3).
- The firm gets a minimised, masked set by default. Full images are examined only in the bank's laboratory (PH01 16.2).

B7, by 09:00 (conditional). If the third-party register held by the Chief Risk Officer shows any supplier that supports, hosts or has remote access to the gateway:
- SEC drafts a preservation and production request for each one (PH01 6.7(a)).
- LC clears the wording, and the vendor relationship owner sends it.
- Records are accepted only as native exports with a SHA-256 manifest (PH01 6.7(b)).

B8, custody of every item:
- The SHA-256 hash is taken at acquisition by the collector, with a witness.
- Each entry records the tool and version, and the time in HKT with the clock offset.
- Items are stored on a write-once evidence store separated from the affected directory and network.
- Each transfer and each access is logged.
- Analysis is done only on verified copies (PH01 6.3, Annex B).
- Release needs SEC and LC jointly, with the forensic lead consulted.

B9, timeline. Each entry keeps the original timestamp, the measured offset, the normalised HKT time and its uncertainty (PH01 6.4). It feeds LC the "Earliest Identifiable Time" and the "Time Becoming Aware" (R02 Annex F, PDF p44, fields B5–B6).
None of this evidence work delays any external report (R05 p2; PH01 2.4).

OWNER
- Accountable: SEC.
- Execution: the evidence custodian, SEC analysts and the forensic firm. LC issues the legal hold. The vendor relationship owner sends any supplier requests.

TIMES / TRIGGERS
- Hold and register at 08:00.
- Volatile capture 08:00–08:10, or skipped if spread is active.
- Images and log exports from about 08:15.
- Supplier request drafts by 09:00.
- Standby snapshot by 12:00.

DESTINATION / CHANNEL
- The evidence store, the evidence register, and the decision log cross-reference.
- The forensic firm is reached by phone through its contract contact under the master services agreement.
- No evidence or incident facts go by corporate email until SEC logs it as safe.

BASIS: EXTERNAL
1. R02, s.7.2.3(a)(v)(2), PDF p32. Quote: "Digital evidence handling, including identification, collection, acquisition, preservation of evidence and chain of custody".
   - Authority and scope as in Q01a item 3.
   - Left to judgment: the custody fields, hashing and timing.
2. R02, s.7.2.3(f), PDF p33: "Otherwise, more time should be allocated to evidence collection". Here containment comes first, so collection is limited in time.
   - R02, s.7.2.3(h), PDF p33: "engage capable incident response and forensic examination personnel".
3. R03, HKMA Sectoral Code for Designated AIs, s.6.2.23(c), PDF p18. Quote: "The logs should be retained for a minimum period of 6 months. Such logs should be secured so that they cannot be deleted or altered".
   - Authority: the HKMA category 2 code under Cap. 653.
   - Why it applies: the gateway is a critical computer system (CCS), so its logs are in scope.
4. General principle: R01, Cap. 653, s.36(2)(b), PDF p52. The Commissioner may require the operator "to preserve the state of the system". No notice has been received, but preserving now means the bank can comply with that, or with a production notice under s.35, PDF p50.
5. Conditional: R11, PCPD Guidance, PDF p4, Step 2: "Keeping records of the occurrence of the breach and all follow-up actions taken". This applies only if personal data exposure is found; none is confirmed now.

NO DIRECT RULE LOCATED in the assigned sources for the custody record fields (SHA-256, witness, clock offset).
Files searched: all allowed files. Terms: "chain of custody" (R02 p32 only), "hash" (PH01 only), "evidence", "forensic", "preserv", "immutable", "clock".
R02 6.2.23(g) (clock synchronisation) is only supporting: for a designated AI, the R03 sectoral code governs category 2 matters.

BASIS: INTERNAL (PH01 v1.0)
- s.6.1: "At declaration SEC places an evidence hold on affected systems."
- s.6.3: "The evidence custodian is an SEC designate who does not administer the affected systems. Every item gets an evidence ID, source, time with clock offset, collector and witness, tool, SHA-256 hash, storage location and a transfer record."
- Also s.6.2, 6.4, 6.5, 6.6, 6.7, 16.2, 17.1, s.3 (evidence release and third-party data-sharing rows), and Annex B.
- No conflict found.

---------------------------------------------------------------
FACTS SEC PASSES TO THE INCIDENT TEAM
Verbally at once, confirmed in the decision log, and in the 09:00 status report.

To LC:
- Confirmed: unauthorised commands encrypted payment gateway components (a designated CCS).
- Confirmed: outbound domestic transfers and payroll submission (a core function) are disrupted.
- Confirmed: the bank confirmed this at 08:00. LC decides the awareness point. If it is 08:00, the 12-hour limit (Cap. 653 Schedule 6 item 1(a), R01 p97) falls at 20:00.
- Containment status: isolation of the gateway segment, the time it was completed, and whether accounts have been disabled.
- Unverified: the intrusion route, the earliest identifiable time, data exfiltration, and any extortion demand.
- The filing terminal release decision and the email-safety decision (08:30).
- The log of changes deployed to the CCS, for s.22.

To Payments Ops and the CMT chair:
- In-flight instructions are "status unknown" and their queues are preserved.
- Failover is held under A7.
- Alternate processing needs SEC's written clearance (PH01 8.2), and SEC is starting the independence assessment.
- Tolerance clocks: 24 hours for transfers, with 50% at 12 hours. The start of the disruption, which may be before 08:00, is being fixed from the logs.

To COM, for fact-checking:
- Confirmed: balance view is working and branches are open; transfers and payroll are disrupted.
- No restoration time can be given.

---------------------------------------------------------------
LOG-READY ACTIONS (HKT, status)
- 08:00: Severity 1 criteria met; declaration requested from the chair (scheduled).
- 08:00: Evidence hold and register opened; custodian named; legal hold requested from LC (executed).
- 08:00–08:10: Pre-change capture of E1, E3, E2 (executed, or skipped if spread is active).
- By 08:10, latest 08:15: Gateway segment isolated (A3); credentials actioned (A4) (executed).
- 08:15: Forensic firm called in (executed).
- 08:15–08:30: Validation checks (scheduled).
- 08:30: Filing terminal and email logs (scheduled).
- 09:00: Supplier request drafts if any supplier is in scope (conditional); first status report (scheduled).
- Until 12:00: Failover held under the A7 four-item condition (held).
- Continuous: Widen isolation on observed spread (trigger).