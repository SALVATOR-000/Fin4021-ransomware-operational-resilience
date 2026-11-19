COM response for C01, Q03a and Q03b (Monday 16 Nov 2026, 08:00 HKT, H+0). I locked this response before seeing any colleague's answer. No handoff was received.

Summary: affected customers get a link-free alert and calls from 08:45 HKT. A public holding statement goes out by 09:00 HKT. Both need CMT chair approval and LC clearance, and SEC and Operations must check every factual line. Neither waits for LC's HKMA report or the Cap. 653 notification, which are on separate tracks. All actions below are simulated, for the facilitator to log.

---
## Q03a: Alerting affected and likely affected customers

**Decision and action**
1. **Audience.** All customers are treated as likely affected, because outbound domestic transfers and payroll submission are down bank-wide. The approval asked of the CMT chair is "all 180,000 retail and 12,000 SME customers, likely affected".
   - **Priority 1:** SME customers with payroll batches or value dates of today or the next business day. These follow the same urgency order as PH01 8.4, never customer size.
   - **Priority 2:** retail and SME customers with pending or rejected outbound instructions since the disruption began.
   - **Priority 3:** everyone else.
2. **Channels**
   - Priority 1 SMEs get a personal call from a named relationship-manager or contact-centre team. The team offers to call back on the number printed on the customer's card, or on the number on file.
   - Everyone gets a short SMS or app push **alert with no link**. App push is used only if SEC logs that the push platform is outside the affected segment. Otherwise SMS only, from verified contact records; any contact details changed after the incident began are checked by Fraud first.
   - The same text goes into the contact-centre IVR message, frontline scripts and branch counter notices.
   - The secure inbox is not used until SEC logs that it is trusted. Any written follow-up goes by letter.
   - Corporate email is not used until SEC logs it safe.
3. **Wording.** This is conditional on approval, and every factual line needs SEC and Operations sign-off.
   - Confirmed: "Since this morning, Lan Tidal Bank's outbound local transfers and payroll submission are disrupted because of a cyber security incident we are handling. You can still view balances in the mobile app, and our branches are open."
   - Being verified: "We are working to restore the service and are checking alternative processing. We will give a restoration time once it is confirmed."
   - What customers can do: "Keep this message for reference. Do not resubmit the same payment repeatedly. For urgent payments or payroll, call [hotline on the back of your card] or your relationship manager. Fees and charges caused by this disruption will be waived. Documented direct losses caused by the disruption, such as late-payment charges, can be claimed through our hotline, your relationship manager or a branch. We will never send you a link or ask for your password or one-time password. Next update by [time]."
   - Not said: the attacker, vendor or affected system, the bank's designation status, unconfirmed figures, or any promise that branches can make outbound transfers (that is not confirmed).
4. **Supporting actions**
   - Brief frontline staff and the contact centre by 08:40. COM approves the script and LC clears it.
   - Ask Operations to add hotline capacity and consider extended branch hours.
   - Open the delivery register at the first send. Approval and scheduling do not count as delivery. Completion figures go to LC daily.

**Owners**
- Audience approval: CMT chair (Chief Executive).
- Text: LC clears it; SEC and Head of Payments Operations confirm the facts.
- Drafting, sending and the register: COM.
- Calls: Payments Operations, RMs and the contact centre.
- Push-platform and inbox trust: SEC.

**Timing (HKT)**
- 08:20: draft to the CMT.
- 08:40: approvals done and scripts live.
- 08:45: first Priority 1 calls and the SMS batch start. All alert batches dispatched by 10:00 (my judgment).
- Precondition logged under PH01 2.3: CMT chair approval and LC clearance by 08:40, verified by COM. If the chair is not reached by then, the COO approves as alternate. The default is to go ahead with the confirmed-facts-only text. Any line that is not confirmed is dropped, and the missing confirmation is logged afterwards.

**Basis (external)**
- **R05**, HKMA circular "Incident response and management procedures", 22 Jun 2010, PDF p.1, heading "Customer notifications" (quote checked against the scan): "The AI should proactively notify the customers affected or likely to be affected through the most effective means and advise them of the steps or precautionary measures that they need to take as well as whether the bank would reimburse any losses". Also PDF p.3, heading "Handling of customers' and media's enquiry": "deploy swiftly adequate resources and communication channels (e.g. customer service hotlines and extended office hours of branch services)".
- **R09**, SPM TM-E-1 V.4, §8.2.2 (PDF p.33): "proactively notify the customers affected, or likely to be affected, through the most effective means".
- **Authority:** HKMA supervisory guidance to authorized institutions (AIs). It applies because this is a significant incident that disrupts a critical banking service channel and affects a large customer base.
- **Left to judgment:** the exact timing, the channel mix and how the audience is divided into priority groups.

**Basis (internal)** — Internal bank procedure, PH01 v1.0:
- §10.1: "COM drafts and sends; the CMT chair approves the audience; LC clears the text".
- §10.2: "SMS, push and email may carry an alert but never a link."
- §10.3: "Approval and scheduling are not delivery."
- §13.1: fee waiver "Staff may promise this at once."
- §13.2: direct losses "reimbursed on claim".
- §3: frontline scripts are approved by COM and cleared by LC.
- No conflict with the external rules found.

**Judgment:** an alert that carries no link and points customers to the number on their card is the most effective safe channel during a live attack, when phishing is likely.

---
## Q03b: Public holding statement

**Decision and action**
1. Publish a holding statement with the same confirmed, being-verified and what-you-can-do content as in Q03a. It also says that services other than outbound transfers and payroll are running, and gives a "next update by 12:00 HKT" line.
2. **Channels**
   - Bank website notice. This needs SEC to log that the website and its content system are outside the affected segment. If SEC has not logged that by 08:50, use the fallback below.
   - Press release to media by a distribution route that does not use corporate email until SEC logs email safe.
   - The same text on branch posters, the IVR and social media accounts, with no links to anything except the bank's own homepage.
   - Fallback: press release, branch notices and IVR only, with the web notice added once SEC confirms.
3. **Copy to HKMA.** LC sends a copy to HKMA at the time of release and logs it as a public-statement trigger for an HKMA update (PH01 5.8).
4. **Not dependent on Q02.** Release does not wait for LC's HKMA or Cap. 653 notifications. It is better practice for LC to have made at least the first HKMA phone call before release. COM will check with LC at 08:45, but the statement is not held for that call.
5. **Next updates.** Updates at least every 6 hours between 07:00 and 22:00, and at once on any change in service status. The next one is due by 12:00.
6. **Spokesperson.** The CMT chair is the only spokesperson. All staff refer media to COM.

**Approval**
- CMT chair approves. If the chair is unreachable for 15 minutes, the COO approves as alternate.
- LC clears the text. SEC and Operations check the facts.
- LC also confirms that the wording does not prejudice any Police referral or investigation.
- COM releases the statement and keeps the communications log.

**Timing (HKT)**
- Approval by 08:50 and release by 09:00.
- Default if approval is late: escalate to the COO at 08:50+15 min under PH01 §3, and release on the COO's approval.

**Basis (external)**
- **R05**, PDF p.2, heading "Public announcement" (quote checked against the scan): "consider making a public announcement where the situation so warrants, such as … (a) where the nature of the incident is serious, for example if the incident entails the disruption of any essential and critical banking service channel … or (b) where a large number of customers have been or may be affected". Same page: the need to inform the public "may need to be weighed against … whether a public announcement may prejudice any ongoing criminal proceedings or any investigation." PDF p.3: "copies of public communication materials should be submitted to the HKMA for reference."
- **R09** TM-E-1 §8.2.3 (PDF p.33): "an AI is expected to issue a press release (or make a similarly effective notification) shortly after the commencement of any disruption to its critical e-banking service that could affect a significant number of customers if the AI does not have reasonable confidence that the service can be resumed in the near future."
- **How the trigger applies:** the outage covers about 192,000 customers, failover is unverified, and the bank therefore has no reasonable confidence of a near-term restoration.
- **R07** TM-G-2 §4.7.1–4.7.2 (PDF pp.13–14): communication strategy; "clearly indicate who can speak to the media".
- **Left to judgment:** the exact release time ("shortly after") and the choice of channel.

**Basis (internal)** — Internal bank procedure, PH01 v1.0:
- §3: "Approve public statements and replies to media | CMT chair; alternate COO if the chair is unreachable for 15 minutes | LC clears; SEC and Operations fact-check".
- §11.1: "The CMT chair is the only spokesperson."
- §11.2: "at least every six hours between 07:00 and 22:00".
- §11.3: "does not name the attacker, the vendor, the affected system or the bank's designation status".
- §11.4: figures are published only once confirmed from a record.
- §5.1: COM supplies copies of public material.
- No conflict with the external rules: these limits on content are consistent with R05's caution about prejudicing an investigation.

---
**Unverified items I depend on, for the facilitator:**
- whether failover works
- whether the website, push platform, secure inbox and email are uncompromised (SEC to log)
- whether branches can take outbound payments (Operations)
- the time of LC's first HKMA contact (Q02)