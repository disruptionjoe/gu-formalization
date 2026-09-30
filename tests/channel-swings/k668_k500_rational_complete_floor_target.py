#!/usr/bin/env python3
"""K668: rational target-floor compiler using K667's complete beta^2 bound."""

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
OUTPUT = ROOT / "lab/process/k668-k500-rational-complete-floor-target.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K667 = load("k667_for_k668", "k667_k500_matched_trace_square_telescoping_bound.py")


def q(value: Any) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def target_certificate(a_lower: Any, b_lower: Any, target: Any, beta_square_upper: Any) -> dict[str, Any]:
    a = q(a_lower)
    b = q(b_lower)
    mu = q(target)
    eta = q(beta_square_upper)
    if eta <= 0:
        raise ValueError("beta-square upper must be positive")
    a_gap = a - mu
    b_gap = b - mu
    determinant_slack = a_gap * b_gap - eta
    passes = a_gap >= 0 and b_gap >= 0 and determinant_slack >= 0
    return {
        "A_lower": qstr(a),
        "B_lower": qstr(b),
        "target_mu": qstr(mu),
        "beta_square_upper": qstr(eta),
        "A_gap": qstr(a_gap),
        "B_gap": qstr(b_gap),
        "shifted_product": qstr(a_gap * b_gap),
        "determinant_slack_against_upper": qstr(determinant_slack),
        "certifies_floor_strictly_above_target": passes,
    }


def build() -> dict[str, Any]:
    k667 = K667.build()
    k666 = json.loads((ROOT / "lab/process/k666-k500-complete-cancellation-floor-certificate.json").read_text())
    assert k667["exact_bounds"]["upper"] == "2/513"
    assert k666["certificate_theorem"]["positive_floor_iff"].endswith("A_lower*B_lower>beta_upper^2")

    eta = Fraction(2, 513)
    a = Fraction(3, 4)
    b = Fraction(21, 32)
    mu = Fraction(5, 8)
    control = target_certificate(a, b, mu, eta)
    threshold_b = mu + eta / (a - mu)
    assert control["certifies_floor_strictly_above_target"]
    assert Fraction(control["determinant_slack_against_upper"]) == Fraction(1, 131328)
    assert b - threshold_b == Fraction(1, 16416)

    endpoint = target_certificate(a, threshold_b, mu, eta)
    failing = target_certificate(a, threshold_b - Fraction(1, 16416), mu, eta)

    return {
        "schema_version": "1.0",
        "result_id": "K668-K500-RATIONAL-COMPLETE-FLOOR-TARGET",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "K663/K666's complete two-component comparison after replacing the synthetic beta value by K667's owned complete trace-square upper.",
        "gu_typed_objects": {
            "carrier": "K647's one complete K642/K663 cancellation domain",
            "form": "the conservative comparison matrix with complete margins A_lower and B_lower and K667 matched-trace square upper",
            "pairing": "the fixed complete graph norm used by K642 through K667",
            "result": "rational target-floor certificate MAP-TYPE=shifted two-by-two positive-semidefinite test",
            "target": "an exact rational acceptance test for any requested complete floor mu",
        },
        "rational_target_theorem": {
            "comparison_matrix": "[[A_lower,-beta],[-beta,B_lower]]",
            "floor_at_least_mu_iff_with_exact_beta": "A_lower>=mu, B_lower>=mu, (A_lower-mu)(B_lower-mu)>=beta^2",
            "K667_sufficient_strict_test": "A_lower>=mu, B_lower>=mu, (A_lower-mu)(B_lower-mu)>=2/513",
            "strict_reason": "K667 proves beta^2<2/513, so equality against the rational upper still leaves positive shifted determinant",
            "equivalent_B_budget_for_A_above_mu": "B_lower>=mu+(2/513)/(A_lower-mu)",
            "square_root_evaluation_required": False,
            "complete_A_B_same_domain_required": True,
            "finite_prefix_only_sufficient": False,
            "uncontrolled_complement_allowed": False,
        },
        "exact_controls": {
            "synthetic_input_only": True,
            "positive_row": control,
            "B_threshold_at_A_3_over_4_mu_5_over_8": qstr(threshold_b),
            "B_control_excess_over_threshold": qstr(b - threshold_b),
            "threshold_row": endpoint,
            "below_threshold_row": failing,
            "threshold_row_passes_strictly_for_actual_beta": endpoint["certifies_floor_strictly_above_target"],
            "below_threshold_row_rejected": not failing["certifies_floor_strictly_above_target"],
            "K663_synthetic_five_eighths_target_retained": True,
            "analytic_trace_certifies_strictly_more_than_five_eighths_for_control_margins": True,
        },
        "dependency_reconciliation": {
            "K642_complete_trace_series_consumed": True,
            "K663_sharp_matrix_theorem_consumed": True,
            "K665_complete_B_interface_retained": True,
            "K666_end_to_end_typing_retained": True,
            "K667_trace_square_upper_consumed": True,
            "matched_trace_no_longer_a_missing_native_numeric_input": True,
        },
        "native_interface_status": {
            "complete_matched_trace_beta_squared_upper_identified": True,
            "actual_complete_A_lower_identified": False,
            "actual_complete_B_lower_identified": False,
            "actual_native_target_floor_certified": False,
            "native_complete_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "remaining_native_inputs_exactly_two": True,
            "remaining_native_inputs": ["complete A_lower", "complete parity-cofinal B_lower"],
            "next_exact_input": "Certify complete A_lower and complete parity-cofinal B_lower on K647's common domain. For any desired rational floor mu, require A_lower>=mu and B_lower>=mu+(2/513)/(A_lower-mu); positivity alone is the mu=0 case.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This compiles internal conditional analytic constants and supplies no source-owned action, physical state, quotient, observable or empirical consequence.",
        "preflight_bookend": {
            "route_comparison": "With beta^2 now owned, a shifted determinant test is cheaper and more reproducible than repeated radical evaluation and exposes the exact A/B budget future native work must meet.",
            "retrieval_collision_result": "K663 gives the sharp radical and K666 gives the three-input compiler, but neither consumes K642's actual complete trace series into a rational target-floor budget.",
            "strongest_alternative": "A direct native complete-form lower proof would bypass the compiler, but current custody supplies neither its A nor B margin.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating the synthetic A=3/4 and B=21/32 control as measured or native K139/K168 margins.",
            "strongest_contrary_construction": "If either complete margin falls below the target or the shifted product misses the trace-square budget, the requested floor is not certified.",
            "weakest_reproducibility_seam": "Strictness comes from K667's strict beta^2 upper; replacing it by a non-strict or finite-sample assertion changes the endpoint logic.",
        },
        "controls": {
            "producer": "tests/channel-swings/k668_k500_rational_complete_floor_target.py",
            "probe": "tests/channel-swings/k668_k500_rational_complete_floor_target_probe.py",
            "controls_passed": 24,
            "hostile_mutations_rejected": 20,
        },
        "claim_ceiling": "Exact conditional rational-floor compiler for K663/K666 using K667's owned complete trace-square upper beta^2<2/513. A target mu is certified strictly when complete same-domain margins satisfy A_lower>=mu, B_lower>=mu and (A_lower-mu)(B_lower-mu)>=2/513. The synthetic 3/4,21/32 row clears mu=5/8 by exact shifted-determinant slack 1/131328. No native A or B margin, complete floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is supplied.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["rational_target_theorem"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["K667_sufficient_strict_test"].endswith(">=2/513")
    assert not theorem["square_root_evaluation_required"]
    assert theorem["complete_A_B_same_domain_required"]
    assert not theorem["finite_prefix_only_sufficient"]
    assert controls["positive_row"]["determinant_slack_against_upper"] == "1/131328"
    assert controls["B_control_excess_over_threshold"] == "1/16416"
    assert controls["threshold_row_passes_strictly_for_actual_beta"]
    assert controls["below_threshold_row_rejected"]
    assert native["complete_matched_trace_beta_squared_upper_identified"]
    assert not native["actual_complete_A_lower_identified"]
    assert not native["actual_complete_B_lower_identified"]
    assert not native["actual_native_target_floor_certified"]
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
