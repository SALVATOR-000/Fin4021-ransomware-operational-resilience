## COM submission for C03: Monday 16 Nov 2026, 12:00 HKT (H+4)

I locked this before seeing colleagues' answers. All actions are simulated, for the facilitator to log. C03 has no handoff, and nothing tells me whether the C02 10:00 reply or the 09:00 holding statement went out. So the 13:00 update below stands on its own and does not refer to earlier statements.

**Facts on this card**
- **Confirmed:**
  - Independent, time-stamped logs show an unauthorised export of a file holding 80 customers' names, Hong Kong identity card (HKID) numbers and telephone numbers.
  - The attacker's sample matches bank records.
  - A vendor support credential was used in that session.
  - Mobile transfer submission is still interrupted.
- **Unverified:**
  - Whether the wider set of up to 18,000 records in the same workspace was exported.
  - Whether sessions or tokens linked to the revoked credential are still active.
  - The exact export time (SEC holds the timeline).
  - Police, PCPD and HKMA reporting status, all for LC.
  - Whether any customer's contact details have changed since the incident began.
  - Whether "no ransom paid" is still true at 13:00.

---

## Q09 a. Notifying the 80 customers directly

### My recommendation
I recommend **sending now**, to the 80 customers whose exposure is confirmed. Approving the audience is the CEO's decision under PH01 s.3. For the wider group of up to 18,000, I recommend **no individual notice yet**: wait for the scope review in PH01 s.10.4(b)–(c), with the templates ready so a send can start within two hours of a decision to widen.

Reasons for sending now:
- HKID numbers are sensitive and, combined with a name and phone number, create a real risk of identity theft and impersonation.
- The attacker holds these customers' phone numbers, so scam calls can start at any time.
- The extortion deadline is 02:00, after which the data may be published.
- Customers should hear from the bank before they hear from the media or the attacker.

### Channels (all approved under PH01 s.10.2)
1. **Personal call** from a named notification team of about eight trained staff, each with a short list of customers.
   - Calls show the bank's main hotline number.
   - The caller asks for no personal data and offers a call-back on the number on the customer's card or statement.
   - Details are given only to the named customer. Voicemail or a third party gets only a call-back request with a reference number.
2. **SMS alert after an unanswered call.** No link and no new phone number. It asks the customer to call the number on their card or statement.
3. **Letter by courier** to the verified address, for all 80 customers, including those reached by phone. The letter is the written record of the full notice.
4. **Secure-inbox notice** only if SEC logs the inbox as trusted. Otherwise letter only, which is the PH01 default.

Email is not used. Corporate email has not been logged safe, and email may carry only an alert.

**Why calls lead.** Calls are the fastest way to reach customers before 02:00. They let staff explain the risk and offer monitoring, and the call-back step gives two-way verification. The letter provides a written notice with proof of delivery.

**Language.** Bilingual, English and Traditional Chinese, following each customer's language preference on record.

### Owners
- **COM drafts and sends;** LC clears the text; SEC and Operations confirm each factual line (PH01 s.10.1).
- **The CEO approves the audience,** after consulting LC, SEC and the Data Protection Officer (DPO) (PH01 s.3).
- **Executing:** the named notification team, the Fraud team (contact-detail checks), the courier, and Operations (SMS platform).
- **Data handling:** the team works from a minimum extract (name, verified phone and address, case reference), never the HKID numbers. The extract is erased once the task is complete unless LC directs it be kept (PH01 s.17.2).

### Timing (HKT)
| Time | Action |
|---|---|
| 12:15 | Drafts ready (simulated, done) |
| 12:30 | CEO decides the audience at the CMT |
| 12:50 | LC clears the text; SEC and Operations fact-check; Fraud starts checking contact details |
| 13:00 | Calls start, timed with the 13:00 public update |
| 16:00 | First call attempt made to all 80; SMS alert sent to those not reached |
| 17:00 | All 80 letters with the courier |
| 20:00 | Second call attempt |
| 22:00 | Register summary to LC |
| Before 02:00 | Target: evidenced contact with all 80. Anyone still not reached is flagged for a relationship-manager or branch visit on 17 Nov. |

### Conditions (PH01 s.2.3)
| ID | Condition | Verifier | Latest time | Default if not met |
|---|---|---|---|---|
| N1 | Audience approved | CEO; COO as alternate chair (PH01 s.2.1) | 12:30, then escalate | At 13:15, escalate to the COO. COM logs the delay risk against the external "as soon as practicable" standard and tells LC (PH01 s.1.3). |
| N2 | Text cleared | LC | 12:50 | Hold and escalate to the CEO. This is a compliance condition, so the default is never to go ahead. |
| N3 | Each factual line confirmed: export time, data fields, "no other fields", containment, extra account checks | SEC, Fraud, Operations | 12:50 | Any unconfirmed line is removed |
| N4 | Contact details unchanged since the incident began, or cleared by Fraud (PH01 s.10.5) | Fraud | 13:30 per customer | That customer's call and SMS are held; letter goes to the address held before the incident; relationship manager follows up |
| N5 | Secure inbox trusted | SEC | 13:00 | Letter only |
| N6 | Police ask for a delay | LC logs any specific Police request; LC and CEO decide | When it arises | No delay unless such a request is logged. I recommend that no delay run past the 02:00 deadline. |

### Delivery evidence
- Batch "C03-B1 confirmed-80": one register row per customer, recording the data types, the contact details used, and the time, channel and outcome of every attempt, with proof (PH01 s.10.3).
- Approval or scheduling does not count as delivery.
- COM gives LC the notification status and the media-statement status for the PCPD form (R16a p.3).

### Core message
This is the master text for the letter and secure inbox; the call script uses the same core. LC clears it and the CEO signs it.

> **Important: your personal information – Lan Tidal Bank. Reference [case ref]**
>
> Dear [name],
>
> We are writing to tell you that some of your personal information held by Lan Tidal Bank was taken without authorisation during a cyber security incident affecting our systems. We are sorry this has happened.
>
> **What happened.** On [date/time, from SEC's verified timeline] an unauthorised party exported a file from our systems. On 16 November 2026 we confirmed from independent records that the file contained your information.
>
> **What information was involved.** Your name, Hong Kong identity card number and telephone number. [Only if SEC confirms: The file did not contain your passwords, PINs, card numbers or account balances.]
>
> **What this could mean for you.** Someone could use this information to pretend to be you, or to contact you pretending to be from us, the Police or another organisation in order to obtain more information or money.
>
> **What we have done.** We have contained the incident and are investigating with specialists. [Only if Fraud confirms: We have added extra checks before any change is made to your account or contact details.] [Only the bodies LC has logged as notified: We have reported the incident to the Office of the Privacy Commissioner for Personal Data / the Hong Kong Monetary Authority / the Police.]
>
> **What you can do.**
> - Be cautious with any call, SMS, WhatsApp message or email that mentions this incident or quotes your identity card number.
> - We will never send you a link, ask for your password, PIN or one-time password, or ask you to transfer money.
> - If anyone claiming to be from us contacts you, hang up and call the number on the back of your card or on your statement.
> - Check your account activity and tell us at once about anything you do not recognise.
> - Watch for any account, loan or credit application in your name that you did not make. Report any misuse to the Police.
>
> **Our support.** We offer you 12 months of identity-protection monitoring at our cost. To join, call our dedicated team on the number on your card or statement and quote your reference. If you suffer a loss you believe is linked to this incident, tell us and we will register a case with a reference number. You may also contact our Data Protection Officer at [address on record].
>
> [Chief Executive]

**Call script, opening:**
> "My name is [name] from Lan Tidal Bank's customer protection team. I will not ask you for any personal information, password or code. If you prefer, hang up and call us on the number on the back of your card and quote reference [X]."

After the opening, the caller gives the core points above. The caller does not promise compensation. Unauthorised transactions are handled in LC-confirmed wording (PH01 s.13.3), and scam losses are not promised (PH01 s.13.4).

**SMS alert after an unanswered call:**
> "Lan Tidal Bank: We tried to call you about an important matter concerning your personal information. Please call the number on the back of your card or on your statement and quote ref [X]. We will never send you a link or ask for your password or OTP."

### Basis: external
- **R11, PCPD Guidance on Data Breach Handling, June 2023.**
  - **p.8, "When to notify?":** "A notification should generally be given as soon as practicable after becoming aware of the incident, regardless of the progress of any internal investigation."
  - **p.8, "How to notify?":** "The data subjects can be notified directly by phone, in writing, via email or in person."
  - **p.7, contents:** the notice should include "A list of the types of personal data involved" and "Information and advice on the actions the data subjects can take to protect themselves ... from identity theft or fraud".
  - **p.5, risk of harm:** "a combination of Hong Kong Identity Card information, date of birth, address, credit card details and bank account information is more likely to result in identity theft".
  - **Authority:** PCPD guidance, which AIs are expected to take into account (R16b p.3).
  - **Trigger:** export is confirmed for the 80, so the bank is aware of a breach for them.
  - **Left to judgment:** the exact timing and mix of channels.
- **R16b, HKMA circular "Customer Data Protection", 14 Oct 2014, p.3.** Where a privacy incident is serious, including where "the customer data stolen, lost or leaked is sensitive", banks are "expected to report the incident to the HKMA and notify the affected customers as soon as practicable". HKID numbers are sensitive, so this applies.
  - **p.2:** "in case the AI concerned decided not to notify affected customers, it should provide justification on why it did not do so". For the 18,000 who are not being notified, the reason is logged under PH01 s.10.4(d).
- **R05, HKMA circular of 22 Jun 2010, p.1, "Customer notifications"** (checked against the scan in C01): notify "the customers affected or likely to be affected through the most effective means".
- **R16a, PCPD Data Breach Notification Form, p.3:** "Were the affected individuals notified? Yes / No / No, will do so within ( ) days".
- **R10, Cap. 486:** a search for "data breach" found no statutory breach-notification duty. R16b p.3 confirms there is "no statutory requirement" to report to the Privacy Commissioner.

### Basis: internal bank procedure (PH01, v1.0)
- **s.10.4(a):** customers whose exposure is confirmed "are notified as soon as practicable. They are not held back for the wider review."
- **s.10.2:** "Personal call from a named team with an offer to call back on the number on the customer's card ... SMS, push and email may carry an alert but never a link."
- **s.10.5:** "Details changed after the incident started are checked by the Fraud team before use."
- **s.13.5:** "Offered identity-protection monitoring at the bank's cost for 12 months, on opt-in."
- **s.3:** "Approve the audience for customer notices | CMT chair | LC, SEC, DPO".

**Conflict check.** No conflict. PH01's default of letter-only notice would be too slow to count as "as soon as practicable", so calls lead, which s.10.2 permits.

---

## Q09 b. What to say publicly

### Decision
Put the verified exposure into the scheduled 13:00 update, at the same time as the first calls. Describe the wider claim as unverified, without publishing the figure of up to 18,000.

The data lines go out with, or after, the start of direct notification, and no later than 14:00. If the CEO has not approved the audience by then, the 13:00 update carries the service lines only, and COM escalates to the COO.

### Channels and approval
- **Channels:** website status page, press release, official social media, app banner (if trusted), branch notices and the IVR message, plus the same lines in staff script v3 so everyone hears the same thing (R09 s.8.2.2).
- **Approval:** the CEO, or the COO if the CEO is unreachable for 15 minutes. LC clears; SEC and Operations fact-check (PH01 s.3).
- **HKMA:** COM sends a copy to LC at release, and LC sends it to the HKMA (R05 p.3; PH01 s.5.8, which requires an update "at once" on confirmed data exposure).
- **Next update:** by 19:00, which keeps within PH01 s.11.2's six-hour maximum.

### Draft public update
> "Lan Tidal Bank update – 16 November 2026, 13:00 HKT.
>
> **Customer information.** Our investigation has confirmed that during the cyber security incident an unauthorised party took a file containing the names, Hong Kong identity card numbers and telephone numbers of 80 customers. We are contacting each of these customers directly from today by phone and letter. [Only bodies LC has logged as notified: We have notified the Office of the Privacy Commissioner for Personal Data / the HKMA / the Police.]
>
> **The wider claim.** The party responsible claims to have taken more customer information. We have not verified this claim. We are urgently checking whether other customer records were taken. If we find that any other customer's information was taken, we will contact them directly.
>
> **Payment services.** Outgoing local transfers, payroll submissions and mobile transfer submission remain interrupted. You can still view balances in our app, and our branches are open. Please do not resubmit transfers you have already submitted.
>
> **What every customer can do.** Be alert to calls, SMS, WhatsApp messages or emails that mention this incident or quote your personal details, including your identity card number. We will never send you a link, ask for your password, PIN or one-time password, or ask you to transfer money. If in doubt, hang up and call the number on the back of your card. Check your account activity and report anything unusual. Fees caused by the disruption will be waived.
>
> [Only if re-verified: The bank has not paid a ransom.]
>
> Next update by 19:00 HKT."

### Release conditions
| ID | Line | Verifier | Latest time | Default if not verified |
|---|---|---|---|---|
| S1 | The figure "80" and the three data types | SEC, from the log record (PH01 s.11.4) | 12:45 | "a number of customers – the figure is being checked and will be given by 19:00" |
| S2 | Name of each body notified | LC logs each notification | 12:50 | Line omitted. The PCPD line needs the submitted form, because the PCPD does not accept oral notifications (R11 p.8). |
| S3 | "Has not paid a ransom" | CEO and CFO re-verify | 12:50 | Line omitted. Receipt of the demand is never denied. |
| S4 | Direct calls to the 80 have started | COM notification team | 13:00 | Data lines move to the start of calls, no later than 14:00 |

### Why the 18,000 figure is not published now (professional judgment)
- It is the number of records stored in the workspace, not a count of exposed customers.
- PH01 s.10.4(c) says the size of a data store does not by itself define who is affected.
- PH01 s.11.4 allows a figure to be published only once its owner has confirmed it from a record.
- Publishing it now could cause disproportionate alarm.

The update is still truthful. It discloses the claim and the check, and it gives every customer protective advice. Whether the public statement covers customers who have not been notified individually is the CEO's decision under PH01 s.10.4(d); I recommend that it does, as drafted.

**Reactive line if asked how many records the location held:**
> "That location also holds records of other customers. We have not confirmed that any of those were taken and are checking urgently. We will publish verified figures as soon as they are confirmed."

The record count is re-decided at the 19:00 update, alongside the scope review.

**Triggers for an immediate public update and wider notification:**
- SEC finds evidence the wider set was exported.
- The data is published or offered for sale, including after the 02:00 deadline.
- Misuse is reported.
- The CEO decides to widen the scope after the 12-hour review, due no later than 24:00 (PH01 s.10.4(b)).

### What the update never includes
- The vendor, the credential, the affected system or the bank's critical infrastructure status (PH01 s.11.3).
- The amount of the demand or its deadline.
- "No other customers affected".

### Summary for the facilitator log
- **Confirmed:** 80 customers' names, HKID numbers and phone numbers taken; transfers still interrupted.
- **Being verified:** the wider claim and the time for restoring service.
- **What customers can do:** watch for impersonation, check their accounts, never share credentials, and call the number on the back of their card.

### Basis
- **External:**
  - **R16b p.3:** "If a large number of customers are affected, the AI concerned should consider making a public announcement". The 80 alone is not a large number. The update is still warranted because of the earlier public statements, the extortion and the wider claim.
  - **R11 p.8:** if data subjects "are not immediately identifiable or if public interest exists, then public announcements ... may be more effective".
  - **R09 s.8.2.2, p.33:** "consistent and up-to-date messages".
  - **R05 p.2, quote checked against the scan:** "include the key facts of the incident".
  - **R16a p.3:** "Has your company/organisation issued or does your company/organisation intend to issue a media statement?" COM gives LC the answer.
- **Internal bank procedure (PH01, v1.0):** s.10.4(c) "An unverified claim, or the size of the data store, does not by itself make everyone in the store a notification batch"; s.10.4(d) "The CMT chair decides whether a public statement under section 11 covers customers not notified individually"; s.11.4; s.11.3; s.5.8.
- **Conflict check:** no conflict.
  - **Data-breach sources:** R11 and R16b set no rule on publishing a data-store size. PH01's evidence-based scope agrees with R11's risk-of-harm assessment in Step 3.
  - **R11 p.7 and naming the vendor:** R11 p.7 says a notice "may include" the source of the breach. That is optional, so describing the source as "our systems" without naming the vendor is consistent with it.

---

## No direct rule located in assigned sources
- I found no fixed number of hours for notifying customers of a data breach. Both R11 and R16b say "as soon as practicable". My times are professional judgment, set against the 02:00 extortion deadline.
- I found no rule on whether to publish the size of an unverified data store.
- **Search terms:** "data breach" (R10), "notif" (R11, R16b), "notified" and "data subjects" (R16a), and "ransom" and "extortion" across all documents.
- **Read:** R11 pp.1–8, R16b pp.1–3, R16a p.3, and PH01 ss.10, 11, 13 and 17.