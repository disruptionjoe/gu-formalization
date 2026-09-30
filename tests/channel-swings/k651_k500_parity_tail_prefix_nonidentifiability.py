#!/usr/bin/env python3
"""K651: finite K179 prefixes do not identify K650 parity tails."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k651-k500-parity-tail-prefix-nonidentifiability.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K179 = load("k179_for_k651", "k179_matched_normal_order_coefficient_family.py")


def floor(a: Fraction, d: Fraction, kappa: Fraction = Fraction()) -> Fraction:
    return min(a - kappa, d - kappa)


def comparison_family(prefix_end: int, depth: int) -> dict[str, Any]:
    prefix = []
    adverse_tail = []
    positive_tail = []
    for n in range(2, prefix_end + 1):
        row = {"n": n, "plus_floor": "2", "minus_floor": "7/4"}
        prefix.append(row)
    for n in range(prefix_end + 1, prefix_end + 5):
        adverse_tail.append({
            "n": n,
            "plus_floor": str(floor(Fraction(-depth), Fraction(3))),
            "minus_floor": str(floor(Fraction(-depth - 1), Fraction(4))),
        })
        positive_tail.append({"n": n, "plus_floor": "2", "minus_floor": "7/4"})
    return {
        "prefix": prefix,
        "adverse_tail": adverse_tail,
        "positive_tail": positive_tail,
        "prefixes_identical": True,
        "parity_covariant": True,
        "same_domain": "C^2 in every bath/parity sector",
        "relative_coupling_rho": "0",
        "residual_coupling_kappa": "0",
        "adverse_complete_tail_floor_at_most": str(Fraction(-depth - 1)),
        "positive_complete_tail_floor": "7/4",
    }


def build() -> dict[str, Any]:
    family = K179.coefficient_family()
    orders = sorted({int(row["order"]) for row in family})
    assert orders == list(range(2, 13))
    digest = hashlib.sha256(
        json.dumps(family, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    controls = [comparison_family(12, depth) for depth in (1, 8, 64, 1024)]
    return {
        "schema_version": "1.0",
        "result_id": "K651-K500-PARITY-TAIL-PREFIX-NONIDENTIFIABILITY",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Whether K179's currently serialized orders two through twelve determine either independent K650 total-parity tail.",
        "gu_typed_objects": {
            "carrier": "K643 bath sectors split by K648 total parity into K650's two complete cancelled quadrants",
            "form": "the complete same-domain cancelled-quadrant form, not separated singular exchange factors",
            "prefix": "K179's coefficient-complete orders two through twelve",
            "result": "parity-tail prefix nonidentifiability MAP-TYPE=finite-data obstruction",
            "target": "the independent uniform tails t_plus,t_minus required by K646/K650",
        },
        "k179_prefix": {
            "orders": orders,
            "maximum_order": max(orders),
            "term_count": len(family),
            "family_sha256": digest,
            "all_order_tail_serialized": False,
        },
        "prefix_nonidentifiability_theorem": {
            "quantifier": "for every finite prefix N and every L>0",
            "construction": "two closed parity-covariant same-domain diagonal cancelled-form families agree in every sector n<=N; one has both tails bounded below while the other has a later parity floor below -L",
            "preserves_K650_relative_interface": True,
            "preserves_total_parity_reduction": True,
            "uses_separately_singular_raw_rows": False,
            "finite_prefix_determines_uniform_tail": False,
            "finite_prefix_plus_qualitative_semiboundedness_determines_numeric_tail": False,
            "fixed_native_operator_has_no_floor": False,
            "future_all_order_estimate_excluded": False,
        },
        "exact_controls": controls,
        "decision": {
            "orders_two_through_twelve_are_not_a_tail_certificate": True,
            "another_finite_order_extension_alone_closes_the_tail": False,
            "K612_custody_obstruction_sharpened_to_K650_parity_interface": True,
            "next_exact_input": "Prove an all-order same-domain asymptotic lower for both complete cancelled quadrants and an all-order residual-coupling upper in each parity sign; then compose them through K650 rather than extrapolating a finite prefix.",
        },
        "native_interface_status": {
            "actual_uniform_parity_tails_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "dependency_reconciliation": {
            "K179_prefix_retracted": False,
            "K612_data_custody_obstruction_retracted": False,
            "K643_uniform_tail_requirement_consumed": True,
            "K650_cancelled_quadrant_interface_consumed": True,
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a finite-data theorem inside a repository-supplied conditional point-Fock operator model and supplies no action-owned physical state, observable or source mechanism.",
        "preflight_bookend": {
            "route_comparison": "K650 makes independent all-sector parity tails load bearing; before extending the finite coefficient bank, test whether any finite extension can logically certify that tail.",
            "retrieval_collision_result": "K612 proves broad quantitative custody insufficiency, but does not give the prefix-matched parity-covariant counterfamily on K650's exact interface.",
            "strongest_alternative": "A direct native all-order estimate is stronger and remains live; K651 prevents a finite prefix from being mistaken for it.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Saying the fixed native K139/K168 form is unbounded below rather than saying its current finite coefficient prefix does not prove a tail.",
            "strongest_contrary_construction": "A separately proved closed generating function or all-order graph estimate can distinguish the two counterfamilies and certify a native tail.",
            "weakest_reproducibility_seam": "The exact controls are abstract same-interface families; they audit data sufficiency rather than evaluate the native kernels.",
        },
        "claim_ceiling": "Exact prefix-specific data-sufficiency obstruction for K650. K179's serialized orders two through twelve, even with total-parity covariance and the same cancelled-form interface, do not determine independent uniform parity tails: exact closed families can agree on that entire prefix while their later floors differ without bound. This does not deny a floor for the fixed native K139/K168 operator or exclude a new all-order estimate. No native m, alpha, delta, K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    prefix = payload["k179_prefix"]
    theorem = payload["prefix_nonidentifiability_theorem"]
    native = payload["native_interface_status"]
    assert prefix["orders"] == list(range(2, 13))
    assert prefix["term_count"] == 2958
    assert not prefix["all_order_tail_serialized"]
    assert not theorem["finite_prefix_determines_uniform_tail"]
    assert not theorem["fixed_native_operator_has_no_floor"]
    assert all(row["prefixes_identical"] for row in payload["exact_controls"])
    assert not native["native_global_m_identified"]


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
