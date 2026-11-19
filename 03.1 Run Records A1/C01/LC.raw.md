LC response, C01 Q02 — locked at 08:00 HKT, Monday 16 November 2026 (H+0), before colleagues' answers.

Both paths are triggered and both go by telephone within the first 30 minutes. Neither waits for root cause, failover verification or the secure filing terminal. They are separate duties: telling the HKMA does not discharge the Cap. 653 notification, and the reverse is also true.

Internal bank procedure: N/A for both units. PH01 is not in my allowed manifest (search "PH01", all documents: 0 hits).

## Q02a — Initial HKMA report

**Decision and action.** Report now as a significant incident: I telephone the HKMA, then send a written confirmation. No hold for rectification or missing facts.
- Condition 1: SEC confirms the one-page fact sheet (a five-minute check, not an approval gate).
- Condition 2: SEC confirms corporate email is safe to use. If not, I agree an out-of-band written route with the HKMA contact on the call.

**Information to send now** (confirmed facts only; unknowns stated as unknown):
- Confirmed at 08:00 HKT: unauthorised commands encrypted components of the payment gateway.
- Impact: outbound domestic transfers and payroll submission are disrupted.
- Still available: mobile balance viewing; all eight branches open.
- Scale: 180,000 retail and 12,000 SME customers on the book; number actually affected not yet known.
- Unknown: cause and entry point, earliest time of the activity, whether any data was accessed or taken, failover capability (unverified), expected duration.
- Under way: containment and evidence preservation (SEC); customer communication decision (COM).
- Cap. 653: the gateway is a designated critical computer system and a section 28 notification is being made to the Commissioner by telephone this morning.
- Named contacts and the time of the next update.
- Not to be said: the label "ransomware" (no ransom fact on the card), any restoration time, or any statement that customer data is unaffected.

**Owner and executing party.** LC is accountable and makes the call. SEC confirms the technical facts. The Chief Executive or incident lead is informed at the same time; no assigned source makes management approval a precondition, so I do not make it one (judgment).

**Trigger, awareness point and clock.**
- Trigger: the bank becomes aware of a significant incident.
- Awareness point: 08:00 HKT, 16 November 2026.
- Clock: "immediately". No hour figure exists in the assigned sources.
- My targets (judgment): call by 08:15 HKT; written confirmation by 08:45 HKT; next update at 10:00 HKT.
- Earlier update triggers: failover result, BCP activation, any sign of data compromise, or any public statement.

**Recipient and channel.** HKMA, through the bank's usual Banking Supervision contact, by telephone and then email (judgment). No direct rule located in assigned sources for the channel, form or contact point.

**Basis and application.**
- Direct rule: R05, HKMA circular "Incident response and management procedures", PDF p.2, heading "Reporting incident to the HKMA", sole paragraph. Quotes checked against the scan:
  - "once an AI has become aware that a significant incident has occurred, the AI concerned should notify the HKMA immediately and provide it with whatever information is available at the time"
  - "an AI should not wait until it has rectified the problem before reporting the incident to the HKMA"
  - Status: supervisory circular to all authorized institutions, not statute. Scope: the bank is a licensed bank.
- Judgment: R05 does not define "significant incident". I classify this as one because a confirmed unauthorised act has stopped transfers and payroll at a bank of this size on a Monday morning.
- Supporting, R09 SPM TM-E-1 para 8.2.5 (p.33), statutory guideline under Banking Ordinance s.7(3): "should notify the HKMA promptly in accordance with the relevant arrangements set out by the HKMA from time to time". Those arrangements are not in my manifest.
- Supporting, R04 SPM TM-C-1 para 2.4 (p.4), statutory guideline: "promptly report significant cyber incidents to the HKMA and, where appropriate, relevant authorities".
- Supporting, R08 SPM TM-G-1 para 3.3.3 (p.14), non-statutory guideline: "timely reporting to the HKMA of any confirmed IT-related fraud cases or major security breaches".
- Conditional rule: R07 SPM TM-G-2 para 1.3.3 (p.5), non-statutory guideline: "AIs should inform the HKMA promptly if their BCP is activated." Missing fact: whether the BCP is activated. If it is, I tell the HKMA at once and send periodic progress reports until resolution.
- Next step linked to COM: R05 p.3, heading "Handling of customers' and media's enquiry", first paragraph, last sentence (checked against the scan): "copies of public communication materials should be submitted to the HKMA for reference". I send COM's materials when issued.

## Q02b — Critical infrastructure incident notification

**Decision and action.** Triggered, in the serious (12-hour) category. I notify by telephone now and open the call with "this is a notification under section 28 of Cap. 653". The call must cover:
- The nature of the incident: unauthorised commands encrypted gateway components.
- The critical computer system: the payment gateway.
- A brief summary: outbound domestic transfers and payroll submission disrupted, core function affected, bank aware at 08:00 HKT, earliest time of the activity unknown.
- A contact point.
I log the time, the receiving officer's name and any reference number.

**Owner and executing party.** LC is accountable and places the call. SEC supplies a technical contact. SEC or IT owns restoring the secure filing terminal.

**Trigger, awareness point and clock.**
- Trigger: the bank becomes aware of a computer-system security incident on a critical computer system.
- Awareness point: 08:00 HKT, 16 November 2026, when the bank confirmed the unauthorised commands.
- Statutory limit: as soon as practicable, and in any event by 20:00 HKT, Monday 16 November 2026.
- My target (judgment): call completed by 08:30 HKT.
- Missing fact: whether SEC's logs show reasonable certainty before 08:00. If so, the clock started earlier; this does not change the action.

**Recipient and channel.** The Commissioner of Critical Infrastructure (Computer-system Security), not the HKMA. The feasible initial channel is the designated telephone number, reached by the bank's verified telephone route, because the secure filing terminal is unavailable. The number itself is not in the sources.

**Next steps.**
- Written record in the specified form (R02 Annex E, form CICS005) through the designated secured channel within 48 hours of the logged call. If the call ends at 08:30, that is 08:30 HKT, Wednesday 18 November 2026.
- Terminal checkpoint (judgment): 12:00 HKT, Tuesday 17 November. On the first call I ask what alternative way applies if the terminal stays down.
- Written report (R02 Annex F, form CICS006) by Monday 30 November 2026. This is my computation of 14 days after the awareness date.
- SEC to supply the earliest identifiable time of the incident for Annex E.

**Basis and application.**
- Statute: R01, Cap. 653 (version date 2026-09-10).
  - s.2(1), "computer-system security incident" (p.10): an act "without lawful authority" that "has an actual adverse effect on the computer-system security of the critical computer system". Unauthorised commands encrypting gateway components meet both limbs.
  - s.28(1) (pp.43–44): "the operator must notify the Commissioner of the incident in accordance with subsection (2)". The bank's designation is effective and the gateway is a designated system.
  - s.28(2)(a) (p.44): "must be made as soon as practicable and in any event within the specified time".
  - Schedule 6 item 1(a) (p.97): "has disrupted, is disrupting or is likely to disrupt the core function of the critical infrastructure concerned—12 hours after the CI operator concerned becomes aware of the incident". The card states that transfer and payroll processing is a core function and is disrupted.
  - s.28(2)(b)(ii) (p.44), for a notification not in the specified form: "include information on the nature of the computer-system security incident and identify the critical computer system concerned".
  - s.28(3) and Schedule 6 item 2 (p.97): "48 hours after the notification concerned is made under section 28(1)".
  - s.28(4) and Schedule 6 item 3 (p.97): "14 days after the date on which the CI operator concerned becomes aware".
  - s.28(5)–(6) (p.44): failure is an offence, with fines of $3,000,000 on summary conviction or $5,000,000 on indictment.
  - s.10(2) (pp.20–21): a regulating authority may specify "more than one way". This supports asking for an alternative route.
- Why the Commissioner and not the HKMA:
  - R01 s.2(1) (p.9): "category 3 obligation (第3類責任) means an obligation imposed by Division 3 of Part 4". Section 28 sits in that Division.
  - R01 s.6(b)–(c) (p.15) confines a designated authority to category 1 and 2 obligations.
  - R03, HKMA Sectoral Code (2 June 2026), para 1.1.3 (p.3): "A Designated AI should refer to guidance published by the Commissioner in relation to category 3 obligations".
- Code of practice: R02, OCCICS Code of Practice (Generic) v1.0. Status per para 1.1.4 (p.4): "This Code is not subsidiary legislation"; under R01 s.9 it is admissible in proceedings.
  - Para 7.3.5 (p.36): "At the point the CI operator has a reasonable degree of certainty that a computer-system security incident has occurred, the CI operator is deemed to have become aware".
  - Para 7.3.6(b) (p.36): "the CI operator may first make the notification to a designated telephone number", followed by the form "within 48 hours of the notification".
  - Para 7.3.6(c) (p.36): the operator "is obliged to fulfil any sector specific requirements in incident notification". This confirms the HKMA report is additional.
  - Para 7.3.4(c) (p.36): "has triggered or is likely to trigger the activation of business continuity or disaster recovery procedures". Judgment: likely met while failover is unverified.
  - The bank's maximum tolerable downtime and minimum service level are unknown to me. They are not needed, because the Schedule 6 wording is met directly.

## Other paths checked, outside the two Q02 decisions

- Privacy Commissioner (PCPD) data breach notification: not triggered on card facts, because no personal data compromise is known. If SEC finds personal data exposed:
  - R11, PCPD guidance (non-statutory), p.6 says notify "as soon as practicable"; p.8 says "Oral notifications are not accepted", so the R16a form is used.
  - R16b, HKMA circular, p.3 adds a report to the HKMA.
- Police report: no direct rule located in assigned sources. R04 footnote 1 only names the Police cyber crime bureau as a relevant authority.
- R16c and R16d: no fact on this card engages them; I did not analyse them.

## Search record and limits

- "PH01": 0 hits.
- "serious computer system security incident": 0 hits; the hyphenated "computer-system security incident" gave 66 hits in R01–R03.
- HKMA channel or form, regex "sector-specific form|case officer|incident report form|relevant arrangements|usual supervisory contact": hits only at R02 pp.36–37 and R09 p.33.
- Numeric HKMA clock, regex "within \w+ (hours?|minutes?|working days?)": hits only at R02 pp.35–36.
- "significant incident": R05 and R09 only; no definition.
- Designated telephone number, regex "designated telephone|designated secured channel|secured channel|telephone": R02 pp.4, 36, 37; no number given.
- The timeline figure at R02 para 7.3.8 is not in the text layer, so I relied on s.28 and Schedule 6.
- R05 quotations were checked against the page images.

## Simulated actions for the facilitator to log

1. 08:05 — LC obtains the SEC-confirmed fact sheet (version 1, facts as at 08:00).
2. 08:15 — LC telephones the HKMA supervisory contact.
3. 08:30 — LC telephones the Commissioner's designated number.
4. 08:45 — LC sends written confirmation to the HKMA.
5. LC opens a regulator notification register recording time, officer, content and reference for each contact.
6. LC tasks SEC or IT with restoring the secure filing terminal and starts drafting Annex E.
7. 10:00 — next HKMA update.