#!/usr/bin/env python3
"""Independent raw K185 replay of K227 pair support and anchored cells."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
MANIFEST = ROOT / "lab/process/k227-order-six-two-exception-support.json"
K224 = ROOT / "lab/process/k224-order-six-second-shell-cost-stress.json"
K225 = ROOT / "lab/process/k225-order-six-diagonal-cancellation.json"
K226 = ROOT / "lab/process/k226-order-six-global-anchor-obstruction.json"


def raw():
    source = json.loads(SOURCE.read_text())
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    for entry in source["complete_face_hypergraph"]["entries"]:
        multiplier = entry["coefficient_product"] * (1 if entry["left"] == entry["right"] else 2)
        for term in entry["terms"]:
            masks = [int(s, 16) for s in catalog[term["allocation_id"]]["support_masks_hex"].split(",")]
            yield multiplier * term["leibniz_sign"], masks


def rational_point(rows, c):
    result = F(0)
    for w, masks in rows:
        loads = [256 + sum(c[h] for h in range(8) if (masks[h] >> i) & 1) for i in range(14)]
        product = 1
        for a in loads:
            product *= a
        result += F(w, product)
    return result


def grouped(rows, j, k):
    groups = defaultdict(int)
    for w, masks in rows:
        factors = []
        for i in range(14):
            factors.append((sum((masks[h] >> i) & 1 for h in range(2, 8) if h not in (j, k)),
                            *((masks[h] >> i) & 1 for h in (0, 1, j, k))))
        groups[tuple(sorted(factors))] += w
    return groups


def cosh(x):
    return (x + 1/x)/2


def sinh(x):
    return (x - 1/x)/2


def raw_hessian(rows, c, j, k):
    total = F(0)
    for w, masks in rows:
        loads = [256 + sum(c[h] for h in range(8) if (masks[h] >> i) & 1)
                 for i in range(14)]
        product = 1
        for a in loads:
            product *= a
        # Ordered factor pairs include the same factor twice; no shared-load loss.
        second = sum((1 + (i == z)) * F(1, loads[i] * loads[z])
                     for i in range(14) if (masks[j] >> i) & 1
                     for z in range(14) if (masks[k] >> z) & 1)
        total += abs(w) * second / product
    return total


def cell(rows, high, b):
    low_exp = [F(4) if h in high else F(1) for h in range(8)]
    up_exp = [F(5) if h in high else F(4) for h in range(8)]
    low, up = [cosh(a) for a in low_exp], [cosh(a) for a in up_exp]
    measure = F(1)
    for a, z in zip(low_exp, up_exp):
        measure *= sinh(z) - sinh(a)
    bound = F(0)
    for j in range(2, 8):
        for k in range(j + 1, 8):
            c = [low[0], low[1]] + [b] * 6
            for h in (*range(2, j), j, k):
                c[h] = min(b, low[h])
            bound += (max(abs(low[j]-b), abs(up[j]-b)) *
                      max(abs(low[k]-b), abs(up[k]-b)) *
                      raw_hessian(rows, c, j, k))
    return (F(2**8 * 256**6, 120) * measure * bound) / F(31, 10)**8


def main():
    manifest = json.loads(MANIFEST.read_text())
    for name, path in (("k185", SOURCE), ("k224", K224), ("k225", K225), ("k226", K226)):
        assert sha256(path.read_bytes()).hexdigest() == manifest["input_sha256"][name]
    rows = list(raw())
    assert len(rows) == 1864
    zeros = []
    for record in manifest["pairs"]:
        j, k = record["pair"]
        groups = grouped(rows, j, k)
        assert len(groups) == record["factor_multisets"]
        assert sum(bool(v) for v in groups.values()) == record["nonzero_coefficient_groups"]
        c = [F(5, 4), F(17, 8)] + [F(1)] * 6
        c[j], c[k] = F(5, 4), F(17, 8)
        witness = rational_point(rows, c)
        assert sha256(str(witness).encode()).hexdigest() == record["witness_sha256"]
        assert (witness > 0) - (witness < 0) == record["witness_sign"]
        if not any(groups.values()):
            zeros.append([j, k])
            damaged = [(w, bits) for w, bits in rows]
            damaged[0] = (-damaged[0][0], damaged[0][1])
            assert any(grouped(damaged, j, k).values())
    assert zeros == manifest["identically_zero_pair_slices"] == [[2, 3], [6, 7]]
    headroom = F(json.loads(K224.read_text())["combined_cube_budget_headroom"])
    for record in manifest["mixed_bands"]:
        high = tuple(record["high_indices"])
        local, global_ = cell(rows, high, F(17, 8)), cell(rows, high, F(1))
        assert local == F(record["local_upper_using_pi_gt_31_over_10"])
        assert global_ == F(record["global_upper_same_cell"])
        assert local / headroom == F(record["local_over_k224_headroom"])
        assert local < global_
    # A changed original denominator mask breaks an exact witness.
    point = (F(5,4),F(17,8),F(5,4),F(1),F(17,8),F(1),F(1),F(1))
    altered = [(w, list(bits)) for w, bits in rows]
    altered[0][1][2] ^= 1
    assert rational_point(altered, point) != rational_point(rows, point)
    print("[PASS] independent K227 raw grouping, rational witnesses, anchored cells and hostile signs")


if __name__ == "__main__":
    main()
