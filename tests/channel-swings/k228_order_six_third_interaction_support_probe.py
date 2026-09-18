#!/usr/bin/env python3
"""Independent raw K185 traversal for all K228 Boolean third differences."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
K227 = ROOT / "lab/process/k227-order-six-two-exception-support.json"
MANIFEST = ROOT / "lab/process/k228-order-six-third-interaction-support.json"


def original_rows():
    source = json.loads(SOURCE.read_text())
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    for entry in source["complete_face_hypergraph"]["entries"]:
        signed = entry["coefficient_product"] * (1 if entry["left"] == entry["right"] else 2)
        for term in entry["terms"]:
            yield signed * term["leibniz_sign"], [int(x, 16) for x in
                catalog[term["allocation_id"]]["support_masks_hex"].split(",")]


def original_value(rows, c):
    total = F(0)
    for weight, masks in rows:
        product = 1
        for slot in range(14):
            product *= 256 + sum(c[h] for h in range(8) if masks[h] >> slot & 1)
        total += F(weight, product)
    return total


def original_grouping(rows, triple):
    groups = defaultdict(int)
    for weight, masks in rows:
        factors = []
        for slot in range(14):
            factors.append((sum(masks[h] >> slot & 1 for h in range(2, 8) if h not in triple),
                            *(masks[h] >> slot & 1 for h in (0, 1) + triple)))
        groups[tuple(sorted(factors))] += weight
    return len(groups), sum(v != 0 for v in groups.values())


def third_difference(rows, triple):
    terms = []
    for mask in range(8):
        c = [F(5, 4), F(17, 8)] + [F(1)] * 6
        for i, coordinate in enumerate(triple):
            if mask >> i & 1:
                c[coordinate] = (F(5, 4), F(17, 8), F(3, 2))[i]
        terms.append(original_value(rows, c))
    return terms[7] - terms[6] - terms[5] - terms[3] + terms[4] + terms[2] + terms[1] - terms[0]


def main():
    expected = json.loads(MANIFEST.read_text())
    assert expected["input_sha256"] == {"k185": sha256(SOURCE.read_bytes()).hexdigest(),
                                        "k227": sha256(K227.read_bytes()).hexdigest()}
    rows = list(original_rows())
    assert len(rows) == 1864
    assert [r["triple"] for r in expected["triples"]] == [list(t) for t in combinations(range(2, 8), 3)]
    for recorded in expected["triples"]:
        triple = tuple(recorded["triple"])
        assert original_grouping(rows, triple) == (recorded["factor_multisets"],
                                                  recorded["nonzero_coefficient_groups"])
        delta = third_difference(rows, triple)
        assert delta and (delta > 0) - (delta < 0) == recorded["third_difference_sign"]
        assert sha256(str(delta).encode()).hexdigest() == recorded["third_difference_sha256"]
    # A one-term corruption changes a raw triple witness, so the manifest is not a vacuous replay.
    damaged = [(w, list(masks)) for w, masks in rows]
    damaged[0] = (-damaged[0][0], damaged[0][1])
    assert third_difference(damaged, (2, 3, 4)) != third_difference(rows, (2, 3, 4))
    # The two K227 zero pair restrictions hold at these corners, yet triple interactions survive.
    for j, k in ((2, 3), (6, 7)):
        c = [F(5, 4), F(17, 8)] + [F(1)] * 6
        c[j], c[k] = F(5, 4), F(17, 8)
        assert original_value(rows, c) == 0
    print("[PASS] independent K228 original rows, twenty triple witnesses, hostile and zero-pair controls")


if __name__ == "__main__":
    main()
