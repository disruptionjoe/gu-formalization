#!/usr/bin/env python3
"""THREAD A8 -- constant-section Delta^perp H0 gate.

A7 named the normal-connection Laplacian of the constant-section mean curvature
as the first still-open background slot before the higher-codimension Willmore
EL can be assembled.

This gate checks the flat constant section of Y14 = Met(X4) with the same
trace-reversed DeWitt normal metric used by A3-A7. The block metric is

    G_ij = h_ij,     G_i alpha = 0,
    G_alpha beta = DeWitt_h(S_alpha, S_beta).

At h = eta and with base-independent coordinates, the normal-normal base
connection block Gamma^beta_{i alpha} vanishes. The mixed ambient block
Gamma^k_{i alpha} is nonzero, so this is not claiming the ambient derivative
of H0 is zero. It says the normal projection is zero:

    nabla_i^perp H0 = 0, hence Delta^perp H0 = 0.

Run: python tests/threads/A8_constant_section_delta_perp_h0.py
"""
from __future__ import annotations

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


def B0(mu: int, nu: int, a: int, b: int) -> sp.Expr:
    """Constant-section vertical SFF from ii-s-coordinate-formula section 6.1."""
    return -sp.Rational(1, 2) * (
        sym2(eta, a, b, mu, nu) - sp.Rational(1, 2) * eta[a, b] * eta[mu, nu]
    )


normal_metric = sp.Matrix([[dewitt_pairing(S[alpha], S[beta]) for beta in pairs] for alpha in pairs])
normal_inverse = sp.simplify(normal_metric.inv())


def gamma_tangent(k: int, i: int, alpha: tuple[int, int]) -> sp.Expr:
    """Mixed ambient block Gamma^k_{i alpha} = 1/2 eta^{kl} S_alpha_il."""
    return sp.simplify(sp.Rational(1, 2) * sum(eta_inv[k, ell] * S[alpha][i, ell] for ell in range(DIM)))


def d_base_vertical_metric(_i: int, _alpha_idx: int, _beta_idx: int) -> sp.Expr:
    """Base derivative of G_{alpha beta}; zero at the constant flat section."""
    return sp.Integer(0)


def d_vertical_cross_metric(_alpha_idx: int, _i: int, _beta_idx: int) -> sp.Expr:
    """Vertical derivative of G_{i beta}; zero because the block metric has no cross term."""
    return sp.Integer(0)


def gamma_normal(gamma_idx: int, i: int, alpha_idx: int) -> sp.Expr:
    """Normal-normal base block Gamma^gamma_{i alpha} from the block Christoffel formula."""
    total = sp.Integer(0)
    for delta_idx in range(len(pairs)):
        total += normal_inverse[gamma_idx, delta_idx] * (
            d_base_vertical_metric(i, alpha_idx, delta_idx)
            + d_vertical_cross_metric(alpha_idx, i, delta_idx)
            - d_vertical_cross_metric(delta_idx, i, alpha_idx)
        )
    return sp.simplify(sp.Rational(1, 2) * total)


H_lower = sp.Matrix(
    [
        sp.simplify(sum(eta_inv[mu, nu] * B0(mu, nu, a, b) for mu in range(DIM) for nu in range(DIM)))
        for a, b in pairs
    ]
)
H_upper = sp.simplify(normal_inverse * H_lower)


def normal_derivative_h(i: int, gamma_idx: int) -> sp.Expr:
    """Upper normal components of nabla_i^perp H0."""
    return sp.simplify(sum(gamma_normal(gamma_idx, i, beta_idx) * H_upper[beta_idx] for beta_idx in range(len(pairs))))


def second_normal_derivative_h(i: int, j: int, gamma_idx: int) -> sp.Expr:
    """Upper normal components of nabla_i^perp nabla_j^perp H0."""
    first = [normal_derivative_h(j, beta_idx) for beta_idx in range(len(pairs))]
    return sp.simplify(sum(gamma_normal(gamma_idx, i, beta_idx) * first[beta_idx] for beta_idx in range(len(pairs))))


def delta_perp_h(gamma_idx: int) -> sp.Expr:
    """Rough normal Laplacian in upper normal components; sign convention is irrelevant for zero."""
    return sp.simplify(
        sum(eta_inv[i, j] * second_normal_derivative_h(i, j, gamma_idx) for i in range(DIM) for j in range(DIM))
    )


def ambient_tangent_derivative_h(i: int, k: int) -> sp.Expr:
    """Tangential part of the ambient derivative nabla_i^Y H0."""
    return sp.simplify(sum(gamma_tangent(k, i, alpha) * H_upper[alpha_idx] for alpha_idx, alpha in enumerate(pairs)))


print("[A8] constant-section Delta^perp H0 gate\n")

normal_eigs = normal_metric.eigenvals()
positive_signature = sum(mult for eig, mult in normal_eigs.items() if eig > 0)
negative_signature = sum(mult for eig, mult in normal_eigs.items() if eig < 0)

check("DeWitt normal metric is nondegenerate in the symmetric-pair basis", normal_metric.det() == 64)
check("DeWitt normal metric has signature (6,4)", (positive_signature, negative_signature) == (6, 4))

H_expected = sp.Matrix([sp.Rational(1, 2) * eta[a, b] for a, b in pairs])
check("constant-section mean curvature lower components are H0_ab = (1/2) eta_ab", H_lower == H_expected)
check("raising H0 with the DeWitt inverse is exact", normal_metric * H_upper == H_lower)

normal_connection_entries = [
    gamma_normal(gamma_idx, i, alpha_idx)
    for gamma_idx in range(len(pairs))
    for i in range(DIM)
    for alpha_idx in range(len(pairs))
]
check("normal-normal base connection block Gamma^beta_{i alpha} vanishes",
      all(entry == 0 for entry in normal_connection_entries))

tangent_entries = [
    gamma_tangent(k, i, alpha)
    for k in range(DIM)
    for i in range(DIM)
    for alpha in pairs
    if gamma_tangent(k, i, alpha) != 0
]
check("mixed ambient block Gamma^k_{i alpha} is nonzero in exactly 16 entries",
      len(tangent_entries) == 16, f"observed {len(tangent_entries)}")
check("mixed ambient block entries are exactly +/-1/2",
      set(tangent_entries) == {sp.Rational(-1, 2), sp.Rational(1, 2)})

ambient_tangent = sp.Matrix(DIM, DIM, lambda i, k: ambient_tangent_derivative_h(i, k))
print("    tangential part of nabla_i^Y H0:")
print(ambient_tangent)
check("ambient derivative of H0 has nonzero tangential Weingarten part -1/4 delta_i^k",
      ambient_tangent == -sp.Rational(1, 4) * sp.eye(DIM))

first_normal = sp.Matrix(DIM, len(pairs), lambda i, alpha_idx: normal_derivative_h(i, alpha_idx))
laplacian = sp.Matrix([delta_perp_h(alpha_idx) for alpha_idx in range(len(pairs))])

check("normal covariant derivative of H0 vanishes: nabla^perp H0 = 0",
      first_normal == sp.zeros(DIM, len(pairs)))
check("normal Laplacian slot vanishes: Delta^perp H0 = 0",
      laplacian == sp.zeros(len(pairs), 1))

symbols_used = set()
for entry in list(first_normal) + list(laplacian) + list(ambient_tangent):
    symbols_used |= entry.free_symbols
check("A8 is an O(M^0) exact background computation with no fitted symbols",
      symbols_used == set(),
      f"free symbols observed: {sorted(str(symbol) for symbol in symbols_used)}")

print("\n[verdict]")
print("  In the flat constant-section DeWitt/gimmel block metric, the normal-normal")
print("  base connection Gamma^beta_{i alpha} vanishes. H0 is constant in this")
print("  normal frame, so nabla^perp H0 = 0 and Delta^perp H0 = 0.")
print()
print("  This is not a claim that the ambient derivative of H0 vanishes: its tangential")
print("  Weingarten part is -1/4 delta_i^k. That tangential piece belongs to the shape")
print("  terms, not to the normal Laplacian slot.")
print()
print("  Honest scope: this closes only A7's Delta^perp H0 background slot. The Rperp_0")
print("  EL insertion, ambient RY.H0/B0 term, full W(H)|s0 assembly, M-linearization,")
print("  and OQ2-A selection remain open.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = constant-section Delta^perp H0 vanishes; full background EL remains open.")
