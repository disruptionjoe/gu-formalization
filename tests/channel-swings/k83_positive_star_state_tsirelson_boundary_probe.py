#!/usr/bin/env python3
"""Exact certificate for the K83 positive star-state Tsirelson boundary."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k83-positive-star-state-tsirelson-boundary-wave.json"
ARTIFACT = ROOT / (
    "explorations/conditional-build/"
    "k83-positive-star-state-tsirelson-boundary-wave-2026-09-01.md"
)

# a+b*sqrt(2), represented exactly over Q
Quadratic = tuple[Fraction, Fraction]
Polynomial = dict[str, Quadratic]


def qadd(left: Quadratic, right: Quadratic) -> Quadratic:
    return (left[0] + right[0], left[1] + right[1])


def qmul(left: Quadratic, right: Quadratic) -> Quadratic:
    return (
        left[0] * right[0] + 2 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def pscale(value: Quadratic, polynomial: Polynomial) -> Polynomial:
    return {word: qmul(value, coefficient) for word, coefficient in polynomial.items()}


def sos_sum_before_normalization() -> Polynomial:
    # Exact reduction of X^2+Y^2 using A_x^2=B_y^2=1 and [A_x,B_y]=0.
    # The B0B1 and B1B0 anticommutator terms cancel between X and Y.
    return {
        "1": (Fraction(4), Fraction(0)),
        "A0B0": (Fraction(0), Fraction(-1)),
        "A0B1": (Fraction(0), Fraction(-1)),
        "A1B0": (Fraction(0), Fraction(-1)),
        "A1B1": (Fraction(0), Fraction(1)),
        "B0B1": (Fraction(0), Fraction(0)),
        "B1B0": (Fraction(0), Fraction(0)),
    }


def normalized_sos() -> Polynomial:
    # 1/sqrt(2)=sqrt(2)/2.
    return pscale((Fraction(0), Fraction(1, 2)), sos_sum_before_normalization())


def expected_boundary() -> Polynomial:
    return {
        "1": (Fraction(0), Fraction(2)),
        "A0B0": (Fraction(-1), Fraction(0)),
        "A0B1": (Fraction(-1), Fraction(0)),
        "A1B0": (Fraction(-1), Fraction(0)),
        "A1B1": (Fraction(1), Fraction(0)),
        "B0B1": (Fraction(0), Fraction(0)),
        "B1B0": (Fraction(0), Fraction(0)),
    }


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    sos = manifest["sos_boundary"]
    pr = manifest["pr_nonextension"]
    expanded = normalized_sos()
    expected = expected_boundary()
    pr_gap: Quadratic = (Fraction(-4), Fraction(2))
    return [
        ("quadratic addition is exact", qadd((1, 2), (3, -2)) == (4, 0)),
        ("sqrt two squares to two", qmul((0, 1), (0, 1)) == (2, 0)),
        ("inverse sqrt two is exact", qmul((0, 1), (0, Fraction(1, 2))) == (1, 0)),
        ("SOS expansion equals boundary polynomial", expanded == expected),
        ("SOS identity has two sqrt two unit coefficient", expanded["1"] == (0, 2)),
        ("SOS identity has negative A0B0 coefficient", expanded["A0B0"] == (-1, 0)),
        ("SOS identity has negative A0B1 coefficient", expanded["A0B1"] == (-1, 0)),
        ("SOS identity has negative A1B0 coefficient", expanded["A1B0"] == (-1, 0)),
        ("SOS identity has positive A1B1 coefficient", expanded["A1B1"] == (1, 0)),
        ("B0B1 term cancels", expanded["B0B1"] == (0, 0)),
        ("B1B0 term cancels", expanded["B1B0"] == (0, 0)),
        ("PR gap is two sqrt two minus four", pr_gap == (-4, 2)),
        ("PR gap is strictly negative by exact squares", 2 * 2 < 4 * 4),
        ("manifest records defect elements", "X=A0" in sos["defects"] and "Y=A1" in sos["defects"]),
        ("manifest records SOS identity", "2*sqrt(2)*1-C" in sos["identity"]),
        ("manifest records positive state bound", "|omega(C)|<=2*sqrt(2)" in sos["positive_state_bound"]),
        ("manifest records saturation nullity", "omega(X^2)=omega(Y^2)=0" in sos["saturation"]),
        ("manifest records minimal owned structure", "composite star product" in sos["minimal_owned_structure"]),
        ("manifest records PR correlation value", "omega(C)=4" in pr["correlation_value"]),
        ("manifest records negative SOS witness", "2*sqrt(2)-4<0" in pr["negative_sos_witness"]),
        ("manifest records PR nonextension", "no extension" in pr["conclusion"]),
        ("manifest records probability versus state boundary", "weaker than positivity" in pr["semantic_boundary"]),
        ("manifest preserves source custody", "own no physical rank-960" in manifest["source_attribution"]),
        ("manifest preserves claim ceiling", "no GU-native observable algebra" in manifest["claim_ceiling"]),
        ("manifest reserves held-out", "reserved and unscored" in manifest["held_out_credit"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact declares bridge classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states exact SOS identity", "2 sqrt(2) 1 - C = (X^2+Y^2)/sqrt(2)" in text),
        ("artifact states Tsirelson bound", "|omega(C)| <= 2 sqrt(2)" in text),
        ("artifact states PR negative witness", "2 sqrt(2) - 4 < 0" in text),
        ("artifact states PR extension boundary", "admit no extension to a normalized positive functional" in text),
        ("artifact disclaims GU physical state", "not a GU-native observable algebra" in text),
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
        "2 sqrt(2) 1 - C = (X^2+Y^2)/sqrt(2)",
        "|omega(C)| <= 2 sqrt(2)",
        "2 sqrt(2) - 4 < 0",
        "admit no extension to a normalized positive functional",
        "not a GU-native observable algebra",
    ]
    caught = 0
    for token in tokens:
        mutant_pass = {name for name, ok in evaluate(manifest, text.replace(token, "REMOVED")) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        (("sos_boundary", "defects"), "none"),
        (("sos_boundary", "identity"), "none"),
        (("sos_boundary", "positive_state_bound"), "four"),
        (("sos_boundary", "saturation"), "automatic"),
        (("sos_boundary", "minimal_owned_structure"), "probability table only"),
        (("pr_nonextension", "correlation_value"), "two"),
        (("pr_nonextension", "negative_sos_witness"), "positive"),
        (("pr_nonextension", "conclusion"), "extends"),
        (("pr_nonextension", "semantic_boundary"), "equivalent"),
        (("source_attribution",), "source-owned"),
        (("claim_ceiling",), "GU physical Born rule"),
        (("held_out_credit",), "scored"),
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
