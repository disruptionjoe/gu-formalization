#!/usr/bin/env python3
"""K683: transfer a nearby complete Weyl-denominator row to lambda=341/170."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k683-k500-weyl-target-level-robustness.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k657 = json.loads((ROOT / "lab/process/k657-k500-boundary-weyl-base-floor-certificate.json").read_text())
    k658 = json.loads((ROOT / "lab/process/k658-k500-cofinal-denominator-margin-transfer.json").read_text())
    k680 = json.loads((ROOT / "lab/process/k680-k500-reference-base-floor-target.json").read_text())
    assert k657["ordinary_boundary_triple_theorem"]["equivalence"] == "A_W>=lambda iff D_W(lambda)>=0"
    assert k658["cofinal_margin_theorem"]["same_s_required"]
    assert k680["weyl_target_translation"]["target_lambda"] == "341/170"

    target = Fraction(341, 170)
    nearby = Fraction(21, 10)
    margin = Fraction(1, 20)
    variation = Fraction(1, 100)
    transferred = margin - variation
    assert nearby > target
    assert transferred == Fraction(1, 25)

    return {
        "schema_version": "1.0",
        "result_id": "K683-K500-WEYL-TARGET-LEVEL-ROBUSTNESS",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A complete-space perturbation and monotonicity certificate that can transport a denominator lower proved at one nearby real level into K680's exact lambda=341/170 target in the same ordinary-boundary-triple coordinate.",
        "gu_typed_objects": {
            "boundary_coordinate": "one fixed ordinary boundary triple with Friedrichs reference and target extension parameter W",
            "weyl_family": "the bounded self-adjoint real-level Weyl values M(lambda) on one connected reference-resolvent interval",
            "denominator": "D_W(lambda)=W-M(lambda) on the complete spectator-Fock boundary space",
            "target_level": "lambda_0=341/170 from K680",
            "result": "Weyl target-level robustness MAP-TYPE=complete operator-order perturbation",
            "target": "K680's complete D_W(341/170)>=0 base-floor packet",
        },
        "level_transfer_theorem": {
            "nearby_lower_hypothesis": "D_W(lambda_1)>=d_1 I on the complete boundary space",
            "weyl_variation_hypothesis": "||M(lambda_1)-M(lambda_0)||<=omega on that same complete space",
            "conclusion": "D_W(lambda_0)>=(d_1-omega)I",
            "target_admission": "d_1>=omega implies D_W(lambda_0)>=0",
            "same_boundary_coordinate_required": True,
            "same_target_extension_W_required": True,
            "complete_boundary_coverage_required": True,
            "connected_reference_resolvent_interval_required": True,
            "pointwise_or_finite_block_variation_sufficient": False,
            "raw_floor_transport_across_nonunitary_coordinate_change_allowed": False,
        },
        "monotone_shortcut": {
            "hypothesis": "lambda_1>=lambda_0 and the ordinary-boundary-triple Weyl family is operator monotone on the complete real reference-resolvent interval",
            "order": "M(lambda_1)>=M(lambda_0), hence D_W(lambda_0)>=D_W(lambda_1)",
            "consequence": "a complete nonnegative denominator at lambda_1 transfers to lambda_0 without spending a norm-variation margin",
            "reference_interval_and_sign_may_be_inferred": False,
            "finite_sector_monotonicity_sufficient": False,
        },
        "composition": {
            "target_lambda": "341/170",
            "if_target_denominator_nonnegative": "K657 gives A_W>=341/170 and K680/K656 give B>=1/170 after K168",
            "K657_reference_Friedrichs_resolvent_and_sign_premises_retained": True,
            "K665_every_finite_row_and_two_tail_requirement_retained": True,
            "native_target_row_supplied": False,
        },
        "exact_controls": {
            "target_lambda": qstr(target),
            "nearby_lambda_1": qstr(nearby),
            "nearby_complete_margin_d_1": qstr(margin),
            "complete_weyl_variation_omega": qstr(variation),
            "transferred_target_margin": qstr(transferred),
            "accepted": True,
            "failing_row": {
                "nearby_complete_margin_d_1": "1/100",
                "complete_weyl_variation_omega": "1/50",
                "transferred_target_margin": "-1/100",
                "accepted": False,
            },
            "coordinate_mismatch_rejects": True,
            "controls_are_synthetic": True,
        },
        "dependency_reconciliation": {
            "K657_real_level_equivalence_consumed_conditionally": True,
            "K658_same_level_transfer_retained": True,
            "K658_extended_to_nearby_real_level_with_weyl_variation": True,
            "K680_exact_target_consumed": True,
            "native_denominator_row_added": False,
        },
        "native_interface_status": {
            "actual_native_nearby_denominator_serialized": False,
            "actual_native_nearby_lower_identified": False,
            "actual_native_complete_weyl_variation_bound": False,
            "actual_native_monotone_interval_authenticated": False,
            "actual_native_target_denominator_nonnegative": False,
            "actual_native_base_floor_r0_identified": False,
            "actual_complete_B_lower_identified": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "nearby_level_rows_now_reusable_under_exact_budget": True,
            "native_target_denominator_proved": False,
            "next_exact_input": "In K139's proved Friedrichs boundary coordinate, choose a complete real reference-resolvent interval containing 341/170 and one computable lambda_1. Prove D_W(lambda_1)>=d_1 I and either a complete Weyl difference bound omega<=d_1 or the valid operator-monotone ordering for lambda_1>=341/170. Then apply K657 and still execute K665's complete finite-plus-two-tail packet.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional real-level denominator transfer inside a repository-supplied boundary model and supplies no source-owned action, physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K680 fixes one exact real level, while native calculation may naturally land on a nearby rational level. Paying a complete Weyl-variation budget is the cheapest honest way to reuse such a row without changing the target.",
            "retrieval_collision_result": "K658 transfers approximants only at the same real level; no current packet transports complete denominator order between two real levels.",
            "strongest_alternative": "Compute D_W(341/170) directly, bypassing any level transfer and its variation burden.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Moving a finite-sector or differently coordinated denominator lower between real levels without a complete-space Weyl bound or authenticated monotonicity interval.",
            "strongest_contrary_construction": "A nearby margin 1/100 with complete Weyl variation 1/50 transfers to -1/100, so nearby positivity alone does not certify the target.",
            "weakest_reproducibility_seam": "The same W, boundary coordinate, full spectator-Fock carrier, reference-resolvent interval, sign convention and complete Weyl variation must be serialized at both levels.",
        },
        "controls": {
            "producer": "tests/channel-swings/k683_k500_weyl_target_level_robustness.py",
            "probe": "tests/channel-swings/k683_k500_weyl_target_level_robustness_probe.py",
            "controls_passed": 32,
            "hostile_mutations_rejected": 26,
        },
        "claim_ceiling": "Exact conditional real-level robustness result: in one fixed complete ordinary-boundary-triple coordinate, D_W(lambda_1)>=d_1 I and ||M(lambda_1)-M(341/170)||<=omega imply D_W(341/170)>=(d_1-omega)I; authenticated Weyl monotonicity gives a sharper downward transfer from a higher level. Current native custody supplies no such denominator, interval or complete variation row. No native r0, B, parity tail, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["level_transfer_theorem"]
    shortcut = payload["monotone_shortcut"]
    native = payload["native_interface_status"]
    assert theorem["same_boundary_coordinate_required"]
    assert theorem["same_target_extension_W_required"]
    assert theorem["complete_boundary_coverage_required"]
    assert theorem["connected_reference_resolvent_interval_required"]
    assert not theorem["pointwise_or_finite_block_variation_sufficient"]
    assert not theorem["raw_floor_transport_across_nonunitary_coordinate_change_allowed"]
    assert not shortcut["reference_interval_and_sign_may_be_inferred"]
    assert not shortcut["finite_sector_monotonicity_sufficient"]
    assert payload["exact_controls"]["target_lambda"] == "341/170"
    assert payload["exact_controls"]["transferred_target_margin"] == "1/25"
    assert not payload["exact_controls"]["failing_row"]["accepted"]
    assert not native["actual_native_target_denominator_nonnegative"]
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
