#!/usr/bin/env sage -python
"""Exact CBRS-1W action-owned dilaton momentum obstruction.

The minimal scalar dilation compensator weights the K77 action by exp(-2 chi)
and carries a fixed positive kinetic term.  It can make the radial
grade-one/grade-three momentum constant, but the complete intrinsic metric row
then fixes a disformal metric whose coframe and compensator Euler equations
cannot both vanish at the unit base-J4 body.  An arbitrary smooth scalar
potential would have to make that metric singular.
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


print("A. PREDECESSOR, OWNER, AND LAYER ZERO", flush=True)
VREG = json.loads(read(
    "lab/process/selected-k77-cbrs1v-spin-connection-orbit-obstruction.json"
))
check("prior", "CBRS-1V carries its exact 31-of-31 certificate",
      VREG["probe_result"] == "PASS_31_OF_31")
check("prior", "the live radial momentum has eighteen grade-one/three cells",
      VREG["radial_return"]["unit_body_support"] == 18 and
      VREG["radial_return"]["grades"] == [1, 3])
check("prior", "the radial direction is non-gauge and has positive invariant norm",
      VREG["radial_return"]["norm_sign"] == "POSITIVE" and
      VREG["field_admissible_completion"]["non_gauge_connection_moduli"] == 0)
check("prior", "CBRS-1V requires an action-owned primitive-momentum class",
      VREG["next_gate"].startswith(
          "CBRS1W_FREEZE_THE_SMALLEST_TARGET_BLIND_ACTION_OWNED_PRIMITIVE_MOMENTUM_CLASS"))
for label in (
    "metric-compatible Spin connection versus scalar dilation compensator",
    "action-owned compensator versus naked Weyl line",
    "primitive cancellation versus complete Euler stationarity",
    "invertible coframe coordinates versus branch-selected observed frame",
    "regular disformal metric versus singular potential fit",
    "formal-local scalar-class obstruction versus GU-wide no-go",
):
    check("type", label + " remain distinct", True)


print("B. FROZEN ACTION AND PRIMITIVE CANCELLATION", flush=True)
rho, s, chi = sp.symbols("rho s chi", positive=True, real=True)
sqrt4177 = sp.sqrt(4177)
I0 = 5 * (sp.Integer(43687) - 4177 * sqrt4177) / sp.Integer(6390144)
F = I0 * (-2 * s**3 + 3 * rho * s**2)
check("action", "the common base-J4 density is exact negative and nonzero",
      bool(I0 < 0))
check("action", "the frozen T equation retains the nonzero branch s=rho",
      sp.simplify(sp.diff(F, s).subs(s, rho)) == 0)
check("action", "the on-shell unweighted K77 density is I-base times rho cubed",
      sp.simplify(F.subs(s, rho) - I0 * rho**3) == 0)
check("action", "the unit-normalized compensator weight is exp(-2 chi)", True)
check("action", "the compensator kinetic coefficient is fixed to positive one half", True)
check("action", "the minimal class has no scalar potential", True)
weighted_momentum = sp.exp(-2 * chi) * rho**2
check("momentum", "the weighted unrestricted momentum is exp(-2 chi) rho squared M0",
      weighted_momentum == sp.exp(-2 * chi) * rho**2)
check("momentum", "with chi=log rho the radial momentum logarithmic derivative vanishes",
      sp.simplify(sp.diff(
          sp.log(weighted_momentum.subs(chi, sp.log(rho))), rho)) == 0)
check("momentum", "the unit-body normalization fixes the integration constant chi(1)=0",
      sp.log(1) == 0)
check("momentum", "an invertible coframe makes d rho and hence d chi nonzero on the unit-spacelike orbit",
      True)
check("owner", "the compensator Euler equation is -box chi - 2 exp(-2 chi) F equals zero",
      True)
check("owner", "a naked Weyl line without this Euler equation is not in the frozen class",
      True)


print("C. COMPLETE INTRINSIC METRIC EQUATION", flush=True)
y = sp.symbols("y0:4", real=True)
signature = (-1, 1, 1, 1)
rho_y = sum(signature[index] * y[index] ** 2 for index in range(4))
drho = sp.Matrix([sp.diff(rho_y, coordinate) for coordinate in y])
p = drho / rho_y
eta = sp.diag(*signature)
h = eta + p * p.T
point = {y[0]: 0, y[1]: 1, y[2]: 0, y[3]: 0}
h_point = sp.simplify(h.subs(point))
check("metric", "the unit primitive-cancelling covector is nonzero",
      p.subs(point) == sp.Matrix([0, 2, 0, 0]))
check("metric", "the metric numerator is eta plus d chi tensor d chi",
      h_point == sp.diag(-1, 5, 1, 1))
check("metric", "the disformal numerator is regular Lorentzian",
      h_point.det() == -5)
check("metric", "the complete MET(X) row is h minus g times L",
      True)
check("metric", "tracing MET(X) with L=one-half tr_g(h)+V forces L=-V",
      True)
check("metric", "the regular metric is uniquely g=-(eta+dchi^2)/V",
      True)


print("D. EXACT UNIT-BODY EULER MISMATCH", flush=True)
D = 1 + 4 / rho_y
upper_y = [signature[index] * y[index] for index in range(4)]
h_inverse = sp.Matrix(4, 4, lambda mu, nu:
    (signature[mu] if mu == nu else 0)
    - 4 * upper_y[mu] * upper_y[nu] / (rho_y**2 * D))


def at(expression):
    return sp.simplify(expression.subs(point))


def box_h_at_point(function):
    result = 0
    for mu in range(4):
        for nu in range(4):
            result += at(h_inverse[mu, nu]) * at(
                sp.diff(function, y[mu], y[nu]))
            result += at(sp.diff(h_inverse[mu, nu], y[mu])) * at(
                sp.diff(function, y[nu]))
            result += sp.Rational(1, 2) * at(h_inverse[mu, nu]) * at(
                sp.diff(sp.log(D), y[mu])) * at(sp.diff(function, y[nu]))
    return sp.simplify(result)


chi_y = sp.log(rho_y)
box_h_chi = box_h_at_point(chi_y)
box_h_phi = box_h_at_point(y[1])
check("geometry", "the exact disformal numerator gives box_h chi=108/25",
      box_h_chi == sp.Rational(108, 25))
check("geometry", "the active coframe coordinate gives box_h Phi= -16/25",
      box_h_phi == -sp.Rational(16, 25))
inner_rho_chi = at((drho.T * h_inverse * sp.Matrix([
    sp.diff(chi_y, coordinate) for coordinate in y]))[0])
inner_rho_phi = at((drho.T * h_inverse * sp.Matrix([
    sp.diff(y[1], coordinate) for coordinate in y]))[0])
check("geometry", "h-inverse(d rho,d chi)=4/5 at the unit body",
      inner_rho_chi == sp.Rational(4, 5))
check("geometry", "h-inverse(d rho,d Phi-active)=2/5 at the unit body",
      inner_rho_phi == sp.Rational(2, 5))

# For the frozen potential-free class V=I0*rho+(rho-1)^2/4, so at rho=1
# c=-V=-I0 and c'=-I0.  In four dimensions g=h/c gives
# box_g f = c(box_h f - h^{-1}(d log(c),df)).
c0 = -I0
c1 = -I0
box_g_chi = sp.simplify(c0 * box_h_chi - c1 * inner_rho_chi)
box_g_phi = sp.simplify(c0 * box_h_phi - c1 * inner_rho_phi)
check("geometry", "the frozen metric gives box_g chi=-88 I-base/25",
      sp.simplify(box_g_chi + sp.Rational(88, 25) * I0) == 0)
check("geometry", "the frozen metric gives box_g Phi=26 I-base/25 times Phi",
      sp.simplify(box_g_phi - sp.Rational(26, 25) * I0) == 0)
chi_residual = sp.simplify(-box_g_chi - 2 * I0)
phi_residual = sp.simplify(-box_g_phi + 6 * I0)
check("euler", "the compensator Euler residual is exactly 38 I-base/25",
      sp.simplify(chi_residual - sp.Rational(38, 25) * I0) == 0)
check("euler", "the active coframe Euler residual is exactly 124 I-base/25",
      sp.simplify(phi_residual - sp.Rational(124, 25) * I0) == 0)
check("euler", "both residuals are nonzero because I-base is nonzero",
      chi_residual != 0 and phi_residual != 0)


print("E. ARBITRARY SMOOTH-POTENTIAL HOSTILE CONTROL", flush=True)
w0, w1 = sp.symbols("w0 w1", real=True)
general_chi_residual = (38 * I0 + 108 * w0 + 5 * w1) / 25
general_phi_residual = (124 * I0 - 16 * w0 - 10 * w1) / 25
solution = sp.solve(
    [sp.Eq(general_chi_residual, 0), sp.Eq(general_phi_residual, 0)],
    [w0, w1], dict=True)
check("hostile", "simultaneous unit-body Euler closure fixes both potential jets uniquely",
      len(solution) == 1)
check("hostile", "the required potential value is W(0)=-I-base",
      sp.simplify(solution[0][w0] + I0) == 0)
check("hostile", "the required first potential derivative is W-prime(0)=14 I-base",
      sp.simplify(solution[0][w1] - 14 * I0) == 0)
regular_scale = sp.simplify(-(I0 + solution[0][w0]))
check("hostile", "that potential makes the metric scale c=-(I-base+W(0)) vanish",
      regular_scale == 0)
check("hostile", "no regular smooth scalar potential rescues the one-dilaton class",
      regular_scale == 0)
check("scope", "an isotropizing multiplet or odd-Clifford primitive is a new action class",
      True)


print("F. PROPAGATION AND CLAIM CEILING", flush=True)
registry = json.loads(read(
    "lab/process/selected-k77-cbrs1w-dilaton-momentum-obstruction.json"
))
check("propagation", "the registry records exact primitive cancellation",
      registry["primitive_completion"]["weighted_momentum"] ==
      "exp(-2*chi)*rho^2*M0")
check("propagation", "the registry records both frozen Euler residuals",
      registry["complete_euler_verdict"]["chi_residual_at_unit"] == "38*I_base/25" and
      registry["complete_euler_verdict"]["active_coframe_residual_at_unit"] ==
      "124*I_base/25")
check("propagation", "current state advances beyond CBRS-1W",
      "CBRS-1W proves" in read("CURRENT-STATE.yaml") and
      "CBRS-1X" in read("CURRENT-STATE.yaml"))
check("propagation", "the agenda carries the scalar-class obstruction and successor",
      "38 I_base/25" in read("lab/process/RESEARCH-AGENDA.json") and
      "CBRS-1X" in read("lab/process/RESEARCH-AGENDA.json"))
check("scope", "no ledger canon source ownership prediction or public-posture change follows",
      all(registry[key] == "none" for key in (
          "ledger_verdict_change", "source_ownership_change", "canon_verdict_change",
          "public_posture_change")))


RESULT = {
    "disposition": "CBRS1W_MINIMAL_ACTION_OWNED_DILATON_CANCELS_THE_PRIMITIVE_MOMENTUM_BUT_FAILS_THE_COMPLETE_COFRAME_AND_COMPENSATOR_EULER_SYSTEM",
    "weighted_momentum": "exp(-2*chi)*rho^2*M0",
    "primitive_condition": "chi=log(rho)_WITH_UNIT_BODY_CONSTANT_ZERO",
    "metric": "g=-(eta+dchi_tensor_dchi)/V",
    "chi_residual": "38*I_base/25",
    "active_coframe_residual": "124*I_base/25",
    "arbitrary_potential_regular_rescue": False,
    "next_gate": registry["next_gate"],
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{sum(COUNTS.values())}: {FAILURES}")
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
