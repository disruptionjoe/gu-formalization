#!/usr/bin/env python3
"""K591: sharp spectral-diameter certificate for K583/K500 leakage."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k591-k500-spectral-diameter-leakage-boundary.json"


def leakage_square(matrix: sp.Matrix, vector: sp.Matrix) -> sp.Expr:
    norm2 = (vector.T * vector)[0]
    action = matrix * vector
    mean = (vector.T * action)[0] / norm2
    residual = action - mean * vector
    return sp.factor((residual.T * residual)[0] / norm2)


def q(value: sp.Expr) -> str:
    return str(sp.factor(value))


def row(name: str, matrix: sp.Matrix, vector: sp.Matrix, lower: sp.Expr, upper: sp.Expr) -> dict[str, Any]:
    leak2 = leakage_square(matrix, vector)
    diameter = sp.factor(upper - lower)
    bound2 = sp.factor(diameter**2 / 4)
    action = matrix * vector
    norm2 = (vector.T * vector)[0]
    tensor2 = sp.factor(2 * ((action.T * action)[0] * norm2 - (vector.T * action)[0] ** 2))
    return {
        "name": name,
        "matrix": [[str(value) for value in matrix.row(i)] for i in range(matrix.rows)],
        "vector": [str(value) for value in vector],
        "spectral_interval": [q(lower), q(upper)],
        "spectral_diameter": q(diameter),
        "leakage_square": q(leak2),
        "diameter_bound_square": q(bound2),
        "bound_holds": bool(leak2 <= bound2),
        "tensor_pair_square": q(tensor2),
        "tensor_bound_rhs": q(sp.factor(diameter**2 * norm2**2 / 2)),
        "tensor_bound_holds": bool(tensor2 <= diameter**2 * norm2**2 / 2),
        "sharp": bool(leak2 == bound2),
    }


def build() -> dict[str, Any]:
    controls = [
        row("sharp endpoints", sp.diag(-2, 4), sp.Matrix([1, 1]), sp.Integer(-2), sp.Integer(4)),
        row("interior three-level", sp.diag(-3, 1, 5), sp.Matrix([1, 2, 3]), sp.Integer(-3), sp.Integer(5)),
        row("exchange block", sp.Matrix([[0, 2, -1], [2, 1, 3], [-1, 3, 4]]), sp.Matrix([1, -2, 1]), sp.Integer(-3), sp.Integer(8)),
        row("reducing line", sp.Matrix([[3, 2, 0], [2, 3, 0], [0, 0, -4]]), sp.Matrix([1, 1, 0]), sp.Integer(-4), sp.Integer(5)),
    ]
    payload = {
        "schema_version": "1.0",
        "result_id": "K591-K500-SPECTRAL-DIAMETER-LEAKAGE-BOUNDARY",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "scope": "Every self-adjoint K500 bath-level normal-action block W_n with nonzero cyclic vector v_n and a certified spectral interval [a_n,b_n], including off-diagonal exchange blocks.",
        "gu_typed_objects": {
            "carrier": "one K162 q00 or q10 bath-number level in the regular-coordinate Hilbert image",
            "form": "self-adjoint full normal action W_n, including matched exchange blocks",
            "pairing": "regular Hilbert pairing transported from physical M=S* S",
            "result": "spectral-diameter leakage certificate MAP-TYPE=orthogonal-block-norm-bound",
            "target": "uniform K500 cyclic/noncyclic cross norm",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Apply the sharp variance bound to K583's exact tensor identity; it retains exchange blocks and requires only a true spectral interval, unlike the invalid higher-level scalar-multiplier extrapolation.",
            "retrieval_collision_result": "K578 proves the diagonal multiplier variance formula and K583 the all-level tensor identity; neither states the sharp spectral-diameter certificate or audits native availability of its uniform input.",
            "strongest_alternative": "Direct action-vector evaluation can beat the diameter bound but still needs normalized all-level coefficients and denominators not presently serialized.",
        },
        "theorem": {
            "hypotheses": "W=W* on a Hilbert space, v nonzero, and spec(W) subset [a,b] with finite a<=b",
            "rank_one_leakage": "lambda(W,v)^2=||(1-P_v)Wv||^2/||v||^2",
            "spectral_measure_variance": "lambda(W,v)^2 is the variance of the spectral measure of W in the normalized state v/||v||",
            "popoviciu_bound": "lambda(W,v)^2 <= (b-a)^2/4",
            "leakage_bound": "lambda(W,v) <= (b-a)/2",
            "tensor_pair_bound": "||Wv tensor v-v tensor Wv||^2 <= ((b-a)^2/2)||v||^4",
            "uniform_release": "if sup_n(b_n-a_n)<=2 mu then K500's complete cyclic/noncyclic cross norm is at most mu",
            "sharp": True,
            "scalar_shift_invariant": True,
            "diagonal_multiplier_required": False,
            "exchange_blocks_allowed": True,
        },
        "exact_controls": {
            "rows": controls,
            "row_count": len(controls),
            "all_bounds_hold": all(item["bound_holds"] and item["tensor_bound_holds"] for item in controls),
            "sharp_endpoint_control_present": any(item["sharp"] for item in controls),
            "off_diagonal_exchange_control_present": True,
            "reducing_line_zero_present": controls[-1]["leakage_square"] == "0",
        },
        "native_applicability": {
            "K583_all_level_tensor_identity_reused": True,
            "K177_higher_level_exchange_terms_retained": True,
            "K580_level_one_result_preserved": True,
            "native_each_level_spectral_interval_serialized": False,
            "native_uniform_spectral_diameter_serialized": False,
            "finite_orders_through_12_supply_all_level_uniform_bound": False,
            "K168_shape_oscillation_supplies_normal_action_diameter": False,
            "reason": "K500 eliminates the scalar and K168 shape cross; the remaining normal action includes K177 exchange blocks, and current artifacts serialize neither complete all-level W_n spectra nor a uniform diameter theorem.",
        },
        "decision": {
            "sharp_coefficient_free_leakage_certificate_emitted": True,
            "complete_native_K500_uniform_leakage_emitted": False,
            "native_noncyclic_floor_emitted": False,
            "K473_beta_emitted": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Prove a uniform spectral interval width for the actual all-level normal blocks W_n, or evaluate the normalized action vectors directly; separately serialize the complete-sector/noncyclic numerical floor required by K584.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating the width-three K168 shape operator or finite order-twelve census as a uniform spectral diameter for K500's distinct full normal action.",
            "strongest_contrary_construction": "Self-adjoint blocks can have arbitrarily large diameter while preserving the abstract tensor identity; the theorem needs a native uniform interval and does not create one.",
            "weakest_reproducibility_seam": "The infinite-level application is conditional on spectral intervals; exact finite controls test the theorem, not native all-level interval availability.",
        },
        "controls": {
            "producer": "tests/channel-swings/k591_k500_spectral_diameter_leakage_boundary.py",
            "probe": "tests/channel-swings/k591_k500_spectral_diameter_leakage_boundary_probe.py",
        },
        "claim_ceiling": "Sharp self-adjoint spectral-diameter certificate: each K500 level satisfies lambda(W_n,v_n)<=diam(spec W_n)/2, equivalently the K583 tensor numerator is at most diam(spec W_n)^2 ||v_n||^4/2. A uniform diameter at most 2 mu would prove complete leakage at most mu. Current native artifacts do not serialize that all-level diameter, and the separate noncyclic floor remains absent; no K473 beta, K152 interval, source, ledger, canon, paper, public, novelty or physical conclusion follows.",
    }
    validate(payload)
    return payload


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["theorem"]
    controls = payload["exact_controls"]
    native = payload["native_applicability"]
    decision = payload["decision"]
    if not theorem["sharp"] or not theorem["exchange_blocks_allowed"] or theorem["diagonal_multiplier_required"]:
        raise AssertionError("K591 theorem boundary changed")
    if controls["row_count"] != 4 or not controls["all_bounds_hold"] or not controls["sharp_endpoint_control_present"] or not controls["off_diagonal_exchange_control_present"]:
        raise AssertionError("K591 controls failed")
    if not native["K583_all_level_tensor_identity_reused"] or not native["K177_higher_level_exchange_terms_retained"]:
        raise AssertionError("K591 native typing failed")
    if native["native_each_level_spectral_interval_serialized"] or native["native_uniform_spectral_diameter_serialized"] or native["finite_orders_through_12_supply_all_level_uniform_bound"] or native["K168_shape_oscillation_supplies_normal_action_diameter"]:
        raise AssertionError("K591 invented native diameter")
    if not decision["sharp_coefficient_free_leakage_certificate_emitted"] or decision["complete_native_K500_uniform_leakage_emitted"] or decision["native_noncyclic_floor_emitted"] or decision["K473_beta_emitted"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K591 decision changed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
