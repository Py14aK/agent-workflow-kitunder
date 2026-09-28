#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import yaml
LANES = ("L0_SNAPSHOT", "L1_ATOM", "L2_EVIDENCE", "L3_DRAFT", "STOP")

def lane_for(ticket: dict) -> str:
    actions = " ".join(ticket.get("required_actions") or [])
    blockers = ticket.get("blockers") or []
    if ticket.get("owner_conflict"):
        return "L0_SNAPSHOT"
    if ticket.get("clone_of") and "Confirm" in actions:
        return "L1_ATOM"
    if "CDTR.AGT.NM.1" in actions or "field-presence" in actions:
        return "L2_EVIDENCE"
    if blockers:
        return "L2_EVIDENCE"
    if ticket.get("phase") == "FSD":
        return "L1_ATOM"
    return "L3_DRAFT"

def next_lane(current: str) -> str:
    idx = LANES.index(current)
    return LANES[min(idx + 1, len(LANES) - 1)]

def prompt_for(ticket: dict, current: str) -> str:
    return (
        f"MODE: /DO\nLANE: {current}\nNEXT_LANE: {next_lane(current)}\n"
        f"TSC: {ticket['key']}\nCLONE_OF: {ticket.get('clone_of') or 'none'}\n"
        f"TITLE: {ticket.get('title')}\n"
        f"DO: emit only the {current} artefact. Do not post Jira. Do not open a second key.\n"
    )

def render(data: dict) -> str:
    lines = [f"# Desk lanes {data.get('date', '')}", "", "```mermaid", "flowchart LR",
             "    L0[L0 SNAPSHOT] --> L1[L1 ATOM]", "    L1 --> L2[L2 EVIDENCE]",
             "    L2 --> L3[L3 DRAFT]", "    L3 --> S[STOP]", "```", "",
             "| Key | Lane | Next | Clone of |", "|---|---|---|---|"]
    blocks = []
    for t in data["tickets"]:
        current = lane_for(t)
        lines.append(f"| {t['key']} | {current} | {next_lane(current)} | {t.get('clone_of') or '—'} |")
        blocks.append(prompt_for(t, current))
    lines.extend(["", "## Agent prompts", ""])
    for block in blocks:
        lines.extend(["```", block.rstrip(), "```", ""])
    lines.append("JIRA_WRITE not_performed\n")
    return "\n".join(lines)

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("snapshot", type=Path)
    p.add_argument("-o", "--output", type=Path)
    args = p.parse_args()
    data = yaml.safe_load(args.snapshot.read_text(encoding="utf-8"))
    out = args.output or Path("desk_lanes_board.md")
    out.write_text(render(data), encoding="utf-8")
    print(f"WROTE {out}")
    print(f"TICKETS {len(data['tickets'])}")

if __name__ == "__main__":
    main()
