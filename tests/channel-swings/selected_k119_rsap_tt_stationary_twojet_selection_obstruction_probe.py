#!/usr/bin/env python3
"""Exact K119 stationary pullback and two-jet selection obstruction."""

from itertools import combinations_with_replacement
from pathlib import Path
import json
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


# One-dimensional pullback verifies exactly which jets survive stationarity.
x = sp.symbols("x")
ell, H, C, p, q, r = sp.symbols("ell H C p q r")
F = p*x + q*x**2/2 + r*x**3/6
I = ell*F + H*F**2/2 + C*F**3/6
d1 = sp.expand(I).diff(x).subs(x, 0)
d2 = sp.expand(I).diff(x, 2).subs(x, 0)
d3 = sp.expand(I).diff(x, 3).subs(x, 0)
check("stationarity", "pullback first derivative is ell times DF", d1 == ell*p)
check("stationarity", "stationary pullback constrains neither p nor q", d1.subs(ell, 0) == 0)
check("stationarity", "stationary Hessian depends only on H and DF", sp.expand(d2.subs(ell, 0) - H*p**2) == 0)
check("stationarity", "stationary cubic retains the second map jet", sp.expand(d3.subs(ell, 0) - (C*p**3 + 3*H*p*q)) == 0)
check("control", "off-shell cubic restores the third map jet", sp.expand(d3 - d3.subs(ell, 0)) == ell*r)


# T(Q)_ijk = H_ka Q_ij^a + cyclic on dim(E)=3.
n = 3
pairs = list(combinations_with_replacement(range(n), 2))
triples = list(combinations_with_replacement(range(n), 3))
qvars = {(i, j, a): sp.symbols(f"q_{i}{j}_{a}") for i, j in pairs for a in range(n)}


def qvar(i, j, a):
    return qvars[(min(i, j), max(i, j), a)]


def jet_matrix(metric):
    expressions = []
    for i, j, k in triples:
        expression = sum(
            metric[k, a]*qvar(i, j, a)
            + metric[j, a]*qvar(i, k, a)
            + metric[i, a]*qvar(j, k, a)
            for a in range(n)
        )
        expressions.append(sp.expand(expression))
    variables = [qvars[key] for key in sorted(qvars)]
    return sp.Matrix([[expr.coeff(var) for var in variables] for expr in expressions])


T = jet_matrix(sp.eye(3))
check("dimension", "quadratic three-field map jet has dimension 18", T.cols == 18)
check("dimension", "symmetric three-field cubic has dimension 10", T.rows == 10)
check("surjectivity", "nondegenerate second-jet contribution has full cubic rank", T.rank() == 10)
check("surjectivity", "full cubic match leaves an eight-dimensional jet kernel", len(T.nullspace()) == 8)

# Explicit right inverse Q_ij^a=S_ija/3.
svars = {ijk: sp.symbols("s_" + "".join(map(str, ijk))) for ijk in triples}


def svar(i, j, k):
    return svars[tuple(sorted((i, j, k)))]


right_inverse = sp.Matrix([svar(i, j, a)/3 for i, j in pairs for a in range(n)])
target = sp.Matrix([svars[ijk] for ijk in triples])
check("surjectivity", "explicit one-third polarization is a right inverse", sp.simplify(T*right_inverse - target) == sp.zeros(10, 1))

Tdeg = jet_matrix(sp.diag(1, 1, 0))
check("boundary", "degenerate Hessian can leave a cubic cokernel", Tdeg.rank() < 10)
check("boundary", "nondegeneracy is a live hypothesis", Tdeg.rank() < T.rank())

# Affine diagonal lift: two matched products in three lift scales.
lam, a, b = sp.symbols("lam a b", nonzero=True)
constraints = sp.Matrix([lam*a**2, lam*b**2])
J = constraints.jacobian((lam, a, b)).subs({lam: 1, a: 1, b: 1})
kernel_direction = sp.Matrix([-2, 1, 1])
check("scaling", "two diagonal projection constraints have rank two", J.rank() == 2)
check("scaling", "the affine diagonal lift retains one scaling direction", len(J.nullspace()) == 1)
check("scaling", "stated rescaling tangent preserves both projections", J*kernel_direction == sp.zeros(2, 1))

# Source/action and repository custody checks.
k118 = (ROOT / "explorations/conditional-build/selected-k118-rsap-tt-full-moving-d3-owner-sufficiency-and-action-layer-gate-2026-08-15.md").read_text()
layers = (ROOT / "explorations/conditional-build/two-layer-action-selected-cubic-owner-retype-2026-08-06.md").read_text()
jets = (ROOT / "explorations/conditional-build/selected-action-second-soldering-observation-jets-2026-08-06.md").read_text()
stationary = (ROOT / "explorations/conditional-build/selected-k77-i2b-local-stationary-bianchi-jet-witness-2026-08-13.md").read_text()
artifact = (ROOT / "explorations/conditional-build/selected-k119-rsap-tt-stationary-twojet-selection-obstruction-2026-08-15.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k119-rsap-tt-stationary-twojet-selection-obstruction.json").read_text())
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()

check("source", "K118 distinguishes all four action layers", all(name in k118 for name in ("I_sc", "I1B", "I2B", "I_II")))
check("source", "two-layer theorem keeps I1B and I2B cubics distinct", "no common scale identifies the cubics" in layers)
check("source", "geometric artifact owns jet locations but not selected coefficients", "do **not** yet expand the actual\nselected action" in jets)
check("source", "stationary I2B witness is a native solution jet", "local connection-jet witness" in stationary)
check("artifact", "routing notice is present", "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
check("artifact", "classification is explicit", "Classification: `SOURCE_NATIVE_ROUTE`." in artifact)
check("artifact", "target claim is internal and exact", "target_claim: K118_NEXT_GATE" in artifact)
check("registry", "registry records full rank and eight-dimensional kernel", registry["nondegenerate_branch"]["second_jet_to_cubic_rank"] == 10 and registry["nondegenerate_branch"]["second_jet_to_cubic_kernel_dimension"] == 8)
check("registry", "no complete selection tuple is claimed", registry["complete_selection_tuple_owned"] is False)
check("repo", "current state advances through K121 to native cubic custody", "complete native i1b pullback cubic" in current.lower())
check("repo", "roadmap preserves K119 beneath current K121", "K121" in roadmap[:4500] and "K119" in roadmap and "cubic matching" in roadmap.lower())
check("repo", "context states the surjective obstruction", "eight-dimensional" in context[:8000].lower())
check("repo", "K118 carries the K119 successor correction", "K119 selection correction" in k118)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
raise SystemExit(1 if failures else 0)
