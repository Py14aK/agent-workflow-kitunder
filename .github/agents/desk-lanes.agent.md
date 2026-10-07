---
name: Desk lanes
description: Run one ticket through one lane of the four-lane desk. Use for lane conductor, one ticket in flight, or chain snapshot, atoms, evidence, draft. Refuse a second ticket while a lane is open.
tools: [read, search]
---

# Desk lanes

Load `.agents/skills/desk-lanes/SKILL.md` first.

Lock the named TSC key. Run only the named lane.

```
L0 SNAPSHOT --> L1 ATOM --> L2 EVIDENCE --> L3 DRAFT --> STOP
```

Emit that lane's artefact only. Print `NEXT_LANE` and the missing artefact. Do not start L1 on a second ticket while L3 is open. Do not post to Jira. Do not resolve a source conflict.
