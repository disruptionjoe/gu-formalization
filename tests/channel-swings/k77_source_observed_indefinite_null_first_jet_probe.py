#!/usr/bin/env python3
"""Exact certificate for the K77 indefinite-null first-jet classification."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-source-observed-indefinite-null-first-jet-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k77-source-observed-indefinite-null-first-jet-wave-2026-09-01.md"

Vector = tuple[Fraction, Fraction]
Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def vector(x: int, y: int) -> Vector:
    return (Fraction(x), Fraction(y))


def add(left: Vector, right: Vector) -> Vector:
    return (left[0] + right[0], left[1] + right[1])


def scale(value: Fraction, item: Vector) -> Vector:
    return (value * item[0], value * item[1])


def pair(left: Vector, form: Matrix, right: Vector) -> Fraction:
    return (
        left[0] * (form[0][0] * right[0] + form[0][1] * right[1])
        + left[1] * (form[1][0] * right[0] + form[1][1] * right[1])
    )


def gram(form: Matrix, w0: Vector, w1: Vector) -> tuple[Fraction, Fraction, Fraction]:
    return (pair(w0, form, w0), pair(w0, form, w1), pair(w1, form, w1))


def quadratic_coefficients(
    form: Matrix, w0: Vector, w1: Vector
) -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction]:
    """Coefficients of r^2, r*s, s^2, s*t, t^2 in Q_2."""
    g00, g01, g11 = gram(form, w0, w1)
    return (
        g00 / 2,
        g01,
        (g11 - g00) / 2,
        -g01,
        -g11 / 2,
    )


def highest_jet_value(
    form: Matrix,
    w0: Vector,
    w1: Vector,
    r: Fraction,
    s: Fraction,
    t: Fraction,
) -> Fraction:
    u0 = add(scale(r, w0), scale(s, w1))
    u1 = add(scale(s, w0), scale(t, w1))
    return (pair(u0, form, u0) - pair(u1, form, u1)) / 2


def polynomial_value(
    coefficients: tuple[Fraction, Fraction, Fraction, Fraction, Fraction],
    r: Fraction,
    s: Fraction,
    t: Fraction,
) -> Fraction:
    c_r2, c_rs, c_s2, c_st, c_t2 = coefficients
    return c_r2 * r**2 + c_rs * r * s + c_s2 * s**2 + c_st * s * t + c_t2 * t**2


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    lorentz: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(-1)))
    positive: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    null = vector(1, 1)
    q_direction = vector(1, -1)
    null_w0 = null
    null_w1 = scale(Fraction(2), null)
    opposite_w0 = vector(1, 1)
    opposite_w1 = vector(1, -1)

    null_gram = gram(lorentz, null_w0, null_w1)
    null_coefficients = quadratic_coefficients(lorentz, null_w0, null_w1)
    positive_coefficients = quadratic_coefficients(positive, null_w0, null_w1)
    opposite_gram = gram(lorentz, opposite_w0, opposite_w1)
    opposite_coefficients = quadratic_coefficients(lorentz, opposite_w0, opposite_w1)
    result = manifest["exact_result"]
    result_flat = " ".join(json.dumps(result, sort_keys=True).split())
    controls = manifest["witnesses_and_controls"]

    samples = [
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(2), Fraction(-3), Fraction(5)),
    ]

    return [
        ("null witness has nonzero velocity derivative and rank-two total differential", (
            null_w0 != (0, 0)
            and null_w1 != (0, 0)
            and q_direction[0] * null_w0[1] - q_direction[1] * null_w0[0] != 0
        )),
        ("null witness Gram is exactly zero", null_gram == (0, 0, 0)),
        ("null witness highest-jet polynomial is identically zero", null_coefficients == (0, 0, 0, 0, 0)),
        ("direct and coefficient evaluations agree on exact samples", all(
            highest_jet_value(lorentz, null_w0, null_w1, r, s, t)
            == polynomial_value(null_coefficients, r, s, t)
            for r, s, t in samples
        )),
        ("null witness vanishes on every exact sample", all(
            highest_jet_value(lorentz, null_w0, null_w1, r, s, t) == 0
            for r, s, t in samples
        )),
        ("positive control Gram is nonzero", gram(positive, null_w0, null_w1) == (2, 4, 8)),
        ("positive control r squared coefficient is one", positive_coefficients[0] == 1),
        ("positive control detects planted acceleration", highest_jet_value(
            positive, null_w0, null_w1, Fraction(1), Fraction(0), Fraction(0)
        ) == 1),
        ("opposite null columns are individually null", opposite_gram[0] == 0 and opposite_gram[2] == 0),
        ("opposite null columns have nonzero cross pairing", opposite_gram[1] == 2),
        ("cross pairing populates r*s and s*t with opposite signs", opposite_coefficients == (0, 2, 0, -2, 0)),
        ("cross-term plant is detected", highest_jet_value(
            lorentz, opposite_w0, opposite_w1, Fraction(1), Fraction(1), Fraction(0)
        ) == 2),
        ("zero polynomial forces both norms and cross pairing to vanish", (
            null_coefficients[0] == 0
            and null_coefficients[4] == 0
            and null_coefficients[1] == 0
            and null_gram == (0, 0, 0)
        )),
        ("manifest freezes Lorentzian 1+1 base", "Lorentzian 1+1" in manifest["frozen_model"]["base"]),
        ("manifest freezes symmetric second-jet comparison", "symmetric second jet" in manifest["frozen_model"]["comparison"]),
        ("manifest states the exact totally-null iff", "iff im(D_v Phi) is totally H-null" in result_flat),
        ("manifest bounds the conclusion to quadratic survival", "only to survive" in result["survival_ceiling"]),
        ("manifest records the nonzero null witness", "Phi=m*q+n*(v_0+2*v_1)" in controls["nonzero_null_witness"]),
        ("manifest records positive-definite control", "H=I_2" in controls["positive_definite_control"]),
        ("manifest records cross-term control", "pairing is 2" in controls["cross_term_control"]),
        ("manifest records rank-one 1+1 consequence", "rank at most one" in controls["signature_1_1_consequence"]),
        ("manifest preserves source custody", "repository-derived" in manifest["source_attribution"]),
        ("manifest preserves full-carrier ceiling", "rank-1920" in manifest["claim_ceiling"]),
        ("manifest preserves gauge ceiling", "gauge quotient" in manifest["claim_ceiling"]),
        ("manifest preserves domain ceiling", "analytic domain" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact classifies bridge boundary", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states total-null equivalence", "im(D_v Phi)=span{w_0,w_1} is totally H-null" in text),
        ("artifact states individual nullity is insufficient", "Individual nullity is insufficient" in text),
        ("artifact distinguishes base and carrier indefiniteness", "Indefiniteness of the **base symbol alone**" in text),
        ("artifact disclaims complete bridge existence", "not yet an existence theorem for the full bridge" in text),
        ("artifact preserves source and physical credit ceiling", "earns no source-action, full-carrier bridge" in text),
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
    text_tokens = [
        "GU-COMPARATOR-ROUTING",
        "```gu-typed-objects",
        "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "im(D_v Phi)=span{w_0,w_1} is totally H-null",
        "Individual nullity is insufficient",
        "Indefiniteness of the **base symbol alone**",
        "not yet an existence theorem for the full bridge",
        "earns no source-action, full-carrier bridge",
    ]
    caught = 0
    for token in text_tokens:
        mutant_text = text.replace(token, "REMOVED")
        mutant_pass = {name for name, ok in evaluate(manifest, mutant_text) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        ("base", ("frozen_model", "base"), "Euclidean line"),
        ("comparison", ("frozen_model", "comparison"), "on shell"),
        ("classification", ("exact_result", "classification"), "each column is null"),
        ("survival ceiling", ("exact_result", "survival_ceiling"), "complete bridge exists"),
        ("null witness", ("witnesses_and_controls", "nonzero_null_witness"), "none"),
        ("positive control", ("witnesses_and_controls", "positive_definite_control"), "none"),
        ("cross control", ("witnesses_and_controls", "cross_term_control"), "none"),
        ("rank consequence", ("witnesses_and_controls", "signature_1_1_consequence"), "rank two"),
        ("source custody", ("source_attribution",), "source-owned theorem"),
        ("claim ceiling", ("claim_ceiling",), "full physical equivalence"),
    ]
    for label, path, value in mutations:
        mutant = mutate(manifest, path, value)
        mutant_pass = {name for name, ok in evaluate(mutant, text) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|mutate {label}")
        caught += int(detected)

    total = len(text_tokens) + len(mutations)
    print(f"SUMMARY|hostile_caught={caught}|hostile_total={total}")
    return 0 if caught == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
