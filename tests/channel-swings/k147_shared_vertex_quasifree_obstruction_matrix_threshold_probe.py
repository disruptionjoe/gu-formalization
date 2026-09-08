#!/usr/bin/env python3
"""Exact/hostile checks for the K147 shared-vertex boundary wave."""

from __future__ import annotations

import argparse
import copy
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k147-shared-vertex-quasifree-obstruction-matrix-threshold-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k147-shared-vertex-quasifree-obstruction-matrix-threshold-wave-2026-09-08.md"


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def add(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def rank(a: list[list[float]], tol: float = 1e-12) -> int:
    work = [row[:] for row in a]
    rows, cols = len(work), len(work[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if abs(work[r][col]) > tol), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [x / scale for x in work[pivot_row]]
        for r in range(rows):
            if r == pivot_row:
                continue
            scale = work[r][col]
            work[r] = [x - scale * y for x, y in zip(work[r], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def close_matrix(a: list[list[float]], b: list[list[float]], tol: float = 1e-12) -> bool:
    return len(a) == len(b) and all(
        len(ar) == len(br) and all(abs(x - y) < tol for x, y in zip(ar, br))
        for ar, br in zip(a, b)
    )


def matvec(a: list[list[float]], x: list[float]) -> list[float]:
    return [sum(v * w for v, w in zip(row, x)) for row in a]


def trapz(values: list[float], step: float) -> float:
    return step * (sum(values) - (values[0] + values[-1]) / 2)


def integral(fun, cutoff: float = 60.0, n: int = 120000) -> float:
    step = 2 * cutoff / n
    vals = [fun(-cutoff + j * step) for j in range(n + 1)]
    return trapz(vals, step) / (2 * math.pi)


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    # Klein factors multiply the nonzero cross products by a unitary; the
    # impurity matrix-unit calculation already decides whether they vanish.
    b1 = [[0, 0, 0], [1, 0, 0], [0, 0, 0]]
    b2 = [[0, 0, 0], [0, 0, 0], [1, 0, 0]]
    z3 = [[0, 0, 0] for _ in range(3)]
    i3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    own1 = add(matmul(b1, transpose(b1)), matmul(transpose(b1), b1))
    own2 = add(matmul(b2, transpose(b2)), matmul(transpose(b2), b2))
    cross12 = add(matmul(b1, transpose(b2)), matmul(transpose(b2), b1))
    gamma = [[1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
    gram = matmul(gamma, transpose(gamma))
    kernel = [1, 0, -1, 0]
    eps = lambda p: math.sqrt(1 + p * p) + 0.25
    i2 = integral(lambda p: 1 / eps(p) ** 2)
    z2, z1 = 1 / (1 + 2 * i2), 1 / (1 + i2)
    gap_samples = [-2.0, -0.7, -0.2, 0.2, 0.7, 1.1]
    schur_factors = {
        degree: [
            1 + degree * integral(lambda p, z=z: 1 / (eps(p) * (eps(p) - z)))
            for z in gap_samples
        ]
        for degree in (1, 2)
    }
    pauli_ranks = []
    pauli_eigenvalues = []
    diag = [z2, z1, z1]
    for blocked in range(3):
        compressed = [[diag[i] if i == j and i != blocked else 0 for j in range(3)] for i in range(3)]
        pauli_ranks.append(rank(compressed))
        pauli_eigenvalues.append([diag[i] for i in range(3) if i != blocked])
    native = data["native_shared_vertex_algebra"]
    projected = data["projected_matrix_boundary"]
    pauli = data["pauli_thresholds"]
    rel = data["relative_comparison_and_conjugate"]
    bounds = data["boundaries"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("classification", data["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", data["direction"] == "observed_to_native"),
        ("two edges", data["fixed_control"]["oriented_edges"] == [[0, 1], [0, 2]]),
        ("shared vertex", data["fixed_control"]["shared_vertex"] == 0),
        ("equal couplings", data["fixed_control"]["equal_real_couplings"] is True),
        ("not full rook", data["fixed_control"]["complete_rook_graph"] is False),
        ("B1 nilpotent", close_matrix(matmul(b1, b1), z3)),
        ("B2 nilpotent", close_matrix(matmul(b2, b2), z3)),
        ("own anticommutator 1 not identity", not close_matrix(own1, i3)),
        ("own anticommutator 2 not identity", not close_matrix(own2, i3)),
        ("cross anticommutator nonzero", not close_matrix(cross12, z3)),
        ("manifest cross CAR", native["cross_anticommutator_zero"] is False),
        ("no two-mode CAR", native["two_mode_CAR_representation"] is False),
        ("no collective repair", native["single_collective_mode_covers_both_edges"] is False),
        ("native nonquasifree", native["native_full_signed_corner_is_quadratic_quasifree"] is False),
        ("K146 lift blocked", native["K146_Bogoliubov_lift_to_native_corner"] is False),
        ("projection noninvariant", projected["projection_invariant_under_native_full_signed_Fock_Hamiltonian"] is False),
        ("projected carrier", projected["carrier"] == "C3 direct-sum L2(R;C4)"),
        ("endpoint gram exact", close_matrix(gram, [[2, 0, 0], [0, 1, 0], [0, 0, 1]])),
        ("endpoint rank", rank(gamma) == 3 and projected["endpoint_rank"] == 3),
        ("kernel vector", matvec(gamma, kernel) == [0, 0, 0]),
        ("kernel nullity", len(gamma[0]) - rank(gamma) == 1 and projected["channel_kernel_dimension"] == 1),
        ("threshold", projected["threshold"] == "5/4"),
        ("schur matrix", projected["schur_matrix"] == "S(z)=-z I3-M(z)D"),
        ("positive degree-one factors", min(schur_factors[1]) > 1),
        ("positive degree-two factors", min(schur_factors[2]) > 1),
        ("zero multiplicity", projected["gap_point_spectrum"] == "{0}" and projected["zero_mode_multiplicity"] == 3),
        ("no other gap", projected["other_gap_eigenvalues"] is False),
        ("no embedded", projected["embedded_eigenvalues"] is False),
        ("no singular continuous", projected["singular_continuous_spectrum"] is False),
        ("continuum multiplicity", projected["absolutely_continuous_spectrum"] == "[5/4,infinity) with multiplicity 8"),
        ("weights ordered", 0 < z2 < z1 < 1),
        ("weight labels", projected["zero_mode_impurity_weights"] == ["Z_2=(1+2 I_2)^-1", "Z_1=(1+I_2)^-1", "Z_1=(1+I_2)^-1"]),
        ("vacuum D", pauli["vacuum_D_tau"] == "diag(Z_2,Z_1,Z_1)"),
        ("vacuum rank", pauli["vacuum_rank"] == 3),
        ("vacuum kernel", pauli["vacuum_channel_kernel_dimension"] == 1),
        ("vacuum no dark", pauli["vacuum_dark_impurity_dimension"] == 0),
        ("all residual labels", pauli["residual_zero_labels"] == [0, 1, 2]),
        ("computed residual ranks", pauli_ranks == [2, 2, 2]),
        ("manifest residual ranks", pauli["every_single_residual_rank"] == 2),
        ("central residual eigenvalues", pauli["residual_0_D_tau_nonzero_eigenvalues"] == ["Z_1", "Z_1"] and abs(pauli_eigenvalues[0][0] - z1) < 1e-12),
        ("leaf one residual eigenvalues", pauli["residual_1_D_tau_nonzero_eigenvalues"] == ["Z_2", "Z_1"] and pauli_eigenvalues[1] == [z2, z1]),
        ("leaf two residual eigenvalues", pauli["residual_2_D_tau_nonzero_eigenvalues"] == ["Z_2", "Z_1"] and pauli_eigenvalues[2] == [z2, z1]),
        ("residual channel kernels", pauli["every_single_residual_channel_kernel_dimension"] == 2),
        ("allowed no dark", pauli["every_allowed_compressed_dark_dimension"] == 0),
        ("blocked not dark", pauli["Pauli_blocked_direction_is_dark"] is False),
        ("no native double occupation", pauli["native_double_zero_mode_occupation_available"] is False),
        ("no full Fock threshold census", pauli["full_Fock_bound_residual_threshold_census_claimed"] is False),
        ("projected relative HS", rel["self_dual_double_of_projected_boundary_has_Hilbert_Schmidt_relative_polarization"] is True),
        ("artificial implementer", rel["artificial_exterior_Fock_relative_transform_implementable"] is True),
        ("implementer native fence", rel["implements_native_shared_corner_Hamiltonian"] is False),
        ("projected C11", rel["projected_boundary_C11"] is True),
        ("corner Mourre", rel["corner_strict_Mourre_away_from_zero_and_threshold"] is True),
        ("corner LAP", rel["corner_weighted_LAP_s_greater_than_half"] is True),
        ("degree norm", rel["endpoint_norm_squared"] == 2 and rel["endpoint_norm_squared_equals_max_degree"] is True),
        ("rook degree bound", rel["rook_subgraph_maximum_endpoint_degree"] == 4),
        ("projected uniform C11", rel["projected_C11_seminorm_degree_uniform_for_rook_subgraphs"] is True),
        ("strict constant fence", rel["rook_cycle_uniform_strict_Mourre_constant"] is False),
        ("native Mourre fence", rel["native_full_Fock_C11_or_Mourre"] is False),
        ("native spectrum fence", bounds["native_shared_corner_point_spectrum_solved"] is False),
        ("native pauli fence", bounds["native_shared_corner_Pauli_thresholds_solved"] is False),
        ("full rook fence", bounds["complete_rook_full_Fock_solved"] is False),
        ("scattering fence", bounds["many_body_asymptotic_completeness"] is False),
        ("NESS fence", bounds["NESS_or_current"] is False),
        ("source fence", bounds["Weinstein_source_or_GU_action_owner"] is False),
        ("Born fence", bounds["Born_rule_derived"] is False),
        ("prediction fence", bounds["prediction_or_confirmation_credit"] is False),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("hard-core scope", "hard-core" in text),
        ("next interacting route", "charge-sector Feshbach" in text),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text()
    baseline = checks(data, text)
    failed = [name for name, ok in baseline if not ok]
    if failed:
        print(f"FAIL baseline: {failed}")
        return 1
    if not args.selftest:
        print(f"PASS {len(baseline)}/{len(baseline)} K147 exact controls")
        return 0
    mutations: list[tuple[str, callable]] = [
        ("cross CAR", lambda d: d["native_shared_vertex_algebra"].__setitem__("cross_anticommutator_zero", True)),
        ("two-mode CAR", lambda d: d["native_shared_vertex_algebra"].__setitem__("two_mode_CAR_representation", True)),
        ("quasifree", lambda d: d["native_shared_vertex_algebra"].__setitem__("native_full_signed_corner_is_quadratic_quasifree", True)),
        ("projection invariant", lambda d: d["projected_matrix_boundary"].__setitem__("projection_invariant_under_native_full_signed_Fock_Hamiltonian", True)),
        ("endpoint rank", lambda d: d["projected_matrix_boundary"].__setitem__("endpoint_rank", 2)),
        ("kernel", lambda d: d["projected_matrix_boundary"].__setitem__("channel_kernel_dimension", 0)),
        ("zero multiplicity", lambda d: d["projected_matrix_boundary"].__setitem__("zero_mode_multiplicity", 2)),
        ("continuum multiplicity", lambda d: d["projected_matrix_boundary"].__setitem__("absolutely_continuous_spectrum", "[5/4,infinity) with multiplicity 4")),
        ("vacuum rank", lambda d: d["pauli_thresholds"].__setitem__("vacuum_rank", 2)),
        ("residual rank", lambda d: d["pauli_thresholds"].__setitem__("every_single_residual_rank", 1)),
        ("blocked dark", lambda d: d["pauli_thresholds"].__setitem__("Pauli_blocked_direction_is_dark", True)),
        ("double occupation", lambda d: d["pauli_thresholds"].__setitem__("native_double_zero_mode_occupation_available", True)),
        ("native implementer", lambda d: d["relative_comparison_and_conjugate"].__setitem__("implements_native_shared_corner_Hamiltonian", True)),
        ("degree norm", lambda d: d["relative_comparison_and_conjugate"].__setitem__("endpoint_norm_squared", 4)),
        ("strict uniform", lambda d: d["relative_comparison_and_conjugate"].__setitem__("rook_cycle_uniform_strict_Mourre_constant", True)),
        ("native spectrum", lambda d: d["boundaries"].__setitem__("native_shared_corner_point_spectrum_solved", True)),
        ("source", lambda d: d["boundaries"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
    ]
    caught = 0
    for _, mutate in mutations:
        trial = copy.deepcopy(data)
        mutate(trial)
        if any(not ok for _, ok in checks(trial, text)):
            caught += 1
    prose_mutations = [
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING", 1),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", "", 1),
        text.replace("```gu-typed-objects", "```text", 1),
        text.replace("hard-core", "constrained"),
        text.replace("charge-sector Feshbach", "future method", 1),
    ]
    for trial_text in prose_mutations:
        if any(not ok for _, ok in checks(data, trial_text)):
            caught += 1
    total = len(mutations) + len(prose_mutations)
    if caught != total:
        print(f"FAIL hostile selftest caught {caught}/{total}")
        return 1
    print(f"PASS hostile selftest caught {caught}/{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
