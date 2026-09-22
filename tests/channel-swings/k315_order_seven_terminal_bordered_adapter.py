#!/usr/bin/env python3
"""Compile K311 terminal budgets into complete bordered determinant jets.

The only jointly terminal core entry is row 3, column 3 of the regularized
four-by-four core inside the five-by-five bordered determinant.  This compiler
enumerates the complete K305/K308 column-replacement formula first and tags
that entry inside every nonzero determinant monomial.  K311's B0/B1/B2 budget
is then assigned according to the derivative order of column 3.  No detached
cofactor or occurrencewise coherent absolute value is introduced.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K305 = ROOT / "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json"
K308 = ROOT / "lab/process/k308-order-seven-regularized-y-master-operator.json"
K311 = ROOT / "lab/process/k311-order-seven-terminal-radial-join.json"
K314 = ROOT / "lab/process/k314-order-seven-projective-face-oracle.json"
OUTPUT = ROOT / "lab/process/k315-order-seven-terminal-bordered-adapter.json"

SIZE = 5
TERMINAL_SLOT = (3, 3)


def structurally_nonzero(row: int, column: int) -> bool:
    if row == 4:
        return column < 3
    if column == 4:
        return row < 3
    return True


def determinant_monomials(column_orders: tuple[int, ...], multiplicity: int) -> list[dict[str, Any]]:
    rows = []
    for permutation in itertools.permutations(range(SIZE)):
        if not all(structurally_nonzero(row, column) for row, column in enumerate(permutation)):
            continue
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(SIZE)
            for j in range(i + 1, SIZE)
        )
        terminal = permutation[TERMINAL_SLOT[0]] == TERMINAL_SLOT[1]
        rows.append({
            "permutation": list(permutation),
            "sign": -1 if inversions % 2 else 1,
            "multiplicity": multiplicity,
            "column_orders": list(column_orders),
            "contains_terminal_slot": terminal,
            "terminal_jet_order": column_orders[TERMINAL_SLOT[1]] if terminal else None,
        })
    return rows


def complete_jet_expansion() -> list[dict[str, Any]]:
    expansion = []
    specifications = [("value", (0, 0, 0, 0, 0), 1)]
    specifications.extend(
        (f"first_c{column}", tuple(1 if index == column else 0 for index in range(SIZE)), 1)
        for column in range(SIZE)
    )
    specifications.extend(
        (f"second_pure_c{column}", tuple(2 if index == column else 0 for index in range(SIZE)), 1)
        for column in range(SIZE)
    )
    specifications.extend(
        (
            f"second_cross_c{left}_c{right}",
            tuple(1 if index in (left, right) else 0 for index in range(SIZE)),
            2,
        )
        for left, right in itertools.combinations(range(SIZE), 2)
    )
    for family, orders, multiplicity in specifications:
        rows = determinant_monomials(orders, multiplicity)
        expansion.append({
            "family": family,
            "column_orders": list(orders),
            "outer_multiplicity": multiplicity,
            "nonzero_determinant_monomials": len(rows),
            "terminal_monomials": sum(row["contains_terminal_slot"] for row in rows),
            "terminal_jet_histogram": {
                str(key): value
                for key, value in sorted(Counter(
                    row["terminal_jet_order"] for row in rows if row["contains_terminal_slot"]
                ).items())
            },
            "monomials": rows,
        })
    return expansion


def build() -> dict[str, Any]:
    k305 = json.loads(K305.read_text())
    k308 = json.loads(K308.read_text())
    k311 = json.loads(K311.read_text())
    k314 = json.loads(K314.read_text())
    if k308["outward_positive_cell"]["column_replacement_counts"] != {
        "value": 1, "first": 5, "second_pure": 5, "second_cross": 10
    }:
        raise AssertionError("K308 column replacement census changed")
    if not k314["decision"]["all_six_repeated_node_faces_have_finite_regularizer_bounds"]:
        raise AssertionError("K314 face oracle unavailable")

    expansion = complete_jet_expansion()
    if len(expansion) != 21:
        raise AssertionError("complete determinant jet expansion changed")
    weighted_histogram = Counter()
    unweighted_histogram = Counter()
    total_weighted = 0
    total_unweighted = 0
    for family in expansion:
        for row in family["monomials"]:
            total_unweighted += 1
            total_weighted += row["multiplicity"]
            if row["contains_terminal_slot"]:
                unweighted_histogram[row["terminal_jet_order"]] += 1
                weighted_histogram[row["terminal_jet_order"]] += row["multiplicity"]

    budgets = {
        int(row["jet"][1]): Fraction(row["upper_fraction"])
        for row in k311["terminal_weighted_radial_budgets"]
    }
    if set(budgets) != {0, 1, 2}:
        raise AssertionError("K311 terminal budget order changed")
    checksum = sum(weighted_histogram[order] * budgets[order] for order in budgets)

    return {
        "schema_version": "1.0",
        "result_id": "K315-ORDER-SEVEN-TERMINAL-BORDERED-ADAPTER",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json",
                "lab/process/k308-order-seven-regularized-y-master-operator.json",
                "lab/process/k311-order-seven-terminal-radial-join.json",
                "lab/process/k314-order-seven-projective-face-oracle.json",
            ],
            "bordered_matrix_size": SIZE,
            "terminal_core_slot": list(TERMINAL_SLOT),
            "determinant_jet_families": len(expansion),
            "column_replacement_counts": k308["outward_positive_cell"]["column_replacement_counts"],
            "coherent_groups": k305["fixed_control"]["coherent_groups"],
        },
        "terminal_typing": {
            "native_entry": "2*K1(x*(y*(1-u3)+(1-y)*(1-z3)))",
            "regularized_location": "row 3 column 3 of the four-by-four core inside the complete five-by-five bordered determinant",
            "only_joint_terminal_singularity": True,
            "literal_border_zeros": {"row3_column4": True, "row4_column3": True, "row4_column4": True},
            "terminal_bounds": k311["fixed_control"]["terminal_bounds"],
        },
        "complete_column_replacement_expansion": expansion,
        "census": {
            "unweighted_nonzero_monomials": total_unweighted,
            "weighted_nonzero_monomials_after_cross_factors": total_weighted,
            "terminal_monomials_by_jet_order_unweighted": {
                str(key): value for key, value in sorted(unweighted_histogram.items())
            },
            "terminal_monomials_by_jet_order_with_cross_factors": {
                str(key): value for key, value in sorted(weighted_histogram.items())
            },
            "K311_budget_multiplicity_checksum_fraction": str(checksum),
            "K311_budget_multiplicity_checksum_decimal": repr(float(checksum)),
            "checksum_role": "combinatorial completeness control only; other regularized entries remain inside each determinant monomial and this is not a standalone numerical norm",
        },
        "composition_rule": {
            "order": "enumerate each complete bordered determinant column-replacement monomial, then apply B_m only when that monomial contains the native terminal slot",
            "terminal_order_source": "the derivative order carried by column 3 in that complete monomial",
            "nonterminal_remainder": "monomials not containing row3-column3 stay pointwise regular on u3=z3=1 and remain in the K314/K313 outward oracle",
            "detached_cofactor_bound_used": False,
            "occurrencewise_coherent_absolute_values_used": False,
            "complete_bordered_assembly_retained": True,
        },
        "decision": {
            "K311_inserted_into_all_complete_bordered_jet_monomials": True,
            "orders_zero_one_two_all_covered": set(weighted_histogram) == {0, 1, 2},
            "terminal_split_cutoff_required": False,
            "terminal_monomial_census_complete": True,
            "complete_terminal_numerical_constant_emitted": False,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_constants_emitted": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "bound the remaining regularized entries in each tagged determinant monomial with the same r^27/projective cell scaling, then multiply the complete termwise terminal budgets by K312's positive measure and sum the y master",
        },
        "release_test": {
            "all_twenty_one_jet_families_enumerated": len(expansion) == 21,
            "all_nonzero_permutations_serialized": all(
                family["nonzero_determinant_monomials"] == len(family["monomials"])
                for family in expansion
            ),
            "terminal_orders_exactly_zero_one_two": set(weighted_histogram) == {0, 1, 2},
            "K311_all_three_budgets_consumed": set(budgets) == set(weighted_histogram),
            "cross_factor_two_retained": any(family["outer_multiplicity"] == 2 for family in expansion),
            "detached_cofactor_used": False,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k314["ledger_effect"],
        "source_routing": k314["source_routing"],
        "claim_ceiling": "Exact compiler that inserts K311's Peano-weighted B0/B1/B2 radial budgets into every complete nonzero monomial of K305/K308's value, first-y and second-y bordered determinant column-replacement formulas. It serializes all 21 jet families, retains factor-two cross terms and tags the joint terminal core entry only after the full coherent bordered assembly is formed. This proves that all terminal-containing monomials have a finite weighted adapter without a split cutoff. The other regularized entries have not yet been jointly multiplied and integrated on every K312 cell, so no complete terminal constant, y-master norm, five gap-axis constants, K294 gamma join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim is emitted.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["bordered_matrix_size"] != SIZE or fixed["terminal_core_slot"] != list(TERMINAL_SLOT):
        raise AssertionError("terminal slot typing changed")
    expansion = payload["complete_column_replacement_expansion"]
    if len(expansion) != 21:
        raise AssertionError("jet family census changed")
    rule = payload["composition_rule"]
    if rule["detached_cofactor_bound_used"] or rule["occurrencewise_coherent_absolute_values_used"]:
        raise AssertionError("forbidden terminal factorization introduced")
    if not rule["complete_bordered_assembly_retained"]:
        raise AssertionError("complete bordered assembly lost")
    decision = payload["decision"]
    if not decision["K311_inserted_into_all_complete_bordered_jet_monomials"]:
        raise AssertionError("K311 composition missing")
    if decision["terminal_split_cutoff_required"] or decision["complete_y_master_constant_emitted"]:
        raise AssertionError("terminal adapter overclaim")


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
