# FA AI Academy: Copilot Workflows Starter Kit

As of 2026-10-07. Live, commentable version: https://claude.ai/code/artifact/0cfffdbf-198e-4e1a-8c9c-d1a23a9f8d3b

## Purpose

This kit teaches the team to run repeatable FA work (Jira routing, handovers, decision forms, FSD rewrites) through Microsoft 365 Copilot Chat on the free tier, with the same quality bar every time.

It borrows its thinking model from Anthropic Academy's free AI Fluency course and its prompt craft from Anthropic's prompting guidance, then applies both to the tools we actually have at work: Copilot Notebooks, Agent Builder agents and saved prompts.

How to use it: read sections 2 and 3 once (about 20 minutes), set up one workflow from section 4, then do one kata from section 5 each week. Section 6 is mandatory before anyone pastes work content into any AI tool.

## The 4D framework, applied to FA work

Anthropic Academy's AI Fluency course organises good AI use around four competencies: Delegation, Description, Discernment and Diligence ([course page](https://anthropic.skilljar.com/ai-fluency-framework-foundations/291895)).

| D | What it means | FA question to ask | Example in our work |
| --- | --- | --- | --- |
| Delegation | Decide what the AI does and what you keep | Is this drafting, sorting or summarising, or a judgement the bank holds me accountable for? | Copilot sorts the Jira snapshot into buckets; the FA decides what goes to the business |
| Description | Tell the AI the goal, context, format and constraints | Could a new colleague do this from my prompt alone? | State the output columns, the language, and what to do when data is missing |
| Discernment | Judge the output, the reasoning and the style | Can every row be traced back to the source I gave? | Spot-check 3 rows against the ticket; reject any invented ID or date |
| Diligence | Own the result and its use, ethically and safely | Am I allowed to put this content here, and am I signing off on it? | No customer data in prompts; the FA name goes on the handover, not "Copilot" |

The course splits Discernment into product, process and performance ([eWeek summary](https://www.eweek.com/news/anthropic-ai-fluency-course/)). For FA work, product and process matter most: a correct-looking table built from a misread ticket is the typical failure.

## Prompt anatomy for a workflow

1. Role and scope: who the assistant is and which inputs it may use.
2. Goal: one sentence on the result, not the activity.
3. Steps: numbered, each with a goal, an action and when to move on.
4. Rules: what never to do and what to do when data is missing.
5. Output contract: exact format, columns, language, maximum length.
6. Self-check: a short list the assistant verifies before answering.

```
BAD:  Summarise these Jira tickets for the standup.

GOOD: Using only the attached Jira export, list every ticket in a table:
| Key | Summary (max 12 words) | Status | Blocker? | Next action | Owner |
Sort blockers first. Mark anything not in the export as UNKNOWN.
Never invent ticket keys or dates. Answer in Bulgarian, keep Jira
statuses and T24 names in English. Before answering, check every
row traces to the export.
```

## Loading workflows in free Copilot Chat

| Container | Holds | Free-tier limit | Use it for |
| --- | --- | --- | --- |
| Copilot Notebook | Templates, decision log, source register | Up to 50 references, all used | Handover and FSD work over many files |
| Agent Builder agent (instructions only) | Core rules + one workflow family | 8,000 characters of instructions | Jira routing, actions, test cases |
| Saved prompt (Prompt Gallery) | Short launcher with [PLACEHOLDERS] | No documented limit; keep it short | One-click start, shared to the team |

Setup steps are in `../README.md`.

## Kata: one exercise per week

| # | Kata | Drill | Done when |
| --- | --- | --- | --- |
| 1 | Bad prompt makeover | Rebuild a one-line prompt with the six parts | Same table on two separate runs |
| 2 | Delegation map | Mark 10 weekly tasks AI, Me or Together | Every Me task has a reason |
| 3 | Trace test | Check 3 random output rows against the source | Source line found for each |
| 4 | Break it | Feed a snapshot with a missing field and a duplicate key | Agent asks or marks UNKNOWN |
| 5 | Two-tool check | Same prompt in Copilot and one other approved tool | One named difference, right one picked |
| 6 | Hand it on | A colleague runs your saved prompt unaided | Output matches in format and content |
| 7 | Shrink it | Cut agent instructions by 30% | Kata 3 and 4 still pass |

## Data hygiene rules

Confirm with Information Security; these are a starting point, not a policy.

- [ ] Work account, green shield (enterprise data protection) visible.
- [ ] No customer data: names, IBANs, account or CIF numbers, T24 record IDs, balances. Use [REDACTED].
- [ ] No real ticket keys, colleague names or internal hostnames in reusable prompts; use <TICKET_ID>.
- [ ] Web search off in work agents.
- [ ] Agents shared with named people only.
- [ ] Every output leaving the team has a named human owner who checked it.
- [ ] Temporary chat for one-off sensitive drafting.

## Learning path and sources

| Order | Course | Why for FA |
| --- | --- | --- |
| 1 | [AI Fluency: Framework & Foundations](https://anthropic.skilljar.com/ai-fluency-framework-foundations/291895) ([Coursera](https://coursera.org/learn/ai-fluency-framework-foundations)) | 4D model, tool-independent |
| 2 | Prompt Engineering Interactive Tutorial ([overview](https://aihub.msstate.edu/resources/anthropic-learning-resources.html)) | Prompt structure, examples, formatting |
| 3 | Other Anthropic Academy courses ([overview](https://www.i-programmer.info/news/105-artificial-intelligence/18735-anthropic-releases-free-courses-on-ai-.html)) | Optional, mostly Claude-specific |

Copilot setup: [agents in Copilot Chat](https://learn.microsoft.com/en-us/copilot/agents), [agent instructions](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/declarative-agent-instructions), [Notebook references](https://support.microsoft.com/en-us/microsoft-365-copilot/add-references-to-your-microsoft-365-copilot-notebook).
