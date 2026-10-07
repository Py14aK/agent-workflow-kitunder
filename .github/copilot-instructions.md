# Copilot instructions

Read `AGENTS.md` and `docs/ROUTING.md` before acting. Do not rebuild a skill that already exists.

Flow. Read the task. Route to one prebuilt skill. Load only that `SKILL.md`. Emit the artefact. Stop.

| Signal | Agent | Skill |
|---|---|---|
| morning snapshot, TSC board, Teams photo | snapshot-orchestrator | `.agents/skills/snapshot-orchestrator/SKILL.md` |
| one ticket, one lane, desk | desk-lanes | `.agents/skills/desk-lanes/SKILL.md` |
| FSD, BRD, atoms, vertical card | fa-requirement-verifier | `.agents/skills/fa-requirement-verifier/SKILL.md` |
| Morning View, ticket delta, evidenced Jira draft | fa-daily-control-tower | `.agents/skills/fa-daily-control-tower/SKILL.md` |
| Gearheart, listings_clean, PSI, GainLift | end-to-end-sas-ds | `.agents/skills/end-to-end-sas-ds/SKILL.md` |
| re-derive, reproduce a paper number | research-rederive | `.agents/skills/research-rederive/SKILL.md` |
| portfolio, drawdown, holdings | quant-research-lab | `.agents/skills/quant-research-lab/SKILL.md` |
| publish after verification | research-publisher | `.agents/skills/research-publisher/SKILL.md` |
| classify session, AI R&D taxonomy | research-classifier | `.agents/skills/research-classifier/SKILL.md` |

If two skills match, take the more specific one. Never mix FSD or VoP with Gearheart in one turn.

Preserve identifiers exactly. A photo is not live Jira. Do not claim a command, Jira write, or git push succeeded unless a tool result in this turn shows it.

Banned unless the token is in the user-supplied source: FIELD_1_NAME, BEN.NAME.CYR, a guessed T24 field.
