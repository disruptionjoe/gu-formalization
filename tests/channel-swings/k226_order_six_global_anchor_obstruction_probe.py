#!/usr/bin/env python3
"""Independent original-allocation replay of K226's fifteen lower witnesses."""
from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
K224 = ROOT / "lab/process/k224-order-six-second-shell-cost-stress.json"
K225 = ROOT / "lab/process/k225-order-six-diagonal-cancellation.json"
DOC = ROOT / "lab/process/k226-order-six-global-anchor-obstruction.json"


def raw_rows(source):
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    for entry in source["complete_face_hypergraph"]["entries"]:
        coefficient = entry["coefficient_product"]
        if entry["left"] != entry["right"]:
            coefficient *= 2
        for term in entry["terms"]:
            masks = [int(h, 16) for h in catalog[term["allocation_id"]]["support_masks_hex"].split(",")]
            yield abs(coefficient * term["leibniz_sign"]), masks


def raw_hessian(rows, lower, j, k):
    total = Q(0)
    first_nonzero = None
    for weight, masks in rows:
        loads = [256+sum(lower[h] for h in range(8)
                         if masks[h] & (1 << i)) for i in range(14)]
        product = 1
        for a in loads:
            product *= a
        # Two ordered factor choices; i==h contributes twice.
        num = sum(Q(1 + (i == h), loads[i]*loads[h])
                  for i in range(14) if masks[j] & (1 << i)
                  for h in range(14) if masks[k] & (1 << h))
        contribution = weight*num/product
        total += contribution
        if first_nonzero is None and contribution:
            first_nonzero = contribution
    return total, first_nonzero


def check():
    doc = json.loads(DOC.read_text())
    assert doc["input_sha256"] == {p.stem.split("-")[0]: hashlib.sha256(p.read_bytes()).hexdigest()
                                    for p in (K185, K224, K225)}
    rows = list(raw_rows(json.loads(K185.read_text())))
    assert len(rows) == 1864
    c4, c5 = Q(17, 8), Q(13, 5)
    s4, s5 = Q(15, 8), Q(12, 5)
    assert (c4, c5, s4, s5) == tuple((r+1/r)/2 if i < 2 else (r-1/r)/2
                                    for i, r in enumerate((Q(4), Q(5), Q(4), Q(5))))
    prefactor = Q(2**8 * 256**6, 120)
    volume = s4**6 * (s5-s4)**2
    common = prefactor * (c4-1)**2 * volume * (Q(7, 22))**8
    headroom = Q(json.loads(K224.read_text())["combined_cube_budget_headroom"])
    assert headroom == Q(doc["remaining_budget_after_k224"])
    assert len(doc["pairs"]) == 15
    global_sum = local_sum = Q(0)
    for row in doc["pairs"]:
        j, k = row["pair"]
        total, first_nonzero = raw_hessian(rows, (c4,c4)+(Q(1),)*6, j, k)
        local, _ = raw_hessian(rows, (c4,)*8, j, k)
        global_sum += total
        local_sum += local
        lower = common*total
        assert total == Q(row["hessian_majorant_at_lower"])
        assert lower == Q(row["integral_majorant_strict_lower_rational"])
        assert lower/headroom == Q(row["lower_over_remaining_budget"]) > 1
        # A duplicated original weighted term, or missing outer weight, cannot pass.
        assert first_nonzero is not None
        assert total+first_nonzero != Q(row["hessian_majorant_at_lower"])
        assert prefactor != 1 and volume != 1 and lower/prefactor != Q(row["integral_majorant_strict_lower_rational"])
    assert min((Q(r["lower_over_remaining_budget"]), r["pair"])
               for r in doc["pairs"])[1] == doc["minimum_ratio_pair"]
    assert min(Q(r["lower_over_remaining_budget"]) for r in doc["pairs"]) == Q(doc["minimum_ratio"])
    cube = doc["locally_reanchored_high_cube"]
    cube_volume = (s5-s4)**8
    global_upper = prefactor*cube_volume*(c5-1)**2*global_sum/Q(31,10)**8
    local_upper = prefactor*cube_volume*(c5-c4)**2*local_sum/Q(31,10)**8
    assert cube_volume == Q(cube["weight_integral"])
    assert (global_sum,local_sum) == (Q(cube["global_hessian_sum"]),Q(cube["local_hessian_sum"]))
    assert global_upper == Q(cube["fixed_global_upper_same_cube"])
    assert local_upper == Q(cube["local_upper_using_pi_gt_31_over_10"])
    assert local_upper/headroom == Q(cube["upper_to_headroom"]) < Q(1,400)
    assert global_upper/local_upper == Q(cube["improvement_factor"]) > 1
    # The polynomial identity proving 22/7-pi>0 is coefficientwise.
    q = {6: 1, 5: -4, 4: 5, 2: -4, 0: 4}
    numerator = {8: 1, 7: -4, 6: 6, 5: -4, 4: 1}
    assert all(q.get(n, 0)+q.get(n-2, 0)-(4 if n == 0 else 0) == numerator.get(n, 0)
               for n in range(9))
    print("[PASS] K226 raw 1,864-term pair replay, local-anchor cube, exact weights, pi and hostile loads")


if __name__ == "__main__":
    check()
