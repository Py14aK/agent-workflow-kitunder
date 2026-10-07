# Microsoft Copilot reference policy

## Problem this prevents

A Copilot chat can appear grounded while actually receiving several overlapping instruction generations: a master prompt, core kernel, dated indexes, routing docs, handover templates, autonomous-execution contracts, and old snapshots. The result is context competition:

- outdated rules may outrank current task evidence;
- narrative templates can manufacture plausible but unsupported ticket progress;
- linked-ticket text can leak into the wrong ticket;
- the model spends context on instruction duplication instead of the current Jira/Excel evidence.

## Rule: instructions are a budget

For FA daily work, the normal reference set is:

1. `copilot/FA_DAILY_KERNEL.md`;
2. today's authoritative export/workbook;
3. the previous snapshot if a delta is needed.

Add one decision/source-register document only when the current ticket genuinely needs it.

Everything else is retrieved on demand, not permanently pinned.

## Separate roles

| Layer | Contains | Must not contain |
|---|---|---|
| global prompt | stable response/evidence behavior | ticket state, project dates |
| project instructions | stable local project rules | dated daily snapshots |
| skill/kernel | repeatable procedure | current ticket claims |
| current evidence | Jira/Excel/ticket comments for this run | durable instruction policy |
| archive | old prompts, dated indexes, superseded workflows | active instructions |

## FA routing

- BRD/FSD → `fa-requirement-verifier`
- Jira daily/Morning View → `fa-daily-control-tower`

Do not combine them by default. Requirement interpretation is slower and broader than daily status extraction.

## Jira-draft quality gate

Reject a draft if any factual clause cannot be pointed back to one of:

- a current Jira field;
- a dated current-ticket comment;
- an explicit decision/source record;
- an explicitly typed link relationship plus supporting source.

When evidence is absent, write `NEEDS_INPUT` rather than filling the gap with a plausible workflow narrative.
