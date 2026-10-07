# Conversation starters (FA-Jira agent)

1. WF1 Daily routing: `WF1: Route today's Jira snapshot (attached). LANG=BG`
2. WF2 Extract actions: `WF2: Extract actions and owners from the attached ticket comments.`
3. WF3 Test cases: `WF3: Draft test cases for the ticket text I paste next.`
4. Standup digest: `WF1 then WF2 on the attached export; end with 5 talking points.`

# Saved prompt launcher (Notebook, Prompt Gallery)

```
Using only the references in this notebook and the file I attach, run [WORKFLOW].
Rules: no invented IDs, unknowns as UNKNOWN, customer data as [REDACTED], LANG=[BG|EN].
Output: [TEMPLATE NAME] format exactly.
```
