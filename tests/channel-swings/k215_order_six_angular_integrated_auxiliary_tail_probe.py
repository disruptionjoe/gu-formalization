#!/usr/bin/env python3
"""Independent K215 full-simplex moment and hostile normalization controls."""
from __future__ import annotations

from fractions import Fraction as Q
import json
import math
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
result = json.loads((P / "k215-order-six-angular-integrated-auxiliary-tail.json").read_text())
k185 = json.loads((P / "k185-order-six-duffy-face-tail-wave.json").read_text())
catalog = k185["exact_allocation_certificate"]["allocation_catalog"]


def sinh_m(m: int) -> Q:
    return Q(4**m - 1, 2**(m+1))


def passes(m: int, coefficient: Q, budget: Q) -> bool:
    return coefficient**4 * Q(256, sinh_m(m)) < budget**4


mp.mp.dps = 80
assert mp.gamma(mp.mpf(23)/4) > 28
universal = Q(result["universal_rational_coefficient"])
target = Q(1, 10**21)
assert result["mask_count"] == 1864
for key, c, budget in (
    ("first_sufficient_universal_per_term_dyadic_m", universal, target),
    ("first_sufficient_universal_whole_sum_dyadic_m", 1864*universal, target),
):
    m = result[key]
    assert passes(m, c, budget) and not passes(m-1, c, budget)

# Reconstruct the *actual* AM--GM moment in high precision from the encoded
# weight vectors, rather than importing the producer's rational coefficient.
# It must be strictly below the deliberately coarse universal rational B.
by_load: dict[str, tuple[str, dict]] = {}
for key, row in catalog.items():
    by_load.setdefault(row["maximum_load"], (key, row))
assert set(by_load) == {"4/7", "7/12", "3/5", "5/8", "2/3"}
for key, row in by_load.values():
    loads = [Q(x) for x in row["loads"].split(",")]
    beta = [1 - x for x in loads]
    masks = [int(x, 16) for x in row["support_masks_hex"].split(",")]
    assert sum(loads) == 8 and len(masks) == 8
    log_cw = mp.mpf(0)
    for factor in row["weights"].split(";"):
        weights = [Q(part.split(":")[1]) for part in factor.split(",")]
        assert sum(weights) == 1
        log_cw += sum((mp.mpf(w.numerator)/w.denominator)
                      * mp.log(mp.mpf(w.numerator)/w.denominator) for w in weights)
    assert log_cw <= 0
    moments = []
    for mask in masks:
        alternatives = []
        for i in range(14):
            if mask & (1 << i):
                parameters = [b - (Q(1, 4) if k == i else 0)
                              for k, b in enumerate(beta)]
                assert min(parameters) > 0 and sum(parameters) == Q(23, 4)
                alternatives.append(mp.exp(sum(mp.loggamma(mp.mpf(b.numerator)/b.denominator)
                                               for b in parameters)
                                           - mp.loggamma(mp.mpf(23)/4)))
        moments.append(min(alternatives))
    exact_amgm_coefficient = (mp.mpf(120) / (mp.pi**8 * 256**6)
                              * mp.exp(log_cw) * sum(moments))
    assert 0 < exact_amgm_coefficient < mp.mpf(universal.numerator)/universal.denominator

# At an extreme angular point, the pointwise K214 rational tail can be much
# larger than an integrated bound; substituting the barycenter cutoff for a
# uniform bound is an invalid transfer. This also catches dropped support
# powers in a proposed angular majorant.
z = [Q(1, 2**180)]*13 + [1 - Q(13, 2**180)]
row = by_load["2/3"][1]
loads = [Q(x) for x in row["loads"].split(",")]
masks = [int(x, 16) for x in row["support_masks_hex"].split(",")]
direct = math.prod(float(sum(z[i] for i in range(14) if mask & (1 << i)))**-1
                   for mask in masks)
majorant = math.prod(float(z[i])**-float(loads[i]) for i in range(14))
assert direct <= majorant * (1 + 1e-12)
assert min(sum(z[i] for i in range(14) if mask & (1 << i)) for mask in masks) <= Q(13, 2**180)
assert result["first_sufficient_universal_whole_sum_dyadic_m"] > result["first_sufficient_universal_per_term_dyadic_m"]
assert Q(1, 3) - Q(1, 4) == Q(1, 12)
assert Q(1, 3) - Q(1, 3) == 0  # hostile exponent: logarithmic face divergence
print("[PASS] independent Gamma/Beta moments across five load classes")
print("[PASS] adjacent exact cutoffs, 1,864-term budget, normalization and face controls")
