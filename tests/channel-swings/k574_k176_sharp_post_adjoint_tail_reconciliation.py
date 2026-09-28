#!/usr/bin/env python3
"""K574 reconcile K496's sharp tail with K457's residual interface."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k574-k176-sharp-post-adjoint-tail-reconciliation.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K176 = load("k176_for_k574", "k176_last_contraction_exchange_orbit_tail.py")
K496 = load("k496_for_k574", "k496_k176_sharp_exchange_tail.py")


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict:
    k176 = K176.demo()
    k496 = K496.build()
    k457 = json.loads((ROOT / "lab/process/k457-k152-shifted-residual-gram-reduction.json").read_text())
    old_tail = K176.exchange_tail(12)
    sharp_tail = K496.exchange_tail(12)
    old_coefficient = K176.EXCHANGE_COEFFICIENT
    sharp_coefficient = K496.COEFFICIENT
    if old_tail != Fraction(k457["tail_budget"]["epsilon"]):
        raise AssertionError("K457 no longer consumes K176's post-left-adjoint tail")
    if old_tail / sharp_tail != old_coefficient / sharp_coefficient:
        raise AssertionError("K496 did not preserve K176's tail shape")
    return {
        "schema_version": "1.0",
        "result_id": "K574-K176-SHARP-POST-ADJOINT-TAIL-RECONCILIATION",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "K457's complete M-dual residual tail after exchange orders through twelve on the fixed K139/K162 zero-bath seed orbits.",
        "gu_typed_objects": {
            "result": "sharp post-left-adjoint tail reconciliation MAP-TYPE=norm-tail-transfer",
            "carrier": "K162 zero-bath q00/q10 seed exchange orbits",
            "pairing": "regular-coordinate Hilbert pairing induced by M=S* S",
            "form": "K176 coefficient-complete sixteen-monomial exchange tail",
            "target": "K457/K570 complete M-dual residual tail budget",
        },
        "compatibility_replay": {
            "K176_seed_scope": k176["normal_form"]["seed_scope"],
            "K176_post_left_adjoint": True,
            "K176_all_16_exchange_monomials": k176["normal_form"]["all_16_exchange_monomials_included"],
            "K176_tail_formula": k176["post_adjoint_tail"]["formula_after_order_N"],
            "K457_consumed_K176_tail": q(old_tail),
            "K496_seed_scope_unchanged": k496["scope"].startswith("K176's coefficient-complete 16-monomial exchange orbit"),
            "K496_cross_polarity_cancellation_used": k496["premises"]["cross_polarity_cancellation_used"],
            "K496_tail_formula": k496["sharp_tail"]["formula_after_order_N"],
            "same_geometric_tail_shape": True,
            "same_post_left_adjoint_location": True,
        },
        "sharp_tail": {
            "resolved_through_order": 12,
            "old_kernel_norm_upper": q(K176.KERNEL_NORM_UPPER),
            "sharp_kernel_norm_upper": q(K496.KERNEL_NORM),
            "exchange_monomials": K176.EXCHANGE_MONOMIALS,
            "old_coefficient": q(old_coefficient),
            "sharp_coefficient": q(sharp_coefficient),
            "old_tail_norm_upper": q(old_tail),
            "sharp_tail_norm_upper": q(sharp_tail),
            "exact_improvement_factor": q(old_tail / sharp_tail),
            "sharp_tail_strictly_smaller": sharp_tail < old_tail,
        },
        "decision": {
            "K570_tail_input_superseded": True,
            "K569_finite_square_unchanged": True,
            "recompose_complete_M_dual_residual": True,
            "K152_shifted_form_residual_emitted": False,
            "next_exact_input": "Reapply K457's two-sided Hilbert triangle bound to K569's unchanged finite-square enclosure using the sharp post-left-adjoint tail exactly once.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact compatibility and tail sharpening for K457's M-dual residual interface. It changes no finite Gram entry and does not by itself emit a complete residual interval, K152 shifted-form residual, spectrum, source, ledger, canon, paper, public, novelty or physical conclusion.",
    }


def validate(payload: dict) -> None:
    replay = payload["compatibility_replay"]
    sharp = payload["sharp_tail"]
    decision = payload["decision"]
    if not all((replay["K176_post_left_adjoint"], replay["K176_all_16_exchange_monomials"], replay["K496_seed_scope_unchanged"], replay["same_geometric_tail_shape"], replay["same_post_left_adjoint_location"])):
        raise AssertionError("K574 compatibility replay failed")
    if replay["K496_cross_polarity_cancellation_used"]:
        raise AssertionError("K574 invented cross-polarity cancellation")
    if sharp["exact_improvement_factor"] != "40/3" or not sharp["sharp_tail_strictly_smaller"]:
        raise AssertionError("K574 sharp-tail factor changed")
    if not decision["K570_tail_input_superseded"] or not decision["K569_finite_square_unchanged"]:
        raise AssertionError("K574 lost its exact replacement boundary")
    if decision["K152_shifted_form_residual_emitted"]:
        raise AssertionError("K574 overclaimed K152")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
