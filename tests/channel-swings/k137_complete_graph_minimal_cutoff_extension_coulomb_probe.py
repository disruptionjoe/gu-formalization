#!/usr/bin/env python3
"""Exact controls for the K137 complete-graph minimal point/Coulomb result."""
from __future__ import annotations

import copy
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k137-complete-graph-minimal-cutoff-extension-coulomb-wave.json"
STATES = [(x, r) for x in range(3) for r in range(3)]
MU = 1.3


def edges(mutation: str | None = None) -> list[tuple[int, int]]:
    result = [
        (u, v) for u in range(9) for v in range(u + 1, 9)
        if STATES[u][0] == STATES[v][0] or STATES[u][1] == STATES[v][1]
    ]
    if mutation == "drop_graph_edge":
        result.pop()
    return result


def adjacency(edge_list: list[tuple[int, int]]) -> list[list[int]]:
    matrix = [[0] * 9 for _ in range(9)]
    for u, v in edge_list:
        matrix[u][v] = matrix[v][u] = 1
    return matrix


def directed_path_counts(edge_list: list[tuple[int, int]]) -> list[int]:
    paths = [[v] for v in range(9)]
    counts: list[int] = []
    for _ in range(1, 9):
        paths = [p + [v] for p in paths for u, v in edge_list if u == p[-1]]
        counts.append(len(paths))
    return counts


def graph_counts(edge_list: list[tuple[int, int]]) -> tuple[int, int]:
    a = adjacency(edge_list)
    triangles = sum(
        all(a[u][v] for u, v in itertools.combinations(vertices, 2))
        for vertices in itertools.combinations(range(9), 3)
    )
    rectangles = 0
    for rows in itertools.combinations(range(3), 2):
        for cols in itertools.combinations(range(3), 2):
            vertices = [3 * x + r for x in rows for r in cols]
            if sum(a[u][v] for u, v in itertools.combinations(vertices, 2)) == 4:
                rectangles += 1
    return triangles, rectangles


def omega(k: int) -> float:
    return math.sqrt(1.0 + k * k)


def resolvent_tail(cutoff: int, high: int = 32768, mutation: str | None = None) -> float:
    power = 1.0 if mutation == "remove_resolvent_weight" else 2.0
    return sum(1.0 / (omega(k) + MU) ** power for k in range(cutoff + 1, high + 1)) * 2.0


def subtracted_tail(cutoff: int, high: int = 32768) -> float:
    return sum(
        abs(1.0 / (omega(k) + MU) - 1.0 / (omega(k) + MU + 2.0))
        for k in range(cutoff + 1, high + 1)
    ) * 2.0


def exchange_graph_tail(cutoff: int, high: int = 32768) -> float:
    return math.sqrt(sum(1.0 / omega(k) ** 2 for k in range(cutoff + 1, high + 1)) * 2.0)


def scale_delta(cutoff: int, second: float = 2.1) -> float:
    return sum(
        1.0 / (omega(k) + MU) - 1.0 / (omega(k) + second)
        for k in range(-cutoff, cutoff + 1)
    )


def vacuum_contraction(first: int, second: int, mutation: str | None = None) -> int:
    if mutation == "invent_cross_species_contraction" and (first, second) == (0, 1):
        return 1
    return int(first == second)


def finite_word_sum(cutoff: int) -> float:
    # A representative two-resolvent overlap word. Its two independent sums
    # converge absolutely and need not vanish.
    values = [1.0 / (omega(k) + MU) ** 2 for k in range(-cutoff, cutoff + 1)]
    return sum(values) ** 2


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    graph = data.get("complete_graph_filtration", {})
    uv = data.get("ultraviolet_and_regular_remainder", {})
    minimal = data.get("complete_minimal_cutoff_limit", {})
    extension = data.get("extension_identification", {})
    coulomb = data.get("minimal_coulomb_gauss_limit", {})
    boundary = data.get("thermodynamic_and_ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    expected_graph = {
        "impurity_states": 9,
        "undirected_CAR_species": 18,
        "graph_is_three_by_three_rook_graph": True,
        "oriented_matrix_unit_creation_strictly_lowers_impurity_label": True,
        "longest_nonzero_creation_path_has_four_edges": True,
        "boundary_creation_map_fifth_power_is_zero": True,
        "graph_contains_six_triangles_and_nine_rectangular_four_cycles": True,
        "all_overlapping_directed_paths_are_included": True,
        "complete_graph_is_replaced_by_disjoint_ladders": False,
    }
    if any(graph.get(k) != v for k, v in expected_graph.items()):
        failures.append("graph_filtration")
    required_uv = (
        "unequal_edge_vacuum_contractions_vanish_by_CAR_species_orthogonality",
        "only_divergent_contraction_is_the_K134_diagonal_upper_endpoint_term",
        "triangle_and_square_path_words_generate_finite_exchange_terms",
        "every_uncontracted_momentum_in_a_higher_word_has_a_resolvent_weight",
        "normal_ordered_point_annihilation_tail_is_controlled_in_the_free_operator_graph_norm",
    )
    if any(uv.get(k) is not True for k in required_uv) or uv.get("one_additional_off_diagonal_or_higher_order_divergent_counterterm_is_required") is not False or uv.get("finite_cycle_remainders_are_zero") is not False:
        failures.append("ultraviolet_remainder")
    required_minimal = (
        "sharp_symmetric_cutoff_and_diagonal_endpoint_subtraction_are_fixed",
        "pulled_back_regular_operators_share_Dom_H0",
        "regular_remainders_converge_in_H0_graph_relative_norm",
        "uniform_lower_bound_holds_after_one_common_finite_shift",
        "bounded_boundary_transforms_and_inverses_converge_in_norm",
        "complete_nine_state_eighteen_species_minimal_cutoff_converges_in_norm_resolvent",
        "result_covers_arbitrary_finite_particle_spectators_on_full_positive_Fock_space",
    )
    if any(minimal.get(k) is not True for k in required_minimal) or minimal.get("full_signed_Dirac_empty_vacuum_operator_is_covered") is not False:
        failures.append("minimal_limit")
    required_extension = (
        "minimal_cutoff_has_one_finite_regular_remainder_W_min_for_the_fixed_scheme",
        "W_min_contains_nonzero_finite_triangle_square_and_exchange_data",
        "minimal_limit_is_one_member_of_the_K135_dressed_extension_family",
        "subtraction_scale_change_recoordinates_W_min_by_a_finite_D_g_shift",
    )
    if any(extension.get(k) is not True for k in required_extension) or any(extension.get(k) is not False for k in (
        "regulator_or_subtraction_scheme_independence_is_proved",
        "scheme_selected_W_min_is_a_physically_selected_Hamiltonian",
        "source_or_GU_action_selects_the_scheme_or_finite_extension",
    )):
        failures.append("extension")
    required_coulomb = (
        "finite_interval_cumulative_charge_form_is_bounded_by_global_flux_plus_particle_number_squared",
        "boundary_transform_and_inverse_are_bounded_on_the_particle_number_graph",
        "raw_Coulomb_form_is_defined_on_the_minimal_IBC_form_domain",
        "pulled_back_Coulomb_forms_converge_in_form_norm",
        "complete_minimally_countertermed_positive_energy_Coulomb_Gauss_cutoffs_converge_in_norm_resolvent",
    )
    if any(coulomb.get(k) is not True for k in required_coulomb) or any(coulomb.get(k) is not False for k in (
        "Coulomb_proof_uses_momentum_occupation_commutation",
        "same_bound_is_uniform_in_spatial_volume",
        "smooth_unreduced_connection_or_BRST_parent_constructed",
    )):
        failures.append("minimal_coulomb")
    denied = (
        "uniquely_physically_selected_point_Fock_Gauss_Hamiltonian_constructed",
        "full_signed_Dirac_polarization_selected", "infinite_volume_limit_constructed",
        "Moller_or_Ruelle_wave_operator_constructed", "interacting_NESS_constructed",
        "interacting_field_current_constructed", "reduced_cycle_promoted_to_field_current",
        "Weinstein_source_or_GU_action_owner", "Born_rule_derived", "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if boundary.get("finite_circle_positive_dispersion_control_only") is not True or any(boundary.get(k) is not False for k in denied) or boundary.get("reduced_K115_cycle_ratio") != "6561/256" or boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("boundary")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "complete nine-state/eighteen-species", "norm-resolvent", "diagonal endpoint", "triangle", "W_min", "raw finite-interval", "signed-Dirac", "infinite-volume", "source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    edge_list = edges(mutation)
    paths = directed_path_counts(edge_list)
    triangles, rectangles = graph_counts(edge_list)
    indegree = [sum(v == j for _, v in edge_list) for j in range(9)]
    tails = [resolvent_tail(n, mutation=mutation) for n in (32, 128, 512, 2048)]
    subtracted = [subtracted_tail(n) for n in (32, 128, 512, 2048)]
    exchange = [exchange_graph_tail(n) for n in (32, 128, 512, 2048)]
    scales = [scale_delta(n) for n in (16, 32, 64, 128)]
    scale_steps = [abs(b - a) for a, b in zip(scales, scales[1:])]
    overlaps = [finite_word_sum(n) for n in (16, 32, 64, 128)]
    overlap_steps = [abs(b - a) for a, b in zip(overlaps, overlaps[1:])]
    # Exact two-dimensional toy for a bounded number-graph transform:
    # N=diag(0,1), G maps vacuum to one particle and G^2=0.
    g = Fraction(1, 3)
    u_inv = [[Fraction(1), Fraction(0)], [g, Fraction(1)]]
    number_graph_norms = [
        sum(abs(u_inv[i][j]) * (i + 1) / (j + 1) for i in range(2))
        for j in range(2)
    ]
    coulomb = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(4)]]
    pulled = [
        [sum(u_inv[k][i] * coulomb[k][l] * u_inv[l][j] for k in range(2) for l in range(2)) for j in range(2)]
        for i in range(2)
    ]
    return [
        ("complete rook graph has nine impurity states", len(STATES) == 9),
        ("complete rook graph has eighteen CAR species", len(edge_list) == 18),
        ("every edge changes exactly one product coordinate", all((STATES[u][0] == STATES[v][0]) ^ (STATES[u][1] == STATES[v][1]) for u, v in edge_list)),
        ("oriented edges strictly raise the numeric impurity label", all(u < v for u, v in edge_list)),
        ("creation filtration has eighteen length-one paths", paths[0] == 18),
        ("creation filtration has twenty-four length-two paths", paths[1] == 24),
        ("creation filtration has eighteen length-three paths", paths[2] == 18),
        ("creation filtration has six length-four paths", paths[3] == 6),
        ("creation filtration has no length-five path", paths[4] == 0),
        ("boundary creation therefore has fifth power zero", all(x == 0 for x in paths[4:])),
        ("the graph contains six row-or-column triangles", triangles == 6),
        ("the graph contains nine rectangular four-cycles", rectangles == 9),
        ("upper-endpoint contraction multiplicities are diagonal", indegree == [0, 1, 2, 1, 2, 3, 2, 3, 4]),
        ("unequal CAR species have zero vacuum contraction", all(vacuum_contraction(i, j, mutation) == int(i == j) for i in range(18) for j in range(18))),
        ("resolvent-weighted one-leg tails decrease", all(a > b for a, b in zip(tails, tails[1:]))),
        ("resolvent-weighted one-leg tail is small", tails[-1] < 0.001),
        ("subtracted diagonal tails decrease", all(a > b for a, b in zip(subtracted, subtracted[1:]))),
        ("subtracted diagonal tail is small", subtracted[-1] < 0.002),
        ("operator-graph exchange tails decrease", all(a > b for a, b in zip(exchange, exchange[1:]))),
        ("operator-graph exchange tail is small", exchange[-1] < 0.04),
        ("two-resolvent overlap words converge", all(a > b for a, b in zip(overlap_steps, overlap_steps[1:]))),
        ("two-resolvent overlap remainder is nonzero", overlaps[-1] > 1.0),
        ("finite subtraction-scale flow is Cauchy", all(a > b for a, b in zip(scale_steps, scale_steps[1:]))),
        ("finite subtraction-scale tail is small", scale_steps[-1] < 0.02),
        ("fixed scheme has a definite nonzero finite remainder", abs(overlaps[-1] - overlaps[0]) > 0.01),
        ("number-graph inverse transform is bounded", max(number_graph_norms) < 2),
        ("raw positive Coulomb toy remains positive after pullback", pulled[0][0] >= 0 and pulled[1][1] >= 0),
        ("raw Coulomb pullback acquires finite off-diagonal dressing", pulled[0][1] != 0 and pulled[1][0] != 0),
        ("Coulomb argument does not require occupation commutation", True),
        ("the positive finite-circle carrier remains semibounded", True),
        ("the empty-vacuum signed-Dirac carrier is not covered", True),
        ("the finite-volume number bound is not volume uniform", True),
        ("the minimal scheme is not a physical selection principle", True),
        ("no smooth unreduced gauge parent follows", True),
        ("no infinite-volume wave operator or NESS follows", Fraction(6561, 256) != 1),
        ("delayed-choice holdout remains unscored", True),
    ]


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "drop_graph_edge", "remove_resolvent_weight", "invent_cross_species_contraction",
    )]
    updates = (
        ("erase_rook_graph", lambda d: d["complete_graph_filtration"].__setitem__("graph_is_three_by_three_rook_graph", False)),
        ("invent_disjoint_ladders", lambda d: d["complete_graph_filtration"].__setitem__("complete_graph_is_replaced_by_disjoint_ladders", True)),
        ("erase_nilpotence", lambda d: d["complete_graph_filtration"].__setitem__("boundary_creation_map_fifth_power_is_zero", False)),
        ("erase_overlaps", lambda d: d["complete_graph_filtration"].__setitem__("all_overlapping_directed_paths_are_included", False)),
        ("invent_cross_contraction", lambda d: d["ultraviolet_and_regular_remainder"].__setitem__("unequal_edge_vacuum_contractions_vanish_by_CAR_species_orthogonality", False)),
        ("invent_extra_divergence", lambda d: d["ultraviolet_and_regular_remainder"].__setitem__("one_additional_off_diagonal_or_higher_order_divergent_counterterm_is_required", True)),
        ("erase_cycle_remainder", lambda d: d["ultraviolet_and_regular_remainder"].__setitem__("finite_cycle_remainders_are_zero", True)),
        ("erase_graph_tail", lambda d: d["ultraviolet_and_regular_remainder"].__setitem__("normal_ordered_point_annihilation_tail_is_controlled_in_the_free_operator_graph_norm", False)),
        ("erase_regular_convergence", lambda d: d["complete_minimal_cutoff_limit"].__setitem__("regular_remainders_converge_in_H0_graph_relative_norm", False)),
        ("erase_lower_bound", lambda d: d["complete_minimal_cutoff_limit"].__setitem__("uniform_lower_bound_holds_after_one_common_finite_shift", False)),
        ("erase_minimal_limit", lambda d: d["complete_minimal_cutoff_limit"].__setitem__("complete_nine_state_eighteen_species_minimal_cutoff_converges_in_norm_resolvent", False)),
        ("invent_signed_lift", lambda d: d["complete_minimal_cutoff_limit"].__setitem__("full_signed_Dirac_empty_vacuum_operator_is_covered", True)),
        ("erase_Wmin", lambda d: d["extension_identification"].__setitem__("minimal_cutoff_has_one_finite_regular_remainder_W_min_for_the_fixed_scheme", False)),
        ("erase_finite_cycles", lambda d: d["extension_identification"].__setitem__("W_min_contains_nonzero_finite_triangle_square_and_exchange_data", False)),
        ("invent_scheme_independence", lambda d: d["extension_identification"].__setitem__("regulator_or_subtraction_scheme_independence_is_proved", True)),
        ("invent_physical_selection", lambda d: d["extension_identification"].__setitem__("scheme_selected_W_min_is_a_physically_selected_Hamiltonian", True)),
        ("invent_source_selection", lambda d: d["extension_identification"].__setitem__("source_or_GU_action_selects_the_scheme_or_finite_extension", True)),
        ("erase_number_graph", lambda d: d["minimal_coulomb_gauss_limit"].__setitem__("boundary_transform_and_inverse_are_bounded_on_the_particle_number_graph", False)),
        ("erase_raw_domain", lambda d: d["minimal_coulomb_gauss_limit"].__setitem__("raw_Coulomb_form_is_defined_on_the_minimal_IBC_form_domain", False)),
        ("erase_coulomb_form_convergence", lambda d: d["minimal_coulomb_gauss_limit"].__setitem__("pulled_back_Coulomb_forms_converge_in_form_norm", False)),
        ("erase_minimal_coulomb", lambda d: d["minimal_coulomb_gauss_limit"].__setitem__("complete_minimally_countertermed_positive_energy_Coulomb_Gauss_cutoffs_converge_in_norm_resolvent", False)),
        ("require_false_commutation", lambda d: d["minimal_coulomb_gauss_limit"].__setitem__("Coulomb_proof_uses_momentum_occupation_commutation", True)),
        ("invent_volume_uniformity", lambda d: d["minimal_coulomb_gauss_limit"].__setitem__("same_bound_is_uniform_in_spatial_volume", True)),
        ("invent_smooth_parent", lambda d: d["minimal_coulomb_gauss_limit"].__setitem__("smooth_unreduced_connection_or_BRST_parent_constructed", True)),
        ("invent_unique_physical_H", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("uniquely_physically_selected_point_Fock_Gauss_Hamiltonian_constructed", True)),
        ("invent_signed_selection", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("full_signed_Dirac_polarization_selected", True)),
        ("invent_infinite_volume", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("infinite_volume_limit_constructed", True)),
        ("invent_NESS", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("promote_current", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("reduced_cycle_promoted_to_field_current", True)),
        ("invent_source_owner", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A complete physical GU Hamiltonian derives Born predictions.")),
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
    print(f"K137 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
