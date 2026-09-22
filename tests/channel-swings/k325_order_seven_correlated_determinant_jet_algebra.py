#!/usr/bin/env python3
"""Exact correlation-preserving algebra for K315 bordered determinant jets.

The K324 value bank cannot be differentiated by independently bounding its
twenty replacement families.  This compiler keeps one shared generator for
every entry jet, forms the complete bordered determinant polynomial first,
and only then exposes its value, first and second coefficients.  The resulting
second derivative is exactly the five pure replacements plus the ten doubled
cross replacements from K315.
"""

from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K315 = ROOT / "lab/process/k315-order-seven-terminal-bordered-adapter.json"
K319 = ROOT / "lab/process/k319-order-seven-weighted-chart-composition.json"
K324 = ROOT / "lab/process/k324-order-seven-complete-value-chart-bank.json"
OUTPUT = ROOT / "lab/process/k325-order-seven-correlated-determinant-jet-algebra.json"
SIZE = 5

# Sparse exact polynomial: a monomial is a sorted tuple of generator names.
Poly = dict[tuple[str, ...], Fraction]


def add(left: Poly, right: Poly) -> Poly:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, Fraction(0)) + coefficient
        if not result[monomial]:
            del result[monomial]
    return result


def scale(poly: Poly, coefficient: Fraction | int) -> Poly:
    coefficient = Fraction(coefficient)
    return {monomial: coefficient * value for monomial, value in poly.items() if coefficient * value}


def multiply(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            result[monomial] = result.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
            if not result[monomial]:
                del result[monomial]
    return result


def structurally_nonzero(row: int, column: int) -> bool:
    if row == 4:
        return column < 3
    if column == 4:
        return row < 3
    return True


def generator(row: int, column: int, order: int) -> Poly:
    if not structurally_nonzero(row, column):
        return {}
    return {(f"g_r{row}c{column}d{order}",): Fraction(1)}


def determinant_for_orders(column_orders: tuple[int, ...]) -> Poly:
    total: Poly = {}
    for permutation in itertools.permutations(range(SIZE)):
        if not all(structurally_nonzero(row, column) for row, column in enumerate(permutation)):
            continue
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(SIZE)
            for right in range(left + 1, SIZE)
        )
        term: Poly = {(): Fraction(-1 if inversions % 2 else 1)}
        for row, column in enumerate(permutation):
            term = multiply(term, generator(row, column, column_orders[column]))
        total = add(total, term)
    return total


def replacement_coefficients() -> tuple[Poly, Poly, Poly, list[dict[str, Any]]]:
    value = determinant_for_orders((0, 0, 0, 0, 0))
    first: Poly = {}
    second: Poly = {}
    family_rows = []
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
    for name, orders, multiplicity in specifications:
        poly = determinant_for_orders(orders)
        weighted = scale(poly, multiplicity)
        if name.startswith("first_"):
            first = add(first, weighted)
        elif name.startswith("second_"):
            second = add(second, weighted)
        family_rows.append(
            {
                "family": name,
                "column_orders": list(orders),
                "outer_multiplicity": multiplicity,
                "nonzero_determinant_monomials": len(poly),
                "weighted_polynomial_terms": len(weighted),
            }
        )
    return value, first, second, family_rows


def determinant_t_polynomial() -> dict[int, Poly]:
    """Expand det(C_j0+t*C_j1+t^2*C_j2/2) through degree ten."""
    total: dict[int, Poly] = {}
    for permutation in itertools.permutations(range(SIZE)):
        if not all(structurally_nonzero(row, column) for row, column in enumerate(permutation)):
            continue
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(SIZE)
            for right in range(left + 1, SIZE)
        )
        term: dict[int, Poly] = {0: {(): Fraction(-1 if inversions % 2 else 1)}}
        for row, column in enumerate(permutation):
            entry = {
                0: generator(row, column, 0),
                1: generator(row, column, 1),
                2: scale(generator(row, column, 2), Fraction(1, 2)),
            }
            product: dict[int, Poly] = {}
            for left_degree, left_poly in term.items():
                for right_degree, right_poly in entry.items():
                    degree = left_degree + right_degree
                    product[degree] = add(product.get(degree, {}), multiply(left_poly, right_poly))
            term = product
        for degree, poly in term.items():
            total[degree] = add(total.get(degree, {}), poly)
    return total


def evaluate(poly: Poly, values: dict[str, Fraction]) -> Fraction:
    total = Fraction(0)
    for monomial, coefficient in poly.items():
        term = coefficient
        for name in monomial:
            term *= values.get(name, Fraction(0))
        total += term
    return total


def cancellation_witness(families: list[dict[str, Any]]) -> dict[str, Any]:
    # Invertible bordered base with literal zeros.  Columns 0 and 1 are scaled
    # by 1+t and 1-t+t^2.  Thus det A(t)=det A(0)*(1+t^3), so the complete
    # second derivative vanishes although one pure and one doubled-cross
    # family are individually nonzero.
    base = [[Fraction(row == column) for column in range(SIZE)] for row in range(SIZE)]
    base[4][4] = Fraction(0)
    base[0][4] = Fraction(1)
    base[4][0] = Fraction(1)
    values: dict[str, Fraction] = {}
    for row in range(SIZE):
        for column in range(SIZE):
            if not structurally_nonzero(row, column):
                continue
            base_value = base[row][column]
            values[f"g_r{row}c{column}d0"] = base_value
            values[f"g_r{row}c{column}d1"] = base_value if column == 0 else (-base_value if column == 1 else Fraction(0))
            values[f"g_r{row}c{column}d2"] = 2 * base_value if column == 1 else Fraction(0)

    contributions = []
    for family in families:
        if not family["family"].startswith("second_"):
            continue
        orders = tuple(family["column_orders"])
        value = family["outer_multiplicity"] * evaluate(determinant_for_orders(orders), values)
        contributions.append({"family": family["family"], "signed_value": str(value)})
    signed_sum = sum(Fraction(row["signed_value"]) for row in contributions)
    familywise_abs_sum = sum(abs(Fraction(row["signed_value"])) for row in contributions)
    return {
        "base_determinant": str(evaluate(determinant_for_orders((0, 0, 0, 0, 0)), values)),
        "determinant_path": "det(A(t))=det(A(0))*(1+t)*(1-t+t^2)=det(A(0))*(1+t^3)",
        "nonzero_second_family_contributions": [row for row in contributions if Fraction(row["signed_value"])],
        "complete_signed_second_derivative": str(signed_sum),
        "familywise_absolute_sum": str(familywise_abs_sum),
        "post_assembly_strictly_tighter": abs(signed_sum) < familywise_abs_sum,
    }


def build() -> dict[str, Any]:
    k315 = json.loads(K315.read_text())
    k319 = json.loads(K319.read_text())
    k324 = json.loads(K324.read_text())
    value, first, second, families = replacement_coefficients()
    path = determinant_t_polynomial()
    if path.get(0) != value or path.get(1) != first or scale(path.get(2, {}), 2) != second:
        raise AssertionError("complete determinant Taylor coefficients do not replay K315 replacements")
    if [row["family"] for row in families] != [row["family"] for row in k315["complete_column_replacement_expansion"]]:
        raise AssertionError("K315 family order changed")
    if any(row["nonzero_determinant_monomials"] != 54 for row in families):
        raise AssertionError("bordered determinant monomial census changed")
    witness = cancellation_witness(families)
    if not witness["post_assembly_strictly_tighter"]:
        raise AssertionError("shared-generator cancellation witness failed")
    weighted = sum(row["outer_multiplicity"] * row["nonzero_determinant_monomials"] for row in families)
    return {
        "schema_version": "1.0",
        "result_id": "K325-ORDER-SEVEN-CORRELATED-DETERMINANT-JET-ALGEBRA",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k315-order-seven-terminal-bordered-adapter.json",
                "lab/process/k319-order-seven-weighted-chart-composition.json",
                "lab/process/k324-order-seven-complete-value-chart-bank.json",
            ],
            "bordered_matrix_size": SIZE,
            "family_count": len(families),
            "first_family_count": sum(row["family"].startswith("first_") for row in families),
            "second_pure_family_count": sum(row["family"].startswith("second_pure_") for row in families),
            "second_cross_family_count": sum(row["family"].startswith("second_cross_") for row in families),
            "literal_zero_slots": [[3, 4], [4, 3], [4, 4]],
        },
        "shared_generator_contract": {
            "entry_jet": "g_r{row}c{column}d{order}",
            "column_path": "C_j(t)=C_j0+t*C_j1+t^2*C_j2/2",
            "enclosure_order": "assemble exact coherent determinant coefficient in shared generators; substitute chart intervals; enclose once",
            "early_familywise_absolute_enclosure_forbidden": True,
            "detached_cofactor_used": False,
            "literal_border_zeros_retained": True,
            "value_coefficient_exact": path.get(0) == value,
            "first_coefficient_exact": path.get(1) == first,
            "second_derivative_coefficient_exact": scale(path.get(2, {}), 2) == second,
        },
        "family_replay": families,
        "census": {
            "unweighted_family_monomials": sum(row["nonzero_determinant_monomials"] for row in families),
            "cross_weighted_family_monomials": weighted,
            "K315_cross_weighted_census_replayed": weighted == k315["census"]["weighted_nonzero_monomials_after_cross_factors"] == 1674,
            "K319_all_fifteen_second_families_replayed": sum(row["family"].startswith("second_") for row in families) == 15,
            "K324_value_bank_available": k324["decision"]["all_sixteen_value_charts_bounded"],
        },
        "correlation_control": witness,
        "decision": {
            "correlation_preserving_determinant_jet_algebra_implemented": True,
            "all_five_first_families_exact": True,
            "all_fifteen_second_families_exact": True,
            "factor_two_cross_terms_exact": True,
            "fixed_slab_derivative_interval_bank_emitted": False,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_transfer_released": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "substitute chart-specific shared entry-jet intervals into the K325 polynomial before one post-assembly enclosure on each K318 chart, then extend across radial/projective subdivisions",
        },
        "release_test": {
            "K315_family_order_exact": [row["family"] for row in families] == [row["family"] for row in k315["complete_column_replacement_expansion"]],
            "all_54_monomial_families_exact": all(row["nonzero_determinant_monomials"] == 54 for row in families),
            "Taylor_and_replacement_forms_identical": True,
            "cancellation_survives_until_post_assembly": witness["post_assembly_strictly_tighter"],
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k319["ledger_effect"],
        "source_routing": k319["source_routing"],
        "claim_ceiling": "Exact shared-generator algebra for the complete five-by-five bordered determinant jet. Its Taylor coefficients reproduce K315's value, five first, five pure-second and ten doubled-cross families with every literal border zero retained. A bordered cancellation control has zero assembled second derivative while familywise absolute summation is four, proving that enclosure must follow coherent assembly. This supplies the missing correlation contract but no chart-specific first/second interval constants, complete y-master sum, gap-axis transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["family_count"] != 21 or (fixed["first_family_count"], fixed["second_pure_family_count"], fixed["second_cross_family_count"]) != (5, 5, 10):
        raise AssertionError("jet family census changed")
    if fixed["literal_zero_slots"] != [[3, 4], [4, 3], [4, 4]]:
        raise AssertionError("literal bordered zeros changed")
    contract = payload["shared_generator_contract"]
    if not all(contract[key] for key in ("early_familywise_absolute_enclosure_forbidden", "literal_border_zeros_retained", "value_coefficient_exact", "first_coefficient_exact", "second_derivative_coefficient_exact")):
        raise AssertionError("correlation contract incomplete")
    if contract["detached_cofactor_used"]:
        raise AssertionError("detached cofactor introduced")
    if not payload["census"]["K315_cross_weighted_census_replayed"] or not payload["census"]["K319_all_fifteen_second_families_replayed"]:
        raise AssertionError("predecessor census not replayed")
    witness = payload["correlation_control"]
    if witness["complete_signed_second_derivative"] != "0" or witness["familywise_absolute_sum"] != "4" or not witness["post_assembly_strictly_tighter"]:
        raise AssertionError("correlation witness changed")
    decision = payload["decision"]
    if decision["fixed_slab_derivative_interval_bank_emitted"] or decision["complete_y_master_constant_emitted"]:
        raise AssertionError("numerical derivative bank overclaimed")


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
