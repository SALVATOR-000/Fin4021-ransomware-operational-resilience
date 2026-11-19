SEC RESPONSE - C02 (Mon 16 Nov 2026, 09:30 HKT, H+1:30) - Unit Q04 a and b. Locked before colleagues' answers.

Internal bank procedure (PH01): N/A for both units. PH01 is not in my allowed manifest, so no internal basis and no conflict check is possible.

Fact status I am working from
- Released by the card: a 6 BTC demand with a 02:00 HKT 17 Nov deadline; a claim that customer files were copied; a screenshot with several rows of apparent identity data; a Hong Kong support vendor operated a remote access account for the gateway and offers to preserve session logs on request.
- Unverified or unknown: whether the screenshot rows are the bank's data; which system they came from; when and how they were taken; the volume; whether the vendor account was the route for the unauthorised commands; whether the vendor itself is compromised; whether the vendor holds any bank customer data; the vendor contract terms; how and to whom the screenshot was delivered.
- Carried from C01: the vendor's remote access to the gateway stays suspended (C01 Step 2), and the evidence register is open.

---

Q04a - Validating the sample while limiting further exposure

Decision. Validate the screenshot in-house, in a closed two-person cell, using only what the bank already holds. No request to the attacker for more "proof", no visit to attacker links or leak sites, and no upload to any outside service. The screenshot is handled as three things at once: evidence, possible customer personal data, and a possibly hostile file. Until a result is issued, the status given to everyone is "claim unverified".

Simulated actions for the log
1. 09:30 - Intake control. The original message and file are preserved with headers and metadata, hashed (SHA-256) and entered in the evidence register. All other copies are recalled, and everyone who has seen or forwarded it is listed. No further circulation by email or chat.
2. 09:35 - The file is opened only on an isolated analysis workstation with no production connection.
3. 09:40 - Validation cell: one SEC forensic analyst and one delegate of the customer-data owner (privacy officer's office). Both named in the log; no one else views the rows.
4. 09:40-10:30 - Comparison, by read-only logged queries against the customer master and against gateway transfer and payroll file layouts:
   - Do the individuals exist in bank records, and do the values match exactly?
   - Does the layout (column order, headers, internal reference numbers) match a specific bank system or file type?
   - How current are the values, which indicates when the data was copied?
   - Are the individuals bank customers, or payees in SME payroll files who may not be bank customers?
5. In parallel - corroboration from C01 evidence: outbound traffic records for large transfers, gateway file and database access logs, and staging archives on the imaged hosts.
6. 10:30 - Result memo containing no personal data: number of rows checked, number matched, data categories (for example name, identity card number), likely source system, and a confidence level. Matched individuals are listed by internal customer reference only, held in the restricted evidence store.

Outcome classes and their limits (professional judgment)
- Match: those rows are genuine bank data from an identified source. This does not prove the volume claimed, or that the data was taken in this incident and not earlier or from another holder such as the vendor.
- Partial or inconclusive: reported as such, with the corroboration work continuing.
- No match: the sample is not shown to be bank data. This does not disprove copying.
- Production records show what the systems hold now; logs on compromised hosts may have been altered. Offline copies and central logs are more reliable but only to their capture time. Neither alone settles whether data left the bank.

Stop and escalation triggers
- Any match: the incident commander, LC and the privacy officer are told within 15 minutes.
- Data that could only have come from a system outside the gateway: the C01 trigger applies and containment scope is reviewed.
- Active content or malware in the file: validation stops and the file is handled as a malware sample.

Accountable owner: SEC. Executing parties: the validation cell. Legal classification, notifications and any contact with the attacker are LC's units; SEC's validation needs no attacker contact.

Time (judgment targets): intake controls 09:30; status line "claim unverified, validation under way" to COM and LC by 09:50, ahead of the reporter's 10:00 deadline; preliminary result 10:30; corroboration update 12:00. The attacker's 02:00 deadline is not treated as a validation deadline.

Destination and channel: result memo to the incident commander, LC and the privacy officer by the out-of-band bridge and the restricted incident workspace. COM receives the status line only, never the rows.

Basis
- R10, Cap. 486, Schedule 1, Principle 4(1), PDF p.169: personal data held by a data user is to be "protected against unauthorized or accidental access, processing, erasure, loss or use", with s.4, PDF p.21: "A data user shall not do an act, or engage in a practice, that contravenes a data protection principle". Binding statute. It applies if the rows are personal data the bank holds (s.2, PDF p.15: data "from which it is practicable for the identity of the individual to be directly or indirectly ascertained"). That is the fact under test, so I apply the protection from intake as a precaution.
- R11, PCPD Guidance, PDF p.1: "A data breach is generally regarded as a suspected or actual breach of the security of personal data held by a data user", and PDF p.4, Step 1: "the data user shall promptly gather all relevant information of the data breach to assess the impact on data subjects and to identify appropriate mitigation measures". Non-binding PCPD guidance; a suspected breach is enough to trigger it.
- R16b, HKMA circular "Customer Data Protection", PDF p.2, heading "Controls for handling incidents involving loss or leakage of customer data": procedures should cover "ascertaining the nature of the incidents, the causes of the incidents and identity of customers affected". Annex C(i), PDF p.4: access rights "should be granted on a need-to-have basis only". HKMA supervisory circular to all authorized institutions; supports the two-person cell.
- R02, OCCICS Code of Practice (Generic), s.7.2.3(a)(v)(2)-(3), PDF p.32: "Digital evidence handling, including identification, collection, acquisition, preservation of evidence and chain of custody;" and "Investigating the cause and impact of the incident;". Authority and scope as in my C01 answer.
- Fact for LC, not my decision: R02 s.7.3.4(d), PDF p.36, lists as a serious-incident criterion an incident that "has caused or is likely to cause the leakage of material volume of customer data". The incident is already serious on the core-function ground; the validation result feeds LC's reporting content.
- Check for LC: R10 s.2 "matching procedure", PDF p.15, concerns automated comparison for "10 or more data subjects" for the purpose of adverse action. Not my purpose, and the sample is several rows.

No direct rule located in assigned sources for how to validate an attacker-supplied sample, who may view it, isolated handling, or refusing further samples. Files: all. Terms: regex "exfiltrat|leak|dark web|screenshot|sample"; regex "mask|redact|anonymis|pseudonym|need-to-know|need to know|need basis|need-to-have"; "data processor"; regex "ransom payment|pay the ransom|extortion|blackmail|bitcoin|BTC|virtual asset" (one unrelated hit, R16c p.101). Those details are professional judgment: each extra copy or extra sample increases exposure, and a few matched rows cannot support conclusions about scale.

---

Q04b - Evidence to request from the vendor and how to receive it

Decision. Accept the vendor's offer now. Issue a written preservation and production request covering more than session logs. Receive the material as original exports with hashes, over a bank-controlled encrypted route, into the evidence intake. Treat it as the vendor's own account until reconciled with bank-side records. The vendor's remote access to the gateway stays suspended, and the vendor does not log in to "help" or to collect anything.

Preserve immediately (no deletion, no alteration, log rotation suspended) and produce:
1. Remote access session records for the gateway account: start and end times with time zone and clock source, source addresses and devices, the named individual behind each session, authentication and multi-factor events, commands or session recordings, and file transfers (names, sizes, direction).
2. Account administration: who held the credentials, whether shared, how stored, last password and multi-factor changes, joiners and leavers.
3. Vendor-side systems used to reach the bank: logs of the remote access tool, gateway or jump host, and security alerts and images of the workstations used.
4. Any bank data the vendor holds: configuration copies, file extracts, tickets with attachments, as an inventory first. This tests whether the screenshot could have come from the vendor's holdings.
5. Support tickets and change records for gateway work, the staff access list and any subcontractors.
6. A signed statement of what was preserved, by whom, when and with which tool; whether the vendor has detected any compromise of its own; and its log retention period.
Look-back: all retained sessions for 90 days to 09:30 on 16 Nov, with the 14 days before 08:00 on 16 Nov first (judgment). The vendor is also asked not to contact the attacker or media and to refer all queries to the bank.

How it is received
- Request: written notice from SEC with the vendor relationship owner, wording cleared by LC, sent to the contact in the contract and confirmed by call-back to a number already on file, not one taken from recent messages.
- Format: native exports, not screenshots or edited summaries, with a SHA-256 manifest created at export and a signed custody form.
- Transfer: a bank-hosted encrypted file transfer, or bank-issued encrypted media collected in person by the evidence custodian with a signed hand-over. Passphrase by a separate channel. Never ordinary email, the suspended remote access path or the isolated gateway segment.
- Receipt: quarantine intake, malware scan, hash verification, entry in the evidence register continuing custody from vendor to bank, analysis on copies only.
- Reconciliation: against bank-side remote access, privileged access and firewall logs. A discrepancy is escalated to LC, with independent collection at the vendor by the bank's forensic firm if the contract allows.

Accountable owner: SEC. Executing parties: vendor relationship owner (sends), evidence custodian (receives), forensic staff (verify), LC (contract rights and wording).

Time and triggers (judgment targets): request issued 09:45; vendor's written preservation confirmation 10:30; gateway account session records 12:00; remaining items 18:00. If there is no confirmation by 10:30, a refusal, or signs of deletion, LC is asked to serve formal contractual notice and the incident commander is told.

Basis
- R12, SPM SA-2 Outsourcing, s.2.1.1, PDF p.4: "AIs should therefore continue to retain ultimate control of the outsourced activity." s.2.8.1, PDF p.8: "data retrieved from the service providers are accurate and available in Hong Kong on a timely basis". s.2.6.4, PDF p.7: "AIs should establish reporting procedures which can promptly escalate problems relating to the outsourced activity". HKMA supervisory guidance. Missing fact: whether this support arrangement is "outsourcing" as defined in s.1.1.1, PDF p.2. If it is, these apply directly; if not, I rely on them as principle and on the items below.
- R16b Annex I, PDF p.8: "AIs should require their outsourcing operators and other service providers that store, transport or have access to customer data to comply with the AIs' data security policies and procedures". Annex C(vii), PDF p.5, on remote access by service providers: "the data being transmitted should be subject to strong data encryption". Supports the encrypted transfer. Missing fact: whether the vendor had access to customer data.
- R02 s.7.2.3(a)(v)(2), PDF p.32 (quoted above): chain of custody extends to evidence obtained from the vendor.
- R01, Cap. 653, Schedule 3 Part 1 item 3(h), PDF p.92: the security management plan covers "managing contracts and other communications with suppliers of computer-related services and products adopted for the systems". Missing fact: the plan and the contract.
- R02 s.6.2.25(e), PDF p.21: "The CI operator should reserve audit and compliance monitoring rights to verify that external service providers have implemented sufficient controls over its CCSs." and s.6.2.18(b), PDF p.17: "logging and monitoring remote access activities, and revoking authority and access rights when they are no longer needed". These are generic-code provisions. For a designated bank, R03 s.6.2.25(a), PDF p.19, and s.6.2.18(a), PDF p.16, point to an HKMA circular of 21 December 2023 and to C-RAF, neither of which is in my manifest. I use the R02 text as general principle only.
- R08, SPM TM-G-1, s.3.2.3, PDF p.13: "monitoring of the activities performed by privileged and emergency IDs (e.g. peer reviews of activity logs)". Bank-side records of the vendor account should exist for reconciliation; whether they do is unverified.
- R03 s.6.2.19(b)(ii), PDF p.16: "perform malware scans on portable computing devices and removable storage media to prevent a CCS from malware infection". Supports scanning the media on receipt.
- R03 s.6.2.13(b), PDF p.14: "where a password is the single authentication factor used by suppliers for maintenance and support, the password should be changed after every use". Missing fact: how the vendor account authenticated. The account stays suspended; credentials are reset before any reinstatement.
- Conditional on the vendor being a data processor (unknown): R10 Schedule 1, Principle 4(2), PDF pp.169-170: "the data user must adopt contractual or other means to prevent unauthorized or accidental access, processing, erasure, loss or use of the data transferred to the data processor for processing"; R11, PDF p.4: "Requiring the data processor to take immediate remedial measures and to notify the data user of the progress".
- Context, not a current duty: R01 s.37(2), PDF pp.52-53, lets a magistrate's warrant authorise requirements on "an organization having, or appearing to have, control over the investigated system (other than the investigated CI operator)". Whether the vendor has such control is unknown. No warrant or notice exists.

No direct rule located in assigned sources for the specific log types, look-back period, export format, hashing, transfer method or deadlines. Files: all. Terms: regex "session log|session record|access log|activity log" (one hit, R08 p.13); regex "remote access|remote connection|remote support|vendor"; "service provider" in R12; regex "supplier|third party|service provider|contractor" in R01. These are professional judgment: the vendor may bear liability, so its records need integrity controls and independent corroboration.

---

Facts SEC passes to the incident team (09:50 status, 10:30 result, then every 30 minutes)

| Fact | Status at 09:30 | Used by |
|---|---|---|
| Screenshot rows are bank customer data | Unverified; result due 10:30 | LC, COM |
| Data was copied out in this incident | Unverified; no evidence either way | LC, COM |
| Volume or categories of data affected | Unknown | LC (R16a form, PDF p.2: "Types of personal data involved") |
| Individuals may include SME payroll payees who are not bank customers | Possibility under test | LC, COM |
| Vendor remote access account for the gateway existed | Confirmed by card | LC (R02 Annex F nature box "Supply chain attack", PDF p.43; R16a p.2 service-provider question) |
| That account was used for the unauthorised commands | Unverified | LC |
| Vendor access to the gateway | Suspended since C01 | LC, CMT |
| Customer funds or balances altered | SEC holds no evidence of this and has not verified ledger integrity; a reconciliation check is requested from core banking operations, time to be confirmed by its owner | COM (branch calls), CMT |
| Ransom paid | SEC has no record of any payment or attacker contact; the decision is LC's unit | COM, LC |

Limitations: text search and page reads only. Not available to me: the vendor contract, the bank's security management and emergency response plans, C-RAF, and the HKMA third-party circular of 21 December 2023 cited by R03.