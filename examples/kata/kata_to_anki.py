"""Export Tier 2 kata from KATA.md to an Anki-importable CSV.
Front: trigger. Back: move + why.
Usage: python kata_to_anki.py [KATA.md] [out.csv]
"""
import csv, sys, re
from pathlib import Path

def parse_tier2(text: str):
    m = re.search(r"^## Tier 2\s*$(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        raise ValueError("No '## Tier 2' section found")
    cards = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        parts = [p.strip() for p in line[2:].split("->")]
        if len(parts) != 3:
            print(f"skip (need trigger -> move -> why): {line[:60]}", file=sys.stderr)
            continue
        trigger, move, why = parts
        cards.append((trigger, f"{move}<br><br><i>Why:</i> {why}"))
    return cards

def main():
    src = Path(sys.argv[1] if len(sys.argv) > 1 else "KATA.md")
    out = Path(sys.argv[2] if len(sys.argv) > 2 else "kata_tier2_anki.csv")
    cards = parse_tier2(src.read_text(encoding="utf-8"))
    with out.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(cards)
    print(f"{len(cards)} cards -> {out}")

if __name__ == "__main__":
    main()
