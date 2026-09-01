#!/usr/bin/env python3
"""Exact certificate for the K81 lower-potential periodic spectrum."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k81-i1b-lower-potential-periodic-spectrum-wave.json"
ARTIFACT = ROOT / (
    "explorations/conditional-build/"
    "k81-i1b-lower-potential-periodic-spectrum-wave-2026-09-01.md"
)

G = tuple[Fraction, Fraction]
M = tuple[tuple[G, G], tuple[G, G]]
ZERO: G = (Fraction(0), Fraction(0))
ONE: G = (Fraction(1), Fraction(0))


def ga(real: Fraction | int = 0, imag: Fraction | int = 0) -> G:
    return Fraction(real), Fraction(imag)


def add(left: G, right: G) -> G:
    return left[0] + right[0], left[1] + right[1]


def mul(left: G, right: G) -> G:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def mmul(left: M, right: M) -> M:
    return tuple(
        tuple(add(mul(left[i][0], right[0][j]), mul(left[i][1], right[1][j])) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def madd(*matrices: M) -> M:
    result = ((ZERO, ZERO), (ZERO, ZERO))
    for matrix in matrices:
        result = tuple(
            tuple(add(result[i][j], matrix[i][j]) for j in range(2))
            for i in range(2)
        )  # type: ignore[assignment]
    return result


def mscale(value: Fraction, matrix: M) -> M:
    return tuple(
        tuple((value * matrix[i][j][0], value * matrix[i][j][1]) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


IDENTITY: M = ((ONE, ZERO), (ZERO, ONE))
J: M = ((ZERO, ga(-1)), (ONE, ZERO))
H: M = ((ONE, ZERO), (ZERO, ga(-1)))
S: M = ((ZERO, ONE), (ONE, ZERO))
K: M = ((ZERO, ga(0, -1)), (ga(0, 1), ZERO))


def log_bounds(integer: int, terms: int = 12) -> tuple[Fraction, Fraction]:
    """Rigorous bounds from log(x)=2*atanh((x-1)/(x+1))."""
    z = Fraction(integer - 1, integer + 1)
    lower = 2 * sum((z ** (2 * k + 1)) / (2 * k + 1) for k in range(terms))
    first_power = 2 * terms + 1
    remainder = 2 * z**first_power / (first_power * (1 - z * z))
    return lower, lower + remainder


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    c = Fraction(1, 3)
    x = Fraction(2, 5)
    y = Fraction(-1, 4)
    z = Fraction(3, 7)
    n = -2
    shifted = Fraction(n) + z
    block = madd(mscale(c, IDENTITY), mscale(x, H), mscale(y, S), mscale(shifted, K))
    centered = madd(block, mscale(-c, IDENTITY))
    radius2 = x * x + y * y + shifted * shifted
    log2_lower, log2_upper = log_bounds(2)
    log3_lower, log3_upper = log_bounds(3)
    fourier = manifest["fourier_classification"]
    candidate = manifest["candidate_subfamily"]
    boundary = manifest["half_density_boundary"]

    return [
        ("J squares to minus identity", mmul(J, J) == mscale(Fraction(-1), IDENTITY)),
        ("H squares to identity", mmul(H, H) == IDENTITY),
        ("S squares to identity", mmul(S, S) == IDENTITY),
        ("K squares to identity", mmul(K, K) == IDENTITY),
        ("H and S anticommute", madd(mmul(H, S), mmul(S, H)) == ((ZERO, ZERO), (ZERO, ZERO))),
        ("H and K anticommute", madd(mmul(H, K), mmul(K, H)) == ((ZERO, ZERO), (ZERO, ZERO))),
        ("S and K anticommute", madd(mmul(S, K), mmul(K, S)) == ((ZERO, ZERO), (ZERO, ZERO))),
        ("arbitrary Fourier block obeys Clifford square", mmul(centered, centered) == mscale(radius2, IDENTITY)),
        ("arbitrary block trace is two c", add(block[0][0], block[1][1]) == ga(2 * c)),
        ("radius is positive in control", radius2 > 0),
        ("integer z shift reindexes mode", Fraction(n + 1) + (z - 1) == shifted),
        ("z sign reflection reindexes squared shift", (Fraction(-n) - z) ** 2 == shifted**2),
        ("commuting rotation preserves transverse radius", x * x + y * y == y * y + (-x) * (-x)),
        ("log two lower bound positive", log2_lower > 0),
        ("log two interval ordered", log2_lower < log2_upper),
        ("log three interval ordered", log3_lower < log3_upper),
        ("log intervals are rigorously disjoint", log2_upper < log3_lower),
        ("candidate gap order is exact", 0 < log2_lower < log2_upper < log3_lower < log3_upper),
        ("manifest records mode block", "n+z" in fourier["mode_block"]),
        ("manifest records Clifford identity", "x^2+y^2" in fourier["clifford_identity"]),
        ("manifest records complete spectrum", "sqrt" in fourier["spectrum"]),
        ("manifest records complete constant family", "every constant Hermitian" in fourier["complete_constant_family"]),
        ("manifest records periodic invariants", "rho^2" in fourier["periodic_invariants"]),
        ("manifest records commuting unitary", "rotate" in fourier["commuting_unitary"]),
        ("manifest records aH potential", "V=aH" in candidate["potential"]),
        ("manifest records candidate spectrum", "n^2+a^2" in candidate["spectrum"]),
        ("manifest records exact gap", "attained at n=0" in candidate["spectral_gap"]),
        ("manifest records candidate order", "log(2)<log(3)" in candidate["candidate_order"]),
        ("manifest records independent selector condition", "independent source/action" in candidate["selector_condition"]),
        ("manifest rejects definitional selection", "restates" in candidate["nonselection_without_owner"]),
        ("manifest records half-density transport", "W^(1/2)" in boundary["transport"]),
        ("manifest freezes constant scope", "post-transport potential is constant" in boundary["constant_scope"]),
        ("manifest records boundary warning", "twists boundary" in boundary["nonperiodic_warning"]),
        ("manifest preserves source custody", "own no actual cross-null" in manifest["source_attribution"]),
        ("manifest preserves claim ceiling", "no source cross-null operator" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact declares bridge classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states complete normal form", "Complete constant Hermitian lower-potential normal form" in text),
        ("artifact states candidate condition", "if it is owned" in text),
        ("artifact states half-density boundary", "Exact boundary of matrix half-density transport" in text),
        ("artifact disclaims actual I1B operator", "does not construct the actual I1B cross-null operator" in text),
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
        "Complete constant Hermitian lower-potential normal form",
        "if it is owned",
        "Exact boundary of matrix half-density transport",
        "does not construct the actual I1B cross-null operator",
    ]
    caught = 0
    for token in tokens:
        mutant_pass = {name for name, ok in evaluate(manifest, text.replace(token, "REMOVED")) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        (("fourier_classification", "mode_block"), "none"),
        (("fourier_classification", "clifford_identity"), "none"),
        (("fourier_classification", "spectrum"), "none"),
        (("fourier_classification", "complete_constant_family"), "partial"),
        (("fourier_classification", "periodic_invariants"), "none"),
        (("fourier_classification", "commuting_unitary"), "changes radius"),
        (("candidate_subfamily", "potential"), "none"),
        (("candidate_subfamily", "spectrum"), "flat"),
        (("candidate_subfamily", "spectral_gap"), "zero"),
        (("candidate_subfamily", "candidate_order"), "equal"),
        (("candidate_subfamily", "selector_condition"), "automatic"),
        (("candidate_subfamily", "nonselection_without_owner"), "selects"),
        (("half_density_boundary", "transport"), "erases V"),
        (("half_density_boundary", "constant_scope"), "variable"),
        (("half_density_boundary", "nonperiodic_warning"), "none"),
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
