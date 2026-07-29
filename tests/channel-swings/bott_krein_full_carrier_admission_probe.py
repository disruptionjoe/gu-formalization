#!/usr/bin/env python3
"""Bounded admission gate for a full-carrier Bott--Krein weld.

This probe keeps four objects separate:

* the program-native antilinear Krein duality C_perp = K J_obs;
* the program-native quaternionic reality J_H on the Cl(9,5) spinor;
* their proposed linear deck product S_nat = C_perp J_H;
* the standard doubled H-line Bott control.

It checks finite matrix algebra, gamma-trace-kernel preservation, the standard
Bott control gap, and direct-sum multiplicity.  It does NOT compute a Callias,
Fredholm, quaternionic, complex, or physical chiral index.
"""

from __future__ import annotations

from itertools import permutations
import json

import numpy as np


TOL = 1.0e-9
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def kron_all(factors: list[np.ndarray]) -> np.ndarray:
    out = np.array([[1.0 + 0.0j]])
    for factor in factors:
        out = np.kron(out, factor)
    return out


def euclidean_jw_gammas(n_pairs: int) -> list[np.ndarray]:
    identity = np.eye(2, dtype=complex)
    sigma_1 = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)
    gammas: list[np.ndarray] = []
    for index in range(n_pairs):
        left = [sigma_3] * index
        right = [identity] * (n_pairs - 1 - index)
        gammas.append(kron_all(left + [sigma_1] + right))
        gammas.append(kron_all(left + [sigma_2] + right))
    return gammas


def signed_gammas(positive: int, negative: int) -> tuple[list[np.ndarray], np.ndarray]:
    euclidean = euclidean_jw_gammas((positive + negative) // 2)
    metric = np.array([1.0] * positive + [-1.0] * negative)
    gammas = [
        euclidean[index] if metric[index] > 0 else 1j * euclidean[index]
        for index in range(positive + negative)
    ]
    return gammas, metric


def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    out = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        out = out @ matrix
    return out


def normalized_chirality(gammas: list[np.ndarray]) -> np.ndarray:
    omega = matrix_product(gammas)
    scalar = complex(np.trace(omega @ omega) / omega.shape[0])
    if abs(scalar - 1.0) < TOL:
        return omega
    if abs(scalar + 1.0) < TOL:
        return 1j * omega
    raise AssertionError(f"chirality square is not scalar +/-1: {scalar}")


def real_gamma_product(gammas: list[np.ndarray]) -> np.ndarray:
    """Normalized product of the real matrices in a signed JW realization."""
    real_gammas = [
        gamma for gamma in gammas if max_abs(gamma.conj() - gamma) < TOL
    ]
    unitary_part = matrix_product(real_gammas)
    norm_square = unitary_part @ unitary_part.conj().T
    scale = float(np.max(np.abs(np.diag(norm_square))))
    return unitary_part / np.sqrt(scale)


def antilinear_image(unitary_part: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    """Conjugation of a linear map by the antilinear map U o conjugation."""
    return unitary_part @ matrix.conj() @ np.linalg.inv(unitary_part)


def right_h_linearity_defect(linear: np.ndarray, j_h: np.ndarray) -> float:
    """The nontrivial right-H condition for complex-linear S.

    Right multiplication by j is represented by J_H = j_h o conjugation, so
    S is right-H-linear iff S j_h = j_h conjugate(S).
    """
    return max_abs(linear @ j_h - j_h @ linear.conj())


def left_quaternion(q: tuple[float, float, float, float]) -> np.ndarray:
    a, b, c, d = q
    return np.array(
        (
            (a, -b, -c, -d),
            (b, a, -d, c),
            (c, d, a, -b),
            (d, -c, b, a),
        ),
        dtype=float,
    )


RIGHT_I = np.array(
    ((0, -1, 0, 0), (1, 0, 0, 0), (0, 0, 0, 1), (0, 0, -1, 0)),
    dtype=float,
)
RIGHT_J = np.array(
    ((0, 0, -1, 0), (0, 0, 0, -1), (1, 0, 0, 0), (0, 1, 0, 0)),
    dtype=float,
)
RIGHT_K = np.array(
    ((0, 0, 0, -1), (0, 0, 1, 0), (0, -1, 0, 0), (1, 0, 0, 0)),
    dtype=float,
)


def bott_involution(q: tuple[float, float, float, float]) -> np.ndarray:
    left = left_quaternion(q)
    zero = np.zeros((4, 4))
    return np.block([[zero, left.T], [left, zero]])


def alternating_trace_three(
    first: np.ndarray, second: np.ndarray, third: np.ndarray
) -> int:
    matrices = (first, second, third)
    total = 0
    for order in permutations(range(3)):
        inversions = sum(
            order[left] > order[right]
            for left in range(3)
            for right in range(left + 1, 3)
        )
        sign = -1 if inversions % 2 else 1
        total += sign * int(round(float(np.trace(
            matrices[order[0]] @ matrices[order[1]] @ matrices[order[2]]
        ))))
    return total


def main() -> None:
    print("=" * 88)
    print("A. Program-native C_perp, J_H, and S_nat")
    print("=" * 88)

    gamma_4, eta_4 = signed_gammas(3, 1)
    gamma_10, eta_10 = signed_gammas(6, 4)
    omega_4 = normalized_chirality(gamma_4)
    gamma_14 = (
        [np.kron(gamma, np.eye(32)) for gamma in gamma_4]
        + [np.kron(omega_4, gamma) for gamma in gamma_10]
    )
    eta_14 = np.concatenate((eta_4, eta_10))
    identity_128 = np.eye(128, dtype=complex)

    krein = matrix_product(
        [gamma for gamma, sign in zip(gamma_14, eta_14) if sign > 0]
    )
    j_obs = np.kron(real_gamma_product(gamma_4), real_gamma_product(gamma_10))
    c_perp = krein @ j_obs

    # The raw full-product reality anticommutes with every full gamma in this
    # realization.  Multiplication by full chirality gives the quaternionic
    # reality commuting with Cl(9,5), with square -1.
    j_h = normalized_chirality(gamma_14) @ real_gamma_product(gamma_14)

    check(
        "J_H is quaternionic: J_H^2=-1",
        max_abs(j_h @ j_h.conj() + identity_128) < TOL,
    )
    check(
        "J_H commutes antilinearly with all 14 Clifford generators",
        max(max_abs(antilinear_image(j_h, gamma) - gamma) for gamma in gamma_14)
        < TOL,
    )
    check(
        "C_perp is an antilinear involution",
        max_abs(c_perp @ c_perp.conj() - identity_128) < TOL,
    )

    s_nat = c_perp @ j_h.conj()
    check("S_nat is complex-linear and S_nat^2=+1", max_abs(s_nat @ s_nat - identity_128) < TOL)
    check(
        "S_nat is Krein-unitary",
        max_abs(s_nat.conj().T @ krein @ s_nat - krein) < TOL,
    )
    plus_dimension = 128 - int(np.linalg.matrix_rank(s_nat - identity_128, tol=TOL))
    minus_dimension = 128 - int(np.linalg.matrix_rank(s_nat + identity_128, tol=TOL))
    check(
        "S_nat has a balanced complex 64+64 eigensplitting",
        (plus_dimension, minus_dimension) == (64, 64),
        f"{plus_dimension}+{minus_dimension}",
    )

    h_linearity_defect = right_h_linearity_defect(s_nat, j_h)
    h_antilinearity_defect = max_abs(s_nat @ j_h + j_h @ s_nat.conj())
    check(
        "preregistered hostile gate fires: S_nat is NOT right-H-linear",
        h_linearity_defect > 1.0 and h_antilinearity_defect < TOL,
        f"linearity defect {h_linearity_defect:.1f}",
    )

    # Planted phase control.  Multiplication by i repairs H-linearity but
    # changes the square to -1.  It cannot be used as a Z/2 deck involution.
    phased_s_nat = 1j * s_nat
    check(
        "planted i-phase swaps the defect: H-linear but square -1",
        right_h_linearity_defect(phased_s_nat, j_h) < TOL
        and max_abs(phased_s_nat @ phased_s_nat + identity_128) < TOL,
    )
    simultaneous_deck_and_h_linear = (
        max_abs(s_nat @ s_nat - identity_128) < TOL
        and h_linearity_defect < TOL
    ) or (
        max_abs(phased_s_nat @ phased_s_nat - identity_128) < TOL
        and right_h_linearity_defect(phased_s_nat, j_h) < TOL
    )
    check(
        "no allowed normalization passes both involution and right-H gates",
        not simultaneous_deck_and_h_linear,
    )

    # Although it fails the H-linear deck gate, S_nat is a genuine Clifford
    # reflection.  Its induced vector action therefore preserves ker Gamma.
    vector_signs: list[int] = []
    for gamma in gamma_14:
        transformed = s_nat @ gamma @ s_nat
        if max_abs(transformed - gamma) < TOL:
            vector_signs.append(1)
        elif max_abs(transformed + gamma) < TOL:
            vector_signs.append(-1)
        else:
            vector_signs.append(0)
    gamma_intertwiner_defect = max(
        max_abs(sign * gamma @ s_nat - s_nat @ gamma)
        for sign, gamma in zip(vector_signs, gamma_14)
    )
    check(
        "S_nat induces a signed O(9,5) vector action",
        0 not in vector_signs and set(vector_signs) == {-1, 1},
        str(vector_signs),
    )
    check(
        "the induced vector-spinor action preserves ker Gamma",
        gamma_intertwiner_defect < TOL,
        f"Gamma T - S Gamma defect {gamma_intertwiner_defect:.1e}",
    )

    print("\n" + "=" * 88)
    print("B. Standard doubled H-line Bott control")
    print("=" * 88)

    q = (0.5, 0.5, 0.5, 0.5)
    minus_q = tuple(-entry for entry in q)
    bott_mass = bott_involution(q)
    minus_mass = bott_involution(minus_q)
    deck_control = np.diag([1.0] * 4 + [-1.0] * 4)
    doubled_right_actions = [
        np.kron(np.eye(2), action) for action in (RIGHT_I, RIGHT_J, RIGHT_K)
    ]
    bott_gap = float(np.min(np.linalg.svd(bott_mass, compute_uv=False)))

    check(
        "standard Bott mass is self-adjoint and squares to one",
        max_abs(bott_mass.T - bott_mass) < TOL
        and max_abs(bott_mass @ bott_mass - np.eye(8)) < TOL,
    )
    check(
        "standard linear deck grading is a right-H-linear involution",
        max_abs(deck_control @ deck_control - np.eye(8)) < TOL
        and max(max_abs(deck_control @ action - action @ deck_control)
                for action in doubled_right_actions) < TOL,
    )
    check(
        "standard deck grading sends M(q) to M(-q)",
        max_abs(deck_control @ bott_mass @ deck_control - minus_mass) < TOL,
    )
    check(
        "standard Bott mass commutes with the right-H action",
        max(max_abs(bott_mass @ action - action @ bott_mass)
            for action in doubled_right_actions) < TOL,
    )
    check("standard finite mass gap is one", abs(bott_gap - 1.0) < TOL, f"{bott_gap:.1f}")

    print("\n" + "=" * 88)
    print("C. H-line versus full H^64 direct-sum multiplicity")
    print("=" * 88)

    left_i = left_quaternion((0.0, 1.0, 0.0, 0.0)).astype(int)
    left_j = left_quaternion((0.0, 0.0, 1.0, 0.0)).astype(int)
    left_k = left_quaternion((0.0, 0.0, 0.0, 1.0)).astype(int)
    one_line_density = alternating_trace_three(left_i, left_j, left_k)

    identity_64 = np.eye(64, dtype=int)
    full_generators = [
        np.kron(identity_64, generator)
        for generator in (left_i, left_j, left_k)
    ]
    full_density = alternating_trace_three(*full_generators)
    density_ratio = full_density // one_line_density
    check(
        "natural diagonal H^64 lift has exactly 64 copies of the H-line density",
        one_line_density != 0 and density_ratio == 64,
        f"{full_density}/{one_line_density}={density_ratio}",
    )

    # Planted coordinate selection: it returns the desired single-copy
    # density, but a single carrier permutation already breaks its naturality.
    selected_line = np.zeros((64, 64), dtype=int)
    selected_line[0, 0] = 1
    selected_generators = [
        np.kron(selected_line, generator)
        for generator in (left_i, left_j, left_k)
    ]
    selected_density = alternating_trace_three(*selected_generators)
    swap = np.eye(64, dtype=int)
    swap[0, 0] = 0
    swap[1, 1] = 0
    swap[0, 1] = 1
    swap[1, 0] = 1
    selection_naturality_defect = max_abs(selected_line @ swap - swap @ selected_line)
    check(
        "planted one-line selector is detected as non-natural",
        selected_density == one_line_density and selection_naturality_defect > 0.5,
        f"density ratio 1, commutator {selection_naturality_defect:.1f}",
    )
    check(
        "full-carrier identity passes the planted naturality comparator",
        max_abs(identity_64 @ swap - swap @ identity_64) < TOL,
    )

    physical_index_computed = False
    clifford_morita_map_constructed = False
    native_bott_mirror_embedding_constructed = False
    native_bott_mass_rs_gap_test_expressible = False
    check(
        "no clutching multiplicity is misreported as a physical index",
        not physical_index_computed,
    )

    receipt = {
        "clifford_morita_map_constructed": clifford_morita_map_constructed,
        "c_perp_square": 1,
        "h_line_local_cubic_density": one_line_density,
        "h64_direct_sum_copy_count": density_ratio,
        "h64_local_cubic_density": full_density,
        "j_h_square": -1,
        "native_bott_mass_rs_gap_test_expressible": native_bott_mass_rs_gap_test_expressible,
        "native_bott_mirror_embedding_constructed": native_bott_mirror_embedding_constructed,
        "physical_index_computed": physical_index_computed,
        "planted_single_line_naturality_defect": selection_naturality_defect,
        "s_nat_eigenspace_dimensions_complex": [plus_dimension, minus_dimension],
        "s_nat_preserves_gamma_trace_kernel": gamma_intertwiner_defect < TOL,
        "s_nat_right_h_linear": h_linearity_defect < TOL,
        "s_nat_square": 1,
        "standard_bott_control_gap": bott_gap,
        "standard_bott_control_pass": True,
        "triplet_direct_sum_copy_count_if_tensored": 3 * density_ratio,
        "verdict": (
            "KILL-S_NAT-H-LINEAR-DECK;"
            "FULL-CARRIER-BOTT-OPEN-AT-NATIVE-MIRROR-AND-MORITA-MAP"
        ),
    }
    print("\n" + json.dumps(receipt, indent=2, sort_keys=True))

    if FAILURES:
        print(f"\nCONTROLS FAILED: {FAILURES}")
        raise SystemExit(1)
    print("\nBOTT--KREIN FULL-CARRIER ADMISSION PROBE: ALL CONTROLS PASS")


if __name__ == "__main__":
    main()
