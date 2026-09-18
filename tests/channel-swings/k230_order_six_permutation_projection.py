#!/usr/bin/env python3
"""K230: exact S6 projection of the original K185 signed denominator core."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import itertools
import json

from k225_order_six_diagonal_cancellation import K185, ROOT, core, terms

OUT = ROOT / "lab/process/k230-order-six-permutation-projection.json"
PERMS = tuple(itertools.permutations(range(6)))


def row_masks(masks):
    return tuple(sum(((mask >> i) & 1) << j for j, mask in enumerate(masks))
                 for i in range(14))


def transform(rows, perm):
    return tuple(sorted((row & 3) | sum(((row >> (j + 2)) & 1) << (perm[j] + 2)
                                        for j in range(6)) for row in rows))


def orbit_key(rows):
    return min(transform(rows, p) for p in PERMS)


def projected_value(items, c):
    return sum((core(items, tuple(c[:2]) + tuple(c[j + 2] for j in p))
                for p in PERMS), Q()) / len(PERMS)


def generate():
    source = json.loads(K185.read_text())
    items = list(terms(source))
    assert len(items) == 1864
    groups = defaultdict(int)
    for weight, masks in items:
        groups[orbit_key(row_masks(masks))] += weight
    retained = {k: v for k, v in groups.items() if v}
    assert retained
    orbit_sizes = [len({transform(key, p) for p in PERMS}) for key in groups]
    # The six exceptional coordinates have the same integration measure and
    # the cube/shell condition is invariant under their permutation.
    c = (Q(5, 4), Q(17, 8), Q(1), Q(5, 4), Q(3, 2), Q(17, 8), Q(2), Q(9, 4))
    original = core(items, c)
    projected = projected_value(items, c)
    assert original and projected and original != projected
    compact = ";".join(
        ",".join(map(str, key)) + ":" + str(value)
        for key, value in sorted(groups.items()))
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": hashlib.sha256(K185.read_bytes()).hexdigest(),
        "object": "Original signed 1,864-term K185/K218 rational-cosh core, without positive measure or pi^-8",
        "group": "S6 permutes coordinates c2..c7, fixing c0,c1 and each of fourteen unordered affine denominator factors",
        "projection_identity": "For every S6-invariant measurable domain D and S6-invariant positive product-cosh density W, integral_D W H equals integral_D W (1/720) sum_p H(c0,c1,c_(2+p0),...,c_(2+p5)), whenever either integral is defined. Change of variables proves this exactly; it is not a pointwise identity H=projection(H).",
        "orbit_rule": "Encode each factor as an eight-bit incidence mask of its affine load 256+sum_j bit_j*c_j. Sort fourteen factors after each of 720 column permutations and choose the lexicographically smallest tuple. All source terms in one orbit project to the same orbit-average rational function, with coefficient equal to their signed integer weight sum. A zero sum cancels that complete orbit as a rational-function identity.",
        "raw_signed_terms": len(items), "orbit_count": len(groups),
        "zero_coefficient_orbits": len(groups) - len(retained),
        "retained_orbits": len(retained),
        "expanded_distinct_denominator_functions": sum(orbit_sizes),
        "orbit_size_histogram": {str(size): orbit_sizes.count(size) for size in sorted(set(orbit_sizes))},
        "orbit_coefficient_manifest_sha256": hashlib.sha256(compact.encode()).hexdigest(),
        "rational_witness": {
            "coordinates": list(map(str, c)),
            "original_sign": (original > 0) - (original < 0),
            "projected_sign": (projected > 0) - (projected < 0),
            "original_sha256": hashlib.sha256(str(original).encode()).hexdigest(),
            "projected_sha256": hashlib.sha256(str(projected).encode()).hexdigest(),
            "projected_over_original": str(projected / original),
        },
        "claim_ceiling": "Exact S6 projection and coefficientwise orbit cancellation on invariant domains; nonzero finite rational projected witness. No signed whole-shell enclosure, integral value, necessary node cost, K215 or separate boundary composition, source/physics/ledger/canon effect. The witness ratio is local, not a uniform reduction factor."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K230 exact S6 orbit projection", result["orbit_count"], result["retained_orbits"])
    print("witness ratio", float(Q(result["rational_witness"]["projected_over_original"])))
