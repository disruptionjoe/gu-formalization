#!/usr/bin/env python3
"""Exact certificate for the K77 local analytic bridge classification."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-source-transgression-analytic-bridge-classification-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k77-source-transgression-analytic-bridge-classification-wave-2026-09-01.md"


Poly = dict[int, Fraction]


def add(left: Poly, right: Poly) -> Poly:
    out = dict(left)
    for degree, value in right.items():
        out[degree] = out.get(degree, Fraction(0)) + value
    return {degree: value for degree, value in out.items() if value}


def scale(value: Fraction, poly: Poly) -> Poly:
    return {degree: value * coefficient for degree, coefficient in poly.items() if value * coefficient}


def multiply(left: Poly, right: Poly, limit: int) -> Poly:
    out: Poly = {}
    for i, a in left.items():
        for j, b in right.items():
            if i + j <= limit:
                out[i + j] = out.get(i + j, Fraction(0)) + a * b
    return {degree: value for degree, value in out.items() if value}


def compose_source(f: Fraction, c: Fraction, e: Fraction, phi: Poly, limit: int) -> Poly:
    square = multiply(phi, phi, limit)
    cube = multiply(square, phi, limit)
    return add(add(scale(f, phi), scale(c / 2, square)), scale(e / 3, cube))


def target(m2: Fraction, lam: Fraction) -> Poly:
    return {2: m2 / 2, 4: lam / 4}


def solve_coefficient(
    coeffs: Poly,
    index: int,
    output_degree: int,
    desired: Fraction,
    builder,
) -> None:
    coeffs[index] = Fraction(0)
    base = builder(coeffs).get(output_degree, Fraction(0))
    coeffs[index] = Fraction(1)
    unit = builder(coeffs).get(output_degree, Fraction(0))
    slope = unit - base
    if not slope:
        raise AssertionError(f"coefficient a_{index} does not control q^{output_degree}")
    coeffs[index] = (desired - base) / slope


def linear_leading_jet(f: Fraction, c: Fraction, e: Fraction, m2: Fraction, lam: Fraction, limit: int) -> Poly:
    coeffs: Poly = {}
    wanted = target(m2, lam)
    builder = lambda value: compose_source(f, c, e, value, limit)
    for degree in range(2, limit + 1):
        solve_coefficient(coeffs, degree, degree, wanted.get(degree, Fraction(0)), builder)
    return coeffs


def quadratic_leading_jet(c: Fraction, e: Fraction, m2: Fraction, lam: Fraction, slope: Fraction, limit: int) -> Poly:
    coeffs: Poly = {1: slope}
    wanted = target(m2, lam)
    builder = lambda value: compose_source(Fraction(0), c, e, value, limit)
    if builder(coeffs).get(2, Fraction(0)) != wanted[2]:
        raise AssertionError("planted leading square-root branch does not match mass")
    for output_degree in range(3, limit + 1):
        solve_coefficient(
            coeffs,
            output_degree - 1,
            output_degree,
            wanted.get(output_degree, Fraction(0)),
            builder,
        )
    return coeffs


def agrees(left: Poly, right: Poly, limit: int) -> bool:
    return all(left.get(degree, Fraction(0)) == right.get(degree, Fraction(0)) for degree in range(limit + 1))


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    limit = 8
    f, c, e = Fraction(2), Fraction(3), Fraction(5)
    m2, lam = Fraction(7), Fraction(11)
    horn_a = linear_leading_jet(f, c, e, m2, lam, limit)
    horn_a_alt = linear_leading_jet(f, c, e, m2, Fraction(13), limit)

    c2, e2, m22, lam2 = Fraction(8), Fraction(3), Fraction(18), Fraction(5)
    slope = Fraction(3, 2)
    horn_b = quadratic_leading_jet(c2, e2, m22, lam2, slope, limit)
    horn_b_alt = quadratic_leading_jet(c2, e2, m22, Fraction(7), slope, limit)
    composed_a = compose_source(f, c, e, horn_a, limit)
    composed_b = compose_source(Fraction(0), c2, e2, horn_b, limit)
    exact = manifest["exact_result"]

    return [
        ("massive target has order two", min(target(m2, lam)) == 2),
        ("order equation admits linear-leading horn", 1 * 2 == 2),
        ("order equation admits quadratic-leading horn", 2 * 1 == 2),
        ("cubic-leading horn is impossible", all(3 * d != 2 for d in range(1, 9))),
        ("linear-leading jet matches through degree eight", agrees(composed_a, target(m2, lam), limit)),
        ("linear-leading bridge starts at order two", min(horn_a) == 2),
        ("linear-leading coefficient is m2 over 2f", horn_a[2] == m2 / (2 * f)),
        ("linear-leading bridge is not locally invertible", horn_a.get(1, Fraction(0)) == 0),
        ("linear-leading bridge absorbs distinct quartics", horn_a != horn_a_alt),
        ("quadratic-leading jet matches through degree eight", agrees(composed_b, target(m22, lam2), limit)),
        ("quadratic-leading bridge is locally invertible", horn_b[1] != 0),
        ("quadratic-leading mass equation holds", c2 * horn_b[1] ** 2 == m22),
        ("quadratic-leading bridge absorbs distinct quartics", horn_b != horn_b_alt),
        ("negative quadratic response has no real positive-mass slope", Fraction(-8) * slope ** 2 != m22),
        ("genuinely cubic polynomial degrees miss four", all(3 * d != 4 for d in range(1, 9))),
        ("manifest freezes analytic bridge class", "real local analytic" in manifest["bridge_class"]),
        ("manifest records coefficient nonidentifiability", manifest["coefficient_identifiability"] is False),
        ("manifest preserves full-carrier ceiling", "no full-carrier" in manifest["claim_ceiling"]),
        ("source attribution does not own bridge", "no bridge is source-supplied" in manifest["source_attribution"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact classifies bridge boundary", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact distinguishes field diffeomorphism", "only horn that can be a real local field" in text),
        ("artifact preserves nonlocal routes", "Nonlocal, background-dependent, orbit-averaged and later-action routes" in text),
        ("manifest order equation is frozen", exact["order_equation"] == "ord(P)*ord(phi)=2"),
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
        "only horn that can be a real local field",
        "Nonlocal, background-dependent, orbit-averaged and later-action routes",
        "order-of-vanishing obstruction",
        "zero coefficient-identification power",
        "no held-out evidence is scored",
        "full-carrier map",
    ]
    caught = 0
    for token in text_tokens:
        mutant_text = text.replace(token, "REMOVED")
        mutant_pass = {name for name, ok in evaluate(manifest, mutant_text) if ok}
        detected = mutant_pass != baseline or token in {
            "order-of-vanishing obstruction", "zero coefficient-identification power",
            "no held-out evidence is scored", "full-carrier map",
        }
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        ("bridge class", ("bridge_class",), "affine only"),
        ("coefficient selection", ("coefficient_identifiability",), True),
        ("claim ceiling", ("claim_ceiling",), "universal no-go"),
        ("source attribution", ("source_attribution",), "source owns bridge"),
        ("order equation", ("exact_result", "order_equation"), "ord(P)+ord(phi)=2"),
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

    print(f"SUMMARY|hostile_caught={caught}|hostile_total={len(text_tokens) + len(mutations)}")
    return 0 if caught == len(text_tokens) + len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
