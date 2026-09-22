#!/usr/bin/env python3
"""Independent exact replay and hostile controls for K292."""

from __future__ import annotations

import copy
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k292-order-seven-disjoint-native-tube-atlas.json"
COORDINATES = ("r0", "r1", "r2", "c0", "c1", "c2")
BASE = tuple(Fraction(value) for value in ("1/32", "1/64", "1/128", "1/40", "1/80", "1/160"))
H = Fraction(1, 32768)


def check(payload: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    faces = payload.get("strata", {}).get("swept_faces", [])
    if len(faces) != 6 or [row.get("advancing_coordinate") for row in faces] != list(COORDINATES):
        failures.append("face_census")
        return failures
    width, dt = 2 * H, Fraction(1, 4)
    start = width**6
    swept = Fraction(0)
    for index, (row, base) in enumerate(zip(faces, BASE)):
        if Fraction(row.get("native_jacobian", "0")) != base:
            failures.append("jacobian")
        expected = dt * base * width**5
        if Fraction(row.get("exact_native_volume", "0")) != expected:
            failures.append("face_volume")
        if row.get("tie_priority") != index or len(row.get("free_shape_coordinates", [])) != 5:
            failures.append("face_coordinates")
        swept += expected
    volume = payload.get("volume_identity", {})
    total = start + swept
    if Fraction(volume.get("start_box_volume", "0")) != start:
        failures.append("start_volume")
    if Fraction(volume.get("total_native_volume", "0")) != total:
        failures.append("total_volume")
    partition = payload.get("canonical_partition", {})
    if "smallest coordinate index" not in partition.get("swept_rule", "") or "volume zero" not in partition.get("tie_statement", ""):
        failures.append("partition_rule")
    release = payload.get("release_test", {})
    if not release.get("complete_k284_tube_covered") or release.get("radial_or_projective_exterior_covered"):
        failures.append("release_scope")
    if "K284 projective tube only" not in payload.get("claim_ceiling", ""):
        failures.append("claim_ceiling")
    return failures


def mutate(payload: dict[str, Any], name: str) -> dict[str, Any]:
    result = copy.deepcopy(payload)
    if name == "face": result["strata"]["swept_faces"].pop()
    elif name == "order": result["strata"]["swept_faces"][0]["advancing_coordinate"] = "c2"
    elif name == "jacobian": result["strata"]["swept_faces"][0]["native_jacobian"] = "1/1"
    elif name == "face_volume": result["strata"]["swept_faces"][0]["exact_native_volume"] = "0/1"
    elif name == "total": result["volume_identity"]["total_native_volume"] = "0/1"
    elif name == "tie": result["canonical_partition"]["tie_statement"] = "ties ignored"
    elif name == "exterior": result["release_test"]["radial_or_projective_exterior_covered"] = True
    elif name == "ceiling": result["claim_ceiling"] = "Complete action column."
    return result


def main() -> int:
    payload = json.loads(MANIFEST.read_text())
    baseline = check(payload)
    if baseline:
        raise AssertionError(baseline)
    names = ("face", "order", "jacobian", "face_volume", "total", "tie", "exterior", "ceiling")
    rejected = {name: bool(check(mutate(payload, name))) for name in names}
    if not all(rejected.values()):
        raise AssertionError(rejected)
    print(json.dumps({"checks_passed": 8, "hostile_mutations_rejected": rejected}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
