COM response for C06, Q18a and Q18b (Tuesday 17 Nov 2026, 20:00 HKT, H+36). I locked this response before seeing any colleague's answer. No handoff was received.

Summary: the customer update can only say that payments from the recovered system are still on hold, because the laboratory result fails the bank's own pass mark. Counterparties holding unsettled items get a verified call and a written notice tonight, then updates three times a day. All actions below are simulated, for the facilitator to log.

**Recovery position as COM reads it from the card**
- The offline laboratory test reconciled 118 of 120 instructions. The 2 differences are unexplained.
- Under PH01 §9.2, "One unexplained difference is a fail." A sample result is recorded as a sample, not as a pass of the whole set.
- So the PH01 §9.3 gate cannot be met. Production use of the recovered image is on **hold**.
- The approved position (SEC Q16a and the CMT chair) has not been released to COM. COM therefore prepares the versions below and publishes only the one matching the logged decision.
- COM will not draft public wording for staged production from this image while the gate is unmet. That would describe an action PH01 §9.3 does not allow.

---
## Q18a: Customer status update

**Release time and approval**
- Released by 21:00 HKT on 17 Nov (before the 22:00 end of the daily update window).
- Chief Executive approves; COO if the Chief Executive is unreachable for 15 minutes. LC clears the text. SEC and Payments Operations check the facts.
- Next update by 07:00 HKT on 18 Nov, or at once on any change in service status.

**Channels**
- Website notice if SEC has logged it clean.
- Press release by a non-email route.
- Bank-controlled social media with links only to the homepage.
- IVR, branch posters and Frontline Script v6.
- In-app banner with no link, if SEC logs the messaging platform trusted.
- Relationship managers call SMEs whose payroll was missed (list from Payments Operations).
- Copy to the HKMA through LC.

**Core text (all versions)**

"Update at [time] HKT, 17 November 2026.

**Confirmed**
- Outbound local transfers, payroll submission and mobile transfer submission are still disrupted.
- Balances can be viewed in the app and at branches.
- We are sorry that this has now gone on for more than a day, and that some businesses missed payroll deadlines.

**What you can do**
- Do not resubmit payments you have already made. Each instruction is checked so it is paid only once.
- Businesses that missed a payroll deadline can call their relationship manager or [SME line]. We will register a claim for documented direct losses caused by the disruption, such as late-payment charges, and give you a case reference. [Include the next line only if LC clears it:] We can provide a letter confirming that the delay was caused by the bank.
- Fees caused by the disruption are waived.
- We will never ask you to verify your account through a link, or ask for your password, PIN or one-time password. Use only the number on the back of your card."

**Version 1: HOLD.** This is the expected version under PH01 §9.2–9.3.

"Testing of our restored payment system has identified items that need further checking before we can use it. We will not restart it until every check is complete, so that every payment is made correctly and only once. [If the alternate process is running with current security clearance and its reconciliation ties:] Meanwhile we continue to process waiting payments through our alternative process, with business payroll and payments due soonest first. [If it is not:] Waiting payments remain queued and safe. They will not be lost, and we will process them as soon as checks allow."

**Version 2: NARROWER MODE.** Used only if the CMT chair logs it, and only if it runs on the alternate process with current security clearance under §8.2 and tied reconciliation, or on a Board-narrowed scope that passes every item of §9.3 that applies.

"We have restarted [business payroll / payments due today] at a limited rate, with checks every hour. Other transfers and mobile transfer submission remain unavailable. We will extend service step by step once each stage has run without problems."

**Version 3: STAGED PRODUCTION RECOVERY.** Not drafted for release. COM releases it only after the logged §9.3 gate, with all items signed, including a fresh offline pass with no unexplained difference. If the gate is passed:

"We have begun restoring our payment system in stages, starting with a small number of payments that are checked one by one."

**What is never published**
- The 118/120 laboratory figures, which are internal test data.
- Any restoration time.
- The vendor, the system and the bank's designation status.
- Any figure not confirmed from a record (PH01 §11.4).

**Basis (external)**
- **R05**, HKMA circular 22 Jun 2010, PDF p.2, heading "Public announcement" (checked against the scan in C01): include "the key facts of the incident and the steps that affected customers need to take … to gain or regain access to the relevant banking services or to protect their interests". R05 p.1: advise "whether the bank would reimburse any losses incurred by them and if so, how they can apply for compensation". R05 p.3: copies of public materials to the HKMA.
- **R09** TM-E-1 §8.2.2 and footnote 26 (PDF p.33): steps for customers, including "how customers can protect their interests (e.g. apply for compensation for any losses incurred by the disruption)".
- **Why these apply:** the disruption has lasted beyond 24 hours and SMEs have suffered losses.
- **Left to judgment:** the wording and the time of release.

**Basis (internal)** — Internal bank procedure, PH01 v1.0:
- §9.2: "One unexplained difference is a fail."
- §9.3: "Missing any item means hold … The Board may narrow the scope of recovery … the narrower scope must still pass every item above that applies to it."
- §9.4: the stages.
- §11.2 to §11.4: cadence, fixed lines and confirmed figures.
- §13.1, §13.2 and §13.6: fee waiver, reimbursement of direct losses (including "late-payment charges from a missed payroll cut-off") and the claims route.
- No conflict with the external rules found.

**Release condition**
- COM reads the CMT chair's logged decision by 20:45.
- If there is none, Version 1 goes out by 21:00. Under PH01 §2.3 the default is to publish the hold position. Silence would breach the cadence.

---
## Q18b: Message to affected banks and counterparties

**Decision**
1. Before any reply, Payments Operations verifies **both requesting counterparties** by calling back a number already on file. Unverified requests get no reply.
2. **Every** bank or counterparty holding unsettled items, not just the two that asked, then receives a verified call and a written notice **tonight (17 Nov, by 23:00 HKT)**.
3. After that, updates at **08:00, 13:00 and 18:00 HKT** daily until every item is settled or returned.

**Owners**
- Operational contact: Head of Payments Operations.
- Wording: COM. LC clears it.
- List of items and their status: Payments Operations, from its single instruction register.
- Settled, not settled and unknown status: established from independent records under PH01 §8.6.

**Channel**
- Verified call first.
- Written notice by the counterparty's established operational or interbank channel, or by corporate email only if SEC has logged it safe. Otherwise by a secure route agreed in the call, with the route logged.
- No attachments containing more customer data than the counterparty already holds for its own items.

**Wording of the written notice**

"Lan Tidal Bank: operational status, [date/time] HKT.

1. Our outbound domestic transfer and payroll processing remains disrupted following a cyber security incident. Recovery is under way, subject to reconciliation checks.
2. Your unsettled items with us are listed in the attached schedule [references only]. Each is marked SETTLED, NOT SETTLED or STATUS UNKNOWN, based on our ledger and independent records.
   - Items marked NOT SETTLED will be processed once only, or returned. We will tell you which.
   - Items marked STATUS UNKNOWN are held. Please do not treat them as settled, and please send us your receiving-side record for them, so that we can establish their status and avoid duplicates.
3. Please do not act on any payment request or instruction claiming to come from Lan Tidal Bank unless you have checked it by calling us on the number you hold on file.
4. Contact: [named Payments Operations officer, number on file].

Next update: 08:00 HKT, 18 November 2026, and at once on any change."

**Not disclosed:** customer personal data beyond the item references, the vendor, the system, the bank's designation status, the demand, and the laboratory figures.

**Notify other banks whose customers are affected**
- If any receiving bank's customers are affected (for example, employees of SMEs with missed payroll whose salaries go to accounts at that bank), Payments Operations includes that bank in the notice, so that it can deal with its own customers' enquiries.

**Basis (external)**
- **R05**, PDF pp.1–2, heading "Customer notifications" (checked against the scan): "Where necessary, the AI should also notify other affected AIs (so that they can in turn notify their affected customers) as soon as practicable."
- **R07**, SPM TM-G-2 V.2, §4.7.1 (PDF p.13): a "formal strategy for communication with key external parties (e.g. regulators, investors, customers, counterparties …)" so "consistent and up-to-date messages are conveyed". §4.7.2 (PDF p.14): "Important conversations with external parties should be properly logged".
- **Why these apply:** unsettled interbank items and missed payroll affect other banks and their customers.
- **Left to judgment:** which channel to use and the 23:00 deadline for tonight's notice. No source sets either.

**Basis (internal)** — Internal bank procedure, PH01 v1.0:
- §14.1: "The Head of Payments Operations handles operational contact with counterparties and other banks; COM controls the wording."
- §14.2: "Every incoming request is verified by call-back to a number already on file before any reply."
- §14.3: "Counterparties holding unsettled items receive a verified call and a written notice the same day, then updates at 08:00, 13:00 and 18:00 until every item is settled or returned."
- §8.6: items in flight are "held as status unknown until an independent record shows they did not settle".
- §5.7: corporate email only once SEC logs it safe.
- No conflict with the external rules found.

---
**Open items for the facilitator:**
- The CMT chair's logged recovery decision (Q16), which selects the customer-update version.
- Whether the alternate process holds a current security clearance and whether its reconciliation ties.
- The register status for counterparty items.
- LC's clearance of a confirmation letter for SMEs.
- Whether the earlier updates and the Q15 notices were released and delivered.
- The 24-hour transfer tolerance passed at 08:00 on 17 Nov, which brings in Board convening under PH01 §4.3 (LC's Q17b). The public wording does not refer to it.