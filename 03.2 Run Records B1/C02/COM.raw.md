## COM submission for C02: Monday 16 Nov 2026, 09:30 HKT (H+1:30)

I locked this before seeing colleagues' answers. All actions are simulated, for the facilitator to log.

**Facts on this card**
- **Confirmed:**
  - Outgoing local transfers and payroll submission are disrupted.
  - Customers can view balances in the mobile app, and branches are open.
  - The attacker has demanded 6 BTC by 02:00 HKT on 17 Nov.
  - The secure filing channel is available again.
  - Branch staff are getting calls asking whether funds have disappeared.
  - A reporter wants a comment by 10:00 HKT on whether the bank has paid a ransom.
- **Unverified:**
  - The attacker's claim that customer files were copied, and where the screenshot came from (SEC is validating under Q04a).
  - Whether customer balances and ledger records are intact.
  - Whether the bank has reported to the Police.
  - Whether any disclosure under Cap. 455 or Cap. 575 has been made.
  - When service will be restored.
- **From the handoff:**
  - The condition for the "authorities" line is met: the HKMA call was logged by 08:30.
  - No card records that LC cleared the C01 holding statement, so it is not known whether it went out at 09:00 or through which channels.

**My first action at 09:30.** COM's duty officer checks the live website, the app banner and the communications log, takes time-stamped screenshots and logs the result. Every line below that points to "our website" is used only if this check shows the statement is live.

**Correction from C01.** My C01 condition was "hold the text and escalate", but no clearance was ever recorded, so nothing could be verified. This time every clearance is a named, timed entry in the communications log. Each condition has an explicit default under PH01 s.2.3. For legal checks the default is the narrower wording, never an unchecked release.

---

## Q06 a. Instructions for branch and contact-centre staff

### Decision and action
Staff get the instructions in two steps.

**Step 1: interim instruction, issued 09:35.** This is procedural only and adds no new facts. COM's duty officer gives it by phone cascade to the eight branch managers and the contact-centre supervisor. Each confirms receipt by 09:45. The instruction is:
- Use only the confirmed lines.
- Do not speculate about funds, data, a ransom or the cause.
- If a customer says something looks wrong, open a case and give a reference number.
- Refer media to the COM media desk.
- Pass any contact from the attacker to SEC.
- Fees caused by the disruption may be promised as waived (PH01 s.13.1 allows this at once).

**Step 2: full script v2, issued 09:55.**
- Same text as the 10:00 public reply in Q06b, so staff hear it before the media do.
- Sent by staff mobile broadcast and phone cascade, not corporate email unless SEC has logged email as safe. Recipients are all branch staff, contact-centre agents, relationship managers and the SME payroll call team.
- Read out at branch huddles at 10:05.
- The IVR message is updated to match.
- Every branch manager and the contact-centre supervisor confirm receipt by 10:15, logged with the time.
- The script is marked internal and not to be forwarded.
- It is reissued with every public update and on any trigger below. The latest reissue is with the 13:00 update.

**Staffing.** I recommend that Operations add contact-centre agents now and that the CMT consider longer branch hours today.

### Script v2: what staff say
- **Confirmed:**
  - "Since this morning, outgoing local transfers and payroll submissions are disrupted following a cyber security incident affecting some of our systems."
  - "You can check your balance and recent transactions in our app or at any branch."
  - "Fees caused by this disruption will be waived."
  - "If the disruption has caused you a direct loss, such as a late-payment charge, we will register a claim and give you a case reference."
- **If a customer asks whether their money has disappeared:**
  - "Outgoing transfers are disrupted – that is what we are fixing. Let's check your balance and recent transactions now. If anything looks wrong, I will open a case with a reference number and our fraud team will investigate."
  - On liability for unauthorised transactions, staff use only wording LC confirms (PH01 s.13.3).
  - Staff must **not** say "your money is safe" or "nothing has been taken".
  - **Conditional line.** It is released only when the Head of Payments Operations logs it from the reconciliation record: "Our checks so far have found no unexplained movement of customer funds."
- **If asked about data:**
  - "We are investigating, including whether any customer information is affected. Nothing has been confirmed. If we confirm your information is affected, we will contact you directly by phone or letter. We will never send you a link."
  - "Be alert to any call or message that mentions this incident or quotes your personal details and asks for passwords, one-time passwords, card details or a payment. Hang up and call the number on the back of your card."
- **If asked about a ransom, a demand or the attacker:**
  - Staff use the exact line approved for Q06b (main or fallback version).
  - Staff never deny that a demand was received.
  - Staff never say what the bank will do in future.
  - Staff never give the amount, the deadline, the attacker, the vendor, the affected system or the bank's critical infrastructure status.
- **What the customer can do:**
  - Check their balance and transactions now and report anything unusual.
  - Not resubmit transfers already submitted.
  - Have urgent payments logged in the urgent register with a case reference.
  - Ask for their e-banking to be suspended if they suspect fraud. Staff use the standard suspension process with strong authentication.
- **Staff must not:**
  - Talk to the media or post on social media.
  - Reply to, or open links or attachments from, anyone claiming to be the attacker. Pass it to SEC.
  - Act on calls from people claiming to be the vendor, a regulator, the Police or another bank without calling back on a number already on file.
  - Change customer contact details without the Fraud check.
- **Record:** each call's time, the question, the line used and any case reference, plus where the customer heard the "missing funds" story. COM uses this to track the rumour.

### Owners
- **Accountable:** COM approves the script and LC clears it (PH01 s.3).
- **Fact-check:** SEC and the Head of Payments Operations.
- **Executing:** branch managers and the contact-centre supervisor.

### Conditions (PH01 s.2.3)
| Condition | Verifier | Latest time | Default | Close-out |
|---|---|---|---|---|
| LC clears script v2 | LC | 09:50 | Staff stay on the interim instruction (procedural lines and PH01 fixed positions only); script v2 is held | Communications log entry |
| Factual lines checked | SEC and Head of Payments Operations | 09:50 | Any unconfirmed line is deleted | Fact-check record |
| "No unexplained movement of funds" line | Head of Payments Operations, from the reconciliation record | When it is logged | Line not used | Decision log |

### Basis: external
- **R05, HKMA circular "Incident response and management procedures", 22 Jun 2010.** PDF p.3, heading "Handling of customers' and media's enquiry". Quote checked against the scan: "deploy swiftly adequate resources and communication channels (e.g. customer service hotlines and extended office hours of branch services)" and "consistent and up-to-date messages are conveyed to all relevant parties on a timely basis".
  - **Authority:** HKMA supervisory circular.
  - **Why it applies:** this is a significant incident and branches are already getting enquiries.
  - **Left to judgment:** the timing and the channels.
- **R09, HKMA SPM TM-E-1, V.4.** s.8.2.2, PDF p.33: "consistent and up-to-date messages are conveyed to all relevant parties (e.g. customers, media and business partners) on a timely basis".
  - **s.4.4.2, p.17:** a "convenient and easily accessible channel ... available at all times for customers to seek and obtain help with respect to possible unauthorized transactions".
  - **s.4.4.3, p.18:** "a mechanism for customers to promptly suspend their e-banking accounts in cases where fraudulent or suspicious activities are detected".
  - **Why it applies:** customers fear their funds have gone, so they need a way to report unauthorised transactions and to suspend e-banking.
- **R07, SPM TM-G-2.** s.4.7.3, p.14: "how the status of recovery can be promptly and consistently communicated to all staff, ... branches". It names "broadcasting of messages to mobile phones of staff" as a channel. This is a general principle.

### Basis: internal bank procedure (PH01, v1.0)
- **s.3:** "Approve staff and frontline scripts | COM | LC clears".
- **s.11.1:** "Staff refer all media enquiries to COM."
- **s.11.3:** "The bank never denies receipt of a demand."
- **s.11.4:** a figure is published only if confirmed from a record.
- **s.12.3:** "Staff, branches, COM and vendors never reply to an attacker; they pass any message to SEC."
- **s.13.1:** "Staff may promise this at once."
- **s.13.4:** "Staff do not promise reimbursement."
- **s.10.5:** changed contact details are checked by Fraud.
- **s.8.6:** duplicate instructions, the reason for "do not resubmit".

### Professional judgment
- **Calling back on known numbers** for inbound callers (by analogy with PH01 s.14.2): attackers often follow up by posing as vendors, regulators or the press.
- **Tracking where the rumour came from.**
- **Treating the interim instruction as needing no new clearance.** It contains no new customer-facing facts. LC confirms this afterwards and the confirmation is logged.

---

## Q06 b. Answering the reporter by 10:00

### Decision
Yes: answer before 10:00 with a short written statement attributed to Lan Tidal Bank. The Chief Executive remains the only spokesperson and there is no interview at this stage.
- **Same text everywhere:** the same text is posted at 10:00 as a dated update on the website status page and given to any other media.
- **If the 09:00 statement is not live:** it becomes the bank's first public statement, combined with the C01 service content.
- **Why not stay silent:** the "missing funds" calls show a rumour is spreading. The reporter's question implies the reporter already knows of the extortion. "No comment" risks being read as a denial, which PH01 s.11.3 forbids.

### Executing steps
| Time | Action |
|---|---|
| 09:35 | COM calls the reporter back through the outlet's published newsroom number to confirm who they are. COM acknowledges the enquiry and promises a statement by 10:00, with no substance. |
| 09:35 | COM requests the verifications listed in the conditions table below |
| 09:50 | CMT chair approves the text. If the chair has been unreachable for 15 minutes since 09:35, the COO approves. |
| 10:00 | Reply sent by phone and as written text from the media desk (corporate email only if SEC has logged it safe). Same text goes on the website and to staff. |
| 10:00 | At release, COM sends a copy to LC, who forwards it to the HKMA by the HKMA-confirmed route (R05 p.3; PH01 ss.5.1 and 5.8). |
| 10:00 | Communications log entry: "Reply to press enquiry was made/issued", dated 16/11/2026, for Part E of LC's Annex F report |
| 13:00 | Next public update (scheduled), keeping the same lines |

**Sequencing.** LC should tell the HKMA about the demand (PH01 s.5.8, "at once") before 10:00. If LC has not done so, it tells the HKMA at the moment of release. The reply is not held for this.

### Owners
- **Approves:** the CMT chair, or the COO if the chair is unreachable for 15 minutes.
- **Clears and fact-checks:** LC clears; SEC and Operations fact-check (PH01 s.3).
- **Executing:** the COM media desk.

### Conditions (PH01 s.2.3)
| ID | Line | Verifier | Latest time | Default if not verified |
|---|---|---|---|---|
| P1 | "The bank has not paid a ransom" | CMT chair, with written confirmation from the CFO that no payment and no preparatory step has occurred (PH01 ss.11.3, 12.1, 12.2) | 09:50 | No substantive reply. At 10:00 the reporter is told a statement will follow by 10:30. Never denied. |
| P2 | Confirms that a demand was received | LC, with the Police view if available | 09:50 | Use the fallback wording below |
| P3 | "Reported to the Police" | LC logs that a Police report was made (PH01 s.3) | 09:50 | Use "working with the relevant authorities" (HKMA call already logged) |
| P4 | The unverified claim that data was copied | CMT chair decides (PH01 s.10.4(d)); LC clears | 09:50 | Line held for reactive use only |
| P5 | No tipping-off | LC confirms the text reveals nothing about any disclosure made under Cap. 455 s.25A or Cap. 575 s.12 | 09:50 | Any line LC flags is removed |

### Main wording (all conditions met)
> "Lan Tidal Bank statement, 16 November 2026, 10:00 HKT. Since this morning, outgoing local transfers and payroll submissions have been disrupted following a cyber security incident affecting some of our systems. We have received a demand from a party claiming responsibility. The bank has not paid a ransom. The matter has been reported to the Police and we are working with the relevant authorities. We are urgently investigating a claim that customer information was copied; it has not been verified. If we confirm that any customer's information is affected, we will contact those customers directly. Customers can still view balances in our mobile app and our branches are open. Please do not resubmit transfers already submitted. Fees caused by this disruption will be waived. We will never send you a link or ask for your password or one-time password; be alert to any message about this incident asking for personal details or payment. Next update by 13:00 HKT today."

### Fallback wording (default if P2 or P4 is not cleared)
> "...disrupted following a cyber security incident affecting some of our systems. The bank has not paid a ransom. This is a criminal matter; we are working with the relevant authorities and will not comment on further details at this stage. [Customer lines as in the main wording.] Next update by 13:00 HKT today."

### What the reply never includes
- The amount or the 02:00 deadline.
- The attacker, the vendor, the affected system or the bank's critical infrastructure status.
- Any future intent, such as "will not pay". The Board alone decides any departure from the no-ransom policy, and LC's payment recommendation (Q05a) is still open.
- "Funds are safe" or "no data was taken".

**Summary for the facilitator log**
- **Confirmed in the reply:** the disruption, that the app and branches work, that no ransom has been paid (once P1 is verified), and the fee waiver.
- **Being verified:** the data claim and the restoration time.
- **What the audience can do:** not resubmit transfers, ignore links and requests for credentials or payment, and use the app or branches.

### Basis: external
- **R05, PDF p.2, heading "Public announcement".** Quote checked against the scan: "the need to keep the public informed may need to be weighed against the relevant legal considerations, including where appropriate whether a public announcement may prejudice any ongoing criminal proceedings or any investigation" and "If in doubt, AIs should consult the Hong Kong Monetary Authority (HKMA)." This supports the P2 check and the fallback.
  - **R05 p.3:** "copies of public communication materials should be submitted to the HKMA for reference."
- **R09.** s.8.2.2 (consistent messages to customers and media) and footnote 25 on p.33 (the same weighing of legal considerations for a press release).
  - **Authority:** HKMA SPM. s.1.4.2: "AIs should comply with the requirements in this module".
- **R16c, Cap. 455 Organized and Serious Crimes Ordinance, s.25A(5), PDF p.84.** A person "commits an offence if, knowing or suspecting that a disclosure has been made under subsection (1) or (4), he discloses to any other person any matter which is likely to prejudice any investigation".
- **R16d, Cap. 575 United Nations (Anti-Terrorism Measures) Ordinance, s.12(5), PDF p.37.** Same effect: the person "shall not disclose to another person any information or other matter which is likely to prejudice any investigation".
  - **Authority (both):** statute.
  - **Missing fact:** whether any such disclosure has been made, which is for LC under Q05.
  - **Conditional action:** under P5, public text must not mention any such disclosure, consent request or wallet details.
- **R07 s.4.7.2, p.14:** "The BCP should clearly indicate who can speak to the media ... Important conversations with external parties should be properly logged". General principle.
- **R02 Annex F, Part E, PDF p.46:** "Reply to press enquiry was made/issued ... Please specify the date". This is why COM records the date.
- **R11, PCPD Guidance, June 2023, p.8, "When to notify?":** "as soon as practicable after becoming aware of the incident, regardless of the progress of any internal investigation".
  - **R16b, HKMA circular "Customer Data Protection", p.3:** "notify the affected customers as soon as practicable after the AI concerned is aware of or notified of the incident".
  - **Missing fact:** whether a breach has actually occurred. SEC's validation under Q04a decides this.
  - **Conditional action:** if SEC confirms that rows match real customer records, those customers are notified as soon as practicable (PH01 s.10.4(a)). COM prepares the notice now (call, letter, and SMS/push alerts with no link) and updates the public statement at once.

### Basis: internal bank procedure (PH01, v1.0)
- **s.3:** "Approve public statements and replies to media | CMT chair; alternate COO if the chair is unreachable for 15 minutes | LC clears; SEC and Operations fact-check".
- **s.11.3:** "The bank never denies receipt of a demand. It states whether a payment has been made only as a verified present fact."
- **s.12.1:** "Any departure is for the Board alone."
- **s.12.2:** "Treasury holds all preparatory steps".
- **s.10.4(c):** "An unverified claim ... does not by itself make everyone in the store a notification batch."
- **s.5.8:** LC updates the HKMA "at once on any of: ... an extortion demand, ... a public statement".

### Professional judgment
- **Confirming the demand.** I recommend it because a denial is barred, evasion damages credibility, and customers need it to stay alert to scams. Legal and Police concerns are handled by the fallback.
- **Mentioning the data claim proactively,** with "not verified" stated clearly. I expect the attacker to publicise the claim, and the C01 statement already says the bank is checking whether data is affected.
- **Confirming the reporter's identity** before giving the statement.

---

## Conflict check
- **No conflict found that requires overriding PH01.**
- **Tipping-off.** PH01 is silent on tipping-off. Cap. 455 s.25A(5) and Cap. 575 s.12(5) take precedence (PH01 s.1.3), so I added check P5 and logged it to LC.
- **Data notification timing.** R11 and R16b expect notification "as soon as practicable", while PH01 s.10.4(c) scopes notification by evidence. There is no conflict yet because no breach has been confirmed. If SEC validates the sample, the external timing governs and PH01 s.10.4(a) is consistent with it.

## No direct rule located in assigned sources
- I found no external rule on whether to confirm a ransom demand publicly, or on how quickly to answer a press enquiry. The 10:00 deadline is the reporter's, not a regulatory one.
- **Searched all documents for:** "ransom", "extortion", "public announcement", "press release", "holding statement". In R09 I also searched "staff" and "suspend".
- **Read:** R05 pp.1–3 (checked against the scan), R09 pp.16–18 and 32–33, R07 pp.13–14, R11 pp.5–8, R16b p.3, R16c pp.83–84, R16d p.37.
- **What the searches found:** "ransom" appears only in PH01 s.12 and in incident-classification and form text in R02, R04, R11, R14b and R16a. None of these governs public statements.

## Simulated log entries
| Time | Entry |
|---|---|
| 09:30 | Statement-status check logged |
| 09:35 | Interim staff instruction issued by phone cascade |
| 09:35 | Reporter's identity confirmed and enquiry acknowledged |
| 09:35 | Verification requests P1–P5 sent |
| 09:50 | Clearances and approval; defaults applied where not verified |
| 09:55 | Script v2 broadcast |
| 10:00 | Reply and website update released; copy to LC for the HKMA; Annex F log entry |
| 10:15 | Staff receipt confirmations |
| 13:00 | Next public and staff update (scheduled) |