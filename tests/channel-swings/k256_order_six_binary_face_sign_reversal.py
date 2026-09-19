#!/usr/bin/env python3
"""K256: exact binary-face cancellation and far-shell sign reversal.

This classifies the exact K185/K218 rational-cosh core on every nonempty
binary face ray.  It does not integrate the product-cosh shell measure.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
import hashlib
import json

from k225_order_six_diagonal_cancellation import (
    K185,
    OUT as K225,
    ROOT,
    core,
    terms,
)


K218 = ROOT / "lab/process/k218-order-six-exact-angular-elimination.json"
K248 = ROOT / "lab/process/k248-order-six-q16-sign-reversal.json"
OUT = ROOT / "lab/process/k256-order-six-binary-face-sign-reversal.json"
SEARCH_THRESHOLDS = tuple(2**power for power in range(9, 24))
SELECTED_POSITIVE = 0x18  # c3=c4=R
SELECTED_NEGATIVE = 0x14  # c2=c4=R
SELECTED_THRESHOLD = 4096


def complete_homogeneous(values: list[Q], degree: int) -> Q:
    coefficients = [Q(1)] + [Q(0)] * degree
    for value in values:
        updated = [Q(0)] * (degree + 1)
        power = Q(1)
        for k in range(degree + 1):
            for old_degree in range(degree + 1 - k):
                updated[k + old_degree] += coefficients[old_degree] * power
            power *= value
        coefficients = updated
    return coefficients[degree]


def ray_groups(items: list[tuple[int, tuple[int, ...]]], mask: int) -> dict[tuple, int]:
    groups: defaultdict[tuple, int] = defaultdict(int)
    for weight, supports in items:
        factors = []
        for row in range(14):
            active = sum(
                1
                for axis in range(8)
                if mask & (1 << axis) and supports[axis] & (1 << row)
            )
            fixed = 256 + sum(
                1
                for axis in range(8)
                if not mask & (1 << axis) and supports[axis] & (1 << row)
            )
            factors.append((active, fixed))
        groups[tuple(sorted(factors))] += weight
    return {factors: weight for factors, weight in groups.items() if weight}


def group_series_data(groups: dict[tuple, int]) -> list[tuple[int, int, Q, list[Q]]]:
    data = []
    for factors, weight in groups.items():
        exponent = 0
        base = Q(1)
        ratios: list[Q] = []
        for active, fixed in factors:
            if active:
                exponent += 1
                base /= active
                ratios.append(Q(fixed, active))
            else:
                base /= fixed
        data.append((weight, exponent, base, ratios))
    return data


def leading_term(data: list[tuple[int, int, Q, list[Q]]]) -> tuple[int, Q]:
    coefficients: defaultdict[int, Q] = defaultdict(Q)
    for weight, exponent, base, ratios in data:
        for extra in range(15):
            coefficients[exponent + extra] += (
                weight
                * base
                * (-1) ** extra
                * complete_homogeneous(ratios, extra)
            )
    for exponent, coefficient in sorted(coefficients.items()):
        if coefficient:
            return exponent, coefficient
    raise AssertionError("nonzero grouped ray did not expose a leading term")


def normalized_tail_bound(
    data: list[tuple[int, int, Q, list[Q]]],
    leading_exponent: int,
    radius: int,
) -> Q | None:
    """Bound |R^e H(R)-L| after all globally cancelled coefficients.

    Groups starting after e are bounded in full.  Earlier groups are expanded
    through e and their complete-homogeneous tails are continued geometrically.
    """
    bound = Q(0)
    for weight, exponent, base, ratios in data:
        if exponent > leading_exponent:
            bound += abs(weight) * base / radius ** (exponent - leading_exponent)
            continue
        truncation = leading_exponent - exponent
        first = complete_homogeneous(ratios, truncation + 1) / radius
        ratio = (
            max(ratios, default=Q(0))
            * Q(truncation + 1 + len(ratios), truncation + 2)
            / radius
        )
        if ratio >= 1:
            return None
        bound += abs(weight) * base * first / (1 - ratio)
    return bound


def ray_record(items: list[tuple[int, tuple[int, ...]]], mask: int) -> dict:
    groups = ray_groups(items, mask)
    axes = [axis for axis in range(8) if mask & (1 << axis)]
    if not groups:
        return {
            "mask_hex": f"0x{mask:02x}",
            "axes": axes,
            "active_count": len(axes),
            "reduced_groups": 0,
            "status": "IDENTICALLY_ZERO_COEFFICIENTWISE",
        }
    data = group_series_data(groups)
    exponent, coefficient = leading_term(data)
    threshold = None
    remainder = None
    for candidate in SEARCH_THRESHOLDS:
        bound = normalized_tail_bound(data, exponent, candidate)
        if bound is not None and bound < abs(coefficient):
            threshold, remainder = candidate, bound
            break
    if threshold is None or remainder is None:
        raise AssertionError(f"no finite sign threshold found for mask {mask:#x}")
    return {
        "mask_hex": f"0x{mask:02x}",
        "axes": axes,
        "active_count": len(axes),
        "reduced_groups": len(groups),
        "status": "NONZERO_ASYMPTOTIC_SIGN_CERTIFIED",
        "leading_exponent": exponent,
        "leading_sign": 1 if coefficient > 0 else -1,
        "leading_coefficient_sha256": hashlib.sha256(str(coefficient).encode()).hexdigest(),
        "certified_for_R_at_least": threshold,
        "normalized_remainder_to_leading_upper": str(remainder / abs(coefficient)),
    }


def selected_witness(items, mask: int, expected_sign: int) -> dict:
    groups = ray_groups(items, mask)
    data = group_series_data(groups)
    exponent, coefficient = leading_term(data)
    bound = normalized_tail_bound(data, exponent, SELECTED_THRESHOLD)
    lower_threshold_bound = normalized_tail_bound(data, exponent, SELECTED_THRESHOLD // 2)
    assert bound is not None and lower_threshold_bound is not None
    coordinates = tuple(
        Q(SELECTED_THRESHOLD) if mask & (1 << axis) else Q(1)
        for axis in range(8)
    )
    exact_value = core(items, coordinates)
    assert (coefficient > 0) - (coefficient < 0) == expected_sign
    assert (exact_value > 0) - (exact_value < 0) == expected_sign
    assert bound < abs(coefficient)
    assert lower_threshold_bound > abs(coefficient)
    return {
        "mask_hex": f"0x{mask:02x}",
        "axes": [axis for axis in range(8) if mask & (1 << axis)],
        "leading_exponent": exponent,
        "leading_coefficient": str(coefficient),
        "normalized_remainder_upper_at_4096": str(bound),
        "remainder_to_leading_upper_at_4096": str(bound / abs(coefficient)),
        "lower_threshold_2048_fails_this_proof": lower_threshold_bound > abs(coefficient),
        "exact_value_at_4096_sign": expected_sign,
        "exact_value_at_4096_sha256": hashlib.sha256(str(exact_value).encode()).hexdigest(),
    }


def generate() -> dict:
    items = list(terms(json.loads(K185.read_text())))
    assert len(items) == 1864
    rays = [ray_record(items, mask) for mask in range(1, 256)]
    zero = [row for row in rays if row["status"].startswith("IDENTICALLY")]
    nonzero = [row for row in rays if row["status"].startswith("NONZERO")]
    signs = Counter(row["leading_sign"] for row in nonzero)
    exponents = Counter(row["leading_exponent"] for row in nonzero)
    thresholds = Counter(row["certified_for_R_at_least"] for row in nonzero)
    assert len(zero) == 95 and len(nonzero) == 160
    assert signs == {1: 84, -1: 76}
    assert max(row["certified_for_R_at_least"] for row in nonzero) == 262144

    positive = selected_witness(items, SELECTED_POSITIVE, 1)
    negative = selected_witness(items, SELECTED_NEGATIVE, -1)
    assert positive["leading_exponent"] == 5
    assert negative["leading_exponent"] == 6

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "conditional_internal_structure_not_forward_physics_credit",
        "input_sha256": {
            path.stem.split("-")[0]: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (K185, K218, K225, K248)
        },
        "object": (
            "The original signed 1,864-term K185/K218 rational-cosh core H, "
            "before the positive product-cosh density and pi^-8 normalization"
        ),
        "binary_face_ray": (
            "For each nonempty S subset {0,...,7}, set c_j=R for j in S and c_j=1 otherwise. "
            "Every denominator is a_i R+b_i with nonnegative integer a_i and positive integer b_i."
        ),
        "census": {
            "nonempty_binary_rays": len(rays),
            "coefficientwise_identically_zero": len(zero),
            "nonzero": len(nonzero),
            "positive_leading_sign": signs[1],
            "negative_leading_sign": signs[-1],
            "leading_exponent_counts": {str(key): value for key, value in sorted(exponents.items())},
            "certified_threshold_counts": {str(key): value for key, value in sorted(thresholds.items())},
            "maximum_certified_threshold": max(thresholds),
            "rays": rays,
        },
        "proof": {
            "exact_zero": (
                "Group terms by the unordered multiset of fourteen affine pairs (a_i,b_i). "
                "If every grouped integer coefficient is zero, the entire rational function vanishes identically."
            ),
            "leading_sign": (
                "For each surviving group factor R^-e prod a_i^-1 prod(1+(b_i/a_i)/R)^-1, "
                "sum exact complete-homogeneous Laurent coefficients until the first globally nonzero coefficient L."
            ),
            "uniform_tail": (
                "Groups starting above the leading exponent are bounded in full. Earlier groups are expanded through L; "
                "their first omitted complete-homogeneous coefficient is continued using "
                "h_(n+1)/h_n <= r_max*(n+m)/(n+1). At the recorded power-of-two threshold the normalized remainder is below |L|, "
                "so the leading sign holds for every larger R."
            ),
        },
        "selected_same_dimension_sign_reversal": {
            "threshold": SELECTED_THRESHOLD,
            "positive_ray": positive,
            "negative_ray": negative,
            "continuous_shell_path": (
                "Keep c4=R and all other unlisted coordinates equal to 1; set "
                "c2(s)=1+s(R-1), c3(s)=R-s(R-1), 0<=s<=1. "
                "The path lies on the boundary max_j c_j=R and joins the positive {3,4} ray to the negative {2,4} ray."
            ),
            "theorem": (
                "For every R>=4096, H has both signs on the boundary of [1,R]^8. "
                "Continuity and positive denominators force at least one zero on the displayed path; strict endpoint signs also give relative-open sign neighborhoods."
            ),
        },
        "controls": (
            "Independent raw-allocation/Newton replay of both selected rays; direct exact values at R=4096; "
            "the corrected proof rejects R=2048 after including groups whose leading exponent exceeds the global leading exponent; "
            "an absolute-weight mutation removes the signed theorem."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; "
            "LT-GR6b/LT-SM8/RA-F1/AC-F1 remain NEEDS."
        ),
        "decision": (
            "A genuine pointwise farther-region sign-reversal theorem exists and rules out an eventually one-signed K218 core. "
            "It does not supply the weighted measure, magnitude, or region-volume balance needed to cancel K247's positive cumulative prefix."
        ),
        "claim_ceiling": (
            "Exact binary-face rational identities, asymptotic signs, two same-dimensional sign-separated rays, and a zero crossing "
            "on every shell boundary R>=4096 only. No integrated K218 shell cancellation, global tail sign, full-error lower bound, "
            "K215 impossibility, source/ledger/canon/paper/public-posture change, or physical positivity."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K256 binary rays", result["census"]["coefficientwise_identically_zero"], result["census"]["nonzero"])
    print("[PASS] K256 signs", result["census"]["positive_leading_sign"], result["census"]["negative_leading_sign"])
    print("[PASS] K256 shell sign reversal R>=", result["selected_same_dimension_sign_reversal"]["threshold"])
