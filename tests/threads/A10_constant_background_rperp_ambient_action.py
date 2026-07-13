#!/usr/bin/env python3
"""THREAD A10 -- constant-background Rperp/H0 and ambient RY.H0 action.

A9 named the next Thread A frontier as the actual Rperp_0 insertion plus the
ambient R^Y.H0/B0 assembly. This gate advances the part whose contraction is
already fixed by the A3-A9 program-native gimmel/DeWitt convention:

  * Rperp_0 is the A5 commutator-plus-ambient normal-curvature tensor.
  * H0 is the constant-section mean-curvature normal carrier, H0_ab = 1/2 eta_ab.
  * The mixed ambient H-class contraction is
        T_alpha = eta^ij R^Y_{alpha i beta j} H0^beta.

It deliberately does not invent the II-class R^Y.B0 contraction or the scalar
Willmore prefactor c_W. Those remain the next fork until the local EL formula is
pinned.

Run: python tests/threads/A10_constant_background_rperp_ambient_action.py
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
zero4 = sp.zeros(DIM, DIM)


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
    return lower_first_tangent(
        sp.simplify(shape_operator(*alpha) * shape_operator(*beta) - shape_operator(*beta) * shape_operator(*alpha))
    )


@cache
def ambient_projection(alpha: tuple[int, int], beta: tuple[int, int]) -> sp.Matrix:
    """Ambient block Riemann lower component R^Y_{beta alpha i j} from A4."""
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


def rperp_action_on_h(i: int, j: int) -> sp.Matrix:
    """Lower-normal vector Rperp_0(e_i,e_j).H0 in the A5 convention."""
    return sp.Matrix(
        [
            sp.simplify(sum(full_rperp(alpha, beta)[i, j] * H_upper[beta_idx] for beta_idx, beta in enumerate(pairs)))
            for alpha in pairs
        ]
    )


def nonzero_rperp_matrix_count() -> int:
    return sum(1 for alpha in pairs for beta in pairs if full_rperp(alpha, beta) != zero4)


def gamma_fiber_basebase(gamma_idx: int, i: int, j: int) -> sp.Expr:
    """Gamma^gamma_{ij}; same block-Christoffel convention as A8."""
    a, b = pairs[gamma_idx]
    return B0(i, j, a, b)


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
    """Lower-normal H-class contraction eta^ij R^Y_{alpha i beta j} H0^beta."""
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


def pair_vector_to_matrix(vector: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(DIM, DIM, lambda a, b: vector[pairs.index((a, b))] if a <= b else vector[pairs.index((b, a))])


def trace_free_base(tensor: sp.Matrix) -> sp.Matrix:
    tr = sp.simplify(sum(eta_inv[p, p] * tensor[p, p] for p in range(DIM)))
    return sp.Matrix(DIM, DIM, lambda m, n: sp.simplify(tensor[m, n] - sp.Rational(1, DIM) * eta[m, n] * tr))


def base_trace_free_sff_is_nonzero() -> bool:
    H_matrix = pair_vector_to_matrix(H_lower)
    for m in range(DIM):
        for n in range(DIM):
            for a in range(DIM):
                for b in range(DIM):
                    value = sp.simplify(B0(m, n, a, b) - sp.Rational(1, DIM) * eta[m, n] * H_matrix[a, b])
                    if value != 0:
                        return True
    return False


print("[A10] constant-background Rperp/H0 and ambient RY.H0 action\n")

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
check("raising H0 with the DeWitt inverse is exact", normal_metric * H_upper == H_lower)

rperp_actions = [rperp_action_on_h(i, j) for i in range(DIM) for j in range(DIM)]
check(
    "A5 full Rperp_0 tensor is still nonzero on 48 ordered normal-label matrices",
    nonzero_rperp_matrix_count() == 48,
)
check(
    "direct normal-curvature action Rperp_0(e_i,e_j).H0 vanishes for every tangent wedge",
    all(action == sp.zeros(NORMAL_DIM, 1) for action in rperp_actions),
)

ambient_h = ambient_h_contraction()
ambient_h_matrix = pair_vector_to_matrix(ambient_h)
print("    eta^ij RY_{alpha i beta j} H0^beta as a normal-lower matrix:")
print(ambient_h_matrix)
check(
    "mixed ambient H-class contraction is exact: RY.H0 = (1/8) eta = (1/4) H0",
    ambient_h == sp.Rational(1, 4) * H_lower,
)
check(
    "mixed ambient H-class contraction is pure trace, so its trace-free part vanishes",
    trace_free_base(ambient_h_matrix) == sp.zeros(DIM, DIM),
)
check(
    "B0 still has nonzero base-trace-free shear, so RY.B0 is a distinct II-class fork",
    base_trace_free_sff_is_nonzero(),
)

symbols_used = set()
for entry in list(ambient_h) + [entry for action in rperp_actions for entry in list(action)]:
    symbols_used |= entry.free_symbols
check(
    "A10 background contractions are O(M^0) exact rationals with no fitted symbols",
    symbols_used == set(),
    f"free symbols observed: {sorted(str(symbol) for symbol in symbols_used)}",
)

print("\n[verdict]")
print("  In the current A3-A9 gimmel/DeWitt convention, the full nonzero Rperp_0")
print("  tensor annihilates the isotropic H0 carrier under the direct normal-curvature")
print("  endomorphism action. The mixed ambient H-class contraction is not zero, but")
print("  it is pure trace: RY.H0 = (1/8) eta = (1/4) H0, so it contributes no")
print("  trace-free background obstruction by itself.")
print()
print("  Honest scope: this computes the pinned H0 carrier contractions only. It does")
print("  not invent the II-class RY.B0 contraction, choose c_W, assemble full W(H)|s0,")
print("  move OQ2-A, or change claim status, canon verdicts, or public posture.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = Rperp_0.H0 vanishes and RY.H0 is pure trace; II-class RY.B0 remains open.")
