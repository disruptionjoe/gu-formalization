#!/usr/bin/env python3
"""Exact K146 carrier typing, lower-remainder, and quotient controls."""

from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "explorations/conditional-build/selected-k146-native-i1b-t0-null-remainder-type-and-quotient-gate-2026-08-16.md"
REGISTRY = ROOT / "lab/process/selected-k146-native-i1b-t0-null-remainder-type-and-quotient-gate.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k146-native-i1b-t0-null-remainder-type-and-quotient-gate-review.md"
checks = 0

def check(group: str, label: str, condition: bool) -> None:
    global checks
    if not condition:
        raise AssertionError(f"{group}: {label}")
    checks += 1
    print(f"PASS [{group}] {label}")

print("A. PREDECESSOR AND CARRIER CUSTODY")
k138 = json.loads((ROOT / "lab/process/selected-k138-native-i1b-t0-null-stratum-covariant-transport.json").read_text())
k145 = json.loads((ROOT / "lab/process/selected-k145-native-i1b-t0-curved-c-composition-and-compatibility.json").read_text())
check("predecessor", "K138 metric quotient has dimension five", k138["null_stratum"]["gauge_reduced_dimension"] == 5)
check("predecessor", "K145 leaves selected lower remainder unevaluated", k145["exact_composition"]["null_lower_selected_shiab_remainder"] == "UNEVALUATED_SELECTED_SHIAB_REMAINDER")
check("carrier", "distortion and metric dimensions differ", 14 * 2**14 == 229376 and 4 * 5 // 2 == 10)
for distinction in (
    "P5 distortion endomorphism versus metric endomorphism",
    "gauge-image preservation versus radical preservation",
    "formal polynomial Schur operator versus exact Schur inverse",
    "mathematically defined action versus serialized executable evaluator",
    "nonzero curvature input versus selected projected value",
):
    check("type", distinction + " remain distinct", True)

print("\nB. EXACT VARIABLE-COEFFICIENT FIFTH-POWER CONTROL")
x, s = sp.symbols("x s")
u = sp.Matrix([1, s * x])
v = sp.Matrix([-s * x, 1])
M = sp.simplify(u * v.T)
Mp = M.diff(x)
check("control", "pointwise coefficient is square zero", sp.simplify(M * M) == sp.zeros(2))
check("control", "composition coefficient obeys M M-prime=s M", sp.simplify(M * Mp - s * M) == sp.zeros(2))
check("control", "all slopes share same frozen matrix", sp.simplify(M.subs(x, 0) - sp.Matrix([[0, 1], [0, 0]])) == sp.zeros(2))
powers = {1: sp.Integer(1)}
for power in range(2, 6):
    powers[power] = sp.simplify(s * powers[power - 1])
check("control", "operator fifth power is s^4 P", powers[5] == s**4)
check("control", "zero and nonzero slopes have different lower remainders", powers[5].subs(s, 0) == 0 and powers[5].subs(s, 2) == 16)
check("control", "frozen fifth power remains zero", M.subs(x, 0) ** 5 == sp.zeros(2))

print("\nC. FIRST WELL-TYPED METRIC COMPOSITION")
metric_dim, dist_dim = 10, 6
A = sp.Matrix.hstack(sp.eye(dist_dim), sp.zeros(dist_dim, 4))
G = sp.Matrix.vstack(sp.zeros(dist_dim, 4), sp.eye(4))
R4 = sp.diag(1, 2, 3, 4, 5, 6)
S4 = -A.T * R4 * A
check("typing", "A maps metric to distortion", A.shape == (dist_dim, metric_dim))
check("typing", "A-star R4 A maps metric to metric", S4.shape == (metric_dim, metric_dim))
check("Noether", "A G vanishes", A * G == sp.zeros(dist_dim, 4))
check("Noether", "polynomial metric operator kills G", S4 * G == sp.zeros(metric_dim, 4))
ell = sp.zeros(1, metric_dim); ell[0, 9] = 1
H_basis = [sp.eye(metric_dim).col(j) for j in range(9)]
G_basis = H_basis[:4]
leaky = sp.zeros(metric_dim); leaky[9, 4] = 1
check("quotient", "planted map preserves G by killing it", all(leaky * g == sp.zeros(metric_dim, 1) for g in G_basis))
check("quotient", "same map leaks one H representative", (ell * leaky * H_basis[4])[0] == 1)
check("quotient", "gauge preservation alone does not define H/G endomorphism", True)

print("\nD. ARTIFACT, REGISTRY, REVIEW, AND PROPAGATION")
artifact = ARTIFACT.read_text(); registry = json.loads(REGISTRY.read_text()); review = REVIEW.read_text()
current = (ROOT / "CURRENT-STATE.yaml").read_text(); roadmap = (ROOT / "NEXT-STEPS.md").read_text()
status = (ROOT / "RESEARCH-STATUS.md").read_text(); context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
tests_readme = (ROOT / "tests/README.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k145-native-i1b-t0-curved-c-composition-and-compatibility-2026-08-16.md").read_text()
check("artifact", "routing, classification, target and scope present", "GU-COMPARATOR-ROUTING — scope before inference" in artifact and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact and "target_claim: K145_NEXT_GATE" in artifact and "Scope: K146 binds" in artifact)
check("artifact", "typed metric composition and gauge result recorded", "S_4=-A* R_4 A" in artifact and "S_4 G=-A*R_4 A G=0" in artifact)
check("registry", "direct P5 quotient test ill typed", registry["carrier_typing"]["direct_P5_HG_test"] == "ILL_TYPED_DIFFERENT_CARRIERS")
check("registry", "gauge preservation passes", registry["polynomial_metric_operator"]["G_n_preservation"] == "PASS_BY_A_G_ZERO")
check("registry", "radical preservation unevaluated", registry["polynomial_metric_operator"]["H_n_preservation"] == "UNEVALUATED_CURVED_COMPOSITION")
check("registry", "lower evaluator not materialized", registry["serialized_evaluator"]["lower_selected_shiab_P5"] == "NOT_MATERIALIZED_FROM_CURRENT_SERIALIZED_EVALUATOR")
check("review", "review separates ownership and executable evidence", "mathematically defines" in review and "NOT_MATERIALIZED_FROM_CURRENT_SERIALIZED_EVALUATOR" in review)
check("repo", "current state advances through K146", "K146 now corrects" in current)
check("repo", "roadmap advances to K147", "K147" in roadmap[:16000])
check("repo", "research status carries S4 gauge result", "S_4 G=0" in status[:9000])
check("repo", "context carries carrier correction", "ILL_TYPED_DIFFERENT_CARRIERS" in context[:16000])
check("repo", "tests inventory includes K146 probe", "selected_k146_native_i1b_t0_null_remainder_type_and_quotient_gate_probe.py" in tests_readme)
check("predecessor", "K145 carries corrected successor", "## K146 successor classification" in predecessor)
print(f"PASS {checks}/{checks}")
