LC SUBMISSION – C04 (Mon 16 Nov 2026, 18:00 HKT, H+10) – Units Q11a and Q11b
Locked before I see colleagues' answers. All actions are simulated, for the facilitator to log. I relied on the facilitator's C04 handoff of the dispatch records from C01–C03 and on the C04 facts.

New facts at this card:
- The gateway is still impaired.
- About 4,200 payment instructions are queued, independently measured, including time-sensitive SME payroll.
- A secondary process can run up to 400 verified instructions an hour, if approved. It has not been approved and no BCP activation is recorded.
- Some customers retried transfers after a timeout.
- Call volumes have doubled, and some customers cannot reach a branch.

==================================================
UNIT Q11a – Review of the Commissioner (Cap. 653 s.28) record and next action
==================================================
What the record shows
1. Telephone notification on the verified CI route by 08:30. It covered the nature of the incident, the CCS, a summary, the awareness time and contact details.
   - In law this is a notification not in the specified form (s.28(2)(b)(ii)), made inside the 12-hour limit (08:00 to 20:00 HKT).
   - Not evidenced: the exact call time, the Commissioner's reference number, and the Commissioner's answer on an alternative route.
2. Annex E filed through the secure channel by 11:00. It included the extortion demand and the data claim, both marked unverified.
   - This meets the s.28(3) written record, due 48 hours after the call (by about 08:30 HKT 18 Nov).
   - It would also count as a specified-form notification inside the 12-hour limit.
   - Not evidenced: any submission receipt, which PH01 5.5 requires at the moment of filing.
3. Supplementary information on the confirmed data export, which I decided at C03 to send "today", has not been sent.
4. Annex F is scheduled: internal target 27 Nov, statutory limit 30 Nov 2026.

Assessment
- On the log, s.28(1)–(3) appear to be met in substance. They are not yet proven: the record has no receipt for either the call or Annex E.
- The 20:00 HKT outer limit is two hours away. If the Annex E is ever challenged and the call cannot be proved, we would have no evidence of a timely notification.
- The missed supplementary dispatch breaks an internal commitment (PH01 5.9). It is not a statutory breach, unless condition (d) below applies.

Decision and next action
(a) By 18:15 HKT, find our own evidence.
- Pull the secure channel's submission receipt or dispatch record for the 11:00 Annex E, from whichever device was used.
- Pull the 08:30 call record: the officer's contemporaneous note and the phone log.
- Save both under PH01 5.5.
- Close out condition C-1 (the filing terminal) under PH01 2.3: the secure channel became available at C02 and was used at 11:00.

(b) By 18:45 HKT, confirm with the Commissioner.
- Call the Commissioner's office on the verified CI route. Ask them to confirm:
  - receipt of the 08:30 notification, its logged time and the reference number;
  - receipt of the 11:00 Annex E.
- Ask for a written acknowledgement by return.
- Record the name and post of the person reached, the reference and a summary (PH01 5.5).

(c) 19:00 HKT checkpoint, if receipt is still unconfirmed.
- If neither the system nor the Commissioner confirms receipt of Annex E, re-submit it by 19:30 through the secure channel.
- Mark it as a re-submission of the 11:00 filing, updated with current facts. Keep the dispatch record and ask for a receipt by return.
- Fallbacks, in order:
  - the standby device, if the secure channel fails;
  - a fresh phone notification on the CI route before 20:00, giving the nature and identifying the CCS (s.28(2)(b)(ii)).
- Log each step.

(d) By 19:30 HKT, send supplementary information through the designated secured channel. Content:
- confirmed export of 80 customers' names, HKID numbers and phone numbers (no customer data attached);
- up to 18,000 further records in the workspace, export unverified;
- a vendor support credential was used, and the revoked credential may still have live sessions or tokens;
- the gateway is still impaired, with about 4,200 instructions queued;
- the decision on the secondary process is pending. If it is approved, that is a BCP activation, a relevant factor under Code 7.3.4(c), and it goes as a further supplement at once.
Condition: if the data workspace is itself a designated CCS separate from the gateway (a missing fact, which SEC to confirm by 19:00):
- treat the export as a s.28 incident for that CCS;
- awareness was at 12:00, the 12-hour category applies conservatively (Code 7.3.4(d)), so the outer limit is 24:00 HKT 16 Nov;
- file it as an Annex E naming that CCS, by 19:30.

(e) Record the missed C03 supplementary dispatch in the decision log, with the reason and the fix. Update the single list of what each authority has been told and when (PH01 5.9).

(f) Annex F: LC drafts it with SEC from 17 Nov. Internal target 27 Nov, statutory limit 30 Nov 2026. Section E will record the Police case reference, the HKMA and the PCPD.

Accountable owner and executing party
- Accountable: LC.
- Executing: the designated LC officer.
- SEC: confirms the workspace's CCS status and supplies the facts.
- The CMT chair is informed. No internal approval holds any filing (PH01 2.4).

Recipient and channel
- Commissioner of Critical Infrastructure (Computer-system Security).
- The verified CI telephone route for confirmation; the designated secured channel for Annex E and supplementary information.

Basis: external
- R01, Cap. 653. Status: statute.
  - s.28(2)(a), PDF p.44: notification "must be made as soon as practicable and in any event within the specified time".
  - s.28(2)(b)(ii): a notification not in the specified form must "include information on the nature of the computer-system security incident and identify the critical computer system concerned".
  - s.28(3): written record "in the specified form and way ... within the specified time".
  - s.28(5): failure to comply with (1), (3) or (4) is an offence.
  - Schedule 6, PDF p.97: item 1(a) "12 hours"; item 2 "48 hours after the notification concerned is made under section 28(1)"; item 3 "14 days".
- R02, Commissioner's Code of Practice. Status: code of practice under s.8, not subsidiary legislation.
  - 7.3.6(b), PDF p.36: telephone first, then the specified form "within 48 hours of the notification".
  - 7.3.7(a), PDF p.37: information that becomes available after the written report goes "as supplementary material". No direct rule located that requires supplementary information before Annex F. Search: "supplementary" across all documents.

Internal bank procedure (PH01 v1.0)
- 5.5: "For an electronic filing, LC saves the system's submission receipt or dispatch record at the moment of filing. If no receipt is shown, LC asks the recipient for one".
- 5.9: "Facts found after a report are sent as supplementary information by the route the external document sets."
- 2.3: condition close-out.
- Conflict check: no conflict. The gap is in carrying the procedure out, not in the procedure itself.

==================================================
UNIT Q11b – Review of the HKMA record and the supervisory contact to make now
==================================================
What the record shows
- Done in simulation:
  - telephone report by 08:30;
  - telephone updates before 10:00 (extortion demand, data claim, payment posture, media enquiry), between 12:15 and 12:30 (confirmed data exposure), and at 16:30;
  - copies of the 10:00 and 13:00 public statements sent.
- Not evidenced:
  - any receipt;
  - the HKMA's reference number, preferred format and update frequency;
  - the route used for the 10:00 written summary. This matters: if it went by corporate email before SEC logged email as safe, that departs from PH01 5.7 and may have exposed incident information.
- Whether the 09:00 holding statement was actually released cannot be verified. The HKMA was told of a "possibly unreleased" statement.
- No BCP activation is recorded.
- The next scheduled update is 20:30.

Decision: make a follow-up telephone call to the HKMA supervisory contact now, by 18:30 HKT, rather than waiting for 20:30. Reasons:
- the customer impact is now measured;
- SME payroll is time-sensitive;
- a BCP activation decision is imminent;
- customers are having trouble reaching the bank;
- there are evidence gaps to close.
The 20:30 scheduled update stays in place.

Content of the 18:30 call (confirmed and unverified items marked)
1. Service status:
   - the gateway is still impaired;
   - outbound domestic transfers, payroll submission and mobile transfer submission are still interrupted;
   - balance viewing works;
   - branches are open, but some customers report they cannot reach one;
   - call volumes have doubled.
2. Backlog: about 4,200 queued instructions, independently measured, including time-sensitive SME payroll. Some customers retried after timeouts. No instruction will be released until duplicate and status checks are complete (SEC Q10b).
3. Recovery option: a secondary process of up to 400 verified instructions an hour is awaiting the CMT chair's decision on SEC's security clearance. Activating it is a BCP activation, and we will notify the HKMA at once.
   - Professional judgment: even at full rate the backlog needs about 10.5 hours.
   - The Board-approved tolerance for this operation is 24 hours. Measured from 08:00, 50% falls at about 20:00 and 100% at about 08:00 HKT 17 Nov. If the disruption began earlier (unverified), both points come earlier. A breach of tolerance is a real risk.
4. Data and authorities:
   - 80 customers confirmed exposed; up to 18,000 records unverified;
   - the Commissioner was notified by 08:30 and Annex E filed at 11:00;
   - supplementary information to the Commissioner is going by 19:30;
   - PCPD notification status: report only the status actually logged. That filing is not in the handoff, so LC checks the tracker first, files at once if there is no dispatch record, and tells the HKMA the true status.
5. Customer handling: report COM's Q12 measures. A copy of any new public status update goes to the HKMA when released.
6. Closing the gaps. Ask the HKMA to confirm:
   - its reference number;
   - receipt of the 10:00 written summary and of each update and copy so far;
   - its preferred written route and update frequency.
   Also:
   - correct the record on the 09:00 holding statement: COM confirms by 18:20 whether it was released. If yes, send a copy now. If no, tell the HKMA it was not issued;
   - SEC logs its corporate-email decision now.

Follow-up actions
- By 19:30 HKT: a consolidated written update covering everything since 08:30, by the route the HKMA confirms.
  - Re-send the 10:00 written summary if it was not received.
  - Do not use corporate email unless SEC has logged it safe.
  - Save the receipts.
- Immediately on the CMT chair approving the secondary process: telephone the HKMA, then send a written note.
- After 20:30: updates at 00:30 and 04:30, then 08:00 and 18:00 daily. Also update at once on a change in service status, a public statement, reaching 50% or 100% of tolerance, or the pilot or release results.
- If the HKMA sets a different frequency, follow the HKMA.

Accountable owner and executing party
- Accountable and executing: LC.
- Payments Operations and SEC supply the figures and the status of the secondary process.
- COM supplies public material and the 09:00 release status.
- The CMT chair is informed. No internal approval holds the contact (PH01 2.4).

Recipient and channel
- HKMA banking supervision contact (from the RCR) by telephone.
- Written follow-up by the HKMA-confirmed route.

Basis: external
- R05, HKMA circular, 22 Jun 2010. Status: supervisory circular.
  - PDF p.2, "Reporting incident to the HKMA" (checked against the scan): "The HKMA may require the AI concerned to provide further information or updates."
  - PDF p.3, "Handling of customers' and media's enquiry" (checked against the scan): "The HKMA should be kept informed during the process and copies of public communication materials should be submitted to the HKMA for reference."
- R07, SPM TM-G-2. Status: non-statutory guideline. 1.3.3, PDF p.5: "AIs should inform the HKMA promptly if their BCP is activated. The HKMA should also receive periodic progress reports upon being notified until the final resolution of the crisis."
- R09, SPM TM-E-1. Status: statutory guideline. 8.2.5, PDF p.33: notify the HKMA "promptly".
- R06, SPM OR-2. Status: non-statutory guideline. PDF p.3: disruptions to critical operations "must not exceed its 'tolerance for disruption'".
- No direct rule located that requires notifying the HKMA of an expected or actual breach of tolerance. Searched "tolerance" in R06 and R14b, and "progress report" across all documents. Telling the HKMA is professional judgment.

Internal bank procedure (PH01 v1.0)
- 5.8: updates "every four hours during the first 24 hours, then at 08:00 and 18:00 daily", and at once on BCP activation or a change in service status.
- 4.4: "LC is told at once" on BCP activation.
- 4.3: the Board chair is told at 50% of tolerance.
- 5.7: no corporate email until it is logged safe.
- Conflict check: none. PH01's cadence is an internal minimum, and the HKMA's own requirements prevail (PH01 1.3).

No files were created.