# Agent Skills Kit

70 ready-to-use skills for AI coding assistants: maths and statistics, scientific Python, data and BigQuery, research and review, testing and debugging. Each skill is a folder with a `SKILL.md` that tells the assistant when and how to do one kind of task. The assistant loads a skill only when a request matches it.

Works with:

| Tool | Reads skills from |
|---|---|
| GitHub Copilot in VS Code (Agent mode), Copilot CLI | `.agents/skills/` in a repo, or `~/.agents/skills/` |
| Kilo Code | same folders |
| OpenAI Codex | same folders |
| Claude Code | `~/.claude/skills/` (copy the folders there) |

Not supported: Microsoft 365 Copilot Chat (the free web chat). It cannot load skill files.

This folder is a distribution kit, not active skills for this repository. The skills live in `skills-kit/skills/`, which no tool scans automatically, so they do not mix with the repository's own routed skills in `.agents/skills/`. Install them into your personal folder with the scripts below.

## Install

Run the commands from inside the `skills-kit` folder.

Windows (PowerShell), for all your projects:

```
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

For one other repository only (not this one, which routes its own small skill set):

```
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Project C:\path\to\repo
```

macOS / Linux:

```
bash install.sh
bash install.sh --project /path/to/repo
```

Add `-WhatIf` (PowerShell) or `--dry-run` (bash) to preview. Existing skills are never overwritten unless you add `-Force` / `--force`, and then the old copy is kept in a `.backup_<date>` folder.

Then reload VS Code, open Copilot Chat in **Agent** mode, and type `/` to see the skills. You can also just ask normally; Copilot picks a matching skill by its description.

## What is inside

See `skills_index_2026-10-28.csv` for every skill with its source, license, file count, and whether it contains scripts.

| Area | Skills |
|---|---|
| Maths and proofs | mathematician, math-olympiad, siege, solo, sympy |
| Statistics and forecasting | statistician, statsmodels, statistical-power, pymc, timesfm-forecasting, uncertainty-and-units, experimental-design |
| Data and ML | polars, dask, scikit-learn, shap, networkx, exploratory-data-analysis, scientific-visualization, jupyter-notebook, huggingface-datasets, hf-cli |
| Optimisation and simulation | pymoo, simpy |
| Physics and quantum | astropy, qutip, qiskit, pennylane |
| Google Cloud and Gemini | bigquery-basics, bigquery-optimization, bigquery-bigframes, bigquery-ai-ml, gcloud, google-cloud-storage-basics, gemini-api, gemini-interactions-api, developing-genkit-python, finding-google-skills, retrieving-developer-knowledge |
| Research and review | literature-review, paper-lookup, huggingface-papers, citation-management, peer-review, hypothesis-generation, scientific-brainstorming, scientific-critical-thinking, researcher, devils-advocate, fact-checker, consistency-auditor, edge-case-analyst, completion-verifier, economist |
| Engineering practice | brainstorming, writing-plans, test-driven-development, systematic-debugging, verification-before-completion, define-goal, playwright, webapp-testing, gh-fix-ci, security-threat-model, mcp-builder |
| AI and API building | claude-api, session-report, discernment-nudge |
| Documents and visuals | canvas-design, theme-factory |

## Before you rely on a skill

- 30 skills include scripts (Python, shell or JavaScript). The assistant may run them. Read a skill's scripts before first use, as you would any dependency.
- Some skills call outside services (Google Cloud, Gemini, Hugging Face, GitHub). They need your own account and credentials, and they are subject to your organisation's rules on sending data outside.
- Do not paste client data, account numbers or internal documents into a request just because a skill can process them. Apply the same data rules you apply to the assistant itself.

## On hold: `_license-review/`

`physlibsearch` and `doc-coauthoring` were published without a license file. They are kept apart and are not installed by the scripts. Ask whoever approves software at your organisation before using them.

## Sources and licenses

Copied unchanged from public repositories, except where `skills_index_2026-10-28.csv` lists a change (one description shortened to fit the 1024-character limit). Each skill keeps its original license file where the source had one.

| Source | License |
|---|---|
| github.com/anthropics/skills | Apache-2.0 |
| github.com/anthropics/claude-plugins-official | Apache-2.0 |
| github.com/google/skills | Apache-2.0 |
| github.com/huggingface/skills | Apache-2.0 |
| github.com/openai/skills | Apache-2.0 |
| github.com/K-Dense-AI/claude-scientific-skills | MIT |
| github.com/obra/superpowers | MIT |
| github.com/dangeles/claude | MIT (stated in its README) |
| github.com/Kernel-Science/physlibsearch-skill | none found (on hold) |
