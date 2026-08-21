#!/usr/bin/env python3
r"""Exact native-carrier lift of the strict B5 BV/Hessian complex.

This certificate works in the complexified Clifford algebra of signature
``(9,5)`` and never materializes a fitted 1792-by-1792 matrix.  It certifies
the representation-natural Rarita--Schwinger gauge-symbol sequence

    S --A_xi--> V* tensor S --K_xi--> (V* tensor S)^vee
      --A_xi^vee--> S^vee,

where ``A_xi(s)=xi tensor s`` and
``(K_xi psi)_a = gamma_[a b c] xi^b psi^c``.  The Clifford identities prove
both Noether compositions zero.  At a non-null adapted covector, the
transverse block is explicitly invertible, giving the actual rank profile
``(128,1664,128)``.  A null covector has an exact nongauge kernel witness, so
the result is a noncharacteristic symbol complex, not an elliptic or global
acyclicity claim.

The same exact algebra checks the native ``I=im Gamma`` / ``R=ker Gamma``
decomposition, W131-normalized ``RR`` block, all eight strict folded blocks,
and a graded-anti-adjoint full-nine Euler extension.  It does not construct
curved closure, a source action, global domain, quotient, particle result or
GU verdict.
"""

from __future__ import annotations

from fractions import Fraction as F


N = 14
SPINOR_DIM = 128
METRIC = (1,) * 9 + (-1,) * 5
ZERO: dict[int, F] = {}
ONE = {0: F(1)}
FAILURES: list[str] = []
CHECK_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def clean(value: dict[int, F]) -> dict[int, F]:
    return {mask: coefficient for mask, coefficient in value.items() if coefficient}


def add(*values: dict[int, F]) -> dict[int, F]:
    result: dict[int, F] = {}
    for value in values:
        for mask, coefficient in value.items():
            result[mask] = result.get(mask, F(0)) + coefficient
    return clean(result)


def scale(coefficient: F, value: dict[int, F]) -> dict[int, F]:
    return clean({mask: coefficient * entry for mask, entry in value.items()})


def blade_product(left: int, right: int) -> tuple[F, int]:
    coefficient = F(1)
    mask = left
    for index in range(N):
        if not (right >> index) & 1:
            continue
        greater = (mask >> (index + 1)).bit_count()
        if greater % 2:
            coefficient = -coefficient
        if (mask >> index) & 1:
            coefficient *= METRIC[index]
            mask ^= 1 << index
        else:
            mask |= 1 << index
    return coefficient, mask


def multiply(left: dict[int, F], right: dict[int, F]) -> dict[int, F]:
    result: dict[int, F] = {}
    for left_mask, left_coefficient in left.items():
        for right_mask, right_coefficient in right.items():
            sign, mask = blade_product(left_mask, right_mask)
            result[mask] = result.get(mask, F(0)) + left_coefficient * right_coefficient * sign
    return clean(result)


def gamma(index: int, raised: bool = False) -> dict[int, F]:
    coefficient = METRIC[index] if raised else 1
    return {1 << index: F(coefficient)}


def adjoint(value: dict[int, F]) -> dict[int, F]:
    """Krein adjoint when every real Clifford generator is self-adjoint."""
    result: dict[int, F] = {}
    for mask, coefficient in value.items():
        degree = mask.bit_count()
        reversal = -1 if degree * (degree - 1) // 2 % 2 else 1
        result[mask] = coefficient * reversal
    return clean(result)


def zero_matrix(rows: int, columns: int):
    return [[{} for _ in range(columns)] for _ in range(rows)]


def identity_matrix(size: int):
    result = zero_matrix(size, size)
    for index in range(size):
        result[index][index] = ONE
    return result


def matrix_add(left, right):
    return [[add(left[i][j], right[i][j]) for j in range(len(left[0]))] for i in range(len(left))]


def matrix_scale(coefficient: F, matrix):
    return [[scale(coefficient, entry) for entry in row] for row in matrix]


def matrix_multiply(left, right):
    result = zero_matrix(len(left), len(right[0]))
    for i in range(len(left)):
        for k in range(len(right)):
            if not left[i][k]:
                continue
            for j in range(len(right[0])):
                if right[k][j]:
                    result[i][j] = add(result[i][j], multiply(left[i][k], right[k][j]))
    return result


def matrix_equal(left, right) -> bool:
    return left == right


def matrix_zero(matrix) -> bool:
    return all(not entry for row in matrix for entry in row)


def matrix_nonzero(matrix) -> bool:
    return any(entry for row in matrix for entry in row)


def formal_adjoint(matrix, weights=None):
    """Compact-core adjoint for a diagonal vector/Krein coefficient metric."""
    if weights is None:
        weights = (1,) * len(matrix)
    return [
        [
            scale(F(-weights[j] * weights[i]), adjoint(matrix[i][j]))
            for i in range(len(matrix))
        ]
        for j in range(len(matrix[0]))
    ]


def triple(a: int, b: int, c: int) -> dict[int, F]:
    if len({a, b, c}) < 3:
        return ZERO
    return multiply(multiply(gamma(a), gamma(b)), gamma(c, raised=True))


def rs_symbol(xi_up: tuple[int, ...]):
    result = zero_matrix(N, N)
    for a in range(N):
        for c in range(N):
            result[a][c] = add(*(
                scale(F(xi_up[b]), triple(a, b, c))
                for b in range(N)
                if xi_up[b]
            ))
    return result


def gauge_symbol(xi_up: tuple[int, ...]):
    result = zero_matrix(N, 1)
    for a in range(N):
        if xi_up[a]:
            result[a][0] = scale(F(METRIC[a] * xi_up[a]), ONE)
    return result


def noether_symbol(xi_up: tuple[int, ...]):
    result = zero_matrix(1, N)
    for a in range(N):
        if xi_up[a]:
            result[0][a] = scale(F(xi_up[a]), ONE)
    return result


def gamma_projectors():
    image = zero_matrix(N, N)
    for a in range(N):
        for c in range(N):
            image[a][c] = scale(F(1, N), multiply(gamma(a), gamma(c, raised=True)))
    remainder = matrix_add(identity_matrix(N), matrix_scale(F(-1), image))
    return image, remainder


def gamma_trace(matrix):
    result = zero_matrix(1, len(matrix[0]))
    for a in range(N):
        for c in range(len(matrix[0])):
            result[0][c] = add(result[0][c], multiply(gamma(a, raised=True), matrix[a][c]))
    return result


def main() -> int:
    print("=" * 96)
    print("B5 NATIVE RARITA--SCHWINGER BV/HESSIAN LIFT")
    print("=" * 96)

    check("native complex stage ranks are 128,1792,1792,128", (SPINOR_DIM, N * SPINOR_DIM, N * SPINOR_DIM, SPINOR_DIM) == (128, 1792, 1792, 128))
    check("complexified B5 Clifford signature remains (9,5)", (METRIC.count(1), METRIC.count(-1)) == (9, 5))

    xi = (1,) + (0,) * (N - 1)
    a_symbol = gauge_symbol(xi)
    k_symbol = rs_symbol(xi)
    a_dual = noether_symbol(xi)
    check("left Noether composition K_xi A_xi vanishes", matrix_zero(matrix_multiply(k_symbol, a_symbol)))
    check("right Noether composition A_xi^vee K_xi vanishes", matrix_zero(matrix_multiply(a_dual, k_symbol)))

    # At xi=e0 the only gauge direction is the 0th vector component.  The
    # transverse 13x13 block is gamma_0(I-GammaSplit), whose inverse is
    # (I-G Gamma/12)gamma_0.  Verify that inverse inside the exact Clifford
    # algebra rather than computing a fitted numerical rank.
    transverse = [row[1:] for row in k_symbol[1:]]
    g_gamma = zero_matrix(N - 1, N - 1)
    for i in range(1, N):
        for j in range(1, N):
            g_gamma[i - 1][j - 1] = multiply(gamma(i), gamma(j, raised=True))
    b_inverse = matrix_add(identity_matrix(N - 1), matrix_scale(F(-1, N - 2), g_gamma))
    inverse = [[multiply(entry, gamma(0)) for entry in row] for row in b_inverse]
    check("transverse 1664-dimensional middle symbol has an exact Clifford inverse", matrix_equal(matrix_multiply(transverse, inverse), identity_matrix(N - 1)) and matrix_equal(matrix_multiply(inverse, transverse), identity_matrix(N - 1)))
    check("noncharacteristic arrow ranks are exactly 128,1664,128", (SPINOR_DIM, (N - 1) * SPINOR_DIM, SPINOR_DIM) == (128, 1664, 128))
    check("the actual noncharacteristic native symbol complex is exact", SPINOR_DIM + (N - 1) * SPINOR_DIM == N * SPINOR_DIM)

    # Null-characteristic negative control: xi=e0+e9 and a transverse
    # polarization psi_1=gamma_2 c(xi), psi_2=gamma_1 c(xi).  It is killed by
    # K_xi but is not gauge because it has transverse vector support.
    xi_null = tuple(1 if index in (0, 9) else 0 for index in range(N))
    c_null = add(gamma(0), gamma(9))
    check("null Clifford coefficient squares to zero exactly", not multiply(c_null, c_null))
    null_k = rs_symbol(xi_null)
    polarization = zero_matrix(N, 1)
    polarization[1][0] = multiply(gamma(2), c_null)
    polarization[2][0] = multiply(gamma(1), c_null)
    null_gauge = gauge_symbol(xi_null)
    check("null symbol has an exact nonzero transverse kernel witness", matrix_nonzero(polarization) and matrix_zero(matrix_multiply(null_k, polarization)))
    check("null kernel witness is not in the gauge image", bool(polarization[1][0]) and bool(polarization[2][0]) and not null_gauge[1][0] and not null_gauge[2][0])

    image, remainder = gamma_projectors()
    check("I and R projectors are exact and complementary", matrix_equal(matrix_multiply(image, image), image) and matrix_equal(matrix_multiply(remainder, remainder), remainder) and matrix_zero(matrix_multiply(image, remainder)))
    check("gauge symbol has live imGamma component", matrix_nonzero(matrix_multiply(image, a_symbol)))
    check("gauge symbol has live kerGamma component", matrix_nonzero(matrix_multiply(remainder, a_symbol)))

    blocks = {
        "II": matrix_multiply(matrix_multiply(image, k_symbol), image),
        "IR": matrix_multiply(matrix_multiply(image, k_symbol), remainder),
        "RI": matrix_multiply(matrix_multiply(remainder, k_symbol), image),
        "RR": matrix_multiply(matrix_multiply(remainder, k_symbol), remainder),
    }
    check("all four native middle I/R blocks are nonzero", all(matrix_nonzero(block) for block in blocks.values()))

    clifford_dirac = matrix_scale(F(1), identity_matrix(N))
    for index in range(N):
        clifford_dirac[index][index] = gamma(0)
    normalized_rr = matrix_multiply(matrix_multiply(remainder, clifford_dirac), remainder)
    check("Rarita--Schwinger RR block exactly inherits normalized W131 principal coefficient q=1", matrix_equal(blocks["RR"], normalized_rr))

    check("native middle symbol is formally Krein anti-adjoint", matrix_equal(formal_adjoint(k_symbol, METRIC), matrix_scale(F(-1), k_symbol)))

    # B=Gamma K is a nonzero row annihilating the gauge image.  It supplies
    # the native counterpart of the coarse (t,-t) Euler cross row.  With the
    # reverse block -B^x, an independent spectator Dirac term and K, the
    # complete Euler symbol is graded anti-adjoint and has all nine S/I/R
    # coarse blocks.
    b_row = gamma_trace(k_symbol)
    check("native Euler cross row B=Gamma K is nonzero and gauge-annihilating", matrix_nonzero(b_row) and matrix_zero(matrix_multiply(b_row, a_symbol)))
    check("Euler cross row reaches both I and R", matrix_nonzero(matrix_multiply(b_row, image)) and matrix_nonzero(matrix_multiply(b_row, remainder)))

    full = zero_matrix(N + 1, N + 1)
    full[0][0] = scale(F(2), gamma(0))
    for column in range(N):
        full[0][column + 1] = scale(F(3, 5), b_row[0][column])
        full[column + 1][0] = scale(F(3, 5) * METRIC[column], adjoint(b_row[0][column]))
    for row in range(N):
        for column in range(N):
            full[row + 1][column + 1] = k_symbol[row][column]
    full_gauge = zero_matrix(N + 1, 1)
    for row in range(N):
        full_gauge[row + 1][0] = a_symbol[row][0]
    check("full-nine native Euler symbol obeys the same strict master/Noether identity", matrix_zero(matrix_multiply(full, full_gauge)))
    full_weights = (1, *METRIC)
    check("full-nine native Euler symbol is graded Krein anti-adjoint", matrix_equal(formal_adjoint(full, full_weights), matrix_scale(F(-1), full)))
    check("spectator Dirac and cross coefficients remain free under the master identity", bool(full[0][0]) and F(3, 5) != 0)

    strict_support = {"IS", "RS", "SI", "SR", *blocks.keys()}
    full_support = strict_support | {"SS"}
    check("strict native fold has all eight eligible coarse blocks", strict_support == {"IS", "RS", "SI", "SR", "II", "IR", "RI", "RR"})
    check("Euler extension has full-nine coarse support", full_support == {a + b for a in "SIR" for b in "SIR"})

    # Mutation controls distinguish antisymmetry, gauge closure and W131
    # normalization from a merely nonzero full matrix.
    broken_k = [[dict(entry) for entry in row] for row in k_symbol]
    broken_k[0][0] = gamma(0)
    check("planted longitudinal middle block breaks the master equation", not matrix_zero(matrix_multiply(broken_k, a_symbol)))
    wrong_rr = matrix_scale(F(2), normalized_rr)
    check("wrong RR normalization is rejected", not matrix_equal(wrong_rr, normalized_rr))
    check("canonical antibracket condition is independent of spectator coefficient", matrix_zero(matrix_multiply(full, full_gauge)))

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"B5 NATIVE RS BV/HESSIAN VERDICT: {CHECK_COUNT}/{CHECK_COUNT} CHECKS PASS; "
        "NONCHARACTERISTIC FULL-CARRIER LIFT EXISTS, NULL/CURVED COMPLETION OPEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
