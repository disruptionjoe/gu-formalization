#!/usr/bin/env python3
"""K659: compensated chart shifts and qualitative semiboundedness do not identify a floor."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k659-k500-auxiliary-chart-floor-nonidentifiability.json"


def chart_row(chart_shift: Fraction, fixed_floor: Fraction) -> dict[str, Any]:
    return {
        "auxiliary_chart_shift": str(chart_shift),
        "regular_compensation": str(-chart_shift),
        "expanded_operator_floor": str(fixed_floor),
        "expanded_operator_unchanged": True,
        "chart_shift_equals_spectral_floor": chart_shift == -fixed_floor,
    }


def semibounded_row(depth: int) -> dict[str, Any]:
    return {
        "control_depth_L": depth,
        "qualitatively_semibounded": True,
        "some_finite_lower_shift_exists": True,
        "spectral_floor": str(-depth),
    }


def build() -> dict[str, Any]:
    chart_rows = [
        chart_row(Fraction(4), Fraction(-7, 3)),
        chart_row(Fraction(256), Fraction(-7, 3)),
        chart_row(Fraction(4096), Fraction(-7, 3)),
    ]
    semibounded_rows = [semibounded_row(x) for x in (1, 7, 100)]
    return {
        "schema_version": "1.0",
        "result_id": "K659-K500-AUXILIARY-CHART-FLOOR-NONIDENTIFIABILITY",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A custody-relative obstruction to reading K139's compensated auxiliary boundary-chart shift or qualitative uniform semiboundedness as K657's native numerical real-level floor.",
        "gu_typed_objects": {
            "carrier": "K139's complete positive particle/hole Fock carrier with spectator degrees of freedom",
            "form": "the expanded minimally countertermed target operator held fixed while its Neumann boundary chart is changed and exactly compensated",
            "domain": "the common recursive K139 boundary domain represented in different auxiliary resolvent charts",
            "target": "one actual numerical s for K657, not an auxiliary chart coordinate",
            "result": "chart/floor custody obstruction MAP-TYPE=nonidentifiability",
        },
        "compensated_chart_theorem": {
            "K139_identity": "changing auxiliary lambda moves a bounded diagonal term between the free resolvent chart and the regular operator while the expanded target operator is held fixed",
            "spectral_consequence": "the spectrum and lower floor of the fixed expanded operator are independent of the compensated chart parameter",
            "lambda_256_is_native_floor": False,
            "arbitrarily_large_chart_shift_improves_floor": False,
            "chart_contraction_implies_positive_operator": False,
            "same_target_operator_required": True,
        },
        "semiboundedness_nonidentifiability": {
            "serialized_native_statement": "a common finite lower shift makes the regular operators self-adjoint and uniformly semibounded",
            "existence_consequence": "there exists at least one finite s with A>=-s",
            "numerical_s_identified": False,
            "best_floor_identified": False,
            "control_family": semibounded_rows,
            "same_qualitative_interface_allows_arbitrary_negative_floors": True,
            "fixed_native_operator_has_no_floor": False,
        },
        "exact_controls": {
            "chart_rows": chart_rows,
            "chart_rows_preserve_one_floor": len({row["expanded_operator_floor"] for row in chart_rows}) == 1,
            "displayed_256_rejected_as_floor": not chart_rows[1]["chart_shift_equals_spectral_floor"],
            "semibounded_rows": semibounded_rows,
            "qualitative_rows_share_interface": all(row["qualitatively_semibounded"] for row in semibounded_rows),
            "qualitative_rows_have_distinct_floors": len({row["spectral_floor"] for row in semibounded_rows}) == 3,
            "controls_are_synthetic": True,
        },
        "decision": {
            "K139_auxiliary_shift_rejected_as_native_s": True,
            "K139_semiboundedness_retained": True,
            "native_floor_supplied": False,
            "next_exact_input": "Authenticate one K139 ordinary boundary triple and derive an invariant complete denominator D_W(-s) at a separately proposed real level; K660 specifies the harmless boundary translations and K658 specifies the required complete-space margin.",
        },
        "native_interface_status": {
            "actual_native_s_identified": False,
            "actual_native_denominator_serialized": False,
            "actual_native_base_floor_r0_identified": False,
            "actual_native_target_b_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a custody result inside the repository-supplied point-Fock control; it neither selects a physical extension nor constructs a positive physical state space.",
        "preflight_bookend": {
            "route_comparison": "K657 needs a numerical spectral level, while K139's displayed auxiliary lambda is explicitly compensated and can be enlarged without changing the target operator.",
            "retrieval_collision_result": "K139 proves qualitative uniform semiboundedness but records no numerical lower constant for the limiting expanded operator.",
            "strongest_alternative": "K652's cancelled-form all-order route remains available if no invariant real-level boundary denominator can be constructed.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Using lambda=256, or any larger Neumann-chart parameter, as K657's native s.",
            "strongest_contrary_construction": "One fixed operator with floor -7/3 admits compensated charts at 4, 256 and 4096; the chart improves while the spectrum does not move.",
            "weakest_reproducibility_seam": "K139 states existence of a common finite lower shift but does not serialize its value or the estimates needed to recover it.",
        },
        "claim_ceiling": "Exact custody-relative nonidentifiability result. K139's compensated auxiliary resolvent-chart parameter changes the Neumann coordinate but not the expanded target operator, so lambda=256 and arbitrarily large chart shifts cannot be promoted to K657's spectral s. Qualitative uniform semiboundedness proves existence of some finite lower shift but does not identify its value; exact synthetic families share that interface with arbitrary negative floors. This does not say the fixed native operator lacks a floor. No native s, denominator, r0, b, d_N, eta_N, tail, m, alpha, delta, K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is supplied.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["compensated_chart_theorem"]
    controls = payload["exact_controls"]
    assert theorem["same_target_operator_required"]
    assert not theorem["lambda_256_is_native_floor"]
    assert controls["chart_rows_preserve_one_floor"]
    assert controls["qualitative_rows_have_distinct_floors"]
    assert not payload["decision"]["native_floor_supplied"]


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
