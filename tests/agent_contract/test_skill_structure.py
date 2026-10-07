from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / ".agents" / "skills"
EXPECTED = {
    "research-rederive",
    "quant-research-lab",
    "fa-requirement-verifier",
    "fa-daily-control-tower",
    "research-publisher",
    "snapshot-orchestrator",
    "desk-lanes",
    "end-to-end-sas-ds",
}

def test_expected_skills_exist():
    assert EXPECTED <= {p.name for p in SKILLS.iterdir() if p.is_dir()}

def test_skill_frontmatter_and_names():
    for name in EXPECTED:
        path = SKILLS / name / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        assert text.startswith("---\n")
        assert f"name: {name}" in text
        assert "description:" in text
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)

def test_agents_md_remains_compact():
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert len(text.encode("utf-8")) < 12000
