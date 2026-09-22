#!/usr/bin/env python3
"""Rigorous zero-inclusive envelopes for K320's scaled Bessel jets."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K320 = ROOT / "lab/process/k320-order-seven-scaled-endpoint-bessel-bank.json"
OUTPUT = ROOT / "lab/process/k322-order-seven-zero-safe-scaled-bessel-envelopes.json"

ctx.dps = 120
ctx.threads = 1


def ball(value: Fraction) -> arb:
    return arb(f"{value.numerator}/{value.denominator}")


def exact_bounds(width: Fraction) -> list[Fraction]:
    # A=w*K1(w) obeys 0<A<=1 and B=w*K0(w) obeys 0<B<=A.
    return [
        Fraction(2),
        2 * (1 + width),
        4 + 2 * width + 2 * width * width,
    ]


def scaled_values(value: Fraction) -> list[arb]:
    w = ball(value)
    A = w * w.bessel_k(1)
    B = w * w.bessel_k(0)
    return [
        2 * A,
        -2 * (A + w * B),
        4 * A + 2 * w * B + 2 * w * w * A,
    ]


def row(width: Fraction) -> dict[str, Any]:
    bounds = exact_bounds(width)
    samples = sorted({width / 16, width / 4, width}) if width else []
    controls = []
    for sample in samples:
        values = scaled_values(sample)
        controls.append({
            "w": str(sample),
            "absolute_values": [repr(float(abs(value).upper())) for value in values],
            "inside_declared_bounds": [abs(value) <= ball(bound) for value, bound in zip(values, bounds)],
        })
    return {
        "width": str(width),
        "domain": f"0<=w<={width}",
        "absolute_upper_fractions": [str(value) for value in bounds],
        "absolute_upper_decimals": [repr(float(value)) for value in bounds],
        "zero_values": [2, -2, 4],
        "positive_argument_controls": controls,
        "all_controls_inside": all(all(item["inside_declared_bounds"]) for item in controls),
    }


def build() -> dict[str, Any]:
    k320 = json.loads(K320.read_text())
    if k320["scaled_bessel_bank"]["zero_limits"] != {"Phi_0": 2, "Phi_1": -2, "Phi_2": 4}:
        raise AssertionError("K320 zero limits changed")
    widths = [Fraction(1, 16), Fraction(1, 4), Fraction(1), Fraction(4)]
    rows = [row(width) for width in widths]
    if not all(item["all_controls_inside"] for item in rows):
        raise AssertionError("positive-argument control escaped the zero-safe envelope")
    return {
        "schema_version": "1.0",
        "result_id": "K322-ORDER-SEVEN-ZERO-SAFE-SCALED-BESSEL-ENVELOPES",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k320-order-seven-scaled-endpoint-bessel-bank.json",
            ],
            "arb_decimal_digits": 120,
            "threads": 1,
            "orders": [0, 1, 2],
            "widths": [str(value) for value in widths],
        },
        "analytic_envelope": {
            "auxiliary_bounds": [
                "A(w)=w*K1(w) is positive and decreases from A(0)=1",
                "B(w)=w*K0(w) is positive and B(w)<=A(w) because K0(w)<K1(w) for w>0",
            ],
            "formulas": {
                "Phi_0": "2*A",
                "Phi_1": "-2*(A+w*B)",
                "Phi_2": "4*A+2*w*B+2*w^2*A",
            },
            "box_bounds_for_0_le_w_le_W": {
                "abs_Phi_0": "2",
                "abs_Phi_1": "2*(1+W)",
                "abs_Phi_2": "4+2*W+2*W^2",
            },
            "rows": rows,
            "raw_Bessel_evaluation_at_zero_used": False,
            "continuous_zero_values_inserted_exactly": True,
        },
        "determinant_adapter": {
            "aligned_argument": "w=x*rho*sigma*H with H>=1/2 on an aligned K318 Hepp chart",
            "entry_rule": "abs(D^m*Phi_m(w)/H^(m+1)) <= abs(D)^m*U_m(W)*2^(m+1)",
            "orders_covered": [0, 1, 2],
            "terminal_column_scaling_retained": True,
            "detached_terminal_budget_used": False,
        },
        "decision": {
            "zero_inclusive_scaled_Bessel_envelopes_implemented": True,
            "all_three_terminal_jet_orders_covered": True,
            "positive_argument_arb_controls_pass": True,
            "complete_chart_determinant_uppers_emitted": False,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_transfer_released": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "insert these zero-inclusive entry envelopes into the complete weighted old-position-six bordered determinant on the K321 tensor atlas",
        },
        "release_test": {
            "K320_zero_limits_replayed": True,
            "four_nested_widths_checked": len(rows) == 4,
            "all_positive_controls_inside": all(item["all_controls_inside"] for item in rows),
            "bounds_monotone_in_width": all(
                float(rows[index]["absolute_upper_decimals"][order])
                <= float(rows[index + 1]["absolute_upper_decimals"][order])
                for index in range(len(rows) - 1)
                for order in range(3)
            ),
            "raw_zero_evaluation_used": False,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k320["ledger_effect"],
        "source_routing": k320["source_routing"],
        "claim_ceiling": "Rigorous finite zero-inclusive upper envelopes for K320's Phi_0, Phi_1 and Phi_2 on every interval [0,W], derived from 0<A=wK1<=1 and 0<B=wK0<=A and replayed by positive-argument Arb controls at four nested widths. The primitive never evaluates raw K_nu at zero and retains terminal column scaling inside the complete determinant. It is an entry envelope, not a complete chart determinant upper or y-master constant, and releases no gap-axis transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    envelope = payload["analytic_envelope"]
    if envelope["raw_Bessel_evaluation_at_zero_used"] or not envelope["continuous_zero_values_inserted_exactly"]:
        raise AssertionError("zero-safe evaluation contract lost")
    if len(envelope["rows"]) != 4 or not all(row["all_controls_inside"] for row in envelope["rows"]):
        raise AssertionError("zero-safe controls failed")
    adapter = payload["determinant_adapter"]
    if adapter["orders_covered"] != [0, 1, 2] or not adapter["terminal_column_scaling_retained"]:
        raise AssertionError("terminal determinant adapter incomplete")
    if adapter["detached_terminal_budget_used"]:
        raise AssertionError("detached terminal budget introduced")
    decision = payload["decision"]
    if decision["complete_chart_determinant_uppers_emitted"] or decision["complete_y_master_constant_emitted"]:
        raise AssertionError("complete numerical release overclaim")


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
