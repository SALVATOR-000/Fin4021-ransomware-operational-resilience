CEO final decision record for C02 (Mon 16 Nov 2026, 09:30 HKT, H+1:30). Five units are CONFIRM; Q06b is OVERRIDE (one sentence of the media reply changed). All actions are simulated, for the facilitator to log.

**How I checked.** I re-read these sources myself:
- PH01 v1.0, ss.2–18.
- R16c Cap. 455, PDF p.83, s.25A(1)–(2).
- R16d Cap. 575, PDF pp.20–21, ss.8 and 8A.
- R16b, PDF p.3.
- R05 PDF p.2, checked against the scan in C01.

All other citations are taken as they appear in the sealed answers.

**Handoff carried forward from Q03b.** The holding statement went out at about 09:00 on my approval. Two things are not verified:
- whether LC's clearance and the SEC and Operations fact-check were logged before release;
- whether the HKMA received its copy.

I direct LC to log after the event whether it cleared the text, and to get the HKMA receipt (PH01 s.5.5), both by 10:30. COM reconstructs which channels were used by 10:30, as COM itself proposed.

**Conflicts across the three roles.** One conflict needed a change: the scope of COM's "no payment" sentence in the media reply (Q06b). Everything else is consistent:
- SEC's evidence handling matches LC's no-contact rule.
- LC's clearance timings match COM's deadlines.

---
**Q04a | Original: SEC sealed answer, Q04a | CONFIRM**
- **Reason:**
  - The plan takes the attacker's material only into the evidence process, with no outside uploads and no requests for more samples (PH01 s.6.6).
  - Only named people see the unmasked rows, and they work offline. This limits further exposure and meets the DPP4 duty to protect personal data (R10 Sch.1 DPP4(1), p.169).
  - It keeps "the data is genuine" separate from "the data was taken in this incident". That supports the R16b and R11 assessment.
  - If any row matches a real customer, SEC escalates at once. I accept that as the first confirmation of exposure for the PH01 s.10.4(a)/(b) clock. **Professional judgment:** if the attacker holds the row, that is evidence the data was copied.
- **Final action:**
  - Hash and log the attacker's material by 09:45. Collect stray copies.
  - Only two SEC analysts and the DPO see the unmasked rows, on an offline lab workstation.
  - Run the structural, record, exfiltration and recycling checks.
  - Target the row-match result for 11:00 and the interim exfiltration assessment for 12:00.
  - On any match, tell the DPO, LC and me at once. LC then updates the HKMA, and the 12-hour scope review starts.
  - The forensic firm receives masked extracts only.
- **Owner:** SEC. Executed by the evidence custodian and two analysts. The DPO approves and witnesses the record lookup.
- **Time:** 09:45 intake; 11:00 row match; 12:00 interim assessment; any match escalated immediately.
- **Recipient and channel:** evidence register and decision log; verbal briefing to me, LC and the DPO; written results on paper or the lab system, not corporate email.
- **External basis:** SEC Q04a "Basis: external" (R10 DPP4(1); R11 pp.4–5; R16b p.2; R02 s.7.2.3(a)(v)) is adequate. Added: R16b PDF p.3 (verified), which expects the bank to "notify the affected customers as soon as practicable after the AI concerned is aware of or notified of the incident". That is triggered only if the privacy incident is confirmed serious, which is the missing fact the validation supplies.
- **Internal basis:** SEC Q04a "Basis: internal" (PH01 v1.0 ss.6.6, 10.4(a)–(c), 16.2, 12.3, 17.2, 5.8). No conflict.
- **Dispatch:** EXECUTE NOW.

**Q04b | Original: SEC sealed answer, Q04b | CONFIRM**
- **Reason:**
  - The vendor ran a remote account into the gateway, so PH01 s.6.7 (supplier evidence) and s.7.3 (suspected compromised credential) both apply.
  - The scope of the request, the delivery channel (native exports with a SHA-256 manifest, through a bank-hosted encrypted transfer or bank-issued encrypted media, never by email or the vendor's own path), the lockout and closure test, and escalation by 12:00 all meet PH01 and R02 s.7.2.3(a)(v)(2).
  - The vendor's offer to "preserve on request" is not relied on. A written request and a call-back confirmation are required.
- **Final action:**
  - Send the written preservation and production request now, or confirm and supplement the 09:00 request if it already went. Receipt confirmed by 10:00 through a call-back to a number in the third-party register.
  - Capture session and token state (10 minutes at most). Then lock out every account the vendor holds and block its path at the perimeter.
  - Run the closure test by about 10:00.
  - Vendor confirms preservation and delivery by 12:00; escalate if missed.
  - First log export by 14:00 (SEC's judgment).
  - Reconcile the vendor's records with the bank's own logs.
- **Owner:** SEC. LC clears the request wording and decides on contractual notice. The vendor relationship owner sends the request. IT Operations and Network carry out the lockout.
- **Time:** 10:00 request and lockout; 12:00 escalation point; 14:00 first export.
- **Recipient and channel:** the contract contact in the CRO's third-party register; written request plus call-back; material received through bank-hosted encrypted transfer or bank-issued media.
- **External basis:** SEC Q04b "Basis: external" (R03 ss.6.2.25(a), 6.2.23(c)–(d); R02 s.7.2.3(a)(v)(2); R12 s.2.8.1, conditional on the contract being an outsourcing; R10 DPP4(2), conditional; R11 Step 2). Adequate.
- **Internal basis:** SEC Q04b "Basis: internal" (PH01 v1.0 ss.6.7(a)–(d), 7.3–7.5, 17.1). SEC reads the s.6.7(c) four hours as running from declaration, giving 12:00. I accept that reading.
- **Facilitator to log:** whether the 09:00 request was actually sent.
- **Dispatch:** EXECUTE NOW. The lockout depends on the token capture of no more than 10 minutes. Reinstating vendor access is on HOLD until SEC signs off in writing and I decide (s.7.5).

**Q05a | Original: LC sealed answer, Q05a | CONFIRM**
- **Reason:** Not paying is the Board policy (PH01 s.12.1). The legal gates are correctly identified and verified:
  - R16c s.25A(2)(a), p.83: a defence exists only where "that disclosure is made before he does that act and he does that act with the consent of an authorized officer".
  - R16d s.8(a), p.20: the bank must not make property available to a person "knowing that, or being reckless as to whether, the person is a terrorist or terrorist associate". The wallet holder is anonymous, so recklessness cannot be excluded.
  - Sanctions screening: LC recorded that no direct rule was located in the assigned sources (search record in LC Q05a item 3). This is an internal gate only.
  - The 02:00 deadline does not move the posture.
- **Final action:**
  - Do not pay, and take no preparatory steps.
  - Written hold to Treasury by 10:30.
  - Police CSTCB report and s.25A disclosure by 11:00.
  - HKMA update on the demand and the data claim by 10:00.
  - Supplementary information to the Commissioner by the secure channel, now available.
  - The CFO notifies the insurer by 08:00 on 17 Nov.
  - I brief the Board chair by 10:00. That covers both the severity 1 declaration and the extortion demand, so it falls within LC's 11:30 latest time (PH01 s.15.1).
  - The Board alone may consider departing from the policy, and only after LC confirms every s.12.2 gate in writing.
- **Owner:** the Board decides on payment. LC owns the gates, the Police report and the regulators. Treasury holds. The CFO handles the insurer. I brief the Board chair.
- **Time:** 10:00, 10:30, 11:00 and 11:30 as above.
- **Recipient and channel:** Treasury in writing; Police CSTCB by phone, then a written disclosure; HKMA supervisory contact by phone, then in writing; Commissioner through the secure channel; Board chair by phone.
- **External and internal basis:** LC Q05a, items 1–6 and "Internal bank procedure". Adequate and verified as stated above.
- **Dispatch:** EXECUTE NOW. Any payment path is on HOLD pending the Board, which itself depends on Police consent under s.25A and clean screening.

**Q05b | Original: LC sealed answer, Q05b | CONFIRM**
- **Reason:** This applies PH01 s.12.3 exactly: no contact unless I authorise it in writing, on a joint LC and SEC recommendation, for a stated limited purpose, after consulting the Police. It conducts contact only through one specialist on a segregated channel, with a full transcript. It is consistent with s.6.6 and with the tipping-off and investigation-prejudice principles (R16c s.25A; R05 p.2). LC recorded that no direct external rule was located, with its search terms.
- **Final action:** no contact with the attacker. LC and SEC review the position after the Police consultation, target 11:00. If there is no recommendation, the default is no contact. All staff and vendors pass any attacker message to SEC.
- **Owner:** I authorise any contact, in writing. LC and SEC recommend. A designated specialist would conduct it.
- **Time:** effective 09:30; review at 11:00.
- **Recipient and channel:** decision log; staff instruction through the Q06a script.
- **Basis:** LC Q05b "Basis".
- **Dispatch:** EXECUTE NOW, as a prohibition. Any contact is on HOLD.

**Q06a | Original: COM sealed answer, Q06a | CONFIRM**
- **Reason:**
  - The script answers the "funds disappeared?" calls without claiming the ledger is intact. That line is gated on C1 (latest time 11:30, default hold), which complies with PH01 s.2.3.
  - It neither confirms nor denies the data claim, and promises direct contact if exposure is confirmed (R16b p.3).
  - It carries the safety line with no links, refers media to COM, sends attacker messages to SEC (s.12.3), and promises remediation only within s.13.1, 13.2 and 13.4.
  - It is distributed by channels that do not depend on corporate email (R05 p.3).
- **Final action:**
  - Frontline Script v2: LC clears by 09:45; live by 09:50; branch-manager call at 09:45; printed copies; floor briefing; IVR update.
  - Supervisors read the script back by 10:00 and COM logs each confirmation.
  - The knowledge base and email are used only after SEC logs them clean.
- **Owner:** COM approves. LC clears. SEC and Payments Operations confirm the facts. Branch managers and the contact-centre head deliver.
- **Time:** 09:45, 09:50 and 10:00. C1 by 11:30.
- **Recipient and channel:** as in COM Q06a item 6.
- **Basis:** COM Q06a "Basis (external)" and "Basis (internal)".
- **Dispatch:** EXECUTE NOW. Line C1 is on HOLD until SEC and Payments log ledger integrity.

**Q06b | Original: COM sealed answer, Q06b | OVERRIDE**
- **Reason:** COM's line [C2] reads "The bank has not made any payment to any party in connection with this incident." That is broader than anything that can be verified. The bank is paying, or has committed to pay, at least the retained forensic firm (engaged at severity 1 under PH01 s.6.5), and may pay remediation such as fee waivers. Read literally, the statement may be false.
  - PH01 v1.0 s.11.3: "It states whether a payment has been made only as a verified present fact."
  - **Professional judgment:** a public statement on a ransom question must be accurate and narrowly scoped.
- **Change:** I replace C2 with: "The bank has not made any payment to those responsible for the attack." The precondition stays: LC verifies with the CFO and Treasury, from records, by 09:50. If that is not verified, COM's fallback line is used. The new wording does not deny that a demand was received and makes no promise about the future. Everything else stays as COM wrote it:
  - the C3 authorities line;
  - the omissions (amount, deadline, screenshot, vendor, system, designation status);
  - my approval, with the COO as alternate after 15 minutes;
  - LC clearance, including that the reply does not prejudice the Police report or tip anyone off (R16c s.25A);
  - sending by 09:55 by phone read-out plus written text through a non-email route;
  - LC copying the reply to the HKMA (R05 p.3);
  - the default holding reply ("we will respond by 12:00").
- **Owner:** I approve. LC clears the text. SEC and Operations check the facts. COM sends.
- **Time:** draft 09:40; approval and C2 verification 09:50; sent 09:55, before the reporter's 10:00 deadline; next update 12:00.
- **Recipient and channel:** the reporter, by phone read-out and written text from COM's verified mobile, unless SEC has logged email as safe; copy to the HKMA through LC.
- **External basis:** COM Q06b "Basis (external)" (R05 pp.2–3; R09 fn.25; R16b p.3, verified; R11 Step 4).
- **Internal basis:** PH01 v1.0 s.11.3, quoted above; s.3 (media replies row); s.11.1; s.12.1; s.5.1.
- **Dispatch:** SCHEDULE the send for 09:55. It depends on my approval and LC's C2 and C3 verification by 09:50. If those are not done, the default holding reply goes at 09:55.

---
**Order of actions that depend on each other on this card:**
1. 09:30: no-pay and no-contact decisions logged. Attacker material taken into evidence by 09:45.
2. 09:40–09:50: script and media reply drafted; LC clears; LC verifies C2 and C3; I approve.
3. 09:45–09:50: frontline script goes live. 09:55: media reply sent, with the HKMA copy.
4. By 10:00:
   - HKMA update on the demand and the data claim. It comes before or with the media reply, and the media reply counts as a further update trigger.
   - Vendor request confirmed and vendor lockout done.
   - I brief the Board chair.
   - Read-back of the frontline script complete.
5. 10:30: Treasury hold in writing; LC logs after the event whether it cleared the 09:00 statement, and obtains the HKMA receipt.
6. 11:00:
   - SEC row-match result. Any match goes at once to the DPO, LC and me, and triggers an immediate HKMA update and the 12-hour scope review.
   - Police report and s.25A disclosure.
   - LC and SEC review the no-contact position. That review depends on the Police consultation.
7. 11:30: C1 ledger-integrity gate.
8. 12:00:
   - Interim exfiltration assessment.
   - Vendor escalation point.
   - HKMA scheduled update.
   - Public update. Its wording on the data claim depends on steps 6 and 8.
9. 14:00: first vendor log export.
10. Any departure on payment: Board only, after Police consent and clean screening. It cannot happen before step 6.