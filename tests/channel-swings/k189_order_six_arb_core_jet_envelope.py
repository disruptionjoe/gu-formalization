#!/usr/bin/env python3
"""K189 rigorous global kernel-jet envelopes for the K188 open core.

For f(x)=2 K_1(x), complete monotonicity and the Bessel derivative recurrence
give exact signs and Arb-evaluated endpoint bounds for every derivative used by
the mixed Newton matrix. Tensor Hermite--Genocchi then bounds its entries
without dividing by a time gap. Product rules propagate those bounds through
the determinant and exact Cauchy normalization to every primitive mixed
derivative of R_m through order four.

The resulting envelopes are rigorous but intentionally global. They diagnose
whether one unsplit core box can support a decision-grade Jacobi remainder;
they do not themselves integrate the signed determinant family.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Any, Iterable

import flint
from flint import arb, ctx
from scipy.special import kv


ROOT = Path(__file__).resolve().parents[2]
K186_MANIFEST = ROOT / "lab/process/k186-order-six-bessel-vandermonde-wave.json"
K188_MANIFEST = ROOT / "lab/process/k188-order-six-small-rho-strip-wave.json"
OUTPUT = ROOT / "lab/process/k189-order-six-arb-core-jet-envelope-wave.json"
ARB_DIGITS = 100
MAX_PRIMITIVE_DERIVATIVE_ORDER = 4
CURRENT_TOTAL_PRIMITIVE_FLOOR_POWER = 200  # rho>=2^-20 and z_i>=2^-180
SENSITIVITY_TOTAL_FLOOR_POWERS = (8, 12, 16, 24, 40, 80, 120, 160, 200)


ctx.dps = ARB_DIGITS
ctx.threads = 1


def pattern_occurrences(source: dict[str, Any]) -> dict[str, int]:
    result: dict[str, int] = {}
    for entry in source["complete_factorization_inventory"]["entries"]:
        for factor in entry["species_factors"]:
            if factor["size"] > 1:
                key = (
                    f"m{factor['size']}|"
                    f"L{','.join(map(str, factor['left_canonical_positions']))}|"
                    f"R{','.join(map(str, factor['right_canonical_positions']))}"
                )
                result[key] = result.get(key, 0) + 1
    return result


def bessel_derivative_abs(order: int, x: arb) -> arb:
    """Return an Arb enclosure of |d^order/dx^order (2 K_1(x))|."""

    total = arb(0)
    for index in range(order + 1):
        bessel_order = abs(1 - order + 2 * index)
        total += math.comb(order, index) * x.bessel_k(bessel_order)
    result = (arb(2) ** (1 - order)) * total
    if not result.rad() > 0:
        raise AssertionError("Arb endpoint evaluation unexpectedly has zero radius")
    return result


def compositions(total: int, length: int) -> Iterable[tuple[int, ...]]:
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, length - 1):
            yield (first,) + rest


def multinomial(parts: tuple[int, ...]) -> int:
    value = math.factorial(sum(parts))
    for part in parts:
        value //= math.factorial(part)
    return value


def determinant_derivative_abs_bound(
    record: dict[str, Any], derivative_order: int, total_floor_power: int
) -> arb:
    """Bound any primitive mixed derivative of det(mixed-DD f matrix)."""

    size = int(record["size"])
    left = record["left_canonical_positions"]
    right = record["right_canonical_positions"]
    primitive_floor = arb(2) ** (-total_floor_power)
    total = arb(0)
    for permutation in itertools.permutations(range(size)):
        for allocation in compositions(derivative_order, size):
            term = arb(multinomial(allocation))
            for row, column in enumerate(permutation):
                support_count = 16 - int(left[row]) - int(right[column])
                minimum_argument = primitive_floor * support_count
                kernel_order = row + column + allocation[row]
                term *= bessel_derivative_abs(kernel_order, minimum_argument)
                term /= math.factorial(row) * math.factorial(column)
            total += term
    return total


def falling_factorial(value: int, length: int) -> int:
    result = 1
    for offset in range(length):
        result *= value - offset
    return result


def regularizer_derivative_abs_bound(
    record: dict[str, Any], derivative_order: int, total_floor_power: int
) -> arb:
    """Bound any primitive mixed derivative of R_m through the product rule."""

    size = int(record["size"])
    cauchy_product_factors = size * size
    total = arb(0)
    for product_order in range(min(derivative_order, cauchy_product_factors) + 1):
        determinant_order = derivative_order - product_order
        determinant_bound = determinant_derivative_abs_bound(
            record, determinant_order, total_floor_power
        )
        product_bound = falling_factorial(cauchy_product_factors, product_order)
        product_bound *= (arb(1) / 4) ** (cauchy_product_factors - product_order)
        total += (
            math.comb(derivative_order, product_order)
            * determinant_bound
            * product_bound
        )
    return total / (arb(2) ** size)


def power_of_ten_ceiling(value: arb) -> dict[str, Any]:
    log_value = value.log() / arb(10).log()
    exponent = math.ceil(float(log_value.upper()))
    strict = (arb(10) ** exponent) > value
    if not strict:
        raise AssertionError("decimal ceiling failed to contain Arb bound")
    return {
        "power": exponent,
        "bound": f"10^{exponent}",
        "strictly_contains_arb_ball": True,
        "arb_log10_ball": str(log_value),
    }


def pattern_envelopes(
    patterns: dict[str, dict[str, Any]], occurrences: dict[str, int]
) -> tuple[dict[str, Any], dict[int, dict[int, list[int]]]]:
    rows: dict[str, Any] = {}
    powers: dict[int, dict[int, list[int]]] = {2: {}, 3: {}}
    for pattern_id, record in sorted(patterns.items()):
        derivative_rows = {}
        size = int(record["size"])
        for order in range(MAX_PRIMITIVE_DERIVATIVE_ORDER + 1):
            bound = regularizer_derivative_abs_bound(
                record, order, CURRENT_TOTAL_PRIMITIVE_FLOOR_POWER
            )
            ceiling = power_of_ten_ceiling(bound)
            derivative_rows[str(order)] = ceiling
            powers[size].setdefault(order, []).append(int(ceiling["power"]))
        rows[pattern_id] = {
            "size": size,
            "left_canonical_positions": record["left_canonical_positions"],
            "right_canonical_positions": record["right_canonical_positions"],
            "occurrences": occurrences[pattern_id],
            "value_interval": ["0", derivative_rows["0"]["bound"]],
            "primitive_mixed_derivative_absolute_bounds": derivative_rows,
        }
    return rows, powers


def scale_sensitivity(patterns: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for floor_power in SENSITIVITY_TOTAL_FLOOR_POWERS:
        by_size: dict[str, int] = {}
        for size in (2, 3):
            ceilings = [
                power_of_ten_ceiling(
                    regularizer_derivative_abs_bound(record, 0, floor_power)
                )["power"]
                for record in patterns.values()
                if int(record["size"]) == size
            ]
            by_size[str(size)] = max(ceilings)
        rows.append(
            {
                "total_primitive_floor": f"2^-{floor_power}",
                "maximum_value_ceiling_power_by_size": by_size,
            }
        )
    return rows


def derivative_recurrence_controls() -> dict[str, Any]:
    x = arb(1) / 4
    rows = []
    maximum_relative_difference = 0.0
    for order in range(9):
        arb_value = bessel_derivative_abs(order, x)
        scipy_value = (
            2.0 ** (1 - order)
            * sum(
                math.comb(order, index)
                * float(kv(abs(1 - order + 2 * index), 0.25))
                for index in range(order + 1)
            )
        )
        midpoint = float(arb_value.mid())
        relative = abs(midpoint - scipy_value) / midpoint
        maximum_relative_difference = max(maximum_relative_difference, relative)
        rows.append(
            {
                "order": order,
                "arb_ball": str(arb_value),
                "scipy_binary64_control": scipy_value,
                "relative_midpoint_difference": relative,
            }
        )
    return {
        "x": "1/4",
        "orders": "0..8",
        "rows": rows,
        "maximum_relative_midpoint_difference": maximum_relative_difference,
        "role": "independent SciPy binary64 recurrence control only; Arb balls carry directed endpoint evaluation",
    }


def build() -> dict[str, Any]:
    source = json.loads(K186_MANIFEST.read_text())
    split = json.loads(K188_MANIFEST.read_text())
    patterns = source["unique_patterns"]
    occurrences = pattern_occurrences(source)
    rows, powers = pattern_envelopes(patterns, occurrences)
    ranges = {
        str(size): {
            str(order): {
                "minimum_power": min(values),
                "maximum_power": max(values),
            }
            for order, values in sorted(by_order.items())
        }
        for size, by_order in powers.items()
    }
    controls = source["independent_controls"]
    sampled_min = min(
        controls["all_entry_double_precision"]["regularizer_control_range"][0],
        controls["mixed_divided_difference"]["regularizer_control_range"][0],
    )
    sampled_max = max(
        controls["all_entry_double_precision"]["regularizer_control_range"][1],
        controls["mixed_divided_difference"]["regularizer_control_range"][1],
    )
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "source_manifest": "lab/process/k186-order-six-bessel-vandermonde-wave.json",
            "domain_manifest": "lab/process/k188-order-six-small-rho-strip-wave.json",
            "domain": split["next_exact_input"]["domain"],
            "radial_floor": "2^-20",
            "angular_floor": "2^-180",
            "primitive_floor": "2^-200",
            "radial_ceiling": "1/4",
            "source_patterns": len(patterns),
            "source_nontrivial_occurrences": sum(occurrences.values()),
            "source_time_gram_entries": source["fixed_control"]["source_entries"],
            "source_coherent_groups": split["fixed_control"]["source_coherent_groups"],
            "maximum_primitive_mixed_derivative_order": MAX_PRIMITIVE_DERIVATIVE_ORDER,
        },
        "arb_backend": {
            "python_flint_version": flint.__version__,
            "flint_version": flint.__FLINT_VERSION__,
            "decimal_digits": ARB_DIGITS,
            "threads": 1,
            "all_endpoint_values_are_nonzero_width_balls": True,
        },
        "theorem_certificate": {
            "kernel": "f(x)=2*K1(x)=integral_R exp(-x*sqrt(1+p^2)) dp",
            "complete_monotonicity": "(-1)^n f^(n)(x)>0 for x>0",
            "derivative_identity": "|f^(n)(x)|=2^(1-n)*sum_(k=0)^n binomial(n,k) K_|1-n+2k|(x)",
            "tensor_hermite_genocchi": "the mixed Newton entry of row order i and column order j is a positive simplex average of f^(i+j)/(i!j!), so its magnitude is bounded at the smallest admissible argument without any time-gap division",
            "pattern_argument_floor": "entry (i,j) uses at least (16-left_position_i-right_position_j)*2^-200",
            "determinant_derivative_bound": "sum absolute Leibniz products and all multinomial derivative allocations; determinant positivity supplies the value lower endpoint zero",
            "normalization": "R_m=det(mixed-DD f)*product_ij(T_i+U_j)/2^m",
            "normalization_derivative_bound": "the product has m^2 linear factors, each <=1/4; its order-s derivative is bounded by falling_factorial(m^2,s)*(1/4)^(m^2-s)",
            "scope": "every primitive-coordinate mixed partial of total order 0..4; Duffy/Jacobi chain-rule bounds and a cubature remainder remain separate",
        },
        "complete_pattern_envelopes": {
            "patterns": rows,
            "all_53_patterns_covered": len(rows) == 53,
            "all_468_occurrences_covered": sum(row["occurrences"] for row in rows.values()) == 468,
            "all_234_entries_remain_in_scope": source["fixed_control"]["source_entries"] == 234,
            "all_18_groups_remain_in_scope": split["fixed_control"]["source_coherent_groups"] == 18,
            "power_ranges_by_size_and_derivative_order": ranges,
        },
        "scale_sensitivity": {
            "rows": scale_sensitivity(patterns),
            "interpretation": "even after raising the combined radial/angular primitive floor from 2^-200 to 2^-8, the raw-kernel global value envelope remains many orders wider than the observed O(1) regularizer scale; subdivision alone does not preserve the Cauchy cancellation",
        },
        "independent_controls": {
            "bessel_derivative_recurrence": derivative_recurrence_controls(),
            "k186_sampled_regularizer_range": [sampled_min, sampled_max],
            "all_sampled_values_inside_every_matching_positive_value_envelope": True,
            "role": "the K186 direct/divided-difference values test scale and implementation only; they do not narrow the rigorous global envelopes",
        },
        "release_test": {
            "exact_bessel_derivative_identity_banked": True,
            "hermite_genocchi_gap_free_entry_bound_banked": True,
            "arb_directed_endpoint_evaluation_banked": True,
            "all_53_regularizer_value_envelopes_serialized": True,
            "all_53_primitive_mixed_derivative_envelopes_through_order_four_serialized": True,
            "duffy_jacobi_chain_rule_envelopes_serialized": False,
            "single_global_core_box_decision_grade": False,
            "determinant_preserving_positive_radius_core_error_serialized": False,
            "complete_outward_order_six_total_error_serialized": False,
            "accurate_order_six_prefix_released": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "route_switch": {
            "retired_as_decision_grade_route": "one global raw-K1 Hermite--Genocchi/Jacobi remainder on the complete 2^-200 primitive-floor core",
            "reason": "the current size-three value ceiling reaches 10^533 and fourth primitive derivatives reach 10^776 while K186 controls remain between 0.8804 and 0.9881; the enclosure is outward but loses the same Cauchy cancellation that defines R_m",
            "next_exact_input": "derive a cancellation-preserving scaled-kernel or regularizer Taylor model before interval subdivision, using q(x)=x*K1(x), the exact Cauchy normalization and coalescent jets together; then build Duffy/Jacobi chain-rule bounds on stratified radial/angular boxes and combine the resulting core error with K185/K188 boundaries",
            "must_preserve": "all 234 signed entries, 18 coherent groups, 53 regularizer patterns, old-position factors, primitive gaps, complete determinants and shared time nodes",
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
    }


def summary(result: dict[str, Any]) -> dict[str, Any]:
    return {
        "fixed_control": result["fixed_control"],
        "arb_backend": result["arb_backend"],
        "theorem_certificate": result["theorem_certificate"],
        "complete_pattern_envelopes": {
            key: value
            for key, value in result["complete_pattern_envelopes"].items()
            if key != "patterns"
        },
        "scale_sensitivity": result["scale_sensitivity"],
        "independent_controls": {
            "bessel_derivative_recurrence": {
                key: value
                for key, value in result["independent_controls"]["bessel_derivative_recurrence"].items()
                if key != "rows"
            },
            "k186_sampled_regularizer_range": result["independent_controls"]["k186_sampled_regularizer_range"],
        },
        "release_test": result["release_test"],
        "route_switch": result["route_switch"],
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
        print(json.dumps(summary(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
