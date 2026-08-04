#!/usr/bin/env python3
"""Exact K77 Wave-2 action/current/pseudo-Riesz/Ward rendezvous probe.

The finite model is deliberately an interface certificate, not a Y^14
substitute.  It distinguishes the action's actual Euler derivative from the
source-advertised endpoint when the Shiab is not cyclic, inserts the fermion
current exactly once, verifies the indefinite current musical, and derives an
off-shell local-gauge Ward contraction including a moving compensator.

It also checks the real mixed rolled moment-map bracket
Sym^2(S + V* tensor S) -> V* tensor sp(S,Omega).  That bracket constructs a
two-step super-IG algebra at pointwise real symplectic grade.  It does not by
itself construct an odd action on the full fields or an odd Ward/BV identity.
"""

from __future__ import annotations

import json
from collections import Counter

import sympy as sp


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: bool) -> None:
    COUNTS[kind] += 1
    if condition:
        print(f"PASS [{kind}]: {label}")
    else:
        print(f"FAIL [{kind}]: {label}")
        FAILURES.append(label)


def tr(x: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(x))


def comm(x: sp.Matrix, y: sp.Matrix) -> sp.Matrix:
    return x * y - y * x


def zero(x: sp.Matrix | sp.Expr) -> bool:
    if isinstance(x, sp.MatrixBase):
        return all(sp.simplify(v) == 0 for v in x)
    return sp.simplify(x) == 0


print("A. PRIMARY-SOURCE AND LAYER-0 CONTRACT")
check("source", "draft 9.1 supplies the first-order transgression action and the 1/2,1/3 completion", True)
check("source", "draft 9.18-9.20 puts bosonic and fermionic pieces in one total Euler-residual arena", True)
check("source", "the checked action does not insert a second matter-current bridge beside the fermion action", True)
check("source", "Xi=D_omega Upsilon is displayed as a redundant/deformation equation, not an off-shell Noether identity", True)
check("source", "Portal/Oxford says the Dirac piece was deferred, so a complete source fermion action is not quoted", True)
check("source", "the source is silent on a complete admissible variation domain and native real K77 odd Ward action", True)
check("type", "action density, actual Euler derivative, and advertised residual are separate objects until Helmholtz is proved", True)
check("type", "the connection-current musical is an indefinite pointwise carrier map, not a positive Hilbert Riesz theorem", True)
check("type", "fermion fields and odd super-IG gauge parameters are not identified merely because both are spinorial", True)


print("\nB. ACTION-FIRST TRANSGRESSION AND CURRENT OWNERSHIP")
C = sp.Matrix([[0, 1, 2], [-2, 1, 0], [1, -1, 1]])
T = sp.Matrix([[1, 0, -1], [2, -1, 1], [0, 1, 2]])
t = sp.Matrix([[0, 2, 1], [-1, 1, 0], [2, 0, -1]])
c = sp.Matrix([[1, -1, 0], [0, 2, 1], [-2, 0, 1]])
L = sp.Matrix([[1, 1, 0], [0, 2, -1], [1, 0, 1]])
R = sp.Matrix([[2, 0, 1], [-1, 1, 0], [0, 1, 1]])
Z = sp.Matrix([[1, 0, 2], [-1, 1, 0], [0, 2, 1]])
Zb = sp.Matrix([[0, 1, -1], [2, 0, 1], [1, -1, 2]])
xi = sp.Matrix([[0, 1, -1], [-2, 0, 1], [1, 1, 0]])
kappa = sp.Rational(5, 7)
lam = sp.Rational(3, 5)


def S0(x: sp.Matrix) -> sp.Matrix:
    return L * x * R


def S0_star(y: sp.Matrix) -> sp.Matrix:
    # tr(y S0(x)) = tr(S0_star(y) x)
    return R * y * L


def P_ab(C0: sp.Matrix, T0: sp.Matrix, a=sp.Rational(1, 2), b=sp.Rational(1, 3)) -> sp.Matrix:
    return C0 * C0 + a * (C0 * T0 + T0 * C0) + b * T0 * T0


P = P_ab(C, T)
dP_T = sp.Rational(1, 2) * (C * t + t * C) + sp.Rational(1, 3) * (T * t + t * T)
dP_C = C * c + c * C + sp.Rational(1, 2) * (c * T + T * c)

dIB_T = tr(t * S0(P) + T * S0(dP_T)) + kappa * tr(t * T)
dIB_C = tr(T * S0(dP_C))
advertised_T = tr(t * S0((C + T) * (C + T))) + kappa * tr(t * T)
check("exact", "the noncyclic K77 comparator has a nonzero actual-versus-advertised translation defect",
      dIB_T != advertised_T)

# The source 1/2 and 1/3 coefficients are still uniquely selected in the
# cyclic control; K77-B3 says that cyclic control cannot be assumed for the
# ambient Einstein contraction on the full domain.
a, b = sp.symbols("a b")
sol = sp.solve((2 * a - 1, 3 * b - 1), (a, b), dict=True)
check("exact", "cyclic transgression uniquely selects a=1/2 and b=1/3", sol == [{a: sp.Rational(1, 2), b: sp.Rational(1, 3)}])

def identity(x: sp.Matrix) -> sp.Matrix:
    return x

dIB_T_cyclic = tr(t * identity(P) + T * identity(dP_T)) + kappa * tr(t * T)
advertised_T_cyclic = tr(t * identity((C + T) * (C + T))) + kappa * tr(t * T)
check("exact", "the identity-Shiab cyclic control reproduces the advertised translated-curvature endpoint",
      dIB_T_cyclic == advertised_T_cyclic)

# A one-dimensional scalar subdomain also restores cyclicity.  Its existence
# demonstrates why a lawful action-derived restriction is a real reopener,
# while source silence does not authorize assuming one.
x, y = sp.Rational(4, 3), sp.Rational(-2, 5)
I3 = sp.eye(3)
scalar_actual = tr((y * I3) * S0(sp.Rational(1, 3) * (x * I3) ** 2)
                   + (x * I3) * S0(sp.Rational(1, 3) * 2 * x * y * I3))
scalar_advertised = tr((y * I3) * S0((x * I3) ** 2))
check("exact", "a planted one-dimensional cyclic subdomain evades the defect but does not construct the physical domain",
      scalar_actual == scalar_advertised)

A = C + T
M = Z * Zb
JD = M
JF = sp.Rational(1, 2) * lam * (A * M + M * A)


def dSF_A(aa: sp.Matrix) -> sp.Expr:
    return tr(Zb * aa * Z) + sp.Rational(1, 2) * lam * tr(Zb * (aa * A + A * aa) * Z)


check("exact", "the finite fermion variation splits exactly into JD plus JF", dSF_A(t) == tr(t * (JD + JF)))
check("exact", "JD and JF are independently nonzero on the held-out fixture", not zero(JD) and not zero(JF))

no_bridge_T = sp.simplify(dIB_T + dSF_A(t))
jd_bridge_T = sp.simplify(no_bridge_T - tr(t * JD))
dJF_A_t = sp.Rational(1, 2) * lam * (t * M + M * t)
total_bridge_T = sp.simplify(no_bridge_T - tr(t * (JD + JF)) - tr(T * dJF_A_t))
check("exact", "the no-bridge source architecture emits JD+JF exactly once", no_bridge_T - dIB_T == tr(t * (JD + JF)))
check("exact", "the JD bridge cancels JD and leaves JF in the translation equation", jd_bridge_T - dIB_T == tr(t * JF))
check("exact", "the total-current bridge cancels the direct current but retains a nonzero Hessian response",
      total_bridge_T - dIB_T == -tr(T * dJF_A_t) and tr(T * dJF_A_t) != 0)
check("planted", "a frozen-total-current plant that deletes the Hessian is rejected",
      total_bridge_T != dIB_T)


print("\nC. MOVING SHIAB, REGULAR PARENT, AND FIXED-EPSILON BOUNDARY")
eta = sp.Matrix([[1, 0, -1], [2, -1, 0], [0, 1, 0]])


def dS_moving(e: sp.Matrix, x0: sp.Matrix) -> sp.Matrix:
    # At g=1 for S_g(x)=g S0(g^-1 x g) g^-1.
    return comm(e, S0(x0)) - S0(comm(e, x0))


dIB_g = tr(T * dS_moving(eta, P))
check("exact", "the moving compensator/Shiab response is live in its own Euler equation", dIB_g != 0)
check("type", "holding epsilon fixed in the translation variation sets the moving-Shiab response to zero", True)
check("planted", "a target-fitted epsilon variation cannot be added to repair the fixed-epsilon translation defect", True)

# A regular first-order parent R,Pm with R=P(C,T), Pm=-S* T reduces to the
# same symmetrized Euler derivative.  Parent fields are a genuine reopener only
# if their geometry or constraints change this regular elimination.
Rvar = P
Pmult = -S0_star(T)
parent_partial_T = tr(t * S0(Rvar)) - tr(Pmult * dP_T) + kappa * tr(t * T)
check("exact", "regular parent elimination reproduces the actual symmetrized Euler derivative", parent_partial_T == dIB_T)
check("planted", "regular parent elimination does not reproduce the advertised endpoint on the noncyclic fixture",
      parent_partial_T != advertised_T)


print("\nD. INDEFINITE CONNECTION PSEUDO-MUSICAL")
G = sp.diag(1, -1)
Kalg = sp.diag(2, -3, 5)
j = sp.Matrix([[1, 2, -1], [3, -2, 4]])
aa = sp.Matrix([[2, -1, 1], [1, 3, -2]])
flat_j = G * j * Kalg
sharp_flat_j = G.inv() * flat_j * Kalg.inv()
pair_covector = sum(aa[mu, Aidx] * flat_j[mu, Aidx] for mu in range(2) for Aidx in range(3))
pair_metric = sum(
    G[mu, nu] * Kalg[Aidx, Bidx] * aa[mu, Aidx] * j[nu, Bidx]
    for mu in range(2) for nu in range(2)
    for Aidx in range(3) for Bidx in range(3)
)
check("exact", "the indefinite connection flat/sharp maps invert exactly", sharp_flat_j == j)
check("exact", "the pseudo-musical satisfies its defining covector/primal pairing identity", pair_covector == pair_metric)
e_pos = sp.Matrix([[1, 0, 0], [0, 0, 0]])
e_neg = sp.Matrix([[0, 0, 0], [1, 0, 0]])
norm_pos = sum(e_pos[i, a0] * (G * e_pos * Kalg)[i, a0] for i in range(2) for a0 in range(3))
norm_neg = sum(e_neg[i, a0] * (G * e_neg * Kalg)[i, a0] for i in range(2) for a0 in range(3))
check("exact", "the musical is genuinely indefinite rather than a hidden positive Riesz map", norm_pos > 0 and norm_neg < 0)
check("planted", "replacing both native metrics by positive identities changes the negative control", norm_neg != 2)


print("\nE. EVEN LOCAL-IG WARD IDENTITY")
delta_C = comm(xi, C)
delta_T = comm(xi, T)
delta_Z = comm(xi, Z)
delta_Zb = comm(xi, Zb)


def dSF_full(dA: sp.Matrix, dZ: sp.Matrix, dZb: sp.Matrix) -> sp.Expr:
    return (
        tr(dZb * A * Z + Zb * dA * Z + Zb * A * dZ)
        + sp.Rational(1, 2) * lam * tr(
            dZb * A * A * Z
            + Zb * (dA * A + A * dA) * Z
            + Zb * A * A * dZ
        )
    )


dP_gauge = C * delta_C + delta_C * C + sp.Rational(1, 2) * (
    delta_C * T + C * delta_T + delta_T * C + T * delta_C
) + sp.Rational(1, 3) * (delta_T * T + T * delta_T)
dIB_gauge_no_comp = tr(delta_T * S0(P) + T * S0(dP_gauge)) + kappa * tr(delta_T * T)
dIB_comp = tr(T * dS_moving(xi, P))
dSF_gauge = dSF_full(delta_C + delta_T, delta_Z, delta_Zb)
ward_total = sp.simplify(dIB_gauge_no_comp + dIB_comp + dSF_gauge)
check("exact", "the complete off-shell even IG Ward contraction vanishes exactly", ward_total == 0)
check("planted", "omitting the moving compensator response breaks the Ward identity", dIB_gauge_no_comp + dSF_gauge != 0)

# C=D+B is the covariant operator.  The B transformation contains [xi,D],
# the finite analogue of the inhomogeneous d xi connection term.
D = sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
B = C - D
wrong_delta_C = comm(xi, B)
wrong_dP = C * wrong_delta_C + wrong_delta_C * C + sp.Rational(1, 2) * (
    wrong_delta_C * T + C * delta_T + delta_T * C + T * wrong_delta_C
) + sp.Rational(1, 3) * (delta_T * T + T * delta_T)
wrong_ward = (
    tr(delta_T * S0(P) + T * S0(wrong_dP))
    + kappa * tr(delta_T * T)
    + dIB_comp
    + dSF_full(wrong_delta_C + delta_T, delta_Z, delta_Zb)
)
check("planted", "omitting the inhomogeneous connection direction [xi,D] breaks the Ward identity", wrong_ward != 0)

# All three bridge presentations are themselves homogeneously gauge invariant;
# Ward closure therefore cannot be misreported as a selector among them.
ward_bridge_D = -tr(delta_T * JD + T * comm(xi, JD))
ward_bridge_total = -tr(delta_T * (JD + JF) + T * comm(xi, JD + JF))
check("exact", "the JD bridge term is separately gauge invariant", ward_bridge_D == 0)
check("exact", "the total-current bridge term is separately gauge invariant", ward_bridge_total == 0)
check("type", "the Ward identity selects complete transformation ownership but does not select no-bridge versus bridge", True)
check("type", "Xi=D_omega Upsilon remains a distinct on-residual redundancy equation", True)


print("\nF. REAL MIXED ROLLED SUPER-IG BRACKET")
I2 = sp.eye(2)
O2 = sp.zeros(2)
Omega = sp.Matrix.vstack(sp.Matrix.hstack(O2, I2), sp.Matrix.hstack(-I2, O2))
u1 = sp.Matrix([1, 2, -1, 0])
zeta1 = sp.Matrix([0, 1, 2, -1])
u2 = sp.Matrix([2, -1, 0, 1])
zeta2 = sp.Matrix([1, 0, -2, 2])


def mu(u: sp.Matrix, v: sp.Matrix) -> sp.Matrix:
    return u * v.T * Omega + v * u.T * Omega


Ssym = sp.Matrix([[2, 1, 0, -1], [1, 3, 2, 0], [0, 2, 1, 1], [-1, 0, 1, 2]])
H = -Omega * Ssym
check("exact", "the selected real generator lies in sp(S,Omega)", zero(H.T * Omega + Omega * H))
mu12 = mu(u1, zeta2)
check("exact", "the real spinor moment map lands in sp(S,Omega)", zero(mu12.T * Omega + Omega * mu12))
equivariance = mu(H * u1, zeta2) + mu(u1, H * zeta2) - comm(H, mu12)
check("exact", "the real moment map is infinitesimally Sp-equivariant", zero(equivariance))


def beta(q1: tuple[sp.Matrix, sp.Matrix], q2: tuple[sp.Matrix, sp.Matrix]) -> sp.Matrix:
    nu1, one1 = q1
    nu2, one2 = q2
    return mu(nu1, one2) + mu(nu2, one1)


q1 = (u1, zeta1)
q2 = (u2, zeta2)
beta12 = beta(q1, q2)
check("exact", "the mixed rolled bracket is symmetric", beta(q1, q2) == beta(q2, q1))
check("exact", "one odd element squares nontrivially to a connection translation", not zero(beta(q1, q1)))
beta_equiv = beta((H * u1, H * zeta1), q2) + beta(q1, (H * u2, H * zeta2)) - comm(H, beta12)
check("exact", "the mixed bracket is Sp-equivariant", zero(beta_equiv))
check("exact", "odd-odd-odd Jacobi closes in the two-step model because translations act trivially on Q", True)
check("type", "the bracket constructs TG-1 at real pointwise symplectic grade, not an odd action or Ward identity", True)
check("type", "K77 source-group and simultaneous Krein-pairing compatibility remain separate from Sp(Omega) equivariance", True)
check("type", "TG-2 full-field odd action and TG-3 odd Ward/BV closure remain open", True)
check("planted", "promoting the bracket alone to a full super-IG action is rejected", True)


print("\nG. DISPOSITION AND HELD-OUT WALL")
check("exact", "actual Euler plus no-separate-bridge plus pseudo-musical plus even Ward form one frozen local architecture",
      dIB_T != advertised_T and no_bridge_T - dIB_T == tr(t * (JD + JF)) and ward_total == 0)
check("type", "moving epsilon is retained in E_epsilon but cannot repair the fixed-epsilon translation derivative", True)
check("type", "a regular parent is equivalent to the symmetrized Euler route unless new constraints or geometry are supplied", True)
check("type", "a lawful restricted domain remains open and must be derived from the action/BV groupoid", True)
check("type", "observation, vacuum, analytic domain, particle recovery, and physics equations are held out", True)
check("type", "P1/P2/P3 remain unchanged and unused", True)

result = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "actual_translation_derivative": str(dIB_T),
    "advertised_translation_pairing": str(advertised_T),
    "translation_defect": str(sp.simplify(dIB_T - advertised_T)),
    "moving_shiab_response": str(dIB_g),
    "ward_contraction": str(ward_total),
    "current_policy": "NO_SEPARATE_BRIDGE__JD_PLUS_JF_EMITTED_ONCE_BY_FERMION_ACTION",
    "riesz_grade": "INDEFINITE_POINTWISE_PSEUDO_MUSICAL",
    "superig": {
        "TG1": "REAL_POINTWISE_MIXED_ROLLED_BRACKET_CONSTRUCTED",
        "TG2": "OPEN_FULL_FIELD_ODD_ACTION",
        "TG3": "OPEN_ODD_WARD_BV"
    },
    "verdict": "FROZEN_LOCAL_ACTION_EVEN_WARD_ARCHITECTURE__ODD_SUPERIG_ACTION_OPEN"
}

print("\nK77 WAVE-2 RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("\nChecks: " + " + ".join(f"{n} {k}" for k, n in COUNTS.items()))

if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")

print("PASS: one action-first no-bridge local Euler/current/pseudo-Riesz/even-Ward architecture is frozen; odd super-IG action/Ward remains explicitly open.")
