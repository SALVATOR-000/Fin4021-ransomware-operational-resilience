Ransomware and Operational Resilience: When a Bank Gets Locked Out
FIN4021 group project, Topic 5, completed on 18 November 2026 (Hong Kong time).

For a bank hit by ransomware, the project asks which first-72-hour decisions Hong Kong's rules settle, which they leave to the bank, and whether a playbook closes the gap. To test this, the group ran a 72-hour tabletop exercise at a fictional bank, Lan Tidal Bank (岚汐银行). AI agents acting as security, legal and compliance, communications and the CEO made 48 scored decisions in each run: run A1 from 19 frozen Hong Kong primary sources alone, and run B1 with the group's playbook PH01 added.

Result in brief. B1 scored 88 of 92 and A1 scored 83. The playbook changed decisions where it set an owner, a condition and a record. It did not correct misreadings of external law: four such errors recurred in B1. Each run was performed once and the two runs used different models, so the report treats the results as indicative. Report Section 7.2 has the detail.

This repository holds the report and everything behind it: the exercise design, both run packages, every agent answer and CEO ruling, the scoring sheets, the original sources, the AI Usage Appendix and the full Claude Code transcripts. Start with the report, then use this page to trace any score, case or citation back to its record.

Most working records are in Chinese, the group's working language. The scenario cards, role prompts, role answers, CEO rulings, playbook PH01 and the report are in English. Times are Hong Kong time (HKT). Lan Tidal Bank is fictional, and this is a student project, not legal or regulatory advice.

中文简介 FIN4021 小组项目（专题 5：勒索软件与运营韧性），2026 年 11 月 18 日（香港时间）完成。项目研究银行遭勒索软件攻击后头 72 小时的决策：哪些由香港的法规定死，哪些留给银行自己定，一份内部应急手册能不能补上缺口。小组在虚构的“岚汐银行”上做了 72 小时桌面推演，由 AI 角色（安全、法律合规、对外沟通、CEO）每轮作出 48 项计分决策：A1 只看 19 份冻结的香港一手来源，B1 另加小组写的手册 PH01。本仓库是报告和它背后的全部材料：推演设计、两个运行包、每一份角色作答和 CEO 裁决、评分底稿、原始来源、AI 使用附录和完整的 Claude Code 对话记录。报告、情景卡和角色作答是英文，工作记录多为中文；以下说明为英文。
Start here
Final report (PDF); an editable copy in Markdown is beside it
Evidence appendix (PDF)
AI Usage Appendix; a Word copy is beside it
Claude Code transcripts index
To download everything, use Code → Download ZIP on GitHub.

Folder guide
Folder	Files	Contents
01 Report	6	The final report and evidence appendix in PDF, editable copies, and the revision log.
02 Exercise Design	42	The facilitator script, PH01 and its A1 gap analysis, sealed expectations, the specification review, and the tools and configurations used to prepare and run the exercise.
02.1 Run Package A	63	The frozen package for run A1: scenario cards, prompts, and the 19 sources as PDF and as the text the agents read.
02.2 Run Package B	65	The same package with PH01 added, for the B round.
03.1 Run Records A1	91	Run A1: original answers, CEO rulings, handoffs and the run log, card by card.
03.2 Run Records B1	90	Run B1, in the same form.
03.3 Scoring and Read Logs	61	Scoring sheets and citation checks for A1 and B1 (A1 核验, B1 核验), and the log of every search and page read (读取记录).
03.4 Test Round B0 Run Records	90	The run records of test round B0, in the same form as A1 and B1.
03.5 Test Round B0 Archive	28	The rest of the B0 archive: the archive note, its checksum file, the role configuration, the raw role sessions and the read logs.
04 Sources and Research	91	Original sources and their register, the A/B frozen whitelist and source checklists, the environment register, evidence cards, and the conflict ledger.
05 AI Use and Transcripts	54	The AI Usage Appendix and correction log, the Claude Code transcripts, and the earlier scenario-generation session.
The first two digits of a folder name mark the part it belongs to: 02 is the design, 03 the runs, 04 the sources, 05 the AI use. Parts 02 and 03 are split into several folders so that no folder holds more than 100 files, which is the most GitHub accepts in one browser upload.

1. How the exercise was designed
Script. 岚汐银行-72小时勒索软件桌面推演.txt sets the scenario, the 24 questions (48 scored decisions), the scoring rule and the run method.
Eight scenario cards. C01 to C08, plus Q25 for the CEO. The A package has the same cards in 02.1 Run Package A/cards/.
Role prompts. The folder prompts holds the common prompt, one prompt per role (SEC, LC, COM, CEO), the CEO wrap-up prompt, the reading note and the system prompt. The agent definitions are in Role agent definitions. Each role transcript also ends with the system prompt the agent actually received.
Playbook PH01. PH01 v1.0. The copy given to the B agents is in the B package. The gap analysis it was drafted from is A1 缺口分析.md.
Sealed expectations. A1, regulatory side: v2 (v1 is kept beside it). B1, playbook side: v1 and the sealed B1 score sheet. Each has a .sha256 file made before the run.
The 19 frozen sources. A-B 共用白名单（2026-11-17 冻结）.md lists each document with its version and official source, and its .sha256 file fixes the 19 files. The agents saw them as SOURCE_MANIFEST.md and the text files in sources/text/. The originals are in 04 Sources and Research/Primary source/原文/; the source register maps exercise IDs (R01 to R16) to report IDs (H, L, F).
Tool restriction. Role agents could only search and read the frozen sources through sources_server.py. The permission test is in 02 Exercise Design/Technical Setup/权限试验（模拟文件）/, and its read logs are in 03.3 Scoring and Read Logs/读取记录/ (PERMTEST-1, PERMTEST-2).
2. What happened in the runs
Run	Model and effort	When (18 Nov, HKT)	Run record	Final scoring	Role transcripts
A1: regulatory sources only	Claude Fable 5.2, xhigh	00:37 to 02:07	00 运行记录.md	A1 评分底稿汇总.md	S05-A01 to S05-A04
B0: test round with PH01 (not compared)	Claude Opus 5.5, Medium	15:11 to 16:10	00 归档说明.md, 00 运行记录.md	Not scored	S06-A01 to S06-A04
B1: sources and PH01	Claude Opus 5.5, xhigh	16:39 to 18:31	00 运行记录.md	B1 评分底稿汇总.md	S07-A01 to S07-A04
Each run folder (03.1, 03.2, and 03.4 for B0) has one sub-folder per card, C01 to C08, and Q25. In each card folder:

SEC.raw.md, LC.raw.md, COM.raw.md are the role agents' original answers;
CEO.final.md is the CEO agent's ruling on those answers;
handoff.md is the facilitator's status log and handoff to the next card;
input.<ROLE>.txt is exactly what each role received.
记录索引.jsonl indexes the records, and the .sha256 file in each run folder fixes them. The log of every search and page read is in 03.3 Scoring and Read Logs/读取记录/ for A1 and B1, and in 03.5 Test Round B0 Archive/读取记录/ for B0.

Why B was rerun. The first B run (B0) used Medium effort to save budget. A1 had run at xhigh. When the group reviewed B0's preliminary results, several answers gave a reasonable action but left too little search record to show that the most relevant rule had been checked. In Q07b, for example, B0 handled the vendor credential under the playbook without citing the applicable provision, which B1 cites. The lead ordered a rerun at xhigh at about 16:35 HKT on 18 November, after B0's results had been seen (transcript S07, turn 2). The report compares A1 with B1. B0 is archived as a test round and is not part of the comparison.

3. How to verify the findings
Final comparison. Report Section 7.2 gives the totals. Evidence Appendix Section C lists all 48 decisions. The source sheets are B1评分底稿_CEO最终.csv and B1评分底稿_原始作答.csv, which show A1 and B1 side by side. In each cell the order is: regulatory code / playbook code / action score / basis score / decision code / record reference. B1评分底稿_明细.csv adds the reason for every score.

Evidence chains for the cases in the report.

Case	A1 record	PH01 clause	B1 role answer	B1 CEO ruling
Q13b, test data	A1 C05 SEC, lines 67 to 92	§9.2	B1 C05 SEC, lines 113 to 117, 163, 176	B1 C05 CEO, lines 92 to 108
Q16a, recovery gate	A1 C06 CEO, line 20	§3 (return to production), §9.2, §9.3	B1 C06 SEC, lines 15 to 21	B1 C06 CEO, lines 36 to 43
Q24a, closing update	A1 C08 COM, line 82	§11.5, §11.2	B1 C08 COM, lines 18 to 20, 77, 82	B1 C08 CEO, lines 313 to 336
Q23a, changes by deployment date	A1 C08 LC, lines 16, 18, 59, 138	§18.4	B1 C08 LC, lines 37 to 54, 117, 124	B1 C08 CEO, lines 177 to 246
The line numbers count lines of the Markdown source. On GitHub, open the file and choose Code instead of Preview to see them.

The misreadings that the playbook did not fix (Q05a, Q14a, Q14b, Q15b) are explained in Section 5 of the B1 scoring summary.

Worked example: tracing Q13b from the report to the score.

The report says (Section 7.2, "Q13b, test data") that A1 planned its offline reconciliation on live ledger extracts, and that B1 made de-sensitisation and prior approval preconditions for testing.
The rule is PH01 §9.2. Open PH01 v1.0 and find "9.2 Offline testing and pass mark".
A1's answer is in A1 C05 SEC.raw.md, lines 67 to 92. It names the data sets but sets no de-sensitisation or approval step.
B1's answer is in B1 C05 SEC.raw.md, lines 113 to 117. It writes both preconditions and cites PH01 §9.2 and TM-G-1 §4.2.4.
The CEO's ruling is in B1 C05 CEO.final.md, lines 92 to 108. It confirms the answer as written.
The score is the Q13b row of B1评分底稿_CEO最终.csv. Column A1 reads GAP / NA / 0 / 1 and column B1 reads GAP / OK / 1 / 1, so the action score rose from 0 to 1. The sealed expectation for Q13b is in the same row and in the sealed expectation files.
The full session in which the B1 security agent wrote this answer is transcript S07-A01 in Claude Code transcripts.
Re-checking with the existing records. Run these commands from the repository root, in a macOS or Linux shell. If you clone with Git on Windows, use git clone -c core.autocrlf=false, or download the ZIP: line-ending conversion changes the files, and the checksums then fail.

Scoring. The script regenerates the three B1 sheets in a scratch copy of the scoring folder, and diff compares them with the stored ones.

scratch="$(mktemp -d)"
cp -R "03.3 Scoring and Read Logs/B1 核验" "$scratch/B1"
python3 -I "02 Exercise Design/Technical Setup/转换脚本/merge_scores_b1.py" \
"02 Exercise Design/组员预注册/岚汐银行-B1评分表-v1封存.csv" \
"03.3 Scoring and Read Logs/A1 核验" "$scratch/B1"
diff -r "$scratch/B1" "03.3 Scoring and Read Logs/B1 核验" && echo "regenerated sheets match the stored ones"
Run records, run packages and sealed expectations. The paths in these checksum files are relative to the folder each file sits in.

(cd "03.1 Run Records A1" && shasum -a 256 -c A1校验.sha256)             # 88 entries
(cd "03.2 Run Records B1" && shasum -a 256 -c B1校验.sha256)             # 87 entries
(cd "03.4 Test Round B0 Run Records" && shasum -a 256 -c B1校验.sha256)  # 87 entries
(cd "02.1 Run Package A" && shasum -a 256 -c 运行包校验.sha256)           # 60 entries
(cd "02.2 Run Package B" && shasum -a 256 -c 运行包校验.sha256)           # 63 entries
(cd "02 Exercise Design/组员预注册" && for f in *.sha256; do shasum -a 256 -c "$f"; done)  # 4 entries
The checksum file in the B0 run folder is named B1校验.sha256 because that round ran under the name B1 before it was archived.

B0 archive. The archive's checksum file lists the run records under 运行记录/, which is now the folder 03.4 Test Round B0 Run Records. This command translates that path and verifies all 116 entries.

(cd "03.5 Test Round B0 Archive" &&
sed 's|  运行记录/|  ../03.4 Test Round B0 Run Records/|' B0归档校验.sha256 | shasum -a 256 -c -)
Frozen sources. The whitelist checksum file records paths from the working folder. This command translates them and verifies all 41 entries (19 originals, 19 text versions, and 3 scan images).

sed -e 's|  Primary source/|  04 Sources and Research/Primary source/|' \
  -e 's|  推演记录/岚汐运行包（A版）/|  02.1 Run Package A/|' \
  "04 Sources and Research/Source Review/A-B 共用白名单（2026-11-17 冻结）.sha256" |
shasum -a 256 -c -
Role definitions and tool scripts. The two checksum files in 检索入口/ cover the eight role definitions and the two scripts behind the tool restriction (6 entries each).

(cd "02 Exercise Design/Technical Setup" && for f in 检索入口/*.sha256; do
sed -e 's|  \.claude/agents/|  Role agent definitions/|' -e 's|  推演记录/检索入口/|  检索入口/|' "$f" |
  shasum -a 256 -c -; done)
Citations. A1 引文核验.md and the two citations.csv files list the quotations checked. verify_quotes.py takes the run folder, the sources/text/ folder of the matching run package, and an output folder. For B1 it reproduces the stored table exactly:

scratch="$(mktemp -d)"
python3 -I "02 Exercise Design/Technical Setup/转换脚本/verify_quotes.py" \
"03.2 Run Records B1" "02.2 Run Package B/sources/text" "$scratch/quotes"
cmp "$scratch/quotes/citations.csv" "03.3 Scoring and Read Logs/B1 核验/citations.csv" && echo "citation table matches the stored one"
For A1, use 03.1 Run Records A1 and 02.1 Run Package A/sources/text. The stored A1 table has the same rows with two more columns, class and note.

AI use. The AI Usage Appendix lists every AI tool, its model and effort, dates and purpose, what the group kept, rewrote or discarded, and how members verified the output. The correction log lists 29 AI errors and their fixes. Prompts are cited by session and turn in the transcript index.

Paths written inside the records
The records were written in the group's working folder and cite files by their paths there, for example 推演记录/B1/核验/citations.csv. The files are the same; only the folders differ.

Path in the records	In this repository
Report/	01 Report/
岚汐银行-72小时勒索软件桌面推演.txt	02 Exercise Design/
推演记录/PH01/	02 Exercise Design/PH01/
I04_规格审查.md and its appendix	02 Exercise Design/Specification Review/
.claude/agents/	02 Exercise Design/Technical Setup/Role agent definitions/
推演记录/权限试验（模拟文件）/, 推演记录/检索入口/, 推演记录/转换脚本/	The folder of the same name in 02 Exercise Design/Technical Setup/
组员预注册/	02 Exercise Design/组员预注册/
推演记录/岚汐运行包（A版）/	02.1 Run Package A/
推演记录/岚汐运行包（B版）/	02.2 Run Package B/
推演记录/A1/, except 核验/	03.1 Run Records A1/
推演记录/B1/, except 核验/	03.2 Run Records B1/
推演记录/A1/核验/, 推演记录/B1/核验/	03.3 Scoring and Read Logs/A1 核验/, 03.3 Scoring and Read Logs/B1 核验/
推演记录/读取记录/	03.3 Scoring and Read Logs/读取记录/
推演记录/B0 测试轮 · Opus 5.5 Medium/运行记录/	03.4 Test Round B0 Run Records/
The rest of 推演记录/B0 测试轮 · Opus 5.5 Medium/	03.5 Test Round B0 Archive/
Primary source/	04 Sources and Research/Primary source/
I01_环境登记表.xlsx, I02_证据卡/, I03_冲突台账.xlsx	04 Sources and Research/Research Notes/
A-B 共用白名单（2026-11-17 冻结） (both files), A版原文核对清单.md, A版剩余取件清单.md	04 Sources and Research/Source Review/
AI Usage Appendix/, Claude Code transcripts/, 岚汐银行-推演方案生成会话.md	05 AI Use and Transcripts/
The transcript exports, run indexes and runtime configurations record the same working-folder paths. A fresh replay requires configuring the role and tool paths for the new workspace.

Third-party documents
04 Sources and Research/Primary source/原文/ and the sources/ folders of the two run packages hold copies of official publications: legislation, regulatory guidance, circulars and reports. They are kept so that every citation can be checked against the text the group and the agents actually used. They belong to their publishers. The source register identifies each document and its issuing body, with the official link for most of them; for any other use, take the document from its official source.

Known gaps
Claude sessions from before 16 November 23:44 HKT, and the prompts given to Gemini 4 Argon and Grok Bot, are not in the project folder and so are not in this repository. The AI Usage Appendix, Section 5, gives the detail.
The transcripts omit hidden reasoning blocks, system reminders and raw tool results; the index explains this.
Links in the source register were not all re-tested: Hong Kong government sites could not be reached from the project computer. The original files are in 04 Sources and Research/Primary source/原文/.
The AI Usage Appendix and the transcripts end on 18 November 2026. Arranging the files into the folders of this repository and rewriting this README were done on 19 November 2026 with Claude Code, and those sessions are not included. Three files differ from the package finalised on 18 November: this README, one link target in 04 Sources and Research/Source Review/A版原文核对清单.md, and the file properties of 04 Sources and Research/Research Notes/I01_环境登记表.xlsx, from which a personal name was removed (the sheets are unchanged). Every other file is byte-identical.
