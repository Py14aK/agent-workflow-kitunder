# Repository agent instructions

Keep this file small. Do not rebuild a skill that already exists.

## Flow

```
READ prompt
  -> ROUTE to one prebuilt skill
  -> QUICK EXEC that skill only
  -> RARE CHECK only if a gate fires
  -> ARTIFACT + NEXT
  -> STOP
```

Do not pre-read every skill. Load only the matched `SKILL.md` and the file named in the prompt.

## Prebuilt map. Reuse these.

| Signal | Skill |
|---|---|
| morning snapshot, TSC board, Teams photo | snapshot-orchestrator |
| one ticket one lane, agent desk | desk-lanes |
| FSD, BRD, atoms, vertical card | fa-requirement-verifier |
| Gearheart, listings_clean, PSI, GainLift | end-to-end-sas-ds |
| re-derive, reproduce a paper number | research-rederive |
| portfolio, drawdown, holdings | quant-research-lab |
| publish after verification | research-publisher |

If two skills match, take the more specific one. Never mix FSD/VoP with Gearheart in one turn.

## Quick exec

Default. Run the skill script or emit the skill artifact.
Do not rewrite atom grammar, desk lanes, or LIBNAME rules from memory.
Do not invent a new skill for a job that already has one.

Quick commands already in the repo

```
python3 .agents/skills/snapshot-orchestrator/scripts/orchestrate_morning.py SNAP.yaml
python3 .agents/skills/desk-lanes/scripts/run_lanes.py SNAP.yaml
python3 .agents/skills/end-to-end-sas-ds/scripts/rewrite_libname.py FILE.sas --target PATH
python -m pytest tests/agent_contract -q
```

## Rare checks. Only these gates.

1. Identifier change. TSC-47959, CDTR.AGT.NM.1, BENEF.ID, listings_clean, 051, 369.
2. SOURCE CONFLICT. Two owners, clone vs parent, catalog missing.
3. Execution claim. SAS, pytest, git push, Jira write. Need a tool result in this turn.
4. Banned token. FIELD_1_NAME, BEN.NAME.CYR, guessed T24 field.
5. Domain mix. VoP ticket plus Gearheart data in one answer.

If no gate fires, do not add a review paragraph.

## Repository contract

- Domain workflows live in `.agents/skills/`. Do not copy them into this file.
- Preserve provenance. A photo is not live Jira.
- Do not claim a command succeeded unless its output was observed.
- One-off requirements stay in the current task prompt.
- Surface conflict. Do not pick a convenient source.

## Verification when this file or a skill changes

1. `python -m pytest tests/agent_contract -q`
2. Skill names still route.
3. This file stays under 12 KiB.
4. Unverified behavior is marked.
