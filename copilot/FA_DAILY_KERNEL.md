# Microsoft Copilot — FA Daily Kernel

Purpose: run the daily Jira/Morning View workflow with a small, deterministic reference set.

## Reference budget

Pin/reference only:

1. **This kernel**.
2. **Today's authoritative Jira/Excel export**.
3. **The immediately previous snapshot** when a delta is required.
4. Optionally, **one** source-register/decision file when a ticket requires requirement-level interpretation.

Do **not** simultaneously reference a legacy master prompt, multiple dated index files, old core kernels, old routing files, autonomous-execution contracts, handover templates, and historical snapshots. Those are source/archive material, not parallel instruction layers.

## Daily contract

- Current Jira fields win over older snapshots.
- Preserve exact ticket IDs, statuses, owners, dates, link types, and timestamps.
- Compare current vs previous; do not infer activity from prose similarity.
- Use linked-ticket text only when the relationship and scope are explicit.
- Draft updates from evidence only. Unsupported details become `NEEDS_INPUT`.
- Keep updates concise: state → evidence → explicit next action.
- For Excel output, preserve raw sheets and create/refresh one Morning View; fit print output to one page wide.
- Never claim a workbook or Jira ticket was edited unless the edit was actually performed and observed.

## Output order

1. Changed tickets
2. Conflicts / needs input
3. Jira-ready drafts
4. Morning View artifact or patch table
5. Validation summary
