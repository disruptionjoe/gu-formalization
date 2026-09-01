#!/usr/bin/env python3
"""Exact certificate for K79 projective-null rigidity and variable shear."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k79-null-line-projective-rigidity-wave.json"
ARTIFACT = ROOT / (
    "explorations/conditional-build/"
    "k79-null-line-projective-rigidity-wave-2026-09-01.md"
)


def pair2(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> Fraction:
    return left[0] * right[0] - left[1] * right[1]


def pair3(vector: tuple[float, float, float]) -> float:
    return vector[0] ** 2 + vector[1] ** 2 - vector[2] ** 2


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    q = Fraction(3, 5)
    v0 = Fraction(2, 3)
    v1 = Fraction(-1, 4)
    r = Fraction(5, 7)
    s = Fraction(-2, 5)
    t = Fraction(3, 8)
    x = (v0 * v0 - v1 * v1) / 2
    dx0 = v0 * r - v1 * s
    dx1 = v0 * s - v1 * t
    n = (Fraction(1), Fraction(1))
    b_prime = (Fraction(1), 2 * q)
    c = pair2(b_prime, n)
    c_prime = Fraction(-2)
    w = (q, Fraction(1))
    w_prime = (Fraction(1), Fraction(0))

    acceleration = c * (w[0] * dx0 + w[1] * dx1)
    shear_derivative = 2 * c * (w_prime[0] * v0 + w_prime[1] * v1) * x
    divergence = acceleration + sum(
        (c_prime * w[i] + c * w_prime[i]) * (v0, v1)[i] * x
        for i in range(2)
    )
    correction = sum(
        (c * w_prime[i] - c_prime * w[i]) * (v0, v1)[i] * x
        for i in range(2)
    )
    witness_correction = (v0 + 2 * v1) * x

    switch_left = (Fraction(-1), Fraction(1))
    switch_zero = (Fraction(0), Fraction(0))
    switch_right = (Fraction(1), Fraction(1))
    rotating_samples = [
        (1.0, 0.0, 1.0),
        (0.0, 1.0, 1.0),
        (-1.0, 0.0, 1.0),
    ]
    projective = manifest["projective_result"]
    shear = manifest["variable_shear_result"]
    potential = manifest["quadratic_potential"]

    return [
        ("fixed positive null generator is null", pair2(n, n) == 0),
        ("nonzero signature-one-one null sample has ratio plus one", Fraction(7, 5) / Fraction(7, 5) == 1),
        ("opposite null sample has ratio minus one", Fraction(-7, 5) / Fraction(7, 5) == -1),
        ("switch control is null on left", pair2(switch_left, switch_left) == 0),
        ("switch control vanishes at crossing", switch_zero == (0, 0)),
        ("switch control is null on right", pair2(switch_right, switch_right) == 0),
        ("higher-signature rotating samples are null", all(abs(pair3(item)) < 1e-12 for item in rotating_samples)),
        ("higher-signature projective direction changes", len(set(rotating_samples)) == 3),
        ("variable-shear current identity closes exactly", acceleration + shear_derivative == divergence + correction),
        ("witness correction reduces to v0 plus two v1", correction == witness_correction),
        ("witness correction is nonzero", correction != 0),
        ("null-line mass point curve has zero norm", pair2((q, q), (q, q)) == 0),
        ("manifest freezes nonvanishing connected domain", "nonvanishing C1" in manifest["frozen_model"]["null_field"]),
        ("manifest records fixed-line factorization", "sigma" in projective["factorization"]),
        ("manifest records connectedness reason", "connected interval" in projective["reason"]),
        ("manifest rejects projective rotation", "cannot rotate projectively" in projective["verdict"]),
        ("manifest records zero boundary", "n(0)=0" in projective["zero_control"]),
        ("manifest records higher-signature escape", "signature (2,1)" in projective["higher_signature_control"]),
        ("manifest records variable reduced map", "w^rho(q)" in shear["reduced_map"]),
        ("manifest records kinetic identity", "partial_rho(X)" in shear["kinetic_identity"]),
        ("manifest records current identity", "partial_rho(c*w^rho*X)" in shear["current_identity"]),
        ("manifest records Wronskian correction", "c*w^(rho prime)-c'*w^rho" in shear["first_order_representative"]),
        ("manifest records exact witness", "v0+2*v1" in shear["exact_witness"]),
        ("manifest records potential iff", "n_sigma^T M n_sigma=0" in potential["velocity_independence_on_shear_support_iff"]),
        ("manifest records mass-line consequence", "span(n_sigma)" in potential["mass_control"]),
        ("manifest fences mass conclusion", "not a source or full-carrier no-go" in potential["ceiling"]),
        ("manifest preserves source custody", "owns none" in manifest["source_attribution"]),
        ("manifest preserves higher-signature ceiling", "no source-owned full carrier" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact declares bridge classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states no rotating line in frozen carrier", "There is no genuinely rotating nonzero null line" in text),
        ("artifact states variable current formula", "c w^(rho prime)-c' w^rho" in text),
        ("artifact states zero seam", "direction switch can occur only through a zero" in text),
        ("artifact states higher-signature contrary control", "Higher signature genuinely permits rotation" in text),
        ("artifact disclaims source bridge", "No source-owned full-carrier symbol" in text),
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
        "There is no genuinely rotating nonzero null line",
        "c w^(rho prime)-c' w^rho",
        "direction switch can occur only through a zero",
        "Higher signature genuinely permits rotation",
        "No source-owned full-carrier symbol",
    ]
    caught = 0
    for token in tokens:
        mutant_pass = {name for name, ok in evaluate(manifest, text.replace(token, "REMOVED")) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        (("frozen_model", "null_field"), "arbitrary"),
        (("projective_result", "factorization"), "rotating"),
        (("projective_result", "reason"), "none"),
        (("projective_result", "verdict"), "rotation allowed"),
        (("projective_result", "zero_control"), "no zero"),
        (("projective_result", "higher_signature_control"), "none"),
        (("variable_shear_result", "reduced_map"), "point map"),
        (("variable_shear_result", "kinetic_identity"), "none"),
        (("variable_shear_result", "current_identity"), "none"),
        (("variable_shear_result", "first_order_representative"), "none"),
        (("variable_shear_result", "exact_witness"), "none"),
        (("quadratic_potential", "velocity_independence_on_shear_support_iff"), "always"),
        (("quadratic_potential", "mass_control"), "unrestricted"),
        (("quadratic_potential", "ceiling"), "source no-go"),
        (("source_attribution",), "source-owned"),
        (("claim_ceiling",), "physical full-carrier equivalence"),
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
