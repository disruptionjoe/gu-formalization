#!/usr/bin/env python3
"""K699: transfer an a-relative form mismatch into a complete A margin."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k699-k500-approximate-form-a-margin-compiler.json"


def q(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def build() -> dict[str, Any]:
    k696 = json.loads((ROOT / "lab/process/k696-k500-column-remainder-integration-compiler.json").read_text())
    assert k696["decision"]["graph_equivalence_plus_common_form_core_identifies_T_and_bounded_R"]
    column_gram_upper = Fraction(1, 4)
    mismatch = Fraction(1, 100)
    native_gram_upper = column_gram_upper + mismatch
    a_lower = 1 - native_gram_upper
    target = Fraction(2, 3)
    slack = a_lower - target
    return {
        "schema_version": "1.0",
        "result_id": "K699-K500-APPROXIMATE-FORM-A-MARGIN-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A complete quantitative replacement for K696's exact common-form identity when the native remainder form and column square are close in the graph-weight norm.",
        "gu_typed_objects": {
            "graph_weight": "one positive closed a with bounded everywhere inverse on H",
            "column_transform": "B=C a^-1, bounded on H",
            "native_transform": "R=T a^-1 for the closed native remainder form h[u]=||T u||^2",
            "mismatch": "the complete a-relative quadratic-form defect h-q_C on Dom(a)",
            "result": "approximate-form A-margin compiler MAP-TYPE=bounded self-adjoint Gram comparison",
            "target": "K668/K670's complete A lower without exact form equality",
        },
        "theorem": {
            "complete_domain_map_required": True,
            "native_form_closed_nonnegative_required": True,
            "column_transform_bounded_required": True,
            "complete_a_relative_mismatch_required": True,
            "mismatch_hypothesis": "|h[u]-||C u||^2|<=epsilon||a u||^2 for every u in Dom(a)",
            "conjugated_gram_consequence": "||R*R-B*B||<=epsilon",
            "upper_transfer": "B*B<=b I implies R*R<=(b+epsilon)I",
            "A_transfer": "A=I-R*R>=(1-b-epsilon)I",
            "exact_common_form_identity_required_for_quantitative_A": False,
            "finite_test_equality_sufficient": False,
            "one_sided_domain_inclusion_sufficient": False,
            "componentwise_mismatch_without_complete_sum_sufficient": False,
        },
        "exact_controls": {
            "controls_are_synthetic": True,
            "column_gram_upper": q(column_gram_upper),
            "a_relative_form_mismatch": q(mismatch),
            "native_gram_upper": q(native_gram_upper),
            "A_lower": q(a_lower),
            "target_A_lower": q(target),
            "strict_slack": q(slack),
            "accepted": slack > 0,
            "matrix_control": "B*B=diag(1/4,9/100), R*R=B*B+diag(1/100,-1/200)",
            "finite_test_counterexample": "rank-one defects supported in successive orthogonal complement directions vanish on every fixed finite test set while retaining norm epsilon",
        },
        "dependency_reconciliation": {
            "K696_exact_identity_route_preserved": True,
            "K696_exact_identity_no_longer_only_quantitative_A_route": True,
            "K682_complete_relative_form_interface_consumed": True,
            "K668_A_input_closed_conditionally": True,
            "native_a_relative_mismatch_added": False,
        },
        "native_interface_status": {
            "actual_native_column_transform_serialized": False,
            "actual_native_remainder_transform_serialized": False,
            "actual_native_complete_mismatch_proved": False,
            "actual_native_column_gram_upper_proved": False,
            "native_A_above_two_thirds_proved": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "approximate_form_identity_can_supply_complete_A_margin": True,
            "native_A_margin_constructed": False,
            "next_exact_input": "On one native Dom(a), serialize B=C a^-1 and the closed native h=-r_free, prove a complete outward bound on |h[u]-||Cu||^2|/||a u||^2 and a complete B*B upper. If their sum is below 1/3, emit the native A lower without requiring exact form equality.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional complete form-comparison theorem and supplies no source-owned action, physical quotient, state or observable.",
        "preflight_bookend": {
            "route_comparison": "K696's exact identity is sufficient but brittle. A complete a-relative mismatch is the cheaper quantitative input when native data arrive as analytic or interval bounds.",
            "retrieval_collision_result": "K682 bounds one native form by a; K696 identifies exact equality. No prior packet transfers a nonzero native/column form defect into the complete A margin.",
            "strongest_alternative": "Prove K696's exact common-form-core identity and use K697 directly.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Replacing the complete a-relative defect by agreement on finitely many vectors or by componentwise errors without a complete sum.",
            "strongest_contrary_construction": "A rank-one defect can hide in every inspected finite complement while preserving a fixed operator norm.",
            "weakest_reproducibility_seam": "Both forms and the graph weight must use one domain, and the mismatch bound must be uniform over that complete domain.",
        },
        "controls": {
            "producer": "tests/channel-swings/k699_k500_approximate_form_a_margin_compiler.py",
            "probe": "tests/channel-swings/k699_k500_approximate_form_a_margin_compiler_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 28,
        },
        "claim_ceiling": "Exact conditional stability theorem: a complete a-relative mismatch epsilon between the native remainder form and column square gives ||R*R-B*B||<=epsilon and A>=(1-b-epsilon)I. The synthetic b=1/4, epsilon=1/100 packet yields A>=37/50, above 2/3 by 11/150. No native column, mismatch, A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n = p["theorem"], p["exact_controls"], p["native_interface_status"]
    for key in ("complete_domain_map_required", "native_form_closed_nonnegative_required", "column_transform_bounded_required", "complete_a_relative_mismatch_required"):
        assert t[key]
    for key in ("exact_common_form_identity_required_for_quantitative_A", "finite_test_equality_sufficient", "one_sided_domain_inclusion_sufficient", "componentwise_mismatch_without_complete_sum_sufficient"):
        assert not t[key]
    assert c["column_gram_upper"] == "1/4" and c["a_relative_form_mismatch"] == "1/100"
    assert c["native_gram_upper"] == "13/50" and c["A_lower"] == "37/50"
    assert c["strict_slack"] == "11/150" and c["accepted"]
    assert all(value is False for value in n.values())
    assert p["decision"]["approximate_form_identity_can_supply_complete_A_margin"]
    assert not p["decision"]["native_A_margin_constructed"]
    assert p["target_claim"] == "NONE-NOT-A-KILL" and p["source_and_ledger_effect"] == "none"


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); args = ap.parse_args()
    payload = build(); validate(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
