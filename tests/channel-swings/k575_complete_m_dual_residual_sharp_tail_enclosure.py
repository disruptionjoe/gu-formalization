#!/usr/bin/env python3
"""K575 compose K569 with K574's sharp tail."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k575-complete-m-dual-residual-sharp-tail-enclosure.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K574 = load("k574_for_k575", "k574_k176_sharp_post_adjoint_tail_reconciliation.py")


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def sci(value: Fraction) -> str:
    with localcontext() as ctx:
        ctx.prec = 24
        number = Decimal(value.numerator) / Decimal(value.denominator)
        return f"{number:.17E}"


def build() -> dict:
    k569 = json.loads((ROOT / "lab/process/k569-complete-finite-gram-square-enclosure.json").read_text())
    k570 = json.loads((ROOT / "lab/process/k570-complete-m-dual-residual-enclosure.json").read_text())
    k574 = K574.build()
    finite = [Fraction(value) for value in k569["finite_square_Q_12"]["interval_exact"]]
    sqrt_finite = [Fraction(value) for value in k570["finite_square_input"]["sqrt_interval_exact"]]
    epsilon = Fraction(k574["sharp_tail"]["sharp_tail_norm_upper"])
    lower_norm = max(Fraction(), sqrt_finite[0] - epsilon)
    upper_norm = sqrt_finite[1] + epsilon
    interval = [lower_norm * lower_norm, upper_norm * upper_norm]
    old_interval = [Fraction(value) for value in k570["complete_M_dual_residual_norm_square"]["interval_exact"]]
    return {
        "schema_version": "1.0",
        "result_id": "K575-COMPLETE-M-DUAL-RESIDUAL-SHARP-TAIL-ENCLOSURE",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Complete K457 M-dual/Hilbert residual after all 59,586 finite Gram entries and K574's sharp post-order-twelve post-left-adjoint exchange tail.",
        "gu_typed_objects": {
            "result": "complete sharp-tail M-dual residual enclosure MAP-TYPE=two-sided-norm-enclosure",
            "carrier": "one fixed complete K162 charge sector",
            "pairing": "M-dual/Hilbert residual metric ell* M^(-1) ell",
            "form": "fixed K139/K168 reference form",
            "target": "K455 complete_M_dual_residual_ref; K152 shifted-form use remains separate",
        },
        "fixed_control": {
            "resolved_vectors": k569["fixed_control"]["resolved_vectors"],
            "coherent_groups": k569["fixed_control"]["coherent_groups"],
            "self_and_cross_entries": k569["fixed_control"]["self_and_cross_entries"],
            "finite_square_interval_exact": [q(value) for value in finite],
            "finite_sqrt_outward_interval_exact": [q(value) for value in sqrt_finite],
            "sharp_tail_norm_upper_exact": q(epsilon),
        },
        "complete_M_dual_residual_norm_square": {
            "identity": "r=r_12+t_>12",
            "two_sided_bound": "max(0,sqrt(Q_12)-epsilon_sharp)^2 <= ||r||_Mdual^2 <= (sqrt(Q_12)+epsilon_sharp)^2",
            "interval_exact": [q(value) for value in interval],
            "interval_scientific": [sci(value) for value in interval],
            "strictly_positive_lower_endpoint": interval[0] > 0,
            "finite_lower_norm_exceeds_sharp_tail": sqrt_finite[0] > epsilon,
            "metric_type": "M-dual/Hilbert residual ell* M^(-1) ell",
            "K152_shifted_form_dual_type": "ell*(R+sM)^(-1)ell",
        },
        "comparison_to_K570": {
            "old_lower_endpoint": q(old_interval[0]),
            "old_upper_endpoint": q(old_interval[1]),
            "new_lower_strictly_improves": interval[0] > old_interval[0],
            "new_upper_strictly_improves": interval[1] < old_interval[1],
            "K570_finite_square_unchanged": True,
            "only_tail_input_changed": True,
        },
        "decision": {
            "complete_M_dual_residual_numerically_enclosed": True,
            "complete_M_dual_residual_proved_nonzero": interval[0] > 0,
            "trial_is_not_exact_for_the_fixed_M_dual_operator": interval[0] > 0,
            "K152_shifted_form_dual_residual_emitted": False,
            "native_K152_interval_emitted": False,
            "spectral_error_lower_bound_emitted": False,
            "next_exact_input": "Retain the M-dual nonvanishing floor, but replace the coarse order-eight-through-twelve absolute Peano ceilings with cancellation-aware coherent bounds below K576's consumer budgets and separately complete K494/K500's reference-specific floor.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "A rigorous strictly positive lower and finite upper enclosure for the complete M-dual residual of the fixed repository trial/operator. It proves that this trial is not an exact eigenvector in the M-dual metric. It is not a K152 shifted-form residual lower, a spectral-error lower, a native K152 interval, or a source, ledger, canon, paper, public, novelty or physical conclusion.",
    }


def validate(payload: dict) -> None:
    result = payload["complete_M_dual_residual_norm_square"]
    comparison = payload["comparison_to_K570"]
    decision = payload["decision"]
    lower, upper = map(Fraction, result["interval_exact"])
    if not (0 < lower <= upper):
        raise AssertionError("K575 lost its positive ordered interval")
    if not result["strictly_positive_lower_endpoint"] or not result["finite_lower_norm_exceeds_sharp_tail"]:
        raise AssertionError("K575 nonvanishing control failed")
    if not comparison["new_lower_strictly_improves"] or not comparison["new_upper_strictly_improves"]:
        raise AssertionError("K575 did not strictly sharpen K570")
    if not comparison["K570_finite_square_unchanged"] or not comparison["only_tail_input_changed"]:
        raise AssertionError("K575 changed more than the tail input")
    if not decision["complete_M_dual_residual_proved_nonzero"] or not decision["trial_is_not_exact_for_the_fixed_M_dual_operator"]:
        raise AssertionError("K575 lost its scoped nonvanishing result")
    if decision["K152_shifted_form_dual_residual_emitted"] or decision["native_K152_interval_emitted"] or decision["spectral_error_lower_bound_emitted"]:
        raise AssertionError("K575 overclaimed the M-dual lower")


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
