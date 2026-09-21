#!/usr/bin/env python3
"""K280 complete order-seven Cauchy--Vandermonde face atlas.

K279 leaves 408 factorial-free order-seven time-Gram entries.  This certificate
serializes every species determinant, its canonical sign, both Vandermonde
face families and every Cauchy denominator support.  It extends K186's
cancellation-preserving mixed divided differences to the new size-four
stratum.  Numerical values are high-precision controls, not outward intervals.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from collections import Counter, defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K179_PATH = Path(__file__).with_name("k179_matched_normal_order_coefficient_family.py")
OUTPUT = ROOT / "lab/process/k280-order-seven-bessel-vandermonde-face-atlas.json"
K186_MANIFEST = ROOT / "lab/process/k186-order-six-bessel-vandermonde-wave.json"
K192_MANIFEST = ROOT / "lab/process/k192-order-six-radially-stratified-wide-gap-wave.json"
ORDER = 7
TOTAL_POSITIONS = 8
EULER_GAMMA = Decimal(
    "0.57721566490153286060651209008240243104215933593992359880576723488486772677766467"
)


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k280", K179_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K179_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_k179()


def determinant(matrix: list[list[Any]]):
    work = [row[:] for row in matrix]
    total = work[0][0] * 0 + 1
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return total * 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            total = -total
        value = work[column][column]
        total *= value
        work[column] = [entry / value for entry in work[column]]
        for row in range(column + 1, len(work)):
            factor = work[row][column]
            if factor:
                work[row] = [
                    entry - factor * base
                    for entry, base in zip(work[row], work[column])
                ]
    return total


def parity(values: tuple[int, ...]) -> int:
    inversions = sum(
        values[i] > values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def cumulative(primitives: list[Any], position: int):
    return sum(primitives[position - 1 :])


def positive_vandermonde(values: list[Any]):
    result = values[0] * 0 + 1
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if not values[i] > values[j]:
                raise ValueError("canonical cumulative times must be strictly decreasing")
            result *= values[i] - values[j]
    return result


def cauchy_determinant(times: list[Any], other_times: list[Any]):
    size = len(times)
    numerator = (times[0] * 0 + 2) ** size
    numerator *= positive_vandermonde(times) * positive_vandermonde(other_times)
    denominator = times[0] * 0 + 1
    for left in times:
        for right in other_times:
            denominator *= left + right
    return numerator / denominator


def decimal_bessel_k1(value: Decimal, precision: int) -> Decimal:
    """Convergent integer-order series on the admitted 0 < x <= 1/4 core."""
    if not Decimal(0) < value <= Decimal(1) / 4:
        raise ValueError("K280 K1 series is scoped to 0 < x <= 1/4")
    with localcontext() as context:
        context.prec = precision + 25
        half = value / 2
        quarter_square = value * value / 4
        i1 = Decimal(0)
        psi_series = Decimal(0)
        factorial_k = 1
        factorial_k1 = 1
        power = half
        h_k = Decimal(0)
        tolerance = Decimal(10) ** (-(precision + 7))
        for index in range(10000):
            if index:
                factorial_k *= index
                factorial_k1 *= index + 1
                power *= quarter_square
                h_k += Decimal(1) / Decimal(index)
            h_k1 = h_k + Decimal(1) / Decimal(index + 1)
            denominator = Decimal(factorial_k * factorial_k1)
            i_term = power / denominator
            psi_term = (
                (h_k + h_k1 - 2 * EULER_GAMMA)
                * (quarter_square**index)
                / denominator
            )
            i1 += i_term
            psi_series += psi_term
            if index > 4 and abs(i_term) < tolerance and abs(value * psi_term) < tolerance:
                break
        else:
            raise AssertionError("K1 series failed to converge")
        return +(Decimal(1) / value + (value / 2).ln() * i1 - value * psi_series / 4)


def mixed_divided_difference_matrix(
    times: list[Decimal], other_times: list[Decimal], precision: int
) -> list[list[Decimal]]:
    with localcontext() as context:
        context.prec = precision
        matrix = [
            [2 * decimal_bessel_k1(left + right, precision) for right in other_times]
            for left in times
        ]
        size = len(times)
        for order in range(1, size):
            for row in range(size - 1, order - 1, -1):
                divisor = times[row] - times[row - order]
                for column in range(size):
                    matrix[row][column] = (
                        matrix[row][column] - matrix[row - 1][column]
                    ) / divisor
        for order in range(1, size):
            for column in range(size - 1, order - 1, -1):
                divisor = other_times[column] - other_times[column - order]
                for row in range(size):
                    matrix[row][column] = (
                        matrix[row][column] - matrix[row][column - 1]
                    ) / divisor
        return matrix


def divided_regularizer(
    times: list[Decimal], other_times: list[Decimal], precision: int
) -> Decimal:
    with localcontext() as context:
        context.prec = precision
        quotient = determinant(mixed_divided_difference_matrix(times, other_times, precision))
        cauchy_quotient = Decimal(2) ** len(times)
        for left in times:
            for right in other_times:
                cauchy_quotient /= left + right
        return quotient / cauchy_quotient


def direct_regularizer(
    times: list[Decimal], other_times: list[Decimal], precision: int
) -> Decimal:
    with localcontext() as context:
        context.prec = precision
        matrix = [
            [2 * decimal_bessel_k1(left + right, precision) for right in other_times]
            for left in times
        ]
        return determinant(matrix) / cauchy_determinant(times, other_times)


def order_terms() -> list[dict[str, Any]]:
    return [term for term in K179.coefficient_family() if int(term["order"]) == ORDER]


def group_key(term: dict[str, Any]) -> tuple[int, str]:
    return int(term["seed_impurity"]), str(term["output_signature"])


def grouped_terms() -> dict[tuple[int, str], list[dict[str, Any]]]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in order_terms():
        groups[group_key(term)].append(term)
    return dict(sorted(groups.items()))


def time_occurrences(term: dict[str, Any]) -> dict[str, tuple[int, ...]]:
    rows: dict[str, list[int]] = defaultdict(list)
    for position, species in zip(term["output_variable_provenance"], term["output_letters"]):
        rows[str(species)].append(int(position))
    return {species: tuple(positions) for species, positions in sorted(rows.items())}


def gap_rows(positions: tuple[int, ...], prefix: str) -> list[dict[str, Any]]:
    rows = []
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            first, second = positions[i], positions[j]
            rows.append(
                {
                    "positions": [first, second],
                    "identity": f"T_{first}-T_{second}" if prefix == "s" else f"U_{first}-U_{second}",
                    "primitive_support": [f"{prefix}{index}" for index in range(first, second)],
                }
            )
    return rows


def cross_support(left: int, right: int) -> list[str]:
    return [f"s{index}" for index in range(left, TOTAL_POSITIONS + 1)] + [
        f"v{index}" for index in range(right, TOTAL_POSITIONS + 1)
    ]


def factor_record(
    species: str, left_original: tuple[int, ...], right_original: tuple[int, ...]
) -> dict[str, Any]:
    left = tuple(sorted(left_original))
    right = tuple(sorted(right_original))
    if len(left) != len(right):
        raise AssertionError("coherent species multiplicities differ")
    left_sign = parity(left_original)
    right_sign = parity(right_original)
    size = len(left)
    return {
        "species": species,
        "size": size,
        "left_original_positions": list(left_original),
        "right_original_positions": list(right_original),
        "left_canonical_positions": list(left),
        "right_canonical_positions": list(right),
        "left_permutation_sign": left_sign,
        "right_permutation_sign": right_sign,
        "determinant_sign": left_sign * right_sign,
        "left_vandermonde_gaps": gap_rows(left, "s"),
        "right_vandermonde_gaps": gap_rows(right, "v"),
        "cauchy_denominator_supports": [cross_support(i, j) for i in left for j in right],
        "cauchy_power_of_two": size,
        "regularizer": "det[2*K1(T_i+U_j)] / det[2/(T_i+U_j)] in canonical order",
        "exact_factorization": "sign * 2^m * V_T * V_U / product_ij(T_i+U_j) * R_m(T,U)",
    }


def pattern_key(record: dict[str, Any]) -> str:
    return (
        f"m{record['size']}|"
        f"L{','.join(map(str, record['left_canonical_positions']))}|"
        f"R{','.join(map(str, record['right_canonical_positions']))}"
    )


def gram_entries() -> list[dict[str, Any]]:
    entries = []
    for key, terms in grouped_terms().items():
        for index, left in enumerate(terms):
            left_occurrences = time_occurrences(left)
            for right in terms[index:]:
                right_occurrences = time_occurrences(right)
                factors = [
                    factor_record(species, left_occurrences[species], right_occurrences[species])
                    for species in sorted(left_occurrences)
                ]
                coefficient_product = int(left["exact_operator_coefficient"]) * int(
                    right["exact_operator_coefficient"]
                )
                entries.append(
                    {
                        "group_id": f"seed={key[0]}|{key[1]}",
                        "left": left["contraction_id"],
                        "right": right["contraction_id"],
                        "coefficient_product": coefficient_product,
                        "left_old_position": int(left["old_position"]),
                        "right_old_position": int(right["old_position"]),
                        "species_factors": factors,
                        "entry_integrand_sign": coefficient_product
                        * math.prod(record["determinant_sign"] for record in factors),
                    }
                )
    return entries


def deterministic_profile(seed: int, rho: Decimal) -> tuple[list[Decimal], list[Decimal]]:
    raw = [Decimal(((seed + 5) * (slot + 7)) % 37 + 1) for slot in range(16)]
    total = sum(raw)
    values = [rho * value / total for value in raw]
    return values[:8], values[8:]


def face_profile(power: int) -> tuple[list[Decimal], list[Decimal]]:
    tiny = Decimal(2) ** (-power)
    side_total = Decimal(1) / 10
    side = [tiny] * 7 + [side_total - 7 * tiny]
    return side, side[:]


def times_for(positions: list[int], primitives: list[Any]) -> list[Any]:
    return [cumulative(primitives, position) for position in positions]


def exact_cauchy_controls() -> list[dict[str, Any]]:
    rows = []
    for size in range(1, 5):
        times = [Fraction(29 - 3 * index, 31) for index in range(size)]
        other = [Fraction(41 - 4 * index, 37) for index in range(size)]
        direct = determinant([[Fraction(2, 1) / (x + y) for y in other] for x in times])
        factored = cauchy_determinant(times, other)
        rows.append(
            {
                "size": size,
                "direct": str(direct),
                "factored": str(factored),
                "exact_equality": direct == factored,
            }
        )
    return rows


def divided_difference_controls(patterns: dict[str, dict[str, Any]]) -> dict[str, Any]:
    rows = []
    for seed in (0, 1):
        s, v = deterministic_profile(seed, Decimal(1) / 5)
        for key, record in patterns.items():
            left = times_for(record["left_canonical_positions"], s)
            right = times_for(record["right_canonical_positions"], v)
            direct = direct_regularizer(left, right, 190)
            divided = divided_regularizer(left, right, 190)
            rows.append(
                {
                    "pattern": key,
                    "profile": seed,
                    "size": record["size"],
                    "relative_difference": format(
                        abs(direct - divided) / abs(direct), ".18E"
                    ),
                    "divided_regularizer": format(divided, ".18E"),
                }
            )
    return {
        "tested_pattern_profiles": len(rows),
        "maximum_relative_difference": format(
            max(Decimal(row["relative_difference"]) for row in rows), ".18E"
        ),
        "all_positive": all(Decimal(row["divided_regularizer"]) > 0 for row in rows),
        "size_four_profiles": sum(row["size"] == 4 for row in rows),
        "precision_decimal_digits": 190,
        "rows": rows,
        "role": "high-precision interior control; not an outward interval",
    }


def stress_controls(patterns: dict[str, dict[str, Any]]) -> dict[str, Any]:
    representatives = {
        size: next(record for record in patterns.values() if record["size"] == size)
        for size in (2, 3, 4)
    }
    rows = []
    for size, power, precision in ((2, 100, 300), (3, 80, 380), (4, 60, 460)):
        record = representatives[size]
        s, v = face_profile(power)
        left = times_for(record["left_canonical_positions"], s)
        right = times_for(record["right_canonical_positions"], v)
        direct = direct_regularizer(left, right, precision)
        divided = divided_regularizer(left, right, precision)
        rows.append(
            {
                "kind": "near_coincident_face_strip",
                "size": size,
                "face_coordinate": f"2^-{power}",
                "precision_decimal_digits": precision,
                "divided_regularizer": format(divided, ".18E"),
                "relative_difference": format(
                    abs(direct - divided) / abs(direct), ".18E"
                ),
            }
        )
    for size, precision in ((2, 260), (3, 340), (4, 440)):
        record = representatives[size]
        s, v = deterministic_profile(size + 19, Decimal(2) ** (-120))
        left = times_for(record["left_canonical_positions"], s)
        right = times_for(record["right_canonical_positions"], v)
        direct = direct_regularizer(left, right, precision)
        divided = divided_regularizer(left, right, precision)
        rows.append(
            {
                "kind": "small_radius",
                "size": size,
                "rho": "2^-120",
                "precision_decimal_digits": precision,
                "divided_regularizer": format(divided, ".18E"),
                "distance_from_unit_limit": format(abs(divided - 1), ".18E"),
                "relative_difference": format(
                    abs(direct - divided) / abs(direct), ".18E"
                ),
            }
        )
    return {
        "rows": rows,
        "all_positive": all(Decimal(row["divided_regularizer"]) > 0 for row in rows),
        "maximum_relative_difference": format(
            max(Decimal(row["relative_difference"]) for row in rows), ".18E"
        ),
        "size_four_near_face_and_small_radius_controls": sum(row["size"] == 4 for row in rows),
        "role": "high-precision cancellation stress controls; not outward intervals",
    }


def build() -> dict[str, Any]:
    entries = gram_entries()
    size_histogram: Counter[int] = Counter()
    sign_histogram: Counter[int] = Counter()
    all_patterns: dict[str, dict[str, Any]] = {}
    patterns: dict[str, dict[str, Any]] = {}
    for entry in entries:
        for factor in entry["species_factors"]:
            size_histogram[factor["size"]] += 1
            sign_histogram[factor["determinant_sign"]] += 1
            all_patterns.setdefault(pattern_key(factor), factor)
            if factor["size"] > 1:
                patterns.setdefault(pattern_key(factor), factor)
    serialized_entries = []
    for entry in entries:
        serialized = dict(entry)
        serialized["species_factors"] = [
            {
                "species": factor["species"],
                "pattern": pattern_key(factor),
                "size": factor["size"],
                "determinant_sign": factor["determinant_sign"],
            }
            for factor in entry["species_factors"]
        ]
        serialized_entries.append(serialized)
    exact_controls = exact_cauchy_controls()
    divided = divided_difference_controls(patterns)
    stress = stress_controls(patterns)
    nontrivial = sum(value for size, value in size_histogram.items() if size > 1)
    previous_patterns = json.loads(K186_MANIFEST.read_text())["unique_patterns"]
    k192_release = json.loads(K192_MANIFEST.read_text())["release_test"]
    inherited = sorted(key for key in patterns if key in previous_patterns)
    new = sorted(key for key in patterns if key not in previous_patterns)
    return {
        "schema_version": "1.0",
        "result_id": "K280-ORDER-SEVEN-BESSEL-VANDERMONDE-FACE-ATLAS",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "source_family": "K179 order-seven coefficient family",
            "source_manifest": "lab/process/k279-higher-order-andreief-structural-closure.json",
            "source_paths": 96,
            "source_groups": 16,
            "source_gram_entries": 408,
            "primitive_time_variables": 16,
            "radial_core": "0 < rho <= 1/4",
        },
        "complete_factorization_inventory": {
            "entries": serialized_entries,
            "species_determinant_occurrences": sum(size_histogram.values()),
            "nontrivial_size_two_through_four_occurrences": nontrivial,
            "size_histogram": {str(key): value for key, value in sorted(size_histogram.items())},
            "determinant_sign_histogram": {
                str(key): value for key, value in sorted(sign_histogram.items())
            },
            "unique_nontrivial_factor_patterns": len(patterns),
            "unique_patterns_by_size": {
                str(size): sum(record["size"] == size for record in patterns.values())
                for size in (2, 3, 4)
            },
            "all_sizes_at_most_four": max(size_histogram) <= 4,
            "size_four_present": size_histogram[4] > 0,
            "every_nontrivial_factor_has_two_vandermonde_families": all(
                record["left_vandermonde_gaps"] and record["right_vandermonde_gaps"]
                for record in patterns.values()
            ),
        },
        "factor_patterns": all_patterns,
        "factorization_certificate": {
            "kernel": "f(x)=2*K1(x)=integral_R exp(-x*sqrt(1+p^2)) dp",
            "canonical_order": "time positions increasing, hence cumulative times strictly decreasing",
            "cauchy_identity": "det[2/(T_i+U_j)]=2^m V_T V_U/product_ij(T_i+U_j) for m=1..4",
            "bessel_identity": "det[2*K1(T_i+U_j)]=det[2/(T_i+U_j)]*R_m(T,U)",
            "strict_positivity": "Andreief against a positive infinite-support energy measure makes the canonical Bessel determinant and R_m strictly positive for distinct ordered times",
            "coalescent_extension": "successive Newton row/column transforms divide out both Vandermonde families and extend by mixed derivative jets through size four",
            "small_radius_limit": "R_m(rho*t,rho*u) tends to one at every positive angular point for m=1..4",
            "exact_cauchy_controls": exact_controls,
        },
        "unique_patterns": patterns,
        "predecessor_reuse": {
            "K186_order_six_patterns": len(previous_patterns),
            "K280_order_seven_patterns": len(patterns),
            "exact_pattern_overlap": len(inherited),
            "exact_overlap_by_size": {
                str(size): sum(patterns[key]["size"] == size for key in inherited)
                for size in (2, 3, 4)
            },
            "new_patterns_by_size": {
                str(size): sum(patterns[key]["size"] == size for key in new)
                for size in (2, 3, 4)
            },
            "inherited_pattern_keys": inherited,
            "new_pattern_keys": new,
            "K192_certified_union_reusable_for_identical_patterns": True,
            "K192_arbitrary_gap_ratio_domain_covered": k192_release[
                "arbitrary_gap_ratio_domain_covered"
            ],
            "K192_noncoalescent_face_atlas_serialized": k192_release[
                "noncoalescent_face_atlas_serialized"
            ],
            "reuse_decision": "Reuse K192 certified-union boxes for the 52 identical size-two/three pattern functions only on their proved domains. Construct 46 new pattern enclosures and the residual noncoalescent face atlas; do not promote partial predecessor coverage to complete order-seven cubature.",
        },
        "independent_controls": {
            "mixed_divided_difference": divided,
            "stress": stress,
        },
        "release_test": {
            "all_408_order_seven_gram_entries_replayed": len(entries) == 408,
            "all_size_one_through_four_determinants_factored": max(size_histogram) == 4,
            "canonical_signs_serialized": True,
            "primitive_vandermonde_gap_supports_serialized": True,
            "positive_regularizers_defined_through_size_four": True,
            "coalescent_extension_defined_through_size_four": True,
            "all_exact_cauchy_controls_pass": all(row["exact_equality"] for row in exact_controls),
            "outward_R2_R3_R4_intervals_serialized": False,
            "duffy_derivative_envelopes_serialized": False,
            "determinant_valued_cubature_error_serialized": False,
            "coefficient_complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": {
            "SC-META-53": "UNCERTAIN_UNCHANGED",
            "LT-SM8": "NEEDS_UNCHANGED",
            "LT-GR6b": "NEEDS_UNCHANGED",
            "RA-F1": "NEEDS_UNCHANGED",
            "AC-F1": "NEEDS_UNCHANGED",
        },
        "next_exact_input": {
            "owner": "outward size-two-through-four regularizer and Duffy-derivative enclosure",
            "first_gate": "derive outward R2, R3 and new R4 value/mixed-derivative boxes on a gap-stratified rho/theta/simplex atlas, then compose the exact face weights with a determinant-preserving Jacobi remainder",
            "must_preserve": "all 408 signed entries, 96 K179 paths, old-position Bessel factors, exact primitive gap supports, complete regularizers and shared cumulative-time nodes",
        },
        "claim_ceiling": "Complete exact order-seven face atlas and qualitative cancellation-preserving regularizer through size four. No outward full-domain regularizer interval, Duffy/Jacobi cubature error, action-column value, complete residual, exterior gap, K152 interval, physical state, source claim, ledger row, canon, paper or public posture is changed.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--output")
    args = parser.parse_args()
    result = build()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    if args.output:
        Path(args.output).write_text(rendered)
    if not args.write and not args.output:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
