---
name: adhd-runbook
description: Turn a repeating job into a short runbook. Trigger on runbook, how we do this, incident steps, or checklist. One procedure, checkbox steps, then stop.
---

# ADHD runbook

One procedure. Checkbox steps. A human can run it on a bad day.

## State line, print first

NOW:
DONE:
NEXT:
BLOCKED:

## Steps

1. Name the job in one line. Name the trigger that starts it.
2. List inputs. Missing input is NOT SUPPLIED, not a guess.
3. Write 5 to 9 steps. Each step is one verb, one object, one done-check.
4. Put a stop rule on any step that can branch. One branch only.
5. End with rollback: what to undo, who to tell, what evidence to keep.
6. Print the state line. NEXT is the first unchecked step, or STOP.

## Step shape

- [ ] Verb object. Done when: observable check.

## Do not

- Do not write background prose.
- Do not merge two jobs.
- Do not hide a decision inside a step. Decisions are a separate checkbox with an owner.
