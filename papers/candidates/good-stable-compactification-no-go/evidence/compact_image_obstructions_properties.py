"""Exact property-based falsifiers for the Sp(n,n) block identities.

The test data are integer quaternions and exact matrix operations.  Hypothesis
generates deterministic small-rank examples.  No NumPy, floating point, or
numerical tolerances are used.
"""

from __future__ import annotations

from dataclasses import dataclass

from hypothesis import given, settings
from hypothesis import strategies as st


@dataclass(frozen=True)
class Q:
    a: int = 0
    b: int = 0
    c: int = 0
    d: int = 0

    def __add__(self, other: Q) -> Q:
        return Q(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    def __neg__(self) -> Q:
        return Q(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, other: Q) -> Q:
        return self + (-other)

    def __mul__(self, other: Q) -> Q:
        a, b, c, d = self.a, self.b, self.c, self.d
        e, f, g, h = other.a, other.b, other.c, other.d
        return Q(
            a * e - b * f - c * g - d * h,
            a * f + b * e + c * h - d * g,
            a * g - b * h + c * e + d * f,
            a * h + b * g - c * f + d * e,
        )

    def conj(self) -> Q:
        return Q(self.a, -self.b, -self.c, -self.d)


ZERO = Q()
ONE = Q(1)


Matrix = list[list[Q]]


def zeros(rows: int, cols: int | None = None) -> Matrix:
    cols = rows if cols is None else cols
    return [[ZERO for _ in range(cols)] for _ in range(rows)]


def eye(n: int) -> Matrix:
    out = zeros(n)
    for i in range(n):
        out[i][i] = ONE
    return out


def madd(A: Matrix, B: Matrix) -> Matrix:
    return [[x + y for x, y in zip(arow, brow)] for arow, brow in zip(A, B)]


def mneg(A: Matrix) -> Matrix:
    return [[-x for x in row] for row in A]


def msub(A: Matrix, B: Matrix) -> Matrix:
    return madd(A, mneg(B))


def mmul(A: Matrix, B: Matrix) -> Matrix:
    rows = len(A)
    inner = len(B)
    cols = len(B[0])
    out = zeros(rows, cols)
    for i in range(rows):
        for j in range(cols):
            value = ZERO
            for k in range(inner):
                value = value + A[i][k] * B[k][j]
            out[i][j] = value
    return out


def mscale(k: int, A: Matrix) -> Matrix:
    scalar = Q(k)
    return [[scalar * x for x in row] for row in A]


def star(A: Matrix) -> Matrix:
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def block(A: Matrix, B: Matrix, C: Matrix, D: Matrix) -> Matrix:
    return [arow + brow for arow, brow in zip(A, B)] + [
        crow + drow for crow, drow in zip(C, D)
    ]


def grading(n: int) -> Matrix:
    return block(zeros(n), eye(n), eye(n), zeros(n))


def beta(n: int) -> Matrix:
    return block(eye(n), zeros(n), zeros(n), mneg(eye(n)))


def isotropic_change_unnormalized(n: int) -> Matrix:
    I = eye(n)
    return block(I, I, I, mneg(I))


def x_plus(B: Matrix) -> Matrix:
    return block(mneg(B), B, mneg(B), B)


def x_minus(B: Matrix) -> Matrix:
    return block(B, B, mneg(B), mneg(B))


def is_zero(A: Matrix) -> bool:
    return all(value == ZERO for row in A for value in row)


def nonzero(A: Matrix) -> bool:
    return not is_zero(A)


qcoeff = st.integers(-4, 4)
quaternion = st.builds(Q, qcoeff, qcoeff, qcoeff, qcoeff)
pure_imaginary = st.builds(Q, st.just(0), qcoeff, qcoeff, qcoeff)


def draw_skew_hermitian(draw, n: int) -> Matrix:
    B = zeros(n)
    for a in range(n):
        B[a][a] = draw(pure_imaginary)
    for a in range(n):
        for b in range(a + 1, n):
            q = draw(quaternion)
            B[a][b] = q
            B[b][a] = -q.conj()
    return B


@st.composite
def skew_hermitian_matrices(draw):
    n = draw(st.integers(1, 4))
    return n, draw_skew_hermitian(draw, n)


@st.composite
def same_rank_skew_pairs(draw):
    n = draw(st.integers(1, 4))
    return n, draw_skew_hermitian(draw, n), draw_skew_hermitian(draw, n)


@settings(max_examples=240, derandomize=True, deadline=None)
@given(skew_hermitian_matrices())
def test_exact_block_identities(data):
    n, B = data
    z = grading(n)
    form = beta(n)
    xp = x_plus(B)
    xm = x_minus(B)

    assert star(B) == mneg(B)
    assert is_zero(madd(mmul(star(xp), form), mmul(form, xp)))
    assert is_zero(madd(mmul(star(xm), form), mmul(form, xm)))
    assert msub(mmul(z, xp), mmul(xp, z)) == mscale(2, xp)
    assert msub(mmul(z, xm), mmul(xm, z)) == mscale(-2, xm)
    assert is_zero(mmul(xp, xp))
    assert is_zero(mmul(xm, xm))


@settings(max_examples=160, derandomize=True, deadline=None)
@given(same_rank_skew_pairs())
def test_mutual_zero_products(data):
    _, B, C = data
    assert is_zero(mmul(x_plus(B), x_plus(C)))
    assert is_zero(mmul(x_minus(B), x_minus(C)))


def test_dimension_formulas() -> None:
    for n in range(1, 33):
        skew = 3 * n + 4 * (n * (n - 1) // 2)
        herm = n + 4 * (n * (n - 1) // 2)
        assert skew == n * (2 * n + 1)
        assert herm == n * (2 * n - 1)
        assert 2 * skew + skew + herm == (2 * n) * (4 * n + 1)
    assert 32 * 65 == 2080
    assert 32 * 63 == 2016
    assert 2080 + 2016 == 4096
    assert 2080 + 4096 + 2080 == 8256


def test_isotropic_basis_change() -> None:
    # T = sqrt(2) S avoids division while checking the exact basis identities:
    # zT = T diag(I,-I) and T* beta T = 2J.
    for n in range(1, 5):
        T = isotropic_change_unnormalized(n)
        z = grading(n)
        form = beta(n)
        assert mmul(z, T) == mmul(T, form)
        assert mmul(mmul(star(T), form), T) == mscale(2, z)

    B = [[Q(0, 1, 2, -1)]]
    T = isotropic_change_unnormalized(1)
    upper = block(zeros(1), mscale(-2, B), zeros(1), zeros(1))
    lower = block(zeros(1), zeros(1), mscale(2, B), zeros(1))
    assert mmul(x_plus(B), T) == mmul(T, upper)
    assert mmul(x_minus(B), T) == mmul(T, lower)


def test_planted_mutations_are_rejected() -> None:
    # One wrong sign in X_+ destroys both the +2 commutator and square-zero law.
    B = [[Q(0, 1, 0, 0)]]
    z = grading(1)
    wrong_plus = block(mneg(B), B, B, B)
    assert msub(mmul(z, wrong_plus), mmul(wrong_plus, z)) != mscale(2, wrong_plus)
    assert nonzero(mmul(wrong_plus, wrong_plus))

    # An involution can be neither commuting nor anticommuting with z.  This
    # falsifies the illicit inference "noncommuting implies purely odd."
    mixed = [[ONE, ONE], [ZERO, -ONE]]
    assert mmul(mixed, mixed) == eye(2)
    assert nonzero(msub(mmul(mixed, z), mmul(z, mixed)))
    assert nonzero(madd(mmul(mixed, z), mmul(z, mixed)))


def main() -> None:
    test_exact_block_identities()
    test_mutual_zero_products()
    test_dimension_formulas()
    test_isotropic_basis_change()
    test_planted_mutations_are_rejected()
    print(
        "PASS exact property certificate: 400 generated examples plus deterministic controls"
    )
    print("arithmetic: integer quaternions; no floating point or tolerances")
    print("planted mutants rejected: wrong X_+ sign; noncommuting-is-not-purely-odd")


if __name__ == "__main__":
    main()
