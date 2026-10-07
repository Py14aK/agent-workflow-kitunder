# copilot-free

Loadable FA workflows for free Microsoft 365 Copilot Chat (Entra work account, no Copilot licence).

## Layout
- `CORE_RULES_BLOCK.txt` paste into Notebook Instructions; also embedded in every agent.
- `AGENT_FA_JIRA_INSTRUCTIONS.txt` Agent Builder instructions (must stay under 8,000 characters; checked in CI).
- `CONVERSATION_STARTERS.md` agent starters + saved-prompt launcher.
- `academy/` team training kit (4D framework, prompt anatomy, kata, data hygiene).

## Load (about 30 min)
1. m365.cloud.microsoft > Notebooks > new notebook. Upload templates (.md/.txt/.docx) from device. No .zip or .svg.
2. Notebook > Instructions > paste `CORE_RULES_BLOCK.txt`.
3. New agent > Configure > paste `AGENT_FA_JIRA_INSTRUCTIONS.txt`. Knowledge empty. Web search off. Add starters.
4. Test with sanitised sample; share with named colleagues only.
5. Save the launcher in Prompt Gallery; share to the team.

## Why this split
Free tier: instructions-only agents are free; file/SharePoint knowledge needs a licence or metered billing.
Directive text placed in knowledge files may be sanitised at runtime (Microsoft Learn, declarative agent instructions).
Notebook instructions are reported as unreliable, so restate critical rules in the launcher.

## Planned
FA-Handover and FA-FSD agents, same pattern, one 8K budget each.
