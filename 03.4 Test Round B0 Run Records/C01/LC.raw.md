LC response to C01 (Monday 16 Nov 2026, 08:00 HKT, H+0). It covers Q02a and Q02b only. Locked before I see colleagues' answers. Facilitator handoff to LC: none. All actions below are simulated, for the facilitator to log.

Facts I rely on, as released: at 08:00 the bank confirmed unauthorised commands that encrypted parts of the payment gateway, which is a designated critical computer system. Outbound domestic transfers and payroll submission are disrupted, and these are a core function of the designated infrastructure. Mobile balance view still works and branches are open. Unverified: whether failover works, the root cause, how far the attack has spread, and whether any data was exposed. Phone route to the Commissioner: verified. Terminal for the verified secure filing channel: unavailable. Dispatch log: empty.

---

**Q02a – Initial HKMA reporting**

- **Decision and action:** Report to the HKMA now by telephone to the bank's HKMA supervisory contact, using the printed Regulator Contact Register. Follow up with a short written initial report by a route that does not rely on the affected systems or on corporate email until SEC has logged email as safe. No internal review, approval or extra fact-finding may hold this report. Internal review runs alongside it.
- **What to send now:**
  - Bank name; LC as contact, with call-back numbers.
  - Awareness time: 08:00 HKT, 16 Nov.
  - Nature: confirmed unauthorised commands encrypted parts of the payment gateway (a ransomware-type act). Treated as a cyber attack.
  - Impact: outbound domestic transfers and payroll submission disrupted. Mobile balance view working. Branches open.
  - Customer exposure: 180,000 retail and 12,000 SME customers. The number actually affected is unverified. Payroll timing is a risk for SME customers.
  - Marked UNVERIFIED: whether failover works, root cause and spread, data exposure (none confirmed so far), and whether there is an extortion demand (none received so far).
  - Actions under way: containment and evidence preservation (SEC), CMT convened.
  - Parallel filings: the bank is notifying the Commissioner under Cap. 653 s.28 (Q02b). COM is preparing customer and public communications, and copies will be sent to the HKMA.
  - Next update time.
- **Owner:** LC, who owns all regulator reports (PH01 s.5.1). Executing party: LC duty officer. SEC supplies the technical facts.
- **Timing:**
  - Call target: by 08:30 HKT. The rule says "immediately"; the 30-minute figure is my professional judgment.
  - Written confirmation: target 10:00 HKT.
  - Updates: every 4 hours for the first 24 hours (12:00, 16:00, 20:00, 24:00, 04:00, 08:00), then 08:00 and 18:00 daily. Also update at once on any of: BCP activation, confirmed data exposure, an extortion demand, a change in service status, or a public statement.
- **Recipient and channel:** HKMA supervisory team, by phone. Then written follow-up by a route the HKMA accepts. I could not find an HKMA filing channel in the assigned sources, so I will ask the HKMA on the call which route it accepts and log the answer.
- **External basis:**
  - **R05**, HKMA circular "Incident response and management procedures", 22 Jun 2010 (supervisory circular, not statute). PDF p.2, heading "Reporting incident to the HKMA". Quote checked against the scan image: "once an AI has become aware that a significant incident has occurred, the AI concerned should notify the HKMA immediately and provide it with whatever information is available at the time." Also: "an AI should not wait until it has rectified the problem before reporting the incident to the HKMA."
    - Why it applies: losing a critical payment channel for a large customer base through a cyber attack is a "significant incident". That classification is my professional judgment, because the circular does not define the term.
  - **R09**, SPM TM-E-1, V.4, s.8.2.5, PDF p.33 (statutory guideline status not verified; HKMA Supervisory Policy Manual guidance). Quote: "should notify the HKMA promptly in accordance with the relevant arrangements set out by the HKMA from time to time." It does not specify the channel.
  - **R07**, SPM TM-G-2, V.2, s.1.3.3, PDF p.5. Its classification (p.1) is "A non-statutory guideline issued by the MA as a guidance note". Quote: "AIs should inform the HKMA promptly if their BCP is activated."
    - Status at this card: BCP activation has not been declared and failover is unverified.
    - Conditional action: as soon as the CMT chair declares BCP activation (PH01 s.4.4), LC tells the HKMA promptly and sends periodic progress reports.
- **Left to judgment:** the exact minutes behind "immediately", the HKMA channel, and how detailed the first report is.
- **Internal bank procedure (PH01 v1.0):**
  - s.5.1: "LC owns every report to a regulator or authority".
  - s.2.4: "The initial report goes on the facts held at the time, with unverified items marked as unverified".
  - s.5.8: "LC updates the HKMA supervisory contact every four hours during the first 24 hours".
  - s.5.7: "An open email check never delays a report."
  - s.1.4: internal times "never extend an external deadline."
  - No conflict with the external requirements.

---

**Q02b – Critical infrastructure incident notification under Cap. 653 s.28**

- **Decision:** Notification is triggered. This is a serious incident, so the 12-hour limit applies.
- **Action:**
  - Notify the Commissioner of Critical Infrastructure (Computer-system Security) now, by the verified telephone route.
  - On the call, give the information R02 7.3.6(b) requires:
    - (i) Nature: unauthorised commands encrypted gateway components (ransomware-type), disrupting a core function.
    - (ii) Critical computer system involved: the payment gateway.
    - (iii) Brief summary: discovered and confirmed 08:00 HKT; outbound domestic transfers and payroll disrupted; failover, root cause and data exposure unverified; containment under way.
  - Log the time, the person reached, any reference number and a summary (PH01 s.5.5). Ask for a reference or receipt in the same call.
  - Then file the specified form (Annex E or the sector form) through the designated secure channel within 48 hours of the call.
  - Because the normal terminal is down:
    - At declaration, Compliance tests and logs the standby filing device and whether it is enrolled for this channel.
    - SEC logs within 30 minutes whether the terminal can be released.
    - If neither works, LC asks the Commissioner's office during the call which alternative route it accepts, and logs the answer (PH01 s.5.6).
- **Owner:** LC. Executing party: LC duty officer. SEC supplies the facts.
- **Awareness point:** 08:00 HKT, 16 Nov 2026, when the bank "confirms" the unauthorised commands. That meets R02 7.3.5's test of "a reasonable degree of certainty".
- **Clocks:**
  - (1) Initial notification: as soon as practicable, and no later than **20:00 HKT on Mon 16 Nov**. Internal target: phone call by 09:00 HKT.
  - (2) Written record in specified form: within 48 hours of the phone notification. Example: a call at 09:00 Mon means a deadline of 09:00 Wed 18 Nov. The exact time is set from the logged call time. Target: Tue 17 Nov.
  - (3) Written report in specified form (Annex F or sector form): within 14 days after the awareness date, which I compute as by **Mon 30 Nov 2026**. That date count is my professional judgment and should be checked by a second LC officer under PH01 s.5.3. Internal target: 27 Nov. Supplementary information follows as facts emerge.
- **Recipient:** the Commissioner, not the HKMA.
  - Section 28 sits in Part 4, Division 3 (R01 PDF p.43). Under s.2 (PDF p.9), "category 3 obligation means an obligation imposed by Division 3 of Part 4".
  - R03 s.1.1.3 (PDF p.3) directs designated AIs to the Commissioner's guidance for category 3 obligations.
  - Tell the HKMA that the filing has been made, as part of the Q02a updates.
- **External basis:**
  - **R01**, Cap. 653 Protection of Critical Infrastructures (Computer Systems) Ordinance (statute; verified copy, version date 10 Sep 2026).
    - s.2 definition, PDF p.10: an event involving "access, without lawful authority" or another unlawful act that "has an actual adverse effect on the computer-system security of the critical computer system". Applied: unauthorised encryption of a designated system meets both limbs.
    - s.28(1), PDF pp.43-44: "If a CI operator becomes aware that a computer-system security incident has occurred in respect of a critical computer system ... the operator must notify the Commissioner".
    - s.28(2), PDF p.44: "as soon as practicable and in any event within the specified time". Under s.28(2)(b)(ii), a notification not made in the specified form must still "include information on the nature of the computer-system security incident and identify the critical computer system concerned".
    - s.28(3): a later written record in specified form. s.28(4): a written report.
    - s.28(5)-(6): failure is an offence, with a fine of up to $5,000,000 on indictment.
    - Schedule 6, item 1(a), PDF p.97: "If the computer-system security incident concerned has disrupted, is disrupting or is likely to disrupt the core function ... 12 hours after the CI operator concerned becomes aware of the incident." Item 2: "48 hours after the notification concerned is made under section 28(1)." Item 3: "14 days after the date on which the CI operator concerned becomes aware".
    - Applied: disruption of the core function is confirmed, so the 12-hour limit applies, not 48 hours.
  - **R02**, OCCICS Code of Practice (Generic), v1.0 (a code of practice under Cap. 653 s.8; per s.1.1.4 it "is not subsidiary legislation", but can be admitted in evidence under R01 s.9).
    - s.7.3.3(b), PDF p.35: example "Ransomware attack that causes suspension of an essential service".
    - s.7.3.4, PDF p.35: serious incident "must be notified within 12 hours".
    - s.7.3.5, PDF p.36: awareness test.
    - s.7.3.6(b), PDF p.36: "the CI operator may first make the notification to a designated telephone number ... and then submit a specified form ... within 48 hours".
    - s.7.3.6(c): sector-specific requirements still apply, so Q02a runs alongside this.
- **Missing facts and conditions:**
  - Whether the bank's verified phone number is the Commissioner's "designated telephone number". I treat it as such because the card calls it the verified route for CI incident notification. If it turns out not to be, a notification that states the nature of the incident and names the system still satisfies s.28(2)(b)(ii).
  - Whether a filing route will be available for the 48-hour written record. LC asks on the call; condition owner is Compliance/LC.
  - No internal condition may hold this call (PH01 s.2.4).
- **Internal bank procedure (PH01 v1.0):**
  - s.5.2 names "Cap. 653, section 28 and Schedule 6, and the Commissioner's Code of Practice section 7.3" and "does not restate their triggers, recipients or time limits".
  - s.5.3: a deadline tracker, with each clock "checked by a second LC officer within 30 minutes".
  - s.5.6: standby filing device and alternate route.
  - s.4.1: Severity 1, "a critical operation is disrupted".
  - No conflict with the external requirements.

---

**Governance and clearance**

- No legal or governance condition holds either report.
- LC clears the content. The CMT chair is informed.
- SEC confirms facts in parallel, and its corrections go in the next update.

**Outside the assigned units, for the facilitator's awareness only:**
- Under PH01 s.3, a Police report is LC's decision. I am flagging it for the CMT and not deciding it in this unit.
- PCPD notification is not triggered on current facts, because no data exposure is confirmed. LC will reassess if exposure is found.