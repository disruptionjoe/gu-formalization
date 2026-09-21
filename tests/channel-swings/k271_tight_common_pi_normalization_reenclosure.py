#!/usr/bin/env python3
"""Exact K271 common-pi re-enclosure of stored K265--K269 raw intervals."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k271-tight-common-pi-normalization-reenclosure.json"
SOURCES = {
    "K265": (ROOT / "lab/process/k265-order-nine-complete-binary-low-high-union.json", "complete_binary_union"),
    "K266": (ROOT / "lab/process/k266-order-nine-first-fixed-axis-middle-collar.json", "complete_collar"),
    "K267": (ROOT / "lab/process/k267-order-nine-exchangeable-axis-middle-collar.json", "complete_collar"),
    "K268": (ROOT / "lab/process/k268-order-nine-two-exchangeable-axis-middle-collar.json", "complete_collar"),
    "K269": (ROOT / "lab/process/k269-order-nine-three-plus-exchangeable-axis-middle-collar.json", "complete_collar"),
}
BALL = re.compile(r"\[([^ ]+) \+/- ([^\]]+)\]")
COMMON_CONSTANT = Fraction(2**8 * 256**6, 120)


class CertificateError(ValueError):
    """Raised when a stored interval or proof parameter is invalid."""


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def exact_hash(value: Fraction) -> str:
    return sha256_bytes(str(value).encode())


def parse_ball(text: str) -> tuple[Fraction, Fraction]:
    match = BALL.fullmatch(text)
    if match is None:
        raise CertificateError(f"unsupported outward ball: {text!r}")
    center, radius = Fraction(match.group(1)), Fraction(match.group(2))
    if radius < 0:
        raise CertificateError("ball radius must be nonnegative")
    return center - radius, center + radius


def atan_alternating_bounds(inverse: int, last_term: int) -> tuple[Fraction, Fraction]:
    """Exact alternating-series bounds for atan(1/inverse)."""
    if inverse <= 1 or last_term < 1:
        raise CertificateError("atan proof requires inverse>1 and at least two terms")
    x = Fraction(1, inverse)
    partials: list[Fraction] = []
    total = Fraction()
    for k in range(last_term + 1):
        total += (-1) ** k * x ** (2 * k + 1) / (2 * k + 1)
        partials.append(total)
    if last_term % 2:
        lower, upper = partials[last_term], partials[last_term - 1]
    else:
        lower, upper = partials[last_term - 1], partials[last_term]
    if not lower < upper:
        raise AssertionError("alternating-series parity failure")
    return lower, upper


def machin_pi_bounds(a_last: int = 50, b_last: int = 12) -> tuple[Fraction, Fraction]:
    a_lower, a_upper = atan_alternating_bounds(5, a_last)
    b_lower, b_upper = atan_alternating_bounds(239, b_last)
    lower = 16 * a_lower - 4 * b_upper
    upper = 16 * a_upper - 4 * b_lower
    if not 3 < lower < upper < 4:
        raise AssertionError("Machin pi interval failed")
    return lower, upper


def decimal_summary(value: Fraction, digits: int = 36) -> str:
    with localcontext() as context:
        context.prec = digits
        return format(Decimal(value.numerator) / Decimal(value.denominator), ".24e")


def interval_record(lower: Fraction, upper: Fraction) -> dict[str, str]:
    if lower > upper:
        raise CertificateError("interval endpoints are reversed")
    return {
        "lower_decimal": decimal_summary(lower),
        "upper_decimal": decimal_summary(upper),
        "lower_exact_sha256": exact_hash(lower),
        "upper_exact_sha256": exact_hash(upper),
        "width_decimal": decimal_summary(upper - lower),
        "width_exact_sha256": exact_hash(upper - lower),
    }


def compute_certificate() -> dict[str, Any]:
    pi_lower, pi_upper = machin_pi_bounds()
    factor_lower = COMMON_CONSTANT / pi_upper**8
    factor_upper = COMMON_CONSTANT / pi_lower**8
    rows: dict[str, Any] = {}
    raw_sum_lower = Fraction()
    raw_sum_upper = Fraction()
    old_sum_lower = Fraction()
    old_sum_upper = Fraction()

    for result_id, (path, key) in SOURCES.items():
        payload = path.read_bytes()
        data = json.loads(payload)[key]
        raw_lower, _ = parse_ball(data["complete_raw_integral_interval"]["lower"])
        _, raw_upper = parse_ball(data["complete_raw_integral_interval"]["upper"])
        old_lower, _ = parse_ball(data["normalized_integral_interval"]["lower"])
        _, old_upper = parse_ball(data["normalized_integral_interval"]["upper"])
        if raw_lower <= 0:
            raise CertificateError(f"{result_id} complete raw lower must be positive")
        tight_lower = raw_lower * factor_lower
        tight_upper = raw_upper * factor_upper
        old_width = old_upper - old_lower
        tight_width = tight_upper - tight_lower
        rows[result_id] = {
            "source": str(path.relative_to(ROOT)),
            "source_sha256": sha256_bytes(payload),
            "raw_interval_exact_sha256": sha256_bytes(f"{raw_lower}|{raw_upper}".encode()),
            "published_coarse_width_decimal": decimal_summary(old_width),
            "published_coarse_width_exact_sha256": exact_hash(old_width),
            "tight_normalized": interval_record(tight_lower, tight_upper),
            "width_reduction_factor_decimal": decimal_summary(old_width / tight_width),
        }
        raw_sum_lower += raw_lower
        raw_sum_upper += raw_upper
        old_sum_lower += old_lower
        old_sum_upper += old_upper

    tight_sum_lower = raw_sum_lower * factor_lower
    tight_sum_upper = raw_sum_upper * factor_upper
    old_sum_width = old_sum_upper - old_sum_lower
    tight_sum_width = tight_sum_upper - tight_sum_lower
    return {
        "machin_pi": {
            "identity": "pi=16*atan(1/5)-4*atan(1/239)",
            "atan_1_over_5_last_term": 50,
            "atan_1_over_239_last_term": 12,
            "endpoint_rule": "odd partial is lower; preceding even partial is upper; subtraction reverses the atan(1/239) endpoints",
            "lower": str(pi_lower),
            "upper": str(pi_upper),
            "width_decimal": decimal_summary(pi_upper - pi_lower),
        },
        "common_normalization": {
            "symbolic": "2^8*256^6/(5!*pi^8)",
            "constant_without_pi": str(COMMON_CONSTANT),
            "factor_lower_decimal": decimal_summary(factor_lower),
            "factor_upper_decimal": decimal_summary(factor_upper),
            "factor_lower_exact_sha256": exact_hash(factor_lower),
            "factor_upper_exact_sha256": exact_hash(factor_upper),
        },
        "per_result": rows,
        "common_sum": {
            "members": list(SOURCES),
            "raw_symbolic_sum": interval_record(raw_sum_lower, raw_sum_upper),
            "published_coarse_sum_width_decimal": decimal_summary(old_sum_width),
            "published_coarse_sum_width_exact_sha256": exact_hash(old_sum_width),
            "tight_common_normalized": interval_record(tight_sum_lower, tight_sum_upper),
            "width_reduction_factor_decimal": decimal_summary(old_sum_width / tight_sum_width),
        },
    }


def metadata_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        failures.append("classification")
    if data.get("direction") != "observed_to_native":
        failures.append("direction")
    r4 = data.get("reassessment_disposition", {}).get("R4", {})
    if r4.get("state") != "concluded" or r4.get("new_boxes_compiled") is not False:
        failures.append("R4")
    boundaries = data.get("boundaries", {})
    denied = (
        "uncomputed_K218_complement_controlled",
        "full_K218_integral_sign",
        "complete_order_six_error",
        "K270_native_consumer_inputs_instantiated",
        "source_claim_change",
        "physics_ledger_change",
        "canon_change",
        "paper_or_public_posture_change",
    )
    if any(boundaries.get(key) is not False for key in denied):
        failures.append("boundaries")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    computed = compute_certificate()
    if args.emit:
        print(json.dumps(computed, indent=2, sort_keys=True))
        return 0
    data = json.loads(MANIFEST.read_text())
    failures = metadata_failures(data)
    if data.get("certificate") != computed:
        failures.append("certificate replay")
    if failures:
        print(f"FAIL K271: {failures}")
        return 1
    if args.selftest:
        attacks = [
            lambda: parse_ball("1.0"),
            lambda: parse_ball("[1 +/- -1]"),
            lambda: atan_alternating_bounds(1, 4),
            lambda: atan_alternating_bounds(5, 0),
        ]
        caught = 0
        for attack in attacks:
            try:
                attack()
            except CertificateError:
                caught += 1
        if caught != len(attacks):
            print(f"FAIL K271 hostile controls caught {caught}/{len(attacks)}")
            return 1
        print(f"PASS K271 hostile controls caught {caught}/{len(attacks)}")
    print("PASS K271 exact common-pi re-enclosure for K265--K269")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
