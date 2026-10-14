#!/usr/bin/env python3
"""K1811: centered sixth-order whole-line Taylor bank on slab three.

The K1807 normalized-jet engine is reused at K1787's rational stationary
anchor, but the integrated quantity here is the full Fisher objective itself.
One point jet supplies cancellation-preserving Taylor coefficients; one jet on
the complete 78-leaf hull encloses the normalized sixth derivatives.  The
K1786 analytic tail machinery supplies whole-line value/gradient/Hessian
bounds.  Exact leaf evaluation then tests stationary rejection, convexity and
value separation without repeating quadrature 78 times.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from flint import arb

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1811-full-fisher-slab-three-anchored-score-bank.json"


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


m = load("k1807_for_k1811", ROOT / "tests/channel-swings/k1807_full_fisher_anchored_score_compact_taylor.py")
atlas = load("k1804_for_k1811", ROOT / "tests/channel-swings/k1804_full_fisher_deduplicated_boundary_atlas.py")
tails = load("k1786_for_k1811", ROOT / "tests/channel-swings/k1786_full_fisher_whole_line_tail_jet.py")
k = tails.k

ANCHOR_T = F(265664669701527, 5000000000000000)
ANCHOR_Z = F(8805034043103, 15625000000000)
STATIONARY_UPPER = F(1591786453049800, 10**22)


def fq(value) -> F:
    return F(str(value))


def slab_three_boxes():
    return [(cell, tuple(fq(value) for value in box))
            for slab, cell, box in atlas.retained_boxes() if slab == 3]


def slab_three_parents():
    return [(cell, tuple(fq(value) for value in box))
            for slab, cell, box in atlas.k.roots() if slab == 3]


def contains(parent, child):
    return parent[0] <= child[0] and child[1] <= parent[1] \
        and parent[2] <= child[2] and child[3] <= parent[3]


def full_integrand(y: m.Y, t: m.P, z: m.P):
    denominator, residual, gaussian, _, rv, v = m.mixture_parts(y, t, z)
    normal = m.P((2 * arb.pi()).sqrt())
    return t * gaussian * residual**2 / (v**2 * rv * normal * denominator)


def compact_jet(tlo: F, thi: F, zlo: F, zhi: F):
    t, z = m.P.var(m.ball(tlo, thi), 0), m.P.var(m.ball(zlo, zhi), 1)
    h = m.CELL_HALF_WIDTH
    cells = int(m.RADIUS / h)
    total = m.P(0)
    for index in range(-cells, cells):
        midpoint = (F(index) + F(1, 2)) * h
        local_half = h / 2
        point_y = m.Y([m.P(m.aq(midpoint)), m.P(1)] + [m.P(0)] * (m.OBSERVATION_ORDER - 2))
        point = full_integrand(point_y, t, z)
        piece = m.P(0)
        for degree in range(0, m.OBSERVATION_ORDER, 2):
            piece += point.c[degree] * m.aq(2 * local_half**(degree + 1) / F(degree + 1))
        interval_y = m.Y([m.P(m.ball(midpoint - local_half, midpoint + local_half)), m.P(1)]
                         + [m.P(0)] * (m.OBSERVATION_ORDER - 2))
        remainder = full_integrand(interval_y, t, z).c[m.OBSERVATION_ORDER - 1]
        scale = m.aq(2 * local_half**m.OBSERVATION_ORDER / F(m.OBSERVATION_ORDER))
        for key in piece.c:
            piece.c[key] += arb(0, (abs(remainder.c[key]) * scale).upper())
        total += piece
    return total


def offset_ball(lo: F, hi: F) -> arb:
    return m.ball(lo, hi)


def derivative_polynomial(point, global_jet, dt, dz, axis_counts):
    at, az = axis_counts
    maximum_degree = m.PARAMETER_ORDER - at - az - 1
    total = arb(0)
    for (i, j), coefficient in point.c.items():
        if i < at or j < az or (i - at) + (j - az) > maximum_degree:
            continue
        factor = 1
        for value in range(i - at + 1, i + 1):
            factor *= value
        for value in range(j - az + 1, j + 1):
            factor *= value
        total += arb(factor) * coefficient * dt**(i - at) * dz**(j - az)
    remainder = arb(0)
    for (i, j), coefficient in global_jet.c.items():
        if i < at or j < az or i + j != m.PARAMETER_ORDER:
            continue
        factor = 1
        for value in range(i - at + 1, i + 1):
            factor *= value
        for value in range(j - az + 1, j + 1):
            factor *= value
        term = arb(factor) * abs(coefficient) * max(abs(dt.lower()), abs(dt.upper()))**(i - at) \
            * max(abs(dz.lower()), abs(dz.upper()))**(j - az)
        remainder += arb(term.upper())
    return total + arb(0, remainder)


def symmetric_ball(text: str) -> arb:
    value = arb(text)
    return arb(0, value.upper())


def compute():
    m.P.order = m.PARAMETER_ORDER
    boxes = slab_three_boxes()
    tlo = min(box[0] for _, box in boxes)
    thi = max(box[1] for _, box in boxes)
    zlo = min(box[2] for _, box in boxes)
    zhi = max(box[3] for _, box in boxes)
    print("K1811: computing centered compact jet", file=sys.stderr, flush=True)
    point = compact_jet(ANCHOR_T, ANCHOR_T, ANCHOR_Z, ANCHOR_Z)
    parents = slab_three_parents()
    leaf_parent = {}
    for index, (_, box) in enumerate(boxes):
        matches = [parent_id for parent_id, (_, parent) in enumerate(parents)
                   if contains(parent, box)]
        assert len(matches) == 1, (index, matches)
        leaf_parent[index] = matches[0]
    global_jets = {}
    derivative_hulls = {}
    for parent_id, (cell, parent) in enumerate(parents):
        ctlo, cthi, czlo, czhi = parent
        member_count = sum(value == parent_id for value in leaf_parent.values())
        print(f"K1811: computing parent-{parent_id:02d} sixth-derivative enclosure",
              file=sys.stderr, flush=True)
        global_jets[parent_id] = compact_jet(ctlo, cthi, czlo, czhi)
        derivative_hulls[str(parent_id)] = {
            "t": [str(ctlo), str(cthi)], "z": [str(czlo), str(czhi)],
            "input_cell": cell,
            "leaf_count": member_count,
        }
    tails.CENTER_T = (tlo + thi) / 2
    tails.CENTER_Z = (zlo + zhi) / 2
    tails.RADIUS_T = (thi - tlo) / 2
    tails.RADIUS_Z = (zhi - zlo) / 2
    tail = tails.compute()
    tv = arb(tail["absolute_two_tail_bounds"]["value"])
    tg = [symmetric_ball(tail["absolute_two_tail_bounds"]["gradient"][key]) for key in ("t", "z")]
    th = [[symmetric_ball(tail["absolute_two_tail_bounds"]["hessian"][key])
           for key in ("tt", "tz")],
          [symmetric_ball(tail["absolute_two_tail_bounds"]["hessian"][key])
           for key in ("tz", "zz")]]
    rows = []
    for index, (cell, box) in enumerate(boxes):
        parent_id = leaf_parent[index]
        global_jet = global_jets[parent_id]
        ta, tb, za, zb = box
        dt = offset_ball(ta - ANCHOR_T, tb - ANCHOR_T)
        dz = offset_ball(za - ANCHOR_Z, zb - ANCHOR_Z)
        compact_value = derivative_polynomial(point, global_jet, dt, dz, (0, 0))
        gradient = [derivative_polynomial(point, global_jet, dt, dz, (1, 0)) + tg[0],
                    derivative_polynomial(point, global_jet, dt, dz, (0, 1)) + tg[1]]
        hessian = [[derivative_polynomial(point, global_jet, dt, dz, (2, 0)) + th[0][0],
                    derivative_polynomial(point, global_jet, dt, dz, (1, 1)) + th[0][1]],
                   [derivative_polynomial(point, global_jet, dt, dz, (1, 1)) + th[1][0],
                    derivative_polynomial(point, global_jet, dt, dz, (0, 2)) + th[1][1]]]
        determinant = hessian[0][0] * hessian[1][1] - hessian[0][1]**2
        rejected_by = [key for key, value in zip(("t", "z"), gradient) if not value.contains(0)]
        rows.append({
            "leaf": index,
            "parent": parent_id,
            "input_cell": cell,
            "box": [str(value) for value in box],
            "compact_value_lower": m.enc(arb(compact_value.lower())),
            "whole_line_value_upper": m.enc(compact_value + arb(0, tv.upper())),
            "whole_line_gradient": {"t": m.enc(gradient[0]), "z": m.enc(gradient[1])},
            "whole_line_hessian": {"tt": m.enc(hessian[0][0]), "tz": m.enc(hessian[0][1]),
                                   "zz": m.enc(hessian[1][1]), "determinant": m.enc(determinant)},
            "stationary_rejected": bool(rejected_by),
            "rejected_by": rejected_by,
            "strictly_convex": bool(hessian[0][0] > 0 and determinant > 0),
            "compact_value_above_stationary_upper": bool(compact_value > m.aq(STATIONARY_UPPER)),
        })
    return {
        "input_partition_digest": json.loads(atlas.k.ARTIFACT.read_text())["enclosure"]["partition_digest"],
        "leaf_count": len(rows),
        "anchor": {"t": str(ANCHOR_T), "z": str(ANCHOR_Z)},
        "stationary_value_upper_threshold": str(STATIONARY_UPPER),
        "hull": {"t": [str(tlo), str(thi)], "z": [str(zlo), str(zhi)]},
        "parameter_taylor_order": m.PARAMETER_ORDER,
        "k1794_parent_count": len(parents),
        "whole_line_tail_method": "one K1786 analytic value-gradient-Hessian tail ball on the complete slab-three hull",
        "rejected_leaf_count": sum(row["stationary_rejected"] for row in rows),
        "convex_leaf_count": sum(row["strictly_convex"] for row in rows),
        "value_separated_leaf_count": sum(row["compact_value_above_stationary_upper"] for row in rows),
        "retained_leaf_count": sum(not row["stationary_rejected"] for row in rows),
        "nonconvex_leaf_count": sum(not row["strictly_convex"] for row in rows),
        "value_unseparated_leaf_count": sum(not row["compact_value_above_stationary_upper"] for row in rows),
        "method_limit": "The centered sixth-order full-Fisher Taylor bank is interval-indeterminate on all 78 leaves even after narrowing sixth-derivative domains to the seventeen exact K1794 parents.",
    }


def validate(data, got=None):
    got = compute() if got is None else got
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1811"),
        ("inputs", data["inputs"] == ["K1781", "K1786", "K1787", "K1796", "K1804"]),
        ("exact replay", data["certificate"] == got),
        ("78 leaves", got["leaf_count"] == 78),
        ("tails analytic", data["decision"]["analytic_whole_line_tails_composed"]),
        ("retention fenced", not data["decision"]["retained_leaf_means_additional_stationary_point"]),
        ("uniqueness withheld", not data["decision"]["complete_stationary_uniqueness_proved"]),
        ("global withheld", not data["decision"]["global_optimizer_proved"]),
    ]


def main():
    got = compute()
    if not ARTIFACT.exists() or "--print" in sys.argv:
        print(json.dumps(got, indent=2))
        return
    checks = validate(json.loads(ARTIFACT.read_text()), got)
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
