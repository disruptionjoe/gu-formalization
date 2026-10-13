#!/usr/bin/env python3
"""Hostile order, center, uniqueness and promotion mutations for K1742."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1742-matched-second-order-selection.json").read_text())


def accepts(data):
    law, chart, decision = data.get("matched_composition", {}), data.get("chart_selection", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1742",
        data.get("classification") == "INTERNAL_STRUCTURAL_ONLY",
        data.get("target_claim") == "NONE-NOT-A-KILL",
        "independent of eta and gamma" in law.get("eleven_halves_selection", ""),
        "(gamma+80/3)^2/120" in law.get("completed_square", ""),
        "(eta-eta_*)^2/5040" in law.get("completed_square", ""),
        "gamma_*=-80/3" in law.get("selected_centers", ""),
        "633.133529791640596" in law.get("selected_centers", ""),
        "det d(kappa_6,x)/d(p,a) is nonzero" in chart.get("second_order", ""),
        "One third-order chart degree of freedom" in chart.get("third_order_boundary", ""),
        not decision.get("q_eleven_halves_selects_second_order_chart", True),
        decision.get("q_six_is_first_later_second_order_selector"),
        decision.get("remaining_second_order_chart_motion_unique"),
        not decision.get("third_order_chart_motion_unique", True),
        not decision.get("complete_local_analytic_branch_unique", True),
        not decision.get("finite_strength_branch_certified", True),
        not decision.get("remote_or_singular_boundaries_excluded", True),
        "uniform moving-seed remainder" in data.get("scope_guard", ""),
    ])


mutations = []
for path, value in [
    (("claim_id",), "K1741"),
    (("classification",), "SOURCE_NATIVE_ROUTE"),
    (("target_claim",), "SC-META-53"),
    (("matched_composition", "eleven_halves_selection"), "q^(11/2) selects eta"),
    (("matched_composition", "completed_square"), "flat"),
    (("matched_composition", "selected_centers"), "gamma=eta=0"),
    (("chart_selection", "second_order"), "Jacobian zero"),
    (("chart_selection", "third_order_boundary"), "complete branch fixed"),
    (("decision", "q_eleven_halves_selects_second_order_chart"), True),
    (("decision", "q_six_is_first_later_second_order_selector"), False),
    (("decision", "remaining_second_order_chart_motion_unique"), False),
    (("decision", "third_order_chart_motion_unique"), True),
    (("decision", "complete_local_analytic_branch_unique"), True),
    (("decision", "finite_strength_branch_certified"), True),
    (("decision", "remote_or_singular_boundaries_excluded"), True),
    (("scope_guard",), "global all-seed finite-strength theorem"),
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
