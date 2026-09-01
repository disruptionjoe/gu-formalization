#!/usr/bin/env python3
"""Exact certificate for the K77 first-jet substitution rigidity packet."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-source-observed-first-jet-contact-rigidity-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k77-source-observed-first-jet-contact-rigidity-wave-2026-09-01.md"


def pulled_kinetic_coefficients(h, phi_q, phi_v, v):
    """Coefficients of a^2, a, and 1 after t_x=Phi_q*v+Phi_v*a."""
    return (
        Fraction(1, 2) * h * phi_v**2,
        h * phi_q * phi_v * v,
        Fraction(1, 2) * h * phi_q**2 * v**2,
    )


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    h = Fraction(5, 3)
    phi_q = Fraction(7, 5)
    phi_v = Fraction(2, 7)
    v = Fraction(3, 2)
    a2, a1, a0 = pulled_kinetic_coefficients(h, phi_q, phi_v, v)
    point_a2, point_a1, point_a0 = pulled_kinetic_coefficients(h, phi_q, 0, v)
    result = manifest["exact_result"]
    result_flat = " ".join(json.dumps(result, sort_keys=True).split())

    return [
        ("positive kinetic control", h > 0),
        ("nonpoint bridge creates positive acceleration square", a2 == Fraction(10, 147) and a2 > 0),
        ("mixed acceleration coefficient exact", a1 == Fraction(1)),
        ("velocity coefficient exact", a0 == Fraction(147, 40)),
        ("point map removes acceleration square", point_a2 == 0),
        ("point map removes mixed acceleration", point_a1 == 0),
        ("point map retains first-order kinetic term", point_a0 == Fraction(147, 40)),
        ("manifest freezes full second-jet comparison", "full second-jet space" in manifest["bridge_class"]),
        ("manifest states prolongation", "Phi_q*v+Phi_v*a" in result["prolongation"]),
        ("manifest states highest-jet square", "Phi_v^2" in result["highest_jet_coefficient"]),
        ("manifest bounds boundary order", "at most linear in a" in result_flat),
        ("manifest derives point rigidity", "forces Phi_v=0" in result["rigidity"]),
        ("manifest reduces to geodesic normal form", "F(phi(q))" in result["reduction"]),
        ("manifest preserves indefinite horn", any("indefinite" in row for row in manifest["unresolved_classes"])),
        ("manifest preserves nonlocal horn", any("nonlocal" in row for row in manifest["unresolved_classes"])),
        ("manifest preserves source custody", "repository-derived" in manifest["source_attribution"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact classifies bridge boundary", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact freezes first-jet map", "t=Phi(q,v)" in text),
        ("artifact states acceleration-square coefficient", "h(Phi)Phi_v^2 a^2" in text),
        ("artifact states boundary term order", "at most linear in `a`" in text),
        ("artifact derives point map", "Positivity of `h` gives `Phi_v=0`" in text),
        ("artifact preserves full-carrier ceiling", "full rank-1920 carrier" in text),
        ("artifact preserves held-out fence", "earns no source-action, physical-state, prediction, confirmation" in text),
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
        "t=Phi(q,v)",
        "h(Phi)Phi_v^2 a^2",
        "at most linear in `a`",
        "Positivity of `h` gives `Phi_v=0`",
        "full rank-1920 carrier",
        "earns no source-action, physical-state, prediction, confirmation",
    ]
    caught = 0
    for token in text_tokens:
        mutant_text = text.replace(token, "REMOVED")
        mutant_pass = {name for name, ok in evaluate(manifest, mutant_text) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        ("bridge class", ("bridge_class",), "point maps only"),
        ("highest jet", ("exact_result", "highest_jet_coefficient"), "none"),
        ("boundary order", ("exact_result", "boundary_order"), "arbitrary"),
        ("rigidity", ("exact_result", "rigidity"), "Phi_v arbitrary"),
        ("source custody", ("source_attribution",), "source-owned theorem"),
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
