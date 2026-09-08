#!/usr/bin/env python3
"""Exact/hostile controls for the K148 native hard-core threshold wave."""

from __future__ import annotations

import argparse
import copy
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k148-hard-core-infinite-u-feshbach-ground-threshold-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k148-hard-core-infinite-u-feshbach-ground-threshold-wave-2026-09-08.md"


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*matrix)]


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def dagger(matrix: list[list[float]]) -> list[list[float]]:
    return transpose(matrix)


def add(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def subtract(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(value: float, matrix: list[list[float]]) -> list[list[float]]:
    return [[value * x for x in row] for row in matrix]


def identity(size: int) -> list[list[float]]:
    return [[float(i == j) for j in range(size)] for i in range(size)]


def close(a: list[list[float]], b: list[list[float]], tol: float = 1e-12) -> bool:
    return len(a) == len(b) and all(
        len(ar) == len(br) and all(abs(x - y) <= tol for x, y in zip(ar, br))
        for ar, br in zip(a, b)
    )


def rank(matrix: list[list[float]], tol: float = 1e-12) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, rows) if abs(work[row][col]) > tol),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][col]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = work[row][col]
            work[row] = [
                x - factor * y for x, y in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def impurity_car() -> tuple[list[list[float]], list[list[float]]]:
    """Two CAR annihilators on |0>,|1>,|2>,|12> with fixed JW order."""
    d1 = [
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
    ]
    d2 = [
        [0, 0, 1, 0],
        [0, 0, 0, -1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    return d1, d2


def native_compressions() -> tuple[list[list[float]], list[list[float]]]:
    d1, d2 = impurity_car()
    p = [row[:3] for row in identity(4)[:3]]
    p_full = [row + [0.0] for row in identity(3)] + [[0.0] * 4]
    return (
        [row[:3] for row in matmul(matmul(p_full, dagger(d1)), p_full)[:3]],
        [row[:3] for row in matmul(matmul(p_full, dagger(d2)), p_full)[:3]],
    )


def native_hubbard() -> tuple[list[list[float]], list[list[float]]]:
    b1 = [[0.0] * 3 for _ in range(3)]
    b2 = [[0.0] * 3 for _ in range(3)]
    b1[1][0] = 1.0
    b2[2][0] = 1.0
    return b1, b2


def block_diag(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    result = [[0.0] * (len(a) + len(b)) for _ in range(len(a) + len(b))]
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            result[i][j] = value
    for i, row in enumerate(b):
        for j, value in enumerate(row):
            result[len(a) + i][len(a) + j] = value
    return result


def threshold_gram(p0: float, leaf: list[list[float]]) -> list[list[float]]:
    return block_diag(leaf, scale(p0, identity(2)))


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    fixed = data.get("fixed_control", {})
    lift = data.get("infinite_u_realization", {})
    feshbach = data.get("feshbach_boundary", {})
    ground = data.get("ground_comparison", {})
    thresholds = data.get("charge_thresholds", {})
    residual = data.get("residual_density_rank", {})
    bounds = data.get("boundaries", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        failures.append("classification")
    if data.get("direction") != "observed_to_native":
        failures.append("direction")
    expected_fixed = {
        "vertices": [0, 1, 2],
        "oriented_edges": [[0, 1], [0, 2]],
        "particle_coupling": 1,
        "hole_coupling": 1,
        "mass": 1,
        "screening_kappa": 1,
        "positive_screened_self_energy": "1/4",
        "subtraction_energy": 0,
        "renormalized_W": 0,
        "physically_selected": False,
    }
    if any(fixed.get(key) != value for key, value in expected_fixed.items()):
        failures.append("fixed_control")
    required_lift = {
        "penalty_forms_monotone": True,
        "strong_resolvent_limit": True,
        "limit_form_domain": "Dom(h_qf) intersect Ran(P)",
        "limit_is_native_three_state_operator": True,
        "finite_U_or_C4_is_native": False,
    }
    if any(lift.get(key) != value for key, value in required_lift.items()):
        failures.append("infinite_u_realization")
    required_feshbach = {
        "self_energy_acts_on_full_bath_Fock_space": True,
        "contains_occupation_dependent_Pauli_terms": True,
        "contains_cross_flavor_exchange_terms": True,
        "commutes_with_every_bath_occupation": False,
        "reduces_to_K147_three_by_three_Schur_matrix": False,
        "complete_charge_sector_point_spectrum_solved": False,
    }
    if any(feshbach.get(key) != value for key, value in required_feshbach.items()):
        failures.append("feshbach_boundary")
    required_ground = {
        "one_flavor_ground_energy": "E_B<0",
        "two_flavor_quadratic_ground_energy": "2*E_B",
        "quadratic_ground_intersects_native_constraint": False,
        "explicit_lower_bound": "E_hc>=2*E_B+tau*p_-^2/(1+p_-^2)",
        "upper_bound": "E_hc<=E_B<0",
        "strictly_above_unconstrained_ground": True,
        "native_global_ground_is_isolated_eigenvalue": True,
        "native_point_spectrum_nonempty": True,
        "closed_form_E_hc_computed": False,
    }
    if any(ground.get(key) != value for key, value in required_ground.items()):
        failures.append("ground_comparison")
    required_thresholds = {
        "particle_escape_shift": "residual q-e_i",
        "hole_escape_shift": "residual q+e_i",
        "first_edge_is_infimum_of_one_escape_set": True,
        "projected_K147_zero_labels_are_residual_energies": False,
        "numerical_thresholds_computed": False,
    }
    if any(thresholds.get(key) != value for key, value in required_thresholds.items()):
        failures.append("charge_thresholds")
    required_residual = {
        "leaf_gram_positive": True,
        "leaf_gram_trace": "1-p_0",
        "leaf_gram_max_rank": 2,
        "rank_formula": "rank(D_phi)=rank(L_phi)+2*1_(p_0>0)",
        "dark_dimension_formula": "dim ker(D_phi)=4-rank(D_phi)",
        "mixed_native_state_rank_when_0_lt_p0_lt_1": [3, 4],
        "SU2_invariant_nontrivial_residual_rank": 4,
        "universal_projected_rank_three_imported": False,
        "degenerate_residual_spaces_require_full_form_factor_matrix": True,
    }
    if any(residual.get(key) != value for key, value in required_residual.items()):
        failures.append("residual_density_rank")
    denied = (
        "complete_charge_sector_point_spectrum",
        "all_residual_energies_computed",
        "native_full_Fock_Mourre_or_scattering",
        "many_body_asymptotic_completeness",
        "NESS_or_current",
        "physical_parameter_or_state_selection",
        "smooth_unreduced_parent",
        "Weinstein_source_or_GU_action_owner",
        "Born_rule_derived",
        "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if any(bounds.get(key) is not False for key in denied):
        failures.append("boundary_overclaim")
    if bounds.get("canon_verdict_change") != "none":
        failures.append("canon")
    if bounds.get("paper_release_or_public_posture_change") != "none":
        failures.append("publication")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in (
        "infinite-U",
        "operator-valued",
        "isolated global ground",
        "residual impurity density",
        "No complete charge-sector",
        "physical/source",
        "Born",
    ):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(data: dict, text: str) -> list[tuple[str, bool]]:
    d1, d2 = impurity_car()
    one = identity(4)
    zeros = [[0.0] * 4 for _ in range(4)]
    car_own_1 = add(matmul(d1, dagger(d1)), matmul(dagger(d1), d1))
    car_own_2 = add(matmul(d2, dagger(d2)), matmul(dagger(d2), d2))
    car_cross = add(matmul(d1, dagger(d2)), matmul(dagger(d2), d1))
    compressed = native_compressions()
    native = native_hubbard()
    n1 = matmul(dagger(d1), d1)
    n2 = matmul(dagger(d2), d2)
    q12 = matmul(n1, n2)
    p = subtract(one, q12)
    z = 25.0 / 57.0
    p_minus = (1.0 - z) / 2.0
    p_plus = (1.0 + z) / 2.0
    tau = 1.25
    ground_q_eigs = [p_minus * p_minus, p_minus * p_plus, p_plus * p_minus, p_plus * p_plus]
    angle_bound = 1.0 / (1.0 + p_minus * p_minus)
    lower_lift = tau * p_minus * p_minus / (1.0 + p_minus * p_minus)
    q = (3, -2)
    particle_residuals = [(q[0] - 1, q[1]), (q[0], q[1] - 1)]
    hole_residuals = [(q[0] + 1, q[1]), (q[0], q[1] + 1)]
    rank_one_leaf = [[0.3, 0.3], [0.3, 0.3]]
    rank_two_leaf = [[0.25, 0.0], [0.0, 0.35]]
    gram_rank_three = threshold_gram(0.4, rank_one_leaf)
    gram_rank_four = threshold_gram(0.4, rank_two_leaf)
    su2_leaf = scale(0.3, identity(2))
    su2_gram = threshold_gram(0.4, su2_leaf)
    checks = [
        ("auxiliary d1 satisfies CAR", close(car_own_1, one)),
        ("auxiliary d2 satisfies CAR", close(car_own_2, one)),
        ("auxiliary cross CAR vanishes", close(car_cross, zeros)),
        ("double occupation is rank-one projection", rank(q12) == 1 and close(matmul(q12, q12), q12)),
        ("native projection has rank three", rank(p) == 3),
        ("compressed d1 creator is Hubbard B1", close(compressed[0], native[0])),
        ("compressed d2 creator is Hubbard B2", close(compressed[1], native[1])),
        ("native B1 own anticommutator is not identity", not close(add(matmul(native[0], dagger(native[0])), matmul(dagger(native[0]), native[0])), identity(3))),
        ("native B2 own anticommutator is not identity", not close(add(matmul(native[1], dagger(native[1])), matmul(dagger(native[1]), native[1])), identity(3))),
        ("native cross anticommutator is nonzero", not close(add(matmul(native[0], dagger(native[1])), matmul(dagger(native[1]), native[0])), [[0.0] * 3 for _ in range(3)])),
        ("finite penalty is positive", all(q12[i][i] >= 0.0 for i in range(4))),
        ("penalty forms increase exactly on double occupation", abs((9.0 - 4.0) * q12[3][3] - 5.0) < 1e-12),
        ("infinite penalty removes only double occupation", [q12[i][i] for i in range(4)] == [0.0, 0.0, 0.0, 1.0]),
        ("zero-mode weight is strictly between zero and one", 0.0 < z < 1.0),
        ("both one-flavor ground occupancies are positive", 0.0 < p_minus < p_plus < 1.0),
        ("ground occupancies sum to one", abs(p_minus + p_plus - 1.0) < 1e-12),
        ("all quadratic ground double-occupancy eigenvalues are positive", all(value > 0.0 for value in ground_q_eigs)),
        ("smallest ground double-occupancy eigenvalue is p-minus squared", abs(min(ground_q_eigs) - p_minus * p_minus) < 1e-12),
        ("quadratic ground misses native constraint", min(ground_q_eigs) > 0.0),
        ("ground-space angle bound is strict", 0.0 < angle_bound < 1.0),
        ("explicit native lower lift is positive", lower_lift > 0.0),
        ("particle one-escape shifts are q-minus-ei", particle_residuals == [(2, -2), (3, -3)]),
        ("hole one-escape shifts are q-plus-ei", hole_residuals == [(4, -2), (3, -1)]),
        ("particle and hole residual sets are disjoint in sample", set(particle_residuals).isdisjoint(hole_residuals)),
        ("rank-one leaf block has trace one-minus-p0", abs(sum(rank_one_leaf[i][i] for i in range(2)) - 0.6) < 1e-12),
        ("rank-one leaf gives native rank three", rank(gram_rank_three) == 3),
        ("rank-one leaf gives one dark signed channel", 4 - rank(gram_rank_three) == 1),
        ("rank-two leaf gives native rank four", rank(gram_rank_four) == 4),
        ("rank-two leaf has no dark signed channel", 4 - rank(gram_rank_four) == 0),
        ("SU2 leaf block is scalar", close(su2_leaf, scale(0.3, identity(2)))),
        ("SU2 nontrivial residual is full rank", rank(su2_gram) == 4),
        ("zero vacuum weight removes the two hole ranks", rank(threshold_gram(0.0, rank_two_leaf)) == 2),
        ("pure vacuum leaves exactly two hole ranks", rank(threshold_gram(1.0, [[0.0, 0.0], [0.0, 0.0]])) == 2),
        ("manifest contracts hold", not manifest_failures(data)),
        ("routing notice present", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose present", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects present", "```gu-typed-objects" in text),
        ("infinite-U scope present", "infinite-U" in text),
        ("operator-valued Feshbach boundary present", "operator-valued" in text and "F_0(z)" in text),
        ("strict ground bracket present", "2E_B <" in text and "E_hc <= E_B < 0" in text),
        ("native threshold formula present", "T_q^(1)" in text),
        ("native residual rank formula present", "rank D_phi=rank L_phi" in text),
        ("complete spectrum fence present", "not its complete charge decomposition" in text),
        ("next nonlinear solve present", "Solve the charge-restricted operator equation (7)" in text),
    ]
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text()
    baseline = exact_checks(data, text)
    failed = [name for name, ok in baseline if not ok]
    if failed:
        print(f"FAIL baseline: {failed}")
        return 1
    if not args.selftest:
        print(f"PASS {len(baseline)}/{len(baseline)} K148 exact controls")
        return 0
    mutations: list[tuple[str, callable]] = [
        ("promote C4 native", lambda d: d["infinite_u_realization"].__setitem__("finite_U_or_C4_is_native", True)),
        ("erase monotonicity", lambda d: d["infinite_u_realization"].__setitem__("penalty_forms_monotone", False)),
        ("erase strong limit", lambda d: d["infinite_u_realization"].__setitem__("strong_resolvent_limit", False)),
        ("wrong form domain", lambda d: d["infinite_u_realization"].__setitem__("limit_form_domain", "Dom(h_qf)")),
        ("scalarize self energy", lambda d: d["feshbach_boundary"].__setitem__("self_energy_acts_on_full_bath_Fock_space", False)),
        ("erase Pauli terms", lambda d: d["feshbach_boundary"].__setitem__("contains_occupation_dependent_Pauli_terms", False)),
        ("erase exchange", lambda d: d["feshbach_boundary"].__setitem__("contains_cross_flavor_exchange_terms", False)),
        ("invent bath commutation", lambda d: d["feshbach_boundary"].__setitem__("commutes_with_every_bath_occupation", True)),
        ("import K147 Schur", lambda d: d["feshbach_boundary"].__setitem__("reduces_to_K147_three_by_three_Schur_matrix", True)),
        ("claim complete spectrum", lambda d: d["feshbach_boundary"].__setitem__("complete_charge_sector_point_spectrum_solved", True)),
        ("erase strict lift", lambda d: d["ground_comparison"].__setitem__("strictly_above_unconstrained_ground", False)),
        ("wrong lower bound", lambda d: d["ground_comparison"].__setitem__("explicit_lower_bound", "E_hc>=2*E_B")),
        ("wrong upper bound", lambda d: d["ground_comparison"].__setitem__("upper_bound", "E_hc<=2*E_B")),
        ("erase ground", lambda d: d["ground_comparison"].__setitem__("native_point_spectrum_nonempty", False)),
        ("invent exact energy", lambda d: d["ground_comparison"].__setitem__("closed_form_E_hc_computed", True)),
        ("reverse particle shift", lambda d: d["charge_thresholds"].__setitem__("particle_escape_shift", "residual q+e_i")),
        ("reverse hole shift", lambda d: d["charge_thresholds"].__setitem__("hole_escape_shift", "residual q-e_i")),
        ("import projected zeros", lambda d: d["charge_thresholds"].__setitem__("projected_K147_zero_labels_are_residual_energies", True)),
        ("invent numerical thresholds", lambda d: d["charge_thresholds"].__setitem__("numerical_thresholds_computed", True)),
        ("wrong leaf trace", lambda d: d["residual_density_rank"].__setitem__("leaf_gram_trace", "p_0")),
        ("wrong rank formula", lambda d: d["residual_density_rank"].__setitem__("rank_formula", "rank(D_phi)=3")),
        ("import universal rank", lambda d: d["residual_density_rank"].__setitem__("universal_projected_rank_three_imported", True)),
        ("erase degenerate form factors", lambda d: d["residual_density_rank"].__setitem__("degenerate_residual_spaces_require_full_form_factor_matrix", False)),
        ("invent full Mourre", lambda d: d["boundaries"].__setitem__("native_full_Fock_Mourre_or_scattering", True)),
        ("invent NESS", lambda d: d["boundaries"].__setitem__("NESS_or_current", True)),
        ("invent source", lambda d: d["boundaries"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent Born", lambda d: d["boundaries"].__setitem__("Born_rule_derived", True)),
        ("promote canon", lambda d: d["boundaries"].__setitem__("canon_verdict_change", "changed")),
        ("publish", lambda d: d["boundaries"].__setitem__("paper_release_or_public_posture_change", "released")),
        ("erase ceiling", lambda d: d.__setitem__("claim_ceiling", "The physical GU spectrum is solved.")),
    ]
    caught = 0
    missed: list[str] = []
    for name, mutate in mutations:
        trial = copy.deepcopy(data)
        mutate(trial)
        if any(not ok for _, ok in exact_checks(trial, text)):
            caught += 1
        else:
            missed.append(name)
    prose_mutations = [
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING", 1),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", "", 1),
        text.replace("```gu-typed-objects", "```text", 1),
        text.replace("infinite-U", "hard constraint"),
        text.replace("operator-valued", "scalar"),
        text.replace("T_q^(1)", "threshold set", 1),
        text.replace("Solve the charge-restricted operator equation (7)", "Continue later", 1),
    ]
    for index, trial_text in enumerate(prose_mutations, start=1):
        if any(not ok for _, ok in exact_checks(data, trial_text)):
            caught += 1
        else:
            missed.append(f"prose_{index}")
    total = len(mutations) + len(prose_mutations)
    if caught != total:
        print(f"FAIL hostile selftest caught {caught}/{total}: missed {missed}")
        return 1
    print(f"PASS hostile selftest caught {caught}/{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
