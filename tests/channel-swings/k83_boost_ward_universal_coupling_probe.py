#!/usr/bin/env python3
"""Exact certificate for the K83 boost-Ward universal-coupling boundary."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k83-boost-ward-universal-coupling-wave.json"
ARTIFACT = ROOT / (
    "explorations/conditional-build/"
    "k83-boost-ward-universal-coupling-wave-2026-09-01.md"
)

Vector = tuple[Fraction, Fraction]
Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
I2: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
COMMON_NONUNIT: Matrix = ((Fraction(2), Fraction(0)), (Fraction(0), Fraction(2)))
TWO_SPEED: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(4)))


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def scale(value: Fraction, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(value * matrix[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def bilinear(left: Vector, matrix: Matrix, right: Vector) -> Fraction:
    return sum(left[i] * matrix[i][j] * right[j] for i in range(2) for j in range(2))


def boost_cross_coefficient(h: Matrix, k: Matrix, cosh: Fraction,
                            sinh: Fraction) -> Matrix:
    return scale(2 * sinh * cosh, subtract(k, h))


def stress_skew(h: Matrix, k: Matrix, dt: Vector, dx: Vector) -> Fraction:
    return bilinear(dt, subtract(h, k), dx)


def energy(h: Matrix, k: Matrix, dt: Vector, dx: Vector) -> Fraction:
    return Fraction(1, 2) * (bilinear(dt, h, dt) + bilinear(dx, k, dx))


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    ward = manifest["ward_classification"]
    boundary = manifest["common_cone_boundary"]
    zero: Matrix = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))
    cosh = Fraction(5, 4)
    sinh = Fraction(3, 4)
    e1: Vector = (Fraction(1), Fraction(0))
    e2: Vector = (Fraction(0), Fraction(1))
    return [
        ("rational boost lies on unit hyperbola", cosh * cosh - sinh * sinh == 1),
        ("unit forms have zero boost cross coefficient", boost_cross_coefficient(I2, I2, cosh, sinh) == zero),
        ("common nonunit form has nonzero boost cross coefficient", boost_cross_coefficient(I2, COMMON_NONUNIT, cosh, sinh) != zero),
        ("two-speed form has nonzero boost cross coefficient", boost_cross_coefficient(I2, TWO_SPEED, cosh, sinh) != zero),
        ("unit forms have zero stress skew on first mode", stress_skew(I2, I2, e1, e1) == 0),
        ("unit forms have zero stress skew on second mode", stress_skew(I2, I2, e2, e2) == 0),
        ("common nonunit control exposes stress skew", stress_skew(I2, COMMON_NONUNIT, e1, e1) == -1),
        ("two-speed control exposes second-mode stress skew", stress_skew(I2, TWO_SPEED, e2, e2) == -3),
        ("cross-mode stress skew remains zero for diagonal control", stress_skew(I2, TWO_SPEED, e1, e2) == 0),
        ("common nonunit control has positive energy", energy(I2, COMMON_NONUNIT, (1, -2), (3, 4)) > 0),
        ("two-speed control has positive energy", energy(I2, TWO_SPEED, (1, -2), (3, 4)) > 0),
        ("boost coefficient vanishes exactly with form difference", boost_cross_coefficient(I2, I2, cosh, sinh) == scale(2 * sinh * cosh, subtract(I2, I2))),
        ("manifest records boost cross coefficient", "2*sinh(theta)*cosh(theta)*(K-H)" in ward["boost_cross_coefficient"]),
        ("manifest records mixed stress identity", "T_0x-T_x0" in ward["mixed_stress_identity"]),
        ("manifest records iff theorem", "iff K=H" in ward["boost_symmetry_iff"]),
        ("manifest records unit normalized conclusion", "H^(-1)K=I" in ward["fixed_metric_conclusion"]),
        ("manifest records scope", "first derivatives" in ward["scope"]),
        ("manifest separates common cone", "K=c*H" in boundary["common_cone_only"]),
        ("manifest records common nonunit control", "K=2I" in boundary["common_nonunit_control"]),
        ("manifest records two-speed control", "diag(1,4)" in boundary["two_speed_control"]),
        ("manifest records nonselection", "do not select" in boundary["nonselection"]),
        ("manifest preserves source custody", "own no coefficient-complete" in manifest["source_attribution"]),
        ("manifest preserves claim ceiling", "no source full-carrier stress" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact declares bridge classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states boost mixed coefficient", "2 sinh(theta) cosh(theta) (K-H)" in text),
        ("artifact states stress Ward identity", "T_0x - T_x0" in text),
        ("artifact states exact unit theorem", "K = H" in text),
        ("artifact states common-cone distinction", "common cone does not itself show universal coupling" in text),
        ("artifact states common nonunit witness", "`H=I`, `K=2I`" in text),
        ("artifact disclaims source stress", "not a source-owned GU stress tensor" in text),
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
        "2 sinh(theta) cosh(theta) (K-H)",
        "T_0x - T_x0",
        "K = H",
        "common cone does not itself show universal coupling",
        "`H=I`, `K=2I`",
        "not a source-owned GU stress tensor",
    ]
    caught = 0
    for token in tokens:
        mutant_pass = {name for name, ok in evaluate(manifest, text.replace(token, "REMOVED")) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        (("ward_classification", "boost_cross_coefficient"), "none"),
        (("ward_classification", "mixed_stress_identity"), "symmetric always"),
        (("ward_classification", "boost_symmetry_iff"), "arbitrary K"),
        (("ward_classification", "fixed_metric_conclusion"), "K=cH"),
        (("ward_classification", "scope"), "all field theories"),
        (("common_cone_boundary", "common_cone_only"), "same as boost symmetry"),
        (("common_cone_boundary", "common_nonunit_control"), "none"),
        (("common_cone_boundary", "two_speed_control"), "none"),
        (("common_cone_boundary", "nonselection"), "selects boost symmetry"),
        (("source_attribution",), "source-owned"),
        (("claim_ceiling",), "GU dynamical metric theorem"),
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
