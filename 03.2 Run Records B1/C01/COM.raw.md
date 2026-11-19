## COM submission for C01: Monday 16 Nov 2026, 08:00 HKT (H+0)

**Status.** I locked this before seeing any colleague's answer. No facilitator handoff was received. Every action below is simulated, for the facilitator to log. The dispatch log is empty, so nothing has been sent yet.

**What I took from the card.**
- **Confirmed:**
  - Unauthorised commands encrypted gateway components.
  - Outbound domestic transfers and payroll submission are disrupted.
  - Mobile customers can still view balances.
  - Branches are open.
- **Not yet verified:**
  - Whether failover works.
  - When the disruption started.
  - The status of instructions that were in flight.
  - When service will be restored.
  - Which branch transactions work, beyond the branches being open.
  - Whether customer data is affected. Nothing on the card suggests it is, but it has not been checked.
  - Whether the SMS, push, app-banner, website and email platforms sit outside the affected path.
  - How many customers are affected. The card's 180,000 retail and 12,000 SME figures are the bank's total customer base, not a confirmed affected count.

**Assumption.** Under PH01 s.4.1, a disrupted critical operation is severity 1. The card does not say severity 1 has been declared. I assume the Crisis Management Team (CMT) meets by 08:30 (PH01 s.2.1 requires the chair to convene it within 30 minutes of declaration). If declaration comes later, the internal approval times move, but the external expectation to act "shortly after" the disruption does not.

---

## Q03 a. Alerting affected and likely affected customers

### Decision and action
Alert customers proactively now, without waiting for a root cause or a restoration time. The alert goes in three groups, which I will propose to the CMT chair at 08:30 for approval. Letter is not the primary channel because it is too slow.

**Group A1 – SMEs with payroll due today or tomorrow** (value-dated 16 or 17 Nov, whether submitted or scheduled)
- **Channel:** a personal call from a named relationship manager or payments team. The caller offers to let the customer hang up and call back on the number on their statement or card. An SMS and push alert also goes, with no link.
- **Order:** earliest value date first. Customer size never sets the order (this mirrors PH01 s.8.4).

**Group A2 – customers whose outbound instruction is in flight, failed or of unknown status since the disruption began**
- **Channel:** SMS and push alert with no link. SME and time-critical items also get a call.
- **Key message:** do not resubmit. This prevents double payments (PH01 s.8.6).

**Group B – everyone else likely affected:** all other retail and SME customers who can make outbound transfers
- **Channel:** SMS and push alert with no link, sent in tranches sized to contact-centre capacity.
- **Also covered by:** the public channels decided under Q03b.

**Supporting actions**
- **Frontline and staff script:** COM approves it and LC clears it. It goes by 08:45 to branches, the contact centre and relationship managers by staff mobile broadcast and phone cascade. It does not go by corporate email until SEC logs email as safe (PH01 s.5.7 applies to regulator reports; I apply it to staff messages by analogy).
- **Phone line:** an IVR status message goes live at 08:45.
- **Capacity:** I recommend that Operations and the CMT chair add contact-centre staff and consider longer branch hours today (R05 p.3).

### Owners
- **Accountable:** COM drafts and sends (PH01 s.10.1). The CMT chair approves the audience, after consulting LC, SEC and the Data Protection Officer (DPO) (PH01 s.3). LC clears the text. SEC and Operations confirm each factual line.
- **Executing:**
  - The contact-centre and SMS/push platform team.
  - The relationship-manager and payments call teams.
  - Payments Operations, which supplies the A1 and A2 lists.
  - The Fraud team, which checks any contact details changed after the incident began (PH01 s.10.5).

### Timing (HKT)
| Time | Action |
|---|---|
| 08:15 | COM drafts ready (simulated, done) |
| 08:20 | COM asks SEC for a channel-trust log and asks the Head of Payments Operations for the A1/A2 lists and the list of branch services that work |
| 08:30 | Audience approved at CMT |
| 08:40 | SEC and Operations confirm the factual lines |
| 08:45 | Frontline script and IVR live |
| 09:00 | A1 calls start; A1 SMS/push sent |
| 09:30 | Group B SME tranche |
| 10:00–11:00 | Group B retail tranches |
| By 11:00 | Every A1 customer with payroll due today has been called at least once |
| By 15:00 | Every A1 customer with payroll due tomorrow has been called |
| List + 1 hour | A2 alerts go within one hour of Payments Operations delivering the list |

### Conditions (logged with the four items PH01 s.2.3 requires)
| Condition | Verifier | Latest time | Default if not verified | Close-out |
|---|---|---|---|---|
| C1. Each alert channel (SMS platform, push, app banner) is outside the affected path | SEC | 08:45 | That channel is not used; the alert goes by the remaining channels (calls, website, IVR, branches). All channels are never held. | SEC log entry |
| C2. Each factual line is correct (balances viewable in app; branches open; which branch services work) | SEC and Head of Payments Operations | 08:40 | The unconfirmed line is deleted and the message goes ahead | Fact-check record |
| C3. Audience approved | CMT chair; alternate chair (COO) if the chair is unreachable for 15 minutes (PH01 s.2.1) | 08:30 at CMT, then escalate | Escalate to the COO. COM logs that any delay risks the external expectation and tells LC (PH01 s.1.3). | Decision-log entry |
| C4. Text cleared | LC | 08:50 | Hold that text and escalate to the chair. The frontline script still goes, so staff answer consistently. | Communications log |
| C5. A1/A2 lists can be produced from records outside the affected systems | Head of Payments Operations | 09:30 | A1 is built from relationship-manager and payroll customer records. A2 is covered by the Group B alert line "if you submitted a transfer since [time], do not resubmit". A targeted A2 alert goes when the list arrives. | List receipt logged |

### Delivery evidence and follow-up
- COM keeps one register row per customer from the first notice, recording the time, channel and outcome of each attempt and the proof of delivery (PH01 s.10.3). Approval or scheduling does not count as delivery.
- For undelivered A1 items, I use a second call and then a relationship-manager visit. This is professional judgment, by analogy with R09 s.4.2.3.
- A customer whose delivery of the current message is evidenced gets nothing more until there is news (PH01 s.10.6).
- Completion figures go to LC daily.

### Draft wording
These drafts await LC clearance and SEC/Operations fact-check. A Traditional Chinese version is made from the approved English, checked by a second bilingual reviewer and sent at the same time.

**Group B SMS/push:**
> "Lan Tidal Bank (16 Nov): Outgoing local transfers and payroll submissions are currently disrupted following a cyber security incident. You can still view balances in our app and our branches are open. Please do not resubmit a transfer you have already made – we are checking each one. Fees caused by this disruption will be waived. We will never send you a link or ask for your password or one-time password. For help, call the number on the back of your card or on your statement."

**Group A2 SMS:**
> "Lan Tidal Bank: A transfer you submitted on [date] may not have been completed because of a service disruption. We are checking its status. Please do not resubmit it; we will contact you with the result. If it is urgent, call the number on the back of your card or on your statement. We never send links or ask for passwords or one-time passwords."

The A2 message carries no amount or payee details (judgment).

**Group A1 call script, key lines:**
- "You may hang up and call us back on the number on your statement."
- "Payroll and outgoing transfers are disrupted following a cyber security incident."
- "Our record shows your payroll due [date] as [submitted/not submitted]; we are checking its status – please do not resubmit."
- "If you decide to pay by another means, tell us first so we can hold the original instruction and avoid a double payment."
- "We cannot yet give a restoration time; we will call again by [time]."
- "You may wish to tell your employees that salaries may be delayed."
- "Fees caused by the disruption are waived."
- "Documented direct losses such as late-payment charges can be claimed; you will receive a case reference."
- "We will never ask for passwords or one-time passwords, or ask you to move money or change payee details."

**What the message says**
- **Confirmed:** transfers and payroll are disrupted; balances are viewable; branches are open; fees are waived.
- **Being verified:** the restoration time, the status of each submitted instruction, and whether customer information is affected.
- **What customers can do:**
  - Do not resubmit a transfer already made.
  - Report urgent payments.
  - Keep records and claim direct losses.
  - Ignore any message that contains a link or asks for a password or one-time password.

---

## Q03 b. Public holding statement

### Decision and action
Publish a bilingual (English and Traditional Chinese) holding statement.
- **Target:** 09:00 HKT.
- **Latest:** 09:30 HKT (professional judgment, to meet R09's "shortly after commencement").
- **Channels:**
  - The bank's official website service-status page. It is static text with no links, provided C1 shows it is hosted outside the affected path.
  - A press release to the media list.
  - The bank's official social-media accounts.
  - A mobile-app banner, if C1 is met.
  - Branch notices.
  - The IVR message.
- **Spokesperson:** the CMT chair only (PH01 s.11.1). All media enquiries go to COM.
- **Copies:** at release, COM sends a copy to LC. LC sends it to the HKMA (R05 p.3; PH01 ss.5.1 and 5.8) and keeps it for the Commissioner record.
- **Record for LC's written report:** COM logs the form ("Press release") and the date (16/11/2026) so LC can complete Part E of the written report (R02 Annex F, p.46).

### Owners
- **Approves:** the CMT chair, or the COO if the chair is unreachable for 15 minutes.
- **Clears and fact-checks:** LC clears; SEC and Operations fact-check.
- **Executes:** COM, which also keeps the communications log (PH01 s.3).

### Cadence
- The next update is due by 13:00 HKT.
- After that, updates come at least every six hours between 07:00 and 22:00, and at once on any change in service status (PH01 s.11.2). Examples of a change: alternate processing is activated, or isolation removes mobile balance viewing.

### Release conditions linked to other decisions on this card
- **Q01a (SEC isolation).** If isolation will remove mobile balance viewing, the CMT chair must be consulted (PH01 s.3). The line then becomes "Mobile banking may be temporarily unavailable; our branches are open." SEC confirms by 08:40.
- **Q02a (LC's HKMA report).** The line "We have informed the relevant authorities" goes in only if LC logs that the first HKMA report has been made. Otherwise the line is dropped. The statement is not held for this and does not need HKMA approval. LC should mention the planned statement in its first HKMA call.
- **Q02b (critical infrastructure notification).** This does not affect the release. The statement does not name the Commissioner or the bank's designation (PH01 s.11.3).

### Draft holding statement
> "Lan Tidal Bank service update – 16 November 2026, 09:00 HKT. Since this morning, outgoing local transfers and payroll submissions are disrupted following a cyber security incident affecting some of our systems. We are working to restore the service and are investigating. [We have informed the relevant authorities.] What is confirmed: outgoing local transfers and payroll submissions cannot currently be processed; customers can still view balances in our mobile app; our branches are open. What we are checking: when service will be restored; the status of transfers submitted before the disruption; and whether any customer information is affected – if it is, we will contact the customers concerned directly. What you can do: please do not resubmit a transfer or payroll already submitted; we are checking each one and will contact you. If a payment is urgent, contact your relationship manager, visit a branch, or call the number on the back of your card or on your statement. Fees caused by this disruption will be waived. We will reimburse documented direct losses caused by the disruption, such as late-payment charges from a missed payroll date; keep your records, and register a claim through your relationship manager, a branch or our hotline – each claim receives a case reference. We will never send you a link or ask for your password or one-time password; please ignore any message that does. We apologise for the disruption. Next update: by 13:00 HKT today, or sooner if service status changes."

### Media questions: fixed lines
- **"Was there a ransom demand?"** Do not speculate and never deny receiving a demand (PH01 s.11.3). Answer: "Our investigation is ongoing."
- **Attacker, vendor, system or designation:** not named.
- **Figures:** "being checked; we will give them by [time]" (PH01 s.11.4).
- **Restoration time:** "we cannot yet give a time."
- **Deposits:** do not say "your money is safe" or "no data affected"; neither has been verified.
- **Scam losses:** no promise of reimbursement (PH01 s.13.4).
- **Messages from the attacker:** passed to SEC only (PH01 s.12.3).

**My judgment on naming the cause.** I use "a cyber security incident". It is a confirmed fact, a key fact under R05, and customers need it to stay alert to scams. LC may switch to "a system incident" if it logs that the wording could prejudice an investigation, which is the weighing R05 p.2 and R09 footnote 25 allow.

---

## Basis

### External requirements

**1. R05 – HKMA circular "Incident response and management procedures", 22 June 2010.** I checked every quote below against the scan.
- **Authority:** an HKMA supervisory circular to all authorized institutions. It applies "whenever any significant incident occurs" (p.1).
- **p.1, "Immediate incident response":** "The top priority should be to safeguard the interests of customers who have been or may be affected by the incident."
- **p.1, "Customer notifications", paragraph 2:** "The AI should proactively notify the customers affected or likely to be affected through the most effective means and advise them of the steps or precautionary measures that they need to take as well as whether the bank would reimburse any losses incurred by them and if so, how they can apply for compensation".
- **p.2, "Public announcement":** the bank should "consider making a public announcement where the situation so warrants", including "(a) ... the disruption of any essential and critical banking service channel (e.g. branch services, e-banking, ATM services, etc.) or the disruption may last for a prolonged period of time; or (b) where a large number of customers have been or may be affected". The same page also says: "include the key facts of the incident and the steps that affected customers need to take".
- **p.3, "Handling of customers' and media's enquiry":** "copies of public communication materials should be submitted to the HKMA for reference"; and "deploy swiftly adequate resources and communication channels (e.g. customer service hotlines and extended office hours of branch services)".
- **Application:** a critical payment channel is disrupted, recovery is uncertain and up to 192,000 customers may be affected, so both (a) and (b) are met.
- **Left to judgment:** whether the incident counts as "significant" (the circular does not define it), the exact timing (no number of hours is set), the channels and the audience.

**2. R09 – HKMA SPM TM-E-1 "Risk Management of E-banking", V.4, 25 Oct 2024.**
- **Authority:** an HKMA Supervisory Policy Manual module. Section 1.4.2 says "AIs should comply with the requirements in this module".
- **Scope:** s.1.2.1 covers payment services delivered over the Internet, including to mobile devices (footnote 1). Section 8.2.1 covers "cyber attacks ... or service interruptions".
- **s.8.2.2 (pp.32–33):** "AIs should proactively notify the customers affected, or likely to be affected, through the most effective means (including considering the possibility of making a press release) and inform them of the key facts relating to the incident and the steps that customers may take". The footnote marker is omitted from this quote.
- **Footnote 26:** "any estimated service resumption time and ... how customers can protect their interests (e.g. apply for compensation ...)".
- **s.8.2.3 (p.33):** "an AI is expected to issue a press release (or make a similarly effective notification) shortly after the commencement of any disruption to its critical e-banking service that could affect a significant number of customers if the AI does not have reasonable confidence that the service can be resumed in the near future."
- **Application:** failover is unverified and gateway components are encrypted, so the bank has no reasonable confidence of a near-term restoration. The trigger is met.
- **Missing fact:** whether SME payroll is submitted through e-banking. If it is submitted at branches, R05 still covers it.

**3. General principles**
- **R06 – SPM OR-2, s.8.3 (p.13):** "Communication plans for reporting incidents to all relevant stakeholders, including both internal and external parties".
- **R07 – SPM TM-G-2, s.4.7.2 (p.14):** "The BCP should clearly indicate who can speak to the media ... Important conversations with external parties should be properly logged".
- **R02 – OCCICS Code of Practice, v1.0:**
  - **s.7.2.3(a)(iv) (p.32):** "Communication plan with internal and external stakeholders, including employees, customers and the public".
  - **s.7.2.3(e) (p.33):** "multiple channels (e.g. phone, email) are available to effectively communicate with stakeholders".
  - **Status:** this is a Code of Practice and not subsidiary legislation (s.1.1.4). It sets the planning standard for the bank's emergency response plan.
- **R02 Annex F, Part E (p.46):** "Has the incident been communicated to the media? ... Press release ... Please specify the date". The annex is the written report under Cap. 653 s.28(4) (p.43). This is why COM records the form and date.

**4. Not triggered on the C01 facts**
- **R16b – HKMA circular "Customer Data Protection", 14 Oct 2014, p.3,** and the PCPD guidance (R11) apply to privacy incidents. No data exposure is confirmed or suspected on this card. If SEC finds evidence that data was accessed, they apply, together with PH01 s.10.4.

**5. No direct rule located in assigned sources**
- I found no number of hours for the first customer alert or the first public statement. The 09:00 / 09:30 / 11:00 / 15:00 times are my professional judgment.
- I found no rule on whether the public text must name the cause as "cyber"; that choice is also judgment.
- **Files read or searched:**
  - Read in full: R05.
  - Read sections: R09 ss.1.2, 4.2–4.4, 8.2; R07 s.4.7; R06 s.8; R02 ss.7.2–7.3 and Annex F; R16b p.3; R14b p.8; R01 s.57.
  - Searched: R03, R04, R08, R13, R14b.
- **Search terms:** "press release", "public announcement", "holding statement", the regular expression "(notify|inform|alert)[a-z]* (the )?customers", "communicat", "customer", "media", "stakeholder", "emergency response plan", "emergency response", "incident", "publish", "secrecy", "public", "Code of Banking Practice", "8.2", "1.3".
- **Limitation:** R01 s.57 binds "specified persons". I found no provision of Cap. 653 that requires or prevents the operator from making a public statement.

### Internal bank procedure: PH01 Cyber Incident Response Playbook, v1.0, effective 1 Oct 2026
I recorded this support separately from the external requirements above.
- **s.3 (authority matrix):**
  - "Approve the audience for customer notices | CMT chair | LC, SEC, DPO".
  - "Approve public statements and replies to media | CMT chair; alternate COO if the chair is unreachable for 15 minutes | LC clears; SEC and Operations fact-check | Communications log".
  - "Approve staff and frontline scripts | COM | LC clears".
- **s.10.1:** "COM drafts and sends; the CMT chair approves the audience; LC clears the text; SEC and Operations confirm each factual line."
- **s.10.2:** "SMS, push and email may carry an alert but never a link."
- **s.10.3:** "Approval and scheduling are not delivery."
- **s.11.2:** "at least every six hours between 07:00 and 22:00, and at once on any change in service status".
- **s.11.3:** "It does not name the attacker, the vendor, the affected system or the bank's designation status."
- **s.13.1:** "Staff may promise this at once" (fee waiver).
- **s.13.2:** direct losses "are reimbursed on claim, with approval under 13.7".
- **s.5.8:** LC updates the HKMA "at once on ... a public statement".
- **s.2.3:** a condition without its four items "is not valid and does not hold the action".

### Conflict check
No outright conflict between PH01 and the external requirements. Two points of tension:
1. **Letter as default (PH01 s.10.2).** PH01 says written notices go by letter by default. Using letter as the main route would not be "the most effective means" (R05, R09 s.8.2.2). I resolve this within PH01 itself by sending SMS and push alerts (which s.10.2 permits), making calls and publishing the statement, and keeping letters for later written confirmation. Under PH01 s.1.3 this is to be recorded in the decision log and LC told.
2. **First release time.** PH01 sets no time for the first statement; its six-hour cadence applies afterwards. The external "shortly after commencement" governs the first release, and PH01 s.1.4 confirms internal times never extend an external deadline.

### Related item for Payments Operations (outside Q03)
Other banks and counterparties may need telling, so their customers, such as SME employees expecting salaries, can be informed (R05 p.1–2). Under PH01 s.14.1 the Head of Payments Operations makes that contact and COM controls the wording.