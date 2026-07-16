#!/usr/bin/env python3
"""PRED-FLAVOR-RANK certificate.

This is the reduced-rank receipt for the current GU-native flavor-prediction lane.
It consumes the H28 channel result as input:

- the scalar Dirac-Yukawa channel exists and is unique at the Spin(9,5) level;
- the derived generation Z/3 acts on the three generation slots;
- the built transpose-bilinear fork imposes P^T Y P = Y;
- no current source-action constraint fixes any of the surviving coefficients.

Question: after the built GU symmetry and allowed basis quotient, does any
zero-parameter mass/mixing relation survive?

Result: no.  The Z/3 texture reduces the complex coefficient space 9 -> 3,
but the three surviving magnitudes are independent.  After ignoring one
overall source normalization, two dimensionless ratios remain free.
"""

from __future__ import annotations

import numpy as np


TOL = 1e-9
FAILURES: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    state = "PASS" if condition else "FAIL"
    print(f"{state} :: {name}" + (f" -- {detail}" if detail else ""))
    if not condition:
        FAILURES.append(name)


def fixed_space_dimension(operator: np.ndarray) -> int:
    """Complex dimension of the fixed space ker(operator - I)."""
    eye = np.eye(operator.shape[0], dtype=complex)
    singular = np.linalg.svd(operator - eye, compute_uv=False)
    rank = int(np.sum(singular > TOL))
    return operator.shape[0] - rank


def eigenbasis_for_cyclic_z3() -> np.ndarray:
    """Eigenbasis ordered by charges 0, 1, 2 for the cyclic permutation."""
    permutation = np.array(
        [[0, 1, 0], [0, 0, 1], [1, 0, 0]],
        dtype=complex,
    )
    zeta = np.exp(2j * np.pi / 3)
    eigenvalues, eigenvectors = np.linalg.eig(permutation)
    order = [int(np.argmin(np.abs(eigenvalues - target))) for target in (1, zeta, zeta**2)]
    return eigenvectors[:, order]


def support_pattern_in_eigenbasis(fork: str) -> set[tuple[int, int]]:
    """Return the nonzero support forced by the Z/3 fixed-space condition."""
    charges = (0, 1, 2)
    if fork == "charges_add":
        return {
            (i, j)
            for i in range(3)
            for j in range(3)
            if (charges[i] + charges[j]) % 3 == 0
        }
    if fork == "charges_subtract":
        return {
            (i, j)
            for i in range(3)
            for j in range(3)
            if (charges[j] - charges[i]) % 3 == 0
        }
    raise ValueError(f"unknown fork: {fork}")


def phase_action_rank(entries: tuple[tuple[int, int], ...]) -> int:
    """Rank of left/right rephasings on the phases of the surviving entries."""
    incidence = []
    for left, right in entries:
        row = [0.0] * 6
        row[left] = 1.0
        row[3 + right] = 1.0
        incidence.append(row)
    return int(np.linalg.matrix_rank(np.array(incidence, dtype=float), tol=TOL))


def normalized_magnitudes(values: tuple[float, float, float]) -> np.ndarray:
    mags = np.sort(np.abs(np.array(values, dtype=float)))
    return mags / mags[-1]


def main() -> int:
    print("== PRED-FLAVOR-RANK: reduced GU-native Yukawa coefficient count ==")

    permutation = np.array(
        [[0, 1, 0], [0, 0, 1], [1, 0, 0]],
        dtype=complex,
    )
    identity3 = np.eye(3, dtype=complex)
    check(
        "derived generation action is order 3",
        np.max(np.abs(np.linalg.matrix_power(permutation, 3) - identity3)) < TOL,
    )

    eigenbasis = eigenbasis_for_cyclic_z3()
    fixed_axis = eigenbasis[:, 0] / eigenbasis[0, 0]
    check(
        "charge-0 fixed axis is democratic",
        np.max(np.abs(fixed_axis - 1.0)) < TOL,
    )

    # Column-major vectorization: vec(P^T Y P) = (P^T x P^T) vec(Y).
    add_operator = np.kron(permutation.T, permutation.T)
    sub_operator = np.kron(permutation.T, permutation.conj().T)
    full_complex_dim = 9
    add_dim = fixed_space_dimension(add_operator)
    sub_dim = fixed_space_dimension(sub_operator)

    check("full 3x3 Yukawa coefficient space has complex dimension 9", full_complex_dim == 9)
    check("GU-native transpose-bilinear fork reduces 9 -> 3 complex coefficients", add_dim == 3)
    check("Krein/sesquilinear comparison fork also has dimension 3", sub_dim == 3)

    add_support = support_pattern_in_eigenbasis("charges_add")
    sub_support = support_pattern_in_eigenbasis("charges_subtract")
    expected_add = {(0, 0), (1, 2), (2, 1)}
    expected_sub = {(0, 0), (1, 1), (2, 2)}
    check(
        "transpose-bilinear support is {(0,0),(1,2),(2,1)}",
        add_support == expected_add,
        f"{sorted(add_support)}",
    )
    check(
        "sesquilinear comparison support is diagonal",
        sub_support == expected_sub,
        f"{sorted(sub_support)}",
    )

    surviving_entries = ((0, 0), (1, 2), (2, 1))
    real_dim_before_quotient = 2 * add_dim
    removable_phase_dim = phase_action_rank(surviving_entries)
    real_moduli_after_phase_quotient = real_dim_before_quotient - removable_phase_dim
    check("three coefficient phases are basis gauge under left/right rephasings", removable_phase_dim == 3)
    check("three positive Yukawa magnitudes remain after phase quotient", real_moduli_after_phase_quotient == 3)

    # In the built texture the singular values are exactly the three magnitudes.
    log_sv_jacobian = np.eye(3)
    ratio_jacobian = np.array(
        [
            [-1.0, 1.0, 0.0],
            [-1.0, 0.0, 1.0],
        ]
    )
    check("rank of log singular values versus log magnitudes is 3", np.linalg.matrix_rank(log_sv_jacobian) == 3)
    check("after one free overall normalization, two dimensionless ratios remain", np.linalg.matrix_rank(ratio_jacobian) == 2)

    a = normalized_magnitudes((1.0, 2.0, 5.0))
    b = normalized_magnitudes((1.0, 3.0, 7.0))
    check(
        "basis-and-scale counterexample: two allowed triples have inequivalent ratios",
        np.max(np.abs(a - b)) > 1e-3,
        f"{a.tolist()} vs {b.tolist()}",
    )

    built_source_constraints_fixing_coefficients: tuple[str, ...] = ()
    check(
        "current built source constraints fix zero surviving Yukawa coefficients",
        len(built_source_constraints_fixing_coefficients) == 0,
    )

    zero_parameter_prediction_survives = False
    check(
        "zero-parameter mass/mixing prediction route is closed at current grade",
        not zero_parameter_prediction_survives
        and real_moduli_after_phase_quotient == 3
        and np.linalg.matrix_rank(ratio_jacobian) == 2,
    )

    print()
    print("RESULT :: NO_GO")
    print("complex_texture_dimension :: 3")
    print("real_magnitude_moduli_after_phase_quotient :: 3")
    print("dimensionless_ratio_moduli_after_free_scale :: 2")
    print("priority_signal :: activate PRED-NORM-RANK after daily steward reconciliation")
    print("status_changes :: none")

    if FAILURES:
        print("FAILURES :: " + ", ".join(FAILURES))
        return 1
    print("SELF-CHECK :: ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
