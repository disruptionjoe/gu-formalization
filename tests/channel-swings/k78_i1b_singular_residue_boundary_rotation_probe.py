#!/usr/bin/env python3
"""Certificate for the K78 singular-residue and boundary-rotation control."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k78-i1b-singular-residue-boundary-rotation-wave.json"
ARTIFACT = ROOT / (
    "explorations/conditional-build/"
    "k78-i1b-singular-residue-boundary-rotation-wave-2026-09-01.md"
)


def matmul(left: tuple[tuple[float, float], ...], right: tuple[tuple[float, float], ...]):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def matvec(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(2)) for i in range(2))


def close(left: float, right: float, tolerance: float = 1e-12) -> bool:
    return abs(left - right) < tolerance


def exp_lower(value: Fraction, order: int) -> Fraction:
    term = Fraction(1)
    total = term
    for index in range(1, order + 1):
        term *= value / index
        total += term
    return total


def exp_upper(value: Fraction, order: int) -> Fraction:
    """Geometric upper bound for the positive exponential tail."""
    lower = exp_lower(value, order)
    term = Fraction(1)
    for index in range(1, order + 2):
        term *= value / index
    ratio_bound = value / (order + 2)
    return lower + term / (1 - ratio_bound)


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    kappa = 0.25
    a2 = math.log(2)
    a3 = math.log(3)
    rho2 = math.hypot(kappa, a2)
    rho3 = math.hypot(kappa, a3)
    threshold = math.sqrt(3) / 4
    a = a2
    rho = rho2
    theta = math.atan2(a, kappa)
    c = math.cos(theta / 2)
    s = math.sin(theta / 2)
    matrix = ((kappa, -a), (-a, -kappa))
    square = matmul(matrix, matrix)
    plus = (c, -s)
    minus = (s, c)
    cplus = matvec(matrix, plus)
    cminus = matvec(matrix, minus)
    fixed_slope = s / c
    indicial = manifest["indicial_result"]
    frame = manifest["eigenframe"]
    weighted = manifest["weighted_mode_census"]
    log2_above_half = exp_upper(Fraction(1, 2), 8) < 2
    log2_below_seven_tenths = exp_lower(Fraction(7, 10), 5) > 2
    log3_above_one = exp_upper(Fraction(1), 9) < 3

    return [
        ("normal square is scalar", close(square[0][0], rho * rho) and close(square[1][1], rho * rho)),
        ("normal square has zero off diagonal", close(square[0][1], 0) and close(square[1][0], 0)),
        ("positive eigenvector is exact numerically", all(close(cplus[i], rho * plus[i]) for i in range(2))),
        ("negative eigenvector is exact numerically", all(close(cminus[i], -rho * minus[i]) for i in range(2))),
        ("eigenframe is orthonormal", close(sum(x * x for x in plus), 1) and close(sum(x * x for x in minus), 1)),
        ("eigenvectors are orthogonal", close(sum(plus[i] * minus[i] for i in range(2)), 0)),
        ("rational series proves log2 above one half", log2_above_half),
        ("rational series proves log2 below seven tenths", log2_below_seven_tenths),
        ("rational series proves log3 above one", log3_above_one),
        ("log2 exceeds unweighted threshold", a2 > threshold),
        ("log3 exceeds unweighted threshold", a3 > threshold),
        ("both candidates are unweighted limit point", rho2 > 0.5 and rho3 > 0.5),
        ("p1 raw count keeps log2 singular mode", rho2 < 1),
        ("p1 raw count rejects log3 singular mode", rho3 > 1),
        ("candidate exponents differ", rho2 < rho3),
        ("candidate frame angles differ", math.atan2(a2, kappa) < math.atan2(a3, kappa)),
        ("fixed component line has half-angle slope", close(fixed_slope, math.tan(theta / 2))),
        ("manifest records singular normal matrix", "kappa*H-a*S" in manifest["control_model"]["normal_matrix"]),
        ("manifest records Clifford identity", "C^2" in indicial["identity"]),
        ("manifest records unweighted threshold", "rho<1/2" in indicial["unweighted_limit_circle_iff"]),
        ("manifest classifies both candidates", "both a=log(2)" in indicial["candidate_class"]),
        ("manifest rejects endpoint selection", "neither candidate" in indicial["candidate_selection"]),
        ("manifest records half-angle frame", "theta/2" in frame["positive_vector"]),
        ("manifest records fixed-line slope", "tan(theta/2)" in frame["fixed_component_line"]),
        ("manifest fences coordinate rotation", "independent owner" in frame["selection_fence"]),
        ("manifest records weighted p1 split", "rho(log(2))<1<rho(log(3))" in weighted["p1_result"]),
        ("manifest fences weighted census", "integrability census only" in weighted["fence"]),
        ("manifest preserves source custody", "do not own" in manifest["source_attribution"]),
        ("manifest preserves physical ceiling", "no source cross-null operator" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact declares bridge classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states both limit point", "strictly limit-point" in text),
        ("artifact states no binary selection", "does not select" in text),
        ("artifact states half-angle line", "c_-/c_+=tan(theta/2)" in text),
        ("artifact fences weighted count", "integrability discriminator only" in text),
        ("artifact disclaims source operator", "They are not the actual cross-null operator" in text),
    ]


def mutate(manifest: dict, path: tuple[str, ...], value: object) -> dict:
    mutant = deepcopy(manifest)
    cursor = mutant
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value
    return mutant


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    text = ARTIFACT.read_text(encoding="utf-8")
    checks = evaluate(manifest, text)
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}|{name}")
    if any(not ok for _, ok in checks):
        return 1
    print(f"SUMMARY|checks_passed={len(checks)}|checks_total={len(checks)}")
    if "--selftest" not in sys.argv:
        return 0

    baseline = {name for name, ok in checks if ok}
    tokens = [
        "GU-COMPARATOR-ROUTING",
        "```gu-typed-objects",
        "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`",
        "strictly limit-point",
        "does not select",
        "c_-/c_+=tan(theta/2)",
        "integrability discriminator only",
        "They are not the actual cross-null operator",
    ]
    caught = 0
    for token in tokens:
        mutant_pass = {name for name, ok in evaluate(manifest, text.replace(token, "REMOVED")) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        (("control_model", "normal_matrix"), "bounded"),
        (("indicial_result", "identity"), "none"),
        (("indicial_result", "unweighted_limit_circle_iff"), "always"),
        (("indicial_result", "candidate_class"), "distinct classes"),
        (("indicial_result", "candidate_selection"), "selects log3"),
        (("eigenframe", "positive_vector"), "fixed"),
        (("eigenframe", "fixed_component_line"), "constant slope"),
        (("eigenframe", "selection_fence"), "automatic selector"),
        (("weighted_mode_census", "p1_result"), "same count"),
        (("weighted_mode_census", "fence"), "self-adjoint theorem"),
        (("source_attribution",), "source-owned"),
        (("claim_ceiling",), "physical selector"),
    ]
    for path, value in mutations:
        mutant_pass = {name for name, ok in evaluate(mutate(manifest, path, value), text) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|mutate {'.'.join(path)}")
        caught += int(detected)

    total = len(tokens) + len(mutations)
    print(f"SUMMARY|hostile_caught={caught}|hostile_total={total}")
    return 0 if caught == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
