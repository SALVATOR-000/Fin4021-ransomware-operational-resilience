COM RESPONSE, CARD C06 (Tuesday 17 November 2026, 20:00 HKT, H+36). Locked before seeing colleagues' answers. Units answered: Q18a, Q18b only.

Both decisions are yes: a customer status update goes out tonight that matches whichever recovery position is actually approved, and the two counterparties get a verified operational notice tonight, followed by a fixed update schedule. All actions below are simulated, for the facilitator to log.

Source position for both units
- PH01 is not in my allowed manifest, so "Internal bank procedure" is N/A throughout.
- The R05 quotations were checked against the page images (PDF pages 1 to 3).
- There is no handoff for this card. I do not know SEC's recovery decision, the current queue figures, or which of my earlier updates were published, so the wording below is self-contained and uses placeholders for those facts.

---

UNIT Q18a: Customer status update for the recovery position actually approved

Decision and action
- Issue one customer status update tonight. It carries one of three "position" paragraphs, chosen by the recorded outcome of SEC's decision (Q16a).
- It does not describe the test as successful, does not say the systems are clean, and gives no completion time.
- It addresses missed payroll directly: an apology, priority handling, help with claims, and a letter confirming the bank caused the delay.
- A pause notice is drafted now, so that it can go out at once if SEC's stop or rollback criteria (Q16b) are met.

Release conditions (dependencies on this card)
1. The Q16a decision is recorded at its authorisation gate. I do not announce a restart that has not been authorised.
2. For Version 1 or Version 3, Operations confirms the stage or mode is actually live before release. We announce what is available, not what is planned.
3. If no decision is recorded by 20:45, Version 2 is issued, because "not restarted" is then the factual position.
4. SEC confirms the scope wording exactly as authorised; Operations supplies the queue figures; LC clears; the Chief Executive approves.
5. The letter of confirmation is offered only if the Chief Executive and LC approve it.

Wording, common text
"Lan Tidal Bank: service status update. Issued [HH:MM] HKT, 17 November 2026. This replaces our earlier service updates.
[Position paragraph: Version 1, 2 or 3.]
Queued payments: [number] queued instructions have been sent and [number] are still waiting. Please do not re-submit. If you have paid another way, tell us so that we can cancel the queued instruction.
Payroll: we know some business customers have missed payroll cut-offs because of this incident, and we are sorry. [Queued payroll is being sent first.] We are calling affected business customers. [On request we will give you a letter confirming that the delay was caused by the bank.]
Costs: you will not bear bank fees or charges caused by this disruption. If you incur a loss because of it, register a claim through your relationship manager, our call-back service or any branch.
Staying safe: the bank has no 'verification' page. We will never ask you to verify your account through a link, or to give a password, PIN or one-time passcode.
Next update: 07:00 HKT on 18 November, and earlier if the position changes."

Position paragraphs
- Version 1, staged recovery authorised and the first stage live: "We have started to bring the payment service back in stages. The first stage is [scope as authorised]. [What customers in that scope can now do.] Everything else remains unavailable for now. We check each stage before moving to the next and will pause if a check does not pass. We cannot yet say when the full service will be back."
- Version 2, hold: "The payment service has not been restarted. Today we tested a recovery system away from our live systems. Most test payments matched our records, but a small number did not, and we do not yet know why. We will not restart the service until we do. [Our next decision point is HH:MM.]"
- Version 3, narrower service mode: "A limited service is available from [time]: [exact scope as authorised]. New transfers through the mobile app and online banking remain unavailable. We cannot yet say when the full service will be back."

Pause notice (only if stop or rollback criteria are met)
"We have paused the restart as a precaution because one of our checks did not pass. [Payments already confirmed to you are not affected.] We will update you by [time]."
- The bracketed sentence is used only if SEC and Operations confirm it.

Status of facts
- Confirmed (card): an offline test reconciled 118 of 120 instructions; two mismatches are unexplained; no recurring encryption activity was seen during the test window; some SMEs report missed payroll cut-offs.
- Not known to me: the recovery decision; the queue figures; whether queued payroll is being prioritised.
- Not asserted: that the cause of the mismatches is harmless, or anything about security beyond the test window.

Accountable owner and executing parties
- Owner: COM.
- Approver: Chief Executive.
- Fact check: SEC and Operations. Clearance and HKMA copy: LC.
- Executing: digital channels team, contact-centre head, SME banking head (calls to payroll customers), branch network head (notices from opening tomorrow).

HKT deadlines
- 20:10: requests to SEC, Operations and LC.
- 20:45: target release, or within 15 minutes of the recorded decision.
- 21:00: latest release, using Version 2 if nothing is recorded.
- 21:30: last targeted push or SMS for tonight; later ones go at 07:30 tomorrow.
- 07:00 on 18 November: next update.

Recipients and channels
- Website status notice.
- App and internet banking notice.
- Recorded hotline message.
- Verified social media accounts.
- Press release to newsdesks.
- Targeted push or SMS with no link to customers with queued instructions.
- Relationship manager calls to SME payroll customers.
- HKMA copy via LC.

Basis, direct rules (external)
- R09, SPM TM-E-1 (statutory guideline under Banking Ordinance §7(3)), section 8.2.2, PDF p.33: AIs should "inform them of the key facts relating to the incident and the steps that customers may take". Footnote 26 names "any estimated service resumption time" and how customers can "apply for compensation for any losses incurred by the disruption".
- R05, HKMA circular (22 June 2010), PDF p.2: notices should include "the steps that affected customers need to take in the circumstances in order to gain or regain access to the relevant banking services or to protect their interests."
- R05, PDF p.1: customers should be told "whether the bank would reimburse any losses incurred by them and if so, how they can apply for compensation". This is the basis for the costs and payroll lines.
- R05, PDF p.3: "consistent and up-to-date messages are conveyed to all relevant parties on a timely basis" and "copies of public communication materials should be submitted to the HKMA for reference."
- Why these apply: the disruption continues at H+36, the service position may change tonight, and customers are reporting losses.

General principles
- R06, SPM OR-2 (non-statutory), section 8.3, PDF p.13: "Communication, where appropriate, should take place during the incident".
- R07, SPM TM-G-2 (non-statutory), section 4.3.2, PDF p.11: the alternate processing phase may entail "record reconstruction and verification, establishment of new controls, alternate manual processes". A staged or limited service is this phase, which is why I describe it as limited.

Rule applicable but a fact is missing
- R09 footnote 26 points to an estimated resumption time. None exists until SEC's decision and the mismatch analysis are done. The update therefore says so plainly and gives the next update time instead.

No direct rule located in assigned sources
- No source says how to describe test results to customers, when to announce a staged restart, or whether to offer a letter confirming the cause of a payroll delay.
- Searches recorded: "reconcil" (R09 p.19, R14b p.2, R16b p.7; none on communication), "payroll" (0 hits), "resumption time", "compensation".

Professional judgment
- "A small number did not match" is accurate and understandable. The exact test figures belong with the regulators and SEC.
- Announcing only what is live avoids a rush to a service that may be paused.
- The letter for SMEs is a practical help to employers facing staff who were not paid on time.

Internal bank procedure: N/A (PH01 absent).

---

UNIT Q18b: What to tell affected banks or counterparties about unsettled instructions

Decision and action
- Answer both counterparties tonight, but verify each request first by calling back the contact numbers the bank already holds. Impersonation linked to this incident is active.
- The head of payment operations speaks to them. I write and control the wording so that it matches our public statements. LC clears it and keeps HKMA informed.
- The same notice goes proactively to other banks and counterparties holding unsettled items.

Content of the notice
"Operational notice from Lan Tidal Bank to [counterparty]. [Date and time.] Reference [number].
1. Status: our outbound domestic payment processing has been impaired since 16 November. [Position as authorised: not restarted / staged restart from (time) / limited mode from (time).]
2. Your unsettled items: a schedule by instruction reference, amount and value date, as at [cut-off time], is being sent through [agreed secure channel]. It is provisional and subject to reconciliation. We may ask you to confirm items with us.
3. What to expect: we will tell you before releasing any batch that includes your items. Until you receive our confirmation, please treat the items as unsettled. Some originators re-submitted instructions. We check for repeats before release; if you receive what looks like a duplicate, please hold it and contact us.
4. Verification: please act only on communications from the contacts named below, verified by call-back to the numbers you already hold. We will not change settlement details during this incident.
5. A line you may give your customers: 'Payments from Lan Tidal Bank are delayed because of an incident at Lan Tidal Bank. Lan Tidal Bank is working to send them and will confirm when they have been sent.'
6. Next update: [schedule]. Contacts: [names, roles, numbers on file]."

What the notice leaves out
- Customer personal data beyond the instruction details the counterparty already needs.
- Forensic findings, the vendor credential and anything about the demand.
- The exact test figures, unless LC clears them. The notice says only that the schedule is provisional.

Conditional wording
- Item 1 follows SEC's recorded decision, as in Q18a.
- If the secure channel on our side is not confirmed as trusted by SEC, the schedule is not sent electronically. It is read over a verified call and delivered by hand or courier.

Missing fact and conditional action
- The card does not say whether the two counterparties are banks. If they are authorized institutions, the R05 sentence below applies directly. If not, R07 section 4.7.1 applies as a general principle and the notice is the same.

Status of facts
- Confirmed (card): two counterparties have asked for an operational status update on unsettled instructions.
- Not known to me: who they are; the number and value of their unsettled items; the recovery decision.

Accountable owner and executing parties
- Owner: COM (wording, consistency, log entries).
- Executing: head of payment operations (calls and notices).
- SEC confirms the channel is trusted. LC clears and informs HKMA.
- Approver: crisis management team chair.

HKT schedule
- 20:30, 17 November: both requests verified by call-back and acknowledged.
- 21:30, or within 30 minutes of the recorded recovery decision: verified call and written notice to each.
- From 18 November: updates at 08:00, 13:00 and 18:00 daily until every item is settled or returned.
- Immediately: on a stage going live, a pause or rollback, or any error affecting their items.
- 08:00 on 18 November: first proactive notice to other affected banks, or tonight where Operations already has the list.

Recipients and channels
- Named operations contacts at each counterparty.
- A verified phone call first, then written confirmation through the secure channel already agreed with that counterparty.
- Not ordinary email with attachments.
- Every contact logged.

Basis, direct rules (external)
- R05, PDF p.2, top of page (continuing the "Customer notifications" section): the AI "should also notify other affected AIs (so that they can in turn notify their affected customers) as soon as practicable."
- R05, PDF p.1: the AI should "determine as quickly as possible after identifying an incident whether the situation is likely to affect other customers or the customers of other AIs".
- Why it applies: payee banks hold unsettled items and their customers, including employees awaiting payroll, are affected. R05 says "where necessary"; two direct requests make it necessary.
- R07 section 4.7.1, PDF p.13: AIs should have "a formal strategy for communication with key external parties (e.g. regulators, investors, customers, counterparties, business partners, service providers, the media and other stakeholders)."
- R07 section 4.7.2, PDF p.14: "Important conversations with external parties should be properly logged for future reference."

General principles
- R07 section 4.3.2, PDF p.11: alternate processing may entail "different ways of dealing with customers and counterparties".
- R09 section 8.2.2, PDF p.33: consistent messages to "all relevant parties (e.g. customers, media and business partners)".
- R06 section 8.3, PDF p.13: communication plans for "all relevant stakeholders, including both internal and external parties".

No direct rule located in assigned sources
- No source prescribes the content, channel or frequency of updates to counterparties on unsettled instructions.
- Searches recorded: "counterpart" (R06 p.7; R07 pp.4, 11, 13, 14, 16, 18, 19; R09 p.24), and the regex "other affected AIs|other AIs|interbank|settlement|clearing" (R05 pp.1 to 2; R06 p.7; others unrelated).

Professional judgment
- Verifying by call-back before replying: a request for payment status is exactly what a fraudster would send this week.
- An operations lead is the right voice for operational counterparties, with communications controlling the text.
- Three fixed updates a day give counterparties something to plan around.
- Marking the schedule provisional is honest while two test mismatches remain unexplained.

Internal bank procedure: N/A (PH01 absent).

---

Simulated actions for the facilitator's log (all HKT, 17 November 2026 unless stated)
- 20:10: COM asks SEC for the recorded recovery decision and exact scope wording.
- 20:10: COM asks Operations for queue figures and each counterparty's unsettled items.
- 20:10: COM asks LC for clearance of both texts and of the SME letter.
- 20:30: counterparties' requests verified by call-back and acknowledged.
- 20:45, latest 21:00: customer status update released on Chief Executive approval; copy to HKMA via LC.
- 21:30: verified call and written notice to each counterparty.
- 07:00 on 18 November: next customer update.
- 08:00 on 18 November: first scheduled counterparty update and proactive notice to other affected banks.