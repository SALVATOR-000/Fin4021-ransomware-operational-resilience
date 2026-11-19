SEC (Information Security Lead): locked response for C02, Monday 16 Nov 2026, 09:30 HKT (H+1:30)

Assigned units: Q04a and Q04b only. The C01 report was handed back earlier. No facilitator handoff was addressed to SEC for C02.

Working assumptions (please log them):
- PH01 Severity 1 is reconfirmed. An extortion demand has been received and customer data exposure is suspected (PH01 4.1).
- No conflict was found between PH01 and any applicable external requirement for these units. Details are in each unit.

Facts not known at this card:
- How and when the demand and screenshot arrived (channel and time received).
- Whether the screenshot rows match any bank record.
- Whether the vendor account was the route for the unauthorised commands.
- Whether the vendor account is shared or named.
- Whether the vendor holds bank customer data.
- The contract's log-retention, audit and production terms.
- Whether the support contract is an outsourcing arrangement.
- Whether any unauthorised debits occurred.
- Whether corporate email has been logged safe. My 08:30 log result is not in the released facts. Until it is, nothing below goes by corporate email.

---------------------------------------------------------------
UNIT Q04a: Validate the sample while limiting further exposure

DECISION AND ACTION (simulated, for the log)

V1, 09:30. Take the attacker material into evidence (PH01 6.6, 6.3).
- The evidence custodian registers the original demand and screenshot exactly as received, with message headers and file metadata, a SHA-256 hash and a witness.
- If they arrived in a staff mailbox, web form or branch device, the original stays there under hold. Access to it is restricted and further forwarding is blocked.
- Staff who received it pass it only to SEC (PH01 12.3).
- Prohibited: replying to the attacker, asking for more samples, opening attacker links, or using any outside service. That includes cloud OCR, AI tools, reverse-image search and paste sites.

V2, 09:45. Name a need-to-know validation cell and record it in the evidence register. Every access is logged (Annex B).
- Members: one SEC analyst; one data-owner query operator; one Data Protection Officer (DPO) delegate; the custodian as witness.
- The DPO is consulted on the matching method at the start. This is consultation, not a hold.
- The screenshot is viewed only on an isolated, non-networked workstation in the bank's forensic lab (PH01 16.2).
- The image does not go into CMT papers, chat, email or the Board pack.

V3, 09:45 to 11:00. Minimised matching (judgment).
- In the lab, record per row the field types and any identifiers.
- The data-owner operator runs read-only, exact-match lookups on those specific identifiers only. The lookups return match / no match plus the source system and the record's date, not full records. There is no bulk extraction.
- Stores to search (judgment): the customer master, and the payroll submission files. Payroll rows may belong to SME employees who are not bank customers, so the DPO's affected group may extend beyond customers.
- Format attribution: check whether the layout, field order, internal codes or record dates match a specific bank system or export. This tells us where the data came from and roughly when it was copied.
- Per-row result: confirmed match, partial match, no match, or cannot be determined.

V4, by 11:00 (judgment). Preliminary result to LC, DPO and the CMT chair.
- It goes in person in the CMT room or by phone, plus a decision-log entry. It is a masked summary only: number of rows, field types, how many match, the system it is attributed to, and stated uncertainty.
- The names of matched individuals go to the DPO only, on paper or through the evidence store. They do not go by email.
- This feeds the chair's Board-chair notice (within two hours of the demand, PH01 15.1) and LC's reporting. It holds neither (PH01 2.4).

V5, by 13:30 (judgment). Check the claim against the technical evidence, then report in SEC's hourly status reports (PH01 2.5).
- Sources: outbound traffic volumes, file-access logs on the attributed store, staging or archive files on the gateway hosts, and the vendor transfer records requested under Q04b.
- Output: whether bulk copying is supported by evidence, and a volume estimate with its uncertainty.

V6, how results may be used (judgment, aligned with PH01 10.4):
- Matched rows are evidence that those individuals' data was accessed or copied. They are notified as soon as practicable (PH01 10.4(a)). COM sends, the chair approves the audience, and the DPO is consulted.
- A match proves exposure of those rows only. It must not be extrapolated to a volume.
- A non-match does not prove that no data was taken. No statement may say "no data was taken".
- The claim and the screenshot do not on their own make everyone in a store a notification batch (PH01 10.4(c)).

V7, handling data during validation:
- Working copies are masked and kept in the evidence store.
- They are erased when the task is complete unless LC directs that they be preserved (PH01 17.2).
- The forensic firm receives only a masked version, with joint LC and SEC approval and the DPO consulted (PH01 s.3, 16.2).
- Any monitoring for publication of the data is done only by the forensic firm, with LC and SEC approval, without uploading the data and without visiting attacker-supplied links (PH01 6.6). This is a recommendation for the CMT.

Stop triggers:
- Rows attributed to a store outside the isolated gateway segment mean the compromise is wider. Containment is widened under my C01 trigger and the chair is phoned at once.
- Any sign that the screenshot file is malicious: stop viewing and analyse it as malware in the lab.

OWNER
- Accountable: SEC.
- Execution: the SEC analyst, the data-owner query operator and the custodian, with the DPO consulted.
- Notification decisions are not SEC's (PH01 s.3, s.10).

TIMES
- Intake at 09:30.
- Validation cell named at 09:45.
- Preliminary result by 11:00.
- Evidence check by 13:30.
- Then hourly reports.

DESTINATION / CHANNEL
- Original material: evidence store and register.
- Masked summary: CMT room or phone bridge, plus a decision-log entry.
- List of matched individuals: DPO only, on paper or through the evidence store.

BASIS: EXTERNAL (direct rules)
1. R10, Cap. 486 PDPO, Schedule 1, Data Protection Principle 4(1) (DPP4(1)), PDF p169.
   - Quote: "All practicable steps shall be taken to ensure that any personal data ... held by a data user is protected against unauthorized or accidental access, processing, erasure, loss or use".
   - Authority: statute.
   - Why it applies: the bank is the data user. The screenshot, and every copy or lookup made while validating it, involves personal data the bank holds or handles. Hence the lab-only viewing, the named cell and the masked outputs.
   - Left to judgment: the specific minimisation methods.
2. R11, PCPD Guidance on Data Breach Handling, June 2023. Authority: guidance from the PCPD, not law.
   - PDF p1, "What is a data breach?": "a suspected or actual breach of the security of personal data". The claim plus the sample makes this a suspected breach now.
   - PDF p4, Step 1: "the data user shall promptly gather all relevant information of the data breach to assess the impact on data subjects".
   - PDF p5, Step 3: lists the risk factors, including "The kind and sensitivity of the personal data". These shape what V3 records.
   - PDF p8: notification should be given "regardless of the progress of any internal investigation". Validation therefore never holds a report.
3. R16b, HKMA circular "Customer Data Protection", 14 Oct 2014, PDF p2, "Controls for handling incidents involving loss or leakage of customer data".
   - Quote: procedures include "ascertaining the nature of the incidents, the causes of the incidents and identity of customers affected".
   - Authority: HKMA circular to all authorised institutions.
   - Why it applies: this is a suspected privacy incident, and V3 is that "ascertaining" step.
   - For LC: PDF p3 expects serious privacy incidents to be reported to the HKMA "as soon as practicable after the AI concerned is aware of or notified of the incident".
4. R02, OCCICS Code of Practice v1.0. Effect: a validated match is a fact LC needs.
   - s.7.3.4(d), PDF p36: an incident is serious if it "has caused or is likely to cause the leakage of material volume of customer data".
   - s.7.3.3(b), PDF p35: lists, as an example incident, ransomware that "shows signs of data compromise".
   - Classifying the incident is LC's call.
5. Point for LC and the DPO, not relied on by SEC: R10 s.58(2), PDF p119, exempts some uses from DPP3 where the use is for crime detection. SEC's judgment is that matching the data to protect the data subjects is directly related to why the bank holds the data. LC and the DPO confirm the DPP3 basis at the same time; no hold is proposed.

NO DIRECT RULE LOCATED in the assigned sources for the method of validating an attacker-supplied sample.
- Files searched: PH01 and R01–R16d.
- Exact terms: "sample", "screenshot", "ransom", "extortion", "claim", "evidence", "forensic".
- "screenshot" returned no hits. The "sample" hits concern audit or testing, apart from PH01 6.6.
- V2–V7 are professional judgment.

BASIS: INTERNAL (Internal bank procedure: PH01, v1.0, effective 1 Oct 2026)
- s.6.6: "Samples, demands and messages from an attacker are received only into the evidence process. Nobody requests further samples, visits attacker links or uploads attacker material to an outside service."
- s.16.2: "Full images are examined only inside the bank's laboratory."
- s.10.4(c): "An unverified claim, or the size of the data store, does not by itself make everyone in the store a notification batch."
- Also s.10.4(a), s.3 (third-party data-sharing row), s.6.3, s.12.3, s.17.2, s.2.4 and s.15.1.

CONFLICT CHECK
- None found.
- PH01 2.4 and 10.4(a) are consistent with R11 p8 and R16b p3. The validation never holds LC's reports.

---------------------------------------------------------------
UNIT Q04b: What evidence to request from the vendor, and how to receive it

DECISION AND ACTION (simulated)

W1, 09:30, credential containment. The vendor remote access account reaches the affected system, and the route of the commands is unknown. So it is treated as a suspected compromised credential (PH01 7.3). If my C01 action A3 has not already done all of this:
- Capture the account's session and token state (10 minutes at most).
- Terminate its sessions and revoke its tokens and keys.
- Disable that account and every other account of the same vendor.
- Block the vendor's remote path at the perimeter.
- Change all associated passwords and secrets (R03 6.2.13(b)).
- Log the closure test: a replayed token and a logon with the old credential must both fail (PH01 7.4).
- Vendor access stays off until reinstated under PH01 7.5, by the chair on SEC's written sign-off (PH01 s.3).
- "A remote access account" may be a shared account, which would breach PH01 7.2. This is unverified; the request below asks who used it.

W2, by 10:00. SEC drafts the written preservation and production request (PH01 6.7(a)).
- Internal timing: the 09:00 target (one hour after declaration) is missed. The vendor was identified only at 09:30. Log it as late against an internal target, with that reason. No external deadline is involved.
- The draft is limited to what the vendor needs: account IDs and the time window. It contains no customer data, attacker material or indicators of compromise. Sharing incident data needs joint LC and SEC approval (PH01 s.3).
- What the vendor must preserve and produce, from the account's creation (or at least 90 days before 16 Nov, judgment) to now:
  - (a) Session and access logs: VPN or remote gateway logs, jump-host logs, session recordings, command logs, source IP addresses and devices, multi-factor authentication and failed-logon events.
  - (b) Account records: every account that can reach the bank, the named individuals who used each account or knew its credentials, creation and change history, credential-vault access logs, last rotation, and multi-factor enrolment.
  - (c) Support tickets and change records relating to the gateway, with the bank authorisations for each.
  - (d) An inventory of every piece of bank data the vendor holds (what, where, since when), and transfer records of any data moved from the bank to the vendor. These are needed to test the "copied files" claim (Q04a V5).
  - (e) Evidence from the vendor's own environment: the devices used for bank sessions are not to be wiped or re-imaged; any indicators of compromise it holds; and any sub-contractors involved.
- Conditions on the vendor: no access to bank systems; no scans of bank systems; no contact with the attacker; no deletion, log rotation or alteration; confidentiality; immediate notice to the bank of anything it finds.
- Requested response times (judgment):
  - written confirmation of preservation and of the contract terms by 11:30;
  - first production (last 30 days of session and access logs, plus account records) by 14:00;
  - the rest by 18:00, or as agreed.

W3, 10:15 to 10:30.
- LC clears the wording. LC's written legal hold to the vendor (PH01 17.1) goes in the same packet.
- The vendor relationship owner sends the packet to the contract contact listed in the third-party register kept by the Chief Risk Officer. It goes by a written route that does not depend on corporate email unless email has been logged safe: hand delivery or courier, or the bank-hosted encrypted portal.
- The relationship owner confirms receipt by calling back a number already on file.
- The vendor's unsolicited offer to "preserve session logs" is a claim to be checked through that call-back. It does not replace the full request.

W4, receiving the evidence (PH01 6.7(b)).
- Only native exports with a SHA-256 manifest are accepted.
- They come either through a one-time vendor account on a bank-hosted encrypted transfer service, or on bank-issued encrypted media collected in person by the evidence custodian.
- Never by ordinary email, and never through the vendor's own remote access path.
- On receipt the custodian checks the hashes against the manifest and records the transfer (from which named person at the vendor, to whom, when, signatures) and every access (Annex B).
- Analysis is done on verified copies only.
- Any customer personal data in the records is handled under the evidence controls, as DPP4(1) requires.

W5, reconciliation (PH01 6.7(d)). Vendor records count only as the vendor's own account until SEC has reconciled them with the bank's own logs (the session, firewall and gateway logs, C01 items E3/E4). Gaps or conflicts are logged as "unreconciled".

W6, escalation (PH01 6.7(c)). If the contract terms (log retention, audit and production rights) or the delivery status are not confirmed by 11:30, and in any case by 12:00 HKT:
- the vendor relationship owner escalates to LC and the CMT chair;
- LC decides on formal contractual notice; the chair decides any other step.
- 12:00 reads "within four hours" as running from declaration. If it runs from the request, the time would be about 14:30. The earlier time is used.

OWNER
- Accountable for the content: SEC.
- LC clears the wording and issues the legal hold.
- The vendor relationship owner sends the request and confirms by call-back.
- The custodian receives the evidence.
- Escalation goes to LC and the CMT chair.
- Reinstating access is the chair's decision on SEC's written sign-off.

TIMES
- Credential action at 09:30, immediately.
- Draft by 10:00.
- Sent by 10:30.
- Vendor confirmation by 11:30.
- Escalation by 12:00 at the latest.
- First production by 14:00; the rest by 18:00.

BASIS: EXTERNAL (direct rules)
1. R02, OCCICS Code of Practice v1.0, s.7.2.3(a)(v)(2), PDF p32.
   - Quote: "Digital evidence handling, including identification, collection, acquisition, preservation of evidence and chain of custody".
   - Authority: the Commissioner's code under Cap. 653 s.8. It covers category 3 (incident response) obligations of all CI operators (R02 1.1.3–1.1.4).
   - Why it applies: chain of custody covers evidence held by suppliers.
   - Left to judgment: the exact channel and the manifest format.
2. R01, Cap. 653, Schedule 3 Part 1, item 3, PDF p91–92. Authority: statute; this is required content of the security management plan.
   - Quote: item 3 requires policies for "(h) managing contracts and other communications with suppliers of computer-related services and products adopted for the systems in order to ensure that— (i) the CI operator concerned complies with category 1 obligations, category 2 obligations and category 3 obligations".
   - Effect: the bank uses its contractual levers so that supplier records support incident response.
3. R03, HKMA Sectoral Code for Designated AIs, s.6.2.13(b), PDF p14.
   - Quote: "all passwords are promptly changed if they have been or are suspected of being compromised".
   - Authority: the HKMA's category 2 code.
   - Why it applies: the vendor account's credentials give access to a critical computer system.
4. R16b, HKMA circular "Customer Data Protection", Annex C(vii), PDF p5.
   - Quote: "remote access by AIs' staff or service providers from external networks ... should be subject to robust authentication (e.g. two-factor authentication)".
   - Effect: multi-factor evidence is requested, and is a precondition for reinstatement.
5. R11, PCPD Guidance, PDF p5, Step 2: "Removing the access rights of users suspected to have committed or contributed to the data breach" and "Keeping a proper record of the compromised system for further investigation". This is a suspected breach (PDF p1).
6. Conditional on facts not known:
   - If the vendor processes bank personal data as a data processor: R10 DPP4(2), PDF p169–170, requires "contractual or other means" to protect the data. R11 PDF p4 suggests "Requiring the data processor to take immediate remedial measures". LC checks the contract.
   - If the support contract is an outsourcing: R12, SPM SA-2 Outsourcing, s.2.1.1 (PDF p4) says the bank keeps "ultimate accountability", and s.2.8.1 (PDF p8) requires that "data retrieved from the service providers are accurate and available in Hong Kong on a timely basis".
7. Supporting principle: R01 s.35(1)(a), PDF p50, lets the Commissioner require documents "in the possession, or under the control, of the operator". Section 37 (PDF p52–53) allows warrants requiring other organisations "to preserve the state of the system". Bringing the vendor's records under bank custody now keeps the bank able to produce them.

NO DIRECT RULE LOCATED in the assigned sources for the delivery specifics (SHA-256 manifest, bank-hosted transfer, call-back confirmation).
- Files searched: all allowed files.
- Terms: "supplier", "chain of custody", "preserv", "hash", "remote access".
- The external sources set the outcome (preservation and custody), not the mechanism. The mechanism comes from PH01 and professional judgment.

BASIS: INTERNAL (PH01 v1.0)
- s.6.7(a): "SEC drafts a written preservation and production request ... covering session and access logs, account records, support tickets, change records and any bank data the supplier holds."
- s.6.7(b): "never received by ordinary email or through the supplier's own remote access path".
- s.6.7(c): escalation "in any case within four hours".
- s.6.7(d): supplier records are "the supplier's account until SEC has reconciled them".
- s.7.3: "disables the account and every other account of the same vendor".
- Also s.7.2, s.7.4, s.7.5, s.17.1, and s.3 (vendor-reinstatement and data-sharing rows).

CONFLICT CHECK
- None found. Only the internal one-hour timing of PH01 6.7(a) was missed, and no external deadline depends on it.

---------------------------------------------------------------
FACTS SEC PASSES TO THE INCIDENT TEAM
In person or by phone, then the decision log and the 10:30 hourly status report.

To LC:
- An extortion demand was received (6 BTC, deadline 02:00 HKT on 17 Nov). The exact time and channel of receipt are being fixed from the evidence.
- The claim that customer files were copied, and the screenshot's origin, are both unverified. Preliminary validation by 11:00.
- The vendor remote account is a candidate intrusion route (unverified). It has been disabled, and the closure test is pending or logged.
- PH01 5.8 requires an HKMA update "at once" on an extortion demand. It is not held by SEC's validation.
- R02 7.3.4(d)/(e) and R16b p3 may be engaged; that is LC's assessment.
- The secure filing channel is available again. SEC will log whether the terminal is outside the isolated segment and not under evidence hold; if not cleared, LC uses the standby device.

To the DPO:
- The rows may include SME payroll beneficiaries who are not bank customers.
- Matched names come to the DPO only.

To COM, for fact-checking:
- Confirmed: a demand was received.
- Unverified: the data claim.
- COM must not say that data was or was not taken.
- Fixed lines (PH01 11.3) on not naming the vendor or the system remain in force.
- SEC can confirm only that SEC has not contacted the attacker. Whether a ransom has been paid must come from its owner as a verified fact.
- Branch callers asking "have my funds disappeared?": SEC cannot yet confirm that no unauthorised debits occurred. Scripts must not say "your funds are safe" until Payments Ops reconciles the ledger against the gateway logs. Staff should verify callers and give out no account data, because callers could be social engineering.

To Payments Ops:
- Priority check: reconcile the ledger against gateway activity for unauthorised debits since the earliest time the attacker is evidenced on the system.

To the CMT chair:
- The Board chair must be told within two hours of the demand (PH01 15.1), so by about 11:30.
- The CFO notifies the insurer within 24 hours of declaration (PH01 12.4).
- No contact with the attacker is to be made without the chair's written authority (PH01 12.3).

---------------------------------------------------------------
LOG-READY ACTIONS (HKT, status)
- 09:30: Demand and screenshot registered as evidence (executed).
- 09:30: Vendor accounts disabled, perimeter path blocked, closure test run (executed or confirmed; test result to be logged).
- 09:45: Validation cell named; DPO consulted (executed).
- By 10:00: Vendor preservation request drafted (scheduled; late against the internal one-hour target, reason logged).
- 10:15 to 10:30: LC clears the request; request and legal hold sent; call-back receipt (scheduled).
- By 11:00: Preliminary validation result to LC, DPO and chair (scheduled).
- 11:30: Vendor confirmation due (scheduled).
- 12:00: Escalation to LC and chair if not confirmed (trigger).
- By 13:30: Check of the data claim against the logs (scheduled).
- 14:00 and 18:00: Vendor production tranches (scheduled).
- Continuous: Widen containment if the rows are attributed to a store outside the isolated gateway segment (trigger).