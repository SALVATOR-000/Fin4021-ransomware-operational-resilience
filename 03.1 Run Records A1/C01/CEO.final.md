## CEO final decisions, C01 (Monday 16 November 2026, 08:00 HKT, H+0)

All six units are CONFIRMED; there are no overrides. I re-read the load-bearing citations in the three sealed answers against the source pages (R05 against the page images of PDF pp.1-3) and found them accurate. PH01 is not in the manifest (search "PH01", all documents: 0 hits), so the internal basis is N/A throughout.

All actions below are simulated, for the facilitator to log.

### My own decisions that the sealed answers asked for

- **08:00, dispatch log entry 1:** I convene the crisis management team (CMT) and implement the emergency response plan. The plan's content is not in the sources; where it differs from a step below, the plan is followed and the deviation logged (SEC's stated condition).
- **Compensation wording (COM asked by 08:20):** Line A.
- **External forensic firm (SEC asked by 08:30):** emergency engagement approved if none is retained.
- **Holding statement:** I approve at 08:35 on the checked draft and act as single spokesperson.
- **Business continuity plan:** not activated at 08:00. The 08:30 CMT decides on SEC's containment report.
- **One log:** the dispatch log is the single master record; SEC's evidence register, LC's regulator register and COM's communications log are cross-referenced to it.

### Conflicts between sealed answers, resolved within their stated branches

1. **Fact sheet timing.** LC wants it at 08:05; SEC says "by 08:30". SEC's sealed 08:00 status table is version 1 and goes to LC and COM at 08:05. LC's check is not an approval gate.
2. **Channel confirmation.** COM's cut-off is 08:15; SEC validates at 08:20. COM's stated 08:15 fallback runs (card-confirmed wording through branch notices, relationship manager calls, IVR). Digital notices follow SEC's 08:20 validation.
3. **Secure filing terminal.** LC wants it restored; SEC preserves it untouched. LC names "SEC or IT" as owner; I select SEC, so SEC's evidence rule applies before any change. LC's question to the Commissioner about an alternative way and LC's 12:00 Tuesday checkpoint stand.
4. **LC's workload.** LC clears COM's customer wording at 08:05-08:12, calls the HKMA at 08:15, reviews the statement draft from 08:20, calls the Commissioner by 08:30, and sends the HKMA written confirmation at 08:45 with the statement copy.

Point 3 is the closest call: if sequencing the restore behind an evidence release is read as a new condition, the affected unit is Q02b, follow-up step only.

---

### Q01a

- **Original answer reference:** SEC sealed answer, C01, Q01a (decision, Steps 1-5 table, stop and escalation triggers).
- **CONFIRM.**
- **Reason:** It isolates only what is already down (the gateway segment and the command route), keeps mobile balance viewing and branches running, tests both after the cut, and holds unverified failover. Its escalation rule already brings to the CMT any step that would remove a working service, which covers inbound transfers if they prove to pass through the gateway (unknown on the card).
- **Final action and condition:** As written. Steps 1, 2, 3 and 5 proceed. Step 4 (standby gateway) stays on hold until SEC records a release. No bank-wide shutdown and no power-off. I ratify as CMT chair.
- **Accountable owner:** SEC. Executing: Network Operations, identity/privileged access administrators, backup team, IT Operations, Security Operations Centre (role names assumed by SEC).
- **HKT time or trigger:** Start 08:00; Step 1 by 08:10; validation by 08:20; report to CMT 08:30; re-validate every 30 minutes. These are SEC's judgment targets.
- **Recipient and channel:** Gateway boundary devices and identity systems, by emergency change record and out-of-band phone bridge. Status to me/CMT, LC, COM and IT Operations.
- **Final external basis:** SEC Q01a "Basis", unchanged. Anchors re-read:
  - R05, PDF p.1, "Immediate incident response": "as soon as practicable rectify or contain the problem".
  - R08 TM-G-1 para 4.3.2, p.19: "Emergency changes should be approved by the information owner".
  - R02 s.7.2.3(a)(v)(1), p.32: "Containing the incident to prevent further harm;".
  - What to isolate first, the order and the times are professional judgment; SEC's "No direct rule located" search record stands.
- **Final internal basis:** N/A (PH01 absent).
- **Dispatch instruction:** EXECUTE NOW for Steps 1-3 and 5. HOLD for Step 4. Dependency: boundary device configurations are exported before Step 1 (Q01b item 1).

### Q01b

- **Original answer reference:** SEC sealed answer, C01, Q01b (decision, evidence items 1-8, custody record).
- **CONFIRM.**
- **Reason:** The hold stops recovery work destroying evidence. The 10-minute cap on pre-isolation capture, and "isolate first if encryption is spreading", stop it delaying containment. No recovery step is ready at this card, so the hold costs no service time now.
- **Final action and condition:** As written. Evidence hold from 08:00; items 1-8 in SEC's order; one register plus a chain-of-custody form per item; SHA-256 at acquisition; sealed masters; a custodian who is not an administrator of the affected systems. The secure filing terminal is preserved untouched until SEC establishes whether its outage is related.
- **Accountable owner:** SEC. Executing: forensic staff, Security Operations Centre, administrators on SEC instruction, external firm if engaged.
- **HKT time or trigger:** 08:00 hold and register; 08:00-08:10 items 1 and 2; by 09:00 log exports and first custody status. Trigger: no recovery change without a recorded SEC evidence release.
- **Recipient and channel:** Evidence repository, safe and register. Hold notice to IT Operations, administrators, backup team, Security Operations Centre and any gateway service provider, by out-of-band bridge and written notice in the log.
- **Final external basis:** SEC Q01b "Basis", unchanged. Anchors re-read:
  - R02 s.7.2.3(a)(v)(2), p.32: "preservation of evidence and chain of custody;".
  - R02 s.7.2.3(f), p.33: "the CI operator should prioritize incidents which had impacted business operations, require swift damage containment or need immediate system recovery".
  - Imaging, hashing and custody fields are professional judgment; SEC's search record stands.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW. HOLD on reboot, restore, rebuild or failover of affected components, and on the terminal.

### Q02a

- **Original answer reference:** LC sealed answer, C01, Q02a.
- **CONFIRM.**
- **Reason:** R05 asks for immediate notice with whatever is known, without waiting for a fix. LC's content separates confirmed from unknown and avoids "ransomware", a restoration time and any data assurance. I agree that my approval is not a precondition.
- **Final action and condition:** As written. LC telephones the HKMA, then confirms in writing.
  - Condition 1 is met by SEC's 08:00 status table at 08:05.
  - Condition 2 (email safe) is for SEC to confirm; if not, LC agrees an out-of-band written route on the call.
  - If the 08:30 CMT activates the business continuity plan, LC tells the HKMA at once (LC's stated conditional action).
- **Accountable owner:** LC.
- **HKT time or trigger:** Awareness 08:00. Clock "immediately". Call by 08:15; written confirmation by 08:45; update at 10:00 or earlier on LC's stated triggers.
- **Recipient and channel:** HKMA, the bank's usual Banking Supervision contact, by telephone then email. The channel is judgment; no rule located (LC's search record stands).
- **Final external basis:** LC Q02a "Basis", unchanged. Anchors re-read:
  - R05, PDF p.2, "Reporting incident to the HKMA" (checked against the scan): "should notify the HKMA immediately and provide it with whatever information is available at the time".
  - R09 TM-E-1 para 8.2.5, p.33.
  - R07 TM-G-2 para 1.3.3, p.5: "AIs should inform the HKMA promptly if their BCP is activated."
  - Classing this as "significant" is judgment, which I share.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the call. SCHEDULE the 08:45 written confirmation and the 10:00 update.

### Q02b

- **Original answer reference:** LC sealed answer, C01, Q02b.
- **CONFIRM.**
- **Reason:** The statutory test is met on card facts: an unauthorised act with actual adverse effect on a designated system, and a disrupted core function, so the 12-hour limit applies. The recipient is the Commissioner, not the HKMA. Telephone is feasible with the terminal down and is permitted.
- **Final action and condition:** As written.
  - LC telephones the designated number and states the nature, the system involved, a brief summary and a contact.
  - LC logs time, officer and reference, and asks what alternative way applies if the terminal stays down.
  - Written record (R02 Annex E) follows through the secured channel; written report (R02 Annex F) after that.
  - Terminal restoration is owned by SEC under its evidence rule.
- **Accountable owner:** LC. SEC supplies the technical contact and the earliest identifiable time.
- **HKT time or trigger:**
  - Awareness: 08:00 HKT, 16 November 2026.
  - Statutory limit: as soon as practicable, and by 20:00 HKT, 16 November.
  - Target: call completed by 08:30.
  - Annex E: within 48 hours of the logged call (08:30 Wednesday 18 November if the call ends at 08:30).
  - Terminal checkpoint: 12:00 Tuesday 17 November.
  - Annex F: by Monday 30 November.
- **Recipient and channel:** Commissioner of Critical Infrastructure (Computer-system Security), designated telephone number, through the bank's verified telephone route. The number is not in the sources.
- **Final external basis:** LC Q02b "Basis", unchanged. Anchors re-read:
  - R01 Cap. 653 s.28(1), pp.43-44: "the operator must notify the Commissioner of the incident".
  - R01 Schedule 6 item 1(a), p.97: "12 hours after the CI operator concerned becomes aware of the incident".
  - R01 s.28(2)(b)(ii), p.44.
  - R02 para 7.3.6(b), p.36: "may first make the notification to a designated telephone number".
  - R03 para 1.1.3, p.3.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the call. SCHEDULE Annex E and Annex F. HOLD the terminal restore pending SEC's release.

### Q03a

- **Original answer reference:** COM sealed answer, C01, Unit Q03a.
- **CONFIRM.**
- **Reason:** R05 asks for proactive notice by the most effective means, with steps to take and the reimbursement position. The tiers reach payroll-critical SME customers first, and the wording stays within confirmed facts and LC's "not to be said" list. COM's own fallback absorbs SEC's 08:20 validation time.
- **Final action and condition:** As written.
  - Three tiers with COM's wording, compensation Line A, my verbal approval as CMT chair logged.
  - 08:15: the stated fallback runs if SEC has not confirmed channels.
  - Digital Tier 1 goes live on SEC's validation.
  - Direct alerts go no later than 08:30 even if LC has not yet reached the HKMA.
  - Extra hotline staffing is authorised.
- **Accountable owner:** COM. Executing: digital channels team, contact-centre head, branch network head, SME banking head, Operations.
- **HKT time or trigger:** 08:05 fact requests; 08:15 staff script; 08:20 Tier 1; 08:30 Tiers 2 and 3 and relationship manager calls; 10:00 update or earlier on a change in service scope.
- **Recipient and channel:**
  - SME customers: email or secure message, SMS or push, relationship manager call.
  - Retail customers: app and internet banking notices, push, targeted SMS or email, IVR, branch notices.
  - Staff: internal broadcast.
- **Final external basis:** COM Q03a "Basis", unchanged. Anchors re-read:
  - R05, PDF p.1, "Customer notifications", 2nd paragraph (checked against the scan): "whether the bank would reimburse any losses incurred by them and if so, how they can apply for compensation".
  - R09 para 8.2.2, p.33.
  - Choosing Line A is my professional judgment. R05 leaves the reimbursement decision to the bank. Waiving our own fees and opening a claims route is low-risk and tells customers how to apply. I settle the wider loss position with LC before the 10:00 update.
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE for 08:15, 08:20 and 08:30. Dependencies: SEC channel confirmation, LC wording clearance, Operations customer lists.

### Q03b

- **Original answer reference:** COM sealed answer, C01, Unit Q03b.
- **CONFIRM.**
- **Reason:** Both R05 circumstances for a public announcement are met: a critical service is disrupted and a large number of customers may be affected. Failover is unverified, so there is no reasonable confidence of early resumption. A statement also reaches payees at other banks.
- **Final action and condition:** As written.
  - One bilingual holding statement in COM's wording with Line A; no interviews; reactive lines identical.
  - Release conditions 1-3 and their fallbacks stand.
  - "have notified" is used only if LC confirms the notifications were made by release time.
  - "contain" is used only once SEC confirms containment has started.
  - A copy goes to the HKMA through LC at or just before release, for reference, not pre-clearance.
- **Accountable owner:** COM. Approver: me; alternate is the CMT chair's delegate as COM wrote. HKMA copy: LC.
- **HKT time or trigger:** 08:20 draft to SEC and LC; 08:35 to me; 08:45 target release; 09:00 latest; 10:00 update.
- **Recipient and channel:**
  - Public: website homepage and newsroom. If the site is inside the isolation scope: email to newsdesks, verified social accounts, branch notices and IVR.
  - Media: press release by email.
  - HKMA: copy via LC.
  - Branches and contact centre: same text.
- **Final external basis:** COM Q03b "Basis", unchanged. Anchors re-read:
  - R05, PDF p.2, "Public announcement" (checked against the scan): "consider making a public announcement where the situation so warrants".
  - R09 para 8.2.3, p.33: "expected to issue a press release (or make a similarly effective notification) shortly after the commencement".
  - R05, PDF p.3: "a proper communication strategy should be formulated by the senior management".
  - No direct rule located naming the approver; my approval is judgment (COM's search record stands).
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE for 08:45, latest 09:00. Dependencies: SEC confirmation, LC status and clearance, my approval.

---

### Order of dependent actions on this card

1. **08:00:** I open the dispatch log, convene the CMT and issue the authorisations above.
2. **08:00-08:10:** SEC exports boundary configurations and captures live state (capped), then isolates the gateway segment. If encryption is spreading, isolation goes first.
3. **08:05:** SEC's 08:00 status table goes to LC and COM. LC clears COM's customer wording by 08:12.
4. **08:15:** LC telephones the HKMA. COM issues the staff script and, without SEC's channel confirmation, the fallback notices.
5. **08:20:** SEC validates isolation, mobile balance viewing and a branch teller function. COM's digital Tier 1 goes live on that validation. COM's statement draft goes to SEC and LC.
6. **08:30:** LC telephones the Commissioner (statutory latest 20:00). COM sends Tiers 2 and 3. SEC reports to the CMT, which decides on the business continuity plan; if activated, LC tells the HKMA at once.
7. **08:35-08:45:** I approve the statement. COM releases it at 08:45 (latest 09:00). LC's written confirmation to the HKMA carries the copy.
8. **09:00:** SEC gives the first custody status.
9. **10:00:** LC updates the HKMA. COM updates customers and the public.
10. **Standing holds:** no failover or restore, and no change to the secure filing terminal, without SEC's recorded release. Annex E follows within 48 hours of the logged call; Annex F by 30 November.

### Open item for the 08:30 CMT (no unit changed)

R05, PDF pp.1-2, "Customer notifications": "Where necessary, the AI should also notify other affected AIs". Whether any other bank needs to act is unknown. COM and Operations report on it at 08:30.

### Still unverified at this card

Failover capability; whether mobile and branch systems are clean; whether any data left the bank; any ransom element; whether the terminal outage is related.

### My search record

- "PH01", all documents: 0 hits.
- "notif" in R03: 25 hits on pp.2, 5, 9, 10, 11, 14; none sets an incident notification to the Monetary Authority.
- Regex "HKICL|Faster Payment|clearing house|settlement institution|other affected AIs", all documents: 4 hits (R01 pp.89-90, R05 p.2, R10 p.14); only R05 p.2 is relevant.
- "senior management" in R02: 4 hits (pp.12, 32, 32, 46); none names an approver for containment, notification or a public statement.
- Limitation: the bank's emergency response plan and business continuity plan are not in the manifest.