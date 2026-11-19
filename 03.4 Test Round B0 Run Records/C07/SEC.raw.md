SEC (Information Security Lead): locked response for C07, Wednesday 18 Nov 2026, 12:00 HKT (H+52). This covers only Q19a and Q19b. I have taken the facilitator's handoff record as the record of execution state.

Facts from C07 and the handoff:
- A forensic partner has delivered time-stamped records from the gateway, the identity provider (IdP) and the vendor remote access service. Some clocks differ by up to 4 minutes.
- A new indicator seen in the incident has appeared on a quarantined host. Whether it is linked to the original compromise is unverified.
- Attribution is unverified.
- The original gateway is still quarantined and under evidence hold. The recovered image is on HOLD. Vendor access is still revoked.

Not verifiable from any card:
- the result of the credential closure test;
- my secondary-process clearance decisions due 19:00 on 16 Nov and 21:00 on 17 Nov, and so whether any secondary releases are running;
- whether the records were delivered through the approved channel.

All actions below are simulated, for the facilitator to log.

== Q19a: A reviewable technical timeline, with clock offsets and uncertainty ==

**Decision.** SEC builds and owns one master technical timeline in the offline forensic lab, using verified copies only. It is versioned, reproducible and reviewed by a second person. Confirmed facts, inferences and unverified items are labelled separately. No attribution is stated.

**Actions**
1. **Intake, starting 12:00.** The evidence custodian logs the partner's delivery in the evidence register: Annex B fields, SHA-256 checked against the manifest, and the delivery channel used.
   - If the delivery did not come by bank-hosted encrypted transfer or on bank-issued encrypted media, the custodian records that as a limitation. The records are kept and used, but marked accordingly.
   - Vendor remote access service records stay the supplier's account until SEC has reconciled them with the bank's own PAM, firewall and IdP logs.
2. **Fields for every timeline entry:**
   - entry ID
   - source system and evidence ID
   - original timestamp exactly as recorded, with its stated or assumed time zone
   - measured offset and how it was measured
   - normalised HKT time
   - uncertainty (±)
   - event description
   - status (confirmed, inferred or unverified)
   - analyst and reviewer
3. **Measuring the offset for each source.** Use the best available method and record which one:
   - (a) the clock offset recorded at acquisition (Annex B);
   - (b) the source's time-sync logs against the bank's primary time source;
   - (c) anchor events seen in two or more sources, such as one session's IdP authentication, VPN or PAM session start, and firewall flow.

   If the offset drifts, it is applied piecewise over time. Uncertainty is the measurement error plus the residual drift. Where only the "up to 4 minutes" bound is known, uncertainty is set at ±4 minutes.
4. **Ordering rule.** Events closer together than their combined uncertainty are recorded as "order undetermined". No causal step (for example "credential used, then export") is asserted unless the order is established beyond the combined uncertainty or by a shared session or transaction ID.
5. **Making it reviewable:**
   - Normalisation scripts and tools are versioned and hashed.
   - Every entry can be traced back to its source excerpt by evidence ID.
   - Each change goes into a version log.
   - An independent reviewer re-derives a sample of offsets and all of the key-event entries. The reviewer is the retained forensic firm working on masked data, or an SEC analyst not involved in building the timeline.
   - Personal data is masked or tokenised in the timeline (DPO informed).
6. **Key questions the timeline must answer, each with an uncertainty band:**
   - first use of the vendor credential (start of dwell time; this decides the backup suitability check from Q13a);
   - the time of the export of 80 customers and of the set of 320;
   - whether any use occurred after revocation (the closure-test question);
   - when the new indicator first appeared;
   - any gaps in log coverage that overlap attacker activity.

**Owner and executing party.** SEC is accountable. SEC forensic analysts build the timeline; the evidence custodian handles intake; the forensic firm or an independent analyst reviews.

**Times (HKT; targets are my judgment, not gates).**
- Intake and hashing by 14:00 on 18 Nov.
- Version 1, with key events and uncertainty bands, by 20:00 on 18 Nov.
- Reviewed version by 12:00 on 19 Nov.
- If LC's written-report deadline (Q20b) is earlier, the timeline is delivered by that deadline as it stands, with open items marked as unverified.

**Recipients and channels.**
- Evidence register and the master timeline file on the offline lab system.
- Summary entries in the decision log.
- A printed or secure-lab copy to LC for the Q20 reporting and to the CEO (CMT chair). Not sent by corporate email unless email has been logged as safe.

**Basis, external:**
- **R02, OCCICS Code of Practice, s.7.2.3(a)(v)(2) and (4), PDF p.32.** Playbooks must cover "chain of custody" and "Recording the incident response process, including details of the incident, actions taken and decisions made".
  - Authority: Code issued under Cap. 653 s.8; Division 3 obligations of a CI operator.
  - It requires the record but leaves the method, offsets and uncertainty to judgment.
- **R02, s.6.2.23(g), PDF p.20:** "synchronise the internal clocks of all CCSs components with a primary time source to enable accurate log-event correlation across the systems."
  - Under R02 s.1.1.3, the HKMA Sectoral Code (R03) governs this Category 2 area for designated AIs. R03 s.6.2.23 (PDF p.18) does not state a clock-sync item, so I use R02(g) as a general principle.
  - The 4-minute differences show a shortfall to record and fix after the incident.
- **R03, HKMA Sectoral Code, s.6.2.23(d), PDF p.18:** logs "should contain sufficient information to support after-the-fact investigation".

**Basis, internal (Internal bank procedure, PH01 v1.0):**
- **s.6.4 "Clocks":** "Every timeline entry keeps the original timestamp, the measured offset, the normalised HKT time and its uncertainty. Events closer together than their combined uncertainty are recorded as 'order undetermined'."
- **s.6.3:** analysis on verified copies only.
- **s.6.7(b) and (d):** delivery channel, and supplier records reconciled.
- **Conflict check:** none.

== Q19b: Monitoring and containment after the new indicator ==

**Decision.** Raise monitoring. Keep and verify all containment. Reduce nothing.
- The quarantine, evidence hold, vendor revocation and the HOLD on the recovered system all stay in place.
- Confirmation of containment is reopened until the new indicator is explained, so SEC status reports go back to hourly.

**Actions** (SOC, EDR and Network teams execute; the evidence custodian witnesses):
1. **12:00–12:30: verify the quarantine is holding.**
   - Confirm the host's network isolation: no outbound flows, no new sessions, no admin logons.
   - If isolation has failed or there is outbound traffic, tighten the block at the network layer at once. Do not power off.
2. **Capture before any change.**
   - Image memory and record process, file and registry artefacts for the indicator, with hashes, in the evidence register.
   - The indicator is not removed, the host is not rebooted, and nothing is deleted until capture is complete and SEC has logged a release.
3. **Classify the indicator.** Decide whether it is new activity or an old artefact being surfaced:
   - new activity: a live process, a fresh file time, or new network attempts;
   - old artefact: for example, found by a fresh scan or delayed execution.

   Place it on the Q19a timeline with an uncertainty band. Its link to the original compromise is recorded as unverified until it is shown.
4. **Hunt across every environment, results by 14:00 HKT** (judgment target). Add the indicator to EDR, SIEM, DNS and proxy detection and blocking, then sweep:
   - all production systems;
   - the secondary-process path;
   - the isolated recovery environment and the candidate image;
   - the lab environment;
   - the backup working copy;
   - systems that the vendor credential could reach.

   If the indicator is found in the immutable backup or the candidate image, the candidate fails integrity and the Q13a backup-timing assessment is reopened.
5. **Secondary process (conditional; its status cannot be verified).**
   - If any secondary releases are running, the Q16b standing trigger applies: an incident indicator stops releases at once. The Head of Payments Operations or SEC stops them, and the CEO is told.
   - Releases resume only when the sweep shows the secondary path is clean, SEC re-confirms its s.8.2 clearance in writing, and reconciliation ties.
   - If no releases are running, no secondary activation goes ahead until the same sweep and written clearance are complete.
   - Professional judgment: this delays payroll. A sweep completed quickly (target 14:00) keeps the delay short. Releasing payments through a path that might be compromised would cause worse harm to customers.
6. **Recovered system.** The HOLD remains. The candidate is added to the scan, and any future gate pack must show the new indicator was checked for.
7. **Vendor and credentials.** Vendor reinstatement stays on HOLD. Check the indicator against the vendor identifiers and captured tokens. If it shows use after revocation, the access window is treated as open and the Q07a scope period is extended up to the present.
8. **Stop and escalation triggers.** Any of the following is escalated at once to the CEO, LC and DPO:
   - the indicator found outside quarantine;
   - outbound traffic from the quarantined host;
   - any link between the indicator and access to customer data.

**Owner and executing party.** SEC decides and is accountable. The SOC, EDR, Network and IT Operations teams execute. The Head of Payments Operations stops any secondary releases. The CEO is told; changes that affect customer services are consulted with the Head of IT Operations.

**Times (HKT, 18 Nov).** Isolation check and capture 12:00–12:30. Sweep results 14:00. Hourly SEC reports from 13:00.

**Recipients and channels.** Emergency change record, evidence register, decision log, and verbal briefing to the CEO.

**Facts for LC:**
- A new indicator, with its relationship to the original compromise unverified.
- Containment status.
- Any stop of secondary releases. A change in service status triggers the HKMA update under PH01 s.5.8. Further facts for statutory reporting go as supplementary information under s.5.9.

**Basis, external:**
- **R05, HKMA circular (22 Jun 2010), p.1, "Immediate incident response":** "as soon as practicable rectify or contain the problem. The top priority should be to safeguard the interests of customers".
- **R03, HKMA Sectoral Code, s.6.2.26(a)–(b), PDF p.19:** "implement measures to detect computer-system security incidents affecting CCSs" and "monitor and analyse threat intelligence in relation to CCSs, and take appropriate actions".
  - Applies to the gateway and its supporting critical computer systems. The detail is left to judgment.
- **R02, s.6.2.23(f), PDF p.20:** "All events suspected of being triggered by a computer-system security incident should be logged and monitored."
- **R02, s.7.2.3(f), PDF p.33:** balance recovery against evidence handling. Here containment is verified first and evidence is captured before any change.
- **R11, PCPD Guidance, PDF p.4–5, Step 2:** containment includes "thoroughly checking whether other interconnected systems containing personal data are affected".

**Basis, internal (Internal bank procedure, PH01 v1.0):**
- **s.7.1:** network-layer isolation; hosts not powered off.
- **s.6.1:** no deletion or rebuild without SEC's logged release.
- **s.2.5:** "SEC reports to the chair every hour until containment is confirmed".
- **s.9.5:** "a security indicator from the incident" stops releases from the recovered system.
- **s.8.2:** clearance for the secondary process.
- **s.7.5:** reinstatement conditions.
- **Gap:** PH01 s.8.7 lists only reconciliation stops for the alternate process. Applying the security-indicator stop to it is my Q16b standing control and professional judgment, consistent with R05's priority on customer protection.
- **Conflict check:** none.

== Facts passed to the incident team ==
1. **To LC (Q20):**
   - Timeline v1 at 20:00 HKT, with uncertainty bands.
   - Facts that are confirmed: the 320 customers, the export times within their bands, use of the vendor credential.
   - Facts that are unverified: the 18,000 claim, attribution, the link of the new indicator.
   - The log-coverage gaps and the clock-sync shortfall, for the written report.
2. **To the CEO:** containment confirmation reopened; sweep result at 14:00; any stop of secondary releases; recovered system still on HOLD.
3. **To the DPO and COM:**
   - The validated file confirms the same 320 customers, so the timeline sets no new scope.
   - SEC will cross-check the 31 scam reports against the 320 and against the fake-page indicators. Any victim outside the 320 is evidence that could widen the scope.
4. **To Fraud:** the new indicator and the fake-page indicators for monitoring.