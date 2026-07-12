#!/usr/bin/env python3
"""THREAD A4 -- ambient R^Y projection for constant-section Rperp_0.

RUN-375 / A3 computed the shape-operator commutator half of the
constant-section normal curvature term named by Thread A. This audit computes
the missing ambient projection half in the same symmetric-pair convention.

Geometry and convention.
  Y14 = Met(X4), with block metric
    G_{ij} = h_{ij}, G_{i alpha} = 0,
    G_{alpha beta} = DeWitt_h(S_alpha, S_beta).

At the flat constant section h = eta, the metric is base-independent, so the
mixed ambient Riemann component has a cheap exact block-Christoffel form:

    R^Y_{beta alpha i j}
      = -1/4 eta^{km} (S_beta_{ik} S_alpha_{mj}
                       - S_beta_{jk} S_alpha_{mi}).

Here alpha, beta are lower normal labels in the same coordinate tangent basis
used by A3: for a < b, S_(ab) = E_ab + E_ba.

Question.
  Does this ambient projection cancel the nonzero A3 shape-operator
  commutator piece, or does the full Ricci-equation normal curvature remain
  nonzero?

Answer.
  It remains nonzero. The ambient term has exactly the same support as the A3
  commutator, but it is not a uniform scalar multiple of it. The full
  commutator-plus-ambient tensor has nonzero support in every slot where A3
  fired. Therefore the full higher-codimension Willmore first variation still
  must carry Rperp_0; codimension-one intuition is still invalid.

Run: python tests/threads/A4_constant_section_rperp_ambient_projection.py
"""
from __future__ import annotations

from functools import cache

import sympy as sp

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


DIM = 4
eta = sp.diag(-1, 1, 1, 1)
eta_inv = eta
pairs = [(a, b) for a in range(DIM) for b in range(a, DIM)]
zero4 = sp.zeros(DIM, DIM)


def symmetric_pair_tangent(a: int, b: int) -> sp.Matrix:
    """Coordinate tangent S_(ab). Off-diagonal directions affect both entries."""
    mat = sp.zeros(DIM, DIM)
    mat[a, b] += 1
    mat[b, a] += 1
    if a == b:
        mat[a, b] = 1
    return mat


S = {pair: symmetric_pair_tangent(*pair) for pair in pairs}


def sym2(metric: sp.Matrix, i: int, j: int, k: int, ell: int) -> sp.Expr:
    return sp.Rational(1, 2) * (metric[i, k] * metric[j, ell] + metric[i, ell] * metric[j, k])


def B0(mu: int, nu: int, a: int, b: int) -> sp.Expr:
    """Constant-section vertical SFF from ii-s-coordinate-formula section 6.1."""
    return -sp.Rational(1, 2) * (
        sym2(eta, a, b, mu, nu) - sp.Rational(1, 2) * eta[a, b] * eta[mu, nu]
    )


@cache
def shape_operator(a: int, b: int) -> sp.Matrix:
    """A_(ab)^i_j = eta^{ik} B0(k,j,ab), with lower normal label (ab)."""
    return sp.Matrix(
        DIM,
        DIM,
        lambda i, j: sp.simplify(sum(eta_inv[i, k] * B0(k, j, a, b) for k in range(DIM))),
    )


def lower_first_tangent(mat: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(
        DIM,
        DIM,
        lambda i, j: sp.simplify(sum(eta[i, ell] * mat[ell, j] for ell in range(DIM))),
    )


@cache
def shape_commutator(alpha: tuple[int, int], beta: tuple[int, int]) -> sp.Matrix:
    A_alpha = shape_operator(*alpha)
    A_beta = shape_operator(*beta)
    return lower_first_tangent(sp.simplify(A_alpha * A_beta - A_beta * A_alpha))


@cache
def ambient_projection(alpha: tuple[int, int], beta: tuple[int, int]) -> sp.Matrix:
    """Ambient block Riemann lower component R^Y_{beta alpha i j}.

    This is G(R(e_i,e_j)n_alpha,n_beta) in the block-Christoffel convention
    used by the gimmel metric audit.
    """
    S_alpha = S[alpha]
    S_beta = S[beta]
    return sp.Matrix(
        DIM,
        DIM,
        lambda i, j: sp.simplify(
            -sp.Rational(1, 4)
            * sum(
                eta_inv[k, m] * (S_beta[i, k] * S_alpha[m, j] - S_beta[j, k] * S_alpha[m, i])
                for k in range(DIM)
                for m in range(DIM)
            )
        ),
    )


def nonzero_matrix_count(fn) -> int:
    return sum(1 for alpha in pairs for beta in pairs if fn(alpha, beta) != zero4)


def nonzero_entry_count(fn) -> int:
    total = 0
    for alpha in pairs:
        for beta in pairs:
            mat = fn(alpha, beta)
            total += sum(1 for entry in mat if sp.simplify(entry) != 0)
    return total


def supports_match() -> bool:
    for alpha in pairs:
        for beta in pairs:
            comm = shape_commutator(alpha, beta)
            amb = ambient_projection(alpha, beta)
            for i in range(DIM):
                for j in range(DIM):
                    if (comm[i, j] != 0) != (amb[i, j] != 0):
                        return False
    return True


print("[A4] constant-section Rperp_0 ambient-projection audit\n")

nonzero_comm_mats = nonzero_matrix_count(shape_commutator)
nonzero_amb_mats = nonzero_matrix_count(ambient_projection)
full = lambda alpha, beta: sp.simplify(shape_commutator(alpha, beta) + ambient_projection(alpha, beta))
nonzero_full_mats = nonzero_matrix_count(full)

check("A3 shape-operator commutator support is reproduced: 48 ordered normal-label matrices fire",
      nonzero_comm_mats == 48, f"observed {nonzero_comm_mats}")
check("ambient R^Y normal projection is nonzero on the same 48 ordered normal-label matrices",
      nonzero_amb_mats == 48 and supports_match(), f"observed {nonzero_amb_mats}")
check("full Ricci-equation normal curvature candidate remains nonzero on all 48 fired matrices",
      nonzero_full_mats == 48, f"observed {nonzero_full_mats}")
check("entry-level support is unchanged: commutator, ambient, and full tensors all have 96 nonzero entries",
      nonzero_entry_count(shape_commutator) == 96
      and nonzero_entry_count(ambient_projection) == 96
      and nonzero_entry_count(full) == 96)

# Minimal A3 witness: the ambient term over-cancels but leaves a nonzero residual.
alpha = (0, 0)
beta = (0, 1)
comm_witness = shape_commutator(alpha, beta)
amb_witness = ambient_projection(alpha, beta)
full_witness = full(alpha, beta)
expected_comm = sp.Matrix(
    [
        [0, sp.Rational(1, 8), 0, 0],
        [sp.Rational(-1, 8), 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
)
expected_amb = sp.Matrix(
    [
        [0, sp.Rational(-1, 4), 0, 0],
        [sp.Rational(1, 4), 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
)
expected_full = sp.Matrix(
    [
        [0, sp.Rational(-1, 8), 0, 0],
        [sp.Rational(1, 8), 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
)
print("    A3 witness C_{ij;(00)(01)}:")
print(comm_witness)
print("    ambient R^Y_{(01)(00)ij}:")
print(amb_witness)
print("    full candidate C + R^Y:")
print(full_witness)
check("A3 witness is reproduced exactly", comm_witness == expected_comm)
check("ambient witness is exact and nonzero", amb_witness == expected_amb)
check("full witness remains exact and nonzero", full_witness == expected_full)

# Not a uniform rescaling: the ambient term modifies the commutator differently
# in timelike/spacelike and diagonal/off-diagonal slots.
ambient_over_comm: set[sp.Expr] = set()
full_over_comm: set[sp.Expr] = set()
for alpha in pairs:
    for beta in pairs:
        comm = shape_commutator(alpha, beta)
        amb = ambient_projection(alpha, beta)
        fmat = sp.simplify(comm + amb)
        for i in range(DIM):
            for j in range(DIM):
                if comm[i, j] != 0:
                    ambient_over_comm.add(sp.simplify(amb[i, j] / comm[i, j]))
                    full_over_comm.add(sp.simplify(fmat[i, j] / comm[i, j]))

check("ambient term is not a uniform scalar multiple of the A3 commutator",
      ambient_over_comm == {sp.Integer(-4), sp.Integer(-2), sp.Integer(2), sp.Integer(4)},
      f"ambient/comm ratios = {sorted(ambient_over_comm, key=str)}")
check("full tensor is not cancelled and not a uniform rescaling",
      full_over_comm == {sp.Integer(-3), sp.Integer(-1), sp.Integer(3), sp.Integer(5)},
      f"full/comm ratios = {sorted(full_over_comm, key=str)}")

# Antisymmetry checks for the combined normal-curvature candidate.
antisym_normal = True
antisym_tangent = True
for alpha in pairs:
    for beta in pairs:
        F_ab = full(alpha, beta)
        F_ba = full(beta, alpha)
        if sp.simplify(F_ab + F_ba) != zero4:
            antisym_normal = False
        if sp.simplify(F_ab + F_ab.T) != zero4:
            antisym_tangent = False
check("full candidate is antisymmetric in normal labels", antisym_normal)
check("full candidate is antisymmetric in tangent labels after lowering the first tangent index",
      antisym_tangent)

print("\n[verdict]")
print("  The ambient R^Y normal projection is nonzero and has the same support as the")
print("  A3 shape-operator commutator. It does not cancel the commutator; it changes")
print("  the coefficients in a signature-sensitive way. Therefore the constant-section")
print("  normal curvature Rperp_0 remains a real O(M^0) term in the higher-codimension")
print("  Willmore first variation.")
print()
print("  Honest scope: this computes the Ricci-equation ambient projection at the flat")
print("  constant section and combines it with A3's commutator piece. It does not assemble")
print("  the full Willmore EL, choose H-class vs II-class, move OQ2-A, or change any claim")
print("  status or canon verdict.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = ambient projection computed; full Rperp_0 support remains nonzero.")
