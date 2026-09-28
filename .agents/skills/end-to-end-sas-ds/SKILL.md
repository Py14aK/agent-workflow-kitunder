---
name: end-to-end-sas-ds
description: Run the Gearheart 2020 SAS data-science spine as one agent lane. Trigger on End-to-End Data Science with SAS, Gearheart, CH2 Get Data, PSI GainLift ICE, listings_clean, or install the SAS-DS skill.
metadata:
  type: workflow
  version: "2026-09-28"
  book: Gearheart 2020 SAS Institute
---

# End-to-end SAS DS

One modeling problem. One chapter family. Then evaluate. Do not open VoP or FSD folders.

## Cite

Gearheart, James. 2020. End-to-End Data Science with SAS. A Hands-On Programming Guide. Cary, NC. SAS Institute.
Paperback 978-1-64295-804-1. EPUB 978-1-64295-806-5.
Official code https://github.com/Gearhj/End-to-End-Data-Science
Mirror https://github.com/Wu-Yang-Monopole/End-to-End-Data-Science

Do not paste book paragraphs. Use the chapter spine and the public SAS files. Chapter map is in [references/chapter-map.md](references/chapter-map.md).

## Lanes

```
G0 QUESTION --> G1 DATA --> G2 FIT --> G3 EVAL --> STOP
```

G0 QUESTION
Book Ch.1–2 start. Business opportunity, initial questions, performance measure.
Out. one target name, one measure, train/test rule.

G1 DATA
Book Ch.2 get-data / target / predictors, Ch.3–5 coding and modeling data set.
Out. rewritten LIBNAME, train table, test table, target analysis note.
Ban. James Gearheart Windows paths left unchanged.

G2 FIT
Pick one family from [references/chapter-map.md](references/chapter-map.md).
Ban. fitting RF and SVM and NN in the same turn.

G3 EVAL
Book Ch.9 macros. Ban claiming a SAS run without a log in this turn.

STOP
Decision time. No Jira. No T24 field names.

## Hard rules

- Domain lock. quant/SAS-DS only.
- listings_clean stays listings_clean.
- Missing data file. Say NOT SUPPLIED.
- CH5_4 and CH6_1 are the same blob.
- If SAS is not on the host, emit the rewritten program and mark EXECUTION not_performed.
- Rewrite LIBNAME with [scripts/rewrite_libname.py](scripts/rewrite_libname.py) when a target path is supplied.
