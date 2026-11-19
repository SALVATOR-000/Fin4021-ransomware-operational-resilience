# Evidence appendix

This appendix holds the material moved out of the report body: case timelines (A), the detailed regulatory mapping (B), the score for every decision (C), the cost basis (D) and the supplementary tests (E). Section F says where the rest of the evidence base is kept and how to reproduce the results. Bracketed IDs refer to the source register.

## A. Case timelines

### A1. ICBC Financial Services, 2023

| Date | Event | Source |
| --- | --- | --- |
| 8 Nov 2023 (US Eastern Time) | Ransomware disrupted systems; the firm disconnected and isolated them. The SEC found the malware "had blocked access to its computer systems and data by encrypting data and programs" | F5; F9 ¶2 |
| 8 Nov 2023 | The firm cut connectivity to its clearing firms and clearing agents, "impeding trading" | F9 ¶2 |
| 8 Nov 2023 | The event was not immediately communicated beyond the core affected parties; the first Core Executive Response Group meeting came "nearly 12 hours" after the attack was identified | F6 p.86 |
| 8 Nov 2023 to 1 Mar 2024 | Books and records were not kept current | F9 §III, Summary |
| 20 Feb 2024 | OFAC named LockBit as responsible and said the attack affected "the settlement of over $9 billion worth of assets backed by Treasury securities" | F8 |
| 2 Dec 2024 | SEC order against the firm | F9 |

Press reports that a ransom was paid rest on the attackers' own claim; we found no primary source and do not rely on them.

### A2. Two Hong Kong cases

| Case | Encryption found | PCPD notified | People affected | PCPD finding |
| --- | --- | --- | --- | --- |
| Hong Kong Institute of Bankers \[H11\] | 30 Dec 2021 (¶8) | 11 Jan 2022 (¶1) | Over 13,000 members and about 100,000 non-members (¶9) | Contravened DPP4(1); enforcement notice (¶¶16–21) |
| Hong Kong Cyberport \[H12\] | 14 Aug 2023, again 18 Aug (¶7) | 18 Aug 2023 (¶7) | 13,632 data subjects (¶10) | Contravened DPP4(1) and DPP2(2); enforcement notice (¶¶34–39) |

At Cyberport the hacker gained access through an administrative account on 6 August 2023, and the ransom note arrived on 17 August \[H12 ¶7\]. HKIB told the PCPD that a hacker had threatened to upload the files to the internet \[H11 ¶1\]; at Cyberport, data samples were uploaded to the dark web \[H12 ¶6\]. The PCPD's guidance asks for notice "as soon as practicable" and gives no fixed time limit \[H10 p.8\].

## B. Detailed regulatory mapping

### B1. Duties in the first 72 hours

| Phase | What the bank must do | Source | Force | Left to the bank |
| --- | --- | --- | --- | --- |
| Before an incident | Submit an emergency response plan within 3 months of designation and implement it; it must cover roles, the threshold for starting the response, reporting, investigation, recovery and communication | L1 s.27; Sch. 3 Pt 2 | Statute; fine for failing to submit (s.27(7)–(8)) | What the plan says: thresholds, approvers, handoffs |
| Contain | Analyse the cause and contain the problem as soon as practicable; customers' interests come first | H4 p.1 | HKMA circular | Whether isolating the gateway, which stops payments, is the right first move |
| Report to HKMA | Notify "immediately" once aware of a significant incident, with whatever information is available; do not wait for a fix | H4 p.2; H3 ¶2.4 | Circular; statutory guideline | What counts as "significant": the circular gives no definition |
| Notify the Commissioner | Notify as soon as practicable: within 12 hours if the incident has disrupted, is disrupting or is likely to disrupt the core function; otherwise within 48 hours | L1 s.28(1)–(2), Sch. 6 item 1 | Statute; fine up to HK$5 million on indictment (s.28(6)) | When awareness starts; four of the seven serious-incident tests use thresholds the bank sets in its continuity plan; the other three do not (L2 ¶¶7.3.4–7.3.5) |
| Follow-up filings | After a phone notice, file the specified form within 48 hours; written report within 14 days of awareness | L2 ¶7.3.6(b); L1 s.28(3)–(4), Sch. 6 items 2–3 | Statute; code of practice | Who drafts and signs; how to file if the bank's own systems are down |
| PCPD | Notice is "not mandatory" but encouraged; the HKMA expects banks to "seriously consider" it and to justify not doing so; "Oral notifications are not accepted" | H13 p.1; H9 p.3; H10 p.8 | PCPD guidance; HKMA circular | Whether to notify on suspected, not confirmed, exfiltration |
| Customers | Proactively notify affected or likely affected customers; say what they should do and whether losses will be reimbursed | H4 p.1; H9 p.3 | HKMA circulars | Who is "likely affected"; reimbursement amounts and who approves them |
| Public and other banks | Consider an announcement if an essential channel is disrupted or many customers are affected; copy materials to the HKMA; notify other affected banks | H4 pp.1–3 | HKMA circular | Timing against the risk of prejudicing an investigation (H4 p.2) |
| Ransom demand | Dealing with property known or believed to be crime proceeds is an offence; suspicion must be disclosed; prior disclosure with consent is a defence; no funds to terrorist associates | L3 ss.25(1), 25A(1)–(2); L4 (Cap. 575 s.8) | Statute | Whether paying a ransom is "dealing" in proceeds: the statute does not say |
| Restore | Set a tolerance for disruption with at least a time-based metric; designated banks should run a secure tertiary data backup, or keep a physically disconnected copy | H1 ¶4.2.1; H7 ¶6.2.20(b)(i) | Non-statutory guideline; sectoral code | When systems are clean enough to restore, and when to roll back |

### B2. Ransom payment rules abroad

**United States: deterrence through sanctions.** Where a payment has a US nexus, paying a sanctioned group can breach US sanctions on a strict-liability basis: a person subject to US jurisdiction can be liable "even if such person did not know or have reason to know" \[F1 p.4\]. OFAC names financial institutions among those who may be exposed when they facilitate payments \[F1 p.1\], and reviews licence requests "with a presumption of denial" \[F1 p.5\]. The nexus can arise through a US person, or through a non-US person who causes a US person to breach the sanctions \[F1 p.4\]. Cap. 537 gives effect only to UN sanctions \[L4\], so for a payment with such a nexus the decisive sanctions test may be US law rather than Hong Kong law. OFAC sanctioned two LockBit affiliates after the ICBC attack \[F8\]. Separately, New York requires covered entities to give notice of an extortion payment within 24 hours and a written explanation within 30 days \[F13 §500.17(c)\].

**Australia: report, but no ban.** Since 30 May 2025, businesses with turnover above A$3 million and responsible entities for critical infrastructure assets must report a ransomware payment within 72 hours of paying or learning of the payment \[F4 ss.26–27; FAQ p.1\]. The penalty is a civil penalty of 60 penalty units. No report is due when the victim refuses to pay \[F4 FAQ p.1\], and the Act limits how the government may use what it is told \[F4 ss.29–30\].

**United Kingdom: a proposed ban and a pre-payment check.** The Home Office proposed three measures: a payment ban for the public sector and regulated critical national infrastructure, a regime under which other victims declare an intent to pay, and mandatory incident reporting \[F3 p.5\]. Under the second, the government could block a payment that may reach sanctioned criminals or breach terrorist-financing law \[F3 p.28\]. Of 273 responses, 72% backed the targeted ban \[F3 p.6\]. The government said scope, including "whether the proposal would have extraterritorial effect", still needs clarity \[F3 p.26\]. It is also discussing the liability of financial institutions "asked to process potentially illegal payments" \[F3 p.27\]. These were proposals at July 2025; we have not checked whether legislation has followed.

**Incident reporting.** Hong Kong: HKMA "immediately"; Commissioner 12 or 48 hours if designated; PCPD voluntary. United Kingdom: proposed first report in 72 hours and full report in 28 days \[F3 p.42\]. United States and Australia: not reviewed.

### B3. Run A1 errors in detail

No unit was scored MISS, and all 710 citation records could be traced to their sources. Every reporting step for the original incident was right (Q02a, Q02b, Q20a, Q20b), as were the customer and PCPD notices (Q03a, Q08a, Q09a, Q15a). Where no rule existed, 17 of 19 answers logged their searches and flagged the decision as judgment, for example who may contact the attacker (Q05b). The seven errors came from applying a rule to the wrong conditions. Four were in units with a direct source (Q05a, Q14a, Q14b, Q23a); the other three relied on a rule whose trigger was not met or not yet verified (Q12a, Q15b, Q24a).

- *Misreading a statute's conditions.* The legal agent turned the consent arrangement in Cap. 455 s.25A(2) into a general precondition for paying (Q05a). It also made the disclosure duty depend on whether the ransom note gave a wallet address, although s.25A(1) turns on knowledge or suspicion \[L3\] (Q14a). In Q23a it merged production changes made on three different days into one assessment, and gave a possible new incident a flat 12-hour limit where Schedule 6 sets 12 or 48 hours \[L1 Sch. 6 item 1\].
- *Treating a trigger as met.* The HKMA expects a police report and public warning for scams "that might give the public the false impression that they originate from the AI" \[H16 ¶4.3.2\]. Two agents treated a fake verification page as meeting that test without checking it (Q14b, Q15b). Two others used the expectation to announce "shortly after the commencement of any disruption" \[H16 ¶8.2.3\] as the basis for later updates (Q12a, Q24a). In all four the action was sound and kept its action score; the legal basis was not.

The basis score counts 44 units, one more than the 43 in the coverage count. The extra unit is Q15b: the facts that would trigger the rule had not been verified, so the sealed expectation left it undetermined; the agent answered as if the trigger were met, so members scored it ERR. The CEO agent labelled 47 of its 48 rulings "CONFIRM"; under the rule agreed before the run, 12 of them changed an action, timing, recipient or threshold and count as overrides. None corrected a misapplied rule.

In B1's Q23a ruling the CEO also added a check on whether PH01 forms part of the submitted emergency response plan, since revisions must then be filed within one month \[L1 s.27(4)\]. A check of B1's quotations found none invented.

## C. Score for every decision

Codes: OK, direct source applied correctly; GAP, no direct source, search logged and judgment flagged; ERR, source misapplied; U, left undetermined, so the basis is not scored. Scores are action then basis. In both runs the original answers and the CEO's final rulings scored the same. A1 has no playbook layer.

| Unit | A1 code and scores | B1 regulatory code | B1 playbook code | B1 scores |
| --- | --- | --- | --- | --- |
| Q01a | GAP, 1, 1 | GAP | OK | 1, 1 |
| Q01b | OK, 1, 1 | OK | OK | 1, 1 |
| Q02a | OK, 1, 1 | OK | OK | 1, 1 |
| Q02b | OK, 1, 1 | OK | OK | 1, 1 |
| Q03a | OK, 1, 1 | OK | OK | 1, 1 |
| Q03b | OK, 1, 1 | OK | OK | 1, 1 |
| Q04a | GAP, 1, 1 | GAP | OK | 1, 1 |
| Q04b | U, 1, not scored | U | OK | 1, not scored |
| Q05a | ERR, 1, 0 | ERR | OK | 1, 0 |
| Q05b | GAP, 1, 1 | GAP | OK | 1, 1 |
| Q06a | GAP, 1, 1 | GAP | OK | 1, 1 |
| Q06b | GAP, 1, 1 | GAP | OK | 1, 1 |
| Q07a | GAP, 1, 1 | GAP | GAP | 1, 1 |
| Q07b | OK, 1, 1 | OK | OK | 1, 1 |
| Q08a | OK, 1, 1 | OK | OK | 1, 1 |
| Q08b | OK, 1, 1 | OK | OK | 1, 1 |
| Q09a | OK, 1, 1 | OK | OK | 1, 1 |
| Q09b | GAP, 1, 1 | GAP | OK | 1, 1 |
| Q10a | GAP, 1, 1 | GAP | OK | 1, 1 |
| Q10b | GAP, 1, 1 | GAP | OK | 1, 1 |
| Q11a | OK, 1, 1 | OK | OK | 1, 1 |
| Q11b | OK, 1, 1 | OK | OK | 1, 1 |
| Q12a | ERR, 1, 0 | GAP | OK | 1, 1 |
| Q12b | OK, 1, 1 | OK | GAP | 1, 1 |
| Q13a | U, 1, not scored | U | OK | 1, not scored |
| Q13b | GAP, 0, 1 | GAP | OK | 1, 1 |
| Q14a | ERR, 1, 0 | ERR | OK | 1, 0 |
| Q14b | ERR, 1, 0 | ERR | OK | 1, 0 |
| Q15a | OK, 1, 1 | OK | OK | 1, 1 |
| Q15b | ERR, 1, 0 | ERR | OK | 1, 0 |
| Q16a | OK, 1, 1 | OK | OK | 1, 1 |
| Q16b | GAP, 1, 1 | GAP | OK | 1, 1 |
| Q17a | OK, 1, 1 | OK | OK | 1, 1 |
| Q17b | GAP, 1, 1 | GAP | OK | 1, 1 |
| Q18a | OK, 1, 1 | OK | OK | 1, 1 |
| Q18b | U, 1, not scored | U | OK | 1, not scored |
| Q19a | GAP, 1, 1 | GAP | OK | 1, 1 |
| Q19b | GAP, 1, 1 | GAP | OK | 1, 1 |
| Q20a | OK, 1, 1 | OK | OK | 1, 1 |
| Q20b | OK, 1, 1 | OK | OK | 1, 1 |
| Q21a | U, 1, not scored | U | OK | 1, not scored |
| Q21b | OK, 1, 1 | OK | OK | 1, 1 |
| Q22a | GAP, 1, 1 | GAP | OK | 1, 1 |
| Q22b | GAP, 1, 1 | GAP | OK | 1, 1 |
| Q23a | ERR, 0, 0 | OK | OK | 1, 1 |
| Q23b | OK, 1, 1 | OK | OK | 1, 1 |
| Q24a | ERR, 1, 0 | GAP | OK | 1, 1 |
| Q24b | GAP, 1, 1 | GAP | OK | 1, 1 |

Totals: A1 action 46 of 48, basis 37 of 44; B1 action 48 of 48, basis 40 of 44. The reasons, record references and group rulings for each unit are in the scoring files listed in Section F.

## D. Cost basis for the roadmap

These are the group's planning estimates of internal staff time, not quotes. Spending on systems depends on vendor quotes we do not have.

- **Phase 1, about 25 person-days.** Two days for each of the nine Crisis Management Team members to check their sections and name alternates (18 days), five LC days for the deadline tracker, contact register and filing routes, and two days for the Board paper.
- **Phase 2, about 75 person-days.** Some 15 days to specify, test and accept each of five items: the alternate payment process, the immutable backup and isolated recovery environment, de-sensitised test data, named and recorded vendor access, and the delivery register tool.
- **Phase 3, about 40 person-days a year.** Two tabletops at about 7.5 days each (nine members for half a day, plus 3 days to prepare and score), four filing drills (about 2 days in all), two payment drills (about 8 days), a full restore test (about 10 days) and two delivery drills (about 3 days).
- **Scale of a tabletop.** Each of our runs took under two hours to play (A1 90 minutes, B1 112 minutes), and scoring and review took several hours more.

Further KPIs not shown in the report table: the standby filing device is logged as working on each designated channel (Phase 1); any revision of a submitted plan is filed within one month \[L1 s.27(4)\] (Phase 1); SEC's separation clearance passes in a test and every vendor session is named and recorded (Phase 2).

## E. Supplementary tests

The report keeps four core tests. Two more complete the programme (PH01 v1.0 sections in brackets).

| Test | How often | Pass threshold | If it fails |
| --- | --- | --- | --- |
| Customer notice and delivery register | Twice a year | Evidenced delivery for every customer in a test batch; no links; verified contact details only (§§10.2–10.3, 10.5) | Correct the data; repeat |
| Vendor credential closure | After every change to vendor access | Replayed token and old credential both fail (§7.4) | Access treated as open |

TM-G-2 says a bank should set its testing frequency by the potential impact of a disruption, the number of critical operations and whether the operating environment has materially changed \[H15 ¶6.1.2\]. The full restore test should also be rerun after any change to the recovery environment.

## F. Where the rest of the evidence is, and how to reproduce the results

- **Source register.** The 来源清单 tab of this document lists all 39 sources with links; the originals are in the folder `Primary source/原文/`.
- **Tabletop script and playbook.** The 推演剧本 tab holds the script; PH01 v1.0 is in `推演记录/PH01/`.
- **Run records.** Sealed answers, CEO rulings, read logs and checksums are in `推演记录/A1/`, `推演记录/B1/` and the archived test round `推演记录/B0 测试轮 · Opus 5.5 Medium/`.
- **Sealed expectations.** The folder `组员预注册/` holds the expectations sealed before each run, with their SHA-256 files.
- **Scoring files.** `推演记录/A1/核验/` and `推演记录/B1/核验/` hold the per-unit scores with reasons and the citation checks.
- **Reproducing the scores.** Run `python3 -I 推演记录/转换脚本/merge_scores_b1.py 组员预注册/岚汐银行-B1评分表-v1封存.csv 推演记录/A1/核验 推演记录/B1/核验` from the project folder; it rebuilds the score sheets and prints the totals. `推演记录/转换脚本/verify_quotes.py` repeats the citation check, and `推演记录/B1/B1校验.sha256` verifies the 87 B1 record files.
- **AI use.** The correction and AI-use log is in section 4 of the 计划与分工 tab.
