#!/usr/bin/env python3
"""Independent raw-entry/Newton-power-sum replay of K234's grouped theorem."""
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
PRIOR = ROOT / "lab/process/k233-order-six-two-exception-local-radius.json"
MANIFEST = ROOT / "lab/process/k234-order-six-grouped-two-exception-radius.json"
ANCHOR = (F(5, 4), F(17, 8)) + (F(1),) * 6


def raw_entries():
    source = json.loads(SOURCE.read_text())
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    for entry in source["complete_face_hypergraph"]["entries"]:
        outer = entry["coefficient_product"] * (1 if entry["left"] == entry["right"] else 2)
        for term in entry["terms"]:
            masks = [int(s, 16) for s in catalog[term["allocation_id"]]["support_masks_hex"].split(",")]
            yield outer * term["leibniz_sign"], masks


def complete_h(rates, degree):
    """Newton identity k*h_k=sum_(j=1)^k p_j*h_(k-j)."""
    p = [sum((r**j for r in rates), F()) for j in range(1, degree+1)]
    h = [F(1)]
    for k in range(1, degree+1):
        h.append(sum((p[j-1]*h[k-j] for j in range(1, k+1)), F())/k)
    return h[degree]


def replay(entries):
    grouped = defaultdict(F)
    raw_c5 = F()
    for weight, masks in entries:
        for first, second in combinations(range(2, 8), 2):
            factors = [(256 + sum(ANCHOR[j] for j in range(8) if masks[j] >> i & 1),
                        (masks[first] >> i & 1) + (masks[second] >> i & 1))
                       for i in range(14)]
            at_zero = F(weight, 15)
            rates = []
            key = []
            for a, n in factors:
                at_zero /= a
                if n:
                    rates.append(F(n, a))
                    key.append(F(a, n))
            raw_c5 -= at_zero * complete_h(rates, 5)
            grouped[tuple(sorted(key))] += at_zero
    b6 = F()
    for key, normalized_at_zero in grouped.items():
        b6 += abs(normalized_at_zero)*complete_h([1/d for d in key], 6)
    return len(grouped), sum(bool(w) for w in grouped.values()), raw_c5, b6


def main():
    manifest = json.loads(MANIFEST.read_text())
    prior = json.loads(PRIOR.read_text())
    assert manifest["input_sha256"] == {
        "k185": sha256(SOURCE.read_bytes()).hexdigest(),
        "k233": sha256(PRIOR.read_bytes()).hexdigest()}
    entries = list(raw_entries())
    assert len(entries) == manifest["raw_signed_terms"] == 1864
    count, nonzero, c5, b6 = replay(entries)
    assert (count, nonzero) == (manifest["normalized_denominator_groups"],
                                manifest["nonzero_group_coefficients"]) == (576, 398)
    assert c5 == F(manifest["signed_fifth_coefficient_C5"]) < 0
    assert b6 == F(manifest["grouped_sixth_bound_B6"]) > 0
    a = F(prior["fourth_coefficient_A"])
    assert a == F(manifest["fourth_coefficient_A"])
    assert a+c5-b6 == F(manifest["unit_interval_lower_at_one"]) > 0
    # Check the algebraic grouping away from zero, including the certified edge.
    grouped = defaultdict(F)
    for weight, masks in entries:
        for pair in combinations(range(2, 8), 2):
            factors = [(256+sum(ANCHOR[j] for j in range(8) if masks[j] >> i & 1),
                        sum(masks[j] >> i & 1 for j in pair)) for i in range(14)]
            at_zero = F(weight, 15)
            key = []
            for load, slope in factors:
                at_zero /= load
                if slope:
                    key.append(F(load, slope))
            grouped[tuple(sorted(key))] += at_zero
    for h in (F(1, 3), F(1)):
        direct = grouped_value = F()
        for weight, masks in entries:
            for pair in combinations(range(2, 8), 2):
                term = F(weight, 15)
                for i in range(14):
                    load = 256+sum(ANCHOR[j] for j in range(8) if masks[j] >> i & 1)
                    slope = sum(masks[j] >> i & 1 for j in pair)
                    term /= load+slope*h
                direct += term
        for key, weight in grouped.items():
            term = weight
            for d in key:
                term /= 1+h/d
            grouped_value += term
        assert direct == grouped_value
        assert direct > h**4*(a+c5*h-b6*h*h) > 0
    corrupt = entries.copy()
    weight, masks = corrupt[0]
    corrupt[0] = (-weight, masks)
    assert replay(corrupt)[2] != c5 and replay(corrupt)[3] != b6
    print("[PASS] K234 independent raw/Newton replay, functional identity and hostile sign")


if __name__ == "__main__":
    main()
