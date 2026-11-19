LC response, C08 Q23 — locked at 08:00 HKT, Thursday 19 November 2026 (H+72), before colleagues' answers.

The compliance work does not close with the exercise window. Eleven actions stay open and the register stays with my function. All incident records stay under a legal hold, with a first review on 18 December 2026. The most urgent open item is proof of when the written record reached the Commissioner: if only the 18 November filing can be evidenced, it was up to five hours late.

Internal bank procedure: N/A for both units. PH01 is not in my allowed manifest (search "PH01": 0 hits).

## Q23a — Compliance actions that stay open, and who receives the register

**Decision and action.** These actions stay open after handover. LC remains the accountable owner, because Legal and Compliance is a standing function.

| Open action | Lead | Date or trigger |
|---|---|---|
| Establish which Annex E filing is evidenced (16 or 18 November) and obtain the dispatch record | LC, SEC | Today, 12:00 HKT |
| Written incident report (Annex F) to the Commissioner | LC; SEC for technical content; Chief Executive approves | Submit 27 November; statutory limit 30 November 2026 |
| Answer on a sector-specific form | LC | Before the 20 November draft |
| Classification of the new indicator | SEC | On reasonable certainty of a separate incident: notify within 12 hours |
| Supplementary material after Annex F (root cause, attribution, wider data claim) | LC, SEC | As each is established |
| Material-change assessment for the containment changes, and for recovery once deployed | SEC assesses; LC files | Assessment by 30 November; filing by 16 December 2026 if material |
| HKMA: periodic updates; confirm receipt; confirm the notices on the secondary process and the Board meeting | LC | Today, then until resolution |
| Privacy Commissioner: prove the 16 November form is on file; file notification completion figures; assess any misdelivery among the 12 corrected contacts | LC, COM | Figures due today; update on any scope change |
| Police: reference number, signed receipt, remaining evidence, their view | LC, SEC | Today for the reference; evidence as imaging completes |
| Wallet-address check and any Cap. 455 disclosure | Disclosure officer, SEC | Today; open since 16 November |
| Board: minute the "do not pay" posture, the recovery gate, customer remediation and oversight; see Annex F | Chief Executive, company secretary | Minutes by 20 November; Annex F sight 26 November |

**If the Annex E filing was late.** If only the 18 November 13:30 filing can be evidenced, I do three things:
- brief the Chief Executive and the Board chair;
- keep the evidence of the 16 November attempt;
- hold the legal assessment as privileged.

**Further standing items.**
- The post-incident review, and resubmission of the emergency response plan within one month of any revision.
- Return or destruction of data held by the forensic firm.
- The vendor's contractual position.
- Any insurance notice (unknown to me).

**Who receives the register.**
- Keeper: a named deputy in Legal and Compliance, under my ownership.
- Full version, restricted: LC, the Chief Executive and the disclosure officer. It holds privileged assessments and the Cap. 455 item.
- Operational version (deadlines and owners only):
  - the Board's risk or crisis committee;
  - the employee supervising the computer-system security management unit;
  - the data protection officer;
  - COM's lead;
  - the head of the standing operations team;
  - Internal Audit, to track closure.

**Timing.** The register is issued by 12:00 HKT today. It is reviewed weekly until Annex F is filed, then monthly.

**Channel.** Handover meeting today, with written acknowledgement from each recipient.

**Basis and application.**
- R01, Cap. 653 (statute, version date 2026-09-10):
  - s.28(4) and Schedule 6 item 3 (pp.44, 97): written report within "14 days after the date on which the CI operator concerned becomes aware".
  - s.28(3) and Schedule 6 item 2: the written record was due 48 hours after the 08:30 notification, that is 08:30 HKT on 18 November. s.28(5) (p.44) makes failure an offence.
  - s.22(1) (p.33): material changes are notified "within 1 month after the date on which the event occurs". s.22(3)(a) (p.34) covers a change that affects the system's security or the bank's ability to respond.
  - s.27(4) (p.43): a revised emergency response plan is submitted "within 1 month after the date on which the revision is made".
  - s.21(1)(b) (p.31): the security management unit exists for "ensuring that this Ordinance is complied with". This is why its supervisor receives the register.
- R03, HKMA Sectoral Code (code of practice):
  - para 6.1.1 (p.11): the event date "generally refers to the moment when a change is deployed to production environments". The containment changes went live on 16 November, so 16 December 2026 is my computation.
  - para 6.1.3 (p.11): notice goes to the Monetary Authority in its specified form. That form is not in my manifest.
- R02, Code of Practice (Generic) (code of practice): para 7.3.7(a) (p.37) on supplementary material; para 7.2.3(i) (p.33) on the post-incident review.
- R07 SPM TM-G-2 para 1.3.3 (p.5, non-statutory guideline): the HKMA receives "periodic progress reports upon being notified until the final resolution of the crisis". The gateway is not back in production, so updates continue.
- R16b, HKMA circular (14 October 2014), p.2: a senior officer or committee oversees "the process of handling and reporting privacy incidents".
- R11, PCPD guidance, p.8: when full details are known, "all information should be submitted to the PCPD and other law enforcement agencies without delay".
- R16c, Cap. 455 s.25A(1) (p.83): disclosure "as soon as it is reasonable". Three days without an answer on the wallet address is too long.
- No direct rule located in assigned sources on a register of commitments or on incident handover. The register, its two versions and its recipients are professional judgment.

## Q23b — Records under preservation, review and disposal

**Decision and action.** I confirm a written legal hold today. It overrides routine deletion, log rotation and backup recycling for the systems in scope. These records stay preserved:
- Forensic evidence: original images of the gateway components, the diagnostic and recovery images, the quarantined host, hash values and the custody log.
- Logs: gateway, identity provider, vendor remote access, privileged access, perimeter and monitoring records, with the clock-offset record.
- Attacker material: the demand, the sample, any wallet address, and the captures of the public file and the fake page.
- Vendor material: session logs, credential and token records, the contract and correspondence.
- Decision records: the incident and dispatch logs, crisis team and Board papers and minutes, and every authorisation and risk acceptance.
- Regulatory and Police records: every form, report, call note, receipt and the register itself.
- Customer records: notification lists (including the superseded list and the 12 corrections), delivery evidence by batch, the 31 scam reports, complaints and remediation files.
- Payment records: queued and retried instructions, both reconciliation tests and the two mismatches, and counterparty correspondence.
- Legal advice, kept separately as privileged.

**Conditions while held.**
- Originals sit in write-protected storage with logged, need-to-know access.
- Personal data is encrypted.
- No in-scope system is re-imaged, decommissioned or returned to the vendor until it has been imaged and released in writing by LC and SEC.
- The vendor and the forensic firm receive written preservation requests.

**Review.** First review on 18 December 2026, then quarterly. An earlier review follows any closure notice from the Police, the Commissioner, the HKMA or the Privacy Commissioner.

**Release and disposal conditions (all required for a class of records).**
1. LC confirms in writing that no investigation, regulatory inquiry, prosecution or claim is pending or reasonably expected for that class.
2. The minimum retention periods have run. For system logs that is six months, so no earlier than mid-May 2027.
3. For records relevant to civil claims, I recommend keeping them for the limitation period. That period is my professional knowledge and is not in the assigned sources.
4. The post-incident review and all supplementary reporting are complete.
5. LC and the record owner approve in writing.

Disposal is by secure destruction, with a certificate and an entry in the custody log. Copies of customer data held only for the incident (extracts, working copies, the firm's and vendor's copies) are erased first, once they are no longer needed.

**Owner and executing party.** LC owns the hold and its release. Custodians are:
- SEC and the standing security team for technical evidence;
- the company secretary for Board records;
- COM for communications;
- payments operations for transaction records.

**Timing.** Hold confirmed by 10:00 HKT today; inventory of held records by 20 November.

**Recipient and channel.** A written hold notice to each custodian, the vendor and the forensic firm, with acknowledgement.

**Basis and application.**
- R03 para 6.2.23(c) (p.18, code of practice): "The logs should be retained for a minimum period of 6 months. Such logs should be secured so that they cannot be deleted or altered". This is a floor, not a disposal date.
- R02 para 7.2.3(a)(v)(2) and (4) (p.32): "preservation of evidence and chain of custody" and "Recording the incident response process".
- R01, Cap. 653 s.35(1)(a) (p.50) lets the Commissioner's officers require documents. s.42(1) (p.60) makes failure to comply, without reasonable excuse, an offence. Records must exist to be produced.
- R10, Cap. 486 (statute):
  - Schedule 1, Principle 2(2) (p.167): personal data "is not kept longer than is necessary".
  - s.26(1) (p.58): erase data "no longer required for the purpose", unless erasure is prohibited by law or retention is in the public interest.
  - Judgment: keeping the data for investigations and claims is a directly related purpose while those are live. That is why each review is recorded.
- R11 p.6, Step 5: "A comprehensive record of the incident is therefore required".
- R08 SPM TM-G-1 para 3.1.3 (p.11, non-statutory guideline): "establish secure processes for disposal and destruction of sensitive information".
- R07 SPM TM-G-2 para 4.7.2 (p.14): "Important conversations with external parties should be properly logged for future reference."
- Conditional: R16c s.7(1)(b) (p.31) makes it an offence to destroy material relevant to an investigation where a production order or warrant has been made or applied for. Missing fact: whether any such order exists.
- No direct rule located in assigned sources setting a retention period for incident evidence beyond the six-month log minimum. The review dates and release conditions are professional judgment.

## Search record and limits

- All documents, regex "retention period|retain(ed)? for|kept for|years|destroys|falsif|conceal": 97 hits; relevant ones at R02 p.20, R03 p.18, R16c p.31.
- R10, regex "erase|erasure|no longer required|longer than is necessary": 17 hits; relevant ones at pp.58, 167.
- R01, regex "destr|dispos|falsif|alter": 7 hits, none creating a preservation duty.
- Not in the manifest: limitation legislation, the bank's retention schedule, the Monetary Authority's material-change form and the assessment matrix that R03 cites.

## Simulated actions for the facilitator to log

1. By 10:00 — LC confirms the legal hold in writing to all custodians, the vendor and the forensic firm.
2. By 12:00 — LC and SEC establish the evidenced Annex E filing time.
3. By 12:00 — LC issues the register in two versions and holds the handover meeting.
4. Today — the disclosure officer and SEC close the wallet-address check.
5. Today — LC obtains the Police reference and sends the HKMA update with the confirmations.
6. 20 November — inventory of held records; first Annex F draft.
7. 27 November — Annex F submitted; statutory limit 30 November 2026.
8. 16 December — material-change notice filed, if SEC's assessment finds a material change.
9. 18 December — first hold review.