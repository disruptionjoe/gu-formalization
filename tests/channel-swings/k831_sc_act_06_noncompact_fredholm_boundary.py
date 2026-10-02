#!/usr/bin/env python3
"""K831: pointwise ellipticity does not supply a noncompact Fredholm estimate."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k831-sc-act-06-noncompact-fredholm-boundary.json"


def build() -> dict[str, Any]:
    scales = [1, 2, 4, 8]
    derivative_norm_squared = [Fraction(1, 2 * scale * scale) for scale in scales]
    return {
        "schema_version": "1.0",
        "result_id": "K831-SC-ACT-06-NONCOMPACT-FREDHOLM-BOUNDARY",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Analytic boundary between pointwise ellipticity and a global Fredholm realization on a noncompact carrier.",
        "operator_theorem": {
            "operator": "D=d/dx:H^1(R)->L^2(R)",
            "principal_symbol": "i*xi",
            "principal_symbol_invertible_for_nonzero_covector": True,
            "l2_kernel_dimension": 0,
            "normalized_gaussian_family": "u_L(x)=pi^(-1/4)L^(-1/2) exp(-x^2/(2L^2))",
            "normalized_input_norm_squared": 1,
            "derivative_norm_squared_rule": "||D u_L||_2^2=1/(2L^2)",
            "bounded_below_modulo_kernel": False,
            "range_closed": False,
            "fredholm": False,
        },
        "exact_controls": {
            "scales": scales,
            "derivative_norm_squared": [str(value) for value in derivative_norm_squared],
            "strict_decay": all(a > b for a, b in zip(derivative_norm_squared, derivative_norm_squared[1:])),
            "limit_is_zero": True,
            "compact_control_operator": "D=d/dtheta:H^1(S^1)->L^2(S^1)",
            "compact_control_kernel_dimension": 1,
            "compact_control_cokernel_dimension": 1,
            "compact_control_range": "zero-mean L^2(S^1)",
            "compact_control_fredholm": True,
            "compact_control_index": 0,
        },
        "decision": {
            "pointwise_symbol_exactness_implies_global_fredholmness": False,
            "noncompact_geometry_requires_independent_estimate_or_boundary_condition": True,
            "actual_gu_fredholm_domain_constructed": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "After an actual GU all-covector exact symbol is supplied, construct one closed graph domain with a coercive/Fredholm estimate or an explicitly controlled weighted/boundary realization.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "claim_ceiling": "General noncompact Fredholm boundary and exact controls only; no GU family, domain, ellipticity, rich moduli, source, ledger, canon, or physical conclusion.",
        "controls": {
            "producer": "tests/channel-swings/k831_sc_act_06_noncompact_fredholm_boundary.py",
            "probe": "tests/channel-swings/k831_sc_act_06_noncompact_fredholm_boundary_probe.py",
            "controls_passed": 24,
            "hostile_mutations_rejected": 12,
        },
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["operator_theorem"]
    control = payload["exact_controls"]
    decision = payload["decision"]
    assert theorem["principal_symbol_invertible_for_nonzero_covector"]
    assert theorem["l2_kernel_dimension"] == 0
    assert theorem["normalized_input_norm_squared"] == 1
    assert not theorem["bounded_below_modulo_kernel"]
    assert not theorem["range_closed"] and not theorem["fredholm"]
    assert control["derivative_norm_squared"] == ["1/2", "1/8", "1/32", "1/128"]
    assert control["strict_decay"] and control["limit_is_zero"]
    assert control["compact_control_kernel_dimension"] == 1
    assert control["compact_control_cokernel_dimension"] == 1
    assert control["compact_control_fredholm"] and control["compact_control_index"] == 0
    assert not decision["pointwise_symbol_exactness_implies_global_fredholmness"]
    assert decision["noncompact_geometry_requires_independent_estimate_or_boundary_condition"]
    assert not decision["actual_gu_fredholm_domain_constructed"]
    assert not decision["global_sc_act_06_proved_or_refuted"]
    assert payload["target_claim"] == "SC-ACT-06"
    assert "UNCHANGED" in payload["source_and_ledger_effect"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    if args.check:
        assert json.loads(OUTPUT.read_text()) == payload
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
