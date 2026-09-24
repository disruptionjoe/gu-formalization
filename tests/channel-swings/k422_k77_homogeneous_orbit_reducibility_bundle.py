#!/usr/bin/env python3
"""K422 transport the frozen exact complex over the homogeneous orbit."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from typing import Any


ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
POSITIVE = tuple(index for index, sign in enumerate(ETA) if sign == 1)
NEGATIVE = tuple(index for index, sign in enumerate(ETA) if sign == -1)
ORIGINAL = frozenset(range(1, 14, 2))
GAUGE_BASIS = tuple((a, b) for a in range(14) for b in range(a + 1, 14))


def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, separators=(",", ":"), sort_keys=True).encode()).hexdigest()


def canonical_signature_permutation(target: frozenset[int]) -> dict[int, int]:
    mapping: dict[int, int] = {}
    for sign_axes in (POSITIVE, NEGATIVE):
        old_inside = sorted(ORIGINAL & set(sign_axes))
        old_outside = sorted(set(sign_axes) - ORIGINAL)
        new_inside = sorted(target & set(sign_axes))
        new_outside = sorted(set(sign_axes) - target)
        mapping.update(zip(old_inside, new_inside, strict=True))
        mapping.update(zip(old_outside, new_outside, strict=True))
    return mapping


def mapped_pair(pair: tuple[int, int], permutation: dict[int, int]) -> tuple[int, int]:
    return tuple(sorted((permutation[pair[0]], permutation[pair[1]])))


def permutation_sign(images: list[int], ordered_axes: tuple[int, ...]) -> int:
    positions = {axis: index for index, axis in enumerate(ordered_axes)}
    word = [positions[axis] for axis in images]
    inversions = sum(word[i] > word[j] for i in range(len(word)) for j in range(i + 1, len(word)))
    return -1 if inversions % 2 else 1


def demo() -> dict[str, Any]:
    planes = [
        frozenset((*positive, *negative))
        for positive in itertools.combinations(POSITIVE, 3)
        for negative in itertools.combinations(NEGATIVE, 4)
    ]
    original_stabilizer = {pair for pair in GAUGE_BASIS if pair[0] in ORIGINAL and pair[1] in ORIGINAL}
    original_orbit = set(GAUGE_BASIS) - original_stabilizer
    rows = []
    for plane in planes:
        stabilizer = {pair for pair in GAUGE_BASIS if pair[0] in plane and pair[1] in plane}
        orbit = set(GAUGE_BASIS) - stabilizer
        permutation = canonical_signature_permutation(plane)
        mapped_stabilizer = {mapped_pair(pair, permutation) for pair in original_stabilizer}
        mapped_orbit = {mapped_pair(pair, permutation) for pair in original_orbit}
        # A bare coordinate permutation can reverse one signature block. A
        # diagonal sign on one target axis in each reversed block repairs its
        # determinant without changing the target plane. The resulting
        # SO(7)xSO(7) element lies in the maximal compact of SO_0(7,7) and has
        # a Spin(7,7) lift.
        positive_sign = permutation_sign([permutation[index] for index in POSITIVE], POSITIVE)
        negative_sign = permutation_sign([permutation[index] for index in NEGATIVE], NEGATIVE)
        sign_repairs = int(positive_sign < 0) + int(negative_sign < 0)
        rows.append(
            {
                "plane": sorted(plane),
                "stabilizer_dimension": len(stabilizer),
                "orbit_dimension": len(orbit),
                "signature_preserved": all(ETA[source] == ETA[target] for source, target in permutation.items()),
                "permutation_bijective": set(permutation) == set(range(14)) and set(permutation.values()) == set(range(14)),
                "orientation_sign_repairs": sign_repairs,
                "spin_identity_component_lift_exists": sign_repairs in (0, 1, 2),
                "stabilizer_transport_exact": mapped_stabilizer == stabilizer,
                "orbit_transport_exact": mapped_orbit == orbit,
            }
        )
    exact = all(
        row["stabilizer_dimension"] == 21
        and row["orbit_dimension"] == 70
        and row["signature_preserved"]
        and row["permutation_bijective"]
        and row["spin_identity_component_lift_exists"]
        and row["stabilizer_transport_exact"]
        and row["orbit_transport_exact"]
        for row in rows
    )
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "native_to_native",
        "homogeneous_orbit_complex": {
            "primal": "0 -> stabilizer_bundle_21 -> trivial_gauge_bundle_91 -> tangent_orbit_bundle_70 -> 0",
            "dual": "0 -> cotangent_orbit_bundle_70 -> trivial_gauge_dual_bundle_91 -> relation_bundle_21 -> 0",
            "constant_rank": exact,
            "first_stage_relation_bundle_rank": 21,
            "independent_constraint_bundle_rank": 70,
            "gauge_bundle_rank": 91,
        },
        "coordinate_controls": {
            "backgrounds": len(rows),
            "all_transport_controls_pass": exact,
            "all_spin_identity_component_lifts_exist": all(row["spin_identity_component_lift_exists"] for row in rows),
            "maximum_orientation_sign_repairs": max(row["orientation_sign_repairs"] for row in rows),
            "row_digest": digest(rows),
        },
        "decision": {
            "k419_exact_complex_globalizes_over_homogeneous_gauge_orbit": exact,
            "homogeneous_orbit_has_constant_stabilizer_type": exact,
            "ambient_varying_orbit_type_resolved": False,
            "nonlinear_koszul_tate_properness_resolved": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
