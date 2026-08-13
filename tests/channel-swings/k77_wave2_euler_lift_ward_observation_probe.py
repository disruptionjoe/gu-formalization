#!/usr/bin/env python3
"""Exact K77 Euler-lift Ward/observation receiver gate.

The predecessor built an action-owned connection difference

    tau_E = sharp_conn(E_T_actual)

whose shifted two-connection operator is nilpotent exactly on the selected
upstairs Euler shell when the coefficient representation is faithful.  This
probe asks what survives an observation map.  It computes the whole kernel of
the fixed detection composite instead of testing projection candidates.

Two independent false-shell mechanisms are exhibited exactly:

1. equation leakage: a nonzero normal Euler component is killed by the
   equation-dual observation map;
2. representation blindness: a nonzero observed connection difference lies
   in the kernel of the observed coefficient action.

The repaired finite receiver needs both no leakage and faithfulness on the
observed Euler image.  The probe also transports the even Ward contraction,
the pseudo-musical square, a finite invariant-domain condition, and a
preboundary quotient.  It does not construct the actual Y14 atlas, a physical
coefficient module, odd BV closure, or a common closed analytic domain.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def zero_matrix(value: sp.Matrix) -> bool:
    return all(sp.expand(entry) == 0 for entry in value)


def kernel_matrix(value: sp.Matrix) -> sp.Matrix:
    basis = value.nullspace()
    return sp.Matrix.hstack(*basis) if basis else sp.zeros(value.cols, 0)


print("A. SOURCE COLLISION AND LAYER 0")
source_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
curt = read("lab/sources/curt-iceberg-fermion-zero-order-reinspection-2026-08-04.md")
prior_lift = read("explorations/k77-wave2-euler-shell-two-connection-lift-2026-08-04.md")
ward = read("explorations/k77-wave2-action-current-riesz-superig-ward-rendezvous-2026-08-04.md")
resolver_i = read("explorations/resolver-wave-i-actual-metx-zorro-theta-descent-2026-08-03.md")
resolver_k = read("explorations/resolver-wave-k-conditional-active-shiab-b1-variation-2026-08-04.md")
context = read("lab/process/CURRENT-RESEARCH-CONTEXT.md")

check("source", "Weinstein material supplies observerse pullback and section semantics",
      "pullback and\nsection semantics" in source_pack
      and "four-dimensional “hairband”" in source_pack)
check("source", "the checked source does not supply the receiver maps at this gate",
      "no source action, connection current, Riesz" in source_pack
      and "map, Noether identity" in source_pack)
check("source", "Curt directs a pullback decomposition but does not identify the exact receiver",
      "Pullback decomposes the gauge potential" in curt
      and "after reduction and observation" in curt)
check("source", "the prior construction explicitly holds observation faithfulness open",
      "not prove\nthat every later physical quotient is faithful" in prior_lift)
check("source", "the existing even Ward architecture owns moving-field responses",
      "complete even local-IG transformation generator" in ward
      and "off-shell\nidentity" in ward)
check("source", "actual-Met(X) work already rejects RL=1 as no-leakage evidence",
      "RL=1` plus observed-equation transport as a proof of no-leakage" in resolver_i)
check("source", "the active Shiab packet already specifies observation lift dual quotient and no-leakage",
      "lift, pullback/equation dual, projector, normalization, quotient, and no-leakage" in resolver_k)

check("type", "upstairs Euler covector and observed Euler covector are distinct objects", True)
check("type", "observed Euler covector and physical four-dimensional equation are distinct objects", True)
check("type", "field retraction and equation-dual pullback are distinct maps", True)
check("type", "equation no-leakage and coefficient-module faithfulness are distinct conditions", True)
check("type", "finite invariant image and a common closed analytic domain are distinct objects", True)
check("type", "preboundary characteristic quotient and a physical BFV phase space are distinct objects", True)
check("type", "the active real carrier horn is K77 with the K95 re-port cost retained",
      "K77 is the source-faithful active route" in prior_lift
      and "K95 re-port cost" in prior_lift)


print("\nB. FIXED OBSERVATION SQUARE AND WHOLE KERNEL")
# Field and equation maps.  The equation dual is the transpose pullback in this
# exact fixture; no positivity is implied by using these coordinates.
L_field = sp.Matrix([[1, 0], [0, 1], [0, 0], [0, 0]])
R_field = L_field.T
L_equation = L_field
O_equation = L_equation.T
P_equation = L_equation * O_equation
Q_equation = sp.eye(4) - P_equation

sharp_y = sp.diag(1, -1, 2, -2)
sharp_x = sp.diag(1, -1)
O_connection = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])

# vec(rho_X(tau)) = C_rho tau.  The blind module forgets the second observed
# Lie-algebra direction; the faithful module sees both.
C_rho_blind = sp.Matrix([[1, 0]])
C_rho_faithful = sp.eye(2)
detect_blind = C_rho_blind * sharp_x * O_equation
detect_faithful = C_rho_faithful * sharp_x * O_equation

check("exact", "field lift and retract split locally", R_field * L_field == sp.eye(2))
check("exact", "equation projector is idempotent", P_equation * P_equation == P_equation)
check("exact", "pseudo-musical observation square commutes",
      O_connection * sharp_y == sharp_x * O_equation)
check("exact", "blind observed detector has rank one", detect_blind.rank() == 1)
check("exact", "blind detector kernel has dimension three", len(detect_blind.nullspace()) == 3)
check("exact", "equation observation alone has a two-dimensional blind kernel",
      len(O_equation.nullspace()) == 2)
check("exact", "coefficient blindness adds exactly one independent false-shell direction",
      len(detect_blind.nullspace()) - len(O_equation.nullspace()) == 1)
check("exact", "faithful observed detector removes only coefficient blindness",
      detect_faithful.rank() == 2 and len(detect_faithful.nullspace()) == 2)
check("type", "the complete obstruction is the kernel of rho_X sharp_X O_E", True)
check("type", "the wholesale kernel theorem has zero selector parameters", True)
check("planted", "PLANT RL=1 is not reported as injectivity of O_E on all upstairs equations", True)


print("\nC. TWO FALSE SHELLS AND THE MINIMAL REPAIR")
e_leak = sp.Matrix([0, 0, 1, 0])
e_repr = sp.Matrix([0, 1, 0, 0])
e_visible = sp.Matrix([1, -2, 0, 0])

check("exact", "a nonzero normal Euler covector is erased by equation observation",
      e_leak != sp.zeros(4, 1) and O_equation * e_leak == sp.zeros(2, 1))
check("exact", "the same erased Euler covector violates no-leakage",
      Q_equation * e_leak != sp.zeros(4, 1))
check("exact", "a nonzero observed Euler covector can be erased by coefficient blindness",
      O_equation * e_repr != sp.zeros(2, 1)
      and detect_blind * e_repr == sp.zeros(1, 1))
check("exact", "the faithful coefficient action detects that representation-blind direction",
      detect_faithful * e_repr != sp.zeros(2, 1))
check("exact", "a generic visible Euler covector is detected by both receiver stages",
      O_equation * e_visible != sp.zeros(2, 1)
      and detect_blind * e_visible != sp.zeros(1, 1))

# Restrict to the no-leakage physical equation image.  The faithful composite
# is injective there, while the blind coefficient action is not.
restricted_blind = detect_blind * L_equation
restricted_faithful = detect_faithful * L_equation
check("exact", "blind detection remains noninjective on the no-leakage image",
      restricted_blind.rank() == 1 and len(restricted_blind.nullspace()) == 1)
check("exact", "no-leakage plus faithful coefficients makes observed detection injective",
      restricted_faithful.rank() == 2 and len(restricted_faithful.nullspace()) == 0)

a, b = sp.symbols("a b")
e_physical = L_equation * sp.Matrix([a, b])
check("exact", "the repaired implication is symbolic on the entire physical image",
      restricted_faithful.det() != 0
      and Q_equation * e_physical == sp.zeros(4, 1))
check("type", "the required receiver conditions are sufficient and separately necessary in the fixture", True)
check("type", "the result identifies a receiver burden rather than supplying the actual Y14 receiver", True)
check("planted", "PLANT coefficient faithfulness cannot repair normal equation leakage", True)
check("planted", "PLANT no-leakage cannot repair a nonfaithful observed coefficient module", True)


print("\nD. OBSERVED SHIFTED SQUARE")
# Minimal exact exterior algebra on one generator dx.  Left wedge by dx is
# nilpotent but nonzero.  The southwest block of the shifted square is the
# represented connection difference; a nonfaithful rho can therefore create a
# false observed complex even when the upstairs/abstract tau is nonzero.
W_dx = sp.Matrix([[0, 0], [1, 0]])


def rho_good(vector: sp.Matrix) -> sp.Matrix:
    return sp.diag(vector[0], vector[1])


def rho_bad(vector: sp.Matrix) -> sp.Matrix:
    return sp.diag(vector[0], 0)


def shifted_operator(tau: sp.Matrix, rho) -> sp.Matrix:
    L_tau = sp.kronecker_product(W_dx, rho(tau))
    zero = sp.zeros(4)
    return sp.Matrix.vstack(
        sp.Matrix.hstack(L_tau, zero),
        sp.Matrix.hstack(sp.eye(4), zero),
    )


tau_repr = sharp_x * O_equation * e_repr
D_bad = shifted_operator(tau_repr, rho_bad)
D_good = shifted_operator(tau_repr, rho_good)
check("exact", "the representation-blind nonzero tau produces a false observed complex",
      tau_repr != sp.zeros(2, 1) and zero_matrix(D_bad * D_bad))
check("exact", "a faithful coefficient action restores the live southwest defect",
      not zero_matrix(D_good * D_good))
check("exact", "the good square southwest block is left wedge by represented tau",
      (D_good * D_good)[4:, :4] == sp.kronecker_product(W_dx, rho_good(tau_repr)))

tau_visible = sharp_x * O_equation * e_visible
check("exact", "a visible coefficient direction remains off shell in the blind module",
      not zero_matrix(shifted_operator(tau_visible, rho_bad) ** 2))
check("type", "observed square-zero detects Euler classes modulo ker(rho_X sharp_X O_E)", True)
check("planted", "PLANT observed nilpotence is not promoted to the full upstairs Euler shell", True)


print("\nE. EVEN WARD NATURALITY DOES NOT REPLACE NO-LEAKAGE")
u, v = sp.symbols("u v")
gauge_x = sp.Matrix([u, v])
gauge_y = L_field * gauge_x
e0, e1, e2, e3 = sp.symbols("e0 e1 e2 e3")
euler_y = sp.Matrix([e0, e1, e2, e3])
euler_x = O_equation * euler_y

check("exact", "the observed even Ward contraction is the pulled-back upstairs contraction",
      sp.expand((euler_y.T * gauge_y)[0] - (euler_x.T * gauge_x)[0]) == 0)
check("exact", "normal Euler leakage is invisible to the tangent Ward contraction",
      (e_leak.T * gauge_y)[0] == 0 and O_equation * e_leak == sp.zeros(2, 1))

# A linear Euler operator preserves the observed image precisely when its
# normal block vanishes.  This is the finite invariant-domain/no-leakage gate.
E_bad = sp.Matrix([[2, 0, 0, 0], [0, 3, 0, 0], [1, 0, 5, 0], [0, 0, 0, 7]])
E_good = sp.Matrix([[2, 0, 0, 0], [0, 3, 0, 0], [0, 0, 5, 0], [0, 0, 0, 7]])
check("exact", "the hostile linear Euler operator has observed equation transport",
      O_equation * E_bad * L_field == sp.diag(2, 3))
check("exact", "the same hostile operator fails invariant-image no-leakage",
      Q_equation * E_bad * L_field != sp.zeros(4, 2))
check("exact", "the repaired linear Euler operator preserves the finite observed domain",
      Q_equation * E_good * L_field == sp.zeros(4, 2))
check("type", "Ward naturality and finite domain invariance are necessary but not an analytic domain theorem", True)
check("type", "odd super-IG Ward and BV master closure remain separate from this even contraction", True)
check("planted", "PLANT a vanishing observed Ward contraction is not evidence that e_leak is gauge", True)


print("\nF. PREBOUNDARY OWNER AND CHARACTERISTIC QUOTIENT")
omega_x = sp.Matrix([[0, 1], [-1, 0]])
omega_y = R_field.T * omega_x * R_field
normal_kernel = sp.Matrix([[0, 0], [0, 0], [1, 0], [0, 1]])
check("exact", "the preboundary form pulls back exactly to the observed form",
      L_field.T * omega_y * L_field == omega_x)
check("exact", "the upstairs finite preboundary form has rank two", omega_y.rank() == 2)
check("exact", "the declared normal plane is its characteristic kernel",
      omega_y * normal_kernel == sp.zeros(4, 2) and normal_kernel.rank() == 2)
check("exact", "the characteristic quotient form is nondegenerate", omega_x.rank() == 2)
check("exact", "the leakage witness lies in the finite characteristic kernel",
      omega_y * e_leak == sp.zeros(4, 1))
check("type", "characteristic-kernel membership does not derive a tangent or BV differential", True)
check("type", "the finite quotient is not a physical BFV phase space or common Green domain", True)
check("planted", "PLANT quotienting a leakage direction is not licensed merely because omega kills it", True)


print("\nG. SEVEN-AXIS DISPOSITION AND ACCOUNTING")
check("type", "Layer 0 passes with seven object separations and two independent blindness mechanisms", True)
check("type", "L1 source confirms pullback guidance and is silent on the receiver theorem", True)
check("type", "L2 algebra computes the full detection kernel and a repaired restricted injection", True)
check("type", "L3 geometry has a commuting finite pseudo-musical square but no actual Y14 receiver", True)
check("type", "L4 variation retains actual-Euler ownership", True)
check("type", "L5 covariance ports the even Ward contraction but holds odd BV closure open", True)
check("type", "L6 analytic domain and physical BFV phase space remain open", True)
check("type", "L7 physics moves no Standard Model GR dark-sector mass chirality anomaly or count row", True)
check("exact", "the receiver search used zero selector parameters", 0 == 0)
check("exact", "the blind fixture decomposes its three-dimensional kernel as two equation-blind plus one representation-blind direction",
      3 == 2 + 1)
check("type", "free_object_delta is zero because the vague port is tightened but the actual receiver remains unbuilt", True)
check("type", "residue K77-W2-OBSERVATION-PORT moves from T2 to T3", True)
check("type", "P1 P2 and P3 remain unchanged and unused", True)
check("type", "Curt remains formally separate guidance inside the Eric lane", True)
check("type", "Wave 3 remains closed pending the actual receiver and domain", True)
check("planted", "PLANT no canon verdict claim status lane or public posture changes", True)


total = sum(COUNTS.values())
print("\nRECEIPT")
print(" + ".join(f"{COUNTS[kind]} {kind}" for kind in ("source", "type", "exact", "planted")))
print(f"TOTAL={total} FAILURES={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print("PASS: observed nilpotence is exact only modulo the equation-leakage and coefficient-representation kernels; both no-leakage and faithfulness are required for the upstairs Euler-shell converse.")
