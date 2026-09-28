# Installation map

## ChatGPT / current chat
Use `prompt` as the compact cross-domain instruction set. This package cannot directly rewrite account-level ChatGPT instructions from the current tool surface.

## ChatGPT Project / Work
Paste `chatgpt-work/PROJECT_INSTRUCTIONS.md` into the relevant project's instructions. Keep domain-specific project state in project files, not in the global prompt.

## Codex global
Copy `codex/GLOBAL_AGENTS.md` to:

`~/.codex/AGENTS.md`

Then verify with:

`codex --ask-for-approval never "Summarize the current instructions."`

## Codex repository
Copy:
- `AGENTS.md`
- `.agents/skills/`
- `tests/agent_contract/`
- `.github/workflows/agent-contract.yml`

into the repository.

## Existing large prompt
Before replacing the existing `prompt`, save it under a legacy filename or rely on Git history. Do not silently destroy it.

## GitHub connector limitation observed
The current connector could read `Py14aK/cute-heliotrope-120103` but branch creation returned HTTP 403, so this package was not remotely committed.
