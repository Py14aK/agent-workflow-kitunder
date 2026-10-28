#!/usr/bin/env bash
# install.sh  (agent-skills-kit, 2026-10-28)
# Copies ./skills into a folder GitHub Copilot (VS Code), Kilo Code and Codex all read.
#   bash install.sh                    personal: ~/.agents/skills
#   bash install.sh --project PATH     one repository: PATH/.agents/skills
#   --force    replace existing copies (old copy moved to .backup_<ts>)
#   --dry-run  preview only
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; SRC="$HERE/skills"
DEST="$HOME/.agents/skills"; FORCE=0; DRY=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --project) [[ -d "${2:-}" ]] || { echo "project folder not found: ${2:-}" >&2; exit 1; }; DEST="$2/.agents/skills"; shift 2 ;;
    --force) FORCE=1; shift ;; --dry-run) DRY=1; shift ;;
    *) echo "unknown option $1" >&2; exit 2 ;;
  esac
done
[[ -d "$SRC" ]] || { echo "cannot find $SRC" >&2; exit 1; }
TS="$(date +%Y%m%d_%H%M%S)"; ok=0; skip=0
[[ $DRY -eq 0 ]] && mkdir -p "$DEST"
for d in "$SRC"/*/; do
  n="$(basename "$d")"; t="$DEST/$n"
  if [[ -e "$t" ]]; then
    if [[ $FORCE -eq 0 ]]; then echo "skip     $n (already there)"; skip=$((skip+1)); continue; fi
    [[ $DRY -eq 0 ]] && mkdir -p "$DEST/.backup_$TS" && mv "$t" "$DEST/.backup_$TS/"
  fi
  echo "install  $n"; [[ $DRY -eq 0 ]] && cp -r "$d" "$t"; ok=$((ok+1))
done
echo; echo "Done: $ok installed, $skip skipped -> $DEST (dry-run=$DRY)"
echo "Reload VS Code. In Copilot Chat use Agent mode; type / to see skills."
