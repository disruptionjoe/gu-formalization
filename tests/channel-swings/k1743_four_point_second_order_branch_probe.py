#!/usr/bin/env python3
"""Hostile jet-order, uniqueness, and scope mutations for K1743."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
d = json.loads((ROOT/"lab/process/k1743-four-point-second-order-branch.json").read_text())


def accepts(x):
    pre = x.get("pre_flight", {})
    conv = x.get("coefficient_convention", {})
    q6 = x.get("q6_selection", {})
    sol = x.get("second_order_chart_solution", {})
    rem = x.get("remaining_freedom", {})
    dec = x.get("decision", {})
    post = x.get("post_flight", {})
    ints = sol.get("certified_intervals", {})
    return all([
        x.get("claim_id") == "K1743",
        "K1742 is not assumed" in pre.get("rederived_inputs", ""),
        "do not include factorials" in conv.get("chart_path", ""),
        "gamma=-80/3" in q6.get("exact_stationarity", ""),
        "eta=-385-y_0 y_x/72" in q6.get("exact_stationarity", ""),
        ints.get("P_2") == "[-0.704591778388654,-0.704591778388653]",
        ints.get("A_2") == "[-1.046975744740560,-1.046975744740558]",
        "det J is nonzero" in sol.get("uniqueness", ""),
        "One third-order chart degree remains free" in rem.get("dimension", ""),
        dec.get("second_order_chart_coefficients_unique") is True,
        dec.get("third_order_chart_coefficients_unique") is False,
        dec.get("complete_local_analytic_branch_unique") is False,
        dec.get("finite_strength_global_optimizer_identified") is False,
        "factor of two" in post.get("mistyping_check", ""),
        "remote branches" in x.get("scope_guard", ""),
    ])


mutations = []
for path, value in [
    (("pre_flight", "rederived_inputs"), "Assume K1742."),
    (("coefficient_convention", "chart_path"), "P_2 and A_2 are second derivatives."),
    (("q6_selection", "exact_stationarity"), "gamma=0 and eta=0"),
    (("second_order_chart_solution", "certified_intervals", "P_2"), "[-0.71,-0.70]"),
    (("second_order_chart_solution", "certified_intervals", "A_2"), "[-1.05,-1.04]"),
    (("second_order_chart_solution", "uniqueness"), "Assume uniqueness."),
    (("remaining_freedom", "dimension"), "No freedom remains."),
    (("decision", "third_order_chart_coefficients_unique"), True),
    (("decision", "complete_local_analytic_branch_unique"), True),
    (("decision", "finite_strength_global_optimizer_identified"), True),
    (("post_flight", "mistyping_check"), "No coefficient convention needed."),
    (("scope_guard",), "Global all-seed optimizer theorem."),
]:
    item = copy.deepcopy(d)
    cursor = item
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value
    mutations.append(item)

assert accepts(d)
for i, item in enumerate(mutations, 1):
    assert not accepts(item), i
    print(f"PASS {i:02d}: rejected hostile mutation")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
