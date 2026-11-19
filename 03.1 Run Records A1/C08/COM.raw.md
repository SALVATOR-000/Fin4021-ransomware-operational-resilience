COM RESPONSE, CARD C08 (Thursday 19 November 2026, 08:00 HKT, H+72). Locked before seeing colleagues' answers. Units answered: Q24a, Q24b only.

I would not publish a closing update: the service is still on hold and the record shows no public update since 07:00 HKT on 18 November, so regular updates continue and one goes out now. Unresolved cases and messaging are handed to named standing owners with a pack that marks unevidenced items as open, not done. All actions below are simulated, for the facilitator to log.

Source position for both units
- PH01 is not in my allowed manifest, so "Internal bank procedure" is N/A throughout.
- The R05 quotations were checked against the page images (PDF pages 1 to 3).
- I rely on the handoff for the live position: hold, unchanged at 08:00 on 19 November. The card's test results describe the test environment only.
- The handoff also shows what is not recorded: queue figures, the public data updates, case outcomes, the remediation decision, and delivery evidence for every notification batch.

---

UNIT Q24a: Closing status update, or continue regular updates

Decision and action
- No closing update. Continue regular updates and publish one now.
- Reasons: the payment service has not been restarted; customer cases are open; delivery of the breach notices is not evidenced; vendor credential questions and regulatory follow-ups are unresolved.
- The second test is described as a test result, not as a restart and not as proof that systems are secure.
- A closing update will be proposed to the Chief Executive only when all of these are true:
  1. The service is running in production and SEC confirms it is stable.
  2. Every queued instruction is settled or returned and reconciled.
  3. The notification register shows evidenced delivery to all affected customers.
  4. Every open case has a named standing owner and the customer knows who it is.
  5. LC confirms the regulators know the bank is moving to normal communications.
- Even then, the closing text says what remains open and that support continues.

Release conditions (dependency on Q22a)
- The position paragraph follows the recorded production decision. Version 1 is the recorded position and is used unless SEC's decision changes it before release.
- Version 2 or 3 is released only once Operations confirms the service is actually live.
- Operations supplies queue figures. LC clears the text. The Chief Executive approves it.
- Before release I check the dispatch log:
  - The apology sentence is used only if the log confirms no update after 07:00 on 18 November.
  - If the log does not show the public data updates of 16 and 17 November as issued, the customer information paragraph is used in its Chief Executive-approved form from those cards; otherwise it refers to them.

Wording, common text
"Lan Tidal Bank: service status update. Issued [08:30] HKT, 19 November 2026. This replaces our earlier service updates.
[Our last update was at 07:00 on 18 November. We should have updated you sooner, and we are sorry.]
[Position paragraph: Version 1, 2 or 3.]
Queued payments: [number] queued instructions have been sent and [number] are still waiting. Please do not re-submit.
Customer information: we have confirmed that information about 320 customers was copied and made public, and we are contacting those customers directly. For a wider group of customers we have not confirmed whether information was copied.
Help and costs: you will not bear bank fees or charges caused by this disruption. To register a loss, or to report a suspected scam, use our call-back service, your relationship manager or any branch.
Staying safe: the bank has no 'verification' page. We will never ask you to verify your account through a link, or to give a password, PIN or one-time passcode.
Next update: 18:00 HKT today, then 08:00 and 18:00 each day until the service is restored, and at once if the position changes."

Position paragraphs
- Version 1, hold (recorded position): "The payment service has not been restarted. A second round of testing, carried out away from our live systems, matched every test payment in the sample. This is a test result. It is not yet a decision to restart, and we will tell you as soon as that decision is made."
- Version 2, staged or limited restart authorised and live: "We have started to bring the payment service back in stages. The first stage is [scope as authorised]. Everything else remains unavailable for now. We check each stage and will pause if a check does not pass."
- Version 3, full service live and verified: "The payment service is working again from [time]. We are monitoring it closely and are sending the remaining queued instructions first." This is a restoration notice, not a closing update.

Things the update does not say
- That all affected customers have been notified; delivery is not evidenced.
- That the incident is over or the systems are secure.
- Anything about the vendor credential or attribution.

Status of facts
- Confirmed: second offline test reconciled all 240 sampled instructions in a rebuilt access environment; no new alarms in the offline environment for six hours; live position is hold.
- Not known to me: SEC's decision on restrictions; current queue figures.

Accountable owner and executing parties
- Owner: COM.
- Approver: Chief Executive, including for any later closing update.
- Fact check: SEC and Operations. Clearance and HKMA copy: LC.
- Executing: digital channels team, contact-centre head, branch network head.

HKT deadlines, 19 November
- 08:10: dispatch-log check and requests to SEC, Operations and LC.
- 08:30: target release.
- 08:45: latest release.
- 18:00: next update.
- From 20 November: 08:00 and 18:00 daily until restoration, and at once on any change.

Recipients and channels
- Website status notice.
- App and internet banking notice.
- Recorded hotline message.
- Verified social media accounts.
- Press release to newsdesks.
- Branch notices.
- HKMA copy via LC.

Basis, direct rules (external)
- R09, SPM TM-E-1 (statutory guideline under Banking Ordinance §7(3)), section 8.2.3, PDF p.33: a press release or similarly effective notice is expected "if the AI does not have reasonable confidence that the service can be resumed in the near future." The service is still down at H+72 with no restart decision, so the expectation continues.
- R09 section 8.2.2, PDF p.33: AIs should "inform them of the key facts relating to the incident and the steps that customers may take".
- R05, HKMA circular (22 June 2010), PDF p.3: "consistent and up-to-date messages are conveyed to all relevant parties on a timely basis. The HKMA should be kept informed during the process and copies of public communication materials should be submitted to the HKMA for reference."
- R05, PDF p.2: notices should include "the steps that affected customers need to take in the circumstances in order to gain or regain access to the relevant banking services or to protect their interests."

General principles
- R06, SPM OR-2 (non-statutory), section 8.3, PDF p.13: "Communication, where appropriate, should take place during the incident (e.g. to provide performance metrics), and after, including to convey analysis of lessons learned." This supports continuing now and a later closing communication.
- R07, SPM TM-G-2 (non-statutory), section 1.3.3, PDF p.5: the HKMA "should also receive periodic progress reports upon being notified until the final resolution of the crisis." It applies if the BCP was activated, which is not recorded for me; the same logic supports updating until final resolution.

No direct rule located in assigned sources
- No source says when public incident updates may stop, how often they must be issued, or what a closing statement must contain.
- Searches recorded: the regex "post-incident|lessons learn|closure|close the incident|handover|hand over|hand-over". Its results were dominated by "disclosure" matches; the relevant hits were R01 p.93, R02 pp.32 to 33 and R06 p.13. Also "resumption time" and "press release".

Professional judgment
- Calling this "closing" while customers still cannot make payments would be wrong and would have to be reversed.
- Twice-daily updates are predictable without being noise.
- The closure criteria tie the last bulletin to things customers can see: service back, payments settled, people told, cases owned.

Internal bank procedure: N/A (PH01 absent).

---

UNIT Q24b: Handing off unresolved customer cases and follow-up messaging

Decision and action
- Hand each stream to a named standing owner today, with a written pack and a signed acceptance.
- Nothing transfers as "done" without evidence.
- Customer-facing references and contact routes do not change.
- Corporate Communications keeps ownership of all customer and public wording after handover.

Who receives what

| Stream | Standing owner after handover |
|---|---|
| Scam and fraud cases | Head of fraud |
| Disruption claims and payroll losses | Claims desk lead, with head of SME banking for payroll customers |
| Privacy matters and oversight of the breach notification process | Data protection officer in LC, under the senior officer or committee designated for privacy incidents |
| Notification register and all notice wording | Corporate Communications, named deputy |
| Hotline, call-back service and branch priority desks | Contact-centre head and branch network head |
| Counterparty updates on unsettled instructions | Head of payment operations |
| Public status updates and scam alerts | Corporate Communications |

Handover pack
1. State of the record: a first page listing what is not evidenced. From the handoff this is: outcomes of first contacts; number of open cases; content of the Chief Executive's remediation decision; completion figures for the rebuilt register; whether anything was misdelivered; whether the 16:00 consolidated notices went out; delivery for every batch.
2. Case register: each open case with owner, status, last contact, next promised contact and anything promised.
3. Notification register: the 320 and the wider group, with delivery evidence, the gap list and the 12 corrected records.
4. Commitments register: every promise made publicly or individually, each with an owner and due date. It includes: the costs line; "we will contact you directly"; "we will tell you the outcome"; call-back times; the SME letter if approved; update times.
5. Approved wording: public statements, notices, Frontline Instructions and the promise list, showing what the Chief Executive approved and what is conditional.
6. Open decisions: the remediation decision; the outcome for the wider group once SEC concludes on scope.
7. Dispatch log and call records, kept under LC's preservation decision (Q23b). Nothing is deleted until LC releases it.

Conditions for handover
- Each receiving owner signs acceptance of a specific list.
- No case transfers without a named handler and a next-contact date.
- A notification batch transfers as "open, delivery not evidenced" unless the register proves otherwise.
- The remediation decision is obtained in writing and recorded before the promise list is handed on. If it is not available, the "cannot promise" wording stays in force.

Follow-up messaging after handover
- Customers with open cases are told at their next scheduled contact: "Your case reference is unchanged. [Team] is handling it, and will contact you by [date]." There is no separate mass message.
- Planned messages, each sent once and only on its trigger:
  - a restoration notice;
  - an outcome letter for each case;
  - a final notice to the 320 when the investigation concludes;
  - an outcome notice to the wider group when SEC concludes on scope;
  - scam alerts when new variants appear;
  - the closing update, on the criteria in Q24a.
- I supply LC with the dates and facts of customer and media communication for the written incident report, which asks about them.

Status of facts
- Confirmed (card): unresolved vendor credential questions, customer cases and regulatory follow-ups remain, and the exercise window is closing.
- Not recorded: the items listed in pack section 1.

Accountable owner and executing parties
- Owner: COM for the pack, the wording and the registers until accepted.
- Receiving owners as in the table.
- Approver of the handover: crisis management team chair. The Chief Executive is informed.
- LC receives the commitments register for its own register of deadlines (Q23a).

HKT deadlines
- 09:00, 19 November: open items checked with each executing owner.
- 10:00: handover meeting.
- 12:00: pack issued.
- 17:00: acceptances signed; any item not accepted stays with COM and is escalated to the chair.
- 17:00, 20 November: first open-case and notification summary from the standing owners to the Chief Executive and LC. Daily at first, then weekly.
- 24 November: my communication facts to LC for the written incident report. This date is my estimate; the report deadline itself is LC's.

Recipients and channels
- Standing owners: handover meeting and the written pack on the internal secure share.
- Customers: through their existing case handler and existing channels.
- LC: registers and figures.

Basis, direct rules (external)
- R16b, HKMA circular "Customer Data Protection" (14 October 2014), PDF p.2: "each AI should designate an officer of sufficiently senior ranking or a designated management committee, which is chaired by senior management, for overseeing the process of handling and reporting privacy incidents." This fixes where oversight of the breach stream sits after the incident team stands down.
- R16b, PDF p.2: "taking prompt remedial actions to protect affected customers' interests and prevent similar incidents from happening again."
- R11, PCPD guidance (June 2023, not statute), PDF p.6, Step 5: "A comprehensive record of the incident is therefore required, which should include all facts relating to the breach, ranging from details of the breach and its effects to the containment and remedial actions taken by the data user." This is the basis for the registers and the "state of the record" page.
- R11, PDF p.3: "the customer service department for addressing the issues of affected individuals and for providing updates to customers".
- R02, Code of Practice (Generic), section 7.2.3(a)(v)(4), PDF p.32: "Recording the incident response process, including details of the incident, actions taken and decisions made". The Code is practical guidance (section 1.1.4).
- R02 section 7.3.7(a), PDF p.37: the written report is due "within 14 days after becoming aware of the computer-system security incident". Annex F section E (PDF p.46) asks about stakeholder and media communication. This is why LC needs my facts.
- R05, PDF p.3: "consistent and up-to-date messages". One owner for wording after handover keeps this true.

General principles
- R02 section 7.2.3(i)(iii), PDF p.33: the post-incident review covers "Effectiveness and efficiency in executing the emergency response plan". The gaps in delivery evidence and the missed update are inputs I will give that review.
- R08, SPM TM-G-1, section 5.1.3, PDF p.20: incidents should be recorded and tracked "until rectification of the incidents". That passage concerns IT incidents; I apply the same discipline to customer cases by analogy.
- R07 section 4.7.2, PDF p.14: "Important conversations with external parties should be properly logged for future reference."

No direct rule located in assigned sources
- No source prescribes how to hand customer cases from an incident team to standing teams, the contents of a handover pack, or acceptance conditions.
- Searches recorded: the same regex as in Q24a, with the same limitation; "complaint"; "customer service"; "stakeholder".

Professional judgment
- A signed acceptance against a list stops cases falling between teams.
- Keeping references and channels unchanged avoids confusing customers at a time when scammers are imitating the bank.
- Listing unevidenced items first is the honest way to hand over an incomplete record.

Internal bank procedure: N/A (PH01 absent).

---

Simulated actions for the facilitator's log (all HKT, 19 November 2026 unless stated)
- 08:10: COM checks the dispatch log for updates after 07:00 on 18 November and for the public data updates.
- 08:10: COM asks SEC for the recorded production decision, Operations for queue figures and LC for clearance.
- 08:30, latest 08:45: status update released on Chief Executive approval (Version 1 unless the decision changes); copy to HKMA via LC.
- 09:00: open items checked with executing owners.
- 10:00: handover meeting.
- 12:00: handover pack issued.
- 17:00: acceptances signed; exceptions escalated to the chair.
- 18:00: next public update.
- 17:00 on 20 November: first standing summary to the Chief Executive and LC.
- 24 November: communication facts to LC for the written incident report.