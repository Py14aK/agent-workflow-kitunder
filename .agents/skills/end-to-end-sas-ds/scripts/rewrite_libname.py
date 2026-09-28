#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
OLD_LIB = "C:/Users/James Gearheart/Desktop/SAS Book Stuff/Data"
OLD_FILE = r"C:\Users\James Gearheart\Desktop\SAS Book Stuff\Data\listings_clean.csv"

def rewrite(text: str, target: str) -> str:
    target = target.rstrip("\\/")
    posix = target.replace("\\", "/")
    win = target.replace("/", "\\")
    out = text.replace(OLD_LIB, posix)
    out = out.replace(OLD_FILE, f"{win}\\listings_clean.csv")
    return out

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("sas_file", type=Path)
    p.add_argument("--target", required=True)
    p.add_argument("-o", "--output", type=Path)
    args = p.parse_args()
    text = args.sas_file.read_text(encoding="utf-8", errors="replace")
    new = rewrite(text, args.target)
    out = args.output or args.sas_file.with_name(args.sas_file.stem + "_rewritten.sas")
    out.write_text(new, encoding="utf-8")
    print(f"WROTE {out}")
    print(f"PATH_REWRITE {new != text}")

if __name__ == "__main__":
    main()
