CEO FINAL DECISION RECORD: C03 (Mon 16 Nov 2026, 12:00 HKT, H+4). Lan Tidal Bank, CMT chair.

All actions are simulated, for the facilitator to log. I received sealed answers for all six units. No facilitator handoffs were given for C03.

Citations I checked myself before relying on them:
- R11 PDF pp.4–8, in particular p.6 Step 4, p.7 notification contents, p.8 "When to notify?" and "How to notify?".
- R16a PDF pp.1–4 (voluntary status; channels on p.3, including fax 2877 7026; Annex p.4).
- R16b PDF pp.2–3.
- R10 Sch.1 DPP4(1), PDF p.169. A search of R10 for "data breach" returned 0 hits.
- R03 6.2.13(b), PDF p.14.
- R02 Annex F D.1, PDF p.45.
- PH01 v1.0 in full.

**CEO record entries at 12:00**
1. **Severity 1 continues.** Confirmed customer data exposure is an additional trigger under PH01 v1.0 s.4.1.
2. **Board chair call.** PH01 s.15.1 requires the Board chair to be told of confirmed data exposure within 2 hours. I will phone by 13:00; the limit is 14:00.
3. **Scope-review clock.** The PH01 s.10.4(b) clock starts at SEC's logged first-confirmation time, taken as 12:00. The review limit is therefore 24:00.
4. **Monitoring cost.** The 12-month monitoring offer (PH01 s.13.5) counts towards the incident total. The CFO tracks the running total under s.13.7.

==================================================================
**UNIT C03-Q07a: scope of exfiltration, and what evidence changes the estimate**

**Original answer reference:** sealed SEC answer for C03, "UNIT Q07a", steps S1–S7 and "EVIDENCE THAT WOULD CHANGE THE ESTIMATE".

**Decision:** CONFIRM.

**Reason**
- The scope is built from evidence: the access window, an exact population taken from an offline lab copy, a sweep of every way data could leave, and four classes (confirmed / evidence of access / possible / excluded).
- It is never extrapolated from the 80 or taken from the attacker's claim. This matches PH01 s.10.4(c).
- The rule that a record can be excluded only where logs are complete and integrity-checked is the right standard for HKID data.
- The 20:00 package leaves time for the s.10.4(b) review, which I bring forward to 21:00 under Q08b.
- Counts of records and of individuals are kept separate, as R11 p.7 asks: "approximate number of data subjects" and "approximate number of personal data records".
- No report is held for this work (PH01 s.2.4).

**Final action and condition:** S1–S7 and the evidence criteria exactly as written. The window stays "open" until the Q07b closure test passes.

**Accountable owner:**
- SEC is accountable.
- Execution: SEC analysts, the retained forensic firm and the custodian. The data owner supplies the population.
- The DPO and LC review. I decide the scope.

**HKT time, deadline or trigger:**

| Step | Time |
|---|---|
| Confirmed facts to LC, DPO and chair | 12:15 |
| Workspace containment check | 12:30 |
| Access window fixed | 13:00 |
| Population count and preliminary scope | 15:00 |
| Evidence sweep | 15:00–20:00 |
| Full scope package | 20:00 |
| Re-report | on each new piece of evidence, and hourly |

**Recipient and channel:**
- Inside the CMT room or by phone, plus the decision log: LC, the DPO and the chair.
- Tokenised analysis copies stay in the lab or evidence store only.

**Final external basis:**
- SEC Q07a, "BASIS: EXTERNAL" items 1–5, adopted: R11 pp.4, 7, 8; R16b p.2; R03 6.2.23(b),(d); R10 DPP4(1)(a); R02 7.3.4(d); R16a p.2. I verified R11 pp.7–8 and R16a p.2.
- SEC's "no direct rule located" search record for the scoping method is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.10.4(a)–(d), s.6.4, s.6.7(d), s.16.2, s.17.2 and s.2.4, as in SEC Q07a.
- No conflict found.

**Dispatch instruction:**
- EXECUTE NOW: S1 and S2.
- SCHEDULE: S3 at 13:00, S4 at 15:00, S5 from 15:00 to 20:00, S7 at 15:00 and 20:00.
- Dependency: the window end depends on Q07b K4.

==================================================================
**UNIT C03-Q07b: vendor credential, active sessions and tokens**

**Original answer reference:** sealed SEC answer for C03, "UNIT Q07b", steps K1–K9.

**Decision:** CONFIRM.

**Reason**
- SEC correctly logs the C02 revocation as "not closed". PH01 s.7.4 says a credential is closed only when "a replayed token and a logon with the old credential both fail".
- Capture is capped at 10 minutes and is overridden if data is moving (PH01 s.7.3, s.6.2).
- Server-side session invalidation, rotation of secrets and a persistence sweep all follow.
- Every vendor account is disabled.
- Reinstatement is held under s.7.5.
- SEC's alternate-process clearance (s.8.2) and any reopening of mobile transfer submission are held until closure passes on every path. This protects recovery from the same credential.
- The external support is verified: R03 6.2.13(b), PDF p.14, "all passwords are promptly changed if they have been or are suspected of being compromised"; and R11 p.5, "Removing the access rights of users suspected to have committed or contributed to the data breach".

**Final action and condition:** K1–K9 exactly as written.
- If the K4 closure test fails on any path, that path stays open: K3 is repeated and I am phoned at once.
- A directory-wide reset comes to me as a decision.

**Accountable owner:**
- SEC decides.
- Execution: identity, privileged-access, network and application administrators, under emergency change. The custodian witnesses.
- The vendor relationship owner handles K8.
- Reinstatement is my decision, on SEC's written sign-off.

**HKT time, deadline or trigger:**

| Step | Time |
|---|---|
| Capture | 12:10 |
| Terminate and revoke | 12:15 |
| Closure test on each path | 12:30 |
| Secret rotation | 14:00 |
| Persistence sweep | 16:00 |
| Detection | continuous; any successful use re-contains and extends the window |

**Recipient and channel:**
- The identity provider, single sign-on, VPN, privileged-access system, application servers and perimeter.
- The vendor by call-back to a number on file, never over the vendor's own path.
- Decision log and emergency change record. Each change to the critical computer system is logged for the Cap. 653 s.22 register.

**Final external basis:**
- SEC Q07b, "BASIS: EXTERNAL" items 1–7, adopted. I verified R03 6.2.13(b), R11 p.5, R16a p.4 ("Change login details for the compromised device / software / database / system") and R02 Annex F D.1, p.45 ("Compromised accounts have been removed or isolated", which may be ticked only after K4 passes).
- SEC's "no direct rule located" record for token replay is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.7.2–7.5, s.3 (vendor-reinstatement row), s.6.2, s.8.2 and s.9.3.
- No conflict found.

**Dispatch instruction:**
- EXECUTE NOW: K1–K3.
- SCHEDULE: K4 at 12:30, K5 at 14:00, K6 at 16:00. K7 runs continuously.
- HOLD: vendor reinstatement, alternate-process clearance and clearance to reopen mobile transfer submission, until K4 passes on every path.

==================================================================
**UNIT C03-Q08a: notifying the Privacy Commissioner (PCPD)**

**Original answer reference:** sealed LC answer for C03, "UNIT Q08a".

**Decision:** OVERRIDE (timing only; LC's content, status wording and channels are kept).

**Reason**
- LC set a target of 15:00. Its own basis, R16a p.1, says the form "may take about 10-15 minutes to complete", and the core facts reach LC by 12:15.
- The bank goes public with the exposure at 13:00 (Q09b) and starts calling the 80 at the same time (Q09a).
- R11 p.6 says to notify the PCPD "as soon as practicable after becoming aware of the data breach, particularly if the data breach is likely to result in a real risk of harm". Here the 13:00 public disclosure is what makes the earlier time practicable and appropriate. The PCPD should not first learn of a confirmed HKID exposure from the bank's public statement or the media (professional judgment).
- Filing first also lets the 13:00 update carry the PCPD line truthfully (COM S2).
- Changing the target time is a material change, so this is an OVERRIDE.

**Final action and condition:**
- **What is filed:** a voluntary initial notification on the PCPD Data Breach Notification Form, with the content, labels and exclusions exactly as in LC Q08a: no claim of a statutory filing; no admission about DPP4; no customer data attached; no mention of any Cap. 455 disclosure.
- **Field fills:**
  - "Number of individuals affected": 80 confirmed, plus any screenshot-only matches SEC confirms by 12:30. The narrative says up to 18,000 records are held in the workspace and that their export is unverified.
  - "Media statement": "Intend to issue" (13:00).
  - "Other authorities": only bodies logged in the Regulator Contact Register (RCR) as notified.
- **Updates go in at once** on any of: a wider group; completion of customer notification; publication of the data; the final scope.

**Accountable owner:**
- LC is accountable and signs.
- The DPO prepares the form.
- SEC confirms the facts in parallel. No internal approval holds the filing (PH01 s.2.4).
- I am informed.

**HKT time, deadline or trigger:**
- Target: filed by 12:55.
- Latest: 14:00. The standard is "as soon as practicable".
- If the form is not filed by 13:00, the public update omits the PCPD line, and filing goes ahead without further delay.

**Recipient and channel:**
- To the Office of the Privacy Commissioner for Personal Data.
- By fax to 2877 7026, or by hand to Room 1303, 13/F, Dah Sing Financial Centre (R16a p.3).
- Email to dbn@pcpd.org.hk only if SEC has logged corporate email safe. A call alone does not count as notification (R11 p.8, "Oral notifications are not accepted").
- The fax confirmation or hand-delivery receipt is saved under PH01 s.5.5.

**Final external basis:**
- LC Q08a "Basis: external", adopted: R10 DPP4(1)–(2), p.169 (verified; 0 hits for "data breach"); R16a pp.1 and 3 (verified: "Although it is not mandatory under the Ordinance ... data users are encouraged to give such notifications timely"); R11 pp.1, 5, 6, 8 (verified); R16b p.3 (verified: "the AI concerned should seriously consider doing so").
- New point for the timing: R11 p.6, Step 4 (quoted above), and R16a p.1 (the form takes 10–15 minutes).

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.5.1, s.5.2, s.2.4, s.5.5 and s.5.7.
- s.1.4: internal times never extend an external deadline.
- No conflict found.

**Dispatch instruction:**
- EXECUTE NOW: DPO prepares the form, LC signs, and it is faxed or hand-delivered by 12:55.
- It depends only on SEC's 12:15 facts. Unverified items are marked as unverified.

==================================================================
**UNIT C03-Q08b: who is notified now, and what widens the group**

**Original answer reference:** sealed LC answer for C03, "UNIT Q08b".

**Decision:** OVERRIDE (timing; group and widening triggers are kept).

**Reason**
LC's group is right and is kept:
- the 80 whose export is confirmed;
- plus anyone matched from the attacker's screenshot who is not among the 80;
- the rest of the store is not notified yet, with the reasons logged;
- widening triggers (i)–(v) are based on evidence and risk, as PH01 s.10.4(c) requires.

Two timing changes:
1. **Delivery timing.** LC proposed approval at 13:00, clearance at 13:30, first contact at 14:00 and all first attempts by 18:00. COM's Q09a timing is earlier and is feasible: approval 12:30, clearance 12:50, first calls 13:00, all first attempts by 16:00. R16b p.3 expects notice "as soon as practicable" where the data is sensitive. The attacker's 02:00 deadline makes publication, and scam calls to these numbers, a real risk. So the earlier timing governs.
2. **Scope review timing.** I bring the review forward from 24:00 to 21:00 (decision by 22:00). If the scope must widen, the notices and public line can then start before the 02:00 deadline rather than after it. The 24:00 limit in s.10.4(b) remains the outer limit.

**Final action and condition:**
1. **Notify now: batch C03-B1.**
   - The 80, plus a sub-batch B1a: any screenshot-matched individual outside the 80.
   - SEC confirms the B1a list from verified copies by 12:30. If SEC has not confirmed by 12:30, B1 goes as the 80 alone and B1a follows as soon as SEC confirms. B1 is never held for B1a.
2. **Not individually notified yet:** the remaining workspace records. LC logs the reasons, because R16b p.2 says an AI that does not notify "should provide justification". The group is covered by the public statement (my s.10.4(d) decision under Q09b).
3. **Scope review.** The DPO and LC review at 21:00 using SEC's 20:00 package. I log my decision and reasons by 22:00; the limit is 24:00. After that, the group is reviewed on any new evidence and at least every 24 hours.
4. **Widening rule.** LC's triggers (i)–(v) are adopted as the decision rule. Under (v), if SEC cannot bound the export because of log gaps, I widen to every record that session could reach.
5. **Fraud controls.** By 12:50 the Head of Fraud applies enhanced fraud monitoring and stronger caller-identity checks to the B1 accounts (LC's recommendation, which I approve).

**Accountable owner:**
- I approve the audience and decide the scope.
- LC and the DPO co-lead the review; LC clears the text.
- SEC confirms the lists.
- COM sends.
- Fraud applies the account controls.

**HKT time, deadline or trigger:**

| Step | Time |
|---|---|
| B1a list | 12:30 |
| Audience approval | 12:30 |
| Text clearance | 12:50 |
| First calls | 13:00 |
| All first attempts | 16:00 |
| Letters with the courier | 17:00 |
| Scope review | 21:00 |
| Decision logged | 22:00 (limit 24:00) |
| Re-review | at once on any widening trigger, including publication after 02:00 |

**Recipient and channel:** the affected individuals through the Q09a channels; the decision log.

**Final external basis:**
- LC Q08b "Basis: external", adopted:
  - R16b p.3 (verified: notify affected customers "as soon as practicable" where data "is sensitive"; justification needed if not);
  - R11 pp.6–8 (verified);
  - R05 p.1 "Customer notifications" (scan-checked in C01).
- For the earlier review time: no direct rule located in assigned sources sets a time for a scope review before an attacker's deadline. Searches across all files for "notif", "data subjects", "ransom" and "extortion" found only R11, R16a, R16b and PH01, which say "as soon as practicable" or give 12 hours.
- Professional judgment: deciding scope before the 02:00 deadline lets the bank reach people before any publication.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.10.4(a), "not held back for the wider review"; s.10.4(b), "No later than 12 hours"; s.10.4(c) and (d); s.10.5; s.13.5; s.3 (audience row).
- No conflict found.

**Dispatch instruction:**
- EXECUTE NOW for B1, through Q09a. It depends on the 12:50 text clearance.
- SCHEDULE: the review at 21:00.
- HOLD individual notice to the remaining records, pending the review or a trigger.

==================================================================
**UNIT C03-Q09a: core message and channel for the directly notified group**

**Original answer reference:** sealed COM answer for C03, "Q09 a". This includes COM's independent recommendation to send now.

**Decision:** OVERRIDE (audience widened conditionally; one wording rule; the rest kept).

**Reason**
I adopt COM's recommendation to send now, and its channels:
- a call from a named team, with a call-back offer;
- an SMS alert with no link after an unanswered call;
- a courier letter to all of the group;
- the secure inbox only if SEC logs it trusted.

These are permitted by PH01 s.10.2. They suit an exposure involving phone numbers before a 02:00 deadline, and they give R11 p.8's "directly by phone, in writing".

Two changes:
1. **Audience.** COM's audience was the 80 only. LC (Q08b) correctly adds screenshot-matched individuals outside the 80 (B1a), whose data the attacker demonstrably holds.
2. **"We have contained the incident".** The draft says this, but SEC Q07b logs the access window as open until the 12:30 closure test passes. COM's N3 default would simply delete the line. I set an accurate alternative instead.

Changing the audience is material, so this is an OVERRIDE.

**Final action and condition:**
- **Audience.** I approve batch C03-B1 (the 80 plus B1a) at the 12:30 CMT, after consulting LC, SEC and the DPO (PH01 s.3). The send recommendation is accepted.
- **Text.** COM's master letter, call script and SMS, with one change to "What we have done":
  - if SEC logs that K4 passed on every path by 12:50: "We have stopped the unauthorised access we identified and are investigating with specialists";
  - otherwise: "We have taken steps to block the unauthorised access and are investigating with specialists".
  - "We have added extra checks..." is included once the Head of Fraud logs that the checks are in place.
  - The bodies notified are named only once they are logged.
- **Conditions N1–N6 as written.** N2, LC clearance at 12:50, defaults to hold and escalate to me; I am in the CMT. On N6, any Police request to delay is decided by LC and me, and no delay is to run past 02:00.
- **Data handling.** Bilingual, using each customer's language preference on record. No HKID numbers in any notice. Notifiers work from the minimum extract, which is erased afterwards (PH01 s.17.2).
- **Delivery register.** Batch C03-B1 is logged per customer (PH01 s.10.3).

**Accountable owner:**
- COM drafts and sends.
- I approve the audience and sign the letter.
- LC clears the text. SEC, Operations and Fraud confirm the facts.
- Execution: the named notification team, Fraud (contact-detail checks), Operations (SMS) and the courier.

**HKT time, deadline or trigger:**

| Step | Time |
|---|---|
| Audience approval | 12:30 |
| Clearance and fact-check | 12:50 |
| Calls start | 13:00 |
| Fraud contact-detail check | 13:30 per customer |
| First attempt to all, plus SMS to those not reached | 16:00 |
| Letters with the courier | 17:00 |
| Second call attempt | 20:00 |
| Register summary to LC | 22:00 |
| Target: evidenced contact with all of B1 | before 02:00 |
| Anyone not reached gets a relationship-manager or branch visit | 17 Nov |

**Recipient and channel:** the B1 individuals:
- a personal call showing the bank's main hotline number;
- an SMS with no link;
- a courier letter to the address in verified records;
- the secure inbox only if trusted.
- No email.

**Final external basis:**
- COM Q09a "Basis: external", adopted: R11 pp.5, 7, 8 (verified); R16b pp.2–3 (verified); R05 p.1; R16a p.3; R10 search record.
- For the wording change: R11 p.7 (verified), a notice may include "A description of the measures taken or to be taken to mitigate the loss or to prevent further unauthorised access". The description must be accurate. PH01 s.7.4 (an open window until closure) is the internal fact source.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.10.1, s.10.2, s.10.3, s.10.4(a), s.10.5, s.13.3–13.5, s.3, s.17.2 and s.7.4.
- COM's letter-default point is resolved within s.10.2. No conflict with external requirements.

**Dispatch instruction:**
- SCHEDULE calls at 13:00.
- Dependencies: audience approval at 12:30; LC clearance and SEC/Fraud fact-check at 12:50; for each customer, Fraud's check of any changed contact details.
- B1a follows SEC's list confirmation.

==================================================================
**UNIT C03-Q09b: public statement on verified exposure and the unverified wider claim**

**Original answer reference:** sealed COM answer for C03, "Q09 b".

**Decision:** CONFIRM.

**Reason**
- **Verified exposure stated.** The 13:00 update states the verified exposure (80; names, HKID numbers, phone numbers) once SEC confirms it from the record (PH01 s.11.4, S1).
- **Wider claim described accurately.** It is called unverified and under urgent checking, without asserting or ruling out exposure. This matches LC's legal view in Q08b.
- **18,000 figure withheld.** It is a store size, not a confirmed count (PH01 s.10.4(c), s.11.4). It is re-decided at 19:00 with SEC's 15:00 exact population.
- **Data lines follow the calls.** They go only once calls to the group have started (S4), so customers hear from the bank first.
- **Fixed lines and cadence.** The fixed lines (PH01 s.11.3) and the next update by 19:00 (within s.11.2) are kept.
- **My PH01 s.10.4(d) decision.** I select COM's recommended branch: this public statement covers the customers not notified individually, giving every customer protective advice, until the 21:00 review. This is a branch COM stated explicitly, kept as written.
- **Consistency with C02.** The draft does not confirm the demand or its details and never denies a demand. That keeps my C02 stance, because no Police view has been logged.
- **PCPD line.** It can now be included if the Q08a filing is logged by 13:00.

**Final action and condition:**
- COM's draft 13:00 update and release conditions S1–S4, exactly as written.
- The reactive line on the size of the location is as written.
- Immediate-update triggers are as written.

**Accountable owner:**
- I approve and am the spokesperson; the COO is the alternate after 15 minutes.
- LC clears. SEC and Operations fact-check.
- COM executes.

**HKT time, deadline or trigger:**
- 13:00, together with the first calls. Data lines no later than 14:00.
- Next update by 19:00.
- Immediate update on: evidence of a wider export, publication or offer of the data (including after 02:00), reported misuse, or my widening decision.

**Recipient and channel:**
- Public: the website status page, press release, official social media, the app banner (if trusted), branch notices and IVR.
- Staff: script v3.
- HKMA: copy from COM to LC to the HKMA at release (PH01 s.5.8).
- R16a: the form's media-statement field is updated.

**Final external basis:** COM Q09b "Basis", adopted: R16b p.3 (verified); R11 p.8 (verified: "if public interest exists, then public announcements ... may be more effective"); R09 s.8.2.2; R05 p.2 (scan-checked); R16a p.3 (verified). COM's "no direct rule located" record on publishing the size of a data store is adopted.

**Final internal basis:** Internal bank procedure, PH01 v1.0:
- s.10.4(c)–(d), s.11.2–11.4 and s.5.8.
- No conflict found.

**Dispatch instruction:**
- SCHEDULE for 13:00.
- Dependencies: S1 (SEC, 12:45), S2 (LC logs, 12:50), S3 (CEO and CFO re-verify, 12:50) and S4 (calls started).
- The service lines are never held. If S4 slips, only the data lines wait, to 14:00 at the latest.

==================================================================
**CROSS-ROLE CONFLICT RESOLUTION**
1. **Notification timing (LC Q08b vs COM Q09a).** COM's earlier timing is adopted. LC's group definition is kept.
2. **Notification audience (COM Q09a vs LC Q08b).** LC's screenshot-match addition (B1a) is adopted, and it never holds the 80.
3. **PCPD timing (LC 15:00 vs COM's S2 line at 13:00).** Filing is moved to 12:55, so the line can be truthful.
4. **Containment wording (COM's letter vs SEC's open window).** The wording now depends on the K4 closure-test result.

**ORDER OF DEPENDENT ACTIONS (HKT)**
1. **12:00–12:15.** SEC logs the confirmation time and the open window. Session and token capture (K2) is followed by revocation (K3). Confirmed facts go to LC, the DPO and me.
2. **12:15–12:30, in parallel:**
   - the DPO prepares the PCPD form;
   - LC updates the HKMA by phone ("at once" under PH01 s.5.8; never held);
   - SEC confirms the B1/B1a lists;
   - SEC runs the workspace containment check and the closure test (K4).
3. **12:30 CMT.** I approve the B1 audience. Fraud starts contact-detail checks and the account controls.
4. **By 12:45.**
   - LC updates the Police under the existing case and logs any specific Police request (N6).
   - SEC confirms the S1 figure.
5. **12:50.**
   - LC clears the letter, script and public update.
   - The containment wording is fixed from the K4 result.
   - The CFO and I re-verify S3.
6. **12:55.** PCPD form filed and receipt saved. This needs step 1 only.
7. **13:00.**
   - Calls start (Q09a).
   - The public update follows, with data lines once calls have started (Q09b).
   - At release, a copy goes from COM to LC to the HKMA.
   - Staff script v3 is issued.
   - I phone the Board chair (limit 14:00).
8. **13:00–17:00.**
   - SEC fixes the window (13:00) and rotates secrets (14:00).
   - Population count and preliminary scope at 15:00, followed by supplementary information to the PCPD, HKMA and Commissioner if the facts change (PH01 s.5.9).
   - All first attempts and SMS alerts by 16:00; persistence sweep at 16:00.
   - Letters with the courier by 17:00.
   - LC sends supplementary information to the Commissioner today.
9. **19:00–22:00.**
   - Public update at 19:00, where I re-decide the record figure.
   - SEC's scope package at 20:00, then the second call attempt.
   - DPO and LC review at 21:00.
   - My scope decision at 22:00, followed by any widened notices and public update.
   - LC's posture note (from C02) at 22:00.
10. **02:00 Tue 17 Nov.** If data is published or offered at the attacker's deadline: immediate re-review, widened notices, a public update, and PCPD and HKMA updates.
11. **Standing holds.**
    - Vendor reinstatement, alternate-process clearance and reopening of mobile transfer submission stay held until K4 passes on every path (Q07b K9).
    - Any widened individual notice waits for my logged scope decision or a widening trigger.

No files were created.