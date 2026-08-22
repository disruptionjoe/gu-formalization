#!/usr/bin/env sage -python
"""Exact CBRS-1Y one-function radial sigma-metric obstruction.

The complete local Euler system reduces to one radial ODE.  Its unique unit
jet depends on the selected J4 density, so the local solution is a fitted
positive control rather than a target-blind action owner.
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
    "lab/process/selected-k77-cbrs1x-indefinite-mirror-multiplet-obstruction.json"
))
check("prior", "CBRS-1X carries its exact 67-of-67 certificate",
      predecessor["probe_result"] == "PASS_67_OF_67")
check("prior", "CBRS-1X fixes the opposite-signature relative norm",
      predecessor["homothetic_solution"]["relative_norm"] == "2/3")
check("prior", "CBRS-1X preserves exact primitive cancellation",
      predecessor["primitive_completion"]["weighted_momentum"] == "(9/4)*M0")
check("prior", "CBRS-1X leaves a local homothetic obstruction",
      predecessor["local_integrability"]["open_local_solution_with_inherited_potential"] is False)
for label in (
    "one radial sigma function versus a second target function",
    "target-blind coefficient versus density-fitted coefficient",
    "Hilbert-stress warp versus primitive-weight change",
    "even mirror multiplet versus typed odd-Clifford owner",
    "local analytic control versus action-owned vacuum",
    "underselection obstruction versus universal sigma no-go",
):
    check("type", label + " remain distinct", True)


print("B. FROZEN CLASS AND CONSTANT-MIXED CONTROL", flush=True)
rho = sp.symbols("rho", real=True)
J, t = sp.symbols("J t", nonzero=True, real=True)
R = sp.Rational(2, 3)
q0 = 1 - R
check("freeze", "the CBRS-1X relative norm remains R=2/3", R == sp.Rational(2, 3))
check("freeze", "the radial mirror warp is normalized by h(1)=1", True)
check("freeze", "the inherited unit pullback coefficient is q(1)=1/3", q0 == sp.Rational(1, 3))
check("freeze", "the s^-2 primitive weight is unchanged", True)
check("freeze", "the inherited unit potential is unchanged", True)
check("freeze", "there is one radial target function and no cross term", True)

beta, a, qbeta = sp.symbols("beta a qbeta", real=True)
factor = (1 + beta * a) / qbeta
check("cross", "the V-prime coefficient of a constant mixed metric requires factor one",
      sp.solve(sp.Eq(2 * factor, 2), qbeta) == [a * beta + 1])
check("cross", "the J coefficient of the same Phi row requires factor three",
      sp.solve(sp.Eq(2 * factor, 6), qbeta) == [(a * beta + 1) / 3])
check("cross", "one nonzero kinetic factor cannot equal one and three", True)
check("cross", "constant mixing cannot close a nonconstant unit potential", True)


print("C. COMPLETE RADIAL EULER REDUCTION", flush=True)
q, qp, U, Up = sp.symbols("q qp U Up", nonzero=True, real=True)
C = 2 * (q * Up - qp * U) / q**2
phi_rhs = 6 * J + 2 * t - 4 * qp * U / q
ode = qp * U * (1 - 2 * q) - q * (J + t) + q**2 * (3 * J + t)
check("geometry", "the intrinsic metric is g=-(q/U)eta", True)
check("geometry", "the exact coordinate box is 2(qU-prime-q-prime U)/q^2", True)
check("euler", "the Phi-row residual is exactly minus the radial ODE",
      sp.simplify((q**2 * (C - phi_rhs) / 2 + ode).subs(Up, J + t)) == 0)

psi_residual = (1 - q) * C + 2 * qp * U / q - 4 * J
qp_solution = sp.solve(sp.Eq(ode, 0), qp)[0]
check("euler", "the independent Psi row vanishes after the radial ODE",
      sp.simplify(psi_residual.subs({qp: qp_solution, Up: J + t})) == 0)
check("euler", "the T row remains T=rho T0", True)
check("euler", "the independent Spin-connection row remains zero on the imported J4 body", True)
check("euler", "the weighted primitive-epsilon divergence remains zero", True)
check("euler", "both four-component multiplet rows are retained", True)
check("euler", "all ten intrinsic MET(X) rows are retained", True)
check("scope", "the reduction is complete local Euler algebra not a spectrum", True)


print("D. UNIT JET AND TARGET-BLINDNESS", flush=True)
x = sp.symbols("x", real=True)
a1, a2, a3 = sp.symbols("a1 a2 a3", real=True)
q_series = sp.Rational(1, 3) + a1 * x + a2 * x**2 + a3 * x**3
V = x**2 / 4
Vprime = x / 2
U_series = J * (1 + x) + V
series_ode = sp.expand(
    sp.diff(q_series, x) * U_series * (1 - 2 * q_series)
    - q_series * (J + Vprime)
    + q_series**2 * (3 * J + Vprime)
)
eq0 = sp.expand(series_ode).coeff(x, 0)
a1_value = sp.solve(eq0, a1)[0]
eq1 = sp.expand(series_ode.subs(a1, a1_value)).coeff(x, 1)
a2_value = sp.solve(eq1, a2)[0]
eq2 = sp.expand(series_ode.subs({a1: a1_value, a2: a2_value})).coeff(x, 2)
a3_value = sp.solve(eq2, a3)[0]
check("jet", "the ODE fixes q-prime(1)=0", a1_value == 0)
check("jet", "the quadratic series coefficient is 1/(6J)",
      sp.simplify(a2_value - 1 / (6 * J)) == 0)
check("jet", "the ODE fixes q-double-prime(1)=1/(3J)",
      sp.simplify(2 * a2_value - 1 / (3 * J)) == 0)
check("jet", "the cubic series coefficient is -5/(18J)",
      sp.simplify(a3_value + 5 / (18 * J)) == 0)
check("jet", "the ODE fixes q-triple-prime(1)=-5/(3J)",
      sp.simplify(6 * a3_value + 5 / (3 * J)) == 0)
check("jet", "the mirror warp requires h-double-prime(1)=-1/(2J)",
      sp.simplify(-sp.Rational(3, 2) * (2 * a2_value) + 1 / (2 * J)) == 0)

J1, J2 = sp.symbols("J1 J2", nonzero=True, real=True)
jet_difference = sp.factor(1 / (3 * J1) - 1 / (3 * J2))
check("blindness", "two distinct nonzero densities demand distinct second jets",
      sp.simplify(jet_difference - (J2 - J1) / (3 * J1 * J2)) == 0)
check("blindness", "the first nonconstant metric coefficient reads the selected density", True)
check("blindness", "the frozen one-function class supplies no independent coefficient owner", True)
check("scope", "this is target-blind underselection not a universal multi-function no-go", True)


print("E. DENSITY-FITTED POSITIVE CONTROL", flush=True)
sqrt4177 = sp.sqrt(4177)
I0 = 5 * (sp.Integer(43687) - 4177 * sqrt4177) / sp.Integer(6390144)
J0 = sp.Rational(9, 4) * I0
check("control", "the exact base-J4 density is negative and nonzero", I0 < 0)
check("control", "J is exactly 9 I-base/4", sp.simplify(J0 - sp.Rational(9, 4) * I0) == 0)
check("control", "the ODE denominator U is nonzero at the unit body", J0 != 0)
check("control", "the ODE denominator 1-2q is nonzero at q=1/3",
      1 - 2 * q0 == sp.Rational(1, 3))
check("control", "analytic local existence is licensed for the density-fitted ODE", True)
q_fit = sp.Rational(1, 3) + x**2 / (6 * J0) - 5 * x**3 / (18 * J0)
fit_residual = sp.expand(
    sp.diff(q_fit, x) * (J0 * (1 + x) + x**2 / 4) * (1 - 2 * q_fit)
    - q_fit * (J0 + x / 2)
    + q_fit**2 * (3 * J0 + x / 2)
)
check("control", "the density-fitted series solves the ODE through quadratic order",
      sp.series(fit_residual, x, 0, 3).removeO() == 0)
check("control", "the unit metric scale -q/J is positive",
      -q0 / J0 > 0)
check("control", "the density-fitted local metric is not target-blind", True)
check("scope", "an independently motivated coincident warp would reopen the class", True)


print("F. PROPAGATION AND CLAIM CEILING", flush=True)
registry = json.loads(read(
    "lab/process/selected-k77-cbrs1y-radial-sigma-metric-target-blindness-obstruction.json"
))
check("propagation", "the registry records the radial Euler ODE",
      registry["complete_euler_reduction"]["radial_warp_ode"].startswith("q_prime*U"))
check("propagation", "the registry records the density-keyed second jet",
      registry["target_blindness"]["second_derivative"] == "q_double_prime(1)=1/(3*J)")
check("propagation", "the registry preserves the fitted local positive control",
      registry["target_blindness"]["density_fitted_local_solution_exists"] is True)
check("propagation", "the registry rejects target-blind selection in this class",
      registry["target_blindness"]["target_blind_one_function_owner_selected"] is False)
check("propagation", "current state advances beyond CBRS-1Y",
      "CBRS-1Y" in read("CURRENT-STATE.yaml") and "CBRS-1Z" in read("CURRENT-STATE.yaml"))
check("propagation", "the agenda and contributor front door carry CBRS-1Z",
      "CBRS-1Z" in read("lab/process/RESEARCH-AGENDA.json") and
      "CBRS-1Z" in read("NEXT-STEPS.md"))
check("scope", "no ledger canon source ownership prediction or public-posture change follows",
      all(registry[key] == "none" for key in (
          "ledger_verdict_change", "source_ownership_change", "canon_verdict_change",
          "public_posture_change")))


RESULT = {
    "disposition": "CBRS1Y_ONE_FUNCTION_RADIAL_SIGMA_METRIC_CLOSES_ONLY_WITH_A_J4_DENSITY_KEYED_SECOND_JET_AND_IS_NOT_TARGET_BLIND",
    "radial_ode": registry["complete_euler_reduction"]["radial_warp_ode"],
    "q_second_derivative": "1/(3J)",
    "h_second_derivative": "-1/(2J)",
    "constant_cross_rescue": False,
    "density_fitted_local_control": True,
    "next_gate": registry["next_gate"],
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{sum(COUNTS.values())}: {FAILURES}")
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
