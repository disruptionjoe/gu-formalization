#!/usr/bin/env python3
"""K578 pairwise-difference certificate for K501 normalized leakage."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k578-k500-pairwise-variance-certificate.json"


def f(value: Any) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def weighted_variance(weights: Sequence[Any], values: Sequence[Any]) -> Fraction:
    a = [f(value) for value in weights]
    m = [f(value) for value in values]
    if not a or len(a) != len(m) or any(value <= 0 for value in a):
        raise ValueError("positive weights and equally many values are required")
    total = sum(a, Fraction())
    mean = sum((x * y for x, y in zip(a, m, strict=True)), Fraction()) / total
    return sum((x * (y - mean) ** 2 for x, y in zip(a, m, strict=True)), Fraction()) / total


def pairwise_variance(weights: Sequence[Any], values: Sequence[Any]) -> Fraction:
    a = [f(value) for value in weights]
    m = [f(value) for value in values]
    if not a or len(a) != len(m) or any(value <= 0 for value in a):
        raise ValueError("positive weights and equally many values are required")
    total = sum(a, Fraction())
    numerator = sum(
        (a[i] * a[j] * (m[i] - m[j]) ** 2 for i in range(len(a)) for j in range(i + 1, len(a))),
        Fraction(),
    )
    return numerator / (total * total)


def oscillation_upper(values: Sequence[Any]) -> Fraction:
    m = [f(value) for value in values]
    if not m:
        raise ValueError("at least one value is required")
    return (max(m) - min(m)) ** 2 / 4


def build() -> dict:
    controls = [
        ([1, 4], [2, -1]),
        ([1, 1, 2], [-3, 1, 4]),
        ([3, 5, 7, 11], [9, 9, 9, 9]),
    ]
    rows = []
    for weights, values in controls:
        direct = weighted_variance(weights, values)
        pairwise = pairwise_variance(weights, values)
        oscillation = oscillation_upper(values)
        if direct != pairwise or direct > oscillation:
            raise AssertionError("pairwise or oscillation identity failed")
        rows.append({
            "weights": [str(value) for value in weights],
            "multipliers": [str(value) for value in values],
            "weighted_variance": q(direct),
            "pairwise_variance": q(pairwise),
            "oscillation_upper": q(oscillation),
            "identity_passes": True,
            "oscillation_bound_passes": True,
        })
    shifted = pairwise_variance([1, 4], [9, 6])
    if shifted != Fraction(36, 25):
        raise AssertionError("scalar-shift invariance failed")
    return {
        "schema_version": "1.0",
        "result_id": "K578-K500-PAIRWISE-VARIANCE-CERTIFICATE",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "K501's normalized rank-one leakage on every discrete or discretized bath-number level, expressed without division by a separately estimated word-norm lower.",
        "gu_typed_objects": {
            "result": "pairwise normalized-leakage certificate MAP-TYPE=orthogonal-block-norm",
            "carrier": "one K162 bath-number level with cyclic vector v_n",
            "pairing": "regular Hilbert pairing transported from physical M=S* S",
            "form": "self-adjoint normal action W_n",
            "target": "the levelwise K500 cyclic/noncyclic cross norm",
        },
        "theorem": {
            "normalized_weights": "p_i=a_i/A with a_i=|v_i|^2 and A=sum_i a_i",
            "K501_variance": "lambda_n^2=sum_i p_i(m_i-mubar)^2",
            "pairwise_identity": "lambda_n^2=sum_(i<j) a_i*a_j*(m_i-m_j)^2/A^2",
            "oscillation_bound": "lambda_n^2<=(max_i m_i-min_i m_i)^2/4",
            "scalar_shift_invariance": "all pairwise differences and lambda_n are unchanged by m_i -> m_i+c",
            "continuum_extension": "replace the finite pair sum by one half of the product-measure integral of |m(x)-m(y)|^2",
            "uniform_K500_certificate": "for every supported level n, certify the pairwise numerator <=mu^2*A_n^2; then sup_n lambda_n<=mu",
            "no_word_lower_required": True,
        },
        "native_data_contract": {
            "required_per_level": [
                "a positive normalized or unnormalized weight measure induced by the actual v_n",
                "the actual self-adjoint normal-action multiplier or a certified pairwise-difference kernel",
                "an outward upper bound on the pairwise energy uniform in n",
            ],
            "sufficient_routes": [
                "direct pairwise-energy enclosure",
                "uniform multiplier oscillation bound",
                "weighted Poincare or Efron-Stein bound proved for the actual v_n measure",
            ],
            "forbidden_substitutions": [
                "K175/K496 absolute residual divided by an upper word-norm estimate",
                "K510 simplex-volume-only selected-path lower",
                "one finite bath prefix presented as the all-level supremum",
            ],
        },
        "exact_controls": {
            "rows": rows,
            "row_count": len(rows),
            "K501_control_replayed": rows[0]["weighted_variance"] == "36/25",
            "scalar_shifted_K501_control": q(shifted),
            "all_pairwise_identities_pass": all(row["identity_passes"] for row in rows),
            "all_oscillation_bounds_pass": all(row["oscillation_bound_passes"] for row in rows),
        },
        "decision": {
            "K510_factorial_path_template_bypassed": True,
            "direct_normalized_variance_route_released": True,
            "native_uniform_all_level_variance_emitted": False,
            "complete_K500_uniform_leakage_emitted": False,
            "noncyclic_floor_emitted": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Instantiate the pairwise energy for the actual q00/q10 K177/K500 cyclic measures and prove a uniform-in-level upper; separately certify the K500 noncyclic compressed-form floor.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact pairwise and oscillation identities for K501 normalized leakage, plus a sufficient all-level certificate interface. No native uniform pairwise-energy bound, complete K500 leakage, noncyclic floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty or physical conclusion follows.",
    }


def validate(payload: dict) -> None:
    theorem = payload["theorem"]
    controls = payload["exact_controls"]
    decision = payload["decision"]
    if not theorem["no_word_lower_required"] or controls["row_count"] != 3:
        raise AssertionError("K578 certificate interface changed")
    if not controls["K501_control_replayed"] or controls["scalar_shifted_K501_control"] != "36/25":
        raise AssertionError("K578 lost the K501 control")
    if not controls["all_pairwise_identities_pass"] or not controls["all_oscillation_bounds_pass"]:
        raise AssertionError("K578 exact controls failed")
    if not decision["K510_factorial_path_template_bypassed"] or not decision["direct_normalized_variance_route_released"]:
        raise AssertionError("K578 route decision changed")
    if decision["native_uniform_all_level_variance_emitted"] or decision["complete_K500_uniform_leakage_emitted"] or decision["noncyclic_floor_emitted"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K578 overclaimed downstream closure")


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
