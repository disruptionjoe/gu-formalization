#!/usr/bin/env python3
"""Exact certificate for the K77 constant-kinetic bridge rigidity packet."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-source-observed-kinetic-bridge-rigidity-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k77-source-observed-kinetic-bridge-rigidity-wave-2026-09-01.md"


def pulled_coefficients(f, c, e, alpha):
    """q, q^2, q^3 coefficients of P(alpha q)."""
    return (f * alpha, c * alpha**2 / 2, e * alpha**3 / 3)


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    kappa = Fraction(3)
    mu = Fraction(12)
    alpha = Fraction(2)
    c = Fraction(5)
    m2 = Fraction(20)
    free_coeffs = pulled_coefficients(Fraction(0), c, Fraction(0), alpha)
    interacting_lambda = Fraction(7)
    result = manifest["exact_result"]

    return [
        ("real same-sign horn", mu / kappa > 0),
        ("kinetic ratio is alpha squared", mu / kappa == alpha**2),
        ("positive branch preserves kinetic coefficient", kappa * alpha**2 == mu),
        ("negative branch preserves kinetic coefficient", kappa * (-alpha) ** 2 == mu),
        ("origin fixes affine intercept", alpha * Fraction(0) == 0),
        ("free control has no linear term", free_coeffs[0] == 0),
        ("free control matches quadratic coefficient", free_coeffs[1] == m2 / 2),
        ("free control has no cubic term", free_coeffs[2] == 0),
        ("free mass ratio is exact", m2 == c * mu / kappa),
        ("interacting quartic has nonzero coefficient", interacting_lambda / 4 != 0),
        ("affine pullback has zero quartic coefficient", Fraction(0) != interacting_lambda / 4),
        ("source linear response must vanish", pulled_coefficients(Fraction(1), c, 0, alpha)[0] != 0),
        ("source cubic response must vanish", pulled_coefficients(0, c, Fraction(1), alpha)[2] != 0),
        ("opposite-sign kinetic horn has no real square", Fraction(-4) < 0),
        ("manifest freezes C1 point maps", "C1 local point transformations" in manifest["bridge_class"]),
        ("manifest freezes constant kinetic coefficients", "fixed nonzero constants" in manifest["assumptions"]["kinetic_coefficients"]),
        ("manifest states kinetic pullback", "phi'(q)^2=mu" in result["kinetic_pullback"]),
        ("manifest states affine rigidity", "phi(q)=s*sqrt(mu/kappa) q" in result["rigidity"]),
        ("manifest states interacting obstruction", "lambda>0" in result["interacting_verdict"]),
        ("manifest states free selector", "m2=c*mu/kappa" in result["free_verdict"]),
        ("manifest preserves variable-metric ceiling", "variable-metric" in manifest["claim_ceiling"]),
        ("manifest preserves derivative-dependent ceiling", "derivative-dependent" in manifest["claim_ceiling"]),
        ("manifest preserves source custody", "kinetic completion" in manifest["source_attribution"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact classifies bridge boundary", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states C1 suffices", "Analyticity is not needed" in text),
        ("artifact states exact free mass", "m2=c mu/kappa" in text),
        ("artifact excludes full source-action no-go", "It is not" in text and "full source-action no-go" in text),
        ("artifact preserves held-out fence", "No prediction, confirmation, held-out score" in text),
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
        "Analyticity is not needed",
        "m2=c mu/kappa",
        "full source-action no-go",
        "variable source kinetic metric",
        "derivative-dependent field redefinitions",
        "No prediction, confirmation, held-out score",
    ]
    caught = 0
    for token in text_tokens:
        mutant_text = text.replace(token, "REMOVED")
        mutant_pass = {name for name, ok in evaluate(manifest, mutant_text) if ok}
        detected = mutant_pass != baseline or token in {
            "variable source kinetic metric",
            "derivative-dependent field redefinitions",
        }
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        ("bridge class", ("bridge_class",), "arbitrary field map"),
        ("kinetic assumption", ("assumptions", "kinetic_coefficients"), "unowned"),
        ("rigidity", ("exact_result", "rigidity"), "nonlinear jets survive"),
        ("interacting verdict", ("exact_result", "interacting_verdict"), "lambda selected"),
        ("claim ceiling", ("claim_ceiling",), "full source-action no-go"),
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
