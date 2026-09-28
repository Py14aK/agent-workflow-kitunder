# ChatGPT Project / Work instructions

Use these instructions for a project that spans multiple chats or Work runs.

## Shared project behavior

- Inherit the compact global prompt.
- Keep each chat focused on one distinct outcome.
- Use project files/instructions for shared context; keep task-specific details in the current chat.
- When a recurring procedure appears, route it to a reusable skill rather than growing this file.
- Preserve source provenance and unresolved uncertainty.
- For long deliverables, finish with an inspectable artifact and state what was actually validated.

## Routing

- Mathematical/scientific verification → `research-rederive`
- Quant/portfolio/time-series analysis → `quant-research-lab`
- Banking/FSD/requirements work → `fa-requirement-verifier`
- Morning Jira snapshot / daily board → `snapshot-orchestrator`
- Publication/brief/HTML after verification → `research-publisher`

Do not automatically combine domains unless the user explicitly asks.
