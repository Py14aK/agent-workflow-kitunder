# Copilot paste packs

Paste the whole file into GPT-5.6 Sol Copilot as one message.
Keep SYSTEM above USER. Do not split them.

| Pack | Use |
|---|---|
| COPILOT_SNAPSHOT_ORCHESTRATOR_2026-09-28.txt | Morning Jira board from workbook or screenshots |
| COPILOT_ELLIPTIC_HEART_2026-09-28.txt | Elliptic heart only. Not a work ticket. |
| COPILOT_AGENTS_2026-10-07.md | Best-case first prompt for each Copilot agent |

Agent files that GitHub Copilot Chat can read when this repository is open:

- `.github/copilot-instructions.md`
- `.github/agents/*.agent.md`
- `.agents/skills/*/SKILL.md`

Microsoft 365 Copilot Chat does not read those paths. Use the paste block in `COPILOT_AGENTS_2026-10-07.md` and attach the skill file.

After paste, attach morning_daily_*.xlsx if you have a newer file. The frozen ticket list is a photo extract, not live Jira.
