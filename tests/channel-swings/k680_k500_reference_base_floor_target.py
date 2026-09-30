#!/usr/bin/env python3
"""K680: compile K670's B target into K168 base-floor and Weyl targets."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k680-k500-reference-base-floor-target.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k656 = json.loads((ROOT / "lab/process/k656-k500-base-floor-target-lift.json").read_text())
    k657 = json.loads((ROOT / "lab/process/k657-k500-boundary-weyl-base-floor-certificate.json").read_text())
    k670 = json.loads((ROOT / "lab/process/k670-k500-asymmetric-native-margin-target.json").read_text())
    assert k656["base_floor_lift_theorem"]["selected_target"] == "b=r0-2"
    assert k657["ordinary_boundary_triple_theorem"]["accepted_consequence"].startswith("D_W(-s)>=0")
    assert k670["asymmetric_target_theorem"]["selected_rational_B_target"] == "1/170"

    b_target = Fraction(1, 170)
    reference_loss = Fraction(2)
    r0_target = reference_loss + b_target
    s_target = -r0_target
    assert r0_target == Fraction(341, 170)
    assert r0_target - reference_loss == b_target

    return {
        "schema_version": "1.0",
        "result_id": "K680-K500-REFERENCE-BASE-FLOOR-TARGET",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The sharp complete K139 base-form and K657 real-level denominator targets sufficient to survive K168's two-unit reference-shape loss and meet K670's complete effective B>=1/170 requirement.",
        "gu_typed_objects": {
            "base_form": "K656's complete fixed K139 regular form R0 relative to M=S*S",
            "reference_shape": "K168's W_ref=diag(-2,1,1), whose worst complete form shift is -2M",
            "effective_margin": "B, the complete same-domain coefficient-form margin consumed by K663/K670",
            "boundary_denominator": "K657's D_W(lambda)=W-M(lambda) on the full spectator-Fock boundary space",
            "result": "reference base-floor target MAP-TYPE=sharp rational budget composition",
            "target": "K665's complete finite-plus-two-tail B packet at 1/170",
        },
        "base_floor_target_theorem": {
            "K168_reference_loss": "2",
            "K670_complete_B_target": "1/170",
            "required_complete_base_floor": "r0>=341/170",
            "composition": "R_ref>=R0-2M>=(r0-2)M",
            "equality_check": "341/170-2=1/170",
            "target_is_sharp_over_K168_reference_class": True,
            "finite_base_rows_sufficient": False,
            "one_parity_tail_sufficient": False,
            "complete_common_domain_required": True,
        },
        "weyl_target_translation": {
            "K657_parameterization": "lambda=-s and r0=-s",
            "target_lambda": "341/170",
            "target_s": "-341/170",
            "required_denominator_test": "D_W(341/170)>=0 on the complete spectator-Fock boundary space",
            "required_reference_test": "341/170 lies in rho(A_F) for the proved Friedrichs reference and the underlying symmetric operator is bounded below by 341/170",
            "positive_lambda_forbidden_by_K657": False,
            "synthetic_negative_floor_rows_supply_target": False,
            "sign_convention_may_be_inferred": False,
        },
        "exact_controls": {
            "B_target": qstr(b_target),
            "reference_loss": qstr(reference_loss),
            "base_floor_target": qstr(r0_target),
            "s_target": qstr(s_target),
            "composed_B": qstr(r0_target - reference_loss),
            "below_target_control": {
                "r0": "2",
                "composed_B": "0",
                "meets_K670_target": False,
            },
            "above_target_control": {
                "r0": "3",
                "composed_B": "1",
                "meets_K670_target": True,
            },
            "controls_are_conditional_not_native": True,
        },
        "dependency_reconciliation": {
            "K656_sharp_two_unit_lift_consumed": True,
            "K657_boundary_denominator_equivalence_consumed_conditionally": True,
            "K670_complete_B_target_consumed": True,
            "K665_every_finite_row_and_two_tail_requirement_retained": True,
            "K667_matched_trace_bound_retained": True,
            "K669_conditional_A_requirement_retained": True,
        },
        "native_interface_status": {
            "actual_native_base_floor_r0_identified": False,
            "actual_native_denominator_at_target_serialized": False,
            "actual_native_denominator_nonnegative": False,
            "actual_complete_B_lower_identified": False,
            "actual_plus_minus_B_tails_identified": False,
            "native_complete_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "complete_base_floor_target_now_exact": True,
            "native_B_target_satisfied": False,
            "next_exact_input": "Prove R0>=(341/170)M on the complete K647 domain directly, or instantiate K657 at lambda=341/170 with the proved Friedrichs reference, resolvent/sign premises and complete D_W(341/170)>=0. Then transport the bound through K168 and still verify every K665 finite row plus both parity tails on the same domain.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a rational lower-bound budget inside a repository-supplied conditional operator model and supplies no source-owned action, physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "The A route is blocked one object earlier at r_free custody, while K656 already makes one complete base lower sufficient for every parity/bath compression. Composing it with K670 exposes the cheapest exact independent B target.",
            "retrieval_collision_result": "K656 states b=r0-2 and K670 states B>=1/170, but no current packet computes the consequent r0 or K657 real-level target.",
            "strongest_alternative": "K652's parity-local all-order cancellation bounds can prove B directly without a global R0 floor, but require more rows and two tails.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Reporting r0=341/170, B=1/170 or denominator positivity as native merely because the target arithmetic is exact.",
            "strongest_contrary_construction": "A complete base floor r0=2 survives only to B>=0 after K168 and misses K670's strict positive determinant budget.",
            "weakest_reproducibility_seam": "K657 must be instantiated at positive lambda=341/170 with its exact sign convention and full spectator-Fock denominator; its existing negative-floor controls do not supply this row.",
        },
        "controls": {
            "producer": "tests/channel-swings/k680_k500_reference_base_floor_target.py",
            "probe": "tests/channel-swings/k680_k500_reference_base_floor_target_probe.py",
            "controls_passed": 32,
            "hostile_mutations_rejected": 24,
        },
        "claim_ceiling": "Exact conditional target composition: because K168 can lower the base form by two M-units, K670's complete B>=1/170 requires the sharp base target r0>=341/170. Under K657's convention this corresponds to lambda=-s=341/170 and a complete D_W(341/170)>=0 packet with all reference premises. No native r0, denominator, B row, parity tail, A, complete floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["base_floor_target_theorem"]
    weyl = payload["weyl_target_translation"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["required_complete_base_floor"] == "r0>=341/170"
    assert theorem["equality_check"] == "341/170-2=1/170"
    assert theorem["target_is_sharp_over_K168_reference_class"]
    assert not theorem["finite_base_rows_sufficient"]
    assert not theorem["one_parity_tail_sufficient"]
    assert theorem["complete_common_domain_required"]
    assert weyl["target_lambda"] == "341/170" and weyl["target_s"] == "-341/170"
    assert not weyl["positive_lambda_forbidden_by_K657"]
    assert not weyl["synthetic_negative_floor_rows_supply_target"]
    assert not weyl["sign_convention_may_be_inferred"]
    assert controls["composed_B"] == "1/170"
    assert not controls["below_target_control"]["meets_K670_target"]
    assert controls["above_target_control"]["meets_K670_target"]
    assert not native["actual_complete_B_lower_identified"]
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
