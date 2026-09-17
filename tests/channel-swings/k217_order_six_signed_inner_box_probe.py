#!/usr/bin/env python3
"""Independent K217 normalization, moment and hostile-sign controls."""
from __future__ import annotations

from fractions import Fraction as Q
import importlib.util
import json
from math import comb, factorial
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
K185 = json.loads((P / "k185-order-six-duffy-face-tail-wave.json").read_text())
K202 = json.loads((P / "k202-order-six-common-weighted-core.json").read_text())
K216 = json.loads((P / "k216-order-six-analytic-angular-prefix.json").read_text())
K217 = json.loads((P / "k217-order-six-signed-inner-box.json").read_text())
spec = importlib.util.spec_from_file_location("k217", ROOT / "tests/channel-swings/k217_order_six_signed_inner_box.py")
assert spec and spec.loader
producer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(producer)


def independent_uniform_moment(masks: tuple[int, ...], js: tuple[int, ...]) -> Q:
    """Coefficient of a product of linear forms under Dirichlet(1)^14."""
    n = len(js)
    if n == 0:
        return Q(1)
    # E[z_i z_k z_l] = product of factorials of repeated indices/(14)_n.
    answer = Q(0)
    from itertools import product
    for indices in product(range(14), repeat=n):
        if any(not masks[j] & (1 << i) for j, i in zip(js, indices)):
            continue
        repeated = 1
        for i in set(indices):
            repeated *= factorial(indices.count(i))
        answer += repeated
    return answer / Q(factorial(13+n), factorial(13))


def pointwise_series(masks: tuple[int, ...], c: tuple[Q, ...], n: int) -> Q:
    """Independent complete homogeneous polynomial in fourteen affine loads."""
    loads = [sum(c[j] for j, mask in enumerate(masks) if mask & (1 << i))
             for i in range(14)]
    coeff = [Q(1)] + [Q(0)] * n
    for load in loads:
        for k in range(1, n+1):
            coeff[k] += load * coeff[k-1]
    return coeff[n] * Q(factorial(n) * factorial(13), factorial(13+n))


def main() -> None:
    assert K202["rule"]["angular_weight"] == "product_i z_i^(-2/3)"
    assert "beta_i=1, beta_0=14" in K216["identity"]
    assert "prior K216 Dirichlet(5/3)" in K216["historical_correction"]
    assert K185["radial_duffy_certificate"]["angular_weight"].find("beta_i-1") >= 0
    assert K217["ordered_term_count_with_off_diagonal_twice"] == 2928
    assert Q(K217["remainder"]["whole_2928_ordered_term_absolute_ceiling"]) < Q(1, 10**21)
    assert K217["signed_inner_box_polynomial_in_log2"] == ["0"] * 4
    catalog = K185["exact_allocation_certificate"]["allocation_catalog"]
    entries = K185["complete_face_hypergraph"]["entries"]
    first = tuple(int(x, 16) for x in catalog[entries[0]["terms"][0]["allocation_id"]]
                  ["support_masks_hex"].split(","))
    last = tuple(int(x, 16) for x in catalog[entries[-1]["terms"][-1]["allocation_id"]]
                 ["support_masks_hex"].split(","))
    for masks in (first, last):
        for js in ((0,), (1, 2), (0, 0), (2, 3, 7), (4, 4, 4)):
            assert independent_uniform_moment(masks, js) == producer.angular_moment(masks, js)

    # An ordinary one-dimensional integral independently checks J_0..J_3.
    mp.mp.dps = 60
    h = mp.log(2)
    for power, coeff in enumerate(producer.J):
        direct = mp.quad(lambda t: mp.cosh(t)**(power+1), [0, h])
        formula = mp.mpf(0)
        for i, x in enumerate(coeff):
            formula += mp.mpf(x.numerator)/x.denominator * h**i
        assert abs(direct-formula) < mp.mpf("1e-55")

    # Independent pointwise coefficient generation at two distinct t profiles.
    nonzero_higher = 0
    for c in ((Q(i+1) for i in range(8)),
              (Q(2*i*i+3) for i in range(8))):
        profile = tuple(c)
        for n in range(4):
            total = Q(0)
            for e in entries:
                factor = e["coefficient_product"] * (2 if e["left"] != e["right"] else 1)
                for term in e["terms"]:
                    masks = tuple(int(x, 16) for x in catalog[term["allocation_id"]]
                                  ["support_masks_hex"].split(","))
                    total += factor * term["leibniz_sign"] * pointwise_series(masks, profile, n)
            if n <= 1:
                assert total == 0
            elif total:
                nonzero_higher += 1
    assert nonzero_higher > 0  # integrated cancellation is not pointwise
    # A planted sign flip must violate the exact order-zero determinant control.
    hostile = [dict(t) for t in entries[0]["terms"]]
    hostile[0]["leibniz_sign"] *= -1
    try:
        producer.pointwise_cancellation(hostile, catalog)
    except AssertionError:
        pass
    else:
        raise AssertionError("planted sign mutation escaped")
    print("[PASS] true-measure moments, ordinary cosh integrals and independent signed point controls")
    print("[PASS] corrected K216 normalization, historical mismatch and hostile sign mutation")


if __name__ == "__main__":
    main()
