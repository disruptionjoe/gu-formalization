#!/usr/bin/env python3
"""Pre-claim novelty check: grep the repo BEFORE asserting a result is new.

Motivation (measured, not hypothetical). In a single session on 2026-08-09, SEVEN
separate "new" findings turned out to be already recorded in this repository --
by the orchestrator and by subagents alike. Every one would have been caught by a
30-second grep. This tool is that grep, made mechanical.

Usage
-----
    python3 lab/process/novelty-check.py "term one" "term two" ...
    python3 lab/process/novelty-check.py --strict "C2/bare" "sqrt(7)"

Exit codes
----------
    0  no prior hits found  (claim MAY be new -- still your judgement)
    1  prior hits found     (claim is NOT new, or needs scoping against prior art)
    2  usage error

--strict makes hits fatal in a pipeline. Without it the exit code still reflects
hits; use it to be explicit about intent.

What it does NOT do: decide novelty. It surfaces prior art. A hit does not always
mean your claim is old -- it may be adjacent, or a homonym (this repo has at least
six same-letter collisions). Read the hits.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1].parent
SURFACES = ["explorations", "canon", "tests", "papers", "docs", "lab"]
MAX_PER_TERM = 12


def search(term: str) -> list[str]:
    cmd = ["grep", "-rn", "--include=*.md", "--include=*.py", "-F", term]
    cmd += [str(ROOT / s) for s in SURFACES if (ROOT / s).exists()]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=120).stdout
    except Exception as exc:  # pragma: no cover - defensive
        print(f"  ! search failed for {term!r}: {exc}", file=sys.stderr)
        return []
    lines = [ln for ln in out.splitlines() if ln.strip()]
    # never let this tool report itself as prior art
    return [ln for ln in lines if "novelty-check.py" not in ln]


def main(argv: list[str]) -> int:
    strict = "--strict" in argv
    terms = [a for a in argv if not a.startswith("--")]
    if not terms:
        print(__doc__)
        return 2

    total = 0
    for term in terms:
        hits = search(term)
        total += len(hits)
        print(f"\n=== {term!r}: {len(hits)} hit(s) ===")
        for ln in hits[:MAX_PER_TERM]:
            try:
                print("   ", str(Path(ln.split(':', 1)[0]).relative_to(ROOT)) + ":" + ln.split(':', 2)[1])
            except Exception:
                print("   ", ln[:160])
        if len(hits) > MAX_PER_TERM:
            print(f"    ... and {len(hits) - MAX_PER_TERM} more")

    print("\n" + "=" * 70)
    if total:
        print(f"PRIOR ART FOUND ({total} hits). Do NOT call this new without reading them.")
        print("If it is genuinely new, say what is new ABOUT it relative to these.")
        return 1
    print("No prior hits. Novelty is still your judgement -- terms may be phrased differently.")
    return 0 if not strict else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
