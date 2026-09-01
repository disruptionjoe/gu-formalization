#!/usr/bin/env python3
"""Exact certificate for the K77 variable-metric bridge normal-form packet."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-source-observed-variable-metric-bridge-normal-form-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k77-source-observed-variable-metric-bridge-normal-form-wave-2026-09-01.md"


def selected_coefficients(h0, h1, h2, c, e, mu):
    """Observed m2, exact cubic-cancellation numerator, and lambda."""
    m2 = c * mu / h0
    cubic_numerator = 3 * c * h1 - 4 * e * h0
    lam = -mu**2 * (9 * c**2 * h2 - 2 * e**2 * h0) / (27 * c * h0**3)
    return m2, cubic_numerator, lam


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    h0 = Fraction(4)
    h1 = Fraction(32, 9)
    h2 = Fraction(0)
    c = Fraction(3)
    e = Fraction(2)
    mu = Fraction(9)
    m2, cubic_numerator, lam = selected_coefficients(h0, h1, h2, c, e, mu)
    result = manifest["exact_result"]

    return [
        ("positive source metric at origin", h0 > 0),
        ("positive observed kinetic coefficient", mu > 0),
        ("cubic-cancellation metric jet", h1 == 4 * e * h0 / (3 * c)),
        ("quadratic coefficient selected", m2 == Fraction(27, 4)),
        ("observed cubic coefficient vanishes", cubic_numerator == 0),
        ("nonzero quartic generated", lam == Fraction(1, 2)),
        ("constant metric with cubic source fails cubic cancellation", Fraction(0) != 4 * e * h0 / (3 * c)),
        ("constant metric horn has zero quartic when source cubic vanishes", selected_coefficients(h0, 0, 0, c, 0, mu)[2] == 0),
        ("metric second jet changes quartic", selected_coefficients(h0, h1, 1, c, e, mu)[2] != lam),
        ("manifest freezes positive metric", "h(t)>0 fixed independently" in manifest["source_lagrangian"]),
        ("manifest freezes point-map class", "C1 local point transformations" in manifest["bridge_class"]),
        ("manifest defines arc length", "sqrt(h(s))" in result["arc_length_coordinate"]),
        ("manifest states geodesic normal form", "F(phi(q))=s*sqrt(mu)*q" in result["kinetic_normal_form"]),
        ("manifest states unique bridge", "F^{-1}" in result["unique_local_bridge"]),
        ("manifest states mass formula", "m2=c*mu/h0" in result["quadratic_coefficient"]),
        ("manifest states cubic cancellation", "h1=4*e*h0/(3*c)" in result["cubic_cancellation"]),
        ("manifest states quartic formula", "9*c^2*h2" in result["quartic_coefficient"]),
        ("manifest distinguishes fitted metric", "target-fitted" in result["ownership_verdict"]),
        ("manifest preserves derivative ceiling", "derivative-dependent" in manifest["claim_ceiling"]),
        ("manifest preserves source custody", "repository-derived" in manifest["source_attribution"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact classifies bridge boundary", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact names affine geodesic coordinate", "affine in source geodesic distance" in text),
        ("artifact records exact positive control", "m2=27/4" in text and "lambda=1/2" in text),
        ("artifact distinguishes ownership", "Ownership is the discriminator" in text),
        ("artifact fences target fitting", "target-fitting recipe" in text),
        ("artifact preserves full-carrier ceiling", "constructs neither source ownership nor a full-carrier" in text),
        ("artifact preserves broader map classes", "derivative-dependent maps" in text and "nonlocal maps" in text),
        ("artifact preserves held-out fence", "No source-action, physical-state, prediction, confirmation" in text),
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
        "affine in source geodesic distance",
        "m2=27/4",
        "lambda=1/2",
        "Ownership is the discriminator",
        "target-fitting recipe",
        "constructs neither source ownership nor a full-carrier",
        "No source-action, physical-state, prediction, confirmation",
    ]
    caught = 0
    for token in text_tokens:
        mutant_text = text.replace(token, "REMOVED")
        mutant_pass = {name for name, ok in evaluate(manifest, mutant_text) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        ("source metric", ("source_lagrangian",), "target-fitted metric"),
        ("normal form", ("exact_result", "kinetic_normal_form"), "arbitrary map"),
        ("quartic", ("exact_result", "quartic_coefficient"), "lambda arbitrary"),
        ("ownership", ("exact_result", "ownership_verdict"), "automatic source selection"),
        ("claim ceiling", ("claim_ceiling",), "full source-action equivalence"),
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
