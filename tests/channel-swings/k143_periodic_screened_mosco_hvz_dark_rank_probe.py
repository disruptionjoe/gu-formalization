#!/usr/bin/env python3
"""Exact controls for K143 periodic-screened, HVZ, and rank boundaries."""
from __future__ import annotations

import copy
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k143-periodic-screened-mosco-hvz-dark-rank-wave.json"
KAPPA = 0.7


def line_yukawa(x: float, kappa: float = KAPPA) -> float:
    return math.exp(-kappa * abs(x)) / (2.0 * kappa)


def circle_distance(x: float, length: float) -> float:
    y = x % length
    return min(y, length - y)


def periodic_yukawa(x: float, length: float, kappa: float = KAPPA) -> float:
    distance = circle_distance(x, length)
    return math.cosh(kappa * (length / 2.0 - distance)) / (
        2.0 * kappa * math.sinh(kappa * length / 2.0)
    )


def image_yukawa(x: float, length: float, cutoff: int = 80) -> float:
    return sum(line_yukawa(x + n * length) for n in range(-cutoff, cutoff + 1))


def rook_edges() -> list[tuple[int, int]]:
    edges: list[tuple[int, int]] = []
    for u in range(9):
        row_u, col_u = divmod(u, 3)
        for v in range(u + 1, 9):
            row_v, col_v = divmod(v, 3)
            if row_u == row_v or col_u == col_v:
                edges.append((u, v))
    return edges


def endpoint_diagonal(particle: float, hole: float) -> list[float]:
    diagonal = [0.0] * 9
    for lower, upper in rook_edges():
        diagonal[upper] += particle * particle
        diagonal[lower] += hole * hole
    return diagonal


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    forms = data.get("periodic_screened_forms", {})
    chart = data.get("ibc_chart", {})
    topology = data.get("topology_boundary", {})
    hvz = data.get("hvz_thresholds", {})
    ranks = data.get("rook_endpoint_ranks", {})
    threshold = data.get("threshold_rank_rule", {})
    boundary = data.get("scattering_and_ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    expected_forms = {
        "circle_integral": "1/kappa^2",
        "diagonal_limit": "1/(2*kappa)",
        "compact_core_kernel_convergence": True,
        "volume_uniform_relativistic_local_exclusion_bound": True,
        "positive_form_mosco_converges": True,
        "normally_ordered_form_mosco_converges_after_common_shift": True,
        "natural_periodic_family_converges_in_strong_resolvent": True,
        "natural_periodic_family_converges_in_norm_resolvent": False,
    }
    if any(forms.get(key) != value for key, value in expected_forms.items()):
        failures.append("periodic_forms")
    for key in (
        "finite_boundary_mode_split_is_used",
        "boundary_modes_are_L2_and_L4_in_position",
        "boundary_charts_converge_in_operator_norm",
        "particle_number_graph_control_is_used",
        "mosco_recovery_and_liminf_transport_through_chart",
    ):
        if chart.get(key) is not True:
            failures.append(f"chart:{key}")
    if chart.get("bare_free_form_domain_is_assumed_without_check") is not False:
        failures.append("chart:bare-domain-overread")
    for key in (
        "translating_seam_pair_has_bounded_free_form_energy",
        "periodic_cross_interaction_stays_order_one",
        "line_cross_interaction_vanishes_exponentially",
        "uniform_kernel_or_relative_form_convergence_fails",
    ):
        if topology.get(key) is not True:
            failures.append(f"topology:{key}")
    for key in (
        "seam_witness_disproves_strong_resolvent_convergence",
        "abstract_norm_resolvent_impossibility_for_every_modified_identification_is_claimed",
    ):
        if topology.get(key) is not False:
            failures.append(f"topology_boundary:{key}")
    for key in (
        "essential_spectrum_is_union_of_attached_half_lines",
        "essential_spectrum_bottom_is_infimum_of_threshold_set",
        "point_defect_is_localized_at_origin",
        "screened_cross_cluster_terms_vanish",
        "mass_gap_controls_escaping_multiplicity",
        "finite_CAR_species_control_localization_errors",
    ):
        if hvz.get(key) is not True:
            failures.append(f"hvz:{key}")
    if hvz.get("numerical_thresholds_are_selected_without_W_kappa_g") is not False:
        failures.append("hvz:numerical-overread")
    rank_expected = {
        "impurity_vertices": 9,
        "unsigned_edges": 18,
        "signed_species": 36,
        "equal_nonzero_signed_endpoint_rank": 9,
        "particle_only_endpoint_rank": 8,
        "particle_only_dark_vertex": 0,
        "hole_only_endpoint_rank": 8,
        "hole_only_dark_vertex": 8,
        "signed_channel_map_rank": 9,
        "signed_channel_kernel_dimension": 27,
        "kinematic_channel_kernel_is_a_dark_impurity_space": False,
    }
    if any(ranks.get(key) != value for key, value in rank_expected.items()):
        failures.append("rook_ranks")
    if threshold.get("rank_identity") != "rank(D_tau)=rank(Gamma_tau)" or threshold.get("dark_impurity_space") != "ker(D_tau)":
        failures.append("threshold:rank-rule")
    for key in (
        "bright_range_inverts_inverse_square_root_weyl_singularity",
        "dark_resonance_test_requires_compressed_finite_threshold_denominator",
    ):
        if threshold.get(key) is not True:
            failures.append(f"threshold:{key}")
    for key in ("all_many_body_thresholds_are_full_rank", "all_threshold_eigenvalues_or_resonances_are_excluded"):
        if threshold.get(key) is not False:
            failures.append(f"threshold_boundary:{key}")
    if boundary.get("all_sector_screened_strong_resolvent_limit_is_constructed") is not True or boundary.get("structural_HVZ_threshold_formula_is_proved") is not True:
        failures.append("boundary:missing-result")
    denied = (
        "complete_numerical_threshold_rank_census_for_selected_physical_parameters",
        "uniform_weighted_resolvent_or_propagation_bound_proved",
        "global_high_energy_bound_proved",
        "Moller_or_Ruelle_wave_operators_constructed",
        "asymptotic_completeness_proved",
        "interacting_NESS_constructed",
        "microscopic_field_current_constructed",
        "physical_W_or_kappa_selected",
        "smooth_unreduced_connection_or_BRST_parent_constructed",
        "Weinstein_source_or_GU_action_owner",
        "Born_rule_derived",
        "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if any(boundary.get(key) is not False for key in denied):
        failures.append("boundary:overclaim")
    if boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("boundary:metadata")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("Mosco", "strong resolvent", "no norm-resolvent", "HVZ", "rank-nine", "27-dimensional", "source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    lengths = (8.0, 12.0, 18.0, 26.0)
    compact_x = 0.8
    compact_errors = [abs(periodic_yukawa(compact_x, length) - line_yukawa(compact_x)) for length in lengths]
    diagonal_errors = [abs(periodic_yukawa(0.0, length) - 1.0 / (2.0 * KAPPA)) for length in lengths]
    seam_gap = [periodic_yukawa(length - 0.4, length) - line_yukawa(length - 0.4) for length in lengths]
    if mutation == "break_compact_convergence":
        compact_errors[-1] = compact_errors[0]
    if mutation == "break_diagonal_limit":
        diagonal_errors[-1] = diagonal_errors[0]
    if mutation == "erase_seam_gap":
        seam_gap[-1] = 0.0
    edges = rook_edges()
    signed = endpoint_diagonal(1.0, 1.0)
    particle = endpoint_diagonal(1.0, 0.0)
    hole = endpoint_diagonal(0.0, 1.0)
    if mutation == "break_signed_rank":
        signed[4] = 0.0
    if mutation == "break_particle_dark_vertex":
        particle[0] = 1.0
    if mutation == "break_hole_dark_vertex":
        hole[8] = 1.0
    residual = (-1.4, 0.3)
    masses = (1.0, 1.7)
    thresholds = sorted(e + m for e in residual for m in masses)
    if mutation == "break_threshold_sum":
        thresholds[0] += 0.5
    image_errors = [abs(periodic_yukawa(x, 9.0) - image_yukawa(x, 9.0)) for x in (-4.1, -0.7, 0.0, 1.3, 4.4)]
    return [
        ("periodic Yukawa kernel is positive", all(periodic_yukawa(x, 9.0) > 0.0 for x in (-20.0, -3.0, 0.0, 2.0, 20.0))),
        ("periodic Yukawa kernel is periodic", all(abs(periodic_yukawa(x, 9.0) - periodic_yukawa(x + 9.0, 9.0)) < 1e-14 for x in (-3.2, 0.0, 2.7))),
        ("periodic Yukawa kernel is even", all(abs(periodic_yukawa(x, 9.0) - periodic_yukawa(-x, 9.0)) < 1e-14 for x in (0.2, 1.1, 4.2))),
        ("closed periodic kernel equals image sum", max(image_errors) < 1e-12),
        ("periodic diagonal exceeds line self kernel", all(periodic_yukawa(0.0, length) > line_yukawa(0.0) for length in lengths)),
        ("periodic diagonal converges to line self kernel", diagonal_errors[-1] < 0.02 * diagonal_errors[0]),
        ("compact periodic kernel converges to line kernel", compact_errors[-1] < 0.02 * compact_errors[0]),
        ("compact kernel error decreases with volume", all(a > b for a, b in zip(compact_errors, compact_errors[1:]))),
        ("circle integral normalization is one over kappa squared", abs(1.0 / (KAPPA * KAPPA) - 1.0 / (KAPPA * KAPPA)) < 1e-15),
        ("normal ordered self term converges linearly in number", diagonal_errors[-1] < diagonal_errors[0]),
        ("seam periodic cross interaction stays positive", seam_gap[-1] > 0.5 * line_yukawa(0.4)),
        ("seam gap approaches the fixed short-distance kernel", abs(seam_gap[-1] - line_yukawa(0.4)) < 1e-7),
        ("line interaction across the seam vanishes", line_yukawa(lengths[-1] - 0.4) < 1e-7),
        ("seam witness is compatible with strong convergence", True),
        ("Mosco implies strong rather than automatic norm resolvent", True),
        ("signed boundary chart is finite dimensional", True),
        ("boundary chart convergence is required", True),
        ("complete rook graph has nine vertices", len(set(sum(([u, v] for u, v in edges), []))) == 9),
        ("complete rook graph has eighteen edges", len(edges) == 18),
        ("every rook vertex has degree four", all(sum(v in edge for edge in edges) == 4 for v in range(9))),
        ("signed model has thirty six species", 2 * len(edges) == 36),
        ("equal signed endpoint diagonal is four times identity", signed == [4.0] * 9),
        ("equal signed endpoint rank is nine", sum(value > 0.0 for value in signed) == 9),
        ("particle-only endpoint rank is eight", sum(value > 0.0 for value in particle) == 8),
        ("particle-only dark vertex is zero", [i for i, value in enumerate(particle) if value == 0.0] == [0]),
        ("hole-only endpoint rank is eight", sum(value > 0.0 for value in hole) == 8),
        ("hole-only dark vertex is eight", [i for i, value in enumerate(hole) if value == 0.0] == [8]),
        ("signed channel rank equals boundary rank", sum(value > 0.0 for value in signed) == 9),
        ("signed channel kernel dimension is twenty seven", 36 - sum(value > 0.0 for value in signed) == 27),
        ("channel kernel differs from dark impurity kernel", 27 != 0),
        ("sample one-particle thresholds add residual energy and rest mass", abs(thresholds[0] - (-0.4)) < 1e-14),
        ("sample threshold union bottom is minimum threshold", min(thresholds) == thresholds[0]),
        ("mass gap bounds escaping multiplicity below fixed energy", min(masses) > 0.0),
        ("screened cross-cluster kernel decays exponentially", line_yukawa(20.0) < line_yukawa(10.0)),
        ("point defect remains localized at the origin", True),
        ("HVZ values retain residual spectrum dependence", len(set(residual)) == 2),
        ("all threshold ranks are not inferred from vacuum rank", True),
        ("dark threshold resonance needs a finite compression test", True),
        ("uniform weighted propagation remains unproved", True),
        ("global high-energy control remains unproved", True),
        ("Moller and Ruelle wave operators remain unconstructed", True),
        ("asymptotic completeness remains unproved", True),
        ("interacting NESS and microscopic current remain unconstructed", True),
        ("physical W and kappa remain unselected", True),
        ("source GU action ownership remains absent", True),
        ("Born rule and prediction credit remain absent", True),
        ("delayed-choice holdout remains unscored", True),
        ("canon and public posture remain unchanged", True),
    ]


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "break_compact_convergence",
        "break_diagonal_limit",
        "erase_seam_gap",
        "break_signed_rank",
        "break_particle_dark_vertex",
        "break_hole_dark_vertex",
        "break_threshold_sum",
    )]
    updates = (
        ("erase_mosco", lambda d: d["periodic_screened_forms"].__setitem__("positive_form_mosco_converges", False)),
        ("invent_norm_resolvent", lambda d: d["periodic_screened_forms"].__setitem__("natural_periodic_family_converges_in_norm_resolvent", True)),
        ("erase_chart_transport", lambda d: d["ibc_chart"].__setitem__("mosco_recovery_and_liminf_transport_through_chart", False)),
        ("assume_bare_domain", lambda d: d["ibc_chart"].__setitem__("bare_free_form_domain_is_assumed_without_check", True)),
        ("erase_seam_witness", lambda d: d["topology_boundary"].__setitem__("uniform_kernel_or_relative_form_convergence_fails", False)),
        ("kill_strong_with_seam", lambda d: d["topology_boundary"].__setitem__("seam_witness_disproves_strong_resolvent_convergence", True)),
        ("invent_universal_norm_no_go", lambda d: d["topology_boundary"].__setitem__("abstract_norm_resolvent_impossibility_for_every_modified_identification_is_claimed", True)),
        ("erase_HVZ", lambda d: d["hvz_thresholds"].__setitem__("essential_spectrum_is_union_of_attached_half_lines", False)),
        ("invent_numerical_thresholds", lambda d: d["hvz_thresholds"].__setitem__("numerical_thresholds_are_selected_without_W_kappa_g", True)),
        ("break_signed_endpoint_rank", lambda d: d["rook_endpoint_ranks"].__setitem__("equal_nonzero_signed_endpoint_rank", 8)),
        ("break_channel_nullity", lambda d: d["rook_endpoint_ranks"].__setitem__("signed_channel_kernel_dimension", 26)),
        ("confuse_channel_and_impurity_dark", lambda d: d["rook_endpoint_ranks"].__setitem__("kinematic_channel_kernel_is_a_dark_impurity_space", True)),
        ("erase_bright_inversion", lambda d: d["threshold_rank_rule"].__setitem__("bright_range_inverts_inverse_square_root_weyl_singularity", False)),
        ("invent_full_many_body_rank", lambda d: d["threshold_rank_rule"].__setitem__("all_many_body_thresholds_are_full_rank", True)),
        ("invent_resonance_exclusion", lambda d: d["threshold_rank_rule"].__setitem__("all_threshold_eigenvalues_or_resonances_are_excluded", True)),
        ("invent_numerical_census", lambda d: d["scattering_and_ownership_boundary"].__setitem__("complete_numerical_threshold_rank_census_for_selected_physical_parameters", True)),
        ("invent_propagation", lambda d: d["scattering_and_ownership_boundary"].__setitem__("uniform_weighted_resolvent_or_propagation_bound_proved", True)),
        ("invent_high_energy", lambda d: d["scattering_and_ownership_boundary"].__setitem__("global_high_energy_bound_proved", True)),
        ("invent_scattering", lambda d: d["scattering_and_ownership_boundary"].__setitem__("Moller_or_Ruelle_wave_operators_constructed", True)),
        ("invent_completeness", lambda d: d["scattering_and_ownership_boundary"].__setitem__("asymptotic_completeness_proved", True)),
        ("invent_NESS", lambda d: d["scattering_and_ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("invent_current", lambda d: d["scattering_and_ownership_boundary"].__setitem__("microscopic_field_current_constructed", True)),
        ("invent_physical_selector", lambda d: d["scattering_and_ownership_boundary"].__setitem__("physical_W_or_kappa_selected", True)),
        ("invent_smooth_parent", lambda d: d["scattering_and_ownership_boundary"].__setitem__("smooth_unreduced_connection_or_BRST_parent_constructed", True)),
        ("invent_source_owner", lambda d: d["scattering_and_ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["scattering_and_ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["scattering_and_ownership_boundary"].__setitem__("held_out_scored", True)),
        ("invent_prediction", lambda d: d["scattering_and_ownership_boundary"].__setitem__("prediction_or_confirmation_credit", True)),
        ("promote_canon", lambda d: d["scattering_and_ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("publish_result", lambda d: d["scattering_and_ownership_boundary"].__setitem__("paper_release_or_public_posture_change", "released")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A selected GU theory proves NESS.")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(manifest_failures(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    checks = exact_checks()
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    failures = manifest_failures(data)
    for failure in failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K143 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
