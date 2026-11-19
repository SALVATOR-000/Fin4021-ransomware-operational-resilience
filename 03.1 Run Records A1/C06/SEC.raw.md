SEC RESPONSE - C06 (Tue 17 Nov 2026, 20:00 HKT, H+36) - Unit Q16 a and b. Locked before colleagues' answers.

Internal bank procedure (PH01): N/A for both units. PH01 is not in my allowed manifest, so no internal basis and no conflict check is possible.

Fact status I am working from
- Released by the card: an offline laboratory test on a recovery image reconciled 118 of 120 payment instructions; the two mismatches are unexplained; the laboratory saw no recurring encryption during its test window; some SMEs report missed payroll cut-offs.
- From the facilitator's handoff: my Q13a candidate was approved for testing only, and production use is on hold. No card records the result of integrity checks 1-8, the separation checks, the 17:00 test report or any of the ten reconciliation checks. The production decision sits with the Chief Executive as crisis management team chair, after both SEC reports.
- Unverified or unknown: what kind of mismatch the two are (amount, payee, status, duplicate); whether they come from the test set-up, the period after the backup, the rebuilt software, or altered data; the length of the laboratory's test window; whether rollback has been tested; the current state of the secondary-process queue.

---

Q16a - Start staged recovery, hold, or permit a narrower mode; the authorisation gate

Decision. Hold. No staged production recovery starts tonight, and the recovery image is not used in production in any mode. The only service mode permitted is the one already running: the secondary process, with the same verification and duplicate controls as in C04. SMEs reporting missed payroll cut-offs go to the front of that queue once their instructions are verified.

Reasons (professional judgment)
- My own Q13b pass condition is no unexplained difference. Two unexplained mismatches in 120 fail it. At that rate a queue of thousands would produce dozens of wrong or doubtful payments.
- The checks that would show the image is clean and separate are not recorded as passed, so I treat them as not passed.
- "No recurring encryption during the test window" is a limited finding. It covers one offline image for one window. It does not rule out dormant or timed code, or other attacker footholds.
- An offline result describes the copy tested. It does not validate production connections.
- A wrong or repeated payment harms customers more lastingly than further delay that the interim process can partly relieve.

Simulated actions for the log
1. 20:00 - Hold recorded. SEC recommendation to the Chief Executive by 20:15.
2. 20:15 - Mismatch investigation opens. For each of the two items, compare the customer's original instruction, the ledger posting, the external confirmation and the image's own logs. Classify the cause as one of: test set-up error; an item from the period after the backup; a defect in the rebuilt software or configuration; altered or corrupt restored data; attacker tampering.
3. 21:00 - Both SEC reports (Q13a test report and Q13b reconciliation report) are issued on time with the true status of every check, including "not recorded" where that is the case, and an overall result of "not passed".
4. By 23:00 - Preliminary classification of the two mismatches to the Chief Executive, the information owner and LC.
5. After a fix - Full re-run of the 120 instructions and all ten reconciliation checks.

What each classification leads to
- Test set-up error or post-backup item: correct it and re-run in full.
- Software or configuration defect: fix under change control, then repeat the functional test and the reconciliation.
- Altered data or tampering: this candidate fails. Move to an earlier backup copy or a data-only restore, and widen the forensic review.

Authorisation gate (all conditions recorded in the incident log before any production activity)

| Condition | Evidence | Signed by |
|---|---|---|
| 1. Both mismatches explained and resolved | Investigation note | SEC and payments operations |
| 2. Re-run reconciles 120 of 120 and all ten checks pass | Reconciliation report | Maker, checker, independent reviewer |
| 3. Integrity checks 1-8 and separation checks recorded as passed | Test report | SEC |
| 4. Rollback to the secondary process rehearsed | Rehearsal record | IT Operations |
| 5. Final delta reconciliation plan and live test plan ready | Plans | Payments operations |
| 6. Business acceptance | Sign-off | Payments information owner |
| 7. Regulatory steps confirmed | Note | LC |
| 8. Authorisation | Recorded decision with time | Chief Executive as crisis management team chair |

SEC cannot authorise alone, and neither can the information owner. If any condition is missing, the hold stands.

Stages if the gate is passed (judgment): Stage 1, a pilot of 20 verified payroll instructions with every item matched three ways. Stage 2, verified payroll and time-critical items at a capped rate with hourly reconciliation. Stage 3, mobile transfer submission reopened with limits. Stage 4, full service. The secondary process stays ready as fall-back throughout. Each stage needs the criteria in Q16b before the next.

Accountable owner: SEC for the hold recommendation, the security conditions and the gate design. Executing parties: forensic staff and payments operations (mismatch investigation), IT Operations (re-run, rollback rehearsal). Decision: Chief Executive.

Time (judgment targets): as in the actions. Earliest gate review 08:00 HKT on Wed 18 Nov, and only if conditions 1-7 are recorded by then.

Destination and channel: recommendation and reports to the Chief Executive, the payments information owner, LC and IT Operations through the restricted incident workspace and the out-of-band bridge; hold entered in the incident log and on the emergency change record.

Basis
- R03, HKMA Sectoral Code, s.6.2.16(a), PDF p.15: change controls adhere to "relevant requirements outlined in SPM TM-G-1 sections 4.2.4 and 4.3". R08, SPM TM-G-1, s.4.2.4, PDF p.18: "only properly tested and approved systems are promoted to the production environment". Authority: sectoral code under Cap. 653 s.8, pointing to HKMA supervisory guidance. It applies because the recovery image would replace the designated gateway. A test with unexplained mismatches is not "properly tested", so the rule supports the hold. It does not define a pass mark; zero unexplained difference is my criterion.
- R08 s.4.3.1, PDF p.19: "no single person can effect changes to the production environment without the review and approval of other authorized personnel". s.4.3.2, PDF p.19: "Emergency changes should be approved by the information owner (for application system or production data related changes) and other relevant parties at the time of change." Supports the multi-signature gate.
- R07, SPM TM-G-2, s.4.2.2, PDF p.10: the crisis process includes "the process for overseeing the recovery and restoration efforts of the affected facilities and the business services". s.4.3.2, PDF p.11, on full recovery: "It is as difficult and critical to the business as the process to activate the BCP." Supports the decision resting with the crisis management team chair.
- R09, SPM TM-E-1, s.5.1.2, PDF p.19: "AIs should also implement sufficient controls to maintain and verify the integrity of the information processed by their Internet banking systems." s.9.4.1, PDF p.35: "It is important that the actual effectiveness of the resilience of the system should be properly verified and tested." Annex B item B.2, PDF p.40: "testing of the changes with satisfactory results" (written for scheduled maintenance; used as principle).
- For the narrower mode: R09 s.9.5.4, PDF p.37: "AIs should ensure that their other service channels will have the capacity and related operational procedures to provide an acceptable level of service to their customers". R14b, good-practice annex, PDF p.2: bypass options with "appropriate risk mitigating measures to ensure critical operations can continue during prolonged system disruptions" (encouraged practice, not a requirement).
- Weighed against the hold: R06, SPM OR-2, PDF p.3, bullet list before s.2: "Resume normal operations in a timely manner after disruptions occur". R05, HKMA circular, PDF p.1, "Immediate incident response" (checked against the scan in C01): "The top priority should be to safeguard the interests of customers who have been or may be affected by the incident." Missing fact: the bank's tolerance for disruption and recovery time figures. If the Chief Executive judges that a tolerance is about to be breached, the gate conditions still apply; what changes is the resourcing of the interim process.
- R01, Cap. 653, s.27(5), PDF p.43: "A CI operator must implement an emergency response plan." Missing fact: the plan's recovery section; if it sets stricter entry conditions, those govern.

No direct rule located in assigned sources for a pass mark on reconciliation, the staged sequence, the mismatch classification or the gate composition. Files: all. Terms: regex "staged|phased|in phases|pilot|go/no-go|resumption criteria|resume normal"; regex "parallel run|dry run|cut-?over|go-live|live test|acceptance test|fall-?back procedure|roll(ing)?-?back"; regex "senior management|Chief Executive" in R07. These are professional judgment.

---

Q16b - Stop and rollback criteria if any production activity is authorised

Decision. No production activity is authorised by this unit tonight. If the Chief Executive authorises a stage, the following apply from its first transaction. "Stop" pauses all releases from the recovered gateway. "Rollback" disconnects it and returns service to the secondary process.

Stop criteria (any one; SEC, the payments operations lead or the IT Operations duty manager may stop without prior approval)

| Area | Criterion |
|---|---|
| Security | Any indicator from this incident on the recovered gateway or its accounts: encryption activity, attacker tools, unauthorised commands, new accounts or keys, use of the revoked vendor credential or its tokens, connections to attacker addresses |
| Security | Any traffic between the recovered environment and the isolated compromised segment |
| Security | Logging or monitoring on the recovered gateway unavailable for more than 5 minutes |
| Security | Any change to configuration or static data not matched to an approved change record |
| Integrity | One unexplained mismatch between customer instruction, ledger posting and external confirmation |
| Integrity | Any duplicate or replayed payment, or any payment whose payee or amount differs from the customer's original |
| Integrity | An hourly reconciliation not completed on time or not tying to zero; any settlement position difference; any reference number collision |
| Operations | Rejects or errors above 1% of instructions in a checkpoint interval, or timeouts that could cause customers to resubmit |
| Operations | A counterparty reports unexpected or repeated messages |
| External | A written requirement or direction from an authority relayed by LC |

Rollback criteria
- Any security stop criterion confirmed as genuine: immediate rollback, and the recovered gateway is isolated and preserved as evidence.
- An integrity stop not explained within 30 minutes, or a second integrity stop in the same stage.
- Any customer financial effect: wrong payee, wrong amount or double debit.
- Two consecutive reconciliation checkpoints that do not tie.

Rollback method and preconditions
- Before each stage: rollback rehearsed; the secondary process staffed and its register in step; a record of queue and register state at stage start.
- On rollback: the recovered gateway is disconnected from payment interfaces and its keys are revoked. Instructions in flight are classified as settled, not settled or unknown from independent confirmations; unknown items are held and not resent. A delta reconciliation covers everything the gateway processed in the stage. COM and LC are told at once.
- No second attempt without a new pass through the Q16a gate.

Decision rights: stop, by any of the three duty holders. Rollback, by SEC or the payments information owner, reported to the Chief Executive immediately. Resumption after a stop, and every stage advance, by the Chief Executive on the joint recommendation of SEC and the information owner.

Stage advance criteria (judgment): Stage 1 to 2, all pilot items matched three ways with no stop. Stage 2 to 3, four consecutive clean hourly checkpoints. Stage 3 to 4, 24 hours with no stop. Enhanced monitoring continues for 30 days.

Accountable owner: SEC for the criteria and for security stops. Executing parties: payments operations (reconciliation checkpoints), IT Operations (rollback), Security Operations Centre (monitoring).

Time and triggers: criteria take effect at the first production transaction of any authorised stage; checkpoints hourly; the 5-minute and 30-minute limits above are the observable triggers.

Destination and channel: criteria attached to the emergency change record and briefed to the three duty holders; stops and rollbacks announced on the out-of-band bridge and entered in the incident log.

Basis
- R08 s.4.3.1, PDF p.19 (reached through R03 s.6.2.16(a)): the change process includes "a process for rolling-back changes to re-instate the original programs, system configuration or data in the event of production release problems" and "a post implementation verification of the changes made". Direct support for having rollback and post-change checks; it sets no thresholds.
- R09 Annex B, PDF p.40, items B.2 and B.3: "well-tested fall-back procedures to cater for any exceptional and unexpected situations" and "Live test after the scheduled system maintenance/drills to ensure the effective operation of the relevant services". Principle.
- R14b, PDF p.2: "reconciliation procedures to maintain accuracy following a bypass"; PDF p.1: "duplication checks when re-attempting transactions". Encouraged practice supporting the integrity criteria.
- R09 s.5.1.2, PDF p.19 (quoted above): integrity controls and reconciliation.
- Context for the external criterion, not a current duty: R01 s.36(2)(a), PDF p.52, allows a written notice requiring the operator "not to use the investigated system". No notice has been received.

No direct rule located in assigned sources for the specific stop thresholds, the 5-minute, 30-minute and 1% limits, in-flight handling or stage advance criteria. Files and terms as listed under Q16a. These are professional judgment: limits are set tight for early stages because the candidate has not yet shown a clean result.

---

Facts SEC passes to the incident team (20:15, 21:00, 23:00, then at gate review)

| Fact | Status at 20:00 | Used by |
|---|---|---|
| Recovery position from this unit | Hold; no production use of the recovery image; interim secondary process continues | COM (Q18a), Chief Executive |
| Laboratory result | 118 of 120 reconciled; two unexplained. These are test results on an offline image, not errors in customers' payments | COM, LC |
| "No recurring encryption" | True for the laboratory's window only; not proof the image is clean | Chief Executive, LC |
| My Q13 checks | Results not recorded; treated as not passed until recorded | Chief Executive, LC (Q17b board escalation) |
| Restoration time | None can be given; earliest gate review 08:00 on 18 Nov, conditional | COM |
| Unsettled instructions for the two counterparties | Status per item (settled, not settled, unknown) comes from the instruction register; SEC attests only to what the register records, and holds no figures on this card | COM (Q18b) |
| Missed payroll cut-offs | Reported by some SMEs; those verified are moved to the front of the interim queue | COM, LC |
| Report status field | R02 Annex F item D(2), PDF p.45: the original gateway is still impaired, so "Operation in primary site has resumed normal" does not apply; which of the other boxes fits the interim process is for LC | LC |
| Staged recovery and change notification | If recovery is later staged, R03 s.6.1.1, PDF p.11, says "the date on which the event occurs should be applicable to each individual phase of the change deployment"; for LC to assess under R01 s.22 | LC |
| Forensic firm's request for the diagnostic image (LC's decision) | SEC technical input: the firm may be able to work from system artefacts, logs and file metadata with customer fields excluded, or examine the image inside a bank-controlled environment without taking a copy. Any transfer should be encrypted, hashed and entered in the custody record with a named access list and a return or destruction date | LC (Q17a) |

Limitations: text search and page reads only. Not available to me: the laboratory's test report, the bank's recovery plan and tolerance figures, and the records of my Q13 checks.