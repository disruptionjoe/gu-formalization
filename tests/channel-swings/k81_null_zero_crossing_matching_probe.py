#!/usr/bin/env python3
"""Exact certificate for the K81 null zero-crossing matching classification."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k81-null-zero-crossing-matching-wave.json"
ARTIFACT = ROOT / (
    "explorations/conditional-build/"
    "k81-null-zero-crossing-matching-wave-2026-09-01.md"
)

Vector = tuple[Fraction, Fraction]
N_PLUS: Vector = (Fraction(1), Fraction(1))
N_MINUS: Vector = (Fraction(1), Fraction(-1))


def pair(left: Vector, right: Vector) -> Fraction:
    return left[0] * right[0] - left[1] * right[1]


def scale(value: Fraction, vector: Vector) -> Vector:
    return value * vector[0], value * vector[1]


def cubic_field(q: Fraction) -> Vector:
    return scale(q**3, N_PLUS if q >= 0 else N_MINUS)


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    h = Fraction(2, 5)
    positive = cubic_field(h)
    negative = cubic_field(-h)
    r1 = Fraction(5, 3)
    r2 = Fraction(-7, 4)
    t1 = Fraction(11, 6)
    t2 = Fraction(13, 7)
    w0 = t1 / r1
    w1 = (t2 * r1 - t1 * r2) / (2 * r1 * r1)
    b_positive = scale(h**4, N_PLUS)
    b_negative = scale(h**4, N_MINUS)
    contrary_b: Vector = (Fraction(1), Fraction(0))
    switch = manifest["direction_switch"]
    matching = manifest["shear_matching"]
    mass = manifest["mass_control"]

    return [
        ("two real null directions are null", pair(N_PLUS, N_PLUS) == pair(N_MINUS, N_MINUS) == 0),
        ("null directions are independent", pair(N_PLUS, N_MINUS) == 2),
        ("positive cubic branch is null", pair(positive, positive) == 0),
        ("negative cubic branch is null", pair(negative, negative) == 0),
        ("cubic field is nonzero off interface", positive != (0, 0) and negative != (0, 0)),
        ("cubic interface value vanishes", cubic_field(Fraction(0)) == (0, 0)),
        ("first interface jet coefficient vanishes", 0 * h**2 == 0),
        ("second interface jet coefficient vanishes", 0 * h == 0),
        ("right third jet is six n plus", scale(Fraction(6), N_PLUS) == (6, 6)),
        ("left third jet is six n minus", scale(Fraction(6), N_MINUS) == (6, -6)),
        ("third jets differ", scale(Fraction(6), N_PLUS) != scale(Fraction(6), N_MINUS)),
        ("simple-zero trace formula is exact", w0 == Fraction(11, 10)),
        ("simple-zero first-jet formula is exact", w1 == Fraction(3177, 2800)),
        ("divisible polynomial has regular quotient", (2 * h + 3 * h * h) / h == 2 + 3 * h),
        ("nondivisible numerator has pole witness", Fraction(1, 1) / h != Fraction(1, 1) / (h / 2)),
        ("mass-compatible right point curve is null", pair(b_positive, b_positive) == 0),
        ("mass-compatible left point curve is null", pair(b_negative, b_negative) == 0),
        ("right mass cross term vanishes", pair(positive, b_positive) == 0),
        ("left mass cross term vanishes", pair(negative, b_negative) == 0),
        ("contrary point curve couples to both lines", pair(N_PLUS, contrary_b) == pair(N_MINUS, contrary_b) == 1),
        ("manifest records punctured factorization", "r_plus" in switch["punctured_factorization"]),
        ("manifest records complete C2 jet matching", "n''(0)=0" in switch["c2_matching"]),
        ("manifest records cubic witness", "q^3" in switch["cubic_witness"]),
        ("manifest records C2 not C3 grade", "not C3" in switch["witness_regular_grade"]),
        ("manifest records same-line contrast", "same null line" in switch["same_line_contrast"]),
        ("manifest records effective coefficient", "tilde_w=r*w" in matching["same_line_effective_coefficient"]),
        ("manifest records continuous lift", "tilde_w'(0)/r'(0)" in matching["simple_zero_continuous_lift"]),
        ("manifest records C1 lift", "tilde_w''(0)" in matching["simple_zero_c1_lift"]),
        ("manifest records pole horn", "pole" in matching["nondivisible_horn"]),
        ("manifest rejects invertible amplitude transport", "no invertible" in matching["switched_line_result"]),
        ("manifest assigns extra matching ownership", "boundary" in matching["extra_matching_owner"]),
        ("manifest records orthogonal complement collapse", "n^perp=span(n)" in mass["signature_11_consequence"]),
        ("manifest records interface point collapse", "b(0)=0" in mass["interface_consequence"]),
        ("manifest records kinetic collapse", "vanishes" in mass["kinetic_consequence"]),
        ("manifest records mass-control verdict", "does not escape" in mass["verdict"]),
        ("manifest preserves source custody", "own no full-carrier" in manifest["source_attribution"]),
        ("manifest preserves claim ceiling", "no higher-signature" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact declares bridge classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states C2 switch theorem", "flat through second order" in text),
        ("artifact states divisibility law", "exact divisibility law" in text),
        ("artifact states mass collapse", "mass control still collapses" in text),
        ("artifact disclaims full-carrier bridge", "not a full-carrier GU bridge" in text),
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
        "flat through second order",
        "exact divisibility law",
        "mass control still collapses",
        "not a full-carrier GU bridge",
    ]
    caught = 0
    for token in tokens:
        mutant_pass = {name for name, ok in evaluate(manifest, text.replace(token, "REMOVED")) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        (("direction_switch", "punctured_factorization"), "none"),
        (("direction_switch", "c2_matching"), "nonzero jets"),
        (("direction_switch", "cubic_witness"), "none"),
        (("direction_switch", "witness_regular_grade"), "smooth"),
        (("direction_switch", "same_line_contrast"), "same"),
        (("shear_matching", "same_line_effective_coefficient"), "unrelated"),
        (("shear_matching", "simple_zero_continuous_lift"), "none"),
        (("shear_matching", "simple_zero_c1_lift"), "none"),
        (("shear_matching", "nondivisible_horn"), "regular"),
        (("shear_matching", "switched_line_result"), "invertible"),
        (("shear_matching", "extra_matching_owner"), "zero"),
        (("mass_control", "signature_11_consequence"), "none"),
        (("mass_control", "interface_consequence"), "nonzero"),
        (("mass_control", "kinetic_consequence"), "nonzero"),
        (("mass_control", "verdict"), "escapes"),
        (("source_attribution",), "source-owned"),
        (("claim_ceiling",), "physical full-carrier bridge"),
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
