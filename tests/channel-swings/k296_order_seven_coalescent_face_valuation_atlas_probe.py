#!/usr/bin/env python3
"""Independent replay and hostile mutations for K296."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k296-order-seven-coalescent-face-valuation-atlas.json"


def valid(payload: dict) -> bool:
    faces = payload["projective_face_atlas"]
    one = [row for row in faces if row["codimension"] == 1]
    two = [row for row in faces if row["codimension"] == 2]
    decision = payload["decision"]
    release = payload["release_test"]
    return all(
        (
            len(payload["occurrence_census"]) == 24,
            len(one) == 6,
            len(two) == 15,
            all(row["common_size_four_cauchy_valuation"] == 1 for row in one),
            all(row["native_gap_product_valuation"] == 1 for row in one),
            decision["one_gap_native_plus_cauchy_valuation"] == 2,
            decision["all_one_gap_faces_have_companion_zero"] is False,
            decision["companion_zero_is_uniform_on_terminal_endpoint_join"] is False,
            len(payload["endpoint_joins"]) == 2,
            release["complete_exterior_integrand_bound_emitted"] is False,
        )
    )


def main() -> int:
    payload = json.loads(MANIFEST.read_text())
    if not valid(payload):
        raise AssertionError("K296 manifest failed independent replay")
    mutations = [
        ("occurrences", 23), ("one", 5), ("two", 14), ("cauchy", 0),
        ("native", 0), ("combined", 1), ("all_companion", True),
        ("uniform_join", True), ("joins", 1), ("exterior", True),
    ]
    rejected = 0
    for name, value in mutations:
        candidate = json.loads(json.dumps(payload))
        if name == "occurrences": candidate["occurrence_census"] = candidate["occurrence_census"][:value]
        elif name == "one": candidate["projective_face_atlas"] = [row for row in candidate["projective_face_atlas"] if row["codimension"] != 1][:] + [row for row in candidate["projective_face_atlas"] if row["codimension"] == 1][:value]
        elif name == "two": candidate["projective_face_atlas"] = [row for row in candidate["projective_face_atlas"] if row["codimension"] != 2][:] + [row for row in candidate["projective_face_atlas"] if row["codimension"] == 2][:value]
        elif name == "cauchy": next(row for row in candidate["projective_face_atlas"] if row["codimension"] == 1)["common_size_four_cauchy_valuation"] = value
        elif name == "native": next(row for row in candidate["projective_face_atlas"] if row["codimension"] == 1)["native_gap_product_valuation"] = value
        elif name == "combined": candidate["decision"]["one_gap_native_plus_cauchy_valuation"] = value
        elif name == "all_companion": candidate["decision"]["all_one_gap_faces_have_companion_zero"] = value
        elif name == "uniform_join": candidate["decision"]["companion_zero_is_uniform_on_terminal_endpoint_join"] = value
        elif name == "joins": candidate["endpoint_joins"] = candidate["endpoint_joins"][:value]
        else: candidate["release_test"]["complete_exterior_integrand_bound_emitted"] = value
        if not valid(candidate): rejected += 1
    if rejected != len(mutations):
        raise AssertionError("hostile mutation escaped K296 probe")
    print(f"K296 independent replay: 10/10 checks passed; hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
