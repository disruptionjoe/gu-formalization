#!/usr/bin/env python3
"""Local whole-line KKT certificates on the first two K1771 slab boundaries."""
import importlib.util
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from flint import arb

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1788-full-fisher-first-two-slab-exclusion.json"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


k = load("k1781_for_k1788", ROOT / "tests/channel-swings/k1781_full_fisher_compact_jet.py")
q = load("k1786_for_k1788", ROOT / "tests/channel-swings/k1786_full_fisher_whole_line_tail_jet.py")


CASES = [
    {
        "slab": 1,
        "center_t": F(43983463391, 10**12),
        "center_z": F(91, 128),
        "radius_t": F(1, 10**11),
        "radius_z": F(0),
        "free_axis": 0,
        "outward_axis": 1,
        "outward_sign": 1,
        "boundary": "z=91/128 lower boundary",
    },
    {
        "slab": 2,
        "center_t": F(887855469, 17179869184),
        "center_z": F(576161143609, 10**12),
        "radius_t": F(0),
        "radius_z": F(1, 10**11),
        "free_axis": 1,
        "outward_axis": 0,
        "outward_sign": -1,
        "boundary": "t=887855469/17179869184 upper boundary",
    },
]


def symmetric_ball(text):
    value = arb(text)
    return arb(0, value.upper())


def one_case(case):
    q.CENTER_T, q.CENTER_Z = case["center_t"], case["center_z"]
    q.RADIUS_T, q.RADIUS_Z = case["radius_t"], case["radius_z"]
    tail = q.compute()["absolute_two_tail_bounds"]
    t, z, rt, rz = case["center_t"], case["center_z"], case["radius_t"], case["radius_z"]
    center = k.compact_jet(t, t, z, z)
    box = k.compact_jet(t - rt, t + rt, z - rz, z + rz)
    axis, outward = case["free_axis"], case["outward_axis"]
    gkey = "t" if axis == 0 else "z"
    hkey = "tt" if axis == 0 else "zz"
    okey = "t" if outward == 0 else "z"
    gradient = center.g[axis] + symmetric_ball(tail["gradient"][gkey])
    hessian = box.h[axis][axis] + symmetric_ball(tail["hessian"][hkey])
    center_hessian = center.h[axis][axis]
    radius = k.aq(rt if axis == 0 else rz)
    correction = -gradient / center_hessian
    residual_radius = abs(1 - hessian / center_hessian) * radius
    inclusion_radius = abs(correction) + residual_radius
    outward_gradient = box.g[outward] + symmetric_ball(tail["gradient"][okey])
    outward_ok = outward_gradient > 0 if case["outward_sign"] > 0 else outward_gradient < 0
    tail_value = arb(tail["value"]).upper()
    value_center = center.v + arb(tail_value / 2, tail_value / 2)
    variation = abs(gradient) * radius + abs(hessian) * radius**2 / 2
    value_enclosure = value_center + arb(0, variation.upper())
    return {
        "slab": case["slab"],
        "boundary": case["boundary"],
        "center": {"t": str(t), "z": str(z)},
        "free_radius": str(rt if axis == 0 else rz),
        "free_axis": gkey,
        "full_free_gradient_at_center": k.enc(gradient),
        "full_free_hessian_on_box": k.enc(hessian),
        "krawczyk_correction": k.enc(correction),
        "krawczyk_residual_radius": k.enc(residual_radius),
        "krawczyk_inclusion_radius": k.enc(inclusion_radius),
        "strict_inclusion": bool(inclusion_radius < radius),
        "full_inward_gradient_on_box": k.enc(outward_gradient),
        "strict_kkt_inward_sign": bool(outward_ok),
        "boundary_stationary_value_enclosure": k.enc(value_enclosure),
        "absolute_tail_value_bound": tail["value"],
    }


def compute():
    return {"boundary_boxes": [one_case(case) for case in CASES]}


def validate(data, got=None):
    got = compute() if got is None else got
    old = data["certificate"]["boundary_boxes"]
    new = got["boundary_boxes"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1788"),
        ("two boxes", len(old) == len(new) == 2),
    ]
    for a, b in zip(old, new):
        checks += [
            (f"slab {b['slab']} identity", a["slab"] == b["slab"]),
            (f"slab {b['slab']} inclusion", a["strict_inclusion"] and b["strict_inclusion"]),
            (f"slab {b['slab']} KKT sign", a["strict_kkt_inward_sign"] and b["strict_kkt_inward_sign"]),
            (f"slab {b['slab']} value", arb(a["boundary_stationary_value_enclosure"]).contains(
                arb(b["boundary_stationary_value_enclosure"]))),
        ]
    checks += [
        ("two local KKT points", data["decision"]["unique_local_boundary_kkt_points"] == 2),
        ("not slab excluded", not data["decision"]["slabs_one_and_two_globally_excluded"]),
    ]
    return checks


def main():
    if not ARTIFACT.exists() or "--print" in sys.argv:
        print(json.dumps(compute(), indent=2))
        return
    data = json.loads(ARTIFACT.read_text())
    checks = validate(data)
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
