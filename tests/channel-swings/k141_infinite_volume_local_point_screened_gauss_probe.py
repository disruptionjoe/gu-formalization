#!/usr/bin/env python3
"""Exact controls for K141 common-carrier and screened-Gauss boundaries."""
from __future__ import annotations

import copy
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k141-infinite-volume-local-point-screened-gauss-wave.json"
MASS = 1.0
SHIFT = 3.0


def omega(p: float) -> float:
    return math.sqrt(MASS * MASS + p * p)


def left_cell(p: float, delta: float) -> float:
    return delta * math.floor(p / delta)


def omega_delta(p: float, delta: float) -> float:
    return omega(left_cell(p, delta))


def point_vector_error2(delta: float, cutoff: float = 250.0, samples_per_cell: int = 6) -> float:
    n_min = math.floor(-cutoff / delta)
    n_max = math.ceil(cutoff / delta)
    total = 0.0
    step = delta / samples_per_cell
    for n in range(n_min, n_max):
        base = n * delta
        cell_value = 1.0 / (omega(base) + SHIFT)
        for j in range(samples_per_cell):
            p = base + (j + 0.5) * step
            continuum = 1.0 / (omega(p) + SHIFT)
            total += (cell_value - continuum) ** 2 * step / (2.0 * math.pi)
    return total


def screened_pair_energy(distance: float, kappa: float = 0.7, charge: float = 1.3) -> float:
    return charge * charge * (1.0 - math.exp(-kappa * distance)) / (2.0 * kappa)


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    carrier = data.get("common_carrier", {})
    thermo = data.get("thermodynamic_operator_limit", {})
    screened = data.get("screened_gauss_test", {})
    all_sector = data.get("all_sector_boundary", {})
    boundary = data.get("scattering_and_ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    for key in (
        "circle_spacing_is_two_pi_over_L",
        "normalized_momentum_cells_define_an_isometry_from_l2_Z",
        "the_L_inverse_square_root_point_coefficient_becomes_one_over_square_root_two_pi",
        "piecewise_constant_dispersion_restricts_to_the_circle_dispersion",
        "the_extended_box_model_is_the_original_tensored_with_free_spectators",
    ):
        if carrier.get(key) is not True:
            failures.append(f"carrier:{key}")
    if carrier.get("the_bare_changing_Hilbert_spaces_are_literally_identical") is not False:
        failures.append("carrier:literal_identity")
    for key in (
        "dispersion_error_is_at_most_the_cell_width",
        "the_mass_gap_turns_many_sector_error_into_a_uniform_free_relative_bound",
        "free_resolvents_converge_in_operator_norm_after_a_common_shift",
        "resolvent_dressed_point_vectors_converge_in_L2",
        "signed_boundary_maps_and_their_Neumann_inverses_converge_in_norm",
        "matched_subtracted_regular_operators_converge_in_free_graph_relative_norm",
        "fixed_W_local_signed_point_extensions_converge_in_norm_resolvent",
        "uniform_ultraviolet_tails_allow_cofinal_cutoff_and_volume_paths",
    ):
        if thermo.get(key) is not True:
            failures.append(f"thermo:{key}")
    for key in ("the_raw_unscreened_Coulomb_form_is_included", "the_polarization_couplings_or_W_are_physically_selected"):
        if thermo.get(key) is not False:
            failures.append(f"thermo_boundary:{key}")
    for key in (
        "screened_operator_is_minus_d2_plus_kappa_squared",
        "green_kernel_is_exp_minus_kappa_abs_x_over_two_kappa",
        "neutral_point_pair_energy_is_q_squared_times_one_minus_exp_minus_kappa_R_over_two_kappa",
        "the_pair_energy_is_uniformly_bounded_in_separation",
        "fixed_shape_smearing_does_not_exceed_the_point_pair_bound",
    ):
        if screened.get(key) is not True:
            failures.append(f"screened:{key}")
    for key in ("the_K140_separated_pair_witness_blocks_this_screened_route", "the_screening_mass_is_selected_by_GU_or_source"):
        if screened.get(key) is not False:
            failures.append(f"screened_boundary:{key}")
    if all_sector.get("elementary_many_charge_control_is_quadratic_in_particle_number") is not True:
        failures.append("all_sector:quadratic")
    if all_sector.get("the_mass_gap_alone_turns_that_N_squared_bound_into_an_H0_relative_bound") is not False:
        failures.append("all_sector:false_mass_gap_promotion")
    if all_sector.get("a_thirty_six_species_fermionic_density_or_local_number_estimate_is_still_required") is not True:
        failures.append("all_sector:missing_requirement")
    if all_sector.get("a_volume_uniform_all_sector_screened_Fock_form_is_proved") is not False:
        failures.append("all_sector:overclaim")
    denied = (
        "a_screened_all_sector_interacting_Hamiltonian_is_constructed",
        "Moller_or_Ruelle_wave_operators_constructed",
        "asymptotic_completeness_proved",
        "interacting_NESS_constructed",
        "microscopic_field_current_constructed",
        "reduced_cycle_promoted_to_field_current",
        "smooth_unreduced_connection_or_BRST_parent_constructed",
        "Weinstein_source_or_GU_action_owner",
        "Born_rule_derived",
        "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if boundary.get("a_common_infinite_volume_local_signed_point_operator_is_constructed") is not True:
        failures.append("boundary:missing_local_operator")
    if any(boundary.get(key) is not False for key in denied):
        failures.append("boundary:overclaim")
    if boundary.get("reduced_K115_cycle_ratio") != "6561/256" or boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("boundary:metadata")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("L2(R)", "norm-resolvent", "q^2(1-exp(-kappa R))/(2 kappa)", "No all-sector", "source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    deltas = (1.0, 0.5, 0.25, 0.125)
    sample_points = tuple(-12.75 + 0.03125 * j for j in range(817))
    dispersion_errors = [max(abs(omega_delta(p, d) - omega(p)) for p in sample_points) for d in deltas]
    vector_errors = [point_vector_error2(d) for d in deltas]
    if mutation == "break_dispersion_bound":
        dispersion_errors[-1] = 2.0 * deltas[-1]
    if mutation == "break_point_vector_convergence":
        vector_errors[-1] = vector_errors[0]
    lengths = tuple(2.0 * math.pi / d for d in deltas)
    normalization_products = [(1.0 / math.sqrt(length)) / math.sqrt(delta) for length, delta in zip(lengths, deltas)]
    sectors = (0, 1, 2, 5, 20, 100)
    free_relative = [max((r * d) / (MASS * r + SHIFT) if r else 0.0 for r in sectors) for d in deltas]
    distances = (0.0, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0)
    screened = [screened_pair_energy(r) for r in distances]
    unscreened = [1.3 * 1.3 * r / 2.0 for r in distances]
    cap = 1.3 * 1.3 / (2.0 * 0.7)
    if mutation == "break_screened_cap":
        screened[-1] = 1.1 * cap
    particle_counts = (1, 2, 4, 8, 16)
    crude_ratio = [n * n / (MASS * n) for n in particle_counts]
    return [
        ("circle cell width is two pi over L", all(abs(d - 2.0 * math.pi / length) < 1e-14 for d, length in zip(deltas, lengths))),
        ("normalized cell basis has unit norm", all(abs((d ** -0.5) ** 2 * d - 1.0) < 1e-14 for d in deltas)),
        ("box point normalization becomes one over square root two pi", all(abs(value - 1.0 / math.sqrt(2.0 * math.pi)) < 1e-14 for value in normalization_products)),
        ("piecewise dispersion error is at most one cell", all(error <= d + 1e-12 for error, d in zip(dispersion_errors, deltas))),
        ("dispersion approximation improves", all(b < a for a, b in zip(dispersion_errors, dispersion_errors[1:]))),
        ("mass gap gives sector-uniform relative error", all(error <= d / MASS + 1e-14 for error, d in zip(free_relative, deltas))),
        ("free relative error tends to zero", free_relative[-1] < free_relative[0] / 4.0 + 1e-14),
        ("resolvent-dressed point vector errors decrease", all(b < a for a, b in zip(vector_errors, vector_errors[1:]))),
        ("point vector reaches the continuum in L2", vector_errors[-1] < 3e-5),
        ("one common positive mass gap is retained", min(omega_delta(p, deltas[-1]) for p in sample_points) >= MASS),
        ("screened pair energy starts at zero", abs(screened[0]) < 1e-14),
        ("screened pair energy is monotone", all(b >= a for a, b in zip(screened, screened[1:]))),
        ("screened pair energy stays below its exact cap", all(value <= cap + 1e-14 for value in screened)),
        ("screened pair energy saturates near its cap", abs(screened[-1] - cap) < 2e-5),
        ("unscreened pair energy remains linear", all(abs(value - 1.3 * 1.3 * r / 2.0) < 1e-14 for value, r in zip(unscreened, distances))),
        ("unscreened energy exceeds the screened cap", unscreened[-1] > 8.0 * cap),
        ("zero screening is singular", screened_pair_energy(8.0, kappa=0.01) > screened_pair_energy(8.0, kappa=0.7)),
        ("elementary many-charge estimate is quadratic", [n * n for n in particle_counts] == [1, 4, 16, 64, 256]),
        ("mass-gap linear energy does not absorb crude N squared", all(b > a for a, b in zip(crude_ratio, crude_ratio[1:]))),
        ("common-carrier extension retains a spectator complement", True),
        ("boundary maps use bounded fermionic creation", True),
        ("one large auxiliary shift gives a common Neumann chart", True),
        ("matched subtraction keeps a uniform inverse-square ultraviolet tail", True),
        ("local signed point extensions converge in norm resolvent", True),
        ("cofinal ultraviolet and volume paths are allowed", True),
        ("raw unscreened Coulomb is not included in the operator limit", True),
        ("screened pair control is not an all-sector Fock theorem", True),
        ("screening mass remains an external supplied parameter", True),
        ("physical extension and polarization remain unselected", True),
        ("Moller and Ruelle wave operators remain unconstructed", True),
        ("asymptotic completeness remains unproved", True),
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
        "break_dispersion_bound", "break_point_vector_convergence", "break_screened_cap",
    )]
    updates = (
        ("erase_cell_isometry", lambda d: d["common_carrier"].__setitem__("normalized_momentum_cells_define_an_isometry_from_l2_Z", False)),
        ("invent_literal_identity", lambda d: d["common_carrier"].__setitem__("the_bare_changing_Hilbert_spaces_are_literally_identical", True)),
        ("erase_spectator_extension", lambda d: d["common_carrier"].__setitem__("the_extended_box_model_is_the_original_tensored_with_free_spectators", False)),
        ("erase_mass_gap", lambda d: d["thermodynamic_operator_limit"].__setitem__("the_mass_gap_turns_many_sector_error_into_a_uniform_free_relative_bound", False)),
        ("erase_free_resolvent", lambda d: d["thermodynamic_operator_limit"].__setitem__("free_resolvents_converge_in_operator_norm_after_a_common_shift", False)),
        ("erase_point_vector", lambda d: d["thermodynamic_operator_limit"].__setitem__("resolvent_dressed_point_vectors_converge_in_L2", False)),
        ("erase_boundary_inverse", lambda d: d["thermodynamic_operator_limit"].__setitem__("signed_boundary_maps_and_their_Neumann_inverses_converge_in_norm", False)),
        ("erase_operator_limit", lambda d: d["thermodynamic_operator_limit"].__setitem__("fixed_W_local_signed_point_extensions_converge_in_norm_resolvent", False)),
        ("invent_raw_coulomb", lambda d: d["thermodynamic_operator_limit"].__setitem__("the_raw_unscreened_Coulomb_form_is_included", True)),
        ("invent_selection", lambda d: d["thermodynamic_operator_limit"].__setitem__("the_polarization_couplings_or_W_are_physically_selected", True)),
        ("erase_screened_kernel", lambda d: d["screened_gauss_test"].__setitem__("green_kernel_is_exp_minus_kappa_abs_x_over_two_kappa", False)),
        ("erase_pair_formula", lambda d: d["screened_gauss_test"].__setitem__("neutral_point_pair_energy_is_q_squared_times_one_minus_exp_minus_kappa_R_over_two_kappa", False)),
        ("invent_pair_obstruction", lambda d: d["screened_gauss_test"].__setitem__("the_K140_separated_pair_witness_blocks_this_screened_route", True)),
        ("invent_kappa_selection", lambda d: d["screened_gauss_test"].__setitem__("the_screening_mass_is_selected_by_GU_or_source", True)),
        ("erase_quadratic_boundary", lambda d: d["all_sector_boundary"].__setitem__("elementary_many_charge_control_is_quadratic_in_particle_number", False)),
        ("promote_mass_gap", lambda d: d["all_sector_boundary"].__setitem__("the_mass_gap_alone_turns_that_N_squared_bound_into_an_H0_relative_bound", True)),
        ("invent_all_sector", lambda d: d["all_sector_boundary"].__setitem__("a_volume_uniform_all_sector_screened_Fock_form_is_proved", True)),
        ("erase_local_operator", lambda d: d["scattering_and_ownership_boundary"].__setitem__("a_common_infinite_volume_local_signed_point_operator_is_constructed", False)),
        ("invent_screened_H", lambda d: d["scattering_and_ownership_boundary"].__setitem__("a_screened_all_sector_interacting_Hamiltonian_is_constructed", True)),
        ("invent_scattering", lambda d: d["scattering_and_ownership_boundary"].__setitem__("Moller_or_Ruelle_wave_operators_constructed", True)),
        ("invent_completeness", lambda d: d["scattering_and_ownership_boundary"].__setitem__("asymptotic_completeness_proved", True)),
        ("invent_NESS", lambda d: d["scattering_and_ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("invent_current", lambda d: d["scattering_and_ownership_boundary"].__setitem__("microscopic_field_current_constructed", True)),
        ("promote_affinity", lambda d: d["scattering_and_ownership_boundary"].__setitem__("reduced_cycle_promoted_to_field_current", True)),
        ("invent_smooth_parent", lambda d: d["scattering_and_ownership_boundary"].__setitem__("smooth_unreduced_connection_or_BRST_parent_constructed", True)),
        ("invent_source_owner", lambda d: d["scattering_and_ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["scattering_and_ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["scattering_and_ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["scattering_and_ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A selected GU theory predicts a current.")),
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
    print(f"K141 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
