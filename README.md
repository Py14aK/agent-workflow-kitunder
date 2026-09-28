# Compact ChatGPT / Work / Codex Workflow

This package implements the compact instruction architecture agreed on 2026-09-28.

## Architecture

- `prompt` — compact cross-domain prompt.
- `AGENTS.md` — repository-wide Codex guidance only.
- `.agents/skills/` — four reusable workflow skills.
- `chatgpt-work/PROJECT_INSTRUCTIONS.md` — project/Work instructions.
- `codex/GLOBAL_AGENTS.md` — ready-to-copy global Codex instructions.
- `docs/EVIDENCE.md` — documentation basis and synthesized recommendations.
- `docs/ROUTING.md` — Global vs Project vs Skill vs transient task routing.
- `docs/MIGRATION.md` — migration steps from the existing large prompt.
- `tests/agent_contract/` — lightweight structural/routing checks.

The existing GitHub `prompt` file should be preserved as legacy history before replacement.
