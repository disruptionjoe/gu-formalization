#!/usr/bin/env python3
"""THREAD A6 -- constant-section Simons / Q^TF background stress.

A5 pinned the constant-section normal-curvature tensor Rperp_0. Another open
piece of the background Willmore-EL assembly is the purely extrinsic Simons /
shape-stress term

    Q^TF_mn(B) = [ (1/2) H_i hatB^i_mn - (hatB^2)_mn ]^TF.

This gate computes that term for the flat constant section B0 from the gimmel /
DeWitt metric. The result is robust under two contractions:

  * exact symmetric-pair DeWitt contraction on Sym^2(T*X);
  * the older ordered-index contraction used by existing Q-gates.

Both produce a pure trace stress, so Q^TF(B0) = 0. The coefficient differs by a
normalization factor between conventions, but the trace-free conclusion is
unchanged.

Run: python tests/threads/A6_constant_section_simons_stress.py
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


def B0_pair(mu: int, nu: int, alpha: int) -> sp.Expr:
    a, b = pairs[alpha]
    return B0(mu, nu, a, b)


def trace_free_base(tensor: sp.Matrix) -> sp.Matrix:
    tr = sp.simplify(sum(eta_inv[p, p] * tensor[p, p] for p in range(DIM)))
    return sp.Matrix(
        DIM,
        DIM,
        lambda m, n: sp.simplify(tensor[m, n] - sp.Rational(1, DIM) * eta[m, n] * tr),
    )


def build_qtf_dewitt_pair() -> tuple[sp.Matrix, sp.Matrix, sp.Expr]:
    """Build Q and Q^TF using the exact symmetric-pair DeWitt inverse."""
    normal_metric = sp.Matrix([[dewitt_pairing(S[alpha], S[beta]) for beta in pairs] for alpha in pairs])
    normal_inverse = sp.simplify(normal_metric.inv())
    H_lower = [
        sp.simplify(sum(eta_inv[m, m] * B0_pair(m, m, alpha) for m in range(DIM)))
        for alpha in range(len(pairs))
    ]
    H_upper = [
        sp.simplify(sum(normal_inverse[alpha, beta] * H_lower[beta] for beta in range(len(pairs))))
        for alpha in range(len(pairs))
    ]

    def hatB(m: int, n: int, alpha: int) -> sp.Expr:
        return sp.simplify(B0_pair(m, n, alpha) - sp.Rational(1, DIM) * eta[m, n] * H_lower[alpha])

    Q = sp.zeros(DIM, DIM)
    for m in range(DIM):
        for n in range(DIM):
            linear_h = sp.Rational(1, 2) * sum(H_upper[alpha] * hatB(m, n, alpha) for alpha in range(len(pairs)))
            quadratic = sp.Integer(0)
            for p in range(DIM):
                for q in range(DIM):
                    for alpha in range(len(pairs)):
                        for beta in range(len(pairs)):
                            quadratic += (
                                eta_inv[p, q]
                                * normal_inverse[alpha, beta]
                                * hatB(m, p, alpha)
                                * hatB(q, n, beta)
                            )
            Q[m, n] = sp.simplify(linear_h - quadratic)
    return Q, trace_free_base(Q), sp.simplify(sum(eta_inv[p, p] * Q[p, p] for p in range(DIM)))


def build_qtf_ordered_index() -> tuple[sp.Matrix, sp.Matrix, sp.Expr]:
    """Build Q and Q^TF using the legacy ordered-index contraction from existing Q gates."""
    H = sp.Matrix(
        DIM,
        DIM,
        lambda a, b: sp.simplify(sum(eta_inv[m, m] * B0(m, m, a, b) for m in range(DIM))),
    )

    def hatB(m: int, n: int, a: int, b: int) -> sp.Expr:
        return sp.simplify(B0(m, n, a, b) - sp.Rational(1, DIM) * eta[m, n] * H[a, b])

    def normal_dot(fn) -> sp.Expr:
        return sp.simplify(
            sum(eta_inv[a, a] * eta_inv[b, b] * fn(a, b) for a in range(DIM) for b in range(DIM))
        )

    Q = sp.zeros(DIM, DIM)
    for m in range(DIM):
        for n in range(DIM):
            linear_h = sp.Rational(1, 2) * normal_dot(lambda a, b: H[a, b] * hatB(m, n, a, b))
            quadratic = sum(
                eta_inv[p, p] * normal_dot(lambda a, b: hatB(m, p, a, b) * hatB(p, n, a, b))
                for p in range(DIM)
            )
            Q[m, n] = sp.simplify(linear_h - quadratic)
    return Q, trace_free_base(Q), sp.simplify(sum(eta_inv[p, p] * Q[p, p] for p in range(DIM)))


def base_trace_free_sff_is_nonzero() -> bool:
    H = sp.Matrix(
        DIM,
        DIM,
        lambda a, b: sp.simplify(sum(eta_inv[m, m] * B0(m, m, a, b) for m in range(DIM))),
    )
    for m in range(DIM):
        for n in range(DIM):
            for a in range(DIM):
                for b in range(DIM):
                    value = sp.simplify(B0(m, n, a, b) - sp.Rational(1, DIM) * eta[m, n] * H[a, b])
                    if value != 0:
                        return True
    return False


print("[A6] constant-section Simons / Q^TF background stress\n")

normal_metric = sp.Matrix([[dewitt_pairing(S[alpha], S[beta]) for beta in pairs] for alpha in pairs])
normal_eigs = normal_metric.eigenvals()
positive_signature = sum(mult for eig, mult in normal_eigs.items() if eig > 0)
negative_signature = sum(mult for eig, mult in normal_eigs.items() if eig < 0)
check("DeWitt normal metric is nondegenerate in the symmetric-pair basis", normal_metric.det() == 64)
check("DeWitt normal metric has signature (6,4)", (positive_signature, negative_signature) == (6, 4))

H_matrix = sp.Matrix(
    DIM,
    DIM,
    lambda a, b: sp.simplify(sum(eta_inv[m, m] * B0(m, m, a, b) for m in range(DIM))),
)
check("constant-section mean curvature is H0 = (1/2) eta", H_matrix == sp.Rational(1, 2) * eta)
check("B0 has a nonzero base-trace-free shear part, so Q^TF=0 is not because B0 is umbilic",
      base_trace_free_sff_is_nonzero())

Q_dewitt, QTF_dewitt, tr_dewitt = build_qtf_dewitt_pair()
Q_ordered, QTF_ordered, tr_ordered = build_qtf_ordered_index()

print("    exact symmetric-pair DeWitt contraction:")
print(f"      Q(B0)   = {-sp.Rational(9, 32)} * eta")
print(f"      trace   = {tr_dewitt}")
print("      Q^TF    = 0")
print("    legacy ordered-index contraction:")
print(f"      Q(B0)   = {-sp.Rational(9, 16)} * eta")
print(f"      trace   = {tr_ordered}")
print("      Q^TF    = 0")

check("exact DeWitt-pair contraction makes Q(B0) pure trace: Q = -9/32 eta",
      Q_dewitt == -sp.Rational(9, 32) * eta, f"Q={Q_dewitt}")
check("exact DeWitt-pair trace-free stress vanishes: Q^TF(B0)=0",
      QTF_dewitt == sp.zeros(DIM, DIM))
check("legacy ordered-index contraction also makes Q(B0) pure trace: Q = -9/16 eta",
      Q_ordered == -sp.Rational(9, 16) * eta, f"Q={Q_ordered}")
check("legacy ordered-index trace-free stress also vanishes: Q^TF(B0)=0",
      QTF_ordered == sp.zeros(DIM, DIM))
check("the two contractions differ only by normalization before trace-free projection",
      sp.simplify(Q_ordered - 2 * Q_dewitt) == sp.zeros(DIM, DIM))

print("\n[verdict]")
print("  The constant-section Simons / shape-stress contribution is pure trace.")
print("  Under the exact DeWitt normal metric Q(B0) = -9/32 eta; under the older")
print("  ordered-index contraction Q(B0) = -9/16 eta. In both cases the trace-free")
print("  background stress vanishes exactly: Q^TF(B0)=0.")
print()
print("  Thread A consequence: B0 still carries a real Lambda-shaped background and")
print("  nonzero shear, but its purely extrinsic Simons stress adds no trace-free")
print("  background obstruction. The remaining background assembly still needs")
print("  Delta^perp H0, the A5 Rperp_0 term, and the ambient R^Y.H0/B0 term.")
print()
print("  Honest scope: this is the constant-background Simons/Q gate only. It does")
print("  not compute the full Willmore EL, choose H-class vs II-class, move OQ2-A,")
print("  or change claim status, canon verdicts, or public posture.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = constant-section Simons stress is pure trace; Q^TF(B0)=0.")
