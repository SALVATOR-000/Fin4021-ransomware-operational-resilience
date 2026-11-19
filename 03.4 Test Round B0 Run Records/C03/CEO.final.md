CEO final decision record for C03 (Mon 16 Nov 2026, 12:00 HKT, H+4). Five units are CONFIRM. Q08a is OVERRIDE, limited to two answers on the PCPD form. All actions are simulated, for the facilitator to log.

**What I checked myself:**
- PH01 v1.0, ss.2–18.
- R16a, PCPD Data Breach Notification Form (Revised 06/2023), PDF pp.1–3: the form fields and submission channels.
- R16b, PDF p.3.
- All other citations are taken unchanged from the sealed answers.

**Time of first confirmation of exposure.** I fix it at 12:00 HKT unless SEC logs an earlier analyst time by 12:15. All PH01 s.10.4(b) clocks run from the logged time. On 12:00, the scope review is due by 24:00 on 16 Nov.

**Conflicts across the roles, resolved:**
- **Audience approval:** COM asks for it by 12:45 and LC by 13:00. I approve at 12:45, which meets both.
- **Group B (up to about 17,920 other customers in the same workspace):**
  - LC holds individual notices for this group; COM does not publish the 18,000 figure. These are consistent.
  - As CMT chair I decide under PH01 s.10.4(d) that the 13:30 public statement covers Group B for now. s.10.4(d): "The CMT chair decides whether a public statement under section 11 covers customers not notified individually."

---
**Q07a | Original: SEC sealed answer, Q07a | CONFIRM**
- **Reason:** The tiered estimate (T1 = 80 confirmed export, T2 = evidence of access or staging, T3 = up to 18,000 reachable, T4 = other stores to be mapped) keeps confirmed facts and unverified claims apart, as PH01 s.10.4(c) requires. SEC treats log gaps as limits on narrowing the scope, not as findings that nothing was taken. The evidence that would raise or lower the estimate matches the s.10.4(c) factors. The 18,000 records are not extracted in bulk, which minimises handling.
- **Final action:**
  - Rebuild the timeline of every session that used the vendor credential, from its first use.
  - Run the volume, access, reach and coverage tests and reconcile with the vendor's records, as in SEC Q07a.
  - Notify me, LC and the DPO now that T1 = 80.
  - Report the tiers hourly.
  - Deliver a written scope paper by 20:00.
  - Escalate any increase at once.
- **Owner:** SEC. Executed by SEC analysts, with the forensic firm on masked data. The DPO is told of each tier change.
- **Time:** from 12:00; tier status in each hourly report; scope paper by 20:00; review deadline 24:00 (or the logged confirmation time plus 12 hours).
- **Recipient and channel:** evidence register and decision log; verbal briefing in the CMT room; paper or secure lab system, not corporate email.
- **External basis:** as in SEC Q07a, "Basis (external)" (R11 pp.4–5; R16b p.2; R02 s.7.2.3(a)(v)(3); R03 s.6.2.23(d)).
- **Internal basis:** as in SEC Q07a, "Basis (internal)" (PH01 v1.0 ss.10.4(b)–(c), 6.4, 6.7(d), 16.2). No conflict.
- **Dispatch:** EXECUTE NOW.

**Q07b | Original: SEC sealed answer, Q07b | CONFIRM**
- **Reason:** It applies PH01 s.7.3 and s.7.4 exactly:
  - capture session and token state for at most 10 minutes, and terminate at once if data is moving;
  - revoke at every layer (PAM, VPN, identity provider, applications, keys, tickets);
  - disable every account of the same vendor;
  - rotate the secrets that vendor access could read;
  - sweep for persistence (accounts, keys, tasks the credential created);
  - run the closure test: a replayed token and a logon with the old credential must both fail.

  Until the closure test passes, the access window stays open. Reinstating vendor access stays on hold (s.7.5).
- **Final action:** as in SEC Q07b, steps 1 to 8.
- **Owner:** SEC. IAM, Network and IT Operations execute. The Head of IT Operations is consulted if a working service would be affected. Any reinstatement is my decision, on SEC's written sign-off.
- **Time:** capture 12:00–12:10; revocation by 12:15; closure test logged by 12:30; status in the 13:00 report.
- **Trigger:** if any post-revocation use succeeds, SEC re-blocks at once, tells me and LC, and extends Q07a up to the present.
- **Recipient and channel:** emergency change record, decision log, evidence register; briefing to me and LC. The result feeds the containment items of the Cap. 653 form.
- **External basis:** as in SEC Q07b, "Basis (external)" (R11 p.5 Step 2; R10 DPP4(1); R08 s.3.2.3; R03 s.6.2.25(a)).
- **Internal basis:** as in SEC Q07b, "Basis (internal)" (PH01 v1.0 ss.7.3–7.5, 3). No conflict.
- **Dispatch:** EXECUTE NOW. Secret rotation on held hosts goes ahead only after the custodian has captured their state; no held host is rebuilt. Vendor reinstatement is on HOLD.

**Q08a | Original: LC sealed answer, Q08a | OVERRIDE**
- **Reason:** I keep LC's decision to file a voluntary PCPD notification by 15:00, by fax or in person, and keep its description of the legal status. Two pre-set answers on the form would be inaccurate when it is filed, and LC's own decision requires the "notification status" to be described accurately.
  1. **"Were the affected individuals notified?"** LC pre-sets "No, will do so within (1) days". Calls to Group A start at 13:00, so by 15:00 some of the 80 will have been reached.
  2. **"Did you engage a service provider / contractor to handle the above personal data?"** LC pre-sets "Yes" because a vendor credential was used. The form asks about engagement to handle the data, not about involvement in the breach. Whether the support contract covers handling of this workspace data is not verified.
- **Changed answers** (everything else in LC Q08a stands):
  1. Answer from the COM delivery register as it stands at the moment of filing. If any of the 80 has an evidenced delivery, answer "Yes" and state in "Summary of the remedial actions taken" how many of the 80 have been reached, with calls and letters to the rest under way by 16 Nov. If none, answer "No, will do so within (1) days". Send an update notification when delivery is complete.
  2. Answer "Yes" only if LC confirms from the contract, before filing, that the vendor's engagement covers systems holding this data. Otherwise answer "No". In either case, state in "Details of the data breach", as a neutral fact, that a vendor support credential was used in the session, without saying who is to blame.
- **Final action:**
  - File a voluntary notification by 15:00 as a new notification. The 80 confirmed records are stated as fact. The wider set of up to 18,000 is described as "possible, under investigation, export not verified".
  - Cause: Cyberattack. Real risks: Identity theft and Financial loss.
  - Other authorities: HKMA, Cap. 653 Commissioner and Police, in neutral wording cleared for tipping-off.
  - Media statement: "Issued" if the 13:30 update has been released, otherwise "Intend to issue".
  - Save the receipt. Send updates on any change of scope and after the scope review.
  - Related paths, as LC set them:
    - HKMA update by phone, then in writing, by 12:30.
    - Supplementary information to the Commissioner through the secure channel this afternoon.
    - Police case updated.
    - I tell the Board chair of the confirmed exposure by 14:00 (PH01 s.15.1).
- **Owner:** LC. The DPO prepares the form with LC. SEC confirms the facts. COM supplies the delivery and media status.
- **Time:** PCPD by 15:00; HKMA by 12:30; Board chair by 14:00.
- **Recipient and channel:** PCPD by fax to 2877 7026 or in person at Room 1303, 13/F, Dah Sing Financial Centre. Email to dbn@pcpd.org.hk only once SEC logs corporate email as safe.
- **External basis:** as in LC Q08a, "Basis – external" (R10 DPP4(1); R16a p.1; R11 pp.5–8; R16b p.3). Added: R16a PDF p.3, "ASSESSMENT OF THE INCIDENT AND REMEDIAL ACTIONS TAKEN", whose field reads "Were the affected individuals notified? *# Yes / No / No, will do so within ( ) days". R16a PDF p.2: "Did you engage a service provider / contractor to handle the above personal data? # Yes / No". These fields require factual answers on the date of filing.
- **Professional judgment:** a notification to a regulator must be accurate when filed. Inaccurate pre-set answers undermine the bank's credibility and would later need correcting.
- **Internal basis:** as in LC Q08a, "Internal bank procedure" (PH01 v1.0 ss.5.2, 5.4, 4.1, 15.1). Added: s.5.5, which requires a record of "a summary of what was said or sent, and the receipt". No conflict.
- **Dispatch:** SCHEDULE filing by 15:00. It depends on the delivery-register status from COM at filing time and on LC's contract check. It must not be held past 15:00 for either: if either is still unresolved, file with the conservative answer and send an update notification later (PH01 s.2.4). HKMA update: EXECUTE NOW.

**Q08b | Original: LC sealed answer, Q08b | CONFIRM**
- **Reason:** It separates the group to notify now from the group held for review, consistent with PH01 s.10.4(a)–(d) and R11 p.6 Step 4, and justifies the hold under R16b p.2. The events that would widen the group are specific, including LC's recommendation to notify all 18,000 if export cannot be ruled out, given that the records are co-located and HKID data is sensitive.
- **My decisions as CMT chair:**
  - I approve Group A (the 80) as the audience at 12:45.
  - Group B is held, with the reason logged.
  - The public statement covers Group B for now (s.10.4(d)).
- **Final action:**
  - Group A: personal calls from 13:00 and letters on 16 Nov.
  - Group B: the DPO and LC review with SEC's evidence by 24:00. I decide and log it. Review again on any new evidence and at least every 24 hours.
- **Owner:** I approve the audience. LC clears and recommends. The DPO advises. COM sends.
- **Time:** approval 12:45; scope review by 24:00. Any expansion trigger leads to notification of the affected customers as soon as practicable.
- **Recipient and channel:** personal call plus letter, as in COM Q09a.
- **External and internal basis:** as in LC Q08b, the "Basis – external" and "Internal bank procedure" fields.
- **Dispatch:** Group A: EXECUTE NOW. Group B: HOLD until the scope review or an expansion trigger.

**Q09a | Original: COM sealed answer, Q09a | CONFIRM, SEND**
- **Reason:** These customers' exposure is confirmed, and PH01 s.10.4(a) requires that they are "not held back for the wider review". Using a named-team call plus a letter, and no SMS, push or email, is sound given that the attacker holds their phone numbers. Contact details are taken only from verified records (s.10.5). The content covers the items listed in R11 p.7. The bracketed lines in the message are gated on SEC confirming facts and LC confirming which reports were made. Identity monitoring is offered under s.13.5.
- **Final action:** send the core message as drafted. Hold only if a written Police request to delay arrives; in that case log the reason and review every 24 hours.
- **Owner:** I approve the audience. LC clears the text. SEC and the DPO confirm the facts. COM sends and keeps the delivery register. Fraud and the contact centre call. Operations sends the letters.
- **Time:** approval and clearance 12:45; calls from 13:00, every customer attempted by 18:00; letters posted 16 Nov.
- **Recipient and channel:** the 80 customers, by personal call and then letter. The secure inbox only once SEC logs it as trusted.
- **Basis:** as in COM Q09a, "Basis (external)" and "Basis (internal)".
- **Dispatch:** EXECUTE NOW after LC clearance at 12:45.

**Q09b | Original: COM sealed answer, Q09b | CONFIRM**
- **Reason:**
  - The data update is released at 13:30, after the first calls, so the 80 customers do not hear first from the media.
  - "80" is published only if SEC confirms it from a record (PH01 s.11.4).
  - The 18,000 figure is not published, because it is the size of a store, not a verified exposure (s.10.4(c)).
  - The wider claim is stated plainly as unverified.
  - The fixed lines are kept (s.11.3).
  - The release is brought forward if the data is published first.
  - The statement is copied to the HKMA (R05 p.3).
  - It serves as the s.10.4(d) public coverage for Group B.
- **Final action:** release the data update by 13:30, with the wording and conditions as in COM Q09b. Frontline Script v3 is issued by 13:30. Next update by 18:00.
- **Owner:** I approve, with the COO as alternate after 15 minutes. LC clears the text and checks it does not prejudice the Police investigation. SEC and the DPO check the facts. COM releases.
- **Time:** 13:30, or immediately if the data is published or reported first.
- **Recipient and channel:** the public, through the same channels as the 09:00 statement; copy to the HKMA through LC.
- **Basis:** as in COM Q09b, "Basis (external)" and "Basis (internal)".
- **Dispatch:** SCHEDULE for 13:30. It depends on SEC confirming "80" and on LC clearance. The authorities line depends on LC holding the receipts.

---
**Order of actions that depend on each other:**
1. 12:00–12:15:
   - SEC captures token and session state, then revokes.
   - SEC logs the time of first confirmation.
   - SEC notifies me, LC and the DPO that T1 = 80.
2. By 12:30:
   - Closure test logged. If it fails, SEC re-blocks and Q07a extends to the present.
   - LC updates the HKMA on the confirmed exposure.
   - COM's draft is ready.
3. 12:45: I approve Group A and the Group B coverage decision. LC clears the notice text.
4. 13:00: calls to the 80 begin; the delivery register opens.
5. 13:30: public data update and Script v3 released; copy to the HKMA. This depends on SEC confirming "80" and on step 4 having started.
6. By 14:00: I tell the Board chair of the confirmed exposure.
7. By 15:00: PCPD form filed. Its answers depend on the delivery register (step 4), the media status (step 5) and LC's contract check.
8. Afternoon: supplementary information to the Commissioner; Police case updated.
9. 18:00: all 80 customers attempted; public update.
10. 20:00:
    - SEC scope paper delivered.
    - I tell the Board chair that 50% of the transfer and payroll tolerance has been reached.
11. By 24:00: scope review and my Group B decision. Any expansion leads to notices to the affected customers, a public update and PCPD and HKMA updates.