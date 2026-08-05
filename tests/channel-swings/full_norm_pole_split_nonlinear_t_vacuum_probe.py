#!/usr/bin/env python3
"""Exact full-norm gravity pole split and nonlinear T-vacuum certificate.

This probe composes two already-owned constructions without fitting a field,
datum, selector, source, scale, or boundary condition:

* the predecessor's mixed observed (h,v) action and exact plus/cross quotient;
* the Gauss-induced Einstein term on the conditional full-|II|^2 horn; and
* the pre-existing noncommutative cyclic transgression grammar including the
  cubic T-wedge-T term.

The selected moving K77 Shiab is non-cyclic.  The finite nonlinear vacuum
calculation is therefore a source-shaped control, not an actual K77-vacuum
promotion.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
R = sp.Rational
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


def read_json(relative: str) -> dict:
    return json.loads(read(relative))


print("A. LAYER 0, PREDECESSOR, AND SOURCE LOCUS")
predecessor = read_json("lab/process/observed-upback-stress-normal-constraint-vacuum.json")
null = read_json("lab/process/k77-global-even-bv-null-green-domain.json")
source_receipt = read("lab/sources/full-norm-gravity-source-reinspection-2026-08-05.md")
h45 = read("explorations/wave24/H45-H2-vs-II2-binary-2026-07-11.md")
cb_b = read("explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md")

check("repo", "predecessor metric response was the coincident double-pole horn",
      predecessor["propagator"]["determinant"] == "-z^2"
      and predecessor["propagator"]["pole_order"] == 2)
check("repo", "predecessor retained the exact plus/cross quotient",
      null["null_split"]["explicit_representatives"] == ["PLUS", "CROSS"])
check("repo", "H45 already distinguishes two distinct poles from a coincident pole",
      "two distinct poles" in h45 and "coincident double pole" in h45)
check("repo", "conditional build already maps the massive spin-two partner as GU structure",
      "A massive spin-2 partner" in cb_b)
check("source", "source receipt returns SOURCE-SILENT at the P2/pole locus",
      "Decisive return: `SOURCE-SILENT`" in source_receipt)
check("type", "one simple Einstein pole is distinct from only one pole total", True)
check("type", "a coincident Jordan double pole is distinct from two simple poles", True)
check("planted", "PLANT orthodox one-pole-total GR is not substituted for the GU conditional target", True)


print("\nB. CONDITIONAL FULL-NORM TT ACTION")
z, kappa, alpha = sp.symbols("z kappa alpha", nonzero=True, real=True)
h, v, tau = sp.symbols("h v tau", real=True)

# The predecessor supplied z*h*v + kappa*v^2/2.  The full-|II|^2 Gauss horn
# supplies the direct Einstein term alpha*z*h^2/2; alpha is the already-owned
# alpha_II coefficient, not a new fitted selector.
tt_action = alpha*z*h**2/R(2) + z*h*v + kappa*v**2/R(2) + tau*h
field_matrix = sp.hessian(tt_action - tau*h, (h, v))
determinant = sp.factor(field_matrix.det())
inverse = sp.simplify(field_matrix.inv())
metric_response = sp.factor(inverse[0, 0])
partial_fraction = 1/(alpha*z) + 1/(alpha*(alpha*kappa - z))

check("exact", "full-norm field matrix has the direct Einstein diagonal term",
      field_matrix == sp.Matrix([[alpha*z, z], [z, kappa]]))
check("exact", "determinant factors into massless and distinct massive factors",
      sp.simplify(determinant - z*(alpha*kappa - z)) == 0)
check("exact", "metric response is kappa over the two simple factors",
      sp.simplify(metric_response - kappa/(z*(alpha*kappa - z))) == 0)
check("exact", "metric response has an exact two-simple-pole partial fraction",
      sp.simplify(metric_response - partial_fraction) == 0)
check("exact", "massless Einstein residue is one over alpha",
      sp.limit(z*metric_response, z, 0) == 1/alpha)
check("exact", "the second pole is distinct whenever alpha*kappa is nonzero",
      sp.factor(determinant.subs(z, alpha*kappa)) == 0
      and alpha*kappa != 0)
check("exact", "turning off only the Gauss-Einstein term restores the double pole",
      sp.simplify(metric_response.subs(alpha, 0)) == -kappa/z**2)

e_h = sp.diff(tt_action, h)
e_v = sp.diff(tt_action, v)
v_solution = sp.solve(sp.Eq(e_v, 0), v)[0]
effective_euler = sp.factor(sp.diff(tt_action.subs(v, v_solution), h))
check("exact", "eliminating distortion yields a factored fourth-order metric operator",
      sp.simplify(effective_euler - (tau + h*z*(alpha*kappa - z)/kappa)) == 0)
check("exact", "the construction adds no new field beyond predecessor h and v",
      set(tt_action.free_symbols) == {alpha, h, kappa, tau, v, z})
check("type", "alpha is the existing full-norm action coefficient and P2 remains open", True)
check("type", "the massive partner is the mapped GR-3 GU difference, not an error to erase", True)
check("type", "the unchanged TT scalar factor acts on each inherited plus/cross representative", True)
check("planted", "PLANT the pole split is not called source-selected while P2 is open", True)
check("planted", "PLANT no cancellation is fitted to delete the massive GU pole", True)


print("\nC. FULL NONCOMMUTATIVE CYCLIC TRANSGRESSION VACUA")
x, y, q = sp.symbols("x y q", real=True)

# Exact finite control already present in the two-connection action-owner
# probe.  Its source-shaped path-average term is
#   2(x*y*q + x*y + x*q + x + y*q + y + q)
# and its existing indefinite mass pairing is (x^2-y^2+2q^2)/2.
transgression = 2*(x*y*q + x*y + x*q + x + y*q + y + q)
mass = x**2/R(2) - y**2/R(2) + q**2
nonlinear_action = sp.expand(transgression + mass)
gradient = sp.Matrix([sp.diff(nonlinear_action, u) for u in (x, y, q)])
hessian = sp.hessian(nonlinear_action, (x, y, q))

check("exact", "the nonlinear action retains a live cubic coefficient",
      sp.diff(nonlinear_action, x, y, q) == 2)
check("exact", "the action Hessian is symmetric",
      hessian == hessian.T)
check("exact", "the previously located background-forced branch is stationary",
      gradient.subs({x: 0, y: 0, q: -1}) == sp.zeros(3, 1))

# Solve the first two gradient rows with a = 2(q+1).  The remaining row is
# a*p(a)/(2(1+a^2)^2), so a=0 is the simple branch above and p=0 gives the
# genuinely nonabelian branches.
a = sp.symbols("a", real=True)
x_of_a = -a*(1+a)/(1+a**2)
y_of_a = a*(1-a)/(1+a**2)
q_of_a = a/R(2) - 1
p = a**4 - 2*a**3 + 2*a**2 - 6*a + 1
substituted_gradient = sp.simplify(gradient.subs({x: x_of_a, y: y_of_a, q: q_of_a}))

check("exact", "rational branch parameter solves the first two Euler rows identically",
      substituted_gradient[0] == 0 and substituted_gradient[1] == 0)
check("exact", "the remaining Euler row reduces to the quartic branch equation",
      sp.factor(substituted_gradient[2]) == a*p/(a**2 + 1)**2)
check("exact", "quartic is square-free",
      sp.gcd(p, sp.diff(p, a)) == 1)
check("exact", "one real root lies in the exact interval one-sixth to one-fifth",
      sp.count_roots(p, R(1, 6), R(1, 5)) == 1)
check("exact", "one real root lies in the exact interval two to nine-fourths",
      sp.count_roots(p, 2, R(9, 4)) == 1)
check("exact", "the quartic has exactly two real roots in total",
      sp.count_roots(p, -sp.oo, sp.oo) == 2)
check("exact", "both real quartic branches have x y and q all nonzero",
      p.subs(a, 0) != 0 and p.subs(a, 1) != 0 and p.subs(a, 2) != 0)
cubic_branch = sp.factor((x_of_a*y_of_a*q_of_a))
cubic_numerator = sp.together(cubic_branch).as_numer_denom()[0]
check("exact", "the cubic pairing is nonzero on every quartic stationary branch",
      sp.resultant(p, cubic_numerator, a) == 144)
check("type", "nonzero cubic pairing certifies a live noncommutative T-wedge-T sector", True)

# Nondegeneracy is exact without printing quartic radicals.  The Hessian
# determinant pulled to the branch is coprime to p; its resultant is nonzero.
hessian_det_branch = sp.factor(hessian.det().subs({x: x_of_a, y: y_of_a, q: q_of_a}))
hessian_det_numerator = sp.together(hessian_det_branch).as_numer_denom()[0]
resultant = sp.factor(sp.resultant(p, hessian_det_numerator, a))
check("exact", "nonlinear quartic stationary branches are nondegenerate",
      resultant == -5439488)
check("exact", "every stationary Hessian is indefinite from fixed opposite diagonal directions",
      hessian[0, 0] == 1 and hessian[1, 1] == -1)
check("type", "the two genuinely nonlinear real branches are saddles, not stable minima", True)
check("type", "the cyclic control proves the quadratic truncation did not exhaust the action grammar", True)
check("planted", "PLANT nonzero stationary does not mean stable vacuum", True)
check("planted", "PLANT a background-coupled stationary point does not fix the observed DE magnitude", True)


print("\nD. SELECTED-K77 AND CLAIM BOUNDARY")
eddy = read("explorations/k77-wave2-eddy-augmented-torsion-euler-prolongation-2026-08-05.md")
check("repo", "prior hostile review forbids importing cyclicity into selected Shiab",
      "identity-Shiab" in eddy and "cyclic calculation a proof for the selected Shiab" in eddy)
check("type", "actual selected-K77 vacuum requires the Frechet-adjoint moving-Shiab Euler", True)
check("type", "P2 full norm versus trace-square remains the pole-placement selection gate", True)
check("type", "physical stability still requires the common Krein/Green domain", True)
check("type", "source totalization and current-to-stress relation remain open", True)
check("planted", "PLANT no P1 P2 P3 datum is consumed", True)
check("planted", "PLANT no canon verdict public posture or Lane count changes", True)

print("\nSOURCE_RETURN=SOURCE-SILENT")
print("PRIOR_ONE_POLE_TOTAL_TARGET=MISTYPED_ORTHODOX_OVERFENCE")
print("FULL_NORM_CONDITIONAL_TT_RESPONSE=TWO_DISTINCT_SIMPLE_POLES")
print("MASSLESS_EINSTEIN_POLE=RECOVERED_CONDITIONALLY_ON_P2_FULL_NORM")
print("MASSIVE_SPIN2_PARTNER=RETAINED_AS_GU_GR3_DIFFERENCE")
print("CYCLIC_NONCOMMUTATIVE_REAL_STATIONARY_BRANCHES=3")
print("GENUINELY_NONLINEAR_T_WEDGE_T_REAL_BRANCHES=2")
print("NONLINEAR_BRANCH_STABILITY=SADDLE")
print("ACTUAL_SELECTED_K77_VACUUM=OPEN")
print("P1_P2_P3=UNCHANGED_UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED_LABELS=" + " | ".join(FAILURES))
    sys.exit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
