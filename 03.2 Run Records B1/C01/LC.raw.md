LC SUBMISSION – C01 (Mon 16 Nov 2026, 08:00 HKT, H+0) – Units Q02a and Q02b
Locked before receiving colleagues' answers. All actions below are simulated, for the facilitator to log. The dispatch log is empty at 08:00, so nothing has been sent yet.

Facts I am relying on from the card: at 08:00 the bank confirmed that unauthorised commands encrypted payment gateway components. Outbound domestic transfers and payroll submission are disrupted. That processing is a core function of the designated CI, and the gateway is a designated critical computer system (CCS). Mobile balance view still works and branches are open.
Not yet verified at this card: whether failover works; the attack vector; the earliest time of compromise or of reasonable certainty before 08:00; whether any data was accessed or taken; how many customers or payroll batches are affected; whether there is any extortion demand.

==================================================
UNIT Q02a – Initial HKMA reporting action
==================================================
Decision and action
- Report to the HKMA now, by telephone to the HKMA supervisory contact. The contact is taken from the printed Regulator Contact Register (RCR), so the call does not depend on corporate systems.
- Give the HKMA whatever information we have now. Do not wait for containment, root cause, the CMT meeting or any internal sign-off.
- Information to give now. Each item is labelled confirmed or unverified.
  1. Bank identity, LC name and direct contact, and the time we became aware: 08:00 HKT 16 Nov 2026.
  2. Confirmed: unauthorised commands encrypted payment gateway components. Outbound domestic transfers and payroll submission (retail and SME) are disrupted.
  3. Confirmed still working: mobile balance view and branches.
  4. Unverified: failover capability, the attack vector and earliest compromise time, any data access or exfiltration, the number of customers and payroll batches affected, and an estimated restoration time. No extortion demand is known to LC at this card. This is not yet established either way.
  5. Actions under way: SEC containment and evidence preservation, and the CMT being convened. A Cap. 653 s.28 notification to the Commissioner is being made in parallel; we will give its time and reference. BCP or alternate processing has not yet been declared, and we will tell the HKMA at once if it is.
  6. COM is preparing customer and public communications. We will send copies of public material to the HKMA when they are issued.
  7. Time of the next update.
- Ask the HKMA during the call: what reference number it gives the incident, which written format and channel it wants for follow-up, and what update frequency it wants. Log the answers.
- Professional judgment: send a short written summary of the call by 10:00 HKT, by the route the HKMA names. Until SEC logs corporate email as safe, do not use it (PH01 5.7).
- Later updates: every four hours after the first report, i.e. about 12:30, 16:30, 20:30, 00:30 and 04:30 if the call is made at 08:30. After that, 08:00 and 18:00 daily. Also update at once on any of: BCP activation, confirmed data exposure, an extortion demand, a change in service status, or a public statement. If the HKMA asks for a different frequency, follow the HKMA.

Accountable owner and executing party
- Accountable: LC (PH01 v1.0 s.5.1).
- Executing: LC personally makes the call. SEC provides technical facts at the same time. Its checks run alongside the call and do not hold it.
- The CMT chair is informed. Chair approval is not needed and is not a precondition (PH01 2.4).
- Who must clear: no internal clearance is required. Only the HKMA can change the follow-up format or update frequency.

Deadline and trigger
- Trigger: becoming aware of a significant incident. That point is 08:00 HKT 16 Nov 2026.
- External standard: "immediately" (R05) and "promptly" (R09, R04). Neither gives a number of hours.
- Professional judgment: complete the call by 08:30 HKT at the latest.

Recipient and channel
- HKMA banking supervision contact, by telephone (RCR). Written follow-up by the route the HKMA confirms in the call.
- Record every contact under PH01 5.5: time, channel, name and post of the person reached, reference, summary and receipt.

External basis
- R05, HKMA circular "Incident response and management procedures", 22 Jun 2010. Status: HKMA supervisory circular, non-statutory. PDF p.2, heading "Reporting incident to the HKMA", first paragraph. I checked this against the scan image:
  "once an AI has become aware that a significant incident has occurred, the AI concerned should notify the HKMA immediately and provide it with whatever information is available at the time."
  Also: "an AI should not wait until it has rectified the problem before reporting the incident to the HKMA."
  PDF p.3, heading "Handling of customers' and media's enquiry", first paragraph (checked against the scan): "copies of public communication materials should be submitted to the HKMA for reference."
  The circular is still current: OR-2 8.5 (R06 PDF p.13) lists it as "existing HKMA guidance on incident management".
- R09, SPM TM-E-1 V.4. Status: statutory guideline under Banking Ordinance §7(3) (PDF p.1). s.8.2.5, PDF p.33: "the AI concerned should notify the HKMA promptly in accordance with the relevant arrangements set out by the HKMA from time to time."
  It applies here because s.8.2.1 covers "cyber attacks ... or service interruptions" affecting e-banking. Outbound transfers made through mobile banking are disrupted. Note: the card does not state expressly that mobile transfer submission is down.
- R04, SPM TM-C-1 V.1. Status: statutory guideline under Banking Ordinance §7(3). para 2.4, PDF p.4: AIs "should also promptly report significant cyber incidents to the HKMA".
- R08, SPM TM-G-1. Status: non-statutory guideline. s.3.3.3, PDF p.14: procedures "should include timely reporting to the HKMA of any confirmed IT-related fraud cases or major security breaches."
- R07, SPM TM-G-2 V.2. Status: non-statutory guideline. s.1.3.3, PDF p.5: "AIs should inform the HKMA promptly if their BCP is activated." This is a conditional next step; it is not triggered yet.

How the rules apply: "Significant incident" is not defined in R05 or R09. Applying it is professional judgment, and the threshold is clearly met:
- a confirmed cyber attack on a designated CCS;
- disruption of a Board-approved critical operation (PH01 4.2: outbound domestic transfers and SME payroll, tolerance 24 h);
- disruption of a CI core function;
- a large customer base that is potentially affected (180,000 retail and 12,000 SME).

Internal bank procedure (PH01 v1.0, effective 1 Oct 2026)
- s.5.1: "LC owns every report to a regulator or authority".
- s.5.2 names R05, TM-E-1 s.8.2 and TM-G-2 s.1.3, and says "This playbook does not restate their triggers, recipients or time limits."
- s.2.4: "The initial report goes on the facts held at the time, with unverified items marked as unverified".
- s.5.8: "LC updates the HKMA supervisory contact every four hours during the first 24 hours".
Conflict check: none. PH01 is consistent with R05, and under PH01 1.3 and 1.4 the external requirement prevails if any HKMA request differs.

No direct rule located in assigned sources for the HKMA initial-report channel, form, or a numeric time limit.
- Files searched: R05, R09, R04, R07, R08, R06, R13, R14a, R14b.
- Terms: "notify the HKMA", "significant incident", "relevant arrangements", "telephone", plus "incident" and "report" within individual documents.
- Limitation: the "relevant arrangements" referred to in R09 8.2.5 are not in the allowed manifest. The phone numbers on R05 p.3 are 2010 contacts for questions about the letter itself, not a reporting channel.
Conditional action: use the RCR supervisory contact, and adopt whatever written format the HKMA names.

==================================================
UNIT Q02b – Critical infrastructure (Cap. 653 s.28) incident notification
==================================================
Decision: Triggered. Notify the Commissioner now. This is the 12-hour category.

Action, in sequence
1. Telephone notification to the Commissioner of Critical Infrastructure (Computer-system Security) using the bank's verified CI-incident telephone route. Give:
   - (i) Nature: unauthorised commands encrypting payment gateway components.
   - (ii) CCS involved: the designated payment gateway, using SEC's system identifier.
   - (iii) Brief summary: outbound domestic transfers and payroll submission (a CI core function) are disrupted; balance view and branches are working; failover unverified.
   - Seriousness: core function disrupted.
   - Awareness time: 08:00 HKT 16 Nov 2026. Earliest identifiable time: under investigation.
   - Reporting officer's contact details.
   Then:
   - Get a reference number.
   - Tell the Commissioner's office that the bank's secure-filing terminal is unavailable, ask which alternative secured route it accepts for the written record, and log the answer.
2. Written record in the specified form through the designated secured channel. Use Annex E of the Commissioner's Code, because no sector-specific form was located (see the no-rule list below).
   - Internal target (professional judgment): file Annex E by 20:00 HKT 16 Nov. That puts a notification in the specified form inside the original 12-hour window, in case the phone notification is later challenged.
   - Statutory limit: 48 hours after the phone notification, e.g. 08:30 HKT Wed 18 Nov 2026 if the call is at 08:30.
   - Route, in order:
     a. The normal terminal, only if SEC logs it released. It must stay under any evidence hold until then (PH01 6.1, 5.6).
     b. Otherwise Compliance's standby filing device, only if Compliance has logged that it works and is enrolled for the Commissioner's designated channel.
     c. Otherwise the alternative route the Commissioner's office confirmed.
   - Never use an unconfirmed route. Do not use corporate email until SEC logs it safe.
   - Note: the email address in the Annex E collection statement is for personal-data enquiries only. It is not a filing channel.
3. Written report on Annex F through the designated secured channel. Statutory limit: 30 Nov 2026 (14 days after 16 Nov). Internal target: 27 Nov 2026, because the rules for counting the 14 days (Cap. 1) are not in the allowed sources.
4. Tell the HKMA in the Q02a call that the s.28 notification has been made, with its time and reference. Offer a copy of Annex E. This is professional judgment; no rule requires it.

Accountable owner and executing party
- Accountable: LC (PH01 5.1).
- Executing: a designated LC officer makes the phone notification in parallel with LC's HKMA call, using only the card facts. No pre-approval hold.
- SEC provides the CCS identifier and nature at the same time, and decides by 08:30 whether the terminal can be released.
- Compliance tests and logs the standby device immediately.
- Who must clear conditions: SEC (terminal release); Compliance (standby device); the Commissioner's office (any alternative written route).
- The CMT chair is informed. Chair approval is not needed (PH01 2.4).

Awareness point, clock and fallback
- Awareness: 08:00 HKT 16 Nov 2026 at the latest. That is when the bank confirmed unauthorised commands and the disruption.
- Outer limit: 20:00 HKT 16 Nov 2026 (12 hours). The primary duty is "as soon as practicable". Target: phone notification completed by 08:30 HKT, and in no case later than 09:00.
- Missing fact: if SEC's timeline shows the bank had reasonable certainty before 08:00, the clock runs from that earlier time and the outer limit moves earlier. The early phone call removes this risk. Record both times in Annex E fields B3 and B4.
- Fallback: if the phone route fails, notify immediately by any route that states the nature of the incident and identifies the CCS (s.28(2)(b)(ii)), such as another Commissioner route in the RCR or the standby device. Escalate to the CMT chair. Do not wait until 30 minutes before 20:00.

External basis
- R01, Cap. 653 Protection of Critical Infrastructures (Computer Systems) Ordinance. Status: statute (verified copy, version date 10 Sep 2026).
  - s.28(1), PDF pp.43–44, heading "Obligation to notify computer-system security incidents": "the operator must notify the Commissioner of the incident in accordance with subsection (2)."
  - s.28(2)(a), PDF p.44: "must be made as soon as practicable and in any event within the specified time".
  - s.28(2)(b)(ii): "despite not being made in the specified form and way, include information on the nature of the computer-system security incident and identify the critical computer system concerned."
  - s.28(3): must "subsequently submit a written record ... in the specified form and way to the Commissioner within the specified time."
  - s.28(4): further "written report".
  - s.28(5)–(6): breach is an offence, fine up to HK$3,000,000 on summary conviction or HK$5,000,000 on indictment.
  - Schedule 6, PDF p.97, item 1(a): if the incident "has disrupted, is disrupting or is likely to disrupt the core function of the critical infrastructure concerned—12 hours after the CI operator concerned becomes aware of the incident". Item 2: "48 hours after the notification concerned is made under section 28(1)." Item 3: "14 days after the date on which the CI operator concerned becomes aware".
  - s.2 definition, PDF p.10: a computer-system security incident involves "any other act done, without lawful authority, on or through the critical computer system" and "has an actual adverse effect on the computer-system security". "Computer-system security" (PDF p.9) covers the availability and integrity of the system's services.
  - Recipient: the Commissioner, not the MA. s.6 (PDF p.15) limits a designated authority to "category 1 obligations and category 2 obligations". s.28 sits in Part 4 Division 3, which is category 3 (PDF p.9). The MA is the designated authority for AIs (Sch. 2 Pt 2, PDF p.89).
  - s.10, PDF p.20: a regulating authority may specify forms and ways, including "more than one way".
- R02, OCCICS Code of Practice (Generic) v1.0. Status: code of practice issued by the Commissioner under Cap. 653 s.8. Per para 1.1.4 it is "not subsidiary legislation", but it is admissible in proceedings under s.9.
  - 7.3.5, PDF p.36: "At the point the CI operator has a reasonable degree of certainty that a computer-system security incident has occurred, the CI operator is deemed to have become aware".
  - 7.3.6(b): "the CI operator may first make the notification to a designated telephone number", followed by the form "within 48 hours of the notification".
  - 7.3.6(c): the s.28 notification does not replace "sector specific requirements", so Q02a still applies.
  - 1.1.6, PDF p.4: submit "through secured channels as advised by regulating authorities".
  - 7.3.3(b) and (e), PDF p.35: examples include ransomware and a CCS modified by a malicious payload.
  - 7.3.7, PDF p.37: Annex F within 14 days.
- R03, HKMA Sectoral Code of Practice. Status: code of practice issued by the MA under s.8(1)(b), covering category 1 and 2 only. 1.1.3, PDF p.3: Designated AIs "should refer to guidance published by the Commissioner in relation to category 3 obligations".

How the rules apply
- The unauthorised commands are acts done without lawful authority on the gateway, a designated CCS.
- Encryption of gateway components with loss of transfer and payroll service is an actual adverse effect on availability and integrity. It is not a pure technical failure (R02 7.3.2).
- The core function is disrupted now, so the 12-hour category applies. R02 7.3.4(c) (likely BCP activation) and (a) (likely to exceed the 24 h tolerance) may also apply, but they are not needed.

Internal bank procedure (PH01 v1.0)
- s.5.2 names "Cap. 653, section 28 and Schedule 6, and the Commissioner's Code of Practice section 7.3 and its Annexes E and F" and does not restate the triggers.
- s.5.3: deadline tracker, "checked by a second LC officer within 30 minutes".
- s.5.6: "If the normal filing terminal is unavailable ... SEC logs within 30 minutes whether it can be released"; otherwise use the standby device, "or asks the recipient which alternative it accepts".
- s.2.4: "No internal condition, review or approval may delay an action needed to meet an external deadline."
- Conflict check: no substantive conflict. Reading caution: the s.2.4 rule that applies "30 minutes before the external deadline" is only a last-resort deadline. It must not be read as allowing filing up to 19:30, because s.28(2)(a) requires "as soon as practicable" (see also PH01 1.4).

No direct rule located in assigned sources:
- A sector-specific CI incident form. Searched R03 for "incident" (5 hits, none a form) and R02 for "notif" and "secured channel". Use Annex E.
- Any duty to copy the HKMA on the s.28 notification. Searched R01 for "designated authority" and R03 for "incident".
- The method for counting "14 days after the date". Cap. 1 is not in the manifest.

==================================================
Conditions logged under PH01 2.3 (verifier / latest time / default / close-out)
==================================================
- C-1, filing terminal: SEC / 08:30 HKT / standby device if logged working and enrolled, otherwise the Commissioner-accepted route. The written record is never held beyond 48 h / log the receipt (PH01 5.5).
- C-2, corporate email safe: SEC / 08:30 HKT / do not use email; use the phone and the confirmed route / log.
- C-3, deadline tracker second check: second LC officer / 08:30 HKT / LC re-checks personally / log.
- C-4, earlier awareness time: SEC timeline / next hourly SEC report / if earlier, recompute the outer limits and tell the Commissioner in Annex E / log.

==================================================
Simulated actions for the facilitator log
==================================================
- 08:00: LC records awareness at 08:00 and opens the deadline tracker with four clocks: HKMA (immediately); s.28 (ASAP, outer limit 20:00 16 Nov); s.28(3) (48 h after the call); s.28(4) (30 Nov).
- 08:05: LC asks SEC for the CCS identifier and a decision on C-1 and C-2. Compliance tests the standby device.
- By 08:30: two calls in parallel, both recorded under PH01 5.5. LC calls the HKMA supervisory contact. The designated LC officer calls the Commissioner on the verified CI route.
- By 10:00: written follow-up to the HKMA by the route it confirmed.
- About 12:30: first four-hourly HKMA update, plus immediate updates on any trigger.
- By 20:00 HKT 16 Nov (internal target): Annex E filed by a compliant route, receipt saved. Statutory limit: 48 h after the call.
- By 27 Nov (internal target): Annex F filed. Statutory limit: 30 Nov 2026.

Related paths, not decided in this unit
- PCPD (R11) and the HKMA customer-data circular (R16b): not triggered on C01 facts, because no personal data exposure is known. Reassess at once if SEC finds data access.
- Police CSTCB: listed as a "relevant authority" in R04 footnote 1. Under PH01 s.3 this is LC's decision, and I will log it as a separate decision.

No files were created.