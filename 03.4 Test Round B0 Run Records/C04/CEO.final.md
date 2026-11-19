C04 is decided: five units CONFIRM and Q12b OVERRIDE. The override changes the wording and recipient list of COM's SMS alert. The urgent items are the Commissioner specified form, which must be filed by 19:00 against the statutory 20:00 limit, and the SEC security clearance, due by 19:00, that gates the secondary process. Final CEO record for Mon 16 Nov 2026, 18:00 HKT (H+10). All actions are simulated, for the facilitator to log.

**What I checked myself:**
- R01 s.28(2)–(5), PDF p.44, and Sch.6, PDF p.97.
- R02 Annex E, PDF p.42.
- PH01 v1.0, ss.2–18. I read these at earlier cards.
- All other citations are taken unchanged from the sealed answers.

**Facts from the handoffs that I rely on:**
- The Commissioner's record shows only the 09:00 call. There is no logged time, no reference number and no receipt. Whether the number called is the Commissioner's designated one was never established. No specified form has been sent.
- The HKMA contacts were all made, but none has a verified receipt.
- Of the public updates, only the 09:00 statement can be verified as released. The 12:00 update and the 13:30 data update cannot.

**Conflicts across the roles, resolved:**
- **Timing of COM's 18:45 update and the secondary process:** SEC's clearance is due at 19:00. COM's latest time to choose a version is 18:40, so COM's default Version B goes out. It says the alternative process is being prepared, which matches SEC's hold. If I activate the process later, COM issues Version A at once (PH01 s.11.2, a change in service status).
- **SMS wording:** "will not be lost" in COM's SMS conflicts with SEC's Q10b position. In-flight items have unknown status, and the queue itself is not trusted. I resolve this in Q12b.
- **Board:** I tell the Board chair at 20:00, when 50% of the 24-hour tolerance is reached (PH01 s.4.3). Because SEC's numbers put the tail of the queue at risk of passing 100% at 08:00 Tue, I also ask the Board chair to put the Board or Risk Committee on notice (PH01 s.4.3, s.15.2).

---
**Q10a | Original: SEC sealed answer, Q10a | CONFIRM**
- **Reason:**
  - It applies PH01 s.8.2: activation only after SEC's written clearance that the process "shares no hosts, accounts, keys or network path with any affected system". The security default is hold (s.2.3).
  - Instructions are rebuilt from records outside the gateway, not trusted from the compromised queue. This is supported by R07 s.4.3.2, "record reconstruction and verification".
  - The pilot is 20 instructions (s.8.3) and the priority order follows s.8.4.
  - The arithmetic is right: about 360 an hour after the 10% urgent reserve, so 4,200 items take about 11.7 hours. The resulting tolerance risk is escalated to me.
- **Final action:**
  - SEC's clearance review runs 18:00–19:00, covering items (i) to (v) in SEC's answer. Default is hold.
  - If cleared in writing: I activate and log it as a BCP activation (s.4.4), and LC is told at once.
  - Pilot of 20 SME payroll instructions about 19:30, reconciled end to end. Full run from about 20:00.
  - Priority: payroll by earliest value date, then items due today or the next business day, then order of submission. 10% of capacity reserved for urgent referrals. Customer size never sets the order.
  - Reconciliation every hour. The stop triggers apply as in SEC's answer.
  - Taking data off a held system needs a joint SEC and LC release (PH01 s.3).
- **Owner:** SEC for clearance. I activate, after consulting the Head of Payments Operations. Payments Operations runs the process.
- **Time:** clearance by 19:00; pilot about 19:30; full run about 20:00; 50% tolerance at 20:00; 100% at 08:00 Tue.
- **Recipient and channel:** written clearance or refusal into the decision log; BCP activation entry; emergency change record; LC for the HKMA; COM for the public status.
- **External basis:** as in SEC Q10a, "Basis: external sources" (R07 ss.1.3.3, 4.3.2; R06 s.3.4 by analogy; R05 p.1; R09 s.8.2.1).
- **Internal basis:** as in SEC Q10a, "Basis: internal bank procedure" (PH01 v1.0 ss.8.2–8.4, 8.7, 2.3, 6.1, 4.3). No conflict.
- **Dispatch:** EXECUTE NOW for the clearance review. Activation is on HOLD until SEC's written clearance; then I activate and the pilot is SCHEDULED for about 19:30. Full run only after the pilot reconciles.

**Q10b | Original: SEC sealed answer, Q10b | CONFIRM**
- **Reason:**
  - It applies PH01 s.8.6 in full: one register, one processing ID, each instruction released once only.
  - Retries, suspected duplicates and in-flight items need two checks: intent, by call-back to a number on file, and status, from the ledger plus an independent record from the receiving side. If either is missing, the item is held.
  - Each instruction is also checked against the customer's original authenticated instruction (s.8.5), with Fraud reviewing mismatches.
  - It is consistent with R14b A.1 ("duplication checks when re-attempting transactions").
  - The extra care for call-backs to the 80 customers whose data was exposed is sound judgment.
- **Final action:** as in SEC Q10b, steps 1 to 7. The control must be in place before the first pilot item.
- **Owner:** the Head of Payments Operations. SEC sets and audits the integrity checks. Fraud reviews flagged items.
- **Time:** before about 19:30, and applied to every batch. Held items reviewed every hour.
- **Recipient and channel:** instruction register, case register and decision log; call-backs to numbers on file; duplicate statistics to LC and COM.
- **External basis:** as in SEC Q10b, "Basis: external sources" (R14b p.1 s.A.1; R07 s.4.3.2; R05 p.1; R09 s.8.2.1; R08 s.3.2.2).
- **Internal basis:** as in SEC Q10b, "Basis: internal bank procedure" (PH01 v1.0 ss.8.5–8.7, 10.5). No conflict.
- **Dispatch:** EXECUTE NOW. The pilot (Q10a) depends on this control being in place.

**Q11a | Original: LC sealed answer, Q11a | CONFIRM**
- **Reason:**
  - Under R01 s.28(2)(b)(ii), the 09:00 call counts only if it included the nature of the incident and identified the system. None of that is evidenced.
  - The secure-channel supplementary messages are not the specified form.
  - Filing Annex E now, before the 20:00 limit in R01 Sch.6 item 1(a), makes the notification compliant in its own right under s.28(2)(b)(i). The Annex E heading on R02 p.42 reads "Pursuant to section 28(2)(b)(i)".
  - The same filing also serves as the s.28(3) written record, well within 48 hours.
  - Failing s.28(1) or (3) is an offence (s.28(5)). Filing now removes that risk at minimal cost.
  - LC correctly records that its C01 target of Tuesday for the written record has been overtaken by the evidence gap.
- **Final action:**
  - File Annex E (or the HKMA sector form if the contact register shows one) through the designated secure channel by 19:00. Tick B1 "Has disrupted / is disrupting / likely to disrupt the core function of CI". Content as in LC Q11a item 1; "Supply chain attack" is ticked only if SEC confirms.
  - Save the receipt the moment it is filed.
  - Separately, call the Commissioner's office by 18:30 to get the reference and logged time of the morning call. This call must not delay the filing.
  - If no filing device is logged as working by 19:00, file by the route the Commissioner names before 20:00.
  - Written report (Annex F) due 30 Nov; internal target 27 Nov.
- **Owner:** LC. Executed by the LC duty officer. SEC confirms the facts. A second LC officer checks the form.
- **Time:** 18:30 call; filed by 19:00; statutory limit 20:00 HKT 16 Nov; report by 30 Nov 2026.
- **Recipient and channel:** the Commissioner of Critical Infrastructure (Computer-system Security); the designated secure channel through the standby device or the released terminal, or the route the Commissioner names.
- **External basis:** as in LC Q11a, "Basis (external)". Checked against the source: R01 PDF p.44, s.28(2)(b)(i) "be made in the form and way specified under section 10", s.28(3) and s.28(5); R02 PDF p.42, Annex E.
- **Internal basis:** as in LC Q11a, "Internal bank procedure" (PH01 v1.0 ss.5.5, 5.6, 2.4, 1.4). No conflict.
- **Dispatch:** EXECUTE NOW. Not held by any internal condition (s.2.4).

**Q11b | Original: LC sealed answer, Q11b | CONFIRM**
- **Reason:**
  - The change in service status (4,200 queued, payroll at risk, retries, call surge, branch access) triggers an immediate update under PH01 s.5.8 ("at once on ... a change in service status").
  - The missing acknowledgements and the unverified written route justify asking the HKMA to confirm what it received.
  - Sending copies only of public material whose release is verified meets R05 p.3 accurately.
  - The BCP report is correctly made conditional on my activation, under R07 s.1.3.3.
  - LC's "no direct rule located" record on update cadence (its regex searches of R05, R06, R07, R09 and R13) is adequate.
- **Final action:**
  - Phone the HKMA by 18:30 with the content in LC Q11b item 1.
  - Written follow-up by 19:30 by the route the HKMA confirms, with copies of verified public material, including the 18:45 update once it is released. Re-send the 10:00 confirmation if the HKMA did not receive it.
  - Call the HKMA at once on BCP activation.
  - Scheduled updates at 20:00 (to include the Commissioner receipt and my decision on the secondary process), 24:00 and 04:00, then 08:00 and 18:00.
  - **Added instruction (no change to execution):** if COM establishes that the 12:00 public update was not issued, LC tells the HKMA in the 20:00 update.
- **Owner:** LC. Executed by the LC duty officer. SEC and Payments confirm the figures. COM supplies the copies.
- **Time:** 18:30, 19:30, 20:00; on activation, at once.
- **Recipient and channel:** HKMA supervisory contact; phone from the printed contact register, then a confirmed written route (corporate email only if logged safe).
- **External basis:** as in LC Q11b, "Basis (external)".
- **Internal basis:** as in LC Q11b, "Internal bank procedure". No conflict.
- **Dispatch:** EXECUTE NOW. The BCP report is triggered by my activation decision.

**Q12a | Original: COM sealed answer, Q12a | CONFIRM**
- **Reason:**
  - The update stands on its own, because only the 09:00 statement can be verified. It covers what is confirmed, what is being verified, what customers can do and when the next update is due (PH01 s.11.2).
  - Figures are given only when confirmed from a record (s.11.4). The fixed lines are kept (s.11.3).
  - The Version A/B condition has all four items s.2.3 requires, with a go-ahead default. That is permitted, because this is not a security condition.
  - The "do not resubmit" message supports the Q10b duplicate control.
  - COM logged the possible cadence breach openly.
- **Final action:**
  - Release by 18:45 after my approval, LC clearance and fact-check. Version B applies, because activation will not be logged by 18:40.
  - Version A goes out at once on activation and a clean pilot.
  - Frontline Script v4 goes out at the same time. Copy to the HKMA through LC.
  - Next update by 22:00, then from 07:00 on 17 Nov.
  - COM establishes by 19:00 whether the 12:00 and 13:30 updates were issued, and tells LC.
- **Owner:** I approve (COO as alternate after 15 minutes). LC clears. SEC, the DPO and Payments check the facts. COM releases.
- **Time:** 18:45; 22:00; at once on any change in service status.
- **Recipient and channel:** same channels as 09:00 (website only if SEC has logged it clean); copy to the HKMA.
- **External basis:** as in COM Q12a, "Basis (external)".
- **Internal basis:** as in COM Q12a, "Basis (internal)". No conflict.
- **Dispatch:** EXECUTE NOW for Version B by 18:45. Version A is SCHEDULED on the trigger of activation and a clean pilot.

**Q12b | Original: COM sealed answer, Q12b | OVERRIDE (item 5 only)**
- **Kept unchanged:** items 1 to 4 and 6. These are the contact-centre surge with call-back registration, RM calls to SMEs by 21:00, extended branch hours and priority desks, the urgent-referral route, and monitoring of social media.
- **Reason for the override:** COM's SMS reads "your payment instruction is waiting and will not be lost". That is not a verified present fact, for three reasons:
  - Under PH01 s.8.6, "Items in flight at the failure are held as status unknown until an independent record shows they did not settle". Some instructions may already have settled, so "waiting" can be wrong.
  - SEC (Q10b) treats the queue as untrusted and rebuilds instructions from external records.
  - Taking the recipient list from the gateway queue would rely on a system under evidence hold (s.6.1).

  **Professional judgment:** a promise that is later broken causes more calls and more retries, which defeats the purpose. Both COM and SEC require statements to be consistent and verifiable (R05 PDF p.3: "consistent and up-to-date messages are conveyed to all relevant parties on a timely basis").
- **Changed action:**
  - **Text:** "Lan Tidal Bank: we are checking payment instructions affected by the service disruption so each payment is made only once. Please do not resubmit. We may call you on the number in our records; we never ask for PINs or one-time passwords. Questions: call the number on the back of your card." No link.
  - **Recipients:** customers identified from the Payments Operations instruction register built under Q10b, not from the raw gateway queue. The 80 customers whose data was exposed are excluded and handled through their direct notice. Contact details changed since 08:00 go to Fraud first (s.10.5).
  - **Time:** send by 20:00, once the register list exists. Until then, the IVR and the 18:45 update carry the same message.
- **Owner:** COM drafts and sends. LC clears. I approve the audience (s.10.1). The Head of Payments Operations supplies the list. The COO and the heads of the contact centre and branch network deliver items 1 to 4.
- **Time:** measures live 18:30–19:00; SME calls by 21:00; SMS by 20:00 after the register list is ready; COM reviews at 21:00.
- **Recipient and channel:** customers by IVR call-back, RM phone calls, branches, and SMS with no link.
- **External basis:** as in COM Q12b, "Basis (external)" (R05 PDF p.3 "Handling of customers' and media's enquiry"; R05 PDF p.1; R09 fn.24). COM's "No direct rule located" record for call-back registration stands. Added: R05 PDF p.3, as quoted above.
- **Internal basis:** as in COM Q12b, "Basis (internal)". Added: PH01 v1.0 s.8.6 (quoted above), s.6.1 (evidence hold) and s.10.1 ("the CMT chair approves the audience").
- **Dispatch:** EXECUTE NOW for items 1 to 4 and 6. SCHEDULE the SMS for 20:00; it depends on the Q10b register list and LC clearance.

---
**Order of actions that depend on each other:**
1. 18:00: SEC clearance review begins. Q10b duplicate control is built. LC prepares Annex E. Surge measures are started.
2. 18:30: LC calls the Commissioner's office and the HKMA. Customer-access measures go live. If the call-back route is live, COM includes it in the 18:45 update.
3. 18:40–18:45: Version B public update and Script v4 released. LC copies them to the HKMA.
4. By 19:00:
   - Annex E filed and receipt saved. Fallback route before 20:00.
   - SEC signs or refuses clearance.
   - COM reports whether the 12:00 and 13:30 updates were issued.
5. If cleared: I activate the process (BCP entry). LC phones the HKMA at once. The pilot of 20 runs about 19:30, but only with the Q10b control in place.
6. 19:30: written HKMA follow-up.
7. 20:00:
   - I tell the Board chair (50% tolerance) and put the Board or Risk Committee on notice for 08:00 Tue.
   - Scheduled HKMA update.
   - Full run starts if the pilot reconciled. COM issues Version A at once.
   - SMS sent from the register list.
8. 21:00: SME calls complete and COM reviews call-centre performance.
9. 22:00: public update.
10. Hourly reconciliation. Any stop trigger halts releases and leads to a public update and an HKMA update.
11. 08:00 Tue: 100% of tolerance. Board or Risk Committee convened (s.4.3; meets within 12 hours under s.15.2).