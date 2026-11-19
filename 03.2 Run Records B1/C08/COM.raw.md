## COM submission for C08: Thursday 19 November 2026, 08:00 HKT (H+72)

I locked this before seeing colleagues' answers. All actions are simulated, for the facilitator to log.

**Status taken from the facilitator record**
- **Recovered system:** on HOLD, unchanged.
- **Alternate process:** status cannot be verified.
- **Last recorded public update:** 07:00 on 18 Nov.
  - PH01 s.11.2 requires an update at least every six hours between 07:00 and 22:00 while a critical operation is disrupted. That means updates were due by 13:00 and 19:00 on 18 Nov. Neither is recorded.
  - The content of several earlier updates cannot be verified either. The full list is in the handoff.
- **Second offline test:** reconciled all 240 sampled instructions, in a rebuilt access environment, with no new alarms in six hours. These results describe the test environment only.

---

## Q24 a. Closing update or continued updates

### Decision
Do **not** publish a closing update. Publish a self-contained update at 09:00 HKT and keep to the regular schedule after that: 13:00 and 19:00 today, then at least every six hours between 07:00 and 22:00, plus an immediate update on any change of service. This continues until every closing condition in PH01 s.11.5 is evidenced. The exercise window closing does not change this.

**Closing conditions in PH01 s.11.5, checked at 08:00:**
| Condition | Position |
|---|---|
| Service running in production and stable | **Not met:** the recovered system is on HOLD |
| Queued instructions settled or returned | **Not evidenced** |
| Register shows evidenced delivery to all affected customers | **Not evidenced:** no delivery figures are recorded |
| Every open case has a named owner | Owners assigned in simulation; case outcomes not recorded |
| LC confirms the regulators have been told | **Not recorded** |

**The 240/240 result.** PH01 s.9.2 says "A sample result is recorded as a sample, not as a pass of the whole set." So the update must not suggest the system is restored or ready.

### Actions (HKT)
| Time | Action |
|---|---|
| 08:05 | COM checks the website archive and every channel. If the 13:00 and 19:00 updates of 18 Nov were not published, they are logged as **not evidenced**, LC is told (PH01 ss.1.3 and 5.8), and the 09:00 update includes an apology line. |
| 08:30 | CEO approves (COO if the CEO is unreachable for 15 minutes) |
| 08:45 | LC clears in a fixed slot, with the second LC officer as backup. SEC and Operations fact-check. |
| 09:00 | Publish on the website status page, press release, official social media (text only), app banner (if trusted), IVR, branch notices and staff scripts |
| 09:00 | COM sends a copy to LC at release; LC forwards it to the HKMA and asks for a receipt (R05 p.3; PH01 s.5.5) |

### Conditions (PH01 s.2.3)
| ID | Line | Verifier | Latest time | Default if not met |
|---|---|---|---|---|
| W1 | Production position (stays HOLD unless the CEO logs a gate pass under PH01 s.9.3) | CEO's decision log | 08:45 | Version H3 |
| W2 | Alternate-process status | Head of Payments Operations | 08:45 | "Queued payments remain on hold" |
| W3 | Data and case lines | SEC, COM register, Fraud | 08:45 | Any unconfirmed line is removed |
| W4 | "Has not paid a ransom" | CEO and CFO re-verify | 08:45 | Line omitted. The previous ransom decision was never supplied to me. |
| W5 | LC clearance | LC | 09:00 | The CEO directs a minimum update containing only facts SEC and Operations have verified, with LC's review running alongside. COM records the conflict under PH01 s.1.3: a hold with no time limit would extend the lapse in updates. |

### Version H3: hold continues (default)
> "Lan Tidal Bank service update – 19 November 2026, 09:00 HKT.
>
> [If confirmed not published: We are sorry we did not publish updates at our usual times yesterday afternoon and evening.]
>
> **Payments.** Outgoing local transfers, payroll submission and mobile transfer submission are still not available through our main system. [W2: queued payments are being processed through our alternative process / remain on hold.] Each payment will be made only once. Please do not resubmit.
>
> **Recovery.** We have rebuilt the system and completed further offline tests. The latest test found no differences in the payments checked and no new security alerts in the test environment. These are test results. Before we use the rebuilt system for real payments, it must pass all our remaining checks. If it does, we will restart in stages, starting with a small batch, and tell you at each stage. We cannot yet give a date for full service.
>
> **Customer information.** We have been contacting each of the 320 customers whose information was published. If you think you are one of them and have not heard from us, call the number on the back of your card. The claim that more information was taken has not been verified.
>
> **Scams.** If you think you have been scammed, call the number on the back of your card at any time. We will open a case, give you a reference and tell you when to expect a decision. We never ask you to verify your account through links, QR codes or social media, or ask for passwords, PINs or one-time passwords.
>
> **Fees and losses.** Fees caused by the disruption are waived. Documented direct losses, such as late-payment charges from a missed payroll cut-off, can be claimed with a case reference.
>
> [W4: The bank has not paid a ransom.]
>
> Next update by 13:00 HKT today."

### Version P: production pilot
Usable only if the CEO logs a gate pass under PH01 s.9.3.
> "We have started a first batch of up to 20 payments through the rebuilt system. We will extend in stages only if each stage runs without any unexplained difference. Other payments [continue through our alternative process / remain on hold]."

### Closing update
A template is prepared but not released. It is used only when every PH01 s.11.5 condition is evidenced and the CEO approves.

### Basis
- **Internal bank procedure (PH01, v1.0):**
  - **s.11.5:** "A closing update is issued only when: the service runs in production and SEC confirms it is stable; queued instructions are settled or returned; the notification register shows evidenced delivery to all affected customers; every open case has a named owner; and LC confirms the regulators have been told. Until then updates continue."
  - **s.11.2:** the cadence.
  - **s.9.2:** the rule on sample results.
  - **s.11.4:** figures only from a confirmed record.
- **External:**
  - **R09 s.8.2.2, p.33:** "consistent and up-to-date messages ... on a timely basis".
  - **R05 p.3** (checked against the scan): "The HKMA should be kept informed during the process and copies of public communication materials should be submitted to the HKMA".
  - **R07 s.1.3.3, p.5:** the HKMA "should also receive periodic progress reports upon being notified until the final resolution of the crisis". This is for LC, and it supports continuing.
  - **R06 s.8.3, p.13:** "Communication, where appropriate, should take place during the incident ... and after".
- **Conflict check:** no conflict with an external requirement. A closing update now would be inaccurate and would breach PH01 s.11.5.

---

## Q24 b. Handing off unresolved customer cases and follow-up messaging

### Decision
Hand over item by item, under PH01 s.18.
- **10:00–11:00:** handover meeting.
- **12:00:** signed acceptances due.
- **The pack opens with a "Not evidenced" page** (PH01 s.18.2). Every item that has no evidence passes as **open**, not done.
- **Unsigned items:** COM keeps any communications item whose receiving owner has not signed, and the CMT does not stand down for that item (PH01s.18.1).
- **Restrictions stay in force:** no links, the callback rule, approvals under PH01 s.3, and no closing update until s.11.5 is met (PH01 s.18.3).

### Handover list
| # | Item | Status at 08:00 | Receiving owner (by role) | Next action and due time | Trigger |
|---|---|---|---|---|---|
| 1 | Notification register, all 320 customers | Delivery not evidenced; class sizes not recorded; visits scheduled for 19 Nov | Head of Customer Service. COM keeps the wording. | Rebuild rows from evidence; visit anyone not reached today; figures to LC daily (PH01 s.10.3) | A row closes only on evidenced delivery |
| 2 | Corrections for the 12 and the misdirection assessment | Outcome not recorded | DPO and LC | Assessment result by 19 Nov 18:00 | Finding a further incident: notify under R11 and R16b |
| 3 | Scope of the rest of the workspace | Decisions not recorded | DPO and LC; CEO decides | Review at least every 24 hours and on new evidence (PH01 s.10.4(d)); a reason is logged for each customer not notified (R16b p.2) | New evidence of export, publication or misuse: widen and notify. COM templates are ready. |
| 4 | Case register (the 31 and any others) | Owners assigned; outcomes, acknowledgements and first updates not recorded | Head of Fraud (A–D); Head of Payments Operations (E); CEO (F and anything above HKD 50,000); CFO (running total) | Confirm acknowledgements and decision dates today (PH01 s.13.7); a named owner on every case (PH01 s.11.5) | Total reaching HKD 2.5m or 4m: tell the CEO. Above HKD 5m: the Board approves first. |
| 5 | Results of the cross-match of the 31 | Not recorded | Fraud with the DPO | Report today | Any match outside the 320 goes to item 3 |
| 6 | Identity-protection monitoring enrolment (PH01 s.13.5) | Not recorded | DPO and Customer Service | Track who has opted in; remind once, in the next consolidated contact | |
| 7 | Public updates and closing template | Updates of 18 Nov 13:00 and 19:00 not evidenced | COM standing duty manager; CEO approves | Updates at 13:00 and 19:00, then the PH01 s.11.2 cadence | Closing only once s.11.5 is evidenced |
| 8 | Counterparty updates (PH01 s.14.3) | Not recorded | Head of Payments Operations; COM keeps the wording | 08:00, 13:00 and 18:00 until settled or returned | |
| 9 | Staff scripts | v7 clearance not recorded; interim instruction in use | COM standing team; LC clears | Clear and issue v8 today | |
| 10 | Media and social media log; impersonation and takedown status; spokesperson | Takedown outcome not recorded | COM standing team (CEO remains the only spokesperson) | Monitor daily | New fake pages: warning under R09 s.4.3.2 |
| 11 | Payroll-delay confirmation letters for SMEs | Not recorded | Relationship-manager heads; LC clears the wording | Offer on request | |
| 12 | Communications log for LC's reports (media dates for Annex F Part E; media-statement status for the PCPD form; HKMA copies and receipts) | Receipts not verified | LC, with COM supplying the log | Hand the log over today | |

### Follow-up messaging after handover (standing rules)
- **Approvals:**
  - The CEO approves the audience for customer notices; LC clears the text; SEC and Operations check the facts (PH01 s.10.1).
  - The CEO approves public updates.
- **Channels:** call with a call-back offer, courier letter, and SMS (no link) only for customers not reached by phone. Secure inbox only if trusted; no email; no HKID numbers.
- **One message per customer:**
  - A customer with evidenced delivery gets nothing more until there is something new.
  - A customer with no evidence gets one consolidated notice (PH01 s.10.6).
  - Customers with open cases hear through their case owner.
- **Planned triggers for new messages:**
  - A production restart: a payment-status notice to customers with queued instructions.
  - A case decision.
  - A change of data scope.
  - New scam patterns.
  - The closing update.

### Basis
- **Internal bank procedure (PH01, v1.0):**
  - **s.18.1:** "The CMT hands over to standing teams only when each open item has a named receiving owner who has signed acceptance of a specific list."
  - **s.18.2:** "Each handover pack starts with a page listing what is not evidenced. Items without evidence transfer as open, not done."
  - **s.18.3:** "Restrictions stay in force after handover until their release condition is met".
  - **s.10.3:** "Approval and scheduling are not delivery."
  - **s.10.4(d), s.10.6, s.13.7** (customers are told when to expect a decision), **s.11.5**.
- **External:**
  - **R11 p.6, "Step 5":** "A comprehensive record of the incident is therefore required, which should include all facts relating to the breach".
  - **R11 p.8:** "After the full details of the incident are revealed, all information should be submitted to the PCPD ... without delay". This is for LC; COM's registers feed it.
  - **R16b p.2:** if the bank does not notify affected customers, "it should provide justification".
  - **R09 s.4.4.2:** the 24/7 help channel remains available.
  - **R02 s.7.2.3(a)(v)(4)–(5), p.32:** "Recording the incident response process ... Conducting a post-incident review". General principle.
- **Conflict check:** no conflict.

### No direct rule located in assigned sources
- No external document sets how a bank closes its public incident updates or hands over communications. I relied on PH01 ss.11.5 and 18, and on my professional judgment.
- I re-read PH01 ss.9, 11 and 18, R07 p.5, R06 p.13 and R11 pp.6–8.

### Lessons for the post-incident review
These come from my own decisions:
1. **The C01 default.** "Hold and escalate" for LC clearance left the 09:00 statement, the C03 B1 notices and script v7 unverifiable. From C05 onward I set fixed clearance slots with a minimum-notice default.
2. **Logging.** Releases need to be logged per channel with screenshots or receipts. Several statements cannot now be verified.
3. **Cadence.** Update times after a handoff need a named owner. The 18 Nov 13:00 and 19:00 updates are not evidenced.