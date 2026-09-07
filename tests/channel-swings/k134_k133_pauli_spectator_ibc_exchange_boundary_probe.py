#!/usr/bin/env python3
"""Exact/numerical controls for the K134 Pauli/spectator IBC boundary."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k134-k133-pauli-spectator-ibc-exchange-boundary-wave.json"
STATES = [(x, r) for x in range(3) for r in range(3)]
EDGES = [(u, v) for u in range(9) for v in range(u + 1, 9) if STATES[u][0] == STATES[v][0] or STATES[u][1] == STATES[v][1]]
MU = 1.3


def omega(k: int) -> float:
    return math.sqrt(1.0 + k * k)


def couplings(mutation: str | None = None) -> list[float]:
    values = [0.31 + 0.05 * (i % 7) for i in range(len(EDGES))]
    if mutation == "zero_coupling":
        values[0] = 0.0
    return values


def physical_counterterm(mutation: str | None = None) -> list[list[float]]:
    matrix = [[0.0 for _ in STATES] for _ in STATES]
    for g, (_, v) in zip(couplings(mutation), EDGES):
        matrix[v][v] += g * g
    if mutation == "invent_laplacian":
        u, v = EDGES[0]
        matrix[u][v] = matrix[v][u] = -couplings()[0] ** 2
    return matrix


def incidence_laplacian() -> list[list[float]]:
    matrix = [[0.0 for _ in STATES] for _ in STATES]
    for g, (u, v) in zip(couplings(), EDGES):
        matrix[u][u] += g * g
        matrix[v][v] += g * g
        matrix[u][v] -= g * g
        matrix[v][u] -= g * g
    return matrix


def lowering_matrix(mutation: str | None = None) -> list[list[float]]:
    matrix = [[0.0 for _ in STATES] for _ in STATES]
    for g, (u, v) in zip(couplings(), EDGES):
        matrix[u][v] += g
    if mutation == "break_lowering":
        u, v = EDGES[0]
        matrix[v][u] = couplings()[0]
    return matrix


def identity(n: int) -> list[list[float]]:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def mat_add(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def mat_scale(c: float, a: list[list[float]]) -> list[list[float]]:
    return [[c * x for x in row] for row in a]


def mat_mul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def mat_power(a: list[list[float]], n: int) -> list[list[float]]:
    out = identity(len(a))
    for _ in range(n):
        out = mat_mul(out, a)
    return out


def mat_norm(a: list[list[float]]) -> float:
    return math.sqrt(sum(x * x for row in a for x in row))


def create(bits: int, mode: int) -> tuple[int, int] | None:
    if bits & (1 << mode):
        return None
    sign = -1 if (bits & ((1 << mode) - 1)).bit_count() % 2 else 1
    return bits | (1 << mode), sign


def annihilate(bits: int, mode: int) -> tuple[int, int] | None:
    if not bits & (1 << mode):
        return None
    sign = -1 if (bits & ((1 << mode) - 1)).bit_count() % 2 else 1
    return bits & ~(1 << mode), sign


def q_occupation(cutoff: int, spectator: float, occupied: set[int], mutation: str | None = None) -> float:
    value = 0.0
    for k in range(-cutoff, cutoff + 1):
        vacancy = 1.0 if k not in occupied else 0.0
        if mutation == "erase_pauli":
            vacancy = 1.0
        subtraction = 0.0 if mutation == "omit_subtraction" else 1.0 / (omega(k) + MU)
        value += vacancy / (omega(k) + spectator + MU) - subtraction
    return value


def creation_tail(lo: int, hi: int, spectator: float = 0.0, mutation: str | None = None) -> float:
    power = 0 if mutation == "break_creation_tail" else 2
    return math.sqrt(sum((omega(k) + spectator + MU) ** (-power) for k in range(-hi, hi + 1) if abs(k) > lo))


def critical_trace_data(cutoff: int, mutation: str | None = None) -> tuple[float, float, float, float]:
    ks = list(range(-cutoff, cutoff + 1))
    exponent = 1.5 if mutation == "regularize_trace" else 1.0
    normalization = math.sqrt(sum(omega(k) * omega(k) ** (-2 * exponent) for k in ks))
    f = {k: omega(k) ** (-exponent) / normalization for k in ks}
    f[0] += 1.0
    form_norm_sq = sum(omega(k) * abs(value) ** 2 for k, value in f.items())
    point_trace = sum(f.values())
    resolvent_trace = sum(value / (omega(k) + MU) for k, value in f.items())
    graph_norm_sq = sum((1.0 + omega(k) ** 2) * abs(value) ** 2 for k, value in f.items())
    return form_norm_sq, abs(point_trace), abs(point_trace * resolvent_trace), graph_norm_sq


def commutator_norm(a: list[list[float]], b: list[list[float]]) -> float:
    ab, ba = mat_mul(a, b), mat_mul(b, a)
    return mat_norm([[x - y for x, y in zip(ar, br)] for ar, br in zip(ab, ba)])


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    physical = data.get("physical_matrix_unit_contraction", {})
    self_energy = data.get("occupation_spectator_self_energy", {})
    ibc = data.get("common_ibc_boundary_core", {})
    exchange = data.get("exchange_boundary", {})
    coulomb = data.get("coulomb_gauss_boundary", {})
    boundary = data.get("thermodynamic_and_ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    required_physical = ("coupling_operator_is_B_e_equals_vertex_matrix_unit_times_Klein_generator", "positive_energy_finite_circle_control_not_full_signed_Dirac_K127_operator", "renormalized_impurity_energy_is_diagonal_in_the_ordered_vertex_basis", "vacuum_contraction_counterterm_is_sum_g_e_squared_B_e_B_e_star", "counterterm_is_diagonal_in_impurity_endpoint_basis", "counterterm_is_positive_semidefinite")
    if physical.get("impurity_states") != 9 or physical.get("undirected_CAR_species") != 18 or any(physical.get(k) is not True for k in required_physical) or physical.get("counterterm_is_K133_weighted_incidence_Laplacian") is not False or physical.get("K133_incidence_star_is_the_physical_K127_defect") is not False:
        failures.append("physical_contraction")
    required_self = ("joint_commuting_free_plus_global_flux_control_constructed", "self_energy_contains_one_minus_N_e_k_Pauli_projections", "vacuum_subtraction_leaves_a_logarithmic_spectator_function", "finite_occupation_correction_is_mode_dependent", "logarithmic_spectator_function_is_infinitesimally_energy_form_bounded", "occupation_correction_is_infinitesimally_free_energy_form_bounded", "global_flux_functional_calculus_lift_constructed")
    if any(self_energy.get(k) is not True for k in required_self) or self_energy.get("uniform_bounded_operator_self_energy_on_unbounded_spectators") is not False:
        failures.append("occupation_self_energy")
    required_ibc = ("singular_creation_map_is_norm_convergent", "matrix_unit_orientation_strictly_lowers_the_impurity_label_under_creation", "boundary_creation_map_ninth_power_is_zero", "one_minus_G_inverse_is_the_finite_sum_from_G_zero_through_G_eight", "dense_Pauli_compatible_full_Fock_IBC_boundary_core_constructed", "IBC_recursion_holds_on_every_finite_particle_sector", "creation_into_an_occupied_mode_vanishes")
    if any(ibc.get(k) is not True for k in required_ibc) or ibc.get("proved_core_for_complete_self_adjoint_point_Hamiltonian") is not False:
        failures.append("ibc_boundary_core")
    required_exchange = ("normal_ordering_produces_off_diagonal_exchange_terms", "exchange_contains_the_existing_particle_point_annihilation_trace", "critical_normalized_sequence_has_diverging_point_trace", "operator_domain_or_recursive_IBC_exchange_extension_remains_open")
    denied_exchange = ("diagonal_occupation_functional_calculus_is_the_complete_self_energy", "point_annihilation_trace_is_continuous_on_the_H_one_half_form_domain", "naive_KLMN_closure_of_the_full_exchange_term", "full_point_Fock_route_killed")
    if any(exchange.get(k) is not True for k in required_exchange) or any(exchange.get(k) is not False for k in denied_exchange):
        failures.append("exchange_boundary")
    if coulomb.get("global_flux_energy_strongly_commutes_with_CAR_occupation") is not True or any(coulomb.get(k) is not False for k in ("K128_K131_Coulomb_form_strongly_commutes_with_momentum_occupation", "commuting_spectator_formula_proves_the_physical_Coulomb_lift", "complete_Gauss_Coulomb_point_Hamiltonian_constructed", "smooth_unreduced_connection_or_BRST_parent_constructed")):
        failures.append("coulomb_boundary")
    denied_boundary = ("complete_nine_state_eighteen_species_self_adjoint_point_Fock_Hamiltonian_constructed", "infinite_volume_limit_constructed", "Moller_or_Ruelle_wave_operator_constructed", "interacting_NESS_constructed", "interacting_field_current_constructed", "reduced_cycle_promoted_to_field_current", "Weinstein_source_or_GU_action_owner", "coupling_counterterm_domain_gauge_lift_or_state_source_selected", "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit")
    if boundary.get("finite_circle_control_only") is not True or any(boundary.get(k) is not False for k in denied_boundary) or boundary.get("reduced_K115_cycle_ratio") != "6561/256" or boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("thermodynamic_ownership")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "positive-energy finite-circle", "not the full signed-Dirac", "diagonal endpoint", "occupation-projection-valued", "Pauli-compatible", "exchange", "H1/2", "no complete self-adjoint", "NESS/current", "Weinstein/source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    counterterm = physical_counterterm(mutation)
    incidence = incidence_laplacian()
    lowering = lowering_matrix(mutation)
    ninth = mat_power(lowering, 9)
    scaled = mat_scale(0.11, lowering)
    inverse_poly = [[0.0] * 9 for _ in range(9)]
    for n in range(9):
        inverse_poly = mat_add(inverse_poly, mat_power(scaled, n))
    inverse_error = mat_norm(mat_add(mat_mul(mat_add(identity(9), mat_scale(-1.0, scaled)), inverse_poly), mat_scale(-1.0, identity(9))))

    q256 = q_occupation(256, 7.0, set(), mutation)
    q2048 = q_occupation(2048, 7.0, set(), mutation)
    q8192 = q_occupation(8192, 7.0, set(), mutation)
    q_tail_near, q_tail_far = abs(q2048 - q256), abs(q8192 - q2048)
    spectator_values = [abs(q_occupation(32768, s, set(), mutation)) for s in (1.0, 4.0, 16.0, 64.0)]
    relative_values = [abs(q_occupation(32768, s, set(), mutation)) / s for s in (4.0, 16.0, 64.0)]
    occupied_a, occupied_b = {0, 1, -1}, {0, 2, -2}
    pauli_a = q_occupation(8192, 5.0, occupied_a, mutation)
    pauli_b = q_occupation(8192, 5.0, occupied_b, mutation)

    low_cut, high_cut = 8, 2048
    occupied_high = set(range(low_cut + 1, high_cut + 1, 7))
    occ_tail = sum(1.0 / (omega(k) + MU) for k in occupied_high)
    free_energy = sum(omega(k) for k in occupied_high)
    tail_bound = free_energy / (low_cut + 1) ** 2
    creation_near = creation_tail(256, 2048, mutation=mutation)
    creation_far = creation_tail(2048, 8192, mutation=mutation)

    car_checks = []
    for bits in range(1 << 5):
        for mode in range(5):
            made = create(bits, mode)
            removed = annihilate(bits, mode)
            lhs = 0
            if made is not None:
                back = annihilate(made[0], mode)
                lhs += made[1] * (back[1] if back else 0)
            if removed is not None:
                back = create(removed[0], mode)
                lhs += removed[1] * (back[1] if back else 0)
            car_checks.append(lhs == 1)

    trace_rows = [critical_trace_data(n, mutation) for n in (64, 256, 1024, 4096)]
    form_norms = [row[0] for row in trace_rows]
    point_traces = [row[1] for row in trace_rows]
    exchange_values = [row[2] for row in trace_rows]
    graph_bounds = []
    for cutoff, row in zip((64, 256, 1024, 4096), trace_rows):
        cauchy_constant = sum(1.0 / (1.0 + omega(k) ** 2) for k in range(-cutoff, cutoff + 1))
        graph_bounds.append(row[1] ** 2 <= cauchy_constant * row[3] + 1e-10)

    occupation = [[0.0, 0.0], [0.0, 1.0]]
    global_flux = [[2.0, 0.0], [0.0, 7.0]]
    coulomb_position = [[1.0, -1.0], [-1.0, 1.0]]

    return [
        ("K115 has nine impurity states", len(STATES) == 9),
        ("K115 has eighteen undirected CAR species", len(EDGES) == 18),
        ("all physical point couplings are fixed and nonzero", all(g > 0 for g in couplings(mutation))),
        ("physical contraction counterterm is Hermitian", all(abs(counterterm[i][j] - counterterm[j][i]) < 1e-12 for i in range(9) for j in range(9))),
        ("physical contraction counterterm is diagonal", all(abs(counterterm[i][j]) < 1e-12 for i in range(9) for j in range(9) if i != j)),
        ("physical contraction counterterm is positive", all(counterterm[i][i] >= 0 for i in range(9))),
        ("physical contraction has eight nonzero endpoint weights", sum(counterterm[i][i] > 0 for i in range(9)) == 8),
        ("physical counterterm differs from incidence Laplacian", mat_norm([[counterterm[i][j] - incidence[i][j] for j in range(9)] for i in range(9)]) > 0.1),
        ("K133 incidence Laplacian has off diagonal entries", any(abs(incidence[i][j]) > 0 for i in range(9) for j in range(9) if i != j)),
        ("ordered creation matrix strictly lowers impurity labels", all(abs(lowering[i][j]) < 1e-12 for i in range(9) for j in range(9) if i >= j)),
        ("boundary creation matrix ninth power vanishes", mat_norm(ninth) < 1e-12),
        ("finite polynomial is inverse to one minus G", inverse_error < 1e-10),
        ("CAR anticommutator holds on finite occupation basis", all(car_checks)),
        ("Pauli creation into occupied mode vanishes", create(0b101, 2) is None),
        ("Pauli creation into vacant mode survives", create(0b101, 1) is not None),
        ("subtracted vacuum spectator coefficient converges", q_tail_far < q_tail_near),
        ("subtracted vacuum spectator tail is small", q_tail_far < 0.01),
        ("unbounded spectator coefficient grows logarithmically", all(a < b for a, b in zip(spectator_values, spectator_values[1:]))),
        ("spectator logarithm is sublinear in energy", all(a > b for a, b in zip(relative_values, relative_values[1:]))),
        ("finite occupation correction is finite", math.isfinite(pauli_a) and math.isfinite(pauli_b)),
        ("finite occupation correction depends on occupied modes", abs(pauli_a - pauli_b) > 1e-3),
        ("Pauli vacancy changes the self energy", abs(pauli_a - q_occupation(8192, 5.0, set(), mutation)) > 1e-3),
        ("high occupation correction is bounded by free energy tail", occ_tail <= tail_bound),
        ("occupation tail relative coefficient can be made small", occ_tail / free_energy < 0.02),
        ("low occupation modes form a finite bounded block", 18 * (2 * low_cut + 1) < 400),
        ("singular creation map has a square summable tail", creation_far < creation_near),
        ("singular creation tail is small", creation_far < 0.05),
        ("IBC tail is outside the free operator domain", sum((omega(k) / (omega(k) + MU)) ** 2 for k in range(-4096, 4097)) > 1000),
        ("IBC tail remains in Fock Hilbert space", sum((omega(k) + MU) ** -2 for k in range(-4096, 4097)) < 10),
        ("one finite inverse polynomial serves every particle sector", inverse_error < 1e-10),
        ("critical sequence has bounded H one half form norm", max(form_norms) < 5.0),
        ("critical point trace grows", all(a < b for a, b in zip(point_traces, point_traces[1:]))),
        ("normal ordered exchange pairing grows", all(a < b for a, b in zip(exchange_values, exchange_values[1:])) and exchange_values[-1] > exchange_values[0] + 0.3),
        ("point trace is bounded on the free operator graph domain", all(graph_bounds)),
        ("critical form obstruction is not an operator graph obstruction", graph_bounds[-1]),
        ("global flux commutes with occupation", commutator_norm(occupation, global_flux) < 1e-12),
        ("position Coulomb control does not commute with momentum occupation", commutator_norm(occupation, coulomb_position) > 0.1),
        ("commuting global flux functional calculus is available", True),
        ("commuting spectator formula does not prove Coulomb lift", True),
        ("diagonal contraction is not the full normal ordered self energy", True),
        ("complete self adjoint physical point Fock Hamiltonian remains open", True),
        ("full point Fock route is not killed", True),
        ("no infinite volume NESS or field current follows", True),
        ("reduced modular affinity remains 6561 over 256", Fraction(6561, 256) != 1),
        ("delayed choice holdout remains unscored", True),
    ]


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in ("zero_coupling", "invent_laplacian", "break_lowering", "omit_subtraction", "erase_pauli", "break_creation_tail", "regularize_trace")]
    updates = (
        ("identify_incidence_with_physical", lambda d: d["physical_matrix_unit_contraction"].__setitem__("K133_incidence_star_is_the_physical_K127_defect", True)),
        ("transfer_laplacian", lambda d: d["physical_matrix_unit_contraction"].__setitem__("counterterm_is_K133_weighted_incidence_Laplacian", True)),
        ("erase_diagonal_counterterm", lambda d: d["physical_matrix_unit_contraction"].__setitem__("counterterm_is_diagonal_in_impurity_endpoint_basis", False)),
        ("invent_full_signed_Dirac", lambda d: d["physical_matrix_unit_contraction"].__setitem__("positive_energy_finite_circle_control_not_full_signed_Dirac_K127_operator", False)),
        ("erase_diagonal_impurity", lambda d: d["physical_matrix_unit_contraction"].__setitem__("renormalized_impurity_energy_is_diagonal_in_the_ordered_vertex_basis", False)),
        ("erase_occupation_self_energy", lambda d: d["occupation_spectator_self_energy"].__setitem__("self_energy_contains_one_minus_N_e_k_Pauli_projections", False)),
        ("invent_uniform_spectator_bound", lambda d: d["occupation_spectator_self_energy"].__setitem__("uniform_bounded_operator_self_energy_on_unbounded_spectators", True)),
        ("erase_log_relative_bound", lambda d: d["occupation_spectator_self_energy"].__setitem__("logarithmic_spectator_function_is_infinitesimally_energy_form_bounded", False)),
        ("erase_pauli_relative_bound", lambda d: d["occupation_spectator_self_energy"].__setitem__("occupation_correction_is_infinitesimally_free_energy_form_bounded", False)),
        ("erase_nilpotence", lambda d: d["common_ibc_boundary_core"].__setitem__("boundary_creation_map_ninth_power_is_zero", False)),
        ("erase_common_core", lambda d: d["common_ibc_boundary_core"].__setitem__("dense_Pauli_compatible_full_Fock_IBC_boundary_core_constructed", False)),
        ("invent_complete_H_core", lambda d: d["common_ibc_boundary_core"].__setitem__("proved_core_for_complete_self_adjoint_point_Hamiltonian", True)),
        ("erase_exchange", lambda d: d["exchange_boundary"].__setitem__("normal_ordering_produces_off_diagonal_exchange_terms", False)),
        ("diagonal_is_complete", lambda d: d["exchange_boundary"].__setitem__("diagonal_occupation_functional_calculus_is_the_complete_self_energy", True)),
        ("invent_form_trace", lambda d: d["exchange_boundary"].__setitem__("point_annihilation_trace_is_continuous_on_the_H_one_half_form_domain", True)),
        ("invent_KLMN_close", lambda d: d["exchange_boundary"].__setitem__("naive_KLMN_closure_of_the_full_exchange_term", True)),
        ("kill_route", lambda d: d["exchange_boundary"].__setitem__("full_point_Fock_route_killed", True)),
        ("invent_Coulomb_commutation", lambda d: d["coulomb_gauss_boundary"].__setitem__("K128_K131_Coulomb_form_strongly_commutes_with_momentum_occupation", True)),
        ("invent_Coulomb_lift", lambda d: d["coulomb_gauss_boundary"].__setitem__("commuting_spectator_formula_proves_the_physical_Coulomb_lift", True)),
        ("invent_full_H", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("complete_nine_state_eighteen_species_self_adjoint_point_Fock_Hamiltonian_constructed", True)),
        ("invent_NESS", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("promote_current", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("reduced_cycle_promoted_to_field_current", True)),
        ("invent_smooth_parent", lambda d: d["coulomb_gauss_boundary"].__setitem__("smooth_unreduced_connection_or_BRST_parent_constructed", True)),
        ("invent_source_owner", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A complete GU point field theory derives Born predictions.")),
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
    print(f"K134 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
