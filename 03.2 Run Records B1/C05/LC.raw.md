LC SUBMISSION – C05 (Tue 17 Nov 2026, 08:00 HKT, H+24) – Units Q14a and Q14b
Locked before I see colleagues' answers. All actions are simulated, for the facilitator to log. I rely on the C05 facts and the facilitator's handoff of the Q05a and Q05b records.

C05 facts:
- The attacker's 02:00 deadline has passed.
- A public mirror of a file matching 320 customers' records has been found. It includes the original 80.
- The 18,000-record claim is still unverified.
- A social-media account is using the incident to lure customers to a fake verification page.
- A pre-incident immutable backup exists. Whether it can restore payment processing is unverified.

What the record shows from 16 Nov:
- The no-payment, no-contact posture has been in force since 09:45. No payment, preparatory step, offer or promise has been made.
- Done in simulation, without evidence of the outcome:
  - Treasury hold;
  - Board chair told;
  - Police report at 10:30, with no Police view or case reference recorded;
  - insurer notified, receipt not verified;
  - posture reviews and the 22:00 note, with no content recorded.
- The Cap. 455 (Organized and Serious Crimes Ordinance) disclosure cannot be verified, because no card says whether the demand named a payment destination.

==================================================
UNIT Q14a – Payment posture and recorded commitments
==================================================
Decision: keep the no-payment, no-contact posture. Do not suspend it. Revise only the review triggers and close the gaps in the record.

Reasons:
- Every gate (a)–(g) is still unconfirmed, and the Board has not considered any departure (PH01 12.2).
- Professional judgment:
  - publication of 320 records shows that paying would not have kept the data private, and cannot now;
  - the attacker's claims are only partly verified (18,000 unverified);
  - an immutable backup gives a recovery path that does not depend on the attacker.
- The deadline passing changes nothing in law.

Recorded commitments
1. To the attacker: none are recorded (handoff: "no commitment, offer or promise to the attacker"). There is nothing to honour or withdraw.
   - We send no message to say the bank will not pay. That would be contact, and contact is barred (PH01 12.3).
2. Internal commitments that stay in force:
   - Treasury hold on any virtual-asset step. Only a Board decision lifts it (PH01 12.2).
   - The standing instruction that no one replies to the attacker.
   - The rule that public lines say "no payment has been made" only as a verified present fact. Treasury re-confirms before each statement (PH01 11.3).
3. Gaps to close by 10:00 HKT:
   - LC re-issues the written posture note, with content, timed, and logged in the decision log. This fixes the missing content of the 14:00, 20:00 and 22:00 records.
   - The CFO gets the insurer's written acknowledgement and position.
   - SEC and LC check the demand held in evidence for a payment destination (wallet address or contact channel), by 09:00.
     - If one is named and no disclosure is logged: make the s.25A disclosure now, through the bank's internal disclosure procedure, to a police officer. Log the reason it is late.
     - If none is named: log "no payment destination identified – disclosure not triggered by the demand".
     - Either way, tipping-off controls continue.
4. Board:
   - If outbound transfers and SME payroll have not been restored, the 24-hour tolerance was reached at about 08:00 HKT. The Board or its Risk Committee must then meet by 20:00 HKT (PH01 15.2).
   - LC supplies the payment-posture and authorities sections of the Board paper, with legal advice in a separate privileged section (PH01 15.3).
   - LC recommends that the Board note the no-payment posture. No departure is proposed.
5. Revised review triggers. LC reviews the posture at 08:00 and 18:00 daily, and at once on any of:
   - a new demand or contact attempt from the attacker;
   - further publication, or verification of the 18,000 claim;
   - the Police view or a Police request;
   - a finding that the backup is unsuitable;
   - the insurer's position;
   - a request from a regulator or the Board.
   None of these alone allows a departure. Any departure still needs the written gates (a)–(g) and a Board decision.

Accountable owner and executing party
- Board: the policy and any departure.
- CEO (CMT chair): holds the posture day to day and convenes the Board.
- LC: the recommendation, gates, posture note and any disclosure.
- CFO and Treasury: the hold and the insurer.
- SEC: checks the demand evidence.

Deadlines
- Decision logged by 08:15 HKT.
- Demand check by 09:00.
- Posture note and insurer position by 10:00.
- Board by 20:00 HKT 17 Nov, if the tolerance has been reached.

Recipients and channels
- Decision log.
- Treasury in writing through the CFO.
- Police officer through the disclosure procedure, if triggered.
- Board paper through the CEO.

Basis: external
- R16c, Cap. 455. Status: statute.
  - s.25A(1), PDF p.83: disclose "as soon as it is reasonable".
  - s.25A(2)(a): disclosure "before he does that act and he does that act with the consent of an authorized officer".
  - s.25A(5), PDF p.84: tipping-off offence.
- R16d, Cap. 575 (UN anti-terrorism ordinance). Status: statute (2019 verified copy). s.8(a), PDF p.20: no making property available while "reckless as to whether" the person is a terrorist or terrorist associate. The recipient is still unidentified.
- No direct rule located on an HKMA position on ransom payment. Search: "ransom" and "extortion" in R04, R05, R09, R13, R14a and R14b.

Internal bank procedure (PH01 v1.0)
- 12.1: "The Board's policy is that the bank does not pay a ransom. Any departure is for the Board alone."
- 12.2: "Treasury holds all preparatory steps ... until the Board decides."
- 12.3 and 15.2–15.3.
- Conflict check: none. The one gap was raised at C02: the s.25A duty does not wait for a payment proposal.

==================================================
UNIT Q14b – Law enforcement referral and the evidence that can go with it
==================================================
Decision: yes. Make an updated, formal referral to the Police Cyber Security and Technology Crime Bureau (CSTCB) now. It adds three new crimes, plus the fact that the deadline passed without payment:
- (i) publication of customer data on a public mirror (320 records);
- (ii) the fake verification page and impersonating social-media account, which pose an ongoing risk of phishing and identity theft to customers;
- (iii) the export through a vendor support credential.
The 16 Nov report has no recorded case reference or Police view. So this referral is made formally and in writing, and gets its own reference.

Actions and timing
1. By 08:30 HKT, LC telephones CSTCB using the contact in the Regulator Contact Register (RCR). LC:
   - reports the fake page and the mirror as urgent;
   - confirms or obtains the case reference;
   - asks for the Police view on the takedown requests, on public warning wording, and on whether any public statement could prejudice the investigation;
   - records everything under PH01 5.5.
2. From 08:30 HKT, SEC and COM ask the platform and host to remove the fake page, the social-media account and the mirror. LC clears the legal wording. No member of staff visits the links; SEC captures them in a controlled way.
3. By 12:00 HKT, a written referral with an evidence package goes to CSTCB.
   - LC and SEC release it jointly, with the DPO consulted.
   - The evidence custodian delivers it on bank-issued encrypted media, or through a bank-hosted encrypted transfer, with a SHA-256 manifest.
   - It is logged in the evidence register and the data release record.
4. HKMA: report the fake page in the next HKMA update, and again immediately after COM's press release on the scam (R09 footnote 12).

Evidence that can go with the referral
A. Now, with no customer personal data:
   - a normalised HKT timeline, with confirmed and unverified items marked (PH01 6.4);
   - verified copies of the demand: message, metadata, amount, deadline, any wallet or contact details;
   - the time-stamped export logs;
   - session and access logs showing use of the vendor credential, plus revocation and closure-test status. Any records preserved by the vendor are marked "supplier's account, not yet reconciled" (PH01 6.7(d));
   - indicators of compromise: IPs, domains, tool hashes, commands;
   - for the mirror and the fake page: URLs, account handles, capture times, screenshots and file hashes;
   - the forensic match result as counts only (80 confirmed and 320 published);
   - the dates of notifications to the Commissioner, the HKMA and the PCPD.
B. Customer personal data only to the extent the Police need it, preferably at their request, minimised, and by the secure route above:
   - the identifiers of the 320 records;
   - reports from affected customers about the fake page, with their contact details only where needed.
C. Not shared:
   - privileged legal advice and Board papers;
   - original evidence. Originals stay with the custodian and the Police receive verified copies (PH01 6.3);
   - the full 18,000-record workspace.

Accountable owner and executing party
- LC decides the referral; the CEO is informed (PH01 s.3).
- SEC and LC jointly release the evidence; the forensic lead and the DPO are consulted.
- The evidence custodian delivers it.

Recipient and channel
- Police CSTCB: telephone, then a written referral with an encrypted evidence package.
- Platform and host operators: takedown requests.
- HKMA: by its confirmed route.

Basis: external
- R09, SPM TM-E-1. Status: statutory guideline. 4.3.2, PDF p.17. Where AIs become aware of fake websites or similar scams, they "should consider and decide in a timely manner how to inform their customers and the public more widely and report the matter to the Hong Kong Police Force". They should also "notify promptly their customers through issuing press releases ... and report the matter to the HKMA", and "make attempts to remove the fake or suspicious items where practicable".
- R04, SPM TM-C-1. Status: statutory guideline. 2.4 and footnote 1, PDF p.4: report significant cyber incidents to the HKMA and, where appropriate, to relevant authorities, including the CSTCB.
- R11, PCPD Guidance. Status: privacy guidance.
  - PDF p.4: "Notifying the relevant law enforcement agencies if identity theft or other criminal activities have been or are likely to be committed".
  - PDF p.7: notify "other parties who may be able to take remedial actions", including internet companies.
- R10, Cap. 486 Personal Data (Privacy) Ordinance. Status: statute. s.58(2), PDF p.119: personal data is exempt from DPP3 where its use is for "the prevention or detection of crime" and applying DPP3 "would be likely to prejudice" that purpose. Disclosure of minimised customer data to the Police falls within this.
- R16c, Cap. 455. s.25A(3)(a), PDF p.83: a disclosure "shall not be treated as a breach of any restriction upon the disclosure of information imposed by contract".

Internal bank procedure (PH01 v1.0)
- s.3: "Report to the Police | LC | CMT chair informed".
- s.3: sharing incident data with a third party is decided by "LC and SEC jointly".
- 6.3: custody.
- 6.6: no one visits attacker links.
- Conflict identified: PH01 16.1 says data goes to an "other third party only under a signed agreement". Read literally, that would block or delay evidence to the Police, which conflicts with R09 4.3.2 and R04 2.4.
  - Action consistent with the external requirement: treat 16.1 as written for commercial processors.
  - Send the Police minimised data under a covering letter stating the purpose (crime investigation), recorded in the data release record.
  - Record the difference under PH01 1.3.

==================================================
Updates to existing LC reporting tracks (not a C05 unit)
==================================================
- PCPD: send an updated notification by 12:00 HKT on the PCPD form, marked "update of a previous notification". Content: 320 records confirmed and publicly mirrored; 18,000 unverified; the fake page; the Police referral (R11 p.8: "without delay").
- HKMA: the 08:00 update covers the newly confirmed 240 customers, the mirror, the fake page and the unchanged posture.
- Commissioner: supplementary information on the publication through the secured channel, today (PH01 5.9).
- COM (Q15a): the 240 newly confirmed customers are notified as soon as practicable (PH01 10.4(a)).

No files were created.