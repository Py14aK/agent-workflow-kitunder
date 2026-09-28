#!/usr/bin/env python3
"""Build a morning execution board from a YAML snapshot. Does not call Jira."""
from __future__ import annotations
import argparse
from datetime import date
from pathlib import Path
import yaml

def load_snapshot(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "tickets" not in data:
        raise ValueError("snapshot must contain tickets")
    return data

def draft_comment(ticket: dict) -> str:
    clone = ticket.get("clone_of") or "none"
    owner = ticket.get("owner") or ticket.get("owner_copilot") or "UNRESOLVED"
    if ticket.get("owner_conflict"):
        owner = (
            f"CONFLICT workbook={ticket.get('owner_workbook')} "
            f"copilot={ticket.get('owner_copilot')}"
        )
    actions = ticket.get("required_actions") or []
    blockers = ticket.get("blockers") or []
    lines = [
        f"{ticket['key']}",
        f"Status. {ticket.get('status', 'UNKNOWN')}",
        f"Owner. {owner}",
        f"Clone of. {clone}",
        "Confirmed next action.",
    ]
    lines.extend(f"- {item}" for item in actions)
    if blockers:
        lines.append("Blocker from snapshot.")
        lines.extend(f"- {item}" for item in blockers)
    lines.append("Evidence still missing.")
    lines.append("- Live Jira page not opened in this run.")
    lines.append("Do not.")
    lines.append("- Treat this block as posted.")
    if clone != "none":
        lines.append(f"- Duplicate parent tests from {clone} on this clone.")
    return "\n".join(lines)

def render_board(data: dict) -> str:
    day = data.get("date") or date.today().isoformat()
    tickets = data["tickets"]
    risk_a = [t["key"] for t in tickets if t.get("risk") == "A"]
    lines = [
        f"# Morning board {day}",
        "",
        f"Operator. {data.get('operator', 'unspecified')}",
        "Mode. WORK/FA + ANALYSIS",
        "Jira write. NOT PERFORMED",
        "",
        "## Sources",
        "",
    ]
    for src in data.get("sources", []):
        lines.append(
            f"- `{src['id']}` {src.get('medium')} `{src.get('path', src.get('note', ''))}`"
        )
    lines.extend(["", "## Board", ""])
    lines.append("| Key | Phase | Status | Clone of | Risk | Route |")
    lines.append("|---|---|---|---|---|---|")
    for t in tickets:
        lines.append(
            f"| {t['key']} | {t.get('phase', '')} | {t.get('status', '')} | "
            f"{t.get('clone_of') or '—'} | {t.get('risk', '')} | {t.get('route', '')} |"
        )
    lines.extend(["", "## Clone map", "", "```mermaid", "flowchart TD"])
    for t in tickets:
        parent = t.get("clone_of")
        if parent:
            lines.append(f"    {parent} --> {t['key']}")
        else:
            lines.append(f"    {t['key']}")
    lines.extend(["```", "", "## Conflicts", ""])
    for c in data.get("conflicts") or ["none recorded"]:
        if isinstance(c, str):
            lines.append(f"- {c}")
        else:
            lines.append(
                f"- `{c['id']}` {'/'.join(c.get('keys', []))} {c.get('statement')}"
            )
    lines.extend(["", "## Risk A", ""])
    lines.extend(f"- {key}" for key in risk_a)
    lines.extend(["", "## Draft comments. NOT POSTED", ""])
    for t in tickets:
        lines.append("```")
        lines.append(draft_comment(t))
        lines.append("```")
        lines.append("")
    lines.extend([
        "## Checkpoints",
        "",
        "- T+00 Inventory of keys and sources.",
        "- T+20 Completeness. Every NEW clone has a parent.",
        "- T+40 Trace. CDTR.AGT.NM.1 and R26_INC19789557 kept exact.",
        "- T+60 Output. Board and drafts written. Jira untouched.",
        "",
        "## Unverified",
        "",
    ])
    for item in data.get("unverified", []):
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    data = load_snapshot(args.snapshot)
    text = render_board(data)
    out = args.output or Path(f"morning_board_{data.get('date', date.today().isoformat())}.md")
    out.write_text(text, encoding="utf-8")
    print(f"WROTE {out}")
    print(f"TICKETS {len(data['tickets'])}")
    print("JIRA_WRITE not_performed")

if __name__ == "__main__":
    main()
