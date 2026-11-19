SEC (Information Security Lead): locked response for C07, Wednesday 18 Nov 2026, 12:00 HKT (H+52)

Assigned units: Q19a and Q19b only. I have taken the facilitator's handoff on the status of my earlier items into account.

Records that do not exist yet, and how I treat them:
- The handoff confirms that no card records:
  - the result of the vendor-credential closure test (C03 K4);
  - the 16 Nov access-window, preliminary-scope and full-package results;
  - SEC's clearance or hold of the alternate process (C04 and C06);
  - the sending of the vendor preservation request (C02).
- None of these is treated as passed or done.
- No conflict was found between PH01 and any applicable external requirement for these units.

---------------------------------------------------------------
UNIT Q19a: A reviewable technical timeline, with clock offsets and uncertainties

DECISION
SEC builds a versioned, evidence-linked timeline under PH01 6.3 and 6.4. Every row can be reproduced from a hashed source record. Clock offsets are measured, not assumed. When the uncertainties do not allow events to be ordered, the timeline says "order undetermined" instead of guessing.

ACTIONS (simulated, for the log)

T1, 12:00 to 13:00: intake.
- The evidence custodian registers each delivery (gateway, identity provider, vendor remote access service) with all Annex B fields: evidence ID, source, acquisition time, collector, witness, tool, SHA-256, storage location and transfer record. The custodian checks the delivered hashes against the manifest.
- The vendor-service records are labelled "supplier's account – unreconciled" until SEC has reconciled them with the bank's own logs (PH01 6.7(d)).
- How the forensic partner obtained the vendor records is unverified, as is whether they came through a PH01 6.7(b) channel. The custodian records the chain from vendor to partner to bank. Judgment: confirm the manifest hash with the vendor by calling back a number on file.
- Analysis uses verified copies only.

T2, 13:00 to 15:00: measure clock offsets for each source and each period. Method (judgment):
- (a) Record each source's time zone explicitly. A UTC log is not misread as HKT (UTC+8).
- (b) Use the bank's primary time-source synchronisation and drift records for the bank's own hosts (PH01 6.4).
- (c) Anchor events: the same event seen in two sources, for example a vendor VPN session start against the identity-provider authentication and the firewall flow. Pairwise offsets are computed from these.
- (d) Reference events with known HKT times, such as SEC's logged isolation (about 08:10, 16 Nov) and revocations (09:30 and 12:15, 16 Nov), as they appear in the logs.
- (e) Several anchors per source, to catch drift. The offset may change over time and is interpolated between anchors.
- The worksheet behind every offset is kept with the timeline.

T3: fields in every row (PH01 6.4 plus judgment):
- the original timestamp exactly as recorded, with its time zone;
- source, evidence ID and record locator (line or record hash);
- the measured offset, with its method and anchor references;
- the normalised HKT time;
- the uncertainty (±), made up of offset measurement error, source resolution and drift;
- a tag: observed / derived / inference / single-source-unreconciled;
- free text, with customers referred to only by token or count, never by name or identity card number (DPP4).
Uncertainty rules (judgment):
- A source with no anchor carries at least ±4 minutes, the largest difference observed on this card.
- "Combined uncertainty" is taken as the SUM of the two rows' uncertainties, which is the conservative reading.
- Events closer together than that are recorded "order undetermined" (PH01 6.4).

T4: ordering-critical questions, answered first. Each answer is recorded as a range, or as "order undetermined":
- (i) the earliest attacker or vendor-credential activity against the backup timestamp (C05 check I1). If the order is undetermined, the backup is NOT treated as pre-incident;
- (ii) the 80- and 320-record exports against isolation (about 08:10) and the revocations (09:30 and 12:15). This shows whether containment failed;
- (iii) the end of the access window against a logged closure test;
- (iv) the first appearance of the new indicator against the time that host was quarantined;
- (v) for LC: the "Earliest Identifiable Time" and the "Time Becoming Aware" (R02 Annex F, fields B5–B6).
SEC's response actions from the decision log go in as rows too, with their own wall-clock uncertainty.

T5, reviewability.
- Version 1.0 is issued by 18:00, covering the ordering-critical rows.
- An independent reviewer (a forensic-firm or SEC analyst who did not build it) checks every ordering-critical row and every offset worksheet against the source by 20:00. All ordering-critical rows are checked, not a sample.
- Revisions are appended with a change log. Nothing is overwritten.
- Each later version is dated and sent to LC as supplementary material (PH01 5.9).

OWNER
- Accountable: SEC.
- Execution: SEC analysts and the forensic firm, with the custodian; an independent reviewer.
- The vendor relationship owner handles the hash confirmation.
- LC decides any external use of the timeline. Sharing it with a third party needs LC and SEC jointly, with the DPO consulted (PH01 s.3).

TIMES
- Intake by 13:00.
- Offsets by 15:00.
- Version 1.0 by 18:00.
- Review by 20:00.
- Updates as new evidence arrives.

DESTINATION / CHANNEL
- Evidence register, write-once evidence store, timeline workbook (versioned).
- Decision log.
- To LC by hand or through the evidence store. Not by corporate email unless it has been logged safe.

BASIS: EXTERNAL
1. R02, OCCICS Code of Practice v1.0, s.7.2.3(a)(v)(3) and (4), PDF p32.
   - The plan's playbooks must cover "(3) Investigating the cause and impact of the incident; (4) Recording the incident response process, including details of the incident, actions taken and decisions made".
   - Authority: category 3 (incident response) guidance under Cap. 653, applying to all CI operators.
2. R03, HKMA Sectoral Code for Designated AIs, s.6.2.23(d), PDF p18: "Retained logs should contain sufficient information to support after-the-fact investigation of computer-system security incident(s)". It applies to the gateway logs, which are critical computer system logs.
3. Supporting only, because the R03 sectoral code governs category 2 matters for a designated AI: R02 s.6.2.23(g), PDF p20, "synchronise the internal clocks of all CCSs components with a primary time source to enable accurate log-event correlation across the systems".
4. For LC: R02 Annex F, PDF p44, fields B5–B6 need the earliest identifiable time and the time of awareness. The written report is due 14 days after awareness (R01 Cap. 653, Schedule 6 item 3, PDF p97). The timeline feeds both; filing is LC's.
5. R11, PCPD Guidance, PDF p6, Step 5: "A comprehensive record of the incident is therefore required, which should include all facts relating to the breach ... to the containment and remedial actions taken".

NO DIRECT RULE LOCATED externally for how to measure offsets or for the "order undetermined" rule.
- Terms searched: "uncertaint", "time source", "clock", "offset".
- Only PH01 6.4 sets it. The anchoring method, the ±4-minute floor and the sum rule are professional judgment.

BASIS: INTERNAL (Internal bank procedure: PH01, v1.0, effective 1 Oct 2026)
- s.6.4: "Every timeline entry keeps the original timestamp, the measured offset, the normalised HKT time and its uncertainty. Events closer together than their combined uncertainty are recorded as 'order undetermined'."
- s.6.3: "Analysis is on verified copies only."
- s.6.7(d): supplier records are "the supplier's account until SEC has reconciled them".
- Also Annex B and s.5.9.

CONFLICT CHECK
- None found.

---------------------------------------------------------------
UNIT Q19b: Retain, raise or reduce monitoring and containment

DECISION
- RAISE monitoring.
- RETAIN all existing containment. Nothing is reduced.
- ADD targeted containment for the new indicator.
- The indicator's link to the original compromise is unverified. It is treated as related until evidence shows otherwise (judgment).
- In the recorded recovery state, nothing could be reduced anyway: the gateway is isolated and held, the recovered image failed and is on hold, the standby is held, vendor access is revoked, and mobile transfer submission is held.
- Containment is NOT confirmed, so SEC's status reports stay hourly (PH01 2.5).

ACTIONS (simulated, for the log)

N1, 12:00 to 12:10: capture first. Capture the quarantined host's volatile state (memory, processes, connections) and a snapshot, hashed and witnessed (PH01 6.2, 6.3). The host stays quarantined and powered on.

N2, by 12:30: check the quarantine is holding.
- Traffic-flow logs are checked for any traffic in or out since quarantine, including blocked call-out attempts.
- Any destination the indicator tries to reach is blocked at the perimeter across the bank.
- If any traffic crossed: containment has failed. Widen isolation to the affected path at once, and tell the chair at once.

N3, by 13:00: sweep for the indicator across the bank.
- Scope: all endpoints and servers, the directory, the workspace, the backup catalogue, the recovery environment, and the alternate-process hosts.
- Alternate process (its status is unverifiable):
  - Any hit there is a security stop under C06 Q16b section A: releases stop and SEC's clearance is suspended.
  - If no clearance is logged and it is releasing: pause at once, as the CE ordered at C06.
  - SEC grants no new clearance until this sweep is clean.
- Any hit in the recovery environment means candidate (1) fails its integrity check (C05 Q13a).

N4, by 13:00: re-run the closure test.
- The C03 closure test has no recorded result. SEC re-runs the test on every access path and logs it (PH01 7.4).
- Until it is logged as passed, the access window stays open.
- If the indicator involves an account, PH01 7.3 is applied to that account.

N5, by 14:00: classify the indicator.
- Timing from the Q19a timeline, with uncertainty: is it new activity after quarantine, or a historical artefact surfaced by new detection?
- Classes:
  - (a) historical, consistent with the original compromise;
  - (b) new activity, meaning persistence or a second stage, and therefore containment has failed;
  - (c) unrelated, on evidence.
- The facts go to LC at once. If it is (b), LC must assess whether it is a NEW computer-system security incident with its own notification clock. That is LC's call (R02 7.3.5 on awareness).

N6, raise monitoring:
- round-the-clock watch;
- detection rules for the new indicator and the original ones;
- alerts on any use of revoked vendor credentials or tokens;
- identity-provider and e-banking login anomaly monitoring, because the fake verification page and 31 scam reports suggest harvesting of customer credentials;
- the Fraud team strengthens transaction monitoring for the 320 affected customers (R09 8.1.4);
- scam report details (caller numbers, URLs, sender IDs, and which data fields were quoted) are received into evidence. SEC tests whether the scams use fields from the 320 file. This is "reports of misuse" evidence under PH01 10.4(c) for the DPO and LC; attribution stays unverified until shown.

N7, retain all restrictions, each until its release condition is met and the PH01 s.3 decision-maker logs the release (PH01 18.3):
- gateway isolation and evidence hold;
- vendor access revoked (reinstatement only under PH01 7.5);
- standby on hold;
- recovered image on hold (gate under PH01 9.3);
- mobile transfer submission held.

N8, criteria for any future reduction (judgment). A proposal to reduce monitoring may be made only when all of these are logged:
- the indicator is classed (a) or (c) on evidence;
- the bank-wide sweep is clean;
- the closure test has passed on every path;
- 72 hours have passed with no new indicator;
- the recovery environment's separation has been re-verified.
SEC proposes; the chair is informed. Gateway isolation is lifted only for the rebuild, and evidence is released only by SEC and LC jointly.

TRIGGERS
- Any hit outside the quarantined host: widen containment to that segment, apply a security stop to the alternate process, and tell the chair at once. If the CMT has stood down, it reconvenes (PH01 18.5).
- Any successful use of a revoked credential: treated the same way.

OWNER
- Decides isolation, monitoring and security stops: SEC (PH01 s.3, 7.1).
- Execution: the security operations team, IT Ops network and identity engineers, the forensic firm and the Fraud team.
- The chair is informed of every widening.

TIMES
- 12:10: capture.
- 12:30: quarantine check.
- 13:00: sweep and closure test.
- 14:00: classification.
- Hourly status reports.
- Earliest reduction review: 72 hours after the last indicator, and only if the other N8 criteria are met.

DESTINATION / CHANNEL
- Changes on the endpoint detection platform, the security monitoring system, perimeter firewalls and the identity provider.
- Decision log, emergency change record, evidence register.
- The CMT room or phone bridge.

BASIS: EXTERNAL
1. R03, HKMA Sectoral Code for Designated AIs, s.6.2.26(a) and (b), PDF p19.
   - "A Designated AI should implement measures to detect computer-system security incidents affecting CCSs".
   - "monitor and analyse threat intelligence in relation to CCSs, and take appropriate actions".
   - Authority: the HKMA's category 2 code.
   - Why it applies: a new indicator from this incident is a direct threat to the critical computer systems.
2. R05, HKMA circular of 22 Jun 2010, PDF p1 (checked against the scan): "as soon as practicable rectify or contain the problem". R02 s.7.2.3(a)(v)(1), PDF p32: "Containing the incident to prevent further harm".
3. R09, SPM TM-E-1, s.8.1.4, PDF p32: fraud monitoring processes "may involve suspending the transactions in a timely manner and/or contacting the customers concerned through a reliable channel to verify the transactions or activities". This applies given the 31 scam reports and the fake page.
4. Supporting: R01 Cap. 653, s.36(2)(c), PDF p52. The Commissioner can require an operator "to monitor the system". Raising monitoring now matches what a regulator could require.

NO DIRECT RULE LOCATED externally for when to reduce monitoring.
- Terms searched: "monitor", "contain", "isolat".
- The N8 criteria and the 72-hour period are professional judgment.

BASIS: INTERNAL (PH01 v1.0)
- s.7.1: "Services still working are kept running unless SEC finds active spread to them."
- s.6.2: limit on capture before containment.
- s.7.3 and 7.4: closure test; the window stays open until it is logged.
- s.2.5: hourly status reports until containment is confirmed.
- s.18.3: "Restrictions stay in force ... until their release condition is met and the decision-maker in section 3 has logged the release."
- s.18.5: the CMT reconvenes "at once on any security trigger".

CONFLICT CHECK
- None found.

---------------------------------------------------------------
FACTS SEC PASSES TO THE INCIDENT TEAM

To LC:
- Facts on the new indicator now, and its classification by 14:00. If it is new activity, LC assesses whether it is a new incident with its own clock.
- Timeline version 1.0 by 18:00, for:
  - the Annex F written report (due 14 days after awareness, about 30 Nov if awareness was 16 Nov);
  - the Police;
  - PCPD supplementary information.
- The vendor-service records are unreconciled.

To COM and the DPO:
- Under PH01 10.5, the 12 corrected contact details must come only from the bank's verified records. Any detail changed after the incident started is checked by Fraud before use, because a scam or the attacker could be the source.
- Whether the scams use data from the 320 file is being tested. Attribution remains unverified until then.

To the chair:
- Containment is not confirmed. Monitoring is raised and nothing is reduced.
- The alternate process may not receive new clearance until the sweep is clean.

---------------------------------------------------------------
LOG-READY ACTIONS (HKT, status)
- 12:00: Intake and hashing of the partner records; vendor records labelled unreconciled (executed).
- 12:00 to 12:10: Capture of the quarantined host (executed).
- 12:30: Quarantine integrity check (scheduled).
- 13:00: Bank-wide indicator sweep; closure test re-run and logged (scheduled).
- 14:00: Indicator classified and sent to LC (scheduled).
- 15:00: Clock offsets measured (scheduled).
- 18:00: Timeline version 1.0 (scheduled).
- 20:00: Independent review (scheduled).
- In force: monitoring raised; all containment retained (executed).
- Reduction: held under the N8 criteria.
- Widening: on any hit (trigger).