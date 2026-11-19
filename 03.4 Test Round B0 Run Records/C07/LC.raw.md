LC answer for C07 (Wednesday 18 November 2026, 12:00 HKT, H+52). Units: Q20a and Q20b only. Locked before I saw colleagues' answers. It is based on the facilitator's dispatch record for C07 as quoted in the handoff.

**What the dispatch record shows (Commissioner path)**
- 16 Nov, by 09:00: notification by telephone, not in the specified form. Exact time, reference number and receipt are not verified. It was not established that the number used is the Commissioner's designated number.
- 16 Nov, by 19:00 (or before 20:00 by a route the Commissioner named): Annex E filed, described as both the specified-form notification and the s.28(3) written record. The route used and the receipt are not verified.
- 16 Nov, 18:30: call to the Commissioner's office. Its outcome (reference number, logged time, whether the number is designated) is not verified.
- Supplementary information sent on 16 and 17 Nov. No receipts verified.
- Annex F (written report): not dispatched.

---

## Q20a – Is the specified-form follow-up required, outstanding, late or satisfied?

**Decision: required, and satisfied on the record, but not yet proven.**
- The follow-up was required because the 09:00 call was not in the specified form (s.28(3)).
- On the record it is satisfied. The Annex E filing on the evening of 16 Nov falls well inside the 48 hours after the call. It also falls inside the 12-hour limit, so it independently counts as a notification in the specified form under s.28(2)(b)(i).
- It is not yet proven because there is no verified receipt or route.
- The 48-hour clock has already run. Measured from a call made no later than 09:00 on 16 Nov, it ended no later than **09:00 HKT on Wed 18 Nov, three hours ago**. If the filing cannot be evidenced, the bank risks being treated as late.

**Clocks**
| Item | Rule | Time |
|---|---|---|
| s.28(1) notification | Sch.6 item 1(a): 12 hours | Ended 20:00 on 16 Nov. Met by the call if its content is accepted, and by the Annex E if its receipt is proven. |
| s.28(3) written record | Sch.6 item 2: 48 hours after the notification | Ended by 09:00 on 18 Nov, depending on the logged call time. |
| s.28(4) written report | Sch.6 item 3 | Due 30 Nov 2026 (see Q20b). |

**Immediate action**
1. **By 13:00 HKT.**
   - The LC duty officer gets the submission receipt or dispatch record from whichever device filed on 16 Nov: the standby device, the released terminal, or the route the Commissioner named. Compliance's device log should show which.
   - LC then calls the Commissioner's office on the verified route and asks it to confirm four things:
     - (a) the reference number and time it logged for the morning call;
     - (b) receipt of the Annex E filing, with its reference and receipt time;
     - (c) receipt of each piece of supplementary information;
     - (d) whether the number the bank called is the designated incident number.
   - Every answer is logged under PH01 s.5.5.
2. **If the Commissioner confirms receipt of the Annex E:** mark the item "satisfied (receipt evidenced)" in the deadline tracker. A second LC officer checks the entry.
3. **If receipt cannot be confirmed, or the Commissioner has no record:**
   - File the Annex E again at once through the designated secure channel, by 14:00 HKT. Mark it as a re-submission of the 16 Nov filing.
   - Attach the evidence the bank holds of the original attempt (time, device, operator).
   - Disclose openly that receipt could not be verified.
   - LC logs the item as a possible missed deadline. The CMT reconvenes (PH01 s.18.5). LC tells the CMT chair, informs the HKMA at the next update, and records it in the Board paper.
   - The bank does not argue the point beyond the evidence it actually holds.
4. **New indicator on the quarantined host.**
   - If SEC reaches reasonable certainty that it is the same incident, it is sent to the Commissioner as supplementary information.
   - If it is a new unauthorised act with an actual adverse effect on a critical computer system, it is a new s.28 incident with its own awareness point (R02 s.7.3.5). The clock would be 12 hours if the core function is affected, otherwise 48 hours.
   - **Missing facts:** whether the host is part of a critical computer system and whether it is related to the original incident. SEC confirms both (Q19b) and logs the time it reaches certainty. LC opens a provisional tracker line now.

**Owner:** LC, executed by the LC duty officer, with a second LC officer checking. SEC supplies the device log and the indicator facts.

**Recipient and channel:** the Commissioner of Critical Infrastructure (Computer-system Security). Telephone on the verified route for confirmation; designated secure channel for any re-filing.

**External basis**
- **R01, Cap. 653 (statute)**
  - s.28(2)(b), PDF p.44: notification must be "(i) ... in the form and way specified under section 10 ... or (ii) despite not being made in the specified form and way, include information on the nature of the computer-system security incident and identify the critical computer system concerned."
  - s.28(3): "If the notification is not made in the specified form and way, the CI operator must subsequently submit a written record ... in the specified form and way to the Commissioner within the specified time."
  - s.28(5): failing to comply with (1), (3) or (4) is an offence.
  - Schedule 6, PDF p.97, item 2: "48 hours after the notification concerned is made under section 28(1)."
  - Application: the call was not in the specified form, so a written record was required.
- **R02, OCCICS Code of Practice v1.0 (code of practice, not subsidiary legislation)**
  - Annex E, PDF p.42: "Pursuant to section 28(2)(b)(i)".
  - s.7.3.6(b), PDF p.36: telephone first, "then submit a specified form (Annex E or a sector-specific form) through a designated secured channel within 48 hours of the notification".
  - s.7.3.5: awareness at "a reasonable degree of certainty".
- **Professional judgment.** Compliance is a question of fact. Without a receipt the bank cannot prove it. Confirming with the recipient, and re-filing openly if needed, is the step most consistent with the statute.

**Internal bank procedure (PH01 v1.0)**
- s.5.5: "If no receipt is shown, LC asks the recipient for one in the same call or by return, and logs the request."
- s.18.5: "The CMT reconvenes at once on any ... missed external deadline".
- s.5.3: second-officer check of the tracker.
- No conflict with the external requirements.

---

## Q20b – Written incident report (Cap. 653 s.28(4), Annex F)

**Decision.** Prepare and file the written report in the specified form: Annex F, or a sector-specific form only if the Regulator Contact Register (RCR) records that the Commissioner has specified one for designated AIs.
- **To:** the Commissioner, through the designated secure channel. Not the HKMA: this is a category 3 obligation (R01 s.2, PDF p.9; R03 s.1.1.3). The HKMA receives a copy for information under its own supervisory process.
- **Statutory deadline:** within 14 days after the date of awareness (16 Nov), so **by Monday 30 November 2026**. LC treats 30 Nov as the latest date. I could not confirm the day-counting convention because the Interpretation and General Clauses Ordinance is not in the manifest, so I am taking the conservative reading.
- **Internal target:** file by **Friday 27 November 2026, 17:00 HKT**. That leaves a margin for any problem with the channel.

**Who does what**
- Accountable: LC (PH01 s.5.1). LC owns the form and the submission.
- Drafting lead: the LC duty officer, who compiles the sections.
- Section owners, each confirming their facts in writing:

| Section | Content | Owner |
|---|---|---|
| A | CI operator; critical computer system name and physical location (payment gateway; site to be confirmed) | SEC |
| B1–B4 | Nature, description, initial attack vector, root cause summary. Vendor credential use; attribution marked unverified. Whether the root cause appeared in a previous assessment or audit | SEC with the forensic firm |
| B5–B7 | Earliest time, awareness time (16/11/2026 08:00), how first detected | SEC, using the Q19a timeline in HKT with clock offsets of up to 4 minutes and their uncertainties |
| B8 | Hardware and software with vulnerabilities | SEC; the vendor via the relationship owner, through the evidence process |
| C1, C2, C7 | Scope, service impact, duration (transfers and payroll disrupted from 16 Nov 08:00; recovery state as logged) | Head of Payments Operations with SEC |
| C3 | Data impact: 320 customers confirmed and publicly mirrored; 18,000-record claim unverified | DPO. Counts and data types only, no customer personal data on the form (minimised, DPP 4) |
| C4 | Customer and third-party impact: SME payroll, counterparties, 31 suspected scam reports | Payments Operations and Head of Fraud |
| C5 | Financial impact estimate | CFO |
| D | Containment, recovery status, planned measures, timeline, external teams (forensic firm, vendor) | SEC |
| E1 | Stakeholders: Board, HKMA, Police (with case reference number if verified), PCPD, affected customers, counterparties | LC |
| E2 | Media communications and dates | COM |
| F | Reporting entity details | LC |

- **Fact-checking:** each fact must come from a record. Unverified items are marked "unverified" and are not left out (PH01 s.2.4, s.11.4).
- **Sign-off:** a second LC officer checks the form against Annex F and the deadline tracker. The CMT chair is informed and reviews in parallel. No internal approval may delay filing past the external deadline (PH01 s.2.4).

**Schedule (HKT)**
| Date | Step |
|---|---|
| 18 Nov | Assign sections and set the template |
| 23 Nov, 17:00 | Section inputs due |
| 24 Nov | LC consolidated draft |
| 25–26 Nov | Fact check, plus Compliance test of the filing route logged |
| 27 Nov | File |
| 28–30 Nov | Fallback window |

**Submission:** through the designated secure channel. The submission receipt is saved at the moment of filing (PH01 s.5.5). If no receipt appears, LC asks the Commissioner the same day. After filing, any new facts, such as the root cause or the outcome of the new indicator, go as supplementary material (R02 s.7.3.7(a)).

**External basis**
- **R01, Cap. 653, s.28(4), PDF p.44:** "After a CI operator makes a notification ... in the specified form and way, or submits a written record of such an incident under subsection (3), the CI operator must further submit a written report of the incident in the specified form and way to the Commissioner within the specified time."
- **R01, Schedule 6, item 3, PDF p.97:** "14 days after the date on which the CI operator concerned becomes aware of the computer-system security incident concerned."
- **R01, s.28(5)–(6):** failure is an offence, with a fine of up to $5,000,000 on indictment.
- **R02, s.7.3.7(a), PDF p.37:** "submit a written report in a specified form (Annex F or a sector-specific form) via the designated secured channel within 14 days ... If additional information become available after submitting the written report, the CI operator should also provide such information to the Commissioner as supplementary material."
- **R02, Annex F, PDF pp.43–46:** heading "Pursuant to section 28(4)"; "All fields should be completed as far as practicable based on the information available."
- **R02, s.7.3.7(b):** sector-specific requirements still apply. That is why the HKMA copy is sent.
- **Left to judgment:** how far the root cause analysis can be completed in 14 days. Where it is incomplete, it is marked as preliminary and followed by supplementary material.

**Internal bank procedure (PH01 v1.0)**
- s.5.2: LC applies "Cap. 653, section 28 and Schedule 6, and the Commissioner's Code of Practice section 7.3 and its Annexes E and F".
- s.5.6: "LC first confirms from the external document the form and the way of submission that report requires, and records them in the deadline tracker."
- s.1.4: internal times "never extend an external deadline".
- s.18.4: at handover LC "takes over the register of external deadlines".
- No conflict with the external requirements.

**Simulated actions for the facilitator to log (HKT)**
- 12:05: decision log entry and tracker entries.
- 13:00: receipt retrieval and confirmation call to the Commissioner.
- 14:00: conditional Annex E re-filing.
- On SEC certainty about the new indicator: provisional new-incident line.
- 18 Nov: Annex F section assignments issued.
- 23, 24 and 26 Nov: drafting milestones.
- 27 Nov: Annex F filed through the designated secure channel, receipt saved.
- Statutory latest: 30 Nov 2026.