#!/usr/bin/env python3
"""K670: asymmetric complete-B target after K669's conditional A transfer."""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k670-k500-asymmetric-native-margin-target.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K669 = load("k669_for_k670", "k669_k500_leakage_remainder_factorization_bridge.py")


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k669 = K669.build()
    k667 = json.loads(
        (ROOT / "lab/process/k667-k500-matched-trace-square-telescoping-bound.json").read_text()
    )
    assert k669["exact_bounds"]["conservative_rational_A_lower"] == "2/3"
    assert k667["exact_bounds"]["upper"] == "2/513"

    a_lower = Fraction(2, 3)
    b_threshold = Fraction(1, 171)
    b_target = Fraction(1, 170)
    beta_square_upper = Fraction(2, 513)
    determinant_slack = a_lower * b_target - beta_square_upper
    trace_corner = a_lower + b_target
    rational_floor = determinant_slack / trace_corner
    assert a_lower * b_threshold == beta_square_upper
    assert determinant_slack == Fraction(1, 43605)
    assert trace_corner == Fraction(343, 510)
    assert rational_floor == Fraction(2, 58653)

    return {
        "schema_version": "1.0",
        "result_id": "K670-K500-ASYMMETRIC-NATIVE-MARGIN-TARGET",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "K663's complete two-coordinate comparison under K669's conditional A>2/3 bridge and K667's strict beta^2<2/513 bound.",
        "gu_typed_objects": {
            "carrier": "K647's complete common cancellation domain across both K648 total parities and every K643 bath sector",
            "form": "the K663 comparison with conditional A>2/3 and a separately certified complete effective B margin",
            "pairing": "the same complete graph norm and matched trace used by K642 through K669",
            "result": "asymmetric native-margin target MAP-TYPE=rational two-by-two lower certificate",
            "target": "one concrete complete B threshold for K665's finite-plus-two-tail packet",
        },
        "asymmetric_target_theorem": {
            "conditional_A_input": "A>2/3 from K669 only after its native factorization bridge is proved",
            "complete_B_input": "B>=1/170 on the same domain, including every finite row and both parity tails",
            "matched_trace_input": "beta^2<2/513 from K667",
            "positivity_threshold_at_A_two_thirds": "B=1/171",
            "selected_rational_B_target": "1/170",
            "determinant_slack_against_trace_upper": "1/43605",
            "worst_corner_trace": "343/510",
            "strict_complete_floor": "lambda_->2/58653",
            "floor_argument": "lambda_min is monotone in the two diagonal lowers and decreasing in |beta|; at the conservative corner lambda_min=det/lambda_max>det/trace",
            "same_domain_required": True,
            "both_total_parity_tails_required": True,
            "finite_prefix_only_sufficient": False,
            "uncontrolled_complement_allowed": False,
        },
        "exact_controls": {
            "A_conservative": qstr(a_lower),
            "beta_square_upper": qstr(beta_square_upper),
            "zero_slack_B_threshold": qstr(b_threshold),
            "selected_B_target": qstr(b_target),
            "B_target_excess_over_threshold": qstr(b_target - b_threshold),
            "determinant_slack": qstr(determinant_slack),
            "trace_corner": qstr(trace_corner),
            "det_over_trace_floor": qstr(rational_floor),
            "strictness_sources": ["K669 conditional A>2/3", "K667 beta^2<2/513"],
            "synthetic_or_conditional_only": True,
        },
        "dependency_reconciliation": {
            "K609_complete_leakage_number_retained": True,
            "K663_sharp_comparison_consumed": True,
            "K665_complete_B_composition_retained": True,
            "K667_strict_trace_square_upper_consumed": True,
            "K668_rational_target_logic_sharpened_for_mu_zero": True,
            "K669_bridge_consumed_conditionally": True,
        },
        "native_interface_status": {
            "actual_K669_native_factorization_identified": False,
            "actual_complete_A_lower_identified": False,
            "actual_complete_B_lower_identified": False,
            "actual_finite_B_rows_identified": False,
            "actual_plus_minus_B_tails_identified": False,
            "native_complete_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "conditional_B_target_now_rational_and_explicit": True,
            "native_B_target_satisfied": False,
            "next_exact_input": "First prove K669's same-domain factorization or certify A directly. If A>2/3 is obtained, certify the complete effective B form at 1/170 through K665: every finite row through one N and independent plus/minus tail lowers. Those inputs would give a complete floor above 2/58653.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This conditionally reallocates internal analytic margin budgets and supplies no source-owned action, physical state, quotient, observable or empirical consequence.",
        "preflight_bookend": {
            "route_comparison": "Once K609 can supply A>2/3, the weakest useful next demand is not a symmetric large B margin but the exact determinant budget. The 1/170 target is a cheap rational certificate with explicit positive floor.",
            "retrieval_collision_result": "K668 gives the general A/B tradeoff, but no current artifact composes K609's possible A margin into a concrete parity-cofinal B target and rational floor.",
            "strongest_alternative": "A direct full-form lower proof bypasses the split target and remains stronger; K670 is the fail-closed sectorwise route when B evidence arrives through K665.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Reporting B>=1/170, A>2/3 or the 2/58653 floor as native before the K669 factorization and K665 complete rows/tails are proved.",
            "strongest_contrary_construction": "Hold every finite B row above 1/170 and place one uncontrolled parity-tail sector below it; the complete target and floor both fail.",
            "weakest_reproducibility_seam": "The determinant uses beta squared while the floor estimate uses determinant over trace at the conservative matrix corner; mixing beta with beta squared changes the result.",
        },
        "controls": {
            "producer": "tests/channel-swings/k670_k500_asymmetric_native_margin_target.py",
            "probe": "tests/channel-swings/k670_k500_asymmetric_native_margin_target_probe.py",
            "controls_passed": 24,
            "hostile_mutations_rejected": 20,
        },
        "claim_ceiling": "Exact conditional asymmetric margin target for K663. If K669's native factorization bridge is proved, then A>2/3; together with K667's beta^2<2/513, a complete same-domain B>=1/170 yields determinant slack above 1/43605 and a complete floor above 2/58653. The factorization, native A, finite B rows and both parity tails remain absent, so no native complete floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["asymmetric_target_theorem"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["positivity_threshold_at_A_two_thirds"] == "B=1/171"
    assert theorem["selected_rational_B_target"] == "1/170"
    assert theorem["determinant_slack_against_trace_upper"] == "1/43605"
    assert theorem["strict_complete_floor"] == "lambda_->2/58653"
    assert theorem["same_domain_required"]
    assert theorem["both_total_parity_tails_required"]
    assert not theorem["finite_prefix_only_sufficient"]
    assert not theorem["uncontrolled_complement_allowed"]
    assert controls["determinant_slack"] == "1/43605"
    assert controls["trace_corner"] == "343/510"
    assert controls["det_over_trace_floor"] == "2/58653"
    assert not native["actual_K669_native_factorization_identified"]
    assert not native["actual_complete_A_lower_identified"]
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
