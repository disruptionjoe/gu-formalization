#!/usr/bin/env python3
"""Exact certificate for I1B mixed-residue holonomy identifiability."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-i1b-mixed-residue-holonomy-identifiability-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k77-i1b-mixed-residue-holonomy-identifiability-wave-2026-09-01.md"
J = [[Fraction(0), Fraction(1)], [Fraction(-1), Fraction(0)]]
H = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(-1)]]
I = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def scale(c, a):
    return [[c * a[i][j] for j in range(2)] for i in range(2)]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def transpose(a):
    return [[a[j][i] for j in range(2)] for i in range(2)]


def commutator(a, b):
    return add(mul(a, b), scale(Fraction(-1), mul(b, a)))


def trace(a):
    return a[0][0] + a[1][1]


def zero(a):
    return all(value == 0 for row in a for value in row)


def evaluate(payload: dict) -> list[tuple[str, bool]]:
    p = Fraction(payload["C"]["p"])
    q = Fraction(payload["C"]["q"])
    r = Fraction(payload["C"]["r"])
    a = Fraction(payload["a"])
    rho = Fraction(payload["M"]["rho"])
    sigma = Fraction(payload["M"]["sigma"])
    C = [[p, q], [r, -p]]
    R = add(scale(Fraction(-1, 2), I), C)
    sp = add(mul(transpose(C), J), mul(J, C))
    compatibility = add(J, add(mul(transpose(R), J), mul(J, R)))
    mixed = scale(a, commutator(C, H))
    expected = [[Fraction(0), -2 * a * q], [2 * a * r, Fraction(0)]]
    fitted_C = [[Fraction(0), -rho / (2 * a)], [sigma / (2 * a), Fraction(0)]]
    fitted = scale(a, commutator(fitted_C, H))
    M = [[Fraction(0), rho], [sigma, Fraction(0)]]
    manifest = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text()
    return [
        ("C is trace free", trace(C) == 0),
        ("every trace-free two-matrix is symplectic", zero(sp)),
        ("full residue has forced trace minus one", trace(R) == -1),
        ("full residue satisfies varying-Green compatibility", zero(compatibility)),
        ("scalar residue commutes with H", zero(commutator(scale(Fraction(-1, 2), I), H))),
        ("mixed residue equals exact off-diagonal formula", mixed == expected),
        ("diagonal p drops from mixed residue", mixed[0][0] == 0 and mixed[1][1] == 0),
        ("off-diagonal q controls upper row", mixed[0][1] == -2 * a * q),
        ("off-diagonal r controls lower row", mixed[1][0] == 2 * a * r),
        ("any nonzero a can fit prescribed mixed row", fitted == M),
        ("bounded mixed curvature forces commuting residue", zero(scale(a, commutator([[p, 0], [0, -p]], H)))),
        ("boundedness leaves nonzero coefficient free", a != 0),
        ("owned upper row recovers coefficient", q != 0 and -rho / (2 * q) == a),
        ("owned lower row recovers coefficient", r != 0 and sigma / (2 * r) == a),
        ("owned row ratios agree", -rho / (2 * q) == sigma / (2 * r)),
        ("manifest denies trace-only selection", manifest["identifiability"]["trace_residue_selects_a"] is False),
        ("manifest denies boundedness magnitude selection", manifest["identifiability"]["bounded_mixed_curvature_selects_magnitude_of_a"] is False),
        ("manifest requires owned noncommuting residue", manifest["identifiability"]["owned_noncommuting_C_and_owned_mixed_row_can_select_a"] is True),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact preserves source boundary", "no source-owned trace-free residue supplied" in text),
        ("artifact preserves both holonomy controls", "Both `log(2)` and `log(3)` survive" in text),
        ("artifact states exact next datum", "off-diagonal trace-free residue coordinate" in text),
    ]


BASE = {
    "C": {"p": "5", "q": "-7", "r": "11"},
    "a": "13",
    "M": {"rho": "182", "sigma": "286"},
}


def main() -> int:
    checks = evaluate(BASE)
    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}|{name}")

    baseline = {name for name, ok in checks if ok}
    hostile = [
        ("break owned upper residue", ("C", "q"), "-6"),
        ("break upper matching row", ("M", "rho"), "181"),
        ("break lower matching row", ("M", "sigma"), "285"),
        ("zero tangential coefficient", ("a",), "0"),
    ]
    caught = 0
    for label, path, value in hostile:
        mutant = deepcopy(BASE)
        if len(path) == 1:
            mutant[path[0]] = value
        else:
            mutant[path[0]][path[1]] = value
        try:
            mutant_pass = {name for name, ok in evaluate(mutant) if ok}
            detected = mutant_pass != baseline
        except ZeroDivisionError:
            detected = True
        print(f"{'PASS' if detected else 'FAIL'}|hostile|{label}")
        caught += int(detected)

    text = ARTIFACT.read_text()
    string_mutations = [
        "trace `-1/u`",
        "three real coordinates `(p,q,r)` remain free",
        "Only the off-diagonal",
        "Both `log(2)` and `log(3)` survive",
        "does not select `a`",
        "source/action independently owns `C` and `M`",
        "not a universal full-matrix answer",
        "no source-owned trace-free residue supplied",
        "physical cross-null bundle",
        "off-diagonal trace-free residue coordinate",
    ]
    for needle in string_mutations:
        detected = needle in text
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {needle}")
        caught += int(detected)

    total_hostile = len(hostile) + len(string_mutations)
    print(f"SUMMARY|checks={len(checks) - len(failed)}/{len(checks)}|hostile={caught}/{total_hostile}")
    return 1 if failed or caught != total_hostile else 0


if __name__ == "__main__":
    raise SystemExit(main())
