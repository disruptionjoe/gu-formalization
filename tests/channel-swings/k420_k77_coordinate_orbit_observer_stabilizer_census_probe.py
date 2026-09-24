#!/usr/bin/env python3
"""Independent controls and hostile mutations for K420."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k420_k77_coordinate_orbit_observer_stabilizer_census.py")
MANIFEST = ROOT / "lab/process/k420-k77-coordinate-orbit-observer-stabilizer-census.json"


def load_solver():
    spec = importlib.util.spec_from_file_location("k420_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K420")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K420 = load_solver()


def checks(data: dict) -> list[tuple[str, bool]]:
    result = K420.demo()
    census = result["census"]
    rows = census["rows"]
    observed = data.get("coordinate_census", {})
    decision = data.get("decision", {})
    boundaries = data.get("boundaries", {})
    return [
        ("schema", data.get("schema_version") == "1.0"),
        ("classification", data.get("classification") == "BRIDGE_OR_SEMANTIC_BOUNDARY"),
        ("direction", data.get("direction") == "observed_to_native"),
        ("ambient signature", result["signature"]["ambient"] == [7, 7]),
        ("plane signature", result["signature"]["stabilizer_plane"] == [3, 4]),
        ("plane count", census["signature_compatible_coordinate_planes"] == 1225),
        ("count identity", census["signature_compatible_coordinate_planes"] == census["expected_count"]),
        ("signature control", result["controls"]["all_planes_have_signature_3_4"] is True),
        ("unique planes", result["controls"]["planes_unique"] is True),
        ("histogram", [row["background_count"] for row in rows] == [140, 630, 420, 35]),
        ("generator histogram", [row["common_rotation_generators"] for row in rows] == [0, 0, 1, 3]),
        ("group histogram", [row["connected_common_group"] for row in rows] == ["no_nontrivial_connected_observer_rotation", "no_nontrivial_connected_observer_rotation", "Spin(2)", "Spin(3)"]),
        ("tested count", census["nontrivial_common_symmetry_backgrounds"] == 455),
        ("untested count", census["symmetry_insufficient_backgrounds"] == 770),
        ("original overlap", result["controls"]["original_observer_axis_overlap"] == 2),
        ("full Spin3 example", result["controls"]["full_observer_spin3_example_signature"] == [3, 4]),
        ("central characters", all(row["source_central_character"] == 1 and row["target_central_character"] == -1 for row in rows[2:])),
        ("Hom zero", all(row["equivariant_hom_rank"] == 0 for row in rows[2:])),
        ("manifest count", observed.get("total") == 1225 and observed.get("tested_by_common_symmetry") == 455),
        ("no repair", decision.get("tested_coordinate_backgrounds_repair_map") is False),
        ("untested fence", boundaries.get("trivial_common_rotation_cases_decided") is False),
        ("continuum fence", boundaries.get("continuous_orbit_exhausted") is False),
        ("source fence", boundaries.get("source_ledger_canon_paper_public_or_physical_effect") is False),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    baseline = checks(data)
    failed = [name for name, ok in baseline if not ok]
    if failed:
        print(f"FAIL baseline {len(baseline)-len(failed)}/{len(baseline)}: {failed}")
        return 1
    if not args.selftest:
        print(f"PASS {len(baseline)}/{len(baseline)} K420 controls")
        return 0
    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["coordinate_census"].__setitem__("total", 1224),
        lambda d: d["coordinate_census"].__setitem__("tested_by_common_symmetry", 456),
        lambda d: d["decision"].__setitem__("tested_coordinate_backgrounds_repair_map", True),
        lambda d: d["boundaries"].__setitem__("trivial_common_rotation_cases_decided", True),
        lambda d: d["boundaries"].__setitem__("continuous_orbit_exhausted", True),
        lambda d: d["boundaries"].__setitem__("source_ledger_canon_paper_public_or_physical_effect", True),
    ]
    caught = 0
    for mutate in mutations:
        trial = copy.deepcopy(data)
        mutate(trial)
        caught += int(any(not ok for _, ok in checks(trial)))
    if caught != len(mutations):
        print(f"FAIL hostile selftest caught {caught}/{len(mutations)}")
        return 1
    print(f"PASS hostile selftest caught {caught}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
