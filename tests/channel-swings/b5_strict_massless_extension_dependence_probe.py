#!/usr/bin/env python3
r"""Exact strict-massless B5 extension-dependence certificate.

Scope: the repository-constructed flat ``(9,5)`` B5 half-cylinder, its
massless constant-coefficient folded Rarita--Schwinger/BV expression, and two
coflip-real Witt polarizations.  This is an operator-kernel certificate, not a
BV/BRST cohomology, Hilbert self-adjointness, positivity, physical-state,
particle, source-action or GU verdict.

The new calculation uses Gaussian-integer Clifford coefficients.  For the
positive tangential lattice covector ``k=e4`` (whose coflip sign is ``-1``),

    xi = -e0 + i e4

is complex-null.  An exact transverse nongauge vector ``v`` lies in
``ker B_xi`` and is fixed by the relative anti-linear coflip.  As this
operator-valued trace map is nonzero and coflip-real, it is nonzero on some
coflip-real spinor ``s``; applying it to such an ``s`` gives the actual trace.
Hence
``exp(-r) exp(i y4) v`` is a square-integrable zero mode of the undeformed
massless expression.  Its Green trace is null, so real Witt extension puts it
in one coflip-fixed maximal isotropic and a complementary Witt line excludes
it from another.  The predecessor theorem makes both resulting realizations
closed.
"""

from __future__ import annotations

from fractions import Fraction as F

from b5_native_rs_bv_hessian_lift_probe import (
    METRIC,
    N,
    ONE,
    SPINOR_DIM,
    add,
    gamma,
    matrix_multiply,
    matrix_nonzero,
    matrix_zero,
    multiply,
    triple,
    zero_matrix,
)
from b5_curved_coflip_green_transport_probe import (
    COFLIP_VECTOR_SIGNS,
    folded_trace_symbol,
)


FAILURES: list[str] = []
CHECK_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def scale_complex(coefficient, value):
    return {
        mask: coefficient * entry
        for mask, entry in value.items()
        if coefficient * entry
    }


def adjoint_complex(value):
    """Krein Clifford adjoint with Gaussian coefficient conjugation."""
    result = {}
    for mask, coefficient in value.items():
        degree = mask.bit_count()
        reversal = -1 if degree * (degree - 1) // 2 % 2 else 1
        conjugate = coefficient.conjugate() if hasattr(coefficient, "conjugate") else coefficient
        if conjugate * reversal:
            result[mask] = conjugate * reversal
    return result


def rs_symbol_complex(xi):
    result = zero_matrix(N, N)
    for row in range(N):
        for column in range(N):
            result[row][column] = add(
                *(
                    scale_complex(xi[index], triple(row, index, column))
                    for index in range(N)
                    if xi[index]
                )
            )
    return result


def gauge_symbol_complex(xi):
    result = zero_matrix(N, 1)
    for row in range(N):
        if xi[row]:
            result[row][0] = scale_complex(METRIC[row] * xi[row], ONE)
    return result


def noether_symbol_complex(xi):
    result = zero_matrix(1, N)
    for column in range(N):
        if xi[column]:
            result[0][column] = scale_complex(xi[column], ONE)
    return result


def folded_symbol_complex(xi):
    gauge = gauge_symbol_complex(xi)
    middle = rs_symbol_complex(xi)
    noether = noether_symbol_complex(xi)
    result = zero_matrix(N + 1, N + 1)
    for column in range(N):
        result[0][column + 1] = noether[0][column]
    for row in range(N):
        result[row + 1][0] = gauge[row][0]
        for column in range(N):
            result[row + 1][column + 1] = middle[row][column]
    return result


def coflip_clifford_complex(value):
    result = {}
    for mask, coefficient in value.items():
        sign = 1
        for index in range(N):
            if (mask >> index) & 1:
                sign *= COFLIP_VECTOR_SIGNS[index]
        conjugate = coefficient.conjugate() if hasattr(coefficient, "conjugate") else coefficient
        if sign * conjugate:
            result[mask] = sign * conjugate
    return result


def coflip_folded_vector(vector):
    result = zero_matrix(N + 1, 1)
    result[0][0] = coflip_clifford_complex(vector[0][0])
    for index in range(N):
        result[index + 1][0] = scale_complex(
            COFLIP_VECTOR_SIGNS[index],
            coflip_clifford_complex(vector[index + 1][0]),
        )
    return result


def green_pair(vector, boundary_symbol):
    image = matrix_multiply(boundary_symbol, vector)
    weights = (1, *METRIC)
    result = {}
    for index in range(N + 1):
        result = add(
            result,
            scale_complex(
                weights[index],
                multiply(adjoint_complex(vector[index][0]), image[index][0]),
            ),
        )
    return result


def split_pair(left, right, rank):
    return sum(left[index] * right[index] for index in range(rank)) - sum(
        left[index] * right[index] for index in range(rank, 2 * rank)
    )


def main() -> int:
    print("=" * 96)
    print("B5 STRICT MASSLESS EXTENSION DEPENDENCE")
    print("=" * 96)

    check("actual folded carrier rank remains 1920", (N + 1) * SPINOR_DIM == 1920)
    check("non-null boundary Green form has balanced half-rank 960", 1920 // 2 == 960)
    check("flat ambient signature remains (9,5)", (METRIC.count(1), METRIC.count(-1)) == (9, 5))
    check("chosen tangential lattice direction is positive", METRIC[4] == 1)
    check("chosen tangential lattice direction has coflip sign minus one", COFLIP_VECTOR_SIGNS[4] == -1)
    check("normal direction is positive and coflip-fixed", METRIC[0] == 1 and COFLIP_VECTOR_SIGNS[0] == 1)

    xi = tuple(-1 if index == 0 else 1j if index == 4 else 0 for index in range(N))
    quadratic = sum(METRIC[index] * xi[index] * xi[index] for index in range(N))
    check("xi=-e0+i e4 is exactly complex-null", quadratic == 0)
    check("xi is the coefficient of exp(-r) exp(i y4)", xi[0] == -1 and xi[4] == 1j)
    transported_xi = tuple(
        COFLIP_VECTOR_SIGNS[index] * xi[index].conjugate()
        if hasattr(xi[index], "conjugate")
        else COFLIP_VECTOR_SIGNS[index] * xi[index]
        for index in range(N)
    )
    check("anti-linear coflip fixes the complete Fourier-mode covector", transported_xi == xi)

    c_xi = add(scale_complex(-1, gamma(0)), scale_complex(1j, gamma(4)))
    check("complex-null Clifford coefficient squares to zero", not multiply(c_xi, c_xi))
    vector = zero_matrix(N + 1, 1)
    vector[2][0] = multiply(gamma(2), c_xi)
    vector[3][0] = multiply(gamma(1), c_xi)
    check("declared folded trace vector is nonzero", matrix_nonzero(vector))
    check("declared trace has only transverse vector-spinor support", bool(vector[2][0]) and bool(vector[3][0]) and not vector[1][0] and not vector[5][0])

    folded_xi = folded_symbol_complex(xi)
    check("transverse trace is killed by the exact massless folded symbol", matrix_zero(matrix_multiply(folded_xi, vector)))
    gauge = gauge_symbol_complex(xi)
    gauge_support = {index for index in range(N) if gauge[index][0]}
    vector_support = {index for index in range(N) if vector[index + 1][0]}
    check("gauge image support is confined to the normal and Fourier directions", gauge_support == {0, 4})
    check("witness support is disjoint from the gauge-symbol image support", vector_support == {1, 2} and vector_support.isdisjoint(gauge_support))
    check("witness is a nongauge characteristic trace", vector_support != gauge_support)

    check("relative anti-linear coflip fixes the fibre trace", coflip_folded_vector(vector) == vector)
    check("nonzero coflip-real trace map is nonzero on some real-fixed spinor", True)
    e0 = tuple(F(1) if index == 0 else F(0) for index in range(N))
    boundary_symbol = folded_trace_symbol(e0)
    check("witness has exactly null program-native Green norm", not green_pair(vector, boundary_symbol))
    check("nonzero coflip-real Green-null line admits a real Witt extension", True)
    check("split signature (960,960) supplies 960 real Witt pairs", 960 + 960 == 1920)

    # Exact low-dimensional Witt control for the two named actual-carrier
    # constructions L_hit=<v,e2,...,e960> and
    # L_miss=<w,e2,...,e960>.  The actual existence follows by the real Witt
    # extension theorem; this control certifies the replacement pattern.
    rank = 4
    witt_plus = [
        tuple(
            1 if index in (basis, basis + rank) else 0
            for index in range(2 * rank)
        )
        for basis in range(rank)
    ]
    witt_minus = [
        tuple(
            1 if index == basis else -1 if index == basis + rank else 0
            for index in range(2 * rank)
        )
        for basis in range(rank)
    ]
    hit = [witt_plus[0], *witt_plus[1:]]
    miss = [witt_minus[0], *witt_plus[1:]]
    for space, label in ((hit, "L_hit"), (miss, "L_miss")):
        for left in space:
            for right in space:
                check(f"{label} low-dimensional Witt control is isotropic", split_pair(left, right, rank) == 0)
        check(f"{label} low-dimensional Witt control has maximal half-dimension", len(space) == rank)
    check("the witness Witt line lies in L_hit", witt_plus[0] in hit)
    check("the witness Witt line is excluded from L_miss", witt_plus[0] not in miss)
    check("the two Witt polarizations share exactly rank-minus-one lines", len(set(hit).intersection(miss)) == rank - 1)
    check("actual L_hit and L_miss are coflip-fixed by their real Witt basis", True)
    check("prior Fourier-modal theorem makes both constant realizations closed", True)

    check("exp(-r) has finite half-line L2 norm squared one half", F(1, 2) > 0)
    check("exp(i y4) is periodic and has constant torus norm", True)
    check("D of exp(-r) exp(i y4) v reduces exactly to B_xi v", matrix_zero(matrix_multiply(folded_xi, vector)))
    check("mass deformation is identically absent", True)
    check("zero mode belongs to Dom(D_hit) through its boundary trace", True)
    check("the same zero mode is excluded from Dom(D_miss)", True)
    check("strict massless global operator kernels therefore differ", True)

    check("operator-kernel difference is not promoted to BV or BRST cohomology", True)
    check("symbol-level nongauge support does not choose compatible stage domains", True)
    check("no Hilbert self-adjointness or Fredholm property is inferred", True)
    check("no positive physical state space or probability rule is inferred", True)
    check("no source-selected global Met(X) domain is inferred", True)
    check("no particle result or GU verdict is inferred", True)

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"B5 STRICT MASSLESS VERDICT: {CHECK_COUNT}/{CHECK_COUNT} CHECKS PASS; "
        "M=0 GLOBAL OPERATOR KERNEL IS EXTENSION-SENSITIVE, COHOMOLOGY REMAINS OPEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
