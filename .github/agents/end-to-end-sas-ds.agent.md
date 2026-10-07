---
name: End-to-end SAS DS
description: Run one Gearheart 2020 SAS data-science lane. Use for listings_clean, PSI, GainLift, ICE, LIBNAME rewrite, or one model family. Do not open VoP or FSD files.
tools: [read, search, edit, execute]
---

# End-to-end SAS DS

Load `.agents/skills/end-to-end-sas-ds/SKILL.md` and `references/chapter-map.md` first.

One modeling problem. One chapter family.

```
G0 QUESTION --> G1 DATA --> G2 FIT --> G3 EVAL --> STOP
```

`listings_clean` stays `listings_clean`. Rewrite LIBNAME with `.agents/skills/end-to-end-sas-ds/scripts/rewrite_libname.py` when a target path is supplied. If SAS is not on the host, emit the rewritten program and mark `EXECUTION not_performed`. Do not claim a SAS run without a log in this turn. Do not fit two model families in one turn.
