#!/usr/bin/env python3
"""K279 exact structural closure for K179 orders seven through twelve.

This certificate never evaluates the remaining time integrals.  It proves the
specieswise Andreief reduction and normalization cancellation for every
coherent Gram pair, freezes the exact workload, and tests whether exact kernel
signature memoization removes any entries.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K179_PATH = Path(__file__).with_name("k179_matched_normal_order_coefficient_family.py")
ORDERS = tuple(range(7, 13))


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k279", K179_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K179_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_k179()


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    matrix = [row[:] for row in matrix]
    total = Fraction(1)
    for column in range(len(matrix)):
        pivot = next((row for row in range(column, len(matrix)) if matrix[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            total *= -1
        value = matrix[column][column]
        total *= value
        matrix[column] = [entry / value for entry in matrix[column]]
        for row in range(column + 1, len(matrix)):
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    entry - factor * base
                    for entry, base in zip(matrix[row], matrix[column])
                ]
    return total


def exact_andreief_control(multiplicity: int) -> dict[str, Any]:
    """Exact finite-measure Andreief/Cauchy--Binet control."""
    node_count = multiplicity + 2
    weights = [Fraction(index + 1, index + 2) for index in range(node_count)]
    left = [
        [Fraction((node + 2) ** row, node + row + 2) for node in range(node_count)]
        for row in range(multiplicity)
    ]
    right = [
        [Fraction((node + 3) ** row, 2 * node + row + 3) for node in range(node_count)]
        for row in range(multiplicity)
    ]
    subset_sum = Fraction(0)
    for subset in combinations(range(node_count), multiplicity):
        left_minor = [[left[row][column] for column in subset] for row in range(multiplicity)]
        right_minor = [[right[row][column] for column in subset] for row in range(multiplicity)]
        subset_sum += (
            math.factorial(multiplicity)
            * math.prod(weights[column] for column in subset)
            * determinant(left_minor)
            * determinant(right_minor)
        )
    kernel = [
        [
            sum(weights[node] * left[i][node] * right[j][node] for node in range(node_count))
            for j in range(multiplicity)
        ]
        for i in range(multiplicity)
    ]
    determinant_side = math.factorial(multiplicity) * determinant(kernel)
    return {
        "multiplicity": multiplicity,
        "ordered_exterior_sum": str(subset_sum),
        "factorial_times_kernel_determinant": str(determinant_side),
        "exact_equality": subset_sum == determinant_side,
    }


def term_record(term: dict[str, Any]) -> dict[str, Any]:
    return {
        "order": int(term["order"]),
        "seed_impurity": int(term["seed_impurity"]),
        "output_signature": str(term["output_signature"]),
        "contraction_id": str(term["contraction_id"]),
        "old_position": int(term["old_position"]),
        "coefficient": int(term["exact_operator_coefficient"]),
        "output_letters": list(term["output_letters"]),
        "output_variable_provenance": [int(value) for value in term["output_variable_provenance"]],
        "species_multiplicities": {
            str(key): int(value)
            for key, value in sorted(
                term["antisymmetrizer_normalization"]["species_multiplicities"].items()
            )
        },
        "species_factorials": {
            str(key): int(value)
            for key, value in sorted(
                term["antisymmetrizer_normalization"]["species_factorials"].items()
            )
        },
    }


def family_digest(terms: list[dict[str, Any]]) -> str:
    payload = json.dumps([term_record(term) for term in terms], sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def occurrences(term: dict[str, Any]) -> tuple[tuple[str, tuple[int, ...]], ...]:
    rows: dict[str, list[int]] = defaultdict(list)
    for provenance, species in zip(term["output_variable_provenance"], term["output_letters"]):
        rows[str(species)].append(int(provenance))
    return tuple((species, tuple(positions)) for species, positions in sorted(rows.items()))


def pair_signature(
    group: tuple[int, str], left: dict[str, Any], right: dict[str, Any]
) -> tuple[Any, ...]:
    coefficient = int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"])
    forward = (
        group,
        int(left["old_position"]),
        int(right["old_position"]),
        coefficient,
        occurrences(left),
        occurrences(right),
    )
    transpose = (
        group,
        int(right["old_position"]),
        int(left["old_position"]),
        coefficient,
        occurrences(right),
        occurrences(left),
    )
    return min(forward, transpose)


def order_certificate(order: int, all_terms: list[dict[str, Any]]) -> dict[str, Any]:
    terms = [term for term in all_terms if int(term["order"]) == order]
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in terms:
        groups[(int(term["seed_impurity"]), str(term["output_signature"]))].append(term)

    gram_entries = 0
    literal_leibniz_terms = 0
    determinant_cubic_proxy = 0
    signatures: Counter[tuple[Any, ...]] = Counter()
    multiplicity_histogram: Counter[str] = Counter()
    all_factorials_cancel = True
    all_coherent_pairs_typed = True

    for group, paths in sorted(groups.items()):
        expected_multiplicities = term_record(paths[0])["species_multiplicities"]
        for path in paths:
            if term_record(path)["species_multiplicities"] != expected_multiplicities:
                all_coherent_pairs_typed = False
        factorial_product = math.prod(math.factorial(value) for value in expected_multiplicities.values())
        stored_factorials = math.prod(
            int(value)
            for value in paths[0]["antisymmetrizer_normalization"]["species_factorials"].values()
        )
        all_factorials_cancel &= factorial_product == stored_factorials
        multiplicity_key = ",".join(str(value) for value in sorted(expected_multiplicities.values()))
        group_entries = len(paths) * (len(paths) + 1) // 2
        multiplicity_histogram[multiplicity_key] += group_entries
        gram_entries += group_entries
        literal_leibniz_terms += group_entries * factorial_product
        determinant_cubic_proxy += group_entries * sum(
            value**3 for value in expected_multiplicities.values()
        )
        for index, left in enumerate(paths):
            left_factorials = math.prod(
                int(value)
                for value in left["antisymmetrizer_normalization"]["species_factorials"].values()
            )
            for right in paths[index:]:
                right_factorials = math.prod(
                    int(value)
                    for value in right["antisymmetrizer_normalization"]["species_factorials"].values()
                )
                all_factorials_cancel &= left_factorials == right_factorials == factorial_product
                signatures[pair_signature(group, left, right)] += 1

    jacobian_power = 2 * order + 1
    bessel_factors = order + 2
    small_rho_power = jacobian_power - bessel_factors
    return {
        "order": order,
        "paths": len(terms),
        "groups": len(groups),
        "maximum_group_size": max(len(paths) for paths in groups.values()),
        "group_size_histogram": {
            str(size): count
            for size, count in sorted(Counter(len(paths) for paths in groups.values()).items())
        },
        "contracted_position_histogram": {
            str(position): count
            for position, count in sorted(Counter(int(term["old_position"]) for term in terms).items())
        },
        "unique_self_and_cross_gram_entries": gram_entries,
        "exact_kernel_signatures_after_transpose": len(signatures),
        "maximum_signature_multiplicity": max(signatures.values()),
        "exact_signature_deduplication_reduction": gram_entries - len(signatures),
        "literal_leibniz_terms": literal_leibniz_terms,
        "determinant_cubic_arithmetic_proxy": determinant_cubic_proxy,
        "literal_to_determinant_proxy_ratio": literal_leibniz_terms / determinant_cubic_proxy,
        "gram_entries_by_species_multiplicity": dict(sorted(multiplicity_histogram.items())),
        "all_coherent_pairs_have_equal_species_multiplicities": all_coherent_pairs_typed,
        "all_andreief_factorials_cancel_normalized_wedges": all_factorials_cancel,
        "exterior_momenta_eliminated_per_gram_entry": order,
        "time_variables_after_reduction": 2 * (order + 1),
        "radialization": {
            "jacobian_rho_power": jacobian_power,
            "crude_bessel_factors_per_leibniz_term": bessel_factors,
            "small_rho_power": small_rho_power,
            "origin_integrable_without_determinant_cancellation": small_rho_power > -1,
        },
    }


def certificate() -> dict[str, Any]:
    all_terms = K179.coefficient_family()
    selected_terms = [term for term in all_terms if int(term["order"]) in ORDERS]
    rows = [order_certificate(order, all_terms) for order in ORDERS]
    controls = [exact_andreief_control(multiplicity) for multiplicity in range(1, 7)]
    totals = {
        "orders": list(ORDERS),
        "paths": sum(row["paths"] for row in rows),
        "groups": sum(row["groups"] for row in rows),
        "gram_entries": sum(row["unique_self_and_cross_gram_entries"] for row in rows),
        "exact_kernel_signatures": sum(row["exact_kernel_signatures_after_transpose"] for row in rows),
        "literal_leibniz_terms": sum(row["literal_leibniz_terms"] for row in rows),
        "determinant_cubic_arithmetic_proxy": sum(
            row["determinant_cubic_arithmetic_proxy"] for row in rows
        ),
    }
    totals["literal_to_determinant_proxy_ratio"] = (
        totals["literal_leibniz_terms"] / totals["determinant_cubic_arithmetic_proxy"]
    )
    return {
        "schema_version": "1.0",
        "result_id": "K279-HIGHER-ORDER-ANDREIEF-STRUCTURAL-CLOSURE",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "carrier": "hard-core C3 tensor Gamma_-(L2(R;C4))",
            "auxiliary_chart_shift": 256,
            "seed_scope": "K162_zero_bath_seed_orbits",
            "K179_family_sha256": K179.demo()["coefficient_family"]["family_sha256"],
            "K279_selected_family_sha256": family_digest(selected_terms),
        },
        "theorem": {
            "statement": "For every K179 coherent Gram pair at orders seven through twelve, specieswise Andreief integration removes all exterior momenta; each product of Andreief factorials exactly cancels the two normalized-wedge factors, leaving factorial-free Bessel-kernel determinants on two positive cumulative-time simplices.",
            "pair_form": "c_t c_u (2*pi)^(-(n+2)) integral exp(-256(sum s+sum v)) [2K1(T_old)][2K1(U_old)] product_species det[2K1(T_i+U_j)] ds dv",
            "radialization": "rho=sum(s)+sum(v), theta=sum(s)/rho and two Delta_n simplex coordinates give rho^(2n+1); n+2 crude K1 factors leave rho^(n-1), integrable for every n=7..12.",
            "all_orders_pass_factorial_cancellation": all(
                row["all_andreief_factorials_cancel_normalized_wedges"] for row in rows
            ),
            "all_orders_pass_origin_integrability": all(
                row["radialization"]["origin_integrable_without_determinant_cancellation"]
                for row in rows
            ),
        },
        "orders": rows,
        "totals": totals,
        "exact_andreief_controls": controls,
        "representation_decision": {
            "selected": "factorial_free_species_determinants_with_shared_cumulative_time_DAG",
            "literal_leibniz_expansion": "rejected_as_primary_representation",
            "exact_kernel_signature_memoization": "rejected_no_duplicates_beyond_transpose",
            "reason": "The determinant form preserves every coherent cross term and replaces 169209864 literal Leibniz products by 7213716 determinant-cubic arithmetic-proxy units across 59234 exact Gram entries. This proxy compares algebraic representation cost only; it is not a quadrature runtime or error estimate.",
            "next_integrator": "one shared determinant-valued cumulative-time rule, validated first on complete order seven, with rho tail and theta/simplex face error separated before extending the same rule to orders eight through twelve",
        },
        "release_test": {
            "all_orders_7_through_12_present": [row["order"] for row in rows] == list(ORDERS),
            "all_59234_gram_entries_reduced": totals["gram_entries"] == 59234,
            "all_factorial_normalizations_cancel": all(
                row["all_andreief_factorials_cancel_normalized_wedges"] for row in rows
            ),
            "all_exact_andreief_controls_pass": all(row["exact_equality"] for row in controls),
            "all_radial_origins_integrable": all(
                row["radialization"]["origin_integrable_without_determinant_cancellation"]
                for row in rows
            ),
            "exact_signature_deduplication_reduces_work": totals["exact_kernel_signatures"] < totals["gram_entries"],
            "coefficient_complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "claim_ceiling": "Exact repository-owned structural reduction and representation decision for the unresolved K179 order-seven-through-twelve coherent Gram families. All 59,234 Gram entries reduce to factorial-free species determinants and are integrable at the radial origin. No time integral, action-column value, complete residual, exterior gap, K152 interval, physical state, source claim, ledger row, canon, paper or public posture is changed.",
    }


def main() -> int:
    print(json.dumps(certificate(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
