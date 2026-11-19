## CEO final decisions, C07 (Wednesday 18 November 2026, 12:00 HKT, H+52)

All six units are CONFIRMED; there are no overrides. I re-read the citations in the three sealed answers against the source pages and found them accurate. PH01 is not in the manifest ("PH01", all documents: 0 hits), so the internal basis is N/A throughout.

All actions below are simulated, for the facilitator to log.

### My own decisions that the sealed answers asked for

- **Containment and monitoring:** containment is retained in full and monitoring is raised. Nothing is reduced without my approval on a change record.
- **Recovery gate:** I adopt SEC's ninth condition (the new indicator classified, and the search for it clean in the recovery environment). The recovery hold stays. I tell the Board chair today.
- **Secondary process:** if SEC's 14:00 check finds a C04 gate unmet, releases pause on SEC's or payments operations' authority. I am told at once and I decide resumption.
- **Written incident report:** LC owns it and SEC owns the technical content. I approve it on Thursday 26 November, the Board sees it, and it is submitted on Friday 27 November. The statutory limit is Monday 30 November.
- **Staff promise list:** approved as COM wrote it, once LC clears it. Staff do not promise reimbursement of scam losses.
- **Remediation position:** I give the decision COM asks for by 17:00 today, covering scam losses linked to the exposure and support for the 320. The Board's C06 remediation decision is not on record, so I take it to the Board chair today.
- **Notification register:** process approved. The audience is unchanged at the same 320.

### Conflicts between sealed answers, resolved within their stated branches

1. **Timeline dates.** LC wants SEC's timeline in the report draft on Monday 23 November; SEC's reviewed baseline is due Wednesday 25 November. Monday's draft uses the latest independently reviewed version (the first review completes Thursday 19 November). The 25 November baseline is reconciled at LC's check that day, before my approval.
2. **Awareness time.** LC treats 08:00 on 16 November as fixed; SEC will state statutory timestamps with their uncertainty. The reports give the recorded time with SEC's uncertainty note. A four-minute shift changes no deadline: the margins were hours, and the 14-day clock runs from the date.
3. **State of the secondary process.** No card records that its gates were cleared. SEC verifies by 14:00. LC's HKMA update and any COM service line follow that result; until then the state is described as being verified.
4. **New indicator and the statutory clock.** LC files supplementary information by 14:00, describing the relationship as unverified. SEC classifies by 18:00. If SEC reaches reasonable certainty of a separate incident, LC's fresh 12-hour clock starts then and LC notifies within the hour.
5. **Scam details.** COM's single case register feeds SEC for blocking and removal requests, and LC for the Police and HKMA. Nobody collects them twice.
6. **Completion figures.** LC states no "customers notified" figure to any regulator before COM's rebuilt register produces one at 15:00.

---

### Q19a

- **Original answer reference:** SEC sealed answer, C07, Q19a.
- **CONFIRM.**
- **Reason:** With clocks up to four minutes apart, a timeline that silently "corrects" times could not be checked. SEC keeps the original timestamp, the offset and the uncertainty on every row, and refuses to assert an order the evidence cannot support. That is what makes it reviewable by a regulator or the Police.
- **Final action and condition:** As written.
  - One master timeline from the three delivered record sets, the bank's independent logs, the incident log and the evidence register. Original records are never altered.
  - Reference clock: HKT from the bank's primary time source.
  - An offsets table is built first, from direct comparison, anchor events and a three-way consistency check, measured at more than one point.
  - Each row carries the source, original timestamp, offset, normalised time, uncertainty in seconds, evidence reference and hash, status, analyst and reviewer.
  - Events closer together than their combined uncertainty are marked "order undetermined".
  - Hypotheses are labelled; attribution is not stated; log gaps are listed.
  - No customer personal data.
  - Normalisation is scripted and versioned. An independent reviewer traces a sample and re-runs it; SEC signs.
- **Accountable owner:** SEC. Executing: bank forensic staff with the forensic partner, an independent reviewer, the vendor for its clock source.
- **HKT time or trigger:** Offsets table by 14:00; timeline version 1 by 18:00 today; independent review complete by 12:00 Thursday 19 November; updated daily and on new evidence; reviewed baseline for the written report by Wednesday 25 November.
- **Recipient and channel:** Restricted incident workspace; versions to me, LC and the privacy officer; each version and hash entered in the evidence register.
- **Final external basis:** SEC Q19a "Basis", unchanged. Anchors re-read:
  - R02 s.7.2.3(a)(v)(4), p.32: "Recording the incident response process, including details of the incident, actions taken and decisions made;".
  - R02 s.6.2.23(g), p.20: "synchronise the internal clocks of all CCSs components with a primary time source to enable accurate log-event correlation across the systems".
  - R02 Annex E items B(3)-(4), p.42.
  - No direct rule located for recording offsets, uncertainty or the ordering rule; the method is professional judgment.
- **Final internal basis:** N/A (PH01 absent).
- **Dispatch instruction:** EXECUTE NOW. Dependency: the vendor's statement of its clock source.

### Q19b

- **Original answer reference:** SEC sealed answer, C07, Q19b.
- **CONFIRM.**
- **Reason:** An unexplained indicator, together with validation results that no card records, does not support relaxing anything. Residual attacker access cannot be excluded, and customer data for the wider group is still at risk while that is so.
- **Final action and condition:** As written.
  - Retain all containment; raise monitoring; raise containment only on SEC's triggers.
  - Steps 1-8: preserve the quarantined host and fix the indicator's first-seen time; detection rules with round-the-clock review; search back across all environments; review sign-ins and tokens since revocation; perform or re-perform and record the C03 tests, rotation and persistence removal; record the actual state of the secondary process and its seven gates; heightened monitoring on the 320 accounts using details from the scam reports; preliminary classification.
  - Triggers: the indicator on another host means isolation at once. In the recovery environment the candidate fails. On secondary-process hosts, or with a gate unmet, releases pause. Any use of a revoked identity is treated as active intrusion.
  - The recovery hold stays, with the ninth gate condition.
  - Reduction criteria as written; none is met.
- **Accountable owner:** SEC. Executing: forensic staff, Security Operations Centre, forensic partner, identity administrators, IT Operations, payments operations, fraud monitoring team.
- **HKT time or trigger:** Step 1 by 12:30; Step 2 by 13:00; Steps 6 and 7 by 14:00; Steps 3-5 by 16:00; classification by 18:00; hourly report to me until classified; next review 08:00 Thursday 19 November or on any trigger.
- **Recipient and channel:** Monitoring, endpoint, perimeter and identity systems, under emergency change records. Hourly status to me and LC on the out-of-band bridge.
- **Final external basis:** SEC Q19b "Basis", unchanged. Anchors re-read:
  - R03 s.6.2.26(a), p.19: "implement measures to detect computer-system security incidents affecting CCSs".
  - R02 s.6.2.26(d), p.22: "24 x 7 monitoring and a timely response to any security events".
  - R08 TM-G-1 para 6.1.4, p.22: "The network should be monitored on a continuous basis."
  - R05, PDF p.1, "Immediate incident response" (checked against the scan): "as soon as practicable rectify or contain the problem".
  - R10 Cap. 486, Schedule 1, Principle 4(1), p.169.
  - No direct rule located on raising or reducing monitoring after a new indicator; that is professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW. HOLD on any reduction of containment and on production recovery.

### Q20a

- **Original answer reference:** LC sealed answer, C07, Q20a.
- **CONFIRM.**
- **Reason:** LC reads the record correctly. The first notification was by telephone with no specified form, so a written record in the specified form was required. The record shows it filed by 19:00 on 16 November, well inside the limit. No receipt is recorded and the limit has now passed, so the filing has to be proved today.
- **Final action and condition:** As written.
  - Status: required; satisfied on the record; not late; unproven for want of a receipt.
  - SEC retrieves the secure channel's dispatch record or submission receipt.
  - LC telephones the designated number with a witness, asks for confirmation of the form and both calls, and records officer, post and reference.
  - If either confirms: recorded as satisfied in time, with the evidence filed.
  - If neither confirms by 13:00: treated as late. LC files Annex E by 13:30 with a factual covering note, tells me and the Board chair, preserves the evidence of the 16 November attempt, and includes it in the next HKMA update.
  - LC sends the undispatched supplementary information through the secure channel: the public file, the 320 figure, the fake page, the 31 scam reports, the new indicator and unverified attribution.
- **Accountable owner:** LC. SEC retrieves the dispatch record.
- **HKT time or trigger:**
  - 12 hours from awareness at 08:00 on 16 November: ended 20:00 that day; met by the 08:30 call.
  - 48 hours from the 08:30 notification: ended 08:30 today; met by the 19:00 filing if it was dispatched.
  - 14 days from the awareness date: ends Monday 30 November (see Q20b).
  - Immediate actions: 12:10, 12:20, 13:00 decision point, 13:30 contingent filing, 14:00 supplementary information.
- **Recipient and channel:** Commissioner of Critical Infrastructure (Computer-system Security), by the designated telephone number and the designated secure filing channel.
- **Final external basis:** LC Q20a "Basis", unchanged. Anchors re-read:
  - R01 Cap. 653 s.28(3), p.44: "must subsequently submit a written record of the computer-system security incident concerned in the specified form and way".
  - R01 Schedule 6 item 2, p.97: "48 hours after the notification concerned is made under section 28(1)".
  - R01 s.67(1)(a)(iii), p.84.
  - R02 para 7.3.6(b), p.36.
  - R02 para 7.3.5, p.36: "a reasonable degree of certainty".
  - No direct rule located requiring interim updates before the written report; sending one is professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the 12:10 retrieval and 12:20 call. SCHEDULE the 14:00 supplementary filing. The 13:30 filing is conditional on no confirmation by 13:00.

### Q20b

- **Original answer reference:** LC sealed answer, C07, Q20b.
- **CONFIRM.**
- **Reason:** The written report is a separate statutory step from the notification and the written record, with its own form and its own clock. No dispatch is recorded, so it is still to come. Assigning owners now and submitting three days early leaves room for the timeline review and my approval.
- **Final action and condition:** As written.
  - What: R02 Annex F (form CICS006), completed as far as information allows, with uncertain items stated as uncertain: clock offsets, the new indicator, attribution and the wider data claim.
  - Who: the bank as designated operator carries the duty. LC is the accountable owner, coordinates and submits. The employee supervising the computer-system security management unit (assumed to be SEC) owns the technical content. I approve; the Board or its committee sees it first.
  - Section owners: SEC with the forensic partner; payments operations; LC; COM; Finance.
  - If the investigation is incomplete, the report still goes on time, marked preliminary, with supplementary material to follow.
  - Missing fact: whether a sector-specific form applies. LC asks on today's call; the default is Annex F.
  - A copy goes to the HKMA as a courtesy.
- **Accountable owner:** LC. Technical content: SEC. Approval: me.
- **HKT time or trigger:** Owners assigned today; first full draft Friday 20 November; timeline and preliminary root cause in on Monday 23 November; legal and factual check Wednesday 25 November; my approval and Board sight Thursday 26 November; submission Friday 27 November. Statutory limit: Monday 30 November 2026.
- **Recipient and channel:** Commissioner of Critical Infrastructure (Computer-system Security), through the designated secure filing channel, with the dispatch record kept.
- **Final external basis:** LC Q20b "Basis", unchanged. Anchors re-read:
  - R01 s.28(4), p.44: "must further submit a written report of the incident in the specified form and way to the Commissioner within the specified time".
  - R01 Schedule 6 item 3, p.97: "14 days after the date on which the CI operator concerned becomes aware".
  - R02 para 7.3.7(a), p.37: "via the designated secured channel within 14 days after becoming aware".
  - R01 s.21(1)(b), p.31.
  - R03 para 1.1.3, p.3.
  - Internal sign-off and the 27 November target are professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE. Section assignments go out today; submission is 27 November. Dependency: SEC's reviewed timeline.

### Q21a

- **Original answer reference:** COM sealed answer, C07, Unit Q21a.
- **CONFIRM.**
- **Reason:** One intake and one register let the bank see patterns, such as several of the 320 reporting the same approach. The promise list gives a worried customer something concrete, namely account protection, a reference and a named handler. It does not promise what would have to be withdrawn later.
- **Final action and condition:** As written.
  - One intake, one case register, four routes: fraud team (details given, or money lost); fraud intelligence desk (suspicious contact only); data protection officer in LC (identity misuse or privacy question); claims desk (disruption fees and losses).
  - Each reporter is checked against the list of 320 and the wider group.
  - Staff may promise: immediate account protection; a case reference, named contact and times; investigation and an outcome; no bank fees or charges from the disruption and registration of loss claims; handling of unauthorised transactions in line with R09, in wording LC confirms; support for a Police report and an attempt to stop or recall funds.
  - Staff may not promise: reimbursement of any scam loss, its amount or timing; that a scam was or was not caused by the exposure; recovery of funds; who is responsible; that the incident is over; paid support; anything admitting or denying liability.
- **Accountable owner:** COM for intake wording, the promise list and the staff instruction. Executing: head of fraud, claims desk lead, data protection officer and LC, SEC.
- **HKT time or trigger:** 12:30 Frontline Instruction No. 6; 13:00 the 31 reports triaged and assigned; 17:00 every reporter has had first contact, and the daily case summary reaches the crisis management team and LC.
- **Recipient and channel:** Staff by briefing call and intranet. Customers by a call from the case handler using the reference, then written confirmation in the secure inbox or by letter. Daily totals to LC.
- **Final external basis:** COM Q21a "Basis", unchanged. Anchors re-read:
  - R09 TM-E-1 para 4.4.3, p.18: "a mechanism for customers to promptly suspend their e-banking accounts".
  - R09 para 4.4.4, p.18: "should not be responsible for any direct loss suffered by him or her as a result of unauthorized transactions".
  - R09 para 8.2.5, p.33.
  - R05, PDF p.1, "Customer notifications" (checked against the scan): "whether the bank would reimburse any losses incurred by them".
  - Missing fact: no remediation decision for scam losses exists yet; I supply it by 17:00.
  - Routing and response times are professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for triage. SCHEDULE the 12:30 instruction and the 17:00 first-contact deadline. Dependency: LC's clearance of the promise list.

### Q21b

- **Original answer reference:** COM sealed answer, C07, Unit Q21b.
- **CONFIRM.**
- **Reason:** The record shows approvals and schedules but no completion figures for any batch. Sending more notices on that footing risks duplicates that look like the scams now circulating. Rebuilding from delivery evidence, fixing the 12 first and then filling only real gaps is the right order.
- **Final action and condition:** As written.
  - One notification register, one row per customer, built from call logs, secure inbox records and courier proofs. Approvals and schedules do not count as delivery.
  - Bulk follow-ups are paused until it is rebuilt. First notices to anyone not yet reached are not paused.
  - The 12: stop using the old details at once; check what went where; confirm the corrections come from the bank's verified records; refer any change made after 16 November to the fraud team; deliver one consolidated notice by personal call plus secure inbox or signed-for letter.
  - If anything reached a wrong person: try to retrieve it, ask for destruction, and pass it to LC as a possible further privacy incident.
  - Duplicate rules: nothing further where current content is evidenced as delivered; one consolidated notice where it is not; the 320 removed from the wider-group list; case handlers deliver follow-ups to customers with open scam cases; a second person checks every send list.
  - No SMS or email carrying a link.
- **Accountable owner:** COM. Executing: call team lead, digital channels team, Operations, SEC, fraud team, LC.
- **HKT time or trigger:** 12:15 bulk follow-ups paused and old details blocked; 13:00 check on the 12 complete and calls begin; 14:00 first attempts to the 12; 15:00 register rebuilt with completion figures; 16:00 consolidated notices to the gap list and letters to the 12; 17:00 figures to me and LC.
- **Recipient and channel:** The 12 and the gap list by phone, secure inbox and couriered letter. The register and figures to LC and the dispatch log.
- **Final external basis:** COM Q21b "Basis", unchanged. Anchors re-read:
  - R10 Cap. 486, Schedule 1, Principle 2(1)(b)(i), pp.166-167: "the data is not used for that purpose unless and until those grounds cease to be applicable to the data".
  - R16a, p.5: "Adopt four-eyes principle".
  - R11, p.6, Step 5: "A comprehensive record of the incident is therefore required".
  - No direct rule located on duplicate or consolidated notices; the rules are professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the pause and the block on old details. SCHEDULE the 13:00, 15:00 and 16:00 steps. HOLD on bulk follow-ups until the register is rebuilt.

---

### Order of dependent actions on this card

1. **12:10-12:30:** SEC's evidence custodian retrieves the dispatch record for LC. LC telephones the Commissioner's designated number. COM pauses bulk follow-ups and blocks the old details. SEC preserves the quarantined host. COM issues Frontline Instruction No. 6.
2. **13:00:** LC records the written record as satisfied, or files Annex E by 13:30. SEC's detection rules go live. The 31 scam reports are triaged. Calls to the 12 begin.
3. **14:00:** SEC's offsets table, the verified state of the secondary process, and heightened monitoring on the 320 accounts. LC's supplementary information goes to the Commissioner. LC's HKMA update follows SEC's result.
4. **15:00:** COM's register is rebuilt, with completion figures.
5. **16:00:** SEC's searches, sign-in review and re-performed tests are recorded. COM sends consolidated notices to the gap list.
6. **17:00:** Every scam reporter has had first contact. Figures go to me and LC. I give the remediation decision.
7. **18:00:** SEC's timeline version 1 and the indicator's classification. If it is a separate incident, LC notifies within the hour.
8. **19 November:** Independent review of the timeline by 12:00; SEC's containment review at 08:00.
9. **20-27 November:** Report draft, timeline in, checks, my approval, submission on the 27th. Statutory limit is the 30th.

### Still unverified at this card

Receipt of the 16 November written record and both calls; whether the secondary process's gates were cleared and whether it is releasing; which host carries the new indicator and when it appeared; the C03 test, rotation and persistence-removal results; delivery of every notification batch; whether anything was misdelivered for the 12; any link between the 31 scams and the exposure; attribution; the Board's 17 November decisions.

### My search record

- Regex "clock|time source|synchroni[sz]", all documents: 4 hits (R02 p.20, three times; R09 p.6, unrelated). No source says how to record offsets.
- Regex "reimburs|compensat", all documents: 39 hits, first 25 shown. The relevant ones are R05 p.1, R09 p.33 and R10 p.135. None sets a position on scam losses following a data exposure, so the 17:00 decision is judgment.
- Limitation: the second search was truncated at 25 hits; the unseen hits are in R16c and R16d, the two crime statutes. The delivered record sets, the industry control matrix R03 cites, and the Code of Banking Practice that R09 refers to are not in the manifest.