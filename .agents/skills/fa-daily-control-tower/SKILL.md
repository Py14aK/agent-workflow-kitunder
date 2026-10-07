---
name: fa-daily-control-tower
description: Build an evidence-bound FA morning view from current Jira or spreadsheet snapshots, compare with the prior snapshot, and draft concise ticket updates without inventing progress.
---

# FA daily control tower

Use for daily Jira review, Morning View spreadsheets, ticket-delta extraction, handoff/status preparation, and Jira-ready update drafts.

Do not use this skill to derive BRD/FSD requirements; route those tasks to `fa-requirement-verifier`.

## Evidence precedence

Use the newest authoritative evidence first:

1. current Jira export or current ticket data, with retrieval/update timestamp;
2. current daily workbook/snapshot;
3. previous daily snapshot, only for delta calculation;
4. explicit ticket comments, linked-ticket evidence, meeting decisions, and source register;
5. static templates and legacy workflow documentation.

A lower-priority source must never overwrite a newer authoritative field without an explicit conflict note.

## Workflow

1. Record the as-of timestamp and inventory the current and prior sources.
2. Preserve ticket IDs and raw fields exactly before normalization.
3. Reconcile one row per ticket. Detect duplicates, stale rows, and identifier mismatches.
4. Compute only evidenced deltas: status, assignee, due date, fix version, updated timestamp, links, blockers, comments, and explicitly recorded next action.
5. Validate linked issues by relationship type (`clones`, `blocks`, `relates`, parent/epic). Do not copy a linked ticket's narrative into the current ticket unless the source explicitly establishes that scope.
6. Classify each ticket:
   - `CHANGED` — at least one authoritative field or explicit work item changed;
   - `UNCHANGED` — no evidenced delta;
   - `CONFLICT` — authoritative sources disagree;
   - `NEEDS_INPUT` — a requested conclusion is not supported by evidence.
7. Draft a Jira update only from current evidence:
   - sentence 1: observed state/delta;
   - sentence 2: concrete evidence/work explicitly present in the source;
   - sentence 3: next action only when explicit, otherwise `Next action: needs confirmation.`
8. Produce a Morning View with at least:
   `Ticket | Summary | Status | Owner | Due | Delta | Blocker/Link | Evidence | Next action | Jira draft`.
9. Keep raw/source sheets unchanged. Write derived content to a new or refreshed Morning View sheet.
10. Finish with a compact exception list: conflicts, missing evidence, stale sources, and tickets requiring human confirmation.

## Spreadsheet presentation

When editing an `.xlsx` and the tool supports it:

- preserve source worksheets and formulas;
- freeze the header row and enable filters on the Morning View;
- wrap text only where needed and use practical column widths;
- set print area to the used range;
- use landscape orientation and fit to **1 page wide** with automatic page height;
- avoid merged cells in the data table;
- do not expose page-break clutter as the primary working view.

Formatting is downstream of evidence correctness; never hide rows or fields to make the status look cleaner.

## Failure conditions

Stop or mark `CONFLICT`/`NEEDS_INPUT` when:

- current evidence is older than the supposed prior snapshot;
- ticket IDs or row ownership cannot be reconciled;
- status/assignee/due-date sources disagree without a clear authoritative timestamp;
- the proposed Jira narrative requires facts not present in the evidence;
- a linked ticket is being used as a substitute for current-ticket evidence.

Never turn a plausible story into a factual status update.
