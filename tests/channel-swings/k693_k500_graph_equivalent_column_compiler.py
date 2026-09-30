#!/usr/bin/env python3
"""K693: close a complete column from a two-sided graph equivalence."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k693-k500-graph-equivalent-column-compiler.json"


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k690 = json.loads((ROOT / "lab/process/k690-k500-summable-core-density-compiler.json").read_text())
    k691 = json.loads((ROOT / "lab/process/k691-k500-form-core-remainder-identification.json").read_text())
    assert k690["summable_core_theorem"]["same_graph_weight_required"]
    assert k691["form_core_theorem"]["one_common_form_core_for_both_required"]

    a_square = Fraction(73)
    c_square = Fraction(153, 4)
    lower = Fraction(1, 2)
    upper = Fraction(3, 4)
    assert lower * lower * a_square <= c_square <= upper * upper * a_square

    return {
        "schema_version": "1.0",
        "result_id": "K693-K500-GRAPH-EQUIVALENT-COLUMN-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A complete-domain sufficient packet making a column on Dom(a) closed and its bounded transform C a^-1 well defined from a two-sided graph equivalence.",
        "gu_typed_objects": {
            "carrier": "one Hilbert carrier H with a densely defined closed bijective graph weight a and bounded inverse",
            "column": "C:Dom(a)->direct_sum_j K_j, defined by the complete native component family",
            "result": "graph-equivalent column compiler MAP-TYPE=closed complete operator",
            "target": "K684/K687's closed column and bounded C a^-1 inputs before K691 identification",
        },
        "graph_equivalence_theorem": {
            "domain_identity": "Dom(C)=Dom(a)",
            "closed_graph_weight_required": True,
            "bounded_everywhere_a_inverse_required": True,
            "upper_inequality": "||C u||<=M||a u|| for every u in Dom(a)",
            "strict_lower_inequality": "m||a u||<=||C u|| for every u in Dom(a), with m>0",
            "closedness_consequence": "C is closed because C-Cauchy implies a-Cauchy; closedness of a identifies the limit and the upper inequality identifies C u",
            "bounded_transform_consequence": "B=C a^-1 is bounded with ||B||<=M and bounded below by m",
            "upper_bound_alone_sufficient_for_closedness": False,
            "finite_component_equivalence_sufficient_for_complete_column": False,
            "equivalence_on_nondense_or_noncore_tests_sufficient": False,
            "form_identity_with_native_remainder_automatic": False,
        },
        "exact_controls": {
            "controls_are_synthetic": True,
            "model": "H=C^2, a=diag(1,2), C=diag(1/2,3/2), Dom(a)=H",
            "test_vector": "u=(3,4)",
            "a_norm_square": q(a_square),
            "column_norm_square": q(c_square),
            "lower_graph_constant": q(lower),
            "upper_graph_constant": q(upper),
            "bounded_transform": "C a^-1=diag(1/2,3/4)",
            "upper_only_counterexample": "on l2, take unbounded closed a with proper Dom(a) and C=0 restricted to Dom(a); ||Cu||<=M||au|| holds but the zero operator on the nonclosed domain is not closed",
        },
        "dependency_reconciliation": {
            "K690_upper_summable_domination_not_promoted_to_closedness": True,
            "K687_component_route_sharpened_to_graph_equivalence": True,
            "K684_bounded_C_a_inverse_supplied_conditionally": True,
            "K691_common_form_core_identity_still_required": True,
            "native_component_or_graph_constants_added": False,
        },
        "native_interface_status": {
            "actual_native_components_serialized": False,
            "actual_native_DomC_equals_Doma_proved": False,
            "actual_native_two_sided_graph_equivalence_proved": False,
            "actual_native_closed_column_proved": False,
            "actual_native_bounded_C_a_inverse_proved": False,
            "actual_native_remainder_identity_proved": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "two_sided_graph_equivalence_suffices_for_closed_column": True,
            "native_closed_column_constructed": False,
            "next_exact_input": "Serialize the native complete component family on Dom(a) and prove both graph inequalities with m>0 and finite M; then prove K691's common-form-core identity before using the resulting bounded transform.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional complete-operator theorem and supplies no source-owned action, physical quotient, state or observable.",
        "preflight_bookend": {
            "route_comparison": "K690 supplies only an upper core domination. A two-sided graph equivalence on the full proposed domain is the cheapest direct closedness certificate and simultaneously constructs C a^-1.",
            "retrieval_collision_result": "K684 assumes a closed column and K687 derives it from closed components; no prior packet proves closedness directly from one full-domain graph equivalence.",
            "strongest_alternative": "Prove every component closed and density through K687/K690, or construct the remainder form first through K681.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Using K690's upper domination alone as if it made a column closed or identified its square with the native remainder.",
            "strongest_contrary_construction": "The zero operator restricted to the proper nonclosed domain of an unbounded closed a obeys every upper graph bound but is not closed.",
            "weakest_reproducibility_seam": "The lower inequality must cover the complete column norm on the exact full Dom(a), not a finite prefix or merely a dense algebraic test set.",
        },
        "controls": {
            "producer": "tests/channel-swings/k693_k500_graph_equivalent_column_compiler.py",
            "probe": "tests/channel-swings/k693_k500_graph_equivalent_column_compiler_probe.py",
            "controls_passed": 36,
            "hostile_mutations_rejected": 30,
        },
        "claim_ceiling": "Exact conditional graph-equivalence theorem: on Dom(a), a complete two-sided column/graph estimate makes C closed and C a^-1 bounded; the upper estimate alone does not. Current native custody supplies no component family, common domain, lower graph constant or remainder identity. No native r_free, T, R, A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(p: dict[str, Any]) -> None:
    t, n, c = p["graph_equivalence_theorem"], p["native_interface_status"], p["exact_controls"]
    assert t["closed_graph_weight_required"] and t["bounded_everywhere_a_inverse_required"]
    assert not t["upper_bound_alone_sufficient_for_closedness"]
    assert not t["finite_component_equivalence_sufficient_for_complete_column"]
    assert not t["equivalence_on_nondense_or_noncore_tests_sufficient"]
    assert not t["form_identity_with_native_remainder_automatic"]
    assert c["a_norm_square"] == "73" and c["column_norm_square"] == "153/4"
    assert c["lower_graph_constant"] == "1/2" and c["upper_graph_constant"] == "3/4"
    assert p["target_claim"] == "NONE-NOT-A-KILL" and p["source_and_ledger_effect"] == "none"
    assert all(value is False for value in n.values())
    assert p["decision"]["two_sided_graph_equivalence_suffices_for_closed_column"]
    assert not p["decision"]["native_closed_column_constructed"]


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); args = ap.parse_args()
    payload = build(); validate(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
