#!/usr/bin/env python3
"""THREAD A12 -- constant-background coefficient-family assembly gate.

A11 pinned the natural full-SFF mixed ambient contraction RY.B0. This gate
assembles the computed A6/A8/A10/A11 background pieces into a formal coefficient
family for the still-open W(H)|s0 residual:

    F0 =
        q_Q * Q^TF(B0)
      + q_D * Delta^perp H0
      + q_R * Rperp_0.H0
      + c_H * (RY.H0)
      + c_B * (RY.B0).

The coefficients are deliberately symbolic. A12 does not choose the final
higher-codimension Willmore-EL formula, sign, scalar prefactor c_W, or OQ2-A
H/II branch. It only shows which already-computed slots can carry a trace-free
constant-background term.

Run: python tests/threads/A12_constant_background_coefficient_family.py
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


def B0_pair(mu: int, nu: int, alpha_idx: int) -> sp.Expr:
    a, b = pairs[alpha_idx]
    return B0(mu, nu, a, b)


H_lower = sp.Matrix(
    [
        sp.simplify(sum(eta_inv[mu, nu] * B0(mu, nu, a, b) for mu in range(DIM) for nu in range(DIM)))
        for a, b in pairs
    ]
)
H_upper = sp.simplify(normal_inverse * H_lower)


def pair_vector_to_matrix(vector: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(DIM, DIM, lambda a, b: vector[pairs.index((a, b))] if a <= b else vector[pairs.index((b, a))])


def trace_free_base(tensor: sp.Matrix) -> sp.Matrix:
    tr = sp.simplify(sum(eta_inv[p, p] * tensor[p, p] for p in range(DIM)))
    return sp.Matrix(DIM, DIM, lambda m, n: sp.simplify(tensor[m, n] - sp.Rational(1, DIM) * eta[m, n] * tr))


def build_qtf_dewitt_pair() -> sp.Matrix:
    """A6 exact symmetric-pair DeWitt Simons stress, represented as a base matrix."""

    def hatB(m: int, n: int, alpha_idx: int) -> sp.Expr:
        return sp.simplify(B0_pair(m, n, alpha_idx) - sp.Rational(1, DIM) * eta[m, n] * H_lower[alpha_idx])

    q_matrix = sp.zeros(DIM, DIM)
    for m in range(DIM):
        for n in range(DIM):
            linear_h = sp.Rational(1, 2) * sum(H_upper[alpha_idx] * hatB(m, n, alpha_idx) for alpha_idx in range(NORMAL_DIM))
            quadratic = sp.Integer(0)
            for p in range(DIM):
                for q in range(DIM):
                    for alpha_idx in range(NORMAL_DIM):
                        for beta_idx in range(NORMAL_DIM):
                            quadratic += (
                                eta_inv[p, q]
                                * normal_inverse[alpha_idx, beta_idx]
                                * hatB(m, p, alpha_idx)
                                * hatB(q, n, beta_idx)
                            )
            q_matrix[m, n] = sp.simplify(linear_h - quadratic)
    return trace_free_base(q_matrix)


def d_base_vertical_metric(_i: int, _alpha_idx: int, _beta_idx: int) -> sp.Expr:
    """Base derivative of G_{alpha beta}; zero at the constant flat section."""
    return sp.Integer(0)


def d_vertical_cross_metric(_alpha_idx: int, _i: int, _beta_idx: int) -> sp.Expr:
    """Vertical derivative of G_{i beta}; zero because the block metric has no cross term."""
    return sp.Integer(0)


def gamma_normal(gamma_idx: int, i: int, alpha_idx: int) -> sp.Expr:
    """Normal-normal base block Gamma^gamma_{i alpha} from the block Christoffel formula."""
    total = sp.Integer(0)
    for delta_idx in range(NORMAL_DIM):
        total += normal_inverse[gamma_idx, delta_idx] * (
            d_base_vertical_metric(i, alpha_idx, delta_idx)
            + d_vertical_cross_metric(alpha_idx, i, delta_idx)
            - d_vertical_cross_metric(delta_idx, i, alpha_idx)
        )
    return sp.simplify(sp.Rational(1, 2) * total)


def delta_perp_h_matrix() -> sp.Matrix:
    """A8 normal Laplacian slot, represented as a normal-lower matrix."""
    normal_connection_entries = [
        gamma_normal(gamma_idx, i, alpha_idx)
        for gamma_idx in range(NORMAL_DIM)
        for i in range(DIM)
        for alpha_idx in range(NORMAL_DIM)
    ]
    if any(entry != 0 for entry in normal_connection_entries):
        raise AssertionError("unexpected nonzero normal connection")
    return zero4


@cache
def shape_operator(a: int, b: int) -> sp.Matrix:
    """A_(ab)^i_j = eta^{ik} B0(k,j,ab), with lower normal label (ab)."""
    return sp.Matrix(
        DIM,
        DIM,
        lambda i, j: sp.simplify(sum(eta_inv[i, k] * B0(k, j, a, b) for k in range(DIM))),
    )


def lower_first_tangent(mat: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(DIM, DIM, lambda i, j: sp.simplify(sum(eta[i, ell] * mat[ell, j] for ell in range(DIM))))


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
    """Lower-normal vector Rperp_0(e_i,e_j).H0 in the A5/A10 convention."""
    return sp.Matrix(
        [
            sp.simplify(sum(full_rperp(alpha, beta)[i, j] * H_upper[beta_idx] for beta_idx, beta in enumerate(pairs)))
            for alpha in pairs
        ]
    )


def rperp_direct_h_matrix() -> sp.Matrix:
    actions = [rperp_action_on_h(i, j) for i in range(DIM) for j in range(DIM)]
    if any(action != sp.zeros(NORMAL_DIM, 1) for action in actions):
        raise AssertionError("unexpected nonzero direct Rperp_0.H0 action")
    return zero4


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
    """Gamma^gamma_{ij}; same block-Christoffel convention as A8-A11."""
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


print("[A12] constant-background coefficient-family assembly gate\n")

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

qtf_matrix = build_qtf_dewitt_pair()
delta_matrix = delta_perp_h_matrix()
rperp_direct_matrix = rperp_direct_h_matrix()
ambient_h_matrix = pair_vector_to_matrix(ambient_h_contraction())
ambient_full_b_matrix = pair_vector_to_matrix(ambient_full_b_contraction())

expected_ambient_h = sp.Rational(1, 8) * eta
expected_full_b = sp.diag(sp.Rational(-1, 32), sp.Rational(5, 32), sp.Rational(5, 32), sp.Rational(5, 32))
expected_full_b_tf = sp.diag(sp.Rational(3, 32), sp.Rational(1, 32), sp.Rational(1, 32), sp.Rational(1, 32))

check("A6 exact DeWitt Q^TF(B0) slot vanishes", qtf_matrix == zero4)
check("A8 Delta^perp H0 slot vanishes", delta_matrix == zero4)
check("A10 direct Rperp_0.H0 carrier action vanishes", rperp_direct_matrix == zero4)
check("A10 H-class ambient carrier is pure trace: RY.H0 = (1/8) eta", ambient_h_matrix == expected_ambient_h)
check("A11 full-B ambient carrier is exact: RY.B0 = diag(-1,5,5,5)/32", ambient_full_b_matrix == expected_full_b)
check("A11 full-B ambient carrier has trace-free shear", trace_free_base(ambient_full_b_matrix) == expected_full_b_tf)

q_Q, q_D, q_R, c_H, c_B = sp.symbols("q_Q q_D q_R c_H c_B")
family = sp.simplify(
    q_Q * qtf_matrix
    + q_D * delta_matrix
    + q_R * rperp_direct_matrix
    + c_H * ambient_h_matrix
    + c_B * ambient_full_b_matrix
)
trace_free_family = trace_free_base(family)
expected_family = sp.simplify(c_H * expected_ambient_h + c_B * expected_full_b)
expected_trace_free_family = c_B * expected_full_b_tf

print("    formal computed-slot family F0:")
print(family)
print("    trace-free family TF(F0):")
print(trace_free_family)

check("computed-slot family reduces to c_H RY.H0 plus c_B RY.B0", family == expected_family)
check("H-class ambient coefficient contributes no trace-free background term", trace_free_base(c_H * ambient_h_matrix) == zero4)
check("trace-free computed family depends only on the full-B ambient coefficient", trace_free_family == expected_trace_free_family)
check(
    "within this computed family TF(F0) vanishes exactly when the full-B coefficient is zero",
    trace_free_family.subs(c_B, 0) == zero4 and any(sp.simplify(entry / c_B) != 0 for entry in trace_free_family if entry != 0),
)
check(
    "unresolved symbols are explicit coefficient slots, not fitted numeric data",
    trace_free_family.free_symbols == {c_B} and family.free_symbols == {c_H, c_B},
    f"family symbols={sorted(str(symbol) for symbol in family.free_symbols)}",
)

print("\n[verdict]")
print("  In the current A6-A11 gimmel/DeWitt convention, the computed constant-background")
print("  slots assemble to")
print("    F0 = (c_H/8) eta + c_B * diag(-1,5,5,5)/32.")
print("  After trace-free projection, the H-class ambient carrier and the already-zero")
print("  Q^TF, Delta^perp H0, and direct Rperp_0.H0 slots drop out:")
print("    TF(F0) = c_B * diag(3,1,1,1)/32.")
print()
print("  Honest scope: A12 narrows the remaining full-background problem to the still")
print("  unchosen full-B ambient coefficient/formula. It does not choose the final")
print("  Willmore-EL insertion formula, sign, scalar prefactor c_W, M-linearization,")
print("  OQ2-A functional, claim status, canon verdict, or public posture.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = computed trace-free background family is localized to the full-B coefficient.")
