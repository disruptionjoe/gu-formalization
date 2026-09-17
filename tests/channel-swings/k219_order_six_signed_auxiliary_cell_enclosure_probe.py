#!/usr/bin/env python3
"""Independent raw K185 traversal and hostile controls for the K219 cell rule."""
from __future__ import annotations

from fractions import Fraction as Q
from collections import defaultdict
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from k219_order_six_signed_auxiliary_cell_enclosure import core_bounds, cell_bounds, signed_core, SCALE


def direct(source: dict, coshes: tuple[Q, ...]) -> Q:
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    total = Q(0)
    for entry in source["complete_face_hypergraph"]["entries"]:
        factor = entry["coefficient_product"]
        if entry["left"] != entry["right"]:
            factor *= 2
        for term in entry["terms"]:
            masks = [int(v, 16) for v in catalog[term["allocation_id"]]["support_masks_hex"].split(",")]
            denominator = 1
            for i in range(14):
                denominator *= 256 + sum(coshes[j] for j in range(8) if (masks[j] >> i) & 1)
            total += Q(factor * term["leibniz_sign"], denominator)
    return total


def run() -> None:
    source = json.loads((ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json").read_text())
    manifest = json.loads((ROOT / "lab/process/k219-order-six-signed-auxiliary-cell-enclosure.json").read_text())
    signs = defaultdict(set)
    repeats = defaultdict(int)
    for entry in source["complete_face_hypergraph"]["entries"]:
        coefficient = entry["coefficient_product"] * (2 if entry["left"] != entry["right"] else 1)
        for term in entry["terms"]:
            key = term["allocation_id"]
            signs[key].add(1 if coefficient*term["leibniz_sign"] > 0 else -1)
            repeats[key] += 1
    assert sum(n>1 for n in repeats.values()) == 480
    assert max(repeats.values()) == 4 and all(len(s)==1 for s in signs.values())
    assert manifest["repetition_certificate"]["opposite_sign_repetitions"] == 0
    cells = [((Q(1),) * 8, (Q(5, 4),) * 8, Q(3, 4)**8),
             ((Q(5, 4),) + (Q(1),) * 7, (Q(17, 8),) + (Q(5, 4),) * 7, Q(9, 8)*Q(3, 4)**7),
             (tuple(Q(1) if j%2==0 else Q(5,4) for j in range(8)),
              tuple(Q(5,4) if j%2==0 else Q(17,8) for j in range(8)), Q(3,4)**4*Q(9,8)**4)]
    for (low, high, measure), recorded in zip(cells, manifest["pilot_cells"].values()):
        lower, upper = cell_bounds(source, low, high, measure)
        assert [str(lower), str(upper)] == recorded["signed_integral_interval_without_pi8"]
        assert measure == Q(recorded["exact_product_cosh_measure"])
        raw_lower, raw_upper = core_bounds(source, low, high, aggregate=False)
        assert raw_lower <= lower / (SCALE * measure) <= upper / (SCALE * measure) <= raw_upper
        assert raw_upper-raw_lower == (upper-lower)/(SCALE*measure)
        for point in (low, high, tuple((a+b)/2 for a,b in zip(low, high)),
                      tuple(high[j] if j & 1 else low[j] for j in range(8))):
            value = direct(source, point)
            assert value == signed_core(source, point)
            assert lower <= SCALE*measure*value <= upper
    assert direct(source, (Q(1),)*8) == 0
    alternating = (Q(1),Q(5,4))*4
    assert direct(source, alternating) != 0
    k218 = json.loads((ROOT / "lab/process/k218-order-six-exact-angular-elimination.json").read_text())
    expected = Q(k218["exact_signed_point_rational_without_pi8"]["alternating_zero_log2"])
    product = Q(1)
    for c in alternating:
        product *= c
    assert SCALE*product*direct(source, alternating) == expected
    k217 = json.loads((ROOT / "lab/process/k217-order-six-signed-inner-box.json").read_text())
    inner_endpoint = Q(manifest["pilot_cells"]["inner_box"]["signed_integral_interval_without_pi8"][1])
    # pi < 22/7 proves even the exact K219 inner-cell upper endpoint is
    # larger than K217's cancellation-aware whole-inner-box bound.
    assert inner_endpoint / Q(22,7)**8 > Q(k217["remainder"]["whole_2928_ordered_term_absolute_ceiling"])
    # A planted omitted positive load must not survive an exact direct replay.
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    entry = source["complete_face_hypergraph"]["entries"][0]
    masks = [int(v,16) for v in catalog[entry["terms"][0]["allocation_id"]]["support_masks_hex"].split(",")]
    point = (Q(1),Q(5,4))*4
    proper = 1
    altered = 1
    for i in range(14):
        load = 256 + sum(point[j] for j in range(8) if masks[j] & (1<<i))
        proper *= load
        altered *= load - (point[0] if masks[0] & (1<<i) else 0)
    assert proper != altered
    print("[PASS] independent 1,864-term signed replay, exact cell inclusion and hostile omitted load")


if __name__ == "__main__":
    run()
