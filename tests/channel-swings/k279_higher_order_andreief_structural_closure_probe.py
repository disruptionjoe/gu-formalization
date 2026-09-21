#!/usr/bin/env python3
"""Independent replay and hostile controls for K279."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k279_higher_order_andreief_structural_closure.py")
K179_PATH = Path(__file__).with_name("k179_matched_normal_order_coefficient_family.py")
EXPECTED = {
    7: (96, 16, 408, 7920, 14664, 1),
    8: (192, 23, 1296, 58968, 61344, 1),
    9: (256, 20, 2368, 313344, 158784, 1),
    10: (480, 28, 6890, 2583072, 586700, 1),
    11: (640, 24, 12920, 16430400, 1461520, 1),
    12: (1152, 33, 35352, 149816160, 4930704, 1),
}


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k279_probe", K179_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K179_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def independent_counts(terms: list[dict[str, Any]], order: int) -> tuple[int, int, int, int, int]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in terms:
        if int(term["order"]) == order:
            groups[(int(term["seed_impurity"]), str(term["output_signature"]))].append(term)
    entries = literal = cubic = 0
    for paths in groups.values():
        count = len(paths) * (len(paths) + 1) // 2
        multiplicities = paths[0]["antisymmetrizer_normalization"]["species_multiplicities"]
        entries += count
        literal += count * math.prod(math.factorial(int(value)) for value in multiplicities.values())
        cubic += count * sum(int(value) ** 3 for value in multiplicities.values())
    return sum(map(len, groups.values())), len(groups), entries, literal, cubic


def structural_errors(terms: list[dict[str, Any]]) -> list[str]:
    errors = []
    for order, expected in EXPECTED.items():
        actual = independent_counts(terms, order)
        if actual != expected[:5]:
            errors.append(f"order {order} count mismatch: {actual} != {expected[:5]}")
        selected = [term for term in terms if int(term["order"]) == order]
        if any(int(term["old_position"]) % 2 != (order + 1) % 2 for term in selected):
            errors.append(f"order {order} contracted-position parity mismatch")
        for term in selected:
            multiplicities = {
                str(key): int(value)
                for key, value in term["antisymmetrizer_normalization"]["species_multiplicities"].items()
            }
            observed = Counter(str(value) for value in term["output_letters"])
            if multiplicities != dict(observed):
                errors.append(f"{term['contraction_id']} species multiplicity mismatch")
            factorials = {
                str(key): int(value)
                for key, value in term["antisymmetrizer_normalization"]["species_factorials"].items()
            }
            if factorials != {
                key: math.factorial(value) for key, value in multiplicities.items()
            }:
                errors.append(f"{term['contraction_id']} factorial mismatch")
            if sorted(int(value) for value in term["output_variable_provenance"]) != list(
                range(1, order + 2)
            )[: int(term["old_position"]) - 1] + list(
                range(1, order + 2)
            )[int(term["old_position"]):]:
                errors.append(f"{term['contraction_id']} provenance mismatch")
    return errors


def hostile_controls(terms: list[dict[str, Any]]) -> dict[str, bool]:
    mutations: dict[str, list[dict[str, Any]]] = {}
    mutations["deleted_order12_term"] = copy.deepcopy(terms[:-1])

    changed = copy.deepcopy(terms)
    target = next(term for term in changed if int(term["order"]) == 7)
    target["old_position"] = 1
    mutations["wrong_contracted_parity"] = changed

    changed = copy.deepcopy(terms)
    target = next(term for term in changed if int(term["order"]) == 8)
    target["output_signature"] += "__mutated"
    mutations["split_coherent_group"] = changed

    changed = copy.deepcopy(terms)
    target = next(term for term in changed if int(term["order"]) == 9)
    key = next(iter(target["antisymmetrizer_normalization"]["species_factorials"]))
    target["antisymmetrizer_normalization"]["species_factorials"][key] += 1
    mutations["wrong_wedge_factorial"] = changed

    changed = copy.deepcopy(terms)
    target = next(term for term in changed if int(term["order"]) == 10)
    target["output_variable_provenance"][0] = target["old_position"]
    mutations["contracted_variable_leak"] = changed

    return {name: bool(structural_errors(mutated)) for name, mutated in mutations.items()}


def main() -> int:
    producer = json.loads(subprocess.check_output([sys.executable, str(PRODUCER)], text=True))
    k179 = load_k179()
    terms = [term for term in k179.coefficient_family() if 7 <= int(term["order"]) <= 12]
    errors = structural_errors(terms)
    rows = {int(row["order"]): row for row in producer["orders"]}
    comparisons = {}
    for order, expected in EXPECTED.items():
        row = rows[order]
        actual = (
            row["paths"],
            row["groups"],
            row["unique_self_and_cross_gram_entries"],
            row["literal_leibniz_terms"],
            row["determinant_cubic_arithmetic_proxy"],
            row["maximum_signature_multiplicity"],
        )
        comparisons[str(order)] = actual == expected
    hostile = hostile_controls(terms)
    checks = {
        "independent_structural_replay": not errors,
        "producer_rows_match_hardcoded_replay": all(comparisons.values()),
        "producer_totals_match_replay": producer["totals"]["gram_entries"] == 59234
        and producer["totals"]["literal_leibniz_terms"] == 169209864
        and producer["totals"]["determinant_cubic_arithmetic_proxy"] == 7213716,
        "all_exact_andreief_controls_pass": all(
            row["exact_equality"] for row in producer["exact_andreief_controls"]
        ),
        "all_hostile_mutations_rejected": all(hostile.values()),
        "no_exact_signature_deduplication": producer["totals"]["exact_kernel_signatures"]
        == producer["totals"]["gram_entries"],
        "claim_ceiling_preserved": not producer["release_test"]["coefficient_complete_base_action_column_evaluated"]
        and not producer["release_test"]["native_K152_interval_emitted"],
    }
    payload = {
        "schema_version": "1.0",
        "producer_result_id": producer["result_id"],
        "checks": checks,
        "order_comparisons": comparisons,
        "hostile_controls": hostile,
        "structural_errors": errors,
        "pass_count": sum(checks.values()),
        "check_count": len(checks),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
