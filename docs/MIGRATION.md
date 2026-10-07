# Migration from the existing large prompt/reference stack

1. Preserve the existing repository `prompt` file as a legacy snapshot before replacement.
2. Replace the active global prompt with the compact version in this package.
3. Copy `codex/GLOBAL_AGENTS.md` to `~/.codex/AGENTS.md` for Codex global guidance.
4. Keep repository-specific guidance in root or nested `AGENTS.md`.
5. Install/copy the skill directories where Codex, ChatGPT, or Copilot skill discovery can see them.
6. Paste `chatgpt-work/PROJECT_INSTRUCTIONS.md` into the relevant ChatGPT Project/Work project instructions.
7. For licensed Microsoft Copilot daily FA work, pin `copilot/FA_DAILY_KERNEL.md`, today's export/workbook, and at most the immediately previous snapshot.
8. For free-tier Copilot Chat, paste `copilot-free/AGENT_FA_JIRA_INSTRUCTIONS.txt` into an instructions-only agent. Do not put directive text only in knowledge files.
9. Move domain-specific material out of the old main prompt:
   - physics/gravity/paper procedures → research skill/project docs
   - portfolio horizons/current positions → Investment project state
   - BRD/FSD rules → `fa-requirement-verifier`
   - Jira daily/Morning View rules → `fa-daily-control-tower`
   - Friday/newsletter formatting → publisher skill/project instructions
   - Sudoku-specific constraints → Sudoku project instructions
10. Treat legacy master prompts, dated indexes, old core kernels, routing docs, and autonomous-execution contracts as archive/source material. Do not pin them all as active Copilot references.
11. Keep one-off scripts and examples outside active instruction files.
12. Validate positive and negative routing examples.
13. Keep the old prompt/reference set until the compact setup has been used successfully on representative tasks, then archive rather than delete it.

## GitHub write status

Writes on 2026-10-07 landed on `Py14aK/agent-workflow-kitunder` `main` through the authenticated GitHub account. The site page and `robots.txt` attached with this batch were not copied here. They belong to a different repository.
