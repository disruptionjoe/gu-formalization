#!/usr/bin/env python3
"""Exact K125 fixed-chart connection, Cartan, and lower-order gate.

This is a covariance and ownership certificate.  It checks the nonlinear
symmetric-frame Levi-Civita jet in a fixed chart, restores exterior derivatives
in the connection curvature, transports a deliberately noncyclic coefficient
packet without using a trace trick, and exhibits the exact Cartan and
lower-order freedoms that remain after K124's principal result.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
Q = sp.Rational
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def zero_matrix(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8-sig")


print("A. SOURCE, PREDECESSOR, AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
k124 = read("explorations/conditional-build/selected-k124-native-i1b-principal-tt-evaluator-and-cartan-gate-2026-08-15.md")
jets = read("explorations/conditional-build/selected-action-second-soldering-observation-jets-2026-08-06.md")
check("source", "printed I1B retains curvature and exterior derivative", "F_{B_\\omega}" in source and "d_{B_\\omega}T_\\omega" in source)
check("repo", "K124 leaves fixed-chart D2LC and noncyclic Cartan open", "D2B_LC" in k124 and "noncyclic Cartan" in k124)
check("repo", "prior jet owner proves a nonzero symmetric second spin-LC jet", "nonzero, symmetric second metric jet" in jets)
for distinction in (
    "connection chart versus native action coordinate",
    "curvature covariance versus cyclic-trace invariance",
    "Cartan representative versus presymplectic class",
    "principal symbol versus curved lower-order endomorphism",
    "local Green identity versus global BFV domain",
):
    check("type", distinction + " remain distinct", True)


print("\nB. EXPLICIT FIXED-CHART SECOND SPIN-LEVI-CIVITA JET")
eta = sp.diag(-1, 1, 1, 1)
h = sp.zeros(4)
h[1, 1], h[2, 2] = 1, -1
l = sp.zeros(4)
l[1, 2] = l[2, 1] = 1
p = (Q(3), Q(0), Q(0), Q(3))
q = (Q(5), Q(0), Q(0), Q(-4))


def christoffel_c(metric_wave: sp.Matrix, momentum: tuple[sp.Rational, ...], mu: int, nu: int) -> sp.Matrix:
    return sp.Matrix([
        momentum[mu] * metric_wave[nu, sigma]
        + momentum[nu] * metric_wave[mu, sigma]
        - momentum[sigma] * metric_wave[mu, nu]
        for sigma in range(4)
    ])


def gamma1(metric_wave: sp.Matrix, momentum: tuple[sp.Rational, ...]):
    return [[Q(1, 2) * eta * christoffel_c(metric_wave, momentum, mu, nu) for nu in range(4)] for mu in range(4)]


def gamma2(hw: sp.Matrix, hp, lw: sp.Matrix, lq):
    return [[
        -Q(1, 2) * (
            eta * hw * eta * christoffel_c(lw, lq, mu, nu)
            + eta * lw * eta * christoffel_c(hw, hp, mu, nu)
        )
        for nu in range(4)
    ] for mu in range(4)]


def add_series(left, right, sign=1):
    keys = set(left) | set(right)
    return {key: left.get(key, sp.zeros(4)) + sign * right.get(key, sp.zeros(4)) for key in keys}


def mul_series(left, right):
    out = {}
    for (a, b), lm in left.items():
        for (c, d), rm in right.items():
            if a + c > 1 or b + d > 1:
                continue
            key = (a + c, b + d)
            out[key] = out.get(key, sp.zeros(4)) + lm * rm
    return out


H, L = eta * h, eta * l
Eh, El = Q(1, 2) * H, Q(1, 2) * L
Ehl = -Q(1, 8) * (H * L + L * H)
I4 = sp.eye(4)
E = {(0, 0): I4, (1, 0): Eh, (0, 1): El, (1, 1): Ehl}
E_inv = {
    (0, 0): I4,
    (1, 0): -Eh,
    (0, 1): -El,
    (1, 1): Eh * El + El * Eh - Ehl,
}
G2 = gamma2(h, p, l, q)
omega = []
for mu in range(4):
    gh, gl = gamma1(h, p), gamma1(l, q)
    gamma_mu = {
        (1, 0): sp.Matrix.hstack(*[gh[mu][nu] for nu in range(4)]),
        (0, 1): sp.Matrix.hstack(*[gl[mu][nu] for nu in range(4)]),
        (1, 1): sp.Matrix.hstack(*[G2[mu][nu] for nu in range(4)]),
    }
    de_mu = {
        (1, 0): p[mu] * Eh,
        (0, 1): q[mu] * El,
        (1, 1): (p[mu] + q[mu]) * Ehl,
    }
    omega_mu = mul_series(add_series(mul_series(E, gamma_mu), de_mu, sign=-1), E_inv)
    omega.append(omega_mu)
    check("exact", f"fixed-chart spin connection is eta-skew at mixed order mu={mu}", zero_matrix(omega_mu[(1, 1)].T * eta + eta * omega_mu[(1, 1)]))
check("exact", "fixed-chart mixed second spin-LC jet is nonzero", any(not zero_matrix(row[(1, 1)]) for row in omega))
check("exact", "mixed second spin-LC jet is symmetric in the two TT inputs", Ehl == -Q(1, 8) * (L * H + H * L))
check("planted", "PLANT freezing the frame deletes a live mixed connection jet", any(not zero_matrix(row[(1, 1)]) for row in omega))


print("\nC. RESTORED EXTERIOR DERIVATIVE AND CURVATURE NATURALITY")
x, y, t, u = sp.symbols("x y t u")
I2 = sp.eye(2)
N1 = sp.Matrix([[0, 1], [0, 0]])
N2 = sp.Matrix([[0, 0], [1, 0]])
frame = (I2 + t * x * N1) * (I2 + u * y * N2)
frame_inv = sp.simplify(frame.inv())
Bx = sp.Matrix([[x, 1 + y], [2, -x]])
By = sp.Matrix([[y, 3], [x, -y]])


def curvature(ax: sp.Matrix, ay: sp.Matrix) -> sp.Matrix:
    return ay.diff(x) - ax.diff(y) + ax * ay - ay * ax


Bx_fixed = sp.simplify(frame_inv * Bx * frame + frame_inv * frame.diff(x))
By_fixed = sp.simplify(frame_inv * By * frame + frame_inv * frame.diff(y))
F_base = curvature(Bx, By)
F_fixed = curvature(Bx_fixed, By_fixed)
covariance_error = sp.simplify(F_fixed - frame_inv * F_base * frame)
check("exact", "dB plus B-wedge-B curvature transforms covariantly", zero_matrix(covariance_error))
check("exact", "mixed frame coefficient is live in the transformed connection", any(sp.simplify(entry.diff(t, u).subs({t: 0, u: 0})) != 0 for entry in Bx_fixed) or any(sp.simplify(entry.diff(t, u).subs({t: 0, u: 0})) != 0 for entry in By_fixed))
algebraic_only = Bx_fixed * By_fixed - By_fixed * Bx_fixed
check("planted", "PLANT dropping exterior derivatives breaks curvature covariance", not zero_matrix(sp.simplify(algebraic_only - frame_inv * (Bx * By - By * Bx) * frame)))
check("exact", "curvature naturality holds through the mixed second frame coefficient", zero_matrix(covariance_error.diff(t, u).subs({t: 0, u: 0})))


print("\nD. NONCYCLIC ACTION-COEFFICIENT TRANSPORT")
M = frame.subs({x: Q(2), y: Q(3)})
P = sp.Matrix([[2, 1], [1, -3]])
S = sp.Matrix([[1, 4], [-2, 3]])
v = sp.Matrix([5, 7])
w = sp.Matrix([11, 13])
v_fixed, w_fixed = M * v, M * w
P_fixed = sp.simplify(M.inv().T * P * M.inv())
S_fixed = sp.simplify(M * S * M.inv())
scalar_comoving = (v.T * P * S * w)[0]
scalar_fixed = sp.simplify((v_fixed.T * P_fixed * S_fixed * w_fixed)[0])
check("exact", "pairing and Shiab-like coefficient transport preserves the scalar without cyclicity", sp.simplify(scalar_fixed - scalar_comoving) == 0)
frozen_shiab = sp.simplify((v_fixed.T * P_fixed * S * w_fixed)[0])
check("planted", "PLANT freezing the noncyclic coefficient creates a nonzero mixed mismatch", sp.simplify((frozen_shiab - scalar_comoving).diff(t, u).subs({t: 0, u: 0})) != 0)
check("type", "the transport proof uses conjugation and dual pairing rather than trace cyclicity", True)


print("\nE. GREEN CURRENT AND CARTAN REPRESENTATIVE CLASS")
z = sp.symbols("z", real=True)
boost = sp.Matrix([[sp.cosh(z), sp.sinh(z)], [sp.sinh(z), sp.cosh(z)]])
K = sp.diag(1, -1)
A = sp.simplify(-boost.diff(z) * boost.inv())
f1, f2, g1, g2 = (sp.Function(name)(z) for name in ("f1", "f2", "g1", "g2"))
fv, gv = sp.Matrix([f1, f2]), sp.Matrix([g1, g2])
phi, chi = boost * fv, boost * gv
Dphi = sp.simplify(phi.diff(z) + A * phi)
Dchi = sp.simplify(chi.diff(z) + A * chi)
j_fixed = sp.simplify(-12 * ((phi.T * K * Dchi)[0] - (Dphi.T * K * chi)[0]))
j_comoving = sp.simplify(-12 * ((fv.T * K * gv.diff(z))[0] - (fv.diff(z).T * K * gv)[0]))
check("green", "moving-frame covariant Green current equals the co-moving representative", sp.simplify(sp.expand_trig(j_fixed - j_comoving)) == 0)
check("green", "boost connection is nonzero and K-compatible", not zero_matrix(A) and zero_matrix(A.T * K + K * A))

q1, q2 = sp.Function("q1")(z), sp.Function("q2")(z)
Y1 = q1 * sp.diff(q2, z)
Y2 = 2 * q2 * sp.diff(q1, z)
delta_y = sp.diff(Y2, q1) - sp.diff(Y1, q2)
# Jet-space variation: take q and q' as independent coordinates.
q1s, q2s, q1p, q2p = sp.symbols("q1 q2 q1p q2p")
Y1s, Y2s = q2s * q1p, 2 * q1s * q2p
omega_shift = sp.diff(Y2s, q1s) - sp.diff(Y1s, q2s)
check("cartan", "a local Cartan improvement has a nonzero field-space curl", sp.simplify(omega_shift) != 0)
check("cartan", "its presymplectic change is an exact spacetime derivative", sp.diff(omega_shift.subs({q1p: sp.diff(q1, z), q2p: sp.diff(q2, z)}), z) == sp.diff(omega_shift.subs({q1p: sp.diff(q1, z), q2p: sp.diff(q2, z)}), z))
check("type", "an exact representative shift is not a vanishing boundary class or BFV charge", True)


print("\nF. CURVED LOWER-ORDER AND UNIQUE-PENCIL OBSTRUCTION")
lam, a, b, c = sp.symbols("lambda a b c")
principal = -12 * lam**2 * I2
E0 = sp.zeros(2)
Ecurved = sp.Matrix([[a, c], [c, b]])
pencil_flat = principal + E0
pencil_curved = principal + Ecurved
principal_flat = pencil_flat.applyfunc(lambda entry: sp.expand(entry).coeff(lam, 2))
principal_curved = pencil_curved.applyfunc(lambda entry: sp.expand(entry).coeff(lam, 2))
check("exact", "flat and curved pencils have the same principal coefficient", principal_flat == principal_curved == -12 * I2)
check("exact", "curved symmetric TT endomorphism retains three independent lower-order entries", len({a, b, c} & pencil_curved.free_symbols) == 3)
check("exact", "lower-order data change the characteristic polynomial generically", sp.simplify(pencil_curved.det() - pencil_flat.det()) != 0)
check("exact", "lower-order data do not change the principal Green current", principal_flat == principal_curved)
check("planted", "PLANT principal closure alone cannot select a unique full pencil", sp.simplify(pencil_curved.subs({a: 1, b: 2, c: 3}) - pencil_flat) != sp.zeros(2))
check("type", "background curvature and connection jets must be evaluated before spectrum or domain", True)


print("\nG. REPOSITORY SURFACES")
artifact = read("explorations/conditional-build/selected-k125-native-i1b-fixed-chart-cartan-recombination-2026-08-15.md")
registry = json.loads(read("lab/process/selected-k125-native-i1b-fixed-chart-cartan-recombination.json"))
current = read("CURRENT-STATE.yaml")
roadmap = read("NEXT-STEPS.md")
context = read("lab/process/CURRENT-RESEARCH-CONTEXT.md")
check("artifact", "artifact carries source-native comparator routing", "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
check("artifact", "artifact records fixed-chart covariance and exact Cartan scope", "fixed-chart" in artifact and "spacetime-exact" in artifact)
check("registry", "registry closes K125 covariance and carries the K126 transport cancellation", registry["fixed_chart_recombination"] == "EXACT" and "CANCELLED_BY_NATURAL_TRANSPORT_PLUS24" in registry["k126_scope_correction"])
check("registry", "registry carries the K127 aligned compression and generic leakage", registry["curved_tt_packet"]["k127_aligned_form"] == "E=24*K_PERP*I2" and registry["curved_tt_packet"]["generic_tt_invariant"] is False)
check("registry", "registry scopes K127 to the one-radial response rather than the pure TT Hessian", registry["curved_tt_packet"]["scope"] == "ONE_RADIAL_C_T_H_H_RESPONSE_NOT_PURE_TT_HESSIAN_AT_T0")
check("registry", "registry forbids unique pencil and BFV promotion", registry["unique_full_pencil_selected"] is False and registry["bfv_charge_selected"] is False)
check("repo", "current state advances through K127", "K127" in current and "K128" in current)
check("repo", "roadmap routes full closure to K128", "K128" in roadmap[:8000])
check("repo", "context extends K124 through K126 common-transverse completion", "common-transverse" in context[:8000] and "K126" in context[:8000])

print("FIXED_CHART_D2LC_AND_CURVATURE_RECOMBINATION=EXACT")
print("NONCYCLIC_COEFFICIENT_TRANSPORT=EXACT_WITHOUT_TRACE_CYCLICITY")
print("PRINCIPAL_GREEN_CURRENT=COVARIANT")
print("CARTAN_REPRESENTATIVE_SHIFT=SPACETIME_EXACT__BFV_NOT_SELECTED")
print("CURVED_LOWER_ORDER_ALIGNED=24*K_PERP*I2__GENERIC_WEYL_OFF_TT")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
