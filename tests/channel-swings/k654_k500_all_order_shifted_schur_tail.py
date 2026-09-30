#!/usr/bin/env python3
"""K654: all-order parity tail from shifted-Schur target tests."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k654-k500-all-order-shifted-schur-tail.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K651 = load("k651_for_k654", "k651_k500_parity_tail_prefix_nonidentifiability.py")
K653 = load("k653_for_k654", "k653_k500_shifted_schur_target_certificate.py")


def parity_rows(
    sign: str,
    b: Fraction,
    a: Callable[[int], Fraction],
    d: Callable[[int], Fraction],
    c: Callable[[int], Fraction],
) -> dict[str, Any]:
    rows = []
    for n in (4, 8, 32, 128):
        row = K653.scalar_target_test(a(n), d(n), c(n), b)
        row["n"] = n
        rows.append(row)
    return {"sign": sign, "target_b": str(b), "rows": rows}


def build() -> dict[str, Any]:
    k651 = K651.build()
    k653 = K653.build()
    b = Fraction(5, 4)
    plus = parity_rows(
        "+", b,
        lambda n: b + 1 + Fraction(1, n + 1),
        lambda n: b + 2,
        lambda n: Fraction(1, 2),
    )
    minus = parity_rows(
        "-", b,
        lambda n: b + Fraction(1, 2),
        lambda n: b + Fraction(3, 2) + Fraction(1, n + 1),
        lambda n: Fraction(3, 4),
    )
    return {
        "schema_version": "1.0",
        "result_id": "K654-K500-ALL-ORDER-SHIFTED-SCHUR-TAIL",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Composition of K653 target-relative sector certificates into K650 independent total-parity tails and a finite-prefix global lower bound.",
        "gu_typed_objects": {
            "carrier": "all K643 bath sectors beyond one cutoff, separately in each K648 total-parity sign",
            "form": "K650's complete cancellation-preserving quadrant form in every sector",
            "domain": "the K647 common graph form domain sector by sector",
            "target": "one proposed uniform floor b shared by both parity tails",
            "result": "all-order shifted-Schur tail certificate MAP-TYPE=uniform target composition",
        },
        "all_order_shifted_tail_theorem": {
            "hypotheses": [
                "for one b and cutoff N, every n>N and sign s has both shifted diagonal forms nonnegative on one common domain",
                "the shifted cross form is contractive with theta_s,n<=1 in every such sector",
                "every finite sector n<=N in both parity signs has a certified floor at least b",
            ],
            "sector_conclusion": "ell_s,n>=b for every n>N and s in {+,-}",
            "tail_conclusion": "t_plus>=b and t_minus>=b",
            "finite_prefix_composition": "m>=b",
            "single_target_may_be_tested_directly": True,
            "absolute_A_D_K_envelopes_required": False,
            "all_order_shifted_hypotheses_required": True,
            "finite_prefix_alone_sufficient": False,
            "equivalent_native_burden_is_not_removed": True,
        },
        "exact_controls": {
            "synthetic_not_native": True,
            "target_b": str(b),
            "plus": plus,
            "minus": minus,
            "finite_sector_floors": ["3/2", "7/4"],
            "finite_sectors_at_least_target": True,
            "all_tail_rows_pass": all(
                row["target_floor_certified"]
                for block in (plus, minus)
                for row in block["rows"]
            ),
        },
        "decision": {
            "K651_prefix_obstruction_consumed": k651["decision"]["orders_two_through_twelve_are_not_a_tail_certificate"],
            "K653_target_certificate_consumed": k653["decision"]["direct_target_route_closed_abstractly"],
            "direct_all_order_target_route_closed_abstractly": True,
            "native_uniform_floor_emitted": False,
            "next_exact_input": "On the actual K650 forms, choose one target b and prove the K653 shifted diagonal positivity and shifted cross contraction for all sectors of both parity signs, plus finite-sector floors at b; or exhibit the first failing target row. Then prove alpha,delta independently.",
        },
        "native_interface_status": {
            "all_order_shifted_tail_shape_complete": True,
            "actual_native_target_b_identified": False,
            "actual_all_order_shifted_hypotheses_proved": False,
            "actual_uniform_parity_tails_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "dependency_reconciliation": {
            "K651_finite_prefix_obstruction_preserved": True,
            "K652_absolute_envelope_route_retracted": False,
            "K653_shifted_target_route_consumed": True,
            "K612_custody_obstruction_retracted": False,
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This all-order composition theorem and its synthetic controls remain inside a conditional internal operator model and provide no action-owned physical state, observable or source mechanism.",
        "preflight_bookend": {
            "route_comparison": "K651 forbids finite-prefix extrapolation; K653 permits a direct target test. Uniformly applying that test in both parity signs is the shortest target-specific tail certificate.",
            "retrieval_collision_result": "K652 gives an absolute-envelope route, but no artifact composes a prescribed shifted target without first serializing A_s,D_s,K_s.",
            "strongest_alternative": "K652 remains the more informative route if reusable absolute envelopes can be proved; K654 is narrower and potentially cheaper for one target b.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Reporting synthetic b=5/4 as native m or claiming that the target-relative route avoids all-order native estimates.",
            "strongest_contrary_construction": "One later sector with a negative shifted diagonal or supercontractive cross invalidates the uniform tail while preserving every finite prefix.",
            "weakest_reproducibility_seam": "The theorem is exact, but the actual all-order shifted forms and a native target remain unserialized.",
        },
        "claim_ceiling": "Exact all-order composition theorem for K653 on K650's two total-parity signs. Uniform same-domain shifted positivity and cross contraction at one prescribed b give both parity tails and, with finite-sector floors, m>=b. The synthetic b=5/4 controls are not native, and the theorem does not remove the all-order native proof burden exposed by K651. No native b, tail, m, alpha or delta is supplied. No K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["all_order_shifted_tail_theorem"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["all_order_shifted_hypotheses_required"]
    assert not theorem["finite_prefix_alone_sufficient"]
    assert controls["all_tail_rows_pass"] and controls["finite_sectors_at_least_target"]
    assert controls["target_b"] == "5/4"
    assert native["all_order_shifted_tail_shape_complete"]
    assert not native["actual_uniform_parity_tails_identified"]


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
