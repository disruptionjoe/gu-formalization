#!/usr/bin/env python3
"""Deterministic algebraic/manifest certificate for the I1B Green control."""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-i1b-green-boundary-extension-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k77-i1b-green-boundary-extension-wave-2026-09-01.md"

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def matrix(a, b, c, d) -> Matrix:
    return ((Fraction(a), Fraction(b)), (Fraction(c), Fraction(d)))


def transpose(item: Matrix) -> Matrix:
    return matrix(item[0][0], item[1][0], item[0][1], item[1][1])


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return matrix(
        left[0][0] * right[0][0] + left[0][1] * right[1][0],
        left[0][0] * right[0][1] + left[0][1] * right[1][1],
        left[1][0] * right[0][0] + left[1][1] * right[1][0],
        left[1][0] * right[0][1] + left[1][1] * right[1][1],
    )


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return matrix(*(left[i][j] - right[i][j] for i in range(2) for j in range(2)))


def omega(left: tuple[complex, complex], right: tuple[complex, complex]) -> complex:
    return -left[0].conjugate() * right[1] + left[1].conjugate() * right[0]


def l2_power(power: Fraction) -> bool:
    """Whether integral_0^1 u^power du is finite."""
    return power > -1


def evaluate(manifest: dict, text: str) -> list[tuple[str, bool]]:
    zero = matrix(0, 0, 0, 0)
    identity = matrix(1, 0, 0, 1)
    J = matrix(0, -1, 1, 0)
    S = matrix(0, 1, 1, 0)
    H = matrix(1, 0, 0, -1)
    kappa = Fraction(1, 4)
    commutator = subtract(multiply(S, H), multiply(H, S))
    green = manifest["green_boundary"]
    extensions = manifest["extension_classification"]
    coefficient = manifest["coefficient_verdict"]
    fences = manifest["fences"]

    rational_lagrangians = ((1, 0), (0, 1), (1, 1), (2, -3), (5, 7))
    bad_line = (1 + 0j, 0 + 1j)

    return [
        ("J is skew-adjoint", transpose(J) == matrix(0, 1, -1, 0)),
        ("S is self-adjoint", transpose(S) == S),
        ("H is self-adjoint", transpose(H) == H),
        ("J squares to minus identity", multiply(J, J) == matrix(-1, 0, 0, -1)),
        ("indicial multiplication gives J*S=-H", multiply(J, S) == matrix(-1, 0, 0, 1)),
        ("bounded tangential multiplication gives J*H=S", multiply(J, H) == S),
        ("residue and bounded coefficient genuinely do not commute", commutator != zero),
        ("frozen negative mode is L2", l2_power(-2 * kappa)),
        ("frozen positive mode is L2", l2_power(2 * kappa)),
        ("threshold density is logarithmic", 2 * Fraction(-1, 2) == -1 and not l2_power(Fraction(-1))),
        ("singular Green matrix is nondegenerate", multiply(J, matrix(0, 1, -1, 0)) == identity),
        ("real-slope lines are isotropic", all(omega(v, v) == 0 for v in rational_lagrangians)),
        ("complex-slope hostile line is not isotropic", omega(bad_line, bad_line) == -2j),
        ("manifest freezes positive pairing", manifest["control_model"]["positive_pairing"] == "<f,g>=integral f^*g du"),
        ("manifest freezes kappa", manifest["control_model"]["kappa"] == "1/4"),
        ("manifest freezes symmetric expression", "(kappa/u)*S+a*H" in manifest["control_model"]["formal_expression"]),
        ("manifest records limit-circle threshold", "limit-circle iff |kappa|<1/2" in manifest["indicial_classification"]["general_threshold"]),
        ("manifest refuses L2-as-law", manifest["indicial_classification"]["terminology_fence"] == "the L2 count is not itself a self-adjoint law"),
        ("manifest gives both singular traces", "c_-=lim" in manifest["domains"]["singular_traces"] and "c_+=lim" in manifest["domains"]["singular_traces"]),
        ("manifest gives full minimal data", manifest["domains"]["minimal_boundary_data"] == "c_-=c_+=0 and f(1)=0"),
        ("manifest gives full maximal data", "arbitrary (c_-,c_+) in C^2" in manifest["domains"]["maximal_boundary_data"]),
        ("manifest gives exact Green form", green["singular_form"] == "omega_0(c,d)=-conj(c_-)d_+ + conj(c_+)d_-"),
        ("manifest states Green nondegeneracy", green["nondegenerate"] is True),
        ("manifest gives reduced deficiency indices", extensions["reduced_symmetric_deficiency_indices"] == [1, 1]),
        ("manifest gives Lagrangian family", "theta in R/piZ" in extensions["lagrangian_family"]),
        ("manifest gives U1-equivalent parameter space", "U(1)" in extensions["equivalent_parameter_space"]),
        ("manifest fixes regular endpoint", extensions["fixed_regular_condition"] == "f2(1)=0"),
        ("bounded coefficient leaves both operator domains fixed", coefficient["minimal_domain_changes"] is False and coefficient["maximal_domain_changes"] is False),
        ("bounded coefficient leaves boundary and extension family fixed", coefficient["green_boundary_form_changes"] is False and coefficient["lagrangian_extension_space_changes"] is False and coefficient["self_adjoint_domain_family_changes"] is False),
        ("spectral dependence is not erased", coefficient["spectral_data_may_change"] is True),
        ("source operator fence remains closed", fences["actual_source_cross_null_operator_constructed"] is False),
        ("physical pairing fence remains closed", fences["native_positive_physical_pairing_constructed"] is False),
        ("coefficient selector fence remains closed", fences["tangential_coefficient_selected"] is False),
        ("artifact carries comparator notice", "GU-COMPARATOR-ROUTING" in text),
        ("artifact carries typed objects", "```gu-typed-objects" in text),
        ("artifact names positive control", "positive Hilbert space" in text),
        ("artifact states minimal/maximal domain identity", "Dom(Dmax,a)=Dom(Dmax,0),     Dom(Dmin,a)=Dom(Dmin,0)" in text),
        ("artifact states L2 is not the boundary law", "not an `L2` count relabelled as a boundary\nlaw" in text),
        ("artifact derives Green cancellation", "zero-order term cancels" in text),
        ("artifact classifies exact singular Lagrangians", "L_theta = {(c_-,c_+): cos(theta)c_-+sin(theta)c_+=0}" in text),
        ("artifact rejects arbitrary complex slopes", "spanned by `(1,i)` has `omega_0(v,v)=-2i`" in text),
        ("artifact distinguishes extension and spectrum", "It may alter spectra, resolvents and zero modes" in text),
        ("artifact states actual-operator limitation", "not established as\nthe actual source cross-null I1B operator" in text),
        ("artifact preserves no-selector ceiling", "selector of `log(2)` versus `log(3)`" in text),
    ]


def main() -> int:
    manifest = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text()
    checks = evaluate(manifest, text)
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}|{name}")
    if any(not ok for _, ok in checks):
        return 1

    print(f"SUMMARY|passed={len(checks)}|total={len(checks)}")
    if "--selftest" not in sys.argv:
        return 0

    baseline = {name for name, ok in checks if ok}
    text_tokens = [
        "GU-COMPARATOR-ROUTING",
        "```gu-typed-objects",
        "positive Hilbert space",
        "Dom(Dmax,a)=Dom(Dmax,0),     Dom(Dmin,a)=Dom(Dmin,0)",
        "not an `L2` count relabelled as a boundary\nlaw",
        "zero-order term cancels",
        "L_theta = {(c_-,c_+): cos(theta)c_-+sin(theta)c_+=0}",
        "spanned by `(1,i)` has `omega_0(v,v)=-2i`",
        "It may alter spectra, resolvents and zero modes",
        "not established as\nthe actual source cross-null I1B operator",
        "selector of `log(2)` versus `log(3)`",
    ]
    caught = 0
    for token in text_tokens:
        mutant_text = text.replace(token, "REMOVED")
        mutant_pass = {name for name, ok in evaluate(manifest, mutant_text) if ok}
        detected = mutant_pass != baseline
        print(f"{'PASS' if detected else 'FAIL'}|hostile|remove {token.replace(chr(10), ' ')}")
        caught += int(detected)

    mutations = [
        ("positive pairing", ("control_model", "positive_pairing"), "indefinite native form"),
        ("kappa", ("control_model", "kappa"), "3/4"),
        ("formal expression", ("control_model", "formal_expression"), "a enters the residue"),
        ("threshold", ("indicial_classification", "general_threshold"), "always limit-circle"),
        ("L2 fence", ("indicial_classification", "terminology_fence"), "L2 count is a self-adjoint law"),
        ("minimal data", ("domains", "minimal_boundary_data"), "one trace free"),
        ("Green form", ("green_boundary", "singular_form"), "zero"),
        ("deficiency indices", ("extension_classification", "reduced_symmetric_deficiency_indices"), [0, 0]),
        ("Lagrangian family", ("extension_classification", "lagrangian_family"), "all complex slopes"),
        ("domain dependence", ("coefficient_verdict", "maximal_domain_changes"), True),
        ("boundary dependence", ("coefficient_verdict", "green_boundary_form_changes"), True),
        ("spectral fence", ("coefficient_verdict", "spectral_data_may_change"), False),
        ("source promotion", ("fences", "actual_source_cross_null_operator_constructed"), True),
        ("physical promotion", ("fences", "native_positive_physical_pairing_constructed"), True),
        ("selector promotion", ("fences", "tangential_coefficient_selected"), True),
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
