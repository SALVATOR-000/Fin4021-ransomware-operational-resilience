---
name: lantidal-b1-com
description: Lan Tidal tabletop exercise role session for run B1 (COM). Started only by the facilitator. It can read the allowed sources through the read-only source tools and nothing else.
tools: mcp__sources__list_sources, mcp__sources__search, mcp__sources__read_page, mcp__sources__view_scan_page
model: opus
effort: medium
omitClaudeMd: true
mcpServers:
  - sources:
      type: stdio
      command: /usr/bin/python3
      args: ["-I", "/Users/zehaoliu/FIN 4021 Group Project/推演记录/检索入口/sources_server.py", "--role", "COM"]
hooks:
  PreToolUse:
    - matcher: "*"
      hooks:
        - type: command
          command: "/usr/bin/python3 -I '/Users/zehaoliu/FIN 4021 Group Project/推演记录/检索入口/tool_gate.py' --role COM"
---

You are taking part in a simulated tabletop exercise run by a facilitator. The facilitator's messages give you your role, the rules, the scenario cards and any handoffs. Follow them. Your final message in each turn is your submitted answer.
