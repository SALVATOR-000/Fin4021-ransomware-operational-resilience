CEO final decision record for C01 (Mon 16 Nov 2026, 08:00 HKT, H+0). All six units are CONFIRM; there are no overrides. Every action below is simulated, for the facilitator to log.

Assumption for the facilitator to confirm: I declare severity 1 at 08:00 HKT (PH01 v1.0 s.4.1, "a critical operation is disrupted"). All internal timers run from 08:00. As CMT chair I convene the CMT by 08:30 (PH01 s.2.1, "within 30 minutes").

Cross-check of sources (I read these myself):
- PH01 v1.0, ss.2–18
- R01 Sch.6, PDF p.97
- R02 ss.7.3.2–7.3.6, PDF pp.35–36
- R05 PDF p.2, checked against the scan: "should notify the HKMA immediately and provide it with whatever information is available at the time"
- All other citations are taken unchanged from the sealed answers.

Conflicts across the three answers: none that change any action. Two points to note:
- Corrected wording in the SEC answer (no change to execution): see Q01a.
- Each answer depends on another: SEC's status logs feed LC's channel choice and COM's channel choice. These are sequenced at the end.

---
**Q01a | Original: SEC sealed answer, Q01a | CONFIRM**
- **Reason:** It follows PH01 s.7.1 (isolate the segment and the route at the network layer, no power-off, keep working services running) and the R05 p.1 duty to contain. It respects the 10-minute cap in PH01 s.6.2/7.3. It keeps balance view and branches running. It holds failover behind a security condition whose default is hold, as PH01 s.2.3 requires.
- **Correction to wording only (execution unchanged):** SEC describes 12:00 HKT as "50% of the 24h tolerance". That is wrong. 50% of 24 hours from 08:00 is 20:00 (PH01 s.4.2/4.3). 12:00 is kept as SEC's chosen latest time to verify failover cleanliness. The default stays hold, and 20:00 stays the 50% point for telling the Board chair.
- **Final action:**
  - Spread triage 08:00–08:10.
  - Then quarantine the gateway segment at the network layer. Block the entry route; until that route is known, suspend all privileged and vendor remote sessions into the segment. Disable the accounts used, after a capture of no more than 10 minutes. Hosts stay on.
  - Block only the flows to and from the gateway. Front ends reject or queue new transfer submissions and show a service message.
  - Precondition: IT Operations confirms the out-of-band console route before quarantine. After quarantine, run reachability and health tests.
  - Widen isolation only on evidence of active spread. If a working customer service would be removed, consult me first.
  - Failover and alternate processing stay on HOLD:
    - SEC verifies cleanliness; latest time 12:00; default is hold; SEC logs a close-out entry.
    - Activation needs SEC's written clearance and then my decision (PH01 s.3, s.8.2). That activation is a BCP activation (s.4.4).
- **Owner:** SEC. Executed by Network/Firewall Operations and IT Operations. Consult the Head of IT Operations, and me if a working customer service would be removed.
- **Time:** triage ends 08:10. Isolation target 08:10–08:15. SEC reports to me hourly from 09:00 (PH01 s.2.5). Failover checkpoint 12:00. 50% of tolerance at 20:00.
- **Recipient and channel:** emergency change record; decision log; verbal briefing in the CMT room.
- **External basis:** as in SEC Q01a "Basis – External" (R05 p.1 "Immediate incident response"; R09 s.8.2.1 p.32; R02 s.7.2.3(a)(v)(1) p.32). Confirmed as adequate.
- **Internal basis (internal bank procedure):** PH01 v1.0 s.7.1 "Hosts are not powered off. Services still working are kept running unless SEC finds active spread to them"; s.3 isolation row; s.2.3 ("security ... conditions ... the default is to hold ... never to go ahead"); s.8.2. No conflict with the external sources.
- **Dispatch:** EXECUTE NOW. Quarantine depends on the out-of-band route being confirmed. Failover and alternate processing: HOLD pending SEC's written clearance and my activation.

**Q01b | Original: SEC sealed answer, Q01b | CONFIRM**
- **Reason:** It applies PH01 ss.6.1–6.4 and 6.6–6.7 and Annex B. Volatile capture is capped and comes after containment if the attack is spreading (consistent with R02 s.7.2.3(f)). The custodian is independent of the gateway. Supplier preservation requests are drafted within 1 hour. The terminal and email statuses are logged within 30 minutes (s.5.6, 5.7).
- **Final action:**
  - Evidence hold at 08:00 on the gateway and its support systems.
  - Volatile capture (no more than 10 minutes) only if nothing is spreading. Then disk images and log exports.
  - Stop log rotation and backup recycling. Keep immutable backups unmounted.
  - Snapshot of in-flight and queued instructions sent to Payments.
  - Custody record with all Annex B fields, kept by an SEC designate who does not administer the gateway.
  - Supplier preservation and production requests drafted by 09:00 (LC clears the wording; the vendor relationship owner sends them with call-back confirmation). Escalate to LC and me if not confirmed within 4 hours.
  - Retained forensic firm engaged now (PH01 s.6.5). Data sharing under s.16 is decided jointly by LC and SEC.
  - By 08:30, SEC logs (1) whether the filing terminal can be released and (2) whether corporate email is safe. Neither log delays any report.
- **Owner:** SEC. Executed by the evidence custodian and SEC analysts. LC owns the legal hold.
- **Time:** hold 08:00; volatile capture by 08:10; terminal and email logs by 08:30; supplier drafts by 09:00; supplier escalation by 12:00.
- **Recipient and channel:** evidence register; decision log; change record. Supplier records come in only through bank-hosted encrypted transfer or bank-issued encrypted media.
- **External basis:** as in SEC Q01b "Basis – External" (R02 s.7.2.3(a)(v)(2), (f), (h), pp.32–33; R03 s.6.2.23(c) p.18, where whether current log retention meets the rule is still a missing fact; R01 s.36(2)(b) p.52 as context only). Confirmed.
- **Internal basis (internal bank procedure):** PH01 v1.0 s.6.1 "No reboot, rebuild, restore, failover or deletion on a held system without SEC's logged release for that item"; s.6.7(a) "Within one hour of declaration SEC drafts..."; s.17.1. No conflict with the external sources.
- **Dispatch:** EXECUTE NOW. Supplier requests: SCHEDULE for 09:00, after the vendor list is matched against the CRO's third-party register and LC has cleared the wording.
- **Added instruction (does not change execution):** LC issues the written legal hold at declaration (PH01 s.17.1, "LC issues a written legal hold at declaration"). This was missing from the LC answer.

**Q02a | Original: LC sealed answer, Q02a | CONFIRM**
- **Reason:** R05 p.2 (verified on the scan) requires the HKMA to be notified "immediately" with "whatever information is available at the time", and the bank must not wait for rectification. A telephone call targeted for 08:30, from the printed contact register, with unverified items marked, meets that. It is never held by internal review (PH01 s.2.4). Written follow-up goes by a non-email route. Updates are every 4 hours plus on the listed events (s.5.8). It is conditional on BCP activation under R07 s.1.3.3.
- **Final action:** telephone the HKMA supervisory contact with the information set listed in LC Q02a. Written confirmation target 10:00, by a route the HKMA confirms on the call. Updates at 12:00, 16:00, 20:00, 24:00 and 04:00, then 08:00 and 18:00 daily. Update at once on: BCP activation, data exposure, an extortion demand, a change in service status, or the public statement (COM's 09:00 release is such a trigger).
- **Owner:** LC. Executed by the LC duty officer. SEC supplies the facts.
- **Time:** call by 08:30; written confirmation by 10:00.
- **Recipient and channel:** HKMA supervisory team; telephone, then a written route the HKMA accepts (not corporate email until SEC logs it safe).
- **External basis:** as in LC Q02a (R05 p.2 "Reporting incident to the HKMA"; R09 s.8.2.5 p.33; R07 s.1.3.3 p.5). Confirmed.
- **Internal basis (internal bank procedure):** PH01 v1.0 ss.5.1, 2.4, 5.7, 5.8, as quoted in LC Q02a. No conflict with the external sources.
- **Dispatch:** EXECUTE NOW. No dependency. Copy of the public statement to the HKMA at release (see Q03b).

**Q02b | Original: LC sealed answer, Q02b | CONFIRM**
- **Reason:**
  - The R01 s.2 incident definition and the R02 s.7.3.2 "actual adverse effect" test are met. The example in R02 s.7.3.3(b) fits: "Ransomware attack that causes suspension of an essential service".
  - The core function is disrupted, so the 12-hour limit applies. R01 Sch.6 item 1(a), p.97 (I verified it): "12 hours after the CI operator concerned becomes aware".
  - Awareness is 08:00, on confirmation, which meets the R02 s.7.3.5 "reasonable degree of certainty" test.
  - The telephone-first route is permitted. R02 s.7.3.6(b), p.36 (verified): "may first make the notification to a designated telephone number ... then submit a specified form ... within 48 hours of the notification".
  - The statutory standard is "as soon as practicable" (s.28(2)). LC's call target is 09:00. As CEO I direct the call to be made as soon as the HKMA call is finished, and to be made in parallel if a second LC officer is available. This is a target within the branch LC stated, not a change.
- **Final action:** telephone notification to the Commissioner giving the nature of the incident, the critical computer system (CCS) involved and a short summary. Ask for a reference number on the call. Log the call under PH01 s.5.5. Then:
  - Written record in Annex E or sector form within 48 hours of the logged call time.
  - Written report within 14 days.
  - Filing route: the standby device, if logged as working and enrolled; otherwise the released terminal; otherwise the alternative the Commissioner names on the call.
- **Owner:** LC. Executed by the LC duty officer. A second LC officer checks the deadline tracker within 30 minutes (s.5.3).
- **Time:** awareness 08:00 Mon 16 Nov. Statutory latest for the call: 20:00 HKT Mon 16 Nov. Call target 09:00 or earlier. Written record: call time plus 48 hours (09:00 Wed 18 Nov if the call is at 09:00). Report by Mon 30 Nov 2026 (16 Nov plus 14 days; LC second check). Internal target 27 Nov.
- **Recipient and channel:** the Commissioner of Critical Infrastructure (Computer-system Security); the verified telephone route; then the designated secure channel.
- **External basis:** as in LC Q02b (R01 s.28(1)–(6) pp.43–44, s.2 pp.9–10, Sch.6 p.97; R02 ss.7.3.3–7.3.6 pp.35–36; R03 s.1.1.3 p.3). Verified and confirmed.
- **Missing fact (carried):** whether the bank's verified number is the Commissioner's "designated telephone number". The conditional action in LC Q02b stands.
- **Internal basis (internal bank procedure):** PH01 v1.0 ss.5.2, 5.3, 5.5, 5.6. No conflict with the external sources.
- **Dispatch:** EXECUTE NOW. The call depends on nothing. The 48-hour filing depends on SEC's 08:30 terminal log and Compliance's standby-device test; if neither is available, use the route the Commissioner names.

**Q03a | Original: COM sealed answer, Q03a | CONFIRM**
- **Reason:**
  - R05 p.1 and R09 s.8.2.2 require proactive notice "through the most effective means".
  - Alerts with no link, plus personal calls, follow PH01 s.10.2.
  - Priority order follows s.8.4 (never by customer size). Verified contacts and the Fraud check on changed details follow s.10.5.
  - The delivery register follows s.10.3.
  - The fee-waiver promise is permitted by s.13.1. The direct-loss wording invites a claim and does not promise payment, consistent with s.13.2 and 13.7.
- **As CMT chair I approve now:** the audience of all 180,000 retail and 12,000 SME customers as likely affected, in priority groups 1 to 3. This meets the 08:40 precondition, so the COO-alternate default is not needed.
- **Final action:** as in COM Q03a.
  - Priority 1 SME payroll calls and the SMS batch start at 08:45. All batches dispatched by 10:00.
  - App push only if SEC logs the push platform as outside the affected segment; otherwise SMS only.
  - The secure inbox and email are not used until SEC logs them trusted. Written follow-up goes by letter.
- **Owner:** CMT chair (CEO) approves the audience. LC clears the text. SEC and the Head of Payments Operations confirm each factual line. COM sends and keeps the register. RMs and the contact centre make the calls.
- **Time:** draft 08:20; approval, clearance and scripts by 08:40; first sends 08:45; all batches by 10:00.
- **Recipient and channel:** affected customers by personal call, SMS or app push with no link, IVR, branch notices, and letter.
- **External and internal basis:** as in COM Q03a "Basis (external)" and "Basis (internal)" (PH01 v1.0 ss.10.1–10.3, 13.1–13.2, 3). Confirmed. No conflict.
- **Dispatch:** EXECUTE NOW for the approval. SCHEDULE sends for 08:45, after LC clearance and the SEC and Operations fact-check. The push channel depends on SEC's log.

**Q03b | Original: COM sealed answer, Q03b | CONFIRM**
- **Reason:**
  - The R05 p.2 "Public announcement" circumstances (a) and (b) are both present (verified on the scan): an essential and critical banking channel is disrupted, and a large number of customers are affected.
  - R09 s.8.2.3 expects a press release "shortly after" the disruption when there is no reasonable confidence of near-term restoration. Failover is unverified.
  - Content limits (PH01 s.11.3) address R05's caution about prejudicing an investigation.
  - The copy to the HKMA follows R05 p.3.
- **As CMT chair I will approve by 08:50.**
- **Final action:** as in COM Q03b.
  - Holding statement released by 09:00: website (if SEC logs it clean by 08:50; otherwise press release, branch notices and IVR, with the web notice added later) and social media with links only to the bank homepage.
  - "Next update by 12:00", then at least every 6 hours from 07:00 to 22:00, and at once on any change in service status.
  - I am the only spokesperson.
  - LC sends a copy to the HKMA at release, which counts as an HKMA update trigger.
- **Owner:** CMT chair approves (COO as alternate after 15 minutes). LC clears. SEC and Operations fact-check. COM releases.
- **Time:** approval 08:50; release 09:00; next update 12:00.
- **Recipient and channel:** the public and media; website, press release by a non-email route, branch posters, IVR, social media; copy to the HKMA.
- **External and internal basis:** as in COM Q03b (R05 pp.2–3; R09 s.8.2.3 p.33; R07 ss.4.7.1–4.7.2; PH01 v1.0 ss.3, 11.1–11.4, 5.1). Confirmed. No conflict.
- **Dispatch:** SCHEDULE release for 09:00, after LC clearance and the fact-check. The website channel depends on SEC's 08:50 log. Not held for the LC reports.

---
**Added CEO instructions** (outside the scored units; they do not change any unit):
- SEC logs by 08:45 whether the website, content system, push platform and secure inbox are trusted.
- I tell the Board chair of the severity 1 declaration by 10:00 (PH01 s.15.1, "within two hours of ... severity 1 declaration"), and again at 20:00 (50% of tolerance).
- The CFO notifies the cyber insurer by 08:00 on 17 Nov (s.12.4).
- LC decides on a Police report (s.3) and tells me.

**Order of actions that depend on each other:**
1. 08:00: severity 1 declared; evidence hold; LC legal hold; LC opens the deadline tracker; Compliance tests the standby filing device.
2. 08:00–08:10: SEC spread triage and capped volatile capture.
3. About 08:10–08:15: network quarantine, after the out-of-band console route is confirmed. Then the health check of balance view and branches.
4. By 08:30: HKMA call (Q02a); CMT convened; SEC logs terminal and email status.
5. Right after the HKMA call, target 09:00 at the latest: Commissioner phone notification (Q02b). The statutory latest is 20:00.
6. 08:40: customer text cleared; 08:45: customer alerts start (Q03a).
7. 08:50: public statement approved, with SEC's website log; 09:00: release; LC copies it to the HKMA (Q03b).
8. 09:00: supplier preservation requests; first SEC status report.
9. 10:00: written HKMA confirmation; Board chair told.
10. 12:00: failover clearance checkpoint (default hold); HKMA update; public update.
11. 48-hour Cap. 653 written record, running from the logged call time.
12. Any alternate processing only after SEC's written clearance, then my activation, then LC's immediate BCP report to the HKMA.