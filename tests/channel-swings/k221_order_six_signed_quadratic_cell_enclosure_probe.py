#!/usr/bin/env python3
"""Independent raw K185 product-polynomial second/third jet controls for K221."""
from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from k221_order_six_signed_quadratic_cell_enclosure import (
    K185, K217, K218, K219, K220, OUT, SCALE, signed_quadratic_bounds,
)


def raw_terms(source: dict):
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    for entry in source["complete_face_hypergraph"]["entries"]:
        multiplier = entry["coefficient_product"] * (2 if entry["left"] != entry["right"] else 1)
        for term in entry["terms"]:
            masks = tuple(int(v, 16) for v in
                          catalog[term["allocation_id"]]["support_masks_hex"].split(","))
            yield multiplier*term["leibniz_sign"], masks


def polynomial_jet(masks: tuple[int, ...], c: tuple[Q, ...]):
    """Coefficients of the fourteen-factor denominator through degree two."""
    p0, p1 = Q(1), [Q(0)]*8
    p2 = [[Q(0)]*8 for _ in range(8)]  # actual mixed derivative, including diagonal
    for i in range(14):
        a = 256 + sum((c[j] for j in range(8) if masks[j] & (1 << i)), Q(0))
        bits = [int(bool(masks[j] & (1 << i))) for j in range(8)]
        old = p1[:]
        for j in range(8):
            for k in range(j, 8):
                p2[j][k] = p2[j][k]*a + old[j]*bits[k] + old[k]*bits[j]
        for j in range(8):
            p1[j] = old[j]*a + p0*bits[j]
        p0 *= a
    return p0, p1, p2


def raw_hessian(source: dict, c: tuple[Q, ...]):
    h = [[Q(0)]*8 for _ in range(8)]
    count = 0
    for w, masks in raw_terms(source):
        p0, p1, p2 = polynomial_jet(masks, c)
        for j in range(8):
            for k in range(j, 8):
                h[j][k] += w*(2*p1[j]*p1[k]/p0**3 - p2[j][k]/p0**2)
        count += 1
    assert count == 1864
    for j in range(8):
        for k in range(j):
            h[j][k] = h[k][j]
    return tuple(tuple(row) for row in h)


def raw_point(source: dict, c: tuple[Q, ...]):
    total = Q(0)
    for w, masks in raw_terms(source):
        p0 = Q(1)
        for i in range(14):
            p0 *= 256 + sum((c[j] for j in range(8) if masks[j] & (1 << i)), Q(0))
        total += w/p0
    return total


def reciprocal_third_polynomial(masks, c, direction):
    # Independent univariate product coefficients; no logarithmic derivative.
    p = [Q(1), Q(0), Q(0), Q(0)]
    for i in range(14):
        a = 256 + sum((c[j] for j in range(8) if masks[j] & (1 << i)), Q(0))
        d = sum((direction[j] for j in range(8) if masks[j] & (1 << i)), Q(0))
        p = [p[0]*a, p[1]*a+p[0]*d,
             p[2]*a+p[1]*d, p[3]*a+p[2]*d]
    return 6*(-p[1]**3/p[0]**4 + 2*p[1]*p[2]/p[0]**3 - p[3]/p[0]**2)


def raw_cubic_majorant(source, low, radius):
    total = Q(0)
    for w, masks in raw_terms(source):
        q = Q(1)
        u = []
        for i in range(14):
            a = 256+sum((low[j] for j in range(8) if masks[j] & (1<<i)), Q(0))
            d = sum((radius[j] for j in range(8) if masks[j] & (1<<i)), Q(0))
            q /= a
            u.append(d/a)
        s1 = sum(u,Q(0))
        total += abs(w)*q*(s1**3+3*s1*sum((v*v for v in u),Q(0))
                           +2*sum((v**3 for v in u),Q(0)))/6
    return total


def run():
    paths = {"k185": K185, "k217": K217, "k218": K218,
             "k219": K219, "k220": K220}
    manifest = json.loads(OUT.read_text())
    assert all(manifest["input_sha256"][key] == hashlib.sha256(path.read_bytes()).hexdigest()
               for key, path in paths.items())
    source = json.loads(K185.read_text())
    ratios = []
    for name, recorded in manifest["pilot_cells"].items():
        low = tuple(map(Q, recorded["cosh_lower"]))
        high = tuple(map(Q, recorded["cosh_upper"]))
        measure = Q(recorded["exact_product_cosh_measure"])
        bound = signed_quadratic_bounds(source, low, high)
        raw = raw_hessian(source, bound["center"])
        assert raw == bound["signed_hessian"]
        assert [[str(x) for x in row] for row in raw] == recorded["signed_hessian"]
        assert raw_cubic_majorant(source, low, bound["radius"]) == bound["cubic_remainder"]
        for key, field in (("quadratic_core", "quadratic_integral_interval_without_pi8"),
                           ("intersection_core", "intersection_integral_interval_without_pi8")):
            assert [str(SCALE*measure*x) for x in bound[key]] == recorded[field]
        for c in (low, high, bound["center"],
                  tuple(high[j] if j%2 else low[j] for j in range(8)),
                  tuple(low[j] if j%2 else high[j] for j in range(8))):
            point = raw_point(source, c)
            assert bound["quadratic_core"][0] <= point <= bound["quadratic_core"][1]
            assert bound["intersection_core"][0] <= point <= bound["intersection_core"][1]
        old = bound["k220_core"][1]-bound["k220_core"][0]
        ratio = (bound["intersection_core"][1]-bound["intersection_core"][0])/old
        assert ratio == Q(recorded["intersection_width_to_k220_width"]) < 1
        ratios.append(float(ratio))
    # Directional third derivative of one raw allocation checks the 2*s3
    # shared-load coefficient; the lower corner dominates a midpoint sample.
    w, masks = next((w, masks) for w, masks in raw_terms(source) if masks[0])
    low = (Q(1),)*8
    c = (Q(9,8),)*8
    direction = (Q(1,8),)*8
    direct = reciprocal_third_polynomial(masks, c, direction)
    loads = [256+sum((c[j] for j in range(8) if masks[j] & (1<<i)), Q(0))
             for i in range(14)]
    q = Q(1)
    for a in loads:
        q /= a
    u = [sum((direction[j] for j in range(8) if masks[j] & (1<<i)), Q(0))/loads[i]
         for i in range(14)]
    s1, s2, s3 = sum(u,Q(0)), sum((v*v for v in u),Q(0)), sum((v**3 for v in u),Q(0))
    assert s3 > 0 and direct == -q*(s1**3+3*s1*s2+2*s3)
    assert direct != -q*(s1**3+3*s1*s2)  # hostile omitted triple shared load
    assert direct != q*(s1**3+3*s1*s2+2*s3)  # hostile sign
    inner = manifest["pilot_cells"]["k219_inner"]
    exact_upper = Q(inner["intersection_integral_interval_without_pi8"][1])/3**8
    assert exact_upper == Q(manifest["full_inner_comparison"]["absolute_upper_rational_using_pi_gt_3"])
    assert exact_upper < Q(manifest["full_inner_comparison"]["k220_absolute_upper_rational"])
    print("[PASS] independent 1,864-term polynomial Hessian, exact cells and cubic shared-load controls")
    print("width ratios:", ", ".join(f"{x:.8g}" for x in ratios))


if __name__ == "__main__":
    run()
