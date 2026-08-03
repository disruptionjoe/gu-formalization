"""Exact SageMath certificate for the Sp(32,32) block specialization.

This file uses only exact rational quaternion arithmetic.  It does not use
floating point, random sampling, or numerical tolerances.  The general theorem
is proved in the manuscript; this certificate checks the concrete block model.
"""

from sage.all import (
    QQ,
    QuaternionAlgebra,
    block_matrix,
    identity_matrix,
    matrix,
    vector,
)

H = QuaternionAlgebra(QQ, -1, -1)
qi = H.gen(0)
qj = H.gen(1)
qk = qi * qj
QBASIS = (H.one(), qi, qj, qk)

checks = 0


def check(label, condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def qstar(M):
    return M.conjugate_transpose()


def zero(n):
    return matrix(H, n, n, 0)


def eye(n):
    return identity_matrix(H, n)


def beta(n):
    I = eye(n)
    O = zero(n)
    return block_matrix([[I, O], [O, -I]])


def grading(n):
    I = eye(n)
    O = zero(n)
    return block_matrix([[O, I], [I, O]])


def isotropic_change_unnormalized(n):
    """Twice-normalized basis change: T = sqrt(2) S and T^-1 = T/2."""
    I = eye(n)
    return block_matrix([[I, I], [I, -I]])


def diagonal_grading(n):
    return beta(n)


def y_plus(B):
    O = zero(B.nrows())
    return block_matrix([[O, -2 * B], [O, O]])


def y_minus(B):
    O = zero(B.nrows())
    return block_matrix([[O, O], [2 * B, O]])


def y_zero(A, B):
    O = zero(A.nrows())
    return block_matrix([[A + B, O], [O, A - B]])


def x_plus(B):
    return block_matrix([[-B, B], [-B, B]])


def x_minus(B):
    return block_matrix([[B, B], [-B, -B]])


def x_zero(A, B):
    return block_matrix([[A, B], [B, A]])


def skew_hermitian_basis(n):
    out = []
    for a in range(n):
        for q in (qi, qj, qk):
            B = zero(n)
            B[a, a] = q
            out.append(B)
    for a in range(n):
        for b in range(a + 1, n):
            for q in QBASIS:
                B = zero(n)
                B[a, b] = q
                B[b, a] = -q.conjugate()
                out.append(B)
    return out


def hermitian_basis(n):
    out = []
    for a in range(n):
        B = zero(n)
        B[a, a] = H.one()
        out.append(B)
    for a in range(n):
        for b in range(a + 1, n):
            for q in QBASIS:
                B = zero(n)
                B[a, b] = q
                B[b, a] = q.conjugate()
                out.append(B)
    return out


def lie_member(X, n):
    form = beta(n)
    return qstar(X) * form + form * X == 0


def certify_rank(n):
    I2 = eye(2 * n)
    P = beta(n)
    z = grading(n)
    T = isotropic_change_unnormalized(n)
    Tinv = QQ(1) / 2 * T
    skew = skew_hermitian_basis(n)
    herm = hermitian_basis(n)

    check(f"n={n}: z lies in sp(n,n)", qstar(z) * P + P * z == 0)
    check(f"n={n}: z is involutory", z * z == I2)
    check(f"n={n}: P is involutory", P * P == I2)
    check(f"n={n}: P anticommutes with z", P * z + z * P == 0)
    check(f"n={n}: isotropic change inverse", Tinv * T == I2 and T * Tinv == I2)
    check(f"n={n}: grading diagonalized", Tinv * z * T == diagonal_grading(n))
    check(f"n={n}: form becomes hyperbolic", qstar(T) * P * T == 2 * z)

    v = vector(H, [H.one()] + [H.zero()] * (n - 1))
    v_plus = vector(H, list(v) + list(v))
    v_minus = vector(H, list(v) + list(-v))
    check(f"n={n}: z has eigenvalue +1", z * v_plus == v_plus)
    check(f"n={n}: z has eigenvalue -1", z * v_minus == -v_minus)

    check(f"n={n}: skew basis count", len(skew) == n * (2 * n + 1))
    check(f"n={n}: Hermitian basis count", len(herm) == n * (2 * n - 1))
    check(f"n={n}: g0 dimension", len(skew) + len(herm) == 4 * n * n)
    check(
        f"n={n}: total Lie dimension",
        2 * len(skew) + len(skew) + len(herm) == (2 * n) * (4 * n + 1),
    )

    for index, B in enumerate(skew):
        check(f"n={n}, skew[{index}]: B*=-B", qstar(B) == -B)
        xp = x_plus(B)
        xm = x_minus(B)
        check(f"n={n}, plus[{index}]: nonzero", xp != 0)
        check(f"n={n}, minus[{index}]: nonzero", xm != 0)
        check(f"n={n}, plus[{index}]: Lie member", lie_member(xp, n))
        check(f"n={n}, minus[{index}]: Lie member", lie_member(xm, n))
        check(f"n={n}, plus[{index}]: ad eigenvalue +2", z * xp - xp * z == 2 * xp)
        check(f"n={n}, minus[{index}]: ad eigenvalue -2", z * xm - xm * z == -2 * xm)
        check(f"n={n}, plus[{index}]: square zero", xp * xp == 0)
        check(f"n={n}, minus[{index}]: square zero", xm * xm == 0)
        check(
            f"n={n}, plus[{index}]: isotropic upper block",
            Tinv * xp * T == y_plus(B),
        )
        check(
            f"n={n}, minus[{index}]: isotropic lower block",
            Tinv * xm * T == y_minus(B),
        )
        check(
            f"n={n}, plus[{index}]: linear truncation",
            (I2 + 7 * xp) * (I2 - 7 * xp) == I2,
        )
        check(
            f"n={n}, minus[{index}]: linear truncation",
            (I2 + 7 * xm) * (I2 - 7 * xm) == I2,
        )

    for index, A in enumerate(skew):
        for jndex, B in enumerate(herm):
            x0 = x_zero(A, B)
            check(f"n={n}, zero[{index},{jndex}]: Lie member", lie_member(x0, n))
            check(
                f"n={n}, zero[{index},{jndex}]: ad eigenvalue 0", z * x0 - x0 * z == 0
            )
            check(
                f"n={n}, zero[{index},{jndex}]: isotropic diagonal block",
                Tinv * x0 * T == y_zero(A, B),
            )

    for index, B in enumerate(skew):
        for jndex, C in enumerate(skew):
            check(
                f"n={n}, plus product[{index},{jndex}]",
                x_plus(B) * x_plus(C) == 0,
            )
            check(
                f"n={n}, minus product[{index},{jndex}]",
                x_minus(B) * x_minus(C) == 0,
            )


for rank in (1, 2, 3):
    certify_rank(rank)

n = 32
dim_skew = n * (2 * n + 1)
dim_herm = n * (2 * n - 1)
dim_g0 = dim_skew + dim_herm
dim_g = 2 * dim_skew + dim_g0
dim_k = 2 * dim_skew

check("Sp(32,32): dim g+", dim_skew == 2080)
check("Sp(32,32): dim g-", dim_skew == 2080)
check("Sp(32,32): dim g0", dim_g0 == 4096)
check("Sp(32,32): dim g", dim_g == 8256)
check("Sp(32,32): dim K", dim_k == 4160)
check("Sp(32,32): dim G/K", dim_g - dim_k == 4096)

print(f"PASS exact SageMath certificate: {checks} checks")
print("decomposition: 8256 = 2080 + 4096 + 2080")
print("arithmetic: rational quaternions; no floating point or tolerances")
