#!/usr/bin/env python3
"""Hostile jet-order, uniqueness and scope mutations for K1748."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1748-four-point-third-order-branch.json").read_text())


def accepts(data):
    pre = data.get("pre_flight", {})
    convention = data.get("coefficient_convention", {})
    solution = data.get("third_order_chart_solution", {})
    remaining = data.get("remaining_freedom", {})
    decision = data.get("decision", {})
    post = data.get("post_flight", {})
    return all([
        data.get("claim_id") == "K1748",
        data.get("classification") == "INTERNAL_STRUCTURAL_ONLY",
        "K1748 is not assumed" in pre.get("rederived_inputs", ""),
        "do not include factorials" in convention.get("chart_path", ""),
        "Jv_3=" in solution.get("exact_equations", ""),
        "det J is nonzero" in solution.get("uniqueness", ""),
        "2.530573688729724736" in solution.get("reported_solution", ""),
        "4.748609191761382895" in solution.get("reported_solution", ""),
        "x_4 remains absent" in remaining.get("dimension", ""),
        decision.get("third_order_chart_coefficients_unique") is True,
        decision.get("fourth_order_chart_coefficients_unique") is False,
        decision.get("complete_local_analytic_branch_unique") is False,
        decision.get("finite_strength_global_optimizer_identified") is False,
        "factor of six" in post.get("mistyping_check", ""),
        "different x_4 values" in post.get("counterexample_seam", ""),
        "u=q singular face" in data.get("scope_guard", ""),
    ])


mutations = []
for path, value in [
    (("claim_id",), "K1743"),
    (("classification",), "SOURCE_NATIVE_ROUTE"),
    (("pre_flight", "rederived_inputs"), "Assume K1748."),
    (("coefficient_convention", "chart_path"), "P_3 and A_3 are third derivatives."),
    (("third_order_chart_solution", "exact_equations"), "No chain rule."),
    (("third_order_chart_solution", "uniqueness"), "Assume uniqueness."),
    (("third_order_chart_solution", "reported_solution"), "P_3=A_3=0."),
    (("remaining_freedom", "dimension"), "Complete branch fixed."),
    (("decision", "third_order_chart_coefficients_unique"), False),
    (("decision", "fourth_order_chart_coefficients_unique"), True),
    (("decision", "complete_local_analytic_branch_unique"), True),
    (("decision", "finite_strength_global_optimizer_identified"), True),
    (("post_flight", "mistyping_check"), "No convention needed."),
    (("post_flight", "counterexample_seam"), "No contrary path."),
    (("scope_guard",), "Global all-seed optimizer theorem."),
]:
    mutant = copy.deepcopy(DATA)
    cursor = mutant
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value
    mutations.append(mutant)

assert accepts(DATA)
for i, mutant in enumerate(mutations, 1):
    assert not accepts(mutant), i
    print(f"PASS {i:02d}: rejected hostile mutation")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
