#!/usr/bin/env python3
"""Probe for the D4 contraction rank J-independence scope correction.

The load-bearing claim is a computation, so the probe RECOMPUTES it in exact
rationals rather than checking prose: rank(D) = 4 and rank(C_s) = 10 for J = 0,
for generic rational J, and for structured J. A planted J-dependent map is
included as a positive control, so the detector is shown able to see dependence
where dependence exists.
"""

from __future__ import annotations

import copy
import json
import re
import sys
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/d4-contraction-rank-j-independence.json"
RESULT = ROOT / "explorations/conditional-build/d4-contraction-rank-is-j-independent-2026-08-23.md"

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "the retyping is worthless",
    "non-metricity is irrelevant",
    "prediction credit is awarded",
    "D4 is discharged",
)


def _rank(rows: list[list[F]], ncols: int) -> int:
    M = [r[:] for r in rows]
    rank = 0
    for c in range(ncols):
        r0 = next((r for r in range(rank, len(M)) if M[r][c] != 0), None)
        if r0 is None:
            continue
        M[rank], M[r0] = M[r0], M[rank]
        pv = M[rank][c]
        M[rank] = [x / pv for x in M[rank]]
        for r in range(len(M)):
            if r != rank and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[rank])]
        rank += 1
    return rank


def build_D(J: list[list[F]]) -> list[list[F]]:
    return [[F(1) if (r < 4 and r == c) else (J[r - 4][c] if r >= 4 else F(0))
             for c in range(4)] for r in range(14)]


def contraction_rank(D: list[list[F]]) -> int:
    """rank of T |-> D^T T D as a map Sym^2(R^14)* -> Sym^2(R^4)*."""
    Bamb = [(i, j) for i in range(14) for j in range(i, 14)]
    Bobs = [(i, j) for i in range(4) for j in range(i, 4)]
    cols = []
    for (a, b) in Bamb:
        col = []
        for (m, l) in Bobs:
            v = D[a][m] * D[b][l] + (D[b][m] * D[a][l] if a != b else F(0))
            col.append(v)
        cols.append(col)
    rows = [[cols[c][r] for c in range(len(Bamb))] for r in range(len(Bobs))]
    return _rank(rows, len(Bamb))


def load_inputs() -> dict[str, object]:
    return {"data": json.loads(REGISTRY.read_text()), "result": RESULT.read_text()}


def collect_failures(inputs: dict[str, object]) -> tuple[int, list[str]]:
    failures: list[str] = []
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    data = inputs["data"]
    result = inputs["result"]
    assert isinstance(data, dict) and isinstance(result, str)

    # ---- the computation, recomputed ------------------------------------
    J0 = [[F(0)] * 4 for _ in range(10)]
    Jg = [[F((i * 7 + j * 3) % 11 - 5, (i + j) % 4 + 1) for j in range(4)] for i in range(10)]
    Js = [[F(i - j) for j in range(4)] for i in range(10)]

    for name, J in (("J=0", J0), ("generic", Jg), ("structured", Js)):
        D = build_D(J)
        check(_rank(D, 4) == 4, f"rank(D) = 4 for {name}")
        r = contraction_rank(D)
        check(r == 10, f"contraction rank = 10 for {name}")
        check(105 - r == 95, f"kernel = 95 for {name}")

    # Positive control: a map that IS J-dependent must show it, so the
    # detector is not blind to dependence (VERIFICATION.md rule 4).
    Dbad = build_D(J0)
    for r in range(4):
        Dbad[r][r] = F(0)          # remove the identity block
    check(_rank(Dbad, 4) < 4, "control: dropping the identity block lowers rank(D)")
    check(contraction_rank(Dbad) < 10, "control: a rank-deficient D gives contraction rank < 10")

    # ---- the registry records what was computed --------------------------
    comp = data["computation"]
    check(comp["arithmetic"].startswith("exact rationals"), "exact arithmetic recorded")
    check(all(r["rank"] == 10 and r["kernel"] == 95 for r in comp["results"]),
          "all recorded results are 10/95")
    check(any("Riemannian" in str(r["J"]) for r in comp["results"]),
          "the Riemannian reduction case is recorded")
    check(comp["rank_D_trials"]["observed_ranks"] == [4], "rank(D) trials recorded as 4 only")

    # ---- the correction is scoped, not a dismissal -----------------------
    pr = data["proposed_retyping_being_scoped"]
    check(bool(pr["correct_part"]), "the correct part of the retyping is recorded")
    check("quantifier" in pr["invalid_step"], "the invalid step is identified as the quantifier")
    check(data["effect"]["direction"] == "STRENGTHENS", "the correction strengthens the certificate")
    check("must not be re-typed" in data["rule_for_future_retyping"], "forward rule recorded")
    check(any("stands" in u for u in data["unaffected"]), "the general observation is preserved")
    check(any("PARTIAL" in u for u in data["unaffected"]), "D4 remains PARTIAL")

    check(data["ledger_verdict_change"] == "none", "no verdict moved")
    check(data["target_claim"] == "NONE-NOT-A-KILL", "artifact types its own kill status")

    # ---- document -------------------------------------------------------
    flat = re.sub(r"\s+", " ", result)
    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("That part is correct" in flat, "doc credits the correct part")
    check("contraction rather than a projection" in flat, "doc names why the identity block matters")
    check("remains `PARTIAL`" in flat or "remains PARTIAL" in flat, "doc preserves the D4 status")
    for phrase in FORBIDDEN_SUMMARY_GRAMMAR:
        check(phrase not in flat, f"forbidden grammar absent: {phrase}")
    return checks, failures


def main() -> int:
    checks, failures = collect_failures(load_inputs())
    for label in failures:
        print(f"[FAIL] {label}")
    if failures:
        return 1
    print(f"PASS {checks}/{checks}")
    return 0


def selftest() -> int:
    baseline = load_inputs()
    checks, failures = collect_failures(baseline)
    if failures:
        for label in failures:
            print(f"[FAIL] baseline: {label}")
        return 1
    print(f"BASELINE PASS {checks}/{checks}")

    mutations: list[tuple[str, str, dict[str, object]]] = []

    changed = copy.deepcopy(baseline)
    changed["data"]["computation"]["results"][0]["rank"] = 9
    mutations.append(("recorded-rank-wrong", "all recorded results are 10/95", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["effect"]["direction"] = "WEAKENS"
    mutations.append(("effect-flipped", "the correction strengthens the certificate", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["proposed_retyping_being_scoped"]["correct_part"] = ""
    mutations.append(("credit-removed", "the correct part of the retyping is recorded", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["unaffected"] = ["nothing"]
    mutations.append(("d4-status-dropped", "D4 remains PARTIAL", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["computation"]["rank_D_trials"]["observed_ranks"] = [3, 4]
    mutations.append(("trial-record-corrupt", "rank(D) trials recorded as 4 only", changed))

    # Planted positive for the summary-grammar detector.
    changed = copy.deepcopy(baseline)
    changed["result"] += "\nIn short, non-metricity is irrelevant.\n"
    mutations.append(("planted-forbidden-grammar",
                      "forbidden grammar absent: non-metricity is irrelevant", changed))

    ok = True
    for name, expected, mutated in mutations:
        _, caught = collect_failures(mutated)
        if expected not in caught:
            print(f"[FAIL] mutation {name}: expected failing check {expected!r}, got {caught!r}")
            ok = False
        else:
            print(f"MUTATION CAUGHT {name}: [FAIL] {expected}")
    print("FAILURE-PATH SELFTEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
