#!/usr/bin/env python3
"""Exact certificate for the K77 cross-null curvature-integrability packet."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-i1b-degenerate-measure-curvature-integrability-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k77-i1b-degenerate-measure-curvature-integrability-wave-2026-09-01.md"

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


def trace(item: Matrix) -> Fraction:
    return item[0][0] + item[1][1]


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return subtract(multiply(left, right), multiply(right, left))


def radial_integrable(power: int) -> bool:
    """Whether integral_0^1 u^(power-2) du is finite."""
    return power > 1


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    H = matrix(1, 0, 0, -1)
    C = matrix(5, 2, 3, -5)
    D = commutator(C, H)
    D2_trace = trace(multiply(D, D))
    nil_C = matrix(1, 2, 0, -1)
    nil_D = commutator(nil_C, H)
    commuting_C = matrix(4, 0, 0, -4)
    zero = matrix(0, 0, 0, 0)
    a = Fraction(7)
    result = manifest["exact_result"]

    return [
        ("nonnilpotent commutator is nonzero", D != zero),
        ("nonnilpotent invariant is nonzero", D2_trace == -48),
        ("mixed-action coefficient is nonzero", a**2 * D2_trace != 0),
        ("unweighted density diverges", not radial_integrable(0)),
        ("Darboux Pfaffian density is logarithmic", not radial_integrable(1)),
        ("faster vanishing density is finite", radial_integrable(2)),
        ("zero coefficient removes divergence", Fraction(0) ** 2 * D2_trace == 0),
        ("distinct nonzero coefficients both diverge", Fraction(2) ** 2 * D2_trace != 0 and Fraction(3) ** 2 * D2_trace != 0),
        ("nilpotent commutator is nonzero", nil_D != zero),
        ("nilpotent square vanishes", multiply(nil_D, nil_D) == zero),
        ("nilpotent trace invariant vanishes", trace(multiply(nil_D, nil_D)) == 0),
        ("commuting horn has zero curvature", commutator(commuting_C, H) == zero),
        ("manifest freezes weighted measure", "u^p du dy" in manifest["measure_family"]),
        ("manifest separates bare and counterterm laws", "separately from counterterm" in manifest["action_test"]),
        ("manifest states radial threshold", "iff p>1" in result["radial_factor"]),
        ("manifest states nonnilpotent zero selector", "forces a=0" in result["nonnilpotent_horn"]),
        ("manifest states Darboux logarithm", "log(1/epsilon)" in result["darboux_measure_horn"]),
        ("manifest preserves both log candidates", "log(2)" in result["darboux_measure_horn"] and "log(3)" in result["darboux_measure_horn"]),
        ("manifest states nilpotent blindness", "trace-power invariant vanishes" in result["nilpotent_horn"]),
        ("manifest states commuting blindness", "F_uy=0" in result["commuting_horn"]),
        ("manifest states counterterm nonselection", "rather than selects" in result["counterterm_horn"]),
        ("manifest preserves source ceiling", "no source-owned measure/action/domain law" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact classifies bridge boundary", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact names native density horn", "native Darboux density `p=1`" in text),
        ("artifact rejects both nonzero candidates", "candidate law does not choose between them; it rejects both" in text),
        ("artifact preserves nilpotent horn", "nonzero nilpotent" in text),
        ("artifact separates renormalization", "renormalizes rather than selects" in text),
        ("artifact rejects positive-norm inference", "indefinite trace" in text and "positive physical norm" in text),
        ("artifact preserves held-out fence", "No source-action" in text and "physical-quotient, prediction, confirmation" in text),
        ("artifact preserves null-stratum ceiling", "does not extend through `u=0`" in text),
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
        "native Darboux density `p=1`",
        "candidate law does not choose between them; it rejects both",
        "nonzero nilpotent",
        "renormalizes rather than selects",
        "positive physical norm",
        "does not extend through `u=0`",
    ]
    caught = 0
    for token in text_tokens:
        mutant_text = text.replace(token, "REMOVED")
        mutant_pass = {name for name, ok in evaluate(manifest, mutant_text) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        ("measure", ("measure_family",), "constant measure only"),
        ("radial threshold", ("exact_result", "radial_factor"), "always finite"),
        ("nonnilpotent horn", ("exact_result", "nonnilpotent_horn"), "selects log(2)"),
        ("counterterm horn", ("exact_result", "counterterm_horn"), "selects log(3)"),
        ("claim ceiling", ("claim_ceiling",), "source-owned physical boundary law"),
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
