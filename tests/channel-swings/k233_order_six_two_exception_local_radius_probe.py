#!/usr/bin/env python3
"""Independent raw-entry and power-sum replay of K233's local certificate."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
import json
from math import prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
MANIFEST = ROOT / "lab/process/k233-order-six-two-exception-local-radius.json"
ANCHOR = (F(5, 4), F(17, 8)) + (F(1),) * 6


def raw_entries():
    source = json.loads(SOURCE.read_text())
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    for entry in source["complete_face_hypergraph"]["entries"]:
        outer = entry["coefficient_product"] * (1 if entry["left"] == entry["right"] else 2)
        for term in entry["terms"]:
            masks = tuple(int(s, 16) for s in catalog[term["allocation_id"]]["support_masks_hex"].split(","))
            yield outer * term["leibniz_sign"], masks


def replay(entries):
    fourth = fifth_bound = F()
    for weight, masks in entries:
        loads = [256 + sum(ANCHOR[j] for j in range(8) if masks[j] & (1 << i))
                 for i in range(14)]
        q = F(1, prod(loads))
        for pair in combinations(range(2, 8), 2):
            r = [F(sum(bool(masks[j] & (1 << i)) for j in pair), loads[i])
                 for i in range(14)]
            s1 = sum(r, F())
            s2 = sum((x*x for x in r), F())
            s3 = sum((x**3 for x in r), F())
            s4 = sum((x**4 for x in r), F())
            h4 = (s1**4 + 6*s1*s1*s2 + 3*s2*s2 + 8*s1*s3 + 6*s4) / 24
            fourth += weight*q*h4 / 15
            fifth_bound += abs(weight)*q*s1**5 / 15
    return fourth, fifth_bound


def main():
    manifest = json.loads(MANIFEST.read_text())
    assert manifest["input_sha256"]["k185"] == sha256(SOURCE.read_bytes()).hexdigest()
    entries = list(raw_entries())
    assert len(entries) == manifest["raw_signed_terms"] == 1864
    a, b5 = replay(entries)
    assert a == F(manifest["fourth_coefficient_A"]) > 0
    assert b5 == F(manifest["absolute_fifth_bound_B5"]) > 0
    assert a/b5 == F(manifest["certified_radius"])
    assert F(1, 30000) < a/b5 < F(1, 25000)
    # One original-sign corruption must change the exact signed coefficient.
    corrupt = entries.copy()
    weight, masks = corrupt[0]
    corrupt[0] = (-weight, masks)
    damaged_a, _ = replay(corrupt)
    assert damaged_a != a
    # h_5(r) <= (sum r)^5 is a coefficient inequality, not a sampled claim.
    r = [F(1, 256), F(2, 257), F(0), F(1, 260)]
    coefficients = [F(1)] + [F()] * 5
    for x in r:
        coefficients = [sum(coefficients[k-j]*x**j for j in range(k+1))
                        for k in range(6)]
    assert 0 < coefficients[5] < sum(r)**5
    print("[PASS] K233 independent raw fourth/fifth replay and hostile sign")


if __name__ == "__main__":
    main()
