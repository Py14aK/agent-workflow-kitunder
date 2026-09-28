---
name: desk-lanes
description: Run the four-lane work desk for agents. Trigger on cool workflow for agents, desk lanes, lane conductor, one ticket in flight, or chain snapshot atoms evidence draft.
metadata:
  type: workflow
  version: "2026-09-28"
---

# Desk lanes

One ticket in one lane. No domain mix. No Jira write from this skill.

```
L0 SNAPSHOT --> L1 ATOM --> L2 EVIDENCE --> L3 DRAFT --> STOP
```

## Lanes

L0 SNAPSHOT
Skill. snapshot-orchestrator
In. photo, workbook, Teams, Copilot draft
Out. morning_board_YYYY-MM-DD.md
Ban. field names, FSD rewrite, elliptic heart

L1 ATOM
Skill. fa-requirement-verifier or ubb-fsd-rewrite
In. one TSC key plus Word FSD or snapshot title
Out. 03_BRD_ATOMS.txt and 04_FSD_ATOMS.txt
Ban. markdown tables, FIELD_1_NAME, guessed T24 tokens

L2 EVIDENCE
Skill. fa-requirement-verifier
In. T24 screenshot, XML, payload, catalog slice
Out. 06_GAPS.txt plus matched FIELD lines
Ban. binding a T24 name or Teams text to a key unless the key is on the same artefact

L3 DRAFT
Skill. snapshot-orchestrator draft grammar
In. atoms plus gaps
Out. DRAFT NOT POSTED comment
Ban. posting, collapsing clone into parent, resolving SOURCE CONFLICT

STOP
Print NEXT_LANE and the missing artefact. Do not start L1 on a second ticket while L3 is open.

## Ticket lock

If the user names TSC-46805, stay on TSC-46805.
VoP clones stay under their parents. TSC-47959 does not eat TSC-47675.

## Cool path

Agents look fast when they skip lanes. This desk is cool because it refuses the skip.

1. Name the ticket.
2. Name the lane.
3. Emit only that lane's artefact.
4. Print NEXT_LANE or STOP.
