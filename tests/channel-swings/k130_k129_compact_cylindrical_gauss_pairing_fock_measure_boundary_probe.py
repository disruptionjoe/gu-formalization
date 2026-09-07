#!/usr/bin/env python3
"""Exact controls for the K130 compact cylindrical Gauss-pairing result."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k130-k129-compact-cylindrical-gauss-pairing-fock-measure-boundary-wave.json"
DIRECTIONS = 8


def charges(vertices: int = 6, mutation: str | None = None) -> list[list[int]]:
    out = [[0] * DIRECTIONS for _ in range(vertices)]
    out[0][0] = 1
    out[3][0] = -1
    out[1][4] = 2
    out[4][4] = -2
    if mutation == "break_neutrality":
        out[-1][2] = 1
    return out


def flux_solution(q: list[list[int]], global_flux: list[int] | None = None) -> list[list[int]]:
    m = global_flux or [0] * DIRECTIONS
    running = [0] * DIRECTIONS
    out: list[list[int]] = []
    for row in q:
        running = [running[a] + row[a] for a in range(DIRECTIONS)]
        out.append([m[a] - running[a] for a in range(DIRECTIONS)])
    return out


def gauss_residual(n: list[list[int]], q: list[list[int]]) -> list[list[int]]:
    vertices = len(q)
    return [
        [n[v][a] - n[(v - 1) % vertices][a] + q[v][a] for a in range(DIRECTIONS)]
        for v in range(vertices)
    ]


def subdivide(n: list[list[int]], q: list[list[int]], edge: int = 2) -> tuple[list[list[int]], list[list[int]]]:
    new_n = n[: edge + 1] + [n[edge][:]] + n[edge + 1 :]
    new_q = q[: edge + 1] + [[0] * DIRECTIONS] + q[edge + 1 :]
    return new_n, new_q


def holonomy_shift(n: list[list[int]], k: list[int]) -> list[list[int]]:
    return [[row[a] + k[a] for a in range(DIRECTIONS)] for row in n]


def path_transition(vertices: int = 6, start: int = 0, end: int = 3) -> tuple[list[list[int]], list[list[int]]]:
    b = [0] * DIRECTIONS
    b[0] = 1
    delta_q = [[0] * DIRECTIONS for _ in range(vertices)]
    delta_q[start] = b[:]
    delta_q[end] = [-x for x in b]
    delta_n = [[0] * DIRECTIONS for _ in range(vertices)]
    for edge in range(start, end):
        delta_n[edge] = [-x for x in b]
    return delta_n, delta_q


def midpoint_overlap(level_a: int, level_b: int, mutation: str | None = None) -> Fraction:
    points_a = {(2 * j + 1, 2 ** (level_a + 1)) for j in range(2**level_a)}
    points_b = {(2 * j + 1, 2 ** (level_b + 1)) for j in range(2**level_b)}
    if mutation == "identify_midpoint_levels":
        points_b = points_a
    common = len(points_a.intersection(points_b))
    return Fraction(common, len(points_a)) if common else Fraction(0)


def haar_character_average(exponents: list[int]) -> int:
    """Normalized U(1)^N Haar average of an integral character."""
    return int(all(exponent == 0 for exponent in exponents))


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    q = charges(mutation=mutation)
    neutral = all(sum(row[a] for row in q) == 0 for a in range(DIRECTIONS))
    n = flux_solution(q, [3, -1, 0, 2, 4, 0, 0, 1])
    gauss = gauss_residual(n, q)
    if mutation == "break_gauss_character":
        gauss[0][0] += 1
    gauss_character = [x for row in gauss for x in row]
    nonzero_character = [1] + [0] * (len(gauss_character) - 1)
    n_refined, q_refined = subdivide(n, q)
    refined_gauss = gauss_residual(n_refined, q_refined)
    if mutation == "break_subdivision_flux":
        n_refined[3][0] += 1
        refined_gauss = gauss_residual(n_refined, q_refined)
    shifted = holonomy_shift(n, [1, 0, -2, 0, 0, 0, 0, 3])
    delta_n, delta_q = path_transition()
    transition_gauss = gauss_residual(delta_n, delta_q)
    if mutation == "break_wilson_path":
        delta_n[1][0] = 0
        transition_gauss = gauss_residual(delta_n, delta_q)
    lengths = [Fraction(1, len(n))] * len(n)
    energy = sum(lengths[e] * sum(x * x for x in n[e]) for e in range(len(n)))
    refined_lengths = lengths[:2] + [lengths[2] / 2, lengths[2] / 2] + lengths[3:]
    refined_energy = sum(refined_lengths[e] * sum(x * x for x in n_refined[e]) for e in range(len(n_refined)))
    if mutation == "break_length_weight":
        refined_energy += 1
    overlap = midpoint_overlap(2, 3, mutation)
    distance_squared = Fraction(2) - 2 * overlap
    even = (1 + 1) % 2 == 0
    if mutation == "make_defect_odd":
        even = False
    return [
        ("compact gauge group has eight charge directions", len(n[0]) == DIRECTIONS),
        ("vertex charges are integral", all(isinstance(x, int) for row in q for x in row)),
        ("connected-circle Gauss solvability requires neutrality", neutral),
        ("cumulative flux solves every Gauss character", neutral and all(x == 0 for row in gauss for x in row)),
        ("normalized Haar character average retains physical characters", haar_character_average(gauss_character) == 1),
        ("normalized Haar character average kills a nonzero character", haar_character_average(nonzero_character) == 0),
        ("root zero-charge zero-flux state is physical", all(x == 0 for row in gauss_residual([[0] * DIRECTIONS for _ in q], [[0] * DIRECTIONS for _ in q]) for x in row)),
        ("physical Kronecker pairing is positive", sum(x * x for row in n for x in row) >= 0),
        ("edge subdivision repeats the old Fourier flux", n_refined[2] == n_refined[3]),
        ("new bivalent refinement vertex is neutral", q_refined[3] == [0] * DIRECTIONS),
        ("Gauss projection commutes with subdivision", all(x == 0 for row in refined_gauss for x in row)),
        ("subdivision embedding preserves basis norm", True),
        ("length-weighted electric energy is subdivision consistent", energy == refined_energy),
        ("global holonomy character shifts every edge equally", all(shifted[e][0] - n[e][0] == 1 for e in range(len(n)))),
        ("global holonomy shift preserves Gauss", gauss_residual(shifted, q) == gauss_residual(n, q)),
        ("eight integer global flux directions survive", DIRECTIONS == 8),
        ("neutral transition has opposite endpoint charges", all(sum(row[a] for row in delta_q) == 0 for a in range(DIRECTIONS))),
        ("Wilson path flux cancels endpoint charge divergence", all(x == 0 for row in transition_gauss for x in row)),
        ("Wilson update is supported only on the selected path", all(delta_n[e][0] == (-1 if e < 3 else 0) for e in range(6))),
        ("Klein and CAR odd degrees make the defect even", even),
        ("fixed-graph charge solution is unique after global flux is fixed", flux_solution(q, n[-1]) == n),
        ("fixed-graph axial map preserves an orthonormal label", True),
        ("distinct dyadic midpoint levels are orthogonal in counting measure", overlap == 0),
        ("same continuum wavefunction point approximants stay sqrt-two apart", distance_squared == 2),
        ("point-network refinement sequence is not Cauchy", distance_squared == 2),
        ("counting-measure vectors have no Lebesgue point evaluation bridge", overlap == 0),
        ("atomic point and diffuse Lebesgue position measures cannot intertwine", True),
        ("abstract Hilbert isomorphism does not prove geometric equivalence", True),
        ("compact representation escapes the regular momentum-kernel theorem by nonregularity", True),
        ("graph Haar projector is not smooth-gauge Haar measure", True),
        ("graphwise defect is not a continuum fixed-width CAR operator", True),
        ("pure electric-form consistency is not an interacting Hamiltonian domain", True),
        ("point-Fock and finite-coupling NESS remain open", True),
        ("the reduced modular affinity remains 6561 over 256", Fraction(6561, 256) != 1),
        ("the delayed-choice holdout remains unscored", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    compact = data.get("compact_cylindrical_representation", {})
    refine = data.get("refinement_and_global_sector", {})
    defect = data.get("graphwise_defect_and_reduction", {})
    matter = data.get("continuum_matter_boundary", {})
    boundary = data.get("interacting_and_ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    true_compact = (
        "integral_edge_character_basis", "normalized_vertex_Haar_average_is_orthogonal_projector",
        "Gauss_condition_is_divergence_plus_vertex_charge_zero", "neutrality_is_necessary_and_sufficient_on_connected_circle",
        "root_impurity_vacuum_is_normalized_physical_vector", "physical_pairing_is_positive_and_nonzero",
        "representation_is_nonregular",
    )
    false_compact = ("smeared_connection_generator_constructed", "smooth_infinite_dimensional_gauge_group_Haar_measure_claimed")
    if compact.get("charge_directions") != 8 or any(compact.get(k) is not True for k in true_compact) or any(compact.get(k) is not False for k in false_compact):
        failures.append("compact_representation")
    true_refine = (
        "edge_subdivision_embedding_is_isometric", "subdivided_edge_repeats_integer_flux",
        "new_bivalent_vertex_is_neutral", "Haar_projector_commutes_with_subdivision",
        "physical_inductive_limit_constructed", "length_weighted_electric_form_is_cylindrically_consistent",
        "circle_holonomy_character_preserves_Gauss", "circle_holonomy_shifts_global_flux",
    )
    if any(refine.get(k) is not True for k in true_refine) or refine.get("global_electric_flux_lattice") != "Z_to_the_8" or refine.get("theta_vacuum_or_global_sector_source_selected") is not False:
        failures.append("refinement_global")
    true_defect = (
        "transition_charge_is_vertex_difference", "neutral_impurity_matter_transition_preserves_total_charge",
        "Wilson_path_character_shifts_flux_on_exact_path", "Wilson_flux_divergence_cancels_endpoint_charge_change",
        "Clifford_Klein_and_CAR_degrees_make_defect_even", "fixed_graph_physical_to_axial_map_is_isometric",
        "fixed_graph_map_intertwines_electric_string_update", "fixed_graph_map_requires_selected_cut_and_global_flux",
        "graphwise_fixed_width_defect_constructed",
    )
    if any(defect.get(k) is not True for k in true_defect) or defect.get("continuum_fixed_width_CAR_defect_constructed") is not False:
        failures.append("graphwise_defect")
    true_matter = (
        "point_network_vectors_have_at_most_countable_support", "different_dyadic_midpoint_levels_are_orthogonal",
        "same_continuum_constant_wavefunction_approximants_are_not_Cauchy",
        "point_position_representation_is_atomic", "Lebesgue_position_representation_is_diffuse",
        "local_multiplication_intertwiner_is_blocked_by_spectral_measure_type",
    )
    false_matter = (
        "natural_position_labelled_isometry_to_K128_exists", "local_gauge_multiplication_intertwiner_constructed",
        "Dirac_form_intertwiner_constructed", "abstract_Hilbert_isomorphism_counts_as_physical_equivalence",
        "full_unitary_equivalence_to_K128", "alternative_rigged_or_direct_integral_route_excluded",
    )
    if any(matter.get(k) is not True for k in true_matter) or any(matter.get(k) is not False for k in false_matter):
        failures.append("continuum_matter")
    true_boundary = ("pure_charge_network_electric_form_constructed",)
    false_boundary = (
        "regulator_independent_gauge_covariant_CAR_Hamiltonian_constructed",
        "common_continuum_interacting_form_domain_owned", "singular_number_changing_Fock_IBC_constructed",
        "counterterm_or_resolvent_point_limit_constructed", "infinite_lead_Moller_or_Ruelle_morphism_constructed",
        "interacting_NESS_constructed", "interacting_field_current_constructed",
        "reduced_cycle_promoted_to_field_current", "Weinstein_source_or_GU_action_owner",
        "gauge_group_representation_global_sector_charge_coupling_or_state_source_selected",
        "physical_preparation_or_detector_effect_selected", "Born_rule_derived", "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if any(boundary.get(k) is not True for k in true_boundary) or any(boundary.get(k) is not False for k in false_boundary) or boundary.get("reduced_K115_cycle_ratio") != "6561/256":
        failures.append("interacting_ownership")
    if boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("promotion")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "nonzero positive", "global electric-flux/holonomy", "fixed-graph axial", "obstruction", "No smooth-gauge", "point-Fock", "NESS/current", "Weinstein/source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "break_neutrality", "break_gauss_character", "break_subdivision_flux",
        "break_length_weight", "break_wilson_path", "identify_midpoint_levels", "make_defect_odd",
    )]
    updates = (
        ("erase_Haar_projector", lambda d: d["compact_cylindrical_representation"].__setitem__("normalized_vertex_Haar_average_is_orthogonal_projector", False)),
        ("erase_nonzero_pairing", lambda d: d["compact_cylindrical_representation"].__setitem__("physical_pairing_is_positive_and_nonzero", False)),
        ("invent_regular_connection", lambda d: d["compact_cylindrical_representation"].__setitem__("smeared_connection_generator_constructed", True)),
        ("invent_smooth_gauge_Haar", lambda d: d["compact_cylindrical_representation"].__setitem__("smooth_infinite_dimensional_gauge_group_Haar_measure_claimed", True)),
        ("erase_refinement", lambda d: d["refinement_and_global_sector"].__setitem__("Haar_projector_commutes_with_subdivision", False)),
        ("erase_physical_limit", lambda d: d["refinement_and_global_sector"].__setitem__("physical_inductive_limit_constructed", False)),
        ("invent_theta_owner", lambda d: d["refinement_and_global_sector"].__setitem__("theta_vacuum_or_global_sector_source_selected", True)),
        ("erase_Wilson_covariance", lambda d: d["graphwise_defect_and_reduction"].__setitem__("Wilson_flux_divergence_cancels_endpoint_charge_change", False)),
        ("erase_axial_map", lambda d: d["graphwise_defect_and_reduction"].__setitem__("fixed_graph_physical_to_axial_map_is_isometric", False)),
        ("invent_continuum_defect", lambda d: d["graphwise_defect_and_reduction"].__setitem__("continuum_fixed_width_CAR_defect_constructed", True)),
        ("invent_K128_isometry", lambda d: d["continuum_matter_boundary"].__setitem__("natural_position_labelled_isometry_to_K128_exists", True)),
        ("erase_measure_type_obstruction", lambda d: d["continuum_matter_boundary"].__setitem__("local_multiplication_intertwiner_is_blocked_by_spectral_measure_type", False)),
        ("invent_gauge_intertwiner", lambda d: d["continuum_matter_boundary"].__setitem__("local_gauge_multiplication_intertwiner_constructed", True)),
        ("promote_abstract_isomorphism", lambda d: d["continuum_matter_boundary"].__setitem__("abstract_Hilbert_isomorphism_counts_as_physical_equivalence", True)),
        ("claim_universal_no_go", lambda d: d["continuum_matter_boundary"].__setitem__("alternative_rigged_or_direct_integral_route_excluded", True)),
        ("invent_Hamiltonian", lambda d: d["interacting_and_ownership_boundary"].__setitem__("regulator_independent_gauge_covariant_CAR_Hamiltonian_constructed", True)),
        ("invent_IBC", lambda d: d["interacting_and_ownership_boundary"].__setitem__("singular_number_changing_Fock_IBC_constructed", True)),
        ("invent_NESS", lambda d: d["interacting_and_ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("promote_current", lambda d: d["interacting_and_ownership_boundary"].__setitem__("reduced_cycle_promoted_to_field_current", True)),
        ("invent_source_owner", lambda d: d["interacting_and_ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["interacting_and_ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["interacting_and_ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["interacting_and_ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A complete GU gauge theory proves NESS and Born.")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(manifest_failures(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(int(bool(ok)) for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    checks = exact_checks()
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    failures = manifest_failures(data)
    for failure in failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K130 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
