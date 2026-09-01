#!/usr/bin/env python3
"""Exact certificate for the K77 I1B radial-domain indicial packet."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-i1b-radial-domain-indicial-classification-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k77-i1b-radial-domain-indicial-classification-wave-2026-09-01.md"


def exponent(p: Fraction, c: Fraction) -> Fraction:
    """Power of u in the squared weighted norm integrand."""
    return p + 1 - 2 * c


def integrable(p: Fraction, c: Fraction) -> bool:
    return exponent(p, c) > -1


def commutator_square_trace(s: Fraction) -> Fraction:
    """tr([sX,Z]^2) for X=[[0,1],[1,0]], Z=diag(1,-1)."""
    return -8 * s**2


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    p = Fraction(1)
    s = Fraction(1, 4)
    threshold = (p + 2) / 2
    result = manifest["exact_result"]
    result_flat = " ".join(json.dumps(result, sort_keys=True).split())

    return [
        ("Darboux threshold exact", threshold == Fraction(3, 2)),
        ("positive indicial mode integrable below threshold", integrable(p, s)),
        ("negative indicial mode integrable below threshold", integrable(p, -s)),
        ("threshold mode logarithmic", exponent(p, Fraction(3, 2)) == -1),
        ("supercritical positive mode excluded", not integrable(p, Fraction(2))),
        ("supercritical negative mode retained", integrable(p, Fraction(-2))),
        ("noncommuting curvature invariant nonzero", commutator_square_trace(s) == Fraction(-1, 2)),
        ("zero residue freedom gives zero commutator", commutator_square_trace(0) == 0),
        ("manifest freezes regular-singular model", "u*a*H" in manifest["radial_model"]),
        ("manifest distinguishes control pairing", "not the native alternating" in manifest["control_pairing"]),
        ("manifest states indicial family", "u*a*H does not enter" in result_flat),
        ("manifest states mode powers", "u^(1/2-c)" in result["mode_powers"]),
        ("manifest states weighted threshold", "c<(p+2)/2" in result["weighted_integrability"]),
        ("manifest states Darboux horns", "s<3/2" in result["darboux_threshold"] and "s>3/2" in result["darboux_threshold"]),
        ("manifest compares log coefficients", "log(2) and log(3)" in result["coefficient_verdict"]),
        ("manifest records noncommuting control", "-8s^2" in result["noncommuting_control"]),
        ("manifest preserves boundary owner gap", "self-adjoint or variational Lagrangian extension" in manifest["boundary_owner_gap"]),
        ("manifest preserves source custody", "repository-derived" in manifest["source_attribution"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact classifies bridge boundary", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact freezes bounded tangential order", "coefficient `u aH` is bounded and lower radial order" in text),
        ("artifact states exact threshold", "both modes are admissible for" in text and "`0<=s<3/2`" in text),
        ("artifact states coefficient blindness", "mode count is identical\nfor every finite `a`" in text),
        ("artifact preserves extension ceiling", "asymptotic space, not a\nself-adjoint or variational boundary condition" in text),
        ("artifact preserves positive-norm warning", "trace polynomial as a positive\nnorm" in text),
        ("artifact preserves held-out fence", "prediction or confirmation is obtained" in text),
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
        "coefficient `u aH` is bounded and lower radial order",
        "`0<=s<3/2`",
        "mode count is identical\nfor every finite `a`",
        "asymptotic space, not a\nself-adjoint or variational boundary condition",
        "trace polynomial as a positive\nnorm",
        "prediction or confirmation is obtained",
    ]
    caught = 0
    for token in text_tokens:
        mutant_text = text.replace(token, "REMOVED")
        mutant_pass = {name for name, ok in evaluate(manifest, mutant_text) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token.replace(chr(10), ' ')}")
        caught += int(detected)

    mutations = [
        ("radial model", ("radial_model",), "a enters residue"),
        ("control pairing", ("control_pairing",), "native positive norm"),
        ("indicial family", ("exact_result", "indicial_family"), "depends on a"),
        ("threshold", ("exact_result", "weighted_integrability"), "always finite"),
        ("coefficient verdict", ("exact_result", "coefficient_verdict"), "selects log(2)"),
        ("source custody", ("source_attribution",), "source-owned domain"),
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
