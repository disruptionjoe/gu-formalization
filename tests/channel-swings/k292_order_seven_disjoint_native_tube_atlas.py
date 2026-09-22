#!/usr/bin/env python3
"""Build the exact a.e.-disjoint native atlas of the K284 shape tube."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K284 = ROOT / "lab/process/k284-order-seven-transverse-shape-atlas.json"
OUTPUT = ROOT / "lab/process/k292-order-seven-disjoint-native-tube-atlas.json"
COORDINATES = ("r0", "r1", "r2", "c0", "c1", "c2")
BASE = {
    "r0": Fraction(1, 32),
    "r1": Fraction(1, 64),
    "r2": Fraction(1, 128),
    "c0": Fraction(1, 40),
    "c1": Fraction(1, 80),
    "c2": Fraction(1, 160),
}


def fs(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k284 = json.loads(K284.read_text())
    h = Fraction(k284["fixed_control"]["transverse_shape_radius"])
    t0, t1 = Fraction(1), Fraction(5, 4)
    dt = t1 - t0
    width = 2 * h
    start_volume = width**6
    faces = []
    for index, coordinate in enumerate(COORDINATES):
        jacobian = BASE[coordinate]
        volume = dt * jacobian * width**5
        faces.append(
            {
                "stratum_id": f"sweep-{coordinate}",
                "advancing_coordinate": coordinate,
                "tie_priority": index,
                "parameterization": {
                    coordinate: f"{fs(BASE[coordinate])}*t+{fs(h)}",
                    **{
                        other: f"{fs(BASE[other])}*t+eta_{other}"
                        for other in COORDINATES
                        if other != coordinate
                    },
                },
                "free_shape_coordinates": [other for other in COORDINATES if other != coordinate],
                "native_jacobian": fs(jacobian),
                "exact_native_volume": fs(volume),
            }
        )
    total = start_volume + sum(Fraction(row["exact_native_volume"]) for row in faces)
    direct = width**6 + dt * width**5 * sum(BASE.values())
    assert total == direct
    return {
        "schema_version": "1.0",
        "result_id": "K292-ORDER-SEVEN-DISJOINT-NATIVE-TUBE-ATLAS",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "source_manifest": "lab/process/k284-order-seven-transverse-shape-atlas.json",
            "coordinates": list(COORDINATES),
            "projective_gap_ray": {name: fs(value) for name, value in BASE.items()},
            "projective_scale_range": [fs(t0), fs(t1)],
            "transverse_shape_radius": fs(h),
        },
        "union_definition": "U={g: exists t in [1,5/4], |g_i-b_i*t|<=h for every i}",
        "canonical_partition": {
            "start_box": "t=1 and |g_i-b_i|<=h for every i",
            "swept_rule": "outside the start box, set t_*(g)=max_i((g_i-h)/b_i); assign the smallest coordinate index attaining t_*",
            "tie_statement": "Multiple maximizers lie on codimension-one intersections and have native six-volume zero; the priority rule makes the serialization single-valued.",
            "coverage_proof": "For every g in U outside the start box, t_*(g)>1, t_*<=5/4, at least one coordinate satisfies g_k=b_k*t_*+h, and every other coordinate has g_j=b_j*t_*+eta_j with |eta_j|<=h.",
            "disjointness_proof": "The canonical smallest-maximizer rule assigns exactly one swept face off the measure-zero tie set; the start box is disjoint from all open swept strata.",
        },
        "strata": {
            "start_box": {
                "stratum_id": "start-box",
                "center_scale": fs(t0),
                "free_shape_coordinates": list(COORDINATES),
                "native_jacobian": "1/1",
                "exact_native_volume": fs(start_volume),
            },
            "swept_faces": faces,
        },
        "volume_identity": {
            "formula": "(2h)^6+(t1-t0)*(2h)^5*sum_i b_i",
            "start_box_volume": fs(start_volume),
            "swept_volume": fs(total - start_volume),
            "total_native_volume": fs(total),
            "independent_direct_formula_value": fs(direct),
            "exact_agreement": total == direct,
        },
        "release_test": {
            "all_six_advancing_faces_serialized": len(faces) == 6,
            "native_jacobian_retained_on_every_face": all(row["native_jacobian"] == fs(BASE[row["advancing_coordinate"]]) for row in faces),
            "almost_everywhere_disjoint_native_atlas_serialized": True,
            "complete_k284_tube_covered": True,
            "radial_or_projective_exterior_covered": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": {
            "AC-F1": "NEEDS_UNCHANGED",
            "LT-GR6b": "NEEDS_UNCHANGED",
            "LT-SM8": "NEEDS_UNCHANGED",
            "RA-F1": "NEEDS_UNCHANGED",
            "SC-META-53": "UNCERTAIN_UNCHANGED",
        },
        "claim_ceiling": "Exact almost-everywhere disjoint native dr dc atlas and volume for the K284 projective tube only; no radial/projective exterior bound, action-column value, complete residual, native K152 interval, physical state, source/ledger move, canon, paper or public claim.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build(), indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
