#!/usr/bin/env python3
"""Independent regeneration and hostile probe for K542."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k542_order_ten_normal_projective_partition.py"
STORED = ROOT / "lab/process/k542-order-ten-normal-projective-partition.json"
spec = importlib.util.spec_from_file_location("k542_probe_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K542 producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    module.validate_payload(stored)
    checks = [
        stored == rebuilt,
        len(stored["program_partition_map"]) == 936,
        sum(row["certified_normal_cells"] for row in stored["program_partition_map"]) == 6552,
        len(stored["mask_atlas"]) == stored["fixed_control"]["unique_zero_masks"],
        sum(row["chart_count"] for row in stored["mask_atlas"]) == stored["fixed_control"]["unique_maximum_charts"],
        sum(len(row["chart_ids"]) for row in stored["program_partition_map"]) == stored["fixed_control"]["program_chart_uses"],
        all(row["agrees"] for row in stored["jacobian_controls"]),
        all(row["reconstructed_exactly"] and row["chart_mass_sum_is_simplex_mass"] for row in stored["exact_controls"]),
        stored["coordinate_and_measure_contract"]["closed_chart_union_covers_complete_projective_simplex"],
        all(stored["determinant_preservation_contract"].values()),
        all(stored["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("K542 independent control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("face_programs", 935),
        lambda p: p["fixed_control"].__setitem__("certified_positive_width_normal_cells", 6545),
        lambda p: p["program_partition_map"].pop(),
        lambda p: p["program_partition_map"][0].__setitem__("program_id", p["program_partition_map"][1]["program_id"]),
        lambda p: p["program_partition_map"][0].__setitem__("certified_normal_cells", 6),
        lambda p: p["mask_atlas"].pop(),
        lambda p: p["exact_controls"][0].__setitem__("chart_mass_sum_is_simplex_mass", False),
        lambda p: p["jacobian_controls"][0].__setitem__("agrees", False),
        lambda p: p["coordinate_and_measure_contract"].__setitem__("closed_chart_union_covers_complete_projective_simplex", False),
        lambda p: p["determinant_preservation_contract"].__setitem__("K413_singular_and_confluent_template_ids_preserved_per_program", False),
        lambda p: p["boundary_routing_contract"].__setitem__("interval_closures_still_require_one_sided_zero_safe_majorants", False),
        lambda p: p["decision"].__setitem__("positive_width_projective_ratio_cells_evaluated", True),
        lambda p: p["decision"].__setitem__("recursive_positive_interior_cover_complete", True),
        lambda p: p["decision"].__setitem__("complete_hybrid_integrals_emitted", True),
        lambda p: p["release_test"].__setitem__("native_K152_interval_not_emitted", False),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"K542 hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K542 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
