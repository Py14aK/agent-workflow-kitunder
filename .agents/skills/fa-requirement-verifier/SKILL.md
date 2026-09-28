---
name: fa-requirement-verifier
description: Convert FSD/BRD, meetings, banking or risk evidence into atomic traceable requirements, gaps, acceptance criteria, and tests.
---

# FA requirement verifier

## Workflow

1. Inventory authoritative sources with version/date.
2. Extract atomic requirements: one obligation per requirement.
3. Preserve exact system names, fields, identifiers, statuses, and legacy conventions.
4. Classify each item as CONFIRMED, INFERRED, CONFLICTING, MISSING, or OUT-OF-SCOPE.
5. Represent business rules as precondition → event/input → required behavior → exception.
6. Produce acceptance criteria and at least happy-path, boundary, and negative/error tests where applicable.
7. Keep unresolved decisions visible and assign an owner if known.
8. Produce a concise handoff/Jira-ready summary.

Never upgrade an inferred rule to confirmed without evidence.
