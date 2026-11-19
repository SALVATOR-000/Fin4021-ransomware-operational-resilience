SEC (Information Security Lead), locked response for C02, Monday 16 Nov 2026, 09:30 HKT (H+1:30). This answers only Q04a and Q04b. No handoff was received for SEC.

Facts I treat as unverified:
- That the attacker copied customer files.
- Where the screenshot came from and whether it is genuine.
- Whether the vendor's remote account was the way in.
- Whether the vendor will actually preserve its logs. It has only said it can do so on request.

Facts as given:
- A demand for 6 BTC by 02:00 HKT on 17 Nov.
- The secure filing channel is available again. That means my C01 logged decision on the filing terminal can be closed out.

All actions below are simulated, for the facilitator to log.

== Q04a: Validating the sample while limiting further exposure ==

**Decision and action**

1. **09:30–09:45: take the screenshot into evidence.** The screenshot, the demand and the message they came with go into the evidence process only.
   - The evidence custodian gives each an evidence ID, a SHA-256 hash and full message headers, and records source, time, collector and witness.
   - If anyone outside SEC received it (branch, COM, any mailbox), they forward it unchanged to the SEC evidence intake and do not reply or reshare. The custodian logs each copy and has stray copies deleted after capture.
   - Nobody asks for more samples, opens attacker links, replies to the attacker, or uploads the material to any outside service. That includes reverse image search, paste-site lookups and online OCR.
2. **Need-to-know handling.**
   - Only two named SEC forensic analysts and the DPO (or a DPO designate) see the unmasked rows, and only on an offline workstation in the bank's forensic lab.
   - The screenshot is not circulated by email or chat, not shown at the CMT, and not used in COM or LC drafts.
   - All reporting refers to rows by row number and masked identifiers (for example, the last 4 ID characters and the internal customer number).
3. **Validation steps, running in parallel, results logged by about 12:00 HKT.** The timing is my professional judgment; I explain it under Basis.
   - (i) **Structural match.** Compare the field names, field order, formats, internal customer numbers and code values against the bank's own data schemas, so we can identify which system and table the rows could come from (gateway payee/payroll files, CRM, core banking).
   - (ii) **Record match.** The DPO-approved analyst runs a minimal, logged, read-only lookup of only the visible rows against the bank's records. The analyst uses a replica or the forensic copy, never the held gateway hosts. Each row is recorded as one of:
     - matches a current record;
     - matches a stale record (that shows the date range of the data);
     - no match.
   - (iii) **Exfiltration evidence (the decisive test).** Examine the held logs and images for:
     - bulk reads and exports;
     - archive or staging files;
     - unusual outbound data volume through the firewall, proxy and DNS;
     - vendor remote sessions that touched data stores.
     A matching row shows the data is real. It does not show that it was taken in this incident.
   - (iv) **Fabrication or recycling check.** Compare against any internal records of past incidents. No external upload is involved.
4. **Result categories reported to the CMT.**
   - *Not genuine.* This can only be stated once (ii) shows no match and (iii) shows nothing.
   - *Genuine, source system identified, exfiltration not shown.*
   - *Confirmed exposure.* The rows match and there is evidence of access or copying.
   - *Indeterminate.*
5. **Stop or escalation trigger.** If any row matches a real customer, I tell the DPO, LC and the CMT chair at once, without waiting for the full analysis. That moment is logged as the "first confirmation of exposure" for those customers. Two consequences follow:
   - Those customers are a notification batch to be notified as soon as practicable. The wider scope review must be done within 12 hours (by first confirmation + 12h), with my evidence on which tables or stores were reachable.
   - LC sends an immediate HKMA update, because confirmed data exposure is an update trigger.
   An unverified claim, or the size of a data store, does not by itself make the whole store a notification batch.
6. **Limits on the work itself.**
   - Analysis is done on verified copies only.
   - Working extracts are erased when the task ends unless LC directs preservation.
   - The retained forensic firm sees masked extracts only. The full screenshot does not leave the bank without written approval from both LC and SEC.
   - No contact with the attacker to "prove" the claim. Any contact needs the CMT chair's written authorisation; that is LC's Q05b.

**Owner and execution**
- Accountable: SEC.
- Executing: the evidence custodian and two named SEC analysts.
- The DPO approves and witnesses the record lookup.
- The forensic firm works on masked data only.

**Deadlines**
- Intake and hash: by 09:45.
- Row-match result: target 11:00.
- Exfiltration assessment: interim at 12:00, then in each hourly SEC status report.
- A positive match is escalated at once.
- Everything feeds LC and the CMT well before the 02:00 demand time.

**Recipients and channels**
- Evidence register and decision log.
- Verbal briefing in the CMT room to the CMT chair, LC and DPO.
- Written results on paper or the secure lab system. Corporate email is not used unless it has been logged as safe.

**Basis: external**
- **R10, Cap. 486 PDPO, Sch.1 DPP4(1), PDF p.169:** "All practicable steps shall be taken to ensure that any personal data ... held by a data user is protected against unauthorized or accidental access, processing, erasure, loss or use".
  - Authority: statute.
  - Why it applies: the rows look like identity data. If they are genuine, they are personal data held by the bank, so internal handling during validation must also prevent unauthorised access.
  - Left to judgment: the specific steps.
- **R11, PCPD Guidance on Data Breach Handling (June 2023), PDF p.4, "Step 1: Immediate gathering of essential information":** "the data user shall promptly gather all relevant information of the data breach". Its listed questions include "What kind of personal data was involved?" and "How many data subjects might be affected?".
  - Authority: regulator guidance.
  - It supports a prompt, structured assessment. A breach is not yet confirmed, so I apply it as an assessment framework.
  - PDF p.5, Step 3: risk factors include "The kind and sensitivity of the personal data being leaked".
- **R16b, HKMA circular "Customer Data Protection" (14 Oct 2014), PDF p.2, "Controls for handling incidents involving loss or leakage of customer data":** procedures should include "ascertaining the nature of the incidents, the causes of the incidents and identity of customers affected".
  - Authority: HKMA circular.
  - It applies to suspected leakage of customer data.
- **R02, OCCICS CoP s.7.2.3(a)(v)(2)–(3), PDF p.32:** evidence handling and "Investigating the cause and impact of the incident".

**Basis: internal (Internal bank procedure, PH01 v1.0)**
- **s.6.6 "Attacker material":** "Samples, demands and messages from an attacker are received only into the evidence process. Nobody requests further samples, visits attacker links or uploads attacker material to an outside service."
- **s.10.4(a)–(c):** confirmed or evidenced exposure is notified as soon as practicable; the scope review is due "No later than 12 hours after the first confirmation of exposure"; and "An unverified claim, or the size of the data store, does not by itself make everyone in the store a notification batch."
- **s.16.2:** "By default the firm receives a minimised data set with customer personal data masked."
- **s.12.3:** no contact with the attacker.
- **s.17.2:** working copies are erased.
- **s.5.8:** HKMA update on confirmed data exposure.
- Conflict check: none. PH01 is consistent with DPP4, R11 and R16b.

**Professional judgment**
- I separate "data is genuine" from "data was taken in this incident" because a match alone could reflect old or third-party data. Only log evidence of access or exfiltration establishes exposure.
- The 11:00/12:00 targets are my judgment, set so that LC and the CMT have a validated position early in the extortion window and before COM's next six-hourly update.

== Q04b: Evidence to request from the vendor and how to receive it ==

**Decision and action**

1. **Immediate written preservation and production request.** PH01 6.7(a) set a due time of 09:00, one hour after declaration.
   - If my C01 draft has already gone to this vendor, I confirm it and issue a supplement naming the remote account.
   - If it has not gone, the request is overdue. I issue it now, no later than 10:00. LC clears the wording in parallel. The vendor relationship owner sends it to the contract contact in the third-party register and confirms receipt by call-back to a number already on file. We do not use any number supplied in the vendor's own outreach.
   - The facilitator should log whether the request was sent at 09:00. I cannot verify this from the card.
2. **Scope of the request.** Covers 1 Oct 2026 to now, or the vendor's full retention period if longer. The extra time window is my judgment, to cover initial access.
   - Remote access and session logs for every account the vendor has used on bank systems: logon and logoff, source IPs, MFA events, session recordings, commands and file transfers.
   - Account records: which named individuals used the account; whether it was shared; credential and MFA changes; who holds the secrets.
   - Logs from the vendor's own jump hosts, VPN and endpoints used to reach the bank, plus EDR alerts on those endpoints.
   - Support tickets, change records, and scripts or tools deployed to the gateway.
   - Any bank data the vendor holds or copied: what it is, where it is, and the access log for it.
   - The vendor's own incident status: any known compromise of its staff or systems, and other clients affected. Its answer is recorded as the vendor's account only.
   - Confirmation that the vendor has suspended rotation and deletion for all of the above. This mirrors LC's legal hold under PH01 17.1.
3. **Delivery channel.**
   - Native exports with a SHA-256 manifest, delivered through the bank-hosted encrypted transfer or on bank-issued encrypted media collected in person by the evidence custodian.
   - Never by ordinary email, and never through the vendor's own remote access path.
   - The custodian checks the hashes against the manifest, enters each item in the evidence register (Annex B fields), and works on copies only.
4. **Containing the vendor path, done alongside the request.** The vendor account is the gateway's only known remote path, so I treat it as a suspected compromised credential.
   - Capture session and token state (10 minutes at most).
   - Terminate all sessions, revoke tokens and keys, disable this account and every other account belonging to the vendor, and block the vendor's remote path at the perimeter. IT Operations and Network execute this under an emergency change.
   - Closure test: a replayed token and a logon with the old credential must both fail. Log the result and the time. Until then the access window counts as open.
   - Reinstatement only on my written sign-off and the CMT chair's decision, once the cause is known and the access meets the 7.2 standard (named accounts, MFA, time-limited, recorded).
   - If the vendor needs to support recovery, it does so only under bank-controlled, supervised sessions after reinstatement. Its old path is not reopened.
5. **Escalation.** If the contract rights (log retention, audit and production) or delivery cannot be confirmed by the due time in the request, the vendor relationship owner escalates to LC and the CMT chair. I set that due time at 12:00 HKT on 16 Nov, which also meets the outer four-hour limit counted from declaration. LC decides on formal contractual notice.
6. **Reconciliation.** Vendor records are treated as the vendor's account until I have reconciled them with the bank's own PAM, firewall and gateway logs. Any gap goes to the incident team as unverified.

**Owner and execution**
- Accountable: SEC, who drafts the request and decides containment.
- LC clears the wording and decides contractual notice.
- The vendor relationship owner sends the request and does the call-back.
- The evidence custodian receives the material.
- IT Operations and Network execute the lockout.

**Deadlines**
- Request out and receipt confirmed by 10:00.
- Vendor lockout and closure test: target 10:00.
- Vendor confirmation of preservation and delivery: 12:00, with escalation if missed.
- Delivery: as the request sets. I propose an initial log export by 14:00 HKT. That is my judgment.

**Recipients and channels**
- The contract contact in the third-party register, by a written request plus call-back on a number on file.
- Material back through bank-hosted encrypted transfer or bank-issued media.
- Records in the evidence register, decision log and emergency change record.

**Basis: external**
- **R03, HKMA Sectoral CoP for Designated AIs, s.6.2.25(a), PDF p.19:** "A Designated AI should manage supply chain risks of CCS arising from the engagement with suppliers".
  - Applies because the vendor has remote access to a designated critical computer system.
  - Left to judgment: the specifics of the request.
- **R03 s.6.2.23(c)–(d), PDF p.18:** logs "should be secured so that they cannot be deleted or altered" and "contain sufficient information to support after-the-fact investigation". This supports demanding preserved, native, hashed logs.
- **R02, OCCICS CoP s.7.2.3(a)(v)(2), PDF p.32:** evidence handling must cover "preservation of evidence and chain of custody". This supports the hash manifest and custodian receipt.
- **R12, SPM SA-2 Outsourcing, s.2.8.1, PDF p.8:** "data retrieved from the service providers are accurate and available in Hong Kong on a timely basis".
  - Applies if the support arrangement is an outsourcing. That is unverified; LC should confirm the contract.
- **R10, PDPO DPP4(2), PDF p.169:** if the vendor processes personal data for the bank, the bank "must adopt contractual or other means to prevent unauthorized or accidental access". Whether the vendor processes personal data is unknown and must be confirmed.
- **R11, PDF p.4–5, Step 2:** containment measures include "Changing users' passwords and system configurations to block any (further) unauthorised access" and "Removing the access rights of users suspected to have committed or contributed to the data breach".

**Basis: internal (Internal bank procedure, PH01 v1.0)**
- **s.6.7(a)–(d), "Evidence held by suppliers":** (a) "Within one hour of declaration SEC drafts a written preservation and production request"; (b) "They are never received by ordinary email or through the supplier's own remote access path"; (c) escalation "in any case within four hours"; (d) reconciliation.
- **s.7.3:** "terminates all sessions, revokes tokens and keys, and disables the account and every other account of the same vendor. The vendor's remote path is blocked at the perimeter."
- Also s.7.4 (closure test), s.7.5 (reinstatement) and s.17.1 (LC legal hold to the vendor).
- Detail left to judgment: PH01 6.7(c) does not say what the four hours run from. I have read it conservatively as 12:00 HKT.
- Conflict check: none found.

== Facts passed to the incident team ==
1. **To LC (for Q05 and regulatory updates):**
   - The data-theft claim is unverified, and the validation plan and timing are in place.
   - Any positive match is escalated at once; it triggers an HKMA update and is the start point for PCPD and customer-notification assessment.
   - The vendor request has been issued and the vendor path is closed.
   - Whether the vendor was the route in is unknown.
   - The demand has been received and is held in evidence.
   - The secure filing channel is available; my terminal entry has been closed out.
2. **To the DPO:** the data types visible in the screenshot and the candidate source system once identified. The rows themselves are not passed.
3. **To COM (for Q06):**
   - Confirmed: no change to balances found so far. This is unverified until Payments reconciles; it is Payments' figure to confirm, not mine.
   - The data claim is under investigation.
   - Do not quote or describe the screenshot contents.
   - Staff must pass any attacker contact to SEC and not reply.
4. **To the CMT chair:** the containment status of the vendor path and the first exfiltration assessment at 12:00.