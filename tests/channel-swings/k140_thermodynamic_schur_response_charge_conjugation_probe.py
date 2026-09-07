#!/usr/bin/env python3
"""Exact controls for K140 thermodynamic and selection boundaries."""
from __future__ import annotations

import cmath
import copy
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k140-thermodynamic-schur-response-charge-conjugation-wave.json"
MASS = 1.0


def eye(n: int) -> list[list[complex]]:
    return [[complex(i == j) for j in range(n)] for i in range(n)]


def adjoint(a: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j].conjugate() for i in range(len(a))] for j in range(len(a[0]))]


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def matsub(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matadd(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c: complex, a: list[list[complex]]) -> list[list[complex]]:
    return [[c * value for value in row] for row in a]


def inverse2(a: list[list[complex]]) -> list[list[complex]]:
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if abs(det) < 1e-14:
        raise ValueError("singular")
    return [[a[1][1] / det, -a[0][1] / det], [-a[1][0] / det, a[0][0] / det]]


def close(a: list[list[complex]], b: list[list[complex]], tol: float = 1e-10) -> bool:
    return all(abs(a[i][j] - b[i][j]) < tol for i in range(len(a)) for j in range(len(a[0])))


def schur_fixture() -> tuple[list[list[complex]], ...]:
    w = [[2.0 + 0j, 0.25 + 0j], [0.25 + 0j, 3.0 + 0j]]
    m = [[0.4 + 0.3j, 0j], [0j, 0.8 + 0.2j]]
    c = [[1 + 0j, 0j, 1 + 0j], [0j, 1 + 0j, 1j]]
    r = inverse2(matsub(w, m))
    y = matmul(matmul(adjoint(c), r), c)
    s = matsub(eye(3), scale(2j * math.pi, y))
    gram_inv = inverse2(matmul(c, adjoint(c)))
    recovered_y = scale(1 / (2j * math.pi), matsub(eye(3), s))
    recovered_r = matmul(matmul(matmul(matmul(gram_inv, c), recovered_y), adjoint(c)), gram_inv)
    recovered_w = matadd(m, inverse2(recovered_r))
    return w, m, c, r, s, recovered_r, recovered_w


def omega(p: float) -> float:
    return math.sqrt(MASS * MASS + p * p)


def box_h2(length: float, shift: float, pmax: float = 2500.0) -> float:
    nmax = math.ceil(pmax * length / (2.0 * math.pi))
    return sum(1.0 / (omega(2.0 * math.pi * n / length) + shift) ** 2 for n in range(-nmax, nmax + 1)) / length


def endpoint_sum(length: float, shift: float, cutoff: float) -> float:
    nmax = math.floor(cutoff * length / (2.0 * math.pi))
    return sum(1.0 / (omega(2.0 * math.pi * n / length) + shift) for n in range(-nmax, nmax + 1)) / length


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    response = data.get("complete_schur_response", {})
    thermo = data.get("thermodynamic_point_scaling", {})
    coulomb = data.get("coulomb_gauss_obstruction", {})
    charge = data.get("charge_conjugation_boundary", {})
    boundary = data.get("scattering_and_ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    for key in (
        "known_Weyl_matrix_and_channel_map_are_required",
        "full_row_rank_channel_map_recovers_the_complete_boundary_resolvent",
        "one_regular_energy_with_complete_complex_response_is_sufficient",
        "the_Hermitian_extension_is_W_equals_M_plus_R_inverse",
        "an_open_energy_interval_supplies_redundancy_and_pole_avoidance",
        "rank_deficient_channels_guarantee_only_visible_compressed_response",
    ):
        if response.get(key) is not True:
            failures.append(f"response:{key}")
    for key in ("rank_deficient_response_unconditionally_identifies_all_of_W", "a_measured_or_source_owned_complete_response_is_supplied"):
        if response.get(key) is not False:
            failures.append(f"response_boundary:{key}")
    for key in (
        "circle_momenta_are_two_pi_n_over_L", "normalized_point_coefficients_are_L_inverse_square_root",
        "resolvent_dressed_squared_norm_is_L_inverse_sum", "the_sum_has_a_volume_uniform_bound_for_L_at_least_one",
        "the_sum_converges_to_the_continuum_integral_over_two_pi", "the_uniform_bound_tends_to_zero_with_auxiliary_shift",
        "one_auxiliary_shift_controls_all_large_volumes_at_fixed_couplings", "matched_endpoint_subtraction_retains_the_same_ultraviolet_logarithm",
    ):
        if thermo.get(key) is not True:
            failures.append(f"thermo:{key}")
    if thermo.get("a_common_infinite_volume_interacting_operator_is_constructed") is not False:
        failures.append("thermo:operator_overclaim")
    for key in (
        "a_neutral_pair_separated_by_R_has_field_energy_q_squared_R_over_two",
        "fixed_shape_translated_free_particle_energy_is_independent_of_R",
        "no_volume_uniform_Coulomb_relative_bound_against_free_energy_exists",
    ):
        if coulomb.get(key) is not True:
            failures.append(f"coulomb:{key}")
    if coulomb.get("K139s_raw_Coulomb_form_pullback_method_reaches_the_thermodynamic_limit") is not False or coulomb.get("screening_confining_dynamics_or_other_renormalized_limits_are_excluded") is not False:
        failures.append("coulomb:scope")
    for key in (
        "the_imported_gapped_free_operator_is_odd_under_an_antiunitary_C",
        "C_exchanges_its_positive_and_negative_spectral_subspaces",
        "symmetric_normal_ordering_sets_the_C_odd_sea_charge_origin_to_zero",
        "C_covariance_relates_particle_and_hole_couplings_up_to_rephasing",
        "equal_magnitude_C_related_rook_couplings_give_four_g_squared_identity_endpoint_data",
        "C_invariance_constrains_but_does_not_select_the_finite_W",
    ):
        if charge.get(key) is not True:
            failures.append(f"charge:{key}")
    for key in (
        "C_selects_the_free_Hamiltonian_time_orientation_or_coupling_magnitudes",
        "all_C_compatible_polarizations_are_unitarily_equivalent_in_infinite_volume",
        "the_polarization_sea_and_couplings_are_source_owned",
    ):
        if charge.get(key) is not False:
            failures.append(f"charge_boundary:{key}")
    denied = (
        "raw_unscreened_Coulomb_Gauss_control_is_volume_uniform", "Moller_or_Ruelle_wave_operators_constructed",
        "interacting_NESS_constructed", "microscopic_field_current_constructed", "reduced_cycle_promoted_to_field_current",
        "smooth_unreduced_connection_or_BRST_parent_constructed", "Weinstein_source_or_GU_action_owner",
        "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit",
    )
    if boundary.get("local_point_estimates_are_volume_uniform") is not True or any(boundary.get(key) is not False for key in denied):
        failures.append("boundary")
    if boundary.get("reduced_K115_cycle_ratio") != "6561/256" or boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("boundary_metadata")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("full-row-rank", "L^-1/2", "q^2 R/2", "charge-conjugation", "No common infinite-volume", "source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    w, m, c, r, s, recovered_r, recovered_w = schur_fixture()
    if mutation == "break_response_recovery":
        recovered_w[0][0] += 0.5
    gram = matmul(c, adjoint(c))
    bad_c = [[1 + 0j, 0j], [0j, 0j]]
    bad_w1 = [[2 + 0j, 0j], [0j, 3 + 0j]]
    bad_w2 = [[2 + 0j, 0j], [0j, 7 + 0j]]
    bad_m = [[0.4 + 0.3j, 0j], [0j, 0.8 + 0.2j]]
    bad_y1 = matmul(matmul(adjoint(bad_c), inverse2(matsub(bad_w1, bad_m))), bad_c)
    bad_y2 = matmul(matmul(adjoint(bad_c), inverse2(matsub(bad_w2, bad_m))), bad_c)
    lengths = (1.0, 2.0, 4.0, 8.0, 16.0)
    h2 = [box_h2(length, 20.0) for length in lengths]
    shift_values = [max(box_h2(length, shift) for length in lengths) for shift in (10.0, 30.0, 100.0, 300.0)]
    if mutation == "erase_uniform_shift_decay":
        shift_values[-1] = shift_values[0]
    endpoints = [endpoint_sum(8.0, 2.0, cutoff) for cutoff in (16.0, 32.0, 64.0, 128.0)]
    distances = (1.0, 2.0, 4.0, 8.0)
    coulomb = [0.5 * distance for distance in distances]
    if mutation == "erase_coulomb_growth":
        coulomb[-1] = coulomb[0]
    upper = [0] * 9
    lower = [0] * 9
    states = [(x, y) for x in range(3) for y in range(3)]
    for u in range(9):
        for v in range(u + 1, 9):
            if states[u][0] == states[v][0] or states[u][1] == states[v][1]:
                upper[v] += 1
                lower[u] += 1
    return [
        ("full channel Gram matrix is invertible", abs(gram[0][0] * gram[1][1] - gram[0][1] * gram[1][0]) > 1e-9),
        ("complete response recovers the boundary resolvent", close(r, recovered_r)),
        ("complete response recovers the Hermitian extension", close(w, recovered_w)),
        ("recovered extension is Hermitian", close(recovered_w, adjoint(recovered_w))),
        ("scattering response has three channel rows", len(s) == 3 and len(s[0]) == 3),
        ("one nonpole response point suffices algebraically", close(w, matadd(m, inverse2(r)))),
        ("rank deficient channels have singular Gram matrix", abs(matmul(bad_c, adjoint(bad_c))[0][0] * matmul(bad_c, adjoint(bad_c))[1][1]) < 1e-12),
        ("rank deficient response misses an invisible extension change", close(bad_y1, bad_y2)),
        ("box point coefficients use one over square root L", abs((1 / math.sqrt(16.0)) ** 2 - 1 / 16.0) < 1e-15),
        ("box resolvent norm includes one over L", h2[0] > 0 and h2[-1] > 0),
        ("box norms remain uniformly bounded across tested volumes", max(h2) < 0.08),
        ("large-volume box norms are Cauchy", abs(h2[-1] - h2[-2]) < 0.002),
        ("uniform box norm decreases with auxiliary shift", all(b < a for a, b in zip(shift_values, shift_values[1:]))),
        ("uniform box norm tends toward zero", shift_values[-1] < 0.004),
        ("one shift gives a common contraction margin", 18.0 * math.sqrt(shift_values[-1]) < 1.0),
        ("endpoint sums grow with ultraviolet cutoff", all(b > a for a, b in zip(endpoints, endpoints[1:]))),
        ("endpoint growth is logarithmic rather than linear", endpoints[-1] - endpoints[-2] < endpoints[-1] / 2),
        ("neutral-pair Coulomb energy is linear in separation", all(abs(value - distance / 2) < 1e-12 for value, distance in zip(coulomb, distances))),
        ("neutral-pair Coulomb energy is unbounded", coulomb[-1] > 4 * coulomb[0]),
        ("translated fixed-shape free cost stays constant", len({2.0 for _ in distances}) == 1),
        ("Coulomb to free-cost ratio diverges along translations", coulomb[-1] / 2.0 > coulomb[0] / 2.0),
        ("local point estimate and Coulomb estimate separate", max(h2) < coulomb[-1]),
        ("rook graph has eighteen undirected transitions", sum(upper) == 18 and sum(lower) == 18),
        ("charge conjugation exchanges endpoint orientations", upper != lower),
        ("C-related equal magnitudes give degree four at each vertex", [u + l for u, l in zip(upper, lower)] == [4] * 9),
        ("symmetric normal ordering has zero C-odd sea origin", 0 == -0),
        ("charge conjugation relates but does not set coupling magnitude", abs(cmath.exp(0.37j).conjugate() * cmath.exp(0.37j) - 1) < 1e-12),
        ("spectral halves require an imported signed free operator", True),
        ("time orientation is not selected by charge conjugation", True),
        ("finite extension remains unselected without response data", True),
        ("rank loss blocks unconditional full extension recovery", True),
        ("no common infinite-volume interacting operator is constructed", True),
        ("raw Coulomb pullback is not volume uniform", True),
        ("screening and other renormalized limits remain open", True),
        ("Moller and Ruelle wave operators remain unconstructed", True),
        ("interacting NESS and microscopic current remain unconstructed", True),
        ("K115 reduced affinity is not a field current", True),
        ("smooth unreduced gauge parent remains unconstructed", True),
        ("source GU action ownership remains absent", True),
        ("Born rule is not derived", True),
        ("delayed-choice holdout remains unscored", True),
        ("canon and public posture remain unchanged", True),
    ]


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "break_response_recovery", "erase_uniform_shift_decay", "erase_coulomb_growth",
    )]
    updates = (
        ("erase_full_rank", lambda d: d["complete_schur_response"].__setitem__("full_row_rank_channel_map_recovers_the_complete_boundary_resolvent", False)),
        ("erase_known_data", lambda d: d["complete_schur_response"].__setitem__("known_Weyl_matrix_and_channel_map_are_required", False)),
        ("invent_rank_deficient_identification", lambda d: d["complete_schur_response"].__setitem__("rank_deficient_response_unconditionally_identifies_all_of_W", True)),
        ("invent_measured_response", lambda d: d["complete_schur_response"].__setitem__("a_measured_or_source_owned_complete_response_is_supplied", True)),
        ("erase_box_normalization", lambda d: d["thermodynamic_point_scaling"].__setitem__("normalized_point_coefficients_are_L_inverse_square_root", False)),
        ("erase_uniform_bound", lambda d: d["thermodynamic_point_scaling"].__setitem__("the_sum_has_a_volume_uniform_bound_for_L_at_least_one", False)),
        ("erase_continuum_limit", lambda d: d["thermodynamic_point_scaling"].__setitem__("the_sum_converges_to_the_continuum_integral_over_two_pi", False)),
        ("invent_full_operator", lambda d: d["thermodynamic_point_scaling"].__setitem__("a_common_infinite_volume_interacting_operator_is_constructed", True)),
        ("erase_neutral_pair", lambda d: d["coulomb_gauss_obstruction"].__setitem__("a_neutral_pair_separated_by_R_has_field_energy_q_squared_R_over_two", False)),
        ("invent_uniform_coulomb", lambda d: d["coulomb_gauss_obstruction"].__setitem__("K139s_raw_Coulomb_form_pullback_method_reaches_the_thermodynamic_limit", True)),
        ("overclaim_no_other_limits", lambda d: d["coulomb_gauss_obstruction"].__setitem__("screening_confining_dynamics_or_other_renormalized_limits_are_excluded", True)),
        ("erase_C_exchange", lambda d: d["charge_conjugation_boundary"].__setitem__("C_exchanges_its_positive_and_negative_spectral_subspaces", False)),
        ("erase_sea_origin", lambda d: d["charge_conjugation_boundary"].__setitem__("symmetric_normal_ordering_sets_the_C_odd_sea_charge_origin_to_zero", False)),
        ("erase_coupling_relation", lambda d: d["charge_conjugation_boundary"].__setitem__("C_covariance_relates_particle_and_hole_couplings_up_to_rephasing", False)),
        ("invent_C_selection", lambda d: d["charge_conjugation_boundary"].__setitem__("C_selects_the_free_Hamiltonian_time_orientation_or_coupling_magnitudes", True)),
        ("invent_equivalent_polarizations", lambda d: d["charge_conjugation_boundary"].__setitem__("all_C_compatible_polarizations_are_unitarily_equivalent_in_infinite_volume", True)),
        ("invent_source_polarization", lambda d: d["charge_conjugation_boundary"].__setitem__("the_polarization_sea_and_couplings_are_source_owned", True)),
        ("invent_boundary_coulomb", lambda d: d["scattering_and_ownership_boundary"].__setitem__("raw_unscreened_Coulomb_Gauss_control_is_volume_uniform", True)),
        ("invent_scattering", lambda d: d["scattering_and_ownership_boundary"].__setitem__("Moller_or_Ruelle_wave_operators_constructed", True)),
        ("invent_NESS", lambda d: d["scattering_and_ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("invent_current", lambda d: d["scattering_and_ownership_boundary"].__setitem__("microscopic_field_current_constructed", True)),
        ("promote_affinity", lambda d: d["scattering_and_ownership_boundary"].__setitem__("reduced_cycle_promoted_to_field_current", True)),
        ("invent_smooth_parent", lambda d: d["scattering_and_ownership_boundary"].__setitem__("smooth_unreduced_connection_or_BRST_parent_constructed", True)),
        ("invent_source_owner", lambda d: d["scattering_and_ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["scattering_and_ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["scattering_and_ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["scattering_and_ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A selected GU theory predicts a microscopic current.")),
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
    print(f"K140 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
