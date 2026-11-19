LC answer to C03 (Monday 16 Nov 2026, 12:00 HKT, H+4). This covers my units Q08a and Q08b only. I locked it before seeing colleagues' answers. The facilitator gave LC no handoff for C03. My earlier answers (C01 Q02, C02 Q05) stand.

**Facts I am using**
- Independent, time-stamped logs confirm that a file holding 80 customers' names, HKID numbers and phone numbers was exported without authority. The forensic match is to bank records.
- Up to 18,000 customers' records sat in the same workspace. Export of that wider set is UNVERIFIED.
- A vendor support credential was used in the session.
- The attacker claims to have copied files. That claim is UNVERIFIED beyond the 80 records.
- Exposure awareness point: confirmed at or before 12:00 HKT on 16 Nov. SEC must log the exact confirmation time, and all clocks below run from that time.

---

## Q08a – Notifying the Privacy Commissioner (PCPD)

**Decision.** Notify the PCPD now as a voluntary data breach notification. Describe it accurately: no statute requires it, but the HKMA expects it and the PCPD recommends it. In the notification:
- State the 80 records as a confirmed fact.
- State the wider set of up to 18,000 customers as "possible, under investigation, export not verified". Do not present it as a confirmed figure or as the bank's estimate.
- Tick "Cyberattack (e.g. hacking)" as the cause.
- Tick "Identity theft" and "Financial loss" as real risks.
- Answer "Yes" to whether a service provider or contractor handled the data. A vendor credential was involved; whether the vendor itself acted is not established.
- Answer "Yes" to whether other authorities were notified. List the HKMA, the Cap. 653 Commissioner and the Police in neutral terms. LC clears the wording because of the Cap. 455 s.25A(5) tipping-off point from C02.
- Mark customer notification as "No, will do so within (1) days" for the 80. Update this when letters are delivered.
- Mark media statement according to COM's actual status at the time of filing.

**Owner and executor.**
- Accountable: LC, who owns all authority reports under PH01 s.5.1.
- Supporting: the Data Protection Officer (DPO) prepares the form content with LC. SEC confirms each fact.
- No internal approval may delay the filing (PH01 s.2.4).

**Timing.** "As soon as practicable". Target: filed by 15:00 HKT today, Mon 16 Nov.
- Send update notifications ("an update of a previous notification") whenever scope changes. Also send one with the 24-hour scope review result.
- The deadline is my professional judgment. No fixed statutory clock applies; the 3-hour target lets us check the facts without delay.

**Recipient and channel.** PCPD, using its Data Breach Notification Form (R16a) in writing. Oral notification is not accepted.
- Channel: fax to 2877 7026, or delivery in person to Room 1303, 13/F, Dah Sing Financial Centre, 248 Queen's Road East, Wanchai.
- Email to dbn@pcpd.org.hk only once SEC has logged corporate email as safe (PH01 s.5.7).
- An online route is also listed in the guidance.
- Save the receipt (PH01 s.5.5).
- Note that R11 p.8 lists "online, by fax, in person or by post" while the R16a form p.3 lists post/in person, fax and email. Both are valid. I choose fax or in person because they do not depend on our possibly compromised systems.

**Basis – external**
1. **Statute: R10, Cap. 486 PDPO, Schedule 1, DPP 4(1), PDF p.169.** "All practicable steps shall be taken to ensure that any personal data ... held by a data user is protected against unauthorized or accidental access". This is the substantive duty the breach engages. The PDPO has no breach-notification duty.
2. **PCPD notification form: R16a, Data Breach Notification Form (Revised 06/2023), p.1, introductory paragraph 2.** "Although it is not mandatory under the Ordinance for data users to give data breach notifications, data users are encouraged to give such notifications timely". This confirms the notification is voluntary.
3. **Privacy guidance: R11, PCPD Guidance on Data Breach Handling (June 2023)** (non-binding).
   - p.6, "Step 4": "the data user should notify the PCPD and the affected data subjects as soon as practicable after becoming aware of the data breach, particularly if the data breach is likely to result in a real risk of harm".
   - p.8, "When to notify?": "regardless of the progress of any internal investigation."
   - p.8, "Notification to the PCPD": "Oral notifications are not accepted."
   - p.5, Step 3: HKID information can "facilitate the commission of identity theft or fraud".
   - How this applies: HKID number plus name plus phone number, taken by a criminal who is extorting the bank, gives a real risk of identity theft and phishing or fraud.
4. **HKMA supervisory circular: R16b, Customer Data Protection (14 Oct 2014), PDF p.3, paragraph 1.**
   - "while there is no statutory requirement on AIs to report privacy incidents to the Privacy Commissioner, the AI concerned should seriously consider doing so ... In case the AI concerned decided not to report the incident to the Privacy Commissioner, it should provide justification".
   - Same paragraph: serious incidents (sensitive data) are to be reported "to the HKMA and notify the affected customers as soon as practicable".
   - HKID data is sensitive, so this is triggered.

**Related paths opened by this card** (each with its own clock; supporting Q08):
- **HKMA.** Update immediately on confirmed data exposure.
  - Basis: R16b p.3 (above); PH01 v1.0 s.5.8 "at once on any of: ... confirmed data exposure".
  - Owner: LC. Target: by 12:30 HKT by phone to the supervisory contact, then in writing. Tell the HKMA that the PCPD filing is under way and send a copy.
- **Cap. 653 Commissioner.** Send supplementary information on the data exfiltration through the secure channel (now available). This adds to the s.28 notification already made.
  - Basis: R02 s.7.3.4(d) lists leakage of customer data as a serious-incident criterion. R02 s.7.3.7(a) says supplementary material should be given "If additional information become available".
  - Include it in the s.28(3) written record if that has not yet been filed. That record is due 48 hours after the phone notification.
- **Police.** Add the confirmed exfiltration to the existing Police CSTCB case.
  - Basis: R11 p.4: "Notifying the relevant law enforcement agencies if identity theft or other criminal activities have been or are likely to be committed".

**Internal bank procedure (PH01 v1.0)**
- s.5.2 lists "the PCPD Guidance on Data Breach Handling and the Data Breach Notification Form" as external documents that LC applies directly.
- s.5.4: the Regulator Contact Register (RCR) holds the PCPD filing address.
- s.4.1: Severity 1 covers "customer personal data is confirmed or suspected to be exposed".
- s.15.1: the CMT chair tells the Board chair within two hours of "confirmed customer data exposure". Latest time: by 14:00 HKT.
- No conflict with the external requirements.

---

## Q08b – Which individuals to consider for notification now, and what expands the group

**Decision.**
- **Group A – notify now:** the 80 customers whose export is confirmed.
  - The CMT chair approves this audience. LC clears the text. The DPO and SEC confirm the data types per customer.
  - Recommended content follows R11 p.7. LC clears the final text:
    - what happened, and when it was detected;
    - the data types (name, HKID number, phone number);
    - that no account credentials are confirmed exposed (SEC to confirm);
    - risks: impersonation calls, SMS or phishing, and identity misuse;
    - protective steps: the bank never asks for PINs or OTPs; call back on the number on the card; be alert to account activity;
    - the named contact team;
    - remediation, per COM and section 13.
- **Group B – up to about 17,920 other workspace customers: hold individual notification for now.** This is a held decision, not a closed one.
  - Reason: export is unverified. Under PH01 s.10.4(c), an unverified claim or the size of the store does not by itself make everyone a notification batch.
  - Log the reason. Review whenever new evidence arrives, and at least every 24 hours.
  - The CMT chair decides whether a public statement (Q09b, COM) covers Group B in the meantime. That decision is in line with R16b p.3 ("If a large number of customers are affected, the AI concerned should consider making a public announcement") and R11 p.8.

**Owner.**
- The CMT chair approves the audience (PH01 s.3, s.10.1).
- LC clears the text and makes the legal recommendation. The DPO advises.
- COM sends and keeps the delivery register (s.10.3).

**Timing.**
- Group A: approval target 13:00 HKT. Personal calls start the same afternoon. Letters are dispatched by end of day 16 Nov. Completion is evidenced in the delivery register, with figures to LC daily.
- Group B: a formal scope review by the DPO and LC with SEC evidence must happen no later than 12 hours after first confirmation. That is by 24:00 HKT on 16 Nov if confirmation was 12:00; adjust to the logged confirmation time. The CMT chair then decides and logs the decision and reasons.

**Channel.** Under PH01 s.10.2:
- personal call by a named team, offering to call back on the number on file; plus
- a letter.
- The secure inbox may be used only once SEC logs it as trusted.
- SMS may carry an alert with no link. This matters especially because the leaked phone numbers increase the risk of smishing.
- Contact details are taken only from verified records (s.10.5).

**Events that would expand the group** (any one triggers notifying the affected subset as soon as practicable, under s.10.4(a)):
1. SEC logs, flow records, the vendor session logs (requested under C02/Q04) or forensic analysis show that further records were exported, accessed or staged. Notify the customers whose records are shown.
2. The attacker publishes or offers data, or sends new samples that match bank records. Notify the matched customers. If the leak is published and its scope cannot be bounded, consider the whole workspace.
3. Reports of misuse: impersonation or phishing calls, fraud or identity misuse reported by customers outside Group A.
4. Evidence that the logs are incomplete or cannot exclude bulk export. For example, gaps in coverage, or the revoked credential's tokens or sessions being shown to have stayed active. If export cannot be ruled out for the whole workspace, LC's professional judgment is to recommend notifying all 18,000. The reasons are the sensitivity of the data (HKID numbers) and that the records are co-located with confirmed records (s.10.4(c)).
5. Conversely, solid evidence limiting export to the 80 supports keeping Group B on hold. Group B is then covered by the public statement, with the reason logged.

**Basis – external**
- R11 p.6 Step 4 (quoted above), and p.5: the factors in "The likelihood of identity theft or fraud". Notification should be based on risk of harm.
- R11 p.8: direct notification "by phone, in writing, via email or in person". Public announcement "if data subjects are not immediately identifiable".
- R16b p.2: banks should be "notifying affected customers as appropriate (in case the AI concerned decided not to notify affected customers, it should provide justification on why it did not do so)". Logging the Group B hold reason meets this.
- R05 p.1 (supervisory circular): "The AI should proactively notify the customers affected or likely to be affected through the most effective means".
  - In LC's judgment, "likely to be affected" requires real evidence for the wider group. Size alone does not meet it. The judgment is left to the bank.

**Internal bank procedure (PH01 v1.0)**
- s.10.4(a): "Customers whose exposure is confirmed ... are notified as soon as practicable. They are not held back for the wider review."
- s.10.4(b): "No later than 12 hours after the first confirmation of exposure, the DPO and LC review ... The CMT chair decides".
- s.10.4(c): "An unverified claim, or the size of the data store, does not by itself make everyone in the store a notification batch."
- s.10.4(d): review "at least every 24 hours".
- No conflict with the external sources. PH01 is consistent with the "likely to be affected" standard in R05 provided the review gives real weight to co-location and sensitivity.

---

## Simulated actions for the facilitator to log

| Time (HKT) | Action | Owner |
|---|---|---|
| 12:10 | Decision log entry: PCPD voluntary notification; Group A (80) notify now; Group B (up to about 17,920) held with reasons; scope review due by 24:00 | LC |
| By 12:30 | HKMA update by phone, then written, on the confirmed exposure | LC |
| By 13:00 | CMT chair approves the Group A audience; LC clears the text | CMT chair, LC |
| By 14:00 | Board chair told of the confirmed exposure | CMT chair |
| By 15:00 | PCPD form filed by fax or in person; receipt saved | LC, DPO |
| Same afternoon | Cap. 653 Commissioner supplementary information through the secure channel | LC |
| Same afternoon | Police case updated | LC |
| By 24:00 | DPO/LC scope review; CMT chair decision logged | DPO, LC, CMT chair |