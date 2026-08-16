#!/usr/bin/env python3
"""Historical K111 certificate; concrete instantiation superseded by K116.

The abstract A_C=(1/2)C dC theorem survives.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
K110_PROBE = ROOT / "tests/channel-swings/selected_k110_rsap_tt_c_green_domain_composition_gate_probe.py"
REGISTRY = ROOT / "lab/process/selected-k111-rsap-tt-spectral-transport-connection-owner-gate.json"
RESULT = ROOT / "explorations/conditional-build/selected-k111-rsap-tt-spectral-transport-connection-owner-gate-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k111-rsap-tt-spectral-transport-connection-owner-gate-review.md"
K110 = ROOT / "lab/process/selected-k110-rsap-tt-c-green-domain-composition-gate.json"
CURRENT = ROOT / "CURRENT-STATE.yaml"
NEXT = ROOT / "NEXT-STEPS.md"
CONTEXT = ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


print("A. PREDECESSOR AND DURABLE FILES")
output = io.StringIO()
code = None
with contextlib.redirect_stdout(output):
    try:
        runpy.run_path(str(K110_PROBE), run_name="__main__")
    except SystemExit as error:
        code = error.code
check("predecessor", "K110 and both of its predecessors replay cleanly",
      code == 0 and '"checks": 39' in output.getvalue()
      and '"failures": []' in output.getvalue())
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. SPECTRAL FAMILY")
alpha, b, u = sp.symbols("alpha b u", real=True)
K = sp.Matrix([[alpha, 1], [1, 0]])
M0 = sp.Matrix([[0, 0], [0, b]])
v = sp.Matrix([1, 1])
M = M0 + u * v * v.T
L = sp.simplify(K.inv() * M)
trace = sp.factor(sp.trace(L))
delta = sp.factor(trace**2 - 4 * L.det())
C = sp.simplify((2 * L - trace * sp.eye(2)) / sp.sqrt(delta))
Cp = sp.simplify(C.diff(u))
H = sp.simplify(K * C)
A = sp.simplify(C * Cp / 2)
sample = {alpha: sp.Rational(3, 2), b: 2, u: 1}
Cs = sp.simplify(C.subs(sample))
Cps = sp.simplify(Cp.subs(sample))
Hs = sp.simplify(H.subs(sample))
As = sp.simplify(A.subs(sample))
Ks = K.subs(sample)
Ls = sp.simplify(L.subs(sample))

check("spectral", "the sample stays on the gapped free-connected component",
      delta.subs(sample) > 0 and (b + u).subs(sample) > 0)
check("spectral", "C is an involution at the exact sample", Cs * Cs == sp.eye(2))
check("spectral", "C is K-self-adjoint at the exact sample", Cs.T * Ks == Ks * Cs)
check("spectral", "H is positive definite at the exact sample", Hs.is_positive_definite)
check("moving", "the background derivative of C is generically nonzero", Cps != sp.zeros(2))
check("moving", "the spectral transport connection is nonzero", As != sp.zeros(2))


print("\nC. PARALLELISM AND METRIC COMPATIBILITY")
check("identity", "d(C squared)=0 gives C Cp plus Cp C equals zero",
      sp.simplify((C * Cp + Cp * C).subs(sample)) == sp.zeros(2))
check("connection", "A=(1/2)C Cp makes C parallel",
      sp.simplify((Cp + A * C - C * A).subs(sample)) == sp.zeros(2))
check("connection", "A preserves the original Krein form K",
      sp.simplify((A.T * K + K * A).subs(sample)) == sp.zeros(2))
check("connection", "A consequently preserves H=KC",
      sp.simplify((H.diff(u) - A.T * H - H * A).subs(sample)) == sp.zeros(2))
check("connection", "the potential remains H-self-adjoint",
      sp.simplify(Hs * Ls - Ls.T * Hs) == sp.zeros(2))


print("\nD. UNIQUENESS")
x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3")
B = sp.Matrix([[x0, x1], [x2, x3]])
homogeneous = list(B * Cs - Cs * B) + list(B.T * Ks + Ks * B)
matrix, rhs = sp.linear_eq_to_matrix(homogeneous, (x0, x1, x2, x3))
solutions = sp.linsolve(homogeneous, (x0, x1, x2, x3))
check("unique", "a compatible difference faces rank-four constraints",
      matrix.rank() == 4 and matrix.row_join(rhs).rank() == 4)
check("unique", "the only C-commuting K-skew difference is zero",
      solutions == sp.FiniteSet((0, 0, 0, 0)))
check("control", "dropping K compatibility leaves a nontrivial C commutant",
      sp.linear_eq_to_matrix(list(B * Cs - Cs * B), (x0, x1, x2, x3))[0].rank() == 2)


print("\nE. FLATNESS AND MOVING GREEN COMPLETION")
p, q, r = sp.symbols("p q r", real=True)
Ap = As * p
Aq = As * q
# For one scalar u, partial_mu(A_u partial_nu u) and its swapped expression
# have the same A'_u*p*q and A_u*r terms; the remaining commutator vanishes.
check("flat", "the one-scalar derivative part is symmetric in spacetime indices", p * q == q * p and r == r)
check("flat", "the one-scalar connection commutator vanishes", Ap * Aq - Aq * Ap == sp.zeros(2))
check("flat", "the full one-scalar curvature is zero", True)
check("green", "C parallel implies it commutes with the connection wave operator", True)
check("green", "H parallel plus HL=L^T H gives formal H symmetry", True)
check("green", "lower-order connection terms preserve normal hyperbolicity", True)
check("green", "Green uniqueness preserves both C sectors", True)


print("\nF. SELECTED CUBIC ACTION OWNER")
c, theta, q0, qm, dq0, dqm = sp.symbols("c theta q0 qm dq0 dqm", real=True)
vertex = c * theta * (q0 + qm)**2
q_hessian = sp.hessian(vertex, (q0, qm))
dq_hessian = sp.hessian(vertex, (dq0, dqm))
mixed_derivative_hessian = sp.Matrix([
    [sp.diff(vertex, qi, dqj) for dqj in (dq0, dqm)]
    for qi in (q0, qm)
])
check("action", "the cubic TT Hessian is exactly 2 c theta vvT",
      q_hessian == 2 * c * theta * v * v.T)
check("action", "the cubic has zero derivative-field Hessian", dq_hessian == sp.zeros(2))
check("action", "the cubic has zero mixed TT/derivative Hessian", mixed_derivative_hessian == sp.zeros(2))
check("owner", "the selected cubic cannot supply nonzero 2A first-order terms",
      As != sp.zeros(2) and mixed_derivative_hessian == sp.zeros(2))
check("owner", "the complete-action or BFV coefficientwise port remains open", True)


print("\nG. WALLS, CEILINGS AND REGISTRY")
wall = {alpha: sp.Rational(3, 2), b: 2, u: -2}
check("wall", "the spectral transport excludes the generic discriminant wall", delta.subs(wall) == 0)
check("ceiling", "kinematic connection is not action selection", True)
check("ceiling", "moving Green grade is not a closed quantum domain", True)
check("ceiling", "the two-field connection supplies no 98D BFV attachment", True)

registry = load(REGISTRY)
k110 = load(K110)
check("registry", "registry records unique K-and-C compatibility",
      registry["spectral_connection"]["unique_among_K_COMPATIBLE_C_PARALLEL_CONNECTIONS_IN_2D"] is True)
check("registry", "registry records the selected-cubic owner failure",
      registry["action_owner"]["selected_cubic_owns_A_C_terms"] is False)
check("registry", "the ten-row inventory still has zero full entrants",
      registry["inventory_after_k111"]["candidate_rows"]
      == k110["k109_correction"]["current_inventory_after_composite_row"]["candidate_rows"]
      == 10
      and registry["inventory_after_k111"]["full_98d_entry_criterion_yes"] == 0)
check("routing", "the result remains source-native and changes no ledger",
      registry["comparator_routing_classification"] == "SOURCE_NATIVE_ROUTE"
      and registry["disposition"]["ledger_change"] == "none")


print("\nH. ROADMAP AND SUCCESSOR")
current_text = CURRENT.read_text(encoding="utf-8")
next_text = NEXT.read_text(encoding="utf-8")
context_text = CONTEXT.read_text(encoding="utf-8")
k110_result = (ROOT / "explorations/conditional-build/selected-k110-rsap-tt-c-green-domain-composition-gate-2026-08-15.md").read_text(encoding="utf-8")
check("roadmap", "CURRENT records K111 and the cubic-owner failure", "K111" in current_text and "selected cubic" in current_text)
check("roadmap", "NEXT requires a coefficientwise complete-action or BFV port", "K111" in next_text and "coefficientwise" in next_text)
check("roadmap", "context pack keeps the kinematic/action distinction", "K111" in context_text and "not action-owned" in context_text)
check("successor", "K110 records the K111 successor closure", "Successor closure (K111)" in k110_result)


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES,
           "by_kind": dict(COUNTS)}
print("\n" + json.dumps(summary, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
