LC SUBMISSION – C03 (Mon 16 Nov 2026, 12:00 HKT, H+4) – Units Q08a and Q08b
Locked before I see colleagues' answers. All actions are simulated, for the facilitator to log. There was no facilitator handoff to LC for this card.

Facts I am relying on:
- Forensics have matched the attacker's sample to bank records.
- Independent, time-stamped logs confirm that a file holding 80 customers' names, Hong Kong identity card (HKID) numbers and telephone numbers was exported without authorisation.
- The same workspace holds records for up to 18,000 customers. Whether that wider set was exported is unverified.
- A vendor support credential was used in the session. A revoked credential may still have live sessions or tokens.
- Mobile transfer submission is still interrupted.

Missing facts:
- The exact time of the export, and the exact time forensics confirmed it. I treat 12:00 HKT as the first confirmation.
- Whether every row in the attacker's screenshot is among the 80.
- Whether corporate email has been logged as safe.

==================================================
UNIT Q08a – Notifying the Privacy Commissioner (PCPD)
==================================================
Decision and action
- Notify the PCPD today. Target: by 15:00 HKT 16 Nov 2026.
- Submit it as an initial notification on the PCPD Data Breach Notification Form, then send updates as facts change.
- How to describe its status: a voluntary data breach notification. The Personal Data (Privacy) Ordinance does not require one. We are making it in line with PCPD guidance and the HKMA's supervisory expectation.
- What it must not say:
  - It must not call itself a statutory or mandatory filing.
  - It must not admit a breach of Data Protection Principle 4 (DPP4); whether there was one is a legal judgment.
  - It must not suggest the PCPD has approved anything.
- What the form will say. Each item is labelled as confirmed or unverified.
  - It is a new notification.
  - Date the bank became aware: 16/11/2026. The narrative explains that the claim arrived about 09:30 and was unverified, and that forensics confirmed it by 12:00.
  - Date of the breach: the export time from SEC's logs, or "under investigation".
  - Individuals affected: 80 confirmed. The narrative adds that the same workspace holds up to 18,000 customer records, that export of the wider set is unverified and under investigation, and that an update will follow.
  - Hong Kong residents affected: "Yes / To be confirmed".
  - Data types: name, HKID number, telephone number.
  - Service provider involved: "Yes". A vendor support credential was used in the session, and the vendor's role is under investigation.
  - Cause: cyberattack (hacking).
  - Real risks: identity theft and financial loss through fraud or phishing.
  - Remedial actions so far: isolation, evidence preservation, revocation of the vendor credential (closure test pending), and Police informed.
  - Individuals notified: "No, will do so within (1) days", or the actual status at the time of filing.
  - Media statement: the status COM decides under Q09b.
  - Other authorities informed: HKMA, the Commissioner under Cap. 653, and the Police.
- Also on content:
  - Attach no customer data. If the PCPD asks for the list, provide it by a secure route.
  - Do not mention any disclosure made under Cap. 455 (Organized and Serious Crimes Ordinance), because s.26(3) and s.25A(5) restrict revealing one.
- PCPD updates go in at once on any of:
  - a wider affected group;
  - completion of customer notification;
  - publication of the data;
  - the final scope.

Accountable owner and executing party
- Accountable: LC (PH01 5.1).
- Executing: the DPO prepares the form and LC signs it. SEC confirms the facts at the same time, not before.
- No internal approval holds the filing (PH01 2.4). The CMT chair is informed.

Deadline and trigger
- Trigger: a confirmed breach of personal data security, with a real risk of harm. HKID numbers combined with names and phone numbers create a real risk of identity theft and fraud, and an extortioner holds them.
- Standard: "as soon as practicable", with no fixed number of hours.
- Professional judgment: 15:00 HKT is practicable. The form takes about 10–15 minutes and the core facts are known.

Recipient and channel
- Recipient: the Office of the Privacy Commissioner for Personal Data.
- Accepted channels, all written (oral notification is not accepted):
  - email to dbn@pcpd.org.hk;
  - fax to 2877 7026;
  - post, or in person at Room 1303, 13/F, Dah Sing Financial Centre, 248 Queen's Road East.
- Use corporate email only if SEC has logged it safe (PH01 5.7). Otherwise fax, or deliver by hand.
- Record the receipt or acknowledgement under PH01 5.5.

Basis: external
- R10, Cap. 486 Personal Data (Privacy) Ordinance. Status: statute (verified copy, 1 Oct 2022).
  - Schedule 1, DPP4(1), PDF p.169: "All practicable steps shall be taken to ensure that any personal data ... held by a data user is protected against unauthorized or accidental access, processing, erasure, loss or use". This is the substantive duty, and it is why the bank should make no admission.
  - DPP4(2) covers data processors. This is relevant to the vendor.
  - No mandatory breach-notification provision located in R10. Search terms: "data breach" (0 hits) and "notif" (hits only on access/correction requests and direct marketing).
- R16a, PCPD Data Breach Notification Form (rev. 06/2023). Status: PCPD form, privacy guidance material.
  - PDF p.1: "Although it is not mandatory under the Ordinance for data users to give data breach notifications, data users are encouraged to give such notifications timely".
  - PDF p.3 lists the submission channels.
- R11, PCPD Guidance on Data Breach Handling (June 2023). Status: privacy guidance, non-statutory (disclaimer at PDF p.10).
  - PDF p.6, Step 4: "the data user should notify the PCPD and the affected data subjects as soon as practicable after becoming aware of the data breach, particularly if the data breach is likely to result in a real risk of harm".
  - PDF p.8: "regardless of the progress of any internal investigation" and "Oral notifications are not accepted."
  - PDF p.5: HKID information combined with other data "is more likely to result in identity theft".
  - PDF p.1: a data breach includes a "suspected or actual breach".
- R16b, HKMA circular "Customer Data Protection" (14 Oct 2014). Status: HKMA supervisory circular. PDF p.3: "while there is no statutory requirement on AIs to report privacy incidents to the Privacy Commissioner, the AI concerned should seriously consider doing so". If the bank decides not to report, "it should provide justification".

Internal bank procedure (PH01 v1.0)
- 5.2 names "the PCPD Guidance on Data Breach Handling and the Data Breach Notification Form".
- 5.1: LC owns the report.
- 2.4: the report "goes on the facts held at the time, with unverified items marked as unverified".
- Conflict check: none. PH01 states no rule that conflicts.

==================================================
UNIT Q08b – Who is considered for breach notification now, and what widens the group
==================================================
Decision and action
1. Notify now:
   - The 80 customers whose export is confirmed by the independent logs.
   - Any customer whose row appears in the attacker's screenshot and has been matched to bank records, if not already among the 80. The attacker demonstrably holds their data.
2. Not individually notified at this point: the rest of the up-to-18,000 records in the workspace.
   - Their export is unverified.
   - The size of the data store does not by itself make them a notification batch.
   - This group stays under review. LC records the reasons in the decision log, because the HKMA expects a justification for not notifying.
3. Mandatory scope review by the DPO and LC, using SEC's evidence, by 24:00 HKT 16 Nov. That is 12 hours after the first confirmation; it moves earlier if confirmation was earlier.
   - The CMT chair decides and logs the decision and reasons.
   - After that, review whenever new evidence arrives, and at least every 24 hours.
   - The CMT chair also decides whether a public statement covers customers not notified individually. LC's legal view on that, for COM's Q09b:
     - state the confirmed exposure accurately;
     - describe the wider set only as under investigation, without asserting it was exposed or ruling it out;
     - never deny that a demand was received.

Proposed timing for the 80
- 13:00 HKT: the CMT chair approves the audience.
- 13:30 HKT: LC clears the notice text.
- 14:00 HKT: first contact attempts begin, by the channels COM sets under PH01 10.2.
- 18:00 HKT (professional judgment): every one of the 80 has had a first attempt. Letters go out the same day.
- Contact details come only from the bank's verified records, never from the exported file. Any details changed since the incident began are checked by the Fraud team first.
- Notices contain no HKID numbers.
- Notices include:
  - what happened;
  - the data types involved;
  - the risk of identity theft, phishing and impersonation;
  - steps the customer can take;
  - the bank's contact point;
  - the offer of 12 months' identity-protection monitoring, opt-in (PH01 13.5).
- Professional judgment: put the 80 accounts under enhanced fraud monitoring and stronger identity checks for callers.

Events that would widen the group
The trigger in each case is evidence or risk, not the attacker's claim and not the size of the store.
- (i) Logs, egress records or forensic artefacts show further records were accessed, queried, copied or exported. Widen to the evidenced records.
- (ii) The attacker publishes, offers or sends further samples that match bank records beyond the 80. Widen to the matched records, or to the whole set if the material shows it.
- (iii) Customers report fraud, phishing or impersonation using these data types, and the Fraud team links it to workspace records.
- (iv) The vendor's session logs, or activity on tokens or sessions surviving the revocation (SEC Q07b), show access to the workspace by that path.
- (v) Professional judgment: at the 24:00 review, SEC cannot bound the export, for example because of a log gap during the session window. LC will then recommend widening to every record that session could reach. Reasons: HKID numbers are sensitive, and the records sat in the same place as the confirmed ones.

Accountable owner and executing party
- CMT chair: approves the audience (PH01 s.3, 10.1).
- LC: clears the text and co-leads the scope review.
- DPO: co-leads the scope review.
- SEC: confirms the list of 80 from verified copies only.
- COM: sends the notices and keeps the delivery register.

Basis: external
- R16b, HKMA circular, PDF p.3: where "the customer data stolen, lost or leaked is sensitive", AIs are expected to "notify the affected customers as soon as practicable after the AI concerned is aware of or notified of the incident". If they do not notify, "it should provide justification".
- R11, PCPD guidance:
  - PDF p.6: notify affected data subjects as soon as practicable where there is a real risk of harm.
  - PDF p.7: content of a notification.
  - PDF p.8: direct notification by phone, in writing, email or in person; public announcement where direct notification is "not practicable".
- R05, HKMA circular, PDF p.1 under "Customer notifications" (from the C01 reading): notify customers "affected or likely to be affected".

Internal bank procedure (PH01 v1.0, 10.4)
- (a): "Customers whose exposure is confirmed ... are notified as soon as practicable. They are not held back for the wider review."
- (b): "No later than 12 hours after the first confirmation of exposure, the DPO and LC review".
- (c): "An unverified claim, or the size of the data store, does not by itself make everyone in the store a notification batch."
- Conflict check: no conflict. PH01's test is based on evidence and risk, and it already weighs data sensitivity and co-location, which matches R11.

==================================================
Updates to LC's existing reporting tracks from C03 facts (not a new unit)
==================================================
- HKMA, by 12:30 HKT, by telephone.
  - Basis: PH01 5.8 requires an immediate update on confirmed data exposure; R16b p.3 applies to a serious privacy incident.
  - Content: the 80 confirmed and their data types; up to 18,000 unverified; the vendor credential; mobile transfers still interrupted; the plan for PCPD and customer notification; a copy of any public statement to follow.
- Commissioner (Cap. 653). Send supplementary information today through the designated secured channel: confirmed data exfiltration and use of the vendor credential (PH01 5.9). Carry it into the Annex F report due by 30 Nov.
- Board. Under PH01 15.1 the CMT chair tells the Board chair of confirmed data exposure by 14:00 HKT.
- Police (CSTCB). Update them under the existing case reference.

No files were created.