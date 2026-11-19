## CEO final decisions, C05 (Tuesday 17 November 2026, 08:00 HKT, H+24)

All six units are CONFIRMED; there are no overrides. I re-read the citations in the three sealed answers against the source pages and found them accurate. PH01 is not in the manifest ("PH01", all documents: 0 hits), so the internal basis is N/A throughout.

All actions below are simulated, for the facilitator to log.

### My own decisions that the sealed answers asked for

- **Payment posture:** maintained. The handoff cannot verify the 23:00 review or the Board's confirmation, so I record my review now at 08:00 and ask the Board chair for a minuted confirmation by 10:00. No attacker contact.
- **Notification audience today:**
  - the 240 newly verified customers, by direct notice;
  - the original 80, with a follow-up that the file is now public;
  - the rest of the wider group, with the precautionary notice or an update by 12:00. The 320-record file removes the ground for withholding it.
- **Wording:** the revised notices are approved. The 11:00 public update with the 320 figure is approved in principle; COM shows me the text first.
- **Scam alert:** approved for 08:30 without the page address or account name.
- **Recovery:** the new build from the immutable backup is approved for testing only. Production stays my decision as crisis management team chair, after both SEC reports. No restoration time is published.
- **Removal requests:** these go to platforms and hosting providers only. Nobody writes to whoever posted the file; that would be attacker contact.
- **Support offer for the 320 (for example identity-protection cover):** not in the notice. The proposal deferred at C03 comes to me by 12:00.

### Conflicts between sealed answers, resolved within their stated branches

1. **List of the 240.** COM needs it by 08:40; SEC promises only a delivery time by 09:00. Calls to the 240 start on receipt, under COM's hold condition 1. Calls to any of the 80 with no logged contact start at 08:45 regardless. If the list is not in by 10:00, COM brings the 11:00 public update to me; I will not hold a public warning behind a list.
2. **Secure inbox.** SEC's confirmation was never recorded. COM's stated fallback applies: without it by 08:40, the written notice goes by couriered letter the same day.
3. **Who lodges removal requests.** SEC and the fraud team lodge the platform and host requests for the fake page before 08:30, so the alert's removal sentence is true. LC takes the Police and Privacy Commissioner routes for the public file.
4. **Alert's reporting sentence.** LC's Police report is due by 09:00 and the HKMA report follows release. At 08:30 the bracket names only bodies LC confirms, so it is likely left out and added when the alert is repeated.
5. **Same numbers everywhere.** LC's HKMA update goes first, then LC's Privacy Commissioner update by 10:00, then COM's public update at 11:00, all using 320.
6. **Vendor logs to the Police.** LC would inform the vendor. I ask LC to raise with the Police what the vendor is told; this is not a hold on the evidence.

---

### Q13a

- **Original answer reference:** SEC sealed answer, C05, Q13a.
- **CONFIRM.**
- **Reason:** A new build from trusted media plus the immutable backup is the only candidate that depends on nothing the attacker could reach. The backup is "pre-incident" only relative to the encryption; the attacker's first access may be earlier, so the date test decides how much of it is used. A pass is not a production approval.
- **Final action and condition:** As written.
  - Test candidate A in an isolated recovery environment.
  - The standby gateway is second choice only if A fails, under the same checks.
  - The original gateway is not repaired in place; it stays under evidence hold.
  - The secondary process continues as the interim service.
  - Integrity checks 1-8: provenance, date test, clean build, scan, baseline, entry route closed, synthetic function test, independent review.
  - Separation checks on network, identity, management and data path.
  - If the backup cannot be dated before first access, only data is restored from it.
  - Stop triggers as written.
- **Accountable owner:** SEC for candidate selection, criteria and the test report. Executing: IT Operations and backup team, forensic staff, an independent reviewer, the payments information owner. Production decision: the crisis management team.
- **HKT time or trigger:** Provenance and date test by 09:00; environment built and separation verified by 11:00; restore and checks 3-6 by 15:00; functional test by 16:30; report by 17:00. Later times depend on restore duration, which is unknown.
- **Recipient and channel:** The isolated recovery environment, under an emergency change record. Test report to me, the information owner, LC and IT Operations through the restricted incident workspace.
- **Final external basis:** SEC Q13a "Basis", unchanged. Anchors re-read:
  - R08 TM-G-1 para 4.2.4, p.18 (reached through R03 s.6.2.16(a), p.15): "only properly tested and approved systems are promoted to the production environment".
  - R03 s.6.2.20(b)(i), p.17: "implement a secure tertiary data backup (STDB)".
  - R02 s.6.2.20(a), p.18: "Backup restoration tests should be conducted regularly without affecting the production environment."
  - R14b, p.5: "setting up dedicated environments and utilities for recovery" (good practice).
  - Candidate choice, date test and separation checks are professional judgment; SEC's "No direct rule located" search record stands.
- **Final internal basis:** N/A (PH01 absent).
- **Dispatch instruction:** EXECUTE NOW for the test. HOLD on any production use.

### Q13b

- **Original answer reference:** SEC sealed answer, C05, Q13b.
- **CONFIRM.**
- **Reason:** A restored system knows nothing after the backup time. The two risks are paying again what has settled and losing what has not. The ten checks close both before anyone proposes production, and the stated limits stop an offline pass being read as proof of live readiness.
- **Final action and condition:** As written.
  - Reconciliation runs offline on hashed extracts; nothing is posted or sent.
  - Ten checks: baseline, gap period, secondary-process items, queue tie-out, three-way match, replay protection, sequence numbers, static data, settlement position, dry run.
  - Pass means no unexplained difference; "unknown" gap items stay held.
  - Sign-off by maker and checker, independent review, SEC attestation and the payments information owner.
  - Before any cut-over: a final delta reconciliation, the secondary process kept as fall-back, and a live test afterwards.
- **Accountable owner:** SEC for check design and integrity attestation. Executing: payments operations and finance, IT Operations, independent reviewer, payments information owner.
- **HKT time or trigger:** Check design by 09:00; extracts by 12:00; checks 15:00-20:00; report by 21:00. All conditional on the candidate passing Q13a. Trigger: no production proposal without a signed report showing all ten checks passed.
- **Recipient and channel:** Reconciliation workspace in the isolated environment. Report to me, the information owner and LC through the restricted incident workspace.
- **Final external basis:** SEC Q13b "Basis", unchanged. Anchors re-read:
  - R09 TM-E-1 para 5.1.2, p.19: "reconcile data file balances after transaction updates".
  - R14b, p.2: "reconciliation procedures to maintain accuracy following a bypass".
  - R09 Annex B, p.40, items B.2 and B.3: "well-tested fall-back procedures" and "Live test".
  - The ten checks and pass conditions are professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE, dependent on a Q13a pass. HOLD on production.

### Q14a

- **Original answer reference:** LC sealed answer, C05, Q14a.
- **CONFIRM.**
- **Reason:** The data is public, so payment can no longer buy anything. None of the legal checks is cleared. The handoff shows no contact, offer, promise or payment, so there is no commitment to honour or withdraw.
- **Final action and condition:** As written.
  - "Do not pay" is maintained; the hold on preparatory steps and the ban on contact stay.
  - LC reconfirms the Treasury and Finance hold in writing.
  - Reviews are daily and on events: backup test result, wider-set verification, a new demand, a Police view.
  - The HKMA is told before any change.
  - Written confirmations of no contact and no promise are collected from Treasury and Finance, SEC, COM, the vendor and any adviser or insurer.
  - If an unrecorded commitment surfaces, it is unauthorised and not performed. No message goes to the attacker; the facts go to the Police and the Board.
  - SEC checks whether the demand names a wallet address. If it does and no Cap. 455 disclosure is on file, the disclosure officer makes it today.
- **Accountable owner:** LC for the advice. The Board for any departure. I hold the operating posture. The disclosure officer for any Cap. 455 disclosure.
- **HKT time or trigger:** Review recorded 08:00; advice note 08:30; Board confirmation and written confirmations by 10:00.
- **Recipient and channel:** Me and the Board chair, by telephone bridge and written note. Hold reconfirmation to Treasury and Finance.
- **Final external basis:** LC Q14a "Basis", unchanged. Anchors re-read:
  - R16c Cap. 455 s.25A(2)(a), p.83: "he does that act with the consent of an authorized officer".
  - R16d Cap. 575 s.8(a), p.20.
  - R06 OR-2 para 3.4, p.6.
  - R02 s.7.2.3(a)(v)(4), p.32: "actions taken and decisions made".
  - No direct rule located on ransom payment or commitments to an attacker; the posture is professional judgment bounded by the two statutes.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW. HOLD on any payment, preparatory step or contact.

### Q14b

- **Original answer reference:** LC sealed answer, C05, Q14b.
- **CONFIRM.**
- **Reason:** Publication of 320 customers' data and a fake page trading on the incident are new criminal matters. The guidance expects a Police report for the fake page. The 16 November report has no verified reference, so today's report must be able to stand as the formal referral. Sending hash-verified copies under custody keeps the originals usable.
- **Final action and condition:** As written.
  - Police: obtain the 16 November reference; lodge a supplementary report covering the intrusion and demand, the export and public file, and the fake page as a possibly separate actor.
  - Privacy Commissioner: refer the public file and update the breach notification to 320 verified.
  - Ask the Police for their view on payment and contact, and for help with removal.
  - Evidence now: timeline, demand with metadata, sample and match report, export logs, gateway logs and images, credential and session records, capture details for the public file and the fake page.
  - With limits: customers' full identities only on Police request; vendor session logs.
  - Withheld: privileged advice, information from the Commissioner's office about other parties, the fact of any Cap. 455 disclosure.
- **Accountable owner:** LC for the referral and evidence schedule. SEC prepares and hands over evidence. I am informed, not asked to approve.
- **HKT time or trigger:** Reference check by 08:30; supplementary report by 09:00; Privacy Commissioner referral by 10:00; first evidence tranche by 12:00; the rest as imaging completes.
- **Recipient and channel:** Police (the handling officer or the cyber crime bureau), by written report and hand-delivered encrypted media against a signed receipt. Privacy Commissioner in writing. The Police channel is judgment; no rule located.
- **Final external basis:** LC Q14b "Basis", unchanged. Anchors re-read:
  - R09 para 4.3.2, p.17: "report the matter to the Hong Kong Police Force".
  - R11, p.4: "Notifying the relevant law enforcement agencies if identity theft or other criminal activities have been or are likely to be committed".
  - R10 Cap. 486 s.64(1), p.130: "obtained from a data user without the data user's consent".
  - R10 s.58(2), p.119.
  - R02 s.7.2.3(a)(v)(2), p.32.
  - No direct rule located mandating a Police report for the intrusion; that referral is professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the reports. SCHEDULE the 12:00 evidence tranche. Dependency: SEC's captures and custody log.

### Q15a

- **Original answer reference:** COM sealed answer, C05, Unit Q15a.
- **CONFIRM.**
- **Reason:** The 240 have verified, public exposure and must hear today. The original 80 face a changed risk and need a follow-up. COM rightly treats "approved" and "delivered" as different, so nobody is told "as we said yesterday" when the record cannot show it.
- **Final action and condition:** As written.
  - Reconcile the 16 November call and inbox records first.
  - The 240: personal call, written notice in the secure inbox (or couriered letter), no SMS or email with a link, in COM's wording.
  - Data types are stated per customer only as SEC confirms them.
  - The original 80: follow-up notice; full first notice to anyone with no logged contact.
  - Rest of the wider group: a short update if the precautionary notice was sent; the notice itself with revised figures if not.
  - No notice says where the public copy is.
  - "have updated" and "working to have the file removed" are used only on LC's or SEC's confirmation.
  - Hold conditions 1-5 stand; condition 3 is met by my approval above.
- **Accountable owner:** COM. Audience: me. Fact check: SEC. Clearance and regulator update: LC. Executing: branch network head, digital channels team, contact-centre head.
- **HKT time or trigger:** 08:10 requests; 08:40 reconciliation and SEC confirmations due; 08:45 calls begin; 10:00 follow-up to the 80; 11:00 first attempts complete and public update; 12:00 wider-group notice or update; 13:00 second attempts; 14:00 letters.
- **Recipient and channel:** The 240 and the 80 by phone, secure inbox and letter. The wider group by secure inbox with a push or SMS alert carrying no link, and letters for non-digital customers.
- **Final external basis:** COM Q15a "Basis", unchanged. Anchors re-read:
  - R11, p.6, Step 4: "notify the PCPD and the affected data subjects as soon as practicable".
  - R11, p.5: "online data leakage is difficult to be effectively contained".
  - R16b, p.3: "notify the affected customers as soon as practicable after the AI concerned is aware of or notified of the incident".
  - No direct rule located on follow-up notices or unverified earlier delivery; that is professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE from 08:45. Dependencies: SEC's list and data types, the reconciliation, the inbox answer, LC clearance.

### Q15b

- **Original answer reference:** COM sealed answer, C05, Unit Q15b.
- **CONFIRM.**
- **Reason:** A positive rule ("the bank has no verification page") still works when the scammers change address, and publishing the address would send people to it. Speed matters more than a combined statement, and the alert needs none of the data facts still being checked.
- **Final action and condition:** As written.
  - Standalone scam alert in COM's wording: no address, account name, screenshot, link or scannable code.
  - An original pinned post on verified accounts; no reply to, quote or tag of the fake account.
  - Full address and account details go only to the platform, the hosting provider, the Police and the HKMA.
  - Staff Instruction No. 5 goes out at the same time.
  - A priority hotline option for anyone who entered details, so the account can be suspended at once.
  - The warning is repeated in every Q15a notice and in the 11:00 update.
  - Fallback if LC or the HKMA require the address: broken, non-clickable text.
- **Accountable owner:** COM. Approver: me. Clearance and Police and HKMA reports: LC. Removal requests: SEC and the fraud team. Hotline option: contact-centre head.
- **HKT time or trigger:** 08:15 draft to LC and SEC; 08:30 alert and staff instruction; LC's HKMA report immediately after release.
- **Recipient and channel:** Website security banner and log-in page, app notice and push with no link, recorded hotline message, branch notices, verified social media accounts, press release, SMS with no link to the likeliest targets.
- **Final external basis:** COM Q15b "Basis", unchanged. Anchors re-read:
  - R09 para 4.3.2, pp.16-17: "AIs should make attempts to remove the fake or suspicious items where practicable."
  - R09 footnote 12, p.17: "report the cases to the HKMA immediately after the press releases are issued".
  - R09 para 4.4.3, p.18: "a mechanism for customers to promptly suspend their e-banking accounts".
  - No direct rule located on withholding the fake address; that is professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE for 08:30. Dependencies: removal requests lodged first, LC clearance.

---

### Order of dependent actions on this card

1. **08:00:** I record the posture review. LC's scheduled HKMA update carries the public file, the 320 figure, the fake page and the unchanged posture.
2. **08:10-08:30:** COM sends its requests and starts the reconciliation. SEC blocks the fake page on bank networks; SEC and the fraud team lodge removal requests. LC asks SEC about a wallet address and seeks the Police reference.
3. **08:30:** COM releases the scam alert and Staff Instruction No. 5; LC reports to the HKMA straight after. LC's advice note and hold reconfirmation go out.
4. **08:40:** Reconciliation complete; SEC's inbox answer due.
5. **08:45:** Calls start to any of the 80 with no logged contact, and to the 240 on receipt of SEC's list.
6. **By 09:00:** LC lodges the supplementary Police report. SEC completes the backup provenance and date test and agrees the reconciliation design.
7. **By 10:00:** Board confirmation and written confirmations collected. LC's referral and updated notification go to the Privacy Commissioner. COM posts the follow-up to the 80.
8. **11:00:** First call attempts complete; COM's public update with the 320 figure; LC copies the HKMA. SEC confirms separation of the recovery environment.
9. **12:00:** Wider-group notice or update; first evidence tranche to the Police; reconciliation extracts ready; support-offer proposal to me.
10. **13:00-14:00:** Second call attempts; letters dispatched.
11. **17:00:** SEC's candidate test report.
12. **21:00:** Reconciliation report. Only then can a production proposal come to me.

### Carried open item (no unit changed)

Bringing a rebuilt gateway into service may be a notifiable material change under R01 s.22 (basis quoted at C04). LC assesses it with SEC's technical description before any production decision.

### Still unverified at this card

The Board's confirmation and the 23:00 review; the Police reference and view; whether a Cap. 455 disclosure was made; delivery of yesterday's notices; whether the secure inbox is trusted; the data types for the 240 and whether they sit inside the workspace list; the 18,000 claim; the backup's date against the attacker's first access; who runs the fake page and whether any customer entered details.

### My search record

- Regex "take.?down|removal request|cached links|remove the fake", all documents: 3 hits (R09 p.17; R11 pp.4, 7). None says who may be asked to remove content, so the "not the poster" rule is judgment tied to the no-contact decision.
- Regex "immutable|tertiary data backup|STDB", all documents: 12 hits (R02 p.18; R03 p.17; R04 p.8; R14b p.5). None sets a test method for a restored backup.
- Limitation: the bank's recovery plan, the industry backup guideline R03 cites and backup system records are not in the manifest.