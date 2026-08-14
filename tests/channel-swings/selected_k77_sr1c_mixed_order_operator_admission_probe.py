#!/usr/bin/env python3
"""Exact mixed-order admission gate for the SR-1C owner operator."""

from collections import Counter
from fractions import Fraction as Q
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def strict(relative):
    return json.loads(read(relative))


registry = strict("lab/process/selected-k77-sr1c-mixed-order-operator-admission.json")
branch = strict("lab/process/selected-k77-zorro-nonzero-t-first-action-jet-gate.json")
type_gate = strict("lab/process/selected-k77-sr1c-owner-operator-type-gate.json")
bulk = read("explorations/conditional-build/selected-k77-bulk-operator-admission-2026-08-09.md")
result = read("explorations/conditional-build/selected-k77-sr1c-mixed-order-operator-admission-2026-08-14.md")

print("A. OWNED MIXED-ORDER GRAMMAR")
check("prior", "the exact two-root branch is unchanged",
      branch["amplitudes"]["polynomial"] == "28392*t^2+91*t-351")
check("prior", "O_SR1C remains the named missing common-basis operator",
      type_gate["missing_operator"]["id"] == "O_SR1C")
check("source", "the owned density weights are g2 varpi1 epsilon1",
      "g : 2       varpi : 1       epsilon : 1" in bulk)
check("source", "the owned safe Euler table includes fourth-order g-g",
      "E_g              4          3              3" in bulk)
check("registry", "the registry preserves the primitive coordinates",
      registry["source_coordinates"] == ["g", "varpi", "epsilon"])
check("registry", "the immediate epsilon ceiling is (3,2,2)",
      registry["operator_contract"]["primitive_epsilon_input_ceiling"]
      == {"g": 3, "varpi": 2, "epsilon": 2})
check("registry", "the complete metric ceiling is (4,3,3)",
      registry["operator_contract"]["complete_fixed_varpi_metric_input_ceiling"]
      == {"g": 4, "varpi": 3, "epsilon": 3})

print("\nB. EXACT SOURCE-SHAPED TOP-ORDER CONTROL")
# In one dimension take B=g', T=varpi-B and the first-order cell
# L=1/2(DT)^2. Then p=DT=varpi'-g'', the varpi/epsilon-shaped adjoint row is
# -Dp=-varpi''+g''', and the metric row is -D^2p=-varpi'''+g''''.
g = [Q(2), Q(-3), Q(5), Q(7), Q(11)]
varpi = [Q(-1), Q(13), Q(17), Q(19)]
p0 = varpi[1] - g[2]
primitive = -varpi[2] + g[3]
metric = -varpi[3] + g[4]
check("exact", "the planted action momentum is live", p0 != 0)
check("exact", "the formal-adjoint primitive row is -varpi2+g3", primitive == Q(-10))
check("exact", "the twice-adjoint metric row is -varpi3+g4", metric == Q(-8))

g_same_two_jet = [g[0], g[1], g[2], Q(29), g[4]]
primitive_b = -varpi[2] + g_same_two_jet[3]
check("planted", "same primitive g two-jet can change the epsilon row",
      g_same_two_jet[:3] == g[:3] and primitive_b != primitive)
g_same_three_jet = [g[0], g[1], g[2], g[3], Q(31)]
metric_b = -varpi[3] + g_same_three_jet[4]
check("planted", "same primitive g three-jet can change the metric row",
      g_same_three_jet[:4] == g[:4] and metric_b != metric)
check("planted", "wrong first-adjoint sign fires", varpi[2] - g[3] != primitive)
check("planted", "wrong second-adjoint sign fires", varpi[3] - g[4] != metric)

print("\nC. HELD-OUT EXACT BRANCH CONTROL")
# For q(t)=1+t in A=QQ[t]/P, the product over the two real embeddings is
# 1 + sum(roots) + product(roots) = 13975/14196, hence neither branch is zero.
root_sum = Q(-91, 28392)
root_product = Q(-351, 28392)
norm_one_plus_t = Q(1) + root_sum + root_product
check("branch", "the quadratic discriminant still gives two real embeddings",
      branch["amplitudes"]["discriminant"] == 39870649
      and branch["amplitudes"]["real_nonzero_roots"] == 2)
check("branch", "the held-out quotient element 1+t has the serialized norm",
      norm_one_plus_t == Q(13975, 14196))
check("branch", "the held-out element is nonzero on both branches", norm_one_plus_t != 0)
check("scope", "the order control is not the selected coefficient bank",
      "NOT_THE_SELECTED_ACTION_COEFFICIENT_BANK" in registry["exact_control"]["interpretation"])

print("\nD. ADMISSION AND CLAIM CEILING")
check("result", "uniform field two-jet admission is rejected",
      registry["operator_contract"]["uniform_field_two_jet_admissible"] is False)
check("result", "exact cancellation is allowed to lower the safe ceiling",
      registry["operator_contract"]["ceiling_may_lower_after_exact_cancellation"] is True)
check("result", "the actual top coefficients remain uncomputed",
      registry["operator_contract"]["top_coefficients_computed"] is False)
check("result", "O_SR1C remains coefficient-type-missing after interface repair",
      registry["disposition"].endswith("O_SR1C_COEFFICIENT_BANK_TYPE_MISSING"))
check("scope", "both conjugate branches remain not yet falsified",
      registry["branch_status"].startswith("BOTH_NOT_YET_FALSIFIED"))
check("scope", "SR-1 and SR-2 remain gated",
      registry["sr1"] == "BACKGROUND-MISSING" and registry["sr2"] == "BLOCKED")
check("next", "the next gate computes coefficients before solving",
      registry["next_gate"].startswith("COMPUTE_BRANCH_SPECIFIC_TOP_COEFFICIENTS"))
check("accounting", "no ledger canon residue quotient datum or posture move occurs",
      set(registry["changes"].values()) == {"none"})
check("propagation", "the native result states both mixed-order interfaces",
      "(3,2,2)" in result and "(4,3,3)" in result)

summary = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "disposition": registry["disposition"],
    "next_gate": registry["next_gate"],
}
print(json.dumps(summary, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
