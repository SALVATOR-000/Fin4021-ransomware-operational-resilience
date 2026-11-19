# Ransomware and Operational Resilience: When a Bank Gets Locked Out

FIN4021 group project, Topic 5 · Nov 18, 2026 · @Salvator

## 1. Executive summary

For a bank hit by ransomware, we ask which first-72-hour decisions Hong Kong's rules settle, which they leave to the bank, and whether a playbook closes the gap.

The rules fix who must be told and the outer deadlines: a bank designated under Cap. 653 must notify the Commissioner within 12 or 48 hours, the HKMA expects immediate notice, and PCPD notice is voluntary. The bank sets its own thresholds, approvers and recovery steps; no statute we reviewed mentions ransom.

We tested this in a 72-hour tabletop at a fictional designated bank. AI agents for security, legal, communications and the CEO made 48 scored decisions, first from regulatory sources alone (A1), then with our playbook PH01 (B1). B1 scored 88 of 92, A1 83. PH01 helped where it set an owner, condition and record: de-sensitisation and prior approval became preconditions for testing, no recovery gate could be waived, changes awaiting assessment were split by deployment date, and the closing update awaited set conditions. It did not fix misreadings of external law: four errors on money-laundering disclosure and scam warnings recurred, unnoticed by the CEO. With one run each, on different models, the results are indicative.

Refusal to pay should be the rule. Paying should stay lawful only when there is no safe way back, harm is serious and widespread, paying would credibly help, and every money-laundering, terrorist-financing and sanctions test is met.

The bank should first adopt the playbook with named owners, give customer messages a fixed clearance slot, add a second legal check on external triggers, build an isolated payment process and backup, and test twice a year. We also propose four reforms: a confidential ransom-payment report within 72 hours, one intake for incident reports, mandatory PCPD notice for high-risk breaches, and a notice duty for critical vendors.

## 2. Background and problem statement

### 2.1 What ransomware does to a bank

On 8 November 2023 (US Eastern Time), ransomware encrypted systems at ICBC Financial Services, the US broker-dealer of ICBC \[F5; F9 ¶2\]. The firm cut its links to its clearing firms, "impeding trading" \[F9 ¶2\], and its books and records were not kept current until 1 March 2024 \[F9 §III, Summary\]. OFAC named LockBit as responsible and said the attack affected "the settlement of over $9 billion worth of assets backed by Treasury securities" \[F8\]. Escalation was slow: the first Core Executive Response Group meeting came "nearly 12 hours" after the attack was identified \[F6 p.86\].

### 2.2 Two Hong Kong cases

Two cases investigated by the Privacy Commissioner (PCPD) paired encryption with a ransom demand. At the Hong Kong Institute of Bankers (HKIB), the backups were encrypted too, because staff had not made the offline backup its policy required \[H11 fn 9\]. At Cyberport, about 40% of the 13,632 people affected were people whose data had been kept past its retention period \[H12 ¶¶10, 33\]. Both were found to have contravened DPP4(1) \[H11 ¶¶16–21; H12 ¶¶34–39\]. The PCPD still described HKIB's notice, sent 12 days after discovery, as "a timely data breach notification" \[H11 ¶20\]. Appendix A gives the timelines of all three cases.

### 2.3 The rules a Hong Kong bank now faces

Since 1 January 2026, a bank designated under Cap. 653 runs a statutory clock beside its HKMA reporting \[L1; L.N. 144 of 2025\]. The three channels have different recipients, triggers and deadlines: the HKMA expects notice "immediately" \[H4 p.2\], the Commissioner must be told within 12 or 48 hours \[L1 s.28, Sch. 6\], and the PCPD "as soon as practicable" \[H10 p.6\]. The HKMA also expects banks to notify affected customers proactively and to say "whether the bank would reimburse any losses" \[H4 p.1\]. Section 3.1 maps these duties phase by phase.

### 2.4 Problem statement and method

To test these questions, we built Lan Tidal Bank Limited, a fictional Hong Kong licensed bank with about 180,000 retail customers and 12,000 SMEs. As a scenario fact, it is a designated operator under Cap. 653: domestic transfers and payroll are its core function, and the payment gateway is its critical computer system. A 72-hour tabletop exercise runs eight scenario cards with 24 scored questions, two decisions each. Three AI role agents (security, legal and compliance, communications) answer independently from a frozen set of Hong Kong primary sources, and an AI CEO agent confirms or overrides each answer.

Run A1 asks what the agents decide from the regulatory sources alone. Run B1 repeats it with our playbook PH01 added. A1 ran on Claude Fable 5.2 and B1 on Claude Opus 5.5, each at that model's xhigh reasoning-effort setting. Each run is performed once and the two use different models, so differences cannot be attributed to PH01 alone. Group members sealed the expected answers before each run and reviewed and finalised all scores.

B1 is a rerun. The first B run used Opus 5.5 at Medium effort to save budget; it is archived as test round B0 and not compared. B0 and A1 ran at different effort settings, and on review the searches and basis behind several B0 decisions were hard to verify: some roles gave a reasonable action and flagged it as judgment, but left too little search record to show they had checked the most relevant rule. In Q07b, for example, B0 handled the vendor credential under the playbook but did not cite the requirement to change promptly any password that is or may be compromised \[H7 ¶6.2.13(b)\]; B1 cites it. Once our usage quota was restored, we reran B at xhigh so that both runs use their model's xhigh setting. We took that decision after seeing B0's preliminary results.

Bracketed IDs such as \[H4\] refer to the source register in the evidence appendix. Appendices A to E there hold the case timelines, the detailed regulatory mapping, the score for every decision, the cost basis and the supplementary tests.

## 3. Regulatory mapping and gap analysis

Hong Kong's rules fix who must be told and the outer deadlines, but leave the bank to set its own thresholds, internal steps and any ransom decision.

### 3.1 Duties in the first 72 hours

| Phase | Duty and source | Left to the bank |
| --- | --- | --- |
| Report to HKMA | Notify "immediately" once aware of a significant incident, and do not wait for a fix \[H4 p.2; H3 ¶2.4\] | What counts as "significant" |
| Notify the Commissioner | Within 12 hours if the incident has disrupted, is disrupting or is likely to disrupt the core function, otherwise 48; the specified form within 48 hours of a phone notice; a written report within 14 days \[L1 s.28, Sch. 6; L2 ¶7.3.6(b)\] | When awareness starts; the thresholds in four of the seven serious-incident tests \[L2 ¶7.3.4\] |
| PCPD and customers | PCPD notice is "not mandatory", but the HKMA expects banks to "seriously consider" it; "Oral notifications are not accepted"; notify affected or likely affected customers proactively \[H13 p.1; H9 p.3; H10 p.8; H4 p.1\] | Whether to notify on suspected exfiltration; who is "likely affected" |
| Ransom demand | Dealing with known or believed crime proceeds is an offence; suspicion must be disclosed; no funds to terrorist associates \[L3 ss.25(1), 25A(1)–(2); L4 (Cap. 575 s.8)\] | Whether paying is "dealing": the statute does not say |

Appendix B gives the full mapping, including the legal force of each duty.

### 3.2 Where the rules stop

**Outer limits, not internal steps.** The sources name recipients and deadlines, not who decides, drafts or signs inside the bank. Cap. 653 makes a designated operator write and implement its own plan, but lists only the topics it must cover \[L1 s.27; Sch. 3 Pt 2\]. In four of the Code's seven serious-incident tests, downtime, service level and "material" are "defined by the CI operator in the business continuity management plan" \[L2 ¶7.3.4(a), (b), (d), (f)\]; the other three must still be checked against their own conditions \[L2 ¶7.3.4(c), (e), (g)\].

**Three clocks, three triggers.** The HKMA clock runs from awareness that a significant incident "has occurred" \[H4 p.2\]. The Commissioner's runs from a "reasonable degree of certainty" \[L2 ¶7.3.5\], and the PCPD's from awareness of a breach that may only be suspected \[H10 pp.1, 6\]. A single timed and signed awareness log is the simplest way to show each clock was met.

**Silence on ransom.** None of the statutes we reviewed uses the word "ransom" \[L1, L3, L4, L5\]. Legality turns on general money-laundering and terrorist-financing offences; HKCERT advises "Don't pay the ransom", but it is not a regulator \[O1\].

These are the gaps an internal playbook has to fill. The HKMA now asks banks to review "playbooks prepared for prominent cyber-attacks" and to test them where appropriate \[H8 p.2\]. Section 3.3 tests how the A1 agents handled them.

### 3.3 What run A1 showed

**How much the sources cover.** Before the run, group members sealed an expected answer for each of the 48 scored decisions (two per question). Following the branches that applied in A1, 43 of them could be judged against the sources. In 24 of those, the frozen sources give a direct basis for at least one decision or necessary condition; in the other 19 they offer only general principles. The remaining 5 could not be judged, because key facts or cross-referenced texts were missing.

**Main gaps.** Finding the right rule was not enough. No direct source was missed, and every reporting step for the original incident was right. But in seven decisions the agents applied a rule to the wrong conditions: they misread the consent and disclosure conditions of Cap. 455 s.25A \[L3\], merged system changes made on three days into one assessment, treated the HKMA's scam-warning trigger as met without checking it \[H16 ¶4.3.2\], and used the expectation to announce "shortly after the commencement of any disruption" \[H16 ¶8.2.3\] as the basis for later updates. Two actions scored zero: that merged assessment, and an offline test planned on production data without de-sensitisation or prior approval \[H2 ¶4.2.4\]. The CEO agent labelled 47 of its 48 rulings "CONFIRM" and corrected none of the seven. Section 7.2 gives the results of both runs and Appendix C the score for every decision. A1 is a single run by AI agents, so these figures describe this exercise, not banks in general.

### 3.4 How Hong Kong compares

Hong Kong is with the majority: it neither bans ransom payments nor has a dedicated report for them. FATF's 2023 study found incident reporting "In most cases ... voluntary" \[F2 ¶47\] and that most jurisdictions "did not criminalise victims making ransom payments" \[F2 fn 31\]. The US deters payment through sanctions risk, Australia requires payments to be reported, and the UK has proposed a ban for its most critical sectors.

|  | Hong Kong | United States | United Kingdom | Australia |
| --- | --- | --- | --- | --- |
| Payment banned? | No; no statute we reviewed mentions ransom \[L1, L3, L4, L5\] | No; government "strongly discourages" payment \[F1 p.1\] | Proposed for the public sector and regulated critical national infrastructure \[F3 p.5\] | No \[F4 Pt 3\] |
| Payment reported? | No dedicated payment report; suspected crime proceeds must be disclosed \[L3 s.25A(1)\] | A prompt, complete report to law enforcement is a "significant mitigating factor" \[F1 p.5\]; New York requires covered firms to report a ransom payment within 24 hours \[F13 §§500.1(e), 500.17(c)\] | Proposed: report the intent to pay; the government may block the payment \[F3 p.28\] | Yes, within 72 hours of paying \[F4 s.27\] |
| Status | In force | Advisory, 2021; New York rule since 1 December 2023 \[F13 §500.22\] | Proposals, July 2025 | In force from 30 May 2025 \[F4 FAQ p.1\] |

**What this means for Hong Kong.** No rule requires a ransom payment to be reported as such; the authorities may learn of one only through incident notifications or a Cap. 455 disclosure. And where a payment has a US nexus, strict-liability US sanctions may be the decisive test, since Cap. 537 gives effect only to UN sanctions \[F1 p.4; L4\]. Appendix B gives the detail for each jurisdiction; Part 4 proposes a confidential payment report.

### 3.5 Are the rules adequate? A CIA test

Measured against the CIA triad, Cap. 653 covers all three pillars for a designated bank's critical systems. The gaps lie in judgment-dependent triggers, the voluntary PCPD notice, non-designated vendors and the ransom itself.

The lecture framework treats ransomware as an availability problem: it "kills availability but not integrity" (Lecture 4, slide 28). The ICBC case cuts against that, since the firm's books "reflected inaccurate and/or incomplete information" \[F9 ¶4\]. Cap. 653 defines security as protection against events that compromise "availability, integrity or confidentiality" \[L1 s.2\], and its clock turns on the core function, not on which pillar is hit \[L1 Sch. 6 item 1\].

| Pillar | What ransomware did | Hong Kong rule | Gap |
| --- | --- | --- | --- |
| Availability | ICBC FS cut links to its clearing firms, "impeding trading" \[F9 ¶2\] | 12 hours if the core function has been, is being or is likely to be disrupted \[L1 Sch. 6 item 1(a)\]; HKMA "immediately" \[H4 p.2\] | Statutory clock covers designated operators only |
| Integrity | ICBC FS books inaccurate or incomplete \[F9 ¶4\] | Same test: 12 hours if the core function is or is likely to be disrupted, otherwise 48 hours \[L1 Sch. 6 item 1\] | Corrupted records may not look disruptive at first, so the clock turns on the bank's judgment of likely disruption |
| Confidentiality | HKIB: servers encrypted and a threat to upload their files to the internet \[H11 ¶1\]; Cyberport: data exfiltrated, with samples posted on the dark web \[H12 ¶¶6, 19\] | Leaking a material volume of customer data counts as serious, so 12 hours \[L2 ¶7.3.4(d)\]; PCPD notice "not mandatory" \[H13 p.1\] | The bank defines "material"; no statutory notice to the PCPD |

A critical fintech vendor is the weakest point. Cap. 653's notice duty falls on the designated operator \[L1 s.28\], so a vendor that is not itself designated carries none, while the system stays the bank's critical computer system even when it is outsourced \[H7 ¶3.1.3(a)\]. And because Hong Kong has "No single cyber law" (Lecture 4, slide 57), the ransom question falls to general money-laundering and terrorist-financing offences (Section 3.2).

## 4. Ethical analysis: should paying a ransom ever be lawful?

A bank facing a ransom demand has to weigh the immediate harm to customers against the risk of encouraging future attacks.

### 4.1 Two frameworks, one default

Lecture 1 sets out two competing theories (slide 6). Deontology holds that "Some acts are absolutely wrong — full stop." Utilitarianism holds that "The right act maximizes total well-being."

**Deontology: do not pay.** On a duty-based view, paying rewards extortion whatever the bank gains: payments "perpetuate and incentivize additional attacks" \[F1 p.3\]. The bank's own duty comes earlier, to take "All practicable steps" to protect personal data \[L6 Sch. 1, DPP4(1)\].

**Utilitarianism: count everyone's harm.** The benefit of paying is uncertain: "there is no guarantee that companies will regain access to their data or be free from further attacks" \[F1 p.3\]. The costs fall on future victims and on customers whose data may be published anyway. The sum can favour paying only when no safe recovery path is left, waiting would cause severe and widespread harm, and paying would credibly reduce it. That case is not hypothetical: HKIB's backups were encrypted too \[H11 fn 9\].

Both frameworks set the same default: do not pay. A targeted ban, as the UK has proposed for its most critical sectors \[F3 p.5\], makes that default absolute, at a cost to victims with no way out \[F3 p.26\].

### 4.2 Fairness, accountability, transparency and privacy

- **Fairness.** The people with most at stake have no say: at Cyberport, about 40% of those affected were people whose data had been kept past its retention period \[H12 ¶33\].
- **Accountability.** A payment decision needs a named owner, a written record and legal sign-off. In run A1 the AI CEO labelled 47 of 48 rulings "CONFIRM" and corrected none of the seven legal errors (Section 3.3).
- **Transparency.** Secret payments hide the threat from everyone else; FATF finds ransomware attacks "generally underreported" \[F2 p.3\].
- **Privacy.** Paying for deletion buys a criminal's promise. Customers whose data was taken should be notified as if it will be published.
- **Inclusion and environment.** An outage hurts most the customers who cannot switch channel, so the playbook must keep branch and phone service open (Part 5). Environmental effects do not bear on this decision.

### 4.3 Our position

Refusal should be the rule, and paying should remain lawful in Hong Kong only as a tightly bounded exception. We do not support a ban for Hong Kong banks yet: with no dedicated payment report, no regulator here can measure how often banks pay (Section 3.4), and the UK's own ban was still a proposal in July 2025.

As a policy recommendation, the group proposes three tests for when a board should even consider an exception. All three must be met:

1. **No safe way back.** Every feasible safe recovery path, including isolated backups \[H7 ¶6.2.20(b)(i)\], has been tried and exhausted.
2. **Serious, widespread harm.** Waiting longer would cause serious and widespread harm to customers, the payment system or the public, not only to the bank.
3. **Payment would help.** There is credible evidence that paying would materially reduce that harm; on its own, a payment carries "no guarantee" of recovery \[F1 p.3\].

Passing these tests does not make a payment lawful. The anti-money-laundering, counter-terrorist-financing and applicable sanctions requirements must each still be met separately: the Cap. 455 disclosure and consent route where applicable \[L3 s.25A\], the Cap. 575 bar on funds for terrorist associates \[L4\] and, where a payment has a US nexus, OFAC rules under which licences face "a presumption of denial" \[F1 p.5\].

The three tests are our recommendation, not part of PH01. PH01 v1.0 makes refusal the Board's policy, states that "Any departure is for the Board alone", and requires written legal gates before the Board may consider one \[PH01 v1.0 §§12.1–12.2\]. We also propose a confidential report of any ransom payment within 72 hours, with limits on its use, following Australia \[F4 ss.27, 29–30\]; no such duty exists in Hong Kong today. Parts 5 to 8 turn these conditions into controls.

## 5. Control and policy proposal: the response and disclosure playbook

PH01 turns the duties in Part 3 into owners, conditions and records. It does not restate any external trigger, recipient or time limit, and its internal times never extend an external deadline \[PH01 v1.0 §§1.2, 1.4\]. Two rules run through it. A condition that holds an action must name who verifies it, by when, the default if it is not verified, and a close-out; for security, reconciliation and compliance conditions the default is never to go ahead (§2.3). And no internal review may delay a report to a regulator (§2.4). Section numbers in this part refer to PH01 v1.0.

| Control | Owner and trigger | Record | What B1 decided |
| --- | --- | --- | --- |
| Crisis command | Chief Executive chairs the Crisis Management Team (CMT) within 30 minutes of a severity 1 or 2 declaration; COO is alternate (§2.1) | Master decision log (§2.2) | CMT kept running at hour 72 (Q22a) |
| Regulatory reporting | Head of Legal and Compliance (LC); a second LC officer checks each clock within 30 minutes (§5.3) | Receipt of every contact (§5.5) | Commissioner called by 08:30, limit 20:00 (Q02b) |
| Customer notification | Communications (COM) sends; CEO approves the audience; LC clears the text (§10.1) | Delivery register per customer (§10.3) | Register rebuilt from evidence only (Q21b) |
| Alternate payments | CEO activates, only on written clearance from Information Security (SEC) that nothing is shared with affected systems (§8.2) | BCP activation entry; hourly reconciliation (§§4.4, 8.7) | Clearance defaulted to hold (Q10a) |
| Recovery | CEO authorises after all seven gate items: "No gate condition may be waived" (§§3, 9.3) | Evidence and signer per gate item (§9.3) | Two of 120 test items unexplained: production stayed shut (Q16a) |
| Handover | LC takes the deadline register once each open item has a signed receiver (§18.1) | Each system change dated (§18.4) | Unsigned items stayed with COM and the CMT (Q24b) |

**People and technology.** Each key role has a backup: the COO for the chair and a second LC officer for every clock (§§2.1, 5.3). Four pieces of architecture keep the controls working while core systems are down: a standby filing device off the production network and a printed contact register (§§5.4, 5.6); an alternate payment process kept apart from affected systems (§8.2); a clean rebuild from the immutable backup in an isolated recovery environment (§9.1), in line with the sectoral code \[H7 ¶6.2.20(b)(i)\]; and named vendor accounts with multi-factor authentication and recorded sessions (§7.2).

**Customers who cannot switch channel.** PH01 keeps up to 10% of alternate payment capacity for urgent cases referred by branches and the contact centre (§8.4), but sets no branch or contact-centre hours. B1's CEO set them, keeping all eight branches open until at least 20:00 and the contact centre until midnight (Q12b); PH01 should fix these hours in advance.

**Metrics.** Each control yields a measure, such as minutes from declaration to the first CMT meeting, the share of reports with a saved receipt and the share of affected customers with evidenced delivery. Part 7 sets the pass marks.

## 6. Implementation roadmap

The roadmap runs in three phases over a year, after which the testing cycle repeats. Costs are the group's planning estimates of internal staff time in person-days; Appendix D gives the basis for each. Spending on systems depends on vendor quotes we do not have, so we give no dollar figures.

| Phase and owner | Delivers | Depends on | Cost and KPI |
| --- | --- | --- | --- |
| 1. Adopt and staff (months 0–3). Chief Executive; LC for filings | Board approval of PH01; named owners and alternates; deadline tracker, printed contact register and standby filing device | Board Risk Committee approval | About 25 person-days. Every role has a named owner and alternate |
| 2. Build (months 3–9). Heads of IT Operations and Payments Operations; SEC signs off separation | Isolated alternate payment process; immutable backup and isolated recovery environment; de-sensitised test data; named, recorded vendor access | Phase 1 owners; vendor contracts that give log, audit and production rights (PH01 §6.7) | About 75 person-days, plus systems spending by vendor quote. A full restore shows no unexplained difference |
| 3. Test and embed (months 6–12, then yearly). Chief Risk Officer | The Part 7 tests; reviews; PH01 revisions | Phase 1 for tabletops and filing drills; Phase 2 for payment and restore tests | About 40 person-days a year. Part 7 pass marks met; failed tests rerun within 3 months |

Phase 1 is the cheapest and unlocks the rest: the first tabletop needs only the playbook. The plan should be reviewed after any material change to a critical computer system and at least once every two years \[L2 ¶7.2.2\].

## 7. Testing plan and tabletop results

### 7.1 What to test and how often

TM-G-2 leaves the frequency of continuity testing to the bank and expects senior management to take part each time \[H15 ¶6.1.2\]. The Commissioner's drill comes at most once every two years \[L2 ¶7.1.2\], too rarely to rely on. We propose four core tests (PH01 v1.0 sections in brackets); Appendix E adds two more.

| Test | How often | Pass threshold | If it fails |
| --- | --- | --- | --- |
| Full tabletop with all CMT roles, as in A1 and B1 | Twice a year, and within 3 months of a PH01 revision | No action scored 0; no misread trigger, deadline or recipient (no ERR); every judgment call backed by a logged search | Amend PH01 or the legal trigger check (Part 8); retest failed decisions within 3 months |
| Regulatory filing drill, out of hours, normal terminal down | Quarterly | Report sent by a permitted route within the internal target; receipt saved; clock checked within 30 minutes (§§5.3, 5.5–5.6) | Fix the route or device; repeat within a month |
| Alternate payment process | Twice a year | Written clearance before activation; pilot of at most 20 reconciled end to end; no unexplained difference (§§8.2–8.3, 8.7) | Stop, explain, re-clear; repeat within a month |
| Restore from the immutable backup | Full set yearly, and after changes to the recovery environment | No unexplained difference; a sample recorded as a sample; rollback rehearsed (§§9.2–9.3) | Production stays shut in a real incident; fix and retest |

Each test ends with a review signed off by senior management, and weaknesses go back into the plan \[H15 ¶6.1.4\].

### 7.2 Results of A1 and B1

Both runs used the same cards, 48 scored decisions and sealed regulatory expectations; B1 added PH01 and was also scored against sealed playbook expectations (Section 2.4).

|  | A1: sources only | B1: sources and PH01 |
| --- | --- | --- |
| Model and effort | Claude Fable 5.2, xhigh | Claude Opus 5.5, xhigh |
| Action score | 46 of 48 | 48 of 48 |
| Basis score | 37 of 44 | 40 of 44 |
| Total | 83 of 92 | 88 of 92 |
| Regulatory codes: OK, GAP, ERR, U | 20, 17, 7, 4 | 21, 19, 4, 4 |
| Playbook codes: OK, GAP | — | 46, 2 |
| CEO rulings counted as overrides | 12 | 18 |

The original answers and the CEO's final rulings scored the same in both runs, so each figure holds for both layers. The four undetermined units (Q04b, Q13a, Q18b, Q21a) are outside the basis denominator in both. Forty-four decisions scored the same; the gain comes from four. In the 18 decisions where only PH01 gave a direct rule, B1 applied it correctly every time. Because the runs used different models and ran once each, we credit PH01 only where the A1 answer, the PH01 clause B1 cited and the CEO's ruling line up.

**Q13b, test data (action 0 to 1).** A1 planned the offline reconciliation on live ledger extracts, without the masking and prior approval TM-G-1 requires \[H2 ¶4.2.4\]. B1's security agent made de-sensitisation and the information owner's prior approval preconditions for testing under PH01 §9.2, citing the same paragraph, and the CEO confirmed them as written. The same clause decided the next card: with two of 120 items unexplained, the test failed and production stayed shut.

**Q24a, the closing update (basis 0 to 1).** A1 justified updates at hour 72 with the HKMA's expectation of a press release "shortly after the commencement of any disruption" \[H16 ¶8.2.3\], a rule about the first notice. B1's communications agent checked PH01 §11.5's five closing conditions, found none met and issued no closing update, citing external guidance only as a general principle. The CEO adopted this, changing one default line under §11.2 so that an unverified status was reported as being checked. Q12a followed the same pattern.

**Q16a, the recovery gate (score unchanged).** Both runs scored OK, but the rulings differ. A1's CEO wrote "Any waiver of a gate condition goes back to the Board", leaving a route to waive. B1's security agent applied PH01 §3, "No gate condition may be waived": narrowing recovery to payroll could not rescue a failed test. The CEO kept the hold and added a 20:15 check that paused any alternate-process release lacking a logged clearance.

**Q23a, dated registration (action and basis 0 to 1).** A1 merged changes made on three days into one assessment and one deadline. Under PH01 §18.4, B1's legal agent split the changes awaiting assessment by deployment date, so each batch is assessed against its own one-month limit \[L1 s.22(1)\].

**Where the playbook did not help.** Four of A1's misreadings of external law recurred in B1. Q05a and Q14a misread the conditions of Cap. 455 s.25A \[L3\]; Q14b and Q15b treated the HKMA's test for scams that might give a "false impression" of coming from the bank as met without checking it \[H16 ¶4.3.2\]. All four scored OK at the playbook layer: PH01 settled who decides and by what steps, but it does not restate external triggers \[PH01 v1.0 §§1.2, 5.2\], so it could not correct how they were read. The CEO caught none either: 18 of its rulings counted as overrides, against 12 in A1, yet none changed a score. A playbook fixes the process; reading the law needs a legal check (Part 8).

These are single runs by AI agents on a fictional bank: they show where the playbook changed decisions in this exercise, not how a human team would perform.

## 8. Recommendations

### 8.1 What the bank should do first

| Action | Owner | Why |
| --- | --- | --- |
| 1. Adopt PH01 with named owners and alternates; if it forms part of the submitted emergency response plan, file every revision within one month \[L1 s.27(4)\] | Chief Executive; LC files | The controls in Part 5 need named people |
| 2. Give customer and public messages a fixed clearance slot: LC clears at a set time, a second LC officer backs up, and failing that the chair releases the verified facts | LC and COM, amending PH01 §§2.3–2.4 | In B1 the first public statement was held for LC's clearance with no end point; the CEO fixed this only at card 5 (Q25) |
| 3. Add a legal trigger check: LC records the facts that meet an external rule's trigger and a second LC officer checks them, as for deadlines (PH01 §5.3) | LC | Four misreadings recurred in B1 and no CEO ruling caught them (Section 7.2) |
| 4. Build the isolated alternate payment process and the immutable backup and recovery environment first | Heads of Payments Operations and IT Operations | In B1 recovery had not passed its gate by hour 72 (Q16a, Q22a) |
| 5. Run the Part 7 tests and report the results to the Board | Chief Risk Officer | Senior management should take part in each test \[H15 ¶6.1.2\] |

### 8.2 Reforms the group proposes

These are our proposals, not current law.

1. **A confidential ransom-payment report** within 72 hours, with limits on how it may be used, following Australia \[F4 ss.27, 29–30\] (Section 4.3).
2. **One intake for incident reports:** a shared form or single submission reaching the HKMA, the Commissioner and the PCPD, so a bank under attack files once against three clocks (Section 3.2).
3. **Mandatory PCPD notice** for breaches likely to result in "a real risk of harm", the test the PCPD's own guidance uses \[H10 p.6\], in place of today's voluntary notice \[H13 p.1\].
4. **A notice duty for critical vendors** towards the designated operator they serve, since Cap. 653 places the duty on the operator alone \[L1 s.28\] (Section 3.5).
