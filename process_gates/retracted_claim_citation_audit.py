#!/usr/bin/env python3
"""No canon/ or docs/ file may cite a RETRACTED claim as live.

Motivation (2026-08-08..10): retracted phrasings kept resurfacing as live text -- the retracted
"source-typed arithmetic" settlement rationale was found inside a canon file's controlling banner,
and the "non-convex" pi_! diagnosis propagated into two canon files and a spec. A phrase hit is
EXEMPT when retraction-context markers appear within a +/-6 line window (documenting a retraction
is fine; citing it as live is not). Hits known-open at seeding (2026-08-10 sweep) are REPORTED as
NEEDS_RECHECK without failing; NEW hits fail. Baseline-tolerant, regression-blocking.
"""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SURFACES = ("canon", "docs")
WINDOW = 6

MARKERS = (
    "retract", "retired", "correction", "superseded", "refuted", "dispute",
    "do not cite", "wrong diagnosis", "~~", "amendment", "scoped", "corrected",
)

# (phrase, retraction id, {known-open relative paths})
RETRACTED = [
    ("is non-convex", "SD-01", {"canon/no-go-class-relative-map.md"}),
    ("fibre is non-convex", "SD-01", {"canon/no-go-class-relative-map.md"}),
    ("domain is UNIQUE and FORCED", "C1-REFUTATION-2026-08-08", set()),
    ("count = 3 iff import the prime 3", "MULTIPLICITY-SUPERSEDED", set()),
    ("from source-typed arithmetic", "REAL-CLIFFORD-FORM-RATIONALE-2026-08-08",
     {"canon/no-go-quaternionic-parity-generation-sector.md"}),
    ("integer content is 24", "24ROOT2-RETRACTION-2026-08-09", set()),
]


def hits(path: Path) -> list[tuple[str, str, int, bool]]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    lowered = [ln.lower() for ln in lines]
    out = []
    for phrase, rid, _known in RETRACTED:
        needle = phrase.lower()
        for i, ln in enumerate(lowered):
            if needle in ln:
                lo, hi = max(0, i - WINDOW), min(len(lowered), i + WINDOW + 1)
                exempt = any(m in lowered[j] for j in range(lo, hi) for m in MARKERS)
                out.append((phrase, rid, i + 1, exempt))
    return out


class RetractedClaimCitationAudit(unittest.TestCase):
    def test_no_new_live_citations_of_retracted_claims(self) -> None:
        new_bad: list[str] = []
        known_report: list[str] = []
        for surface in SURFACES:
            for path in sorted((ROOT / surface).glob("*.md")):
                rel = str(path.relative_to(ROOT))
                for phrase, rid, lineno, exempt in hits(path):
                    if exempt:
                        continue
                    known = rel in next(k for p, r, k in RETRACTED if p == phrase and r == rid)
                    line = f"{rel}:{lineno} cites retracted [{rid}] as live: '{phrase}'"
                    (known_report if known else new_bad).append(line)
        for line in known_report:
            print(f"NEEDS_RECHECK (known at seeding 2026-08-10): {line}")
        self.assertEqual(
            new_bad, [],
            "NEW live citation of a retracted claim (add retraction context or remove):\n" + "\n".join(new_bad),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
