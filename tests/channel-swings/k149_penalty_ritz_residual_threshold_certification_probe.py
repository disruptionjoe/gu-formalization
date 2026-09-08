#!/usr/bin/env python3
"""Exact/hostile controls for the K149 penalty--Ritz certification wave."""

from __future__ import annotations

import argparse
import copy
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k149-penalty-ritz-residual-threshold-certification-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k149-penalty-ritz-residual-threshold-certification-wave-2026-09-08.md"


def penalty_ground(u: float) -> float:
    return (u + 2.0 - math.sqrt((u + 2.0) ** 2 + 4.0)) / 2.0


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*a)]


def eigenvalues_2x2(a: list[list[float]]) -> list[float]:
    tr = a[0][0] + a[1][1]
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    disc = max(0.0, tr * tr - 4.0 * det)
    return sorted([(tr - math.sqrt(disc)) / 2.0, (tr + math.sqrt(disc)) / 2.0], reverse=True)


def gram(vectors: list[list[float]]) -> list[list[float]]:
    return matmul(vectors, transpose(vectors))


def failures(data: dict) -> list[str]:
    out: list[str] = []
    enc = data.get("penalty_ritz_enclosure", {})
    clu = data.get("cluster_transport", {})
    thr = data.get("threshold_certification", {})
    bounds = data.get("boundaries", {})
    required_enc = {
        "commutes_with_both_charges": True,
        "finite_penalty_is_native": False,
        "penalty_minmax_direction": "lambda_k(U,q) increases to lambda_k(hc,q)",
        "ritz_spaces_are_native_conforming": True,
        "ritz_minmax_direction": "rho_k(N,q) decreases to lambda_k(hc,q)",
        "two_sided_bracket": "lambda_k(U,q)<=lambda_k(hc,q)<=rho_k(N,q)",
        "cofinal_width_converges_to_zero": True,
        "truncated_finite_U_ritz_is_automatic_lower_bound": False,
    }
    if any(enc.get(k) != v for k, v in required_enc.items()):
        out.append("enclosure")
    required_clu = {
        "requires_certified_cluster_count": True,
        "requires_positive_gap": True,
        "spectral_projection_gap_norm_converges": True,
        "includes_degenerate_off_diagonal_residual_entries": True,
        "basis_covariant": True,
        "rank_basis_invariant": True,
        "gram_error_bound": "eta_G=2*m*c^2*eta_P",
        "one_state_K148_block_is_complete_when_degenerate": False,
    }
    if any(clu.get(k) != v for k, v in required_clu.items()):
        out.append("cluster")
    required_thr = {
        "candidate_interval": "[l_a+tau,u_a+tau]",
        "unique_first_test": "u_a<min_{b!=a}l_b",
        "overlap_means": "unresolved_or_degenerate",
        "gram_eigenvalue_error": "abs(mu_j^n-mu_j)<=eta_G",
        "full_rank_test": "mu_d^n>eta_G",
        "rank_lower_bound_test": "mu_s^n>eta_G implies rank>=s",
        "deficient_exact_rank_requires_structural_kernel": True,
        "numerical_smallness_proves_exact_zero": False,
    }
    if any(thr.get(k) != v for k, v in required_thr.items()):
        out.append("threshold")
    denied = (
        "numerical_native_residual_energies",
        "complete_charge_sector_point_spectrum",
        "certified_IBC_quadrature_tail_solver",
        "native_full_Fock_Mourre_or_scattering",
        "many_body_asymptotic_completeness",
        "NESS_or_current",
        "physical_parameter_or_state_selection",
        "Weinstein_source_or_GU_action_owner",
        "Born_rule_derived",
        "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if any(bounds.get(k) is not False for k in denied):
        out.append("boundary")
    if bounds.get("canon_verdict_change") != "none" or bounds.get("paper_release_or_public_posture_change") != "none":
        out.append("external_boundary")
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        out.append("classification")
    if data.get("direction") != "observed_to_native":
        out.append("direction")
    return out


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    us = [0.0, 1.0, 4.0, 16.0, 64.0]
    lows = [penalty_ground(u) for u in us]
    threshold_intervals = {"a": (-0.30, -0.28), "b": (-0.10, -0.07), "c": (0.05, 0.08)}
    tau = 1.25
    attached = {k: (lo + tau, hi + tau) for k, (lo, hi) in threshold_intervals.items()}
    vecs = [[1.0, 0.0], [0.0, 0.6]]
    g = gram(vecs)
    eigs = eigenvalues_2x2(g)
    eta = 0.1
    rank_one = [[1.0, 0.0], [0.0, 0.0]]
    rank_one_eigs = eigenvalues_2x2(rank_one)
    return [
        ("schema", data.get("schema_version") == "1.0"),
        ("classification", data.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", data.get("direction") == "observed_to_native"),
        ("two native edges", data["fixed_control"]["oriented_edges"] == [[0, 1], [0, 2]]),
        ("threshold mass", data["fixed_control"]["threshold"] == "5/4"),
        ("penalty values below hard core", all(value < 0.0 for value in lows)),
        ("penalty values monotone", all(a < b for a, b in zip(lows, lows[1:]))),
        ("penalty closes on hard core", abs(penalty_ground(10**7)) < 2e-7),
        ("penalty exact at zero", abs(penalty_ground(0.0) - (1.0 - math.sqrt(2.0))) < 1e-12),
        ("hard core Ritz upper", 0.0 >= lows[-1]),
        ("cofinal width shrinks", -lows[-1] < -lows[1]),
        ("charge commutation retained", data["penalty_ritz_enclosure"]["commutes_with_both_charges"] is True),
        ("finite U not native", data["penalty_ritz_enclosure"]["finite_penalty_is_native"] is False),
        ("Ritz conforming", data["penalty_ritz_enclosure"]["ritz_spaces_are_native_conforming"] is True),
        ("two-sided bracket recorded", "<=" in data["penalty_ritz_enclosure"]["two_sided_bracket"]),
        ("isolated scope", "isolated" in data["penalty_ritz_enclosure"]["applies_to"]),
        ("truncated lower-bound refusal", data["penalty_ritz_enclosure"]["truncated_finite_U_ritz_is_automatic_lower_bound"] is False),
        ("cluster count required", data["cluster_transport"]["requires_certified_cluster_count"] is True),
        ("cluster gap required", data["cluster_transport"]["requires_positive_gap"] is True),
        ("projection norm convergence", data["cluster_transport"]["spectral_projection_gap_norm_converges"] is True),
        ("degenerate entries retained", data["cluster_transport"]["includes_degenerate_off_diagonal_residual_entries"] is True),
        ("basis covariance retained", data["cluster_transport"]["basis_covariant"] is True),
        ("Gram positive", all(value >= 0.0 for value in eigs)),
        ("Gram full-rank margin", min(eigs) > eta),
        ("full-rank certificate", data["threshold_certification"]["full_rank_test"] == "mu_d^n>eta_G"),
        ("rank-one positive margin", rank_one_eigs[0] > eta),
        ("rank-one needs kernel", rank_one_eigs[1] <= eta and data["threshold_certification"]["deficient_exact_rank_requires_structural_kernel"] is True),
        ("smallness not zero", data["threshold_certification"]["numerical_smallness_proves_exact_zero"] is False),
        ("candidate a first", attached["a"][1] < min(attached["b"][0], attached["c"][0])),
        ("rest mass cancels in ordering", threshold_intervals["a"][1] < min(threshold_intervals["b"][0], threshold_intervals["c"][0])),
        ("overlap unresolved", data["threshold_certification"]["overlap_means"] == "unresolved_or_degenerate"),
        ("manifest contracts", not failures(data)),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("penalty lower qualification", "exact finite-penalty min--max value" in text),
        ("Ritz upper direction", "rho_k(N,q) decreases" in text),
        ("full residual matrix", "complete residual form-factor Gram operator" in text),
        ("degenerate fence", "not substituted" in text),
        ("threshold separation", "u_a < min_(b != a) l_b" in text),
        ("kernel requirement", "exact structural kernel" in text),
        ("numerical fence", "does **not** provide the" in text and "missing numerical IBC tail implementation" in text),
        ("Mourre dependency", "Only after those margins close" in text),
        ("source fence", data["boundaries"]["Weinstein_source_or_GU_action_owner"] is False),
        ("Born fence", data["boundaries"]["Born_rule_derived"] is False),
        ("holdout fence", data["held_out"] == "delayed-choice entanglement swapping, reserved_unscored"),
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
        print(f"PASS {len(baseline)}/{len(baseline)} K149 exact controls")
        return 0
    mutations = [
        lambda d: d["penalty_ritz_enclosure"].__setitem__("finite_penalty_is_native", True),
        lambda d: d["penalty_ritz_enclosure"].__setitem__("commutes_with_both_charges", False),
        lambda d: d["penalty_ritz_enclosure"].__setitem__("penalty_minmax_direction", "decreases"),
        lambda d: d["penalty_ritz_enclosure"].__setitem__("ritz_minmax_direction", "increases"),
        lambda d: d["penalty_ritz_enclosure"].__setitem__("cofinal_width_converges_to_zero", False),
        lambda d: d["penalty_ritz_enclosure"].__setitem__("truncated_finite_U_ritz_is_automatic_lower_bound", True),
        lambda d: d["cluster_transport"].__setitem__("requires_certified_cluster_count", False),
        lambda d: d["cluster_transport"].__setitem__("requires_positive_gap", False),
        lambda d: d["cluster_transport"].__setitem__("spectral_projection_gap_norm_converges", False),
        lambda d: d["cluster_transport"].__setitem__("includes_degenerate_off_diagonal_residual_entries", False),
        lambda d: d["cluster_transport"].__setitem__("basis_covariant", False),
        lambda d: d["cluster_transport"].__setitem__("one_state_K148_block_is_complete_when_degenerate", True),
        lambda d: d["threshold_certification"].__setitem__("unique_first_test", "l_a<min l_b"),
        lambda d: d["threshold_certification"].__setitem__("full_rank_test", "mu_d^n>=0"),
        lambda d: d["threshold_certification"].__setitem__("deficient_exact_rank_requires_structural_kernel", False),
        lambda d: d["threshold_certification"].__setitem__("numerical_smallness_proves_exact_zero", True),
        lambda d: d["boundaries"].__setitem__("numerical_native_residual_energies", True),
        lambda d: d["boundaries"].__setitem__("complete_charge_sector_point_spectrum", True),
        lambda d: d["boundaries"].__setitem__("native_full_Fock_Mourre_or_scattering", True),
        lambda d: d["boundaries"].__setitem__("Weinstein_source_or_GU_action_owner", True),
        lambda d: d["boundaries"].__setitem__("Born_rule_derived", True),
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
    prose_mutations = [
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING", 1),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", "", 1),
        text.replace("```gu-typed-objects", "```text", 1),
        text.replace("exact finite-penalty min--max value", "finite matrix value", 1),
        text.replace("rho_k(N,q) decreases", "rho_k(N,q) varies", 1),
        text.replace("complete residual form-factor Gram operator", "diagonal residual blocks", 1),
        text.replace("not substituted", "substituted", 1),
        text.replace("u_a < min_(b != a) l_b", "l_a < min_(b != a) l_b", 1),
        text.replace("exact structural kernel", "small numerical entries"),
        text.replace("does **not** provide the\nmissing numerical IBC tail implementation", "provides the numerical native spectrum", 1),
        text.replace("Only after those margins close", "Before those margins close", 1),
    ]
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
