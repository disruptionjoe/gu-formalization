#!/usr/bin/env python3
"""Independent raw-entry orbit replay and signed rational K230 controls."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
OUT = ROOT / "lab/process/k230-order-six-permutation-projection.json"
PERMS = tuple(itertools.permutations(range(2, 8)))


def raw_entries():
    source = json.loads(SOURCE.read_text())
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    for entry in source["complete_face_hypergraph"]["entries"]:
        coefficient = entry["coefficient_product"]
        if entry["left"] != entry["right"]:
            coefficient *= 2
        for term in entry["terms"]:
            masks = tuple(int(x, 16) for x in
                          catalog[term["allocation_id"]]["support_masks_hex"].split(","))
            yield coefficient * term["leibniz_sign"], masks


def canonical(masks):
    # Unlike the producer, permute source columns directly before building
    # fourteen bit incidence rows. Denominator factor order remains unordered.
    return min(tuple(sorted(sum(int(bool(masks[j] & (1 << i))) << dest
                                for dest, j in enumerate((0, 1) + p))
                           for i in range(14))) for p in PERMS)


def relabel(key, p):
    return tuple(sorted((row & 3) | sum(((row >> j) & 1) << p[j - 2]
                                        for j in range(2, 8)) for row in key))


def at_point(entries, c):
    result = Q()
    for weight, masks in entries:
        factors = [256 + sum(c[j] for j in range(8) if masks[j] & (1 << i))
                   for i in range(14)]
        product = 1
        for factor in factors:
            product *= factor
        result += Q(weight, product)
    return result


def replay(doc, entries):
    groups = defaultdict(int)
    for weight, masks in entries:
        groups[canonical(masks)] += weight
    compact = ";".join(",".join(map(str, key)) + ":" + str(value)
                       for key, value in sorted(groups.items()))
    assert len(entries) == doc["raw_signed_terms"] == 1864
    assert len(groups) == doc["orbit_count"]
    assert sum(v != 0 for v in groups.values()) == doc["retained_orbits"]
    assert sum(v == 0 for v in groups.values()) == doc["zero_coefficient_orbits"]
    assert hashlib.sha256(compact.encode()).hexdigest() == doc["orbit_coefficient_manifest_sha256"]
    sizes = [len({relabel(key, p) for p in PERMS}) for key in groups]
    assert sum(sizes) == doc["expanded_distinct_denominator_functions"]
    assert {str(n): sizes.count(n) for n in set(sizes)} == doc["orbit_size_histogram"]


def run():
    doc = json.loads(OUT.read_text())
    entries = list(raw_entries())
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == doc["input_sha256"]
    replay(doc, entries)
    c = tuple(map(Q, doc["rational_witness"]["coordinates"]))
    original = at_point(entries, c)
    projected = sum((at_point(entries, c[:2] + tuple(c[j] for j in p))
                     for p in PERMS), Q()) / 720
    assert original and projected
    assert hashlib.sha256(str(original).encode()).hexdigest() == doc["rational_witness"]["original_sha256"]
    assert hashlib.sha256(str(projected).encode()).hexdigest() == doc["rational_witness"]["projected_sha256"]
    assert projected / original == Q(doc["rational_witness"]["projected_over_original"])
    bad = entries.copy()
    weight, masks = bad[0]
    bad[0] = -weight, masks
    try:
        replay(doc, bad)
    except AssertionError:
        pass
    else:
        raise AssertionError("hostile sign mutation escaped")
    print("[PASS] K230 independent raw orbit, rational S6 replay and hostile sign control")


if __name__ == "__main__":
    run()
