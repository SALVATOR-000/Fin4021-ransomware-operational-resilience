LC answer to C04 (Monday 16 Nov 2026, 18:00 HKT, H+10). I cover Q11a and Q11b only, and locked this before seeing colleagues' answers. My earlier answers stand except where I correct them below.

**Facts I relied on**
- From the C04 card: the gateway is still impaired. About 4,200 payment instructions are queued, including time-sensitive SME payroll. A secondary process (400 verified instructions an hour) is available if approved. Some customers retried transfers after a timeout. Call volumes have doubled and some customers cannot reach a branch.
- From the facilitator's handoff, taken as the logged record:
  - HKMA: phone report by 08:30. Written confirmation by 10:00, but the route used cannot be verified. Updates at 12:00 and 16:00. No receipts verified for any of these.
  - Commissioner: phone call by 09:00. Exact time, reference number and receipt are not verified. It was never established that the bank's verified number is the Commissioner's designated telephone number. No specified form has been dispatched. Supplementary information was sent through the secure channel, with no receipt verified. The secure channel has been available since C02.

---

## Q11a – Commissioner's notification (Cap. 653 s.28)

**What the record shows**
- The 12-hour limit for this serious incident ends at 20:00 HKT today. Awareness was 08:00 (R01 Sch.6 item 1(a)).
- The only logged notification is the 09:00 call. It did not use the specified form and way. So whether s.28(1) has been met depends on s.28(2)(b)(ii): the call must have included the nature of the incident and identified the critical computer system. The handoff says it did.
- But we cannot prove it. There is no exact time, no reference number, no receipt, and the designated status of the number is unconfirmed.
- The secure-channel supplementary messages are not an Annex E form, and their receipt is unverified. They do not cure the gap.
- I am correcting my C01 plan. Filing the written record "by Tue 17 Nov" leaves the bank unable to evidence compliance before 20:00 today.

**Decision and action**
1. **File the specified-form notification now (main action).**
   - Form: Annex E or the HKMA sector-specific form if the Regulator Contact Register (RCR) shows one, through the designated secure channel.
   - Tick box B1 "Has disrupted / is disrupting / likely to disrupt the core function of CI".
   - Nature: "Ransomware / malware attack", "Unauthorized system access / intrusion", "Data breach (leakage / tampering)". Also tick "Supply chain attack" only if SEC confirms; for now say "vendor credential used, under investigation".
   - System: payment gateway.
   - Earliest identifiable time: as SEC has logged it, marked unverified if not fixed.
   - Awareness: 16/11/2026 08:00.
   - Summary, with unverified items marked:
     - core function still disrupted at 18:00;
     - about 4,200 instructions queued;
     - 6 BTC demand, which the bank is not paying;
     - 80 customer records' export confirmed; wider export of up to 18,000 records unverified;
     - vendor credential revoked; session and token closure under test.
   - State on the form that it is (i) the notification in specified form under s.28(2)(b)(i), and (ii) the written record under s.28(3) of the phone notification made at about 09:00. The exact time is to be confirmed.
   - Owner: LC. Executed by the LC duty officer, with SEC confirming facts. A second LC officer checks the form.
   - Deadline: **dispatched by 19:00 HKT**, which leaves a 60-minute buffer before 20:00.
   - Device: the standby filing device if its log shows it working and enrolled, or the released terminal. If neither is logged as available by 19:00, call the Commissioner's office and file by whatever route it names before 20:00 (PH01 s.5.6).
   - Save the submission receipt the moment it is filed (PH01 s.5.5).
2. **Confirm the record (in parallel).**
   - By 18:30 HKT, call the Commissioner's office on the verified route.
   - Ask for: the reference number of the morning notification and the time they logged it; confirmation that the number called is the designated incident-notification number; acknowledgement of the supplementary messages; confirmation of the accepted written route.
   - Log the name, post, reference and answer. This call does not replace item 1 and must not delay it.
3. **Pending.**
   - Written report in specified form (Annex F or sector form) by **30 Nov 2026**, 14 days from the awareness date (R01 Sch.6 item 3). Internal target is 27 Nov. The second LC officer re-checks the date count.
   - Later facts go as supplementary information (R02 s.7.3.7(a)).
   - If the Commissioner confirms the 09:00 call was received and logged, item 1 still stands as the s.28(3) record, filed well within 48 hours. If the call cannot be confirmed, item 1 filed before 20:00 is the compliant notification in its own right.

**Basis (external)**
- **R01**, Cap. 653 (statute; PDF p.44):
  - s.28(2)(a): "as soon as practicable and in any event within the specified time"
  - s.28(2)(b)(ii): "despite not being made in the specified form and way, include information on the nature of the computer-system security incident and identify the critical computer system concerned"
  - s.28(3): "If the notification is not made in the specified form and way, the CI operator must subsequently submit a written record ... in the specified form and way"
  - s.28(5): failing to comply with (1), (3) or (4) is an offence.
  - Schedule 6, PDF p.97, item 1(a): "12 hours after the CI operator concerned becomes aware". Item 2: "48 hours after the notification concerned is made under section 28(1)."
- **R02**, OCCICS Code of Practice v1.0 (code of practice, not subsidiary legislation):
  - Annex E, PDF p.42, heading: "Pursuant to section 28(2)(b)(i)"; "All fields should be completed as far as practicable based on the information available."
  - s.7.3.6(b), PDF p.36: a phone notification first, then "submit a specified form ... through a designated secured channel within 48 hours of the notification".
- **Professional judgment.** The legal burden is to notify. Evidence that we notified is how we would show compliance if challenged. When the receipt, reference and designated status of the phone route are all unproven and the channel is now open, the prudent step is a notification in specified form before the 12-hour deadline. The cost is minimal and it removes the risk of an offence.

**Internal bank procedure (PH01 v1.0)**
- s.5.5: "If no receipt is shown, LC asks the recipient for one in the same call or by return, and logs the request."
- s.5.6: "LC first confirms from the external document the form and the way of submission that report requires".
- s.2.4: "If an internal condition is still open 30 minutes before the external deadline, the default in 2.3 applies".
- s.1.4: internal times "never extend an external deadline."
- No conflict with the external requirements. The C01 internal target of Tue for the written record was lawful but has been overtaken by the evidence gap. I now bring it forward.

---

## Q11b – HKMA supervisory contact

**What the record shows**
- The initial phone report and the 12:00 and 16:00 updates were made, but no acknowledgements or receipts are logged.
- The written confirmation route is unverified, and so is the corporate-email safety log.
- Copies of the public updates decided at C03 cannot be verified as sent.
- Since 16:00 there are new facts:
  - a material change in service status and customer impact (4,200 queue, payroll at risk, retries and possible duplicates, call volumes doubled, branch access problems);
  - a pending decision on activating the secondary process, which would be a BCP activation (PH01 s.8.2, s.4.4);
  - the Board-approved tolerance for transfers and payroll is 24 hours. It reaches 50% at 20:00 and 100% at 08:00 Tue (PH01 s.4.2–4.3).

**Decision and action**
1. **Phone the HKMA supervisory contact now (change in status).** Target **18:30 HKT**. Do not wait for the scheduled 20:00 update.
   - Report the current status: gateway still impaired; about 4,200 queued instructions, with SME payroll prioritised; retried and possible duplicate instructions held under a verification control (Q10b, SEC); doubled call volumes and branch reach problems, with the COM measures (Q12b).
   - Report that the CMT is considering activating the secondary process (400 verified an hour) on SEC's written security clearance and a 20-instruction pilot. Say that BCP activation, if declared, will be reported at once.
   - Give the projected tolerance points (50% at 20:00 today, 100% at 08:00 Tue) and that the Board chair is being told.
   - Report the Commissioner filing status: the specified-form notification is being filed before 20:00.
   - Data and extortion position unchanged since 12:30, unless SEC reports otherwise.
   - Ask the HKMA to: acknowledge the earlier reports and written confirmation, including which route it actually received them by; confirm the written route for future reports; say whether it wants any other cadence or format.
   - Log everything under PH01 s.5.5.
2. **Written follow-up by 19:30 HKT** by the route the HKMA confirms on this call. Use corporate email only if SEC's log shows it is safe.
   - Include copies of all public statements and media replies released so far. For the C03 updates, COM must first confirm what was actually published. Send only material whose release COM has verified, and say so.
   - Re-send the 10:00 written confirmation if the HKMA cannot confirm it received it.
3. **On BCP activation** (the CMT chair's decision under PH01 s.8.2): phone the HKMA at once, followed in writing. Then send periodic progress reports until the incident is resolved.
4. **Keep the schedule.** Updates at 20:00, 24:00 and 04:00, then 08:00 and 18:00 daily. The 20:00 update reports the outcome of the Commissioner filing (with its reference or receipt) and the decision on the secondary process.

**Owner.** LC, executed by the LC duty officer. SEC and the Head of Payments Operations confirm the figures. COM supplies the copies of public material.

**Basis (external)**
- **R05**, HKMA circular of 22 Jun 2010 (supervisory circular). Quotations checked against the scan.
  - PDF p.2, "Reporting incident to the HKMA": "The HKMA may require the AI concerned to provide further information or updates."
  - PDF p.3, "Handling of customers' and media's enquiry": "The HKMA should be kept informed during the process and copies of public communication materials should be submitted to the HKMA for reference."
- **R07**, SPM TM-G-2 v.2 (non-statutory guideline; the cover classification reads "A non-statutory guideline issued by the MA as a guidance note"). s.1.3.3, PDF p.5: "AIs should inform the HKMA promptly if their BCP is activated. The HKMA should also receive periodic progress reports upon being notified until the final resolution of the crisis." This applies only if the secondary process is activated, so the BCP report is conditional.
- **R09**, SPM TM-E-1 v.4, s.8.2.5, PDF p.33: notify "promptly in accordance with the relevant arrangements set out by the HKMA from time to time".
- **No direct rule located** in the assigned sources for a specific HKMA update cadence or a requirement to get acknowledgements.
  - Searched R05, R06, R07, R09 and R13 with "(inform|notify).{0,40}HKMA" (regex), plus the earlier manifest-wide regex "(notify|inform|report).{0,20}(the HKMA|the MA)".
  - The cadence comes from PH01 and from professional judgment.

**Internal bank procedure (PH01 v1.0)**
- s.5.8: "at once on any of: BCP activation, confirmed data exposure, an extortion demand, a change in service status, a public statement".
- s.4.4: "LC is told at once so that any external reporting that follows from activation is made."
- s.5.5: receipts.
- s.5.9: "LC keeps one list of what each authority has been told and when."
- No conflict with the external requirements.

**Governance.** No internal condition holds either action (PH01 s.2.4). LC clears the content. The CMT chair is told of both filings. The Board chair is to be told at the 50% tolerance point, by 20:00 (PH01 s.4.3); that is the CMT chair's action.

---

**Simulated actions for the facilitator to log**

| Time (HKT) | Action |
|---|---|
| 18:05 | Decision log entry, and deadline tracker corrected to show the s.28 evidence gap and the 20:00 limit |
| 18:30 | Call to the Commissioner's office to confirm the morning call |
| 18:30 | Call to the HKMA with the status update |
| By 19:00 | Annex E or sector form filed through the secure channel; receipt saved |
| By 19:30 | Written HKMA follow-up, with copies of verified public material |
| 20:00 | Scheduled HKMA update, including the Commissioner receipt |
| On activation | Immediate HKMA BCP report |
| By 30 Nov | Commissioner written report (Annex F) |