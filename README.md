# Compact ChatGPT / Work / Codex / Copilot Workflow

This package implements a compact layered instruction architecture.

## Architecture

- `prompt` — compact cross-domain prompt.
- `AGENTS.md` — repository-wide agent guidance only.
- `.agents/skills/` — reusable, narrowly routed workflow skills.
- `.github/agents/` — GitHub Copilot agents. Each loads one skill.
- `.github/copilot-instructions.md` — Copilot routing for this repository.
- `chatgpt-work/PROJECT_INSTRUCTIONS.md` — project/Work instructions only.
- `chatgpt-work/COPILOT_AGENTS_2026-10-07.md` — first prompts when Chat cannot see the repository.
- `copilot/` — licensed Copilot daily kernel and run prompt.
- `copilot-free/` — free-tier Agent Builder instructions, starters, and academy kit.
- `codex/GLOBAL_AGENTS.md` — ready-to-copy global Codex instructions.
- `docs/EVIDENCE.md` — documentation basis and synthesized recommendations.
- `docs/ROUTING.md` — Global vs Project vs Skill vs transient task routing.
- `docs/COPILOT_REFERENCE_POLICY.md` — reference-budget rules that prevent prompt pile-up.
- `docs/MIGRATION.md` — migration steps from the existing large prompt/reference set.
- `tests/agent_contract/` — structural, isolation, and routing checks.
- `examples/` — one-off demos and archived case material. Not active instructions.
- `skills-kit/` — 70 third-party skills (maths, statistics, scientific Python, BigQuery, research review, engineering practice) for coworkers to install into their personal `~/.agents/skills/`. Not active in this repository. See `skills-kit/README.md`.

## FA split

- FSD/BRD/requirements verification → `fa-requirement-verifier`
- Daily Jira snapshot / Morning View / evidenced status updates → `fa-daily-control-tower`

Do not pin a stack of legacy master prompts, kernels, routing docs, and dated indexes at the same time. Use the smallest reference set that proves the current task.
