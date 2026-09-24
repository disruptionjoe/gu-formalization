#!/usr/bin/env python3
"""Independent controls and hostile mutations for K421."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k421_k77_equivariant_quotient_green_obstruction.py")
MANIFEST = ROOT / "lab/process/k421-k77-equivariant-quotient-green-obstruction.json"


def load_solver():
    spec = importlib.util.spec_from_file_location("k421_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K421")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K421 = load_solver()


def checks(data: dict) -> list[tuple[str, bool]]:
    result = K421.demo()
    argument = result["central_character_argument"]
    functors = result["exact_functors"]
    observed = data.get("central_character_theorem", {})
    decision = data.get("decision", {})
    boundaries = data.get("boundaries", {})
    return [
        ("schema", data.get("schema_version") == "1.0"),
        ("classification", data.get("classification") == "BRIDGE_OR_SEMANTIC_BOUNDARY"),
        ("direction", data.get("direction") == "observed_to_native"),
        ("background count", result["scope"]["coordinate_backgrounds"] == 455),
        ("common groups", result["scope"]["common_groups"] == ["Spin(2)", "Spin(3)"]),
        ("source character", argument["source_character"] == 1),
        ("target character", argument["target_character"] == -1),
        ("characteristic", argument["field_characteristic"] == 0),
        ("Hom zero", argument["equivariant_hom_zero"] is True),
        ("kernel", functors["equivariant_kernel_preserves_target_character"] is True),
        ("image", functors["equivariant_image_preserves_target_character"] is True),
        ("quotient", functors["equivariant_quotient_preserves_target_character"] is True),
        ("cohomology", functors["equivariant_cohomology_preserves_target_character"] is True),
        ("Green subset", functors["green_compatible_maps_subset_of_equivariant_maps"] is True),
        ("manifest count", observed.get("coordinate_backgrounds") == 455),
        ("manifest equation", observed.get("intertwiner_equation") == "F=-F, hence F=0 in characteristic zero"),
        ("differential no repair", decision.get("same_target_equivariant_differential_repairs_map") is False),
        ("quotient no repair", decision.get("same_target_equivariant_quotient_repairs_map") is False),
        ("Green no repair", decision.get("green_pairing_or_adjointness_repairs_map") is False),
        ("other carrier fence", boundaries.get("other_target_carriers_excluded") is False),
        ("symmetry breaking fence", boundaries.get("symmetry_breaking_excluded") is False),
        ("domain fence", boundaries.get("functional_domain_constructed") is False),
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
        print(f"PASS {len(baseline)}/{len(baseline)} K421 controls")
        return 0
    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["central_character_theorem"].__setitem__("coordinate_backgrounds", 454),
        lambda d: d["central_character_theorem"].__setitem__("intertwiner_equation", "F=F"),
        lambda d: d["decision"].__setitem__("same_target_equivariant_differential_repairs_map", True),
        lambda d: d["decision"].__setitem__("same_target_equivariant_quotient_repairs_map", True),
        lambda d: d["decision"].__setitem__("green_pairing_or_adjointness_repairs_map", True),
        lambda d: d["boundaries"].__setitem__("other_target_carriers_excluded", True),
        lambda d: d["boundaries"].__setitem__("symmetry_breaking_excluded", True),
        lambda d: d["boundaries"].__setitem__("functional_domain_constructed", True),
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
