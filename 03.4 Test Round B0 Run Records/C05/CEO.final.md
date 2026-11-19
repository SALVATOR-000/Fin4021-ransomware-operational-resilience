C05 is decided: all six units are CONFIRM. Nothing in the three answers had to change; the only additions are reasons and instructions to other owners. CEO final record for Tue 17 Nov 2026, 08:00 HKT (H+24). All actions are simulated, for the facilitator to log.

**What I checked myself:**
- R09 PDF p.17, s.4.3.2 (fake websites): "Whenever AIs become aware of fake or suspicious emails, websites, Apps…" and "make attempts to remove the fake or suspicious items where practicable".
- R10 s.58(1)(a), PDF p.117: "the prevention or detection of crime".
- PH01 v1.0, read at earlier cards.
- Other citations are as they appear in the sealed answers.

**Handoffs I rely on:**
- No ransom payment, no preparatory step and no contact with the attacker are recorded. No commitment to the attacker exists.
- The Police report was made, but the Police's view, the case reference and any s.25A response are not verified.
- None of the HKMA, Commissioner or insurer receipts is verified.
- The 80 customers' notices were approved, but dispatch is not verified.
- The Group B scope decision is not verified.

COM said it did not receive the ransom record. The LC handoff now supplies it, so I pass the record to COM through LC. LC confirms to COM at 08:15 that "no payment has been made" is a verified present fact (PH01 s.11.3).

**Points that cut across roles, resolved:**
1. **Tolerance and the Board.** The 24-hour tolerance for transfers and payroll was reached at 08:00.
   - I convene the Board or Risk Committee now, to meet by 20:00 HKT (PH01 s.4.3; s.15.2, "within 12 hours"). The Board paper is prepared under s.15.3.
   - The Board may narrow the recovery scope, for example to payroll first. Any narrowed scope still has to pass every applicable 9.3 check (SEC Q13b).
2. **Group B, about 17,920 others in the workspace.**
   - Publication of 320 matched records is new evidence. It triggers a review under PH01 s.10.4(c)–(d) now ("whenever new evidence arrives").
   - The DPO and LC review with SEC's evidence on whether the mirrored set came from the same workspace, by 14:00. I decide and log the result.
   - COM's Group B notice stays ready, to go within 4 hours of a decision to widen.
3. **Related regulator filings.** These are coordination items that support Q14 and Q15 and change no unit. All are LC's:
   - HKMA update at once on the publication and the fake page, by 08:30 (s.5.8). A second report immediately after COM's scam press release (R09 fn.12).
   - PCPD "update of a previous notification", raising 80 to 320 confirmed (R16a p.2), by 12:00.
   - Supplementary information to the Commissioner through the secure channel, today.
4. **Fake page indicators.** SEC captures them passively (PH01 s.6.6) and supplies them to LC (Police), COM (no-link wording) and Fraud. SEC requests the platform takedown.

---
**Q13a | Original: SEC sealed answer, Q13a | CONFIRM**
- **Reason:**
  - It follows PH01 s.9.1: candidate 1 is a new build from trusted media, using data from the immutable backup, in an isolated recovery environment. The standby system is tested only if candidate 1 fails. Nothing is repaired in place.
  - Separation is proven before any data is loaded: reachability tests, no shared identities, newly issued keys, no vendor access (s.7.5).
  - The backup is checked against the attacker's dwell period, its lock and audit logs, and a read-only scan of a hashed working copy. Executable content is never restored from the backup.
  - Test data follows PH01 s.9.2 and R08 s.4.2.4 (de-sensitised, information owner approval).
- **Final action:** as in SEC Q13a, items 1 to 5.
- **Owner:** SEC, accountable for verification and sign-off. The Head of IT Operations builds. The payments information owner approves test data. The evidence custodian handles the backup copy.
- **Time:**
  - Environment build from 08:30.
  - Separation result by 12:00.
  - Backup timing and integrity result by 14:00.
  - Status in each SEC report.
  - These are targets. Missing one never releases a check (s.2.3).
- **Recipient and channel:** recovery test record, change record, evidence register, decision log; briefing to me and the Head of Payments Operations; results go into the Board paper.
- **External basis:** SEC Q13a "Basis: external" (R02 s.6.2.20(c); R03 ss.6.2.20(b)(i), 6.2.22(c); R08 s.4.2.4; R14b s.B.6).
- **Missing fact:** whether this backup is the secure tertiary data backup (STDB), with the HKAB principles applied. The facilitator should confirm.
- **Internal basis:** SEC Q13a "Basis: internal" (PH01 v1.0 ss.9.1, 9.2, 6.1, 7.5). No conflict.
- **Dispatch:** EXECUTE NOW. Data load depends on the separation validation. Test-data use depends on the s.9.2 records.

**Q13b | Original: SEC sealed answer, Q13b | CONFIRM**
- **Reason:**
  - It applies the zero-tolerance pass mark in PH01 s.9.2. A sample result is never treated as a full pass.
  - Seven checks: baseline tie-out at the backup point; delta rebuild against the secondary-process register, so nothing is paid twice at cutover; duplicate and replay rejection; static data; message and key testing against a simulator only; total count and value tie-out; signed evidence.
  - The gate dependencies under s.9.3 and the stop triggers under s.9.5 are correctly identified.
  - It is consistent with R08 s.4.2.4 and s.4.3.1.
- **Final action:** as in SEC Q13b, checks 1 to 7.
  - Production use only after every 9.3 item is passed and logged, and only on my authorisation.
  - The rollback target is the secondary process only if it holds a current clearance under s.8.2 and its reconciliation ties. Otherwise releases are suspended.
  - The facilitator should confirm whether the secondary-process clearance from C04 was signed. No card records it.
- **Owner:** SEC for integrity sign-off. The Head of Payments Operations for reconciliation. I authorise production. The Board may narrow the scope.
- **Time:** offline result targeted for 20:00 HKT 17 Nov. It is never shortened to meet the target.
- **Recipient and channel:** recovery test record and decision log; the gate pack to me and the Board or Risk Committee.
- **External basis:** SEC Q13b "Basis: external" (R08 ss.4.2.4, 4.3.1; R07 s.4.3.2; R14b s.A.1).
- **Internal basis:** SEC Q13b "Basis: internal" (PH01 v1.0 ss.9.2–9.5, 8.6). No conflict.
- **Dispatch:** SCHEDULE. It runs once the Q13a data load is cleared. Production is on HOLD until the full s.9.3 gate is passed.

**Q14a | Original: LC sealed answer, Q14a | CONFIRM**
- **Reason:**
  - Keeping the no-payment posture is required: PH01 s.12.1 is Board policy.
  - The legal gates are still not cleared. There is no Police consent under R16c s.25A(2)(a) and no screening of the recipient under R16d s.8(a).
  - The new facts strengthen the case. The deadline has passed and the data has already been published, so paying would neither protect the data nor speed recovery.
  - There is nothing to unwind: no commitment is recorded. LC's written "nil-step" confirmations close the evidence gap.
- **Final action:**
  - Log "posture maintained, nil commitment" at 08:15.
  - Treasury hold reissued by 09:00. Any new or "discount" demand goes only to SEC and the evidence process, and is passed to the Police.
  - Written nil-step confirmations from Treasury, the CFO and the vendor relationship owner by 10:00. If any step is found, it is frozen and reported to me and the Board, and LC assesses it under s.25/25A.
  - The CFO obtains the insurer's position by 12:00.
  - I record the unchanged posture in the Board paper. No Board decision is sought.
- **Owner:** LC. The Board alone could depart from the posture. Treasury holds. The CFO handles the insurer.
- **Time:** 08:15, 09:00, 10:00, 12:00.
- **Recipient and channel:** decision log; Treasury in writing; Board paper.
- **External basis:** LC Q14a "External basis" (R16c ss.2, 25(1), 25A(2)(a); R16d s.8(a); sanctions search record).
- **Internal basis:** LC Q14a "Internal bank procedure" (PH01 v1.0 ss.12.1–12.3, 11.3). No conflict.
- **Dispatch:** EXECUTE NOW. The payment path stays on HOLD and has no trigger short of a Board decision.

**Q14b | Original: LC sealed answer, Q14b | CONFIRM**
- **Reason:**
  - It is a supplementary referral to the existing Police case. It covers the mirror and, as a separate cross-referenced matter, the fake page.
  - The fake page referral is required. R09 s.4.3.2, p.17: AIs should "report the matter to the Hong Kong Police Force".
  - The evidence pack is mostly free of personal data. Customer data goes only as a minimised set, under LC's and SEC's joint written approval, relying on PDPO s.58(1)–(2) (verified, p.117).
  - LC's reading that the s.16.1 signed-agreement rule does not apply to the Police, while the s.16.2 minimisation controls still do, is sound under s.1.3. The external requirement prevails, and LC logs the point.
- **Final action:**
  - Phone the Police CSTCB by 09:00, covering both the mirror and the fake page. Ask for the case reference, the Police's view and the s.25A status.
  - Written follow-up by 11:00.
  - Evidence pack handed over on bank-issued encrypted media, in person with the custody record, by 12:00 or at the time the Police set.
  - Open a data release record.
  - LC clears COM's wording for tipping-off (s.25A(5)).
- **Owner:** LC decides and reports. SEC prepares the evidence pack. LC and SEC jointly approve any data release. The DPO is consulted. I am informed.
- **Time:** 09:00, 11:00, 12:00.
- **Recipient and channel:** Police CSTCB by phone from the printed contact register, then in writing; evidence on encrypted media handed over in person.
- **External basis:** LC Q14b "External basis" (R16c s.25A(1), (3)(a), (5); R10 s.58; R11 p.4; R09 s.4.3 and fn.12).
- **Internal basis:** LC Q14b "Internal bank procedure" (PH01 v1.0 ss.3, 6.3, 6.6, 16.2, and the logged s.16.1 point). No conflict.
- **Dispatch:** EXECUTE NOW. Personal-data release depends on LC's and SEC's joint written approval.

**Q15a | Original: COM sealed answer, Q15a | CONFIRM (SEND)**
- **Reason:**
  - Publication makes all 320 confirmed-exposure customers. Under PH01 s.10.4(a) they are notified as soon as practicable.
  - None of the 80 has evidenced delivery (s.10.3, "Approval and scheduling are not delivery"). So the consolidated notice under s.10.6 goes to the 240 new customers and to those of the 80 without evidenced delivery.
  - Those of the 80 with evidenced delivery get a short supplementary notice, because publication is new content.
  - Channels are call plus letter, with no SMS. This is correct because the phone numbers are published.
  - Hard-to-reach customers are followed up on a risk basis (R09 s.4.2.3).
  - LC clearance is kept as a condition that does not lapse.
- **Decision as CEO:** I approve the audience of 320, split into batches C1, A-nd and A-d, at 08:45.
- **Final action:** as in COM Q15a.
  - Per-customer data fields are confirmed by SEC and the DPO before the letter text is final. Calls go ahead with the confirmed fields only.
  - The line about reports to authorities is included only for reports LC confirms, with receipts.
- **Owner:** I approve the audience. LC clears. SEC and the DPO confirm the list and fields. COM sends and keeps the delivery register. Fraud and the contact centre call. Operations sends letters.
- **Time:** approval and clearance 08:45; calls from 09:00; every customer attempted by 13:00; letters posted 17 Nov; register figures to LC by 18:00.
- **Recipient and channel:** the 320, by named-team call and then letter. Secure inbox only once SEC logs it trusted.
- **External basis:** COM Q15a "Basis (external)" (R16b p.3; R11 pp.6–8; R09 s.4.2.3).
- **Internal basis:** COM Q15a "Basis (internal)" (PH01 v1.0 ss.10.1–10.6, 13.5–13.6). No conflict.
- **Dispatch:** EXECUTE NOW after LC clearance at 08:45. If clearance is not logged, HOLD with escalation every 30 minutes, as COM set out.

**Q15b | Original: COM sealed answer, Q15b | CONFIRM**
- **Reason:**
  - R09 s.4.3.2 (verified, p.17) and fn.12 require a timely press release or equivalent, a Police report, an HKMA report immediately after the press release, and takedown attempts.
  - COM's warning carries no URL, account handle, screenshot or QR code, so it does not drive traffic to the page. It points to one safe route, the number on the customer's card.
  - The SMS carries no link (s.10.2).
  - The warning is never held for the data lines.
  - A go-ahead default is acceptable, because this is not a security, reconciliation or compliance condition (s.2.3).
- **Decision as CEO:** I approve at 08:45.
- **Final action:** as in COM Q15b.
  - Scam warning released by 09:15.
  - The status lines follow within 60 minutes. The 320 figure is published only if SEC confirms it. The 18,000 figure is not published.
  - No-link SMS to all customers except the 320 from 09:30.
  - Frontline Script v5 with a Fraud triage step.
  - Re-issue at once if new fake accounts appear.
  - The bank's own social media accounts are used only after SEC confirms the bank still controls them. If SEC has not confirmed by 09:15, the warning goes by the other channels.
- **Owner:** I approve (COO as alternate if I am unreachable for 15 minutes). LC clears. SEC checks the facts and requests takedown. COM releases. LC reports to the HKMA and the Police. Fraud monitors for customers who entered details.
- **Time:** 09:15 release; 09:30 SMS; next update by 14:00.
- **Recipient and channel:** the public and customers: press release by a non-email route, website if clean, verified social media, in-app banner with no link if trusted, IVR, branches, SMS. LC sends copies to the HKMA.
- **External basis:** COM Q15b "Basis (external)" (R09 s.4.3.2 and fn.12, verified; R05 p.3). COM's statement that no source governs how to avoid driving traffic to the page is accepted as professional judgment.
- **Internal basis:** COM Q15b "Basis (internal)" (PH01 v1.0 ss.10.2, 11.2–11.4, 3, 13.4). No conflict.
- **Dispatch:** EXECUTE NOW. The social-media channel depends on SEC's control check. The HKMA report follows immediately after the press release.

---
**Order of actions that depend on each other:**
1. 08:00–08:15:
   - I convene the Board or Risk Committee (tolerance at 100%).
   - LC logs the posture and nil commitment, and confirms "no payment" to COM.
   - SEC captures the mirror and fake page indicators passively.
2. By 08:30: LC updates the HKMA on the publication and the fake page. SEC begins the recovery environment build.
3. 08:45:
   - I approve the 320 audience and the scam warning.
   - LC clears both texts, including the tipping-off check.
   - SEC confirms the "320" figure and the data fields.
4. 09:00:
   - Police referral (needs SEC's indicators).
   - Treasury hold reissued.
   - Calls to the 320 begin.
5. 09:15: scam warning released. LC reports to the HKMA immediately afterwards. 09:30: SMS batch starts. Status lines follow by about 10:15.
6. 10:00: written nil-step confirmations.
7. 11:00: written Police follow-up.
8. 12:00:
   - Police evidence pack, after LC and SEC jointly approve any personal-data release.
   - PCPD update notification.
   - Insurer position.
   - Separation result for the recovery candidate. The data load depends on it.
9. 13:00: all 320 customers attempted.
10. 14:00:
    - Backup integrity result.
    - Group B scope review and my decision. If I widen the scope, the Group B notice goes within 4 hours, followed by PCPD, HKMA and public updates.
    - Public update.
11. By 20:00:
    - Offline reconciliation result.
    - Board or Risk Committee meets and may narrow the recovery scope.
    - Production only after the full s.9.3 gate and my authorisation.