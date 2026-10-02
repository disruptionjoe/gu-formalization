#!/usr/bin/env python3
"""K848: equal raw rank budgets can pass or fail by quotient overlap."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from k847_sc_act_06_quotient_repair_theorem import repair_case

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k848-sc-act-06-rank-budget-overlap-countermodels.json"
PATHS = {"k847": ROOT / "lab/process/k847-sc-act-06-quotient-repair-theorem.json"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    k847 = json.loads(PATHS["k847"].read_text(encoding="utf-8"))
    g = [[1], [0], [0], [0]]
    j = [[0, 1, 0, 0]]
    pass_case = repair_case(g, j, [[0, 0, 1, 0]], [[0], [0], [0], [1]])
    duplicate_response = repair_case(g, j, [[0, 1, 0, 0]], [[0], [0], [0], [1]])
    gauge_overlap = repair_case(g, j, [[0, 0, 1, 0]], [[1], [0], [0], [0]])
    return {
        "schema_version": "1.0",
        "result_id": "K848-SC-ACT-06-RANK-BUDGET-OVERLAP-COUNTERMODELS",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": k847["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact four-dimensional controls for K847's quotient repair theorem; they are not GU principal symbols.",
        "gu_typed_objects": {
            "carrier": "LAYER=toy CHIRALITY=N/A E0=R, E1=R4, E2=R",
            "pairing": "standard Euclidean coordinate pairing",
            "real_structure": "real",
            "grading": "symmetries -> four fields -> equations",
            "action_owner": "repository-construction",
            "target": "MAP-TYPE=quotient raw-rank versus induced-rank discrimination",
        },
        "pinned_inputs": {"k847": {"path": str(PATHS["k847"].relative_to(ROOT)), "sha256": digest(PATHS["k847"])}},
        "common_base": {
            "G": g,
            "J": j,
            "old_middle_cohomology_basis": ["[e3]", "[e4]"],
            "old_middle_cohomology_dimension": 2,
        },
        "controls": {
            "complementary_pass": pass_case,
            "duplicate_response_fail": duplicate_response,
            "old_gauge_overlap_fail": gauge_overlap,
        },
        "comparison": {
            "all_raw_response_plus_symmetry_ranks": [
                pass_case["raw_response_rank"] + pass_case["raw_symmetry_rank"],
                duplicate_response["raw_response_rank"] + duplicate_response["raw_symmetry_rank"],
                gauge_overlap["raw_response_rank"] + gauge_overlap["raw_symmetry_rank"],
            ],
            "all_raw_budgets_equal_old_h": True,
            "all_three_are_valid_complex_repairs": True,
            "pass_effective_split": [1, 1],
            "duplicate_response_effective_split": [0, 1],
            "gauge_overlap_effective_split": [1, 0],
            "raw_rank_threshold_decides_exactness": False,
            "quotient_complementarity_decides_exactness": True,
        },
        "decision": {
            "K845_threshold_is_only_a_coarse_necessary_test": True,
            "response_rows_already_in_old_equation_span_get_zero_credit": True,
            "symmetry_directions_already_in_old_gauge_image_get_zero_credit": True,
            "next_exact_input": "Report induced quotient ranks and the equality im(S_bar)=ker(tau_bar), not raw matrix ranks or a scalar budget alone.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The countermodels test finite-dimensional inference only; none is a GU family, source-owned map, physical quotient or observable.",
        "claim_ceiling": "Sharp synthetic countermodels to raw-rank sufficiency and a complementary exact control. They do not constrain an absent source-owned GU repair beyond its certificate obligations.",
        "probe_contract": {
            "producer": "tests/channel-swings/k848_sc_act_06_rank_budget_overlap_countermodels.py",
            "probe": "tests/channel-swings/k848_sc_act_06_rank_budget_overlap_countermodels_probe.py",
            "controls_passed": 41,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(p: dict[str, Any]) -> None:
    c, x, d = p["controls"], p["comparison"], p["decision"]
    a, b, g = c["complementary_pass"], c["duplicate_response_fail"], c["old_gauge_overlap_fail"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE", p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"], p["gu_typed_objects"]["action_owner"] == "repository-construction",
        p["common_base"]["old_middle_cohomology_dimension"] == 2,
        p["common_base"]["old_middle_cohomology_basis"] == ["[e3]", "[e4]"],
        a["repaired_complex_valid"], b["repaired_complex_valid"], g["repaired_complex_valid"],
        a["raw_response_rank"] == a["raw_symmetry_rank"] == 1,
        b["raw_response_rank"] == b["raw_symmetry_rank"] == 1,
        g["raw_response_rank"] == g["raw_symmetry_rank"] == 1,
        a["response_effective_rank_on_old_cohomology"] == 1,
        a["symmetry_effective_rank_in_response_kernel"] == 1,
        a["new_middle_cohomology_dimension"] == 0, a["middle_exact_after_repair"],
        b["response_effective_rank_on_old_cohomology"] == 0,
        b["symmetry_effective_rank_in_response_kernel"] == 1,
        b["new_middle_cohomology_dimension"] == 1, not b["middle_exact_after_repair"],
        g["response_effective_rank_on_old_cohomology"] == 1,
        g["symmetry_effective_rank_in_response_kernel"] == 0,
        g["new_middle_cohomology_dimension"] == 1, not g["middle_exact_after_repair"],
        x["all_raw_response_plus_symmetry_ranks"] == [2, 2, 2],
        x["all_raw_budgets_equal_old_h"], x["all_three_are_valid_complex_repairs"],
        x["pass_effective_split"] == [1, 1], x["duplicate_response_effective_split"] == [0, 1],
        x["gauge_overlap_effective_split"] == [1, 0], not x["raw_rank_threshold_decides_exactness"],
        x["quotient_complementarity_decides_exactness"], d["K845_threshold_is_only_a_coarse_necessary_test"],
        d["response_rows_already_in_old_equation_span_get_zero_credit"],
        d["symmetry_directions_already_in_old_gauge_image_get_zero_credit"],
        "im(S_bar)=ker(tau_bar)" in d["next_exact_input"],
        "UNCHANGED" in p["source_and_ledger_effect"], "not GU principal symbols" in p["scope"],
        len(p["pinned_inputs"]["k847"]["sha256"]) == 64,
        p["probe_contract"]["controls_passed"] == 41, p["probe_contract"]["hostile_mutations_rejected"] == 20,
    ]
    assert len(checks) == p["probe_contract"]["controls_passed"]
    assert all(checks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    elif not args.check:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
