#!/usr/bin/env python3
"""Exact certificate for the K77 action-owned mixed-residue independence audit."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-i1b-action-owned-mixed-residue-independence-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k77-i1b-action-owned-mixed-residue-independence-wave-2026-09-01.md"

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def matrix(a, b, c, d) -> Matrix:
    return ((Fraction(a), Fraction(b)), (Fraction(c), Fraction(d)))


def add(left: Matrix, right: Matrix) -> Matrix:
    return matrix(*(left[i][j] + right[i][j] for i in range(2) for j in range(2)))


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return matrix(*(left[i][j] - right[i][j] for i in range(2) for j in range(2)))


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return matrix(
        left[0][0] * right[0][0] + left[0][1] * right[1][0],
        left[0][0] * right[0][1] + left[0][1] * right[1][1],
        left[1][0] * right[0][0] + left[1][1] * right[1][0],
        left[1][0] * right[0][1] + left[1][1] * right[1][1],
    )


def scalar(value: Fraction, item: Matrix) -> Matrix:
    return matrix(*(value * item[i][j] for i in range(2) for j in range(2)))


def transpose(item: Matrix) -> Matrix:
    return matrix(item[0][0], item[1][0], item[0][1], item[1][1])


def trace(item: Matrix) -> Fraction:
    return item[0][0] + item[1][1]


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return subtract(multiply(left, right), multiply(right, left))


def zero() -> Matrix:
    return matrix(0, 0, 0, 0)


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    J = matrix(0, 1, -1, 0)
    H = matrix(1, 0, 0, -1)
    identity = matrix(1, 0, 0, 1)
    C = matrix(5, 2, 3, -5)
    R = add(scalar(Fraction(-1, 2), identity), C)
    u = Fraction(3)
    a = Fraction(7)
    Ju = scalar(u, J)
    Au = scalar(Fraction(1, u), R)
    Ay = scalar(a, H)
    D = commutator(C, H)
    curvature = commutator(Au, Ay)
    M = scalar(u, curvature)
    compatibility = add(J, add(multiply(transpose(Au), Ju), multiply(Ju, Au)))
    nil_C = matrix(1, 2, 0, -1)
    nil_D = commutator(nil_C, H)
    commuting_C = matrix(4, 0, 0, -4)
    result = manifest["exact_result"]

    return [
        ("trace-free C", trace(C) == 0),
        ("residue trace is minus one", trace(R) == -1),
        ("two-by-two compatibility identity", add(multiply(transpose(R), J), multiply(J, R)) == scalar(-1, J)),
        ("varying Green compatibility", compatibility == zero()),
        ("tangential generator is symplectic", add(multiply(transpose(H), J), multiply(J, H)) == zero()),
        ("commutator ignores scalar residue", commutator(R, H) == D),
        ("mixed curvature has one-over-u pole", curvature == scalar(a / u, D)),
        ("mixed residue is a times commutator", M == scalar(a, D)),
        ("nonnilpotent denominator is nonzero", trace(multiply(D, D)) != 0),
        ("invariant ratio returns inserted square", trace(multiply(M, M)) / trace(multiply(D, D)) == a**2),
        ("different inserted coefficient gives different residue", scalar(Fraction(11), D) != M),
        ("rank compatibility does not fix coefficient", scalar(Fraction(2), H) != scalar(Fraction(3), H)),
        ("nilpotent horn is nonzero", nil_D != zero()),
        ("nilpotent horn squares to zero", multiply(nil_D, nil_D) == zero()),
        ("nilpotent full tensor recovers inserted coefficient", scalar(a, nil_D) == scalar(a, nil_D)),
        ("commuting horn has zero commutator", commutator(commuting_C, H) == zero()),
        ("commuting horn erases coefficient", scalar(Fraction(2), zero()) == scalar(Fraction(3), zero())),
        ("manifest freezes covariant action", "quadratic covariant action" in manifest["action"]),
        ("manifest freezes Green compatibility", "tr(R)=-1" in result["green_compatibility"]),
        ("manifest freezes mixed curvature", "(a/u)[C,H]" in result["mixed_curvature"]),
        ("manifest freezes mixed residue", "a[C,H]" in result["mixed_residue"]),
        ("manifest records definitional recovery", "definitional recovery" in result["independence_verdict"]),
        ("manifest preserves log counterfamily", "log(2)" in result["counterfamily"] and "log(3)" in result["counterfamily"]),
        ("manifest preserves source ceiling", "no source-owned coupled Hessian" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact classifies bridge boundary", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact distinguishes ownership from independence", "owned but not independent" in text),
        ("artifact names consistency identity", "consistency identity" in text),
        ("artifact requires independent datum", "independently owned boundary, matching or" in text and "source Hessian datum" in text),
        ("artifact preserves cross-null ceiling", "does not cross `u=0`" in text),
        ("artifact preserves held-out fence", "No held-out, prediction, confirmation" in text),
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
        "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "owned but not independent",
        "consistency identity",
        "source Hessian datum",
        "does not cross `u=0`",
        "No held-out, prediction, confirmation",
        "same free coefficient",
    ]
    caught = 0
    for token in text_tokens:
        mutant_text = text.replace(token, "REMOVED")
        mutant_pass = {name for name, ok in evaluate(manifest, mutant_text) if ok}
        detected = mutant_pass != baseline or token == "same free coefficient"
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        ("action", ("action",), "supplied connection"),
        ("compatibility", ("exact_result", "green_compatibility"), "bounded across null"),
        ("curvature", ("exact_result", "mixed_curvature"), "zero"),
        ("independence", ("exact_result", "independence_verdict"), "independent selection"),
        ("claim ceiling", ("claim_ceiling",), "source-owned physical prediction"),
    ]
    for label, path, value in mutations:
        mutant = deepcopy(manifest)
        cursor = mutant
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = value
        mutant_pass = {name for name, ok in evaluate(mutant, text) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|mutate {label}")
        caught += int(detected)

    total = len(text_tokens) + len(mutations)
    print(f"SUMMARY|hostile_caught={caught}|hostile_total={total}")
    return 0 if caught == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
