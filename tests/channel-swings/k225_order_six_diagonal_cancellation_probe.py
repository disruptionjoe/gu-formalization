#!/usr/bin/env python3
"""Independent raw-entry replay of the K225 symbolic denominator certificate."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
MANIFEST = ROOT / "lab/process/k225-order-six-diagonal-cancellation.json"


def raw(source):
    allocations = source["exact_allocation_certificate"]["allocation_catalog"]
    for group in source["complete_face_hypergraph"]["entries"]:
        factor = group["coefficient_product"] * (1 if group["left"] == group["right"] else 2)
        for row in group["terms"]:
            bits = [int(s, 16) for s in allocations[row["allocation_id"]]["support_masks_hex"].split(",")]
            yield factor * row["leibniz_sign"], bits


def bucket(raw_rows, free):
    result = Counter()
    fixed = [j for j in range(8) if j not in free]
    for weight, masks in raw_rows:
        factors = []
        for i in range(14):
            factors.append((sum((masks[j] >> i) & 1 for j in fixed),
                            *( (masks[j] >> i) & 1 for j in free)))
        result[tuple(sorted(factors))] += weight
    return result


def point(raw_rows, c):
    answer = Fraction(0)
    for weight, masks in raw_rows:
        denominator = 1
        for i in range(14):
            denominator *= 256 + sum(c[j] for j in range(8) if (masks[j] >> i) & 1)
        answer += weight / denominator
    return answer


def raw_second_majorant(raw_rows, lower, j, k):
    """Differentiate the fourteen factors by ordered pairs, including i=h twice."""
    total = Fraction(0)
    for weight, masks in raw_rows:
        a = [256 + sum(lower[h] for h in range(8) if (masks[h] >> i) & 1)
             for i in range(14)]
        product = 1
        for factor in a:
            product *= factor
        derivative_factor = sum(
            (1 + (i == h)) / (a[i] * a[h])
            for i in range(14) if (masks[j] >> i) & 1
            for h in range(14) if (masks[k] >> h) & 1
        )
        total += abs(weight) * derivative_factor / product
    return total


def main():
    doc = json.loads(MANIFEST.read_text())
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == doc["input_sha256"]["k185"]
    source = json.loads(SOURCE.read_text())
    raw_rows = list(raw(source))
    assert len(raw_rows) == doc["raw_signed_terms"] == 1864
    for free in ((0, 1), *((0, 1, j) for j in range(2, 8))):
        grouped = bucket(raw_rows, free)
        record = doc["certified_strata"][",".join(map(str, free))]
        assert len(grouped) == record["factor_multisets"]
        assert all(not coefficient for coefficient in grouped.values())
        # A sign error in one original term cannot retain this certificate.
        corrupted = [(w, m) for w, m in raw_rows]
        corrupted[0] = (-corrupted[0][0], corrupted[0][1])
        assert any(bucket(corrupted, free).values())
    for first in (Fraction(1), Fraction(5, 4), Fraction(17, 8)):
        for second in (Fraction(1), Fraction(5, 4)):
            for j in range(2, 8):
                c = [first, second] + [Fraction(1)] * 6
                c[j] = Fraction(17, 8)
                assert point(raw_rows, c) == 0
    mixed = tuple(map(Fraction, doc["mixed_control"]["coshes"]))
    value = point(raw_rows, mixed)
    assert value == Fraction(doc["mixed_control"]["core_exact"]) != 0
    lower = mixed[:2] + (Fraction(1),) * 6
    majorant = sum((mixed[j]-1)*(mixed[k]-1)*raw_second_majorant(raw_rows, lower, j, k)
                   for j in range(2, 8) for k in range(j+1, 8))
    assert majorant == Fraction(doc["mixed_control"]["majorant_exact"])
    assert abs(value) <= majorant
    assert any(bucket(raw_rows, (2, 4)).values())
    print("[PASS] independent raw grouping, 36 zero points, ordered-pair Hessian majorant, mixed nonzero and hostile sign")


if __name__ == "__main__":
    main()
