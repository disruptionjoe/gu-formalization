#!/usr/bin/env python3
"""THREAD A5 -- exact invariants of constant-section Rperp_0.

A3 computed the shape-operator commutator piece of the constant-section normal
curvature term. A4 added the ambient R^Y normal projection and showed that the
full support remains nonzero.

This gate asks a sharper invariant question:

    Is the full commutator-plus-ambient Rperp_0 tensor non-null under the actual
    DeWitt normal metric on Sym^2(T*X), and how do the two pieces interact under
    that contraction?

Answer:
    The DeWitt normal metric in the A3/A4 symmetric-pair basis has signature
    (6,4). With tangent indices raised by eta and normal labels raised by the
    inverse DeWitt metric, the raw scalar contractions are

        <comm, comm> = 27/64
        <ambient, ambient> = 9/4
        <comm, ambient> = 0
        <full, full> = 171/64

So the full constant-section Rperp_0 tensor is non-null, and the A3/A4 split is
orthogonal under the metric contraction used by the eventual background
Willmore-EL assembly. This is still not the full EL and does not choose OQ2-A.

Run: python tests/threads/A5_constant_section_rperp_invariants.py
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


def matrix_trace(mat: sp.Matrix) -> sp.Expr:
    return sp.simplify(sum(mat[i, i] for i in range(mat.rows)))


def symmetric_pair_tangent(a: int, b: int) -> sp.Matrix:
    """Coordinate tangent S_(ab). Off-diagonal directions affect both entries."""
    mat = sp.zeros(DIM, DIM)
    mat[a, b] += 1
    mat[b, a] += 1
    if a == b:
        mat[a, b] = 1
    return mat


S = {pair: symmetric_pair_tangent(*pair) for pair in pairs}


def dewitt_pairing(first: sp.Matrix, second: sp.Matrix) -> sp.Expr:
    """Trace-reversed Frobenius pairing at h=eta on symmetric 2-tensors."""
    return sp.simplify(
        matrix_trace(eta_inv * first * eta_inv * second)
        - sp.Rational(1, 2) * matrix_trace(eta_inv * first) * matrix_trace(eta_inv * second)
    )


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
    """Ambient block Riemann lower component R^Y_{beta alpha i j}."""
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


@cache
def full_rperp(alpha: tuple[int, int], beta: tuple[int, int]) -> sp.Matrix:
    return sp.simplify(shape_commutator(alpha, beta) + ambient_projection(alpha, beta))


def nonzero_entries(fn) -> list[tuple[int, int, int, int, sp.Expr]]:
    entries: list[tuple[int, int, int, int, sp.Expr]] = []
    for alpha_idx, alpha in enumerate(pairs):
        for beta_idx, beta in enumerate(pairs):
            mat = fn(alpha, beta)
            for i in range(DIM):
                for j in range(DIM):
                    value = sp.simplify(mat[i, j])
                    if value != 0:
                        entries.append((i, j, alpha_idx, beta_idx, value))
    return entries


def tensor_inner(first_fn, second_fn, normal_inverse: sp.Matrix) -> sp.Expr:
    """Raw contraction eta^ik eta^jl V^alpha,gamma V^beta,delta F_ij,ab G_kl,gd."""
    first_entries = nonzero_entries(first_fn)
    second_entries = nonzero_entries(second_fn)
    total = sp.Integer(0)
    for i, j, alpha_idx, beta_idx, first_value in first_entries:
        for k, ell, gamma_idx, delta_idx, second_value in second_entries:
            total += (
                eta_inv[i, k]
                * eta_inv[j, ell]
                * normal_inverse[alpha_idx, gamma_idx]
                * normal_inverse[beta_idx, delta_idx]
                * first_value
                * second_value
            )
    return sp.simplify(total)


def nonzero_matrix_count(fn) -> int:
    return sum(1 for alpha in pairs for beta in pairs if fn(alpha, beta) != zero4)


print("[A5] constant-section Rperp_0 invariant audit\n")

normal_metric = sp.Matrix([[dewitt_pairing(S[alpha], S[beta]) for beta in pairs] for alpha in pairs])
normal_inverse = sp.simplify(normal_metric.inv())
normal_eigs = normal_metric.eigenvals()
positive_signature = sum(mult for eig, mult in normal_eigs.items() if eig > 0)
negative_signature = sum(mult for eig, mult in normal_eigs.items() if eig < 0)

check("DeWitt normal metric on Sym^2(T*X) is nondegenerate in the A3/A4 symmetric-pair basis",
      normal_metric.det() == 64)
check("DeWitt normal metric has signature (6,4), matching the GU gimmel fiber",
      (positive_signature, negative_signature) == (6, 4),
      f"observed {(positive_signature, negative_signature)}")
check("normal inverse is exact",
      sp.simplify(normal_metric * normal_inverse - sp.eye(len(pairs))) == sp.zeros(len(pairs)))

comm_norm = tensor_inner(shape_commutator, shape_commutator, normal_inverse)
ambient_norm = tensor_inner(ambient_projection, ambient_projection, normal_inverse)
cross_norm = tensor_inner(shape_commutator, ambient_projection, normal_inverse)
full_norm = tensor_inner(full_rperp, full_rperp, normal_inverse)

print("    raw DeWitt/tangent contractions:")
print(f"      <commutator, commutator> = {comm_norm}")
print(f"      <ambient, ambient>       = {ambient_norm}")
print(f"      <commutator, ambient>    = {cross_norm}")
print(f"      <full, full>             = {full_norm}")

check("A3 commutator piece has nonzero raw contraction 27/64", comm_norm == sp.Rational(27, 64))
check("A4 ambient-projection piece has nonzero raw contraction 9/4", ambient_norm == sp.Rational(9, 4))
check("A3 commutator and A4 ambient pieces are orthogonal under the DeWitt/tangent contraction",
      cross_norm == 0)
check("full Rperp_0 tensor is non-null: raw contraction is 171/64",
      full_norm == sp.Rational(171, 64))
check("full contraction equals the orthogonal sum of the two pieces",
      full_norm == sp.simplify(comm_norm + ambient_norm + 2 * cross_norm))

check("full support remains the A4 48 ordered normal-label matrices / 96 entries",
      nonzero_matrix_count(full_rperp) == 48 and len(nonzero_entries(full_rperp)) == 96,
      f"matrices={nonzero_matrix_count(full_rperp)}, entries={len(nonzero_entries(full_rperp))}")

value_set = sorted({entry[-1] for entry in nonzero_entries(full_rperp)}, key=lambda value: float(value))
expected_values = [
    sp.Rational(-3, 8),
    sp.Rational(-5, 16),
    sp.Rational(-3, 16),
    sp.Rational(-1, 8),
    sp.Rational(1, 8),
    sp.Rational(3, 16),
    sp.Rational(5, 16),
    sp.Rational(3, 8),
]
check("full tensor keeps signature-sensitive coefficient values, not one uniform rescaling",
      value_set == expected_values,
      f"values={value_set}")

tangent_wedge_ranks = {}
span_columns = []
for i in range(DIM):
    for j in range(i + 1, DIM):
        normal_matrix = sp.Matrix([[full_rperp(alpha, beta)[i, j] for beta in pairs] for alpha in pairs])
        tangent_wedge_ranks[(i, j)] = normal_matrix.rank()
        span_columns.append(sp.Matrix(list(normal_matrix)))

span_rank = sp.Matrix.hstack(*span_columns).rank()
check("each tangent two-plane sees a rank-6 normal-curvature skew matrix",
      set(tangent_wedge_ranks.values()) == {6},
      f"ranks={tangent_wedge_ranks}")
check("the six tangent wedge components are linearly independent as normal-curvature matrices",
      span_rank == 6,
      f"span rank={span_rank}")

print("\n[verdict]")
print("  With the actual DeWitt normal metric on Sym^2(T*X), the full constant-section")
print("  Rperp_0 tensor is not merely support-nonzero: it is non-null under the raw")
print("  tangent-plus-normal contraction. The A3 shape commutator and A4 ambient")
print("  projection pieces are orthogonal under that contraction, so the full scalar")
print("  invariant is their sum, 171/64.")
print()
print("  Honest scope: this is an invariant summary of the constant-section Rperp_0")
print("  tensor. It does not assemble Delta^perp H0, Simons stress, or the full")
print("  background Willmore EL; it does not choose H-class vs II-class or move OQ2-A.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = full constant-section Rperp_0 is DeWitt-non-null and A3/A4 split is orthogonal.")
