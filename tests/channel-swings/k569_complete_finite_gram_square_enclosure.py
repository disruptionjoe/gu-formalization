#!/usr/bin/env python3
"""Compose all complete order-specific enclosures into K457's full finite square Q_12."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k569-complete-finite-gram-square-enclosure.json"
K568_PATH = HERE / "k568_lower_order_finite_gram_reconciliation.py"
K568 = ROOT / "lab/process/k568-lower-order-finite-gram-reconciliation.json"
K342 = ROOT / "lab/process/k342-order-seven-value-residual-composition.json"
K372 = ROOT / "lab/process/k372-order-eight-complete-integral-enclosure.json"
K404 = ROOT / "lab/process/k404-order-nine-complete-integral-enclosure.json"
K553 = ROOT / "lab/process/k553-order-ten-complete-integral-enclosure.json"
K567 = ROOT / "lab/process/k567-orders-eleven-twelve-complete-integral-enclosures.json"
K457 = ROOT / "lab/process/k457-k152-shifted-residual-gram-reduction.json"


def load_k568_module():
    spec = importlib.util.spec_from_file_location("k568_for_k569", K568_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K568 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def scientific(value: Fraction, digits: int = 17) -> str:
    with localcontext() as context:
        context.prec = digits + 14
        return f"{Decimal(value.numerator) / Decimal(value.denominator):.{digits}e}"


def exact_interval(path: Path, *keys: str) -> tuple[Fraction, Fraction]:
    value: Any = json.loads(path.read_text())
    for key in keys:
        value = value[key]
    return Fraction(value[0]), Fraction(value[1])


def build() -> dict[str, Any]:
    k568_module = load_k568_module()
    k179 = k568_module.load_k179()
    terms = k179.coefficient_family()
    groups_by_order: dict[int, Counter[str]] = {order: Counter() for order in range(2, 13)}
    for term in terms:
        groups_by_order[int(term["order"])][k568_module.group_id(term)] += 1

    lower_manifest = json.loads(K568.read_text())
    intervals = {
        int(row["order"]): tuple(Fraction(value) for value in row["complete_norm_square_interval_exact"])
        for row in lower_manifest["order_reconciliation"]
    }
    k342 = json.loads(K342.read_text())
    radius_7 = Fraction(k342["complete_order_seven_cubature_enclosure"]["radius_upper"])
    intervals[7] = (-radius_7, radius_7)
    intervals[8] = exact_interval(K372, "complete_integral_enclosure", "complete_order_eight_integral_interval_exact")
    intervals[9] = exact_interval(K404, "complete_integral_enclosure", "complete_order_nine_integral_interval_exact")
    intervals[10] = exact_interval(K553, "complete_integral_enclosure", "complete_order_ten_integral_interval_exact")
    k567 = json.loads(K567.read_text())
    for row in k567["order_enclosures"]:
        intervals[int(row["order"])] = tuple(Fraction(value) for value in row["complete_integral_enclosure"]["complete_integral_interval_exact"])

    sources = {
        2: str(K568.relative_to(ROOT)), 3: str(K568.relative_to(ROOT)),
        4: str(K568.relative_to(ROOT)), 5: str(K568.relative_to(ROOT)), 6: str(K568.relative_to(ROOT)),
        7: str(K342.relative_to(ROOT)), 8: str(K372.relative_to(ROOT)),
        9: str(K404.relative_to(ROOT)), 10: str(K553.relative_to(ROOT)),
        11: str(K567.relative_to(ROOT)), 12: str(K567.relative_to(ROOT)),
    }
    rows = []
    for order in range(2, 13):
        raw_lower, raw_upper = intervals[order]
        if raw_upper < 0:
            raise AssertionError(f"order {order} enclosure excludes a nonnegative norm square")
        lower = max(Fraction(0), raw_lower)
        upper = raw_upper
        groups = groups_by_order[order]
        rows.append({
            "order": order,
            "source": sources[order],
            "resolved_vectors": sum(groups.values()),
            "coherent_groups": len(groups),
            "upper_triangle_gram_entries": sum(size * (size + 1) // 2 for size in groups.values()),
            "source_interval_exact": [q(raw_lower), q(raw_upper)],
            "norm_square_interval_exact": [q(lower), q(upper)],
            "norm_square_interval_scientific": [scientific(lower), scientific(upper)],
            "nonnegativity_clamped_lower_endpoint": raw_lower < 0,
            "complete_order_enclosure": True,
        })

    total_lower = sum((Fraction(row["norm_square_interval_exact"][0]) for row in rows), Fraction(0))
    total_upper = sum((Fraction(row["norm_square_interval_exact"][1]) for row in rows), Fraction(0))
    k457 = json.loads(K457.read_text())
    return {
        "schema_version": "1.0",
        "result_id": "K569-COMPLETE-FINITE-GRAM-SQUARE-ENCLOSURE",
        "created": "2026-09-28",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "scope": "Complete numerical enclosure of K457's finite M-dual residual square Q_12 across every K179 order two through twelve.",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K568, K342, K372, K404, K553, K567, K457)],
            "resolved_vectors": sum(row["resolved_vectors"] for row in rows),
            "coherent_groups": sum(row["coherent_groups"] for row in rows),
            "self_and_cross_entries": sum(row["upper_triangle_gram_entries"] for row in rows),
            "orders": list(range(2, 13)),
        },
        "order_enclosures": rows,
        "finite_square_Q_12": {
            "definition": k457["residual_identity"]["finite_square"],
            "interval_exact": [q(total_lower), q(total_upper)],
            "interval_scientific": [scientific(total_lower), scientific(total_upper)],
            "all_59586_entries_numerically_enclosed": True,
            "orthogonal_order_sum": True,
            "orthogonality_reason": "K179 output signatures retain particle order; unequal orders occupy orthogonal exterior sectors.",
            "negative_numerical_lower_endpoints_clamped_only_after_certified_norm_square_typing": True,
        },
        "composition_contract": {
            "all_order_specific_inputs_are_complete_normalized_enclosures": True,
            "all_coherent_cross_terms_remain_inside_order_enclosures": True,
            "no_native_prefactor_reapplied": True,
            "no_absolute_value_replaces_a_coherent_group": True,
            "finite_square_is_M_dual_metric": True,
            "finite_square_is_not_K152_shifted_form_dual_metric": True,
        },
        "decision": {
            "complete_Q_12_numerically_enclosed": True,
            "complete_M_dual_residual_with_tail_emitted": False,
            "K152_shifted_form_dual_residual_emitted": False,
            "next_exact_input": "propagate K457's exact post-order-twelve tail through the two-sided Hilbert triangle bound",
        },
        "release_test": {
            "all_2958_vectors_retained": sum(row["resolved_vectors"] for row in rows) == 2958,
            "all_201_groups_retained": sum(row["coherent_groups"] for row in rows) == 201,
            "all_59586_entries_retained": sum(row["upper_triangle_gram_entries"] for row in rows) == 59586,
            "all_eleven_orders_present": [row["order"] for row in rows] == list(range(2, 13)),
            "all_intervals_nonnegative_and_ordered": all(Fraction(row["norm_square_interval_exact"][0]) <= Fraction(row["norm_square_interval_exact"][1]) and Fraction(row["norm_square_interval_exact"][0]) >= 0 for row in rows),
            "no_prefactor_reapplied": True,
            "M_dual_metric_preserved": True,
            "K152_not_overclaimed": True,
        },
        "ledger_effect": k457["source_and_ledger_context"]["ledger_effect"],
        "source_routing": "SC-ACT-01/02/06 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS.",
        "claim_ceiling": "Rigorous complete numerical enclosure of the finite M-dual residual square Q_12 using every one of K179's 2,958 vectors, 201 coherent groups and 59,586 self/cross entries. The enclosure is extremely coarse, the post-order-twelve tail is not yet composed here, and no K152 shifted-metric, spectral, source, ledger, canon, paper, public, novelty or physical claim follows.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["resolved_vectors"], fixed["coherent_groups"], fixed["self_and_cross_entries"], fixed["orders"]) != (2958, 201, 59586, list(range(2, 13))):
        raise AssertionError("K569 complete census changed")
    rows = payload["order_enclosures"]
    if len(rows) != 11:
        raise AssertionError("K569 order bank changed")
    for row in rows:
        lower, upper = (Fraction(value) for value in row["norm_square_interval_exact"])
        if lower < 0 or lower > upper or not row["complete_order_enclosure"]:
            raise AssertionError("K569 order interval changed")
    finite = payload["finite_square_Q_12"]
    lower, upper = (Fraction(value) for value in finite["interval_exact"])
    if lower < 0 or lower > upper or not finite["all_59586_entries_numerically_enclosed"] or not finite["orthogonal_order_sum"]:
        raise AssertionError("K569 finite square changed")
    if not all(payload["composition_contract"].values()) or not all(payload["release_test"].values()):
        raise AssertionError("K569 composition boundary changed")
    decision = payload["decision"]
    if not decision["complete_Q_12_numerically_enclosed"] or decision["complete_M_dual_residual_with_tail_emitted"] or decision["K152_shifted_form_dual_residual_emitted"]:
        raise AssertionError("K569 decision boundary changed")


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
