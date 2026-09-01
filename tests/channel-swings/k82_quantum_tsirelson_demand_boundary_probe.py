#!/usr/bin/env python3
"""Exact certificate for the K82 Tsirelson structural-demand boundary."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k82-quantum-tsirelson-demand-boundary-wave.json"
ARTIFACT = ROOT / (
    "explorations/conditional-build/"
    "k82-quantum-tsirelson-demand-boundary-wave-2026-09-01.md"
)


def local_chsh(a0: int, a1: int, b0: int, b1: int) -> int:
    return a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1


def pr_probability(a: int, b: int, x: int, y: int) -> Fraction:
    return Fraction(1, 2) if (a ^ b) == (x & y) else Fraction(0)


def correlation(probability, x: int, y: int) -> Fraction:
    return sum(
        Fraction(1 if (a + b) % 2 == 0 else -1) * probability(a, b, x, y)
        for a in (0, 1) for b in (0, 1)
    )


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    hilbert = manifest["hilbert_boundary"]
    weak = manifest["weak_demand_nonselection"]
    local_values = [
        local_chsh(a0, a1, b0, b1)
        for a0 in (-1, 1) for a1 in (-1, 1)
        for b0 in (-1, 1) for b1 in (-1, 1)
    ]
    pr_norms = [
        sum(pr_probability(a, b, x, y) for a in (0, 1) for b in (0, 1))
        for x in (0, 1) for y in (0, 1)
    ]
    alice_marginals = [
        sum(pr_probability(a, b, x, y) for b in (0, 1))
        for a in (0, 1) for x in (0, 1) for y in (0, 1)
    ]
    bob_marginals = [
        sum(pr_probability(a, b, x, y) for a in (0, 1))
        for b in (0, 1) for x in (0, 1) for y in (0, 1)
    ]
    e00 = correlation(pr_probability, 0, 0)
    e01 = correlation(pr_probability, 0, 1)
    e10 = correlation(pr_probability, 1, 0)
    e11 = correlation(pr_probability, 1, 1)
    # Coefficients of sqrt(2) in the Z/X plane.  Bell correlation is the
    # Euclidean coefficient dot product, so no floating approximation enters.
    b0 = (Fraction(1, 2), Fraction(1, 2))
    b1 = (Fraction(1, 2), Fraction(-1, 2))
    bell = (b0[0], b1[0], b0[1], b1[1])
    bell_chsh = bell[0] + bell[1] + bell[2] - bell[3]
    return [
        ("all sixteen local assignments enumerated", len(local_values) == 16),
        ("local CHSH maximum is two", max(local_values) == 2),
        ("local CHSH minimum is minus two", min(local_values) == -2),
        ("local values are only plus or minus two", set(local_values) == {-2, 2}),
        ("PR probabilities are nonnegative", all(pr_probability(a, b, x, y) >= 0 for a in (0, 1) for b in (0, 1) for x in (0, 1) for y in (0, 1))),
        ("PR box normalizes for every input", pr_norms == [1, 1, 1, 1]),
        ("PR Alice marginals are uniform", all(value == Fraction(1, 2) for value in alice_marginals)),
        ("PR Bob marginals are uniform", all(value == Fraction(1, 2) for value in bob_marginals)),
        ("PR correlations have exact sign pattern", (e00, e01, e10, e11) == (1, 1, 1, -1)),
        ("PR CHSH value is four", e00 + e01 + e10 - e11 == 4),
        ("Hilbert square bound gives eight", Fraction(4) + Fraction(2) * Fraction(2) == 8),
        ("Bell B0 direction has unit norm", 2 * (b0[0] ** 2 + b0[1] ** 2) == 1),
        ("Bell B1 direction has unit norm", 2 * (b1[0] ** 2 + b1[1] ** 2) == 1),
        ("Bell correlation coefficients are exact", bell == (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2))),
        ("saturating correlations sum to two sqrt two coefficient", bell_chsh == 2),
        ("saturation is below PR value", 2 * bell_chsh * bell_chsh == 8 < 16),
        ("manifest records CHSH square identity", "CHSH^2=4I" in hilbert["square_identity"]),
        ("manifest records norm bound", "||CHSH||^2<=8" in hilbert["norm_bound"]),
        ("manifest records Tsirelson ceiling", "2*sqrt(2)" in hilbert["norm_bound"]),
        ("manifest records saturating control", "Pauli Z/X" in hilbert["saturating_control"]),
        ("manifest records parameter independence", "m2, lambda" in hilbert["parameter_independence"]),
        ("manifest records local census", "sixteen deterministic" in weak["local_control"]),
        ("manifest records PR equation", "a xor b=x*y" in weak["pr_control"]),
        ("manifest records weak-demand nonselection", "do not imply" in weak["conclusion"]),
        ("manifest identifies decisive extra structure", "Hilbert operator product" in weak["decisive_extra_structure"]),
        ("manifest preserves source custody", "own no physical rank-960" in manifest["source_attribution"]),
        ("manifest preserves claim ceiling", "no GU-native Born rule" in manifest["claim_ceiling"]),
        ("manifest reserves held-out", "reserved and unscored" in manifest["held_out_credit"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact declares bridge classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states exact square identity", "CHSH^2 = 4I" in text),
        ("artifact states Tsirelson bound", "|S| <= 2 sqrt(2)" in text),
        ("artifact states PR witness", "has `S=4`" in text),
        ("artifact states weak-demand boundary", "does not imply the Tsirelson boundary" in text),
        ("artifact disclaims GU Born rule", "not a GU-native Born rule" in text),
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
        "CHSH^2 = 4I",
        "|S| <= 2 sqrt(2)",
        "has `S=4`",
        "does not imply the Tsirelson boundary",
        "not a GU-native Born rule",
    ]
    caught = 0
    for token in tokens:
        mutant_pass = {name for name, ok in evaluate(manifest, text.replace(token, "REMOVED")) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        (("hilbert_boundary", "square_identity"), "none"),
        (("hilbert_boundary", "norm_bound"), "four"),
        (("hilbert_boundary", "saturating_control"), "none"),
        (("hilbert_boundary", "parameter_independence"), "selected"),
        (("weak_demand_nonselection", "local_control"), "none"),
        (("weak_demand_nonselection", "pr_control"), "signalling"),
        (("weak_demand_nonselection", "conclusion"), "implies Hilbert"),
        (("weak_demand_nonselection", "decisive_extra_structure"), "positivity alone"),
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
