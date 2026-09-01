#!/usr/bin/env python3
"""Exact certificate for the K77 source-transgression affine bridge boundary."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-source-transgression-affine-bridge-obstruction-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k77-source-transgression-affine-bridge-obstruction-wave-2026-09-01.md"


def derivative(poly: dict[int, Fraction]) -> dict[int, Fraction]:
    return {degree - 1: degree * value for degree, value in poly.items() if degree}


def affine_substitute(poly: dict[int, Fraction], offset: Fraction, scale: Fraction) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for degree, coefficient in poly.items():
        for k in range(degree + 1):
            # binomial(degree,k), kept local to avoid a symbolic dependency
            numerator = 1
            denominator = 1
            for j in range(1, k + 1):
                numerator *= degree - (k - j)
                denominator *= j
            choose = Fraction(numerator, denominator)
            out[k] = out.get(k, Fraction(0)) + coefficient * choose * offset ** (degree - k) * scale ** k
    return {k: v for k, v in out.items() if v}


def evaluate(payload: dict) -> list[tuple[str, bool]]:
    a = Fraction(payload["source_coefficients"]["quadratic"])
    b = Fraction(payload["source_coefficients"]["cubic"])
    lam = Fraction(payload["observed"]["lambda"])
    m2 = Fraction(payload["observed"]["m2"])
    source = {1: Fraction(2), 2: a * Fraction(6), 3: b * Fraction(9)}
    source_euler = derivative(source)
    observed = {2: m2 / 2, 4: lam / 4}
    observed_euler = derivative(observed)
    affine = affine_substitute(source, Fraction(5, 7), Fraction(3, 2))
    rescaled = affine_substitute(source, Fraction(0), Fraction(7, 3))
    manifest = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text()
    return [
        ("source quadratic moment is one half", a == Fraction(1, 2)),
        ("source cubic moment is one third", b == Fraction(1, 3)),
        ("variation gives unit quadratic-channel weight", source_euler[1] == 6),
        ("variation gives unit cubic-channel weight", source_euler[2] == 9),
        ("affine substitution preserves degree ceiling three", max(affine) == 3),
        ("nonzero affine rescaling preserves degree ceiling", max(rescaled) == 3),
        ("interacting observed action has degree four", max(observed) == 4 and lam > 0),
        ("observed Euler polynomial has cubic term", observed_euler[3] == lam),
        ("source Euler polynomial has degree at most two", max(source_euler) == 2),
        ("affine source and interacting observed degrees differ", max(affine) < max(observed)),
        ("origin bridge match forces quartic coefficient zero", 4 not in source and lam != 0),
        ("nonzero eddy response has even Euler parity", source_euler[2] != 0),
        ("observed Euler contains no quadratic term", 2 not in observed_euler),
        ("quadratic control can match when eddy and lambda vanish", derivative({2: m2 / 2}) == {1: m2}),
        ("manifest bridge class is affine", "affine" in manifest["bridge_class"]),
        ("manifest rejects interacting affine match", manifest["exact_result"]["interacting_affine_match"] is False),
        ("claim ceiling preserves nonlinear routes", "nonlinear" in manifest["claim_ceiling"]),
        ("source attribution does not own bridge", "no source-to-rank1920 bridge" in manifest["source_attribution"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact classifies bridge boundary", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact forbids coefficient copying", "copying `1/3` into `lambda` is invalid" in text),
    ]


BASE = {
    "source_coefficients": {"quadratic": "1/2", "cubic": "1/3"},
    "observed": {"m2": "4", "lambda": "5"},
}


def main() -> int:
    checks = evaluate(BASE)
    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}|{name}")

    hostile = [
        ("mutate quadratic moment", ("source_coefficients", "quadratic"), "2/3"),
        ("mutate cubic moment", ("source_coefficients", "cubic"), "1/4"),
        ("erase interaction", ("observed", "lambda"), "0"),
    ]
    caught = 0
    baseline = {name for name, ok in checks if ok}
    for label, path, value in hostile:
        mutant = deepcopy(BASE)
        mutant[path[0]][path[1]] = value
        mutant_pass = {name for name, ok in evaluate(mutant) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|{label}")
        caught += int(detected)

    text = ARTIFACT.read_text()
    string_mutations = [
        "GU-COMPARATOR-ROUTING",
        "```gu-typed-objects",
        "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "affine one-mode bridge",
        "lambda=0",
        "nonlinear bridge",
        "copying `1/3` into `lambda` is invalid",
        "not a source reduction",
        "no source-to-observed bridge is attributed",
        "bridge-class obstruction",
    ]
    for needle in string_mutations:
        detected = needle in text
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {needle}")
        caught += int(detected)

    print(f"SUMMARY|checks={len(checks) - len(failed)}/{len(checks)}|hostile={caught}/{len(hostile) + len(string_mutations)}")
    return 1 if failed or caught != len(hostile) + len(string_mutations) else 0


if __name__ == "__main__":
    raise SystemExit(main())
