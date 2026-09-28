# Repository agent instructions

Keep this file small and repository-wide.

## Repository contract

- Reusable domain workflows live in `.agents/skills/`; do not duplicate them here.
- Preserve provenance for sources, data, and generated artifacts.
- Do not claim a command, test, notebook, rendering, or reproduction succeeded unless its output was actually observed.
- Keep durable project rules here; keep one-off requirements in the current task prompt.
- Surface conflicting evidence rather than silently choosing a convenient source.
- Use project documentation only when relevant to the current task; do not force broad pre-reading for every edit.

## Verification

For changes to agent instructions or skills:
1. Run `python -m pytest tests/agent_contract -q`.
2. Check skill names/descriptions still route clearly.
3. Confirm repository instructions remain compact.
4. Record any unverified behavior explicitly.

## Code Review Rules

- Flag duplicated global/project/skill instructions.
- Flag unsupported certainty or invented verification.
- Flag workflows that lose source/data provenance.
- Flag skill descriptions broad enough to trigger on unrelated tasks.
