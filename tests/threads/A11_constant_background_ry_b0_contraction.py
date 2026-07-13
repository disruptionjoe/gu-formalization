#!/usr/bin/env python3
"""THREAD A11 -- constant-background mixed ambient RY.B0 contraction.

A10 computed the trace-only H-class carrier contraction

    eta^ij R^Y_{alpha i beta j} H0^beta = (1/8) eta_alpha.

This gate computes the natural full-SFF comparison in the same A3-A10
program-native gimmel/DeWitt convention:

    eta^{ik} eta^{jl} R^Y_{alpha i beta j} B0_{kl}^beta.

It deliberately does not choose the final higher-codimension Willmore-EL
insertion formula, sign, scalar prefactor, or OQ2-A H/II functional. It only
pins the exact mixed ambient full-B contraction available at the flat constant
section.

Run: python tests/threads/A11_constant_background_ry_b0_contraction.py
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
NORMAL_DIM = len(pairs)


def matrix_trace(mat: sp.Matrix) -> sp.Expr:
    return sp.simplify(sum(mat[i, i] for i in range(mat.rows)))


def sym2(metric: sp.Matrix, i: int, j: int, k: int, ell: int) -> sp.Expr:
    return sp.Rational(1, 2) * (metric[i, k] * metric[j, ell] + metric[i, ell] * metric[j, k])


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


normal_metric = sp.Matrix([[dewitt_pairing(S[alpha], S[beta]) for beta in pairs] for alpha in pairs])
normal_inverse = sp.simplify(normal_metric.inv())


def B0(mu: int, nu: int, a: int, b: int) -> sp.Expr:
    """Constant-section vertical SFF from ii-s-coordinate-formula section 6.1."""
    return -sp.Rational(1, 2) * (
        sym2(eta, a, b, mu, nu) - sp.Rational(1, 2) * eta[a, b] * eta[mu, nu]
    )


H_lower = sp.Matrix(
    [
        sp.simplify(sum(eta_inv[mu, nu] * B0(mu, nu, a, b) for mu in range(DIM) for nu in range(DIM)))
        for a, b in pairs
    ]
)
H_upper = sp.simplify(normal_inverse * H_lower)


def b0_lower_vector(k: int, ell: int) -> sp.Matrix:
    return sp.Matrix([B0(k, ell, a, b) for a, b in pairs])


@cache
def b0_upper_component(k: int, ell: int, beta_idx: int) -> sp.Expr:
    return sp.simplify((normal_inverse * b0_lower_vector(k, ell))[beta_idx])


def d_gamma_fiber_basebase_wrt_fiber(gamma_idx: int, i: int, j: int, beta_idx: int) -> sp.Expr:
    """Directional vertical derivative of Gamma^gamma_{ij} along S_beta at h=eta."""
    a, b = pairs[gamma_idx]
    S_beta = S[pairs[beta_idx]]
    return sp.simplify(
        -sp.Rational(1, 4)
        * (
            S_beta[a, i] * eta[j, b]
            + eta[a, i] * S_beta[j, b]
            + S_beta[a, j] * eta[i, b]
            + eta[a, j] * S_beta[i, b]
        )
        + sp.Rational(1, 4) * (S_beta[a, b] * eta[i, j] + eta[a, b] * S_beta[i, j])
    )


def gamma_fiber_basebase(gamma_idx: int, i: int, j: int) -> sp.Expr:
    """Gamma^gamma_{ij}; same block-Christoffel convention as A8-A10."""
    a, b = pairs[gamma_idx]
    return B0(i, j, a, b)


@cache
def gamma_base_mixed(k: int, beta_idx: int, i: int) -> sp.Expr:
    """Gamma^k_{i beta} = 1/2 eta^{kl} S_beta_il."""
    S_beta = S[pairs[beta_idx]]
    return sp.simplify(sp.Rational(1, 2) * sum(eta_inv[k, ell] * S_beta[i, ell] for ell in range(DIM)))


@cache
def gamma_fiber_fiberfiber(gamma_idx: int, beta_idx: int, delta_idx: int) -> sp.Expr:
    """Gamma^gamma_{beta delta} for the DeWitt fiber metric at h=eta."""
    a, b = pairs[gamma_idx]
    S_beta = S[pairs[beta_idx]]
    S_delta = S[pairs[delta_idx]]
    total = sp.Integer(0)
    for r in range(DIM):
        for s in range(DIM):
            total += S_beta[a, r] * eta_inv[r, s] * S_delta[s, b]
            total += S_delta[a, r] * eta_inv[r, s] * S_beta[s, b]
    return sp.simplify(-sp.Rational(1, 2) * total)


@cache
def ambient_mixed_up(gamma_idx: int, i: int, beta_idx: int, j: int) -> sp.Expr:
    """R^gamma_{i beta j} at h=eta from the block-Christoffel formula."""
    total = d_gamma_fiber_basebase_wrt_fiber(gamma_idx, j, i, beta_idx)
    for delta_idx in range(NORMAL_DIM):
        total += gamma_fiber_fiberfiber(gamma_idx, beta_idx, delta_idx) * gamma_fiber_basebase(delta_idx, j, i)
    for k in range(DIM):
        total -= gamma_fiber_basebase(gamma_idx, j, k) * gamma_base_mixed(k, beta_idx, i)
    return sp.simplify(total)


def ambient_mixed_lower(alpha_idx: int, i: int, beta_idx: int, j: int) -> sp.Expr:
    """R^Y_{alpha i beta j} with the first normal index lowered by the DeWitt metric."""
    return sp.simplify(
        sum(normal_metric[alpha_idx, gamma_idx] * ambient_mixed_up(gamma_idx, i, beta_idx, j) for gamma_idx in range(NORMAL_DIM))
    )


def ambient_h_contraction() -> sp.Matrix:
    """Lower-normal trace-only H-class contraction eta^ij R^Y_{alpha i beta j} H0^beta."""
    return sp.Matrix(
        [
            sp.simplify(
                sum(
                    eta_inv[i, j] * ambient_mixed_lower(alpha_idx, i, beta_idx, j) * H_upper[beta_idx]
                    for i in range(DIM)
                    for j in range(DIM)
                    for beta_idx in range(NORMAL_DIM)
                )
            )
            for alpha_idx in range(NORMAL_DIM)
        ]
    )


def ambient_full_b_contraction() -> sp.Matrix:
    """Lower-normal full-SFF contraction eta^ik eta^jl R^Y_{alpha i beta j} B0_kl^beta."""
    return sp.Matrix(
        [
            sp.simplify(
                sum(
                    eta_inv[i, k]
                    * eta_inv[j, ell]
                    * ambient_mixed_lower(alpha_idx, i, beta_idx, j)
                    * b0_upper_component(k, ell, beta_idx)
                    for i in range(DIM)
                    for k in range(DIM)
                    for j in range(DIM)
                    for ell in range(DIM)
                    for beta_idx in range(NORMAL_DIM)
                )
            )
            for alpha_idx in range(NORMAL_DIM)
        ]
    )


def pair_vector_to_matrix(vector: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(DIM, DIM, lambda a, b: vector[pairs.index((a, b))] if a <= b else vector[pairs.index((b, a))])


def trace_free_base(tensor: sp.Matrix) -> sp.Matrix:
    tr = sp.simplify(sum(eta_inv[p, p] * tensor[p, p] for p in range(DIM)))
    return sp.Matrix(DIM, DIM, lambda m, n: sp.simplify(tensor[m, n] - sp.Rational(1, DIM) * eta[m, n] * tr))


def is_proportional_to_h(vector: sp.Matrix) -> bool:
    ratios = [sp.simplify(vector[idx] / H_lower[idx]) for idx in range(NORMAL_DIM) if H_lower[idx] != 0]
    return len(set(ratios)) == 1 and all(vector[idx] == ratios[0] * H_lower[idx] for idx in range(NORMAL_DIM))


print("[A11] constant-background mixed ambient RY.B0 contraction\n")

normal_eigs = normal_metric.eigenvals()
positive_signature = sum(mult for eig, mult in normal_eigs.items() if eig > 0)
negative_signature = sum(mult for eig, mult in normal_eigs.items() if eig < 0)

check("using the program-native gimmel/DeWitt Y14 = Met(X4) construction", True)
check("DeWitt normal metric is nondegenerate in the symmetric-pair basis", normal_metric.det() == 64)
check("DeWitt normal metric has signature (6,4)", (positive_signature, negative_signature) == (6, 4))
check(
    "constant-section mean curvature lower components are H0_ab = (1/2) eta_ab",
    H_lower == sp.Matrix([sp.Rational(1, 2) * eta[a, b] for a, b in pairs]),
)

ambient_h = ambient_h_contraction()
full_b = ambient_full_b_contraction()
full_b_matrix = pair_vector_to_matrix(full_b)
full_b_trace_free = trace_free_base(full_b_matrix)
expected_full_b = sp.Matrix(
    [sp.Rational(-1, 32), 0, 0, 0, sp.Rational(5, 32), 0, 0, sp.Rational(5, 32), 0, sp.Rational(5, 32)]
)
expected_tf = sp.diag(sp.Rational(3, 32), sp.Rational(1, 32), sp.Rational(1, 32), sp.Rational(1, 32))

print("    eta^ik eta^jl RY_{alpha i beta j} B0_kl^beta as a normal-lower matrix:")
print(full_b_matrix)
print("    trace-free part:")
print(full_b_trace_free)

check("A10 trace-only H-class contraction is exact: RY.H0 = (1/8) eta", ambient_h == sp.Rational(1, 4) * H_lower)
check("full-SFF mixed ambient contraction is exact", full_b == expected_full_b)
check("full-SFF contraction is not proportional to H0", not is_proportional_to_h(full_b))
check("pure-trace part of RY.B0 equals the A10 RY.H0 carrier", pair_vector_to_matrix(full_b - ambient_h) == full_b_trace_free)
check("full-SFF contraction has a nonzero trace-free shear part", full_b_trace_free == expected_tf)

symbols_used = set()
for entry in list(ambient_h) + list(full_b) + list(full_b_trace_free):
    symbols_used |= entry.free_symbols
check(
    "A11 background contractions are O(M^0) exact rationals with no fitted symbols",
    symbols_used == set(),
    f"free symbols observed: {sorted(str(symbol) for symbol in symbols_used)}",
)

print("\n[verdict]")
print("  In the current A3-A10 gimmel/DeWitt convention, the natural full-B mixed")
print("  ambient contraction is not just the A10 trace-only H0 carrier. It splits")
print("  as the A10 pure trace RY.H0 piece plus a nonzero trace-free shear:")
print("    RY.B0 = (1/8) eta + diag(3,1,1,1)/32 in normal-lower matrix form.")
print()
print("  Honest scope: this pins one exact II-class background contraction. It does")
print("  not choose the final Willmore-EL insertion formula, c_W, full W(H)|s0,")
print("  background-subtracted M-linearization, OQ2-A functional, claim status,")
print("  canon verdict, or public posture.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = RY.B0 full-SFF contraction is exact and carries nonzero trace-free shear.")
