SEC (Information Security Lead), locked response for C01, Monday 16 Nov 2026, 08:00 HKT (H+0). This answers only Q01a and Q01b. No handoff was received for SEC.

Facts I take as confirmed from the card: unauthorised commands encrypted payment gateway components. Outbound domestic transfers and payroll submission are down. Mobile balance view still works and branches are open.

Facts I treat as unverified: whether the attack is still spreading, how the attacker got in (route, credential, vendor path), whether failover works or is clean, whether the filing terminal is part of the affected estate, whether any data was taken, and whether corporate email is safe.

All actions below are simulated, for the facilitator to log. I assume severity 1 was declared at 08:00 (PH01 4.1: "a critical operation is disrupted"). The facilitator should confirm the declaration time, because every internal timer below runs from it.

== Q01a: What I isolate first and how available services are protected ==

Decision and action:
1. **08:00–08:10: confirm whether the attack is spreading.** I run a triage of no more than 10 minutes using EDR/SIEM telemetry: are new encryption events, new command executions or new hosts touched outside the gateway segment?
   - If anything is still spreading, I do not wait for the 10 minutes or for evidence capture. Containment goes first.
   - If nothing is spreading, volatile capture (Q01b) runs inside the same 10-minute cap.
2. **By about 08:10: isolate at the network layer.**
   - **Who executes:** Network/firewall operations, on my instruction, under an emergency change record.
   - **What changes:**
     - The payment-gateway segment is put into quarantine: block all inbound and outbound traffic except a single forensic/management VLAN reachable only from the incident response jump host.
     - The route the attacker used is blocked: the admin, jump, remote-access or vendor path into that segment. Which path it was is unverified. Until it is identified, I suspend all privileged and vendor remote sessions into the gateway segment through the privileged access system.
     - Gateway service and admin accounts known to be used in the unauthorised commands are disabled and their sessions and tokens revoked, after a session/token state capture of no more than 10 minutes.
   - **What does not change:** hosts are not powered off, rebooted, restored or failed over. Encrypted hosts stay powered on in quarantine.
3. **Services kept running:**
   - Mobile balance view, branch systems, the core ledger, card authorisation and the channels leading into the gateway stay up.
   - At the boundary of those systems, I block only the specific flows to and from the quarantined gateway segment. Flows that are needed and inspected stay open.
   - The incoming customer channel will fail because the gateway is down. The front end should reject or queue new submissions with a service message, not let them silently sit "in flight". That needs Payments Operations and COM coordination.
4. **Stop and widen triggers:**
   - Widen isolation to a working service only if I find active spread to it, such as encryption, attacker commands or lateral logons. If that would remove a working customer service, I first consult the Head of IT Operations and the CMT chair and log it.
   - Precondition before quarantine is applied: IT Operations confirms the console or out-of-band management route, so we do not lock ourselves out.
   - Validation after quarantine: run reachability tests from both sides of the boundary, and check that mobile balance view and branch systems are healthy. Log the results and the time.
5. **Failover is on hold.** No failover or standby activation until:
   - Failover is shown not to share hosts, accounts, keys or a network path with the affected systems, and
   - The evidence hold for the gateway is released.
   This hold is a security condition. The default if it is not cleared is to hold or use an approved alternate process. The default is never to go ahead. Alternate payment processing needs my written clearance before the CMT chair can activate it.
   Condition per PH01 2.3: I verify it; the latest time is 12:00 HKT, which is 50% of the 24h tolerance; the default is hold; I log a close-out when verified.

Owner: SEC decides. Network/firewall operations and IT Operations execute. I must consult the Head of IT Operations. I must also consult the CMT chair only if a working customer service would be removed.

Timing:
- Spread triage ends 08:10.
- Isolation is in place as soon as possible, target 08:10–08:15.
- First SEC status report to the CMT chair at 09:00, then hourly until containment is confirmed.
- The transfer/payroll tolerance (24h, PH01 4.2) runs out at 08:00 on 17 Nov. 50% is reached at 20:00 on 16 Nov, when the chair tells the Board chair.

Recipient and channel:
- Firewall/network change through the emergency change record.
- Decision log entry (PH01 Annex A fields).
- Verbal briefing to the CMT chair and Head of IT Operations in the CMT room.

Basis:
- **External:**
  - R05, HKMA circular "Incident response and management procedures", 22 Jun 2010, PDF p.1, heading "Immediate incident response". Quote checked against the scan: "The AI concerned should immediately analyse the cause of the incident and as soon as practicable rectify or contain the problem. The top priority should be to safeguard the interests of customers who have been or may be affected by the incident."
    - Authority: HKMA supervisory circular to all AIs.
    - Why it applies: this is a significant incident that disrupts a critical payment service.
    - Left to judgment: how containment is done.
    - Application: contain fast, but keep balance view and branches running because that protects customers.
  - R09, SPM TM-E-1 V.4, PDF p.32, s.8.2.1: "The top priority should be to protect the interests of customers who have been or may be affected by the incident." It applies because mobile/e-banking transfer submission is affected.
  - R02, OCCICS Code of Practice (Generic) v1.0, PDF p.32, s.7.2.3(a)(v)(1). Playbooks must cover "Containing the incident to prevent further harm". This sits under Division 3 obligations (emergency response plan), which apply to a designated CI operator.
    - Authority: Code issued under Cap. 653 s.8. It is not subsidiary legislation, but the Commissioner may issue directions with reference to it (s.1.1.4, PDF p.4).
    - Left to judgment: technical method and sequencing.
- **Internal bank procedure:** PH01 v1.0 (effective 1 Oct 2026).
  - s.7.1 "Isolation order": "SEC isolates at the network layer first: the affected segment and the route used. Hosts are not powered off. Services still working are kept running unless SEC finds active spread to them."
  - s.3, Authority matrix, row "Isolate a system or segment": SEC decides; consult the Head of IT Operations, and the CMT chair if a working customer service will be removed.
  - s.7.3 covers session/token capture of 10 minutes at most before termination.
  - s.8.2 covers SEC's written clearance for alternate processing.
- **Conflict check:** none found. PH01 is consistent with R05, R09 and R02.
- **Professional judgment:** I isolate at the network layer rather than shutting hosts down because that keeps volatile memory and encryption keys that may be in memory. Blocking the gateway at the boundary, rather than shutting down channels, keeps the services that are currently working (balance view, branches) available.

== Q01b: Evidence secured before systems change, and custody ==

Decision and action:
1. **08:00: evidence hold.** I place an evidence hold on the payment gateway hosts and their supporting systems, including directory/admin hosts used in the commands and the jump/PAM path once identified. The hold blocks reboot, rebuild, restore, failover and deletion without my logged release for each item. IT Operations and Payments Operations are told at once.
2. **08:00–08:10: before containment changes anything, capped at 10 minutes, and only if nothing is spreading:**
   - Memory images of one or two representative encrypted gateway hosts.
   - Running processes and network connections.
   - Active sessions and token state for the accounts used.
   - Firewall/PAM session snapshots.
   If anything is spreading, containment goes first and I take these from the isolated hosts afterwards.
3. **After isolation:**
   - Disk images of the affected hosts.
   - Exports of gateway, OS, directory, PAM/session-recording, firewall, EDR and SIEM logs.
   - Copies of the ransom note and encrypted samples. These are handled only inside the evidence process: no outside uploads and no visits to attacker links.
   - Gateway transaction and queue state at failure, for Payments Operations to reconcile in-flight items.
   - Change records.
   - Clock offset readings against the bank's primary time source.
4. **Log retention:** I ask IT Operations to stop log rotation and backup recycling for in-scope systems now. LC issues the written legal hold. The immutable backups are protected: they are not mounted on any affected network.
5. **Suppliers:** I draft written preservation and production requests for any supplier that supports, hosts or has remote access to the gateway by 09:00. LC clears the wording. The vendor relationship owner sends them. Which suppliers are in scope is unknown until the vendor list is checked against the third-party register.
6. **Retained forensic firm:** I engage it at severity 1. Sharing incident data with it is decided jointly by LC and SEC.

Custody:
- **Custodian:** an SEC designate who does not administer the gateway.
- **Fields recorded for each item (PH01 Annex B):**
  - evidence ID, description and source system;
  - HKT acquisition time and clock offset;
  - collector, witness, and tool with version;
  - SHA-256 hash and storage location (offline, encrypted, access-controlled);
  - every transfer (from, to, time, purpose, signatures) and every access.
- **Analysis:** only on verified hash copies.
- **Scope rule:** production artefacts stay held. Analysis copies are offline only. Nothing goes back to production.

Dependency (time-critical): the secure filing terminal is unavailable.
- By 08:30 HKT I will log whether it is within the affected estate or under evidence hold, and whether it can be released.
  - If it is not affected, I release it to LC.
  - If it is affected, I hold it, image it later, and say so. LC then uses the Compliance standby device, if logged as working and enrolled, or another permitted route.
- By 08:30 I will also log whether corporate email is safe. Until then I treat it as not safe.
- Neither check delays any external report. LC's verified telephone route is unaffected.

Owner: SEC. The evidence custodian and SEC forensic analysts execute, with the retained forensic firm assisting. LC owns the legal hold and clearance of supplier requests.

Timing:
- Hold at 08:00.
- Volatile capture by 08:10, capped.
- Filing terminal and email logs by 08:30.
- Supplier preservation requests drafted by 09:00, escalated if not confirmed within 4 hours.
- First evidence register summary in the 09:00 status report.

Recipient and channel:
- Evidence register.
- Decision log.
- Emergency change record.
- Supplier requests sent in writing to the contract contact, with call-back confirmation. Records are received only through bank-hosted encrypted transfer or bank-issued encrypted media, never by email.

Basis:
- **External:**
  - R02, s.7.2.3(a)(v)(2), PDF p.32. Playbooks must cover "Digital evidence handling, including identification, collection, acquisition, preservation of evidence and chain of custody".
  - R02, s.7.2.3(f), PDF p.33: "When balancing the need for timely system recovery and digital evidence handling, the CI operator should prioritize incidents which had impacted business operations, require swift damage containment or need immediate system recovery. Otherwise, more time should be allocated to evidence collection."
    - Application: business operations are affected, so the time spent on evidence before containment is kept short. How long is left to judgment; PH01 sets 10 minutes.
  - R02, s.7.2.3(h), PDF p.33: engage "capable incident response and forensic examination personnel".
  - R03, HKMA Sectoral Code for Designated AIs, PDF p.18, s.6.2.23(c): logs "should be retained for a minimum period of 6 months. Such logs should be secured so that they cannot be deleted or altered". This applies because the gateway is a designated critical computer system (CCS). Missing fact: whether current retention and immutability meet this. To be confirmed.
  - R01, Cap. 653, s.36(2)(b), PDF p.52. The Commissioner may by written notice require the operator "to preserve the state of the system". This is context only and not triggered at C01. Keeping held systems in their current state makes it easy to comply with any such notice.
- **Internal bank procedure:** PH01 v1.0.
  - s.6.1 "Evidence hold": "No reboot, rebuild, restore, failover or deletion on a held system without SEC's logged release for that item."
  - s.6.2: "Collection of volatile evidence before containment is capped at 10 minutes."
  - s.6.3 "Custody": "The evidence custodian is an SEC designate who does not administer the affected systems."
  - Also: s.6.4 (clocks), s.6.6 (attacker material), s.6.7 (supplier preservation requests within one hour), s.5.6 and 5.7 (30-minute terminal and email logs), s.17.1 (LC legal hold), Annex B.
- **Conflict check:** none found. PH01 s.6.2 matches R02 s.7.2.3(f).

== Facts I pass to the incident team (CMT/LC/COM) at the 08:15 briefing and 09:00 report ==
1. **For LC:**
   - Confirmed and unverified items for the HKMA and Cap. 653 reports: gateway encrypted by unauthorised commands; core function (domestic transfers and payroll) disrupted from about 08:00 or earlier. The exact detection time comes from the SIEM timeline.
   - Containment checkbox status for the Cap. 653 forms (R02 Annex, PDF p.45: segments isolated, accounts removed, IPs blocked).
   - Filing terminal and email status by 08:30.
2. **For COM and Payments:**
   - Balance view and branches are working and are being kept running.
   - The transfer/payroll restoration time is unknown.
   - Failover is unverified and on hold.
   - New transfer submissions should be refused or queued visibly, not accepted silently.
3. **For the DPO/LC:** there is no evidence yet of data access or exfiltration. This is unverified. Exfiltration analysis is running, and any indicator will be escalated at once.
4. **For Payments:** the snapshot of in-flight and queued instructions has been preserved. Items in flight stay "status unknown" until independent records show their status.
5. **Open dependencies:**
   - Attacker entry route and credential (drives vendor lockout).
   - Supplier list for preservation requests.
   - Clean status of failover and the immutable backup.
   - 12:00 security-clearance checkpoint for alternate processing.