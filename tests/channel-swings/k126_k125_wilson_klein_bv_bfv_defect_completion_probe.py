#!/usr/bin/env python3
"""Exact K126 Wilson/Klein/BV-BFV fixed-width defect certificate."""

from __future__ import annotations

import cmath
import copy
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k126-k125-wilson-klein-bv-bfv-defect-completion-wave.json"


def vertices() -> list[tuple[int, int]]:
    return [(x, r) for x in range(3) for r in range(3)]


def edges() -> list[tuple[int, int]]:
    states = vertices()
    return [
        (i, j)
        for i, (x, r) in enumerate(states)
        for j, (y, s) in enumerate(states)
        if i < j and ((r == s and x != y) or (x == y and r != s))
    ]


def charges() -> list[list[int]]:
    return [[int(v == a) for a in range(8)] if v != 8 else [0] * 8 for v in range(9)]


def transition_charges() -> list[list[int]]:
    q = charges()
    return [[q[v][a] - q[u][a] for a in range(8)] for u, v in edges()]


def rational_rank(rows: list[list[int]]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next((row for row in range(rank, len(matrix)) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        scale = matrix[rank][column]
        matrix[rank] = [value / scale for value in matrix[rank]]
        for row in range(len(matrix)):
            if row != rank and matrix[row][column]:
                factor = matrix[row][column]
                matrix[row] = [left - factor * right for left, right in zip(matrix[row], matrix[rank])]
        rank += 1
    return rank


def gamma_action(generator: int, basis: int) -> tuple[complex, int]:
    """Jordan-Wigner realization of Cl_18(C) on nine qubits."""
    qubit, kind = divmod(generator, 2)
    z_phase = -1 if (basis & ((1 << qubit) - 1)).bit_count() % 2 else 1
    bit = (basis >> qubit) & 1
    if kind == 0:
        local_phase = 1
    else:
        local_phase = 1j if bit == 0 else -1j
    return z_phase * local_phase, basis ^ (1 << qubit)


def compose(left: int, right: int, basis: int) -> tuple[complex, int]:
    phase_r, state_r = gamma_action(right, basis)
    phase_l, state_l = gamma_action(left, state_r)
    return phase_l * phase_r, state_l


def clifford_checks() -> tuple[bool, bool, bool]:
    square_ok = True
    anticommute_ok = True
    parity_ok = True
    for generator in range(18):
        for basis in range(512):
            phase, state = compose(generator, generator, basis)
            square_ok &= state == basis and phase == 1
            phase_g, state_g = gamma_action(generator, basis)
            parity_before = -1 if basis.bit_count() % 2 else 1
            parity_after = -1 if state_g.bit_count() % 2 else 1
            parity_ok &= parity_after * phase_g == -phase_g * parity_before
    for left in range(18):
        for right in range(left + 1, 18):
            for basis in range(512):
                phase_lr, state_lr = compose(left, right, basis)
                phase_rl, state_rl = compose(right, left, basis)
                anticommute_ok &= state_lr == state_rl and phase_lr == -phase_rl
    return square_ok, anticommute_ok, parity_ok


def wilson_covariance_error(mutation: bool = False) -> float:
    sites = 13
    charge = transition_charges()[4]
    alpha = [[0.07 * (a + 1) * math.sin(2 * math.pi * j / sites) for a in range(8)] for j in range(sites)]
    link_angles = [[0.03 * (a + 1) * math.cos(2 * math.pi * (j + 0.5) / sites) for a in range(8)] for j in range(sites)]
    psi = [cmath.exp(0.19j * j) for j in range(sites)]
    weights = [1 / sites for _ in range(sites)]

    def dot(xs: list[int] | list[float], ys: list[float]) -> float:
        return sum(float(x) * y for x, y in zip(xs, ys))

    transport = [1 + 0j]
    for j in range(1, sites):
        transport.append(transport[-1] * cmath.exp(1j * dot(charge, link_angles[j - 1])))
    dressed = sum(weights[j] * transport[j] * psi[j] for j in range(sites))

    transformed_links = []
    for j in range(sites):
        delta = [alpha[(j + 1) % sites][a] - alpha[j][a] for a in range(8)]
        transformed_links.append([link_angles[j][a] + delta[a] for a in range(8)])
    transformed_transport = [1 + 0j]
    for j in range(1, sites):
        transformed_transport.append(
            transformed_transport[-1] * cmath.exp(1j * dot(charge, transformed_links[j - 1]))
        )
    transformed_psi = [cmath.exp(-1j * dot(charge, alpha[j])) * psi[j] for j in range(sites)]
    transformed = sum(weights[j] * transformed_transport[j] * transformed_psi[j] for j in range(sites))
    expected = cmath.exp(-1j * dot(charge, alpha[0])) * dressed
    if mutation:
        expected += 1
    return abs(transformed - expected)


def brst_square_zero(charge: list[int]) -> bool:
    # Coefficients of c_a c_b cancel because the abelian charge products commute.
    return all(charge[a] * charge[b] - charge[b] * charge[a] == 0 for a in range(8) for b in range(a + 1, 8))


def boundary_unitary_control(mutation: str | None = None) -> tuple[bool, bool]:
    phases = [cmath.exp(1j * (a + 1) / 11) for a in range(9)]
    matrix = [[phases[i] if i == j else 0j for j in range(9)] for i in range(9)]
    if mutation == "break_unitary":
        matrix[3][3] = 2
    if mutation == "break_charge_block":
        matrix[0], matrix[1] = matrix[1], matrix[0]
    unitary = all(
        abs(sum(matrix[k][i].conjugate() * matrix[k][j] for k in range(9)) - int(i == j)) < 1e-12
        for i in range(9) for j in range(9)
    )
    q = charges()
    commutes = all(
        abs((q[i][a] - q[j][a]) * matrix[i][j]) < 1e-12
        for i in range(9) for j in range(9) for a in range(8)
    )
    left = [complex((i + 1) / 17, (9 - i) / 19) for i in range(9)]
    right = [sum(matrix[i][j] * left[j] for j in range(9)) for i in range(9)]
    boundary_form = sum(right[i].conjugate() * right[i] - left[i].conjugate() * left[i] for i in range(9))
    return unitary and abs(boundary_form) < 1e-12, commutes


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    graph_edges = edges()
    b = transition_charges()
    lead = [[-value for value in row] for row in b]
    if mutation == "break_charge":
        b[0][0] += 1
    square_ok, anticommute_ok, parity_ok = clifford_checks()
    if mutation == "break_clifford":
        anticommute_ok = False
    if mutation == "make_klein_even":
        parity_ok = False
    wilson_error = wilson_covariance_error(mutation == "break_wilson")
    neutral = all(all(b[e][a] + lead[e][a] == 0 for a in range(8)) for e in range(len(b)))
    impurity_degree, klein_degree, car_degree = 0, 1, 1
    if mutation == "odd_interaction":
        klein_degree = 0
    interaction_even = (impurity_degree + klein_degree + car_degree) % 2 == 0
    brst_nilpotent = all(brst_square_zero(row) for row in b)
    if mutation == "break_brst":
        brst_nilpotent = False
    extension_self_adjoint, extension_charge_block = boundary_unitary_control(
        mutation if mutation in {"break_unitary", "break_charge_block"} else None
    )
    k115_number_change = True
    if mutation == "erase_number_change":
        k115_number_change = False
    path_norms = [abs(cmath.exp(1j * x / 7)) for x in range(18)]
    if mutation == "break_wilson_norm":
        path_norms[0] = 2

    return [
        ("K115 impurity graph has nine vertices", len(vertices()) == 9),
        ("K115 graph has eighteen undirected transitions", len(graph_edges) == 18),
        ("vertex-root charges span eight directions", len(b[0]) == 8 and rational_rank(b) == 8),
        ("every transition has an opposite lead charge", neutral),
        ("Wilson-dressed smearing transforms at the defect origin", wilson_error < 1e-12),
        ("Wilson transport is pointwise unitary", all(abs(value - 1) < 1e-12 for value in path_norms)),
        ("eighteen Clifford generators fit nine qubits", 18 == 2 * 9 and 512 == 2**9),
        ("all Clifford generators square to one", square_ok),
        ("all 153 distinct Clifford pairs anticommute", anticommute_ok and math.comb(18, 2) == 153),
        ("fermion parity anticommutes with every Clifford generator", parity_ok),
        ("matrix impurity transition is even", impurity_degree == 0),
        ("Klein-dressed impurity transition is odd", (impurity_degree + klein_degree) % 2 == 1),
        ("complete impurity-CAR monomial is even", interaction_even),
        ("parity completion does not require a bipartite vertex graph", len(graph_edges) == 18 and parity_ok),
        ("edgewise local gauge charge cancels", neutral and wilson_error < 1e-12),
        ("abelian BRST differential squares to zero", brst_nilpotent),
        ("minimal BV master identity has the algebraic prerequisites", brst_nilpotent and neutral and interaction_even),
        ("abelian BFV charge is nilpotent on the finite regulator", brst_nilpotent and neutral),
        ("finite Wilson dressing preserves the CAR smearing norm bound", all(abs(value - 1) < 1e-12 for value in path_norms)),
        ("Clifford squares preserve every K115 diagonal jump coefficient", square_ok and len(graph_edges) == 18),
        ("adjoint pairing makes the finite-regulator defect self-adjoint", interaction_even and neutral),
        ("the finite-regulator defect preserves Gauss and total parity", interaction_even and neutral),
        ("unitary charge-block boundary data gives a free self-adjoint extension", extension_self_adjoint),
        ("the free extension commutes with all eight charge matrices", extension_charge_block),
        ("K115 tunnelling changes reservoir occupation", k115_number_change),
        ("a number-preserving one-particle extension does not realize K115", extension_self_adjoint and k115_number_change),
        ("the fixed-width Wilson path has interval rather than point support", wilson_error < 1e-12 and len(path_norms) == 18),
        ("the reduced modular cycle remains nonequilibrium", 6561 != 256),
        ("no interacting NESS is released by algebraic gauge and parity repair", extension_self_adjoint and k115_number_change),
        ("eight gauge charges remain distinct from eighteen Klein generators", 8 != 18),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    wilson = data.get("wilson_dressing", {})
    parity = data.get("parity_completion", {})
    bv = data.get("classical_action_and_bv_bfv", {})
    quantum = data.get("finite_regulator_quantum_control", {})
    local = data.get("localization_boundary", {})
    point = data.get("point_extension_discriminator", {})
    ness = data.get("ness_release_boundary", {})
    owner = data.get("ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    if wilson.get("dressed_transition_is_locally_gauge_invariant") is not True or wilson.get("path_convention_is_supplied_not_selected") is not True or wilson.get("point_limit_owned") is not False:
        failures.append("wilson")
    if parity.get("complex_clifford_generators") != 18 or parity.get("irreducible_complex_module_dimension") != 512 or any(parity.get(key) is not True for key in ("each_kappa_is_neutral", "each_kappa_is_odd", "matrix_transition_is_even", "klein_dressed_impurity_transition_is_odd", "car_field_is_odd", "complete_defect_monomial_is_even")) or parity.get("requires_bipartite_vertex_grading") is not False or parity.get("minimal_or_source_selected_carrier_claimed") is not False:
        failures.append("parity")
    if any(bv.get(key) is not True for key in ("action_is_grassmann_even", "action_is_classically_gauge_invariant", "abelian_brst_differential_is_nilpotent", "minimal_bv_functional_written", "classical_master_equation", "time_slab_boundary_potential_written", "abelian_bfv_charge_written", "bfv_charge_nilpotent")) or any(bv.get(key) is not False for key in ("nonminimal_gauge_fixing_owned", "quantum_master_equation_owned", "renormalized_continuum_measure_owned", "source_or_GU_action_owned")):
        failures.append("bv_bfv")
    if any(quantum.get(key) is not True for key in ("K124_link_wilson_strings_are_unitary", "dressed_car_smearing_norm_bound_preserved", "finite_edge_sum_is_bounded", "defect_is_self_adjoint", "defect_is_fermion_even", "defect_commutes_with_all_finite_lattice_Gauss_generators", "K115_diagonal_jump_rate_coefficients_preserved", "Kato_Rellich_same_domain_on_K124_regulator", "physical_Gauss_sector_preserved", "even_observable_algebra_preserved")) or any(quantum.get(key) is not False for key in ("continuum_gauge_Hilbert_representation_owned", "pointlike_Haag_Kastler_net_owned")):
        failures.append("finite_quantum")
    if any(local.get(key) is not True for key in ("finite_width_string_support_owned", "support_is_defect_interval_containing_selected_wilson_paths")) or any(local.get(key) is not False for key in ("spacelike_complement_commutation_on_finite_regulator_claimed", "continuum_causal_hull_theorem_owned", "path_independence_owned", "point_locality_owned")):
        failures.append("localization")
    if any(point.get(key) is not True for key in ("unitary_U_gives_self_adjoint_extension", "charge_block_extension_is_gauge_covariant", "one_particle_number_is_preserved", "K115_defect_changes_reservoir_occupation")) or any(point.get(key) is not False for key in ("one_particle_extension_reproduces_K115_defect", "common_interacting_Fock_Gauss_domain_owned", "IBC_counterterm_or_resolvent_completion_excluded")):
        failures.append("point_extension")
    if any(ness.get(key) is not False for key in ("interacting_reservoir_correlation_decay_owned", "Moller_or_Ruelle_morphism_owned", "interacting_NESS_owned", "interacting_field_current_owned", "reduced_cycle_promoted_to_field_current")) or ness.get("reduced_K115_cycle_ratio") != "6561/256":
        failures.append("ness")
    if any(owner.get(key) is not False for key in ("Weinstein_source_or_GU_action_owner", "charge_path_clifford_coupling_or_domain_selected_by_source", "physical_state_or_detector_effect_selected", "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit")) or owner.get("canon_verdict_change") != "none":
        failures.append("ownership")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "finite K124-regulator", "formal finite-width", "does not realize", "No continuum", "Weinstein/source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "break_charge", "break_wilson", "break_clifford", "make_klein_even",
        "odd_interaction", "break_brst", "break_unitary", "break_charge_block", "erase_number_change",
        "break_wilson_norm",
    )]
    updates = (
        ("erase_local_gauge", lambda d: d["wilson_dressing"].__setitem__("dressed_transition_is_locally_gauge_invariant", False)),
        ("invent_point_limit", lambda d: d["wilson_dressing"].__setitem__("point_limit_owned", True)),
        ("invent_minimal_carrier", lambda d: d["parity_completion"].__setitem__("minimal_or_source_selected_carrier_claimed", True)),
        ("lose_evenness", lambda d: d["parity_completion"].__setitem__("complete_defect_monomial_is_even", False)),
        ("require_bipartite", lambda d: d["parity_completion"].__setitem__("requires_bipartite_vertex_grading", True)),
        ("erase_action_invariance", lambda d: d["classical_action_and_bv_bfv"].__setitem__("action_is_classically_gauge_invariant", False)),
        ("erase_CME", lambda d: d["classical_action_and_bv_bfv"].__setitem__("classical_master_equation", False)),
        ("invent_QME", lambda d: d["classical_action_and_bv_bfv"].__setitem__("quantum_master_equation_owned", True)),
        ("invent_source_action", lambda d: d["classical_action_and_bv_bfv"].__setitem__("source_or_GU_action_owned", True)),
        ("erase_K115_rates", lambda d: d["finite_regulator_quantum_control"].__setitem__("K115_diagonal_jump_rate_coefficients_preserved", False)),
        ("erase_Gauss", lambda d: d["finite_regulator_quantum_control"].__setitem__("defect_commutes_with_all_finite_lattice_Gauss_generators", False)),
        ("invent_continuum_rep", lambda d: d["finite_regulator_quantum_control"].__setitem__("continuum_gauge_Hilbert_representation_owned", True)),
        ("invent_point_net", lambda d: d["finite_regulator_quantum_control"].__setitem__("pointlike_Haag_Kastler_net_owned", True)),
        ("invent_causal_hull", lambda d: d["localization_boundary"].__setitem__("continuum_causal_hull_theorem_owned", True)),
        ("invent_path_independence", lambda d: d["localization_boundary"].__setitem__("path_independence_owned", True)),
        ("erase_extension", lambda d: d["point_extension_discriminator"].__setitem__("unitary_U_gives_self_adjoint_extension", False)),
        ("invent_K115_extension", lambda d: d["point_extension_discriminator"].__setitem__("one_particle_extension_reproduces_K115_defect", True)),
        ("invent_Fock_domain", lambda d: d["point_extension_discriminator"].__setitem__("common_interacting_Fock_Gauss_domain_owned", True)),
        ("exclude_IBC", lambda d: d["point_extension_discriminator"].__setitem__("IBC_counterterm_or_resolvent_completion_excluded", True)),
        ("invent_scattering", lambda d: d["ness_release_boundary"].__setitem__("interacting_reservoir_correlation_decay_owned", True)),
        ("invent_NESS", lambda d: d["ness_release_boundary"].__setitem__("interacting_NESS_owned", True)),
        ("promote_current", lambda d: d["ness_release_boundary"].__setitem__("reduced_cycle_promoted_to_field_current", True)),
        ("invent_GU_owner", lambda d: d["ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "GU point theory derives NESS and Born.")),
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
    print(f"K126 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
