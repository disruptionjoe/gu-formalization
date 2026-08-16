#!/usr/bin/env python3
"""Historical mixed-frame K114 certificate; result superseded in full by K116."""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
K113_PROBE = ROOT / "tests/channel-swings/selected_k113_rsap_tt_spectral_transport_normal_form_and_boundary_support_gate_probe.py"
REGISTRY = ROOT / "lab/process/selected-k114-rsap-tt-alpha-normalization-invariant-owner-gate.json"
RESULT = ROOT / "explorations/conditional-build/selected-k114-rsap-tt-alpha-normalization-invariant-owner-gate-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k114-rsap-tt-alpha-normalization-invariant-owner-gate-review.md"
K113 = ROOT / "lab/process/selected-k113-rsap-tt-spectral-transport-normal-form-and-boundary-support-gate.json"
COEFFICIENT_CENSUS = ROOT / "explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md"
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
        runpy.run_path(str(K113_PROBE), run_name="__main__")
    except SystemExit as error:
        code = error.code
check("predecessor", "K113 and its full predecessor chain replay cleanly",
      code == 0 and '"checks": 36' in output.getvalue()
      and '"failures": []' in output.getvalue())
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. FREE/INTERACTION COMMUTATOR INVARIANT")
alpha, b, u = sp.symbols("alpha b u", nonzero=True)
K = sp.Matrix([[alpha, 1], [1, 0]])
M0 = sp.Matrix([[0, 0], [0, b]])
v = sp.Matrix([1, 1])
M1 = v * v.T
L0 = sp.simplify(K.inv() * M0)
L1 = sp.simplify(K.inv() * M1)
G = sp.Matrix([[-1, 0], [alpha, 1]])
comm = sp.simplify(L0 * L1 - L1 * L0)

check("invariant", "L0 has the exact free form",
      L0 == sp.Matrix([[0, b], [0, -alpha * b]]))
check("invariant", "L1 has the exact interaction form",
      L1 == sp.Matrix([[1, 1], [1 - alpha, 1 - alpha]]))
check("invariant", "the commutator is b(alpha-1)G",
      sp.simplify(comm - b * (alpha - 1) * G) == sp.zeros(2))
check("invariant", "G is invertible because it squares to identity", G * G == sp.eye(2))
check("invariant", "alpha=1 is commuting", comm.subs(alpha, 1) == sp.zeros(2))
check("invariant", "a generic alpha control is noncommuting", comm.subs({alpha: 3, b: 2}) != sp.zeros(2))
check("invariant", "the generic commutator has rank two", comm.subs({alpha: 3, b: 2}).rank() == 2)


print("\nC. ARBITRARY FIELD-CHANGE COVARIANCE")
p, q, r, s = sp.symbols("p q r s")
S = sp.Matrix([[p, q], [r, s]])
Sinv = S.inv()
Kp = S.T * K * S
M0p = S.T * M0 * S
M1p = S.T * M1 * S
L0p = sp.simplify(Kp.inv() * M0p)
L1p = sp.simplify(Kp.inv() * M1p)
commp = sp.simplify(L0p * L1p - L1p * L0p)
check("covariance", "free dynamics transforms by similarity",
      sp.simplify(L0p - Sinv * L0 * S) == sp.zeros(2))
check("covariance", "interaction dynamics transforms by similarity",
      sp.simplify(L1p - Sinv * L1 * S) == sp.zeros(2))
check("covariance", "the commutator transforms by similarity",
      sp.simplify(commp - Sinv * comm * S) == sp.zeros(2))
S_control = sp.Matrix([[2, 1], [1, 1]])
comm_control = sp.simplify((S_control.inv() * comm * S_control).subs({alpha: 3, b: 2}))
check("covariance", "a nontrivial invertible control cannot erase noncommutation",
      comm_control != sp.zeros(2) and comm_control.rank() == 2)


print("\nD. STRUCTURE-PRESERVING CLASSIFICATION")
a, c, e = sp.symbols("a c e", nonzero=True)
S_tri = sp.Matrix([[a, c], [0, e]])
K_tri = sp.expand(S_tri.T * K * S_tri)
check("classification", "preserving the free mass kernel makes S upper triangular",
      sp.simplify(S_tri.T * M0 * S_tri - sp.Matrix([[0, 0], [0, b * e**2]])) == sp.zeros(2))
check("classification", "preserving the interaction ray imposes c=a-e",
      sp.simplify((S_tri.T * v).subs(c, a - e) - a * v) == sp.zeros(2, 1))
bottom_right = sp.factor(K_tri[1, 1].subs(c, a - e))
check("classification", "the lower-right kinetic condition has exactly the two displayed factors",
      sp.simplify(bottom_right - (a - e) * (alpha * (a - e) + 2 * e)) == 0)

S_A = sp.Matrix([[a, 0], [0, a]])
K_A = sp.simplify(S_A.T * K * S_A)
check("branch_A", "branch A preserves alpha after common action scaling",
      sp.simplify(K_A / a**2 - K) == sp.zeros(2))

e_B = alpha * a / (alpha - 2)
c_B = 2 * a / (2 - alpha)
S_B = sp.Matrix([[a, c_B], [0, e_B]])
lam_B = sp.factor(alpha * a**2 / (2 - alpha))
alpha_B = 2 - alpha
K_B = sp.simplify(S_B.T * K * S_B)
M0_B = sp.simplify(S_B.T * M0 * S_B / lam_B)
M1_B = sp.simplify(S_B.T * M1 * S_B / lam_B)
check("branch_B", "branch B is invertible away from alpha=0,2",
      sp.factor(S_B.det()) == alpha * a**2 / (alpha - 2))
check("branch_B", "branch B sends the kinetic form to K(2-alpha)",
      sp.simplify(K_B / lam_B - sp.Matrix([[alpha_B, 1], [1, 0]])) == sp.zeros(2))
check("branch_B", "branch B sends b to alpha*b/(2-alpha)",
      sp.simplify(M0_B - sp.Matrix([[0, 0], [0, alpha * b / (2 - alpha)]])) == sp.zeros(2))
check("branch_B", "branch B sends interaction u to (2-alpha)u/alpha",
      sp.simplify(u * M1_B - u * (2 - alpha) / alpha * M1) == sp.zeros(2))
check("branch_B", "the free mass pole alpha*b is invariant",
      sp.simplify(alpha_B * alpha * b / (2 - alpha) - alpha * b) == 0)
check("classification", "both alpha branches reach one only from one",
      sp.solve(sp.Eq(alpha, 1), alpha) == [1]
      and sp.solve(sp.Eq(2 - alpha, 1), alpha) == [1])
check("classification", "the nontrivial alpha=3/2 control maps to alpha=1/2, not one",
      alpha_B.subs(alpha, sp.Rational(3, 2)) == sp.Rational(1, 2))


print("\nE. OWNERSHIP, ROUTING AND CEILINGS")
registry = load(REGISTRY)
k113 = load(K113)
census_text = COEFFICIENT_CENSUS.read_text(encoding="utf-8")
check("ownership", "alpha_II remains the charged U7 coefficient",
      registry["ownership"]["alpha_II_registry_slot"] == "U7"
      and "**U7**" in census_text and "`alpha_II`" in census_text)
check("ownership", "the source/action does not select alpha_II=1",
      registry["ownership"]["source_or_action_selects_alpha_II_one"] is False
      and k113["zero_transport_locus"]["current_action_selects_alpha_II_one"] is False)
check("ownership", "the normalization horn is excluded without selecting the coefficient",
      registry["ownership"]["normalization_horn"] == "EXCLUDED")
check("routing", "the artifact is source-native and changes no ledger",
      registry["comparator_routing_classification"] == "SOURCE_NATIVE_ROUTE"
      and registry["disposition"]["ledger_change"] == "none")
check("ceiling", "stationary background remains unconstructed",
      registry["ceilings"]["stationary_moving_background"] == "NOT_CONSTRUCTED")
check("ceiling", "the 98D attachment remains open and non-invariant/nonlinear",
      registry["ceilings"]["typed_98d_attachment"].startswith("OPEN_NONINVARIANT_NONLINEAR"))
check("ceiling", "no physical BFV cohomology is claimed",
      registry["ceilings"]["physical_BFV_cohomology"] == "OPEN")


print("\nF. ROADMAP AND SUCCESSOR CLOSURE")
current_text = CURRENT.read_text(encoding="utf-8")
next_text = NEXT.read_text(encoding="utf-8-sig")
context_text = CONTEXT.read_text(encoding="utf-8")
k113_result = (ROOT / "explorations/conditional-build/selected-k113-rsap-tt-spectral-transport-normal-form-and-boundary-support-gate-2026-08-15.md").read_text(encoding="utf-8")
check("roadmap", "CURRENT records K114 as superseded in full",
      "K114" in current_text and "superseded in full" in current_text.lower())
check("roadmap", "NEXT retracts the normalization result",
      "K114" in next_text and "normalization result" in next_text and "superseded" in next_text.lower())
check("roadmap", "context blocks reuse of the alpha orbit conclusion",
      "K114" in context_text and "superseded in full" in context_text.lower())
check("successor", "K113 records the K114 successor closure", "Successor closure (K114)" in k113_result)


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES,
           "by_kind": dict(COUNTS)}
print("\n" + json.dumps(summary, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
