# Copilot best-case prompts

Date: 2026-10-07.

GitHub Copilot agent mode reads `.github/agents/*.agent.md` and `.agents/skills/*/SKILL.md` when this repository is open. Select the agent. Do not paste the skill body.

Microsoft 365 Copilot Chat does not discover those files. Paste one block below, then attach the named `SKILL.md` and the inputs. One agent per chat.

## GitHub Copilot first messages

Kit router

```
AGENT: kit-router
Read AGENTS.md. Route this request to one agent. Do not execute it.
REQUEST: (one sentence)
```

Snapshot orchestrator

```
AGENT: snapshot-orchestrator
Load .agents/skills/snapshot-orchestrator/SKILL.md.
SOURCE: morning_daily workbook or attached photo. Not live Jira.
DATE: YYYY-MM-DD
Emit the four artefacts. Mark comments DRAFT NOT POSTED. Stop.
```

Desk lanes

```
AGENT: desk-lanes
Load .agents/skills/desk-lanes/SKILL.md.
TICKET: TSC-xxxxx
LANE: L0
Emit only this lane. Print NEXT_LANE. Do not open a second ticket.
```

FA requirement verifier

```
AGENT: fa-requirement-verifier
Load .agents/skills/fa-requirement-verifier/SKILL.md.
FSD_ID: (one id)
WORD_FSD: attached or NOT SUPPLIED
CATALOG_SLICE: attached or NOT SUPPLIED
One obligation per requirement. Preserve identifiers. No guessed T24 fields.
```

End-to-end SAS DS

```
AGENT: end-to-end-sas-ds
Load .agents/skills/end-to-end-sas-ds/SKILL.md.
LANE: G1
FILE: listings_clean path or NOT SUPPLIED
TARGET_LIB: path or NOT SUPPLIED
One model family. If SAS is absent, emit the program and mark EXECUTION not_performed.
```

Research rederive

```
AGENT: research-rederive
Load .agents/skills/research-rederive/SKILL.md.
CLAIM: (one sentence)
SOURCE: citation or NOT SUPPLIED
Re-derive. One adversarial check. Do not publish.
```

Quant research lab

```
AGENT: quant-research-lab
Load .agents/skills/quant-research-lab/SKILL.md.
SNAPSHOT: file and valuation date
DECISION: one statistic
Reconcile one total before any other figure.
```

Research publisher

```
AGENT: research-publisher
Load .agents/skills/research-publisher/SKILL.md.
DOSSIER: verified file or NOT SUPPLIED
If the central claim is unverified, stop and name research-rederive.
```

Research classifier

```
AGENT: research-classifier
Load .agents/skills/research-classifier/SKILL.md.
SESSION: attached
TAXONOMY: attached
Return one leaf label only.
```

## Microsoft 365 Copilot Chat paste

Use when the chat cannot see the repository. Attach the skill file. Do not ask the chat to fetch GitHub.

```
SYSTEM
You are one agent. Load only the attached SKILL.md.
Do not invent a second workflow.
Preserve identifiers exactly.
A photo is not live Jira.
Do not claim a tool, Jira write, or run unless the result is in this turn.
Banned unless present in the attached source: FIELD_1_NAME, BEN.NAME.CYR, guessed T24 field.
If the request matches a different skill, print SWITCH_AGENT and the skill name, then stop.

USER
SKILL: (name)
INPUTS: (attached or NOT SUPPLIED)
OUTPUT: the artefact named in the skill, then stop.
```
