# AI Usage Appendix

FIN4021 group project, Topic 5 (ransomware and operational resilience). Prepared 18 November 2026, Hong Kong time (HKT).

The group used AI tools at every stage of the project, and the tabletop exercise itself is run by AI agents. This appendix lists each tool, what it was used for, what the group kept, rewrote or discarded, and how members verified the output. Full prompts and outputs are in [`../Claude Code transcripts/`](../Claude%20Code%20transcripts/00%20INDEX.md). They are cited below by session and turn, for example "S07 T3" (session S07, user turn 3).

## 1. Tools used

| Tool | Provider | Model and effort | Dates of use (HKT) | Used for | Where the prompts are |
|---|---|---|---|---|---|
| Claude Code (desktop app), main assistant | Anthropic | Claude Opus 5.5 and Claude Fable 5.2; the lead switched models with `/model` (each transcript header lists the models). The effort setting of the main sessions is not stored in the session files | 16 to 18 Nov 2026 | Checking the source register against the originals; correcting the evidence cards; building the tabletop script, run packages and tool-permission setup; facilitating runs A1, B0 and B1; citation checks; drafting scores for members to rule on; drafting playbook PH01; drafting and editing the English report and evidence appendix; assembling this package | S01 to S11, every "USER" turn |
| Claude Code role agents, run A1 | Anthropic | Claude Fable 5.2, effort xhigh (recorded in `推演记录/A1/00 运行记录.md`) | 18 Nov, 00:37 to 02:07 | Four role agents (security, legal and compliance, communications, CEO) answering cards C01 to C08 and Q25 from the regulatory sources only | S05-A01 to S05-A04 |
| Claude Code role agents, test round B0 | Anthropic | Claude Opus 5.5, effort Medium | 18 Nov, 15:11 to 16:10 | First B run with PH01 added; archived and not used in the comparison | S06-A01 to S06-A04 |
| Claude Code role agents, run B1 | Anthropic | Claude Opus 5.5, effort xhigh (stored in the agent metadata) | 18 Nov, 16:39 to 18:31 | Rerun of the B round with PH01 added; the run compared with A1 in the report | S07-A01 to S07-A04 |
| Claude Code helper sub-agents | Anthropic | Claude Opus 5.5, Claude Fable 5.2, Claude Haiku 5.5 (see the index) | 17 to 18 Nov | Parallel helper tasks (each file's first turn states the task): the permission test (S04), drafting scores card by card (S05-A05 to A08 for A1; S07-A05 to A08 for B1), one web fetch (S07-A09) | The sub-agent files listed in the index |
| Gemini 4 Argon | Google | Effort not recorded | On or before 16 Nov; exact date not recorded | Produced the environment register (I01) and the evidence cards (I02); member A verified them | Not held in the project folder (see Section 5) |
| GPT6.1 Sol | OpenAI | Extra High | As recorded in the saved session | Generated the first Lan Tidal Bank scenario plan | The whole session is saved as `岚汐银行-推演方案生成会话.md` in the package root |
| Grok Bot | xAI | Not recorded | 17 Nov | Fetched seven official files (Cap. 653, Cap. 486, Cap. 455, Cap. 575 and three HKMA circulars); the retrieval record is merged into batch 5 of `Primary source/00 更新记录.md` | Not held in the project folder (see Section 5) |

The conflict ledger (I03) was also machine-drafted; the tool is not recorded in the project files.

## 2. Purpose by deliverable, and who decided

| Deliverable | What the AI did | What group members did |
|---|---|---|
| Source register (`Primary source/00 来源清单.md`) | Claude compared each entry with the original file and recorded what it had read | Members supplied the originals, approved every addition to the folder (for example S01 T23, S07 T10), and fill the "checked by" and "result" columns |
| Evidence cards and ledgers (I01 to I04) | Gemini 4 Argon drafted I01 and I02; Claude corrected them and I03 on instruction | The lead found the errors and listed them (S01 T6, T10, T14), then accepted the corrected files (S01 T8, T16, T17) |
| Tabletop script and run packages | GPT6.1 Sol proposed the scenario; Claude built the script, the frozen source packages and the restricted role agents | The group set the run method, the source whitelist and the model settings (S01 T21 to T30, T32), and approved the script |
| Sealed expectations (`组员预注册/`) | Claude prepared the expectation files under the lead's direction (S05 T2 to T4) | Members decided the contested items, signed off version 2 (S05 T5) and sealed the playbook-side expectations (S06 T15); each file has a SHA-256 seal made before the run |
| Runs A1, B0, B1 | The role agents produced every answer and CEO ruling; Claude facilitated and logged | The lead started, paused and redirected the runs (S05 T5 to T9, T17 to T20; S06 T17; S07 T2) |
| Scores | Claude drafted a score and reason for each of the 48 units in each run | Members ruled on the open and disputed units and accepted the result: A1 in three rounds (S05 T24 to T27), B1 in S07 T6 and T7 |
| Playbook PH01 | Claude drafted v0.1 from the A1 gap analysis | The group revised it in three rounds and ruled it final (S05 T15, T16; S06 T13, T14) |
| Report, Parts 2 to 4 | Claude drafted from the checked register and the A1 scores | The lead reviewed in three rounds and directed the changes (S06 T10 to T12); see `Report/修订记录.md` |
| Report, Parts 1 and 5 to 8; evidence appendix | Claude drafted from PH01 and the accepted scores (S07 T8), then cut the body to 15 pages (S09 T5) | The lead corrected facts and wording (S07 T9, T10) and gave final approval |

## 3. What was kept, rewritten or discarded

**Kept as produced.** The role answers and CEO rulings of A1, B0 and B1 are kept exactly as the agents wrote them, with checksum files. They are data, and nobody edited them.

**Rewritten by the group.**

- A1 scores: members changed Q05a, Q13b, Q14a and Q23a in the first round, Q14b and Q15b in the second, and Q24a and Q12a in the third.
- B1 scores: members ruled Q12a to GAP and confirmed Q06a, Q24a and Q24b.
- PH01: sections 2.3 to 2.4, 5.6 to 5.7, 8.6 to 8.7, 9.3, 9.5 and 17.2 were amended on group comments.
- Report: Section 3.3 was rewritten; the United States column in Section 3.4 and the Hong Kong case facts in Section 3.5 were corrected; the statement that members "do all scoring" was corrected to say that members sealed the expectations and reviewed and finalised the scores.

**Discarded.**

- Test round B0 as a comparison run. It ran at Medium effort; on review, several answers left too little search record to verify their basis (for example Q07b), so the group reran the round at xhigh. The decision was taken after seeing B0's preliminary results (S06 T17, S07 T2).
- An earlier scenario (Qingyu Bank), replaced by the Lan Tidal Bank script.
- Runs A2, A3, B2 and B3, cut for budget (S05 T12).
- AI statements that failed a source check. The correction log has 29 entries. Examples: "ICBC paid a ransom" (only the attackers claimed this), "the Police advise against paying" (no official source found), "OR-2 sets fixed 2023 and 2026 deadlines" (the text gives periods, not dates), "payment report: not required" for the United States (New York requires one within 24 hours).

## 4. How members verified AI output

1. **Sources.** Every cited source is an original file in `Primary source/原文/`. The register records, for each source, what was compared with the original and who checked it. No citation in the report rests on an AI summary alone.
2. **Correction log.** Each AI error found is logged with what the AI said, what the source says and the fix. The full log, in English, is in [`Correction log (English).md`](<Correction log (English).md>); the Chinese original is section 4 of the 计划与分工 tab of the work document. Of the 29 entries, the lead found 13 during review; Claude found the rest while checking originals.
3. **Sealing before the runs.** Expected answers were sealed with SHA-256 files before A1 and before B1, so scores could not be fitted to the answers.
4. **Citation checks on the agents.** A script extracted every quoted passage from the role answers and compared it with the frozen source text. In A1 all 710 citations were traced; in B1 no invented quotation was found. See `推演记录/A1/核验/A1 引文核验.md` and `推演记录/B1/核验/citations.csv`.
5. **Scoring.** Scores follow the rule fixed in the script before the runs. Claude's drafts list a reason and a record reference for each unit; members ruled on the disputed units and the lead accepted the final sheets (S07 T7).
6. **Report text.** After each edit the local copy was compared with the work document paragraph by paragraph using hashes (`Report/修订记录.md`). The lead's review found the factual errors listed in the last four rows of the correction log.

Limits. A link check run from the project computer opened 18 of the 49 register links; 27 Hong Kong government and ICBC FS links could not be reached from that computer and 4 sites refuse scripted access, so those links were not re-tested there.

## 5. Material that could not be included

- **Claude sessions before 16 November 2026, 23:44 HKT.** The source register and the first version of the work document were drafted on 14 and 15 November. Those sessions are not in the local Claude Code project folder, so they are not in the transcripts. Session S01 opens with the handover text pasted from that earlier work.
- **Prompts for Gemini 4 Argon and Grok Bot.** They are not held in the project folder. Their outputs (I01, I02 and the seven fetched files) are in the package.
- **The tool that drafted I03.** Not recorded.
- **Hidden reasoning and raw tool results.** The transcripts contain the visible inputs and outputs. They omit the models' hidden reasoning blocks, system reminders added by the app, and the raw results of tool calls (file contents and command output). The files those results came from are in this package.
- **Effort settings.** The session files store the effort setting only for the B1 role agents. The A1 and B0 settings are taken from the run records.
- **Overlap.** Claude Code starts a new session file when a long session is continued. S01 to S03 share their opening turns, and so do S08 to S11.
