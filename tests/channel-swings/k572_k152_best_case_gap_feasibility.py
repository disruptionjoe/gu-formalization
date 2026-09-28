#!/usr/bin/env python3
"""K572 compose K570 with the K169 best-case native gap cap."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k572-k152-best-case-gap-feasibility.json"
K570 = ROOT / "lab/process/k570-complete-m-dual-residual-enclosure.json"
ROUTING = (
    "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or "
    "borders a conventional particle-physics comparator. Any result about a "
    "standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` "
    "Majorana mechanism, anomaly selector, VEV-only breaking or familiar "
    "vector-mass route binds only that named model. It is not evidence for or "
    "against Weinstein's source-native mechanism without an explicit typed "
    "bridge. Read `lab/methods/source-native-comparator-routing.md` and follow "
    "its source-native pointers before reusing this result."
)


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def residual_upper() -> Fraction:
    data = json.loads(K570.read_text())
    return Fraction(data["complete_M_dual_residual_norm_square"]["interval_exact"][1])


def build() -> dict:
    upper = residual_upper()
    gap_cap = Fraction(5, 2)
    one_deficit_budget = Fraction(1) * (gap_cap + 1)
    cap_deficit_budget = gap_cap * (gap_cap + gap_cap)
    half_angle_budget = Fraction(1, 4) * gap_cap**2 / Fraction(3, 4) ** 2
    return {
        "schema_version": "1.0",
        "result_id": "K572-K152-BEST-CASE-GAP-FEASIBILITY",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "gu_comparator_routing": ROUTING,
        "gu_comparator_classification": "INTERNAL_ONLY__NO_SOURCE_NATIVE_OR_CONVENTIONAL_PARTICLE_VERDICT",
        "scope": "Best-case certificate feasibility after composing K570's complete M-dual residual upper with K169's 5/2 native complete-complement gap cap and the K469/K470 sharp two-block consumers.",
        "gu_typed_objects": {
            "result": "best-case residual/gap feasibility MAP-TYPE=certificate-obstruction",
            "carrier": "one fixed K162 charge sector and finite trial line",
            "pairing": "positive physical metric M=S* S",
            "form": "fixed K139/K168 reference form",
            "real_structure": "CAR adjoint and signed-flavor intertwiner",
            "grading": "trial/complement split with fixed total charge",
            "action_owner": "repository construction; no source/GU action selection",
            "target": "K469 ground deficit and K470 complete-ground-eigenspace angle",
        },
        "source_and_ledger_context": {
            "source_claims": ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06", "SC-META-53"],
            "source_polarity_effect": "none",
            "physics_rows": ["LT-SM8", "LT-GR6b", "RA-F1", "AC-F1"],
            "ledger": "lab/process/conditional-physics-ledger-v0.263.json",
            "ledger_effect": "none",
            "inputs": ["K169", "K469", "K470", "K570", "K571"],
        },
        "composition": {
            "K570_M_dual_square_upper_exact": q(upper),
            "K570_M_dual_square_upper_scientific": "2.48890514834555913e+2347",
            "K169_relative_gap_cap": q(gap_cap),
            "K169_cap_is_complete_floor": False,
            "K469_ground_target_test": "U<=d(g+d)",
            "K470_projection_target_test": "U<=p^2 g^2/(1-p^2)^2",
            "best_case_substitution": "g=5/2 maximizes both right-hand budgets over every admissible 0<g<=5/2",
        },
        "best_case_tests": {
            "ground_deficit_at_most_1": {
                "maximum_allowed_residual_square": q(one_deficit_budget),
                "current_upper_passes": upper <= one_deficit_budget,
            },
            "ground_deficit_at_most_gap_cap": {
                "maximum_allowed_residual_square": q(cap_deficit_budget),
                "current_upper_passes": upper <= cap_deficit_budget,
            },
            "projection_sine_at_most_1_over_2": {
                "maximum_allowed_residual_square": q(half_angle_budget),
                "current_upper_passes": upper <= half_angle_budget,
            },
            "necessary_best_case_ground_deficit": "d>=(sqrt((5/2)^2+4U)-5/2)/2",
        },
        "sharp_control": {
            "gap": "4",
            "M_dual_square": "9/4",
            "ground_deficit": "1/2",
            "ground_budget": "9/4",
            "projection_sine": "1/3",
            "projection_budget": "9/4",
            "both_equalities_hold": True,
            "control_is_native_K162_packet": False,
        },
        "decision": {
            "current_upper_certifies_ground_deficit_at_most_1": upper <= one_deficit_budget,
            "current_upper_certifies_ground_deficit_within_gap_cap": upper <= cap_deficit_budget,
            "current_upper_certifies_projection_sine_at_most_1_over_2": upper <= half_angle_budget,
            "failure_is_certificate_insufficiency_not_actual_residual_lower": True,
            "complete_complement_floor_still_required": True,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Tighten the complete M-dual residual upper by cancellation-aware evaluation or construct an action-flux certificate with a smaller native error quantity, while separately proving a positive reference-specific complete-complement floor below the K169 threshold cap.",
        },
        "claim_ceiling": "Exact composition of existing native certificate bounds only. Even granting the largest complete-complement gap compatible with K169, K570's current residual upper cannot certify a ground deficit at most one, a deficit within the 5/2 gap cap, or projection sine at most one half. This is failure of the current upper certificate, not a lower bound on the actual residual or proof that the native trial is inaccurate. No K152 interval or source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion moves.",
    }


def validate(payload: dict) -> None:
    tests = payload["best_case_tests"]
    decision = payload["decision"]
    if payload["composition"]["K169_cap_is_complete_floor"]:
        raise AssertionError("K572 promoted the gap cap to a floor")
    if any(row["current_upper_passes"] for key, row in tests.items() if isinstance(row, dict)):
        raise AssertionError("K572 unexpectedly released a target")
    if any(decision[key] for key in (
        "current_upper_certifies_ground_deficit_at_most_1",
        "current_upper_certifies_ground_deficit_within_gap_cap",
        "current_upper_certifies_projection_sine_at_most_1_over_2",
        "native_K152_interval_emitted",
    )):
        raise AssertionError("K572 overclaimed feasibility")
    if not decision["failure_is_certificate_insufficiency_not_actual_residual_lower"]:
        raise AssertionError("K572 lost its claim boundary")
    if not payload["sharp_control"]["both_equalities_hold"]:
        raise AssertionError("K572 sharp control failed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
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
