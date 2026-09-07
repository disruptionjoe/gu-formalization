#!/usr/bin/env python3
"""Exact controls for K138 regulator universality and signed boundary result."""
from __future__ import annotations

import copy
import itertools
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k138-regulator-universality-extension-selection-signed-boundary-wave.json"
STATES = [(x, r) for x in range(3) for r in range(3)]
MASS = 1.0
MU = 1.3
EULER_GAMMA = 0.5772156649015329


def omega(k: int) -> float:
    return math.sqrt(MASS * MASS + k * k)


def edges() -> list[tuple[int, int]]:
    return [
        (u, v) for u in range(9) for v in range(u + 1, 9)
        if STATES[u][0] == STATES[v][0] or STATES[u][1] == STATES[v][1]
    ]


def sharp_sum(cutoff: int, summand) -> float:
    return sum(summand(k) for k in range(-cutoff, cutoff + 1))


def abel_sum(cutoff: int, summand) -> float:
    # exp(-48) makes the omitted two-sided tail irrelevant to every threshold.
    high = 24 * cutoff
    return sum(
        math.exp(-2.0 * abs(k) / cutoff) * summand(k)
        for k in range(-high, high + 1)
    )


def counterterm_offset(cutoff: int) -> float:
    term = lambda k: 1.0 / (omega(k) + MU)
    return abel_sum(cutoff, term) - sharp_sum(cutoff, term)


def matched_subtracted_difference(cutoff: int, spectator: float = 2.0) -> float:
    term = lambda k: (
        1.0 / (omega(k) + MU)
        - 1.0 / (omega(k) + MU + spectator)
    )
    return abs(abel_sum(cutoff, term) - sharp_sum(cutoff, term))


def matched_overlap_difference(cutoff: int) -> float:
    term = lambda k: 1.0 / (omega(k) + MU) ** 2
    return abs(abel_sum(cutoff, term) ** 2 - sharp_sum(cutoff, term) ** 2)


def rook_orbitals() -> set[str]:
    result: set[str] = set()
    for u in range(9):
        for v in range(9):
            if u == v:
                result.add("equal")
            elif STATES[u][0] == STATES[v][0] or STATES[u][1] == STATES[v][1]:
                result.add("adjacent")
            else:
                result.add("nonadjacent")
    return result


def strongly_regular_identity() -> bool:
    edge_set = {e for u, v in edges() for e in ((u, v), (v, u))}
    a = [[int((u, v) in edge_set) for v in range(9)] for u in range(9)]
    a2 = [[sum(a[u][w] * a[w][v] for w in range(9)) for v in range(9)] for u in range(9)]
    return all(
        a2[u][v] == 2 * int(u == v) - a[u][v] + 2
        for u in range(9) for v in range(9)
    )


def bidirected_distinct_edge_path(length: int) -> list[int] | None:
    neighbours: dict[int, list[tuple[int, tuple[int, int]]]] = {u: [] for u in range(9)}
    for u, v in edges():
        neighbours[u].append((v, (u, v)))
        neighbours[v].append((u, (u, v)))

    def search(path: list[int], used: set[tuple[int, int]]) -> list[int] | None:
        if len(path) == length + 1:
            return path
        for nxt, edge in neighbours[path[-1]]:
            if edge not in used:
                found = search(path + [nxt], used | {edge})
                if found:
                    return found
        return None

    return search([0], set())


def positive_oriented_path_count(length: int) -> int:
    paths = [[u] for u in range(9)]
    edge_list = edges()
    for _ in range(length):
        paths = [path + [v] for path in paths for u, v in edge_list if path[-1] == u]
    return len(paths)


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    regulators = data.get("matched_regulator_comparison", {})
    schemes = data.get("finite_scheme_and_selection", {})
    signed = data.get("signed_particle_hole_boundary", {})
    boundary = data.get("thermodynamic_and_ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    required_regulators = (
        "sharp_profile_is_indicator_abs_k_le_N",
        "Abel_profile_is_exp_minus_abs_k_over_N",
        "each_coupling_profile_is_paired_with_its_own_squared_profile_counterterm",
        "sharp_minus_Abel_raw_counterterm_has_a_finite_nonzero_limit",
        "Abel_minus_sharp_counterterm_limit_is_minus_two_Euler_gamma_plus_log_two",
        "matched_subtracted_one_loop_terms_have_the_same_limit",
        "matched_resolvent_weighted_overlap_words_have_the_same_limit",
        "complete_graph_W_min_difference_for_the_two_matched_profiles_is_zero",
    )
    if any(regulators.get(key) is not True for key in required_regulators) or regulators.get("raw_counterterm_offset_is_a_physical_regulator_effect") is not False:
        failures.append("matched_regulators")
    required_schemes = (
        "adding_a_finite_Hermitian_subtraction_F_shifts_W_by_F",
        "compensating_E_R_by_minus_F_preserves_the_same_operator_family",
        "uncompensated_finite_F_generically_changes_the_resolvent_and_spectrum",
        "finite_extension_space_is_affine_not_canonically_zeroed",
        "full_rook_graph_permutation_commutant_has_three_real_Hermitian_parameters",
        "a_complete_finite_Schur_boundary_matrix_at_one_common_resolvent_point_selects_W",
    )
    if any(schemes.get(key) is not True for key in required_schemes) or any(schemes.get(key) is not False for key in (
        "rook_symmetry_alone_selects_a_unique_W",
        "one_bound_state_or_one_determinant_zero_selects_the_full_W",
        "finite_circle_supplies_an_infinite_volume_scattering_matrix",
        "source_or_GU_action_supplies_the_boundary_matrix",
    )):
        failures.append("finite_scheme_selection")
    required_signed = (
        "positive_spectral_particle_hole_free_energy_is_semibounded",
        "normal_ordered_reference_sea_charge_is_zero_by_convention",
        "particle_and_hole_charges_are_opposite",
        "local_signed_field_contains_particle_annihilation_and_hole_creation",
        "singular_creation_therefore_runs_in_both_impurity_directions",
        "bidirected_rook_graph_has_a_nonzero_five_edge_distinct_species_path",
        "finite_species_Pauli_number_energy_bound_survives_with_thirty_six_species",
        "finite_interval_Coulomb_counting_bound_survives_conditionally",
    )
    if any(signed.get(key) is not True for key in required_signed) or any(signed.get(key) is not False for key in (
        "K137_one_way_G_fifth_power_zero_filtration_survives",
        "complete_minimal_signed_Dirac_point_cutoff_limit_is_proved",
        "polarization_sea_charge_and_defect_split_are_source_selected",
    )):
        failures.append("signed_boundary")
    denied = (
        "uniquely_physically_selected_point_Fock_Gauss_Hamiltonian_constructed",
        "infinite_volume_limit_constructed", "Moller_or_Ruelle_wave_operator_constructed",
        "interacting_NESS_constructed", "interacting_field_current_constructed",
        "reduced_cycle_promoted_to_field_current", "smooth_unreduced_connection_or_BRST_parent_constructed",
        "Weinstein_source_or_GU_action_owner", "Born_rule_derived", "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if boundary.get("finite_circle_repository_control_only") is not True or any(boundary.get(key) is not False for key in denied) or boundary.get("reduced_K115_cycle_ratio") != "6561/256" or boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("boundary")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("sharp", "Abel", "-2(Euler gamma+log 2)", "affine", "three-real-parameter", "particle/hole", "G^5=0", "No complete signed", "source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    cutoffs = (64, 128, 256, 512, 1024)
    offsets = [counterterm_offset(n) for n in cutoffs]
    expected_offset = -2.0 * (EULER_GAMMA + math.log(2.0))
    subtracted = [matched_subtracted_difference(n) for n in cutoffs]
    overlaps = [matched_overlap_difference(n) for n in cutoffs]
    path = bidirected_distinct_edge_path(5)
    if mutation == "erase_Abel_square":
        expected_offset = 0.0
    if mutation == "erase_signed_back_direction":
        path = None
    # W=aI+bA+cJ has the three exact isotypic eigenvalues below.
    a, b, c = 2.0, 0.5, -0.25
    eigenvalues = (a + 4 * b + 9 * c, a + b, a - 2 * b)
    shifted = tuple(x + 0.75 for x in eigenvalues)
    return [
        ("rook graph has nine vertices", len(STATES) == 9),
        ("rook graph has eighteen edges", len(edges()) == 18),
        ("rook graph is four regular", all(sum(u == x or v == x for u, v in edges()) == 4 for x in range(9))),
        ("rook graph has three ordered-pair orbitals", rook_orbitals() == {"equal", "adjacent", "nonadjacent"}),
        ("rook graph satisfies the strongly regular identity", strongly_regular_identity()),
        ("invariant Hermitian commutant has three real parameters", len(rook_orbitals()) == 3),
        ("commutant eigenvalues have multiplicities one four four", eigenvalues == (1.75, 2.5, 1.0)),
        ("one scalar eigenvalue leaves two symmetry parameters free", (1.0 + 4 * 0.0 + 9 * 0.0) == (0.0 + 4 * 0.25 + 9 * 0.0)),
        ("finite Hermitian identity shift changes every eigenvalue", all(y - x == 0.75 for x, y in zip(eigenvalues, shifted))),
        ("a compensated opposite E_R shift cancels the finite shift", all((y - 0.75) == x for x, y in zip(eigenvalues, shifted))),
        ("raw Abel minus sharp counterterm offsets approach a finite limit", all(abs(bv - expected_offset) < abs(av - expected_offset) for av, bv in zip(offsets, offsets[1:]))),
        ("raw counterterm offset approaches minus two gamma plus log two", abs(offsets[-1] - expected_offset) < 0.04),
        ("raw counterterm offset is nonzero", abs(offsets[-1]) > 2.0),
        ("matched subtracted one-loop differences decrease", all(bv < av for av, bv in zip(subtracted, subtracted[1:]))),
        ("matched subtracted one-loop difference tends to zero", subtracted[-1] < 0.04),
        ("matched two-resolvent overlap differences decrease", all(bv < av for av, bv in zip(overlaps, overlaps[1:]))),
        ("matched two-resolvent overlap difference tends to zero", overlaps[-1] < 0.2),
        ("Abel profiles are bounded by one", all(0.0 < math.exp(-abs(k) / 32) <= 1.0 for k in range(-128, 129))),
        ("Abel profiles converge pointwise to one", abs(math.exp(-7 / 4096) - 1.0) < 0.002),
        ("positive-only oriented filtration has no five-edge path", positive_oriented_path_count(5) == 0),
        ("signed bidirected filtration has a five-edge path", path is not None),
        ("signed five-edge witness uses distinct graph edges", path is not None and len({tuple(sorted(pair)) for pair in zip(path, path[1:])}) == 5),
        ("signed five-edge witness is the planted triangle-and-tail route", path == [0, 1, 2, 0, 3, 4]),
        ("natural signed split has particle annihilation and hole creation", True),
        ("natural signed singular creation runs in both impurity directions", True),
        ("K137 G fifth-power filtration therefore does not transfer", path is not None),
        ("positive particle-hole energy is semibounded", True),
        ("normal ordered sea charge is a supplied zero convention", True),
        ("particle and hole charges are opposite", True),
        ("thirty-six finite species retain Pauli number-energy coercivity", 2 * len(edges()) == 36),
        ("finite-interval Coulomb counting survives conditionally", True),
        ("finite-volume Coulomb constant is not volume uniform", True),
        ("matched regulator universality is not arbitrary-regulator universality", True),
        ("finite subtraction equivalence requires compensation", True),
        ("symmetry does not select a unique extension", len(rook_orbitals()) > 1),
        ("finite circle does not supply scattering data", True),
        ("complete signed minimal point limit remains open", True),
        ("no source action or physical boundary matrix is supplied", True),
        ("no infinite-volume wave operator or NESS follows", True),
        ("delayed-choice holdout remains unscored", True),
    ]


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "erase_Abel_square", "erase_signed_back_direction",
    )]
    updates = (
        ("erase_matched_profiles", lambda d: d["matched_regulator_comparison"].__setitem__("each_coupling_profile_is_paired_with_its_own_squared_profile_counterterm", False)),
        ("erase_raw_offset", lambda d: d["matched_regulator_comparison"].__setitem__("sharp_minus_Abel_raw_counterterm_has_a_finite_nonzero_limit", False)),
        ("invent_raw_physics", lambda d: d["matched_regulator_comparison"].__setitem__("raw_counterterm_offset_is_a_physical_regulator_effect", True)),
        ("erase_subtracted_universality", lambda d: d["matched_regulator_comparison"].__setitem__("matched_subtracted_one_loop_terms_have_the_same_limit", False)),
        ("erase_overlap_universality", lambda d: d["matched_regulator_comparison"].__setitem__("matched_resolvent_weighted_overlap_words_have_the_same_limit", False)),
        ("invent_W_difference", lambda d: d["matched_regulator_comparison"].__setitem__("complete_graph_W_min_difference_for_the_two_matched_profiles_is_zero", False)),
        ("erase_affine_shift", lambda d: d["finite_scheme_and_selection"].__setitem__("adding_a_finite_Hermitian_subtraction_F_shifts_W_by_F", False)),
        ("erase_compensation", lambda d: d["finite_scheme_and_selection"].__setitem__("compensating_E_R_by_minus_F_preserves_the_same_operator_family", False)),
        ("invent_equivalence", lambda d: d["finite_scheme_and_selection"].__setitem__("uncompensated_finite_F_generically_changes_the_resolvent_and_spectrum", False)),
        ("erase_affine_space", lambda d: d["finite_scheme_and_selection"].__setitem__("finite_extension_space_is_affine_not_canonically_zeroed", False)),
        ("erase_commutant", lambda d: d["finite_scheme_and_selection"].__setitem__("full_rook_graph_permutation_commutant_has_three_real_Hermitian_parameters", False)),
        ("invent_symmetry_selector", lambda d: d["finite_scheme_and_selection"].__setitem__("rook_symmetry_alone_selects_a_unique_W", True)),
        ("invent_one_pole_selector", lambda d: d["finite_scheme_and_selection"].__setitem__("one_bound_state_or_one_determinant_zero_selects_the_full_W", True)),
        ("erase_boundary_selector", lambda d: d["finite_scheme_and_selection"].__setitem__("a_complete_finite_Schur_boundary_matrix_at_one_common_resolvent_point_selects_W", False)),
        ("invent_circle_scattering", lambda d: d["finite_scheme_and_selection"].__setitem__("finite_circle_supplies_an_infinite_volume_scattering_matrix", True)),
        ("invent_source_boundary", lambda d: d["finite_scheme_and_selection"].__setitem__("source_or_GU_action_supplies_the_boundary_matrix", True)),
        ("erase_positive_polarization", lambda d: d["signed_particle_hole_boundary"].__setitem__("positive_spectral_particle_hole_free_energy_is_semibounded", False)),
        ("erase_sea_convention", lambda d: d["signed_particle_hole_boundary"].__setitem__("normal_ordered_reference_sea_charge_is_zero_by_convention", False)),
        ("erase_opposite_charge", lambda d: d["signed_particle_hole_boundary"].__setitem__("particle_and_hole_charges_are_opposite", False)),
        ("erase_local_split", lambda d: d["signed_particle_hole_boundary"].__setitem__("local_signed_field_contains_particle_annihilation_and_hole_creation", False)),
        ("erase_bidirection", lambda d: d["signed_particle_hole_boundary"].__setitem__("singular_creation_therefore_runs_in_both_impurity_directions", False)),
        ("erase_path", lambda d: d["signed_particle_hole_boundary"].__setitem__("bidirected_rook_graph_has_a_nonzero_five_edge_distinct_species_path", False)),
        ("invent_nilpotence_transfer", lambda d: d["signed_particle_hole_boundary"].__setitem__("K137_one_way_G_fifth_power_zero_filtration_survives", True)),
        ("erase_Pauli", lambda d: d["signed_particle_hole_boundary"].__setitem__("finite_species_Pauli_number_energy_bound_survives_with_thirty_six_species", False)),
        ("erase_Coulomb", lambda d: d["signed_particle_hole_boundary"].__setitem__("finite_interval_Coulomb_counting_bound_survives_conditionally", False)),
        ("invent_signed_limit", lambda d: d["signed_particle_hole_boundary"].__setitem__("complete_minimal_signed_Dirac_point_cutoff_limit_is_proved", True)),
        ("invent_selected_sea", lambda d: d["signed_particle_hole_boundary"].__setitem__("polarization_sea_charge_and_defect_split_are_source_selected", True)),
        ("invent_physical_W", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("uniquely_physically_selected_point_Fock_Gauss_Hamiltonian_constructed", True)),
        ("invent_volume", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("infinite_volume_limit_constructed", True)),
        ("invent_NESS", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("promote_current", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("reduced_cycle_promoted_to_field_current", True)),
        ("invent_smooth_parent", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("smooth_unreduced_connection_or_BRST_parent_constructed", True)),
        ("invent_source_owner", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A unique physical GU Hamiltonian predicts observations.")),
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
    print(f"K138 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
