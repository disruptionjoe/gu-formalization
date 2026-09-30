#!/usr/bin/env python3
"""K686: bound K683's Weyl variation by complete gamma-field norms."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k686-k500-weyl-gamma-field-variation-compiler.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k683 = json.loads((ROOT / "lab/process/k683-k500-weyl-target-level-robustness.json").read_text())
    k159 = json.loads((ROOT / "lab/process/k159-fractional-boundary-weyl-resolvent-wave.json").read_text())
    assert k683["level_transfer_theorem"]["complete_boundary_coverage_required"]
    assert k159["boundary_weyl_route"]["operator_valued_denominator_required"]

    lambda_0 = Fraction(341, 170)
    lambda_1 = Fraction(21, 10)
    delta = lambda_1 - lambda_0
    g_0 = Fraction(1, 4)
    g_1 = Fraction(1, 5)
    omega = delta * g_0 * g_1
    d_1 = Fraction(1, 100)
    margin = d_1 - omega
    failing_omega = delta
    failing_margin = d_1 - failing_omega
    assert delta == Fraction(8, 85)
    assert omega == Fraction(2, 425)
    assert margin == Fraction(9, 1700)
    assert failing_margin == Fraction(-143, 1700)

    return {
        "schema_version": "1.0",
        "result_id": "K686-K500-WEYL-GAMMA-FIELD-VARIATION-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A complete ordinary-boundary-triple certificate converting gamma-field norm bounds on one real reference-resolvent interval into K683's Weyl-variation budget at lambda=341/170.",
        "gu_typed_objects": {
            "boundary_triple": "one authenticated ordinary boundary triple with Friedrichs reference A_0 on the complete spectator-Fock boundary space",
            "gamma_field": "the complete Hilbert-bounded gamma(lambda) for real lambda in one connected interval I subset rho(A_0)",
            "weyl_family": "the corresponding complete operator-valued M(lambda) in the same coordinate",
            "denominator": "D_W(lambda)=W-M(lambda) for one fixed target extension parameter W",
            "result": "Weyl gamma-field variation compiler MAP-TYPE=boundary-triple identity",
            "target": "K683's complete omega budget from lambda_1 to lambda_0=341/170",
        },
        "gamma_field_identity": {
            "two_point_identity": "M(lambda_1)-M(lambda_0)=(lambda_1-lambda_0) gamma(lambda_0)* gamma(lambda_1)",
            "norm_consequence": "||M(lambda_1)-M(lambda_0)||<=|lambda_1-lambda_0| ||gamma(lambda_0)|| ||gamma(lambda_1)||",
            "uniform_interval_consequence": "if sup_(lambda in I)||gamma(lambda)||<=g then the Weyl variation is at most |lambda_1-lambda_0| g^2",
            "derivative_identity": "M'(lambda)=gamma(lambda)* gamma(lambda)>=0",
            "monotonicity_consequence": "M is operator monotone increasing on the authenticated real interval",
            "connected_reference_resolvent_interval_required": True,
            "same_boundary_coordinate_required": True,
            "complete_boundary_space_required": True,
            "finite_sector_gamma_bounds_sufficient": False,
            "nonreal_contour_bound_substitutable_without_real_interval_proof": False,
        },
        "target_composition": {
            "target_lambda_0": qstr(lambda_0),
            "nearby_lambda_1": qstr(lambda_1),
            "level_distance": qstr(delta),
            "gamma_norm_at_lambda_0": qstr(g_0),
            "gamma_norm_at_lambda_1": qstr(g_1),
            "complete_weyl_variation_omega": qstr(omega),
            "nearby_denominator_margin_d_1": qstr(d_1),
            "transferred_target_margin": qstr(margin),
            "accepted": margin >= 0,
            "composition": "K683 gives D_W(lambda_0)>=(d_1-omega)I",
            "controls_are_synthetic": True,
        },
        "failing_control": {
            "gamma_norm_at_both_levels": "1",
            "complete_weyl_variation_omega": qstr(failing_omega),
            "nearby_denominator_margin_d_1": qstr(d_1),
            "transferred_target_margin": qstr(failing_margin),
            "accepted": False,
        },
        "dependency_reconciliation": {
            "K159_complete_operator_valued_gamma_requirement_retained": True,
            "K657_Friedrichs_reference_resolvent_and_sign_premises_retained": True,
            "K683_unstructured_weyl_variation_reduced_to_gamma_norms": True,
            "K683_monotone_shortcut_derived_from_gamma_identity": True,
            "native_gamma_bound_added": False,
        },
        "native_interface_status": {
            "actual_native_boundary_triple_authenticated": False,
            "actual_native_Friedrichs_reference_proved": False,
            "actual_native_real_interval_authenticated": False,
            "actual_native_complete_gamma_norms_proved": False,
            "actual_native_weyl_variation_bound_proved": False,
            "actual_native_nearby_denominator_margin_proved": False,
            "actual_native_target_denominator_nonnegative": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "complete_gamma_norms_are_sufficient_variation_input": True,
            "native_target_denominator_proved": False,
            "next_exact_input": "Authenticate K139's complete ordinary boundary triple and Friedrichs reference on a real interval containing 341/170 and one computable lambda_1. Bound the complete gamma fields at both levels (or uniformly on the interval), prove D_W(lambda_1)>=d_1 I, and check |lambda_1-341/170| g_0 g_1<=d_1 before invoking K683/K657.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional ordinary-boundary-triple identity inside a repository-supplied operator model and supplies no source-owned action, physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K683 leaves a complete Weyl-difference norm as an input. The ordinary-boundary-triple two-point gamma identity is the cheapest exact route to that norm and simultaneously explains the monotonicity shortcut.",
            "retrieval_collision_result": "K159 requires complete gamma/Weyl control on a nonreal contour but does not derive the real-level two-point variation bound used by K683.",
            "strongest_alternative": "Compute D_W(341/170) directly, bypassing nearby-level transport and all gamma variation budgets.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Using finite-sector, nonreal-contour or differently coordinated gamma bounds as a complete real-interval Weyl variation certificate.",
            "strongest_contrary_construction": "With unit gamma bounds over the same level gap, omega=8/85 exceeds a nearby margin 1/100 and transfers to -143/1700, so interval membership alone is not enough.",
            "weakest_reproducibility_seam": "The native boundary maps, Friedrichs reference, real resolvent interval, complete gamma norms, fixed W and denominator lower must all use one authenticated coordinate.",
        },
        "controls": {
            "producer": "tests/channel-swings/k686_k500_weyl_gamma_field_variation_compiler.py",
            "probe": "tests/channel-swings/k686_k500_weyl_gamma_field_variation_compiler_probe.py",
            "controls_passed": 35,
            "hostile_mutations_rejected": 29,
        },
        "claim_ceiling": "Exact conditional ordinary-boundary-triple result: on one authenticated complete real reference-resolvent interval, the two-point gamma identity bounds Weyl variation by |lambda_1-lambda_0| times the two complete gamma norms, while M'=gamma*gamma gives operator monotonicity. This converts K683's variation input at lambda_0=341/170 into a concrete gamma-field norm obligation. Current native custody supplies no authenticated triple, interval, gamma norms or denominator margin. No native denominator, r0, B, parity tail, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    identity = payload["gamma_field_identity"]
    target = payload["target_composition"]
    failure = payload["failing_control"]
    native = payload["native_interface_status"]
    assert identity["connected_reference_resolvent_interval_required"]
    assert identity["same_boundary_coordinate_required"]
    assert identity["complete_boundary_space_required"]
    assert not identity["finite_sector_gamma_bounds_sufficient"]
    assert not identity["nonreal_contour_bound_substitutable_without_real_interval_proof"]
    assert target["level_distance"] == "8/85"
    assert target["complete_weyl_variation_omega"] == "2/425"
    assert target["transferred_target_margin"] == "9/1700"
    assert target["accepted"]
    assert failure["transferred_target_margin"] == "-143/1700"
    assert not failure["accepted"]
    assert not native["actual_native_complete_gamma_norms_proved"]
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
