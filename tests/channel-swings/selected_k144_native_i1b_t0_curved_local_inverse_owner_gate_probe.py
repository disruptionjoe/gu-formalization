#!/usr/bin/env python3
"""Exact controls for the K144 curved local-inverse owner gate."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "explorations/conditional-build/selected-k144-native-i1b-t0-curved-local-inverse-owner-gate-2026-08-16.md"
REGISTRY = ROOT / "lab/process/selected-k144-native-i1b-t0-curved-local-inverse-owner-gate.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k144-native-i1b-t0-curved-local-inverse-owner-gate-review.md"

checks = 0


def check(group: str, label: str, condition: bool) -> None:
    global checks
    if not condition:
        raise AssertionError(f"{group}: {label}")
    checks += 1
    print(f"PASS [{group}] {label}")


kappa, xi, x, s = sp.symbols("kappa xi x s", nonzero=True)
i = sp.I

# A positive-order scalar differential symbol has no polynomial inverse.
for degree in range(5):
    coeffs = sp.symbols(f"p0:{degree + 1}")
    polynomial = sum(coeffs[j] * xi**j for j in range(degree + 1))
    equations = sp.Poly(sp.expand((kappa + i * xi) * polynomial - 1), xi).all_coeffs()
    solution = sp.solve(equations, coeffs, dict=True)
    check("locality", f"no polynomial inverse through degree {degree}", solution == [])

rational_inverse = 1 / (kappa + i * xi)
check("locality", "frozen inverse is exact rational response", sp.simplify((kappa + i * xi) * rational_inverse) == 1)
check("locality", "frozen inverse is not polynomial", not rational_inverse.is_polynomial(xi))

# First left-symbol inverse correction for c0=kappa+i*a(x)*xi.
a = sp.Function("a")(x)
c0 = kappa + i * a * xi
r0 = 1 / c0
left_defect = sp.simplify((1 / i) * sp.diff(c0, xi) * sp.diff(r0, x))
r1_left = sp.simplify(-r0 * left_defect)
expected_left = sp.simplify(i * a * sp.diff(a, x) * xi / c0**3)
check("parametrix", "left first correction derived", sp.simplify(r1_left - expected_left) == 0)
check("parametrix", "left correction cancels first composition defect", sp.simplify(c0 * r1_left + left_defect) == 0)

poisson = sp.simplify(sp.diff(c0, xi) * sp.diff(r0, x) - sp.diff(c0, x) * sp.diff(r0, xi))
check("parametrix", "Weyl first Poisson correction vanishes", poisson == 0)

a_s = 1 + s * x
c_s = kappa + i * a_s * xi
r0_s = 1 / c_s
r1_s = sp.simplify(-r0_s * (1 / i) * sp.diff(c_s, xi) * sp.diff(r0_s, x))
r1_at_zero = sp.simplify(r1_s.subs(x, 0))
check("jets", "same-frozen family has common leading inverse", sp.simplify(r0_s.subs(x, 0) - rational_inverse) == 0)
check("jets", "first correction records free slope", sp.simplify(r1_at_zero - i * s * xi / (kappa + i * xi) ** 3) == 0)
check("jets", "zero-slope correction vanishes", sp.simplify(r1_at_zero.subs(s, 0)) == 0)
check("jets", "nonzero-slope correction is nonzero", sp.simplify(r1_at_zero.subs({s: 2, kappa: 1, xi: 1})) != 0)

# Nilpotent system control: the same frozen principal matrix can have a
# derivative-dependent local differential inverse.  For P=M D,
# P^2=(M M')D+M^2 D^2.
u = sp.Matrix([1, s * x])
v = sp.Matrix([-s * x, 1])
M = sp.simplify(u * v.T)
M_prime = M.diff(x)
check("nilpotent-system", "pointwise principal matrix is square-zero", sp.simplify(M * M) == sp.zeros(2))
check("nilpotent-system", "operator first-order composition coefficient is s*M", sp.simplify(M * M_prime - s * M) == sp.zeros(2))
check("nilpotent-system", "all slopes share frozen matrix at x=0", sp.simplify(M.subs(x, 0) - sp.Matrix([[0, 1], [0, 0]])) == sp.zeros(2))

# In the quotient algebra P^2=sP, Q below is an exact two-sided inverse.
q0 = 1 / kappa
q1 = -1 / (kappa * (kappa + s))
identity_coeff = sp.simplify(kappa * q0)
p_coeff = sp.simplify(kappa * q1 + q0 + s * q1)
check("nilpotent-system", "local inverse identity coefficient", identity_coeff == 1)
check("nilpotent-system", "local inverse P coefficient cancels", p_coeff == 0)
check("nilpotent-system", "local inverse depends on neighborhood slope", sp.diff(q1, s) != 0)

# Abstract H/G control: principal quotient data allow basic and non-basic maps.
dim = 10
ell = sp.zeros(1, dim)
ell[0, 9] = 1
H_basis = [sp.eye(dim).col(j) for j in range(9)]
G_basis = H_basis[:4]
check("quotient", "radical dimension nine", len(H_basis) == 9)
check("quotient", "gauge dimension four", len(G_basis) == 4)
check("quotient", "quotient dimension five", len(H_basis) - len(G_basis) == 5)

good = sp.eye(dim)
bad = sp.eye(dim)
bad[:, 0] = H_basis[4]
check("quotient", "planted good map preserves radical", all((ell * good * h)[0] == 0 for h in H_basis))
check("quotient", "planted good map preserves gauge", all(good * g in G_basis for g in G_basis))
check("quotient", "planted bad map still preserves radical", all((ell * bad * h)[0] == 0 for h in H_basis))
check("quotient", "planted bad map fails gauge preservation", bad * G_basis[0] not in G_basis)

artifact = ARTIFACT.read_text()
registry = json.loads(REGISTRY.read_text())
review = REVIEW.read_text()
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text()
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
tests_readme = (ROOT / "tests/README.md").read_text()

check("artifact", "routing notice present", "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
check("artifact", "classification explicit", "Classification: `SOURCE_NATIVE_ROUTE`." in artifact)
check("artifact", "scope sentence present", "Scope: K144 binds" in artifact)
check("artifact", "local coupled owner preserved", "local coupled Hessian" in artifact and "action-owned" in artifact)
check("artifact", "zero overclaim excluded", "not zero, pass, or fail" in artifact)
check("registry", "basicness remains undefined", registry["quotient"]["basicness"] == "UNDEFINED_NO_CURVED_REDUCTION_EVALUATOR")
check("registry", "no reduced endomorphism booked", registry["quotient"]["owned_reduced_endomorphism_exists"] is False)
check("registry", "coupled Noether system retained", registry["owned_result"]["local_coupled_noether_system"] is True)
check("review", "systems overclaim corrected", "corrected before publication" in review)
check("review", "quantization is not physical nonuniqueness", "does not mean observable" in review)
check("repo", "current state advances through K144", "K144 now proves" in current)
check("repo", "roadmap advances to K145", "K145" in roadmap[:12000])
check("repo", "context carries reduction-evaluator result", "UNDEFINED_NO_CURVED_REDUCTION_EVALUATOR" in context[:12000])
check("repo", "tests inventory includes probe", "selected_k144_native_i1b_t0_curved_local_inverse_owner_gate_probe.py" in tests_readme)
k138 = json.loads((ROOT / "lab/process/selected-k138-native-i1b-t0-null-stratum-covariant-transport.json").read_text())
k143 = json.loads((ROOT / "lab/process/selected-k143-native-i1b-t0-fixed-action-subprincipal-owner-obstruction.json").read_text())
check("predecessor", "K138 retains rank-five quotient and Brinkmann freedom", k138["null_stratum"]["gauge_reduced_dimension"] == 5 and k138["three_jet"]["exact_family"].startswith("RICCI_FLAT_BRINKMANN") and k138["three_jet"]["independent_curvature_derivative_parameters"] == 2)
check("predecessor", "K143 retains missing-coefficient disposition", k143["quotient_basicness"]["actual_lower_coefficient_basicness"] == "UNDEFINED_NO_OWNED_COEFFICIENT")

print(f"PASS {checks}/{checks}")
