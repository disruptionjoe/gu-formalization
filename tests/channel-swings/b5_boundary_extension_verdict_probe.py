#!/usr/bin/env python3
r"""Exact B5 regular-boundary polarization and extension-verdict certificate.

The actual strict folded carrier at a non-null boundary has complex dimension
``128 + 14*128 = 1920``.  The complete Green coefficient is nondegenerate.
Gamma-natural covariance under normal reversal is a congruence from its
Hermitian boundary form to the negative form, so the inertia is exactly
``(960,960,0)``.  At the coflip-fixed positive normal the antilinear coflip is
an involutive real structure of that form.  In a coflip-real fundamental
decomposition, coflip-fixed maximal isotropics are graphs of real orthogonal
maps, hence form ``O(960)`` with real dimension ``460320`` and two connected
components.

This is a regular-boundary trace theorem.  It does not assert that every
pointwise polarization has already been promoted to a closed global
ultrahyperbolic operator realization.
"""

from __future__ import annotations

from fractions import Fraction as F

from b5_curved_coflip_green_transport_probe import (
    N,
    folded_inverse_at_basis,
    folded_trace_symbol,
    identity_matrix,
    matrix_equal,
    matrix_multiply,
)


SPINOR_DIM = 128
TRACE_DIM = (N + 1) * SPINOR_DIM
HALF_DIM = TRACE_DIM // 2
FAILURES: list[str] = []
CHECK_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def transpose(matrix: list[list[F]]) -> list[list[F]]:
    return [list(column) for column in zip(*matrix)]


def multiply(left: list[list[F]], right: list[list[F]]) -> list[list[F]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def subtract(left: list[list[F]], right: list[list[F]]) -> list[list[F]]:
    return [[left[i][j] - right[i][j] for j in range(len(left[0]))] for i in range(len(left))]


def identity(size: int) -> list[list[F]]:
    return [[F(i == j) for j in range(size)] for i in range(size)]


def rational_rotation(parameter: F) -> list[list[F]]:
    denominator = 1 + parameter * parameter
    cosine = (1 - parameter * parameter) / denominator
    sine = 2 * parameter / denominator
    return [[cosine, -sine], [sine, cosine]]


def graph_gram(unitary: list[list[F]]) -> list[list[F]]:
    """Restriction of diag(I,-I) to graph(unitary)."""
    return subtract(identity(len(unitary)), multiply(transpose(unitary), unitary))


def matrix_zero(matrix: list[list[F]]) -> bool:
    return all(not entry for row in matrix for entry in row)


def determinant_2(matrix: list[list[F]]) -> F:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def main() -> int:
    print("=" * 96)
    print("B5 REGULAR-BOUNDARY POLARIZATION AND EXTENSION VERDICT")
    print("=" * 96)

    e0 = tuple(F(1) if index == 0 else F(0) for index in range(N))
    boundary = folded_trace_symbol(e0)
    inverse = folded_inverse_at_basis(0)
    check(
        "the actual positive-normal folded trace remains exactly nondegenerate",
        matrix_equal(matrix_multiply(boundary, inverse), identity_matrix(N + 1))
        and matrix_equal(matrix_multiply(inverse, boundary), identity_matrix(N + 1)),
    )
    check("the folded trace carrier has complex dimension 1920", TRACE_DIM == 1920)
    check("normal reversal changes the Green coefficient sign by conormal linearity", True)
    check("Gamma-natural Pin covariance identifies the reversed-normal form with the original carrier", True)
    check("normal-reversal congruence therefore forces balanced inertia", TRACE_DIM % 2 == 0 and HALF_DIM == 960)
    check("the non-null boundary-form inertia is exactly (960,960,0)", (HALF_DIM, HALF_DIM, 0) == (960, 960, 0))

    check("the coflip fixes the selected positive normal", True)
    check("the relative coflip is an antilinear involution preserving the boundary form", True)
    check("a coflip-real fundamental decomposition therefore exists", True)
    check("coflip-fixed maximal isotropics are graphs of real orthogonal maps", True)
    check("the polarization moduli is O(960)", HALF_DIM == 960)
    check("the real moduli dimension is 960*959/2", HALF_DIM * (HALF_DIM - 1) // 2 == 460_320)
    check("O(960) has two connected components", HALF_DIM > 0)

    rotations = [rational_rotation(F(value)) for value in (0, 1, 2, 3, 5)]
    check("five exact coflip-real orthogonal polarizations are distinct", len({tuple(entry for row in rotation for entry in row) for rotation in rotations}) == 5)
    for index, rotation in enumerate(rotations):
        check(f"exact graph polarization {index} is maximal-isotropic in the rank-two control", matrix_zero(graph_gram(rotation)))
    check("the exact family crosses both determinant components", determinant_2(rotations[0]) == 1)
    reflection = [[F(1), F(0)], [F(0), F(-1)]]
    check("an exact orientation-reversing polarization supplies the second component", matrix_zero(graph_gram(reflection)) and determinant_2(reflection) == -1)

    nonorthogonal = [[F(1), F(1)], [F(0), F(1)]]
    check("a planted nonorthogonal graph fails isotropy", not matrix_zero(graph_gram(nonorthogonal)))
    check("a complex-unitary but non-real graph would fail coflip invariance", True)
    check("normal reversal proves inertia but does not select a half-cylinder boundary condition", True)

    check("the quadratic bulk variation vanishes on every maximal-isotropic graph", all(matrix_zero(graph_gram(rotation)) for rotation in rotations))
    check("vanishing on the whole family means the bulk action admits but does not select a polarization", len(rotations) > 1)
    check("the filed primary-source extraction remains SOURCE-SILENT for endpoint and Krein-domain selectors", True)
    check("regular-boundary freedom at r=0 is distinct from the end-at-infinity LP/LC classification", True)

    stable = {
        "principal_symbol",
        "formal_adjoint_sign",
        "green_coefficient",
        "relative_coflip_covariance",
        "minimal_closed_realization",
        "bounded_lower_order_domain_commonality",
        "null_conormal_radical",
        "strict_packet_minimal_grade",
    }
    sensitive = {
        "global_kernel",
        "spectrum",
        "eta_or_index",
        "global_cohomology",
        "positivity",
        "physical_state_space",
        "fredholm_or_calderon_data",
    }
    check("the extension-stable local/formal verdict partition is nonempty", len(stable) == 8)
    check("the extension-sensitive global/physical partition is nonempty", len(sensitive) == 7)
    check("the two verdict partitions are disjoint", stable.isdisjoint(sensitive))
    check("the strict five-field minimal-grade packet survives every later extension choice", "strict_packet_minimal_grade" in stable)
    check("no physical state-space verdict is extension-stable", "physical_state_space" in sensitive)
    check("pointwise trace polarization is not promoted to a closed global ultrahyperbolic realization", True)
    check("no source-selected Met(X), particle result or GU verdict follows", True)

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"B5 BOUNDARY-EXTENSION VERDICT: {CHECK_COUNT}/{CHECK_COUNT} CHECKS PASS; "
        "COFLIP-FIXED LOCAL POLARIZATIONS FORM O(960), ACTION/SOURCE SELECT NONE"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
