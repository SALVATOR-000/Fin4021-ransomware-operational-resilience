## CEO final decisions, C08 (Thursday 19 November 2026, 08:00 HKT, H+72)

Five units are CONFIRMED and one is OVERRIDDEN (Q24a, one sentence only). I re-read the citations in the three sealed answers against the source pages and found them accurate. PH01 is not in the manifest ("PH01", all documents: 0 hits), so the internal basis is N/A throughout.

All actions below are simulated, for the facilitator to log.

### My own decisions that the sealed answers asked for

- **Production: hold continues.** The second test is progress towards gate condition 2, not a pass. None of the nine conditions is recorded as met, so I sign nothing. No restoration date is given.
- **Handover:** approved, from crisis handling to managed recovery under the standing teams. Decision rights are unchanged, and the crisis management team reconvenes on any SEC trigger. I chair one handover meeting at 10:00 for all three packs.
- **Two overdue SEC results are closed first today:** the verified state of the secondary process and its seven gates, and the classification of the C07 indicator with its time. Both go to LC and COM at once.
- **Remediation decision (COM needs it in writing before handing on the promise list).** This is professional judgment; R05 p.1 expects the bank to say whether it will reimburse losses.
  1. Bank fees and charges caused by the disruption are waived (already approved).
  2. Documented direct losses caused by the payment disruption, including missed payroll cut-offs, will be reimbursed on claim. I approve the principle; the Board minutes the budget by 20 November.
  3. Unauthorised transactions are handled on the R09 para 4.4.4 position, in wording LC confirms.
  4. Scam losses where the customer made the payment are assessed case by case by the head of fraud with LC. No blanket promise.
  5. The 320 customers are offered an identity-protection or credit-monitoring service at the bank's cost for 12 months, on opt-in, once LC clears the provider terms.
  - Staff wording changes only when LC has cleared it. Until then COM's "cannot promise" wording stays.
- **Vendor:** access stays disabled. The retain-or-exit decision comes to me by 18 December.

### Conflicts between sealed answers and how I resolved them

1. **Three handover meetings.** SEC and COM each set 10:00 and LC sets "today". There is one meeting at 10:00; acceptances follow as each role wrote.
2. **LC's 12:00 register needs inputs due at the same time.** COM brings its commitments register in draft to the 10:00 meeting. SEC's dates are already in its sealed table.
3. **Two statutory items SEC flags are not on LC's list.** I add both to LC's register as standing entries (basis under Q23a). No LC action, date or recipient changes.
4. **Queue figures in the public update.** COM's text has placeholders "supplied by Operations". The decision record cannot verify the secondary process's activation or releases. This is the one override (Q24a).
5. **Forensic firm's data.** The C06 terms say delete on completion; LC's hold now preserves. The firm deletes nothing until LC releases it.
6. **Indicator classification and the statutory clock.** If SEC has reached reasonable certainty of a separate incident, LC's 12-hour clock is already running. SEC records the classification and its time first thing.

---

### Q22a

- **Original answer reference:** SEC sealed answer, C08, Q22a.
- **CONFIRM.**
- **Reason:** A sample of 240 on an offline image, run on an access environment that production does not have, shows progress and nothing more. Six alarm-free hours is far short of the seven clean days set at C07, and the indicator is not classified. With no gate condition recorded as met, releasing anything would rest on results nobody can show.
- **Final action and condition:** As written.
  - Keep every restriction: gateway isolation, evidence hold, standby gateway hold, vendor accounts disabled and path blocked, recovery hold with the nine-condition gate, secondary process as the only service mode, mobile transfer submission closed, raised monitoring.
  - Stop and rollback criteria carry over.
  - Hourly status to me may move to four-hourly only once the indicator is recorded as an old artefact or unrelated, on a change record.
  - Handover pack of nine items, including the gate status sheet and the open verification list of every result no card records.
  - The evidence register and sealed masters stay with the SEC evidence custodian.
  - Until receiving owners sign, the incident team keeps responsibility.
- **Accountable owner:** SEC stays accountable for the security conditions and stop authority. Receiving owners: head of IT Operations, Security Operations Centre manager, payments operations lead. Gate decision: me.
- **HKT time or trigger:** 08:00 review concluded "retain"; 09:00 pack issued; 10:00 walkthrough and signed acceptance; 18:00 first status from the standing team. Gate review only when conditions 1-7 and 9 are recorded.
- **Recipient and channel:** Handover pack in the restricted incident workspace; acceptance recorded in the incident log and the problem management record.
- **Final external basis:** SEC Q22a "Basis", unchanged. Anchors re-read:
  - R08 TM-G-1 para 4.2.4, p.18 (through R03 s.6.2.16(a), p.15): "only properly tested and approved systems are promoted to the production environment".
  - R08 para 5.1.3, p.20: "keep track of all these incidents until rectification of the incidents".
  - R07 TM-G-2 para 4.2.2, p.10.
  - R03 s.6.2.26(a), p.19.
  - No direct rule located on handover or on criteria for releasing restrictions; that is professional judgment.
- **Final internal basis:** N/A (PH01 absent).
- **Dispatch instruction:** HOLD on every release and on production recovery. EXECUTE NOW for the pack and the two overdue results. SCHEDULE the 10:00 walkthrough.

### Q22b

- **Original answer reference:** SEC sealed answer, C08, Q22b.
- **CONFIRM.**
- **Reason:** Use of the vendor credential is the route, not the cause; how it was obtained is still unknown. Remediation can start on confirmed contributing factors, marked provisional. Closure must rest on recorded evidence, because much of what was done on 16 November cannot be shown.
- **Final action and condition:** As written.
  - The issue stays open and vendor access stays disabled.
  - Remediation is assigned across eleven areas: root cause analysis; vendor and privileged access redesign; review of other vendors; data placement; vendor contract and oversight; logging and clocks; detection; recovery readiness; incident records; independent assurance; post-incident review.
  - Closure needs all twelve evidence items: cause; identity; session reconciliation; closure proof; no further use to the end of the 30-day watch; secrets rotated; persistence removed and indicator classified; extent across this and other vendors; new access design independently tested; vendor's data holdings; contract and assurance; sign-off.
  - Closing the issue releases no evidence.
  - Any use of a revoked identity reopens it as active intrusion.
- **Accountable owner:** SEC. Executing: the named remediation owners (role names assumed by SEC); the vendor for items 1, 3 and 10. Sign-off: SEC, the payments information owner and me, after internal audit review.
- **HKT time or trigger:** Preliminary root cause 25 November, final 18 December; other-vendor review, data placement and logging by 3 December; contract, detection, recovery readiness and post-incident review by 18 December; end of the 30-day watch 16 December; access redesign before any reinstatement.
- **Recipient and channel:** Remediation register held by the standing operations team in the problem management record; closure file in the evidence repository; summary to me and LC.
- **Final external basis:** SEC Q22b "Basis", unchanged. Anchors re-read:
  - R02 s.7.2.3(i), p.33: "The post-incident review should incorporate lessons learned".
  - R06 OR-2 para 8.3, p.13: "Root cause analysis of incidents".
  - R13, p.3: "a clear risk-based framework for determining the timeline and priority of remediations".
  - R03 s.6.2.13(b), p.14.
  - R08 para 3.2.1, p.12.
  - R16b Annex C(vii), p.5.
  - The twelve items, periods and dates are professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the assignments. HOLD on vendor access and on closure until all twelve items are recorded and signed.

### Q23a

- **Original answer reference:** LC sealed answer, C08, Q23a.
- **CONFIRM.**
- **Reason:** The statutory and supervisory duties run past the exercise window, and several are unproven on the record. Legal and Compliance is a standing function, so ownership does not move. The most urgent item is correctly identified: if only the 18 November filing can be evidenced, the written record was up to five hours late.
- **Final action and condition:** As written, with two register entries added from SEC's sealed answer.
  - Open actions as LC lists: which Annex E filing is evidenced; Annex F; the sector-specific form answer; indicator classification; supplementary material after Annex F; material-change assessment and filing; HKMA updates and confirmations; Privacy Commissioner proof, completion figures and misdelivery assessment; Police reference, receipt, remaining evidence and view; wallet-address check and any Cap. 455 disclosure; Board minutes and sight of Annex F.
  - If the written record was late: LC briefs me and the Board chair, keeps the evidence of the 16 November attempt, and holds the legal assessment as privileged.
  - Standing items: post-incident review; emergency response plan resubmission; forensic firm's data; vendor contract; any insurance notice.
  - Added: submission of a revised security management plan within one month of any revision; a possible written notice requiring a risk assessment after a notified change.
  - Register kept by a named LC deputy. Full version to LC, me and the disclosure officer. Operational version to the Board's committee, the security management unit's supervisor, the data protection officer, COM's lead, the head of standing operations and Internal Audit.
- **Accountable owner:** LC. Leads as in LC's table.
- **HKT time or trigger:**
  - Today 12:00: Annex E evidence established; register issued.
  - Annex F: submit 27 November; statutory limit 30 November 2026.
  - Material-change assessment by 30 November; filing by 16 December if material.
  - Board minutes by 20 November.
  - Register reviewed weekly until Annex F is filed, then monthly.
- **Recipient and channel:** Recipients as above, at the 10:00 handover meeting, with written acknowledgement from each.
- **Final external basis:** LC Q23a "Basis", unchanged. Anchors re-read:
  - R01 Cap. 653 s.28(4) and Schedule 6 item 3, pp.44, 97.
  - R01 s.22(1), p.33: "within 1 month after the date on which the event occurs".
  - R03 para 6.1.1, p.11.
  - R07 para 1.3.3, p.5: "until the final resolution of the crisis".
  - R16c Cap. 455 s.25A(1), p.83.
  - New basis for the two added entries: R01 s.23(4), p.36: "must submit the revised plan to the regulating authority that regulates the operator within 1 month after the date on which the revision is made"; R01 s.24(5), pp.37-38: "may, by written notice, require the CI operator". Authority: statute. The first applies only if remediation revises the plan; no notice under the second is recorded.
  - The register and its recipients are professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the Annex E evidence, the wallet-address check and the Police reference. SCHEDULE the register for 12:00 and the dated items above.

### Q23b

- **Original answer reference:** LC sealed answer, C08, Q23b.
- **CONFIRM.**
- **Reason:** Investigations by four authorities, possible claims and a statutory report are all live. Routine deletion would destroy what the bank may be required to produce. The release conditions also keep customer data from being held longer than the purpose needs, and each review is recorded.
- **Final action and condition:** As written.
  - A written legal hold overrides routine deletion, log rotation and backup recycling for systems in scope.
  - Preserved: forensic evidence and custody log; logs with the clock-offset record; attacker material; vendor material; decision records; regulatory and Police records; customer notification and case records; payment and reconciliation records; legal advice, kept separately as privileged.
  - Originals in write-protected storage with logged need-to-know access; personal data encrypted.
  - No in-scope system is re-imaged, decommissioned or returned to the vendor until imaged and released in writing by LC and SEC.
  - Written preservation requests go to the vendor and the forensic firm.
  - Release of a class of records needs all five conditions: no investigation or claim pending or expected; minimum retention run (six months for logs, so no earlier than mid-May 2027); limitation period for claims records; post-incident review and supplementary reporting complete; written approval by LC and the record owner.
  - Disposal by secure destruction with a certificate and custody entry. Incident-only copies of customer data are erased first once no longer needed.
- **Accountable owner:** LC owns the hold and its release. Custodians: SEC and the standing security team, the company secretary, COM, payments operations.
- **HKT time or trigger:** Hold confirmed by 10:00 today; inventory by 20 November; first review 18 December 2026, then quarterly; earlier on any closure notice from an authority.
- **Recipient and channel:** Written hold notice to each custodian, the vendor and the forensic firm, with acknowledgement.
- **Final external basis:** LC Q23b "Basis", unchanged. Anchors re-read:
  - R03 para 6.2.23(c), p.18: "The logs should be retained for a minimum period of 6 months."
  - R02 s.7.2.3(a)(v)(2), p.32: "preservation of evidence and chain of custody".
  - R10 Cap. 486, Schedule 1, Principle 2(2), p.167: "not kept longer than is necessary".
  - R10 s.26(1), p.58.
  - R01 s.35(1)(a), p.50.
  - Conditional: R16c s.7(1)(b), p.31; whether any production order exists is unknown.
  - Review dates and release conditions are professional judgment. The limitation period is not in the sources.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the hold notice. SCHEDULE the inventory and reviews. HOLD on any disposal.

### Q24a

- **Original answer reference:** COM sealed answer, C08, Unit Q24a.
- **OVERRIDE (one sentence only).**
- **Reason:** I keep COM's decision: no closing update, regular updates continue, one goes out now with the hold wording. I change the queued-payments sentence. The decision record cannot verify the secondary process's activation, pilot or releases, so the bank must not publish "sent" and "waiting" figures on an unverified basis. I also do not hold an update that is already more than a day overdue while figures are checked.
- **Final action and condition:**
  - Publish the status update in COM's common text with the Version 1 (hold) paragraph.
  - Changed sentence: the figures appear only if Operations supplies them from the instruction register and SEC has recorded the state of the secondary process. Otherwise the sentence reads: "Queued payments: we are checking the figures for queued instructions and will give them in our 18:00 update. Please do not re-submit."
  - Everything else as COM wrote:
    - the apology sentence only if the log shows no update after 07:00 on 18 November;
    - the customer-information paragraph on the dispatch-log check;
    - the compensation line and the fake-page warning;
    - no claim that all customers are notified, that the incident is over, or anything about the vendor or attribution.
  - Versions 2 and 3 only once Operations confirms the service is live.
  - A closing update is proposed to me only when COM's five criteria are all true.
  - Copy to the HKMA through LC.
- **Accountable owner:** COM. Approver: me, including for any later closing update. Fact check: SEC and Operations. Clearance and HKMA copy: LC.
- **HKT time or trigger:** 08:10 dispatch-log check and requests; 08:30 target release; 08:45 latest; 18:00 next update; from 20 November 08:00 and 18:00 daily until restoration, and at once on any change.
- **Recipient and channel:** Website status notice, app and internet banking notice, recorded hotline message, verified social media accounts, press release, branch notices.
- **Final external basis:** COM Q24a "Basis" for everything unchanged. Anchors re-read:
  - R09 TM-E-1 para 8.2.3, p.33: "if the AI does not have reasonable confidence that the service can be resumed in the near future".
  - R05, PDF p.3 (checked against the scan): "consistent and up-to-date messages are conveyed to all relevant parties on a timely basis".
  - For the changed sentence: No direct rule located in assigned sources on publishing operational figures that cannot be verified. Files: all. Terms: regex "payroll|salary|queued|backlog" (0 hits, run at C04). The change is professional judgment. A public statement is a "key fact" only if the bank can stand behind it, and the card says live status comes from the decision record.
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE for 08:30, latest 08:45. Dependencies: dispatch-log check, LC clearance, my approval (given for both forms of the sentence).

### Q24b

- **Original answer reference:** COM sealed answer, C08, Unit Q24b.
- **CONFIRM.**
- **Reason:** A signed acceptance against a list stops cases falling between teams. Listing the unevidenced items first is the honest way to hand over an incomplete record. Keeping references and channels unchanged avoids confusing customers while scammers imitate the bank.
- **Final action and condition:** As written.
  - Standing owners: head of fraud (scam cases); claims desk lead with head of SME banking (claims and payroll losses); data protection officer in LC (privacy matters); Corporate Communications (notification register, all wording, public updates and scam alerts); contact-centre and branch network heads (hotline, call-back, priority desks); head of payment operations (counterparty updates).
  - Pack: state of the record; case register; notification register; commitments register; approved wording; open decisions; dispatch log and call records under LC's hold.
  - No case transfers without a named handler and next-contact date.
  - A batch transfers as "open, delivery not evidenced" unless the register proves otherwise.
  - The remediation decision above is recorded before the promise list is handed on; staff wording changes only on LC's clearance.
  - No mass message about the handover. Planned messages go once each, on their triggers.
- **Accountable owner:** COM until each item is accepted. Receiving owners as above. Handover approved by me as crisis management team chair.
- **HKT time or trigger:** 09:00 open items checked; 10:00 handover meeting; 12:00 pack issued; 17:00 acceptances signed, with anything not accepted staying with COM and escalated to me; 17:00 on 20 November first standing summary to me and LC; 24 November communication facts to LC for the written report.
- **Recipient and channel:** Standing owners by the meeting and the written pack on the internal secure share. Customers through their existing case handler and channels. Registers and figures to LC.
- **Final external basis:** COM Q24b "Basis", unchanged. Anchors re-read:
  - R16b, p.2: "for overseeing the process of handling and reporting privacy incidents".
  - R11, p.6, Step 5: "A comprehensive record of the incident is therefore required".
  - R02 s.7.2.3(a)(v)(4), p.32.
  - Basis for my remediation decision: R05, PDF p.1 (checked against the scan): "whether the bank would reimburse any losses incurred by them and if so, how they can apply for compensation"; R09 para 4.4.4, p.18: "should not be responsible for any direct loss suffered by him or her as a result of unauthorized transactions". The terms themselves are professional judgment.
  - No direct rule located on handing customer cases to standing teams.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the open-item check. SCHEDULE the 10:00 meeting, 12:00 pack and 17:00 acceptances. Dependency: my remediation decision (given above).

---

### Order of dependent actions on this card

1. **08:00-08:30:** SEC records the secondary process's state and the indicator's classification, and tells LC and COM. COM checks the dispatch log.
2. **08:30 (latest 08:45):** COM releases the status update. LC copies the HKMA.
3. **09:00:** SEC's handover pack issued. COM checks open items with executing owners.
4. **By 10:00:** LC confirms the legal hold in writing.
5. **10:00:** One handover meeting. SEC's receiving owners sign acceptance. COM brings its draft commitments register.
6. **By 12:00:** LC and SEC establish which Annex E filing is evidenced. LC issues the register in two versions. COM issues its pack. The wallet-address check is closed.
7. **Today:** LC obtains the Police reference and updates the HKMA with the confirmations.
8. **17:00:** COM's acceptances signed; exceptions come to me.
9. **18:00:** Next public update; first status from the standing team.
10. **20 November:** Board minutes; inventory of held records; first Annex F draft; first standing case summary.
11. **25-27 November:** Preliminary root cause; checks; my approval and Board sight; Annex F submitted. Statutory limit is 30 November.
12. **3, 16 and 18 December:** Remediation items; end of the 30-day watch and any material-change filing; final root cause, vendor decision and first hold review.

### Still unverified at handover

Whether any of the nine gate conditions is met; the state of the secondary process and its gates; the indicator's classification; the C03 test, rotation and persistence-removal results; which Annex E filing is evidenced; receipt of every regulator contact; the Police reference and view; whether a Cap. 455 disclosure was made; delivery of every notification batch; case outcomes; the Board's 17 November decisions; how the vendor credential was obtained.

### My search record

- Regex "hand-?over|stand(ing)? down|post-incident|lessons learn", all documents: 7 hits (R01 p.93; R02 pp.32, 33, 33; R06 p.13, twice; R11 p.3). None sets handover terms or says when incident updates may stop.
- Limitation: the bank's plans, retention schedule, vendor contract and the Monetary Authority's material-change form are not in the manifest.