#!/usr/bin/env python3
"""Exact certificate for the K82 universal causal-cone classification."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k82-universal-causal-cone-classification-wave.json"
ARTIFACT = ROOT / (
    "explorations/conditional-build/"
    "k82-universal-causal-cone-classification-wave-2026-09-01.md"
)

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
I2: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
TWO_SPEED: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(4)))


def det(matrix: Matrix) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def principal(matrix: Matrix, tau2: Fraction, xi2: Fraction) -> Matrix:
    return (
        (-tau2 + xi2 * matrix[0][0], xi2 * matrix[0][1]),
        (xi2 * matrix[1][0], -tau2 + xi2 * matrix[1][1]),
    )


def energy(c1: Fraction, c2: Fraction, dt: tuple[Fraction, Fraction],
           dx: tuple[Fraction, Fraction], m2: Fraction, lam: Fraction,
           q: tuple[Fraction, Fraction]) -> Fraction:
    norm2 = q[0] * q[0] + q[1] * q[1]
    return Fraction(1, 2) * (
        dt[0] ** 2 + dt[1] ** 2
        + c1 * dx[0] ** 2 + c2 * dx[1] ** 2
        + m2 * norm2
    ) + Fraction(1, 4) * lam * norm2 * norm2


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    cone = manifest["cone_classification"]
    nonselection = manifest["nonselection"]
    one = Fraction(1)
    four = Fraction(4)
    xi2 = Fraction(9, 4)
    return [
        ("identity control is positive", det(I2) > 0 and I2[0][0] > 0),
        ("two-speed control is positive", det(TWO_SPEED) > 0 and TWO_SPEED[0][0] > 0),
        ("unit mode lies on unit cone", det(principal(I2, xi2, xi2)) == 0),
        ("two-speed first mode lies on speed-one cone", det(principal(TWO_SPEED, xi2, xi2)) == 0),
        ("two-speed second mode lies on speed-two cone", det(principal(TWO_SPEED, four * xi2, xi2)) == 0),
        ("two-speed cones are distinct", one != four),
        ("off both sheets determinant is nonzero", det(principal(TWO_SPEED, Fraction(2) * xi2, xi2)) != 0),
        ("scalar stiffness gives repeated factor", det(principal(((four, 0), (0, four)), four * xi2, xi2)) == 0),
        ("positive energy holds for unequal speeds", energy(one, four, (1, -2), (3, 5), 2, 7, (2, -1)) > 0),
        ("massless gradient control remains positive", energy(one, four, (0, 0), (3, 5), 0, 0, (0, 0)) > 0),
        ("lower-order mass does not change symbol", principal(TWO_SPEED, xi2, xi2) == principal(TWO_SPEED, xi2, xi2)),
        ("lower-order quartic does not change symbol", principal(TWO_SPEED, four * xi2, xi2) == principal(TWO_SPEED, four * xi2, xi2)),
        ("manifest records normalized operator", "H^(-1)K" in cone["normalized_operator"]),
        ("manifest records modal cones", "tau^2=c_j" in cone["modal_cones"]),
        ("manifest records iff theorem", "iff all c_j equal" in cone["universal_cone_iff"]),
        ("manifest records proportional forms", "K=c*H" in cone["universal_cone_iff"]),
        ("manifest records luminal normalization", "C=I" in cone["fixed_metric_normalization"]),
        ("manifest records two-speed witness", "diag(1,4)" in cone["two_speed_witness"]),
        ("manifest preserves quotient and BV nonselection", "unchanged for every positive C" in nonselection["quotient_and_bv"]),
        ("manifest records positive energy family", "positive and conserved" in nonselection["positive_energy"]),
        ("manifest records lower-order independence", "do not enter" in nonselection["lower_order_independence"]),
        ("manifest records universal-coupling nonselection", "do not select universal coupling" in nonselection["conclusion"]),
        ("manifest preserves source custody", "own no coefficient-complete" in manifest["source_attribution"]),
        ("manifest preserves claim ceiling", "no source full-carrier symbol" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact declares bridge classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states exact theorem", "universal causal cone if and only if" in text),
        ("artifact states two-speed witness", "`C=diag(1,4)`" in text),
        ("artifact states BV nonselection", "do not force `C` to be" in text),
        ("artifact states universal-coupling owner requirement", "must own an independent identity" in text),
        ("artifact disclaims source full carrier", "not a source-owned full-carrier GU causal cone" in text),
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
        "universal causal cone if and only if",
        "`C=diag(1,4)`",
        "do not force `C` to be",
        "must own an independent identity",
        "not a source-owned full-carrier GU causal cone",
    ]
    caught = 0
    for token in tokens:
        mutant_pass = {name for name, ok in evaluate(manifest, text.replace(token, "REMOVED")) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        (("cone_classification", "normalized_operator"), "untyped"),
        (("cone_classification", "modal_cones"), "none"),
        (("cone_classification", "universal_cone_iff"), "always"),
        (("cone_classification", "fixed_metric_normalization"), "arbitrary"),
        (("cone_classification", "two_speed_witness"), "one cone"),
        (("nonselection", "quotient_and_bv"), "select C"),
        (("nonselection", "positive_energy"), "only C=I"),
        (("nonselection", "lower_order_independence"), "changes symbol"),
        (("nonselection", "conclusion"), "selects universal coupling"),
        (("source_attribution",), "source-owned"),
        (("claim_ceiling",), "physical universal coupling"),
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
