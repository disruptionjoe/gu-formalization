#!/usr/bin/env python3
"""Audit support preservation and the remaining numerical boundary after K305."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K280 = ROOT / "lab/process/k280-order-seven-bessel-vandermonde-face-atlas.json"
K294 = ROOT / "lab/process/k294-order-seven-global-radial-simplex-atlas.json"
K296 = ROOT / "lab/process/k296-order-seven-coalescent-face-valuation-atlas.json"
K300 = ROOT / "lab/process/k300-order-seven-angular-method-selection.json"
K302 = ROOT / "lab/process/k302-order-seven-split-weighted-peano-jet.json"
K304 = ROOT / "lab/process/k304-order-seven-peano-norm-sufficiency-audit.json"
K305 = ROOT / "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json"
OUTPUT = ROOT / "lab/process/k306-order-seven-joint-template-support-audit.json"


def build() -> dict[str, Any]:
    k280 = json.loads(K280.read_text())
    k294 = json.loads(K294.read_text())
    k296 = json.loads(K296.read_text())
    k300 = json.loads(K300.read_text())
    k302 = json.loads(K302.read_text())
    k304 = json.loads(K304.read_text())
    k305 = json.loads(K305.read_text())

    face_rows = k300["face_transfer"]["projective_face_second_derivative_margins"]
    codim_one = [row for row in face_rows if row["codimension"] == 1]
    codim_two = [row for row in face_rows if row["codimension"] == 2]
    if len(codim_one) != 6 or len(codim_two) != 15:
        raise AssertionError("K300 face cover changed")
    if {row["minimum_native_cauchy_companion_valuation"] for row in codim_one} != {2}:
        raise AssertionError("one-gap valuation changed")
    if not k305["coupling_preservation"]["size_four_determinant_kept_joint"]:
        raise AssertionError("K305 detached the common determinant")

    return {
        "schema_version": "1.0",
        "result_id": "K306-ORDER-SEVEN-JOINT-TEMPLATE-SUPPORT-AUDIT",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k280-order-seven-bessel-vandermonde-face-atlas.json",
                "lab/process/k294-order-seven-global-radial-simplex-atlas.json",
                "lab/process/k296-order-seven-coalescent-face-valuation-atlas.json",
                "lab/process/k300-order-seven-angular-method-selection.json",
                "lab/process/k302-order-seven-split-weighted-peano-jet.json",
                "lab/process/k304-order-seven-peano-norm-sufficiency-audit.json",
                "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json",
            ],
            "one_gap_faces": len(codim_one),
            "codimension_two_faces": len(codim_two),
            "endpoint_rows": len(k300["endpoint_integrability"]["rows"]),
            "master_functionals": k305["template_compression"]["new_group_axis_order_master_functionals"],
        },
        "support_preservation": {
            "common_size_four_factorization": k280["factorization_certificate"]["bessel_identity"],
            "left_vandermonde": k296["valuation_rule"]["common_size_four_left_vandermonde"],
            "right_vandermonde": k296["valuation_rule"]["common_size_four_right_vandermonde"],
            "native_global_chart": k294["global_chart"]["definition"],
            "native_density": k294["global_chart"]["transformed_native_density"],
            "bordered_master": k305["coupling_preservation"]["complete_integrand_master"],
            "one_gap_native_plus_cauchy_valuation": sorted({row["minimum_native_cauchy_companion_valuation"] for row in codim_one}),
            "worst_projective_second_derivative_margin": min(row["second_derivative_integrability_margin"] for row in face_rows),
            "worst_endpoint_second_derivative_margin": min(row["second_derivative_integrability_margin"] for row in k300["endpoint_integrability"]["rows"]),
            "why_k305_preserves_the_cover": "K305 is an exact algebraic regrouping before absolute value. It does not divide by a gap, remove D4, replace M by a pointwise supremum, or move the split variables outside the bordered determinant.",
            "qualitative_global_remainder_finite": k300["global_legality"]["qualitative_global_remainder_finite"],
        },
        "numerical_closure_audit": {
            "k304_failure_removed_as_a_formula": True,
            "meaning": "the detached terminal-cofactor supremum is no longer part of the compiled functional",
            "radial_integrability_numerically_certified": False,
            "reason": "exact regrouping preserves the zeros whose loss caused K304, but no outward bound for the regularized D4 times bordered-B5 product has yet been integrated over the complete q/projective/split cover",
            "required_operator": "one interval evaluator for D4*det(B_G) and its first/second complete-column replacements on the K296/K300 finite boundary cover, retaining the exact exponential and Cauchy denominators",
            "composition_order": [
                "regularize the common D4 Vandermonde factors and bordered determinant jointly on each face chart",
                "enclose the 1,160 compiled master slots with coherent group absolute values only after assembly",
                "integrate projective and q variables with exact exponential weight",
                "extract an x-only coefficient only after the preceding integral is finite",
                "join K294 low/middle/high gamma strata",
            ],
            "forbidden_shortcuts": [
                "K302 marginal times detached cofactor supremum",
                "K290 superseded pointwise bank",
                "absolute values on six occurrence patterns before bordered assembly",
                "q integration after discarding Cauchy--Vandermonde denominators",
            ],
            "k302_role": k305["coupling_preservation"]["k302_terminal_bounds_role"],
        },
        "route_comparison": {
            "positive_peano": {
                "status": "selected_with_exact_coherent_master_compiler",
                "master_functionals": k305["template_compression"]["new_group_axis_order_master_functionals"],
                "column_replacement_slots": k305["complete_counts"]["coherent_master_column_replacement_slots"],
                "remaining_new_proof": "outward interval constants and integrated q/projective bounds",
            },
            "analytic_subtraction": k300["method_comparison"]["analytic_subtraction"],
            "selection": "positive_peano",
            "selection_reason": "K305 removes the six-pattern duplication exactly and preserves the already-proved finite cover; subtraction still needs eight singular coefficient functions, overlap ownership and a fourth-derivative residual proof.",
        },
        "decision": {
            "eighteen_y_templates_closed_algebraically": True,
            "ninety_gap_templates_closed_algebraically": True,
            "complete_support_cover_preserved": True,
            "complete_numerical_norms_emitted": False,
            "k294_gamma_join_released": False,
            "analytic_subtraction_promoted": False,
            "next_exact_input": "implement the joint regularized D4-times-bordered-B5 interval evaluator on the six one-gap, fifteen codimension-two and three endpoint chart classes; start with the y master because D4 is y-independent, then reuse the same operator for the five gap axes",
        },
        "release_test": {
            "all_face_rows_replayed": len(face_rows) == 21,
            "all_endpoint_rows_replayed": len(k300["endpoint_integrability"]["rows"]) == 3,
            "worst_margins_positive": min(row["second_derivative_integrability_margin"] for row in face_rows) > 0 and min(row["second_derivative_integrability_margin"] for row in k300["endpoint_integrability"]["rows"]) > 0,
            "k304_bad_factorization_absent": True,
            "qualitative_finiteness_preserved": k300["global_legality"]["qualitative_global_remainder_finite"],
            "numerical_norm_overclaim": False,
            "radial_gamma_join_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k302["ledger_effect"],
        "claim_ceiling": "Exact support and route audit for K305's coherent bordered-determinant compiler. The algebraic compression preserves K296/K300's six one-gap, fifteen codimension-two and three endpoint chart classes, including positive second-derivative integrability margins, and removes K304's detached-cofactor formula from the compiled route. It does not supply outward constants for D4 times the bordered determinant, a numerical Peano norm, q/projective integral, K294 gamma join, exterior action-column value, residual, native K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["one_gap_faces"], fixed["codimension_two_faces"], fixed["endpoint_rows"]) != (6, 15, 3):
        raise AssertionError("boundary cover changed")
    support = payload["support_preservation"]
    if support["one_gap_native_plus_cauchy_valuation"] != [2]:
        raise AssertionError("common one-gap zero was lost")
    if support["worst_projective_second_derivative_margin"] <= 0 or support["worst_endpoint_second_derivative_margin"] <= 0:
        raise AssertionError("positive integrability margin was lost")
    if not support["qualitative_global_remainder_finite"]:
        raise AssertionError("qualitative finiteness was lost")
    decision = payload["decision"]
    if decision["complete_numerical_norms_emitted"] or decision["k294_gamma_join_released"] or decision["analytic_subtraction_promoted"]:
        raise AssertionError("route or numerical overclaim")
    if payload["release_test"]["native_K152_interval_emitted"]:
        raise AssertionError("native K152 overclaim")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
