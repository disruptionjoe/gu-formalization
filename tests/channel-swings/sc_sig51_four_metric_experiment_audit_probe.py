#!/usr/bin/env python3
"""Exact certificate for SC-SIG-51's normalized four-form enumeration.

The certificate intentionally does not simulate an experiment.  It proves the
four inertia rows and checks that the owner artifact preserves the missing-
selector ceiling.  Hostile mutations must fail after the clean baseline passes.
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "explorations/sc-sig51-four-metric-experiment-audit-2026-08-24.md"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
TRANSCRIPT = ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md"


def inertia(eps_tf: int, eps_trace: int) -> tuple[int, int]:
    """Trace line is (1,0); traceless Frobenius block is (6,3)."""
    tf = (6, 3) if eps_tf == 1 else (3, 6)
    tr = (1, 0) if eps_trace == 1 else (0, 1)
    return tf[0] + tr[0], tf[1] + tr[1]


def trace_norm(lam_num: int, lam_den: int = 1) -> tuple[int, int]:
    """Return the exact numerator/denominator of 4-16 lambda."""
    return 4 * lam_den - 16 * lam_num, lam_den


def maximal_compact_dimension(p: int, q: int) -> int:
    return p * (p - 1) // 2 + q * (q - 1) // 2


BASE = {
    "pairs": [(1, 1), (1, -1), (-1, 1), (-1, -1)],
    "expected": [(7, 3), (6, 4), (4, 6), (3, 7)],
    "enumeration_grade": "ADHERED / exact",
    "selector_grade": "SOURCE-UNDERDEFINED",
    "imports_selector": False,
}


def evaluate(spec: dict) -> list[tuple[str, bool]]:
    rows = [inertia(*pair) for pair in spec["pairs"]]
    return [
        ("four ordered normalized sign pairs", len(spec["pairs"]) == 4),
        ("sign pairs are unique", len(set(spec["pairs"])) == 4),
        ("all coefficients are plus or minus one", all(abs(x) == 1 for p in spec["pairs"] for x in p)),
        ("four expected inertia rows", rows == spec["expected"]),
        ("all forms remain rank ten", all(p + q == 10 for p, q in rows)),
        ("all four inertia rows are distinct", len(set(rows)) == 4),
        ("raw Frobenius row is (7,3)", inertia(1, 1) == (7, 3)),
        ("trace reversal row is (6,4)", inertia(1, -1) == (6, 4)),
        ("negative trace reversal row is (4,6)", inertia(-1, 1) == (4, 6)),
        ("negative Frobenius row is (3,7)", inertia(-1, -1) == (3, 7)),
        ("continuous family degenerates at lambda one quarter", trace_norm(1, 4)[0] == 0),
        ("native lambda one half has trace norm minus four", trace_norm(1, 2) == (-8, 2)),
        ("lambda one fixture has trace norm minus twelve", trace_norm(1, 1) == (-12, 1)),
        ("(6,4) maximal compact has dimension 21", maximal_compact_dimension(6, 4) == 21),
        ("(7,3) maximal compact has dimension 24", maximal_compact_dimension(7, 3) == 24),
        ("enumeration is graded exact", spec["enumeration_grade"] == "ADHERED / exact"),
        ("selector remains source-underdefined", spec["selector_grade"] == "SOURCE-UNDERDEFINED"),
        ("no conventional selector is imported", spec["imports_selector"] is False),
    ]


def repository_checks() -> list[tuple[str, bool]]:
    artifact = ARTIFACT.read_text(encoding="utf-8")
    flat_artifact = " ".join(artifact.split())
    register = REGISTER.read_text(encoding="utf-8")
    transcript = TRANSCRIPT.read_text(encoding="utf-8")
    return [
        ("source sentence is in primary transcript", "there are precisely four metrics you can define" in transcript),
        ("trace-reversed survivor sentence is in transcript", "The trace reversed ones remain in the game" in transcript),
        ("artifact cites the banked July result", "source-wave-observer-view-adjudication-2026-07-20.md" in artifact),
        ("artifact carries routing boundary", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in artifact),
        ("artifact forbids imported selector", "no imported experimental selector" in artifact.lower()),
        ("artifact freezes next wake", "admitted GU action/domain" in artifact),
        ("Pati-Salam criterion is not called experiment", "authorial structural criterion, not an experiment" in flat_artifact),
        ("SC-SIG-51 is PARTIAL", "- id: SC-SIG-51" in register and "adherence: PARTIAL" in register.split("- id: SC-SIG-51", 1)[1].split("- id: SC-SIG-52", 1)[0]),
    ]


def main() -> int:
    checks = evaluate(BASE) + repository_checks()
    failures = [label for label, ok in checks if not ok]
    print(f"SC-SIG-51 clean certificate: {len(checks) - len(failures)}/{len(checks)}")
    for label, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if failures:
        return 1

    mutations = []
    for label, expected_failure, change in (
        ("drop one normalized form", "four ordered normalized sign pairs", lambda s: s["pairs"].pop()),
        ("duplicate one sign pair", "sign pairs are unique", lambda s: s["pairs"].__setitem__(3, (1, 1))),
        ("swap a trace-reversal inertia", "four expected inertia rows", lambda s: s["expected"].__setitem__(1, (7, 3))),
        ("promote the selector", "selector remains source-underdefined", lambda s: s.__setitem__("selector_grade", "ADHERED / exact")),
        ("import a comparator selector", "no conventional selector is imported", lambda s: s.__setitem__("imports_selector", True)),
    ):
        mutant = deepcopy(BASE)
        change(mutant)
        mutant_checks = dict(evaluate(mutant))
        caught = mutant_checks.get(expected_failure) is False
        mutations.append((label, caught))
        print(f"  [{'PASS' if caught else 'FAIL'}] hostile mutation caught: {label} -> {expected_failure}")
    print(f"SC-SIG-51 hostile mutations: {sum(ok for _, ok in mutations)}/{len(mutations)}")
    return 0 if all(ok for _, ok in mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
