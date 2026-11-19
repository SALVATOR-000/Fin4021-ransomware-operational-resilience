C08 is decided: all six units are CONFIRM, with no overrides. At H+72 there is no production authorisation and no closing update. Every restriction carries into handover as OPEN until its logged release. This is the CEO final record for Thu 19 Nov 2026, 08:00 HKT. All actions are simulated, for the facilitator to log.

**Checks I made myself:**
- R01 s.22(1)–(3), PDF pp.33–34: notice "within 1 month after the date on which the event occurs". A change is "material" if it "affects— (i) the computer-system security of the critical computer system".
- R03 ss.6.1.1–6.1.3, PDF p.11: the event date "generally refers to the moment when a change is deployed to production environments". s.6.1.2 covers changes with "high security risk implications".
- Other citations are as given in the sealed answers.

**CEO decisions at 08:05, which set the position for every unit:**
1. **Recovered system stays on HOLD.** The 240/240 result is a sample in a test environment. PH01 s.9.2 says "A sample result is recorded as a sample". No s.9.3 gate item is evidenced, and the root cause of the C06 mismatches is not logged.
2. **Secondary process is treated as HOLD.** No card records SEC's clearance, the clean sweep or the re-clearance.
3. **No closing update.** None of the PH01 s.11.5 conditions is met.

There are no conflicts between the three roles: SEC, LC and COM reach the same three positions. The only thing between roles is a dependency: SEC's list of changes made to critical computer systems (CCS) during the incident feeds LC's s.22 register.

---
**Q22a | Original: SEC sealed answer, Q22a | CONFIRM**
- **Reason:**
  - Nothing is released. Each restriction keeps its release condition and its s.3 decision-maker (PH01 s.18.3).
  - The quarantine, evidence hold, production HOLD, vendor revocation, stop controls and raised monitoring all stay. Containment is not confirmed, because the Q19b sweep and the closure test are not evidenced.
  - The handover pack opens with a list of what is not evidenced, and those items transfer as open (s.18.2).
  - Each receiving owner signs for a specific list (s.18.1).
  - The CCS change list goes to LC (s.18.4).
  - The 14-day quiet period before monitoring returns to baseline is reasonable judgment.
- **Final action:** as in SEC Q22a (the restriction table and handover actions 1–5).
- **Owner:** SEC. Execution is by the receiving owners named in SEC's answer. Release decisions stay with the s.3 decision-makers.
- **Time:** handover packs signed by 18:00 on 19 Nov. Each restriction holds until its release is logged.
- **Recipient and channel:** handover packs, signed acceptance sheets, decision log ("held"), evidence register, briefing to me.
- **External basis:** as in SEC Q22a "Basis: external" (R08 s.4.2.4; R07 s.1.3.3; R03 s.6.2.26(a); R05 p.1).
- **Internal basis:** as in SEC Q22a "Basis: internal" (PH01 v1.0 ss.18.1–18.5, 9.2, 9.3, 2.5, 7.5). No conflict.
- **Dispatch:** EXECUTE NOW for the handover. The restrictions stay on HOLD until each release is logged.

**Q22b | Original: SEC sealed answer, Q22b | CONFIRM**
- **Reason:**
  - The two closure points are kept apart:
    - (A) Credential closed under s.7.4: a replayed token and a logon with the old credential both fail, with result and time logged. If this is not on record, it is re-run by 10:00 today, and any success reopens the access window.
    - (B) Vendor issue closed under s.7.5: root cause known, the vendor's records received and reconciled, any new access meets s.7.2, then SEC's written sign-off and my decision.
  - Remediation items 1–8 each have an owner and a risk-based date, consistent with R03 s.6.3.7(c), R02 s.7.2.3(i) and R13 p.3.
  - The playbook gaps in s.8.7 and s.6.7(c) go into the post-incident review.
- **Final action:** as in SEC Q22b (remediation table; evidence lists for A and B).
- **Owner:** SEC, with the named owners in SEC's table. I approve the review and decide any reinstatement.
- **Time:**
  - Closure test by 10:00 on 19 Nov.
  - Remediation from 3 Dec to 31 Dec 2026.
  - Draft post-incident review 18 Dec.
- **Recipient and channel:** treatment-plan register, decision log, evidence register; status to me and the Board; facts to LC.
- **External basis:** as in SEC Q22b "Basis: external".
- **Internal basis:** as in SEC Q22b "Basis: internal" (PH01 v1.0 ss.7.2, 7.4, 7.5, 6.7(d), 3). No conflict.
- **Dispatch:** EXECUTE NOW for the closure test, then SCHEDULE the remediation items. Vendor reinstatement is on HOLD until (A) and (B) are evidenced.

**Q23a | Original: LC sealed answer, Q23a | CONFIRM**
- **Reason:**
  - LC stays accountable and takes over the register of external deadlines item by item (s.18.4). A named Compliance officer signs for it, and a second officer checks each item.
  - Everything without a receipt transfers as OPEN.
  - The items are complete:
    - Commissioner: confirmation, or re-filing of Annex E, by 10:00, with any possibly missed deadline disclosed.
    - Annex F: filed 27 Nov; statutory latest 30 Nov.
    - The new-indicator line.
    - HKMA: the pending 08:00 update. It should also cover COM's cadence gap and the handover.
    - PCPD update, target 25 Nov.
    - Police reference and s.25A status.
    - Treasury hold and the no-contact rule kept.
    - Vendor contract, remediation wording, forensic-firm copies, insurer.
  - The new s.22 item is correctly applied. I verified it: notice "within 1 month after the date on which the event occurs" (R01 s.22(1)). The event date is the production deployment (R03 s.6.1.1). Security changes are material under s.22(3)(a)(i). That makes 16 Dec 2026 the deadline for the 16 Nov changes and 18 Dec for the 18 Nov rules. SEC's s.6.1.2 risk assessment is due by 30 Nov.
- **Final action:** as in LC Q23a, items 1–12 and the handover steps.
- **Owner:** LC. The receiving holder is the Deputy Head of Compliance (regulatory reporting). Copies go to me and the CRO.
- **Time:**
  - HKMA by 08:15; Commissioner by 10:00.
  - Register handed over by 17:00 on 19 Nov.
  - Weekly review from 26 Nov.
  - Annex F 27 Nov (statutory latest 30 Nov).
  - PCPD update 25 Nov.
  - s.22 notices by 16 and 18 Dec.
- **Recipient and channel:**
  - Commissioner, via the designated secure channel.
  - MA, using the s.22 form and way it has specified.
  - HKMA, by phone and then a confirmed written route.
  - PCPD, by fax or in person.
  - Police CSTCB.
- **External basis:** as in LC Q23a, with the s.22 citations verified above.
- **Internal basis:** as in LC Q23a "Internal bank procedure" (PH01 v1.0 ss.18.1, 18.2, 18.4). No conflict.
- **Dispatch:** EXECUTE NOW for the HKMA update, the Commissioner confirmation and the register handover. SCHEDULE Annex F, the PCPD update and the s.22 notices. The s.22 notices depend on SEC's CCS change list and risk assessment.

**Q23b | Original: LC sealed answer, Q23b | CONFIRM**
- **Reason:**
  - The legal hold under s.17.1 continues, and rotation and recycling stay stopped.
  - The table of record types follows s.17.2. Originals are reviewed on 16 Dec and then quarterly. They are released only when LC confirms no investigation or inquiry still needs them, and CCS logs are kept at least 6 months (R03 s.6.2.23(c)).
  - Third-party copies are returned or destroyed within 30 days, with a certificate (DPP2(3)). LC directs the forensic firm to keep its copy for now.
  - Working copies of customer data are minimised and erased when their task ends (DPP2(2)).
  - Disposal needs LC's written confirmation, the record owner's approval and certified destruction (s.17.3).
  - LC's "no direct rule located" search record for the seven-year period is adequate.
- **Final action:** as in LC Q23b. The hold is reconfirmed in writing at 15:00.
- **Owner:** LC, with the record owners named in LC's table.
- **Time:** 15:00 hold reconfirmation; first review 16 Dec 2026; then quarterly or yearly as tabled.
- **Recipient and channel:** written legal hold to custodians, the vendor and the forensic firm; the evidence and records registers.
- **External basis:** as in LC Q23b "External basis".
- **Internal basis:** as in LC Q23b "Internal bank procedure" (PH01 v1.0 ss.17.1–17.3, 18.3). No conflict.
- **Dispatch:** EXECUTE NOW for the hold. Disposal is on HOLD until the stated conditions are met.

**Q24a | Original: COM sealed answer, Q24a | CONFIRM (Version P)**
- **Reason:**
  - None of the five s.11.5 closing conditions is met, so updates continue.
  - COM correctly flags the cadence gap since 07:00 on 18 Nov and passes it to LC.
  - I have logged no s.9.3 gate decision, so Version P (production pending) is the right one.
  - "We have contacted…" is used only if the delivery register shows the evidence; otherwise "We are contacting…".
  - No test figures and no restoration time are published.
- **Final action:**
  - Version P, approved by me and cleared by LC, released by 09:00. Copy to the HKMA.
  - Then updates at least every six hours from 07:00 to 22:00, and at once on any change in service status.
  - The alternative-process sentence is used only if Payments confirms the process is cleared and its reconciliation ties.
  - Version S only after I log the s.9.3 gate. Version C only when every s.11.5 condition is evidenced.
- **Owner:** I approve (COO as alternate after 15 minutes). LC clears. SEC and Payments check facts. COM releases.
- **Time:** 09:00, then on the s.11.2 cadence.
- **Recipient and channel:** as in COM Q24a "Action". The website is used only if SEC has logged it clean. Copy to the HKMA through LC.
- **External basis:** as in COM Q24a "Basis (external)", including COM's no-direct-rule search record.
- **Internal basis:** as in COM Q24a "Basis (internal)" (PH01 v1.0 ss.11.2–11.5, 9.3, 1.4). No conflict.
- **Dispatch:** EXECUTE NOW for Version P. Version S is SCHEDULED to trigger on my logged gate authorisation. Version C is on HOLD.

**Q24b | Original: COM sealed answer, Q24b | CONFIRM**
- **Reason:**
  - The written handover gives named owners for the communications log, the delivery register for the 320, every case, the Group B review and its triggers, public updates, counterparties, HKMA copies and lessons learned. That satisfies s.11.5 ("every open case has a named owner") and s.18.1.
  - COM stays accountable until the closing update.
  - Rows without evidenced delivery are followed up within 24 hours on a risk basis (R09 s.4.2.3; R16b p.3).
  - The rule of one consolidated notice per customer (s.10.6) is kept.
  - Staff still do not promise reimbursement of scam losses (s.13.4).
- **Final action:** as in COM Q24b, items 1–8.
- **Owner:** COM. The Customer Communications deputy executes. Case owners as listed in COM's answer. LC receives the commitments register.
- **Time:** signed by 12:00 on 19 Nov; daily 09:00 review until closure.
- **Recipient and channel:** written handover pack; decision log; case and delivery registers.
- **External basis:** as in COM Q24b "Basis (external)".
- **Internal basis:** as in COM Q24b "Basis (internal)". No conflict.
- **Dispatch:** EXECUTE NOW.

---
**Order of actions that depend on each other:**
1. 08:05: decision log entries: recovered system HOLD, secondary process HOLD, no closing update.
2. 08:15: LC's HKMA update. It covers handover, open items, test-only results, the cadence gap and any outcome from the Commissioner.
3. By 09:00: Version P released, with a copy to the HKMA through LC.
4. By 10:00:
   - Commissioner confirmation. If receipt is still unconfirmed: re-file Annex E, disclose the possibly missed deadline, reconvene the CMT, and tell the HKMA and the Board.
   - SEC closure test. If it fails: reopen the access window and reconvene the CMT.
5. 12:00:
   - COM's handover signed.
   - SEC's CCS change list goes to LC and is entered in the s.22 register.
6. 15:00: legal hold reconfirmed in writing.
7. 17:00: LC register handed over.
8. 18:00: SEC handover packs signed. The CMT stands down only once every open item has a signed owner (s.18.1).
9. Upcoming dates:
   - PCPD update 25 Nov.
   - Weekly register review 26 Nov.
   - Annex F filed 27 Nov (statutory latest 30 Nov).
   - SEC risk assessment for s.22 by 30 Nov.
   - s.22 notices to the MA by 16 and 18 Dec.
   - First review of the originals 16 Dec.
   - Remediation by 31 Dec.
10. Any return to production requires all of these, in order:
    - a full-set re-test with zero unexplained differences;
    - every s.9.3 item signed;
    - my authorisation;
    - an s.22 notice within one month of each deployment phase;
    - an HKMA update and Version S.