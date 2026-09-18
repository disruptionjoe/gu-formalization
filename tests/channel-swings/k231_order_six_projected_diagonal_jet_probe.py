#!/usr/bin/env python3
"""Independent raw K185 replay using Newton power-sum jets, not product series."""
from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
K225 = ROOT / "lab/process/k225-order-six-diagonal-cancellation.json"
K230 = ROOT / "lab/process/k230-order-six-permutation-projection.json"
OUT = ROOT / "lab/process/k231-order-six-projected-diagonal-jet.json"


def raw():
    source = json.loads(SOURCE.read_text())
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    for entry in source["complete_face_hypergraph"]["entries"]:
        weight = entry["coefficient_product"]*(2 if entry["left"] != entry["right"] else 1)
        for term in entry["terms"]:
            bits = [int(x, 16) for x in catalog[term["allocation_id"]]["support_masks_hex"].split(",")]
            yield weight*term["leibniz_sign"], bits


def raw_jet(rows, fixed, size):
    subsets = list(combinations(range(2, 8), size))
    totals = [F(0) for _ in range(5)]
    for weight, bits in rows:
        base = [256+sum(fixed[j] for j in range(8) if bits[j] & (1 << i)) for i in range(14)]
        q0 = F(weight)
        for a in base:
            q0 /= a
        for chosen in subsets:
            ratios = [F(sum((bits[j] >> i) & 1 for j in chosen), base[i]) for i in range(14)]
            powers = [F(0)] + [sum((r**k for r in ratios), F(0)) for k in range(1, 5)]
            complete = [F(1)]
            for k in range(1, 5):
                complete.append(sum((powers[m]*complete[k-m] for m in range(1, k+1)), F(0))/k)
            for k in range(5):
                totals[k] += (-1)**k*q0*complete[k]
    return [t/len(subsets) for t in totals]


def main():
    manifest = json.loads(OUT.read_text())
    for name, path in (("k185", SOURCE), ("k225", K225), ("k230", K230)):
        assert sha256(path.read_bytes()).hexdigest() == manifest["input_sha256"][name]
    rows = list(raw())
    assert len(rows) == 1864
    fixed = tuple(map(F, manifest["exact_jet_point"]))
    jets = {}
    for size in (1, 2, 3):
        values = raw_jet(rows, fixed, size)
        jets[size] = values
        record = manifest["orbit_direction_controls"][str(size)]
        assert values[:4] == [F(v) for v in record["degrees_zero_through_three"]]
        assert (values[4] > 0)-(values[4] < 0) == record["degree_four_sign"]
        assert sha256(str(values[4]).encode()).hexdigest() == record["degree_four_sha256"]
    assert jets[1][4] == 0 and jets[2][4] > 0
    assert jets[3][4] == F(3, 2)*jets[2][4]
    damaged = rows.copy()
    w, bits = damaged[0]
    damaged[0] = -w, bits
    assert raw_jet(damaged, fixed, 2)[0] != 0
    assert json.loads(K230.read_text())["rational_witness"]["projected_sha256"] == manifest["projection_control"]["prior_witness_projected_sha256"]
    print("[PASS] independent K231 raw-entry Newton jets and hostile sign")


if __name__ == "__main__":
    main()
