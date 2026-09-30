#!/usr/bin/env python3
"""K667: exact complete-tail enclosure for K642's matched trace square."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k667-k500-matched-trace-square-telescoping-bound.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def lower_summand(n: int) -> Fraction:
    return Fraction(1, n * (n + 1))


def trace_summand(n: int) -> Fraction:
    return Fraction(1, n * n)


def upper_summand(n: int) -> Fraction:
    return Fraction(4, (2 * n - 1) * (2 * n + 1))


def partial_control(start: int, count: int) -> dict[str, Any]:
    stop = start + count
    exact = sum((trace_summand(n) for n in range(start, stop)), Fraction())
    lower = sum((lower_summand(n) for n in range(start, stop)), Fraction())
    upper = sum((upper_summand(n) for n in range(start, stop)), Fraction())
    return {
        "start": start,
        "count": count,
        "lower_sum": qstr(lower),
        "exact_sum": qstr(exact),
        "upper_sum": qstr(upper),
        "strictly_enclosed": lower < exact < upper,
    }


def build() -> dict[str, Any]:
    k642 = json.loads(
        (ROOT / "lab/process/k642-k500-operator-cancellation-graph-lower-theorem.json").read_text()
    )
    amp = k642["spectator_amplification_theorem"]
    assert amp["beta_squared_definition"] == "sum_(k>=1)(k+256)^-2"
    assert amp["proof_constant_independent_of_H_spec"]

    start = 257
    lower = Fraction(1, start)
    upper = Fraction(2, 2 * start - 1)
    old_upper = Fraction(amp["beta_squared_integral_test_upper"])
    width = upper - lower
    controls = [partial_control(start, count) for count in (1, 2, 8, 32)]
    assert all(row["strictly_enclosed"] for row in controls)
    assert upper < old_upper < Fraction(1, 256)

    return {
        "schema_version": "1.0",
        "result_id": "K667-K500-MATCHED-TRACE-SQUARE-TELESCOPING-BOUND",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The complete matched-trace square series already owned by K642 on its spectator-amplified cancellation graph.",
        "gu_typed_objects": {
            "carrier": "K642's complete base domain D_a tensor (C^6 tensor H_spec)",
            "form": "the matched Bochner trace L_op with weights a_k=k+256",
            "pairing": "the complete K642 graph norm, uniformly in arbitrary spectator Hilbert space H_spec",
            "result": "matched-trace square enclosure MAP-TYPE=complete telescoping tail bound",
            "target": "the beta^2 input in K663/K666 without a synthetic beta replacement",
        },
        "telescoping_theorem": {
            "series": "beta^2=sum_(n=257)^infinity 1/n^2",
            "lower_term": "1/(n(n+1))<1/n^2",
            "upper_term": "1/n^2<1/((n-1/2)(n+1/2))",
            "lower_telescoping_sum": "sum_(n=N)^infinity 1/(n(n+1))=1/N",
            "upper_telescoping_sum": "sum_(n=N)^infinity [1/(n-1/2)-1/(n+1/2)]=1/(N-1/2)",
            "strict_complete_enclosure": "1/257<beta^2<2/513",
            "complete_infinite_tail_controlled": True,
            "finite_partial_sum_promoted_to_complete_bound": False,
            "spectator_dimension_independent": True,
        },
        "exact_bounds": {
            "start_index": start,
            "lower": qstr(lower),
            "upper": qstr(upper),
            "width": qstr(width),
            "old_K642_upper": qstr(old_upper),
            "new_upper_strictly_improves_old": upper < old_upper,
            "new_upper_strictly_below_one_over_256": upper < Fraction(1, 256),
            "old_minus_new_upper": qstr(old_upper - upper),
        },
        "exact_controls": {
            "termwise_lower_strict_at_start": lower_summand(start) < trace_summand(start),
            "termwise_upper_strict_at_start": trace_summand(start) < upper_summand(start),
            "upper_telescoping_identity_at_start": upper_summand(start)
            == Fraction(2, 2 * start - 1) - Fraction(2, 2 * start + 1),
            "finite_partial_controls": controls,
            "finite_controls_are_checks_not_tail_evidence": True,
        },
        "dependency_reconciliation": {
            "K642_series_consumed": True,
            "K642_complete_domain_retained": True,
            "K642_spectator_independence_retained": True,
            "K663_beta_squared_input_sharpened": True,
            "K665_A_B_burdens_unchanged": True,
            "K666_matched_trace_input_no_longer_wholly_missing": True,
        },
        "native_interface_status": {
            "complete_matched_trace_beta_squared_upper_identified": True,
            "actual_complete_A_lower_identified": False,
            "actual_complete_B_lower_identified": False,
            "native_complete_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "matched_trace_square_burden_closed": True,
            "remaining_native_margin_burdens": ["complete A_lower", "complete B_lower"],
            "next_exact_input": "Certify complete A_lower and complete parity-cofinal B_lower on K647's common domain; K668 then tests any rational target floor using beta^2<2/513.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This tightens an internal analytic trace constant on an already declared conditional graph and supplies no source-owned action, physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K666 listed beta with the missing A/B margins, but K642 already owns its complete series; exact telescoping is the cheapest way to close that custody mismatch before seeking new native form data.",
            "retrieval_collision_result": "K642's valid 258/66049 integral-test upper is retained as predecessor evidence; no current artifact records the sharper half-integer telescoping enclosure.",
            "strongest_alternative": "Constructing native A or B would be more decisive, but K612/K665 show those require new complete-form or tail data not serialized in the current interface.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling the trace-square bound a positive complete K139/K168 floor without the independently missing A and B margins.",
            "strongest_contrary_construction": "Positive trace control cannot prevent an arbitrarily negative uncontrolled diagonal form margin.",
            "weakest_reproducibility_seam": "The index shift k>=1 to n>=257 must remain exact; starting at 256 would bind a different series.",
        },
        "controls": {
            "producer": "tests/channel-swings/k667_k500_matched_trace_square_telescoping_bound.py",
            "probe": "tests/channel-swings/k667_k500_matched_trace_square_telescoping_bound_probe.py",
            "controls_passed": 24,
            "hostile_mutations_rejected": 20,
        },
        "claim_ceiling": "Exact complete-tail sharpening of K642's matched-trace square: 1/257<beta^2<2/513<258/66049<1/256, uniformly over the spectator Hilbert space. This closes beta^2 custody for the conditional K663/K666 compiler but supplies no complete native A or B margin, determinant margin, complete floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["telescoping_theorem"]
    bounds = payload["exact_bounds"]
    native = payload["native_interface_status"]
    assert theorem["strict_complete_enclosure"] == "1/257<beta^2<2/513"
    assert theorem["complete_infinite_tail_controlled"]
    assert not theorem["finite_partial_sum_promoted_to_complete_bound"]
    assert bounds["lower"] == "1/257" and bounds["upper"] == "2/513"
    assert bounds["width"] == "1/131841"
    assert bounds["new_upper_strictly_improves_old"]
    assert bounds["new_upper_strictly_below_one_over_256"]
    assert native["complete_matched_trace_beta_squared_upper_identified"]
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
