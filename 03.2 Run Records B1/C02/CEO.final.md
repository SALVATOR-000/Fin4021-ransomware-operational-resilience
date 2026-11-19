CEO FINAL DECISION RECORD: C02 (Mon 16 Nov 2026, 09:30 HKT, H+1:30). Lan Tidal Bank, CMT chair.

All actions are simulated, for the facilitator to log. I received sealed answers for all six units. The only facilitator handoff was COM's, on C01 Q03b. Before relying on the key citations I checked them myself:
- R16c s.25A(1), (2)(a) and (5), pp.83–84.
- R16d s.8, p.20.
- R10 DPP4(1), p.169.
- R11 pp.4–5 and p.8.
- R16b pp.2–3.
- R03 6.2.13(b), p.14.
- R09 4.4.2, p.17, and 8.2.2–8.2.3, p.33.
- R07 4.7.3, p.14.
- R05 pp.2–3 against the scan.
- PH01 v1.0 in full.

CEO RECORD ENTRIES, 09:30
1. **Severity 1 reconfirmed** under PH01 v1.0 s.4.1, which covers the case where "an extortion demand is received". Customer data exposure is also suspected.
2. **C01 Q03b (09:00 holding statement): not evidenced.** Per the facilitator, release cannot be verified because LC's clearance was never recorded. I was the approver. I log it as an open item, not done (PH01 s.10.3: "Approval and scheduling are not delivery"; s.18.2). The fix is in Q06b below. LC tells the HKMA in its 10:00 update.
3. **Board chair.** I phone the Board chair by 10:00 and report the Severity 1 declaration and the extortion demand. PH01 s.15.1 sets the limit as within 2 hours of the demand, so no later than 11:30. LC's posture note goes with the call.

==================================================================
**UNIT C02-Q04a: validate the sample while limiting further exposure**

- **Original answer reference:** sealed SEC answer for C02, "UNIT Q04a", V1–V7 and the stop triggers.
- **Decision:** CONFIRM.

**Reason**
- **Exposure controls:**
  - Attacker material goes only into the evidence process (PH01 s.6.6).
  - The screenshot is viewed only in the bank's lab (s.16.2).
  - A named need-to-know cell runs the work, with the DPO consulted.
  - Lookups are exact-match only and return match or no-match, not full records.

  Together these are proportionate "practicable steps" under DPP4(1). V3 is the "ascertaining ... identity of customers affected" step in R16b p.2.
- **Reporting is not held:** the 11:00 preliminary result feeds LC without holding any report (PH01 s.2.4; R11 p.8, "regardless of the progress of any internal investigation").
- **Limits on conclusions:** a match is not a volume estimate, and a non-match does not mean no breach. This matches PH01 s.10.4(c).
- **No cross-role conflict:** no COM line asserts anything about data.

**Final action and condition:** V1–V7 and the stop triggers, exactly as written.

**Accountable owner:** SEC. Executed by the SEC analyst, the data-owner query operator and the custodian (witness). The DPO is consulted. Notification decisions stay with the CMT chair and COM (PH01 s.3, s.10).

**HKT time, deadline or trigger:**

| Step | Time |
|---|---|
| Intake | 09:30 |
| Cell named | 09:45 |
| Preliminary masked result | by 11:00 |
| Claim-versus-logs check | by 13:30 |
| Status reports | hourly after that |
| Widen containment | at once if rows trace to a store outside the isolated segment |

**Recipient and channel:**
- Originals: evidence store and register.
- Masked summary: LC, the DPO and the CMT chair, in the CMT room or by phone, plus a decision-log entry.
- Matched names: DPO only, on paper or through the evidence store. Never by email.

**Final external basis:** SEC Q04a, "BASIS: EXTERNAL" items 1–5, adopted. I verified:
- R10 Sch.1 DPP4(1), p.169: "All practicable steps shall be taken to ensure that any personal data ... held by a data user is protected against unauthorized or accidental access".
- R11 p.4, Step 1.
- R11 p.8.
- R16b p.2.

SEC's "no direct rule located" search record for the validation method is adopted unchanged.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.6.6, s.16.2, s.10.4(a) and (c), s.6.3, s.12.3, s.17.2, s.2.4 and s.15.1, as listed in SEC Q04a. No conflict.

**Dispatch instruction:**
- EXECUTE NOW: V1 and V2.
- SCHEDULE: V4 (11:00) and V5 (13:30).
- V4 is a trigger for LC, COM and the chair (see the sequence at the end).

==================================================================
**UNIT C02-Q04b: evidence from the vendor and how it is received**

- **Original answer reference:** sealed SEC answer for C02, "UNIT Q04b", W1–W6.
- **Decision:** CONFIRM.

**Reason**
- **Credential:** the vendor account is treated as a suspected compromised credential (PH01 s.7.3–7.4). Passwords are changed under R03 6.2.13(b) (verified p.14: "all passwords are promptly changed if they have been or are suspected of being compromised").
- **Request scope:** it meets PH01 s.6.7(a). It adds a data inventory and transfer records, which are needed to test the "copied files" claim. The request carries no customer data or attacker material (PH01 s.3, data-sharing row).
- **Receipt and reconciliation:**
  - Receipt is by native export with a SHA-256 manifest, through a bank-hosted transfer or on bank-issued media. It is never by ordinary email or over the vendor's own remote access path (s.6.7(b)).
  - Receipt is confirmed by call-back to a number on file.
  - Vendor records count only as the vendor's account until SEC reconciles them (s.6.7(d)).
- **Escalation:** escalation by 12:00 uses the earlier reading of s.6.7(c), which is the prudent choice.
- **Legal hold:** LC's written legal hold to the vendor goes in the same packet (PH01 s.17.1). This matches my C01 direction to LC.
- **Late internal target:** the one-hour PH01 target (09:00) was missed because the vendor was identified only at 09:30. This is logged as late against an internal target; no external deadline is affected.

**Final action and condition:** W1–W6, exactly as written.

**Accountable owner:**
- SEC: content of the request.
- LC: clears the wording and issues the legal hold.
- Vendor relationship owner: sends the request and does the call-back.
- Evidence custodian: receives the material.
- LC and the CMT chair: escalation.
- Reinstating vendor access: the CMT chair, on SEC's written sign-off (PH01 s.7.5).

**HKT time, deadline or trigger:**

| Step | Time |
|---|---|
| W1 credential actions | 09:30, immediately |
| Draft | by 10:00 |
| Cleared and sent | 10:15–10:30 |
| Vendor confirmation | 11:30 |
| Escalation | 12:00 at the latest |
| First production | 14:00 |
| Remaining production | 18:00 |

**Recipient and channel:**
- To: the vendor's contract contact in the CRO's third-party register.
- Outbound: hand delivery, courier or the bank-hosted encrypted portal. Corporate email only if SEC has logged it safe.
- Inbound: as described in W4.

**Final external basis:** SEC Q04b, "BASIS: EXTERNAL" items 1–7, adopted:
- R02 7.2.3(a)(v)(2), p.32.
- R01 Sch.3 Pt 1 item 3, pp.91–92.
- R03 6.2.13(b), p.14 (verified).
- R16b Annex C(vii), p.5.
- R11 p.5, Step 2 (verified: "Removing the access rights of users suspected to have committed or contributed to the data breach").
- Conditional: R10 DPP4(2) and R12 SA-2.

SEC's "no direct rule located" search record on the delivery mechanics is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.6.7(a)–(d), s.7.2–7.5, s.17.1 and s.3. No conflict.

**Dispatch instruction:**
- EXECUTE NOW: W1.
- SCHEDULE: W2 by 10:00, then W3 at 10:15–10:30. W3 depends on LC clearing the wording.
- W6 fires at 12:00 if the vendor has not confirmed.

==================================================================
**UNIT C02-Q05a: payment posture and constraining checks**

- **Original answer reference:** sealed LC answer for C02, "UNIT Q05a".
- **Decision:** CONFIRM.

**Reason**
- **Posture:** LC recommends no payment, no preparatory step and no negotiation. This applies the Board's policy in PH01 s.12.1 ("the bank does not pay a ransom. Any departure is for the Board alone").
- **Treasury hold:** applies s.12.2.
- **Police report:** LC's decision under s.3.
- **Statutory gap closed:** LC found a gap where PH01 is weaker than the statute. Cap. 455 s.25A(1) (verified p.83) requires disclosure "as soon as it is reasonable for him to do so". LC therefore makes a conditional disclosure now if the demand identifies where payment should go, instead of waiting for a payment proposal. That is the external-consistent action.
- **Cap. 575:** the s.8 risk (verified p.20: "being reckless as to whether ... the person is a terrorist or terrorist associate") is correctly treated as a gate.
- **Deadline and timing:** LC treats the 02:00 attacker deadline as non-governing, and its reviews at 14:00, 20:00 and 22:00 all fall before 02:00.
- **No Board meeting:** no departure is proposed, so none is needed (PH01 s.15.2).
- **Board chair notice:** my 10:00 call falls inside LC's stated "by 11:30 HKT, or earlier", so this is a CONFIRM.

**Final action and condition:** items 1–7 and gates (a)–(g), exactly as written. As CMT chair I adopt the no-payment posture for day-to-day operation.

**Accountable owner:**
- Board: the policy and any departure from it.
- CEO (CMT chair): the posture day to day.
- LC (accountable for the recommendation): the gates, the Police report and any disclosure.
- CFO and Treasury: the hold and the insurer notice.

**HKT time, deadline or trigger:**

| Step | Time |
|---|---|
| Treasury hold | 09:45 |
| Police CSTCB report, plus Cap. 455 disclosure if a wallet is identified | 10:30 |
| Board chair notice | 10:00 (limit 11:30) |
| Insurer | 12:00 |
| Posture reviews | 14:00 and 20:00, and at once on any listed trigger |
| Written posture note to the chair | 22:00 |

**Recipient and channel:**
- Treasury: written instruction through the CFO, by hand or by phone with call-back.
- Police CSTCB: phone (RCR), then a formal report.
- Decision log.
- Board chair: phone call from me.

**Final external basis:** LC Q05a, "Basis: external law and guidance", adopted:
- R16c s.25A(1) and (2)(a), p.83 (verified).
- R16c s.25(1) and s.2.
- R16d ss.8, 12 and 14 (s.8 verified).
- R04 para 2.4, fn 1.
- R11 p.4, Step 2 (verified: "Notifying the relevant law enforcement agencies").

LC's "no direct rule located" records on sanctions, the HKMA's stance on paying ransoms, and virtual assets are adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0: s.12.1, s.12.2, s.12.4, s.15.1 and s.3 (payment and Police rows). Conflict identified by LC: s.12.2 treats disclosure only as a pre-payment gate. It is resolved in favour of Cap. 455 s.25A(1), as above.

**Dispatch instruction:**
- EXECUTE NOW: the Treasury hold.
- SCHEDULE: the Police report at 10:30, the insurer at 12:00, and the reviews.
- The Cap. 455 disclosure is conditional on a payment destination being identified.
- HOLD every payment step until the Board decides. No departure is proposed.

==================================================================
**UNIT C02-Q05b: contact with the attacker**

- **Original answer reference:** sealed LC answer for C02, "UNIT Q05b".
- **Decision:** CONFIRM.

**Reason**
- **Preconditions not met:** PH01 s.12.3 requires that the Police have been consulted and that there is a stated limited purpose. Neither is met.
- **No purpose exists:**
  - s.6.6 forbids requesting samples.
  - SEC can validate the sample without contact.
  - The posture is not to pay.
- **Content limits for any later contact:** these follow Cap. 455 s.25A(5) (verified p.84: offence to disclose "any matter which is likely to prejudice any investigation"). They also bind COM's public text.
- **My decision as authoriser:** I authorise no contact.

**Final action and condition:**
- No contact.
- Standing instruction: no staff member, branch, COM officer or vendor replies to the attacker; everything goes to SEC.
- Any later contact needs all of the following:
  - a joint LC and SEC recommendation;
  - the Police consulted first;
  - a stated limited purpose;
  - my written authority.

  Contact is then made by one designated specialist on a segregated channel, with a full transcript, using LC-cleared scripts.

**Accountable owner:**
- Authorises: the CEO (CMT chair) only.
- Recommends: LC and SEC jointly.
- Carries out the standing instruction: SEC, with COM's staff script.

**HKT time, deadline or trigger:**
- Decision logged at 09:45.
- Reviewed on the Police view (target 12:00), at 14:00 and at 20:00.

**Recipient and channel:**
- Decision log.
- Staff: through the COM Q06a script.
- Vendor: through the vendor relationship owner.

**Final external basis:**
- LC Q05b basis adopted: R16c s.25A(5), p.84 (verified), and R16d s.12(5), p.37.
- R05 p.2 by analogy.
- LC's "no direct rule located" search record is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.12.3: "None, unless the CMT chair authorises it in writing on a joint LC and SEC recommendation, for a stated limited purpose, after consulting the Police."
- s.6.6.

No conflict.

**Dispatch instruction:** NO ACTION toward the attacker. EXECUTE NOW the standing instruction to staff, through Q06a.

==================================================================
**UNIT C02-Q06a: branch and contact-centre staff instructions**

- **Original answer reference:** sealed COM answer for C02, "Q06 a".
- **Decision:** OVERRIDE (four changes; everything else kept).

**Reason**
COM's two-step structure is kept: an interim instruction at 09:35, script v2 at 09:55, receipts by 10:15. So are its lines that avoid "your money is safe" and its no-reply-to-attacker line. I change four things:
1. **LC clears before issue.** COM issued the interim instruction before LC clearance and had LC confirm afterwards. PH01 s.3 requires that "LC clears" staff scripts, and LC is in the CMT room, so clearance comes first.
2. **Caller authentication added.** SEC's handoff warned that callers could be using social engineering. Script v2 tells staff to "check your balance and recent transactions now" without saying the caller must first be authenticated. DPP4(1) requires protection against "unauthorized ... access".
3. **Lines aligned with my Q06b decision.** The ransom, demand and data lines now follow the final Q06b text (the fallback branch, decided below).
4. **Reissue triggers and staffing made explicit.** COM only recommended extra staff; I decide it.

**Final action and condition**
1. **Interim instruction.** It contains COM's procedural lines and nothing new, and is issued once LC's oral clearance is logged.
   - Clearance by 09:35, latest 09:40. If LC has not cleared by 09:40, only the lines that restate PH01 fixed positions go out: s.11.1 (media referrals), s.12.3 (pass to SEC), s.13.1 (fee waiver), plus "open a case". The rest is held.
   - Branch managers and the contact-centre supervisor confirm receipt by 09:45.
2. **Script v2.** COM's text, with these changes:
   - **(a) New first rule.** "Before discussing any balance, transaction or personal detail, authenticate the caller by the standard procedure. If you cannot, give only the public lines and ask them to use the app, visit a branch, or call back on the number on their card. Never confirm account details to an unverified caller." The line "Let's check your balance and recent transactions now" is used only after authentication.
   - **(b) Ransom or demand questions.** Staff use only the Q06b final lines: "This is a criminal matter; we are working with the relevant authorities and cannot comment on further details." Add "The bank has not paid a ransom" only if P1 is logged. Staff never deny a demand and never mention the amount, the deadline, the attacker, the vendor, the system or the bank's designation.
   - **(c) Data questions.** COM's line is kept: "We are investigating, including whether any customer information is affected. Nothing has been confirmed..."
   - **(d) Funds.** The conditional line "Our checks so far have found no unexplained movement of customer funds" is used only when the Head of Payments Operations logs it from the reconciliation record.
   - **(e) Reissue at once** on any of:
     - SEC's 11:00 validation result;
     - the Payments Operations reconciliation;
     - the Police view;
     - any new attacker message or publication of data;
     - any change in service status;
     - each public update (next by 13:00).
3. **Staffing (CEO decision).**
   - Operations adds contact-centre agents from 10:00.
   - Branches extend opening hours today. The branch network head sets the closing time by 12:00, and it is announced in the 13:00 update.

**Accountable owner:**
- COM approves the script; LC clears it (PH01 s.3).
- SEC and the Head of Payments Operations fact-check.
- Branch managers and the contact-centre supervisor execute.
- Staffing: Operations.

**HKT time, deadline or trigger:**

| Step | Time |
|---|---|
| LC clears the interim instruction | 09:35 (latest 09:40) |
| Interim receipts | 09:45 |
| LC clears script v2 and the fact-check is done | 09:50 (COM's defaults kept: v2 held / unconfirmed line deleted) |
| Script v2 broadcast | 09:55 |
| Branch huddles | 10:05 |
| Receipts logged | 10:15 |
| Reissue | on the triggers in (e) |

**Recipient and channel:**
- To: all branch staff, contact-centre agents, relationship managers and the SME payroll call team. The IVR is updated to match.
- How: staff mobile broadcast and phone cascade. Corporate email only if SEC has logged it safe.

**Final external basis:**
- COM Q06a, "Basis: external", adopted:
  - R05 p.3 (scan-checked).
  - R09 8.2.2, p.33.
  - R09 4.4.2, p.17 (verified: "available at all times for customers to seek and obtain help with respect to possible unauthorized transactions").
  - R09 4.4.3, p.18.
  - R07 4.7.3, p.14 (verified: "broadcasting of messages to mobile phones of staff").
- New basis for the authentication rule:
  - R10 Sch.1 DPP4(1), p.169 (verified): personal data must be "protected against unauthorized or accidental access, processing, erasure, loss or use".
  - R16b p.2, fn 4 (verified): AIs "are not supposed to disclose customer data to the related parties of the customers concerned without the consent from the customers".
  - Search record: "call cent" across all files found R07 p.12, R12 p.2 and R16b p.7, none on point. "social engineering" found R02 pp.42–43 (form check-boxes only). No direct rule located in assigned sources sets a caller-authentication procedure during an incident.
  - Professional judgment: attackers who claim data theft often follow up with impersonation calls.
- New basis for extended hours: R05 p.3 (scan-checked): "deploy swiftly adequate resources and communication channels (e.g. customer service hotlines and extended office hours of branch services)".

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.3 ("Approve staff and frontline scripts | COM | LC clears").
- s.11.1, s.11.3, s.11.4, s.12.3, s.13.1, s.13.3, s.13.4, s.10.5 and s.8.6.

No conflict.

**Dispatch instruction:**
- EXECUTE NOW: the interim instruction, once LC's oral clearance is logged.
- SCHEDULE: script v2 at 09:55. It depends on LC clearance and the fact-check at 09:50, and on the Q06b final lines.
- The conditional funds line stays held until Payments Operations logs it.

==================================================================
**UNIT C02-Q06b: reply to the reporter before 10:00**

- **Original answer reference:** sealed COM answer for C02, "Q06 b", P1–P5 with main and fallback wording; read with the facilitator's COM handoff on C01 Q03b.
- **Decision:** OVERRIDE.

**Reason**
The facilitator's handoff says the 09:00 holding statement may never have been released. R09 8.2.3 (verified p.33) expects a press release "shortly after the commencement of any disruption". Under COM's P1 default ("No substantive reply ... a statement will follow by 10:30") the bank's first public statement could slip even further for a ransom-line check. I change four things:
1. **Service content decoupled.** The service content goes out by 10:00 whatever happens to P1–P5. Only the conditional lines depend on them.
2. **P2 and P4 decided (they were left to me).** Use the fallback stance on the demand until the Police have been consulted. The LC report is due at 10:30, so no Police view exists before 10:00. This applies R05 p.2's weighing of whether an announcement "may prejudice any ongoing criminal proceedings or any investigation". The attacker's data claim is not mentioned proactively. Instead the update keeps C01's "what we are checking" line, which PH01 s.11.2 requires in each update.
3. **Funds rumour addressed.** A "what you can do" step is added: check your balance and report anything unusual. R05 p.2 requires "the steps that affected customers need to take ... to protect their interests".
4. **P1 default narrowed.** Only the ransom line drops out, and the reporter is told that answer will follow by 10:30.

**Final action and condition**
1. **09:30–09:35.**
   - COM logs whether the C01 statement is live.
   - COM confirms the reporter's identity through the outlet's published newsroom number and promises a statement by 10:00.
2. **Statement text, approved by me now.** Bilingual; LC clears it and SEC and Operations fact-check it by 09:50:

> "Lan Tidal Bank service update – 16 November 2026, 10:00 HKT. Since this morning, outgoing local transfers and payroll submissions have been disrupted following a cyber security incident affecting some of our systems. We are working to restore the service and are investigating. [P1: The bank has not paid a ransom.] This is a criminal matter; we are working with the relevant authorities and will not comment on further details at this stage. What is confirmed: outgoing local transfers and payroll submissions cannot currently be processed; customers can still view balances in our mobile app; our branches are open. What we are checking: when service will be restored; the status of transfers submitted before the disruption; and whether any customer information is affected – if it is, we will contact the customers concerned directly. What you can do: check your balance in our app or at a branch and tell us at once if anything looks unusual – we will open a case with a reference number; please do not resubmit a transfer or payroll already submitted; if a payment is urgent, contact your relationship manager, visit a branch or call the number on the back of your card. Fees caused by this disruption will be waived, and documented direct losses caused by the disruption, such as late-payment charges, will be reimbursed on claim through your relationship manager, a branch or our hotline, each with a case reference. We will never send you a link or ask for your password, one-time password or a payment; please ignore any message about this incident that does. Next update: by 13:00 HKT today, or sooner if the situation changes."

3. **Conditions.** All carry the four PH01 s.2.3 items.

| ID | Condition | Verifier | Latest time | If not met |
|---|---|---|---|---|
| P1 | The ransom line goes in | CFO's written confirmation that no payment and no preparatory step has occurred, logged after LC's 09:45 Treasury hold | 09:50 | That line is omitted; the reporter is told the bank will answer that question by 10:30; the rest goes at 10:00 |
| P3 | "Reported to the Police" line | LC | — | Not used at 10:00; reconsidered for 13:00 once the report is logged and the Police raise no objection |
| P5 | No tipping-off | LC | 09:50 | Any flagged line is removed |
| Fact-check | Each factual line (the facts are unchanged from C01) | SEC and Operations | 09:50 | An unconfirmed line is deleted; the statement still goes |

4. **Reactive lines, never a denial.**
   - On the demand: the "criminal matter" line.
   - On the data claim: "We are investigating whether any customer information is affected; if we confirm it is, we will contact those customers directly."
   - Never: the amount, the deadline, the attacker, the vendor, the system or the bank's designation; any future intent; "funds are safe"; "no data was taken".
5. **10:00 release.**
   - The reporter gets the statement by phone and in writing.
   - It goes on the website status page.
   - If the C01 statement is not live, the 10:00 statement becomes the bank's first public statement and goes on every C01 Q03b channel: press release, official social media, branch notices and IVR. The app banner is used only if SEC has logged it trusted.
   - At release COM gives a copy to LC, and LC sends it to the HKMA.
   - COM logs the Annex F Part E entry.
6. **13:00 update.** I reconsider confirming the demand and the Police line once the Police view is in.

**Accountable owner:**
- Approves: the CEO (CMT chair), sole spokesperson; written statement only, no interview.
- Clears: LC. Fact-check: SEC and Operations.
- P1 verifier: CFO.
- Executes: the COM media desk.

**HKT time, deadline or trigger:** identity check and acknowledgement at 09:35; conditions by 09:50; release at 10:00 with no slippage for any condition; ransom-line fallback by 10:30; next update by 13:00, then under PH01 s.11.2.

**Recipient and channel:**
- Reporter: phone plus written text from the media desk. Corporate email only if SEC has logged it safe.
- Public: the channels in item 5.
- HKMA: copy via COM to LC to the HKMA by the HKMA-confirmed route.

**Final external basis:**
- COM Q06b basis adopted:
  - R05 pp.2–3 (scan-checked).
  - R09 8.2.2 and fn 25.
  - R16c s.25A(5), p.84 (verified).
  - R16d s.12(5).
  - R02 Annex F Part E, p.46.
  - R11 p.8 and R16b p.3, conditional (verified).
- New or corrected support:
  - R09 8.2.3, p.33 (verified): "an AI is expected to issue a press release ... shortly after the commencement of any disruption". This is why the service content cannot be held for any condition.
  - R05 p.2, "Public announcement", paragraphs 2–3 (scan-checked): "include the key facts of the incident and the steps that affected customers need to take ... to protect their interests", and "may prejudice any ongoing criminal proceedings or any investigation". These support the funds step and the fallback stance on the demand.
- COM's "no direct rule located" search record (ransom confirmation, press-reply timing) is adopted. Choosing the fallback until the Police view is professional judgment.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.11.3: "The bank never denies receipt of a demand. It states whether a payment has been made only as a verified present fact."
- s.11.2: "Each update states what is confirmed, what is being verified, what customers can do and when the next update is due."
- s.10.4(c), s.3 (public statements row), s.5.8, s.12.1–12.2, and s.1.4 (internal times never extend an external deadline).

No conflict.

**Dispatch instruction:**
- EXECUTE NOW: the status check and the reporter acknowledgement.
- SCHEDULE: release at 10:00. It is not held by P1–P5; those control only their own lines.
- The HKMA copy depends on the release.

==================================================================
**CROSS-ROLE CONFLICT RESOLUTION**
1. **COM P3 vs LC's Police timing.** COM's P3 check is due at 09:50, but LC's Police report is due at 10:30. The P3 default applies, and LC's timing is unchanged.
2. **COM P1 depends on LC's Treasury hold.** The 09:45 hold comes before the CFO confirmation due at 09:50.
3. **Caller authentication.** SEC's handoff point, that callers may be social engineering, is added to Q06a.
4. **Tipping-off.** LC's tipping-off rule (Cap. 455 s.25A(5)) binds COM through P5 and binds any attacker contact under Q05b.
5. **Unverified C01 statement.** The C01 Q03b statement is resolved by the decoupled 10:00 release.
6. **PH01 s.12.2 gap.** Resolved in favour of Cap. 455 s.25A(1).

**ORDER OF DEPENDENT ACTIONS (HKT)**
1. **09:30**
   - SEC registers the demand and screenshot as evidence (Q04a V1).
   - SEC contains the vendor credential (Q04b W1).
   - COM checks whether the statement is live.
   - CEO logs the 09:30 entries.
2. **09:35**
   - LC clears the interim instruction, then the phone cascade goes out (Q06a).
   - COM confirms the reporter's identity and acknowledges the enquiry.
   - COM requests P1, P3, P5 and the fact-check.
3. **09:45**
   - Treasury hold (Q05a).
   - SEC validation cell named (Q04a V2).
   - No-contact decision logged (Q05b).
4. **09:50**
   - CFO confirms P1 (needs step 3).
   - LC clears script v2 and the statement.
   - SEC and Operations fact-check.
5. **09:55**
   - Script v2 to staff (needs step 4).
6. **Before 10:00**
   - LC phones the HKMA: the demand, the unverified data claim, the posture, the media enquiry, and the possibly unreleased C01 statement (PH01 s.5.8 "at once"; not held by anything).
   - CEO phones the Board chair.
7. **10:00**
   - Statement and reply released (Q06b).
   - At release: copy COM to LC to the HKMA, and the Part E log entry.
8. **10:00–10:30**
   - SEC drafts the vendor request, LC clears it with the legal hold, and the relationship owner sends it and does the call-back (Q04b).
9. **10:30**
   - LC reports to the Police CSTCB.
   - Conditional Cap. 455 disclosure. Tipping-off controls apply from that point.
10. **By 11:00**
    - LC files Annex E on the now-available secure channel, with the demand and the data claim marked unverified.
    - SEC's preliminary validation (Q04a V4). If rows match, each of these follows at once:
      - an HKMA update (PH01 s.5.8; R16b p.3);
      - a DPO and LC decision on the PCPD;
      - notice to matched individuals as soon as practicable (PH01 s.10.4(a)), with COM sending and me approving the audience;
      - a public update and staff reissue;
      - a Board chair notice within 2 hours (s.15.1);
      - supplementary information to the Commissioner (s.5.9).
11. **11:30–12:00**
    - Vendor confirmation due; escalation at 12:00 if missing.
    - CFO notifies the insurer.
    - Police view (target) feeds the Q05a/b reviews.
    - CEO direction: Payments Operations reconciles the ledger against gateway activity by 12:00. This feeds the conditional funds line.
    - Branch closing time set.
12. **13:00**
    - Public update and staff reissue. Whether to confirm the demand and include the Police line is decided on the Police view.
    - 13:30: SEC's claim-versus-logs check.
13. **14:00**
    - Posture review.
    - Vendor production.
14. **18:00**
    - Remaining vendor production.
15. **20:00**
    - Posture review.
    - 50% of transfer tolerance: Board chair notice (C01).
16. **22:00**
    - LC's written posture note to me.
17. **02:00 Tue 17 Nov**
    - The attacker's deadline triggers no action.
18. **Ongoing**
    - Any departure from the no-payment posture goes to the Board only after LC confirms every PH01 s.12.2 gate in writing.

No files were created.