# 岚汐银行 A 版监管侧预期

**版本** v2，在 v1（Codex 赛前复核稿）上按主笔 2026-11-18（香港时间）的两项决定修订，已生成封存校验值，待组员签核。  
**封存时间** 2026-11-17 11:22:14 EST（香港时间 2026-11-18 00:22:14 HKT）  
**上一版** `岚汐银行-A版监管侧预期-v1封存.md`，SHA-256 `320dda5fb25907c6f42e944364ed7f12c7b0bd807ad0482f26d5a331c8205046`，封存于 2026-11-17 03:52:22 EST（香港时间 2026-11-17 16:52:22 HKT），原样保留。  
**范围** C01–C08 的 24 题、48 个计分单元。Q25 为不计分复盘。PH01 等 I11 定稿后在 B 版前登记。  
**保管** 主持人和组员保管本文件。实际角色输入按运行包发放。

这份预期是在查看任何正式作答前形成的。核对时运行目录只有权限试验记录，当前运行标识为 `PERMTEST-2`，未读取正式作答。v1 由 Codex 依据冻结原文起草和复核。v2 的修订由 Claude（Anthropic，Claude Fable 5.2）按主笔的决定执行，只改了下一节列出的地方；修订时运行目录仍只有权限试验记录（PERMTEST-1、PERMTEST-2），当前运行标识仍为 `PERMTEST-2`，没有任何正式作答。组员采纳及签核另行登记，记录真实签核时间。若组员在 A1 之前修订题面、交接或预期，将修订另存为新版本并记下原因和校验值。

## v1 到 v2 的修订

**原因** 主笔在 2026-11-18 00:01 和 00:15（香港时间）作了两项决定：Q20b 题面写清通报路径、收件方留给角色判断；CEO 确认或推翻按同一条规则记，这条规则也写进 CEO 的英文提示词。两项都发生在 A1 之前。

| 位置 | 改了什么 |
| --- | --- |
| 版本、封存时间、起草说明 | 改为 v2，写明上一版及其校验值、修订人和修订时的运行目录状态 |
| 剧本和权限试验复核 | 「剧本与运行包」「冻结原文」两条各加一句 v2 的重新核对结果 |
| 主笔开跑前需拍板的两处 | 第 1 处记为已定；第 2 处记下 CEO 裁决的记法已定，其余待决定项照旧 |
| 复核基准 | TXT、候选依据附录、运行包校验三项换成修订后的校验值，另三项与 v1 相同 |
| 评分判据第 4 条 | 换成主笔定下的规则原文和记录办法 |
| Q20b | 加一条「v2 题面」。监管预期、原文定位、可接受行动、决策码、检索与核验都没有改 |
| 组员采纳记录 | 采纳一栏注明针对 v2 |

**没有改的** 48 个单元的 Y／N／U 判定、原文定位、可接受行动、决策码和检索记录。Q09a、Q18a 决策码一行里关于 CEO 确认的话与新规则一致，原样保留。

**请组员签核时留意**

1. Q20b 新题面要求写明向谁交。本预期把收件方（专员）写在「监管预期」一栏，「可接受行动」一栏没有写。是否在可接受行动里补上，由组员定。
2. v1 评分判据写的是 “CEO 另加条件或改变动作、对象或时点时按推翻”。新规则写的是 materially change，并写明只补理由或纯记录字段仍算确认。两者是否有判分上的差别，由组员定。
3. v2 没有重做 Codex 对 v1 的全面复核，只核对了改动的地方。

## 剧本和权限试验复核

- **剧本与运行包** 核对了项目中的最新版 TXT。八张运行卡与 TXT 逐张一致，SEC、LC、COM 各八道计分题。角色连续会话、英文交接及香港时间、LC 的知悉时间与实际通报记录、Q23a 的执行变更分支均已落实。核对范围以项目 TXT 和运行包为准。 v2：TXT 第 23、102、182、253 行按主笔决定修改、文末加了修订说明以后，Claude 用脚本重新核对，运行包的 9 个卡片文件和 8 个提示词文件仍与 TXT 逐字一致；改动的是 `cards/C07.txt`（Q20b）和 `prompts/CEO.txt`。
- **权限试验** 从两轮原始轨迹及检索日志交叉核对。PERMTEST-1 四角色共收到 50 次检索拒绝，属于模拟越权或非法参数试验。白名单外的工具被平台先拒绝，独立闸门试验与角色轨迹分别留存。PERMTEST-2 四角色均成功读 R01 PDF 第 97 页，各有四次检索成功；四份轨迹均无项目记忆索引和启动说明附件。每个角色的辨认短语在收到的第一条模拟卡消息出现一次、其答复出现两次。模型记录为 `claude-fable-5-2`，角色定义与试验结果所记的请求档位为 `xhigh`。试验的索引识别标准中途调整，采用结果文件已记录的口径。
- **冻结原文** 41 项共用清单、60 项运行包校验和 6 项角色定义及检索脚本校验全部匹配。19 份原件、运行包 PDF、清单所列页数及文字版都对应。候选附录的 140 段引文逐段核对所注页码及 25 词上限，其中 122 段对照 PDF 文字层，R05 的 18 段结合 OCR 及三页扫描原图复核。逐字核对容纳普通的断词空格和版式差异，R05 用 PDF 页码和小标题定位。 v2：运行包校验文件里 `cards/C07.txt` 和 `prompts/CEO.txt` 两行已更新，60 项重新核对全部匹配；共用清单 41 项和检索入口 6 项没有变，重新核对仍全部匹配。140 段引文没有重新核对，候选附录只改了 Q09a、Q18a、Q20b 三处回查提示的文字。

### 主笔开跑前需拍板的两处（v2：第 1 处已定，第 2 处定了一部分）

1. **Q20b 收件方（主笔 2026-11-18 香港时间已定）。** 题面改为 “b. For the same statutory incident-reporting process as in Q20a, decide how to prepare, assign and submit the separate written incident report. State who is responsible, to whom it is submitted, what is submitted and by when.” 收件方不写在题面上，由角色从原文找出，这仍是判分点。本预期继续按第 28(4) 条的专员路径判。v1 提出的在题面加 “to the Commissioner” 没有采用，主笔的理由是这会把答案给出去。TXT 第 102 行和 C07 包已同步，修订文件的校验值见下表。
2. **条件回答和交接。** CEO 裁决怎样记（I04 D3）主笔已于 2026-11-18（香港时间）定下，见评分判据第 4 条；D2 见上一处。I04 的 B2–B6、D1 仍有待决定项。本版按角色实收的交接判分，缺失状态可以用条件答复。请主笔确认这点是否足以按现版运行，或先补实际已执行的遏制、凭证处置、队列处理、公开稿和生产状态等必要交接。Q05a／Q14a 各在原单元内分别判断立场与法律闸门。

### 复核基准

| 项目 | SHA-256 |
| --- | --- |
| 岚汐银行-72小时勒索软件桌面推演.txt | `603174630fc7b19bbe349759fecf1dab83068f7f0609b145b8290120dcc9d75f`（v2 修订后；v1 为 `3fec0fa19e5a8308db0d2493a0c06e9498a92c51fd7ddecc2ef7de5ce2192e00`） |
| 试验结果.md | `a119b74958e064ef577305fd04ce009680970c6dff4109f95d4c6c48ad5f6ea8` |
| A-B 共用白名单（2026-11-17 冻结）.sha256 | `bd64dd118b2edbfe7fa2b0f915a644160badc375e9fe777c8e3d09ef0b78616b` |
| I04_规格审查_候选依据附录.md | `8e5675c4e2d5cc9a5d270df272a6915683b008d3217c6041516103396ee6f775`（v2 修订后；v1 为 `50e643745683f56f0b68b33438636547e60225240e241c61da14321ef2dd025f`） |
| 运行包校验.sha256 | `febe072f4af6ca650beeb60c2feadd6ad0710cf7949b9ebfc2d37af6de640a3e`（v2 修订后；v1 为 `3dcf5b5e22a4dd7577c9dbbb503c8b78f2c462f731b7bebe60515a8b049f3913`） |
| 检索入口校验.sha256 | `ad713bab0b372353c300eac4b1720dddd2416f91983cfa56f7e7ded668455108` |

## 监管预期和评分判据

- **Y** 表示冻结包里有直接支持某个明确决定或必要条件的条文。混合单元列明具体覆盖的是哪一部分，其他部分仍按判断处理。**N** 表示在冻结包已检索和定位的范围内，只有一般原则或相近规定，具体决定未发现直接规则。**U** 表示关键事实或交叉引用原文未能核实。已写明分支的按本轮当时可知事实选择。静态登记为 Y 24、N 18、U 3、随分支 3。实际适用分母按分支确定。
- 依据分依剧本记录 OK、ERR、MISS、GAP、NC 或 U。N 下要取得 GAP，仍须由复核者确认搜索范围，且角色列出可复核的检索并说明专业判断。法规、守则、金管局指引和建议按各自性质判断，R02 第 7 节的第 3 类要求与 R03 的银行业第 1、2 类要求分别适用。无法回查 C-RAF 或别的交叉引用时，先核白名单来源能独立支持到哪一步。A 版 PH 判定为 NA。
- 备选行动列给出可接受的行动、责任人、时点或触发、收件方或执行目标。满足相同必要条件的其他可实施方案也可得行动分。使用决策码时同时记关键范围、时点和对象，按本轮事实编码。分支缺事实时，写明谁核、何时核、核到以后做什么。
- 原答和 CEO 裁决各评分一次。CEO 确认还是推翻，按主笔 2026-11-18（香港时间）定下的规则记。这条规则写进了 CEO 的英文提示词，原文是 “Mark CONFIRM if you select a branch explicitly stated in the original answer and keep its action, timing, recipient, and conditions as written. Mark OVERRIDE if you materially change any of those. Adding a reason or filling in a record field alone still counts as CONFIRM.” 剧本第 23 行的中文写法是：原答已写明几个分支的，CEO 选中其中一个并采用原答对应的内容和条件，记确认；CEO 的决定（包括附条件批准）改变原答动作、时点、收件方或门槛，记推翻；只补一条理由或补齐纯记录字段，仍记确认。CEO 自己填的标签照原样留在记录里。组员评分时看实际裁决，按同一规则记 C／O；和 CEO 填的有出入，就在同一条记录里注明。
- 首报、补表和书面事故报告分别按其起算点判。C01 专员首报从 16 日 08:00 HKT 知悉时起，尽快且最迟同日 20:00。需要补表时，从本轮有效的非指定方式通知实际发出时点起算 48 小时，即使该首报逾期。书面事故报告从知悉的日期起算，到 11 月 30 日。Q23a 重大变更须结合实际执行记录。

## C01

### Q01a · SEC · 隔离范围与方式

- **监管预期 N** ERP须覆盖遏制，通函要求及时遏制并保障客户，电子银行适用时须保持其他渠道容量。原文未指定网关的首隔离对象或可用服务保护方式。C01尚不知个人资料外泄，R16a附件切断受陷设备的例示不可当作本卡强制规则。
- **原文定位** 旁证 R02 p32 §7.2.3(a)(v)(1)，R05 p1 Immediate incident response，R09 p37 §9.5.4，R16a p4 数据外泄附件
- **可接受行动** 08:00 HKT立即由SEC安排网络/SOC隔离受影响网关组件或段，阻断可疑路径，验证余额查询和分行业务的依赖与健康并保留其服务。只有扩散证据或无法分段时才扩大隔离并告知指挥人与受影响营运团队。未经验证的故障转移先不启用。
- **决策码** ISOLATE_TARGETED / ISOLATE_EXPANDED_CONDITIONAL
- **检索与核验** 全包19份逐页检索 first isolate、disconnect compromised、segment、containment、essential service、other service channels、failover，复阅R02 §7.2.3、R05、R09 §9.5.4和R16a附件。

### Q01b · SEC · 证据保全

- **监管预期 Y** 第3类应急计划须含数字证据及保管链。当业务受影响、需迅速控损或立即恢复，R02(f)直接规定取证与遏制/恢复的优先取舍。指定网关日志的防篡改及最少6个月保留仅适用于日志。取证顺序细节和记录格式仍为判断。
- **原文定位** R02 pp32–33 §7.2.3(a)(v)(2)、(f)、(h)，R03 p18 §6.2.23(b)–(d)
- **可接受行动** 08:00 HKT SEC安排具资质取证人员先在安全可行时保全易失数据、网关/验证/网络日志、加密痕迹、勒索材料和镜像。必要遏制优先，可并行获取。原件只读封存，记录来源、采集人、HKT/时区、哈希、交接双方及时间、访问权限，已变更或未及采集写入事件记录。
- **决策码** PRESERVE_BEFORE_OR_PARALLEL / CONTAIN_FIRST_WITH_EXCEPTION
- **检索与核验** 全包19份逐页检索 chain of custody、before change、forensic、evidence collection、preserve、tamper、log retention，核R02 pp32–33、R03 p18正本。

### Q02a · LC · 金管局首报

- **监管预期 Y** R05：显著事故一经知悉应立即通知金管局，提交当时可得资料，不等修复。R04 对显著网络事故用 promptly；R09 对电子银行相关事故指向金管局当时安排。把核心交易和薪资提交中断评为显著有事实依据，法例第653章的12小时并不适用于这条独立路径。收件渠道细节 U，首报责任、时点和内容仍为 Y；不可把信末咨询电话号码或专员热线当作已核实的金管局事故收件渠道。
- **原文定位** R05 p.2 ‘Reporting incident to the HKMA’（核过扫描图）; R04 TM-C-1 §2.4 p.4; R09 TM-E-1 §8.2.5 p.33
- **可接受行动** LC 立即经核实的金管局监管接触途径首报，并记录发出时间、内容和凭据。列08:00发现、已确认网关组件加密和受影响服务、仍可用渠道、临时处置及未知事项；失效转移和资料外泄在这张卡未核实。
- **决策码** HKMA-INITIAL-NOW
- **检索与核验** 19份冻结文本逐页查 HKMA/Monetary Authority 与 hotline/portal/reporting channel/telephone number/electronic filing/relevant arrangements；R09 p.33 只有转引；R05 p.2–3 图像核过。

### Q02b · LC · 专员首报

- **监管预期 Y** 指定 CI 营运者＋指定关键电脑系统＋已确认未获授权加密及核心功能中断。08:00 HKT 已达合理确定程度。尽快通知专员，最迟于16日20:00 HKT完成，不能等到上限。电话通知需事故性质、所涉关键电脑系统与简述，另有§28(3)补件。
- **原文定位** R01 Cap.653 §28(1)–(2), (7) PDF pp.43–45（4-30–4-34），附表6第1(a)项 PDF p.97（S6-2）；R02 §§7.3.2–7.3.6 pp.35–36、附录E p.42；R03 §1.1.3 p.3
- **可接受行动** LC 现在以卡上已核实的指定电话向专员首报，记录通话人、时点、内容和回执状态，待指定安全渠道可用即按指明表格补交；不把金管局报告算成专员首报。
- **决策码** OCCICS-PHONE-NOW
- **检索与核验** 正查 §28、附表6第1项、R02 awareness/telephone。

### Q03a · COM · 受影响客户服务通知

- **监管预期 Y** 重大事故应主动、有效通知已受或可能受影响客户，告知实际受影响服务、可采取的步骤，以及已有赔偿政策与申请方式。R05 的「as quickly as possible」修饰判断影响范围，未设客户通知的固定时限。C01 未明确中断的电子银行渠道，不预设 R09 已触发。渠道、具体发布时间和补偿立场仍待决定。
- **原文定位** R05 PDF 第1–2页 Customer notifications／Public announcement 中通知内容段（扫描已核）；若确认电子银行受阻，另见 R09 §8.2.2，PDF 第32–33页及脚注26。
- **可接受行动** 迅速由传讯向已知受影响的转账和薪资客户及合理可能受影响者发服务提示。区分可查余额、分行仍营业和受阻功能，提供安全有效的路线与下一次更新时间。赔偿待核可写暂未决定和查询方式，不能作无依据承诺。
- **决策码** PROACTIVE_DIRECT；影响范围尚在核实亦可先针对已知群体并设扩发触发条件。
- **检索与核验** R05 Customer notifications，R09 affected or likely；customer notification，most effective means，reimburse，service resumption。

### Q03b · COM · 公开服务公告

- **监管预期 Y** R05 对严重事故或已／可能影响大量客户规定了考虑公告的具体判断因素，发布决定须考虑速度、影响与调查因素。R09 较强的近期发布预期另需关键电子银行服务中断、可能影响大量客户且无合理把握短期恢复。审批人、个别渠道及时间无既定答案。
- **原文定位** R05 PDF 第2页 Public announcement (a)–(b) 及内容段、第3页 Handling of customers’ and media’s enquiry（扫描已核）；R09 §8.2.3、脚注25，PDF 第33页；R07 §4.7.2，PDF 第14页。
- **可接受行动** 说明基于 C01 已知核心支付中断及影响不确定性发布或暂缓的理由。建议采用银行可验证渠道，由授权发言人按本轮审批机制发布，含服务状态和客户步骤，记录发出。暂缓须写何时或什么事实变化复核。
- **决策码** PUBLISH_HOLDING／DEFER_REVIEW；符合 R09 三条件时使用新闻稿或同等有效通知尽早发布。
- **检索与核验** R05 public announcement；R09 critical e-banking service，near future；R07 speak to the media；approval approver。

## C02

### Q04a · SEC · 勒索样本验证

- **监管预期 N** 外泄调查应及时收集资料。实际个人资料及银行客户资料访问仍受保安和最小授权约束。但冻结原文未载截图真伪及是否与真实客户相符的验证方法，截图来源和所示身份未核实。
- **原文定位** 旁证 R11 p4 Step 1，R10 p169 附表1 DPP4(1)，R16b p4 附件C(i)
- **可接受行动** 09:30 HKT由SEC交授权取证员在隔离受控环境封存截图、登记哈希及取得路径，以最少字段与银行原始记录离线比对，留存置信程度和复核者。内部只发遮盖或聚合结果，匹配不等于证明来源或更大外传。
- **决策码** VALIDATE_RESTRICTED / VALIDATE_PENDING_DATA
- **检索与核验** 全包19份逐页检索 attacker-supplied、ransom sample、screenshot、validate、match、need-to-have、gather all relevant information、personal data，复阅R11 p4、R10 DPP4、R16b附件C。

### Q04b · SEC · 供应商证据协助

- **监管预期 U** 一般证据处置可据R02。SA-2的及时、准确在港取得外判资料仅在构成外判安排时适用，卡未提供安排或合同。R03明确引入的第三方通函及C-RAF细节不在包内，故供应商交付义务和专门处理无法裁定。银行可先发保全请求。
- **原文定位** R02 pp32–33 §7.2.3(a)(v)(2)、(h)，R03 pp16、18–19 §§6.2.18(a)、6.2.23、6.2.25(a)，R12 p8 §2.8.1
- **可接受行动** 09:30 HKT SEC安排供应商联络员向已核实联系人即刻书面保全远程会话、账号/验证、来源IP、管理变更及相关端点日志，标明起止时间、时区、来源、原始格式。通过验证过的加密受限渠道交取证库，校验哈希、登记保管交接，跟进完整性及证据缺口。
- **决策码** REQUEST_PRESERVE_SECURE_RECEIPT
- **检索与核验** 全包19份逐页检索 vendor、supplier、session logs、contract、outsourcing、cooperation、retrieve、custody、secure transfer，复阅R03 §§6.2.18/23/25和R12 §§2.5–2.8。

### Q05a · LC · 支付立场与闸门

- **监管预期 Y** 混合单元：付款立场 N，适用的法律闸门 Y（是否触发取决于事实）。§25 是知悉或有合理理由相信所处理财产为可公诉罪行收益；§25A(1) 涵盖已知或怀疑财产为收益、曾用于或拟用于有关罪行，按合理可行时间向授权人员披露；§25A(2) 是特定条件下不构成第25(1)条罪行的安排，不作一般付款许可。Cap.575 §7 要相应意图或知悉用途，§8 要知悉或罔顾收款人为恐怖分子或联系者，另留意许可限定；§12 的披露另看已知或怀疑为恐怖分子财产。卡上攻击者身份、资金归属和用途未核实，不能断言已触发或把暂缓写成一律法定禁付。依据要同时正确处理法律闸门及说明付款立场的判断依据。
- **原文定位** R16c Cap.455 §§25、25A(1)–(2) PDF pp.82–83（5-2–5-4）；R16d Cap.575 §§7、8 PDF pp.20–21（3-2–3-4）、§12(1) PDF p.36（4-2）
- **可接受行动** LC 向 CEO 建议暂缓或拒付，并在17日02:00 HKT前交待复核和升级计划。核实受款者、钱包、财产及用途、相关风险和授权，符合门槛时走适用披露路径。可接受其他有条件且在事实和现有法定门槛下可执行的立场，需指出什么证据会改变决定。
- **决策码** PAY-HOLD / PAY-DECLINE / PAY-CONDITIONAL
- **检索与核验** 19份冻结文本查 ransom/ransomware/extortion/blackmail/bitcoin/BTC/recorded commitment；R02、R04、R11、R14b、R16a 命中事故示例或分类，R16c p.101 命中黑函／勒索相关罪名，未找到直接规定付款立场的条文。Cap.537及制裁名单未在冻结包。

### Q05b · LC · 接触勒索者授权

- **监管预期 N** 谁决定和谁可实际接触勒索者，以及是否在09:30联络，均依专业判断。适用的独立披露保密约束可限制传递内容，不能替代接触授权规则。给可复检检索才支持 GAP；空口否定为 NC。
- **原文定位** 冻结资料中暂无直接授权条文；R02 §§7.3.3–7.3.4 pp.35–36 仅为事故与威胁示例；若已知或怀疑作出披露，另核 R16c §25A(5) PDF p.84（5-6）的可能妨害披露限制。
- **可接受行动** LC 建议现在不接触，或者仅经 CEO 书面批准、LC 审定并由指定响应人员或中介经受控渠道联系。交代复核触发、时限、禁承诺或泄露的信息范围，封存接触原话与授权。
- **决策码** CONTACT-HOLD / CONTACT-CONTROLLED
- **检索与核验** 19份逐页查 ransom、extort*、negotiat*、attacker、threat actor、intermediar*、contact/communicat* 邻近 suspect/attacker/criminal、authoris* 邻近 contact/negotiat*；命中主要为事故示例、测试和无关外包谈判，未定位接触授权。

### Q06a · COM · 前线话术及分发

- **监管预期 N** 一致及时沟通、指定转接和制定恢复状态沟通预案有官方指引。针对本卡前线话术、传播渠道、时点和审批的具体决定未见直接依据。R09 安全预防问询人员培训属另一个问题。
- **原文定位** 近似依据 R05 PDF 第3页 Handling of customers’ and media’s enquiry；R07 §4.7.2–4.7.3 PDF 第14页；R02 §7.2.3(a)(iv) PDF 第32页；R09 §4.3.1 PDF 第16页。
- **可接受行动** 给分行和客服一份当班即用统一口径。复述已知服务状况、采用可验证的查询渠道，转接赎金、资金异常及未证实外泄问题。保持与本轮 Q03b 已发布状态一致，登记更新与替换旧稿渠道。
- **决策码** INTERNAL_BRIEF_AND_ROUTE；同时记录发送对象、时间、版本和升级联系点。
- **检索与核验** 检索19份冻结文字版 front-line，talking point，script，staff guidance，branch staff，call centre，contact centre，internal communication，communication plan；复核 R02/R05/R07/R09 实质命中。

### Q06b · COM · 首次记者回应

- **监管预期 N** 仅有指定发言、避免妨碍调查和沟通记录规则。R02 表格要求列明有无回应，未设置记者截稿回应义务。未见直接规定对这记者必须或不得于 10:00 HKT 前回答、或者规定具体赎金话术。卡上及获发交接无付款状态；猜测已付款或未付款均不可采。
- **原文定位** 近似依据 R05 PDF 第2页 Public announcement 法律权衡及第3页查询处理；R07 §4.7.2 PDF 第14页；R09 §8.2.2 脚注25 PDF 第33页；R02 附件F E项 PDF 第46页；R16c §25A(5)、PDF 第84页（如实际发生相关披露）。
- **可接受行动** 可在截稿前由指定发言人回一条经批准的已证实服务状态或明确暂不置评；也可有理由暂缓并设授权、事实核实和回覆时间。对照发来的 Q03b，记录回应，适用时留稿副本供金管局。
- **决策码** REPLY_HOLDING／NO_COMMENT_REVIEW（按获发 Q03b 分支）。
- **检索与核验** 检索19份冻结版 reporter，press enquiry，journalist，spokesperson，speak to the media，before the deadline，ransom，prejudice，disclosure；回看 R02 附件F、R05/R07/R09 及 R16c/d 披露适用条件。

## C03

### Q07a · SEC · 外传范围核验

- **监管预期 N** 应调查影响范围及受影响身份，保留日志应足够供事后调查。冻结材料未规定外传范围核查方法、扩大范围的证据标准。工作区是否是指定系统未明，不能不加条件地把R03的指定系统要求用于整个工作区。
- **原文定位** 旁证 R16b p2 事故处理、p5 附件C(iv)，R11 p4 Step 1，R03 p18 §6.2.23(d)
- **可接受行动** 12:00 HKT由SEC与取证员对齐网关/身份/文件访问、出口及供应商日志，建立已证实80、其余至18,000待查的两层记录。仅在新增可证外传、可对应出口流量及完整内容或独立样本匹配等足以提高置信度时调整范围，报主持人并交LC/COM所需证据与不确定性摘要。
- **决策码** SCOPE_CONFIRMED_80 / EXPAND_ON_CORROBORATION
- **检索与核验** 全包19份逐页检索 exfiltrate、export、download、how many data subjects、identity of customers affected、egress、massive download、scope threshold，复阅R11 p4及R16b正文与附件。

### Q07b · SEC · 供应商凭证处置

- **监管预期 Y** 若供应商凭证为已或疑似泄露密码，R03直接要求及时更改。供应商维护只用密码单因素则每次使用后更改。令牌、活动会话和非密码凭证处置仍需判断，不能由该密码条款推出全部措施。
- **原文定位** R03 p14 §6.2.13(b)，R11 p5 Step 2，R02 p45 附件F D.1；R03 pp13–14 §§6.2.10(a)(i)、6.2.11(a)为未取得C-RAF细节的指引入口
- **可接受行动** 12:00 HKT SEC令身份管理人员先保全关联日志并阻断涉事远程通道、暂停有关账号。若是疑似泄露密码立即轮换，另独立终止活动会话并使相关令牌/密钥失效，验证原会话与令牌不能继续使用。与供应商确认设备、重新授权和受控接入的前置条件。
- **决策码** SUSPEND_ROTATE_AND_INVALIDATE / NONPASSWORD_INVALIDATE
- **检索与核验** 全包19份逐页检索 promptly changed、suppliers single authentication factor、revoke session/token、terminate session、access rights、remote access，核R03 p14正本。R08/R09令牌例示未规定本卡令牌失效操作。

### Q08a · LC · 私隐专员通知

- **监管预期 Y** 公署表格说明该条例不强制作资料外泄通知；金管局要求认可机构认真考虑并说明不报理由；公署指引建议知悉后切实可行尽快，即使调查仍继续。受影响的80人姓名、身份证及电话得到证实，足以说明实际损害风险。公署接受书面表格的线上、传真、亲身或邮寄方式，口头不收；不要写成另一条法定事故通报或固定小时限期。
- **原文定位** R16a PCPD 通报表 p.1 引言；R16b HKMA 2014 通函 p.3（PDF）；R11 Step 4 p.6、When/How to notify p.8
- **可接受行动** LC 现在经认可的书面渠道向 PCPD 提交已知事实、已知受影响范围及控制措施，区分80人已证实与18,000人未证实，后续调查补全。记录已发、拟报或回执未核实，不把建议当作已发。若决定有条件暂不报，需具体理由和复核触发，可由组员按事实判断。
- **决策码** PCPD-NOTIFY-PROMPTLY / PCPD-DEFER-WITH-REVIEW
- **检索与核验** 正查 R16a statutory status、R16b seriously consider、R11 When/How to notify。

### Q08b · LC · 个人资料外泄通知范围

- **监管预期 Y** 严重私隐事件下从速通知受影响客户的监管期望，及 PCPD 实际损害风险建议为 Y。具体队列阈值、谁算新增受影响者和分批触发为判断，法规未设固定人数门槛。身份证与电话等敏感信息和已证实外泄支持覆盖80名；18,000名只是未证实上限。
- **原文定位** R16b HKMA 2014 通函 PDF pp.2–3；R11 Step 4 p.6；R05 Customer notifications PDF p.1
- **可接受行动** LC 现在向 CEO/COM 提议先覆盖80名已证实受影响客户，明确直接通知时点与新增范围触发，例如可核实日志或文件证明外泄，或证据已足以把明确对象列为很可能受影响。保留范围复核和交接，不把更晚卡的320名带入。
- **决策码** COHORT-80-EXPAND-ON-EVIDENCE / COHORT-EVIDENCED-BROADER
- **检索与核验** 正查 R16b serious/sensitive/affected customers、R11 real risk of harm、R05 affected or likely to be affected。

### Q09a · COM · 首批通知内容与渠道

- **监管预期 Y** 已证实敏感身份资料外泄，严重私隐事故下应尽快告知受影响客户；不通知须有理由。R11 直接提供风险告知、个人防护、联络点等建议内容和可选直接渠道。CEO 尚未裁定 Q08b 的获准对象，具体对象、渠道组合和发布时间属附条件判断。
- **原文定位** R16b PDF 第2–3页 Controls for handling incidents involving loss or leakage of customer data；R11 PDF 第6页 Step 4、第7页 What should be included、第8页 When/How to notify。
- **可接受行动** 据目前已知的80人拟建议尽快按批准名单分发。写确认事实、资料类别、目前不确定范围、已采取措施和客户自保及安全求助方法。用经验证的直达渠道，不在提示本身多曝个人资料。暂缓则限定批次、实际障碍和解决触发条件。
- **决策码** DIRECT_SEND_IF_APPROVED／HOLD_FOR_VERIFICATION；如 CEO 采纳原答预设条件分支且决定字段不变，按确认，不能把同卡待裁决当已批准。
- **检索与核验** R11 what should be included，data subjects can be notified directly；R16b notify the affected customers，as soon as practicable；hold，approval。

### Q09b · COM · 公开外泄表述

- **监管预期 N** 上述材料规定考虑公告及已发公告的内容原则，未规定如何公开复述未验证攻击者声称、必须报出 18,000 或对未公开传闻加以发布。本卡80名已验证、18,000为同一工作区可能范围且外传未证实，是否已有公开指称亦未知。
- **原文定位** 近似依据 R05 PDF 第2页 Public announcement (b)、关键事实及法律权衡；R16b PDF 第3页严重事故通告；R11 PDF 第7–8页通知内容和 When/How to notify；电子银行适用时另见 R09 §8.2.2–8.2.3。
- **可接受行动** 若选择公开声明，只将核实事实作为既定事实，明确仍在调查更大范围；可出于透明度和必要性选择披露带清楚限定的上限，也可不复述估数。给消费者防骗行动和官方咨询渠道，不复述敏感标识。赞成暂缓需说明复核条件。
- **决策码** PUB_VERIFIED_ONLY／PUB_QUALIFIED_SCOPE／DEFER_PUBLIC_REVIEW。
- **检索与核验** 检索19份冻结版 unverified，not confirmed，unconfirmed，public announcement，large number of customers，key facts，as much information as possible，prejudice；回查 R05/R09/R11/R16b 命中。

## C04

### Q10a · SEC · 临时处理优先级

- **监管预期 N** BIA时限用于服务恢复优先、BCP应组织备用处理。附件为观察到的良好做法。冻结原文未载是否启动该备用流程、4,200笔指令的队列顺序或负责人。授权和备用流程可用性须作为条件。重大变更报告另属Q23a。
- **原文定位** 旁证 R07 p8 §3.2.2、p11 §4.3.2，R02 p34 §7.2.4(b)，R14b pp1–2 A.1
- **可接受行动** 18:00 HKT SEC提出在营运及授权负责人批准、核验/防重和对账控制可用时启动，限最多400笔经验证指令每小时。先排时敏且待验证通过的SME工资/其他临近截止交易，以一致规则在同级排序，待确认、不合格和疑似重复留在隔离队列，交营运与主持人记录。无法满足条件时继续等待并报明影响。
- **决策码** ACTIVATE_SECONDARY_CONDITIONAL / HOLD_SECONDARY
- **检索与核验** 全包19份逐页检索 secondary、alternate processing、bypass、recovery priority、payroll、queue、time-critical、approval、service level，复阅R07 pp8、11和R14b pp1–2。

### Q10b · SEC · 重试及重复入账控制

- **监管预期 N** 电子银行资料完整及更新后对账要求只提供控制方向。R14b以自动重试防重为案例。冻结原文未规定本案待处理重试指令的识别字段、核销渠道或超时挂起条件。
- **原文定位** 旁证 R09 p19 §5.1.2，R14b p1 A.1 Auto-switching capabilities，R07 p11 §4.3.2
- **可接受行动** 18:00 HKT备用处理前由支付营运按原指令ID/幂等键核对队列、总账及结算状态。无匹配键时比对付款方、收款方、金额和时间，并由第二人复核。未确认原交易是否入账的重试暂缓，仅放行证实未处理且符合资格的唯一指令，批后对账并报差异。
- **决策码** DEDUPE_BEFORE_RELEASE / HOLD_AMBIGUOUS
- **检索与核验** 全包19份逐页检索 duplication、retry、re-attempt、timeout、idempotency、reconcile、record reconstruction、double entry，核R09 p19、R14b p1、R07 p11。

### Q11a · LC · 专员通知状态核验与处置

- **监管预期 Y** 用本轮记录分支：无有效首报现在立即按指定渠道提交（16日18:00，尚未到20:00上限）；有效电话或其他非指定首报，实际通知时刻 T+48小时补指明表格；首次已按指定方式完成，不触发§28(3)；若指定表格已补交，记实际提交时间和是否按时。记录缺失或回执未核实应追查，不把回执缺失一律当作未发。
- **原文定位** R01 §28(1)–(3) PDF pp.43–44（4-30–4-32），附表6第1(a)、第2项 PDF p.97（S6-2）；R02 §7.3.6 p.36、附录E p.42
- **可接受行动** LC 现在核对首报对象、实际时间、事故性质/系统/简述和记录；安全渠道已恢复，按分支马上首报、补交或核对已交凭据。向专员办理，记明到时和回执。
- **决策码** OCCICS-INITIAL-NOW / FORM-SEND / FORM-SATISFIED / NO-FORM-TRIGGER / VERIFY-DISPATCH
- **检索与核验** 正查 §28(2)(b)(ii)/(3)、附表6第2项、R02 form/48 hours/secured channel。

### Q11b · LC · 金管局跟进

- **监管预期 Y** 看本轮 Q02a 记录。无有效HKMA首报须立即补首报；已报则及时更新已证实外泄、排队和服务影响，公开沟通材料确已形成则送副本。启动 BCP 才触发 R07 从速通知并定期报告，批准备用流程不自动等于 BCP 已启动。LC没收到COM的发布记录，因此公关材料和启动状态待核时用分支，不臆造已发布或已启动。
- **原文定位** R05 PDF pp.2–3（核过扫描图）；R16b HKMA 2014 通函 p.3；R07 TM-G-2 §1.3.3 p.5；R09 TM-E-1 §8.2.5 p.33
- **可接受行动** LC 向金管局现在报已知重大服务和资料影响并登记时点。向运营／传讯索取可披露的 BCP 与公开文案记录；按相应条件送定期进展和副本。
- **决策码** HKMA-INITIAL-NOW / HKMA-UPDATE-NOW + BCP-ACTIVE / BCP-VERIFY
- **检索与核验** 检索同 Q02a 的19份HKMA渠道索引；另查 R07 BCP activated/periodic progress、R05 kept informed/copies。

### Q12a · COM · 公开服务更新

- **监管预期 Y/N/U（依分支）** Y：未发过公告且已核实关键电子银行中断、可能影响大量客户及短期恢复无合理把握，R09 对首发有直接期待；此时已到 H+10，不将时点回溯为准时。N：已有公告后要不要更新、以何频次/方式发布这一具体决定只有及时一致原则；非电子银行时亦不得套用 R09。U：发布状态或适用触发无法据交接判断，按可证条件作答。同一规则所需的公告内容不依赖这个分类。
- **原文定位** R09 §8.2.3 PDF 第33页；R05 PDF 第2页 Public announcement、第3页 Handling of customers’ and media’s enquiry（扫描已核）；R09 §8.2.2 脚注26 PDF 第33页。
- **可接受行动** 据 Q03b 实际发出状态分别补发、更新或暂缓。写已知中断、客服过载和可行渠道；短期恢复时间与次要流程尚未核准时保留条件，不宣称已恢复。按目前获发记录判断，不能假定 Q06b/Q09b 表态已传达。设下次更新时间和批准路由。
- **决策码** FIRST_NOTICE／UPDATE_ISSUED／DEFER_VERIFICATION；每条保留 Q03b 已发、未发或未证分支。
- **检索与核验** R09 shortly after，critical e-banking，R05 up-to-date messages；检索19份冻结版 frequency，interval，periodic updates，press release，update，resumption time；回看 R05/R06/R07/R09。

### Q12b · COM · 受阻客户协助渠道

- **监管预期 Y** 重大事故导致大量查询时迅速部署足够资源和沟通渠道；CI运营者应保证多个可用沟通渠道。服务热线、延长分行服务是可选例子。客户无法联系或到达分行的具体原因与替代渠道容量未核，不预设其中一种。
- **原文定位** R05 PDF 第3页 Handling of customers’ and media’s enquiry 及第2页重获服务步骤（已核扫描）；R02 §7.2.3(e)，PDF 第33页；电子银行适用时 R09 §8.2.2 脚注24 PDF 第32页。
- **可接受行动** 现在加开回拨或热线及验证通过的发布渠道，给受阻客户明确获取服务的步骤，优先安排急迫薪资客户，列明客服负责人和可复核的容量/排队监测点。分行安排要与实际可达性相匹配。
- **决策码** ALT_CHANNEL_SUPPORT；记录主渠道／备用渠道及启动时点。
- **检索与核验** R05 deploy swiftly，extended office hours，customer service hotlines；R02 ensure multiple channels；R09 footnote 24。

## C05

### Q13a · SEC · 干净恢复候选与验证

- **监管预期 U** R03有安全第三备份和限定条件下物理断开备用副本的基线，R08要求验收测试与生产分开。不可把二者当作选择这份快照或证明洁净的具体验证规程。包内无完整验证步骤，R03(a)(i)直接引C-RAF 5.1.2/5.2.3且(b)(i)引银行公会STDB指引，两项均无对应原文，具体恢复控制覆盖待定。
- **原文定位** R03 pp16–17 §6.2.20(a)–(b)，R07 p13 §4.6.2，R04 p8 §4.3，R08 p18 §4.2.4（R03 p15 §6.2.16(a)引入，适用于验收测试）
- **可接受行动** 17日08:00 HKT SEC令恢复工程和取证人员先在隔离实验环境测试已知事前不可变副本，验证时间早于合理最早入侵、来源及哈希、恶意指标和恢复完整性。验证网络/身份/管理平面分离、采用新凭证，通过后仅作为进一步候选，测试失败则保留失败证据、重建或另行择候选。
- **决策码** TEST_IMMUTABLE_ISOLATED / HOLD_OR_SWITCH_CANDIDATE
- **检索与核验** 全包19份逐页检索 immutable、STDB、physically disconnected、restore critical data、backup integrity、malware scan、separated environment，核R03 pp16–17和R04 p8，单列不可回查交叉引用。

### Q13b · SEC · 交易对账方法

- **监管预期 N** 电子银行交易更新后对账、测试数据控制及必要时去敏和批准是已有约束。冻结材料未指定本案离线比对的账目、抽样、差错容忍或生产资格，对照基线也未交给C05角色。
- **原文定位** 旁证 R09 p19 §5.1.2，R03 p17 §6.2.22(c)，R08 p18 §4.2.4，R07 p11 §4.3.2
- **可接受行动** 17日08:00 HKT SEC和支付营运设立去敏且经批准的离线基准，逐笔比对原指令/恢复后的队列、分类账和独立结算记录，核金额、状态、顺序、重复、缺单并复核汇总。设可解释差异的明确处理门槛、保留未解释差异即暂停的条件，交独立复核和主持人记录。
- **决策码** OFFLINE_RECONCILE_ZERO_UNRESOLVED / HOLD_UNAVAILABLE_BASELINE
- **检索与核验** 全包19份逐页检索 reconcile、offline、sample、balance、record reconstruction、acceptance、zero mismatches、production data，复阅R09 p19、R03 p17、R08 p18。

### Q14a · LC · 重新决定勒索支付立场

- **监管预期 Y** 混合单元：现行立场和既有承诺的处置 N，法律闸门 Y（是否触发取决于本轮事实）。沿用 Q05a 的财产、知悉／怀疑、恐资和受款核查条件。到 C05 期限已过，320人资料公开并不自身证明攻击者身份、确立付款义务或改变任何许可。看 Q05a/b 的真实授权、接触和模拟承诺；不要把建议或已写草案当成承诺。
- **原文定位** R16c Cap.455 §§25、25A(1)–(2) PDF pp.82–83（5-2–5-4）；R16d Cap.575 §§7、8 PDF pp.20–21（3-2–3-4）、§12(1) PDF p.36（4-2）
- **可接受行动** LC 在 C05 根据实有记录向 CEO 说明维持、暂停或调整的理由，通常暂停继续联系或支付并核实承诺内容、授权和潜在法律影响；明确新评估的负责人和时点。条件满足时依法披露，保留接触证据和复核记录。
- **决策码** REASSESS-MAINTAIN / REASSESS-SUSPEND / REASSESS-CHANGE + COMMITMENT-NONE / COMMITMENT-LEGAL-REVIEW
- **检索与核验** 同 Q05a 的19份；额外重点核对 recorded commitment / extort* / blackmail，未定位对已作承诺的具体处置规则。

### Q14b · LC · 向执法机关转介

- **监管预期 Y** 核对该已知假验证网页是否足以使公众误以为来自银行；若符合，适用 R09 针对欺诈网站／类似骗局的警方报告期望；勒索事件整体另按 R04 where appropriate 分析，不能写成无条件法定报案。§58(2) 仅在为§58(1)目的使用资料且适用第3原则可能妨害该目的时提供豁免，不产生披露义务。具体报送证据及范围依事实判断；LC没有 SEC 的保全结果。
- **原文定位** R09 TM-E-1 §4.3.2 pp.16–17；R04 TM-C-1 §2.4及注1 p.4；R10 Cap.486 §58(1)–(2) PDF pp.118–119（8-14–8-16）、附表1第3原则 PDF pp.168–169（S1-8–S1-10）；R11 p.4
- **可接受行动** LC 现在安排向香港警务处报告骗局，并基于已确认入侵、勒索和泄漏评估同步转介网络罪行。先交卡上可核实的URL、时间、截图、勒索要求及已知事件摘要，原件保全，客户级资料必要性和合法条件核清后经确认安全渠道按需提交。
- **决策码** POLICE-SCAM-NOW + EXTORTION-REFER / EXTORTION-REVIEW
- **检索与核验** 正查 fake/fraudulent websites、relevant authorities、crime prevention/detection、prejudice、DPP3。

### Q15a · COM · 新增确认客户通知

- **监管预期 Y** 已证实敏感资料且发现公开镜像。应在知悉后切实可行的情况下尽快通知受影响客户，不待较大范围调查明确。可选择电话、书面、电子邮件或面谈，多方法为合理选项。优先批次和去重属执行判断，需要获发 Q08b/Q09a 实际记录。
- **原文定位** R16b PDF 第2–3页 Controls for handling incidents involving loss or leakage of customer data；R11 PDF 第6页 Step 4、第7页通知内容、第8页 When/How to notify。
- **可接受行动** 320名包括初始80名，新核实的240名尽快直达核验。初始80名据发出记录补漏，已成功收到者只在公开镜像或风险变化需要时跟进。采用有身份验证的联系渠道，登记批次、发出时间和失败重试。
- **决策码** NOTIFY_NEW_AND_RECONCILE_PRIOR；前批次已发／未发／状态待核分别处理。
- **检索与核验** R16b as soon as practicable；R11 regardless of the progress，directly by phone，multiple methods；duplicate／de-duplication 属执行。

### Q15b · COM · 防骗公告

- **监管预期 Y/U（依触发）** Y：骗局可能使公众误认出自本行，或出现条文所述短期内影响多名客户的可疑网银登入画面，R09 要及时考虑告知并报警方，客户利益支持时尽快经新闻稿或同等有效方式告知并向HKMA报送。U：目前只知假验证页，未说明冒充途径或符合该复合触发；不能把R09更强机制写为已触发。避免为假页面引流的具体写法属于专业判断。
- **原文定位** R09 §4.3.2，PDF 第16–17页及脚注12；R11 PDF 第7页通知内容建议（防钓鱼）；R05 PDF 第2–3页公告内容和记录。
- **可接受行动** 及早在官方站点／App／核实客户渠道预警，说明勿点击或提交资料，并给官方验证和举报入口。不要发布可点击假链接、二维码或会主动引流的标识。核验是否冒充，通知授权监管联络人员及时处理警方、下架与向金管局通报，记发出时间。
- **决策码** WARN_OFFICIAL_NO_LINK；MARK_TRIGGER_VERIFIED／PENDING。
- **检索与核验** R09 false impression，suspicious Internet banking login screens，best interests，similarly effective means，footnote 12；R11 phishing。

## C06

### Q16a · SEC · 生产分阶段恢复决定

- **监管预期 Y** 正式验收仅把经妥善测试与批准的系统转入生产，适用的紧急变更要由信息负责人和相关方批准；确急且事前无法取得信息负责人批准时须尽快追认。原文未定容忍值及哪位负责人。118/120和短时离线未复发不能自行满足验收，实际前情须按当轮交接核。
- **原文定位** R03 p15 §6.2.16(a)引R08 p18 §4.2.4、pp19–20 §§4.3.1–4.3.3
- **可接受行动** 17日20:00 HKT SEC对涉及未解释差异的生产路径建议暂停。只有与该路径隔离、经过独立测试且符合变更控制的狭窄模式可报批，明确营运与信息负责人、变更授权人和CEO模拟决定，并保留测试、批准、停止及复核记录。后续依据差异解释和清洁环境重测再评估分阶段上线。
- **决策码** HOLD_UNRESOLVED_BREAKS / LIMITED_SAFE_MODE_APPROVED / STAGED_IF_GATE_MET
- **检索与核验** 全包19份逐页检索 formal acceptance、properly tested and approved、emergency changes、information owner、release gate、staged deployment，核R03 p15、R08 pp18–20原件。

### Q16b · SEC · 暂停回退闸门

- **监管预期 N** 生产发布出现问题须有回退流程，紧急变更须留日志与备份。R09附件面向计划维护或演练。冻结原文未规定这场事故的可量停止条件、回退目标及授权分工，已受陷网关不能假定为安全目标。
- **原文定位** 旁证 R03 p15 §6.2.16(a)引R08 p19 §4.3.1第5点、p20 §4.3.3，R09 p40 附件B.2
- **可接受行动** 17日20:00 HKT即在任何批准上线前由SEC与变更负责人明确：新增未解对账差异、重复扣账、恶意指标/漏监控、关键指标越限时立刻暂停并通知指挥。由获授权变更负责人回退至最后验证安全状态或关闭该生产路径，留存证据和受影响交易并重新核账。未授权生产时，记录仅为预置门槛。
- **决策码** ROLLBACK_ON_DEFINED_TRIGGER / CONTINGENCY_ONLY
- **检索与核验** 全包19份逐页检索 rollback、rolling-back、fall-back、stop threshold、abort、production release problems、re-instate、emergency changes，核R08 pp19–20与R09 p40。

### Q17a · LC · 受控取证数据共享

- **监管预期 Y** 如本地取证公司受托代表银行处理个人资料，应以契约或其他方式防止擅自或意外存取、处理等，并限制保留期；另核目的相容或确切例外。若适用外包范围，R12 对授权人员按需访问、保密和分隔有具体控制。原件或缩小数据集的选择是事实和专业判断，不机械把外包范围或最小集选择当法定结论。
- **原文定位** R10 附表1第4(1)–(2)原则 PDF pp.169–170（S1-10–S1-12），第2(3)原则 PDF p.167（S1-6），第3原则 PDF pp.168–169（S1-8–S1-10）；R12 SA-2 §2.5.2 p.6；R16b HKMA 2014 通函附件 I PDF p.8
- **可接受行动** LC 与 SEC 在释放前确定最小可完成任务的范围、保密和必要访问、限期、禁再分发、加密交付和审计、返还销毁与书面确认。通常先给较小/脱敏集合；只有证明确需全像并通过法律和控制审核才升级。明确收件方和交付完成时点。
- **决策码** FORENSICS-LIMITED / FORENSICS-FULL-CONDITIONAL / FORENSICS-HOLD
- **检索与核验** 正查 R10 data processor、access、longer than necessary；R12 outsourcing/need basis；R16b other controls over service providers。

### Q17b · LC · 董事会升级

- **监管预期 N** 现行资料支持高级管理层定时及时向董事会报告，尤其在重大缺陷可能影响关键业务时，及董事会的持续监督职责。对本事故具体要升级哪些事项、临时决策审批、时限和渠道，未定位直接规则。LC 没得到 Q16 的正式恢复裁决，不假定已上线。用引文明确治理旁证，以判断处理具体升级。
- **原文定位** 旁证：R06 OR-2 §§3.2–3.4 pp.5–6；R07 TM-G-2 §2.1.1 p.5；参见 R08 p.8、R14b p.6 的治理/风险报告语境。
- **可接受行动** LC 现在经高级管理层向董事会或其已核实委托渠道报告持续核心服务中断、SME薪资、118/120与两笔未解释不符、风险和决策请求，说明实际恢复状态待证实，并约定定期及触发更新。
- **决策码** BOARD-URGENT-BRIEF / BOARD-DECISION-ESCALATION
- **检索与核验** 19份逐页查 board 与 report/notif/escalat/approval 邻近、significant deficienc*、crisis management team、disruption tolerance；回读 R06 pp.5–6、R07 pp.5–6、R08 p.8、R09 p.11 和 R14b p.6，未找到本事故具体事项和时限。

### Q18a · COM · 客户恢复状态更新

- **监管预期 Y** 向已受或可能受影响客户主动提示事故关键事实与获得/恢复服务、降低损失的步骤，既定赔偿/申领流程可列。R09 举例预计恢复时间可在有根据时提供。离线实验室结果不代表获准生产。C06 COM 作答时没有 Q16a 同卡最终决定。
- **原文定位** R05 PDF 第1页 Customer notifications、第2页 Public announcement（已核扫描）；如电子银行适用，R09 §8.2.2，PDF 第32–33页及脚注26。
- **可接受行动** 以等候批准、限制服务、已授权分阶段恢复分别写短消息；只在对应批准且实际状态可验证时发布，清楚区分已知故障、允许操作、仍受限与下次更新，不把118/120称为全通过，不自行设赔付或恢复承诺。
- **决策码** UPDATE_HOLD／UPDATE_LIMITED／UPDATE_STAGED；CEO按已明确原答分支选定且决定字段不变时可记确认。
- **检索与核验** R05 steps or precautionary measures，reimburse，gain or regain access；R09 key facts，estimated service resumption time。

### Q18b · COM · 受影响银行及对手方通知

- **监管预期 Y/N/U（依对象）** Y：首轮告知对象确属其他受影响认可机构且有需要，应在切实可行情况下尽快通知，便其告知自身客户。N：个别清算状态内容、对非认可机构或定期频次/渠道只有计划原则；U：卡上未确认两家对手方是否认可机构，故企业类别及适用条件须核实。合规转报和具体消息渠道不是规则原文已定。
- **原文定位** R05 PDF 第1–2页 Customer notifications 跨页段（已核扫描）；R07 §4.7.1–4.7.2，PDF 第13–14页；R06 §8.3，PDF 第13页。
- **可接受行动** 立即用已验证对手运营联系人，双边提供未结算状态、暂停重复提交/待核查操作建议、反馈点及下次更新。若为有需要的受影响认可机构，明确及时首报并留痕；若身份待核仍可在获授权下用范围受控的运营沟通，不向未验证接收者发送敏感明细。
- **决策码** COUNTERPARTY_NOTICE_AI／OPERATIONAL_NOTICE_NONAI／VERIFY_RECIPIENT；按 Q16a 决定条件化，记录对象类别和是否为首次消息。
- **检索与核验** R05 other affected AIs，where necessary；R07 counterparties，properly logged；对内容、节奏检索19份冻结版 settlement，unsettled，counterparty update，update schedule，communication channel 并回查 R05/R06/R07。

## C07

### Q19a · SEC · 可审查的技术时间线

- **监管预期 N** 应急计划须安排记录事故过程，报告要求最早可识别和知悉两类时间，日志须支持调查。R02类别2日常同步条款应与银行行业守则范围区分，且该条款未定事后校时法。冻结原文未载本案时钟偏移与不确定性的记录/归一方式。
- **原文定位** 旁证 R02 p32 §7.2.3(a)(v)(4)、p44 附件F B.5–6、p20 §6.2.23(g)，R03 p18 §6.2.23(a)、(d)
- **可接受行动** 18日12:00 HKT SEC指派取证员保留每源原时间、时区、哈希及出处，使用可验证参考时间点建立系统偏移表，转换为HKT并注明估计区间、最多4分钟偏差及时间顺序不能确定的事件。对身份、网关、供应商日志交叉核验，复核后供事件指挥/LC报告，保留修改记录。
- **决策码** TIMELINE_CORRELATED_WITH_UNCERTAINTY
- **检索与核验** 全包19份逐页检索 timeline、chronology、clock offset、primary time source、synchronise、timestamp、earliest identifiable time、uncertainty，核R02 pp20/32/44和R03 p18。

### Q19b · SEC · 监测强度决定

- **监管预期 N** 行业守则要求监测、分析并采取适当措施，详细控制指向不可回查的C-RAF。R02提及时移除或隔离针对事故判定，不能作为减少监测的阈值。冻结原文未设本案提高/维持/降低级别的具体门槛。
- **原文定位** 旁证 R03 p19 §6.2.26(a)–(b)，R08 p15 §3.4.1，R02 p35 §7.3.2
- **可接受行动** 18日12:00 HKT由SEC/SOC保留隔离，针对新指标扩大定向检索并核与原攻击的关系，先检查本轮已执行的恢复和回退条件。无生产扩散证据也不能视为已经证实无关。建立复核时点与可验证降级标准，若发现蔓延/影响按已定闸门收紧并告指挥、LC。
- **决策码** RETAIN_ENHANCE_TARGETED / ESCALATE_ON_CORROBORATION
- **检索与核验** 全包19份逐页检索 monitor、threat intelligence、indicator of compromise、quarantined、heighten、step-down、containment、suspend，核R03 p19和R02 p35，备注C-RAF未提供。

### Q20a · LC · 指定表格补报

- **监管预期 Y** 根据实际发出记录分支。首次指定表格：未触发附报；非指定形式通知：时钟为实际通知 T+48小时。补表记录可判已满足、已交但迟或待核；未交要据 C07 18日12:00 HKT 判断未到期或逾期。初报如早于16日12:00且未补表则已迟；恰在时点则即到期。18日20:00仅为及时初报（最迟16日20:00）的最晚补表时刻，实际晚报仍从其T起算48小时且初报迟另记。没有有效初报不可凭空起算补表。
- **原文定位** R01 §28(1)–(3)、(5) PDF pp.43–44（4-30–4-32），附表6第1(a)、第2项 PDF p.97（S6-2）；R02 §7.3.6 p.36及附录E p.42
- **可接受行动** LC 现在核对对象、时间、首报形式、有效提交记录和回执。如无有效初报立即联系专员完成；需要补表即经指定安全渠道提交附录E或适用行业表，并标注按时与否、保留证据和补救记录。未触发或已满足则说明依据并追踪待核回执。
- **决策码** NO-FORM-TRIGGER / FORM-SATISFIED / FORM-FILED-LATE / FORM-PENDING / FORM-LATE / OCCICS-INITIAL-NOW / VERIFY-DISPATCH
- **检索与核验** 正查 §28(3)、附表6第2项、R02 §7.3.6(b)；核对首报与补表计时不同。

### Q20b · LC · 独立书面事故报告

- **v2 题面** “b. For the same statutory incident-reporting process as in Q20a, decide how to prepare, assign and submit the separate written incident report. State who is responsible, to whom it is submitted, what is submitted and by when.” 收件方不在题面上；角色有没有从原文找出收件方是判分点（主笔 2026-11-18 香港时间决定）。
- **监管预期 Y** 在初次按指定方式通知或已补交指定书面记录后，另向专员按指定方式提交书面事故报告。14日从16日知悉的日期算，到2026-11-30。不得从首次通知或补表算，也不另造08:00等未载明截止时刻。若首报步骤缺失，立刻补正，同时保持报告倒计时。额外资料后续补，真实状态未核实可写未知。
- **原文定位** R01 §28(4)–(5) PDF p.44（4-32），附表6第3项 PDF p.97（S6-2）；R02 §7.3.7 p.37、附录F pp.43–46
- **可接受行动** LC 负责报告和指定安全渠道提交；安排 SEC 提供时间轴、影响、根因与控制措施，业务方确认影响、责任人复核报送。使用附录F或适用行业表，将草拟、复核与提交安排在不迟于11月30日并留存凭据。
- **决策码** WRITTEN-REPORT-PLAN-NOV30 / WRITTEN-REPORT-SUPPLEMENT
- **检索与核验** 正查 §28(4)、附表6项3、Annex F、supplementary material；区分 R02 附录E和F。

### Q21a · COM · 客户补救个案接力

- **监管预期 U** 31宗只为疑似诈骗，未明确未经授权的电子银行交易、实际损失、个人/企业客户、赔偿授权或与外泄人群关系。可能的未经授权电子银行交易有随时求助渠道，检测到欺诈/可疑活动的暂停机制有直接指引。个人客户未经授权直接损失及诈骗/严重疏忽例外等详见R09 §4.4.4，其所指《银行营运守则》未装包；企业客户条款另核。不能据此做统一赔付判断。
- **原文定位** R09 §§4.4.2–4.4.4，PDF 第17–18页，及 §4.3.2，PDF 第16–17页；R05 PDF 第1页 Customer notifications；R11 PDF 第4–5页步骤2、第7页通知内容。
- **可接受行动** 用官方反诈和客户服务入口建案，按凭证可能被盗、账户活动及即时损失程度分流，必要时协助暂停、记录与转介。能承诺受理、追踪、下次联系和经批准的支持；赔偿和责任逐案复核，限制涉及身份或账户明细的沟通。
- **决策码** SCAM_TRIAGE；如证实可能有未经授权电子银行交易，走 E_BANKING_URGENT；赔付保留 PENDING_DECISION。
- **检索与核验** 检索19份冻结版 suspected scam，dedicated hotline，suspend，unauthorized transactions，reimburse，compensation，gross negligence，business customers，police；核对 R09/R05/R11/R16a 决策条件，查源清单确认所引《银行营运守则》不在19份内。

### Q21b · COM · 修正客户通知名单

- **监管预期 Y** 已有合理理由相信12条旧联系方式不准确，须采取所有切实可行步骤确保不再按原用途使用，直至该理由消失或资料被删除；去重、逐人触达方式及具体更正复核流程无直接规定。是否曾错误发出另查真实记录，不能凭批次名单推断。
- **原文定位** R10 Cap.486 附表1 DPP 2(1)(b)(i)–(ii)，PDF 第166–167页；R11 PDF 第4–5页步骤2；R16a PDF 第5页 Email or Postal Leakage；R09 §4.2.3 PDF 第16页仅电子银行交易通知类比。
- **可接受行动** 锁定旧联系人、核验同步新信息，按客户ID合并原批次和新派发记录。仅给需跟进、误送待补或材料内容有更新的客户安全触达。疑似已误送升级 LC 评估并记载，不要求未证实的误送对象自行找回。
- **决策码** RECTIFY_AND_DEDUPE；VERIFIED_MISDIRECTED／NO_EVIDENCE／CHECK_DISPATCH 分支。
- **检索与核验** DPP inaccurate，those grounds cease，rectification，R11 unintended recipients，R16a Email or Postal Leakage；R09 notifications that cannot be delivered 的范围。

## C08

### Q22a · SEC · 运行或持续限制的交接

- **监管预期 N** BCP应安排验证常设地点安全及就绪，恢复正常后检阅，报告填写当前状态和后续。冻结原文未规定本案按何门槛释放何项服务或限制，也未列常态营运的具体交接字段。测试是离线，生产状态及是否满足现行门槛须查本轮交接。
- **原文定位** 旁证 R07 p11 §4.3.3、p18 §6.2.1，R02 p33 §7.2.3(i)、pp45–46 附件F D.2–4
- **可接受行动** 19日08:00 HKT SEC与常态营运核本轮Q16/Q19纪录和实测生产状态，保留未经证明安全的服务限制、供应商隔离及监控，只解除已有独立生产证据且批准的限制。交接已执行/待决动作、现行闸门、回退测试、监控规则、开放指标、责任人与复核时限。
- **决策码** KEEP_RESTRICTIONS / RELEASE_VERIFIED_ONLY / HOLD_PENDING_STATUS
- **检索与核验** 全包19份逐页检索 handover、hand-off、standing operations、normal operations restored、verification of safety and readiness、release restrictions、step down、post-incident review，核R07 pp11/18与R02附件F。

### Q22b · SEC · 根因修复与关闭证据

- **监管预期 N** 须有根因分析和风险为本的整改优先方法，权限应复核和留档。R03有疑似泄露密码及时变更的条件，但未给结案验收条件。冻结原文未规定当前根因整改岗位、具体日期与供应商非密码凭证关闭证据组合，根因尚未证实，部分供应链控制另指不可回查的C-RAF及第三方通函。
- **原文定位** 旁证 R06 p13 §8.3第4点，R13 p3 风险为本整改段，R03 p13 §6.2.10(b)(ii)、p14 §6.2.13(b)、p19 §6.2.25，R02 pp43–46 附件F B.4、D.3–4
- **可接受行动** 19日08:00 HKT SEC把根因调查分给取证负责人，凭证和远程接入整改分给IAM/供应商接口人，定首次复核期限和独立确认者。关闭前核原凭证/会话/令牌无法使用、新通道批准与限权、日志监测无复用证据、供应商书面核证及测试记录。找不到当轮Q07b状态时先回查事故记录并维持开放。
- **决策码** ASSIGN_TRACK_KEEP_OPEN / CLOSE_ON_ATTESTED_EVIDENCE
- **检索与核验** 全包19份逐页检索 root cause、remediation、closure criteria、vendor credential、revocation、re-certification、responsible party、review user privileges、risk-based timeline，核R06 p13、R13 p3、R03 pp13–14/19及R02附件F。

### Q23a · LC · 待办合规事项交接

- **监管预期 Y** 混合单元：待办报告期限、收件监管机关和§22测试为 Y；内部台账具体接收人 N。逐条对本轮 C08 交接的生产环境实际执行变更应用§22；如属实际部署后重大变更或§22(2)(b)–(d)实际移除／加入／变为关键系统项，应由金管局指定形式及途径于事件日期后1个月内通知。重大性按§22(3)及守则，不自动将批准、计划或离线测试视为生产部署。分期通常逐实际阶段算，也可初期合并预告。R03 §6.1.2 进一步指向不可回查的 C-RAF，不能凭空引用该细项；法例主条件仍可用。明确没有实际触发事件时按未触发；执行记录不明时暂 U 并补查，而非臆断。
- **原文定位** R01 §22(1)–(3) PDF pp.33–34（4-10–4-12）、附表2第2部 PDF p.89（S2-4）、§28(3)–(4) PDF p.44（4-32）及附表6项2–3 PDF p.97（S6-2）；R03 §§6.1.1–6.1.3 p.11；R02 §7.3.7 p.37；R05 pp.2–3、R07 §1.3.3 p.5、R11 p.8
- **可接受行动** LC 对照已发/未发/回执待核记录，把专员补表、11月30日报告和补充资料、金管局进度/实际变更、PCPD/客户、警方事项逐项登记归属、到时和证据，交继续负责的合规负责人或获授权代理。对生产变更逐项记系统、部署时点、§22具体分项、金管局通知计划或未触发理由。
- **决策码** REGISTER-HANDOFF + CHANGE-REPORT / CHANGE-NO-TRIGGER / CHANGE-VERIFY
- **检索与核验** 19份逐页查 handover/hand over/hand-off/action register/deadline register/compliance register/successor，未定位内部台账接收人条文；另正查 §22 material/production/phases。

### Q23b · LC · 证据保留与处置

- **监管预期 Y** 指定 CCS 有关日志监管最少保留6个月、防删改并授权访问，不能推广到一切事故资料。应急计划实践覆盖证据保全、保管链和过程记录；个人资料按直接/相关目的所需持有，目的结束应采取切实可行步骤删除，保留§26法律禁止删除或公众利益条件，受托处理者相应期限以约定或其他方法控制。其他证据的具体年限、法律保留触发与处置审批人要陈述为判断。
- **原文定位** R03 §6.2.23(a)–(d) p.18；R02 §§6.2.23(c), 7.2.3(a)(v)(2),(4) pp.20、32；R10 Cap.486 §26(1) PDF p.58（5-32），附表1第2(2)–(3)原则 PDF p.167（S1-6）
- **可接受行动** LC 与 SEC 交接证据清册、授权访问和保管链，至少保全相关 CCS 日志、网关和供应商证据、监管记录和决定凭据。按后续调查、承诺或法律保留需要设置复核，不在未到保留期或存在适用禁止删除情形下处置，目的终结后安排受控销毁或返还和留存处置凭据。
- **决策码** PRESERVE-REVIEW-DISPOSE
- **检索与核验** 19份逐页查 evidence/forensic/incident record/log 与 retention/preserve/delete/disposal 邻近，复读 R02 pp.20/32、R03 p.18 与第486章；未定位一刀切的事故证据期限。

### Q24a · COM · 公开状态收尾

- **监管预期 N** 一致且及时沟通、适当情况下事中事后传递信息、预计服务状态是一般指引。没有原文规定关账公告触发阈值、固定更新频次或72小时时点。C08只给离线240项结果，并未确认生产恢复，传讯获发的是最近公开消息和客户待办。
- **原文定位** 近似依据 R05 PDF 第3页 Handling of customers’ and media’s enquiry；R06 §8.3 Communication plans，PDF 第13页；R09 §8.2.2 脚注26 PDF 第33页。
- **可接受行动** 获核实恢复并批准时发布收尾说明，仍有生产限制则继续定期状态更新，未知时发布附条件更新或先核实。写给客户的实际影响、求助途径、下一次更新时间，避免把推演结束等同事件结束。
- **决策码** CLOSE_IF_OPERATION_VERIFIED／CONTINUE_UPDATES／CONDITIONAL_UPDATE_PENDING。
- **检索与核验** 检索19份冻结版 closing，closure，close-out，stand down，end of incident，after the incident，lessons learned，regular updates，up-to-date messages，resumption time；复核 R02/R05/R06/R07/R09/R11/R13/R14a/b 相关命中。

### Q24b · COM · 客服积压与后续接力

- **监管预期 N** 应变计划指定客户服务职能、通知及留记录，并在可能发生未授权电子银行交易时提供求助入口。未见直接规定本案结转给谁、必须采用何种格式、服务时限或跟进频次；卡上未给案件数量或具体承接团队。
- **原文定位** 近似依据 R11 PDF 第3页应变计划角色、第6页步骤5；R02 §7.2.3(a)(iv)–(v) PDF 第32页、§7.2.3(i) PDF 第33页；R09 §2.2.1 PDF 第7页和 §4.4.2 PDF 第17–18页。
- **可接受行动** 传讯按授权把待办、风险优先度、上次发出消息及承诺和下一次联系点交客户服务/补救负责人签收。保留客户ID和受限访问的日志引用，避免用公开渠道传客户敏感信息；安排值班升级和未签收追踪。
- **决策码** HANDOVER_CASE_REGISTER；仍待接手则 INTERIM_OWNER_AND_REMINDER，避免掉单。
- **检索与核验** 检索19份冻结版 handover，hand over，handoff，backlog，unresolved，customer service department，complaint，case owner，follow-up notification，comprehensive record；回查 R02/R05/R06/R07/R09/R11。

## 组员采纳记录

剧本及权限记录审核人和日期 ________

监管侧预期（v2）采纳人和时间 ________

A1 首次发卡时间另记，供核对先封存后开跑。
