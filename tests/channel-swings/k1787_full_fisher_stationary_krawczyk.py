#!/usr/bin/env python3
"""Whole-line Krawczyk isolation for the K1787 slab-three stationary box."""
import importlib.util
import json
import sys
from pathlib import Path

from flint import arb

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1787-full-fisher-stationary-krawczyk.json"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


k = load("k1781_for_k1787", ROOT / "tests/channel-swings/k1781_full_fisher_compact_jet.py")
q = load("k1786_for_k1787", ROOT / "tests/channel-swings/k1786_full_fisher_whole_line_tail_jet.py")


def symmetric_ball(text):
    value = arb(text)
    return arb(0, value.upper())


def compute():
    tail = q.compute()["absolute_two_tail_bounds"]
    t, z, rt, rz = q.CENTER_T, q.CENTER_Z, q.RADIUS_T, q.RADIUS_Z
    center = k.compact_jet(t, t, z, z)
    box = k.compact_jet(t - rt, t + rt, z - rz, z + rz)
    gradient = [
        center.g[0] + symmetric_ball(tail["gradient"]["t"]),
        center.g[1] + symmetric_ball(tail["gradient"]["z"]),
    ]
    hessian = [
        [box.h[0][0] + symmetric_ball(tail["hessian"]["tt"]),
         box.h[0][1] + symmetric_ball(tail["hessian"]["tz"])],
        [box.h[1][0] + symmetric_ball(tail["hessian"]["tz"]),
         box.h[1][1] + symmetric_ball(tail["hessian"]["zz"])],
    ]
    a, b, c = center.h[0][0], center.h[0][1], center.h[1][1]
    determinant = a * c - b * b
    preconditioner = [[c / determinant, -b / determinant],
                      [-b / determinant, a / determinant]]
    correction = [
        -(preconditioner[i][0] * gradient[0] + preconditioner[i][1] * gradient[1])
        for i in range(2)
    ]
    residual_matrix = [[
        arb(int(i == j)) - sum(preconditioner[i][u] * hessian[u][j] for u in range(2))
        for j in range(2)] for i in range(2)]
    radii = [k.aq(rt), k.aq(rz)]
    residual_radii = [
        sum(abs(residual_matrix[i][j]) * radii[j] for j in range(2))
        for i in range(2)
    ]
    inclusion_radii = [abs(correction[i]) + residual_radii[i] for i in range(2)]
    determinant_box = hessian[0][0] * hessian[1][1] - hessian[0][1]**2
    tail_value = arb(tail["value"]).upper()
    center_value = center.v + arb(tail_value / 2, tail_value / 2)
    variation = sum(abs(gradient[i]) * radii[i] for i in range(2))
    variation += sum(abs(hessian[i][j]) * radii[i] * radii[j]
                     for i in range(2) for j in range(2)) / 2
    stationary_value = center_value + arb(0, variation.upper())
    return {
        "parameter_box": {
            "center": {"t": str(t), "z": str(z)},
            "radius": {"t": str(rt), "z": str(rz)},
        },
        "full_gradient_at_center": {"t": k.enc(gradient[0]), "z": k.enc(gradient[1])},
        "full_hessian_tt_on_box": k.enc(hessian[0][0]),
        "full_hessian_determinant_on_box": k.enc(determinant_box),
        "stationary_value_enclosure": k.enc(stationary_value),
        "krawczyk_correction": {"t": k.enc(correction[0]), "z": k.enc(correction[1])},
        "krawczyk_residual_radius": {"t": k.enc(residual_radii[0]), "z": k.enc(residual_radii[1])},
        "krawczyk_inclusion_radius": {"t": k.enc(inclusion_radii[0]), "z": k.enc(inclusion_radii[1])},
        "strict_inclusion": {
            "t": bool(inclusion_radii[0] < radii[0]),
            "z": bool(inclusion_radii[1] < radii[1]),
        },
    }


def validate(data, got=None):
    got = compute() if got is None else got
    cert = data["certificate"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1787"),
        ("box", cert["parameter_box"] == got["parameter_box"]),
        ("hessian tt positive", arb(cert["full_hessian_tt_on_box"]) > 0),
        ("determinant positive", arb(cert["full_hessian_determinant_on_box"]) > 0),
        ("stationary value", arb(cert["stationary_value_enclosure"]).contains(
            arb(got["stationary_value_enclosure"]))),
        ("strict t inclusion", cert["strict_inclusion"]["t"] and got["strict_inclusion"]["t"]),
        ("strict z inclusion", cert["strict_inclusion"]["z"] and got["strict_inclusion"]["z"]),
    ]
    for group in ("full_gradient_at_center", "krawczyk_correction",
                  "krawczyk_residual_radius", "krawczyk_inclusion_radius"):
        for key, value in got[group].items():
            checks.append((f"{group}.{key}", arb(cert[group][key]).contains(arb(value))))
    checks += [
        ("unique zero in box", data["decision"]["unique_whole_line_stationary_point_in_named_box"]),
        ("not slab unique", not data["decision"]["unique_stationary_point_on_complete_slab_three"]),
        ("not global", not data["decision"]["global_optimizer_proved"]),
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
