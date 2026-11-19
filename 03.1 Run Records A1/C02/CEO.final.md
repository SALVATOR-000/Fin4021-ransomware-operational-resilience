## CEO final decisions, C02 (Monday 16 November 2026, 09:30 HKT, H+1:30)

All six units are CONFIRMED; there are no overrides. I re-read the citations in the three sealed answers against the source pages and found them accurate. PH01 is not in the manifest ("PH01", all documents: 0 hits), so the internal basis is N/A throughout.

All actions below are simulated, for the facilitator to log.

### My own decisions that the sealed answers asked for

- **Payment:** I adopt "do not pay" as the operating posture now. I will not authorise a payment and agree I cannot do so alone. I call the Board chair now; the Board or its delegated committee confirms by 12:00.
- **Attacker contact:** none. I am the only authoriser of any later contact, in writing, on a joint LC and SEC recommendation.
- **Police report and precautionary disclosure:** authorised, by 10:30, as LC proposes.
- **Reporter reply:** I approve the text. I confirm in writing that I have authorised no payment. I confirm that none has been made once the finance head confirms nothing has left the bank; without that by 09:50, Reply B goes.
- **Frontline ransom line (item 4):** approved.
- **Funds wording:** Line B for staff, and no funds sentence to the reporter (see conflict 1).
- **Privacy decision point, 10:30:** on SEC's result memo I decide, with LC, SEC, COM and the privacy officer, the notifications and whether to acknowledge the data claim publicly. It moves forward at once if the attacker publishes or SEC reports a match.

### Conflicts between sealed answers, resolved within their stated branches

1. **Funds wording.** COM's Line A and the reporter's funds sentence need written confirmation from Operations and SEC. SEC's sealed 09:30 status says it "has not verified ledger integrity" and the reconciliation check has no time yet. The condition is not met, so COM's stated default applies. I ask core banking operations to give SEC and COM a time for that check.
2. **"Working with the relevant authorities".** LC says nothing is to be said about reports to law enforcement, and the facilitator's handoff records no outcome for the C01 regulator calls. The phrase stays only if LC confirms at 09:50 that notifications were actually made, as COM wrote. It names no agency.
3. **Route for attacker messages.** LC says pass to SEC; COM says manager to incident desk. The incident desk hands every such message to SEC for preservation. Nobody replies.
4. **LC's clearance queue.** Order: payment hold 09:35; no-contact instruction 09:40; SEC's vendor notice and COM's staff instruction by 09:45; reporter reply by 09:50; then the Commissioner filing and HKMA update; Police report by 10:30. LC may use a named delegate for clearances.
5. **Written record to the Commissioner (carried from C01).** No card records the outcome of the C01 telephone notification. Filing R02 Annex E now through the secure channel works either way: it is the written record if the call was logged, and the notification itself if not. Both fall inside the 20:00 limit. SEC first confirms the terminal is released under the C01 evidence hold.

---

### Q04a

- **Original answer reference:** SEC sealed answer, C02, Q04a.
- **CONFIRM.**
- **Reason:** Validation uses only data the bank already holds, so nothing more is exposed and no attacker contact is needed, which fits LC's Q05b. The two-person cell and a memo without personal data keep the rows away from everyone else. The limits are stated honestly: a match does not prove volume, and no match does not disprove copying.
- **Final action and condition:** As written.
  - Intake control: original preserved, hashed, registered; other copies recalled.
  - File opened only on an isolated workstation.
  - Two-person cell runs read-only logged comparisons against bank records and file layouts.
  - Corroboration from C01 evidence in parallel.
  - Status to everyone is "claim unverified" until a result issues.
  - Stop and escalation triggers as written.
- **Accountable owner:** SEC. Executing: the validation cell (one SEC forensic analyst, one delegate of the customer-data owner).
- **HKT time or trigger:** 09:30 intake; 09:50 status line to COM and LC; 10:30 preliminary result; 12:00 corroboration update. Any match is reported within 15 minutes. The attacker's 02:00 deadline is not a validation deadline.
- **Recipient and channel:** Result memo to me, LC and the privacy officer by out-of-band bridge and the restricted incident workspace. COM receives the status line only.
- **Final external basis:** SEC Q04a "Basis", unchanged. Anchors re-read:
  - R10 Cap. 486, Schedule 1, Principle 4(1), p.169: "protected against unauthorized or accidental access, processing, erasure, loss or use".
  - R11, p.4, Step 1: "promptly gather all relevant information of the data breach".
  - R16b, p.2: "ascertaining the nature of the incidents, the causes of the incidents and identity of customers affected".
  - R16b Annex C(i), p.4: "granted on a need-to-have basis only".
  - The validation method is professional judgment; SEC's "No direct rule located" search record stands.
- **Final internal basis:** N/A (PH01 absent).
- **Dispatch instruction:** EXECUTE NOW. No dependency on other roles; the result feeds my 10:30 decision point.

### Q04b

- **Original answer reference:** SEC sealed answer, C02, Q04b.
- **CONFIRM.**
- **Reason:** The vendor's account is a possible route and the vendor may bear liability. Its records must be frozen now, received with integrity controls and reconciled against the bank's own logs. Keeping its access suspended stops it changing the gateway while "helping".
- **Final action and condition:** As written.
  - Written preservation and production request covering SEC's items 1-6, 90-day look-back, the 14 days before 08:00 on 16 November first.
  - Wording cleared by LC; sent to the contract contact; confirmed by call-back to a number already on file.
  - Native exports with a SHA-256 manifest and signed custody form.
  - Received by bank-hosted encrypted transfer, or bank-issued encrypted media collected by the evidence custodian.
  - Quarantine, malware scan, hash check, register entry, then reconciliation.
  - The vendor is asked not to contact the attacker or media.
- **Accountable owner:** SEC. Executing: vendor relationship owner (sends), evidence custodian (receives), forensic staff (verify), LC (contract rights and wording).
- **HKT time or trigger:** Request 09:45; vendor's written preservation confirmation 10:30; gateway session records 12:00; remaining items 18:00. No confirmation by 10:30, a refusal or signs of deletion: LC serves formal contractual notice and I am told.
- **Recipient and channel:** The vendor's contract contact, by written notice and call-back. Material comes into the bank's evidence intake. Never ordinary email or the suspended remote access path.
- **Final external basis:** SEC Q04b "Basis", unchanged. Anchors re-read:
  - R12 SA-2 para 2.1.1, p.4: "AIs should therefore continue to retain ultimate control of the outsourced activity."
  - R12 para 2.8.1, p.8: "data retrieved from the service providers are accurate and available in Hong Kong on a timely basis".
  - R16b Annex I, p.8.
  - R02 s.7.2.3(a)(v)(2), p.32.
  - Missing facts: the contract, whether the arrangement is "outsourcing", whether the vendor held customer data. Log types, look-back and format are professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW. Dependency: LC wording clearance by 09:45.

### Q05a

- **Original answer reference:** LC sealed answer, C02, Q05a.
- **CONFIRM.**
- **Reason:** Paying does not secure decryption, cannot retrieve copied data and discharges no duty. With the recipient unidentified it risks two criminal offences. No assigned source permits or prohibits payment in terms, so this is judgment bounded by statute.
- **Final action and condition:** As written.
  - No payment is authorised.
  - Hold on any preparatory step: virtual-asset account, buying BTC, payment intermediary.
  - Each of LC's checks 1-5 blocks payment while unresolved.
  - Any departure is for the Board only, and only with checks 1-3 cleared in writing.
  - Review triggers as written.
- **Accountable owner:** LC for the advice and legal checks. The Board for any departure. The bank's disclosure officer for the Cap. 455 disclosure. SEC for attribution.
- **HKT time or trigger:** 09:35 advice and hold; by 10:30 Police report and precautionary disclosure; by 12:00 Board confirmation; 18:00 and 23:00 reviews, or earlier on a trigger. The attacker's 02:00 deadline on 17 November is not a legal deadline.
- **Recipient and channel:** Advice to me and the Board chair by telephone bridge and written note, on a channel SEC confirms is uncompromised. Hold to Treasury and Finance. Disclosure to an authorised officer; the filing channel is not in the sources.
- **Final external basis:** LC Q05a "Basis", unchanged. Anchors re-read:
  - R16c Cap. 455 s.25(1), p.82: "he deals with that property".
  - R16c s.25A(2)(a), p.83: "that disclosure is made before he does that act and he does that act with the consent of an authorized officer".
  - R16d Cap. 575 s.8(a), p.20: "being reckless as to whether, the person is a terrorist or terrorist associate".
  - R06 OR-2 para 3.4, p.6: "The Board bears ultimate responsibility".
  - No direct rule located on ransom payment (my re-run search is below).
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the advice and hold. HOLD on any payment or preparatory step. SCHEDULE the 10:30 report and disclosure, the 12:00 Board confirmation and the two reviews.

### Q05b

- **Original answer reference:** LC sealed answer, C02, Q05b.
- **CONFIRM.**
- **Reason:** Nothing the bank needs at this card requires contact; SEC validates without it. A reply could cut across a Police investigation or reveal a disclosure. Receive-only keeps the evidence and keeps options open.
- **Final action and condition:** As written.
  - No reply, acknowledgement, negotiation or request for more samples or time.
  - SEC preserves every inbound message.
  - The perimeter covers all staff, branches, the contact centre, COM and the vendor.
  - Later contact needs all four of LC's conditions.
  - Authoriser: me, in writing, Board chair informed.
  - Conductor: one designated specialist on a segregated channel with a full transcript.
  - Payment terms stay with the Board.
- **Accountable owner:** LC. Authoriser of any contact: Chief Executive. SEC and COM carry the instruction to the vendor and to staff.
- **HKT time or trigger:** Effective 09:30; issued by 09:40; reviewed at 12:00 after Police consultation and SEC's validation, and no later than 23:00.
- **Recipient and channel:** Me and the crisis management team, then staff (COM's instruction, item 7) and the vendor (SEC's request).
- **Final external basis:** LC Q05b "Basis", unchanged.
  - No direct rule located in assigned sources on contact with an attacker.
  - R07 TM-G-2 para 4.2.1, p.9: "AIs should establish a CMT to respond to and manage the various stages of a crisis."
  - R16c s.25A(5), p.84: "likely to prejudice any investigation".
  - Who authorises and who conducts is professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** EXECUTE NOW for the instruction. NO ACTION towards the attacker.

### Q06a

- **Original answer reference:** COM sealed answer, C02, Unit Q06a.
- **CONFIRM.**
- **Reason:** Branches are already taking calls about missing funds and need exact lines now. The instruction keeps staff to verified facts and withholds the demand and screenshot. It routes attacker, media and police contacts away from the frontline and tightens identity checks against impersonation.
- **Final action and condition:** As written.
  - Frontline Instruction No. 2 replaces the 08:15 script.
  - Funds: Line B, the stated default.
  - Compensation Line A stands from C01.
  - If SEC cannot confirm internal email and intranet are trusted, managers brief by phone and use printed cards.
  - Instruction No. 3 follows when a line changes.
- **Accountable owner:** COM. Executing: branch network head and the eight branch managers, contact-centre head, SME banking head, social media team, switchboard. Clearance: LC. Fact check: SEC and Operations.
- **HKT time or trigger:** 09:35 fact requests; 09:40 briefing call; 09:45 written instruction; 10:00 managers confirm staff briefed; 10:15 and every 30 minutes, enquiry totals to COM and on to LC.
- **Recipient and channel:** Branch and contact-centre staff, by briefing call, intranet knowledge base, internal email and printed desk card. Fallback: phone call-out and SMS to managers.
- **Final external basis:** COM Q06a "Basis", unchanged. Anchors re-read:
  - R05, PDF p.3, "Handling of customers' and media's enquiry" (checked against the scan): "consistent and up-to-date messages are conveyed to all relevant parties on a timely basis".
  - R07 para 4.7.2, p.14: "The BCP should clearly indicate who can speak to the media".
  - R09 para 4.4.2, p.17.
  - Script content is professional judgment; COM's search record stands.
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE for 09:40 and 09:45. Dependencies: LC clearance, the 09:40 no-contact instruction, SEC's channel confirmation.

### Q06b

- **Original answer reference:** COM sealed answer, C02, Unit Q06b.
- **CONFIRM.**
- **Reason:** Silence would be reported as the bank refusing to say whether it paid, which feeds the fears reaching branches. A present-tense statement of fact answers the question without confirming a demand or committing a future posture. Referring to "the incident we announced this morning" fits the public status: the statement is out, but its wording branch and channel cannot be verified.
- **Final action and condition:** As written.
  - Written reply by email, attributed to a spokesperson; no interview.
  - Reply A if all three conditions are met by 09:50; otherwise Reply B.
  - The funds sentence is left out.
  - The "relevant authorities" phrase depends on LC's 09:50 confirmation.
  - The bank never denies a demand.
  - A copy goes to the HKMA through LC at or just before sending.
  - The same line goes to any other outlet.
- **Accountable owner:** COM. Approver: me. Clearance and HKMA copy: LC.
- **HKT time or trigger:** 09:35 confirmation requests; 09:50 cut-off; 09:55 reply sent; 10:00 public update with the same lines.
- **Recipient and channel:** The reporter, by email from the Corporate Communications mailbox. HKMA copy via LC's supervisory contact. Logged as a reply to a press enquiry.
- **Final external basis:** COM Q06b "Basis", unchanged. Anchors re-read:
  - R05, PDF p.3: "copies of public communication materials should be submitted to the HKMA for reference".
  - R05, PDF p.2, "Public announcement", 4th paragraph: "may prejudice any ongoing criminal proceedings or any investigation".
  - R16c s.25A(5), p.84.
  - No direct rule located on confirming or denying a ransom to the media; that is professional judgment.
- **Final internal basis:** N/A.
- **Dispatch instruction:** SCHEDULE for 09:55. Dependencies: LC's 09:35 hold, the finance head's confirmation, my written confirmation, LC's 09:50 clearance.

---

### Order of dependent actions on this card

1. **09:30:** SEC puts the attacker's message and screenshot under intake control. No-contact takes effect.
2. **09:35:** LC issues the advice and payment hold to Treasury and Finance. I adopt the posture and call the Board chair. COM sends its fact requests.
3. **09:40:** The no-contact instruction is issued. COM briefs branch managers and team leaders.
4. **09:45:** SEC's LC-cleared request goes to the vendor with call-back. COM issues Frontline Instruction No. 2 with Line B. I give COM my payment confirmation once the finance head has confirmed.
5. **09:50:** SEC's status line reaches COM and LC. LC confirms notification status and clears the reply. COM selects Reply A or B.
6. **09:55:** COM replies to the reporter. LC copies the HKMA.
7. **By 10:00:** LC files Annex E through the secure channel after SEC's terminal check, and updates the HKMA on the demand, the unverified data claim and the no-payment posture. COM issues the public update.
8. **10:15:** First enquiry totals to COM and LC.
9. **10:30:** SEC's result memo; vendor's preservation confirmation due; Police report and disclosure made; my privacy decision point.
10. **12:00:** Board confirms the posture; vendor session records due; SEC corroboration update; contact review.
11. **18:00 and 23:00:** Posture reviews. The attacker's 02:00 deadline drives nothing.

### New basis for my 10:30 privacy decision point (no unit changed)

- R16b, HKMA circular "Customer Data Protection", PDF p.2, "Controls for handling incidents involving loss or leakage of customer data": "a designated management committee, which is chaired by senior management, for overseeing the process of handling and reporting privacy incidents". Authority: HKMA supervisory circular to all authorized institutions.
- R16b, PDF p.3, first paragraph: "report the incident to the HKMA and notify the affected customers as soon as practicable after the AI concerned is aware of or notified of the incident". This applies where the incident is serious; whether it is depends on SEC's result.
- R11, PDF p.8, "When to notify?": "as soon as practicable after becoming aware of the incident, regardless of the progress of any internal investigation". Non-binding guidance. It is why the decision is taken at 10:30 on whatever result class SEC reports, not deferred until corroboration is complete.

### Still unverified at this card

Whether the screenshot rows are bank data; whether data was copied and how much; whether the vendor account was the route; whether the ledger is intact; the outcome of the C01 regulator calls; which holding-statement wording and channel were used.

### My search record

- "ransom", all documents: 9 hits (R02 pp.35, 42, 43; R04 p.8; R11 p.2; R14b p.5; R16a p.4); none on payment or public comment.
- Regex "threat actor|attacker|negotiat|extortion|blackmail", all documents: 10 hits (R02 pp.22, 25, 36, 44; R03 p.20; R04 p.5; R12 p.5; R14b pp.5, 7; R16c p.101); none on paying or contacting an attacker.
- Limitation: the vendor contract, the bank's emergency response plan, its insurance policy, the Theft Ordinance and sanctions legislation are not in the manifest.