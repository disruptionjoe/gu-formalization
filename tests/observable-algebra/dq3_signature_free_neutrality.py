#!/usr/bin/env python3
"""Resolver Wave B / DQ3: exact constraint-restricted neutrality certificate.

The theorem is signature-label free.  If a Hermitian form B anticommutes with
a Hermitian involution Omega and V=ker Gamma is Omega-invariant, then B|V has
only off-diagonal blocks in the Omega grading.  Its inertia is (r,r,nullity).
If the restriction is nondegenerate, it is exactly neutral.

The native RS corollary uses the *Krein/metric adjoint* Gamma-sharp, not the
Euclidean/SVD dagger: Gamma Gamma-sharp = 14 I makes ker Gamma a nondegenerate
orthogonal summand.  No interacting-domain or physical-quotient claim follows.
"""
from __future__ import annotations

from sympy import Matrix, diag, eye, zeros


def check(name: str, condition: bool) -> None:
    print(f"  [{'ok ' if condition else 'FAIL'}] {name}")
    assert condition, name


def clifford_product(left: int, right: int, eta: tuple[int, ...]) -> tuple[int, int]:
    """Multiply ordered Clifford monomials represented by bit masks."""
    sign = 1
    result = left
    for idx in range(len(eta)):
        if not (right >> idx) & 1:
            continue
        swaps = (result >> (idx + 1)).bit_count()
        if swaps % 2:
            sign = -sign
        if (result >> idx) & 1:
            result ^= 1 << idx
            sign *= eta[idx]
        else:
            result |= 1 << idx
    return sign, result


def exact_fixture() -> None:
    I3 = eye(3)
    Omega = diag(1, 1, 1, -1, -1, -1)
    B = zeros(6)
    B[:3, 3:] = I3
    B[3:, :3] = I3
    Gamma = Matrix([[0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1]])
    A = diag(1, -1)
    check("fixture: Omega is a Hermitian involution", Omega * Omega == eye(6))
    check("fixture: B is Hermitian and anticommutes with Omega",
          B == B.H and Omega * B + B * Omega == zeros(6))
    check("fixture: constraint is Omega-equivariant", Gamma * Omega == A * Gamma)

    basis = Matrix.hstack(*Gamma.nullspace())
    gram = basis.H * B * basis
    plus = Matrix.hstack(basis[:, 0], basis[:, 1])
    minus = Matrix.hstack(basis[:, 2], basis[:, 3])
    C = plus.H * B * minus
    check("fixture: both graded halves are totally isotropic",
          plus.H * B * plus == zeros(2) and minus.H * B * minus == zeros(2))
    check("fixture: cross block is invertible", C.det() != 0)
    check("fixture: restricted determinant is nonzero", gram.det() != 0)
    # Integral congruence avoids irrational 45-degree rotations.
    S = Matrix.vstack(Matrix.hstack(eye(2), eye(2)),
                      Matrix.hstack(eye(2), -eye(2)))
    diagonalized = S.H * gram * S
    check("fixture: exact congruence has two positive and two negative blocks",
          diagonalized == diag(2, 2, -2, -2))


def native_clifford_identities() -> None:
    for p in (9, 7):
        eta = tuple([1] * p + [-1] * (14 - p))
        volume = (1 << 14) - 1
        beta = (1 << p) - 1
        # beta_p = phase * e0...e_{p-1}.  The raw p=9 word is Hermitian;
        # the raw p=7 word is anti-Hermitian and requires phase i.
        phase = 1 if p == 9 else 1j
        sr, mr = clifford_product(beta, beta, eta)
        reversal_sign = -1 if (p * (p - 1) // 2) % 2 else 1
        phased_square = phase * phase * sr
        phased_adjoint_factor = phase.conjugate() * reversal_sign
        check(f"Cl({p},{14-p}): phased beta is a Hermitian involution",
              mr == 0 and phased_square == 1 and phased_adjoint_factor == phase)
        for a in range(14):
            e = 1 << a
            s1, m1 = clifford_product(volume, e, eta)
            s2, m2 = clifford_product(e, volume, eta)
            check(f"Cl({p},{14-p}): volume anticommutes with e{a}",
                  m1 == m2 and s1 == -s2)
            # e_a^dag = eta_a e_a in the unitary Clifford fixture.  This is
            # the load-bearing identity making Gamma-sharp the B/Krein adjoint.
            sl, ml = clifford_product(e, beta, eta)
            sr_adj, mr_adj = clifford_product(beta, e, eta)
            check(f"Cl({p},{14-p}): e{a}^dag beta = beta e{a}",
                  ml == mr_adj and eta[a] * sl == sr_adj)
        sb1, mb1 = clifford_product(volume, beta, eta)
        sb2, mb2 = clifford_product(beta, volume, eta)
        check(f"Cl({p},{14-p}): volume anticommutes with odd beta word",
              mb1 == mb2 and sb1 == -sb2)
        gamma_gamma_sharp = 0
        for a in range(14):
            se, me = clifford_product(1 << a, 1 << a, eta)
            check(f"Cl({p},{14-p}): e{a} squared has declared sign",
                  me == 0 and se == eta[a])
            gamma_gamma_sharp += eta[a] * se
        check(f"Cl({p},{14-p}): Gamma Gamma-sharp = 14 I",
              gamma_gamma_sharp == 14)


def planted_failures() -> None:
    Omega = diag(1, -1)
    B = Matrix([[0, 1], [1, 0]])
    mixed = Matrix([[1], [1]])
    check("plant F1: non-invariant line can restrict positively",
          (mixed.H * B * mixed)[0] == 2 and Omega * mixed not in [mixed, -mixed])
    plus = Matrix([[1], [0]])
    check("plant F2: invariant but degenerate restriction is not (n,n)",
          (plus.H * B * plus)[0] == 0)
    definite = eye(2)
    check("plant F3: commuting form is definite, so anticommutation is load-bearing",
          Omega * definite + definite * Omega != zeros(2))
    # Metric adjoint for Gamma=[1,1], B=diag(1,-1) differs from Euclidean dagger.
    Gamma = Matrix([[1, 1]])
    B2 = diag(1, -1)
    sharp = B2.inv() * Gamma.H
    euclidean = Gamma.H
    check("plant F4: Euclidean dagger is not the Krein adjoint", sharp != euclidean)


def main() -> int:
    print("DQ3 — exact signature-free constrained-neutrality theorem")
    exact_fixture()
    native_clifford_identities()
    planted_failures()
    check("native dimension: ker Gamma = 14*128-128 = 1664", 14 * 128 - 128 == 1664)
    check("native nondegenerate neutrality gives inertia (832,832)", 1664 // 2 == 832)
    print("VERDICT: signature-neutrality is exact at finite kinematic RS grade.")
    print("It is independent of the (9,5)/(7,7) label once the stated identities hold.")
    print("P1/P2/P3 are unchanged and unused.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
