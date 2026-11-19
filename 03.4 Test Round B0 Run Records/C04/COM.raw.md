COM response for C04, Q12a and Q12b (Monday 16 Nov 2026, 18:00 HKT, H+10). I locked this response before seeing any colleague's answer.

Summary: the 18:00 public update should be released at once as a complete restatement, because the only prior update we can verify is the 09:00 statement. For customers who cannot get through, the bank should add hotline staff and IVR call-backs, have relationship managers call SMEs with payroll due, and extend branch hours. All actions below are simulated, for the facilitator to log.

**Handoff reviewed.**
- **Verified prior status:** only the 09:00 holding statement, released on the Chief Executive's approval. The channels used and LC's clearance before release are not verified. The receipt for the HKMA copy is not verified.
- **Not verified:** the 12:00 update, my proposed 13:30 data update, and Frontline Scripts v2 and v3. No card records their clearance or release.
- **Consequence:** the 18:00 update must work on its own. It restates the service status and the confirmed data exposure in full, and does not refer to anything "previously announced" except the 09:00 statement.
- **Possible cadence breach.** If the 12:00 update was not issued, the public may have had nothing since 09:00. That would miss the six-hour cadence (latest 15:00) and the "next update by 12:00" promise.
  - COM logs this as a possible breach. COM tells LC so that LC can tell the HKMA under PH01 §5.8 if it is confirmed.
  - The 18:00 update goes out at once, without waiting to find out whether the 12:00 update was released.

---
## Q12a: Public service-status update

**Decision:** publish a dated status update by 18:45 HKT.
- Approval: the Chief Executive approves, or the COO if the Chief Executive is unreachable for 15 minutes. LC clears the text, and SEC, the DPO and Payments Operations check the facts.
- Channels: the same channels as 09:00. The website is used only if SEC has logged it clean; otherwise press release by a non-email route. Plus branch notices, the IVR first message and social media with links only to the bank homepage.
- Copy to the HKMA through LC at release.
- Frontline Script v4 goes out with the same lines at the same time. COM approves it and LC clears it.
- Next update: by 22:00 tonight, then from 07:00 on 17 Nov. It is issued at once if the secondary process starts or stops, or if service status changes.

**Core wording (common to both versions)**

"Update at [time] HKT, 16 November 2026.

**Confirmed**
- Outbound local transfers, payroll submission and mobile transfer submission remain interrupted following the cyber security incident we reported this morning.
- Balances can be viewed in the mobile app and at branches.
- Our investigation has confirmed that a file containing the names, Hong Kong identity card numbers and telephone numbers of [80 / a small number of] customers was copied without authorisation. We are contacting those customers directly.

**Being verified**
- A claim that more customer information was taken has not been verified, and we are investigating it urgently. Any customer whose information is confirmed to be affected will be contacted directly.
- [The number of instructions waiting / restoration time] is being checked and will be given by [time].

**What you can do**
- Please do not resubmit a payment you have already made, even if your screen timed out. Instructions you have already submitted, including repeated attempts, are being checked so that each payment is made only once.
- We may call you on the number held in our records to confirm a payment or payroll batch. We will never ask for your password, PIN or one-time password, or send you a link. If you are unsure, hang up and call the number on the back of your card.
- Fees caused by the disruption are waived. Documented direct losses, such as late-payment charges, can be claimed through our hotline, your relationship manager or a branch.
- [Extended hours / call-back service — see Q12b.]

Next update by 22:00 HKT."

**Version A: use only if the CMT chair has logged activation of the secondary process** (Q10a, BCP declared under PH01 §4.4):

"We have started processing waiting payment instructions through an alternative process, after checking each one. Payroll for businesses, earliest pay date first, and payments due today or tomorrow are handled first. Payments are being released gradually. We will contact you if we need to confirm an instruction."

**Version B: use if the process is not activated, or is activated but stopped:**

"We are preparing an alternative way to process waiting payments, subject to security and accuracy checks. We will update you as soon as processing starts."

**Rules applied to the wording**
- The figures (4,200 instructions, 400 per hour, the 80 customers) are published only if their owners confirm them from a record. Payments Operations owns the queue and capacity figures; SEC owns the "80".
- No time for completing processing is promised.
- No mention of the vendor, the gateway, the bank's designation status or the demand. "No payment" is stated only as a verified present fact.
- The 18,000 workspace figure is not published.

**Release condition**
- Version A is used only once COM sees the logged activation entry and the pilot result. Otherwise Version B goes out by 18:45 without waiting for Q10.
- PH01 §2.3 entries for this condition:
  - Verifier: COM, from the decision log.
  - Latest time: 18:40.
  - Default: Version B. The update goes ahead; it is not held.
  - Close-out: an entry in the communications log.

**Basis (external)**
- **R05**, HKMA circular 22 Jun 2010 (quotes checked against the scan in C01):
  - PDF p.2, heading "Public announcement": include "the key facts of the incident and the steps that affected customers need to take in the circumstances in order to gain or regain access to the relevant banking services or to protect their interests".
  - PDF p.3, heading "Handling of customers' and media's enquiry": "consistent and up-to-date messages are conveyed to all relevant parties on a timely basis" and "copies of public communication materials should be submitted to the HKMA for reference."
- **R09** TM-E-1 §8.2.2 (PDF p.33): "inform them of the key facts relating to the incident and the steps that customers may take". Footnote 26 gives examples: "any estimated service resumption time and … how customers can protect their interests (e.g. apply for compensation…)".
- **Why these apply:** the disruption has continued for 10 hours, and stopping duplicate payments and scams needs customers to act.
- **Left to judgment:** the timing and exact wording.

**Basis (internal)** — Internal bank procedure, PH01 v1.0:
- §11.2: "at least every six hours between 07:00 and 22:00, and at once on any change in service status. Each update states what is confirmed, what is being verified, what customers can do and when the next update is due."
- §11.4: figures only once confirmed from a record.
- §11.3: fixed lines.
- §3: replies and statements approved by the CMT chair, with the COO as alternate.
- §8.5 and §8.6(a): call-back "to a number already on file". This is the basis for the "we may call you" line.
- §13.1 and §13.2: fee waiver and reimbursement of direct losses.
- No conflict with the external rules found.

---
## Q12b: Reaching and helping customers who cannot use the usual channels

**Decision: activate the measures below, starting 18:30 HKT.**

1. **Contact-centre surge**
   - Redeploy trained back-office and branch staff to the hotline tonight.
   - The IVR first message plays the 18:00 update and offers a **call-back registration** option. The bank calls back on the number on file, in the same priority order as PH01 §8.4. The customer can instead hang up and call the number on their card.
   - The contact centre runs extended hours tonight and opens early on 17 Nov.
2. **SME payroll outreach**
   - Payments Operations gives relationship managers the list of SMEs whose payroll is value-dated today or tomorrow.
   - Relationship managers call each SME's authorised contact on the number on file by 21:00, so the SMEs do not need to get through to us.
   - A dedicated SME payroll line is staffed by relationship managers and Payments Operations.
3. **Branches**
   - Extend hours at all eight branches tonight (proposed: to 20:00) and open early on 17 Nov. Times are confirmed by the COO and branch network.
   - Branch phone overflow is routed to the central team.
   - A queue marshal and a priority desk handle urgent payroll, elderly customers and customers without mobile banking.
4. **Urgent-case route.** Branch and contact-centre staff refer urgent cases into the capacity PH01 §8.4 reserves for referrals, if the secondary process is activated. If it is not, cases are logged for first processing.
5. **Proactive alert.** A no-link SMS goes from verified records to customers with queued instructions: "Lan Tidal Bank: your payment instruction is waiting and will not be lost. Please do not resubmit. Info: call the number on the back of your card." There are two exceptions:
   - The 80 customers with exposed data are reached only through their direct notice, because their phone numbers are held by the attacker.
   - Contact details changed after 08:00 go to Fraud for checking first.
6. **Social media.** Social media is monitored. Replies give only general information and the number on the card, and never ask for account details in public.

**Owners**
- Decision: COO as BCP owner, under the CMT chair.
- Delivery: Heads of the contact centre and branch network, and Payments Operations for the SME list.
- Scripts, IVR text, SMS text and branch notices: COM; LC clears.

**Timing and trigger (HKT)**
- Measures live by 18:30–19:00. SME calls completed by 21:00.
- COM reviews the hourly call-abandonment and branch-queue figures. If the abandonment rate does not fall within 2 hours, COM recommends more staff or longer hours to the CMT at 21:00. The threshold is my judgment.

**Basis (external)**
- **R05**, PDF p.3, heading "Handling of customers' and media's enquiry" (checked against the scan): "it is therefore essential for the AI concerned to deploy swiftly adequate resources and communication channels (e.g. customer service hotlines and extended office hours of branch services) to handle such enquiries."
- **R09** TM-E-1 footnote 24 (PDF p.32): "deploy swiftly adequate resources and communication channels (e.g. customer service hotlines)".
- **R05**, PDF p.1, "Customer notifications": "proactively notify the customers affected or likely to be affected through the most effective means".
- **Why these apply:** call volumes have doubled and customers report they cannot reach branches. That shows the current resources are not adequate.
- **No direct rule located in the assigned sources** on call-back registration or abandonment thresholds; those are professional judgment. Files searched: PH01, R05, R06, R07, R09 and the whole manifest. Search terms: "customer", "communicat", "contact centre|branch|hotline", "alternative channel|alternative means|contingency arrangement".

**Basis (internal)** — Internal bank procedure, PH01 v1.0:
- §8.4: "Up to 10% of hourly capacity is kept for urgent cases referred by branches and the contact centre. Order is never set by customer size."
- §10.2: SMS "may carry an alert but never a link".
- §10.5: contact details changed after the incident started are checked by Fraud.
- §13.6: claims registered "by call-back, relationship manager or branch".
- §3: COM approves frontline scripts and LC clears them.
- No conflict with the external rules found.

**Judgment:** customers who cannot get through are better helped by the bank calling them back. That also cuts repeat calls and retried payments. Every contact must be one a customer can check against the number on their card, because exposed phone numbers make scam calls pretending to be the bank likely.

---
**Open items for the facilitator:**
- The secondary-process decision (Q10), which decides between Version A and Version B.
- Confirmed figures from Payments Operations and SEC.
- Whether the 12:00 update and the data update were released, and whether a missed update needs reporting to the HKMA (LC, Q11b).
- Whether the website is clean.
- Branch extension times (COO).
- The 50% tolerance point for transfers falls at 20:00 HKT. The CMT chair tells the Board chair then (PH01 §4.3). This is not a COM action, but the public wording must not contradict it.