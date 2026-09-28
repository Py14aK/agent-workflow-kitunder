# Migration from the existing large prompt

1. Preserve the existing repository `prompt` file as a legacy snapshot before replacement.
2. Replace the active `prompt` with the compact version in this package.
3. Copy `codex/GLOBAL_AGENTS.md` to `~/.codex/AGENTS.md` for Codex global guidance.
4. Keep repository-specific guidance in root or nested `AGENTS.md`.
5. Install/copy the four skill directories where Codex/ChatGPT project skill discovery can see them.
6. Paste `chatgpt-work/PROJECT_INSTRUCTIONS.md` into the relevant ChatGPT Project/Work project instructions.
7. Move domain-specific material out of the old main prompt:
   - physics/gravity/paper procedures → research skill/project docs
   - portfolio horizons/current positions → Investment project state
   - FA/FSD rules → FA project/skill
   - Friday/newsletter formatting → publisher skill/project instructions
   - Sudoku-specific constraints → Sudoku project instructions
8. Validate positive and negative routing examples.
9. Keep the old prompt until the new setup has been used successfully on representative tasks.

## GitHub status for this migration

A write attempt to create a review branch on `Py14aK/cute-heliotrope-120103` was rejected by the current GitHub integration with HTTP 403 (`Resource not accessible by integration`). No remote file was modified.
