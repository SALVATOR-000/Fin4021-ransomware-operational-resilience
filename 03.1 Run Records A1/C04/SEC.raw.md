SEC RESPONSE - C04 (Mon 16 Nov 2026, 18:00 HKT, H+10) - Unit Q10 a and b. Locked before colleagues' answers.

Internal bank procedure (PH01): N/A for both units. PH01 is not in my allowed manifest, so no internal basis and no conflict check is possible.

Fact status I am working from
- Released by the card: the original gateway is still impaired; about 4,200 payment instructions are queued, including time-sensitive SME payroll; a secondary process can handle up to 400 verified instructions an hour if approved; some customers retried transfers after a timeout.
- Unverified or unknown: how many of the 4,200 are payroll; how many are retries; whether any instruction was already sent before the gateway failed; whether the attacker altered or added queued instructions; whether the secondary process shares hosts, credentials or keys with the gateway; whether it has been tested; clearing cut-off times; the bank's own tolerance for disruption and continuity plan terms.
- Arithmetic: 4,200 at 400 an hour is at least 10.5 hours of continuous processing with no holds.

---

Q10a - Use of the secondary process and prioritisation

Decision. Yes, use the secondary process, on security conditions, starting with a pilot. SEC gives the security clearance; the crisis management team (CMT) gives the activation approval. The 400-an-hour ceiling is not raised by weakening verification. The evidence hold on the original gateway from C01 stays in force.

Security conditions before the first release (SEC gates)

| Gate | Condition | Evidence SEC needs |
|---|---|---|
| 1. Independence | The secondary process does not run on, route through or share accounts, keys or secrets with the isolated gateway. No vendor account is used. It uses only secrets rotated under C03 | Network path and account review; rotation record |
| 2. Clean source | Instructions are taken from the original channel records carrying the customer's authentication, not from files on the impaired gateway | Source confirmed by the payments information owner |
| 3. Verification | Each instruction is checked field by field against the customer's original: payer, payee, amount, value date, reference. Payroll batches have their record count and total confirmed with the SME's authorised contact by call-back to a number on file | Verification record per item or batch |
| 4. Authorisation | Maker and checker for every release, plus one added approval layer for the bypass. Normal fraud and sanctions screening stays in the path | Approval matrix signed by the information owner |
| 5. Duplicate gate | The Q10b control is in force | See Q10b |
| 6. Logging | Every release is logged with operator, approver and time, to a store outside the compromised environment | Log sample |
| 7. Change control | Emergency change record opened and approved | Change record |

Simulated actions for the log
1. 18:00-18:30 - SEC and payments operations check gates 1 to 7.
2. 18:30 - SEC clearance and payments operations' recommendation go to CMT for the activation decision.
3. 18:45 - Pilot of 20 verified payroll instructions. Reconcile end to end: released count and value equal ledger debits and equal receiving-side acknowledgements.
4. 19:15 - Full rate if the pilot reconciles. Reconciliation checkpoint every hour.
5. 01:00-03:00 on 17 Nov - heightened monitoring around the attacker's 02:00 deadline.

Prioritisation of eligible instructions (professional judgment). An instruction is eligible only if it is verified, has passed the duplicate gate, has passed screening and has not been cancelled by the customer.
- Priority 1: SEC-cleared SME payroll, earliest value date first, then time of original submission.
- Priority 2: other instructions with a value date of today or tomorrow, and verified urgent cases referred by branches or the contact centre. Up to 40 an hour are reserved for these referrals.
- Priority 3: all remaining eligible instructions in order of original submission.
- Held: items that fail verification, suspected duplicates, items with no authenticated customer origin, screening alerts, and later-dated items that can wait for the gateway.
Order is not set by customer size or relationship. High-value items get an extra call-back, not a higher place.

Stop triggers (any one pauses releases; SEC or the payments operations lead may pause without prior approval and then informs CMT)
- A reconciliation break at any checkpoint.
- A released item later found to be a duplicate or of unverified origin.
- Any indicator of compromise on the secondary process or its accounts.
- Evidence that queued instructions were altered.

Accountable owner: SEC for the security clearance and stop authority. Executing parties: payments operations (verification, release, reconciliation), the payments information owner (approvals), IT Operations (running the process), CMT (activation).

Time (judgment targets): as in the actions above. Best case for clearing all 4,200 is about 05:45 HKT on Tue 17 Nov (10.5 hours from 19:15), assuming no holds and continuous staffing. This is a projection, not a commitment.

Destination and channel: the secondary process, under an emergency change record; clearance and status to CMT, LC, COM and IT Operations over the out-of-band bridge; every decision entered in the incident log.

Basis
- R07, SPM TM-G-2 Business Continuity Planning, s.4.3.2, PDF p.11: the alternate processing phase "may entail record reconstruction and verification, establishment of new controls, alternate manual processes, and different ways of dealing with customers and counterparties". s.4.2.2, PDF p.10: the crisis process includes a "clear internal decision-making process and criteria for activation of the BCP and/or alternate sites". HKMA supervisory guidance for all authorized institutions; it applies because a critical service is being resumed by an alternate method. It supports CMT approval and the verification gates.
- R07 s.3.2.2, PDF p.8: "The result of the time-frame assessment in the business impact analysis is the key determination factor for the recovery priority of individual services." R06, SPM OR-2, s.3.4, PDF p.6: "an AI should prioritise a critical operation that would more sooner breach its tolerance for disruption over one that is less time sensitive". Both are written for planning and board oversight; I apply them as the principle behind time-sensitive payroll first. Missing fact: the bank's own impact analysis and tolerance figures. If they set a different order, that order governs.
- R14b, Annex to HKMA circular "Good practices for operational resilience", PDF pp.1-2, item 1 "Built-in bypass options": bypass enabling "the download of the latest payment transactions for manual approval and processing to support payment operations", with "a predefined additional layer of approval matrix to ensure proper authorisation, and reconciliation procedures to maintain accuracy following a bypass". Authority: observed good practice; R14a, PDF p.2, says institutions "are encouraged to review the good practices in detail, consider their applicability". Not a requirement, but directly on point for gates 4 and the hourly reconciliation.
- R09, SPM TM-E-1, s.9.5.4, PDF p.37: when Internet banking is not accessible, "AIs should ensure that their other service channels will have the capacity and related operational procedures to provide an acceptable level of service to their customers", naming funds transfers as a critical function.
- R08, SPM TM-G-1, s.4.2.4, PDF p.18: "only properly tested and approved systems are promoted to the production environment". s.4.3.1, PDF p.19: "no single person can effect changes to the production environment without the review and approval of other authorized personnel". s.4.3.2-4.3.3, PDF pp.19-20, on emergency changes (quoted in C01). Missing fact: whether the secondary process was tested. If it was not, the pilot is extended and full rate waits for two clean checkpoints.
- R02, OCCICS Code of Practice (Generic), s.7.2.4(a), PDF p.34: "Business continuity management focuses on sustaining the CI operator's ability to continue essential operation during disruptions arising from computer-security incidents." R01, Cap. 653, s.27(5), PDF p.43: "A CI operator must implement an emergency response plan." with Schedule 3 Part 2 item 5, PDF p.93: "A recovery plan for resuming the provision of essential services". Missing fact: the bank's plan; where it prescribes the secondary process, the plan is followed.

No direct rule located in assigned sources for the security gates, the pilot size, the priority classes, the reserved capacity or the stop triggers. Files: all. Terms: regex "manual process|manual intervention|bypass|break-the-glass|workaround|alternate process|alternative process"; regex "tolerance for disruption|prioriti|recovery priority|time-critical|time-sensitive|payroll|salary" (no hit for payroll or salary); regex "failover|fail-over|fallback|alternate site". These are professional judgment: the attacker had command access, so the queue cannot be trusted until checked against the customer's original.

---

Q10b - Control for retried payments and possible duplicates before processing

Decision. A mandatory duplicate gate sits in front of the secondary process. No instruction is released without passing it, and no exact duplicate is released automatically.

The control
1. One register. Payments operations builds a single instruction register from every source: the 4,200 queued items, retries after the timeout, transfers re-entered at branches or by the contact centre today, items in flight when the gateway failed, and everything the secondary process itself releases.
2. Matching key. Payer account, payee account or identifier, amount, currency, value date and customer reference. For payroll, also employer, pay period, record count and batch total.
   - Same key twice in the incident window: suspected duplicate.
   - Same payer, payee and amount with a different reference or time: possible duplicate.
3. Already-paid check. Each item is checked against the ledger and independent outbound records for a debit or a message already sent. Items in flight at the failure are held as "status unknown" until an independent record shows they did not settle. They are not resent on assumption.
4. One release only. Each verified instruction gets a unique processing identifier. The secondary process rejects any identifier already marked released, and the register is updated before the next batch, so a re-run cannot pay twice.
5. Disposition. Suspected and possible duplicates are held. The earliest authenticated original is released only after the customer, or the SME's authorised contact, confirms by call-back to a number on file. Other copies are cancelled with a record. Call-backs are worked in the Q10a priority order.
6. Unverified origin. A queued item with no matching authenticated customer record is not treated as a duplicate. It is held and passed to the forensic team as possible tampering.
7. Dual control. A maker runs the matching; a checker reviews the exception list independently; SEC attests to the matching logic and the integrity of the register.
8. After each hourly batch. Released count and value must equal ledger debits and receiving-side acknowledgements. A break is a stop trigger under Q10a.
9. At source. Mobile transfer submission stays closed, and IT Operations confirms the timeout path is not accepting further entries. Branches and the contact centre check the register before keying any transfer for a customer who says an earlier attempt failed.

Accountable owner: SEC for the control design and its attestation. Executing parties: payments operations (register, matching, call-backs), the payments information owner (dispositions), IT Operations (processing identifier and source closure), branches and contact centre (register check).

Time and triggers (judgment targets): gate built and proven on the pilot by 18:45 HKT; in force before the first full-rate release at 19:15; exception list reviewed hourly. Observable trigger: zero releases without a "passed" entry in the register.

Destination and channel: the instruction register in the restricted incident workspace; exception list to the payments information owner; summary counts to CMT, LC and COM.

Basis
- R14b, PDF p.1, item 1 "Auto-switching capabilities": controls include "controlled auto-retry logic (e.g. duplication checks when re-attempting transactions)"; PDF p.2: "reconciliation procedures to maintain accuracy following a bypass". Encouraged good practice (R14a, PDF p.2), directly on duplicate checks for retried transactions. It gives no method.
- R09 s.5.1.2, PDF p.19: "AIs should also implement sufficient controls to maintain and verify the integrity of the information processed by their Internet banking systems.", for example to "reconcile data file balances after transaction updates and to check the integrity of data transmitted between different systems". HKMA supervisory guidance; it applies to instructions submitted through mobile and Internet banking, and I use it as principle for other channels.
- R07 s.4.3.2, PDF p.11 (quoted above): "record reconstruction and verification, establishment of new controls".
- R08 s.4.3.1, PDF p.19 (quoted above): supports maker and checker.
- R05, HKMA circular, PDF p.1, "Immediate incident response" (checked against the scan in C01): "The top priority should be to safeguard the interests of customers who have been or may be affected by the incident." A double debit is direct customer harm.

No direct rule located in assigned sources for the matching key, the unique processing identifier, call-back confirmation, treatment of in-flight items or the register. Files: all. Terms: regex "duplicat|reconcil|retry|re-attempt|idempot" (relevant hits R14b pp.1-2 and R09 p.19 only); regex "integrity of (transactions|data|information|records)|transaction integrity|data integrity|accuracy, completeness|non-repudiation|authoris(ation|ed) of transactions"; regex "fund transfer|funds transfer|transaction limit|notif(y|ication) (to )?customers? (promptly|immediately)|unauthori[sz]ed transaction" in R09. These are professional judgment.

---

Facts SEC passes to the incident team (18:30 clearance, then hourly)

| Fact | Status at 18:00 | Used by |
|---|---|---|
| Secondary process cleared on security grounds | Pending gates; result 18:30 | CMT |
| Processing capacity | Up to 400 verified instructions an hour; not to be exceeded by cutting checks | CMT, COM |
| Earliest clearance of the queue | About 05:45 on 17 Nov at best; projection only | COM (no promise to customers), CMT |
| Retries | Some customers retried; count unknown until the register is built | COM, CMT |
| Advice that reduces duplicates | Customers should not resubmit; branches check the register before re-keying | COM (Q12) |
| Queued instructions altered by the attacker | Unknown; each item is verified against the customer's original | LC, CMT |
| Continuity procedures activated | Will be true on CMT approval | LC: R02 s.7.3.4(c), PDF p.36, "has triggered or is likely to trigger the activation of business continuity or disaster recovery procedures"; R02 Annex F item D(2), PDF p.45 |
| Possible material change notification | For LC to assess: R01 s.22(2)(a), PDF p.33, "a material change occurs to the design, configuration, security or operation of a critical computer system", notifiable "within 1 month after the date on which the event occurs". SEC will supply the technical description | LC |
| Dispatch records from the first card | SEC holds none and cannot attest to what was sent or when | LC (Q11) |

Limitations: text search and page reads only. Not available to me: the bank's business continuity plan, impact analysis and tolerance figures, and the secondary process's test records.