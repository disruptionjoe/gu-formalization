#!/usr/bin/env python3
"""Independent raw-allocation/Newton replay for K256's selected rays."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
RECORD = ROOT / "lab/process/k256-order-six-binary-face-sign-reversal.json"
POSITIVE, NEGATIVE = 0x18, 0x14


def raw_terms(source: dict):
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    for entry in source["complete_face_hypergraph"]["entries"]:
        outer = entry["coefficient_product"] * (2 if entry["left"] != entry["right"] else 1)
        for term in entry["terms"]:
            masks = tuple(
                int(value, 16)
                for value in catalog[term["allocation_id"]]["support_masks_hex"].split(",")
            )
            yield outer * term["leibniz_sign"], masks


def groups(items, mask: int, absolute_weights: bool = False):
    out = defaultdict(int)
    for weight, masks in items:
        factors = []
        for row in range(14):
            active = sum(
                bool(mask & (1 << axis) and masks[axis] & (1 << row))
                for axis in range(8)
            )
            fixed = 256 + sum(
                bool(not mask & (1 << axis) and masks[axis] & (1 << row))
                for axis in range(8)
            )
            factors.append((int(active), int(fixed)))
        out[tuple(sorted(factors))] += abs(weight) if absolute_weights else weight
    return {key: value for key, value in out.items() if value}


def newton_h(values: list[Q], maximum: int) -> list[Q]:
    power_sums = [Q(0)] + [sum((value**k for value in values), Q(0)) for k in range(1, maximum + 1)]
    h = [Q(1)] + [Q(0)] * maximum
    for n in range(1, maximum + 1):
        h[n] = sum((power_sums[k] * h[n - k] for k in range(1, n + 1)), Q(0)) / n
    return h


def analyze(grouped, radius: int):
    data = []
    coefficients = defaultdict(Q)
    for factors, weight in grouped.items():
        exponent, base, ratios = 0, Q(1), []
        for active, fixed in factors:
            if active:
                exponent += 1
                base /= active
                ratios.append(Q(fixed, active))
            else:
                base /= fixed
        hs = newton_h(ratios, 15)
        data.append((weight, exponent, base, ratios, hs))
        for extra in range(15):
            coefficients[exponent + extra] += weight * base * (-1) ** extra * hs[extra]
    leading_exponent, leading = next((key, value) for key, value in sorted(coefficients.items()) if value)
    bound = Q(0)
    for weight, exponent, base, ratios, hs in data:
        if exponent > leading_exponent:
            bound += abs(weight) * base / radius ** (exponent - leading_exponent)
            continue
        n = leading_exponent - exponent
        ratio = max(ratios) * Q(n + 1 + len(ratios), n + 2) / radius
        bound += abs(weight) * base * hs[n + 1] / radius / (1 - ratio)
    return leading_exponent, leading, bound


def exact_core(items, mask: int, radius: int) -> Q:
    total = Q(0)
    for weight, masks in items:
        product = 1
        for row in range(14):
            load = 256 + sum(
                radius if mask & (1 << axis) else 1
                for axis in range(8)
                if masks[axis] & (1 << row)
            )
            product *= load
        total += Q(weight, product)
    return total


def main() -> None:
    items = list(raw_terms(json.loads(K185.read_text())))
    record = json.loads(RECORD.read_text())
    assert len(items) == 1864
    selected = record["selected_same_dimension_sign_reversal"]
    assert selected["threshold"] == 4096

    expected = ((POSITIVE, 5, 1), (NEGATIVE, 6, -1))
    for mask, expected_exponent, expected_sign in expected:
        grouped = groups(items, mask)
        exponent, leading, bound = analyze(grouped, 4096)
        _, _, low_bound = analyze(grouped, 2048)
        value = exact_core(items, mask, 4096)
        assert exponent == expected_exponent
        assert (leading > 0) - (leading < 0) == expected_sign
        assert (value > 0) - (value < 0) == expected_sign
        assert bound < abs(leading) < low_bound
        row = selected["positive_ray" if expected_sign > 0 else "negative_ray"]
        assert row["leading_coefficient"] == str(leading)
        assert row["exact_value_at_4096_sha256"] == hashlib.sha256(str(value).encode()).hexdigest()

    # Hostile control: removing every signed cancellation makes both selected
    # grouped functions positive and destroys the opposite-sign theorem.
    for mask in (POSITIVE, NEGATIVE):
        _, leading, _ = analyze(groups(items, mask, absolute_weights=True), 4096)
        assert leading > 0

    # The displayed interpolation keeps c4 fixed at R, so it remains on the
    # max-coordinate boundary throughout and really joins the selected rays.
    assert POSITIVE & (1 << 4) and NEGATIVE & (1 << 4)
    assert POSITIVE ^ NEGATIVE == (1 << 2) | (1 << 3)
    print("[PASS] K256 independent raw/Newton rays, corrected tail, hostile sign, shell path")


if __name__ == "__main__":
    main()
