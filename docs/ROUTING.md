# Instruction routing matrix

| Put it here | Use for | Do not put here |
|---|---|---|
| Global prompt | Cross-domain response, evidence, execution, context-hygiene rules | Portfolio snapshots, paper-specific notation, FSD details, weekly briefing formats |
| `AGENTS.md` | Rules that should apply whenever Codex works in this repository | Detailed multi-step domain workflows |
| Skill | Repeatable recognizable workflows with steps, references, scripts, templates | One-off task details |
| ChatGPT Project / Work instructions | Shared context and rules across chats in one project | Global preferences unrelated to the project |
| Current task prompt | Immediate goal, inputs, constraints, required output | Durable rules already represented elsewhere |

## Practical rule

Global = stable behavior.
Project = stable local context.
Skill = repeatable process.
Task prompt = this run only.
