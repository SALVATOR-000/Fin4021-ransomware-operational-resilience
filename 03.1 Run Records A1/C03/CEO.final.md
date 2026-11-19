## CEO final decisions, C03 (Monday 16 November 2026, 12:00 HKT, H+4)

All six units are CONFIRMED; there are no overrides. I re-read the citations in the three sealed answers against the source pages and found them accurate. PH01 is not in the manifest ("PH01", all documents: 0 hits), so the internal basis is N/A throughout.

All actions below are simulated, for the facilitator to log.

### My own decisions that the sealed answers asked for

- **Approved audience now:** the 80 customers whose export is verified. COM sends; nothing waits for the wider scope work.
- **Wider group (up to 18,000):** no individual notice yet. I decide at 18:00, or at once on any of LC's expansion events. COM pre-stages the precautionary notice and scales the hotline now.
- **Recorded justification for the wider hold:** export is unverified. The exact list of individuals does not exist until SEC's workspace inventory at 15:00. The 14:00 public update carries the protective advice to everyone meanwhile.
- **Public update:** approved with the 18,000 figure stated and labelled as not confirmed. No Police reference. No containment claim unless SEC confirms closure.
- **Extra support offer (for example paid credit monitoring):** not in the first notice. COM and LC bring a costed proposal to the 18:00 checkpoint.
- **Session termination:** I authorise SEC's Steps 2-4 now whatever the service impact. Service impact from secret rotation comes to the crisis management team.
- **Operations:** put the extra monitoring and verification on the 80 accounts now, so the notice can say so.
- **Board:** the confirmed match is one of LC's C02 review triggers. I brief the Board at its 12:00 meeting. My recommendation stays "do not pay", because payment cannot retrieve copied data. No attacker contact.

### Conflicts between sealed answers, resolved within their stated branches

1. **Privacy Commissioner form and public update each quote the other's status.** LC files first, marking the media statement "Intend to issue". COM then releases using "have reported".
2. **Police reference.** COM would add one if LC confirms a report. LC's standing C02 line is that nothing is said about reports to law enforcement. COM's base text, without the reference, is used.
3. **Timing for the 80.** COM starts at 12:45 and finishes first attempts by 14:00. That sits inside LC's 15:00 outer limit, so COM's times govern.
4. **"List of 80 is final" (COM) against "80 confirmed so far" (SEC).** The 80 named individuals are fixed; the total may rise. No text says "only 80".
5. **Three items land at 18:00.** SEC's third scope statement comes first, then my wider-group decision, then LC's regulator updates and COM's public update.
6. **Vendor accounts disabled while mobile transfers are still down.** Recovery support from the vendor is on site, supervised, on a bank-issued temporary account, as SEC wrote. I accept the slower recovery.

---

### Q07a

- **Original answer reference:** SEC sealed answer, C03, Q07a.
- **CONFIRM.**
- **Reason:** The three tiers give LC and COM figures they can act on now without overstating or understating. The 80 is a floor, the 18,000 is neither "exported" nor "safe", and the table says in advance what evidence moves the estimate. Clean-looking logs from compromised hosts are not treated as proof.
- **Final action and condition:** As written.
  - Tiers: confirmed exported (80); accessible, export unverified (up to 18,000); unknown (data outside the workspace).
  - Five parallel workstreams: session reconstruction, outbound volume test, workspace inventory, window and logging coverage, other routes.
  - The estimate stays provisional until Q07b confirms the access window is closed.
  - SEC does not solicit samples from the attacker.
- **Accountable owner:** SEC. Executing: bank forensic staff, external forensic firm, Security Operations Centre, network operations, workspace data owner, the vendor for its records.
- **HKT time or trigger:** Scope statement version 1 at 12:30; version 2 at 15:00; version 3 at 18:00; then daily. Any evidence that raises the estimate is reported within 30 minutes.
- **Recipient and channel:** Me, LC and the privacy officer, by out-of-band bridge and the restricted incident workspace. The statement holds no personal data. COM receives approved figures only.
- **Final external basis:** SEC Q07a "Basis", unchanged. Anchors re-read:
  - R16b, PDF p.2, "Controls for handling incidents involving loss or leakage of customer data": "ascertaining the nature of the incidents, the causes of the incidents and identity of customers affected".
  - R11, p.4, Step 1: "How many data subjects might be affected?".
  - R11, p.8: "regardless of the progress of any internal investigation".
  - The scoping method and tiers are professional judgment; SEC's "No direct rule located" search record stands.
- **Final internal basis:** N/A (PH01 absent).
- **Dispatch instruction:** EXECUTE NOW. Dependency: vendor session records under C02; Q07b closure time.

### Q07b

- **Original answer reference:** SEC sealed answer, C03, Q07b.
- **CONFIRM.**
- **Reason:** Disabling an account does not end sessions or tokens already issued, so closure has to be proved by test. A session that can still reach 18,000 customers' records is not left open for availability or recovery. The 10-minute capture first shows what to terminate and what was touched.
- **Final action and condition:** As written.
  - Step 1: capture session, token and key state as evidence (capped at 10 minutes).
  - Steps 2-4: terminate every session on each layer; revoke tokens, keys and registrations; disable the account and all other accounts of this vendor; block the vendor path.
  - Step 5: rotate secrets the session could read, after a dependency check.
  - Step 6: remove persistence, recorded as evidence first.
  - Step 7: the vendor preserves, then ends its sessions and rotates its credentials.
  - Stop triggers and reinstatement conditions as written. No vendor access returns without SEC sign-off.
- **Accountable owner:** SEC. Executing: Security Operations Centre, identity and privileged access administrators, platform owners, network operations, forensic staff, the vendor on SEC instruction.
- **HKT time or trigger:** Step 1 12:00-12:10; Steps 2-4 by 12:20; replay and logon tests by 12:30 with closure time reported; rechecks 13:30 and 16:30; rotation plan 14:00, complete 18:00. Any use of the identity after Step 3 is treated as active intrusion.
- **Recipient and channel:** Identity, privileged access and perimeter systems, by emergency change record and out-of-band bridge. The vendor through the verified C02 contact. Closure time to me and LC.
- **Final external basis:** SEC Q07b "Basis", unchanged. Anchors re-read:
  - R10 Cap. 486, Schedule 1, Principle 4(1), p.169: "protected against unauthorized or accidental access, processing, erasure, loss or use".
  - R03 s.6.2.13(b), p.14: "promptly changed if they have been or are suspected of being compromised".
  - R11, p.5: "Changing users' passwords and system configurations to block any (further) unauthorised access".
  - R08 TM-G-1 paras 4.3.2-4.3.3, pp.19-20.
  - Extending these to sessions, tokens and keys is professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for Steps 1-4 and 7. SCHEDULE the rotation. HOLD on any reinstatement of vendor access.

### Q08a

- **Original answer reference:** LC sealed answer, C03, Q08a.
- **CONFIRM.**
- **Reason:** A breach is confirmed for 80 people with identity card numbers, so there is a real risk of harm. The guidance says to notify without waiting for the investigation. LC describes the status correctly: a voluntary notification under guidance, not a statutory report, and no admission of a contravention.
- **Final action and condition:** As written.
  - LC files the Privacy Commissioner's Data Breach Notification Form (R16a) as a new notification.
  - It states 80 confirmed, up to 18,000 in the same workspace with export unverified, the three data types, and awareness (suspected 09:30, confirmed 12:00).
  - It says a vendor support credential was used and the vendor's role is under review.
  - Notification and media status are answered as they stand at filing.
  - No customer list is attached, and there is no mention of any Cap. 455 disclosure.
  - Updates are filed when scope, numbers or notification status change.
- **Accountable owner:** LC (or the data protection officer, if separate, signs). SEC supplies the verified facts. I am informed, not asked to approve.
- **HKT time or trigger:** Awareness of the confirmed breach 12:00. Clock "as soon as practicable"; no hour figure in the sources. Target: submitted by 14:00, just before the public update.
- **Recipient and channel:** Office of the Privacy Commissioner for Personal Data, in writing only. Email to the form's address if SEC confirms corporate email is safe; otherwise fax or hand delivery.
- **Final external basis:** LC Q08a "Basis", unchanged. Anchors re-read:
  - R16a, p.1: "Although it is not mandatory under the Ordinance for data users to give data breach notifications, data users are encouraged to give such notifications timely".
  - R11, p.6, Step 4: "notify the PCPD and the affected data subjects as soon as practicable after becoming aware of the data breach".
  - R11, p.8: "Oral notifications are not accepted."
  - R16b, p.3: "the AI concerned should seriously consider doing so".
  - Authority: R16a and R11 are non-binding regulator material; R16b is an HKMA supervisory circular.
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE for 14:00 at the latest. Dependencies: SEC's export timestamp, COM's notification figures and media status, a safe written channel.

### Q08b

- **Original answer reference:** LC sealed answer, C03, Q08b.
- **CONFIRM.**
- **Reason:** The 80 have verified exposure of sensitive data and should hear today. For the wider group, a notice now could be wrong, and the individuals are not yet listed. The fixed 18:00 checkpoint and the six expansion events stop the hold drifting.
- **Final action and condition:** As written.
  - Notify now: the 80.
  - Under review: up to 18,000; SEC and COM build the contact list now.
  - Expansion events 1-6 as LC listed. If export cannot be ruled out by 18:00, or logs are incomplete, a precautionary notice to the whole workspace population is recommended to me.
  - Notice to the 80: cleared by LC, no full identity card number, and it covers what happened, which data, steps to take and a contact point.
  - LC asks the Police whether notification prejudices the investigation. This is not a hold unless the Police ask in writing.
- **Accountable owner:** LC for the scope recommendation and clearance. I decide the audience. COM sends. SEC supplies the list under controlled handling.
- **HKT time or trigger:** Awareness 12:00. Advice to me by 12:30; notices dispatched by 15:00 at the outside; scope checkpoint 18:00.
- **Recipient and channel:** The 80 individuals, by the direct channel COM selected, which lets them verify the bank is the sender.
- **Final external basis:** LC Q08b "Basis", unchanged. Anchors re-read:
  - R16b, p.3: "notify the affected customers as soon as practicable after the AI concerned is aware of or notified of the incident".
  - R16b, p.2: "it should provide justification on why it did not do so".
  - R05, PDF p.1, "Customer notifications" (checked against the scan): "customers affected or likely to be affected".
  - Treating the 18,000 as possibly, not yet likely, affected is judgment, which I share until 18:00.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the 80. HOLD on individual notices to the wider group until an expansion event or the 18:00 decision.

### Q09a

- **Original answer reference:** COM sealed answer, C03, Unit Q09a.
- **CONFIRM.**
- **Reason:** COM's independent recommendation matches LC's and my audience decision: send to the 80, time-box the wider group. The attacker holds these customers' names, identity card numbers and phone numbers. The contact therefore has to be one they can verify and a fraudster cannot easily copy.
- **Final action and condition:** As written.
  - SEND to the 80: personal call from a dedicated senior team, written notice in the authenticated secure inbox within the hour, couriered letter for those without digital access or not reached after two attempts.
  - No SMS or email carrying a link.
  - Call script and notice wording as drafted.
  - The password sentence is used only if SEC confirms the field list is complete.
  - "have reported" is used only for each body LC confirms was notified by send time.
  - Hold conditions 1-4 stand; condition 1 is met by my decision above.
  - HOLD on the wider group, with the precautionary notice pre-staged.
- **Accountable owner:** COM. Audience decision: me. Fact check: SEC. Clearance: LC. Executing: head of branch network, digital channels team, contact-centre head.
- **HKT time or trigger:** 12:10 requests; calls and notices from 12:45; first attempts complete 14:00; second attempts and letters 16:00; wider-group decision 18:00, with precautionary notices by 20:00 if the trigger is met.
- **Recipient and channel:** The 80 customers by phone, secure inbox and letter. Copies and call outcomes to LC and the dispatch log.
- **Final external basis:** COM Q09a "Basis", unchanged. Anchors re-read:
  - R11, p.8, "How to notify?": "The data subjects can be notified directly by phone, in writing, via email or in person."
  - R11, p.7: "A list of the types of personal data involved" and "Information and advice on the actions the data subjects can take to protect themselves".
  - R16b, p.3 (as quoted under Q08b).
  - Channel choice and the time-box are professional judgment; COM's search record stands.
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE the send for 12:45. Dependencies: SEC's 12:30 statement (the 80, export time, fields, inbox trusted), LC clearance, Operations monitoring in place. If SEC cannot confirm the inbox, COM brings that to me at once.

### Q09b

- **Original answer reference:** COM sealed answer, C03, Unit Q09b.
- **CONFIRM.**
- **Reason:** The text separates what is confirmed from what is not, and gives protective advice. It avoids "only 80", "no evidence" and any containment claim. Stating the 18,000 figure is the honest course: regulators are given it, and the wider group cannot yet be told individually.
- **Final action and condition:** As written.
  - Public update in COM's wording, with the figure.
  - No mention of the vendor, the credential, the demand or attribution.
  - Release conditions 1-4 stand, including that the first round of calls to the 80 is complete.
  - "have reported" for the Privacy Commissioner only once LC confirms the form is submitted.
  - Release is brought forward if the attacker publishes or a news outlet is about to report.
  - A copy goes to the HKMA through LC at or just before release.
- **Accountable owner:** COM. Approver: me. Clearance and HKMA copy: LC. Fact check: SEC and Operations.
- **HKT time or trigger:** 12:15 draft to SEC and LC; 13:30 Frontline Instruction No. 3; 14:00 target release; 14:30 latest; 18:00 next update.
- **Recipient and channel:** Website homepage and newsroom, press release by email, verified social media accounts, app and internet banking notice, branches and contact centre. HKMA copy via LC.
- **Final external basis:** COM Q09b "Basis", unchanged. Anchors re-read:
  - R16b, p.3: "If a large number of customers are affected, the AI concerned should consider making a public announcement".
  - R05, PDF p.2, "Public announcement" (checked against the scan): "should include the key facts of the incident".
  - R05, PDF p.3: "copies of public communication materials should be submitted to the HKMA for reference".
  - No direct rule located on publishing the size of an unverified set; that is professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE for 14:00, latest 14:30. Dependencies: first call round complete, LC's form filed, SEC's factual lines, my approval (given).

---

### Order of dependent actions on this card

1. **12:00-12:20:** SEC captures session and token state, then terminates sessions, revokes tokens and disables the vendor's accounts. I brief the Board.
2. **12:15:** LC telephones the HKMA with the privacy-incident update; written confirmation by 13:00.
3. **12:30:** SEC issues scope statement version 1 and the closure time. LC's audience advice reaches me and my decision is logged. LC files the justification for the wider hold.
4. **12:45:** COM's call team starts on the 80 and posts the secure inbox notices.
5. **13:30:** COM issues Frontline Instruction No. 3.
6. **By 14:00:** First call attempts complete. LC files the Privacy Commissioner form.
7. **14:00 (latest 14:30):** COM releases the public update. LC copies the HKMA.
8. **15:00:** SEC's version 2, including the exact workspace list.
9. **16:00:** Second call attempts complete; letters go out.
10. **Today:** LC sends the interim update to the Commissioner of Critical Infrastructure through the secure channel.
11. **18:00:** SEC's version 3; my wider-group decision; LC updates the Privacy Commissioner and HKMA; COM's public update; rotation complete.
12. **By 20:00:** Precautionary notices to the wider group if the trigger is met.

### Still unverified at this card

Export of the wider set; the fields held for it; data outside the workspace; how the vendor credential was obtained; whether the access window is closed; whether the vendor processes personal data for the bank.

### My search record

- R10, regex "data breach notification|notify the Commissioner|mandatory": 3 hits (pp.14, 14, 120), all in the name of the Mandatory Provident Fund legislation. None creates a breach-notification duty, which supports LC's "voluntary" description.
- Limitation: R10 is the version dated 2022-10-01; any later amendment is not in the manifest. The vendor contract and the bank's data breach response plan are also absent.