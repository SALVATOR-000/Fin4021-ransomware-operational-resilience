## CEO final decisions, C04 (Monday 16 November 2026, 18:00 HKT, H+10)

All six units are CONFIRMED; there are no overrides. I re-read the citations in the three sealed answers against the source pages and found them accurate. PH01 is not in the manifest ("PH01", all documents: 0 hits), so the internal basis is N/A throughout.

All actions below are simulated, for the facilitator to log.

### My own decisions that the sealed answers asked for

- **Secondary process:** yes. As crisis management team chair I log the activation at 18:30 on SEC's clearance of all seven gates. If any gate fails, nothing is released and it comes back to me.
- **Business continuity:** that activation is the continuity activation for payment processing. LC tells the HKMA at once and periodic reports start.
- **Public wording at 18:30:** COM's Version 2, because the process will not yet be running. Version 1 follows at 21:00 if it is running at full rate. The queue figure is approved for publication now; the hourly rate goes out with Version 1.
- **Branch hours and staff redeployment:** approved as COM proposes.
- **Secure filing terminal:** SEC answers LC's 18:05 request by 18:30 with a recorded release or a clean device.
- **18:00 posture review (from C02):** unchanged. No payment, no attacker contact. Next review 23:00.

### Conflicts between sealed answers, resolved within their stated branches

1. **Two teams would call the same SME.** SEC has payments operations make verification call-backs; COM has relationship managers make proactive calls. One call does both, on a number on file, in SEC's priority order. Payments operations enters the confirmation in the register.
2. **Calls pause at 22:00 but processing runs overnight.** Payroll batches and suspected repeats not confirmed by 22:00 stay held until calls resume at 07:30. SEC's 05:45 projection is not given to customers.
3. **COM's Version 1 says "we have started".** At 18:30 the pilot has not begun, so Version 2 is used.
4. **Branch priority desk against SEC's register check.** Frontline Instruction No. 4 carries SEC's rule: no transfer is re-keyed without a register check. Urgent cases are referred into SEC's reserved slots.
5. **"Have notified" in the morning statement.** The handoff shows the HKMA call at 08:15 and the Commissioner call at 08:30, both before the 08:45-09:00 release. Either wording branch was accurate, so no correction is needed.
6. **LC's HKMA call at 18:25 falls before the 18:30 activation.** LC reports the decision as pending, then tells the HKMA at once on activation, as LC's conditional step provides.
7. **LC's load.** LC makes two calls and two filings by 19:30. A named LC delegate clears COM's 18:30 text.

---

### Q10a

- **Original answer reference:** SEC sealed answer, C04, Q10a.
- **CONFIRM.**
- **Reason:** Payroll is waiting and the gateway is still down, so the alternative route should be used. The attacker had command access, so nothing in the queue is trusted until checked against the customer's original. Speed is capped by verification, not the other way round. Priority goes by time-sensitivity, not customer size.
- **Final action and condition:** As written.
  - SEC and payments operations check gates 1-7: independence, clean source, verification, authorisation, duplicate gate, logging, change control.
  - Pilot of 20 verified payroll instructions, reconciled end to end; full rate only if it reconciles.
  - Priority 1: SME payroll, earliest value date first.
  - Priority 2: value date today or tomorrow, plus up to 40 an hour for verified urgent referrals.
  - Priority 3: the rest in order of submission.
  - Held: failed verification, suspected duplicates, no authenticated origin, screening alerts, later-dated items.
  - Stop triggers as written. SEC or the payments operations lead may pause without prior approval.
  - The 400-an-hour ceiling is not raised by cutting checks. The evidence hold on the original gateway stays.
  - If the process was never tested, the pilot is extended and full rate waits for two clean checkpoints.
- **Accountable owner:** SEC for security clearance and stop authority. I give the activation. Executing: payments operations, the payments information owner, IT Operations.
- **HKT time or trigger:** Gates 18:00-18:30; activation decision 18:30; pilot 18:45; full rate 19:15; reconciliation hourly; heightened monitoring 01:00-03:00 on 17 November.
- **Recipient and channel:** The secondary process, under an emergency change record. Clearance and status to me, LC, COM and IT Operations over the out-of-band bridge.
- **Final external basis:** SEC Q10a "Basis", unchanged. Anchors re-read:
  - R07 TM-G-2 para 4.3.2, p.11: "record reconstruction and verification, establishment of new controls, alternate manual processes".
  - R07 para 4.2.2, p.10: "clear internal decision-making process and criteria for activation of the BCP and/or alternate sites".
  - R14b, pp.1-2: "a predefined additional layer of approval matrix to ensure proper authorisation, and reconciliation procedures to maintain accuracy following a bypass". Authority: good practice that R14a p.2 says institutions "are encouraged to review".
  - R06 OR-2 para 3.4, p.6.
  - Gates, pilot size and priority classes are professional judgment. Missing fact: the bank's own impact analysis; if it sets a different order, that governs.
- **Final internal basis:** N/A (PH01 absent).
- **Dispatch instruction:** EXECUTE NOW for the gate checks. HOLD on any release until SEC's clearance and my logged activation. SCHEDULE the pilot for 18:45 and full rate for 19:15.

### Q10b

- **Original answer reference:** SEC sealed answer, C04, Q10b.
- **CONFIRM.**
- **Reason:** A double debit is direct customer harm, and retries after a timeout make it likely. The gate catches repeats, items already paid and items with no authenticated origin before anything is released. A re-run cannot pay twice.
- **Final action and condition:** As written.
  - One instruction register from every source, including what the secondary process itself releases.
  - Matching key on payer, payee, amount, currency, value date and reference; payroll also on employer, period, count and total.
  - Already-paid check against the ledger and independent outbound records; in-flight items are held as "status unknown", not resent.
  - A unique processing identifier, so each instruction is released once only.
  - Suspected and possible duplicates are held; the earliest authenticated original is released only after the customer confirms by call-back.
  - Items with no authenticated origin go to the forensic team as possible tampering.
  - Maker, checker and SEC attestation.
  - Mobile submission stays closed; branches and the contact centre check the register before keying.
- **Accountable owner:** SEC for the control and its attestation. Executing: payments operations, the payments information owner, IT Operations, branches and contact centre.
- **HKT time or trigger:** Built and proven on the pilot by 18:45; in force before 19:15; exception list reviewed hourly. Trigger: zero releases without a "passed" entry in the register.
- **Recipient and channel:** The register in the restricted incident workspace. Exception list to the payments information owner. Summary counts to me, LC and COM.
- **Final external basis:** SEC Q10b "Basis", unchanged. Anchors re-read:
  - R14b, p.1: "duplication checks when re-attempting transactions".
  - R09 TM-E-1 para 5.1.2, p.19: "maintain and verify the integrity of the information processed".
  - R05, PDF p.1, "Immediate incident response".
  - No direct rule located for the matching key, identifier or call-back; these are professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the build. HOLD on any release without a register pass.

### Q11a

- **Original answer reference:** LC sealed answer, C04, Q11a.
- **CONFIRM.**
- **Reason:** The logged record shows a telephone notification at 08:30, inside the 12-hour limit, with the content the statute requires. It has no officer's name, reference or receipt, and the written record cannot be shown to have been filed. Re-confirming by phone and filing the form before 20:00 protects the bank whichever way the 08:30 call is later viewed.
- **Final action and condition:** As written.
  - Call the designated number, with a witness: confirm receipt of the 08:30 notification, restate it in full, record officer, post and reference, and ask again about an alternative filing route.
  - File R02 Annex E through the secure channel with the 18:00 facts; this absorbs the undispatched interim update.
  - Keep the submission receipt, telephone records and notes.
  - If the channel shows an earlier submission, retrieve its receipt and file the 18:00 facts as supplementary information.
  - Fallback if there is no channel access by 19:30: the evidenced 18:10 call stands, LC asks for another specified route, and it is escalated to me.
- **Accountable owner:** LC. SEC executes the terminal release or supplies a clean device.
- **HKT time or trigger:** Call 18:10; Annex E by 19:00 and in any event before 20:00 (12-hour limit). Written record otherwise due 08:30 Wednesday 18 November. Written report (Annex F) by Monday 30 November. Checkpoint 09:00 Tuesday if the fallback applies.
- **Recipient and channel:** Commissioner of Critical Infrastructure (Computer-system Security), by the designated telephone number and the designated secure filing channel.
- **Final external basis:** LC Q11a "Basis", unchanged. Anchors re-read:
  - R01 Cap. 653 s.28(2)(b)(ii), p.44: "include information on the nature of the computer-system security incident and identify the critical computer system concerned".
  - R01 s.28(3), p.44: "must subsequently submit a written record".
  - R01 Schedule 6 items 1(a) and 2, p.97.
  - R01 s.67(1)(a)(iii), p.84: "sent in the form of an electronic record to an address in an information system specified by the authority".
  - R02 para 7.3.6(b), p.36.
  - No direct rule located requiring a receipt for a telephone notification; obtaining one is professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the 18:10 call. SCHEDULE Annex E for 19:00, hard limit 20:00. Dependency: SEC's terminal answer by 18:30.

### Q11b

- **Original answer reference:** LC sealed answer, C04, Q11b.
- **CONFIRM.**
- **Reason:** The record shows timely reports at 08:15, 08:45, 10:00, 12:15 and 13:00, but no acknowledgement of any, and the route of two is unknown. A consolidated report that stands alone removes doubt about what the HKMA holds. The situation has also changed materially at 18:00.
- **Final action and condition:** As written.
  - Telephone the supervisory contact (or the out-of-hours contact); confirm receipt of each earlier report; record officer and time.
  - Send a consolidated written situation report with the full chronology and the 18:00 status, asking for written acknowledgement.
  - Ask whether any prescribed form or arrangement applies.
  - On activation of the secondary process, tell the HKMA at once and start periodic progress reports.
  - Attach public materials issued.
  - Use corporate email only if SEC confirms it is safe; otherwise a route agreed on the call.
- **Accountable owner:** LC. SEC confirms figures and the email route. COM supplies public materials.
- **HKT time or trigger:** Call 18:25; written report by 19:30; updates 21:00 and 08:00 Tuesday. Earlier on LC's triggers: process approved or started, duplicates found, a payroll cut-off missed, gateway restored, any public statement.
- **Recipient and channel:** HKMA Banking Supervision contact, by telephone then in writing.
- **Final external basis:** LC Q11b "Basis", unchanged. Anchors re-read:
  - R05, PDF p.2, "Reporting incident to the HKMA" (checked against the scan): "The HKMA may require the AI concerned to provide further information or updates."
  - R07 para 1.3.3, p.5: "AIs should inform the HKMA promptly if their BCP is activated. The HKMA should also receive periodic progress reports".
  - R05, PDF p.3: "copies of public communication materials should be submitted to the HKMA for reference".
  - No direct rule located on acknowledgement or update frequency; those are professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the 18:25 call. SCHEDULE the 19:30 report and the 21:00 and 08:00 updates. Dependency: my 18:30 activation triggers the immediate follow-up.

### Q12a

- **Original answer reference:** COM sealed answer, C04, Unit Q12a.
- **CONFIRM.**
- **Reason:** The morning statement is out of date on every service line, and its "call the hotline" advice no longer works. A dated update that says what changed, gives the queue in plain numbers and tells people who retried what to do lets SME customers plan.
- **Final action and condition:** As written.
  - Service status update replacing the morning's service lines, using Version 2.
  - The sentence on contacting customers before paying a repeat is included, because that is SEC's control.
  - The apology sentence is used only if the dispatch log shows no update went out after the morning statement.
  - Authorities are not restated unless LC confirms.
  - If the log shows no public data statement was issued, the C03 data paragraph goes in or alongside, with its C03 conditions. The update never says the effect on customer information is "being verified".
  - Compensation Line A is repeated.
  - Copy to the HKMA through LC.
- **Accountable owner:** COM. Approver: me. Fact check: SEC and Operations. Clearance and HKMA copy: LC.
- **HKT time or trigger:** 18:10 fact requests and dispatch-log check; 18:15 Frontline Instruction No. 4; 18:30 target release; 18:45 latest; further updates 21:00 and 07:00 Tuesday, and on any change.
- **Recipient and channel:** Website status notice, app and internet banking log-in notice, recorded hotline message, branch door notices, verified social media accounts, press release by email. A targeted push or SMS with no link goes to customers with queued instructions. At minimum, the channel the morning statement actually used.
- **Final external basis:** COM Q12a "Basis", unchanged. Anchors re-read:
  - R09 para 8.2.2, p.33: "inform them of the key facts relating to the incident and the steps that customers may take".
  - R05, PDF p.2 (checked against the scan): "the steps that affected customers need to take".
  - R05, PDF p.3: "consistent and up-to-date messages".
  - No direct rule located on update frequency or publishing queue numbers; that is professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE for 18:30, latest 18:45. Dependencies: dispatch-log check, Operations on balances and branch hours, LC delegate's clearance.

### Q12b

- **Original answer reference:** COM sealed answer, C04, Unit Q12b.
- **CONFIRM.**
- **Reason:** Adding lines will not fix a doubled call volume. The bank already knows who is behind the queued instructions, so calling them removes inbound attempts and reaches people who cannot get through. A reference number on each call-back guards against impersonation, which matters now that phone numbers are in the attacker's hands.
- **Final action and condition:** As written.
  - Proactive calls to customers behind the queued instructions, payroll first.
  - Call-back request by hotline option, by in-app function only if SEC and IT confirm it is trusted, and by branch slip, each with a reference number and a stated window.
  - Recorded status message at the start of the hotline.
  - Staffed branches stay open later tonight; all eight open early tomorrow, each with a priority desk.
  - Proactive calls to customers flagged as elderly or needing assistance who have a queued instruction.
  - No account matters on social media.
- **Accountable owner:** COM for design, wording and reporting. Executing: contact-centre head, branch network head, SME banking head, Operations and SEC for lists. Staffing and hours: approved by me.
- **HKT time or trigger:** 18:15 Instruction No. 4; 18:30 recorded message, call-back option and proactive calls start; 22:00 calls pause; 07:30 Tuesday calls resume; hourly figures to the crisis management team and LC.
- **Recipient and channel:** SME payroll customers by outbound call. Other customers by hotline call-back, in-app request, branch slip and priority desk. Staff by briefing call and intranet.
- **Final external basis:** COM Q12b "Basis", unchanged. Anchors re-read:
  - R05, PDF p.3 (checked against the scan): "deploy swiftly adequate resources and communication channels (e.g. customer service hotlines and extended office hours of branch services)".
  - R09 para 9.5.4, p.37: "other service channels will have the capacity and related operational procedures to provide an acceptable level of service".
  - No direct rule located on call-back services or priority handling; that is professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE for 18:15 and 18:30. Dependencies: customer list from Operations and SEC; Instruction No. 4 carries SEC's register rule.

---

### Order of dependent actions on this card

1. **18:00-18:30:** SEC and payments operations check the seven gates and build the register.
2. **18:05:** LC asks SEC for the terminal; SEC answers by 18:30.
3. **18:10:** LC telephones the Commissioner's designated number, with a witness.
4. **18:15:** COM issues Frontline Instruction No. 4.
5. **18:25:** LC telephones the HKMA; the secondary-process decision is reported as pending.
6. **18:30:** SEC's clearance; I log the activation; LC tells the HKMA at once. COM releases the status update (Version 2); the call-back routes and proactive calls go live.
7. **18:45:** Pilot of 20 payroll instructions, reconciled; duplicate gate proven.
8. **By 19:00:** LC files Annex E and saves the receipt.
9. **19:15:** Full rate if the pilot reconciles; hourly reconciliation from then.
10. **By 19:30:** LC's consolidated report to the HKMA; fallback check on the secure channel.
11. **21:00:** COM's public update (Version 1 if running); LC's HKMA update.
12. **22:00:** Customer calls pause; unconfirmed items stay held.
13. **01:00-03:00 Tuesday:** Heightened monitoring around the attacker's deadline.
14. **07:00-08:00 Tuesday:** Public update, calls resume, HKMA update.

### Carried decision from C03: wider data group (no C04 unit changed)

COM asked for the 18:00 decision. No card reports a scope result, so on the record export of the wider set is still neither confirmed nor ruled out. That is the trigger LC and COM both set at C03.

- I approve the precautionary notice in COM's C03 wording, to go by 20:00.
- It is not sent if SEC's 18:00 scope statement shows complete independent logs that bound the export to the 80; the reason is then recorded.
- Dependency: SEC's exact workspace list.
- One change to COM's C03 condition, made by me: I do not hold the notice until hotline capacity is scaled. The notice gives the Q12b call-back route as its contact point.

### Open item for LC (no unit changed)

SEC flagged a possible material change notification. This is a new basis:

- R01 Cap. 653 s.22(1), p.33: "within 1 month after the date on which the event occurs".
- R01 s.22(2)(a), p.33: "a material change occurs to the design, configuration, security or operation of a critical computer system".
- R03 para 6.1.1, p.11: the date is "the moment when a change is deployed to production environments". R03 para 6.1.3 directs the notification to the Monetary Authority.
- Missing fact: whether the secondary process changes the designated system's operation.
- Conditional action: LC assesses with SEC's technical description. If it does, the latest date is 16 December 2026 (my computation from deployment today).

### Still unverified at this card

Receipt of every regulator contact; whether Annex E was filed earlier; whether the 10:00 and 14:00 public updates were issued; the scope result; how many queued items are payroll or retries; whether the queue was altered; whether the secondary process was tested; clearing cut-off times; whether the continuity plan was formally activated earlier today.

### My search record

- Regex "payroll|salary|queued|backlog", all documents: 0 hits. The priority order is therefore judgment.
- Regex "duplicat|re-attempt|retry", all documents: 4 hits (R07 p.5, unrelated; R14b p.1, three times).
- Limitation: the bank's continuity plan, impact analysis and the secondary process's test records are not in the manifest.