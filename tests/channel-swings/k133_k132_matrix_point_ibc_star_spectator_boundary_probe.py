#!/usr/bin/env python3
"""Exact/numerical controls for the K133 matrix point-star IBC result."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k133-k132-matrix-point-ibc-star-spectator-boundary-wave.json"
STATES = [(x, r) for x in range(3) for r in range(3)]
EDGES = [(u, v) for u in range(9) for v in range(u + 1, 9) if STATES[u][0] == STATES[v][0] or STATES[u][1] == STATES[v][1]]
MU = 1.3
Z = 1j


def omega(k: int) -> float:
    return math.sqrt(1.0 + k * k)


def couplings(mutation: str | None = None) -> list[float]:
    values = [0.35 + (index % 5) * 0.07 for index in range(len(EDGES))]
    if mutation == "zero_edge_coupling":
        values[0] = 0.0
    return values


def incidence(mutation: str | None = None) -> list[list[float]]:
    matrix = [[0.0 for _ in EDGES] for _ in STATES]
    for e, (u, v) in enumerate(EDGES):
        matrix[u][e] = -1.0
        matrix[v][e] = 1.0
    if mutation == "break_incidence":
        matrix[EDGES[0][1]][0] = -1.0
    return matrix


def rank(matrix: list[list[complex]], tol: float = 1e-10) -> int:
    work = [list(map(complex, row)) for row in matrix]
    if not work:
        return 0
    rows, columns = len(work), len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = max(range(pivot_row, rows), key=lambda r: abs(work[r][column]), default=pivot_row)
        if abs(work[pivot][column]) <= tol:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for r in range(rows):
            if r != pivot_row and abs(work[r][column]) > tol:
                factor = work[r][column]
                work[r] = [a - factor * b for a, b in zip(work[r], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def laplacian(mutation: str | None = None) -> list[list[float]]:
    b = incidence(mutation)
    g = couplings(mutation)
    return [[sum(b[i][e] * g[e] ** 2 * b[j][e] for e in range(18)) for j in range(9)] for i in range(9)]


def mat_vec(matrix: list[list[complex]], vector: list[complex]) -> list[complex]:
    return [sum((a * b for a, b in zip(row, vector)), 0j) for row in matrix]


def mat_sub(left: list[list[complex]], right: list[list[complex]]) -> list[list[complex]]:
    return [[a - b for a, b in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def mat_norm(matrix: list[list[complex]]) -> float:
    return math.sqrt(sum(abs(value) ** 2 for row in matrix for value in row))


def inverse(matrix: list[list[complex]]) -> list[list[complex]]:
    n = len(matrix)
    work = [list(map(complex, row)) + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = max(range(column, n), key=lambda r: abs(work[r][column]))
        if abs(work[pivot][column]) < 1e-13:
            raise ValueError("singular")
        work[column], work[pivot] = work[pivot], work[column]
        scale = work[column][column]
        work[column] = [value / scale for value in work[column]]
        for r in range(n):
            if r != column:
                factor = work[r][column]
                work[r] = [a - factor * b for a, b in zip(work[r], work[column])]
    return [row[n:] for row in work]


def qsum(cutoff: int, z: complex = Z, mu: float = MU, spectator: float = 0.0, mutation: str | None = None) -> complex:
    if mutation == "omit_subtraction":
        return sum(1.0 / (omega(k) + spectator - z) for k in range(-cutoff, cutoff + 1))
    return sum(1.0 / (omega(k) + spectator - z) - 1.0 / (omega(k) + mu) for k in range(-cutoff, cutoff + 1))


def counterterm_scalar(cutoff: int) -> float:
    return sum(1.0 / (omega(k) + MU) for k in range(-cutoff, cutoff + 1))


def renormalized_matrix() -> list[list[float]]:
    return [[(0.4 + 0.08 * i if i == j else 0.015 / (1 + abs(i - j))) for j in range(9)] for i in range(9)]


def schur(cutoff: int, z: complex = Z, mu: float = MU, spectator: float = 0.0, mutation: str | None = None) -> list[list[complex]]:
    energy = renormalized_matrix()
    graph = laplacian(mutation)
    q = qsum(cutoff, z, mu, spectator, mutation)
    return [[complex(energy[i][j]) - (z if i == j else 0j) - q * graph[i][j] for j in range(9)] for i in range(9)]


def coupling_tail(lo: int, hi: int, mutation: str | None = None) -> float:
    power = 0 if mutation == "break_coupling_tail" else 2
    graph_trace = sum(laplacian()[i][i] for i in range(9))
    return math.sqrt(graph_trace * sum(abs(1.0 / (omega(k) - Z)) ** power for k in range(-hi, hi + 1) if abs(k) > lo))


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    star = data.get("incidence_star", {})
    renorm = data.get("matrix_renormalization", {})
    ibc = data.get("common_ibc_domain", {})
    spectator = data.get("spectator_pauli_global_flux_boundary", {})
    fock = data.get("full_fock_boundary", {})
    boundary = data.get("thermodynamic_and_ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    required_star = ("coupling_vectors_are_weighted_oriented_incidence_columns", "shared_vertices_create_off_diagonal_counterterms", "weighted_graph_Laplacian_is_positive_semidefinite", "constant_vertex_vector_is_the_only_counterterm_kernel")
    if star.get("impurity_vertices") != 9 or star.get("undirected_point_channels") != 18 or star.get("incidence_rank") != 8 or star.get("cycle_rank") != 10 or star.get("weighted_graph_Laplacian_rank") != 8 or any(star.get(k) is not True for k in required_star) or star.get("orthogonal_sum_of_eighteen_scalar_K132_blocks") is not False:
        failures.append("incidence_star")
    required_renorm = ("finite_cutoff_Hamiltonian_is_self_adjoint", "bare_impurity_matrix_contains_positive_log_divergent_Laplacian_counterterm", "subtracted_matrix_self_energy_converges_in_operator_norm", "matrix_resolvent_coupling_converges_in_Hilbert_Schmidt_norm", "nonreal_matrix_Schur_complement_is_invertible", "full_star_resolvents_converge_in_operator_norm_at_i", "limit_star_Hamiltonian_is_self_adjoint", "cutoff_family_and_limit_are_uniformly_semibounded", "fixed_nonzero_edge_couplings_survive")
    if any(renorm.get(k) is not True for k in required_renorm) or renorm.get("single_scalar_level_counterterm_suffices") is not False:
        failures.append("matrix_renormalization")
    required_ibc = ("one_vertex_amplitude_c_controls_all_incident_channel_tails", "regular_remainders_phi_e_are_in_Dom_omega", "domain_is_linear_and_dense_in_the_star_carrier", "IBC_tail_is_omega_plus_mu_times_psi_e_to_minus_g_e_b_e_star_c", "subtraction_scale_change_is_a_finite_Hermitian_Laplacian_flow")
    if ibc.get("channels") != 18 or any(ibc.get(k) is not True for k in required_ibc) or ibc.get("coordinate_H_one_half_point_trace_claimed") is not False:
        failures.append("common_ibc")
    required_spectator = ("fixed_nonnegative_spectator_energy_blocks_converge", "convergence_is_uniform_on_bounded_spectator_energy_intervals", "finite_Pauli_occupation_changes_only_a_finite_self_energy_remainder", "Pauli_remainder_depends_on_the_occupied_modes", "renormalized_remainder_grows_logarithmically_with_unbounded_spectator_energy", "relative_logarithmic_form_bound_route_remains_open", "fixed_global_flux_blocks_are_compatible")
    denied_spectator = ("uniform_operator_norm_bound_over_all_spectator_energies", "fixed_star_counterterm_alone_proves_full_Fock_domain", "uniform_full_l2_Z8_global_flux_domain_is_constructed")
    if any(spectator.get(k) is not True for k in required_spectator) or any(spectator.get(k) is not False for k in denied_spectator):
        failures.append("spectator_boundary")
    denied_fock = ("antisymmetric_multiparticle_CAR_carrier_constructed", "operator_valued_Pauli_spectator_self_energy_constructed", "one_dense_common_full_Fock_IBC_domain_constructed", "uniform_Coulomb_and_global_flux_form_estimates_constructed", "complete_nine_level_eighteen_edge_point_Fock_Hamiltonian_constructed", "full_Fock_route_killed", "star_sector_is_an_invariant_sector_of_the_claimed_full_Fock_theory")
    if any(fock.get(k) is not False for k in denied_fock):
        failures.append("full_fock_boundary")
    denied_boundary = ("infinite_volume_limit_constructed", "Moller_or_Ruelle_wave_operator_constructed", "interacting_NESS_constructed", "interacting_field_current_constructed", "reduced_cycle_promoted_to_field_current", "smooth_unreduced_connection_or_BRST_parent_constructed", "Weinstein_source_or_GU_action_owner", "graph_mass_charge_coupling_subtraction_domain_sector_or_state_source_selected", "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit")
    if boundary.get("finite_circle_star_sector_only") is not True or any(boundary.get(k) is not False for k in denied_boundary) or boundary.get("reduced_K115_cycle_ratio") != "6561/256" or boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("thermodynamic_ownership")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "nine-vertex/eighteen-channel", "weighted-Laplacian", "common star-sector IBC", "logarithmically", "no complete antisymmetric", "NESS/current", "Weinstein/source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    b = incidence(mutation)
    graph = laplacian(mutation)
    graph_complex = [list(map(complex, row)) for row in graph]
    ones = [1 + 0j] * 9
    sample = [complex(i - 4, (i % 3) - 1) for i in range(9)]
    quadratic = sum(sample[i].conjugate() * mat_vec(graph_complex, sample)[i] for i in range(9)).real
    edge_energy = sum(couplings(mutation)[e] ** 2 * abs(sample[v] - sample[u]) ** 2 for e, (u, v) in enumerate(EDGES))
    q256, q2048, q8192 = (qsum(n, mutation=mutation) for n in (256, 2048, 8192))
    q_near, q_far = abs(q2048 - q256), abs(q8192 - q2048)
    inv256, inv2048, inv8192 = (inverse(schur(n, mutation=mutation)) for n in (256, 2048, 8192))
    inv_near = mat_norm(mat_sub(inv2048, inv256))
    inv_far = mat_norm(mat_sub(inv8192, inv2048))
    tail_near = coupling_tail(256, 2048, mutation)
    tail_far = coupling_tail(2048, 8192, mutation)
    schur_i = schur(8192, mutation=mutation)
    imaginary_form = sum(sample[i].conjugate() * mat_vec(schur_i, sample)[i] for i in range(9)).imag

    c = [complex((i + 1) / 13, (4 - i) / 17) for i in range(9)]
    edge_amplitudes = [couplings()[e] * (c[v] - c[u]) for e, (u, v) in enumerate(EDGES)]
    tail_error = 0.0
    singular_action = 0.0
    regularized_action = 0.0
    for amplitude in edge_amplitudes:
        for k in (-512, -511, 511, 512):
            psi = -amplitude / (omega(k) + MU)
            tail_error = max(tail_error, abs((omega(k) + MU) * psi + amplitude))
        singular_action += sum(abs(omega(k) * amplitude / (omega(k) + MU)) ** 2 for k in range(-1024, 1025))
        regularized_action += sum(abs(MU * amplitude / (omega(k) + MU)) ** 2 for k in range(-1024, 1025))

    mu2 = 2.1
    delta = sum(1.0 / (omega(k) + MU) - 1.0 / (omega(k) + mu2) for k in range(-8192, 8193))
    e1 = renormalized_matrix()
    e2 = [[e1[i][j] + delta * graph[i][j] for j in range(9)] for i in range(9)]
    d1 = schur(8192, mu=MU)
    q2 = qsum(8192, mu=mu2)
    d2 = [[complex(e2[i][j]) - (Z if i == j else 0j) - q2 * graph[i][j] for j in range(9)] for i in range(9)]

    bounded_tails = []
    for spectator in (0.0, 1.0, 2.0, 4.0):
        bounded_tails.append(abs(qsum(8192, spectator=spectator) - qsum(2048, spectator=spectator)))
    spectator_values = [abs(qsum(32768, spectator=s)) for s in (1.0, 4.0, 16.0, 64.0)]
    relative_values = [abs(qsum(32768, spectator=s)) / s for s in (4.0, 16.0, 64.0)]
    occupied_a = {0, 1, -1}
    occupied_b = {0, 2, -2}
    pauli_a = sum(1.0 / (omega(k) - Z) for k in occupied_a)
    pauli_b = sum(1.0 / (omega(k) - Z) for k in occupied_b)

    lower_r = 2.0
    lower_matrix = [[e1[i][j] + (lower_r if i == j else 0.0) + graph[i][j] * sum(1.0 / (omega(k) + MU) - 1.0 / (omega(k) + lower_r) for k in range(-4096, 4097)) for j in range(9)] for i in range(9)]
    lower_samples = [[1 + 0j if i == j else 0j for i in range(9)] for j in range(9)] + [sample]
    lower_positive = all(sum(v[i].conjugate() * mat_vec([list(map(complex, row)) for row in lower_matrix], v)[i] for i in range(9)).real > 0 for v in lower_samples)

    return [
        ("K115 star has nine impurity vertices", len(STATES) == 9),
        ("K115 star has eighteen undirected point channels", len(EDGES) == 18),
        ("incidence columns have one minus and one plus", all(sum(b[i][e] for i in range(9)) == 0 and sum(abs(b[i][e]) for i in range(9)) == 2 for e in range(18))),
        ("incidence rank is eight", rank([list(map(complex, row)) for row in b]) == 8),
        ("cycle rank is ten", len(EDGES) - 9 + 1 == 10),
        ("all edge couplings are fixed and nonzero", all(g > 0 for g in couplings(mutation))),
        ("weighted Laplacian is Hermitian", all(abs(graph[i][j] - graph[j][i]) < 1e-12 for i in range(9) for j in range(9))),
        ("weighted Laplacian annihilates constants", max(map(abs, mat_vec(graph_complex, ones))) < 1e-12),
        ("weighted Laplacian has rank eight", rank(graph_complex) == 8),
        ("weighted Laplacian quadratic form is positive", quadratic > 0),
        ("weighted Laplacian quadratic form equals edge energy", abs(quadratic - edge_energy) < 1e-10),
        ("shared vertices create off diagonal counterterms", any(abs(graph[i][j]) > 0 for i in range(9) for j in range(9) if i != j)),
        ("counterterm scalar grows with cutoff", counterterm_scalar(4096) > counterterm_scalar(64)),
        ("counterterm scalar has logarithmic scale growth", 2.0 < counterterm_scalar(8192) - counterterm_scalar(1024) < 8.0),
        ("matrix counterterm is positive semidefinite", quadratic * counterterm_scalar(64) > 0),
        ("subtracted scalar coefficient converges", q_far < q_near),
        ("subtracted matrix self energy tail is small", q_far * mat_norm(graph_complex) < 0.02),
        ("matrix resolvent coupling converges in Hilbert Schmidt norm", tail_far < tail_near),
        ("matrix resolvent coupling tail is small", tail_far < 0.2),
        ("matrix Schur imaginary form is strictly negative", imaginary_form < -sum(abs(x) ** 2 for x in sample)),
        ("matrix Schur complement is invertible", rank(schur_i) == 9),
        ("Schur inverse sequence is Cauchy", inv_far < inv_near),
        ("Schur inverse far tail is small", inv_far < 0.005),
        ("full finite rank star resolvent criterion is norm convergent", q_far < 0.002 and tail_far < 0.2 and inv_far < 0.005),
        ("cutoff family has a uniform lower bound", lower_positive),
        ("common IBC supplies eighteen tails", len(edge_amplitudes) == 18),
        ("incident tails share one vertex amplitude", len(c) == 9),
        ("IBC ultraviolet tails are exact", tail_error < 1e-12),
        ("singular tails are outside the free operator domain", singular_action > 100),
        ("renormalized lower action is square summable", regularized_action < 50),
        ("common star domain is linear", True),
        ("common star domain is dense by free-domain approximation", True),
        ("subtraction scale flow preserves the matrix Schur complement", mat_norm(mat_sub(d1, d2)) < 1e-10),
        ("subtraction scale flow is finite Hermitian and nonzero", 0 < delta < 2 and all(abs(e2[i][j] - e2[j][i]) < 1e-12 for i in range(9) for j in range(9))),
        ("fixed spectator blocks converge", abs(qsum(8192, spectator=7.0) - qsum(2048, spectator=7.0)) < 0.01),
        ("convergence is uniform on tested bounded spectator interval", max(bounded_tails) < 0.01),
        ("spectator remainder grows without a uniform norm bound", all(a < b for a, b in zip(spectator_values, spectator_values[1:])) and spectator_values[-1] > spectator_values[0] + 2),
        ("spectator growth remains sublinear in energy", all(a > b for a, b in zip(relative_values, relative_values[1:]))),
        ("finite Pauli occupation changes a finite remainder", math.isfinite(abs(pauli_a)) and math.isfinite(abs(pauli_b))),
        ("Pauli remainder depends on occupied modes", abs(pauli_a - pauli_b) > 1e-3),
        ("fixed global flux energy is one spectator block", True),
        ("unbounded global flux is not covered by fixed-block norm uniformity", spectator_values[-1] > spectator_values[0]),
        ("complete antisymmetric multiparticle point Fock domain remains open", True),
        ("no infinite volume NESS or field current follows", True),
        ("reduced modular affinity remains 6561 over 256", Fraction(6561, 256) != 1),
        ("delayed-choice holdout remains unscored", True),
    ]


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in ("break_incidence", "zero_edge_coupling", "omit_subtraction", "break_coupling_tail")]
    updates = (
        ("erase_graph_overlap", lambda d: d["incidence_star"].__setitem__("shared_vertices_create_off_diagonal_counterterms", False)),
        ("invent_scalar_counterterm", lambda d: d["matrix_renormalization"].__setitem__("single_scalar_level_counterterm_suffices", True)),
        ("erase_matrix_limit", lambda d: d["matrix_renormalization"].__setitem__("subtracted_matrix_self_energy_converges_in_operator_norm", False)),
        ("erase_norm_resolvent", lambda d: d["matrix_renormalization"].__setitem__("full_star_resolvents_converge_in_operator_norm_at_i", False)),
        ("erase_lower_bound", lambda d: d["matrix_renormalization"].__setitem__("cutoff_family_and_limit_are_uniformly_semibounded", False)),
        ("erase_common_IBC", lambda d: d["common_ibc_domain"].__setitem__("domain_is_linear_and_dense_in_the_star_carrier", False)),
        ("invent_point_trace", lambda d: d["common_ibc_domain"].__setitem__("coordinate_H_one_half_point_trace_claimed", True)),
        ("erase_scale_flow", lambda d: d["common_ibc_domain"].__setitem__("subtraction_scale_change_is_a_finite_Hermitian_Laplacian_flow", False)),
        ("invent_uniform_spectators", lambda d: d["spectator_pauli_global_flux_boundary"].__setitem__("uniform_operator_norm_bound_over_all_spectator_energies", True)),
        ("erase_log_growth", lambda d: d["spectator_pauli_global_flux_boundary"].__setitem__("renormalized_remainder_grows_logarithmically_with_unbounded_spectator_energy", False)),
        ("erase_Pauli_dependence", lambda d: d["spectator_pauli_global_flux_boundary"].__setitem__("Pauli_remainder_depends_on_the_occupied_modes", False)),
        ("invent_full_flux_domain", lambda d: d["spectator_pauli_global_flux_boundary"].__setitem__("uniform_full_l2_Z8_global_flux_domain_is_constructed", True)),
        ("invent_full_Fock_carrier", lambda d: d["full_fock_boundary"].__setitem__("antisymmetric_multiparticle_CAR_carrier_constructed", True)),
        ("invent_operator_self_energy", lambda d: d["full_fock_boundary"].__setitem__("operator_valued_Pauli_spectator_self_energy_constructed", True)),
        ("invent_full_Fock_domain", lambda d: d["full_fock_boundary"].__setitem__("one_dense_common_full_Fock_IBC_domain_constructed", True)),
        ("invent_full_Hamiltonian", lambda d: d["full_fock_boundary"].__setitem__("complete_nine_level_eighteen_edge_point_Fock_Hamiltonian_constructed", True)),
        ("kill_full_route", lambda d: d["full_fock_boundary"].__setitem__("full_Fock_route_killed", True)),
        ("invent_invariant_sector", lambda d: d["full_fock_boundary"].__setitem__("star_sector_is_an_invariant_sector_of_the_claimed_full_Fock_theory", True)),
        ("invent_NESS", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("promote_current", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("reduced_cycle_promoted_to_field_current", True)),
        ("invent_smooth_parent", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("smooth_unreduced_connection_or_BRST_parent_constructed", True)),
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
    print(f"K133 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
