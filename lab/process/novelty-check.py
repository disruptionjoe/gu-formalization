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


STOP = {
    "the","a","an","of","in","on","for","and","or","is","are","to","with","by","as","at","that",
    "this","it","its","be","not","no","from","was","were","has","have","had","which","if","then",
}


def _files(term_words: list[str]) -> dict[str, set[str]]:
    """Map file -> set of query words found in it. Word-level, so paraphrase survives."""
    hits: dict[str, set[str]] = {}
    for w in term_words:
        cmd = ["grep", "-rlni", "--include=*.md", "--include=*.py", "-F", w]
        cmd += [str(ROOT / s) for s in SURFACES if (ROOT / s).exists()]
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, timeout=180).stdout
        except Exception:
            continue
        for f in out.splitlines():
            if not f.strip() or "novelty-check.py" in f:
                continue
            hits.setdefault(f, set()).add(w)
    return hits


def search(term: str) -> tuple[list[str], list[str]]:
    """Return (exact_phrase_hits, cooccurrence_hits).

    Exact-substring matching alone is NOT sufficient: on 2026-08-09 this tool
    returned 0 hits for "totally isotropic chirality halves" while the repo
    contained "both omega-halves totally isotropic" -- a paraphrase. The
    co-occurrence pass exists because of that failure.
    """
    exact_cmd = ["grep", "-rn", "--include=*.md", "--include=*.py", "-Fi", term]
    exact_cmd += [str(ROOT / s) for s in SURFACES if (ROOT / s).exists()]
    try:
        exact = [ln for ln in subprocess.run(exact_cmd, capture_output=True, text=True,
                                             timeout=180).stdout.splitlines()
                 if ln.strip() and "novelty-check.py" not in ln]
    except Exception:
        exact = []

    words = [w for w in "".join(c if c.isalnum() or c in "_-." else " " for c in term).split()
             if len(w) > 2 and w.lower() not in STOP]
    co: list[str] = []
    if len(words) >= 2:
        fmap = _files(words)
        need = max(2, (len(words) + 1) // 2)   # at least half the significant words
        ranked = sorted(((len(v), k) for k, v in fmap.items() if len(v) >= need), reverse=True)
        co = [f"{n}/{len(words)} words :: {k}" for n, k in ranked]
    return exact, co


def main(argv: list[str]) -> int:
    strict = "--strict" in argv
    terms = [a for a in argv if not a.startswith("--")]
    if not terms:
        print(__doc__)
        return 2

    total = 0
    for term in terms:
        exact, co = search(term)
        total += len(exact) + len(co)
        print(f"\n=== {term!r}: {len(exact)} exact, {len(co)} co-occurrence ===")
        for ln in exact[:MAX_PER_TERM]:
            try:
                print("  EXACT ", str(Path(ln.split(':', 1)[0]).relative_to(ROOT)) + ":" + ln.split(':', 2)[1])
            except Exception:
                print("  EXACT ", ln[:160])
        for ln in co[:MAX_PER_TERM]:
            n, f = ln.split(" :: ", 1)
            try:
                print(f"  NEAR  [{n}] " + str(Path(f).relative_to(ROOT)))
            except Exception:
                print(f"  NEAR  [{n}] " + f[:140])
        if len(exact) + len(co) > 2 * MAX_PER_TERM:
            print("    ... truncated")

    print("\n" + "=" * 70)
    if total:
        print(f"PRIOR ART FOUND ({total} hits). Do NOT call this new without reading them.")
        print("If it is genuinely new, say what is new ABOUT it relative to these.")
        return 1
    print("No prior hits. Novelty is still your judgement -- terms may be phrased differently.")
    return 0 if not strict else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
