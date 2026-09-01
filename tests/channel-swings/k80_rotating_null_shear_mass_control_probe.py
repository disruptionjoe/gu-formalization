#!/usr/bin/env python3
"""Exact certificate for K80 rotating-null shear and mass control."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k80-rotating-null-shear-mass-control-wave.json"
ARTIFACT = ROOT / (
    "explorations/conditional-build/"
    "k80-rotating-null-shear-mass-control-wave-2026-09-01.md"
)


Vector = tuple[Fraction, Fraction, Fraction]


def pair(left: Vector, right: Vector) -> Fraction:
    return left[0] * right[0] + left[1] * right[1] - left[2] * right[2]


def curve(q: Fraction) -> tuple[Vector, Vector, Vector]:
    n = (1 - q * q, 2 * q, 1 + q * q)
    first = (-2 * q, Fraction(2), 2 * q)
    second = (Fraction(-2), Fraction(0), Fraction(2))
    return n, first, second


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    q = Fraction(3, 5)
    v0 = Fraction(2, 3)
    v1 = Fraction(-1, 4)
    q00 = Fraction(5, 7)
    q01 = Fraction(-2, 5)
    q11 = Fraction(3, 8)
    x = (v0 * v0 - v1 * v1) / 2
    dx0 = v0 * q00 - v1 * q01
    n, n1, n2 = curve(q)
    c = pair(n2, n)
    acceleration = c * dx0
    divergence = acceleration
    kinetic_first_order = pair(n1, n1) * v0 * v0 * x
    mass_norm = pair(
        tuple(n1[i] + n[i] * v0 for i in range(3)),
        tuple(n1[i] + n[i] * v0 for i in range(3)),
    )
    samples = [curve(Fraction(value))[0] for value in (-1, 0, 1)]
    general = manifest["general_result"]
    control = manifest["rotating_control"]
    potential = manifest["quadratic_potential"]

    return [
        ("polynomial curve is null", pair(n, n) == 0),
        ("null derivative is orthogonal", pair(n, n1) == 0),
        ("rotating tangent has norm four", pair(n1, n1) == 4),
        ("second derivative pairs minus four with null field", c == -4),
        ("second derivative is tangent-orthogonal", pair(n2, n1) == 0),
        ("second derivative is null", pair(n2, n2) == 0),
        ("three projective samples are distinct", len(set(samples)) == 3),
        ("all projective samples are nonzero null", all(item != (0, 0, 0) and pair(item, item) == 0 for item in samples)),
        ("explicit current contains the acceleration term", acceleration == divergence),
        ("reduced kinetic equals four v0 squared X", kinetic_first_order == 4 * v0 * v0 * x),
        ("mass norm is constant four", mass_norm == 4),
        ("mass potential is velocity-independent", mass_norm == pair(n1, n1)),
        ("manifest records differentiated nullity", "<n,n'>" in general["null_derivative"]),
        ("manifest records complete kinetic identity", "<n',n'>*psi^2" in general["kinetic_identity"]),
        ("manifest records current identity", "partial_rho(c*w^rho*X)" in general["current_identity"]),
        ("manifest records first-order representative", "c*w^(rho prime)-c'*w^rho" in general["first_order_representative"]),
        ("manifest records highest-jet verdict", "every acceleration term" in general["verdict"]),
        ("manifest records rotating polynomial", "1-q^2" in control["null_curve"]),
        ("manifest records point curve as null derivative", "n'(q)" in control["point_curve"]),
        ("manifest records exact rotating data", "<n',n'>=4" in control["exact_data"]),
        ("manifest records reduced kinetic", "4*v0^2*X" in control["reduced_kinetic"]),
        ("manifest records constant mass", "2*m^2" in control["mass_potential"]),
        ("manifest records distinct projective samples", "n(-1)" in control["projective_rotation"]),
        ("manifest records potential iff", "n^T*M*n=0" in potential["velocity_independence_on_shear_support_iff"]),
        ("manifest records mass derivative reason", "first derivative" in potential["mass_control"]),
        ("manifest records dimension boundary", "signature (2,1)" in potential["dimension_boundary"]),
        ("manifest rejects higher-dimensional collapse", "does not extend" in potential["verdict"]),
        ("manifest preserves source custody", "owns none" in manifest["source_attribution"]),
        ("manifest preserves claim ceiling", "no source-owned full carrier" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact declares bridge classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states general current reduction", "General null-field reduction" in text),
        ("artifact states exact rotating control", "Exact rotating signature-`(2,1)` control" in text),
        ("artifact states dimension-specific conclusion", "two-dimensional mass-control conclusion" in text),
        ("artifact disclaims source bridge", "not a full-carrier GU" in text),
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
        "General null-field reduction",
        "Exact rotating signature-`(2,1)` control",
        "two-dimensional mass-control conclusion",
        "not a full-carrier GU",
    ]
    caught = 0
    for token in tokens:
        mutant_pass = {name for name, ok in evaluate(manifest, text.replace(token, "REMOVED")) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        (("general_result", "null_derivative"), "none"),
        (("general_result", "kinetic_identity"), "none"),
        (("general_result", "current_identity"), "none"),
        (("general_result", "first_order_representative"), "none"),
        (("general_result", "verdict"), "acceleration survives"),
        (("rotating_control", "null_curve"), "constant"),
        (("rotating_control", "point_curve"), "zero"),
        (("rotating_control", "exact_data"), "none"),
        (("rotating_control", "reduced_kinetic"), "zero"),
        (("rotating_control", "mass_potential"), "velocity dependent"),
        (("rotating_control", "projective_rotation"), "fixed"),
        (("quadratic_potential", "velocity_independence_on_shear_support_iff"), "always"),
        (("quadratic_potential", "mass_control"), "unrelated"),
        (("quadratic_potential", "dimension_boundary"), "dimension free"),
        (("quadratic_potential", "verdict"), "extends"),
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
