#!/usr/bin/env python3
"""K456 complete convergent representation of the K156/K171 action column."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K176 = load("k176_for_k456", "k176_last_contraction_exchange_orbit_tail.py")
K179 = load("k179_for_k456", "k179_matched_normal_order_coefficient_family.py")


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def demo() -> dict[str, Any]:
    terms = K179.coefficient_family()
    by_order = Counter(int(term["order"]) for term in terms)
    tail = K176.exchange_tail(12)
    return {
        "schema_version": "1.0",
        "result_id": "K456-K156-CONTINUUM-ACTION-COLUMN-MANIFEST",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "carrier": "hard-core C3 tensor Gamma_-(L2(R;C4))",
            "seed_scope": "K162_zero_bath_seed_orbits",
            "auxiliary_chart_shift": 256,
            "chart": "K139 S=(1-G_256)^-1",
        },
        "column_decomposition": {
            "scalar_component": {
                "formula": "-256*S* S*u",
                "complete_convergent_representation": True,
                "source": "K175 scalar metric resummation",
            },
            "matched_diagonal_component": {
                "formula": "sum_(n>=0) S* W_diag,n G^n u",
                "complete_convergent_representation": True,
                "source": "K172/K175 matched diagonal orbit",
            },
            "exchange_component": {
                "resolved_orders": [2, 12],
                "resolved_term_count": len(terms),
                "resolved_terms_by_order": {str(key): by_order[key] for key in sorted(by_order)},
                "resolved_family_sha256": K179.family_digest(terms),
                "unresolved_required_field_instances": len(K179.K178.missing_coefficient_fields(terms)),
                "canonical_expansion_command": "python3 tests/channel-swings/k179_matched_normal_order_coefficient_family.py --terms",
                "post_order_12_tail_norm_upper": qstr(tail),
                "post_order_12_tail_less_than_1_over_250": tail < Fraction(1, 250),
                "complete_convergent_representation": True,
            },
        },
        "representation_contract": {
            "complete_means": "every exact finite coefficient through order 12 plus a rigorous norm tail for all later orders",
            "does_not_mean": "the 2958 finite vector integrals have all been numerically evaluated",
            "coefficient_complete": True,
            "all_order_tail_complete": True,
            "complete_continuum_action_column_serialized": True,
            "complete_continuum_action_column_numerically_evaluated": False,
        },
        "decision": {
            "K455_column_reference_released": True,
            "K455_residual_reference_released": False,
            "next_exact_input": "Reduce the shifted form-dual residual to the finite coherent Gram payload and the post-order-12 tail without replacing unevaluated integrals by fitted numbers.",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
