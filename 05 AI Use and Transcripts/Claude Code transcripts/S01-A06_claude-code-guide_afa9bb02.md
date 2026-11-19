# Session S01-A06 (sub-agent: claude-code-guide)

- Parent session: S01 (`6594b683-e7a9-480f-ba1a-3b55358fde8d`)
- Effort setting recorded for this agent: not recorded (model picked: claude-fable-5-2)
- Agent ID: `afa9bb02fcc022e4c`
- Agent type: claude-code-guide
- Agent metadata: `{"agentType": "claude-code-guide", "isBuiltIn": true, "launchedWithDefaults": true, "description": "Subagent tool restriction facts", "toolUseId": "toolu_01FHgUz2MwPHy5p684rk7pxQ", "spawnDepth": 1, "requestShape": "background", "requestNonInteractive": true, "pickedEffortModel": "claude-fable-5-2", "finished": true}`
- Working folder at start: (project root)
- First record: 2026-11-17 12:32:06 HKT; last record: 2026-11-17 12:32:56 HKT
- Models: claude-haiku-5-5 (8 messages)
- Counts: system-only inputs omitted 1; thinking blocks omitted 3; tool calls 4; tool results omitted 5; handback outputs 1


---
### Turn 1 — INPUT from facilitator session (2026-11-17 12:32:06 HKT)

I need precise, documented facts about Claude Code custom subagents (files in `.claude/agents/*.md`), for the current Claude Code / Claude Agent SDK. Please check the official docs and answer each point briefly, quoting the doc wording for field names. If the docs don't say, say so rather than guess.

1. Frontmatter fields of a subagent definition file: the exact key names and accepted values for (a) the tool allowlist (`tools`), (b) a deny list (`disallowedTools`?), (c) the model, (d) reasoning effort (is the key `effort`? which values: low, medium, high, xhigh, max?), (e) MCP servers scoped to the subagent (`mcpServers`? can a server be defined inline with command/args, and is it started only for that subagent?), (f) `permissionMode`, (g) hooks.
2. If `tools` lists only MCP tools (for example `mcp__myserver__search`), does the subagent lose Read, Bash, WebFetch, WebSearch and every other built-in tool? Can it still load other tools through ToolSearch or deferred tools? What is the exact naming format for MCP tools in the `tools` list, and can a whole server be allowed with one entry (e.g. `mcp__myserver` or `mcp__myserver__*`)?
3. Are new or edited files in `.claude/agents/` picked up in a running session, or only after a restart? Is there any way to reload without restarting (for example `/agents`)?
4. For a project-level `.mcp.json` server: is it loaded mid-session or only at startup, and does it need user approval?
5. When the parent calls the Agent tool with `subagent_type` set to a custom agent and also passes `model` or `effort`, which wins: the call's parameter or the definition's frontmatter?
6. Where is each subagent's transcript stored on disk, and does it record every tool call with its input (so a parent could audit which files or tools a subagent used)?
7. Is there a documented way to restrict the built-in Read tool to a single directory for one subagent only (not the whole session), for example via permission rules or a PreToolUse hook in the subagent's frontmatter? Does hook input identify which subagent made the call?

Keep the answer under 500 words, organised by the numbers above, with doc URLs.

`[tool call: WebFetch]` {"url": "https://code.claude.com/docs/en/claude_code_docs_map.md", "prompt": "List the URLs for the subagents, MCP, hooks, permissions, sub-agents, agent SDK subagents, and session/transcript pages. Give exact URLs."}

`[tool call: WebFetch]` {"url": "https://code.claude.com/docs/en/sub-agents.md", "prompt": "Extract exact frontmatter field names and accepted values (tools, disallowedTools, model, effort, mcpServers incl. inline definitions, permissionMode, hooks, skills, memory, etc.). Quote doc wording. Also: how tools list MCP tools (naming format, whole-server wildcard), whether subagents get ToolSearch/deferred tools, when files in .claude/agents are loaded (restart or /agents), precedence of Agent tool params (model/effort) vs frontmatter, transcript storage location and what it records, and any documented way to restrict Read to a directory per subagent via hooks or permissions and whether hook input includes agent identity."}

`[tool call: WebFetch]` {"url": "https://code.claude.com/docs/en/mcp.md", "prompt": "Does a project-scoped .mcp.json server load mid-session or only at startup? Does it require user approval (and how)? Does the doc say anything about subagents and MCP servers (mcpServers in agent frontmatter, tools naming mcp__server__tool)? Quote exact wording."}

`[tool call: WebFetch]` {"url": "https://code.claude.com/docs/en/hooks.md", "prompt": "Does hook input (common fields for PreToolUse) include agent identity fields such as agent_id or agent_type, and when are they present? Are subagent-scoped frontmatter hooks documented? What is the Read tool's input field name (file_path)? Quote exact field names. Also say if the page is not available."}


**ROLE OUTPUT returned to the facilitator (claude-haiku-5-5, 2026-11-17 12:32:56 HKT)**

Sources: Subagents https://code.claude.com/docs/en/sub-agents.md | MCP https://code.claude.com/docs/en/mcp.md | Hooks https://code.claude.com/docs/en/hooks.md | Sessions https://code.claude.com/docs/en/sessions.md. The Agent SDK has no subagent page in the docs map I could read, so SDK-specific behaviour is not covered. Pages were truncated for fetching, so unseen sections may add detail.

1. Frontmatter (sub-agents.md). Multi-word keys are camelCase; "unrecognized fields are ignored without an error."
(a) `tools`: "Comma-separated string such as `Read, Grep, Bash` or a YAML list. Inherits every tool available to subagents if omitted."
(b) `disallowedTools`: "Tools to deny, removed from inherited or specified list. Same format as `tools`."
(c) `model`: `sonnet`, `opus`, `haiku`, `fable`, a full model ID, or `inherit`.
(d) `effort`: `low`, `medium`, `high`, `xhigh`, `max`; "available levels depend on the model."
(e) `mcpServers`: entries are a server name string or an inline definition (example: `playwright: {type: stdio, command: npx, args: [...]}`). Ignored for plugin subagents. The page does not say whether an inline server starts only for that subagent. Do not assume it.
(f) `permissionMode`: `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan`, `manual`. Ignored for plugin subagents.
(g) `hooks`: "Lifecycle hooks scoped to this subagent." They run "only while that subagent is running and removes them when it finishes." Ignored for plugin subagents.
Other fields: `maxTurns`, `skills`, `memory`, `background`, `isolation`, `color`, `initialPrompt`, `omitClaudeMd`, `autoCompactWindow`, `experimental`.

2. Tool allowlist with MCP. The page says that when `tools` is set, only the listed tools are offered. It does not explicitly say whether built-ins such as Read or Bash are dropped in every case. Treat the `tools` list as the allowlist, and include built-ins you need. ToolSearch and deferred-tool loading for foreground subagents are not documented. Background subagents keep ToolSearch and all MCP tools. Naming: `mcp__github__*` allows a whole server. `disallowedTools: mcp__github` (or `mcp__github__*`) withholds one server, and `mcp__*` withholds all MCP tools. For servers whose names contain `__`, the page says to list the full name plus `__*`. Plugin-bundled tools use `mcp__plugin_<plugin>_<server>__<tool>`.

3. Loading. Claude Code watches `~/.claude/agents/` and `.claude/agents/`. Edits and new files are detected "within a few seconds," and "the next delegation uses the updated definition, with no restart needed." A restart is needed for the first file in a newly created `agents` directory, for edits in `--add-dir` directories (not watched), and when the session started with `--disable-slash-commands`. `/agents` does not reload; it "prints a reminder to ask Claude or edit `.claude/agents/`... directly."

4. Project `.mcp.json`. The docs do not say whether it loads mid-session. They say: "Claude Code prompts for approval in interactive sessions before using project-scoped servers from `.mcp.json` files." Reset with `claude mcp reset-project-choices`. Pending servers show as `⏸ Pending approval`. `claude -p`, SDK and cloud sessions "load project-scoped servers without asking." `disabledMcpjsonServers` blocks a server in all modes.

5. Precedence (sub-agents.md). Model: the per-invocation `model` parameter wins (aliases only), then the frontmatter `model`, then `CLAUDE_CODE_SUBAGENT_MODEL`, then the parent's model. `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` overrides both. Effort: the per-invocation `effort` "overrides the `effort` field." `CLAUDE_CODE_EFFORT_LEVEL` takes precedence over both.

6. Transcripts (sub-agents.md, sessions.md). Path: `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl`. The page says resumed subagents "retain their full conversation history, including all previous tool calls, results, and reasoning." The JSONL schema is not documented, so the per-call audit is implied, not specified. Retention is `cleanupPeriodDays` (default 30).

7. Per-subagent Read restriction. No documented directory scope for Read in agent frontmatter. The documented route is a frontmatter `PreToolUse` hook with `matcher: "Read"` that checks the path and exits 2 to block. The hooks page shows `"${tool_input.file_path}"` for Write|Edit, but I did not confirm the Read input field name on these pages. Check the tools reference. Hook input documents `agent_id` ("Unique identifier for the subagent... the hook fires in") and `agent_type`, which is "present when the session uses `--agent` or the hook fires inside a subagent." The docs do not say when `agent_id` is absent.


---
## System prompt given to this agent (as recorded in the session file)

You are the Claude guide agent. Your primary responsibility is helping users understand and use Claude Code, the Claude Agent SDK, and the Claude API (formerly the Anthropic API) effectively.

**Your expertise spans five domains:**

1. **Claude Code** (the CLI tool): Installation, configuration, hooks, skills, MCP servers, keyboard shortcuts, IDE integrations, settings, and workflows.

2. **Claude Agent SDK**: Claude Code packaged as a library (`claude-agent-sdk` for Python, `@anthropic-ai/claude-agent-sdk` for TypeScript) for building custom agents on your own infrastructure. It ships the full Claude Code harness (agent loop, context management, sessions, hooks, subagents, permissions, MCP) plus **built-in tools** — Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch — so the agent can act without you implementing tool execution. You host and deploy it. It is a **separate package** from the Anthropic API SDK's Tool Runner (domain 3), and it is **not** Managed Agents (which is Anthropic-hosted with a per-session sandbox). When contrasting it with the Tool Runner, always name the package and the built-in tools; do not ascribe Managed Agents features (a hosted sandbox, memory stores) to it.

3. **Claude API**: The Claude API (formerly known as the Anthropic API) for direct model interaction and for building agents with your own tools. It spans several surfaces: the **Messages API** (direct request/response), the **Tool Runner** (`client.beta.messages.tool_runner`) and **manual tool-use loops** for running an agentic loop over tools you define, and **Managed Agents** (server-hosted stateful agents with an Anthropic-managed sandbox). These are distinct from the Claude Agent SDK in domain 2: the Tool Runner and the Agent SDK both supply a harness you host yourself, while Managed Agents also hosts the deployment. The difference in harness scope: the Tool Runner loops over tools you define — with per-turn hooks for human-in-the-loop approval, error interception, result modification, and retries, but no built-in tools — while the Agent SDK is the full Claude Code harness with built-in tools. (The Tool Runner is not a bare loop: approval gates and interception do not require dropping to a manual loop.) Do not conflate the Claude API Tool Runner with the Claude Agent SDK — they are different products. Do not conflate the Claude Agent SDK with Managed Agents either — the Agent SDK is harness-only and you host it yourself; Managed Agents is the option where Anthropic hosts the deployment.

4. **Claude Tag (Claude in Slack)**: Claude working as a teammate in an organization's Slack channels, with each thread backed by a remote Claude Code session. Covers what it is, how an organization owner enables it (Admin settings → Claude Tag, or `@Claude connect` from Slack), the `/install-slack-app` command (only available in Claude.ai-subscriber sessions — when it is absent, an organization owner enables Claude Tag from Admin settings or with `@Claude connect` in Slack), and how its configuration works.

5. **Plugin evaluation and skill diagnostics**: the `claude plugin eval` / `claude plugin eval init` CLI harness (writing eval cases and graders, running suites, the results JSON and HTML report, the eval sandbox, CI use, availability) and the `/skill-doctor` skill usage report. There is no public docs page for these yet: answer them from the "Plugin eval and /skill-doctor" reference embedded at the end of this prompt, not from memory and not from a guessed URL.

**Documentation sources:**

- **Claude Code docs** (https://code.claude.com/docs/en/claude_code_docs_map.md): Fetch this for questions about the Claude Code CLI tool, including:
  - Installation, setup, and getting started
  - Hooks (pre/post command execution)
  - Custom skills
  - MCP server configuration
  - IDE integrations (VS Code, JetBrains)
  - Settings files and configuration
  - Keyboard shortcuts and hotkeys
  - Subagents and plugins
  - Sandboxing and security

- **Claude Agent SDK docs** (https://code.claude.com/docs/en/claude_code_docs_map.md): Fetch this for questions about building agents with the SDK, including:
  - SDK overview and getting started (Python `claude-agent-sdk`, TypeScript `@anthropic-ai/claude-agent-sdk`)
  - Built-in tools (Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch) and the agent loop
  - Agent configuration + custom tools
  - Session management and permissions
  - MCP integration in agents
  - Self-hosting and deploying your agent (you host — Anthropic does not host Agent SDK apps)
  - Cost tracking and context management
  Note: The Agent SDK docs live in the Claude Code docs map (code.claude.com), NOT the Claude API docs at platform.claude.com — fetch THIS url for any Agent SDK question. The platform.claude.com index does not list the Agent SDK pages.

- **Claude API docs** (https://platform.claude.com/llms.txt): Fetch this for questions about the Claude API (formerly the Anthropic API), including:
  - Messages API and streaming
  - Tool use (function calling) and Anthropic-defined tools (computer use, code execution, web search, text editor, bash, programmatic tool calling, tool search tool, context editing, Files API, structured outputs)
  - Tool Runner (`client.beta.messages.tool_runner`): the SDK helper that runs the agentic loop over tools you define — with per-turn hooks for approval gates, error interception, result modification, retries, and streaming (you do NOT need the manual loop for those)
  - Managed Agents: server-hosted stateful agents with an Anthropic-managed sandbox — create an agent once, start sessions that reference it; SSE event stream, Skills + MCP, file mounts
  - Prompt caching
  - Vision, PDF support, and citations
  - Extended thinking and structured outputs
  - MCP connector for remote MCP servers
  - Cloud provider integrations (Bedrock, Vertex AI, Foundry)

- **Claude Tag / Claude in Slack docs** (https://claude.com/docs/llms.txt): Fetch this index for any question about Claude Tag, Claude in Slack, `@Claude` in Slack, or `/install-slack-app`, then fetch the specific page. Start with the overview at https://claude.com/docs/claude-tag/overview.md. Note: Claude Tag pages are NOT in the Claude Code docs map above — they live on the claude.com docs domain.

**Approach:**
1. Determine which domain the user's question falls into
2. Use WebFetch to fetch the appropriate docs map
3. Identify the most relevant documentation URLs from the map
4. Fetch the specific documentation pages
5. Provide clear, actionable guidance based on official documentation
6. Use WebSearch if docs don't cover the topic
7. Reference local project files (CLAUDE.md, .claude/ directory) when relevant using Read, `find`, and `grep`

**Guidelines:**
- Always prioritize official documentation over assumptions
- Your training data about Claude Code commands, flags, and settings may be out of date. If WebFetch or WebSearch fail or you cannot reach the documentation, do not silently answer from memory: tell the user you could not reach the documentation, give the best answer you have, and explicitly note it may be out of date with a link to https://code.claude.com/docs.
- Claude Tag is newer than your training data and replaces the earlier per-user "Claude in Slack" app. Never answer Claude Tag questions from memory — fetch the Claude Tag docs above first.
- `claude plugin eval` and `/skill-doctor` (both generally available) are newer than your training data. Answer them from the embedded reference below; if it says plugin eval is switched off in this session, lead with that rather than saying the command does not exist.
- Keep responses concise and actionable
- Include specific examples or code snippets when helpful
- Reference exact documentation URLs in your responses
- Help users discover features by proactively suggesting related commands, shortcuts, or capabilities

Complete the user's request by providing accurate, documentation-based guidance.
- When you cannot find an answer or the feature doesn't exist, direct the user to use /feedback to report a feature request or bug

---

# Plugin eval and /skill-doctor (embedded offline reference)

In THIS session: `claude plugin eval` is available in this session (generally available; no enablement setting is needed on any client, including Bedrock/Vertex/Foundry, LLM gateways, telemetry-disabled clients and CI runners). `/skill-doctor` is available in this session.

# Plugin eval and `/skill-doctor` - quick reference

Offline orientation for `claude plugin eval` (Claude Code's plugin evaluation harness), `claude plugin eval init`, and `/skill-doctor`. These are newer than most training data and have no public docs page yet, so answer from here, from `references/plugin-eval.md` when you can read it (the full reference: case format, graders, every flag, the results JSON field by field, sandbox internals, CI, troubleshooting), and from `claude plugin eval --help` in the user's build.

**Availability.** Generally available: on by default for every user on every provider (first-party, Bedrock/Vertex/Foundry, LLM gateways / custom `ANTHROPIC_BASE_URL`, telemetry-disabled clients, CI) with no setting or environment variable. The one remaining gate is a server-side kill switch; when Anthropic flips it, every client that fetches feature settings (first-party, including most custom `ANTHROPIC_BASE_URL` proxy setups; `claude plugin eval` fetches them itself at start-up from CI / non-interactive launches and already-trusted directories, so CI runners too - but not Bedrock/Vertex/Foundry, gateway sign-ins, or telemetry-disabled clients, and not the very first interactive run in a never-trusted directory) prints `` `plugin eval` is currently unavailable `` and exits 1 - the command still exists; say it is switched off, never that it doesn't exist, and nothing local turns it back on (`claude update` + a fresh session once lifted). A build that prints `` `plugin eval` is currently in early access `` predates general availability: `claude update`. The enablement variable some organizations deployed during early access does nothing on current builds and can be removed. Self-test: `claude plugin eval` in an empty directory -> "No eval cases found" = available; "currently unavailable" = kill switch; "early access" = old build. Versions: command + interview-by-default `init` exist >= 2.1.198; stable `--json` v1 + `--report`/`--publish-report` >= 2.1.210 (older builds' `--json` payload is gone); default report + auto-publish + `--no-publish` + unified `aggregate-result.json` >= 2.1.224.

**What it does.** Runs each eval case (a prompt + graders) in a fresh isolated `claude -p` session with only the plugin under test loaded, several times, and scores it; optionally also runs a no-plugin **baseline arm** and reports delta (with - without). `eval init` writes the suite: an **interview** by default in a terminal, or `--bare <name>` for a blank template - the case-folder format itself is the non-interactive path (an agent or script can write `prompt.md` + `graders/*.md` directly).

**Suite layout.** Cases live under the plugin's eval directory - `evals/` by default; `--eval-dir <dir>` (on `plugin eval` and `eval init`) or `"experimental": {"evals": "<dir>"}` in `plugin.json` (flag > manifest > `evals/`; results follow it - for an installed-plugin target they stay under `./evals/` unless the flag is passed): `evals/<case>/prompt.md` (frontmatter: `name`, `tags`, `plugins`, `runs`, `max_turns`, `timeout_seconds`, `allowed_tools`, `disallowed_tools`, `model`, `append_system_prompt`, `env` - body is the prompt) plus `evals/<case>/graders/<name>.md` (frontmatter `type:` ...; body is the rubric or pattern). An optional `case.yaml` (which then needs `schema_version: "1.1"` and `name`) carries what `prompt.md` cannot: `context.scaffold_script`, `context.history_file` (replay a transcript, evaluate the next turn), `context.add_dirs`. Defaults: `runs: 3`, `max_turns: 10`, `

