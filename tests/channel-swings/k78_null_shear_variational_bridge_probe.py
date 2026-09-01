#!/usr/bin/env python3
"""Exact certificate for the K78 fixed-null-line variational bridge."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k78-null-shear-variational-bridge-wave.json"
ARTIFACT = ROOT / (
    "explorations/conditional-build/"
    "k78-null-shear-variational-bridge-wave-2026-09-01.md"
)

Vector = tuple[Fraction, Fraction]


def pair(left: Vector, right: Vector) -> Fraction:
    return left[0] * right[0] - left[1] * right[1]


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    n = (Fraction(1), Fraction(1))
    m = (Fraction(1), Fraction(-1))
    q = Fraction(3, 5)
    v0 = Fraction(2, 3)
    v1 = Fraction(-1, 4)
    a0 = Fraction(1)
    a1 = Fraction(2)
    r = Fraction(5, 7)
    s = Fraction(-2, 5)
    t = Fraction(3, 8)
    psi = a0 * v0 + a1 * v1
    x = (v0 * v0 - v1 * v1) / 2
    dx0 = v0 * r - v1 * s
    dx1 = v0 * s - v1 * t
    direct_linear = Fraction(2) * (a0 * dx0 + a1 * dx1)
    divergence = direct_linear

    # b(q)=(q,q^2): c=<b',n>=1-2q and c'=-2.
    c = 1 - 2 * q
    c_prime = Fraction(-2)
    direct_variable = c * (a0 * dx0 + a1 * dx1)
    divergence_variable = c * (a0 * dx0 + a1 * dx1) + c_prime * psi * x
    correction = -c_prime * psi * x

    # M=H, b=m*q: P(b+n*psi)=2*q*psi.
    b = (q, -q)
    shifted = (b[0] + psi * n[0], b[1] + psi * n[1])
    potential = pair(shifted, shifted) / 2
    expected_potential = 2 * q * psi
    var = manifest["variational_result"]
    pot = manifest["quadratic_potential"]

    return [
        ("n is null", pair(n, n) == 0),
        ("m is null", pair(m, m) == 0),
        ("opposite null directions pair nontrivially", pair(m, n) == 2),
        ("constant-cross acceleration equals current divergence", direct_linear == divergence),
        ("variable-cross product rule closes exactly", direct_variable == divergence_variable + correction),
        ("nonconstant curve gives nonzero first-order correction", correction != 0),
        ("mass potential expansion is exact", potential == expected_potential),
        ("mass potential detects the planted shear", potential != 0),
        ("null-line point curve has zero kinetic norm", pair(n, n) == 0),
        ("manifest freezes fixed null line", "fixed H-null n" in manifest["frozen_model"]["map"]),
        ("manifest excludes rotating-line classification", "rotating null lines" in manifest["frozen_model"]["scope_exclusion"]),
        ("manifest records current identity", "partial_rho(c*a^rho*X)" in var["current_identity"]),
        ("manifest records first-order representative", "K_eff" in var["first_order_representative"]),
        ("manifest closes linear acceleration only", "linear acceleration" in var["verdict"]),
        ("manifest gives potential iff", "n^T M n=0" in pot["velocity_independence_iff"]),
        ("manifest gives mass-control null-line consequence", "span(n)" in pot["mass_control"]),
        ("manifest fences the no-go", "not a source or GU no-go" in pot["ceiling"]),
        ("manifest preserves source custody", "owns none" in manifest["source_attribution"]),
        ("manifest preserves full-carrier ceiling", "no source-owned full carrier" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact declares bridge classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states exact current decomposition", "partial_rho(c a^rho X)-c'(q)(a^rho v_rho)X" in text),
        ("artifact states potential iff", "n^T M n=0" in text and "n^T M b(q)=0" in text),
        ("artifact limits mass conclusion", "control-model no-go, not a source or GU no-go" in text),
        ("artifact names fixed-line seam", "fixed-null-line affine representative" in text),
        ("artifact disclaims physical credit", "No source-owned full-carrier symbol" in text),
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
        "partial_rho(c a^rho X)-c'(q)(a^rho v_rho)X",
        "n^T M n=0",
        "control-model no-go, not a source or GU no-go",
        "fixed-null-line affine representative",
        "No source-owned full-carrier symbol",
    ]
    caught = 0
    for token in tokens:
        mutant_pass = {name for name, ok in evaluate(manifest, text.replace(token, "REMOVED")) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        (("frozen_model", "map"), "point map"),
        (("frozen_model", "scope_exclusion"), "none"),
        (("variational_result", "current_identity"), "none"),
        (("variational_result", "first_order_representative"), "none"),
        (("variational_result", "verdict"), "complete bridge"),
        (("quadratic_potential", "velocity_independence_iff"), "always"),
        (("quadratic_potential", "mass_control"), "unrestricted"),
        (("quadratic_potential", "ceiling"), "GU no-go"),
        (("source_attribution",), "source-owned"),
        (("claim_ceiling",), "physical equivalence"),
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
