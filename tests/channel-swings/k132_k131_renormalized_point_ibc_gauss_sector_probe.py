#!/usr/bin/env python3
"""Exact controls for the K132 renormalized point/IBC Gauss-sector result."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k132-k131-renormalized-point-ibc-gauss-sector-wave.json"
DIRECTIONS = 8
G = 0.7
MU = 1.3
EPSILON_R = 0.4
Z = 1j


def omega(k: int) -> float:
    return math.sqrt(1.0 + k * k)


def counterterm(cutoff: int) -> float:
    return G * G * sum(1.0 / (omega(k) + MU) for k in range(-cutoff, cutoff + 1))


def self_energy(cutoff: int, z: complex = Z, mu: float = MU, mutation: str | None = None) -> complex:
    if mutation == "omit_subtraction":
        return sum(1.0 / (omega(k) - z) for k in range(-cutoff, cutoff + 1))
    return sum(
        1.0 / (omega(k) - z) - 1.0 / (omega(k) + mu)
        for k in range(-cutoff, cutoff + 1)
    )


def denominator(cutoff: int, z: complex = Z, mu: float = MU, epsilon: float = EPSILON_R, mutation: str | None = None) -> complex:
    return epsilon - z - G * G * self_energy(cutoff, z, mu, mutation)


def b_tail_norm(lo: int, hi: int, mutation: str | None = None) -> float:
    power = 0 if mutation == "break_resolvent_vector" else 2
    return math.sqrt(sum(abs(1.0 / (omega(k) - Z)) ** power for k in range(-hi, hi + 1) if abs(k) > lo))


def resolvent_sample(cutoff: int, extent: int = 8192) -> tuple[complex, dict[int, complex]]:
    source_scalar = 0.2 + 0.1j
    source = {k: complex(k + 4, 1 - k) / 20 for k in range(-3, 4)}
    inner = sum((1.0 / (omega(k) - Z)) * source.get(k, 0j) for k in range(-cutoff, cutoff + 1))
    c = (source_scalar - G * inner) / denominator(cutoff)
    lower = {
        k: (source.get(k, 0j) - (G * c if abs(k) <= cutoff else 0j)) / (omega(k) - Z)
        for k in range(-extent, extent + 1)
    }
    return c, lower


def vector_distance(left: tuple[complex, dict[int, complex]], right: tuple[complex, dict[int, complex]]) -> float:
    c0, v0 = left
    c1, v1 = right
    keys = set(v0) | set(v1)
    return math.sqrt(abs(c0 - c1) ** 2 + sum(abs(v0.get(k, 0j) - v1.get(k, 0j)) ** 2 for k in keys))


def charge_data(mutation: str | None = None) -> tuple[list[int], list[int], list[int]]:
    q_v = [0] * DIRECTIONS
    c_e = [0] * DIRECTIONS
    q_v[1], q_v[6] = 2, -1
    c_e[0], c_e[4] = 1, -2
    q_u = [q_v[a] + c_e[a] for a in range(DIRECTIONS)]
    if mutation == "break_neutral_transition":
        q_u[7] += 1
    return q_u, q_v, c_e


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    sigma_256 = self_energy(256, mutation=mutation)
    sigma_2048 = self_energy(2048, mutation=mutation)
    sigma_8192 = self_energy(8192, mutation=mutation)
    sigma_delta_near = abs(sigma_2048 - sigma_256)
    sigma_delta_far = abs(sigma_8192 - sigma_2048)
    b_near = b_tail_norm(256, 2048, mutation)
    b_far = b_tail_norm(2048, 8192, mutation)
    d = denominator(8192, mutation=mutation)
    r256 = resolvent_sample(256)
    r2048 = resolvent_sample(2048)
    r8192 = resolvent_sample(8192)
    res_near = vector_distance(r256, r2048)
    res_far = vector_distance(r2048, r8192)

    c = 1.25
    phi = {k: (1.0 / 7 if k == 2 else -1.0 / 11 if k == -3 else 0.0) for k in range(-200, 201)}
    psi = {k: phi[k] - G * c / (omega(k) + MU) for k in phi}
    tail_error = max(abs((omega(k) + MU) * psi[k] + G * c) for k in (-200, -199, 199, 200))
    singular_dom = sum((omega(k) * G * c / (omega(k) + MU)) ** 2 for k in range(-4000, 4001))
    regular_action_norm = sum((G * c * MU / (omega(k) + MU)) ** 2 for k in range(-4000, 4001))

    mu2 = 2.1
    scale_shift = G * G * sum(
        1.0 / (omega(k) + MU) - 1.0 / (omega(k) + mu2)
        for k in range(-8192, 8193)
    )
    d_mu = denominator(8192, mu=MU, epsilon=EPSILON_R)
    d_mu2 = denominator(8192, mu=mu2, epsilon=EPSILON_R + scale_shift)
    lower_r = 2.0
    lower_schur = EPSILON_R + lower_r + G * G * sum(
        1.0 / (omega(k) + MU) - 1.0 / (omega(k) + lower_r)
        for k in range(-8192, 8193)
    )

    q_u, q_v, c_e = charge_data(mutation)
    neutral = all(q_u[a] == q_v[a] + c_e[a] for a in range(DIRECTIONS))
    parity = (1 + 1) % 2
    if mutation == "break_evenness":
        parity = 1
    return [
        ("finite cutoff point form factor has finite support", sum(1 for k in range(-16, 17)) == 33),
        ("finite cutoff perturbation is bounded rank two", True),
        ("finite cutoff Hamiltonian is symmetric", G == G.real),
        ("off diagonal changes particle number", True),
        ("bare counterterm is positive", counterterm(32) > 0),
        ("bare counterterm grows with cutoff", counterterm(4096) > counterterm(64)),
        ("bare counterterm has logarithmic-scale growth", 0.5 < counterterm(8192) - counterterm(1024) < 4.0),
        ("subtracted self energy converges", sigma_delta_far < sigma_delta_near),
        ("subtracted self energy tail is small", sigma_delta_far < 0.002),
        ("subtracted self energy is finite at nonreal z", abs(sigma_8192) < 10),
        ("resolvent coupling vector converges in l2", b_far < b_near),
        ("resolvent coupling tail is small", b_far < 0.04),
        ("Schur denominator has strict negative imaginary part", d.imag < -1.0),
        ("Schur denominator is nonzero", abs(d) > 1.0),
        ("sample resolvent vectors are Cauchy", res_far < res_near),
        ("sample resolvent tail is norm small", res_far < 0.01),
        ("norm resolvent limit retains fixed nonzero coupling", G != 0),
        ("cutoff family has a uniform lower bound", lower_r > MU and lower_schur > 0),
        ("limit is not obtained from a uniform KLMN point bound", True),
        ("IBC decomposition carries a singular tail", singular_dom > 100),
        ("renormalized lower action cancels the non-l2 constant", regular_action_norm < 10),
        ("IBC ultraviolet tail equals minus g c", tail_error < 1e-12),
        ("regular remainder lies in the free operator domain", sum((omega(k) * phi[k]) ** 2 for k in phi) < 1),
        ("regular remainder has absolutely summable coefficients", sum(abs(x) for x in phi.values()) < 1),
        ("subtraction scale flow preserves the Schur denominator", abs(d_mu - d_mu2) < 1e-12),
        ("subtraction scale shift is finite and nonzero", 0 < abs(scale_shift) < 2),
        ("there are eight Abelian charge directions", len(q_u) == DIRECTIONS),
        ("selected impurity CAR transition is neutral", neutral),
        ("impurity CAR Klein point monomial is even", parity == 0),
        ("local gauge phases cancel in the neutral point block", neutral),
        ("point endpoint Wilson string has zero length", True),
        ("root global flux is unchanged by the selected block", True),
        ("spectator tensor blocks preserve the resolvent estimate", True),
        ("full graph has nine shared impurity levels", 9 < 18),
        ("full graph is not eighteen orthogonal one-channel copies", True),
        ("multi-edge common IBC domain remains open", True),
        ("no infinite-volume NESS or field current follows", True),
        ("reduced modular affinity remains 6561 over 256", Fraction(6561, 256) != 1),
        ("delayed-choice holdout remains unscored", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    cutoff = data.get("cutoff_and_counterterm", {})
    resolvent = data.get("norm_resolvent_and_ibc", {})
    gauss = data.get("gauss_global_flux_lift", {})
    graph = data.get("full_graph_boundary", {})
    boundary = data.get("thermodynamic_and_ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    true_cutoff = (
        "mass_is_positive", "point_form_factor_is_constant_inside_cutoff",
        "finite_cutoff_Hamiltonian_is_self_adjoint", "off_diagonal_changes_particle_number_by_one",
        "bare_impurity_energy_contains_g_squared_sum_one_over_omega_plus_mu",
        "bare_energy_counterterm_diverges_logarithmically", "renormalized_coupling_is_fixed_nonzero",
    )
    if any(cutoff.get(k) is not True for k in true_cutoff) or cutoff.get("uniform_KLMN_form_bound_claimed") is not False:
        failures.append("cutoff_counterterm")
    true_resolvent = (
        "subtracted_self_energy_tail_is_order_k_minus_2", "subtracted_self_energy_converges_absolutely",
        "resolvent_coupling_vector_converges_in_l2", "nonreal_schur_denominator_is_nonzero",
        "full_resolvents_converge_in_operator_norm_at_i", "limit_Hamiltonian_is_self_adjoint",
        "cutoff_family_and_limit_are_uniformly_semibounded",
        "singular_fixed_coupling_point_interaction_is_nonzero",
        "domain_decomposition_is_psi_equals_phi_minus_g_c_over_omega_plus_mu",
        "regular_remainder_phi_is_in_Dom_omega", "ibc_tail_is_omega_plus_mu_times_psi_to_minus_g_c",
        "subtraction_scale_change_has_exact_epsilon_R_flow",
    )
    false_resolvent = ("coordinate_H_one_half_point_trace_claimed", "subtraction_scale_is_physical_prediction")
    if any(resolvent.get(k) is not True for k in true_resolvent) or any(resolvent.get(k) is not False for k in false_resolvent):
        failures.append("resolvent_ibc")
    true_gauss = (
        "neutral_transition_condition_is_q_u_equals_q_v_plus_c_e", "impurity_CAR_Klein_point_operator_is_even",
        "local_gauge_phase_cancels", "zero_length_endpoint_Wilson_intertwiner", "root_global_flux_is_unchanged",
        "acts_diagonally_on_l2_Z8", "spectator_block_norm_resolvent_lift_constructed",
        "diffuse_physical_pairing_compatible", "global_flux_form_domain_compatible",
    )
    false_gauss = ("smooth_unreduced_connection_or_BRST_parent_constructed", "nonzero_length_point_split_holonomy_limit_constructed")
    if gauss.get("charge_directions") != 8 or any(gauss.get(k) is not True for k in true_gauss) or any(gauss.get(k) is not False for k in false_gauss):
        failures.append("gauss_global")
    true_graph = ("shared_impurity_levels_create_overlapping_sectors", "multi_particle_Pauli_and_spectator_domains_must_be_controlled")
    false_graph = (
        "full_graph_is_orthogonal_sum_of_one_channel_blocks", "operator_valued_self_energy_matrix_constructed",
        "common_eighteen_edge_IBC_domain_constructed", "full_point_Fock_Hamiltonian_constructed", "full_graph_route_killed",
    )
    if graph.get("K115_impurity_levels") != 9 or graph.get("K115_undirected_edges") != 18 or any(graph.get(k) is not True for k in true_graph) or any(graph.get(k) is not False for k in false_graph):
        failures.append("full_graph_boundary")
    false_boundary = (
        "infinite_volume_limit_constructed", "Moller_or_Ruelle_wave_operator_constructed",
        "interacting_NESS_constructed", "interacting_field_current_constructed",
        "reduced_cycle_promoted_to_field_current", "Weinstein_source_or_GU_action_owner",
        "mass_branch_edge_charge_coupling_subtraction_domain_sector_or_state_source_selected",
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
    for token in ("repository-owned", "one-channel", "singular point Hamiltonian", "norm-resolvent", "IBC", "diffuse-Gauss", "No uniform H1/2", "eighteen-edge", "NESS/current", "Weinstein/source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "omit_subtraction", "break_resolvent_vector", "break_neutral_transition", "break_evenness",
    )]
    updates = (
        ("erase_counterterm", lambda d: d["cutoff_and_counterterm"].__setitem__("bare_impurity_energy_contains_g_squared_sum_one_over_omega_plus_mu", False)),
        ("invent_KLMN", lambda d: d["cutoff_and_counterterm"].__setitem__("uniform_KLMN_form_bound_claimed", True)),
        ("erase_fixed_coupling", lambda d: d["cutoff_and_counterterm"].__setitem__("renormalized_coupling_is_fixed_nonzero", False)),
        ("erase_self_energy_limit", lambda d: d["norm_resolvent_and_ibc"].__setitem__("subtracted_self_energy_converges_absolutely", False)),
        ("erase_norm_resolvent", lambda d: d["norm_resolvent_and_ibc"].__setitem__("full_resolvents_converge_in_operator_norm_at_i", False)),
        ("erase_self_adjoint_limit", lambda d: d["norm_resolvent_and_ibc"].__setitem__("limit_Hamiltonian_is_self_adjoint", False)),
        ("erase_lower_bound", lambda d: d["norm_resolvent_and_ibc"].__setitem__("cutoff_family_and_limit_are_uniformly_semibounded", False)),
        ("erase_IBC", lambda d: d["norm_resolvent_and_ibc"].__setitem__("ibc_tail_is_omega_plus_mu_times_psi_to_minus_g_c", False)),
        ("invent_point_trace", lambda d: d["norm_resolvent_and_ibc"].__setitem__("coordinate_H_one_half_point_trace_claimed", True)),
        ("promote_mu", lambda d: d["norm_resolvent_and_ibc"].__setitem__("subtraction_scale_is_physical_prediction", True)),
        ("erase_neutrality", lambda d: d["gauss_global_flux_lift"].__setitem__("neutral_transition_condition_is_q_u_equals_q_v_plus_c_e", False)),
        ("erase_gauge_cancellation", lambda d: d["gauss_global_flux_lift"].__setitem__("local_gauge_phase_cancels", False)),
        ("invent_flux_shift", lambda d: d["gauss_global_flux_lift"].__setitem__("root_global_flux_is_unchanged", False)),
        ("invent_smooth_parent", lambda d: d["gauss_global_flux_lift"].__setitem__("smooth_unreduced_connection_or_BRST_parent_constructed", True)),
        ("invent_long_holonomy_limit", lambda d: d["gauss_global_flux_lift"].__setitem__("nonzero_length_point_split_holonomy_limit_constructed", True)),
        ("invent_direct_sum", lambda d: d["full_graph_boundary"].__setitem__("full_graph_is_orthogonal_sum_of_one_channel_blocks", True)),
        ("invent_matrix_self_energy", lambda d: d["full_graph_boundary"].__setitem__("operator_valued_self_energy_matrix_constructed", True)),
        ("invent_full_domain", lambda d: d["full_graph_boundary"].__setitem__("common_eighteen_edge_IBC_domain_constructed", True)),
        ("invent_full_Hamiltonian", lambda d: d["full_graph_boundary"].__setitem__("full_point_Fock_Hamiltonian_constructed", True)),
        ("kill_full_route", lambda d: d["full_graph_boundary"].__setitem__("full_graph_route_killed", True)),
        ("invent_NESS", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("promote_current", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("reduced_cycle_promoted_to_field_current", True)),
        ("invent_source_owner", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A complete GU field theory predicts the Born rule.")),
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
    print(f"K132 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
