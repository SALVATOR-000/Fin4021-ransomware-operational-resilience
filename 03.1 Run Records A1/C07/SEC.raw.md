SEC RESPONSE - C07 (Wed 18 Nov 2026, 12:00 HKT, H+52) - Unit Q19 a and b. Locked before colleagues' answers.

Internal bank procedure (PH01): N/A for both units. PH01 is not in my allowed manifest, so no internal basis and no conflict check is possible.

Fact status I am working from
- Released by the card: a forensic partner delivered time-stamped records from the gateway, the identity provider and the vendor remote access service; some clocks differ by up to four minutes; a new indicator seen in the incident has appeared on a quarantined host, relationship to the original compromise unverified; a validated file identifies the same 320 customers and corrects contact details for 12; 31 customers report suspected scams; attribution is unverified.
- From the facilitator's handoff: gateway isolation and the evidence hold are in force; the standby gateway and vendor access are on hold; the recovery image has not been used in production and no gate condition is recorded as met. Not verifiable from any card: my C01 validation results, completion of evidence items, the C03 replay and logon tests, secret rotation and persistence removal, and whether the secondary process's seven gates and pilot were cleared.
- Unknown: which host carries the new indicator, what type of indicator it is, and whether it appeared before or after the host was quarantined.

---

Q19a - A reviewable technical timeline, with clock offsets and uncertainties

Decision. SEC produces one master timeline from the three delivered record sets, the bank's independent logs, the incident log and the evidence register. Original records are never altered. Every entry carries its source time, the measured offset, a normalised time and a stated uncertainty, so that a reviewer can re-derive it. Where the uncertainty is larger than the gap between two events from different sources, their order is recorded as undetermined.

Method (professional judgment)
1. Reference clock. HKT (UTC+8) from the bank's primary time source.
2. Offsets table, built first. For each source: system name, its time zone and stated time source, the offset against the reference (sign and size), how it was measured, when, and by whom. Offsets are obtained by:
   - direct comparison where a system is still running, including readings taken under C01 evidence item 7;
   - anchor events, meaning the same action recorded in two sources (for example a sign-in at the identity provider and the matching session start at the vendor service and logon at the gateway);
   - a three-way consistency check: the gateway-to-identity offset plus the identity-to-vendor offset should equal the gateway-to-vendor offset within tolerance.
   Offsets are measured at more than one point in the period, because drift may not be constant.
3. Entry format. Each timeline row records: source system; original timestamp exactly as logged, with zone; offset applied; normalised HKT time; uncertainty in seconds (timestamp resolution, offset measurement error, drift, log-write delay); event description; evidence register reference and hash; status (confirmed, inferred or unverified); analyst; reviewer.
4. Ordering rule. Events from the same source keep that source's internal order. Events from different sources closer together than their combined uncertainty are flagged "order undetermined". No sequence is asserted for them.
5. Fact and hypothesis kept apart. Hypotheses are labelled. Attribution is not stated. Periods with no log coverage are listed as gaps, not left blank.
6. Structure. Phases: first access, credential use, movement, data access, export, encryption, detection, containment, recovery. Bank decisions are included with the decision-maker and the time taken from the incident log.
7. Reproducibility. Normalisation is done on a working copy by a script kept under version control; the script, its version and the input hashes are recorded.
8. No customer personal data. Individuals appear by internal reference only.
9. Review. Each version is numbered with a change log. An analyst prepares; an independent reviewer (the forensic partner or internal audit) traces a sample of rows to evidence and re-runs the normalisation; SEC signs.

Timestamps where four minutes matter (these are given to LC with the source time and the uncertainty both shown)
- Earliest identifiable time of the incident, and the time the bank became aware.
- First use of the vendor credential, and the export of the customer file.
- Credential revocation against last attacker activity. If the two are within the uncertainty, SEC reports that activity after revocation cannot be excluded.
- Quarantine of the host against first appearance of the new indicator (feeds Q19b).

Outputs: the master timeline; the offsets table; an assumptions and uncertainty register; a summary timeline for LC's reports.

Accountable owner: SEC. Executing parties: bank forensic staff with the forensic partner (preparation), an independent reviewer, the vendor (to state its service's clock source and zone, as asked in C02).

Time (judgment targets): offsets table by 14:00 HKT; timeline v1 by 18:00 today; independent review complete by 12:00 on Thu 19 Nov; updated daily and on new evidence. A reviewed baseline for LC's written incident report by Wed 25 Nov. The statutory date for that report is LC's unit; on my reading of R01 Schedule 6 item 3 it is 14 days after the awareness date.

Destination and channel: restricted incident workspace; versions to the Chief Executive, LC and the privacy officer; the evidence register records each version and its hash.

Basis
- R02, OCCICS Code of Practice (Generic), s.7.2.3(a)(v)(3)-(4), PDF p.32: playbooks for "Investigating the cause and impact of the incident;" and "Recording the incident response process, including details of the incident, actions taken and decisions made;". Code under Cap. 653 s.8, reached for designated banks through R03 s.1.1.3. It requires the investigation and the record; it does not say how to build a timeline.
- R02 s.6.2.23(g), PDF p.20: "The CI operator should synchronise the internal clocks of all CCSs components with a primary time source to enable accurate log-event correlation across the systems." Generic-code text. It covers the gateway's components; the identity provider and the vendor service may sit outside it. I use it as the principle for choosing one reference clock. The four-minute spread shows synchronisation was not uniform, which is itself a finding to record.
- R03, HKMA Sectoral Code, s.6.2.23(d), PDF p.18: "Retained logs should contain sufficient information to support after-the-fact investigation of computer-system security incident(s)".
- R02 Annex E items B(3)-(4), PDF p.42: "Earliest Identifiable Time of the Incident" and "Time Becoming Aware of the Incident"; Annex F items B(3)-(4), PDF p.43: "Initial Attack Vector / Point of Intrusion" and "Root Cause Analysis Summary". The timeline has to support these fields. R02 s.7.3.7(a), PDF p.37: "If additional information become available after submitting the written report, the CI operator should also provide such information to the Commissioner as supplementary material." This is why versions are kept.
- R06, SPM OR-2, s.8.3, PDF p.13: "Root cause analysis of incidents to help with the prevention or minimisation of recurrence." R08, SPM TM-G-1, s.3.3.1, PDF p.13: the security function covers "performing incident analysis, reporting and investigation". HKMA supervisory guidance.
- R11, PCPD Guidance, PDF p.4, Step 1: "When did the breach occur?"; PDF p.6, Step 5: "A comprehensive record of the incident is therefore required, which should include all facts relating to the breach". Non-binding.
- R01, Cap. 653, s.35(1)(a), PDF p.50: an authorised officer may require documents relevant to an investigation. No notice is recorded; a traceable timeline keeps the bank able to respond.

No direct rule located in assigned sources for recording clock offsets, uncertainty, anchor events, the ordering rule or independent review of a timeline. Files: all. Terms: regex "clock|time source|time-?stamp|synchroni[sz]" (relevant hit R02 p.20 only); regex "timeline|chronolog|sequence of events" (no relevant hit). These are professional judgment.

---

Q19b - Retain, raise or reduce monitoring and containment

Decision.
- Containment: retain everything in force. Nothing is reduced or lifted.
- Monitoring: raise.
- Containment is raised selectively, on the triggers below.
- The recovery hold stays, and a ninth condition is added to the C06 gate: the new indicator is classified and the hunt for it is clean in the recovery environment.
- The unverifiable items in the handoff are closed out today, because a new indicator combined with unrecorded validations means residual attacker access cannot be excluded.

Simulated actions for the log

| Step | Operator | Action | Target (HKT) |
|---|---|---|---|
| 1 | Forensic staff | Preserve the quarantined host's memory and disk before any other work; confirm it has no network path; fix the indicator's first-seen time against the quarantine time using the Q19a offsets | 12:30 |
| 2 | Security Operations Centre | Detection rules for the indicator on endpoints, network and identity provider; alerts go to immediate analyst review, staffed round the clock; hourly report to the Chief Executive until classified | 13:00 |
| 3 | Security Operations Centre, forensic partner | Search back through retained logs and across all environments for the indicator: production, recovery environment, secondary-process hosts, backup systems, identity provider | 16:00 |
| 4 | Identity admins | Review sign-ins and token issue since the C03 revocation for vendor and privileged accounts | 16:00 |
| 5 | SEC with IT Operations | Perform or re-perform and record the C03 replay and logon tests, the secret rotation and the persistence removal | 16:00 |
| 6 | SEC with payments operations | Establish and record the actual state of the secondary process and each of its seven C04 gates | 14:00 |
| 7 | Fraud monitoring team, on SEC recommendation | Heightened monitoring on the 320 customers' accounts; indicators from the 31 scam reports (numbers, addresses, account details) fed into monitoring and blocking | 14:00 |
| 8 | SEC | Preliminary classification of the indicator | 18:00 |

Classification and what follows (professional judgment)
- Related, and present before quarantine: an old artefact. Retain containment, keep raised monitoring, update the timeline and scope.
- Related, and appearing after quarantine: treated as live activity or a timed mechanism. Disconnect the host physically, review the quarantine rules, isolate neighbouring systems, and consider a second foothold.
- Unrelated or a tooling artefact: recorded with the evidence; monitoring stays raised until the reduction criteria are met.

Triggers that raise containment
- The indicator on any other host: that host is isolated at once. If it supports a live customer service, the Chief Executive decides, unless destructive activity is under way, in which case SEC acts and reports immediately (the C01 rule).
- The indicator in the recovery environment: the candidate fails and is rebuilt (the C05 stop trigger).
- The indicator on secondary-process hosts, or any C04 gate found unmet at Step 6: releases pause until the gate is met and recorded (the C04 stop trigger).
- Any sign-in or token use by a revoked identity: treated as active intrusion under C03.
- If the indicator is a network address or domain: blocked at the perimeter.

Criteria for any later reduction (none is met now): indicator classified; hunts clean for seven consecutive days; Step 5 results recorded; forensic partner's confirmation; Chief Executive approval on a change record, with reductions made one at a time.

Accountable owner: SEC. Executing parties: as in the table.

Time: as in the table. Next review 08:00 on Thu 19 Nov, or immediately on any trigger.

Destination and channel: monitoring, endpoint, perimeter and identity systems under emergency change records; hourly status to the Chief Executive and LC on the out-of-band bridge; all entries in the incident log.

Basis
- R03 s.6.2.26(a)-(b), PDF p.19: "A Designated AI should implement measures to detect computer-system security incidents affecting CCSs" and "should monitor and analyse threat intelligence in relation to CCSs, and take appropriate actions". Sectoral code under Cap. 653 s.8; applies to the designated gateway. The detailed control principles it cites are in C-RAF, which is not in my manifest.
- R02 s.6.2.26(d), PDF p.22: "Procedures and processes should be in place to ensure 24 x 7 monitoring and a timely response to any security events". Generic-code text, used as principle for round-the-clock coverage.
- R08 s.6.1.4, PDF p.22: "The network should be monitored on a continuous basis." s.6.2.3, PDF p.23: "Network operational personnel should be alerted on a real-time basis to potential security breaches." HKMA supervisory guidance.
- R05, HKMA circular, PDF p.1, "Immediate incident response" (checked against the scan in C01): "The AI concerned should immediately analyse the cause of the incident and as soon as practicable rectify or contain the problem." The new indicator means the problem is not shown to be contained.
- R10, Cap. 486, Schedule 1, Principle 4(1), PDF p.169: personal data is to be "protected against unauthorized or accidental access, processing, erasure, loss or use". Binding; the wider data set is still at risk while residual access is unexcluded.
- R09, SPM TM-E-1, s.8.1.1, PDF p.31: "AIs should take appropriate remediation actions to deal with suspicious transactions and unusual activities in a timely manner even after office hours." s.8.1.2: "AIs should take into account any fraud intelligence gathered from internal or external sources." Supports Step 7.
- R08 s.4.3.2-4.3.3, PDF pp.19-20 (quoted in C01): emergency changes approved, logged and backed up.
- Fact for LC, not my decision: R02 s.7.3.2, PDF p.35, says "a computer-system security threat that is detected and timely removed or quarantined" does not constitute an incident, and s.7.3.5, PDF p.36, ties awareness to "a reasonable degree of certainty". Whether the indicator is part of the reported incident, a contained threat, or a separate incident with its own clock depends on my classification. I will tell LC the moment that classification is reached, with the time and its uncertainty.

No direct rule located in assigned sources for when to raise or reduce monitoring after a new indicator, the hunt scope, the seven-day criterion or the classification outcomes. Files: all. Terms: regex "indicators? of compromise|threat hunting|threat intelligence|quarantin"; "containment"; "isolat". These are professional judgment: an unexplained indicator plus unrecorded validation results does not support any relaxation.

---

Facts SEC passes to the incident team (13:00 hourly status; 14:00, 16:00 and 18:00 results)

| Fact | Status at 12:00 | Used by |
|---|---|---|
| Clock differences | Up to four minutes between sources; every time SEC supplies carries its source and uncertainty | LC (Q20) |
| Awareness time and other statutory timestamps | Supplied from the timeline with uncertainty; where it matters SEC shows the earliest plausible time | LC |
| New indicator | Present on a quarantined host; relationship unverified; classification due 18:00 | LC, Chief Executive |
| Possible separate incident | Not determined; depends on classification | LC |
| Containment | All in force; none reduced | Chief Executive, COM |
| Recovery | Hold continues; ninth gate condition added | Chief Executive, COM (no restoration time) |
| Secondary process | State and gates being verified by 14:00; releases pause if a gate is unmet | Chief Executive, COM |
| Affected customers | 320 confirmed, unchanged; 18,000 claim still unverified | LC, COM |
| Contact corrections for 12 customers | From the validated file; supplied by internal reference through the restricted workspace | COM (Q21b) |
| Scam reports | 31 reported; SEC collects the indicators as evidence and for blocking; no link to the attacker is established | COM (Q21a), LC |
| Attribution | Unverified; not stated in the timeline or any SEC output | LC, COM |
| Notification dispatch record | SEC holds none and cannot attest to it | LC |

Limitations: text search and page reads only. Not available to me: the delivered record sets themselves, C-RAF, the bank's plans, and the records of earlier validation steps.