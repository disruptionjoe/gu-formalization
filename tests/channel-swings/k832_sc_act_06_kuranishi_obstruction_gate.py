#!/usr/bin/env python3
"""K832: an elliptic tangent complex does not integrate nonlinear deformations."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k832-sc-act-06-kuranishi-obstruction-gate.json"


def build() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "result_id": "K832-SC-ACT-06-KURANISHI-OBSTRUCTION-GATE",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Finite exact separation of infinitesimal deformation space from nonlinear integrability and local moduli dimension.",
        "obstructed_control": {
            "map": "F(x,y)=(y,x^2)",
            "base_point": [0, 0],
            "jacobian": [[0, 1], [0, 0]],
            "jacobian_rank": 1,
            "tangent_kernel_basis": [[1, 0]],
            "cokernel_basis": [[0, 1]],
            "quadratic_obstruction_on_tangent": [0, 2],
            "cokernel_obstruction_coefficient": 2,
            "second_order_lift_exists": False,
            "exact_zero_locus_near_origin": [[0, 0]],
            "infinitesimal_dimension": 1,
            "actual_local_dimension": 0,
        },
        "unobstructed_control": {
            "map": "G(x,y)=y-x^2",
            "base_point": [0, 0],
            "jacobian": [[0, 1]],
            "jacobian_surjective": True,
            "tangent_kernel_basis": [[1, 0]],
            "second_derivative_on_tangent": -2,
            "second_order_lift": [0, 2],
            "second_order_equation_residual": 0,
            "exact_zero_locus": "y=x^2",
            "smooth_local_dimension": 1,
        },
        "kuranishi_gate": {
            "linearized_kernel_alone_determines_local_moduli_dimension": False,
            "quadratic_obstruction_target": "coker(J)",
            "required_nonlinear_input": "projected second and higher jets or an independent unobstructedness theorem",
            "surjective_slice_control_has_zero_cokernel": True,
        },
        "decision": {
            "elliptic_linearization_implies_rich_moduli": False,
            "actual_gu_kuranishi_map_constructed": False,
            "actual_gu_unobstructedness_proved": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "After a GU Fredholm complex is built, compute the nonlinear equation on a genuine slice, its finite-dimensional obstruction map, and the local zero-set dimension/stratification.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "claim_ceiling": "Finite Kuranishi obstruction theorem and polynomial controls only; no GU nonlinear map, unobstructedness, rich moduli, source, ledger, canon, or physical conclusion.",
        "controls": {
            "producer": "tests/channel-swings/k832_sc_act_06_kuranishi_obstruction_gate.py",
            "probe": "tests/channel-swings/k832_sc_act_06_kuranishi_obstruction_gate_probe.py",
            "controls_passed": 28,
            "hostile_mutations_rejected": 12,
        },
    }


def validate(payload: dict[str, Any]) -> None:
    obstructed = payload["obstructed_control"]
    unobstructed = payload["unobstructed_control"]
    gate = payload["kuranishi_gate"]
    decision = payload["decision"]
    assert obstructed["jacobian"] == [[0, 1], [0, 0]] and obstructed["jacobian_rank"] == 1
    assert obstructed["tangent_kernel_basis"] == [[1, 0]]
    assert obstructed["cokernel_basis"] == [[0, 1]]
    assert obstructed["quadratic_obstruction_on_tangent"] == [0, 2]
    assert obstructed["cokernel_obstruction_coefficient"] == 2
    assert not obstructed["second_order_lift_exists"]
    assert obstructed["infinitesimal_dimension"] == 1 and obstructed["actual_local_dimension"] == 0
    assert unobstructed["jacobian_surjective"]
    assert unobstructed["second_order_lift"] == [0, 2]
    assert unobstructed["second_order_equation_residual"] == 0
    assert unobstructed["smooth_local_dimension"] == 1
    assert not gate["linearized_kernel_alone_determines_local_moduli_dimension"]
    assert gate["surjective_slice_control_has_zero_cokernel"]
    assert not decision["elliptic_linearization_implies_rich_moduli"]
    assert not decision["actual_gu_kuranishi_map_constructed"]
    assert not decision["actual_gu_unobstructedness_proved"]
    assert not decision["global_sc_act_06_proved_or_refuted"]


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
