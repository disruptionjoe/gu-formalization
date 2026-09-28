#!/usr/bin/env python3
"""Independent replay and hostile mutations for K554."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k554_orders_eleven_twelve_gauss_laguerre_face_atlas.py"
MANIFEST = ROOT / "lab/process/k554-orders-eleven-twelve-gauss-laguerre-face-atlas.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k554_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PRODUCER}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    stored = json.loads(MANIFEST.read_text())
    rebuilt = module.build()
    module.validate_payload(rebuilt)
    controls = [
        stored == rebuilt,
        stored["fixed_control"]["combined_paths"] == 1792,
        stored["fixed_control"]["combined_groups"] == 57,
        stored["fixed_control"]["combined_upper_triangle_entries"] == 48272,
        stored["fixed_control"]["combined_ordered_terms"] == 94752,
        [row["positive_time_variables"] for row in stored["order_interfaces"]] == [24, 26],
        [row["native_prefactor"] for row in stored["order_interfaces"]] == ["(2*pi)^-13", "(2*pi)^-14"],
        all(stored["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("combined_paths", 1791),
        lambda p: p["fixed_control"].__setitem__("combined_groups", 56),
        lambda p: p["fixed_control"].__setitem__("combined_upper_triangle_entries", 48271),
        lambda p: p["fixed_control"].__setitem__("combined_ordered_terms", 94751),
        lambda p: p["order_interfaces"][0].__setitem__("maximum_species_determinant_rank", 5),
        lambda p: p["order_interfaces"][1].__setitem__("native_prefactor", "(2*pi)^-13"),
        lambda p: p["decision"].__setitem__("complete_order_eleven_integral_emitted", True),
        lambda p: p["release_test"].__setitem__("native_K152_interval_not_emitted", False),
    ):
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            mutations.append(True)
        else:
            mutations.append(False)
    if not all(controls) or not all(mutations):
        raise AssertionError(f"K554 probe failed: controls={controls}, mutations={mutations}")
    print(f"K554 probe: {sum(controls)}/{len(controls)} controls; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
