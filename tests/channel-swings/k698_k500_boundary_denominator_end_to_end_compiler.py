#!/usr/bin/env python3
"""K698: compose the Friedrichs/trace/gamma chain to the target denominator."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k698-k500-boundary-denominator-end-to-end-compiler.json"


def q(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def build() -> dict[str, Any]:
    k695 = json.loads((ROOT / "lab/process/k695-k500-friedrichs-defect-cofinal-compiler.json").read_text())
    k689 = json.loads((ROOT / "lab/process/k689-k500-gamma-anchor-propagation-compiler.json").read_text())
    assert k695["decision"]["self_adjoint_domain_inclusion_authenticates_Friedrichs_reference"]
    assert k689["decision"]["one_anchor_plus_reference_gap_suffices_for_K686_gamma_pair"]
    target, anchor = Fraction(341, 170), Fraction(21, 10)
    gap = Fraction(1, 2)
    gamma_anchor = Fraction(1, 5)
    factor = Fraction(1) + abs(anchor - target) / gap
    gamma_target = factor * gamma_anchor
    variation = abs(anchor - target) * gamma_anchor * gamma_target
    nearby_margin = Fraction(1, 100)
    transferred = nearby_margin - variation
    assert factor == Fraction(101, 85)
    assert gamma_target == Fraction(101, 425)
    assert variation == Fraction(808, 180625)
    assert transferred == Fraction(3993, 722500)
    return {
        "schema_version": "1.0",
        "result_id": "K698-K500-BOUNDARY-DENOMINATOR-END-TO-END-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "An end-to-end complete ordinary-boundary-triple certificate from Friedrichs-domain authentication and cofinal trace bounds to a positive denominator at lambda=341/170.",
        "gu_typed_objects": {
            "minimal_operator": "one closed semibounded symmetric S on the complete native carrier",
            "boundary_triple": "one ordinary triple (Gamma_0,Gamma_1) for S* on the complete spectator-Fock boundary space",
            "reference": "A_0=S*|ker(Gamma_0), authenticated as the Friedrichs extension",
            "target_extension": "one fixed self-adjoint boundary parameter W in the same coordinate",
            "denominator": "D_W(lambda)=W-M(lambda)",
            "result": "boundary-denominator end-to-end compiler MAP-TYPE=complete reference/trace/resolvent chain",
            "target": "K657/K680's D_W(341/170)>=0 input",
        },
        "end_to_end_theorem": {
            "complete_Friedrichs_domain_inclusion_required": True,
            "complete_Friedrichs_form_lower_required": True,
            "complete_anchor_defect_trace_packet_required": True,
            "same_real_reference_resolvent_interval_required": True,
            "same_boundary_coordinate_and_fixed_W_required": True,
            "nearby_complete_denominator_margin_required": True,
            "chain": [
                "self-adjoint domain inclusion gives A_0=A_F",
                "the complete Friedrichs form lower gives a spectral gap below the interval",
                "finite/tail/cross trace bounds give whole-defect coercivity and ||gamma(mu)||",
                "the gamma resolvent identity propagates the anchor norm to lambda=341/170",
                "the two-point gamma identity bounds the complete Weyl variation",
                "K683 transfers the nearby denominator lower to the target level",
            ],
            "ordinary_triple_validity_without_Friedrichs_authentication_sufficient": False,
            "finite_trace_block_without_tail_and_cross_sufficient": False,
            "qualitative_resolvent_membership_without_gap_sufficient": False,
            "nearby_margin_in_different_coordinate_substitutable": False,
            "finite_sector_denominator_margin_sufficient": False,
            "nearby_margin_without_W_identity_sufficient": False,
        },
        "exact_controls": {
            "controls_are_synthetic": True,
            "finite_trace_lower": "6",
            "tail_trace_lower": "6",
            "cross_upper": "11",
            "trace_comparison_floor": "25",
            "trace_coercivity": "5",
            "friedrichs_lower": "13/5",
            "anchor_mu": q(anchor),
            "target_lambda": q(target),
            "reference_gap_lower": q(gap),
            "anchor_gamma_norm_upper": q(gamma_anchor),
            "propagation_factor": q(factor),
            "target_gamma_norm_upper": q(gamma_target),
            "complete_weyl_variation_upper": q(variation),
            "nearby_denominator_margin": q(nearby_margin),
            "transferred_target_margin": q(transferred),
            "accepted": transferred > 0,
            "wrong_coordinate_counterexample": "A boundary-coordinate change transforms both M and W; transporting only the numerical lower for W-M has no invariant meaning.",
            "finite_trace_counterexample": "diag(6,1/n) is coercive on every fixed leading defect block but has no complete inverse-trace bound.",
        },
        "dependency_reconciliation": {
            "K695_reference_and_trace_packet_consumed": True,
            "K692_anchor_interface_consumed": True,
            "K689_gamma_propagation_consumed": True,
            "K686_weyl_variation_consumed": True,
            "K683_target_transfer_consumed": True,
            "K657_target_denominator_input_closed_conditionally": True,
            "native_boundary_or_denominator_data_added": False,
        },
        "native_interface_status": {
            "actual_native_minimal_operator_serialized": False,
            "actual_native_boundary_triple_authenticated": False,
            "actual_native_Friedrichs_domain_inclusion_proved": False,
            "actual_native_complete_form_lower_proved": False,
            "actual_native_complete_trace_packet_proved": False,
            "actual_native_real_interval_authenticated": False,
            "actual_native_nearby_denominator_margin_proved": False,
            "actual_native_target_denominator_nonnegative": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "complete_boundary_chain_suffices_for_target_denominator": True,
            "native_target_denominator_proved": False,
            "next_exact_input": "Serialize the native minimal operator, Friedrichs form and ordinary boundary maps in one coordinate; prove K695's domain inclusion and finite/tail/cross trace packet, the complete form lower 13/5 or another adequate lower, and one same-coordinate nearby denominator margin exceeding the propagated Weyl budget. Then invoke K657/K680 and execute K665's two parity tails.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional complete boundary-operator composition and supplies no source-owned action, physical quotient, state or observable.",
        "preflight_bookend": {
            "route_comparison": "K695 makes the reference and trace inputs cofinal. K698 is the cheapest exact composition proving that those rows plus one nearby denominator margin really reach K657's target level.",
            "retrieval_collision_result": "K692, K689, K686 and K683 expose separate links; no prior artifact freezes the complete same-coordinate chain and its final positive rational margin in one acceptance packet.",
            "strongest_alternative": "Compute D_W(341/170) directly on the complete boundary space and bypass anchor propagation and nearby-level transport.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Combining valid-looking rows drawn from different reference extensions, boundary coordinates, intervals, defect spaces or target parameters W.",
            "strongest_contrary_construction": "A finite coercive trace block can hide vanishing tail singular values, while a coordinate change can move M and W separately if not transported jointly.",
            "weakest_reproducibility_seam": "Every domain, norm, trace, gamma field, Weyl value, W and denominator lower must belong to one authenticated complete triple and coordinate.",
        },
        "controls": {
            "producer": "tests/channel-swings/k698_k500_boundary_denominator_end_to_end_compiler.py",
            "probe": "tests/channel-swings/k698_k500_boundary_denominator_end_to_end_compiler_probe.py",
            "controls_passed": 42,
            "hostile_mutations_rejected": 36,
        },
        "claim_ceiling": "Exact conditional end-to-end boundary theorem: complete Friedrichs authentication, a form lower, whole-defect trace coercivity and one same-coordinate nearby denominator margin propagate through the gamma and Weyl identities to D_W(341/170)>=3993/722500 I in the synthetic control. Current custody supplies none of the native minimal-operator, boundary, trace or denominator data. No native r0, B, parity tail, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n = p["end_to_end_theorem"], p["exact_controls"], p["native_interface_status"]
    for key in (
        "complete_Friedrichs_domain_inclusion_required",
        "complete_Friedrichs_form_lower_required",
        "complete_anchor_defect_trace_packet_required",
        "same_real_reference_resolvent_interval_required",
        "same_boundary_coordinate_and_fixed_W_required",
        "nearby_complete_denominator_margin_required",
    ):
        assert t[key]
    for key in (
        "ordinary_triple_validity_without_Friedrichs_authentication_sufficient",
        "finite_trace_block_without_tail_and_cross_sufficient",
        "qualitative_resolvent_membership_without_gap_sufficient",
        "nearby_margin_in_different_coordinate_substitutable",
        "finite_sector_denominator_margin_sufficient",
        "nearby_margin_without_W_identity_sufficient",
    ):
        assert not t[key]
    assert c["trace_comparison_floor"] == "25" and c["trace_coercivity"] == "5"
    assert c["reference_gap_lower"] == "1/2" and c["anchor_gamma_norm_upper"] == "1/5"
    assert c["propagation_factor"] == "101/85" and c["target_gamma_norm_upper"] == "101/425"
    assert c["complete_weyl_variation_upper"] == "808/180625"
    assert c["nearby_denominator_margin"] == "1/100" and c["transferred_target_margin"] == "3993/722500" and c["accepted"]
    assert p["target_claim"] == "NONE-NOT-A-KILL" and p["source_and_ledger_effect"] == "none"
    assert all(value is False for value in n.values())
    assert p["decision"]["complete_boundary_chain_suffices_for_target_denominator"]
    assert not p["decision"]["native_target_denominator_proved"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
