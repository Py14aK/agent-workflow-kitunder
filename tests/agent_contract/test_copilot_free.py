from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
CF = ROOT / "copilot-free"
AGENT_LIMIT = 8000  # Agent Builder instructions limit (Copilot Studio quotas)
TICKET_KEY = re.compile(r"\b[A-Z]{2,10}-\d{3,}\b")

def test_agent_instructions_under_limit():
    for p in CF.glob("AGENT_*_INSTRUCTIONS.txt"):
        n = len(p.read_text(encoding="utf-8"))
        assert n < AGENT_LIMIT, f"{p.name}: {n} chars"

def test_no_real_ticket_keys_in_reusable_files():
    for p in CF.rglob("*"):
        if p.is_file() and p.suffix in {".txt", ".md"}:
            hits = TICKET_KEY.findall(p.read_text(encoding="utf-8"))
            assert not hits, f"{p.name}: {hits}"
