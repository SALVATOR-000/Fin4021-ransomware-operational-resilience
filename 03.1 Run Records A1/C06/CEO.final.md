## CEO final decisions, C06 (Tuesday 17 November 2026, 20:00 HKT, H+36)

All six units are CONFIRMED; there are no overrides. I re-read the citations in the three sealed answers against the source pages and found them accurate. PH01 is not in the manifest ("PH01", all documents: 0 hits), so the internal basis is N/A throughout.

All actions below are simulated, for the facilitator to log.

### My own decisions that the sealed answers asked for

- **Recovery position: HOLD.** No staged production recovery tonight, and the recovery image is not used in production in any mode. The secondary process continues as the only service mode. Verified SME payroll that missed a cut-off goes to the front of that queue.
- **Authorisation gate:** SEC's eight conditions are adopted. I sign condition 8 only when conditions 1-7 are recorded.
- **Customer update:** COM's Version 2 (hold), approved now. The optional "next decision point" sentence is left out, because the gate review time is conditional.
- **SME confirmation letter:** approved by me. It is offered only once LC also approves, as COM's condition requires.
- **Counterparty notice:** approved, with item 1 reading "not restarted".
- **Forensic extract:** management approval recorded for the minimised, masked data set on LC's conditions. No full copy of the image leaves the bank.
- **Board:** I present tonight. My recommendations are: note the hold; approve the gate and delegate its operation to me; minute "do not pay"; approve the remediation principle and a budget; set the oversight arrangements LC lists.
- **Interim capacity:** Operations reports to the Board meeting whether more verification staff can raise throughput without weakening any check.

### Conflicts between sealed answers, resolved within their stated branches

1. **Who authorises production.** SEC's gate ends with my authorisation. LC advises that accepting recovery risk with unexplained mismatches sits with the Board. Under SEC's condition 1, production with an unexplained mismatch is not on the table. I ask the Board to approve the gate and expressly delegate it to me on those conditions, which is LC's stated alternative. Any waiver of a gate condition goes back to the Board.
2. **Customer update before the Board meets.** COM releases by 21:00; the Board meets by 22:00. The update carries only the compensation line approved at C01, so it does not pre-empt the Board's remediation decision.
3. **"Tolerance for disruption" figure.** LC needs management to state whether it has been breached. The figure is not on any card or in the sources. The Board paper states it from the bank's own framework; I cannot state it here.
4. **Counterparty promise.** COM's notice says the bank will tell each counterparty before releasing any batch with its items. The head of payment operations confirms that step is in the release procedure before the notice is sent.
5. **Counterparty confirmations and SEC's register.** COM's notice asks counterparties to confirm items. Their answers go into the instruction register, where SEC's "status unknown" items need exactly that evidence.
6. **HKMA.** Missed payroll cut-offs are one of LC's C04 triggers for an earlier update. LC's update tonight, after the Board meeting, carries the hold, the 118-of-120 result, the missed cut-offs, the counterparty requests and the Board's decisions.

---

### Q16a

- **Original answer reference:** SEC sealed answer, C06, Q16a.
- **CONFIRM.**
- **Reason:** Two unexplained mismatches in 120 fail SEC's own pass condition of no unexplained difference. The checks that would show the image is clean and separate are not recorded as passed. "No recurring encryption" covers one image for one window. A wrong or repeated payment harms customers more lastingly than further delay that the interim process partly relieves.
- **Final action and condition:** As written.
  - Hold. The only permitted mode is the secondary process under the C04 verification and duplicate controls.
  - Mismatch investigation: each item compared across the customer's original, the ledger posting, the external confirmation and the image's logs, then classified by cause.
  - Both SEC reports issue with the true status of every check, including "not recorded", and an overall result of "not passed".
  - Altered data or tampering fails this candidate.
  - Gate conditions 1-8: mismatches explained; re-run 120 of 120 with all ten checks passed; integrity and separation checks recorded; rollback rehearsed; delta and live test plans ready; business acceptance; regulatory steps confirmed by LC; my recorded authorisation.
  - If the gate is later passed, SEC's four stages apply, with the secondary process as fall-back throughout.
- **Accountable owner:** SEC for the recommendation, security conditions and gate design. Decision: me as crisis management team chair. Executing: forensic staff, payments operations, IT Operations.
- **HKT time or trigger:** Hold recorded 20:00; recommendation to me by 20:15; reports 21:00; preliminary mismatch classification by 23:00. Earliest gate review 08:00 Wednesday 18 November, and only if conditions 1-7 are recorded.
- **Recipient and channel:** Me, the payments information owner, LC and IT Operations, through the restricted incident workspace and the out-of-band bridge. Hold entered in the incident log and the emergency change record.
- **Final external basis:** SEC Q16a "Basis", unchanged. Anchors re-read:
  - R08 TM-G-1 para 4.2.4, p.18 (through R03 s.6.2.16(a), p.15): "only properly tested and approved systems are promoted to the production environment".
  - R08 para 4.3.1, p.19: "no single person can effect changes to the production environment without the review and approval of other authorized personnel".
  - R07 TM-G-2 para 4.2.2, p.10: "the process for overseeing the recovery and restoration efforts".
  - Weighed against the hold: R06 OR-2, p.3: "Resume normal operations in a timely manner after disruptions occur".
  - No direct rule located for a pass mark or gate composition; zero unexplained difference is professional judgment, which I adopt.
- **Final internal basis:** N/A (PH01 absent).
- **Dispatch instruction:** HOLD on any production use of the recovery image. EXECUTE NOW for the mismatch investigation. SCHEDULE the gate review, dependent on conditions 1-7.

### Q16b

- **Original answer reference:** SEC sealed answer, C06, Q16b.
- **CONFIRM.**
- **Reason:** No production activity is authorised tonight, so nothing is triggered. The criteria are right to fix now, while nobody is under pressure to continue. Limits are tight because the candidate has not yet shown a clean result. Three duty holders can stop without asking, and restart needs my decision.
- **Final action and condition:** As written; in force from the first production transaction of any stage I later authorise.
  - Stop on any security indicator from this incident, any traffic to the compromised segment, logging down for more than 5 minutes, or any unrecorded change.
  - Stop on one unexplained mismatch, any duplicate or altered payment, a reconciliation that is late or does not tie, rejects above 1%, or a counterparty report of unexpected messages.
  - Rollback on a confirmed security stop, an integrity stop unexplained within 30 minutes or repeated in a stage, any customer financial effect, or two checkpoints that do not tie.
  - On rollback: disconnect the recovered gateway, revoke its keys, classify in-flight items, hold unknown items, run a delta reconciliation, and tell COM and LC at once.
  - No second attempt without a new pass through the Q16a gate.
- **Accountable owner:** SEC for the criteria and security stops. Stop: SEC, the payments operations lead or the IT Operations duty manager. Rollback: SEC or the payments information owner. Resumption and stage advance: me.
- **HKT time or trigger:** No time tonight. Observable triggers are the 5-minute, 30-minute and 1% limits and the hourly checkpoints.
- **Recipient and channel:** Criteria attached to the emergency change record and briefed to the three duty holders. Stops and rollbacks announced on the out-of-band bridge and logged.
- **Final external basis:** SEC Q16b "Basis", unchanged. Anchors re-read:
  - R08 para 4.3.1, p.19: "a process for rolling-back changes to re-instate the original programs, system configuration or data in the event of production release problems".
  - R09 TM-E-1 Annex B, p.40: "well-tested fall-back procedures".
  - R14b, p.2: "reconciliation procedures to maintain accuracy following a bypass".
  - The thresholds are professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** NO ACTION tonight beyond attaching and briefing the criteria. They bind any later authorisation.

### Q17a

- **Original answer reference:** LC sealed answer, C06, Q17a.
- **CONFIRM.**
- **Reason:** The firm needs system artefacts to explain the mismatches, not customers' identities. The bank must keep data that is already public for 320 people from spreading further. A staged release gives the firm what it needs tonight and keeps the full image in the bank's custody.
- **Final action and condition:** As written.
  - Now: a minimised data set (logs, configuration, process records, the two mismatched instructions) with customer personal data masked or tokenised.
  - Full image only by supervised access for named analysts inside the bank's offline laboratory, on a written statement of need.
  - A full copy leaves only if that is technically unworkable, with LC's written approval and SEC's sign-off, and the Police informed if the image is among referred evidence.
  - Before transfer: signed engagement terms or addendum; the firm's statement of need; a hash-verified copy with a custody entry; management approval recorded.
  - On transfer: encrypted registered media, hand-delivered against a receipt, keys sent separately, inventory check afterwards; no email or file-sharing service.
  - On use: Hong Kong only, isolated environment, access log, no onward disclosure, deletion or return with a destruction certificate, findings to LC and SEC only.
  - If the engagement lacks the terms, nothing is released until the addendum is signed.
- **Accountable owner:** LC for the release decision and conditions. SEC prepares, hashes and delivers. The firm's engagement lead signs.
- **HKT time or trigger:** Conditions to the firm 20:10; minimised set released by 22:00 if conditions are met; supervised access from 08:00 Wednesday if justified.
- **Recipient and channel:** The retained Hong Kong forensic firm, by hand delivery of encrypted media or supervised access in the bank's laboratory.
- **Final external basis:** LC Q17a "Basis", unchanged. Anchors re-read:
  - R10 Cap. 486, Schedule 1, Principle 4(2), pp.169-170: "must adopt contractual or other means to prevent unauthorized or accidental access, processing, erasure, loss or use of the data transferred to the data processor".
  - R10 Principle 2(3), p.167.
  - R16b Annex C, p.4: "granted on a need-to-have basis only".
  - R12 SA-2 para 2.5.2, p.6.
  - R02 s.7.2.3(h), p.33.
  - No direct rule located on full image against extract; the staged approach is professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the conditions and extract preparation. HOLD on release until the conditions are signed. HOLD on any full copy.

### Q17b

- **Original answer reference:** LC sealed answer, C06, Q17b.
- **CONFIRM.**
- **Reason:** A core function has been down for 36 hours, customers are reporting losses and recovery evidence is incomplete. The Board owns the tolerance for disruption and ultimate responsibility for resilience. Earlier Board confirmation of the ransom posture could not be verified, so it needs minuting.
- **Final action and condition:** As written.
  - Telephone the Board chair, circulate a written paper, and hold a Board or committee meeting before any production recovery step that needs its decision.
  - To note: the disruption, missed payroll cut-offs and counterparty requests; whether the tolerance is breached; the test result and its limits; the data position (320 public, 18,000 unverified, fake page); no payment and no contact; authorities engaged and the written report due 30 November; legal exposure; the forensic data-sharing conditions.
  - Decisions: (1) the recovery gate; (2) minute "do not pay"; (3) remediation principle and budget; (4) crisis committee, reporting rhythm, remedial priorities and an independent root-cause review covering the vendor.
  - Legal advice goes in a separate privileged section.
  - Missing fact: whether the bank or a parent is listed. If so, a market disclosure assessment is needed, outside the sources.
- **Accountable owner:** LC for content and the legal and regulatory sections. I present and am accountable for management's reporting. The company secretary convenes.
- **HKT time or trigger:** Chair telephoned by 20:30; paper by 21:30; meeting by 22:00.
- **Recipient and channel:** Board chair and directors, or the delegated committee, by telephone or video bridge and a written paper on a channel SEC confirms is safe.
- **Final external basis:** LC Q17b "Basis", unchanged. Anchors re-read:
  - R06 OR-2 para 3.2, p.5: "senior management should provide regular and timely reports to the Board".
  - R06 para 3.3, p.6: "The Board is responsible for approving the tolerance for disruption".
  - R06 para 3.4, p.6.
  - R08 para 2.3.4, p.9: "approval of the risk acknowledgement from the owner of the risk and senior management".
  - R05, PDF p.1, "Customer notifications" (checked against the scan): "whether the bank would reimburse any losses incurred by them".
  - New basis for the delegated committee: R06 footnote 2, p.3: "may be discharged by the Board itself or a Board-level committee assigned to oversee operational resilience matters".
  - No direct rule located fixing when or what to escalate during an incident; timing and the list are professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the 20:30 call. SCHEDULE the paper for 21:30 and the meeting for 22:00. Dependency: SEC's 21:00 reports feed the paper.

### Q18a

- **Original answer reference:** COM sealed answer, C06, Unit Q18a.
- **CONFIRM.**
- **Reason:** The update announces only what is true: the service has not been restarted, and why. It does not call the test a success or the systems clean. It speaks directly to SMEs who missed payroll.
- **Final action and condition:** As written.
  - Common text with the Version 2 position paragraph.
  - Queue figures from Operations.
  - "Queued payroll is being sent first" is included on Operations' confirmation; it is SEC's rule.
  - Compensation line as approved at C01, with claims through the relationship manager, call-back service or any branch.
  - Fake-page warning repeated.
  - The pause notice stays drafted for any later stop or rollback.
  - SEC confirms the scope wording, LC clears, and a copy goes to the HKMA through LC.
- **Accountable owner:** COM. Approver: me. Fact check: SEC and Operations. Clearance and HKMA copy: LC. Executing: digital channels team, contact-centre head, SME banking head, branch network head.
- **HKT time or trigger:** 20:10 requests; 20:45 target release; 21:00 latest; 21:30 last targeted push or SMS tonight; next update 07:00 Wednesday 18 November, earlier if the position changes.
- **Recipient and channel:** Website status notice, app and internet banking notice, recorded hotline message, verified social media accounts, press release, targeted push or SMS with no link, relationship manager calls to SME payroll customers.
- **Final external basis:** COM Q18a "Basis", unchanged. Anchors re-read:
  - R09 para 8.2.2 and footnote 26, p.33: "apply for compensation for any losses incurred by the disruption".
  - R05, PDF p.2 (checked against the scan): "the steps that affected customers need to take".
  - R05, PDF p.3: "consistent and up-to-date messages".
  - Missing fact: no resumption time exists, so none is given.
  - How to describe test results is professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE for 20:45, latest 21:00. Dependencies: my recorded hold (given), Operations' figures, LC clearance.

### Q18b

- **Original answer reference:** COM sealed answer, C06, Unit Q18b.
- **CONFIRM.**
- **Reason:** Receiving parties hold unsettled items, and their own customers, including employees awaiting pay, are affected. Two direct requests make notice necessary. Verifying each request by call-back first is right in a week when impersonation tied to this incident is active.
- **Final action and condition:** As written.
  - Verify both requests by call-back to numbers already held, then acknowledge.
  - The head of payment operations makes a verified call and sends COM's written notice: status "not restarted"; a provisional schedule of unsettled items; what to expect; act only on verified contacts; a line for their customers; the update schedule.
  - The notice leaves out forensic findings, the vendor credential, the demand, and the exact test figures unless LC clears them.
  - If SEC has not confirmed the secure channel, the schedule is read over a verified call and delivered by hand or courier.
  - The same notice goes proactively to other banks and counterparties with unsettled items.
  - LC clears and keeps the HKMA informed.
- **Accountable owner:** COM for wording, consistency and the log. Executing: head of payment operations. Approver: me.
- **HKT time or trigger:** Requests verified and acknowledged by 20:30; verified call and written notice at 21:30; from 18 November updates at 08:00, 13:00 and 18:00 daily until every item is settled or returned; immediately on a stage going live, a pause, a rollback or an error affecting their items; proactive notice to others at 08:00 Wednesday, or tonight where the list exists.
- **Recipient and channel:** Named operations contacts at each counterparty. A verified phone call first, then written confirmation through the secure channel already agreed with that counterparty. Not ordinary email with attachments.
- **Final external basis:** COM Q18b "Basis", unchanged. Anchors re-read:
  - R05, PDF p.2, top of page (checked against the scan): "should also notify other affected AIs (so that they can in turn notify their affected customers) as soon as practicable".
  - R07 para 4.7.1, p.13: "counterparties".
  - R07 para 4.7.2, p.14: "Important conversations with external parties should be properly logged".
  - Missing fact: whether the two counterparties are authorized institutions. If not, R07 applies as principle and the notice is the same.
  - Content, channel and frequency are professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for call-back verification. SCHEDULE the notice for 21:30. Dependencies: the register's per-item status, SEC's channel confirmation, LC clearance, the pre-release notice step confirmed by payment operations.

---

### Order of dependent actions on this card

1. **20:00-20:15:** Hold recorded; SEC's recommendation reaches me; my decision is logged. The mismatch investigation opens.
2. **20:10:** COM sends its requests. LC sends the release conditions to the forensic firm.
3. **20:30:** LC and I telephone the Board chair. Counterparty requests are verified by call-back and acknowledged.
4. **20:45 (latest 21:00):** COM releases the customer update, Version 2; LC copies the HKMA.
5. **21:00:** SEC's two reports issue as "not passed".
6. **21:30:** Board paper circulated. The head of payment operations calls each counterparty and sends the notice.
7. **By 22:00:** Board or committee meets and minutes its decisions. SEC releases the minimised forensic data set if the conditions are signed.
8. **After the meeting:** LC updates the HKMA.
9. **By 23:00:** Preliminary classification of the two mismatches to me, the information owner and LC.
10. **07:00-08:00 Wednesday:** Customer update; first scheduled counterparty update and proactive notice to other banks; gate review only if conditions 1-7 are recorded.

### Carried open item (no unit changed)

If recovery is later staged, each phase may be a separate notifiable change under R01 s.22 and R03 para 6.1.1 (quoted at C04). LC's assessment is part of gate condition 7.

### Still unverified at this card

What the two mismatches are and why they arose; the results of SEC's integrity, separation and reconciliation checks; the length of the laboratory's test window; whether rollback has been tested; current queue figures; the tolerance for disruption figure; the forensic firm's engagement terms; who the two counterparties are and their unsettled items.

### My search record

- Regex "breach(ed|es)? (of )?(its |the )?tolerance|exceed(ed|s)? (its |the )?tolerance|outside (its |the )?tolerance", all documents: 1 hit (R06 p.6). No source sets a report or deadline triggered by breaching the tolerance.
- Regex "staged|phased|go/no-go|resumption criteria|roll(ing)?-?back", all documents: 3 hits (R08 p.19; R14b pp.3, 4). None sets a restart gate or pass mark.
- Limitation: the laboratory's report, the bank's recovery plan and tolerance figures, and the forensic firm's engagement terms are not in the manifest.