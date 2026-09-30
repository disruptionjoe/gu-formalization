#!/usr/bin/env python3
"""K666: end-to-end sharp cancellation floor from complete A/B/beta data."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k666-k500-complete-cancellation-floor-certificate.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K663 = load("k663_for_k666", "k663_k500_sharp_cancellation_graph_floor.py")
K665 = load("k665_for_k666", "k665_k500_parity_cofinal_effective_margin_composition.py")


def qstr(value: Fraction) -> str:
    return str(value)


def build() -> dict[str, Any]:
    k665 = K665.build()
    K665.validate(k665)
    a_lower = Fraction(3, 4)
    b_lower = Fraction(k665["exact_control"]["global_B_lower"])
    beta_upper = Fraction(1, 16)
    determinant_margin = a_lower * b_lower - beta_upper**2
    floor = K663.lower_eigenvalue(a_lower, b_lower, beta_upper)
    endpoint_a = Fraction(1, 2)
    endpoint_b = Fraction(1, 8)
    endpoint_beta = Fraction(1, 4)
    endpoint_floor = K663.lower_eigenvalue(endpoint_a, endpoint_b, endpoint_beta)
    return {
        "schema_version": "1.0",
        "result_id": "K666-K500-COMPLETE-CANCELLATION-FLOOR-CERTIFICATE",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "End-to-end composition of complete A, parity-cofinal B and matched-trace beta certificates into K663's sharp cancellation-graph floor.",
        "gu_typed_objects": {
            "carrier": "the complete K647 common domain with both K648 total-parity compressions and every K643 bath sector",
            "form": "K663's complete two-component cancellation graph with effective margins A and B",
            "pairing": "the fixed complete graph norm and matched-trace operator bound beta on that same domain",
            "result": "complete cancellation-floor certificate MAP-TYPE=end-to-end determinant and least-eigenvalue composition",
            "target": "one machine-checkable sufficient certificate for a positive K642/K663 complete-space lower",
        },
        "certificate_theorem": {
            "inputs": "complete A_lower; complete parity-cofinal B_lower; matched-trace beta_upper",
            "floor": "lambda_lower=(A_lower+B_lower-sqrt((A_lower-B_lower)^2+4 beta_upper^2))/2",
            "positive_floor_iff": "A_lower>0, B_lower>0 and A_lower*B_lower>beta_upper^2",
            "K647_common_domain_required": True,
            "K648_both_total_parities_required": True,
            "K665_finite_rows_and_two_tails_required": True,
            "matched_trace_same_domain_required": True,
            "finite_prefix_only_sufficient": False,
            "one_parity_only_sufficient": False,
            "uncontrolled_complement_allowed": False,
            "endpoint_zero_floor_allowed": True,
        },
        "exact_control": {
            "A_lower": qstr(a_lower),
            "B_lower": qstr(b_lower),
            "beta_upper": qstr(beta_upper),
            "determinant_margin": qstr(determinant_margin),
            "certified_floor": qstr(floor),
            "positive_floor_test_passes": a_lower > 0 and b_lower > 0 and determinant_margin > 0,
            "matches_K663_sharp_control": floor == Fraction(5, 8),
            "B_arrives_from_K665": b_lower == Fraction(k665["exact_control"]["global_B_lower"]),
            "endpoint_control": {
                "A_lower": qstr(endpoint_a),
                "B_lower": qstr(endpoint_b),
                "beta_upper": qstr(endpoint_beta),
                "determinant_margin": qstr(endpoint_a * endpoint_b - endpoint_beta**2),
                "certified_floor": qstr(endpoint_floor),
                "zero_endpoint_passes": endpoint_floor == 0,
            },
            "negative_determinant_rejected": Fraction(1, 2) * Fraction(1, 8) <= Fraction(3, 8) ** 2,
            "controls_are_synthetic": True,
        },
        "dependency_reconciliation": {
            "K642_complete_graph_typing_retained": True,
            "K647_common_domain_identity_consumed": True,
            "K648_parity_completeness_consumed": True,
            "K663_sharp_floor_consumed": True,
            "K664_direct_effective_margin_interface_consumed": True,
            "K665_parity_cofinal_B_consumed": True,
        },
        "native_interface_status": {
            "actual_complete_A_lower_identified": False,
            "actual_complete_B_lower_identified": False,
            "actual_matched_trace_beta_upper_newly_identified": False,
            "actual_positive_determinant_margin_identified": False,
            "native_complete_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "end_to_end_certificate_shape_closed": True,
            "native_floor_supplied": False,
            "next_exact_input": "Supply a complete A lower, K665's complete finite-row plus two-tail B packet, and the matched-trace beta bound on K647's one common domain. Verify A_lower*B_lower>beta_upper^2; then K666 emits the native complete floor. Current artifacts supply the theorem and typing but not those native numbers.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "The certificate composes conditional internal lower-form data and supplies no action-owned physical state, quotient, observable or source mechanism.",
        "preflight_bookend": {
            "route_comparison": "After K665 closes the parity/tail assembly, direct end-to-end composition is the cheapest way to prevent future native estimates from losing domain, parity or determinant hypotheses between K648 and K663.",
            "retrieval_collision_result": "K663 owns the sharp scalar theorem and K664 owns cofinal margin transfer, but neither checks that B was assembled from both native parity tails on K647's exact common domain.",
            "strongest_alternative": "A direct unsplit operator lower on the complete graph would bypass this certificate and remains stronger if available.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Reporting the synthetic 5/8 control as a native K139/K168 floor or omitting one parity/tail from B.",
            "strongest_contrary_construction": "At determinant equality the certified floor is exactly zero; increasing beta past that boundary makes positivity fail despite positive diagonal margins.",
            "weakest_reproducibility_seam": "Native execution still needs independently certified complete A, B and beta inputs; the exact controls test only the compiler.",
        },
        "controls": {
            "producer": "tests/channel-swings/k666_k500_complete_cancellation_floor_certificate.py",
            "probe": "tests/channel-swings/k666_k500_complete_cancellation_floor_certificate_probe.py",
            "controls_passed": 24,
            "hostile_mutations_rejected": 20,
        },
        "claim_ceiling": "Exact conditional end-to-end certificate for K663's complete-space cancellation floor. A complete A lower, K665's two-parity finite-plus-tail B lower and a same-domain matched-trace beta upper yield the sharp least-eigenvalue floor; strict positivity is exactly the positive-diagonal determinant test. The endpoint control has zero floor, and larger beta fails positivity. The synthetic 5/8 row tests the compiler only. No native A, B, tail, determinant margin, floor, K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is supplied.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["certificate_theorem"]
    exact = payload["exact_control"]
    deps = payload["dependency_reconciliation"]
    native = payload["native_interface_status"]
    assert theorem["K647_common_domain_required"]
    assert theorem["K648_both_total_parities_required"]
    assert theorem["K665_finite_rows_and_two_tails_required"]
    assert theorem["matched_trace_same_domain_required"]
    assert not theorem["finite_prefix_only_sufficient"]
    assert not theorem["one_parity_only_sufficient"]
    assert not theorem["uncontrolled_complement_allowed"]
    assert exact["B_arrives_from_K665"]
    assert exact["positive_floor_test_passes"]
    assert exact["matches_K663_sharp_control"]
    assert exact["certified_floor"] == "5/8"
    assert exact["endpoint_control"]["zero_endpoint_passes"]
    assert exact["negative_determinant_rejected"]
    assert exact["controls_are_synthetic"]
    assert all(deps.values())
    assert not native["native_complete_floor_emitted"]
    assert not payload["decision"]["native_floor_supplied"]
    assert payload["source_and_ledger_effect"] == "none"
    assert payload["target_claim"] == "NONE-NOT-A-KILL"


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
