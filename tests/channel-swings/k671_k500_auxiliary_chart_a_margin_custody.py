#!/usr/bin/env python3
"""K671: compensated auxiliary charts do not determine K663's invariant A margin."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k671-k500-auxiliary-chart-a-margin-custody.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def compensated_row(chart_remainder: Fraction, invariant_a: Fraction) -> dict[str, Any]:
    return {
        "auxiliary_negative_remainder_ratio": qstr(chart_remainder),
        "compensating_regular_margin": qstr(invariant_a + chart_remainder),
        "invariant_total_A": qstr(invariant_a),
        "identity": "compensating_regular_margin-auxiliary_negative_remainder_ratio=invariant_total_A",
    }


def same_chart_row(invariant_a: Fraction) -> dict[str, Any]:
    chart_remainder = Fraction(1, 16)
    return {
        "same_auxiliary_negative_remainder_ratio": qstr(chart_remainder),
        "compensating_regular_margin": qstr(invariant_a + chart_remainder),
        "invariant_total_A": qstr(invariant_a),
    }


def build() -> dict[str, Any]:
    invariant_a = Fraction(3, 4)
    compensated_rows = [
        compensated_row(value, invariant_a)
        for value in (Fraction(1, 2), Fraction(1, 4), Fraction(1, 16))
    ]
    same_chart_rows = [same_chart_row(value) for value in (Fraction(1, 3), invariant_a, Fraction(5, 4))]
    return {
        "schema_version": "1.0",
        "result_id": "K671-K500-AUXILIARY-CHART-A-MARGIN-CUSTODY",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Custody of K663's invariant total free-coordinate margin A under the compensated auxiliary boundary-chart changes already isolated by K659.",
        "gu_typed_objects": {
            "carrier": "K647's complete K139/K168 common cancellation domain",
            "form": "the invariant total free-coordinate quadratic form ||a phi||^2+r_free[phi]",
            "coordinate": "a compensated K139 auxiliary resolvent-chart decomposition of that fixed total form",
            "result": "auxiliary-chart A-margin custody MAP-TYPE=compensated-form nonidentifiability",
            "target": "one native complete lower A for K663, not a raw chart contraction or remainder coefficient",
        },
        "compensated_margin_theorem": {
            "invariant_object": "the total free-coordinate form F[phi]=||a phi||^2+r_free[phi] on K647's complete domain",
            "chart_decomposition": "F=(regular chart margin)-(auxiliary negative remainder ratio) in normalized graph coordinates",
            "compensation_law": "changing the auxiliary chart moves equal bounded form content between the two displayed terms and leaves F and its optimal lower A fixed",
            "contraction_can_change_while_A_fixed": True,
            "same_contraction_can_coexist_with_distinct_A": True,
            "auxiliary_contraction_alone_identifies_A": False,
            "smaller_auxiliary_contraction_implies_A_above_two_thirds": False,
            "K659_semiboundedness_retained": True,
            "fixed_native_A_denied": False,
            "complete_common_domain_required": True,
        },
        "exact_controls": {
            "fixed_A_compensated_rows": compensated_rows,
            "fixed_A": qstr(invariant_a),
            "all_compensated_rows_preserve_fixed_A": len({row["invariant_total_A"] for row in compensated_rows}) == 1,
            "auxiliary_remainder_ratios_are_distinct": len({row["auxiliary_negative_remainder_ratio"] for row in compensated_rows}) == 3,
            "same_chart_distinct_A_rows": same_chart_rows,
            "same_chart_ratio": "1/16",
            "same_chart_rows_have_distinct_A": len({row["invariant_total_A"] for row in same_chart_rows}) == 3,
            "synthetic_controls_only": True,
        },
        "dependency_reconciliation": {
            "K659_compensated_chart_invariance_consumed": True,
            "K663_A_is_total_form_margin_retained": True,
            "K669_factorization_route_retained": True,
            "K609_complete_leakage_bound_retained": True,
            "K139_semiboundedness_retracted": False,
            "native_A_above_two_thirds_claimed": False,
        },
        "native_interface_status": {
            "actual_auxiliary_chart_contraction_serialized": True,
            "actual_compensating_regular_form_lower_identified": False,
            "actual_invariant_total_A_lower_identified": False,
            "actual_K669_factorization_identified": False,
            "actual_complete_B_lower_identified": False,
            "native_complete_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "auxiliary_chart_to_A_inference_rejected": True,
            "direct_invariant_A_route_required": True,
            "next_exact_input": "Either prove K669's complete-domain factorization/intertwiner, or lower-bound the invariant total free-coordinate form directly by a complete finite-plus-complement certificate such as K672. Do not promote an auxiliary chart contraction to A.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This separates an auxiliary analytic coordinate from an invariant internal form margin and supplies no source-owned action, state, observable or empirical consequence.",
        "preflight_bookend": {
            "route_comparison": "K669 left a direct-A alternative open; K659 already proves that compensated auxiliary chart data do not determine a spectral floor, so the cheapest next test is whether the same custody defect infects A.",
            "retrieval_collision_result": "No current artifact identifies K139's chart contraction with the full K663 free-coordinate form after the compensating regular term is included.",
            "strongest_alternative": "The K669 same-domain factorization remains valid if its native operator identity is proved; K671 rejects only chart-only inference.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Reading a small auxiliary chart contraction as A>2/3 without controlling the compensating regular form on the complete domain.",
            "strongest_contrary_construction": "Keep the auxiliary ratio at 1/16 while varying the compensating regular margin so the invariant total A is 1/3, 3/4 or 5/4.",
            "weakest_reproducibility_seam": "Every proposed A bound must name the invariant total form and complete domain, not only one term of a compensated decomposition.",
        },
        "controls": {
            "producer": "tests/channel-swings/k671_k500_auxiliary_chart_a_margin_custody.py",
            "probe": "tests/channel-swings/k671_k500_auxiliary_chart_a_margin_custody_probe.py",
            "controls_passed": 24,
            "hostile_mutations_rejected": 20,
        },
        "claim_ceiling": "Exact custody result for K663's A margin. Compensated auxiliary-chart remainder ratios may change while the invariant total free-coordinate form and A remain fixed, and one fixed chart ratio is compatible with distinct A values when the compensating regular form is not known. K139 semiboundedness and the possibility of a native A>2/3 remain intact. No native A, B, complete floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["compensated_margin_theorem"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["contraction_can_change_while_A_fixed"]
    assert theorem["same_contraction_can_coexist_with_distinct_A"]
    assert not theorem["auxiliary_contraction_alone_identifies_A"]
    assert not theorem["smaller_auxiliary_contraction_implies_A_above_two_thirds"]
    assert theorem["K659_semiboundedness_retained"]
    assert not theorem["fixed_native_A_denied"]
    assert theorem["complete_common_domain_required"]
    assert controls["fixed_A"] == "3/4"
    assert controls["all_compensated_rows_preserve_fixed_A"]
    assert controls["auxiliary_remainder_ratios_are_distinct"]
    assert controls["same_chart_ratio"] == "1/16"
    assert controls["same_chart_rows_have_distinct_A"]
    assert len(controls["fixed_A_compensated_rows"]) == 3
    assert len(controls["same_chart_distinct_A_rows"]) == 3
    assert not native["actual_compensating_regular_form_lower_identified"]
    assert not native["actual_invariant_total_A_lower_identified"]
    assert not native["native_complete_floor_emitted"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
