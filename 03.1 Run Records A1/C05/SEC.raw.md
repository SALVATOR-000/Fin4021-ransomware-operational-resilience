SEC RESPONSE - C05 (Tue 17 Nov 2026, 08:00 HKT, H+24) - Unit Q13 a and b. Locked before colleagues' answers.

Internal bank procedure (PH01): N/A for both units. PH01 is not in my allowed manifest, so no internal basis and no conflict check is possible.

Fact status I am working from
- Released by the card: the attacker's deadline has passed; a public mirror holds a file matching 320 customers' records, including the original 80; the 18,000-record claim is unverified; a social-media account is luring customers to a fake verification page; a pre-incident immutable backup exists.
- Unverified or unknown: whether the backup can restore payment processing; the backup's date against the attacker's first access (still unknown since C01); whether the backup system was touched by compromised accounts; whether the standby gateway is clean; how long a restore takes; what was processed between the backup time and the failure.
- Carried forward: the original gateway is under evidence hold (C01); vendor access is suspended (C03); the secondary process and its instruction register are running (C04).

---

Q13a - Which recovery candidate to test, and how to verify integrity and separation

Decision. Test one candidate first: a newly built gateway in an isolated recovery environment, with software installed from trusted media and data restored from the pre-incident immutable backup. Passing the test does not approve it for production.

Candidates considered (professional judgment)

| Candidate | Decision | Reason |
|---|---|---|
| A. New build plus immutable backup, in an isolated environment | Test now | Only option that does not depend on anything the attacker could reach |
| B. Standby gateway | Second choice, only if A fails; same checks apply | May share accounts, secrets or replicated encrypted data with the original |
| C. Repair or decrypt the original gateway in place | Rejected | It is the compromised environment and is held as evidence |
| D. Secondary process | Continues as the interim service | Not a recovery of the gateway |

Integrity checks on the backup and the restored build
1. Provenance. Backup system logs show the retention lock was never lifted, with no deletion or change attempts, in particular by the vendor credential or other suspect accounts. The catalogue checksum matches at restore.
2. Date test. The backup time is compared with the earliest sign of attacker access from the forensic timeline. If the backup is later than that sign, or the timeline cannot rule it out, only data is restored from it: no programs, accounts, scheduled jobs or configuration.
3. Clean build. Operating system and gateway software come from trusted installation media and are compared with reference checksums. Only authorised software is present.
4. Scan. The restored content is scanned for the indicators from this incident: attacker tools, added accounts and keys, scheduled tasks, altered rules.
5. Baseline. Configuration, system parameters and account lists are compared with the approved pre-incident baseline; every difference is explained by an authorised change record.
6. Entry route closed. No vendor remote access path, all secrets newly issued, multi-factor authentication on administrator access, logging and clock synchronisation on, endpoint protection installed, and a vulnerability scan passed.
7. Function. Synthetic test instructions only, sent to simulators. No real customer instruction and no connection to payment interfaces.
8. Independent review. A reviewer who did not build the candidate checks the results.

Separation checks
- Network: a new segment with deny-all to the isolated gateway segment and to production. Verified by rule review, a scan from both sides and flow records showing no traffic.
- Identity: new accounts and newly generated keys and certificates; no trust relationship with the compromised directory; no vendor accounts.
- Management: clean administrator workstations; no shared management tooling, storage or backup agents with compromised hosts. If the same virtualisation or storage platform must be used, it is checked for compromise first.
- Data path: backup media mounted read-only, one-way transfer in. The immutable copy is never attached to the compromised environment.
- Evidence: nothing in the test touches the original gateway.

Stop triggers
- Any incident indicator in the restored content, or a checksum mismatch: stop, quarantine the candidate, move to an earlier copy or data-only restore.
- Any traffic between the recovery environment and the compromised segment: stop and rebuild the separation.
- Backup date cannot be placed before the attacker's first access: system state from the backup is not used.

Accountable owner: SEC for candidate selection on security grounds, the test criteria and the test report. Executing parties: IT Operations and the backup team (build and restore), forensic staff (date test and scan), an independent reviewer from technology risk or internal audit, the payments information owner (functional test). CMT decides on production.

Time (judgment targets; restore duration is unknown, so later times are conditional): provenance and date test by 09:00 HKT; isolated environment built and separation verified by 11:00; restore and checks 3 to 6 by 15:00; functional test by 16:30; SEC test report (pass or fail per criterion) to CMT by 17:00.

Destination and channel: the isolated recovery environment, under an emergency change record; test report to CMT, the information owner, LC and IT Operations by the restricted incident workspace; every step in the incident log.

Basis
- R03, HKMA Sectoral Code, s.6.2.16(a), PDF p.15: change controls adhere to "relevant requirements outlined in SPM TM-G-1 sections 4.2.4 and 4.3". R08, SPM TM-G-1, s.4.2.4, PDF p.18: "System and user acceptance testing should be carried out in an environment separated from the production environment." and "only properly tested and approved systems are promoted to the production environment". Authority: sectoral code under Cap. 653 s.8, pointing to HKMA supervisory guidance. It applies because the candidate is a rebuilt version of the designated gateway. It also says production data is not to be used in testing unless de-sensitised, which is why function is tested with synthetic instructions.
- R03 s.6.2.15(a), PDF p.15, refers to TM-G-1 s.3.4.1. R08 s.3.4.1, PDF p.14: "integrity of static data (e.g. system parameters) should be periodically checked to detect unauthorized changes". Supports check 5.
- R03 s.6.2.20(b)(i), PDF p.17: "implement a secure tertiary data backup (STDB)". R04, SPM TM-C-1, s.4.3, PDF p.8: such backup is "to recover and restore critical data promptly in the event that a cyberattack compromises both the production and backup environments of AIs". Missing fact: whether this backup is that tertiary copy and whether it covers system state as well as data. The HKAB guideline R03 cites is not in my manifest.
- R02, OCCICS Code of Practice (Generic), s.6.2.20(a), PDF p.18: "Backup restoration tests should be conducted regularly without affecting the production environment." Generic-code text, used as principle for testing away from production. s.7.2.4(c), PDF p.34: "Disaster recovery planning focuses on the effective restoration of CCSs from severe disruptions".
- R14b, Annex to HKMA circular on good practices, item 6, PDF p.5: practices include "setting up dedicated environments and utilities for recovery". Encouraged good practice, not a requirement.
- R07, SPM TM-G-2, s.4.6.2, PDF p.13: "Access to back-up vital records should be adequately controlled to ensure that they are reliable for business resumption purposes." s.4.3.3, PDF p.11: plans should cover "the verification of the safety and readiness of the permanent site". Supports checks 1 and 6.
- R08 s.4.3.3, PDF p.20: "Emergency changes need to be reviewed by independent personnel to ensure that the changes are proper and do not have an undesirable impact on the production environment." Supports check 8.
- R01, Cap. 653, s.27(5), PDF p.43, with Schedule 3 Part 2 item 5, PDF p.93 (quoted in C04). Missing fact: the bank's recovery plan; where it names a recovery method, that is followed.

No direct rule located in assigned sources for choosing between candidates, the date test, scanning a restored backup, data-only restore, or the separation checks. Files: all. Terms: regex "restor|rebuild|clean environment|golden image|recovery environment|dedicated environment"; regex "immutable|tertiary|STDB"; regex "failover|fail-over|fallback|alternate site". These are professional judgment: a backup is "pre-incident" only relative to the encryption, and the attacker's first access may be earlier.

---

Q13b - Offline transaction reconciliation checks before the candidate is considered for production

Decision. The candidate is not put forward for production until a reconciliation, run offline on data extracts, ties with no unexplained difference. Nothing is posted or sent during these checks.

Data sets (each extract hashed and entered in the evidence register)
- Candidate state as restored, at backup time T0.
- Core ledger extracts at T0 and at the test time.
- Independent records of gateway activity from T0 to the failure: central logs, outbound message records, and confirmations or statements from receiving parties.
- The C04 instruction register: released, held, cancelled, duplicate and remaining items.

Checks and acceptance criteria

| Check | Test | Pass condition |
|---|---|---|
| 1. Baseline | Candidate at T0 against ledger at T0: counts, totals, last sequence number | Zero difference |
| 2. Gap period | Every transaction from T0 to the failure classified as settled, not settled or unknown, from independent records | All classified; "unknown" items stay held and are not loaded |
| 3. Secondary process | Every item released by the secondary process is marked complete in the candidate | Counts and values equal the register |
| 4. Queue tie-out | Original queue equals released plus held plus cancelled plus remaining | Zero difference in count and value |
| 5. Three-way match | Customer instruction, ledger posting and external confirmation agree, for all items in total and item by item on payroll | No item present on fewer than three sides without explanation |
| 6. Replay protection | Identifiers of settled and released items are fed to the candidate offline | 100% rejected |
| 7. Sequence numbers | Message and reference counters are set above the highest value used by the gateway and the secondary process | No reference can repeat |
| 8. Static data | Payee, routing and limit data against the approved baseline and ledger | Differences matched to authorised change records |
| 9. Settlement position | External statements, ledger and candidate | Agree |
| 10. Dry run | A copy of instructions already processed by the secondary process is run through the candidate to a simulator | Outputs match actual results item by item; no unexpected message |

Sign-off: maker and checker in payments operations and finance; independent review; SEC attests to the integrity of the extracts and the test environment; the payments information owner signs.

Scope of offline results (judgment). The offline result shows the tested copy was consistent at the test time. It does not validate live connectivity or cover items processed after the extracts. Before any cut-over, a final delta reconciliation covers items since the extracts, the secondary process stays available as fall-back, and a live test follows cut-over.

Stop triggers: any unexplained difference; signs that records in the backup were altered; missing external confirmations for the gap period; a replay that is accepted.

Accountable owner: SEC for the check design and integrity attestation. Executing parties: payments operations and finance (reconciliation), IT Operations (extracts and dry run), independent reviewer, payments information owner (sign-off), CMT (production decision).

Time (judgment targets, conditional on the candidate passing Q13a): check design agreed by 09:00 HKT; extracts by 12:00; checks 1 to 10 between 15:00 and 20:00; reconciliation report to CMT by 21:00. Observable trigger: no production proposal without a signed report showing all ten checks passed.

Destination and channel: reconciliation workspace in the isolated environment; report to CMT, the information owner and LC through the restricted incident workspace.

Basis
- R09, SPM TM-E-1, s.5.1.2, PDF p.19: "AIs should also implement sufficient controls to maintain and verify the integrity of the information processed by their Internet banking systems.", for example to "reconcile data file balances after transaction updates and to check the integrity of data transmitted between different systems". HKMA supervisory guidance; applies to instructions from mobile and Internet banking and is used as principle for other channels. It does not list the checks.
- R14b, PDF p.2, item 1: "reconciliation procedures to maintain accuracy following a bypass". Encouraged good practice; on point for checks 3 and 4 because the secondary process is a bypass.
- R07 s.4.3.2, PDF p.11: alternate processing "may entail record reconstruction and verification". Supports check 2.
- R08 s.4.3.1, PDF p.19: change management includes "a process for rolling-back changes to re-instate the original programs, system configuration or data in the event of production release problems" and "a post implementation verification of the changes made". Reached through R03 s.6.2.16(a). Supports the fall-back and live test.
- R09 Annex B, PDF p.40, items B.2 and B.3: "well-tested fall-back procedures to cater for any exceptional and unexpected situations" and "Live test after the scheduled system maintenance/drills to ensure the effective operation of the relevant services". Written for scheduled maintenance and drills; used as principle.
- R09 s.9.4.1, PDF p.35: "It is important that the actual effectiveness of the resilience of the system should be properly verified and tested."

No direct rule located in assigned sources for the ten checks, the pass conditions, replay testing, counter resetting or the delta reconciliation. Files: all. Terms: regex "duplicat|reconcil|retry|re-attempt|idempot"; regex "parallel run|dry run|cut-?over|go-live|live test|acceptance test|fall-?back procedure|roll(ing)?-?back"; regex "integrity of (transactions|data|information|records)|transaction integrity|data integrity|accuracy, completeness|non-repudiation|authoris(ation|ed) of transactions". These are professional judgment: a restored system knows nothing after T0, so the main risks are paying again what has settled and losing what has not.

---

Facts SEC passes to the incident team (09:00, 17:00, 21:00, and at any trigger)

| Fact | Status at 08:00 | Used by |
|---|---|---|
| Records confirmed exported and now public | 320 customers, including the original 80 | LC, COM (Q15a) |
| Scope estimate | Raised from 80 to 320 by the mirror, an "up" trigger under C03. The earlier single-file finding was incomplete, so SEC's confidence that the wider set is unaffected is lower. The 18,000 figure remains unverified | LC, COM |
| Which 240 individuals are new | List by internal reference being produced by the C02 validation method; time to be confirmed by 09:00 | COM, LC |
| Mirror and fake page evidence | SEC captures both with hashes for the evidence register, without spreading the data further | LC (Q14b referral material) |
| Fake verification page | Not yet confirmed as outside bank infrastructure; SEC checks, blocks it on bank networks, and supplies address details for a removal request. R09 s.4.3.2, PDF p.17: "AIs should make attempts to remove the fake or suspicious items where practicable" | COM (Q15b), LC |
| Recovery candidate | Under test; no production date; result 17:00 | CMT, COM (no restoration promise) |
| Immutable backup | Exists; suitability and date against first attacker access unverified | CMT, LC |
| Interim service | Secondary process continues | COM, CMT |
| Restored-system report fields | R02 Annex F item D, PDF p.45: "Affected systems have been restored" is not yet true | LC |
| Material change check | Bringing a rebuilt gateway into service may be notifiable under R01 s.22 (cited in C04); for LC to assess | LC |
| Previous ransom decision and customer notification record | SEC holds neither and cannot attest to them | LC, COM |

Limitations: text search and page reads only. Not available to me: the bank's recovery plan, C-RAF, the HKAB STDB Guideline cited by R03, and backup system records.