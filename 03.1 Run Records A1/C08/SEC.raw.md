SEC RESPONSE - C08 (Thu 19 Nov 2026, 08:00 HKT, H+72) - Unit Q22 a and b. Locked before colleagues' answers.

Internal bank procedure (PH01): N/A for both units. PH01 is not in my allowed manifest, so no internal basis and no conflict check is possible.

Fact status I am working from
- Released by the card: a second offline test reconciled all 240 sampled instructions, using a rebuilt access environment; the offline environment has shown no new alarms in six hours; these results describe the test environment only; vendor credential questions, customer cases and regulatory follow-ups are unresolved.
- From the facilitator's handoff: the production decision is hold. In force: gateway isolation, evidence hold, standby gateway hold, vendor accounts disabled and vendor path blocked, recovery hold, raised monitoring since 13:00 on 18 Nov. None of the nine gate conditions is recorded as met. Not recorded anywhere: the indicator's classification, the search results, the re-performed C03 tests, and the verified state of the secondary process and its gates.
- Unknown: how the vendor credential was obtained; whether it was shared or single-factor; why the first test's two mismatches occurred; whether production has the same rebuilt access environment as the test.

---

Q22a - Restrictions to keep or release, and the handover to standing operations

Decision. Keep every restriction. SEC releases none at this card. The second test is logged as progress towards gate condition 2, not as a pass of the gate. The incident moves from crisis handling to managed recovery under the standing operations team, with decision rights unchanged.

Why the new test does not justify a release (professional judgment)
- It is a sample of 240 on an offline image. My ten reconciliation checks and the explanation of the first two mismatches are not recorded.
- It ran on a rebuilt access environment. Production has no recorded equivalent, and the access route is the open question in Q22b.
- Six alarm-free hours offline is short of the seven clean days set at C07, and the indicator is not recorded as classified.
- No gate condition is recorded as met, so the Chief Executive has nothing to sign.

Restrictions register

| Restriction | Decision | Release condition | Decision-maker |
|---|---|---|---|
| Isolation of the original gateway segment (C01) | Keep | Not released for return to service; decommissioned after evidence release | SEC with LC |
| Evidence hold on the original gateway and quarantined host (C01, C07) | Keep | LC's preservation decision plus SEC release per item | LC and SEC |
| Standby gateway hold (C01) | Keep | Same integrity and separation checks as the recovery candidate | SEC |
| Vendor accounts disabled, vendor path blocked (C03) | Keep | Closure evidence in Q22b | SEC, then Chief Executive |
| Recovery hold and nine-condition gate (C06, C07) | Keep | All nine conditions recorded | Chief Executive |
| Secondary process as the only service mode, with its verification, duplicate gate and hourly reconciliation (C04) | Keep | Replaced stage by stage after the gate | Chief Executive |
| Mobile transfer submission closed | Keep | Stage 3 of the recovery plan | Chief Executive |
| Raised monitoring: indicator rules, round-the-clock review, heightened watch on the 320 accounts (C07) | Keep | Indicator classified, seven clean days, C03 test results recorded, forensic partner's confirmation | Chief Executive on a change record |
| Stop and rollback criteria (C06) | Carried over | Apply from the first production transaction | Three duty holders |
| Hourly status to the Chief Executive | Keep; may move to four-hourly once the indicator classification is recorded as an old artefact or unrelated | As stated | Chief Executive on a change record |

Handover pack for the standing operations team
1. The restrictions register above, with a named owner for each line.
2. Gate status sheet: nine conditions, evidence needed, recorded status (none met), and the second test entered under condition 2 as "sample re-run 240 of 240; ten checks and mismatch explanation outstanding".
3. Open verification list: every result no card records. This covers C01 validations and evidence items; C03 replay tests, rotation and persistence removal; the C04 gates and secondary process state; C05 checks 1-8, separation checks and the ten reconciliation checks; the C06 mismatch classification; and the C07 indicator classification and search results. Also the secure filing terminal release that the Chief Executive ordered at C04, where no record of completion is on any card supplied to me.
4. Monitoring runbook: indicators, detection rules, all triggers from C01 to C07, escalation contacts and the round-the-clock roster.
5. Technical timeline (current version), offsets table, and the scope statement: 320 customers confirmed, 18,000 claim unverified.
6. Secondary process instructions, the instruction register and checkpoint records.
7. Stop and rollback criteria and the four-stage plan.
8. Vendor file: Q22b status and the C02 evidence request.
9. Decision rights and the rule for reconvening the crisis management team: any trigger in item 4.
The evidence register and sealed masters stay with the SEC evidence custodian and are not handed over.

Simulated actions for the log: 08:00 review under C07 concluded as "retain". 09:00 pack issued. 10:00 joint walkthrough, with named receiving owners signing acceptance; until they sign, the incident team keeps responsibility. 18:00 first status from the standing team.

Accountable owner: SEC stays accountable for the security conditions and the stop authority after handover. Executing parties: head of IT Operations (receiving owner for service and recovery), Security Operations Centre manager (monitoring), payments operations lead (secondary process). Gate decision: Chief Executive.

Time (judgment targets): as in the actions. The gate review is convened only when conditions 1-7 and 9 are recorded; no date is promised.

Destination and channel: handover pack in the restricted incident workspace; acceptance recorded in the incident log and the problem management record.

Basis
- R03, HKMA Sectoral Code, s.6.2.16(a), PDF p.15, pointing to R08, SPM TM-G-1, s.4.2.4, PDF p.18: "only properly tested and approved systems are promoted to the production environment". Authority and scope as in C06. An offline sample does not complete the testing or the approval.
- R08 s.5.1.3, PDF p.20: a problem management system is "to record, analyse and keep track of all these incidents until rectification of the incidents". HKMA supervisory guidance. It supports tracked handover with open items. It does not prescribe a handover pack.
- R07, SPM TM-G-2, s.4.2.2, PDF p.10: the crisis process covers "the process for overseeing the recovery and restoration efforts of the affected facilities and the business services". Recovery is not complete, so the Chief Executive's oversight continues.
- R03 s.6.2.26(a), PDF p.19: "A Designated AI should implement measures to detect computer-system security incidents affecting CCSs". R02, OCCICS Code of Practice (Generic), s.6.2.26(d), PDF p.22: "24 x 7 monitoring and a timely response to any security events" (generic-code text, used as principle). Supports keeping raised monitoring.
- R09, SPM TM-E-1, s.9.4.1, PDF p.35: "It is important that the actual effectiveness of the resilience of the system should be properly verified and tested." R09 s.9.5.4, PDF p.37, on other channels providing "an acceptable level of service" supports keeping the interim process.
- R13, HKMA circular of 1 June 2026, PDF p.2: "proper transition to "business-as-usual" is required", with staff equipped "to take ownership". Written about resilience programmes; used as principle for named owners.
- R01, Cap. 653, s.27(5), PDF p.43: "A CI operator must implement an emergency response plan." Missing fact: the plan's stand-down and handover terms; if it sets them, they govern.

No direct rule located in assigned sources for when an incident team may hand over, what a handover pack contains, or criteria for releasing restrictions. Files: all. Terms: regex "handover|hand-?over|closure of|close the incident|business.as.usual|lessons learn|post-incident"; regex "staged|phased|in phases|pilot|go/no-go|resumption criteria|resume normal". These are professional judgment.

---

Q22b - Root cause remediation and the evidence needed to close the vendor credential issue

Decision. The vendor credential issue stays open and vendor access stays disabled. The root cause is not yet established: use of the vendor credential is the route, not the cause. SEC assigns remediation now on the confirmed contributing factors, marked provisional, and sets the closure evidence below. Closing the issue does not release any evidence.

Remediation assignments (owners are assumed role names; dates are judgment targets)

| Area | Action | Owner | Due |
|---|---|---|---|
| Root cause analysis | Establish how the credential was obtained and why controls did not stop or detect its use; preliminary finding for LC's report, then final | SEC with the forensic partner | 25 Nov; final 18 Dec |
| Vendor and privileged access | Individual named accounts, multi-factor authentication, time-limited access through the privileged access system with session recording, least privilege, no reach to customer data | Head of IT infrastructure and identity | Before any reinstatement; all vendors by 18 Dec |
| Other vendors | Review every third-party remote access account for the same weakness | SEC | 3 Dec |
| Data placement | Explain and correct why records of up to 18,000 customers sat in a workspace reachable by a support credential | Payments information owner with the privacy officer | 3 Dec |
| Vendor contract and oversight | Security duties, incident reporting, log keeping and audit rights confirmed or amended; decision to retain or exit the vendor | Vendor relationship owner with LC | 18 Dec |
| Logging and clocks | Close log gaps; synchronise all sources to the primary time source | Head of IT Operations | 3 Dec |
| Detection | Earlier detection of unauthorised commands and bulk exports | Security Operations Centre manager | 18 Dec |
| Recovery readiness | Standby and backup suitability tested; capacity of the interim process against demand; review after plan activation | Business continuity owner | 18 Dec |
| Incident records | Every gate, test and validation recorded at the time it is done | SEC | Immediately |
| Independent assurance | Vulnerability assessment and penetration test of the rebuilt gateway and remote access route; internal audit review of closure evidence | SEC to arrange; internal audit | Before production stage 3 |
| Post-incident review | Facts, causes, control gaps, plan effectiveness, improvements | SEC for the crisis management team | 18 Dec |

Evidence required to close the vendor credential issue (all items, each entered in the evidence register)
1. Cause. The vendor's written incident findings on how the credential was exposed, checked by the forensic partner against the records delivered at C07.
2. Identity. Whose credential it was, whether it was shared, how it authenticated, and what it was entitled to reach.
3. Session reconciliation. Every session of the credential matched between bank and vendor records on the Q19a timeline, with none unexplained.
4. Closure proof. Recorded results of the replay and logon tests (both failing), empty session tables, the revoked token and key inventory, and the closure time.
5. No further use. Identity provider review showing no sign-in or token use from closure to the end of the 30-day watch on 16 Dec.
6. Secrets. An inventory of every secret readable from the session, with rotation time and a test result for each.
7. Persistence. Findings and removal records; the indicator classified; searches clean in all environments for seven consecutive days.
8. Extent. All other accounts of this vendor, and the other-vendor review, completed with results.
9. New design proven. The redesigned access route built and independently tested.
10. Vendor's data holdings. An inventory of bank data held by the vendor. Return or destruction only after LC lifts preservation.
11. Contract and assurance. Amended terms or written confirmation; the bank's assessment of the vendor's remediation.
12. Sign-off. Internal audit review; SEC, the payments information owner and the Chief Executive sign; LC confirms the root cause has been reported where required.

Accountable owner: SEC. Executing parties: as in the table; the vendor for items 1, 3 and 10.

Time and triggers: dates as in the table. Observable trigger for closure: all twelve items recorded and signed. Any use of a revoked identity reopens the issue at once and is treated as active intrusion.

Destination and channel: remediation register held by the standing operations team in the problem management record; closure file in the evidence repository; summary to the Chief Executive and LC.

Basis
- R02 s.7.2.3(a)(v)(5), PDF p.32: "Conducting a post-incident review." s.7.2.3(i), PDF p.33: "The post-incident review should incorporate lessons learned to improve future response and preventive measures", including "Facts and causes of the incident;". Code under Cap. 653 s.8, reached through R03 s.1.1.3. It applies to this incident; it sets no dates.
- R01 Schedule 3 Part 2 item 7, PDF p.93: the emergency response plan covers "The recommended post-incident measures for mitigating the risks of, and preventing, the recurrence of computer-system security incidents." Missing fact: the plan's own measures.
- R02 Annex F item B(4), PDF pp.43-44: "Root cause(s) of the incident and contributing factor(s):" and "Whether the root cause was identified in previous security assessment or audit:"; item D(3)-(4), PDF p.46: "Measures planned to strengthen security and prevent re-occurrence" and "Timeline for implementing the remedial measures?". The remediation table feeds these fields; submission is LC's unit.
- R06, SPM OR-2, s.8.3, PDF p.13: "Root cause analysis of incidents to help with the prevention or minimisation of recurrence." R13, PDF p.3: "There should also be a clear risk-based framework for determining the timeline and priority of remediations." R07 s.6.2.1, PDF p.18: "In the event that a plan has been activated, a review should be carried out once normal operations are restored to identify areas for improvement."
- R03 s.6.2.10(a)(ii), PDF p.13, points to TM-G-1 ss.3.2.1, 3.2.2 and 3.3.1. R08 s.3.2.1, PDF p.12: "all users should be identified by unique user-identification codes (e.g. user IDs) with appropriate method of authentication (e.g. passwords) to ensure accountability for their activities". s.3.2.2: "Stronger authentication methods should be adopted for transactions/activities of higher risk". R03 s.6.2.11(a), PDF p.14, points to TM-G-1 s.3.2.3, PDF p.12: "granting of authorities that are strictly necessary to privileged and emergency IDs". R03 s.6.2.13(b), PDF p.14: "where a password is the single authentication factor used by suppliers for maintenance and support, the password should be changed after every use". These apply to access to the designated gateway and support the access redesign and evidence items 2 and 9.
- R02 s.6.2.10(f), PDF p.14: "Shared or group user-IDs should not be permitted unless strictly necessary." s.6.2.11(b): "just-in-time privileged access for temporary privilege elevation, subject to a formal approval and control procedure". Generic-code text, used as principle.
- R16b, HKMA circular "Customer Data Protection", Annex I, PDF p.8: "AIs should implement effective controls to monitor and validate the service providers' compliance situation." Annex C(vii), PDF p.5: service provider remote access "should be subject to robust authentication (e.g. two-factor authentication)".
- R12, SPM SA-2, s.1.3.5, PDF p.4: "Where there are deficiencies identified in any outsourcing arrangements, AIs should take appropriate action to rectify them". s.2.5.2, PDF p.6: "access rights to AIs' data delegated to authorized employees of the service provider on a need basis". s.2.6.5, PDF p.7: "The control procedures over the outsourcing arrangement should be subject to regular reviews by the Internal Audit." Missing fact: whether this arrangement is outsourcing as R12 defines it; otherwise used as principle.
- R10, Cap. 486, Schedule 1, Principle 4(2), PDF pp.169-170 (quoted in C02), conditional on the vendor being a data processor. R11, PDF p.9: review should consider "The strengthening of the monitoring and supervision mechanisms for employees, agents and data processors."
- Facts for LC, not my decisions: R01 s.23(4), PDF p.36, a revised security management plan must be submitted "within 1 month after the date on which the revision is made"; R01 s.24(5), PDF pp.37-38, the regulating authority "may, by written notice, require the CI operator" to conduct a risk assessment after a notified change. No such notice is recorded.

No direct rule located in assigned sources for the twelve closure items, the seven-day and 30-day periods, the remediation dates or the reinstatement tests. Files: all. Terms: regex "revok|revoc|credential"; "session"; "token"; regex "remote access|remote connection|remote support|vendor"; regex "handover|hand-?over|closure of|close the incident|business.as.usual|lessons learn|post-incident". These are professional judgment. C-RAF and the HKMA third-party circular of 21 December 2023, both cited by R03, are not in my manifest.

---

Facts SEC passes at handover

| Fact | Status at 08:00 | Used by |
|---|---|---|
| Production position | Hold; interim secondary process only; no restoration date | COM (Q24a: conditional wording), Chief Executive |
| Second offline test | 240 of 240 on a sample in the test environment; not a production result and not a gate pass | COM, LC, Chief Executive |
| Gate | Nine conditions; none recorded as met | Chief Executive, LC |
| Restrictions | All kept; none released | COM, LC |
| Indicator from C07 | Classification not recorded | LC (possible separate incident question from C07 remains open) |
| Vendor credential | Open; twelve closure items; vendor access disabled | LC (Q23a register of commitments), COM |
| Root cause | Not established; preliminary finding due 25 Nov | LC (written report), COM (no cause to be stated) |
| Evidence | All holds in force; SEC releases nothing without LC's preservation decision | LC (Q23b) |
| Affected customers | 320 confirmed; 18,000 claim unverified; heightened account monitoring continues | COM (Q24b), LC |
| SEC dates others depend on | 25 Nov preliminary root cause; 3 Dec and 18 Dec remediation items; 16 Dec end of the 30-day watch | LC (register of deadlines) |

Limitations: text search and page reads only. Not available to me: the test reports, the bank's plans, the vendor contract, and the records of earlier validation steps.