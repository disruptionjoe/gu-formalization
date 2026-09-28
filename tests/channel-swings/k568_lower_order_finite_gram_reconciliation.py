#!/usr/bin/env python3
"""Reconcile K180--K184 with K179's complete order-two-through-six Gram census."""

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
OUTPUT = ROOT / "lab/process/k568-lower-order-finite-gram-reconciliation.json"
INPUTS = {
    2: ROOT / "lab/process/k180-order-two-outward-exchange-kernel-wave.json",
    3: ROOT / "lab/process/k181-order-three-determinant-exchange-wave.json",
    4: ROOT / "lab/process/k182-order-four-coherent-gram-wave.json",
    5: ROOT / "lab/process/k183-order-five-coherent-gram-compression-wave.json",
    6: ROOT / "lab/process/k184-order-six-certified-low-rank-wave.json",
}


def load_k179():
    path = HERE / "k179_matched_normal_order_coefficient_family.py"
    spec = importlib.util.spec_from_file_location("k179_for_k568", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K179 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(), parse_float=Decimal)


def frac(value: Any) -> Fraction:
    return Fraction(value)


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def scientific(value: Fraction, digits: int = 17) -> str:
    with localcontext() as context:
        context.prec = digits + 12
        return f"{Decimal(value.numerator) / Decimal(value.denominator):.{digits}e}"


def group_id(term: dict[str, Any]) -> str:
    return f"seed={int(term['seed_impurity'])}|{term['output_signature']}"


def interval_sum(rows: Any) -> tuple[Fraction, Fraction]:
    values = rows.values() if isinstance(rows, dict) else rows
    lower = Fraction(0)
    upper = Fraction(0)
    for row in values:
        lower += frac(row[0])
        upper += frac(row[1])
    return lower, upper


def build() -> dict[str, Any]:
    k179 = load_k179()
    terms = [term for term in k179.coefficient_family() if 2 <= int(term["order"]) <= 6]
    by_order: dict[int, list[dict[str, Any]]] = {order: [] for order in range(2, 7)}
    for term in terms:
        by_order[int(term["order"])].append(term)
    data = {order: parse(path) for order, path in INPUTS.items()}

    k180 = data[2]["seedwise_exchange_vector"]
    order_intervals: dict[int, tuple[Fraction, Fraction]] = {
        2: (
            3 * frac(k180["norm_squared_lower"]),
            3 * frac(k180["norm_squared_upper"]),
        )
    }
    k181 = data[3]["seedwise_exchange_vectors"]
    order_intervals[3] = (
        frac(k181["seed_0_norm_squared_lower"]) + 2 * frac(k181["seed_1_and_2_norm_squared_lower"]),
        frac(k181["seed_0_norm_squared_upper"]) + 2 * frac(k181["seed_1_and_2_norm_squared_upper"]),
    )
    for order in (4, 5, 6):
        order_intervals[order] = interval_sum(data[order]["certified_coherent_norm_squared_intervals"])

    rows = []
    for order in range(2, 7):
        groups = Counter(group_id(term) for term in by_order[order])
        entry_count = sum(size * (size + 1) // 2 for size in groups.values())
        source_groups = None
        if order >= 4:
            source_groups = set(data[order]["certified_coherent_norm_squared_intervals"])
            if source_groups != set(groups):
                raise AssertionError(f"order {order} source group keys do not match K179")
        lower, upper = order_intervals[order]
        rows.append({
            "order": order,
            "resolved_vectors": len(by_order[order]),
            "coherent_groups": len(groups),
            "upper_triangle_gram_entries": entry_count,
            "group_size_histogram": {str(size): count for size, count in sorted(Counter(groups.values()).items())},
            "source": str(INPUTS[order].relative_to(ROOT)),
            "source_group_keys_replayed": source_groups is not None,
            "complete_norm_square_interval_exact": [q(lower), q(upper)],
            "complete_norm_square_interval_scientific": [scientific(lower), scientific(upper)],
            "interval_nonnegative_and_ordered": Fraction(0) <= lower <= upper,
        })

    total_lower = sum((Fraction(row["complete_norm_square_interval_exact"][0]) for row in rows), Fraction(0))
    total_upper = sum((Fraction(row["complete_norm_square_interval_exact"][1]) for row in rows), Fraction(0))
    return {
        "schema_version": "1.0",
        "result_id": "K568-LOWER-ORDER-FINITE-GRAM-RECONCILIATION",
        "created": "2026-09-28",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "scope": "Complete reconciliation of K179 orders two through six against K180--K184's certified coherent norm-square intervals.",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in INPUTS.values()],
            "resolved_vectors": sum(row["resolved_vectors"] for row in rows),
            "coherent_groups": sum(row["coherent_groups"] for row in rows),
            "upper_triangle_gram_entries": sum(row["upper_triangle_gram_entries"] for row in rows),
            "orders": [2, 3, 4, 5, 6],
        },
        "order_reconciliation": rows,
        "lower_order_finite_square": {
            "interval_exact": [q(total_lower), q(total_upper)],
            "interval_scientific": [scientific(total_lower), scientific(total_upper)],
            "all_352_entries_reconciled": sum(row["upper_triangle_gram_entries"] for row in rows) == 352,
            "cross_terms_retained_inside_coherent_group_intervals": True,
        },
        "decision": {
            "orders_two_through_six_numerically_complete": True,
            "full_Q_12_emitted": False,
            "complete_M_dual_residual_emitted": False,
            "K152_shifted_form_dual_residual_emitted": False,
            "next_exact_input": "compose these 352 entries with the complete order-seven-through-twelve enclosures into the full 59,586-entry finite square",
        },
        "release_test": {
            "all_142_lower_order_vectors_retained": sum(row["resolved_vectors"] for row in rows) == 142,
            "all_57_lower_order_groups_retained": sum(row["coherent_groups"] for row in rows) == 57,
            "all_352_lower_order_entries_retained": sum(row["upper_triangle_gram_entries"] for row in rows) == 352,
            "all_source_group_keys_replayed_where_explicit": all(row["source_group_keys_replayed"] for row in rows if row["order"] >= 4),
            "all_intervals_nonnegative_and_ordered": all(row["interval_nonnegative_and_ordered"] for row in rows),
            "full_Q_12_not_overclaimed": True,
            "K152_not_overclaimed": True,
        },
        "ledger_effect": {
            "LT-SM8": "NEEDS_UNCHANGED",
            "LT-GR6b": "NEEDS_UNCHANGED",
            "RA-F1": "NEEDS_UNCHANGED",
            "AC-F1": "NEEDS_UNCHANGED",
        },
        "source_routing": "SC-ACT-01/02/06 ASSERTS and SC-META-53 UNCERTAIN remain unchanged.",
        "claim_ceiling": "Complete exact aggregation of the already certified K180--K184 order-two-through-six coherent norm-square intervals, with K179's 142 vectors, 57 groups and 352 upper-triangle entries replayed. This does not yet compose the full Q_12, evaluate the complete residual, transfer to K152's shifted metric, or move source, ledger, canon, paper, public, novelty or physical claims.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["resolved_vectors"], fixed["coherent_groups"], fixed["upper_triangle_gram_entries"], fixed["orders"]) != (142, 57, 352, [2, 3, 4, 5, 6]):
        raise AssertionError("K568 lower-order census changed")
    if len(payload["order_reconciliation"]) != 5:
        raise AssertionError("K568 order bank changed")
    for row in payload["order_reconciliation"]:
        lo, hi = (Fraction(value) for value in row["complete_norm_square_interval_exact"])
        if lo < 0 or lo > hi or not row["interval_nonnegative_and_ordered"]:
            raise AssertionError("K568 interval changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K568 release boundary changed")
    decision = payload["decision"]
    if not decision["orders_two_through_six_numerically_complete"] or any(decision[key] for key in ("full_Q_12_emitted", "complete_M_dual_residual_emitted", "K152_shifted_form_dual_residual_emitted")):
        raise AssertionError("K568 decision boundary changed")


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
