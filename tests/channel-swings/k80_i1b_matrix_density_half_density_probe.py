#!/usr/bin/env python3
"""Exact certificate for K80 matrix density and half-density transport."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k80-i1b-matrix-density-half-density-wave.json"
ARTIFACT = ROOT / (
    "explorations/conditional-build/"
    "k80-i1b-matrix-density-half-density-wave-2026-09-01.md"
)


G = tuple[Fraction, Fraction]
M = tuple[tuple[G, G], tuple[G, G]]
ZERO: G = (Fraction(0), Fraction(0))
ONE: G = (Fraction(1), Fraction(0))


def ga(real: Fraction | int = 0, imag: Fraction | int = 0) -> G:
    return Fraction(real), Fraction(imag)


def add(x: G, y: G) -> G:
    return x[0] + y[0], x[1] + y[1]


def neg(x: G) -> G:
    return -x[0], -x[1]


def mul(x: G, y: G) -> G:
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def conj(x: G) -> G:
    return x[0], -x[1]


def mmul(left: M, right: M) -> M:
    return tuple(
        tuple(add(mul(left[i][0], right[0][j]), mul(left[i][1], right[1][j])) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def msub(left: M, right: M) -> M:
    return tuple(
        tuple(add(left[i][j], neg(right[i][j])) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def mscale(scale: Fraction, matrix: M) -> M:
    return tuple(
        tuple((scale * matrix[i][j][0], scale * matrix[i][j][1]) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def dagger(matrix: M) -> M:
    return tuple(tuple(conj(matrix[j][i]) for j in range(2)) for i in range(2))  # type: ignore[return-value]


def weight(a: Fraction, beta: Fraction) -> M:
    return ((ga(a), ga(0, beta)), (ga(0, -beta), ga(a)))


def inverse_weight(a: Fraction, beta: Fraction) -> M:
    determinant = a * a - beta * beta
    return mscale(1 / determinant, ((ga(a), ga(0, -beta)), (ga(0, beta), ga(a))))


J: M = ((ZERO, ga(-1)), (ONE, ZERO))
IDENTITY: M = ((ONE, ZERO), (ZERO, ONE))


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    u = Fraction(1, 2)
    w_plus = (1 + u) ** 2
    w_minus = (2 + u) ** 2
    a = (w_plus + w_minus) / 2
    beta = (w_plus - w_minus) / 2
    a_prime = 3 + 2 * u
    beta_prime = Fraction(-1)
    matrix_w = weight(a, beta)
    matrix_wp = weight(a_prime, beta_prime)
    matrix_u = weight((3 + 2 * u) / 2, Fraction(-1, 2))
    matrix_up = IDENTITY
    matrix_u_inv = inverse_weight((3 + 2 * u) / 2, Fraction(-1, 2))
    matrix_w_inv = inverse_weight(a, beta)
    correction = mscale(Fraction(1, 2), mmul(mmul(matrix_w_inv, matrix_wp), J))
    lower_left = msub(mmul(matrix_w, correction), mmul(dagger(correction), matrix_w))
    lower_right = mmul(matrix_wp, J)
    conjugated_correction = msub(
        mmul(mmul(matrix_u, correction), matrix_u_inv),
        mmul(mmul(J, matrix_up), matrix_u_inv),
    )
    model = manifest["control_model"]
    classification = manifest["weight_classification"]
    transport = manifest["matrix_half_density"]
    control = manifest["nonscalar_control"]
    selector = manifest["selector_result"]

    return [
        ("J squares to minus identity", mmul(J, J) == mscale(Fraction(-1), IDENTITY)),
        ("J is skew Hermitian", dagger(J) == mscale(Fraction(-1), J)),
        ("nonscalar weight commutes with J", mmul(matrix_w, J) == mmul(J, matrix_w)),
        ("weight is genuinely nonscalar", beta != 0),
        ("plus eigenweight is positive", w_plus > 0),
        ("minus eigenweight is positive", w_minus > 0),
        ("weight determinant is positive", a * a - beta * beta == w_plus * w_minus > 0),
        ("square root squares to weight", mmul(matrix_u, matrix_u) == matrix_w),
        ("square root inverse is exact", mmul(matrix_u, matrix_u_inv) == IDENTITY),
        ("canonical correction satisfies lower equation", lower_left == lower_right),
        ("canonical correction is skew Hermitian", dagger(correction) == mscale(Fraction(-1), correction)),
        ("matrix half-density cancels correction", conjugated_correction == ((ZERO, ZERO), (ZERO, ZERO))),
        ("manifest records fixed principal operator", "J*d/du" in model["operator"]),
        ("manifest records principal condition", "W*J=J*W" in model["principal_condition"]),
        ("manifest records lower condition", "W*A-A^dagger*W" in model["lower_order_condition"]),
        ("manifest records Green form", "W*J" in model["green_form"]),
        ("manifest records complete matrix form", "[[a,i*beta]" in classification["form"]),
        ("manifest records positivity", "a>|beta|" in classification["positivity"]),
        ("manifest records commutator reason", "purely imaginary" in classification["reason"]),
        ("manifest excludes noncommuting density", "noncommuting" in classification["exclusion"]),
        ("manifest records canonical correction", "W^(-1)*W'*J" in transport["canonical_correction"]),
        ("manifest records general lower solution", "W*V=V^dagger*W" in transport["general_solution"]),
        ("manifest records unitary", "W^(1/2)" in transport["unitary"]),
        ("manifest records cancellation identity", "J*d/du+A_W" in transport["identity"]),
        ("manifest records retained potential", "U*V*U^(-1)" in transport["potential_transport"]),
        ("manifest records boundary transport", "(U*f)^dagger" in transport["boundary_identity"]),
        ("manifest records distinct eigenweights", "(1+u)^2" in control["eigenweights"]),
        ("manifest records affine square root", "1+u" in control["square_root"]),
        ("manifest records full connection removal", "full nonscalar weight connection" in control["result"]),
        ("manifest localizes retained data", "W-self-adjoint V" in control["retained_data"]),
        ("manifest records no weight selector", "no coefficient selector" in selector["verdict"]),
        ("manifest records possible invariants", "rank-jump matching relation" in selector["possible_invariants"]),
        ("manifest records candidate nonselection", "log(2) and log(3)" in selector["candidate_status"]),
        ("manifest preserves source custody", "do not own" in manifest["source_attribution"]),
        ("manifest preserves claim ceiling", "no source cross-null operator" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact declares bridge classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states complete weight classification", "Complete positive matrix-weight classification" in text),
        ("artifact states canonical half-density", "Canonical matrix half-density" in text),
        ("artifact states nonscalar control", "Exact nonscalar control" in text),
        ("artifact disclaims actual I1B operator", "actual I1B cross-null operator" in text),
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
        "Complete positive matrix-weight classification",
        "Canonical matrix half-density",
        "Exact nonscalar control",
        "actual I1B cross-null operator",
    ]
    caught = 0
    for token in tokens:
        mutant_pass = {name for name, ok in evaluate(manifest, text.replace(token, "REMOVED")) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        (("control_model", "operator"), "none"),
        (("control_model", "principal_condition"), "none"),
        (("control_model", "lower_order_condition"), "none"),
        (("control_model", "green_form"), "none"),
        (("weight_classification", "form"), "arbitrary"),
        (("weight_classification", "positivity"), "none"),
        (("weight_classification", "reason"), "none"),
        (("weight_classification", "exclusion"), "all allowed"),
        (("matrix_half_density", "canonical_correction"), "none"),
        (("matrix_half_density", "general_solution"), "none"),
        (("matrix_half_density", "unitary"), "none"),
        (("matrix_half_density", "identity"), "none"),
        (("matrix_half_density", "potential_transport"), "none"),
        (("matrix_half_density", "boundary_identity"), "none"),
        (("nonscalar_control", "eigenweights"), "equal"),
        (("nonscalar_control", "square_root"), "none"),
        (("nonscalar_control", "result"), "survives"),
        (("nonscalar_control", "retained_data"), "nothing"),
        (("selector_result", "verdict"), "selects"),
        (("selector_result", "possible_invariants"), "none"),
        (("selector_result", "candidate_status"), "selected"),
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
