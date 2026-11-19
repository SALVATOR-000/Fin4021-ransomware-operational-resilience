COM response for C02, Q06a and Q06b (Monday 16 Nov 2026, 09:30 HKT, H+1:30). I locked this response before seeing any colleague's answer.

**Handoff accepted.** The 09:00 holding statement is public and the 12:00 update is still scheduled. Two things in the handoff are not verified: whether LC clearance and the fact-check were logged before release, and which channels were actually used. I am logging both as open items. COM will reconstruct them in the communications log by 10:30 and confirm with LC, SEC and Operations.

Summary: frontline staff get a no-speculation script that is live by 09:50 HKT. The reporter gets a short written reply by 09:55 HKT, approved by the Chief Executive. Neither confirms the attacker's data claim, both avoid denying that a demand was received, and "no payment" is said only once it is verified as a present fact. All actions below are simulated, for the facilitator to log.

---
## Q06a: Instructions for branch and contact-centre staff

**Decision and action:** COM issues Frontline Script v2, which replaces the C01 script. Lines marked [C] go out only if their condition is met.

1. **"Have my funds disappeared?"**
   - Say: "Outbound local transfers and payroll are currently disrupted, so some payments you sent may not have been made yet. You can still view your balance in the mobile app or at any branch. If you see a transaction you do not recognise, tell me now and I will open a case with a reference number."
   - [C1] Add "Your deposits and account balances are not affected" only if SEC and Payments Operations log that ledger integrity is confirmed. Until then staff must not say it.
2. **"Has my data been stolen?" or "I heard there is a leak."**
   - Say: "We are investigating a cyber security incident as a priority, including any risk to customer information. If any customer's information is confirmed to be affected, we will contact that customer directly."
   - Staff do not confirm or deny the claim, and do not mention the screenshot, the ransom demand, the vendor, the system or the bank's designation status.
3. **Safety line, said on every call.**
   - Say: "We will never send you a link or ask for your password or one-time password. If anyone contacts you claiming to be the bank, hang up and call the number on the back of your card."
4. **Remediation**
   - Staff may promise at once that fees caused by the disruption will be waived.
   - Documented direct losses, such as late-payment charges, are claimed by call-back, through the relationship manager or at a branch. Each claim gets a case reference.
   - Staff must not promise reimbursement for scam losses.
5. **Media, attacker messages and escalation**
   - Every media enquiry is referred to COM. Staff do not comment.
   - Any message that claims to come from the attacker is not answered and goes to SEC straight away.
   - Unrecognised transactions go to Fraud. Urgent payroll cases go to the Payments Operations urgent queue.
6. **Distribution**
   - Branch managers' conference call at 09:45, where the script is read out.
   - A no-link SMS alert to branch managers and contact-centre supervisors telling them a new script is in force.
   - Printed copies at every counter.
   - Contact-centre floor briefing, plus a knowledge-base update if SEC logs the knowledge-base platform as clean. Otherwise printed copies.
   - Corporate email and the intranet are used only after SEC logs them safe.
   - Supervisors read the script back by 10:00, and COM logs each branch's confirmation.
7. **IVR.** The message is updated to match the holding statement and add the safety line.

**Owners**
- Script approval: COM. LC clears it.
- Facts: SEC and Head of Payments Operations.
- Delivery: branch managers and the contact-centre head.
- Gate C1 (ledger integrity): SEC with Payments Operations, by 11:30. If it is not verified by then, the line stays out (default is hold) and the question is reviewed at the 12:00 update.

**Timing (HKT):** LC clearance by 09:45, script live by 09:50, read-back by 10:00.

**Basis (external)**
- **R05**, HKMA circular 22 Jun 2010, PDF p.3, heading "Handling of customers' and media's enquiry" (checked against the scan in C01): "deploy swiftly adequate resources and communication channels (e.g. customer service hotlines and extended office hours of branch services)" and "consistent and up-to-date messages are conveyed to all relevant parties on a timely basis."
- **R09** TM-E-1 §8.2.2 (PDF p.33): "inform them of the key facts relating to the incident and the steps that customers may take".
- **R07** TM-G-2 §4.7.2 (PDF p.14): the BCP should "have pre-arrangements for redirecting external communications to designated staff".
- **Authority:** HKMA supervisory guidance. It applies because callers are already asking, and a significant incident is affecting a substantial number of customers.
- **Left to judgment:** the exact script wording and how it is distributed.

**Basis (internal)** — Internal bank procedure, PH01 v1.0:
- §3: "Approve staff and frontline scripts | COM | LC clears".
- §11.1: "Staff refer all media enquiries to COM."
- §12.3: "Staff, branches, COM and vendors never reply to an attacker; they pass any message to SEC."
- §13.1: "Staff may promise this at once."
- §13.4: "Staff do not promise reimbursement."
- §2.3: the four items for the C1 condition (who verifies, the latest time, the default, the close-out).
- No conflict with the external rules found.

**Judgment:** the data claim is unverified and has not been validated (that is SEC's Q04a). Confirming it would spread unverified, alarming facts. Denying it might later prove false. Promising direct contact if it is confirmed keeps open the bank's duty to notify customers "as soon as practicable" (R16b p.3), once the facts support it.

---
## Q06b: Reply to the reporter

**Decision:** answer in writing before 10:00. Do not give "no comment", because silence on a ransom question invites speculation. The reply is attributed to "a Lan Tidal Bank spokesperson" and given as the Chief Executive's approved statement. No interview is given. If a quote is needed, only the Chief Executive gives it.

**Proposed wording**

"Lan Tidal Bank is responding to a cyber security incident that has disrupted outbound local transfers and payroll submission since this morning. Customers can still view their balances in our mobile app, and our branches are open. [C2] The bank has not made any payment to any party in connection with this incident. We are investigating all claims made in connection with the incident and [C3] are working with the relevant authorities. We will not comment further on the details while investigations continue. We will contact any customer directly if their information is confirmed to be affected. We never send customers links or ask for passwords or one-time passwords. Our next update will be published by 12:00 HKT today."

**Conditions on the wording**
- **[C2] No-payment line.** This goes in only if, by 09:50, LC confirms with the CFO and Treasury, as a present fact taken from records, that no payment and no preparatory steps have been made.
  - If it is not verified by 09:50, replace it with: "We are not able to comment on that at this time; we will provide an update by 12:00 HKT."
  - The reply must not say or imply that no demand was received.
  - It makes no forward-looking promise about payment, because any departure from the Board's no-payment policy is for the Board alone.
- **[C3] Authorities line.** This goes in only if LC confirms that the HKMA report has been made. Otherwise it reads "are keeping the relevant authorities informed" once LC confirms that is the case. If neither is confirmed, the clause is removed.
- **Omitted on purpose:** the 6 BTC amount, the deadline, the screenshot, the vendor, the gateway and the bank's designation status. LC confirms that the wording does not prejudice any Police referral or investigation.

**Owners and approval**
- The Chief Executive approves. If the Chief Executive is unreachable for 15 minutes, the COO approves as alternate.
- LC clears the text. SEC and Operations check the facts.
- COM sends the reply and logs it.
- LC copies the reply to the HKMA at the same time, and logs it as a public-statement trigger for an HKMA update (PH01 §5.8).

**Timing (HKT)**
- Draft by 09:40.
- Approval and clearance by 09:50.
- Sent by 09:55, by phone read-out followed by written text. The written text goes from the media-relations account only if SEC has logged email safe; otherwise it is read out and sent by SMS or messaging from COM's verified mobile.
- **Default:** if approval is not given by 09:55, COM tells the reporter: "We will respond by 12:00 HKT with our next update." This holding line was already approved as part of the 09:00 statement.
- The 12:00 update stays as scheduled. COM will propose that it covers the investigation of the data claim, with conditional wording depending on the outcome of SEC's Q04a validation.

**Basis (external)**
- **R05**, PDF p.2, heading "Public announcement" (checked against the scan): the need to inform the public "may need to be weighed against the relevant legal considerations, including where appropriate whether a public announcement may prejudice any ongoing criminal proceedings or any investigation." PDF p.3: "copies of public communication materials should be submitted to the HKMA for reference."
- **R09** TM-E-1 footnote 25 (PDF p.33): the same weighing against any investigation.
- **R16b**, HKMA circular "Customer Data Protection", 14 Oct 2014, PDF p.3: where a privacy incident is serious, AIs should "notify the affected customers as soon as practicable after the AI concerned is aware of or notified of the incident".
  - How it applies: the bank has been "notified" of a claim, but the facts needed to apply the rule are unknown — whether any data was actually taken, and whose. Conditional action: if SEC validates that data was exposed, COM prepares customer notices under PH01 §10.4(a) and a public announcement for the CMT chair to approve.
- **R11**, PCPD Guidance, June 2023, PDF p.6, "Step 4": "as soon as practicable after becoming aware of the data breach". The same missing fact applies.

**Basis (internal)** — Internal bank procedure, PH01 v1.0:
- §11.3: "The bank never denies receipt of a demand. It states whether a payment has been made only as a verified present fact. It does not name the attacker, the vendor, the affected system or the bank's designation status."
- §3: replies to media are approved by the CMT chair, or the COO after 15 minutes; LC clears them.
- §11.1: "The CMT chair is the only spokesperson."
- §12.1: "Any departure is for the Board alone."
- §5.1: "COM supplies copies of public material."
- No conflict with the external rules: §11.3 is consistent with R05's caution about prejudicing investigations.

---
**Open items and dependencies, for the facilitator:**
- SEC's validation of the data sample (Q04a).
- LC's payment posture and Police referral (Q05).
- Ledger integrity for gate C1.
- Whether corporate email and the knowledge-base platform are clean.
- Whether LC's HKMA report and HKMA receipt are logged (the receipt for the 09:00 copy is still unverified).