---
name: snapshot-orchestrator
description: Turn morning Jira screenshots, Copilot drafts, and morning_daily workbooks into a one-day execution board. Trigger on snapshot, morning daily, orchestrate workflow, Jira daily routing, TSC board, or draft Jira update from photos.
metadata:
  type: workflow
  version: "2026-09-28"
---

# Snapshot orchestrator

Build today's board from what is actually on screen or in the workbook. Do not fetch Jira unless a tool result exists in the same turn.

## Inputs

Accept any mix of

- morning_daily_*.xlsx or a YAML snapshot extracted from it
- screenshots or video of Copilot drafts
- local prompt files (12_JIRA_DAILY_ROUTING.md, 09_AUTONOMOUS_EXECUTION_CONTRACT.md, 01_THREE_PHASE_WORKFLOW.md)

A path, filename, or photo does not prove the ticket was read in Jira.

## Steps

1. Inventory sources with date and medium. Photo, workbook, Copilot draft, live Jira.
2. Extract exact keys. TSC-47959 stays TSC-47959. Preserve titles in the source language. Preserve CDTR.AGT.NM.1, R26_INC19789557_2, fix-version strings.
3. Group clones under parents. A NEW clone does not replace the parent test pack.
4. Classify each row. CONFIRMED from the snapshot. INFERRED only if labelled. CONFLICT when two sources disagree. MISSING when a required artefact is named but absent.
5. Route. VoP / FSD / T24 field / CDTR.AGT.NM.1 to fa-requirement-verifier. Publication or handover deck to research-publisher. Do not mix Research or portfolio skills into the morning board.
6. Emit four artefacts and stop. morning_board_YYYY-MM-DD.md; draft Jira comments marked DRAFT NOT POSTED; risk list A/B; checkpoint log T+00 T+20 T+40 T+60.
7. Never claim a Jira update, SharePoint write, or git push without a tool result in the same turn.

## Draft comment grammar

```
TSC-xxxxx
Status. [source status]
Clone of. [parent or none]
Confirmed next action.
Evidence still missing.
Do not. [duplicate test / silent field rename / treat draft as posted]
```

## Hard stops

- Do not treat Copilot text as a posted Jira comment.
- Do not collapse TSC-47959 into TSC-47675.
- Do not invent BENEF.ID or T24 fields absent from the snapshot.
- Do not run SAS or elliptic-heart code from this skill.
