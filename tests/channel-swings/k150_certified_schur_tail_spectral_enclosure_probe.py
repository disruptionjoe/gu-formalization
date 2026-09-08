#!/usr/bin/env python3
"""Exact and hostile controls for the K150 Schur-tail certificate kernel."""

from __future__ import annotations

import argparse
import copy
import json
from fractions import Fraction
from pathlib import Path

from k150_certified_schur_tail_solver import (
    CertificateError,
    DEMO,
    certified_rank,
    gram_error,
    inertia,
    isolate_eigenvalue,
    projection_error,
    q,
    schur_tail_enclosure,
    solve,
    sqrt_upper,
    unique_first_threshold,
)


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k150-certified-schur-tail-spectral-enclosure-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k150-certified-schur-tail-spectral-enclosure-wave-2026-09-08.md"


def rejects(callable_) -> bool:
    try:
        callable_()
    except CertificateError:
        return True
    return False


def manifest_failures(data: dict) -> list[str]:
    out: list[str] = []
    solver = data.get("solver", {})
    tail = data.get("block_tail_certificate", {})
    cluster = data.get("cluster_and_gram_certificate", {})
    native = data.get("native_input_contract", {})
    bounds = data.get("boundaries", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        out.append("classification")
    if data.get("direction") != "observed_to_native":
        out.append("direction")
    required_solver = {
        "arithmetic": "exact_rational",
        "finite_spectral_method": "symmetric congruence inertia plus rational bisection",
        "irrational_bound_method": "outward dyadic square-root enclosure",
        "fails_closed": True,
        "assembles_native_ibc_inputs": False,
    }
    if any(solver.get(key) != value for key, value in required_solver.items()):
        out.append("solver")
    required_tail = {
        "required_complement_floor": "D>=d",
        "required_coupling_bound": "norm(B)^2<=beta2",
        "required_separation": "ritz_upper<d",
        "upper_formula": "ritz_upper",
        "supports_ordered_eigenvalue_index": True,
        "truncated_eigenvalue_is_automatic_lower_bound": False,
    }
    if any(tail.get(key) != value for key, value in required_tail.items()):
        out.append("tail")
    required_cluster = {
        "requires_certified_cluster_count": True,
        "requires_true_exterior_separation": True,
        "projection_error_formula": "eta_P=residual_norm_upper/exterior_separation_lower",
        "requires_residual_below_separation": True,
        "gram_error_formula": "eta_G=2*m*c^2*eta_P",
        "first_threshold_test": "u_a<min_{b!=a}l_b",
        "full_rank_test": "all approximate Gram eigenvalues exceed eta_G",
        "deficient_exact_rank_requires_structural_kernel": True,
        "charge_symmetry_transport_requires_proved_unitary": True,
    }
    if any(cluster.get(key) != value for key, value in required_cluster.items()):
        out.append("cluster")
    if native.get("currently_serialized_for_k148") is not False or native.get("numerical_native_table_emitted") is not False:
        out.append("native_input")
    denied = (
        "native_ibc_matrix_assembled",
        "numerical_native_residual_energies",
        "complete_charge_sector_point_spectrum",
        "native_full_Fock_Mourre_or_scattering",
        "many_body_asymptotic_completeness",
        "NESS_or_current",
        "physical_parameter_or_state_selection",
        "Weinstein_source_or_GU_action_owner",
        "Born_rule_derived",
        "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if any(bounds.get(key) is not False for key in denied):
        out.append("boundary")
    if bounds.get("canon_verdict_change") != "none" or bounds.get("paper_release_or_public_posture_change") != "none":
        out.append("external_boundary")
    return out


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    demo = solve(copy.deepcopy(DEMO))
    ritz_lo, ritz_hi = map(q, demo["ritz_interval"])
    full_lo, full_hi = map(q, demo["full_operator_interval"])
    root_bound = sqrt_upper(Fraction(2), bits=32)
    zero_diag = [[0, 1], [1, 0]]
    repeated = [[2, 0, 0], [0, 2, 0], [0, 0, 5]]
    exact_point = isolate_eigenvalue(repeated, 1, 1, 3, 8)
    rank_three = [["0", "0", "0", "0"], ["0", "1/2", "0", "0"], ["0", "0", "1/3", "0"], ["0", "0", "0", "1/4"]]
    return [
        ("schema", data.get("schema_version") == "1.0"),
        ("manifest contracts", not manifest_failures(data)),
        ("rational parser", q("-7/9") == Fraction(-7, 9)),
        ("positive inertia", inertia([[2, 1], [1, 2]]) == (0, 0, 2)),
        ("indefinite inertia", inertia(zero_diag) == (1, 0, 1)),
        ("singular inertia", inertia([[0, 0], [0, 0]]) == (0, 2, 0)),
        ("mixed singular inertia", inertia([[1, 0, 0], [0, -1, 0], [0, 0, 0]]) == (1, 1, 1)),
        ("two-by-two Schur congruence", inertia([[0, 1, 2], [1, 0, 3], [2, 3, 4]]) == (2, 0, 1)),
        ("exact repeated eigenvalue", exact_point == (Fraction(2), Fraction(2))),
        ("Ritz interval ordered", ritz_lo <= ritz_hi),
        ("Ritz ground is negative", ritz_hi < 0),
        ("Ritz width closes", ritz_hi - ritz_lo <= Fraction(1, 2**31)),
        ("Schur lower below Ritz", full_lo < ritz_lo <= full_hi),
        ("Schur upper equals Ritz upper", full_hi == ritz_hi),
        ("Schur correction positive", q(demo["schur_correction_upper"]) > 0),
        ("sqrt upper rigorous", root_bound * root_bound >= 2),
        ("sqrt upper tight", root_bound - Fraction(1414214, 1000000) < Fraction(1, 1000000)),
        ("projection error exact", projection_error("1/100", "1/2") == Fraction(1, 50)),
        ("Gram error exact", gram_error("1/50", 4, 1) == Fraction(4, 25)),
        ("demo projection error", demo["projection_error_upper"] == "1/50"),
        ("demo Gram error", demo["gram_error_upper"] == "4/25"),
        ("demo full rank", demo["gram_rank_certified"] == 4),
        ("structural rank three", certified_rank(rank_three, "1/10", 1) == 3),
        ("unique first threshold", demo["first_threshold_certified"] is True),
        ("common shift irrelevant", unique_first_threshold({"a": ["-1/4", "-1/5"], "b": ["0", "1/10"]}, "a")),
        ("native assembly false", demo["native_ibc_inputs_assembled_by_solver"] is False),
        ("reject asymmetric matrix", rejects(lambda: inertia([[1, 2], [3, 4]]))),
        ("reject nonexact float", rejects(lambda: inertia([[1.0]]))),
        ("reject unbracketed eigenvalue", rejects(lambda: isolate_eigenvalue([[1]], 1, 2, 3))),
        ("reject complement collision", rejects(lambda: schur_tail_enclosure(0, 3, 3, 1))),
        ("reject negative coupling square", rejects(lambda: schur_tail_enclosure(0, 1, 3, -1))),
        ("reject open residual gap", rejects(lambda: projection_error(1, 1))),
        ("reject reversed threshold", rejects(lambda: unique_first_threshold({"a": [2, 1], "b": [3, 4]}, "a"))),
        ("reject malformed threshold", rejects(lambda: unique_first_threshold({"a": [1], "b": [2, 3]}, "a"))),
        ("reject rank without margin", rejects(lambda: certified_rank([["1/10"]], "1/10"))),
        ("reject indefinite Gram", rejects(lambda: certified_rank([["-1", "0"], ["0", "1"]], "1/10"))),
        ("reject deficient rank without kernel", rejects(lambda: certified_rank([[0, 0], [0, 1]], "1/10", 0))),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("finite/native distinction", "This is a certificate for `A`, not yet for `H`." in text),
        ("full block formula", "H = [ A  B* ]" in text),
        ("Schur formula", "sqrt((d-a)^2+4 beta^2)" in text),
        ("truncation fence", "not a lower bound" in text),
        ("projection formula", "eta_P := r/delta" in text),
        ("complete Gram formula", "eta_G := 2 m c^2 eta_P" in text),
        ("structural kernel fence", "structural kernel" in text),
        ("symmetry fence", "phrase “symmetry-related” is not a certificate" in text),
        ("native inputs absent", "found no serialized finite charge-sector IBC basis" in text),
        ("Lehmann switch", "Lehmann--Goerisch" in text),
        ("Mourre dependency", "Only after\nnative margins close" in text),
        ("holdout fence", data.get("held_out") == "delayed-choice entanglement swapping, reserved_unscored"),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text()
    baseline = checks(data, text)
    failed = [name for name, ok in baseline if not ok]
    if failed:
        print(f"FAIL baseline: {failed}")
        return 1
    if not args.selftest:
        print(f"PASS {len(baseline)}/{len(baseline)} K150 exact controls")
        return 0

    mutations = [
        lambda d: d["solver"].__setitem__("arithmetic", "floating_point"),
        lambda d: d["solver"].__setitem__("fails_closed", False),
        lambda d: d["solver"].__setitem__("assembles_native_ibc_inputs", True),
        lambda d: d["block_tail_certificate"].__setitem__("required_complement_floor", "assumed"),
        lambda d: d["block_tail_certificate"].__setitem__("required_coupling_bound", "sampled"),
        lambda d: d["block_tail_certificate"].__setitem__("required_separation", "optional"),
        lambda d: d["block_tail_certificate"].__setitem__("truncated_eigenvalue_is_automatic_lower_bound", True),
        lambda d: d["cluster_and_gram_certificate"].__setitem__("requires_certified_cluster_count", False),
        lambda d: d["cluster_and_gram_certificate"].__setitem__("requires_true_exterior_separation", False),
        lambda d: d["cluster_and_gram_certificate"].__setitem__("requires_residual_below_separation", False),
        lambda d: d["cluster_and_gram_certificate"].__setitem__("deficient_exact_rank_requires_structural_kernel", False),
        lambda d: d["cluster_and_gram_certificate"].__setitem__("charge_symmetry_transport_requires_proved_unitary", False),
        lambda d: d["native_input_contract"].__setitem__("currently_serialized_for_k148", True),
        lambda d: d["native_input_contract"].__setitem__("numerical_native_table_emitted", True),
        lambda d: d["boundaries"].__setitem__("native_ibc_matrix_assembled", True),
        lambda d: d["boundaries"].__setitem__("numerical_native_residual_energies", True),
        lambda d: d["boundaries"].__setitem__("native_full_Fock_Mourre_or_scattering", True),
        lambda d: d["boundaries"].__setitem__("Weinstein_source_or_GU_action_owner", True),
        lambda d: d["boundaries"].__setitem__("Born_rule_derived", True),
        lambda d: d["boundaries"].__setitem__("prediction_or_confirmation_credit", True),
    ]
    prose_mutations = [
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING", 1),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", "", 1),
        text.replace("```gu-typed-objects", "```text", 1),
        text.replace("This is a certificate for `A`, not yet for `H`.", "", 1),
        text.replace("H = [ A  B* ]", "H = [ A  0  ]", 1),
        text.replace("sqrt((d-a)^2+4 beta^2)", "sqrt((d-a)^2)"),
        text.replace("not a lower bound", "is a lower bound", 1),
        text.replace("eta_P := r/delta", "eta_P := 0", 1),
        text.replace("eta_G := 2 m c^2 eta_P", "eta_G := 0", 1),
        text.replace("phrase “symmetry-related” is not a certificate", "symmetry-related is sufficient", 1),
        text.replace("Lehmann--Goerisch", "no fallback"),
        text.replace("Only after\nnative margins close", "Before native margins close", 1),
    ]
    caught = 0
    missed: list[str] = []
    for index, mutate in enumerate(mutations, start=1):
        trial = copy.deepcopy(data)
        mutate(trial)
        if any(not ok for _, ok in checks(trial, text)):
            caught += 1
        else:
            missed.append(f"manifest-{index}")
    for index, trial_text in enumerate(prose_mutations, start=1):
        if any(not ok for _, ok in checks(data, trial_text)):
            caught += 1
        else:
            missed.append(f"prose-{index}")
    total = len(mutations) + len(prose_mutations)
    if caught != total:
        print(f"FAIL hostile selftest caught {caught}/{total}; missed {missed}")
        return 1
    print(f"PASS hostile selftest caught {caught}/{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
