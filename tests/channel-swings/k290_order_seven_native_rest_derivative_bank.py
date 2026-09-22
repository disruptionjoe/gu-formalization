#!/usr/bin/env python3
"""K290 native rest-factor shape-derivative bank on the K284 tube.

The common size-four regularizer is deliberately excluded: K286 already
controls it.  This module bounds every other factor in the 24 K288
occurrences, including the endpoint-safe products y*K1(T_old) and
(1-y)*K1(U_old), through total shape-derivative order four.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K284_PATH = Path(__file__).with_name("k284_order_seven_transverse_shape_atlas.py")
K288_MANIFEST = ROOT / "lab/process/k288-order-seven-native-occurrence-measure.json"
K289_MANIFEST = ROOT / "lab/process/k289-order-seven-common-primitive-composition-boundary.json"
OUTPUT = ROOT / "lab/process/k290-order-seven-native-rest-derivative-bank.json"
MAX_ORDER = 4


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K284 = load_module("k284_for_k290", K284_PATH)
K282 = K284.K282
K283 = K284.K283
ctx.dps = K282.ARB_DIGITS
ctx.threads = 1

X_MIN = K282.BASE_X
X_MAX = K282.UPPER_X
RADIUS = K284.SHAPE_RADIUS


def ball(value: Fraction | int) -> arb:
    if isinstance(value, int):
        return arb(value)
    return arb(f"{value.numerator}/{value.denominator}")


def upper_text(value: arb) -> str:
    numeric = float(value.upper())
    return repr(math.nextafter(numeric, math.inf))


def gap_bounds() -> dict[str, tuple[Fraction, Fraction]]:
    return {
        label: (
            K283.PROJECTIVE_GAPS[label] * K283.T_MIN - RADIUS,
            K283.PROJECTIVE_GAPS[label] * K283.T_MAX + RADIUS,
        )
        for label in K284.GAP_LABELS
    }


def bessel_f_derivative_at(argument: Fraction, order: int) -> arb:
    """Absolute derivative of f(q)=2*K1(q) at a positive point."""
    q = ball(argument)
    total = arb(0)
    for index in range(order + 1):
        nu = abs(1 - order + 2 * index)
        total += math.comb(order, index) * q.bessel_k(nu)
    return arb(2) ** (1 - order) * total


def scaled_bessel_derivative_constant(order: int, q_max: Fraction) -> arb:
    """Upper bound for q^(m+1)*|d^m(2K1(q))/dq^m|.

    The derivative recurrence reduces to integer-order K functions.  For
    nu>=1 use q^nu K_nu(q) <= 2^(nu-1)(nu-1)!; for nu=0 use K0<=K1.
    """
    q = ball(q_max)
    total = arb(0)
    for index in range(order + 1):
        nu = abs(1 - order + 2 * index)
        if nu == 0:
            term = q**order
        else:
            term = q ** (order + 1 - nu) * 2 ** (nu - 1) * math.factorial(nu - 1)
        total += math.comb(order, index) * term
    return arb(2) ** (1 - order) * total


def endpoint_homogeneous_factor(order: int, ratio_min: Fraction) -> Fraction:
    if order == 0:
        return Fraction(1)
    return Fraction(order**order, (order + 1) ** (order + 1)) / ratio_min**order


def old_kernel_piece_bounds(ratio_min: Fraction, q_max: Fraction) -> list[arb]:
    """Bounds D^m[y*2K1(x(y+sum r_j a_j))] for arbitrary shape labels."""
    return [
        scaled_bessel_derivative_constant(order, q_max)
        / ball(X_MIN)
        * ball(endpoint_homogeneous_factor(order, ratio_min))
        for order in range(MAX_ORDER + 1)
    ]


def determinant_product_bound(entry_bounds: list[arb], size: int, order: int) -> arb:
    total = arb(0)
    for assignment in itertools.product(range(size), repeat=order):
        counts = [assignment.count(slot) for slot in range(size)]
        term = arb(1)
        for count in counts:
            term *= entry_bounds[count]
        total += term
    return math.factorial(size) * total


def common_cauchy_bounds() -> list[arb]:
    entries = [2 * math.factorial(order) / ball(X_MIN) for order in range(MAX_ORDER + 1)]
    return [determinant_product_bound(entries, 4, order) for order in range(MAX_ORDER + 1)]


def companion_determinant_bounds() -> list[arb]:
    entries = [
        ball(X_MAX) ** order * bessel_f_derivative_at(X_MIN, order)
        for order in range(MAX_ORDER + 1)
    ]
    return [determinant_product_bound(entries, 3, order) for order in range(MAX_ORDER + 1)]


def exponential_density_bounds(bounds: dict[str, tuple[Fraction, Fraction]]) -> list[arb]:
    l_min = Fraction(1) + sum(value[0] for value in bounds.values())
    base = (-ball(256 * X_MIN * l_min)).exp()
    return [base * ball(256 * X_MAX) ** order for order in range(MAX_ORDER + 1)]


def projective_product_bounds(bounds: dict[str, tuple[Fraction, Fraction]]) -> list[arb]:
    uppers = sorted((value[1] for value in bounds.values()), reverse=True)
    rows = []
    for order in range(MAX_ORDER + 1):
        remaining = max(0, len(uppers) - order)
        rows.append(ball(math.prod(uppers[:remaining], start=Fraction(1))))
    return rows


def labelled_product_bound(factors: list[list[arb]], order: int) -> arb:
    total = arb(0)
    for assignment in itertools.product(range(len(factors)), repeat=order):
        counts = [assignment.count(slot) for slot in range(len(factors))]
        term = arb(1)
        for factor, count in zip(factors, counts):
            term *= factor[count]
        total += term
    return total


def factor_bank() -> dict[str, Any]:
    bounds = gap_bounds()
    left_min = bounds["r2"][0]
    right_min = bounds["c2"][0]
    left_q_max = X_MAX * (Fraction(1) + sum(bounds[label][1] for label in ("r0", "r1", "r2")))
    right_q_max = X_MAX * (Fraction(1) + sum(bounds[label][1] for label in ("c0", "c1", "c2")))
    cauchy = common_cauchy_bounds()
    companion = companion_determinant_bounds()
    left_old = old_kernel_piece_bounds(left_min, left_q_max)
    right_old = old_kernel_piece_bounds(right_min, right_q_max)
    exponential = exponential_density_bounds(bounds)
    projective = projective_product_bounds(bounds)
    factors = [exponential, projective, cauchy, companion, left_old, right_old]
    prefactor_upper = Fraction(1, 6**9)  # pi>3, hence (2*pi)^-9 < 6^-9.
    scalar = ball(prefactor_upper) * ball(X_MAX) ** 15
    rest = [scalar * labelled_product_bound(factors, order) for order in range(MAX_ORDER + 1)]
    return {
        "gap_bounds": {key: [str(value[0]), str(value[1])] for key, value in bounds.items()},
        "x_bounds": [str(X_MIN), str(X_MAX)],
        "old_kernel_q_max": {"left": str(left_q_max), "right": str(right_q_max)},
        "old_kernel_ratio_min": {"left": str(left_min), "right": str(right_min)},
        "factor_componentwise_mixed_derivative_abs_upper": {
            "native_exponential": [upper_text(value) for value in exponential],
            "projective_product": [upper_text(value) for value in projective],
            "common_size_four_cauchy_determinant": [upper_text(value) for value in cauchy],
            "companion_size_three_bessel_determinant": [upper_text(value) for value in companion],
            "left_endpoint_safe_old_kernel_piece": [upper_text(value) for value in left_old],
            "right_endpoint_safe_old_kernel_piece": [upper_text(value) for value in right_old],
        },
        "constant_scalar_upper": {
            "native_prefactor_upper": str(prefactor_upper),
            "x_power": 15,
            "x15_prefactor_upper": upper_text(scalar),
        },
        "single_occurrence_rest_componentwise_mixed_derivative_abs_upper": [
            upper_text(value) for value in rest
        ],
        "labelled_product_assignments": {
            str(order): len(factors) ** order for order in range(MAX_ORDER + 1)
        },
    }


def group_bank(occurrences: list[dict[str, Any]], rest: list[arb]) -> list[dict[str, Any]]:
    groups: dict[str, list[int]] = defaultdict(list)
    for row in occurrences:
        groups[str(row["group_id"])].append(int(row["signed_occurrence_weight"]))
    rows = []
    for group_id, weights in sorted(groups.items()):
        positive = sum(weight for weight in weights if weight > 0)
        negative = -sum(weight for weight in weights if weight < 0)
        derivative_bounds = [max(positive, negative) * rest[0]] + [
            sum(abs(weight) for weight in weights) * rest[order]
            for order in range(1, MAX_ORDER + 1)
        ]
        rows.append(
            {
                "group_id": group_id,
                "records": len(weights),
                "signed_weights": weights,
                "positive_weight_sum": positive,
                "negative_weight_abs_sum": negative,
                "absolute_weight_sum": sum(abs(weight) for weight in weights),
                "value_interval_from_positive_rest_factors": [
                    upper_text(-negative * rest[0]),
                    upper_text(positive * rest[0]),
                ],
                "componentwise_mixed_derivative_abs_upper": [
                    upper_text(value) for value in derivative_bounds
                ],
            }
        )
    return rows


def endpoint_controls(bank: dict[str, Any]) -> dict[str, Any]:
    q_max = max(Fraction(bank["old_kernel_q_max"][side]) for side in ("left", "right"))
    rows = []
    for order in range(MAX_ORDER + 1):
        constant = scaled_bessel_derivative_constant(order, q_max)
        for denominator in (2, 8, 32, 128):
            q = Fraction(1, denominator)
            if q > q_max:
                continue
            actual = ball(q) ** (order + 1) * bessel_f_derivative_at(q, order)
            if not actual <= constant:
                raise AssertionError("scaled Bessel derivative control escaped bound")
            rows.append(
                {
                    "order": order,
                    "q": str(q),
                    "scaled_actual_upper": upper_text(actual),
                    "analytic_constant_upper": upper_text(constant),
                    "contained": True,
                }
            )
    return {"rows": rows, "all_contained": True}


def build() -> dict[str, Any]:
    k288 = json.loads(K288_MANIFEST.read_text())
    k289 = json.loads(K289_MANIFEST.read_text())
    occurrences = k288["coherent_gram_measure"]["size_four_occurrences"]
    if len(occurrences) != 24 or len(k289["dependency_census"]["occurrences"]) != 24:
        raise AssertionError("K288/K289 occurrence census changed")
    bank = factor_bank()
    rest = [arb(value) for value in bank["single_occurrence_rest_componentwise_mixed_derivative_abs_upper"]]
    groups = group_bank(occurrences, rest)
    if len(groups) != 4 or {row["records"] for row in groups} != {6}:
        raise AssertionError("expected four coherent groups of six records")
    return {
        "schema_version": "1.0",
        "result_id": "K290-ORDER-SEVEN-NATIVE-REST-DERIVATIVE-BANK",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k288-order-seven-native-occurrence-measure.json",
                "lab/process/k289-order-seven-common-primitive-composition-boundary.json",
            ],
            "native_variables": k289["fixed_control"]["native_variables"],
            "shape_coordinates": list(K284.GAP_LABELS),
            "maximum_shape_derivative_order": MAX_ORDER,
            "occurrences": len(occurrences),
            "coherent_groups": len(groups),
            "records_per_group": 6,
            "arb_decimal_digits": K282.ARB_DIGITS,
            "threads": 1,
        },
        "factorization": {
            "common_factor_excluded": "K284/K286 size-four regularizer R4",
            "rest_factor": "(2*pi)^-9 exp(-256*x*L) x^15 product(r_i c_i) [y*2K1(T_old)] [(1-y)*2K1(U_old)] C4(Todd,Uodd) D3(Teven,Ueven)",
            "endpoint_pairing": "the native y(1-y) density is paired with the two old kernels before either endpoint is bounded",
            "common_size_four_cauchy_skeleton": "C4 is retained in the rest factor; only the regularizer R4 is excluded",
            "companion": "the complete size-three Bessel determinant D3 is bounded directly, preserving coalescent zeros without division",
        },
        "endpoint_theorem": {
            "bessel_recurrence": "|d^m(2K1(q))/dq^m| = 2^(1-m) sum_k binom(m,k) K_|1-m+2k|(q)",
            "integer_order_bound": "q^nu K_nu(q) <= 2^(nu-1)(nu-1)! for integer nu>=1; K0(q)<=K1(q)",
            "homogeneous_maximum": "sup_{y,a>=0} y*a^m/(y+r*a)^(m+1) = m^m/((m+1)^(m+1) r^m) for m>=1",
            "mixed_labels": "AM-GM reduces distinct participating shape coefficients to the repeated-label homogeneous bound",
            "all_orders_finite": True,
        },
        "derivative_bank": bank,
        "coherent_group_bank": groups,
        "independent_controls": endpoint_controls(bank),
        "decision": {
            "complete_sixteen_variable_rest_factor_typed": True,
            "shape_derivatives_through_order_four_serialized": True,
            "all_four_coherent_group_sums_retained_before_absolute_enclosure": True,
            "common_size_four_regularizer_composed": False,
            "next_exact_input": "compose each coherent-group rest bank with K284/K286 by the complete fourth-order product rule, then apply the K287 positive tensor remainder and identify the dominant factor family",
        },
        "release_test": {
            "all_24_occurrences_replayed": len(occurrences) == 24,
            "all_four_groups_have_six_records": len(groups) == 4 and all(row["records"] == 6 for row in groups),
            "old_kernel_endpoint_singularities_paired_with_native_density": True,
            "all_labelled_product_assignments_through_order_four_retained": True,
            "native_weighted_interior_remainder_serialized": False,
            "complete_arbitrary_gap_ratio_domain_covered": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k288["ledger_effect"],
        "claim_ceiling": "Rigorous componentwise shape-derivative envelopes through order four for the complete native rest factor of all 24 order-seven size-four occurrences on the K284 tube, with four coherent six-entry groups retained before absolute enclosure. No composed native interior remainder, tube volume, radial/projective exterior bound, action-column value, complete residual, native K152 interval, physical state, source/ledger move, canon, paper or public claim.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
