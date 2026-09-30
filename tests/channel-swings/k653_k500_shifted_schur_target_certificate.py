#!/usr/bin/env python3
"""K653: exact shifted-Schur certificate for a prescribed lower target."""

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
OUTPUT = ROOT / "lab/process/k653-k500-shifted-schur-target-certificate.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K647 = load("k647_for_k653", "k647_k500_common_domain_flavor_intertwiner.py")
K650 = load("k650_for_k653", "k650_k500_parity_cancelled_core_lower_interface.py")
K652 = load("k652_for_k653", "k652_k500_all_order_parity_tail_certificate.py")


def scalar_target_test(a: Fraction, d: Fraction, c: Fraction, b: Fraction) -> dict[str, Any]:
    """Sharp real-symmetric 2-by-2 test after shifting by target b."""
    left = a - b
    right = d - b
    cross_square = c * c
    product = left * right
    passed = left >= 0 and right >= 0 and cross_square <= product
    theta_square = None if product <= 0 else cross_square / product
    return {
        "a": str(a), "d": str(d), "abs_c": str(c), "target_b": str(b),
        "left_gap": str(left), "right_gap": str(right),
        "cross_square": str(cross_square), "gap_product": str(product),
        "theta_square": None if theta_square is None else str(theta_square),
        "target_floor_certified": passed,
    }


def build() -> dict[str, Any]:
    k647 = K647.build()
    k650 = K650.build()
    k652 = K652.build()
    controls = {
        "strict_pass": scalar_target_test(Fraction(5), Fraction(9), Fraction(3), Fraction(3)),
        "endpoint_pass": scalar_target_test(Fraction(4), Fraction(7), Fraction(2), Fraction(3)),
        "excessive_cross_fail": scalar_target_test(Fraction(4), Fraction(7), Fraction(5, 2), Fraction(3)),
        "negative_shifted_diagonal_fail": scalar_target_test(Fraction(2), Fraction(5), Fraction(1), Fraction(3)),
    }
    return {
        "schema_version": "1.0",
        "result_id": "K653-K500-SHIFTED-SCHUR-TARGET-CERTIFICATE",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "An exact same-domain lower-target certificate for either K650 complete cancelled quadrant, stated after shifting by a proposed floor b.",
        "gu_typed_objects": {
            "carrier": "one K643 bath sector and one K648 total-parity sign",
            "form": "K650's complete cancellation-preserving two-quadrant form q",
            "domain": "one common K647 graph form domain J for both diagonal forms and the cross form",
            "target": "a prescribed sector floor b without separately serializing absolute A,D,K envelopes",
            "result": "shifted Schur target certificate MAP-TYPE=exact form inequality",
        },
        "shifted_schur_theorem": {
            "shifted_diagonal_hypotheses": "a[x]-b||x||^2>=0 and d[y]-b||y||^2>=0 on one common form domain",
            "cross_hypothesis": "|c[x,y]|<=theta*sqrt((a[x]-b||x||^2)(d[y]-b||y||^2)) with 0<=theta<=1",
            "conclusion": "q[x,y]>=b(||x||^2+||y||^2)",
            "proof_identity": "q-b||x,y||^2>=p_b+d_b-2*theta*sqrt(p_b*d_b)>=(1-theta)(p_b+d_b)>=0",
            "scalar_sharp_iff": "a>=b, d>=b, and |c|^2<=(a-b)(d-b)",
            "theta_endpoint_allowed": True,
            "same_domain_required": True,
            "separately_singular_raw_rows_required": False,
            "absolute_A_D_K_serialization_required": False,
        },
        "exact_controls": {
            "synthetic_not_native": True,
            **controls,
            "expected_pattern": [True, True, False, False],
            "observed_pattern": [row["target_floor_certified"] for row in controls.values()],
        },
        "decision": {
            "direct_target_route_closed_abstractly": True,
            "K652_absolute_envelope_route_remains_valid": k652["decision"]["constructive_all_order_route_closed_abstractly"],
            "native_target_floor_emitted": False,
            "next_exact_input": "Choose a native target b and prove the two shifted diagonal forms are nonnegative plus the shifted cross contraction on K647's common domain for every sector of both parity signs; then combine with the finite prefix and separately prove alpha,delta.",
        },
        "native_interface_status": {
            "K647_common_domain_consumed": bool(k647),
            "K650_cancelled_quadrant_interface_consumed": bool(k650),
            "shifted_target_certificate_shape_complete": True,
            "actual_native_target_b_identified": False,
            "actual_native_shifted_diagonal_positivity_proved": False,
            "actual_native_shifted_cross_contraction_proved": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is an abstract exact theorem for a conditional internal operator form; its scalar controls are synthetic and supply no action-owned quotient, state, observable or source mechanism.",
        "preflight_bookend": {
            "route_comparison": "K652's A,D,K route is sufficient but may serialize more absolute information than a concrete target test needs; shifting first preserves cancellation and asks only for positivity relative to b.",
            "retrieval_collision_result": "No existing artifact states the sharp target-relative same-domain criterion on K650's complete quadrants.",
            "strongest_alternative": "A direct spectral theorem for the fixed operator would be stronger, but a target-relative form argument is the shortest exact certificate when its native hypotheses can be proved.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating the synthetic target three as a native GU lower bound or assuming the shifted hypotheses from unshifted positivity.",
            "strongest_contrary_construction": "A negative shifted diagonal or cross square larger than the gap product defeats the target even when the unshifted block is positive.",
            "weakest_reproducibility_seam": "Native shifted form estimates are not serialized; the theorem closes only the exact proof shape.",
        },
        "claim_ceiling": "Exact same-domain shifted-Schur target theorem for one K650 complete cancelled quadrant. It gives a sharp scalar criterion and a cancellation-preserving form certificate at a prescribed b without requiring separately singular rows or prior absolute A,D,K serialization. No native target b, shifted positivity, shifted contraction, parity tail, m, alpha or delta is supplied. No K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["shifted_schur_theorem"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["theta_endpoint_allowed"] and theorem["same_domain_required"]
    assert not theorem["separately_singular_raw_rows_required"]
    assert controls["observed_pattern"] == controls["expected_pattern"]
    assert native["shifted_target_certificate_shape_complete"]
    assert not native["actual_native_target_b_identified"]


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
