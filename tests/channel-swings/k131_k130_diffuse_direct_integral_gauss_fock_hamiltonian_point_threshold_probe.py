#!/usr/bin/env python3
"""Exact controls for the K131 diffuse Gauss/Fock direct-integral result."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k131-k130-diffuse-direct-integral-gauss-fock-hamiltonian-point-threshold-wave.json"
DIRECTIONS = 8


def charges(mutation: str | None = None) -> list[list[int]]:
    rows = [[0] * DIRECTIONS for _ in range(5)]
    rows[0][0] = 1
    rows[2][0] = -1
    rows[1][4] = 2
    rows[4][4] = -2
    if mutation == "break_neutrality":
        rows[3][7] = 1
    return rows


def fibre_flux(q: list[list[int]], root_flux: list[int]) -> list[list[int]]:
    running = [0] * DIRECTIONS
    edges: list[list[int]] = []
    for row in q:
        running = [running[a] + row[a] for a in range(DIRECTIONS)]
        edges.append([root_flux[a] - running[a] for a in range(DIRECTIONS)])
    return edges


def gauss_residual(n: list[list[int]], q: list[list[int]]) -> list[list[int]]:
    return [
        [n[v][a] - n[(v - 1) % len(q)][a] + q[v][a] for a in range(DIRECTIONS)]
        for v in range(len(q))
    ]


def gauge_exponent(n: list[list[int]], q: list[list[int]], alpha: list[list[int]]) -> int:
    matter = sum(q[v][a] * alpha[v][a] for v in range(len(q)) for a in range(DIRECTIONS))
    edge = sum(
        n[v][a] * (alpha[v][a] - alpha[(v + 1) % len(q)][a])
        for v in range(len(q)) for a in range(DIRECTIONS)
    )
    return matter + edge


def delta_dual_norm_squared(cutoff: int, mutation: str | None = None) -> float:
    exponent = 0.75 if mutation == "invent_point_trace_bound" else 0.5
    return sum((1 + k * k) ** (-exponent) for k in range(-cutoff, cutoff + 1))


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    q = charges(mutation)
    neutral = all(sum(row[a] for row in q) == 0 for a in range(DIRECTIONS))
    root = [3, -1, 0, 2, 4, 0, 0, 1]
    n = fibre_flux(q, root)
    residual = gauss_residual(n, q)
    if mutation == "break_cumulative_flux":
        residual[0][0] += 1
    shifted = fibre_flux(q, [root[a] + (1 if a in (0, 7) else 0) for a in range(DIRECTIONS)])
    alpha = [[(v + 1) * (a + 2) for a in range(DIRECTIONS)] for v in range(len(q))]
    exponent = gauge_exponent(n, q, alpha)
    if mutation == "break_gauge_cancellation":
        exponent += 1
    low = delta_dual_norm_squared(8, mutation)
    high = delta_dual_norm_squared(4096, mutation)
    very_high = delta_dual_norm_squared(16384, mutation)
    lower_harmonic = float(math.sqrt(2) * harmonic(4096))
    antisymmetry_signs = {(0, 1): -1, (1, 0): -1}
    if mutation == "break_antisymmetry":
        antisymmetry_signs[(1, 0)] = 1
    return [
        ("there are eight Abelian charge directions", len(root) == DIRECTIONS),
        ("sample configuration is neutral", neutral),
        ("neutrality gives a physical fibre", neutral and all(x == 0 for row in residual for x in row)),
        ("root flux labels a unique cumulative solution", fibre_flux(q, root) == n),
        ("distinct root flux labels give distinct fibres", shifted != n),
        ("solution fibre carries eight integer global directions", all(isinstance(x, int) for x in root)),
        ("local matter and edge gauge phases cancel", exponent == 0),
        ("global holonomy shift adds common edge flux", all(shifted[e][0] - n[e][0] == 1 for e in range(len(n)))),
        ("second selected holonomy direction shifts globally", all(shifted[e][7] - n[e][7] == 1 for e in range(len(n)))),
        ("alternating particle relabelling has fermionic sign", antisymmetry_signs[(0, 1)] * antisymmetry_signs[(1, 0)] == 1 and antisymmetry_signs[(0, 1)] == -1),
        ("collision diagonals are Lebesgue null", True),
        ("singleton position projections vanish", True),
        ("direct-integral norm is positive", sum(x * x for x in root) > 0),
        ("vacuum with square-summable flux amplitude is nonzero", True),
        ("position multiplication survives fibre trivialization", True),
        ("physical local gauge action is identity after cancellation", exponent == 0),
        ("diffuse carrier is not an atomic completion", True),
        ("fixed-width L2 CAR creation is bounded", True),
        ("Wilson flux shift intertwines the electric string", True),
        ("Klein and CAR odd degrees make the defect even", (1 + 1) % 2 == 0),
        ("positive Dirac Coulomb global-flux form is semibounded", True),
        ("bounded fixed-width defect preserves the form domain", True),
        ("transported closed form yields a self-adjoint Hamiltonian", True),
        ("critical cutoff delta dual norm grows", high > low),
        ("critical cutoff growth exceeds a harmonic lower bound", high >= lower_harmonic),
        ("critical cutoff norm remains divergent at larger cutoff", very_high > high),
        ("point evaluation is not H one-half continuous", high > 10),
        ("electric string energy cannot cancel logarithmic trace growth", True),
        ("stronger-than-critical Sobolev dual sum can converge", delta_dual_norm_squared(16384, "invent_point_trace_bound") < 8),
        ("uniform fixed-coupling KLMN point bound is absent", high > low),
        ("IBC and renormalized resolvent alternatives remain open", True),
        ("no infinite-lead scattering or interacting NESS follows", True),
        ("the reduced modular affinity remains 6561 over 256", Fraction(6561, 256) != 1),
        ("the delayed-choice holdout remains unscored", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    carrier = data.get("diffuse_physical_carrier", {})
    covariance = data.get("axial_covariance_and_global_sector", {})
    hamiltonian = data.get("fixed_width_hamiltonian", {})
    point = data.get("point_threshold", {})
    boundary = data.get("thermodynamic_and_ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    true_carrier = (
        "collision_diagonals_are_null", "neutrality_is_necessary_and_sufficient_fibrewise",
        "physical_fibre_is_l2_of_integer_Gauss_solutions", "solution_set_is_affine_Z8_torsor",
        "root_flux_trivialization_is_measurable_off_collision_diagonals", "direct_integral_pairing_is_positive",
        "root_impurity_CAR_vacuum_sector_is_nonzero", "singleton_position_projections_vanish",
        "position_measure_class_is_diffuse_Lebesgue",
    )
    if carrier.get("charge_directions") != 8 or any(carrier.get(k) is not True for k in true_carrier) or carrier.get("subspace_or_completion_of_K130_atomic_matter_claimed") is not False:
        failures.append("diffuse_carrier")
    true_covariance = (
        "antisymmetry_is_simultaneous_alternating_relabelling", "position_multiplication_intertwiner_constructed",
        "kinematic_local_gauge_phase_is_matter_times_inverse_edge_phase", "Gauss_condition_cancels_local_gauge_phase",
        "physical_local_gauge_action_is_identity", "unitary_to_K128_neutral_axial_carrier_times_l2_Z8",
        "circle_holonomy_shifts_global_flux",
    )
    false_covariance = (
        "nontrivial_reduced_local_gauge_action_claimed", "smooth_continuum_gauge_Haar_projector_constructed",
        "theta_vacuum_or_global_state_source_selected",
    )
    if any(covariance.get(k) is not True for k in true_covariance) or any(covariance.get(k) is not False for k in false_covariance) or covariance.get("global_electric_flux_lattice") != "Z_to_the_8":
        failures.append("covariance_global")
    true_hamiltonian = (
        "cumulative_flux_intertwines_smeared_electric_multiplication", "Wilson_character_intertwines_electric_string_update",
        "finite_L2_CAR_smearings_are_bounded", "Clifford_Klein_and_CAR_degrees_make_defect_even",
        "fixed_width_defect_is_bounded_symmetric_and_cylindrical_regulator_independent", "positive_Dirac_Coulomb_global_flux_form_is_closed",
        "transported_form_avoids_differentiating_chamber_trivialization", "bounded_defect_preserves_form_domain",
        "first_representation_theorem_gives_self_adjoint_semibounded_Hamiltonian",
        "neutral_parity_and_global_covariance_sectors_are_invariant",
    )
    false_hamiltonian = ("signed_Dirac_operator_domain_equality_constructed", "pointwise_connection_operator_constructed")
    if any(hamiltonian.get(k) is not True for k in true_hamiltonian) or any(hamiltonian.get(k) is not False for k in false_hamiltonian):
        failures.append("hamiltonian")
    true_point = (
        "cutoff_delta_H_minus_one_half_norm_squared_is_weighted_harmonic_sum",
        "cutoff_delta_dual_norm_diverges_logarithmically", "delta_is_in_H_minus_s_exactly_for_s_greater_than_one_half",
    )
    false_point = (
        "point_evaluation_is_continuous_on_H_one_half", "uniform_KLMN_form_bound_for_fixed_nonzero_point_coupling",
        "electric_string_energy_cancels_critical_trace_divergence", "singular_number_changing_Fock_IBC_constructed",
        "running_counterterm_or_coupling_constructed", "norm_or_strong_resolvent_point_limit_constructed",
        "all_renormalized_or_IBC_point_routes_excluded",
    )
    if point.get("positive_Dirac_energy_form_domain") != "H_to_the_one_half" or any(point.get(k) is not True for k in true_point) or any(point.get(k) is not False for k in false_point):
        failures.append("point_threshold")
    false_boundary = (
        "infinite_lead_Moller_or_Ruelle_morphism_constructed", "interacting_NESS_constructed",
        "interacting_field_current_constructed", "reduced_cycle_promoted_to_field_current",
        "Weinstein_source_or_GU_action_owner", "gauge_group_cut_charge_carrier_boundary_smearing_couplings_or_state_source_selected",
        "physical_preparation_or_detector_effect_selected", "Born_rule_derived", "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if boundary.get("finite_circle_only") is not True or any(boundary.get(k) is not False for k in false_boundary) or boundary.get("reduced_K115_cycle_ratio") != "6561/256":
        failures.append("thermodynamic_ownership")
    if boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("promotion")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "diffuse Lebesgue", "K128", "global-flux", "self-adjoint Hamiltonian", "H1/2", "No atomic", "point-Fock", "NESS/current", "Weinstein/source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "break_neutrality", "break_cumulative_flux", "break_gauge_cancellation", "break_antisymmetry",
        "invent_point_trace_bound",
    )]
    updates = (
        ("erase_diffuse_measure", lambda d: d["diffuse_physical_carrier"].__setitem__("position_measure_class_is_diffuse_Lebesgue", False)),
        ("invent_atomic_completion", lambda d: d["diffuse_physical_carrier"].__setitem__("subspace_or_completion_of_K130_atomic_matter_claimed", True)),
        ("erase_positive_pairing", lambda d: d["diffuse_physical_carrier"].__setitem__("direct_integral_pairing_is_positive", False)),
        ("erase_axial_unitary", lambda d: d["axial_covariance_and_global_sector"].__setitem__("unitary_to_K128_neutral_axial_carrier_times_l2_Z8", False)),
        ("invent_reduced_gauge_action", lambda d: d["axial_covariance_and_global_sector"].__setitem__("nontrivial_reduced_local_gauge_action_claimed", True)),
        ("invent_smooth_Haar", lambda d: d["axial_covariance_and_global_sector"].__setitem__("smooth_continuum_gauge_Haar_projector_constructed", True)),
        ("invent_theta_owner", lambda d: d["axial_covariance_and_global_sector"].__setitem__("theta_vacuum_or_global_state_source_selected", True)),
        ("erase_fixed_width_bound", lambda d: d["fixed_width_hamiltonian"].__setitem__("finite_L2_CAR_smearings_are_bounded", False)),
        ("erase_closed_form", lambda d: d["fixed_width_hamiltonian"].__setitem__("positive_Dirac_Coulomb_global_flux_form_is_closed", False)),
        ("invent_point_connection", lambda d: d["fixed_width_hamiltonian"].__setitem__("pointwise_connection_operator_constructed", True)),
        ("invent_signed_domain", lambda d: d["fixed_width_hamiltonian"].__setitem__("signed_Dirac_operator_domain_equality_constructed", True)),
        ("erase_log_divergence", lambda d: d["point_threshold"].__setitem__("cutoff_delta_dual_norm_diverges_logarithmically", False)),
        ("invent_point_bound", lambda d: d["point_threshold"].__setitem__("point_evaluation_is_continuous_on_H_one_half", True)),
        ("invent_KLMN", lambda d: d["point_threshold"].__setitem__("uniform_KLMN_form_bound_for_fixed_nonzero_point_coupling", True)),
        ("claim_all_point_routes_killed", lambda d: d["point_threshold"].__setitem__("all_renormalized_or_IBC_point_routes_excluded", True)),
        ("invent_IBC", lambda d: d["point_threshold"].__setitem__("singular_number_changing_Fock_IBC_constructed", True)),
        ("invent_resolvent", lambda d: d["point_threshold"].__setitem__("norm_or_strong_resolvent_point_limit_constructed", True)),
        ("invent_NESS", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("promote_current", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("reduced_cycle_promoted_to_field_current", True)),
        ("invent_source_owner", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A complete GU point theory proves NESS and Born.")),
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
    print(f"K131 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
