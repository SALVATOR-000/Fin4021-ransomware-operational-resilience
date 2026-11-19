# Lan Tidal Bank Limited — Cyber Incident Response Playbook (PH01)

Internal bank procedure. Version 1.0, approved by the Chief Executive on behalf of the Board Risk Committee, effective 1 October 2026. Owner: Head of Information Security. Next review: 30 September 2027.

Lan Tidal Bank Limited is a fictional bank. This playbook is exercise material.

## 1. Purpose, status and use

1.1 This playbook sets the bank's own operating procedure for a cyber incident that disrupts a critical operation or exposes customer data. It covers who decides, in what order, through which channel, and what record is kept.

1.2 It is an internal procedure. It does not create, restate or replace any statutory, supervisory or regulatory requirement. Where it refers to an external requirement it names the document only; staff must read and apply the external document itself.

1.3 Where this playbook and an external requirement differ, the external requirement prevails. The person who notices the difference records it in the decision log and tells the Head of Legal and Compliance at once.

1.4 Internal times in this playbook are the bank's own targets. They never extend an external deadline.

## 2. Incident command

2.1 **Crisis Management Team (CMT).** Chair: Chief Executive; alternate: Chief Operating Officer. Members: Head of Information Security (SEC), Head of Legal and Compliance (LC), Head of Corporate Communications (COM), Head of Payments Operations, Head of IT Operations, Chief Risk Officer, Data Protection Officer. The chair convenes the CMT within 30 minutes of a severity 1 or 2 declaration (section 4).

2.2 **Decision log.** The CMT keeps one master decision log from the first minute. Every decision is entered with: decision, owner, time (HKT), condition if any, recipient and channel, and status (executed, scheduled, held, not executed). Other registers (evidence, regulator contacts, customer notifications, cases) are cross-referenced to it.

2.3 **Preconditions.** Before an action is made to wait on a condition, the condition is logged with four items: who verifies it; the latest time by which it must be verified; the default action if it is not verified by then; and a close-out entry when it is verified or the default is applied. A condition without these four items is not valid and does not hold the action. The default action may be to go ahead, to hold, or to switch to an alternate process approved under section 8. Reconciliation, security and applicable compliance conditions, including every item of the gate in 9.3, stay in force when their time passes: for these the default is to hold or to switch to an approved alternate process, never to go ahead. Where the default is to go ahead, the missing confirmation or evidence is obtained and logged afterwards. Reports to regulators and authorities are never held by an internal condition; they follow 2.4.

2.4 **External reports are not held by internal confirmation.** Internal review of a report to a regulator or authority runs in parallel with the report, not before it. The initial report goes on the facts held at the time, with unverified items marked as unverified; the results of internal checks go in the next update. No internal condition, review or approval may delay an action needed to meet an external deadline. If an internal condition is still open 30 minutes before the external deadline, the default in 2.3 applies and the report goes by a route that meets the requirement for that report (5.6).

2.5 **Status reports.** SEC reports to the chair every hour until containment is confirmed, then every four hours. Each report states what has changed, what is confirmed, what is unverified and what is due next.

## 3. Authority matrix

| Decision | Decides | Must be consulted | Record |
|---|---|---|---|
| Isolate a system or segment | SEC | Head of IT Operations; CMT chair if a working customer service will be removed | Decision log, emergency change record |
| Release evidence held under section 6 | SEC and LC jointly | Forensic lead | Evidence register |
| Activate alternate payment processing (section 8) | CMT chair, on SEC's written security clearance | Head of Payments Operations | Decision log; BCP activation entry (4.4) |
| Approve the audience for customer notices | CMT chair | LC, SEC, DPO | Decision log |
| Approve public statements and replies to media | CMT chair; alternate COO if the chair is unreachable for 15 minutes | LC clears; SEC and Operations fact-check | Communications log |
| Approve staff and frontline scripts | COM | LC clears | Communications log |
| Any payment to an attacker | Board only (section 12) | LC written legal gates | Board minute |
| Any contact with an attacker | CMT chair, in writing | LC and SEC joint recommendation | Decision log |
| Report to the Police | LC | CMT chair informed | Regulator contact register |
| Share incident data with a forensic firm or other third party | LC and SEC jointly | DPO | Evidence register, data release record |
| Return a recovered system to production | CMT chair after the gate in 9.3. No gate condition may be waived. The Board may narrow the scope of recovery; the narrower scope must still pass every check in 9.3 that applies to it | SEC, Head of Payments Operations | Decision log, change record; Board minute for any change of scope |
| Reinstate vendor access | CMT chair on SEC's written sign-off (7.5) | LC on contract terms | Decision log |
| Customer remediation in the categories of section 13 | Approvers and limits in 13.7 | LC | Case register |
| Customer remediation in any other category | CMT chair; counts towards the incident total in 13.7, and the Board approves anything above that total | LC, CFO | Decision log |
| Escalate to the Board | CMT chair | LC | Decision log |

## 4. Severity, tolerance and BCP activation

4.1 **Severity 1:** a critical operation is disrupted, or customer personal data is confirmed or suspected to be exposed, or an extortion demand is received. **Severity 2:** a critical operation is degraded but working, or a security event affects a critical system without confirmed disruption. **Severity 3:** other security events.

4.2 **Critical operations and tolerance for disruption (Board-approved).**

| Critical operation | Maximum tolerable disruption |
|---|---|
| Outbound domestic transfers and SME payroll submission | 24 hours |
| Customer access to balances (mobile and branches) | 8 hours |
| Card authorisation | 4 hours |

4.3 When a disruption reaches 50% of its tolerance, the CMT chair tells the Board chair. When it reaches 100%, the CMT chair convenes the Board or its Risk Committee (section 15).

4.4 **BCP activation is declared, not assumed.** The CMT chair declares activation of the business continuity plan in the decision log, with the time and the operation concerned, whenever alternate processing, an alternate site or a manual workaround is authorised for a critical operation. LC is told at once so that any external reporting that follows from activation is made.

## 5. Regulator, authority and external reporting

5.1 **Ownership.** LC owns every report to a regulator or authority and the Regulator Contact Register (RCR). SEC supplies technical facts; COM supplies copies of public material.

5.2 **External requirements to apply.** LC applies these documents directly, as they stand on the day: the Protection of Critical Infrastructures (Computer Systems) Ordinance (Cap. 653), section 28 and Schedule 6, and the Commissioner's Code of Practice section 7.3 and its Annexes E and F; the HKMA circular "Incident response and management procedures" (22 June 2010); SPM TM-E-1 section 8.2; SPM TM-G-2 section 1.3; the HKMA circular "Customer Data Protection" (14 October 2014); the PCPD Guidance on Data Breach Handling and the Data Breach Notification Form. This playbook does not restate their triggers, recipients or time limits.

5.3 **Deadline tracker.** At declaration LC opens a deadline tracker. Each external clock is computed from its own starting point as stated in the external document, entered with its source reference, and checked by a second LC officer within 30 minutes.

5.4 **Contacts and channels.** The RCR holds the current names, numbers, out-of-hours routes and filing addresses for the HKMA supervisory team, the Commissioner's office, the PCPD and the Police Cyber Security and Technology Crime Bureau. It is printed and kept in the CMT room and in the LC duty pack, so it is available if corporate systems are down.

5.5 **Evidence of every contact.** For every call, filing or letter LC records: time, channel, the name and post of the person reached, any reference number, a summary of what was said or sent, and the receipt. For an electronic filing, LC saves the system's submission receipt or dispatch record at the moment of filing. If no receipt is shown, LC asks the recipient for one in the same call or by return, and logs the request.

5.6 **Submission route and standby device.** For each written report, LC first confirms from the external document the form and the way of submission that report requires, and records them in the deadline tracker. Compliance keeps a standby filing device that is not connected to production systems. At declaration Compliance tests the standby device and logs whether it works and is enrolled for each designated channel likely to be needed; if it is not, Compliance arranges another permitted route at once and logs it. If the normal filing terminal is unavailable or under evidence hold, SEC logs within 30 minutes whether it can be released. If no decision is logged by then, LC submits from the standby device, but only if the device has been logged as working and the route meets the requirement for that report. Otherwise LC uses another route that meets the requirement, or asks the recipient which alternative it accepts and logs the answer. The receipt is saved under 5.5.

5.7 **Email.** SEC logs within 30 minutes of declaration whether corporate email is safe to use. Until it is logged as safe, written material goes by a route that does not depend on corporate email and meets the requirement for that report (5.6). An open email check never delays a report.

5.8 **Updates to the HKMA.** After the first report, LC updates the HKMA supervisory contact every four hours during the first 24 hours, then at 08:00 and 18:00 daily until the HKMA agrees otherwise, and at once on any of: BCP activation, confirmed data exposure, an extortion demand, a change in service status, a public statement.

5.9 **Later evidence.** Facts found after a report are sent as supplementary information by the route the external document sets. LC keeps one list of what each authority has been told and when.

## 6. Evidence, forensics and timeline

6.1 **Evidence hold.** At declaration SEC places an evidence hold on affected systems. No reboot, rebuild, restore, failover or deletion on a held system without SEC's logged release for that item.

6.2 **Containment comes first.** Collection of volatile evidence before containment is capped at 10 minutes. If destructive activity is still spreading, containment goes first and evidence is taken from the isolated system afterwards.

6.3 **Custody.** The evidence custodian is an SEC designate who does not administer the affected systems. Every item gets an evidence ID, source, time with clock offset, collector and witness, tool, SHA-256 hash, storage location and a transfer record. Analysis is on verified copies only.

6.4 **Clocks.** All bank systems synchronise to the bank's primary time source. Every timeline entry keeps the original timestamp, the measured offset, the normalised HKT time and its uncertainty. Events closer together than their combined uncertainty are recorded as "order undetermined".

6.5 **Retained forensic firm.** The bank has a master services agreement with a Hong Kong forensic firm. The agreement already contains the data terms in section 16. SEC may call the firm in without further approval at severity 1. This paragraph applies to the forensic firm only; suppliers of the affected systems are covered by 6.7.

6.6 **Attacker material.** Samples, demands and messages from an attacker are received only into the evidence process. Nobody requests further samples, visits attacker links or uploads attacker material to an outside service.

6.7 **Evidence held by suppliers.** This covers any supplier that supports, hosts or has remote access to an affected system.
(a) **Request.** Within one hour of declaration SEC drafts a written preservation and production request for each such supplier, covering session and access logs, account records, support tickets, change records and any bank data the supplier holds. LC clears the wording. The vendor relationship owner sends it to the contract contact in the third-party register kept by the Chief Risk Officer, and confirms receipt by call-back to a number already on file.
(b) **Channel.** Records come in only as native exports with a SHA-256 manifest, through a bank-hosted encrypted transfer or on bank-issued encrypted media collected by the evidence custodian. They are never received by ordinary email or through the supplier's own remote access path. The custodian enters them in the evidence register on receipt.
(c) **Escalation.** If the contract terms (log retention, audit and production rights) or the delivery status cannot be confirmed by the due time in the request, and in any case within four hours, the vendor relationship owner escalates to LC and the CMT chair. LC decides on formal contractual notice; the CMT chair decides any other step.
(d) **Reconciliation.** Supplier records are treated as the supplier's account until SEC has reconciled them with the bank's own logs.

## 7. Containment, credentials and vendor access

7.1 **Isolation order.** SEC isolates at the network layer first: the affected segment and the route used. Hosts are not powered off. Services still working are kept running unless SEC finds active spread to them.

7.2 **Vendor remote access standard.** Vendor access to bank systems uses individual named accounts, multi-factor authentication and time-limited sessions through the privileged access system, with session recording. Shared vendor accounts are not permitted.

7.3 **On suspicion of a compromised credential.** SEC captures session and token state (10 minutes at most), then terminates all sessions, revokes tokens and keys, and disables the account and every other account of the same vendor. The vendor's remote path is blocked at the perimeter. If no preservation request has yet gone to that vendor, SEC issues one under 6.7 at the same time.

7.4 **Closure test.** A credential is closed only when a replayed token and a logon with the old credential both fail, and the result and time are logged. Until then the access window is treated as open.

7.5 **Reinstatement.** Vendor access is reinstated only when: the cause of the compromise is known; the access meets 7.2; secrets readable by the old access are rotated; and SEC signs off in writing.

## 8. Alternate payment processing

8.1 **Purpose.** The alternate payment process sends verified outbound domestic transfers and payroll when the payment gateway cannot. Its rated capacity and operating steps are in the Payments Operations runbook.

8.2 **Activation.** The CMT chair activates it under section 3, after SEC's written clearance that it shares no hosts, accounts, keys or network path with any affected system. Activation is a BCP activation under 4.4.

8.3 **Pilot.** The first batch is a pilot of at most 20 instructions, reconciled end to end before full operation. Each gate passed and the pilot result are logged with the time.

8.4 **Priority order.** (1) SME payroll, earliest value date first; (2) other instructions with a value date of today or the next business day; (3) everything else in order of submission. Up to 10% of hourly capacity is kept for urgent cases referred by branches and the contact centre. Order is never set by customer size.

8.5 **Verification.** Each instruction is checked against the customer's original authenticated instruction. Payroll batches are confirmed with the SME's authorised contact by call-back to a number already on file.

8.6 **Duplicates and unknown status.** Payments Operations keeps one instruction register for all sources. Each instruction is released once only, under a unique processing ID. Before a suspected duplicate or a retried instruction is released, two checks are made and logged:
(a) intent: the customer, or the SME's authorised contact, confirms by call-back to a number already on file which instruction they want paid;
(b) status: the ledger and an independent receiving-side record show whether the original instruction was already posted or settled.
If either check is incomplete, or the status of an instruction cannot be established, the instruction is held. Items in flight at the failure are held as status unknown until an independent record shows they did not settle.

8.7 **Reconciliation and stop.** Released count and value are reconciled against ledger debits and receiving-side acknowledgements every hour. Any unexplained difference stops all releases until it is explained and logged. SEC or the Head of Payments Operations may stop without prior approval and then tells the chair.

## 9. Recovery and return to production

9.1 **Candidate order.** (1) A new build from trusted media with data from the immutable backup, in an isolated recovery environment; (2) the standby system, only if (1) fails, under the same checks. An affected system is never repaired in place for return to service.

9.2 **Offline testing and pass mark.** Before production data, or an extract of it, is used in testing, SEC records in the test record that the data has been de-sensitised and the de-sensitisation checked, and that the information owner approved its use in advance (SPM TM-G-1 section 4.2.4 applies). If either entry is missing, that data set is not used and testing with it is held. A candidate passes offline testing only if reconciliation shows no unexplained difference. One unexplained difference is a fail. A sample result is recorded as a sample, not as a pass of the whole set.

9.3 **Gate.** Production use needs all of these, each logged with evidence and signer: offline pass under 9.2; integrity and separation checks passed; rollback rehearsed to the target set in 9.5 (the alternate process if it holds a current security clearance under 8.2, otherwise suspension of releases); delta reconciliation and live test plans ready; business acceptance by the payments information owner; LC's confirmation of regulatory steps; the CMT chair's authorisation. Missing any item means hold: releases from the recovered system stay suspended, or service continues on the alternate process if it holds a current security clearance under 8.2 and its own reconciliation ties. Passing the time set for an item does not release the gate (2.3). The Board may narrow the scope of recovery, for example to payroll only; the narrower scope must still pass every item above that applies to it. Reports to regulators and authorities continue under 2.4 whatever the state of the gate.

9.4 **Stages.** (1) pilot of 20 instructions; (2) payroll and time-critical items at a capped rate with hourly reconciliation; (3) mobile transfer submission reopened with limits; (4) full service. Each stage advances only on the chair's decision after the previous stage has run clean for the period set in the change record.

9.5 **Stop and rollback.** Releases from the recovered system stop at once on any of: a security indicator from the incident; one unexplained reconciliation difference; any duplicate, replayed or wrong payment; an instruction whose status cannot be established. SEC, the Head of Payments Operations or the IT Operations duty manager may stop without prior approval. Rollback disconnects the recovered system from payment interfaces. Service then returns to the alternate process only if that process holds a current security clearance under 8.2 and its own reconciliation ties; otherwise rollback means all releases are suspended. In-flight items are classified as settled, not settled or unknown from independent records, and unknown items are held (8.6). Restart needs a new pass through 9.3.

## 10. Customer notification

10.1 **Who.** COM drafts and sends; the CMT chair approves the audience; LC clears the text; SEC and Operations confirm each factual line.

10.2 **Approved channels.** Personal call from a named team with an offer to call back on the number on the customer's card; notice in the authenticated secure inbox; letter. SMS, push and email may carry an alert but never a link. The secure inbox is used only after SEC logs that it is trusted; by default (2.3), written notices go by letter.

10.3 **Delivery register.** From the first notice, COM keeps a register with one row per customer: batch, data types, contact details used, each attempt with time, channel and outcome, and proof of delivery. Approval and scheduling are not delivery. Completion figures go to LC daily.

10.4 **Widening the notification scope.**
(a) Customers whose exposure is confirmed, and customers for whom there is evidence that their data was accessed, copied or misused, are notified as soon as practicable. They are not held back for the wider review.
(b) No later than 12 hours after the first confirmation of exposure, the DPO and LC review, with SEC's evidence, whether the scope should be widened. The CMT chair decides and logs the decision and the reasons.
(c) For a larger group whose exposure is possible but not shown, the scope is set by evidence and risk: evidence that their records were accessed or copied; publication or offer of the data; reports of misuse; the sensitivity of the data types; and whether their records were held in the same place as confirmed records. An unverified claim, or the size of the data store, does not by itself make everyone in the store a notification batch.
(d) Where part of the group is not notified yet, the reason is logged, and the decision is reviewed whenever new evidence arrives and at least every 24 hours until the scope is settled. The CMT chair decides whether a public statement under section 11 covers customers not notified individually.

10.5 **Changed contact details.** Contact details are taken only from the bank's verified records. Details changed after the incident started are checked by the Fraud team before use.

10.6 **Duplicates.** A customer with evidenced delivery of current content gets nothing further until there is something new. A customer with no evidenced delivery gets one consolidated notice.

## 11. Public statements and media

11.1 The CMT chair is the only spokesperson. Staff refer all media enquiries to COM.

11.2 **Cadence.** While a critical operation is disrupted, COM publishes a dated status update at least every six hours between 07:00 and 22:00, and at once on any change in service status. Each update states what is confirmed, what is being verified, what customers can do and when the next update is due.

11.3 **Fixed lines.** The bank never denies receipt of a demand. It states whether a payment has been made only as a verified present fact. It does not name the attacker, the vendor, the affected system or the bank's designation status.

11.4 **Figures.** A figure is published only if its owner has confirmed it from a record. Otherwise the update says the figure is being checked and when it will be given.

11.5 **Closing update.** A closing update is issued only when: the service runs in production and SEC confirms it is stable; queued instructions are settled or returned; the notification register shows evidenced delivery to all affected customers; every open case has a named owner; and LC confirms the regulators have been told. Until then updates continue.

## 12. Ransom and extortion

12.1 **Policy.** The Board's policy is that the bank does not pay a ransom. Any departure is for the Board alone.

12.2 **Legal gates before the Board may consider a departure.** LC confirms in writing: the position under the Organized and Serious Crimes Ordinance (Cap. 455), including any disclosure and consent; screening of the recipient under the United Nations (Anti-Terrorism Measures) Ordinance (Cap. 575); sanctions screening by external counsel; the Police view; and the insurer's position. Treasury holds all preparatory steps (virtual-asset accounts, purchases, intermediaries) until the Board decides.

12.3 **Contact with an attacker.** None, unless the CMT chair authorises it in writing on a joint LC and SEC recommendation, for a stated limited purpose, after consulting the Police. Contact is made only by one designated specialist on a segregated channel, with a full transcript. Staff, branches, COM and vendors never reply to an attacker; they pass any message to SEC.

12.4 **Insurer.** The CFO notifies the cyber insurer within 24 hours of declaration.

## 13. Customer remediation (pre-approved)

13.1 **Fees.** Bank fees and charges caused by a disruption of a critical operation are waived. Staff may promise this at once.

13.2 **Direct losses from the bank's disruption.** Documented direct losses caused by the disruption, including late-payment charges from a missed payroll cut-off, are reimbursed on claim, with approval under 13.7.

13.3 **Unauthorised transactions.** Handled under SPM TM-E-1 section 4.4 and the Code of Banking Practice, in wording LC confirms.

13.4 **Scam losses where the customer made the payment.** Assessed case by case by the Head of Fraud with LC. Staff do not promise reimbursement.

13.5 **Customers whose data is confirmed exposed.** Offered identity-protection monitoring at the bank's cost for 12 months, on opt-in.

13.6 **Claims route.** Claims are registered by call-back, relationship manager or branch, each with a case reference.

13.7 **Approval limits.** Two limits apply at the same time, and every payment must pass both.

| Limit | What it measures | Within the limit | Above the limit |
|---|---|---|---|
| HKD 50,000 per customer | The total approved for one customer in this incident, across all categories in this section | Head of Payments Operations for 13.2; Head of Fraud with LC for 13.3 and 13.4 | CMT chair |
| HKD 5 million per incident | The running total for all customers: amounts paid or approved under this section, fees waived under 13.1, the cost of the service under 13.5, and any remediation in other categories approved under section 3 | The approvers in the row above | Board or its Risk Committee, which approves a revised total |

A payment that would take a customer above HKD 50,000 needs the CMT chair. A payment that would take the incident total above HKD 5 million needs the Board's revised total first, whatever its size. If both limits are crossed, both approvals are needed. The CFO keeps the running total and tells the CMT chair when it reaches HKD 2.5 million and HKD 4 million. While a revised total is awaited, claims continue to be registered and acknowledged, and customers are told when to expect a decision.

## 14. Counterparties and other banks

14.1 The Head of Payments Operations handles operational contact with counterparties and other banks; COM controls the wording.

14.2 Every incoming request is verified by call-back to a number already on file before any reply.

14.3 Counterparties holding unsettled items receive a verified call and a written notice the same day, then updates at 08:00, 13:00 and 18:00 until every item is settled or returned.

## 15. Board escalation

15.1 The CMT chair tells the Board chair within two hours of any of: severity 1 declaration; confirmed customer data exposure; an extortion demand; 50% of a tolerance reached.

15.2 The Board or its Risk Committee meets within 12 hours of: 100% of a tolerance reached; any decision reserved to the Board; a request from a regulator.

15.3 The Board paper states: the disruption against tolerance; data position; payment posture; authorities engaged and deadlines; decisions required. Legal advice is in a separate privileged section.

## 16. Third parties holding incident data

16.1 Data goes to a forensic firm or other third party only under a signed agreement that limits use to the incident and to the bank's instructions, requires confidentiality, keeps processing in Hong Kong, forbids sub-contracting and onward disclosure without consent, requires immediate reporting of any loss, gives the bank audit rights, and requires return or destruction with a certificate.

16.2 By default the firm receives a minimised data set with customer personal data masked. Full images are examined only inside the bank's laboratory. A full copy leaves the bank only with LC's and SEC's written approval.

## 17. Records, legal hold and retention

17.1 LC issues a written legal hold at declaration to all custodians, the vendor and any forensic firm. It overrides routine deletion, log rotation and backup recycling for systems in scope.

17.2 **Retention by type of record.** Each type of record is kept for its stated purpose and no longer than that purpose and any legal hold require. Personal data in incident records is kept only as far as the purpose actually needs it; the Personal Data (Privacy) Ordinance (Cap. 486) and any applicable preservation requirement apply.

| Record | Purpose | Review | Destruction or release condition |
|---|---|---|---|
| Decision log, CMT and Board papers | Accountability; regulatory inquiry; post-incident review | Three months after the incident is closed, then yearly | Seven years after closure, if no investigation, inquiry or claim is pending and LC approves |
| Notification evidence: filings, receipts, call records, deadline tracker | Proof of what was reported, to whom, when and how | Three months after closure, then yearly | Seven years after closure, on the same conditions |
| Original forensic images and logs containing customer personal data | Investigation, legal proceedings, regulatory inquiry | One month after declaration, then quarterly | When LC confirms that no investigation, proceeding or inquiry needs them and the legal hold is lifted, and not before any minimum retention an applicable external document sets for that record. Where analysis must continue, masked extracts replace the originals |
| Third-party copies (forensic firm, vendor, insurer) | The engagement for which they were provided | At the end of each engagement and whenever LC asks | Returned or destroyed within 30 days of the end of the engagement or of LC's request, with a destruction certificate, unless LC directs preservation |
| Working copies and extracts of customer data | Analysis and customer notification | Monthly | Erased as soon as the task is complete, unless LC directs preservation |

17.3 Records are released for disposal only on LC's written confirmation and the record owner's approval, and are destroyed securely with a certificate.

## 18. Handover and stand-down

18.1 The CMT hands over to standing teams only when each open item has a named receiving owner who has signed acceptance of a specific list.

18.2 Each handover pack starts with a page listing what is not evidenced. Items without evidence transfer as open, not done.

18.3 Restrictions stay in force after handover until their release condition is met and the decision-maker in section 3 has logged the release.

18.4 At handover LC takes over the register of external deadlines and commitments item by item, checking for each its owner, its due date and the evidence of any submission. Each item is followed up by its own due date, not only at the weekly review. Each change deployed to a critical computer system during the incident is entered as a separate item with its own deployment date, and LC decides for each whether it must be notified, applying Cap. 653 section 22 and the HKMA Code of Practice for Designated AIs section 6.1. LC reviews the whole register weekly until all statutory reports are filed.

18.5 The CMT reconvenes at once on any security trigger, any missed external deadline or any new data exposure.

## Annex A — Decision log fields

Entry number; HKT time; decision; owner; condition (owner, deadline, default, close-out); recipient and channel; status; evidence reference.

## Annex B — Evidence custody fields

Evidence ID; description; source system; acquisition time (HKT) and clock offset; collector; witness; tool and version; SHA-256; storage location; each transfer (from, to, time, purpose, signatures); each access.
