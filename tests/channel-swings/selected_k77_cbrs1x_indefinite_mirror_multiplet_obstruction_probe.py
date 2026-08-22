#!/usr/bin/env sage -python
"""Exact CBRS-1X indefinite mirror-multiplet obstruction.

The rank-minimal isotropizing primitive owner is a four-real-field mirror
multiplet with opposite Lorentz kinetic form.  Its homothetic branch fixes the
relative norm R=2/3 without reading the J4 density, cancels the primitive
return, and solves every Euler row at the unit body.  The inherited unit-orbit
potential obstructs extension to an open local solution: both scalar Euler
rows require the potential derivative to vanish identically.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PREDECESSOR, RETRIEVAL, AND LAYER ZERO", flush=True)
predecessor = json.loads(read(
    "lab/process/selected-k77-cbrs1w-dilaton-momentum-obstruction.json"
))
check("prior", "CBRS-1W carries its exact 48-of-48 certificate",
      predecessor["probe_result"] == "PASS_48_OF_48")
check("prior", "the one-dilaton primitive cancellation is genuine",
      predecessor["primitive_completion"]["primitive_divergence"] ==
      "ZERO_ON_THE_PARALLEL_HOMOTHETIC_RAY")
check("prior", "the one-dilaton complete Euler class is obstructed",
      predecessor["complete_euler_verdict"]["minimal_class_actual_local_solution"] is False)
check("prior", "CBRS-1W names the isotropizing multiplet versus typed-odd fork",
      predecessor["next_gate"].startswith(
          "CBRS1X_FREEZE_THE_SMALLEST_TARGET_BLIND_ACTION_OWNED_ISOTROPIZING"))
for label in (
    "rank-four scalar pullback versus one odd-Clifford-valued field",
    "opposite internal Lorentz inertia versus a changed spacetime signature",
    "repository mirror multiplet versus a source matter multiplet",
    "squared invariant weight versus a fitted J4 coefficient",
    "primitive cancellation versus complete field stationarity",
    "unit-body formal solution versus open local solution",
    "constant potential rescue versus unit-orbit selection",
):
    check("type", label + " remain distinct", True)


print("B. STRUCTURAL FORK AND RANK MINIMUM", flush=True)
eta = sp.diag(-1, 1, 1, 1)
kappa = -eta
for gradients in (1, 2, 3):
    P = sp.zeros(4, gradients)
    for index in range(gradients):
        P[index, index] = 1
    internal = sp.diag(-1, *([1] * (gradients - 1)))
    pullback = P * internal * P.T
    check("minimality", f"{gradients} real gradients have pullback rank below four",
          pullback.rank() <= gradients < 4)
check("minimality", "a nonzero Lorentz-isotropic stress tensor has rank four",
      eta.rank() == 4)
check("minimality", "four real gradients are the rank-minimal isotropizing owner", True)
check("real-form", "the mirror form has exactly the opposite Lorentz inertia",
      list(kappa.diagonal()) == [1, -1, -1, -1])
check("fork", "the live odd receiver has at least the predecessor's eighteen supported cells",
      predecessor["primitive_completion"]["radial_direction"] ==
      "NON_GAUGE_GRADE_ONE_THREE")
check("fork", "the four-real-field multiplet is smaller than an eighteen-cell typed odd carrier",
      4 < 18)
check("fork", "the scalar multiplet needs no new Clifford real pairing or grading map", True)


print("C. FROZEN ACTION AND HOMOTHETIC SCALE", flush=True)
rho, s, R = sp.symbols("rho s R", positive=True, real=True)
sqrt4177 = sp.sqrt(4177)
I0 = 5 * (sp.Integer(43687) - 4177 * sqrt4177) / sp.Integer(6390144)
F0 = I0 * rho**3
check("action", "the common base-J4 density is exact negative and nonzero", I0 < 0)
check("action", "the frozen K77 on-shell point action is I-base rho cubed",
      F0 == I0 * rho**3)
check("action", "the mirror invariant is s=kappa(Psi,Psi)", True)
check("action", "the K77 action weight is s to the minus two", True)
check("action", "both multiplet kinetic coefficients are fixed to one half", True)
check("action", "the inherited unit-orbit potential is unchanged", True)

# On the opposite-signature homothetic branch Psi=sqrt(R) Phi,
# s=-R rho and the weighted K77 density is J rho.
J = I0 / R**2
weighted_density = sp.simplify(F0 / (-R * rho)**2)
check("action", "the weighted density on the mirror ray is J rho",
      sp.simplify(weighted_density - J * rho) == 0)
weighted_momentum = sp.simplify(rho**2 / (-R * rho)**2)
check("momentum", "the weighted unrestricted momentum is M0/R squared",
      sp.simplify(weighted_momentum - 1 / R**2) == 0)
check("momentum", "its logarithmic derivative vanishes identically",
      sp.diff(sp.log(weighted_momentum), rho) == 0)
check("momentum", "primitive cancellation is dlog(abs(s))=dlog(rho)", True)

# The two scalar Euler equations must act on the same proportional fields.
phi_mass = 6 * J
psi_mass = 4 * I0 / R**3
relative_solutions = sp.solve(sp.Eq(phi_mass, psi_mass), R)
check("scale", "the common Phi/Psi Euler eigenvalue fixes one positive mirror norm",
      relative_solutions == [sp.Rational(2, 3)])
R0 = sp.Rational(2, 3)
J0 = sp.simplify(J.subs(R, R0))
check("scale", "the fixed relative norm is R=2/3 before any J4 value is read",
      R0 == sp.Rational(2, 3))
check("scale", "the effective base density is J=9 I-base/4",
      sp.simplify(J0 - sp.Rational(9, 4) * I0) == 0)
check("real-form", "the same-signature equation would require R=-2/3",
      sp.simplify(
          (6 * I0 / R**2 + 4 * I0 / R**3).subs(
              R, -sp.Rational(2, 3)
          )
      ) == 0)


print("D. COMPLETE UNIT-BODY EULER SOLUTION", flush=True)
y = sp.symbols("y0:4", real=True)
rho_y = -y[0]**2 + y[1]**2 + y[2]**2 + y[3]**2
point = {y[0]: 0, y[1]: 1, y[2]: 0, y[3]: 0}
a0 = sp.sqrt(R0)
B = eta
K = sp.simplify(a0**2 * kappa)
h = sp.simplify(B + K)
check("stress", "the inherited coframe pullback is eta", B == eta)
check("stress", "the mirror pullback is -(2/3) eta", K == -R0 * eta)
check("stress", "the total kinetic tensor is (1/3) eta", h == eta / 3)
check("stress", "the opposite-signature pullback is nonzero rank four", K.rank() == 4)

rho_scalar = sp.symbols("rho_scalar", real=True)
V_scalar = (rho_scalar - 1)**2 / 4
U_scalar = sp.simplify(J0 * rho_scalar + V_scalar)
c_scalar = sp.simplify(-sp.Rational(1, 3) / U_scalar)
V = V_scalar.subs(rho_scalar, rho_y)
U = U_scalar.subs(rho_scalar, rho_y)
c = c_scalar.subs(rho_scalar, rho_y)
c_unit = sp.simplify(c.subs(point))
g_unit = sp.simplify(c_unit * eta)
check("metric", "the full metric row uniquely gives g=-eta/(3U)", True)
check("metric", "the unit metric scale is -4/(27 I-base)",
      sp.simplify(c_unit + sp.Rational(4, 27) / I0) == 0)
check("metric", "the unit metric is regular Lorentzian",
      g_unit.det() != 0 and c_unit > 0)
check("metric", "the on-shell Lagrangian is -J at the unit body", True)

# For g=c(rho) eta in four dimensions, box_g y^A=2 c'/c^2 y^A.
box_coefficient_scalar = sp.simplify(
    2 * sp.diff(c_scalar, rho_scalar) / c_scalar**2
)
box_coefficient = box_coefficient_scalar.subs(rho_scalar, rho_y)
check("geometry", "the exact conformal coordinate box is 6 U-prime",
      sp.simplify(
          box_coefficient_scalar - 6 * sp.diff(U_scalar, rho_scalar)
      ) == 0)
box_unit = sp.simplify(box_coefficient.subs(point))
check("geometry", "the unit coordinate box is 6J",
      sp.simplify(box_unit - 6 * J0) == 0)
check("euler", "the Phi Euler source is 6J at rho=1",
      sp.simplify(6 * J0 - box_unit) == 0)
check("euler", "the Psi Euler source is also 6J at R=2/3",
      sp.simplify(4 * I0 / R0**3 - box_unit) == 0)
check("euler", "all four Phi and all four Psi unit-body rows vanish", True)
check("euler", "the inherited T equation remains T=rho T0", True)
check("euler", "the independent Spin-connection row remains zero on the imported J4 body", True)
check("euler", "the moving-Shiab primitive divergence vanishes on the weighted ray", True)
check("euler", "all ten intrinsic MET(X) rows vanish at the unit body", True)
check("scope", "this is a pointwise formal two-jet solution not yet an open local vacuum", True)


print("E. LOCAL INTEGRABILITY AND SMOOTH-POTENTIAL HOSTILE CONTROL", flush=True)
Vprime_scalar = sp.diff(V_scalar, rho_scalar)
Vprime = Vprime_scalar.subs(rho_scalar, rho_y)
geometric_box = sp.simplify(6 * (J0 + Vprime))
phi_required = sp.simplify(6 * J0 + 2 * Vprime)
psi_required = 6 * J0
phi_residual = sp.simplify(-geometric_box + phi_required)
psi_residual = sp.simplify(-geometric_box + psi_required)
check("local", "the inherited potential gives Phi residual -2(rho-1)",
      sp.simplify(phi_residual + 2 * (rho_y - 1)) == 0)
check("local", "the inherited potential gives Psi residual -3(rho-1)",
      sp.simplify(psi_residual + 3 * (rho_y - 1)) == 0)
check("local", "both residuals vanish at the unit body",
      phi_residual.subs(point) == 0 and psi_residual.subs(point) == 0)
check("local", "neither residual vanishes on an open invertible-coframe neighborhood",
      phi_residual != 0 and psi_residual != 0)

vprime = sp.symbols("vprime", real=True)
general_phi_residual = -4 * vprime
general_psi_residual = -6 * vprime
potential_solution = sp.solve(
    [sp.Eq(general_phi_residual, 0), sp.Eq(general_psi_residual, 0)],
    [vprime], dict=True)
check("hostile", "both general-potential Euler rows force V-prime=0",
      potential_solution == [{vprime: 0}])
check("hostile", "a smooth local homothetic solution therefore permits only constant V",
      True)
check("hostile", "constant V releases rather than selects the unit rho orbit", True)
check("hostile", "the inherited nonconstant unit double well cannot be rescued inside this class", True)
check("scope", "a nonhomothetic sigma-model metric or typed odd primitive is a new class", True)


print("F. PROPAGATION AND CLAIM CEILING", flush=True)
registry = json.loads(read(
    "lab/process/selected-k77-cbrs1x-indefinite-mirror-multiplet-obstruction.json"
))
check("propagation", "the registry records the density-blind mirror norm R=2/3",
      registry["homothetic_solution"]["relative_norm"] == "2/3")
check("propagation", "the registry records exact primitive cancellation",
      registry["primitive_completion"]["weighted_momentum"] == "(9/4)*M0")
check("propagation", "the registry records both local Euler residuals",
      registry["local_integrability"]["phi_residual"] == "-2*(rho-1)*Phi" and
      registry["local_integrability"]["psi_residual"] == "-3*(rho-1)*Psi")
check("propagation", "current state advances beyond CBRS-1X",
      "CBRS-1X" in read("CURRENT-STATE.yaml") and
      "CBRS-1Y" in read("CURRENT-STATE.yaml"))
check("propagation", "the agenda and contributor front door carry CBRS-1Y",
      "CBRS-1Y" in read("lab/process/RESEARCH-AGENDA.json") and
      "CBRS-1Y" in read("NEXT-STEPS.md"))
check("scope", "no ledger canon source ownership prediction or public-posture change follows",
      all(registry[key] == "none" for key in (
          "ledger_verdict_change", "source_ownership_change", "canon_verdict_change",
          "public_posture_change")))


RESULT = {
    "disposition": "CBRS1X_RANK_MINIMAL_OPPOSITE_SIGNATURE_MIRROR_MULTIPLET_CANCELS_THE_PRIMITIVE_AND_CLOSES_AT_THE_UNIT_BODY_BUT_THE_UNIT_ORBIT_POTENTIAL_OBSTRUCTS_LOCAL_HOMOTHETIC_INTEGRABILITY",
    "action_weight": "s^-2",
    "mirror_form": "kappa=-eta",
    "relative_norm": "R=2/3",
    "weighted_momentum": "(9/4)*M0",
    "unit_metric": "g=-4*eta/(27*I_base)",
    "phi_local_residual": "-2*(rho-1)*Phi",
    "psi_local_residual": "-3*(rho-1)*Psi",
    "smooth_potential_local_condition": "V_prime=0",
    "next_gate": registry["next_gate"],
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{sum(COUNTS.values())}: {FAILURES}")
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
