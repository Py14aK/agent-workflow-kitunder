# Documentation basis

Checked 2026-09-28.

## Directly documented

1. **Global + project `AGENTS.md` layering**
   - OpenAI, *Custom instructions with AGENTS.md*
   - https://learn.chatgpt.com/docs/agent-configuration/agents-md
   - Documents global `~/.codex/AGENTS.md`, project/root-to-working-directory discovery, local precedence, and the 32 KiB default combined limit.

2. **Keep `AGENTS.md` small and project-focused**
   - OpenAI, *Customization*
   - https://learn.chatgpt.com/docs/customization/overview
   - Says `AGENTS.md` provides durable project guidance, should be kept small, and global files should shape personal behavior while repo files stay focused on team/codebase rules.

3. **Avoid bloated context**
   - OpenAI, *Rethinking skills and prompts for GPT-6 Astra* (2026-09-11)
   - https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
   - Explicitly recommends revisiting accumulated skills, `AGENTS.md`, and task prompts; warns against unnecessary pre-reading and overly broad/long skill descriptions.

4. **Skills are reusable workflows**
   - OpenAI, *Skills*
   - https://developers.openai.com/api/docs/guides/tools-skills
   - A skill is a directory with `SKILL.md`; name/description are exposed for discovery and full instructions load when selected.
   - OpenAI, *Build skills*
   - https://developers.openai.com/plugins/build/skills
   - Recommends focused skills for recognizable user goals and using skills for tool sequences, decision points, output requirements, examples, and templates.

5. **ChatGPT projects / Work share project instructions**
   - OpenAI, *Projects and chats*
   - https://learn.chatgpt.com/docs/projects
   - States project chats share project files, project instructions, and connected sources; recommends separate chats for distinct outcomes while retaining shared project context.

6. **Systematic skill evaluation**
   - OpenAI, *Testing Agent Skills Systematically with Evals*
   - https://developers.openai.com/blog/eval-skills
   - Recommends treating skills like prompts that should be evaluated for triggering, required steps, and regressions.

## Synthesized recommendations

The following are architecture choices inferred from the documented product model, not quoted OpenAI requirements:

- `SOURCE → NORMALIZE → CLAIMS → VERIFY → COMPUTE → ADVERSARIAL CHECK → SYNTHESIZE → ARTIFACT → FINAL QA`.
- Keeping Research / Investments / Work-FA as separate project contexts.
- The six-symbol epistemic legend.
- The exact four personal skills in this package.
- The routing matrix Global → Project → Skill → Task.
- Preserving the previous large prompt as a migration snapshot.

These are retained because they reduce instruction duplication, improve provenance, and match the user's recurring workflows.
