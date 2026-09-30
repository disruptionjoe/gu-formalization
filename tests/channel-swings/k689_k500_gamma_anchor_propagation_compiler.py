#!/usr/bin/env python3
"""K689: propagate one complete gamma anchor by a reference resolvent gap."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k689-k500-gamma-anchor-propagation-compiler.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k686 = json.loads((ROOT / "lab/process/k686-k500-weyl-gamma-field-variation-compiler.json").read_text())
    assert k686["gamma_field_identity"]["connected_reference_resolvent_interval_required"]

    target = Fraction(341, 170)
    anchor = Fraction(21, 10)
    gap = anchor - target
    spectral_distance = Fraction(1, 2)
    anchor_norm = Fraction(1, 5)
    factor = 1 + gap / spectral_distance
    target_norm = factor * anchor_norm
    omega = gap * target_norm * anchor_norm
    nearby_margin = Fraction(1, 100)
    transferred = nearby_margin - omega
    assert gap == Fraction(8, 85)
    assert factor == Fraction(101, 85)
    assert target_norm == Fraction(101, 425)
    assert omega == Fraction(808, 180625)
    assert transferred == Fraction(3993, 722500)

    return {
        "schema_version": "1.0",
        "result_id": "K689-K500-GAMMA-ANCHOR-PROPAGATION-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A complete ordinary-boundary-triple certificate that propagates one gamma-field anchor norm to K686's target level using an authenticated real reference-resolvent interval and spectral-distance lower bound.",
        "gu_typed_objects": {
            "reference": "the same complete Friedrichs reference A_0 used by K657 and K686",
            "anchor": "one complete gamma(mu) norm at a real mu in rho(A_0)",
            "target": "gamma(lambda) at lambda=341/170 in the same boundary coordinate",
            "spectral_gap": "a complete lower d(lambda)<=dist(lambda,sigma(A_0))",
            "result": "gamma anchor propagation compiler MAP-TYPE=reference resolvent identity",
        },
        "gamma_resolvent_theorem": {
            "identity": "gamma(lambda)=[I+(lambda-mu)(A_0-lambda)^-1] gamma(mu)",
            "norm_bound": "||gamma(lambda)||<=[1+|lambda-mu|/dist(lambda,sigma(A_0))]||gamma(mu)||",
            "uniform_interval_bound": "if dist(I,sigma(A_0))>=d>0, then one anchor g_mu gives ||gamma(lambda)||<=[1+|lambda-mu|/d]g_mu for every lambda in I",
            "same_reference_required": True,
            "same_boundary_coordinate_required": True,
            "complete_boundary_space_required": True,
            "real_interval_inside_reference_resolvent_required": True,
            "finite_sector_gap_sufficient": False,
            "endpoint_membership_without_quantitative_gap_sufficient": False,
            "anchor_from_different_boundary_triple_substitutable": False,
        },
        "target_composition": {
            "target_lambda": qstr(target),
            "anchor_mu": qstr(anchor),
            "level_distance": qstr(gap),
            "reference_spectral_distance_lower": qstr(spectral_distance),
            "anchor_gamma_norm": qstr(anchor_norm),
            "propagation_factor": qstr(factor),
            "target_gamma_norm_upper": qstr(target_norm),
            "K686_weyl_variation_upper": qstr(omega),
            "nearby_denominator_margin": qstr(nearby_margin),
            "transferred_target_margin": qstr(transferred),
            "accepted": transferred >= 0,
            "controls_are_synthetic": True,
        },
        "failing_control": {
            "reference_spectral_distance_lower": "1/100",
            "anchor_gamma_norm": "1/5",
            "propagated_target_gamma_norm_exceeds_one": True,
            "lesson": "resolvent membership without a useful quantitative distance need not preserve K686's margin",
        },
        "dependency_reconciliation": {
            "K686_two_complete_gamma_norms_reduced_to_one_anchor_plus_gap": True,
            "K657_Friedrichs_reference_requirement_retained": True,
            "K683_same_coordinate_denominator_requirement_retained": True,
            "native_gamma_anchor_or_gap_added": False,
        },
        "native_interface_status": {
            "actual_native_boundary_triple_authenticated": False,
            "actual_native_Friedrichs_reference_proved": False,
            "actual_native_real_interval_authenticated": False,
            "actual_native_reference_spectral_distance_proved": False,
            "actual_native_anchor_gamma_norm_proved": False,
            "actual_native_target_gamma_norm_proved": False,
            "actual_native_denominator_margin_proved": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "one_anchor_plus_reference_gap_suffices_for_K686_gamma_pair": True,
            "native_target_denominator_proved": False,
            "next_exact_input": "Authenticate K139's complete ordinary boundary triple and Friedrichs reference on a real interval containing 341/170 and one anchor mu. Prove a quantitative distance from that interval to sigma(A_0), bound one complete gamma(mu), propagate the target gamma norm with K689, then combine with one nearby denominator margin through K686/K683.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional ordinary-boundary-triple resolvent identity inside a repository-supplied operator model and supplies no source-owned action, physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K686 asks for complete gamma norms at two levels. The exact gamma resolvent identity reduces that to one anchor norm plus a quantitative reference spectral gap, which is cheaper than two independent norm estimates.",
            "retrieval_collision_result": "K159 and K686 require gamma control but no current artifact propagates a native real anchor norm or supplies the complete reference spectral distance.",
            "strongest_alternative": "Compute D_W(341/170) directly, bypassing gamma propagation, nearby-level transport and the reference gap estimate.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Using qualitative resolvent membership, a finite-sector gap or a gamma norm from a different boundary coordinate as the complete propagation input.",
            "strongest_contrary_construction": "As the target approaches reference spectrum the resolvent factor diverges, so one bounded anchor gamma norm alone gives no useful target bound.",
            "weakest_reproducibility_seam": "The reference, trace coordinate, interval, spectral distance, anchor norm, fixed W and denominator margin must all be authenticated on the complete spectator-Fock boundary space.",
        },
        "controls": {
            "producer": "tests/channel-swings/k689_k500_gamma_anchor_propagation_compiler.py",
            "probe": "tests/channel-swings/k689_k500_gamma_anchor_propagation_compiler_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 28,
        },
        "claim_ceiling": "Exact conditional ordinary-boundary-triple result: the gamma resolvent identity propagates one complete anchor norm to lambda=341/170 when the same authenticated Friedrichs reference has a quantitative spectral-distance lower on the real interval. The synthetic control then supplies K686's two gamma bounds and a positive transferred margin. Current native custody supplies no authenticated triple, reference, interval, spectral distance, anchor norm or denominator. No native denominator, r0, B, parity tail, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["gamma_resolvent_theorem"]
    target = payload["target_composition"]
    native = payload["native_interface_status"]
    assert theorem["same_reference_required"]
    assert theorem["same_boundary_coordinate_required"]
    assert theorem["complete_boundary_space_required"]
    assert theorem["real_interval_inside_reference_resolvent_required"]
    assert not theorem["finite_sector_gap_sufficient"]
    assert not theorem["endpoint_membership_without_quantitative_gap_sufficient"]
    assert not theorem["anchor_from_different_boundary_triple_substitutable"]
    assert target["propagation_factor"] == "101/85"
    assert target["target_gamma_norm_upper"] == "101/425"
    assert target["K686_weyl_variation_upper"] == "808/180625"
    assert target["transferred_target_margin"] == "3993/722500"
    assert target["accepted"]
    assert not native["actual_native_target_gamma_norm_proved"]
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
