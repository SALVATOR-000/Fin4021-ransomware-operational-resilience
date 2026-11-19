## COM submission for C06: Tuesday 17 November 2026, 20:00 HKT (H+36)

I locked this before seeing colleagues' answers. There is no handoff for C06. All actions are simulated, for the facilitator to log.

**What the card tells me**
- **Confirmed:**
  - The offline laboratory test on the recovery image reconciled 118 of 120 payment instructions. The 2 differences are unexplained.
  - The lab saw no repeat of the encryption activity during its test window only.
  - Some SMEs have missed payroll cut-offs.
  - Two counterparties have asked for the status of their unsettled instructions.
- **Unknown at this card:**
  - The recovery position the CEO will approve (SEC under Q16, Board under Q17b).
  - Whether the secondary process from C04 was activated, and whether it is still running.
  - Which lines the C05 updates actually carried.
  - How many instructions have been settled, are not settled, or have unknown status.
- **Expected position: hold.** PH01 s.9.2 says "One unexplained difference is a fail", and s.9.3 says "Missing any item means hold". On these facts the restored system cannot pass the gate tonight, and nor can a narrower scope (s.9.3). Below I give wording for each possible decision. Nothing is released until the CEO's decision is logged.

---

## Q18 a. Customer status update

### Decision
Publish one self-contained update at 21:00 HKT. It reflects the recovery position the CEO has logged, and repeats no earlier text that I cannot verify.
- **If the CEO has not logged a decision by 20:45:** the 21:00 update states the verified position (the restored system is not in use). A further update goes out at once when the decision is logged.
- **If the Board decides later tonight:** a further update goes out at once on that decision.
- **After that:** the next update is at 07:00 HKT on Wednesday, plus an immediate update on any change of service (PH01 s.11.2).
- **Channels:** website status page, press release, official social media (text only, no link), app banner (if trusted), IVR, branch notices, and staff script v6.
- **HKMA copy:** COM gives a copy to LC at release; LC sends it to the HKMA and asks for a receipt (PH01 ss.5.5 and 5.8).

### Owners
- **Approves:** the CEO, or the COO if the CEO is unreachable for 15 minutes. LC clears; SEC and Operations fact-check.
- **Executes:** COM.
- **Supplies facts:** the Head of Payments Operations gives the payment figures from the instruction register. COM gives the data-notification figures from the notification register.

### Release conditions (PH01 s.2.3)
| ID | Line | Verifier | Latest time | Default if not verified |
|---|---|---|---|---|
| V1 | Recovery position | CEO's logged decision, with every s.9.3 item evidenced for any production use | 20:45 | Version H below |
| V2 | Status of the alternate process (running, paused, never activated) | Head of Payments Operations and SEC clearance log | 20:45 | Say "queued payments remain on hold" |
| V3 | Any figures | Owner confirms from the record (PH01 s.11.4) | 20:45 | "Figures are being checked and will be given at 07:00" |
| V4 | Data lines (320 notified; wider claim unverified) | SEC and the COM register | 20:45 | Remove any line that is not verified |

**Fixed lines in every version:**
- The test figures (118/120) are not published.
- No claim that "the attack is over". The lab result covers only its test window.
- No restoration time.
- No mention of the vendor, the system or the bank's critical infrastructure status (PH01 s.11.3).

### Version H: hold (expected)
> "Lan Tidal Bank service update – 17 November 2026, 21:00 HKT.
>
> **Payments.** Our main payment system is still not working. We have tested a restored version of it offline. The tests found differences we have not yet explained, so we will not use the restored system for your payments until every check is passed. We will not take risks with the accuracy of your payments. We cannot yet give a time for full service.
>
> [If V2 says running: Queued payments continue through our alternative process: SME payroll first (earliest pay date), then payments due today or the next business day, then others in the order received. (V3 figures)]
>
> [If V2 says not running: Queued payments remain on hold until they can be processed safely. We will tell you as soon as that changes.]
>
> Each payment will be made only once. Please do not resubmit.
>
> **SME customers who missed payroll.** We are sorry. Fees caused by the disruption are waived. We will reimburse documented direct losses caused by the disruption, such as late-payment charges from a missed payroll cut-off. Tell your relationship manager, any branch or our call-back service; you will get a case reference and be told when to expect a decision. On request we will give you a letter confirming the delay was caused by the bank's service disruption, which you may show to your employees or others.
>
> **Customer information.** [V4 lines]
>
> **Scam warning.** We never ask you to verify your account through links, QR codes or social media, or ask for your password, PIN or one-time password.
>
> Next update by 07:00 HKT tomorrow, or sooner if service changes."

### Version N: narrower mode, for example payroll only
Usable only after the CEO logs that every item in PH01 s.9.3 has passed for that scope. On tonight's facts it cannot be used.
> "We have started using a restored system for [SME payroll only], beginning with a checked batch of up to 20 payments. We will extend it only after each stage runs without any unexplained difference. Other payments [continue through our alternative process / remain on hold]."

### Version S: staged recovery
Same condition as Version N, with stages as set out in PH01 s.9.4.

### Version R: stop or rollback, if any production activity is later stopped
> "At [time] we paused payments from the restored system after our checks flagged an issue. No payment will be made twice; we are checking the status of each one and will contact you if we need to."

### Basis
- **R05, HKMA circular of 22 Jun 2010** (quotes checked against the scan):
  - **p.1:** tell customers "whether the bank would reimburse any losses incurred by them and if so, how they can apply for compensation".
  - **p.2:** include "the steps that affected customers need to take ... to gain or regain access to the relevant banking services or to protect their interests".
  - **p.3:** copies of public communication materials go to the HKMA.
  - **Why it applies:** the significant incident is still running and SMEs are now losing money.
- **R09, SPM TM-E-1, s.8.2.2, p.33, with footnote 26:** messages must be "consistent and up-to-date". Footnote 26 gives "any estimated service resumption time" and how customers can "apply for compensation".
  - **Missing fact:** a verified restoration time, so none is given.
- **Internal bank procedure (PH01, v1.0):**
  - **s.9.2:** "One unexplained difference is a fail."
  - **s.9.3:** "Missing any item means hold."
  - **s.11.2:** what each update must cover and when.
  - **s.11.4:** figures only from a confirmed record.
  - **s.13.1:** fees waived; staff may promise this at once.
  - **s.13.2:** "late-payment charges from a missed payroll cut-off, are reimbursed on claim".
  - **s.13.6:** claims route and case references.
  - **s.13.7:** "customers are told when to expect a decision".
- **Professional judgment:** the payroll-delay confirmation letter. LC clears its wording. It is not a payment, so the s.13.7 limits do not apply to it.
- **Conflict check:** no conflict.

---

## Q18 b. Counterparties and other banks with unsettled instructions

### Decision
Give operational status to **every** counterparty holding unsettled items, not only the two that asked.
- **Sequence:** a verified call first, then a written notice the same day.
- **Scheduled updates:** 08:00, 13:00 and 18:00 daily until every item is settled or returned (PH01 s.14.3).
- **Two-way purpose:** ask each counterparty to check its receiving-side records for items whose status is unknown. That independent record supports the duplicate and status controls in PH01 s.8.6(b).

### Owners
- **Contact:** the Head of Payments Operations makes the operational contact (PH01 s.14.1).
- **Wording:** COM controls the wording (PH01 s.14.1).
- **LC review:** LC reviews the template for any implied admission of liability. This review runs alongside and does not hold the contact (my judgment, since this is operational information).

### Channels
1. **The two requests:** before any reply, each is verified by calling back on the counterparty's number already on file (PH01 s.14.2).
2. **Verified call** by the named Payments Operations duty manager.
3. **Written notice** through the bank's established secure interbank operations channel, or by courier letter if that channel is unavailable.
   - Not ordinary email unless SEC has logged corporate email as safe.
   - Never through any link or contact route the counterparty supplied in its incoming request.

### Timing (HKT)
| Time | Action |
|---|---|
| 21:00 | Payments Operations lists all counterparties with unsettled items, and classifies each item from independent records as settled, not settled or unknown |
| 21:30 | Verified calls to the two counterparties that asked |
| 23:00 | Calls to all the other counterparties with unsettled items |
| 23:30 | Written notices to all of them, so each gets its notice the same day |
| Desk unreachable tonight | The attempt is logged; the written notice still goes tonight; the call is made at 08:00 |
| 18 Nov onward | Updates at 08:00, 13:00 and 18:00 |

Every contact is logged with time, channel, the person reached and a receipt (R07 s.4.7.2).

### Core counterparty message
> "Lan Tidal Bank – operational status of unsettled instructions, [date/time]. Our outgoing payment system remains disrupted, and a restored system is not yet in production. [Status of the alternate process, per V2.] Attached is the status of each instruction involving you (bank reference, value date, amount, status: settled / not settled / unknown). Items with unknown status are held and will not be resent until independent records show they did not settle. Please check your receiving records for the items marked 'unknown' and confirm through our verified contact whether they were received. Please do not act on any payment instruction, recall, or change of account or contact details said to come from us unless you have verified it by calling back on our numbers on your file. Next updates: 08:00, 13:00 and 18:00 HKT daily until all items are settled or returned. Contact: [named duty manager, number on file]."

**Data minimisation (judgment).** The message carries only transaction references, amounts and value dates. It carries no customer identity or contact data beyond what is needed for payment matching, and no security or technical detail. The reason: 320 customer records have already been published.

### Basis
- **R05, p.1 to p.2** (checked against the scan): "Where necessary, the AI should also notify other affected AIs (so that they can in turn notify their affected customers) as soon as practicable."
  - **Why it applies:** receiving banks can warn their own customers, such as SME employees, that expected payments are delayed.
- **R07, SPM TM-G-2:**
  - **s.4.7.1, p.13:** a strategy for communicating with "counterparties, business partners"; "ongoing and clear communication is likely to assist in maintaining the confidence of customers and counterparties".
  - **s.4.7.2, p.14:** "Important conversations with external parties should be properly logged".
- **R09, s.8.2.2, p.33:** consistent messages to "business partners".
- **Internal bank procedure (PH01, v1.0):**
  - **s.14.1:** Payments Operations handles operational contact; "COM controls the wording".
  - **s.14.2:** "Every incoming request is verified by call-back to a number already on file before any reply."
  - **s.14.3:** "a verified call and a written notice the same day, then updates at 08:00, 13:00 and 18:00 until every item is settled or returned".
  - **s.8.6(b):** "an independent receiving-side record" establishes whether an item settled.
- **No direct rule located in assigned sources:** no external rule sets the content or channel of counterparty notices; those choices are professional judgment. I checked the passages above again in R05, R07 s.4.7 and R09 s.8.2.
- **Conflict check:** no conflict.

---

## Simulated log entries
| Time | Entry |
|---|---|
| 20:45 | Conditions V1–V4 closed, or their defaults applied |
| 21:00 | Customer update published (Version H unless the CEO logs otherwise); copy to LC for the HKMA; staff script v6 |
| 21:00 | Counterparty list and item statuses ready |
| 21:30 | Verified calls to the two counterparties that asked |
| 23:00 | Calls to all other counterparties with unsettled items |
| 23:30 | All written notices sent |
| 18 Nov 07:00 | Next customer update |
| 18 Nov 08:00 | Counterparty update |
| 18 Nov 13:00 | Counterparty update |
| 18 Nov 18:00 | Counterparty update |