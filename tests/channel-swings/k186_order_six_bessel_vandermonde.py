#!/usr/bin/env python3
"""K186 cancellation-free factorization of K185 order-six Bessel determinants.

For every size-two/three kernel det[2 K_1(T_i+U_j)] this module records the
canonical row/column parity and factors the singular Cauchy kernel exactly:

  det[2/(T_i+U_j)] = 2^m V(T) V(U) / prod_ij(T_i+U_j).

The remaining Bessel/Cauchy ratio is positive by the Andreief representation,
has a divided-difference extension across coincident ordered times, and tends
to one at fixed positive angular coordinates as rho tends to zero.  Decimal
series and mixed Newton differences are independent finite-precision controls;
they are not outward interval arithmetic.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from decimal import Decimal, localcontext
from pathlib import Path
from typing import Any, Iterable

import numpy as np
from scipy.special import k1


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "lab/process/k184-order-six-certified-low-rank-wave.json"
OUTPUT = ROOT / "lab/process/k186-order-six-bessel-vandermonde-wave.json"
VARIABLES = tuple([f"s{i}" for i in range(1, 8)] + [f"v{i}" for i in range(1, 8)])
EULER_GAMMA = Decimal(
    "0.57721566490153286060651209008240243104215933593992359880576723488486772677766467"
)


def parity(values: tuple[int, ...]) -> int:
    inversions = sum(
        values[i] > values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def cumulative(values: list[float] | list[Decimal], position: int):
    return sum(values[position - 1 :])


def determinant(matrix: list[list[Any]]):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if size == 3:
        return (
            matrix[0][0]
            * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
            - matrix[0][1]
            * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
            + matrix[0][2]
            * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        )
    raise ValueError("K186 only admits determinants of size one through three")


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
    """Evaluate K_1 on 0 < value <= 1/4 by its convergent integer-order series."""

    if not Decimal(0) < value <= Decimal(1) / 4:
        raise ValueError("K186 decimal series is scoped to 0 < x <= 1/4")
    with localcontext() as context:
        context.prec = precision + 20
        half = value / 2
        quarter_square = value * value / 4
        i1 = Decimal(0)
        psi_series = Decimal(0)
        factorial_k = 1
        factorial_k1 = 1
        power = half
        h_k = Decimal(0)
        tolerance = Decimal(10) ** (-(precision + 5))
        for index in range(10000):
            if index:
                factorial_k *= index
                factorial_k1 *= index + 1
                power *= quarter_square
                h_k += Decimal(1) / Decimal(index)
            h_k1 = h_k + Decimal(1) / Decimal(index + 1)
            denominator = Decimal(factorial_k * factorial_k1)
            i_term = power / denominator
            psi_term = (h_k + h_k1 - 2 * EULER_GAMMA) * (quarter_square**index) / denominator
            i1 += i_term
            psi_series += psi_term
            if index > 4 and abs(i_term) < tolerance and abs(value * psi_term) < tolerance:
                break
        else:
            raise AssertionError("K1 series failed to converge")
        result = Decimal(1) / value + (value / 2).ln() * i1 - value * psi_series / 4
        return +result


def mixed_divided_difference_matrix(
    times: list[Decimal], other_times: list[Decimal], precision: int
) -> list[list[Decimal]]:
    """Apply Newton row and column transforms to the Bessel kernel matrix."""

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


def divided_difference_regularizer(
    times: list[Decimal], other_times: list[Decimal], precision: int
) -> Decimal:
    matrix = mixed_divided_difference_matrix(times, other_times, precision)
    quotient = determinant(matrix)
    cauchy_quotient = (Decimal(2) ** len(times))
    for left in times:
        for right in other_times:
            cauchy_quotient /= left + right
    return quotient / cauchy_quotient


def direct_decimal_regularizer(
    times: list[Decimal], other_times: list[Decimal], precision: int
) -> Decimal:
    with localcontext() as context:
        context.prec = precision
        kernel = [
            [2 * decimal_bessel_k1(left + right, precision) for right in other_times]
            for left in times
        ]
        return determinant(kernel) / cauchy_determinant(times, other_times)


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
    return [f"s{index}" for index in range(left, 8)] + [f"v{index}" for index in range(right, 8)]


def factor_record(species: dict[str, Any]) -> dict[str, Any]:
    left_original = tuple(int(value) for value in species["left_time_positions"])
    right_original = tuple(int(value) for value in species["right_time_positions"])
    left = tuple(sorted(left_original))
    right = tuple(sorted(right_original))
    left_sign = parity(left_original)
    right_sign = parity(right_original)
    size = len(left)
    return {
        "species": species["species"],
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


def source_entries() -> list[dict[str, Any]]:
    source = json.loads(SOURCE.read_text())
    return source["andreief_time_gram_certificate"]["gram_entries"]


def deterministic_profile(index: int, rho: Decimal) -> tuple[list[Decimal], list[Decimal]]:
    raw = [Decimal(((index + 3) * (slot + 5)) % 29 + 1) for slot in range(14)]
    total = sum(raw)
    values = [rho * value / total for value in raw]
    return values[:7], values[7:]


def times_for(
    positions: Iterable[int], primitives: list[Decimal]
) -> list[Decimal]:
    return [cumulative(primitives, position) for position in sorted(positions)]


def pattern_key(record: dict[str, Any]) -> str:
    return (
        f"m{record['size']}|"
        f"L{','.join(map(str, record['left_canonical_positions']))}|"
        f"R{','.join(map(str, record['right_canonical_positions']))}"
    )


def all_entry_control(
    entries: list[dict[str, Any]], patterns: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    s_float = np.array([11, 7, 13, 5, 17, 3, 19], dtype=float)
    v_float = np.array([2, 23, 9, 29, 4, 31, 6], dtype=float)
    scale = 0.2 / float(s_float.sum() + v_float.sum())
    s_float *= scale
    v_float *= scale
    positive = 0
    sign_matches = 0
    regularizers = []
    direct_reconstruction_errors = []
    for entry in entries:
        for species in entry["species_kernels"]:
            record = factor_record(species)
            if record["size"] == 1:
                continue
            left = [cumulative(s_float.tolist(), p) for p in record["left_canonical_positions"]]
            right = [cumulative(v_float.tolist(), p) for p in record["right_canonical_positions"]]
            canonical = np.array([[2.0 * k1(x + y) for y in right] for x in left])
            original_left = [cumulative(s_float.tolist(), p) for p in species["left_time_positions"]]
            original_right = [cumulative(v_float.tolist(), p) for p in species["right_time_positions"]]
            original = np.array([[2.0 * k1(x + y) for y in original_right] for x in original_left])
            canonical_det = float(np.linalg.det(canonical))
            original_det = float(np.linalg.det(original))
            cauchy = float(cauchy_determinant(left, right))
            regularizer = canonical_det / cauchy
            reconstructed = record["determinant_sign"] * cauchy * regularizer
            positive += canonical_det > 0.0
            sign_matches += math.copysign(1.0, original_det) == math.copysign(
                1.0, record["determinant_sign"]
            )
            regularizers.append(regularizer)
            direct_reconstruction_errors.append(
                abs(reconstructed - original_det) / max(abs(original_det), 1e-300)
            )
    return {
        "tested_nontrivial_determinants": len(regularizers),
        "canonical_determinants_positive": positive,
        "original_sign_matches_record": sign_matches,
        "direct_factorized_reconstruction_max_relative_error": max(direct_reconstruction_errors),
        "regularizer_control_range": [min(regularizers), max(regularizers)],
        "unique_factor_patterns": len(patterns),
        "role": "double-precision interior reconstruction control only",
    }


def divided_difference_controls(patterns: dict[str, dict[str, Any]]) -> dict[str, Any]:
    relative_errors = []
    regularizers = []
    for profile in range(3):
        s, v = deterministic_profile(profile, Decimal(1) / 5)
        for record in patterns.values():
            left = times_for(record["left_canonical_positions"], s)
            right = times_for(record["right_canonical_positions"], v)
            direct = direct_decimal_regularizer(left, right, 100)
            divided = divided_difference_regularizer(left, right, 100)
            relative_errors.append(abs(direct - divided) / abs(direct))
            regularizers.append(divided)
    return {
        "tested_pattern_profiles": len(relative_errors),
        "direct_vs_mixed_divided_difference_max_relative_error": float(max(relative_errors)),
        "regularizer_control_range": [float(min(regularizers)), float(max(regularizers))],
        "precision_decimal_digits": 100,
        "role": "convergent-series and mixed-Newton finite-precision control; not an outward interval",
    }


def stress_controls(patterns: dict[str, dict[str, Any]]) -> dict[str, Any]:
    representatives = {}
    for size in (2, 3):
        representatives[size] = next(record for record in patterns.values() if record["size"] == size)
    rows = []
    for size, face_power, precision in ((2, 180, 300), (3, 180, 520)):
        record = representatives[size]
        with localcontext() as context:
            context.prec = precision + 40
            tiny = Decimal(2) ** (-face_power)
            values = [tiny] * 14
            values[-1] = Decimal(1) - tiny * 13
            rho = Decimal(1) / 5
            values = [rho * value for value in values]
            s, v = values[:7], values[7:]
            left = times_for(record["left_canonical_positions"], s)
            right = times_for(record["right_canonical_positions"], v)
            direct = direct_decimal_regularizer(left, right, precision)
            divided = divided_difference_regularizer(left, right, precision)
        rows.append(
            {
                "kind": "near_coincident_face_strip",
                "size": size,
                "face_coordinate": f"2^-{face_power}",
                "precision_decimal_digits": precision,
                "direct_regularizer": format(direct, ".18E"),
                "divided_difference_regularizer": format(divided, ".18E"),
                "relative_difference": float(abs(direct - divided) / abs(direct)),
            }
        )
    for size, precision in ((2, 340), (3, 520)):
        record = representatives[size]
        with localcontext() as context:
            context.prec = precision + 40
            s, v = deterministic_profile(size + 7, Decimal(2) ** (-200))
            left = times_for(record["left_canonical_positions"], s)
            right = times_for(record["right_canonical_positions"], v)
            direct = direct_decimal_regularizer(left, right, precision)
            divided = divided_difference_regularizer(left, right, precision)
        rows.append(
            {
                "kind": "small_radius",
                "size": size,
                "rho": "2^-200",
                "precision_decimal_digits": precision,
                "direct_regularizer": format(direct, ".18E"),
                "divided_difference_regularizer": format(divided, ".18E"),
                "distance_from_unit_limit": format(abs(divided - 1), ".18E"),
                "relative_difference": float(abs(direct - divided) / abs(direct)),
            }
        )
    return {
        "rows": rows,
        "all_positive": all(Decimal(row["divided_difference_regularizer"]) > 0 for row in rows),
        "maximum_relative_difference": max(row["relative_difference"] for row in rows),
        "role": "high-precision stress controls at the admitted face scale and small radius; not outward intervals",
    }


def build() -> dict[str, Any]:
    entries = source_entries()
    size_histogram: Counter[int] = Counter()
    sign_histogram: Counter[int] = Counter()
    patterns: dict[str, dict[str, Any]] = {}
    output_entries = []
    nontrivial = 0
    for entry in entries:
        factors = []
        for species in entry["species_kernels"]:
            record = factor_record(species)
            size_histogram[record["size"]] += 1
            sign_histogram[record["determinant_sign"]] += 1
            if record["size"] > 1:
                nontrivial += 1
                patterns.setdefault(pattern_key(record), record)
            factors.append(record)
        output_entries.append(
            {
                "group_id": entry["group_id"],
                "left": entry["left"],
                "right": entry["right"],
                "coefficient_product": entry["coefficient_product"],
                "left_old_position": entry["left_old_position"],
                "right_old_position": entry["right_old_position"],
                "species_factors": factors,
                "entry_integrand_sign": entry["coefficient_product"]
                * math.prod(record["determinant_sign"] for record in factors),
            }
        )
    direct = all_entry_control(entries, patterns)
    divided = divided_difference_controls(patterns)
    stress = stress_controls(patterns)
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "source_manifest": "lab/process/k184-order-six-certified-low-rank-wave.json",
            "source_entries": len(entries),
            "primitive_time_variables": 14,
            "radial_cutoff": "1/4",
            "face_strip_floor": "2^-180",
        },
        "complete_factorization_inventory": {
            "entries": output_entries,
            "species_determinant_occurrences": sum(size_histogram.values()),
            "nontrivial_size_two_or_three_occurrences": nontrivial,
            "size_histogram": {str(key): value for key, value in sorted(size_histogram.items())},
            "determinant_sign_histogram": {
                str(key): value for key, value in sorted(sign_histogram.items())
            },
            "unique_nontrivial_factor_patterns": len(patterns),
            "all_sizes_at_most_three": max(size_histogram) <= 3,
            "every_nontrivial_factor_has_two_vandermonde_families": all(
                record["left_vandermonde_gaps"] and record["right_vandermonde_gaps"]
                for record in patterns.values()
            ),
        },
        "factorization_certificate": {
            "kernel": "f(x)=2*K_1(x)=integral_R exp(-x*sqrt(1+p^2)) dp",
            "canonical_order": "time positions increasing, hence cumulative times strictly decreasing",
            "cauchy_identity": "det[2/(T_i+U_j)]=2^m V_T V_U/product_ij(T_i+U_j)",
            "bessel_identity": "det[2*K_1(T_i+U_j)]=det[2/(T_i+U_j)]*R_m(T,U)",
            "strict_positivity": "Andreief against a positive infinite-support energy measure gives the canonical Bessel determinant and R_m strictly positive for distinct ordered times",
            "coalescent_extension": "successive Newton row/column transforms divide out V_T V_U and extend by mixed derivative jets; the corresponding Cauchy quotient is nonzero away from T_i+U_j=0",
            "small_radius_limit": "R_m(rho*t,rho*u) tends to one for every positive angular point; on the face-stripped angular simplex the extension is continuous on 0<=rho<=1/4",
            "factorization_is_subtraction_free_after_regularizer_enclosure": True,
        },
        "unique_patterns": patterns,
        "independent_controls": {
            "all_entry_double_precision": direct,
            "mixed_divided_difference": divided,
            "stress": stress,
        },
        "release_test": {
            "all_234_time_gram_entries_replayed": len(entries) == 234,
            "all_size_two_and_three_determinants_factored": nontrivial
            == size_histogram[2] + size_histogram[3],
            "canonical_signs_serialized": True,
            "primitive_vandermonde_gap_supports_serialized": True,
            "positive_regularizer_defined": True,
            "coalescent_extension_defined": True,
            "bounded_compact_core_regularizer_proved_qualitatively": True,
            "outward_regularizer_interval_serialized": False,
            "determinant_preserving_compact_core_quadrature_error_serialized": False,
            "accurate_order_six_prefix_released": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": {
            "SC-META-53": "UNCERTAIN_UNCHANGED",
            "LT-SM8": "NEEDS_UNCHANGED",
            "RA-F1": "NEEDS_UNCHANGED",
            "AC-F1": "NEEDS_UNCHANGED",
        },
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
        "canon_paper_release_or_public_posture_move": False,
        "next_exact_input": {
            "owner": "outward regularizer enclosure and determinant-preserving weighted compact-core cubature",
            "first_gate": "derive explicit outward bounds for R_2 and R_3 and their mixed Duffy derivatives on 0<=rho<=1/4, z_i>=2^-180, then integrate the exact Cauchy--Vandermonde skeleton with certified Jacobi remainder",
            "must_preserve": "all 234 signed entries, old-position Bessel factors, exact primitive gap sums, complete regularizers and shared time nodes",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if args.summary or not args.write:
        inventory = dict(result["complete_factorization_inventory"])
        inventory.pop("entries", None)
        print(
            json.dumps(
                {
                    "classification": result["classification"],
                    "inventory": inventory,
                    "controls": result["independent_controls"],
                    "release_test": result["release_test"],
                    "next_exact_input": result["next_exact_input"],
                },
                indent=2,
                sort_keys=True,
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
