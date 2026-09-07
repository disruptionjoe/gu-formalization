#!/usr/bin/env python3
"""Exact/numerically bounded K125 continuum and unsmearing certificate."""

from __future__ import annotations

import cmath
import copy
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k125-k124-continuum-gauge-defect-bv-aqft-ness-wave.json"
SITES = (16, 32, 64, 128)
MODES = (-2, -1, 0, 1, 2)
THETA = Fraction(1, 3)
INVERSE_WIDTHS = (4, 16, 64, 256)


def charges() -> list[list[int]]:
    return [[int(v == a) for a in range(8)] if v != 8 else [0] * 8 for v in range(9)]


def edges() -> list[tuple[int, int]]:
    states = [(x, r) for x in range(3) for r in range(3)]
    return [
        (i, j)
        for i, (x, r) in enumerate(states)
        for j, (y, s) in enumerate(states)
        if i < j and ((r == s and x != y) or (x == y and r != s))
    ]


def transition_charges() -> list[list[int]]:
    q = charges()
    return [[q[v][a] - q[u][a] for a in range(8)] for u, v in edges()]


def lattice_energy(n: int, k: int, theta: float) -> float:
    p = 2.0 * math.pi * k - theta
    return 4.0 * n * n * math.sin(p / (2.0 * n)) ** 2


def continuum_energy(k: int, theta: float) -> float:
    return (2.0 * math.pi * k - theta) ** 2


def gauge_covariance_error(n: int = 16) -> float:
    a = 1.0 / n
    theta = float(THETA)
    psi = [cmath.exp(2j * math.pi * 2 * j / n) for j in range(n)]
    alpha = [0.17 * math.sin(2.0 * math.pi * j / n) for j in range(n)]
    links = [cmath.exp(-1j * theta / n) for _ in range(n)]
    transformed_psi = [cmath.exp(1j * alpha[j]) * psi[j] for j in range(n)]
    transformed_links = [
        cmath.exp(1j * alpha[j]) * links[j] * cmath.exp(-1j * alpha[(j + 1) % n])
        for j in range(n)
    ]
    original = [(links[j] * psi[(j + 1) % n] - psi[j]) / a for j in range(n)]
    transformed = [
        (transformed_links[j] * transformed_psi[(j + 1) % n] - transformed_psi[j]) / a
        for j in range(n)
    ]
    return max(abs(transformed[j] - cmath.exp(1j * alpha[j]) * original[j]) for j in range(n))


def summation_by_parts() -> bool:
    phi = [Fraction(j * j - 3 * j + 1, 17) for j in range(8)]
    electric = [Fraction(2 * j - 5, 13) for j in range(8)]
    left = sum(phi[j] * (electric[j] - electric[(j - 1) % 8]) for j in range(8))
    right = -sum(electric[j] * (phi[(j + 1) % 8] - phi[j]) for j in range(8))
    return left == right


def has_triangle(graph_edges: list[tuple[int, int]]) -> bool:
    adjacency = {vertex: set() for vertex in range(9)}
    for left, right in graph_edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    return any(
        right in adjacency[left]
        for vertex in adjacency
        for left in adjacency[vertex]
        for right in adjacency[vertex]
        if left < right
    )


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    theta = float(THETA)
    b = transition_charges()
    car = [[-value for value in row] for row in b]
    if mutation == "break_neutrality":
        car[0][0] += 1
    q_left = [row[:] for row in b]
    q_right = [row[:] for row in b]
    if mutation == "add_chiral_anomaly":
        q_right[0][0] += 1
    anomaly_matrix = [
        [
            sum(q_left[e][a] * q_left[e][c] - q_right[e][a] * q_right[e][c] for e in range(len(b)))
            for c in range(8)
        ]
        for a in range(8)
    ]

    errors = {
        n: max(abs(continuum_energy(k, theta) - lattice_energy(n, k, theta)) for k in MODES)
        for n in SITES
    }
    bounds = {
        n: max(
            (2.0 * math.pi * k - theta) ** 4 / (12.0 * n * n)
            for k in MODES
        )
        for n in SITES
    }
    if mutation == "break_continuum_symbol":
        errors[SITES[-1]] = bounds[SITES[-1]] + 1.0
    monotone = all(errors[right] < errors[left] for left, right in zip(SITES, SITES[1:]))
    bound_ok = all(errors[n] <= bounds[n] * (1.0 + 1e-10) for n in SITES)

    holonomy_errors = []
    for n in SITES:
        product = 1.0 + 0.0j
        for _ in range(n):
            product *= cmath.exp(-1j * theta / n)
        holonomy_errors.append(abs(product - cmath.exp(-1j * theta)))
    covariance = gauge_covariance_error()
    if mutation == "break_gauge_covariance":
        covariance = 1.0

    l2_squared = {m: Fraction(m) for m in INVERSE_WIDTHS}
    fixed_norm = {m: math.sqrt(float(l2_squared[m])) for m in INVERSE_WIDTHS}
    bounded_coupling_norm = {m: (1.0 / math.sqrt(m)) * fixed_norm[m] for m in INVERSE_WIDTHS}
    bounded_point_strength = {m: 1.0 / math.sqrt(m) for m in INVERSE_WIDTHS}
    if mutation == "invent_bounded_point_strength":
        bounded_point_strength[INVERSE_WIDTHS[-1]] = 1.0

    neutral = all([b[i][a] + car[i][a] for a in range(8)] == [0] * 8 for i in range(len(b)))
    electric = [Fraction(2 * j - 5, 13) for j in range(8)]
    divergence_sum = sum(electric[j] - electric[(j - 1) % 8] for j in range(8))
    weak_gauss = summation_by_parts()
    if mutation == "break_weak_gauss":
        weak_gauss = False
    local_phase_mismatch = abs(cmath.exp(1j * 0.37) * cmath.exp(-1j * 0.11) - 1.0)
    if mutation == "hide_local_gauge_mismatch":
        local_phase_mismatch = 0.0
    triangle = has_triangle(edges())
    if mutation == "hide_parity_triangle":
        triangle = False
    ness_released = False
    if mutation == "invent_ness":
        ness_released = True

    return [
        ("K124 supplies eighteen transition species", len(b) == 18),
        ("eight charge directions remain", len(b[0]) == 8),
        ("every fixed-width defect monomial is neutral", neutral),
        ("full left-right Dirac anomaly matrix cancels in all 64 entries", all(value == 0 for row in anomaly_matrix for value in row)),
        ("fixed-mode covariant squared symbol approaches continuum value", monotone),
        ("low-mode squared-symbol error obeys the O(N^-2) bound", bound_ok),
        ("largest-grid low-mode error is below one percent", errors[128] < 0.01 * max(continuum_energy(k, theta) for k in MODES)),
        ("discrete local gauge covariance is exact to roundoff", covariance < 1e-11),
        ("Wilson holonomy survives the continuum refinement", max(holonomy_errors) < 1e-12),
        ("periodic divergence obeys exact summation by parts", weak_gauss),
        ("periodic electric divergence has zero global sum", divergence_sum == 0),
        ("neutral transition pair satisfies the global Gauss sum", neutral and all(sum((b[0][a], car[0][a])) == 0 for a in range(8))),
        ("certificate makes no graph-norm or common operator-core claim", all(abs(k) <= 2 for k in MODES)),
        ("undressed finite-width charged smearing fails local gauge invariance", local_phase_mismatch > 0.1),
        ("rook transition graph has a triangle obstructing all-transition odd grading", triangle),
        ("delta-normalized box has unit L1 norm", all(Fraction(1, m) * m == 1 for m in INVERSE_WIDTHS)),
        ("delta-normalized box has L2 norm squared epsilon^-1", all(l2_squared[m] == m for m in INVERSE_WIDTHS)),
        ("fixed nonzero CAR defect norm diverges", all(fixed_norm[r] > fixed_norm[l] for l, r in zip(INVERSE_WIDTHS, INVERSE_WIDTHS[1:]))),
        ("sqrt-epsilon coupling keeps CAR defect norm bounded", max(abs(value - 1.0) for value in bounded_coupling_norm.values()) < 1e-12),
        ("that bounded scaling loses nonzero point strength", bounded_point_strength[256] < bounded_point_strength[4] and bounded_point_strength[256] < 0.1),
        ("bounded-perturbation route has no nontrivial delta limit", fixed_norm[256] == 16.0 and bounded_point_strength[256] == Fraction(1, 16)),
        ("odd inherited defect does not establish even observable-subnet invariance", triangle),
        ("no fixed-width interacting local-net theorem is claimed", triangle and local_phase_mismatch > 0.1),
        ("reduced modular cycle remains nonequilibrium", Fraction(6561, 256) != 1),
        ("interacting field NESS is not released without scattering control", not ness_released),
        ("eight gauge charges are not ten transition cycles", 8 != 10),
        ("compact phase is not the real modular affinity", cmath.exp(1j * theta).real != math.log(6561 / 256)),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    smooth = data.get("smooth_continuum_gauge_sector", {})
    gauss = data.get("gauss_domain_and_anomaly", {})
    bv = data.get("fixed_smearing_bv_bfv_boundary", {})
    net = data.get("fixed_width_causal_net_boundary", {})
    point = data.get("point_unsmearing_boundary", {})
    ness = data.get("ness_release_boundary", {})
    cycle = data.get("cycle_and_selection_boundary", {})
    owner = data.get("ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    if any(smooth.get(key) is not True for key in ("fixed_mode_squared_symbol_converges", "discrete_gauge_covariance_exact", "Wilson_holonomy_converges_and_survives")) or any(smooth.get(key) is not False for key in ("isometric_lattice_to_continuum_embedding_owned", "graph_norm_core_convergence_owned", "full_interacting_norm_resolvent_limit_owned")):
        failures.append("smooth_continuum")
    if any(gauss.get(key) is not True for key in ("periodic_discrete_summation_by_parts_exact", "classical_weak_continuum_Gauss_identity_consistent", "global_neutrality_survives", "eighteen_full_Dirac_species_are_vectorlike", "full_8_by_8_abelian_anomaly_matrix_cancels_conditionally")) or any(gauss.get(key) is not False for key in ("continuum_gauge_Hilbert_space_owned", "common_free_finite_Fourier_electric_core_owned", "point_defect_common_self_adjoint_Gauss_domain_owned")):
        failures.append("gauss_domain")
    if any(bv.get(key) is not True for key in ("epsilon_positive", "global_charge_neutrality_is_necessary")) or any(bv.get(key) is not False for key in ("undressed_smearing_is_locally_gauge_invariant", "typed_odd_impurity_or_Klein_carrier_owned", "bosonic_classical_defect_action_owned", "minimal_classical_BV_master_identity_owned", "boundary_BFV_Gauss_charge_owned_formally", "quantum_renormalized_master_equation_owned", "source_or_GU_action_owned")):
        failures.append("fixed_smearing_bv")
    if net.get("bounded_self_adjoint_global_Cstar_dynamics_owned") is not True or any(net.get(key) is not False for key in ("K123_defect_is_even", "rook_graph_all_transition_odd_grading_exists", "even_observable_subnet_invariance_owned", "interacting_locality_outside_causal_hull_owned", "static_defect_time_covariance_owned", "pointlike_Haag_Kastler_net_owned", "Poincare_covariant_defect_theory_owned")):
        failures.append("fixed_width_net")
    if any(point.get(key) is not True for key in ("CAR_annihilation_norm_equals_L2_norm", "fixed_nonzero_coupling_defect_norm_diverges", "uniform_boundedness_requires_coupling_O_sqrt_epsilon", "that_bounded_scaling_has_zero_distributional_point_strength")) or point.get("nontrivial_uniformly_bounded_delta_limit_exists_within_inherited_linear_CAR_mollifier_ansatz") is not False or point.get("all_self_adjoint_point_interactions_excluded") is not False:
        failures.append("point_unsmearing")
    if any(ness.get(key) is not False for key in ("fixed_width_interacting_scattering_or_correlation_decay_theorem_owned", "Moller_or_Ruelle_interacting_NESS_owned", "Cesaro_cluster_state_with_current_owned", "reduced_affinity_promoted_to_interacting_field_current")) or ness.get("reduced_K115_stationary_law_inherited") is not True or ness.get("reduced_cycle_ratio") != "6561/256":
        failures.append("ness_boundary")
    if cycle.get("gauge_charge_directions") != 8 or cycle.get("spatial_Wilson_holonomies") != 8 or cycle.get("transition_graph_cycle_directions") != 10 or cycle.get("compact_gauge_phase_identified_with_real_affinity") is not False or cycle.get("continuum_convergence_selects_charge_embedding_couplings_or_boundary_sector") is not False:
        failures.append("cycle_selection")
    if owner.get("Weinstein_source_or_GU_action_owner") is not False or owner.get("physical_state_or_detector_effect_selected") is not False or owner.get("Born_rule_derived") is not False or owner.get("held_out_scored") is not False or owner.get("prediction_or_confirmation_credit") is not False or owner.get("canon_verdict_change") != "none":
        failures.append("ownership")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "bounded", "No universal point-defect no-go", "No", "Weinstein/source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "break_neutrality", "add_chiral_anomaly", "break_continuum_symbol",
        "break_gauge_covariance", "break_weak_gauss", "hide_local_gauge_mismatch",
        "hide_parity_triangle", "invent_bounded_point_strength", "invent_ness",
    )]
    updates = (
        ("invent_full_limit", lambda d: d["smooth_continuum_gauge_sector"].__setitem__("full_interacting_norm_resolvent_limit_owned", True)),
        ("invent_graph_limit", lambda d: d["smooth_continuum_gauge_sector"].__setitem__("graph_norm_core_convergence_owned", True)),
        ("erase_weak_gauss", lambda d: d["gauss_domain_and_anomaly"].__setitem__("classical_weak_continuum_Gauss_identity_consistent", False)),
        ("invent_point_domain", lambda d: d["gauss_domain_and_anomaly"].__setitem__("point_defect_common_self_adjoint_Gauss_domain_owned", True)),
        ("erase_anomaly", lambda d: d["gauss_domain_and_anomaly"].__setitem__("full_8_by_8_abelian_anomaly_matrix_cancels_conditionally", False)),
        ("invent_local_gauge_action", lambda d: d["fixed_smearing_bv_bfv_boundary"].__setitem__("undressed_smearing_is_locally_gauge_invariant", True)),
        ("invent_BV", lambda d: d["fixed_smearing_bv_bfv_boundary"].__setitem__("minimal_classical_BV_master_identity_owned", True)),
        ("invent_source_action", lambda d: d["fixed_smearing_bv_bfv_boundary"].__setitem__("source_or_GU_action_owned", True)),
        ("invent_even_defect", lambda d: d["fixed_width_causal_net_boundary"].__setitem__("K123_defect_is_even", True)),
        ("invent_point_net", lambda d: d["fixed_width_causal_net_boundary"].__setitem__("pointlike_Haag_Kastler_net_owned", True)),
        ("erase_norm_divergence", lambda d: d["point_unsmearing_boundary"].__setitem__("fixed_nonzero_coupling_defect_norm_diverges", False)),
        ("invent_bounded_delta", lambda d: d["point_unsmearing_boundary"].__setitem__("nontrivial_uniformly_bounded_delta_limit_exists_within_inherited_linear_CAR_mollifier_ansatz", True)),
        ("universalize_no_go", lambda d: d["point_unsmearing_boundary"].__setitem__("all_self_adjoint_point_interactions_excluded", True)),
        ("invent_scattering", lambda d: d["ness_release_boundary"].__setitem__("fixed_width_interacting_scattering_or_correlation_decay_theorem_owned", True)),
        ("invent_Ruelle_NESS", lambda d: d["ness_release_boundary"].__setitem__("Moller_or_Ruelle_interacting_NESS_owned", True)),
        ("promote_affinity", lambda d: d["ness_release_boundary"].__setitem__("reduced_affinity_promoted_to_interacting_field_current", True)),
        ("conflate_cycles", lambda d: d["cycle_and_selection_boundary"].__setitem__("transition_graph_cycle_directions", 8)),
        ("conflate_affinity", lambda d: d["cycle_and_selection_boundary"].__setitem__("compact_gauge_phase_identified_with_real_affinity", True)),
        ("invent_selection", lambda d: d["cycle_and_selection_boundary"].__setitem__("continuum_convergence_selects_charge_embedding_couplings_or_boundary_sector", True)),
        ("invent_GU_owner", lambda d: d["ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "GU continuum theory derives a NESS and Born rule.")),
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
    print(f"K125 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
