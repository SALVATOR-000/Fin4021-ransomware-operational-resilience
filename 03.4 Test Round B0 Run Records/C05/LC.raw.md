LC answer to C05 (Tuesday 17 Nov 2026, 08:00 HKT, H+24). This covers Q14a and Q14b only. I locked it before seeing colleagues' answers.

**Facts I am relying on**
- The attacker's deadline (02:00) has passed.
- A public mirror contains records that match 320 customers, including the original 80.
- The claim that 18,000 records were taken is still unverified.
- A separate social-media account is using the incident to lure customers to a fake verification page.
- A pre-incident immutable backup exists. Whether it is suitable for recovery is unverified.

**Handoff record I am relying on**
- No payment has been made and no preparatory step has been taken. The Treasury hold has been in place since 10:30 on 16 Nov.
- No contact with the attacker has been authorised or made. No commitment, offer or promise to the attacker is recorded.
- The Police report and Cap. 455 s.25A disclosure were made by 11:00 on 16 Nov. The Police's view, the Police reference number and any s.25A response are not verified.
- Insurer notification and the HKMA and Commissioner receipts are not verified.
- The outcome of the 11:00 review on contact with the attacker is not recorded, so the default (no contact) applies.
- Whether the Q06a staff script went live is not verified.

---

## Q14a – Payment posture

**Decision: keep the posture. No payment, no preparatory steps, no contact.** Nothing has changed that would justify reopening it, and the new facts strengthen it:
- The attacker's deadline passed without payment.
- The attacker has already published data, so paying would not prevent that disclosure.
- Paying would not bring back the gateway faster. Recovery is going through the immutable backup and alternate processing route (SEC, Q13).
- None of the legal gates has been cleared: the Police view, the OSCO s.25A response, the UNATMO screening of the recipient and the sanctions screening are all still outstanding.

**Recorded commitment: none to handle.** The record shows no commitment, offer or promise to the attacker and no Treasury step. LC enters this "nil commitment" confirmation in the decision log at 08:15 HKT.
- LC asks Treasury, the CFO and the vendor relationship owner to confirm in writing by 10:00 HKT that they have made no virtual-asset account, purchase, intermediary engagement or attacker contact.
- If any such step is found, it is frozen at once and reported to the CMT chair and the Board. LC then assesses it under Cap. 455 s.25 and s.25A and makes a further disclosure to the Police if needed.

**Actions and owners**
1. The written Treasury hold continues. LC reissues it by 09:00 HKT with an added instruction: any new or renewed demand, including a "discount" or "extension" offer, goes to SEC only, through the evidence process.
2. The CMT chair records in the Board paper that the posture is unchanged (PH01 s.15.3, "payment posture"). The Board is not asked for any decision unless a departure is proposed. LC does not recommend one.
3. The open items are not holds on the posture. They are records to close:
   - The CFO obtains the insurer's acknowledgement and position by 12:00 HKT.
   - LC obtains the Police reference number and their view on the case, and any s.25A response, on the call in Q14b.
4. Any new demand is logged and passed to the Police. It goes into the same evidence file and does not reopen the posture unless the Board itself decides to.

**External basis**
- **R16c, Cap. 455 OSCO (statute)**
  - s.25(1), PDF p.82: dealing with property "knowing or having reasonable grounds to believe that any property ... represents any person's proceeds of an indictable offence". "Dealing" (s.2, PDF p.6) includes "disposing of or converting the property".
  - s.25A(2)(a), PDF p.83: protection applies only where the disclosure "is made before he does that act and he does that act with the consent of an authorized officer".
  - **Missing fact:** no Police consent is recorded. Any payment therefore stays barred.
- **R16d, Cap. 575 UNATMO (statute)**
  - s.8(a), PDF p.20: a person must not "make any property or financial (or related) services available ... knowing that, or being reckless as to whether, the person is a terrorist or terrorist associate".
  - **Missing fact:** the recipient has not been screened. Payment stays barred.
- **Sanctions:** no direct rule located in the assigned sources. I searched the whole manifest for "sanction", "virtual asset", "ransom" and "extortion" at C02. The only hit was PH01 s.12.2.
- **Professional judgment:** publication after the deadline shows that payment would not secure the data. Paying would add legal and conduct risk and would invite repeat demands.

**Internal bank procedure (PH01 v1.0)**
- s.12.1: "The Board's policy is that the bank does not pay a ransom. Any departure is for the Board alone."
- s.12.2: "Treasury holds all preparatory steps (virtual-asset accounts, purchases, intermediaries) until the Board decides."
- s.12.3: "Staff, branches, COM and vendors never reply to an attacker; they pass any message to SEC."
- s.11.3, for COM: the bank "states whether a payment has been made only as a verified present fact". LC confirms the verified fact for COM at 08:15: "no payment has been made".
- There is no conflict between PH01 and the external sources.

---

## Q14b – Referral to law enforcement

**Decision: yes.** The matter is already with the Police, so this is a supplementary referral to the same case. It covers two new matters:
- **(i)** the public mirror of 320 customers' records;
- **(ii)** the fake verification page and the social-media account, reported as a separate fraud and phishing matter cross-referenced to the incident.

At the same time, LC asks for the Police reference number, their view on the case, and confirmation of the s.25A disclosure.

**Owner**
- LC decides and reports (PH01 s.3, "Report to the Police | LC"). The CMT chair is informed.
- SEC, as evidence custodian, prepares the evidence pack.
- LC and SEC jointly approve any release of data. The Data Protection Officer (DPO) is consulted.

**Timing**
- **(ii) Fake page:** phone report to the Police CSTCB by 09:00 HKT, because customers are being lured now. Written follow-up by 11:00 HKT.
- **(i) Mirror:** phone report by 09:00 HKT, combined with (ii). Evidence pack delivered by 12:00 HKT, or at the time the Police set.

**Channel:** phone to the Police CSTCB using the printed contact register, quoting the existing case reference if the Police can confirm it. Evidence goes on bank-issued encrypted media handed over in person, or by a route the Police nominate. It does not go by ordinary or corporate email unless SEC has logged email as safe. Receipt and chain of custody are logged under PH01 s.5.5 and s.6.3.

**Evidence that can go with the referral**
- **No customer personal data needed:**
  - incident timeline (HKT-normalised, with uncertainty);
  - demand messages and the screenshot, as hashed copies from the evidence register (PH01 s.6.6);
  - the wallet address;
  - indicators of compromise;
  - the vendor credential identifier and session times;
  - the bank's logs of the export;
  - the mirror URL, capture time and SHA-256 hash of the captured file, collected by SEC without interacting with the attacker (PH01 s.6.6);
  - for the fake page: the account handle, post URLs, page URL, capture timestamps and hashes;
  - counts of the matched records (320, including the 80) and a description of the matching method.
- **Customer personal data:** the list of the 320 matched customers and their record content goes as a minimised set, under LC's and SEC's joint written approval, only to the extent the Police need it, or on their formal request.
  - Basis: PDPO s.58(1)(a)-(b) and s.58(2) (below).
  - A data release record is opened under PH01 s.3.
- **Not to be released:** full system images without LC's and SEC's written approval (PH01 s.16.2). Analysis copies only. The originals stay under the bank's custody record.

**External basis**
- **R16c, Cap. 455 OSCO (statute)**
  - s.25A(1), PDF p.83: disclosure "as soon as it is reasonable for him to do so ... to an authorized officer". Under s.2 (PDF p.6), an authorized officer includes "any police officer".
  - s.25A(3)(a): a disclosure "shall not be treated as a breach of any restriction upon the disclosure of information imposed by contract or by any enactment".
  - This applies to further disclosures about the demand and the wallet property.
- **R10, Cap. 486 PDPO, s.58 (statute)**, PDF pp.117-119:
  - s.58(1) covers data held for "(a) the prevention or detection of crime; (b) the apprehension, prosecution or detention of offenders".
  - s.58(2) exempts data from DPP 3 where "the use of the data is for any of the purposes referred to in subsection (1)" and applying DPP 3 "would be likely to prejudice any of the matters".
  - **Judgment left to the bank:** whether withholding the data would prejudice the investigation. LC decides case by case, minimising the data released and recording the reasons.
- **R11, PCPD Guidance (privacy guidance, not binding)**, PDF p.4, Step 2:
  - "Notifying the relevant law enforcement agencies if identity theft or other criminal activities have been or are likely to be committed".
  - "Requesting internet companies to remove any relevant cached links".
  - This supports both the referral and takedown requests for the mirror and the fake page.
- **R09, SPM TM-E-1 V.4 s.4.3 (HKMA supervisory guideline)**, PDF p.17:
  - On fake websites, AIs "should consider and decide in a timely manner how to inform their customers and the public more widely and report the matter to the Hong Kong Police Force".
  - AIs should also "report the matter to the HKMA", and "should make attempts to remove the fake or suspicious items where practicable".
  - Footnote 12: press release "as soon as practicable" and report to the HKMA "immediately after the press releases are issued".
  - The fake verification page falls squarely within this.
- **Tipping-off, R16c s.25A(5), PDF p.84:** LC clears COM's warning and public wording so that nothing likely to prejudice the investigation is disclosed (Q15b is COM's task).

**Internal bank procedure (PH01 v1.0)**
- s.3: "Report to the Police | LC | CMT chair informed".
- s.6.3: chain of custody, SHA-256, "Analysis is on verified copies only".
- s.6.6: "Nobody requests further samples, visits attacker links or uploads attacker material to an outside service". SEC captures the mirror and the fake page passively, through the evidence process.
- s.16.2: "A full copy leaves the bank only with LC's and SEC's written approval."
- **Point of interpretation:** PH01 s.16.1 requires a signed data agreement before data goes to a "third party". A statutory law enforcement agency will not sign the bank's agreement, and the PDPO s.58 exemption governs this disclosure. LC records that s.16.1 does not apply to the Police, but keeps the minimisation and joint-approval controls in s.16.2 and s.3. This is consistent with PH01 s.1.3, which says the external requirement prevails. LC logs the point.

**Related filings with their own clocks (not assigned to LC in this card; noted for coordination)**
- HKMA: immediate update on the 320-record publication and the fake page.
- Commissioner: supplementary information through the secure channel (R02 s.7.3.7(a)).
- PCPD: update to the earlier notification marked "an update of a previous notification" (R16a), raising the confirmed number from 80 to 320.
- The 240 newly matched customers become confirmed for notification (PH01 s.10.4(a); COM's Q15a).

**Simulated actions for the facilitator to log**

| Time (HKT) | Action |
|---|---|
| 08:15 | Posture-maintained and nil-commitment entry in the decision log |
| 09:00 | Treasury hold reissued |
| 09:00 | Phone referral to the Police CSTCB (mirror and fake page); reference and s.25A status requested |
| 10:00 | Written nil-step confirmations from Treasury, the CFO and the vendor owner |
| 11:00 | Written Police follow-up |
| 12:00 | Evidence pack handed over in person with custody record; data release record opened |
| 12:00 | Insurer acknowledgement obtained by the CFO |