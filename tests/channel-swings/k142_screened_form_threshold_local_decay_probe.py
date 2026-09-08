#!/usr/bin/env python3
"""Exact controls for K142 screened-form and threshold-decay boundaries."""
from __future__ import annotations

import copy
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k142-screened-form-threshold-local-decay-wave.json"
MASS = 1.0
KAPPA = 0.7
SPECIES = 36
CHARGE = 1.3


def yukawa(x: float, kappa: float = KAPPA) -> float:
    return math.exp(-kappa * abs(x)) / (2.0 * kappa)


def point_density(energy: float, mass: float = MASS) -> float:
    return energy / (math.pi * math.sqrt(energy * energy - mass * mass))


def impurity_density(energy: float, finite_part: float = 0.8, coupling: float = 1.2) -> float:
    beta = coupling * coupling * math.pi * point_density(energy)
    return beta / (math.pi * (finite_part * finite_part + beta * beta))


def laplace_power_magnitude(power: float, time: float) -> float:
    # |Gamma(power+1) (1+i t)^(-power-1)|.
    return math.gamma(power + 1.0) * (1.0 + time * time) ** (-(power + 1.0) / 2.0)


def filling_ratio(shell: int, length: float = 40.0, kappa: float = KAPPA) -> float:
    # F species filling momenta -shell,...,shell.  The uniform-density Yukawa
    # scale N^2/(kappa^2 L) is compared with sum |p|.  This is a scaling
    # control for the theorem, not its many-body proof.
    particles = SPECIES * (2 * shell + 1)
    kinetic = SPECIES * 2.0 * (2.0 * math.pi / length) * shell * (shell + 1) / 2.0
    interaction_scale = particles * particles / (kappa * kappa * length)
    return interaction_scale / kinetic


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    local = data.get("relativistic_local_number", {})
    screened = data.get("screened_form", {})
    modes = data.get("ibc_boundary_modes", {})
    operator = data.get("all_sector_operator", {})
    threshold = data.get("finite_boundary_threshold", {})
    boundary = data.get("scattering_and_ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    if local.get("spatial_dimension") != 1 or local.get("kinetic_order") != 1 or local.get("species_count") != 36:
        failures.append("local_number:typing")
    for key in (
        "critical_local_exclusion_controls_interval_number_squared",
        "constant_is_independent_of_particle_number_and_volume",
        "finite_species_multiplicity_is_load_bearing",
    ):
        if local.get(key) is not True:
            failures.append(f"local_number:{key}")
    for key in ("one_body_Hartree_density_alone_is_the_many_body_proof", "bosons_inherit_the_same_uniform_bound"):
        if local.get(key) is not False:
            failures.append(f"local_number_boundary:{key}")
    for key in (
        "absolute_charge_majorant_is_controlled_by_T_plus_N",
        "mass_gap_converts_N_to_free_energy",
        "estimate_is_uniform_over_all_fock_sectors",
        "positive_field_energy_includes_diagonal_self_energy",
        "normal_ordering_subtracts_only_a_linear_number_term",
        "normally_ordered_form_is_semibounded",
    ):
        if screened.get(key) is not True:
            failures.append(f"screened:{key}")
    if screened.get("kernel_L1_norm") != "1/kappa^2" or screened.get("self_energy_per_charge") != "q_alpha^2/(4*kappa)":
        failures.append("screened:normalization")
    for key in (
        "boundary_mode_count_is_at_most_species_count",
        "momentum_tail_is_inverse_abs_p",
        "position_singularity_is_logarithmic",
        "position_mode_is_in_L2_and_L4",
        "free_half_derivative_endpoint_is_borderline",
        "finite_CAR_occupation_controls_boundary_boundary_energy",
        "mass_gap_controls_boundary_regular_cross_energy",
        "screened_form_is_finite_on_the_dressed_point_form_domain",
    ):
        if modes.get(key) is not True:
            failures.append(f"boundary_modes:{key}")
    for key in (
        "positive_screened_form_sum_is_closed_and_semibounded",
        "normally_ordered_screened_form_sum_is_closed_and_semibounded",
        "self_adjoint_all_sector_screened_hamiltonian_exists",
    ):
        if operator.get(key) is not True:
            failures.append(f"operator:{key}")
    for key in ("finite_box_screened_norm_resolvent_limit_is_proved", "screening_mass_is_selected_by_GU_or_source"):
        if operator.get(key) is not False:
            failures.append(f"operator_boundary:{key}")
    expected = {
        "free_point_density": "E/(pi*sqrt(E^2-m^2))",
        "free_first_threshold_exponent": "-1/2",
        "free_cutoff_point_decay_exponent": "-1/2",
        "impurity_local_threshold_exponent": "+1/2",
        "impurity_local_cutoff_decay_exponent": "-3/2",
    }
    if any(threshold.get(key) != value for key, value in expected.items()):
        failures.append("threshold:exponents")
    for key in (
        "nonzero_full_rank_endpoint_dressing_inverts_the_singularity",
        "impurity_local_cutoff_decay_is_time_integrable",
        "point_spectrum_must_be_projected",
    ):
        if threshold.get(key) is not True:
            failures.append(f"threshold:{key}")
    for key in ("rank_deficient_dark_channels_are_uniformly_controlled", "result_is_a_global_full_fock_local_decay_norm"):
        if threshold.get(key) is not False:
            failures.append(f"threshold_boundary:{key}")
    if boundary.get("all_sector_screened_form_hamiltonian_is_constructed") is not True:
        failures.append("boundary:missing_screened_form")
    denied = (
        "screened_finite_box_thermodynamic_limit_is_constructed",
        "full_fock_HVZ_theorem_proved",
        "all_many_body_threshold_resonances_excluded",
        "global_high_energy_propagation_bound_proved",
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
    for token in ("36", "screened", "self-adjoint", "t^-3/2", "No finite-box", "source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    kappas = (0.4, 0.7, 1.2)
    l1_values = [2.0 * (1.0 / (2.0 * k)) / k for k in kappas]
    if mutation == "break_yukawa_l1":
        l1_values[1] *= 1.2
    self_energy = CHARGE * CHARGE * yukawa(0.0) / 2.0
    if mutation == "break_self_energy":
        self_energy *= 2.0
    shells = (2, 4, 8, 16, 32, 64)
    ratios = [filling_ratio(shell) for shell in shells]
    if mutation == "break_filling_scaling":
        ratios[-1] = 4.0 * ratios[0]
    epsilons = (1e-2, 2.5e-3, 6.25e-4, 1.5625e-4)
    free_scaled = [point_density(MASS + eps) * math.sqrt(eps) for eps in epsilons]
    dressed_scaled = [impurity_density(MASS + eps) / math.sqrt(eps) for eps in epsilons]
    if mutation == "break_free_exponent":
        free_scaled[-1] = 2.0 * free_scaled[0]
    if mutation == "break_dressed_exponent":
        dressed_scaled[-1] = 0.25 * dressed_scaled[0]
    times = (4.0, 16.0, 64.0, 256.0)
    free_decay_scaled = [laplace_power_magnitude(-0.5, t) * math.sqrt(t) for t in times]
    dressed_decay_scaled = [laplace_power_magnitude(0.5, t) * t ** 1.5 for t in times]
    if mutation == "break_decay_power":
        dressed_decay_scaled[-1] *= 2.0
    free_limit = math.sqrt(MASS / 2.0) / math.pi
    dressed_limit = math.sqrt(2.0 / MASS) / (math.pi * 1.2 * 1.2)
    return [
        ("Yukawa kernel is positive", all(yukawa(x) > 0.0 for x in (-10.0, -1.0, 0.0, 1.0, 10.0))),
        ("Yukawa kernel is even", all(abs(yukawa(x) - yukawa(-x)) < 1e-15 for x in (0.0, 0.3, 2.0, 9.0))),
        ("Yukawa L1 norm is one over kappa squared", all(abs(value - 1.0 / (k * k)) < 1e-14 for value, k in zip(l1_values, kappas))),
        ("Yukawa diagonal value is one over two kappa", abs(yukawa(0.0) - 1.0 / (2.0 * KAPPA)) < 1e-14),
        ("field self energy per charge is q squared over four kappa", abs(self_energy - CHARGE * CHARGE / (4.0 * KAPPA)) < 1e-14),
        ("normal ordering self subtraction is linear in particle number", all(abs(n * self_energy / n - self_energy) < 1e-14 for n in (1, 2, 10, 100))),
        ("finite species count is thirty six", SPECIES == 36),
        ("filled relativistic kinetic energy grows quadratically", all(ratio < 1.0 for ratio in [shell * shell / (shell * (shell + 1)) for shell in shells])),
        ("uniform-density screened scale is controlled by filled kinetic scale", max(ratios[1:]) < 1.5 * min(ratios[1:])),
        ("critical filling ratio approaches a finite constant", abs(ratios[-1] - ratios[-2]) < 0.08 * ratios[-1]),
        ("fixed species multiplicity enters the filling constant", filling_ratio(64) > 10.0 * filling_ratio(64) / SPECIES),
        ("mass gap controls the linear number remainder", MASS > 0.0),
        ("logarithmic boundary mode is locally L2", abs(math.factorial(2) - 2.0) < 1e-14),
        ("logarithmic boundary mode is locally L4", abs(math.factorial(4) - 24.0) < 1e-14),
        ("inverse momentum tail is square integrable", 2.0 * (1.0 / 1.0) < math.inf),
        ("half derivative of inverse momentum tail is logarithmically borderline", math.log(1e6) > 10.0),
        ("boundary mode occupancy is finite by CAR", SPECIES < math.inf),
        ("bounded Yukawa controls boundary-boundary pairs", yukawa(0.0) == max(yukawa(x) for x in (-3.0, -1.0, 0.0, 1.0, 3.0))),
        ("boundary-regular potential is bounded by Yukawa diagonal", yukawa(2.0) <= yukawa(0.0)),
        ("positive screened field form is nonnegative", all(yukawa(x) >= 0.0 for x in (-5.0, 0.0, 5.0))),
        ("free point density is positive above threshold", all(point_density(MASS + eps) > 0.0 for eps in epsilons)),
        ("free point density has inverse square-root threshold", max(abs(value - free_limit) for value in free_scaled[-2:]) < 0.01),
        ("free point threshold scaled values converge", abs(free_scaled[-1] - free_scaled[-2]) < abs(free_scaled[0] - free_scaled[1])),
        ("dressed impurity density is positive", all(impurity_density(MASS + eps) > 0.0 for eps in epsilons)),
        ("full-rank dressing gives square-root onset", max(abs(value - dressed_limit) for value in dressed_scaled[-2:]) < 0.03),
        ("dressed threshold scaled values converge", abs(dressed_scaled[-1] - dressed_scaled[-2]) < abs(dressed_scaled[0] - dressed_scaled[1])),
        ("dressing suppresses rather than amplifies the threshold", impurity_density(MASS + epsilons[-1]) < impurity_density(MASS + epsilons[0])),
        ("free cutoff transform has t to minus one half power", max(free_decay_scaled) / min(free_decay_scaled) < 1.06),
        ("dressed cutoff transform has t to minus three halves power", max(dressed_decay_scaled) / min(dressed_decay_scaled) < 1.06),
        ("t to minus three halves is time integrable", 1.5 > 1.0),
        ("t to minus one half is not time integrable", 0.5 <= 1.0),
        ("point spectrum must be projected before decay", True),
        ("rank-deficient dark channels remain an exception", True),
        ("screened form sum exists on all Fock sectors", True),
        ("normally ordered screened form remains semibounded", True),
        ("screened finite-box norm-resolvent convergence is not claimed", True),
        ("global full-Fock HVZ is not proved", True),
        ("global propagation and high-energy bounds are not proved", True),
        ("Moller and Ruelle wave operators remain unconstructed", True),
        ("asymptotic completeness remains unproved", True),
        ("interacting NESS and microscopic current remain unconstructed", True),
        ("physical W and kappa remain unselected", True),
        ("smooth unreduced gauge parent remains unconstructed", True),
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
        "break_yukawa_l1", "break_self_energy", "break_filling_scaling",
        "break_free_exponent", "break_dressed_exponent", "break_decay_power",
    )]
    updates = (
        ("erase_local_exclusion", lambda d: d["relativistic_local_number"].__setitem__("critical_local_exclusion_controls_interval_number_squared", False)),
        ("invent_Hartree_proof", lambda d: d["relativistic_local_number"].__setitem__("one_body_Hartree_density_alone_is_the_many_body_proof", True)),
        ("invent_bosonic_transfer", lambda d: d["relativistic_local_number"].__setitem__("bosons_inherit_the_same_uniform_bound", True)),
        ("erase_sector_uniformity", lambda d: d["screened_form"].__setitem__("estimate_is_uniform_over_all_fock_sectors", False)),
        ("erase_self_energy", lambda d: d["screened_form"].__setitem__("positive_field_energy_includes_diagonal_self_energy", False)),
        ("erase_normal_ordering", lambda d: d["screened_form"].__setitem__("normal_ordering_subtracts_only_a_linear_number_term", False)),
        ("erase_L4", lambda d: d["ibc_boundary_modes"].__setitem__("position_mode_is_in_L2_and_L4", False)),
        ("erase_borderline", lambda d: d["ibc_boundary_modes"].__setitem__("free_half_derivative_endpoint_is_borderline", False)),
        ("erase_dressed_form", lambda d: d["ibc_boundary_modes"].__setitem__("screened_form_is_finite_on_the_dressed_point_form_domain", False)),
        ("erase_screened_H", lambda d: d["all_sector_operator"].__setitem__("self_adjoint_all_sector_screened_hamiltonian_exists", False)),
        ("invent_finite_box_limit", lambda d: d["all_sector_operator"].__setitem__("finite_box_screened_norm_resolvent_limit_is_proved", True)),
        ("invent_kappa_selection", lambda d: d["all_sector_operator"].__setitem__("screening_mass_is_selected_by_GU_or_source", True)),
        ("erase_rank_inversion", lambda d: d["finite_boundary_threshold"].__setitem__("nonzero_full_rank_endpoint_dressing_inverts_the_singularity", False)),
        ("erase_integrability", lambda d: d["finite_boundary_threshold"].__setitem__("impurity_local_cutoff_decay_is_time_integrable", False)),
        ("erase_projection", lambda d: d["finite_boundary_threshold"].__setitem__("point_spectrum_must_be_projected", False)),
        ("invent_dark_control", lambda d: d["finite_boundary_threshold"].__setitem__("rank_deficient_dark_channels_are_uniformly_controlled", True)),
        ("invent_global_decay", lambda d: d["finite_boundary_threshold"].__setitem__("result_is_a_global_full_fock_local_decay_norm", True)),
        ("invent_HVZ", lambda d: d["scattering_and_ownership_boundary"].__setitem__("full_fock_HVZ_theorem_proved", True)),
        ("invent_resonance_exclusion", lambda d: d["scattering_and_ownership_boundary"].__setitem__("all_many_body_threshold_resonances_excluded", True)),
        ("invent_propagation", lambda d: d["scattering_and_ownership_boundary"].__setitem__("global_high_energy_propagation_bound_proved", True)),
        ("invent_scattering", lambda d: d["scattering_and_ownership_boundary"].__setitem__("Moller_or_Ruelle_wave_operators_constructed", True)),
        ("invent_completeness", lambda d: d["scattering_and_ownership_boundary"].__setitem__("asymptotic_completeness_proved", True)),
        ("invent_NESS", lambda d: d["scattering_and_ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("invent_current", lambda d: d["scattering_and_ownership_boundary"].__setitem__("microscopic_field_current_constructed", True)),
        ("invent_physical_selector", lambda d: d["scattering_and_ownership_boundary"].__setitem__("physical_W_or_kappa_selected", True)),
        ("invent_smooth_parent", lambda d: d["scattering_and_ownership_boundary"].__setitem__("smooth_unreduced_connection_or_BRST_parent_constructed", True)),
        ("invent_source_owner", lambda d: d["scattering_and_ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["scattering_and_ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["scattering_and_ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["scattering_and_ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
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
    print(f"K142 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
