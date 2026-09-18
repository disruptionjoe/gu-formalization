#!/usr/bin/env python3
"""Independent raw K185 polynomial derivative and hostile K220 controls."""
from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from k220_order_six_signed_taylor_cell_enclosure import signed_taylor_bounds, SCALE


def raw_terms(source: dict):
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    for entry in source["complete_face_hypergraph"]["entries"]:
        multiplier = entry["coefficient_product"] * (2 if entry["left"] != entry["right"] else 1)
        for term in entry["terms"]:
            masks = tuple(int(x, 16) for x in catalog[term["allocation_id"]]["support_masks_hex"].split(","))
            yield multiplier * term["leibniz_sign"], masks


def direct_point_and_gradient(source: dict, c: tuple[Q, ...]) -> tuple[Q, tuple[Q, ...]]:
    value = Q(0)
    gradient = [Q(0)]*8
    count = 0
    for w, masks in raw_terms(source):
        loads = [256 + sum(c[j] for j in range(8) if masks[j] & (1 << i)) for i in range(14)]
        p0 = 1
        p1 = [0]*8
        # Coefficient of h in prod_i(a_i + m_ji h), independent of
        # reciprocal logarithmic differentiation in the producer.
        for i, a in enumerate(loads):
            for j in range(8):
                p1[j] = p1[j]*a + (p0 if masks[j] & (1 << i) else 0)
            p0 *= a
        value += Q(w, p0)
        for j in range(8):
            gradient[j] -= Q(w*p1[j], p0*p0)
        count += 1
    assert count == 1864
    return value, tuple(gradient)


def direct_point(source: dict, c: tuple[Q, ...]) -> Q:
    value = Q(0)
    for w, masks in raw_terms(source):
        p = 1
        for i in range(14):
            p *= 256 + sum(c[j] for j in range(8) if masks[j] & (1 << i))
        value += Q(w, p)
    return value


def run() -> None:
    k185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
    k218 = ROOT / "lab/process/k218-order-six-exact-angular-elimination.json"
    k219 = ROOT / "lab/process/k219-order-six-signed-auxiliary-cell-enclosure.json"
    k217 = ROOT / "lab/process/k217-order-six-signed-inner-box.json"
    manifest = json.loads((ROOT / "lab/process/k220-order-six-signed-taylor-cell-enclosure.json").read_text())
    for label, path in (("k185", k185), ("k217", k217), ("k218", k218), ("k219", k219)):
        assert manifest["input_sha256"][label] == hashlib.sha256(path.read_bytes()).hexdigest()
    source = json.loads(k185.read_text())
    ratios = []
    for recorded in manifest["pilot_cells"].values():
        low = tuple(Q(x) for x in recorded["cosh_lower"])
        high = tuple(Q(x) for x in recorded["cosh_upper"])
        measure = Q(recorded["exact_product_cosh_measure"])
        bound = signed_taylor_bounds(source, low, high)
        value, gradient = direct_point_and_gradient(source, bound["center"])
        assert value == Q(recorded["center_core"]) == bound["center_core"]
        assert gradient == tuple(Q(x) for x in recorded["signed_gradient"]) == bound["signed_gradient"]
        for kind, field in (("taylor_core", "taylor_integral_interval_without_pi8"),
                            ("corner_core", "k219_integral_interval_without_pi8"),
                            ("intersection_core", "intersection_integral_interval_without_pi8")):
            assert [str(SCALE*measure*x) for x in bound[kind]] == recorded[field]
        for c in (low, high, bound["center"],
                  tuple(high[j] if j % 2 else low[j] for j in range(8)),
                  tuple(low[j] if j % 2 else high[j] for j in range(8))):
            point = direct_point(source, c)
            assert bound["taylor_core"][0] <= point <= bound["taylor_core"][1]
            assert bound["intersection_core"][0] <= point <= bound["intersection_core"][1]
        ratio = Q(recorded["intersection_width_to_k219_width"])
        assert ratio == (bound["intersection_core"][1]-bound["intersection_core"][0]) / (bound["corner_core"][1]-bound["corner_core"][0])
        assert 0 < ratio < 1
        ratios.append(float(ratio))
    # A load hit by the same coordinate changes its diagonal second
    # derivative even when the squared first slope is included.
    w, masks = next((w, masks) for w, masks in raw_terms(source)
                    if masks[0])
    c = (Q(1), Q(5,4))*4
    loads = [256 + sum(c[j] for j in range(8) if masks[j] & (1 << i)) for i in range(14)]
    q = Q(1)
    for a in loads:
        q /= a
    l0 = sum((Q(1, loads[i]) for i in range(14) if masks[0] & (1 << i)), Q(0))
    shared = sum((Q(1, loads[i]**2) for i in range(14)
                  if masks[0] & (1 << i)), Q(0))
    p0, p1, p2 = 1, 0, 0
    for i, a in enumerate(loads):
        bit = bool(masks[0] & (1 << i))
        p2 = p2*a + (p1 if bit else 0)
        p1 = p1*a + (p0 if bit else 0)
        p0 *= a
    polynomial_second = 2*Q(p1*p1, p0**3) - 2*Q(p2, p0**2)
    assert shared > 0 and polynomial_second == q*(l0*l0 + shared) != q*l0*l0
    # K218's alternating exact point is an independent prefactor/sign control.
    alternating = (Q(1), Q(5,4))*4
    expected = Q(json.loads(k218.read_text())["exact_signed_point_rational_without_pi8"]["alternating_zero_log2"])
    product = Q(1)
    for c_j in alternating:
        product *= c_j
    assert SCALE * product * direct_point(source, alternating) == expected
    inner = manifest["pilot_cells"]["k219_inner"]
    assert all(Q(x) == 0 for x in inner["signed_gradient"])
    inner_bound = Q(inner["intersection_integral_interval_without_pi8"][1])/3**8
    old_bound = Q(json.loads(k217.read_text())["remainder"]["whole_2928_ordered_term_absolute_ceiling"])
    assert inner_bound == Q(manifest["full_inner_comparison"]["absolute_upper_rational_using_pi_gt_3"])
    assert inner_bound < old_bound == Q(manifest["full_inner_comparison"]["k217_absolute_ceiling"])
    print("[PASS] independent 1,864-term polynomial gradients, cell inclusion, shared-load and K218 controls")
    print("width ratios:", ", ".join(f"{x:.8g}" for x in ratios))


if __name__ == "__main__":
    run()
