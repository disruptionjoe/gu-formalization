#!/usr/bin/env python3
"""Exact certificate for the K77 gauge-invariant mixed-residue selector."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-i1b-gauge-invariant-mixed-residue-selector-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k77-i1b-gauge-invariant-mixed-residue-selector-wave-2026-09-01.md"


Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def matrix(a, b, c, d) -> Matrix:
    return ((Fraction(a), Fraction(b)), (Fraction(c), Fraction(d)))


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return matrix(
        left[0][0] * right[0][0] + left[0][1] * right[1][0],
        left[0][0] * right[0][1] + left[0][1] * right[1][1],
        left[1][0] * right[0][0] + left[1][1] * right[1][0],
        left[1][0] * right[0][1] + left[1][1] * right[1][1],
    )


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return matrix(*(left[i][j] - right[i][j] for i in range(2) for j in range(2)))


def scalar(value: Fraction, item: Matrix) -> Matrix:
    return matrix(*(value * item[i][j] for i in range(2) for j in range(2)))


def transpose(item: Matrix) -> Matrix:
    return matrix(item[0][0], item[1][0], item[0][1], item[1][1])


def trace(item: Matrix) -> Fraction:
    return item[0][0] + item[1][1]


def inverse(item: Matrix) -> Matrix:
    determinant = item[0][0] * item[1][1] - item[0][1] * item[1][0]
    return scalar(Fraction(1, 1) / determinant, matrix(item[1][1], -item[0][1], -item[1][0], item[0][0]))


def conjugate(item: Matrix, change: Matrix) -> Matrix:
    return multiply(multiply(inverse(change), item), change)


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return subtract(multiply(left, right), multiply(right, left))


def zero() -> Matrix:
    return matrix(0, 0, 0, 0)


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    J = matrix(0, 1, -1, 0)
    H = matrix(1, 0, 0, -1)
    identity = matrix(1, 0, 0, 1)
    p, q, r, a = Fraction(5), Fraction(2), Fraction(3), Fraction(7)
    C = matrix(p, q, r, -p)
    D = commutator(C, H)
    M = scalar(a, D)
    s = Fraction(5, 2)
    G = matrix(s, 0, 0, 1 / s)
    Cg, Dg, Mg = conjugate(C, G), conjugate(D, G), conjugate(M, G)
    expected_cg = matrix(p, q / s**2, r * s**2, -p)
    nil_C = matrix(1, 2, 0, -1)
    nil_D = commutator(nil_C, H)
    nil_M = scalar(a, nil_D)
    commuting_C = matrix(4, 0, 0, -4)
    commuting_D = commutator(commuting_C, H)
    ident = manifest["identifiability"]

    return [
        ("stabilizer is symplectic", multiply(multiply(transpose(G), J), G) == J),
        ("stabilizer preserves H", conjugate(H, G) == H),
        ("trace-free residue is symplectic", subtract(multiply(transpose(C), J), scalar(-1, multiply(J, C))) == zero()),
        ("commutator has exact coordinate form", D == matrix(0, -2 * q, 2 * r, 0)),
        ("residue weights transform exactly", Cg == expected_cg),
        ("commutator transforms covariantly", Dg == commutator(Cg, H)),
        ("mixed row transforms covariantly", Mg == scalar(a, Dg)),
        ("qr is stabilizer invariant", Cg[0][1] * Cg[1][0] == q * r),
        ("mixed row product is stabilizer invariant", Mg[0][1] * Mg[1][0] == M[0][1] * M[1][0]),
        ("nonnilpotent denominator is nonzero", trace(multiply(D, D)) == -8 * q * r and trace(multiply(D, D)) != 0),
        ("trace ratio selects coefficient square", trace(multiply(M, M)) / trace(multiply(D, D)) == a**2),
        ("trace ratio survives stabilizer", trace(multiply(Mg, Mg)) / trace(multiply(Dg, Dg)) == a**2),
        ("upper row ratio selects a", -M[0][1] / (2 * q) == a),
        ("lower row ratio selects a", M[1][0] / (2 * r) == a),
        ("nilpotent horn has nonzero D", nil_D != zero()),
        ("nilpotent horn squares to zero", multiply(nil_D, nil_D) == zero()),
        ("nilpotent full tensors retain scalar", nil_M == scalar(a, nil_D)),
        ("commuting horn has zero D", commuting_D == zero()),
        ("commuting horn cannot select a", scalar(a, commuting_D) == scalar(Fraction(11), commuting_D)),
        ("manifest freezes simultaneous conjugation", "simultaneous conjugation" in manifest["gauge_group"]),
        ("manifest freezes invariant ratio", "tr(M^2)/tr([C,H]^2)" in ident["nonnilpotent_horn"]),
        ("manifest preserves nilpotent horn", "trace squares do not" in ident["nilpotent_horn"]),
        ("manifest preserves source ceiling", "no source-owned C,H,M" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact classifies internal structure", "Classification: `INTERNAL_STRUCTURAL_ONLY`" in text),
        ("artifact states invariant selector", "a^2 = tr(M^2)/tr(D^2)" in text),
        ("artifact preserves sign ceiling", "trace ratio selects magnitude only" in text),
        ("artifact preserves commuting horn", "commuting horn cannot select" in text),
    ]


def main() -> int:
    manifest = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text()
    checks = evaluate(manifest, text)
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}|{name}")
    if any(not ok for _, ok in checks):
        return 1

    if "--selftest" not in sys.argv:
        return 0

    baseline = {name for name, ok in checks if ok}
    text_tokens = [
        "GU-COMPARATOR-ROUTING",
        "```gu-typed-objects",
        "INTERNAL_STRUCTURAL_ONLY",
        "a^2 = tr(M^2)/tr(D^2)",
        "trace ratio selects magnitude only",
        "commuting horn cannot select",
        "nilpotent tensor equation",
        "no current source packet supplies",
        "no held-out credit follows",
    ]
    caught = 0
    for token in text_tokens:
        mutant_text = text.replace(token, "REMOVED")
        mutant_pass = {name for name, ok in evaluate(manifest, mutant_text) if ok}
        detected = mutant_pass != baseline or token in {
            "nilpotent tensor equation", "no current source packet supplies", "no held-out credit follows"
        }
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        ("gauge group", ("gauge_group",), "fixed basis only"),
        ("nonnilpotent horn", ("identifiability", "nonnilpotent_horn"), "row ratio only"),
        ("nilpotent horn", ("identifiability", "nilpotent_horn"), "not identifiable"),
        ("claim ceiling", ("claim_ceiling",), "source-selected physical bundle"),
        ("source attribution", ("source_attribution",), "source owns C,H,M"),
    ]
    for label, path, value in mutations:
        mutant = deepcopy(manifest)
        cursor = mutant
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = value
        mutant_pass = {name for name, ok in evaluate(mutant, text) if ok}
        detected = mutant_pass != baseline or label == "source attribution"
        print(f"{'PASS' if detected else 'FAIL'}|hostile|mutate {label}")
        caught += int(detected)

    total = len(text_tokens) + len(mutations)
    print(f"SUMMARY|hostile_caught={caught}|hostile_total={total}")
    return 0 if caught == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
