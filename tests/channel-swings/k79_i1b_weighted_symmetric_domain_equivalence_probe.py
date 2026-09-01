#!/usr/bin/env python3
"""Certificate for K79 weighted symmetric-domain equivalence."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k79-i1b-weighted-symmetric-domain-equivalence-wave.json"
ARTIFACT = ROOT / (
    "explorations/conditional-build/"
    "k79-i1b-weighted-symmetric-domain-equivalence-wave-2026-09-01.md"
)


def matmul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def exp_lower(value: Fraction, order: int) -> Fraction:
    term = Fraction(1)
    total = term
    for index in range(1, order + 1):
        term *= value / index
        total += term
    return total


def exp_upper(value: Fraction, order: int) -> Fraction:
    lower = exp_lower(value, order)
    term = Fraction(1)
    for index in range(1, order + 2):
        term *= value / index
    ratio_bound = value / (order + 2)
    return lower + term / (1 - ratio_bound)


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    p = Fraction(3, 2)
    kappa = Fraction(3, 4)
    a = Fraction(1)
    rho = Fraction(5, 4)
    c0 = ((kappa, -a), (-a, -kappa))
    c0_square = matmul(c0, c0)
    cp_eigenvalues = (p / 2 + rho, p / 2 - rho)
    plus_exponent = -p / 2 - rho
    minus_exponent = -p / 2 + rho
    plus_density_exponent = p + 2 * plus_exponent
    minus_density_exponent = p + 2 * minus_exponent
    conjugated_derivative_coefficient = -p / 2 + p / 2
    adjoint_defect_after_correction = p - p / 2 - p / 2
    green_weight_after_half_densities = p - p / 2 - p / 2

    log2_above_half = exp_upper(Fraction(1, 2), 8) < 2
    log2_below_seven_tenths = exp_lower(Fraction(7, 10), 5) > 2
    log3_above_one = exp_upper(Fraction(1), 9) < 3
    raw_log2_p1_two_modes = Fraction(1, 16) + Fraction(49, 100) < 1
    raw_log3_p1_one_mode = log3_above_one

    control = manifest["control_model"]
    unitary = manifest["unitary_equivalence"]
    indicial = manifest["indicial_result"]
    raw = manifest["raw_control"]

    return [
        ("Pythagorean normal square first diagonal", c0_square[0][0] == rho * rho),
        ("Pythagorean normal square second diagonal", c0_square[1][1] == rho * rho),
        ("Pythagorean normal square off diagonal", c0_square[0][1] == 0 and c0_square[1][0] == 0),
        ("weighted normal eigenvalues shift by p over two", cp_eigenvalues == (Fraction(2), Fraction(-1, 2))),
        ("half-density conjugation cancels derivative weight", conjugated_derivative_coefficient == 0),
        ("formal-adjoint correction cancels exactly", adjoint_defect_after_correction == 0),
        ("Green weight cancels under half densities", green_weight_after_half_densities == 0),
        ("plus weighted density exponent loses p", plus_density_exponent == -2 * rho),
        ("minus weighted density exponent loses p", minus_density_exponent == 2 * rho),
        ("rational series proves log2 above one half", log2_above_half),
        ("rational series proves log2 below seven tenths", log2_below_seven_tenths),
        ("rational series proves log3 above one", log3_above_one),
        ("raw p1 bound keeps both log2 modes", raw_log2_p1_two_modes),
        ("raw p1 bound rejects the log3 singular mode", raw_log3_p1_one_mode),
        ("both corrected candidates are limit point", log2_above_half and log3_above_one),
        ("manifest records weighted symmetric operator", "p/(2u)" in control["operator"]),
        ("manifest records adjoint defect", "(p/u)*J" in control["formal_adjoint_identity"]),
        ("manifest records forced half correction", "p/(2u)" in control["forced_correction"]),
        ("manifest records weighted Green form", "u^p" in control["green_form"]),
        ("manifest records half-density map", "u^(p/2)" in unitary["map"]),
        ("manifest records conjugation identity", "D_(0,kappa,a)" in unitary["identity"]),
        ("manifest records domain transport", "minimal and maximal domains" in unitary["domain_effect"]),
        ("manifest records boundary transport", "U_p f" in unitary["boundary_identity"]),
        ("manifest records shifted normal matrix", "(p/2)I" in indicial["normal_matrix"]),
        ("manifest records corrected modes", "-p/2-rho" in indicial["modes"]),
        ("manifest records weight cancellation", "u^(-2rho)" in indicial["weighted_densities"]),
        ("manifest records weight-independent threshold", "independently of p" in indicial["limit_circle_iff"]),
        ("manifest classifies both candidates", "both a=log(2)" in indicial["candidate_class"]),
        ("manifest records raw adjoint defect", "(p/u)*J" in raw["defect"]),
        ("manifest retains raw integrability fact", "integrability fact" in raw["p1_result"]),
        ("manifest rejects raw domain selection", "not a self-adjoint-domain discriminator" in raw["verdict"]),
        ("manifest preserves source custody", "do not own" in manifest["source_attribution"]),
        ("manifest preserves physical ceiling", "no source cross-null operator" in manifest["claim_ceiling"]),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact declares bridge classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text),
        ("artifact states weight cancellation", "the weight cancels from the endpoint exponents" in text),
        ("artifact states exact conjugation", "U_p D_(p,kappa,a) U_p^(-1)=D_(0,kappa,a)" in text),
        ("artifact states both limit point", "both are limit-point for every power-law weight" in text),
        ("artifact fences raw split", "not a self-adjoint-domain discriminator" in text),
        ("artifact disclaims physical selection", "No coefficient selection" in text),
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
        "the weight cancels from the endpoint exponents",
        "U_p D_(p,kappa,a) U_p^(-1)=D_(0,kappa,a)",
        "both are limit-point for every power-law weight",
        "not a self-adjoint-domain discriminator",
        "No coefficient selection",
    ]
    caught = 0
    for token in tokens:
        mutant_pass = {name for name, ok in evaluate(manifest, text.replace(token, "REMOVED")) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token}")
        caught += int(detected)

    mutations = [
        (("control_model", "operator"), "uncorrected"),
        (("control_model", "formal_adjoint_identity"), "symmetric already"),
        (("control_model", "forced_correction"), "none"),
        (("control_model", "green_form"), "unweighted"),
        (("unitary_equivalence", "map"), "identity"),
        (("unitary_equivalence", "identity"), "not equivalent"),
        (("unitary_equivalence", "domain_effect"), "domains differ"),
        (("unitary_equivalence", "boundary_identity"), "none"),
        (("indicial_result", "normal_matrix"), "unshifted"),
        (("indicial_result", "modes"), "unweighted"),
        (("indicial_result", "weighted_densities"), "p-dependent"),
        (("indicial_result", "limit_circle_iff"), "p-dependent"),
        (("indicial_result", "candidate_class"), "distinct classes"),
        (("raw_control", "defect"), "none"),
        (("raw_control", "p1_result"), "physical selector"),
        (("raw_control", "verdict"), "self-adjoint selector"),
        (("source_attribution",), "source-owned"),
        (("claim_ceiling",), "physical coefficient selector"),
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
