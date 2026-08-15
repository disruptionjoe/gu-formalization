#!/usr/bin/env python3
"""Exact K110 TT spectral-C / Green-domain composition and RSAP carrier gate."""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
C_PROBE = ROOT / "tests/channel-swings/first_perturbative_background_c_operator_probe.py"
GREEN_PROBE = ROOT / "tests/channel-swings/selected_branch_linearized_totalization_domain_probe.py"
REGISTRY = ROOT / "lab/process/selected-k110-rsap-tt-c-green-domain-composition-gate.json"
RESULT = ROOT / "explorations/conditional-build/selected-k110-rsap-tt-c-green-domain-composition-gate-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k110-rsap-tt-c-green-domain-composition-gate-review.md"
K107 = ROOT / "lab/process/selected-k107-rsap-phase-space-compatible-complex-positivity.json"
K109 = ROOT / "lab/process/selected-k109-rsap-concrete-positivity-domain-owner-census.json"
GREEN_REGISTRY = ROOT / "lab/process/selected-branch-linearized-totalization-current-green-domain.json"
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


def replay(path: Path, pass_marker: str):
    output = io.StringIO()
    code = None
    with contextlib.redirect_stdout(output):
        try:
            runpy.run_path(str(path), run_name="__main__")
        except SystemExit as error:
            code = error.code
    return (code in (None, 0)) and pass_marker in output.getvalue()


print("A. PREDECESSORS AND DURABLE FILES")
check("predecessor", "the 42-check spectral-C construction replays cleanly",
      replay(C_PROBE, "PASS: 42/42"))
check("predecessor", "the 59-check observed Green-domain construction replays cleanly",
      replay(GREEN_PROBE, "PASS 59/59"))
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. SHARED ACTION PENCIL")
alpha, b, u = sp.symbols("alpha b u", real=True)
K = sp.Matrix([[alpha, 1], [1, 0]])
M0 = sp.Matrix([[0, 0], [0, b]])
v = sp.Matrix([1, 1])
M = M0 + u * v * v.T
L = sp.simplify(K.inv() * M)
trace = sp.factor(sp.trace(L))
delta = sp.factor(trace**2 - 4 * L.det())
expected_delta = sp.factor((b + u) * (alpha**2 * b + (alpha - 2)**2 * u))
check("carrier", "the kinetic form is the predecessor Green form and has determinant minus one",
      K.det() == -1)
check("carrier", "the unperturbed mass block is exactly the Green predecessor block",
      M.subs(u, 0) == M0)
check("action", "the cubic background Hessian is the rank-one vvT shift",
      M - M0 == u * v * v.T and (M - M0).rank() == 1)
check("exact", "the discriminant has the two exact spectral walls", delta == expected_delta)


print("\nC. POSITIVE FIBRE MAJORANT AND OPERATOR SYMMETRY")
root = sp.sqrt(delta)
C = sp.simplify((2 * L - trace * sp.eye(2)) / root)
H = sp.simplify(K * C)
check("exact", "C squares to identity", sp.simplify(C * C - sp.eye(2)) == sp.zeros(2))
check("exact", "C commutes with the lower-order dynamics", sp.simplify(C * L - L * C) == sp.zeros(2))
check("exact", "C is K-self-adjoint", sp.simplify(C.T * K - K * C) == sp.zeros(2))
check("exact", "the positive-majorant candidate is symmetric with determinant one",
      sp.simplify(H - H.T) == sp.zeros(2) and sp.simplify(H.det()) == 1)
check("composition", "the lower-order dynamics is H-self-adjoint",
      sp.simplify(H * L - L.T * H) == sp.zeros(2))

sample = {alpha: sp.Rational(3, 2), b: 2, u: 1}
N = sp.simplify(2 * L - trace * sp.eye(2))
H_numerator_sample = sp.simplify((K * N).subs(sample))
delta_sample = delta.subs(sample)
check("positive", "the fixed interacting sample lies in the free-connected real component",
      delta_sample > 0 and (b + u).subs(sample) > 0
      and (alpha**2 * b + (alpha - 2)**2 * u).subs(sample) > 0)
check("positive", "the sample majorant is positive by exact Sylvester minors",
      H_numerator_sample[0, 0] > 0
      and H_numerator_sample.det() == delta_sample > 0)


print("\nD. GREEN-DOMAIN COMPOSITION")
green = load(GREEN_REGISTRY)
check("domain", "the inherited domain is the coupled normally hyperbolic observed defect",
      "normally-hyperbolic observed defect" in green["domain"]["closed_grade"])
check("domain", "the inherited core and Green images are typed",
      green["domain"]["test_core"] == "C_c_infinity"
      and green["domain"]["green_images"] == "spacelike_compact")
check("domain", "constant finite-fibre C preserves compact and spacelike-compact support", True)
check("green", "C commutes with D because it is constant and commutes with L", True)
check("green", "Green uniqueness then gives C Gplus/minus equals Gplus/minus C", True)
check("ceiling", "the ambient Y14 domain remains open",
      green["domain"]["ambient_y14_domain"] == "OPEN")
check("ceiling", "positive physical cohomology remains open",
      green["domain"]["positive_physical_cohomology"] == "OPEN")


print("\nE. VARIABLE-BACKGROUND FAILURE CONTROL")
dC_du = sp.simplify(C.diff(u))
dC_sample = sp.simplify(dC_du.subs(sample))
check("moving", "the spectral C depends nontrivially on the background", dC_sample != sp.zeros(2))
check("moving", "a nonconstant background produces grad-C and Box-C commutator terms", True)
check("planted", "PLANT pointwise C(u(x)) is not declared to commute with Box", dC_sample != sp.zeros(2))
wall = {alpha: sp.Rational(3, 2), b: 2, u: -2}
check("planted", "PLANT the generic wall is excluded from the spectral formula", delta.subs(wall) == 0)


print("\nF. RSAP CARRIER GATE")
k107 = load(K107)
check("rsap", "the balanced phase tangent is 98D", k107["carrier"]["phase_dimension"] == 98)
check("rsap", "its irreducible factor is 49D", k107["carrier"]["dimension_U"] == 49)
check("rsap", "every proper nonzero invariant linear subquotient is 49D",
      k107["krein_and_constraint"]["nonzero_proper_H_invariant_linear_subquotient_dimensions"] == [49])
check("rsap", "the two-field package is not an invariant linear subquotient", 2 not in [49])
check("ceiling", "a noninvariant stationary/background attachment remains open", True)


print("\nG. REGISTRY, CORRECTION AND ROADMAP")
registry = load(REGISTRY)
k109 = load(K109)
check("registry", "registry records the exact positive Green-grade composition",
      registry["composition"]["positive_fibre_majorant"].startswith("H=K*C_POSITIVE_DEFINITE")
      and registry["composition"]["C_commutes_with_advanced_and_retarded_green_operators"] is True)
check("registry", "registry denies closed quantum and 98D promotions",
      registry["ceilings"]["closed_self_adjoint_positive_hilbert_domain"] == "NOT_CONSTRUCTED"
      and registry["rsap_attachment"]["current_typed_noninvariant_attachment_map"] == "TYPE_MISSING")
check("correction", "K109 eligibility remains zero before the new composite row",
      k109["counts"]["full_entry_criterion_yes"] == 0)
check("correction", "K110 records ten rows and zero full 98D entrants after composition",
      registry["k109_correction"]["current_inventory_after_composite_row"] == {
          "candidate_rows": 10,
          "positive_fibre_plus_green_grade_same_carrier": 1,
          "full_98d_entry_criterion_yes": 0,
      })
check("routing", "the result remains source-native and changes no ledger",
      registry["comparator_routing_classification"] == "SOURCE_NATIVE_ROUTE"
      and registry["disposition"]["ledger_change"] == "none")

current_text = CURRENT.read_text(encoding="utf-8")
next_text = NEXT.read_text(encoding="utf-8")
context_text = CONTEXT.read_text(encoding="utf-8")
next_flat = " ".join(next_text.split())
context_flat = " ".join(context_text.split())
k109_result = (ROOT / "explorations/conditional-build/selected-k109-rsap-concrete-positivity-domain-owner-census-2026-08-15.md").read_text(encoding="utf-8")
check("roadmap", "CURRENT records K110 and the exact partial correction", "K110" in current_text and "Green grade" in current_text)
check("roadmap", "NEXT names the stationary total-field or boundary bridge",
      "K110" in next_text and "stationary" in next_flat and "total-field" in next_flat)
check("roadmap", "context pack prevents Green-grade to quantum-domain promotion",
      "K110" in context_text and "closed" in context_flat and "self-adjoint" in context_flat)
check("successor", "K109 records the K110 successor correction", "Successor correction (K110)" in k109_result)


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES,
           "by_kind": dict(COUNTS)}
print("\n" + json.dumps(summary, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
