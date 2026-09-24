#!/usr/bin/env python3
"""Independent controls and hostile mutations for K422."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k422_k77_homogeneous_orbit_reducibility_bundle.py")
MANIFEST = ROOT / "lab/process/k422-k77-homogeneous-orbit-reducibility-bundle.json"


def load_solver():
    spec = importlib.util.spec_from_file_location("k422_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K422")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K422 = load_solver()


def checks(data: dict) -> list[tuple[str, bool]]:
    result = K422.demo()
    complex_data = result["homogeneous_orbit_complex"]
    controls = result["coordinate_controls"]
    observed = data.get("reducibility_bundle", {})
    decision = data.get("decision", {})
    boundaries = data.get("boundaries", {})
    return [
        ("schema", data.get("schema_version") == "1.0"),
        ("classification", data.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", data.get("direction") == "native_to_native"),
        ("gauge rank", complex_data["gauge_bundle_rank"] == 91),
        ("relation rank", complex_data["first_stage_relation_bundle_rank"] == 21),
        ("constraint rank", complex_data["independent_constraint_bundle_rank"] == 70),
        ("rank split", 21 + 70 == 91),
        ("constant rank", complex_data["constant_rank"] is True),
        ("control count", controls["backgrounds"] == 1225),
        ("transport controls", controls["all_transport_controls_pass"] is True),
        ("Spin lifts", controls["all_spin_identity_component_lifts_exist"] is True),
        ("orientation repairs", controls["maximum_orientation_sign_repairs"] == 2),
        ("digest shape", len(controls["row_digest"]) == 64),
        ("manifest ranks", observed.get("ranks") == [21, 91, 70]),
        ("manifest controls", observed.get("coordinate_transport_controls") == 1225),
        ("globalizes", decision.get("k419_complex_globalizes_on_homogeneous_orbit") is True),
        ("constant type", decision.get("homogeneous_orbit_constant_stabilizer_type") is True),
        ("varying stratum fence", boundaries.get("ambient_varying_orbit_type_resolved") is False),
        ("nonlinear fence", boundaries.get("nonlinear_koszul_tate_properness_proved") is False),
        ("functional fence", boundaries.get("functional_bfv_domain_or_physical_cohomology_constructed") is False),
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
        print(f"PASS {len(baseline)}/{len(baseline)} K422 controls")
        return 0
    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "observed_to_native"),
        lambda d: d["reducibility_bundle"].__setitem__("ranks", [20, 91, 71]),
        lambda d: d["reducibility_bundle"].__setitem__("coordinate_transport_controls", 1224),
        lambda d: d["decision"].__setitem__("k419_complex_globalizes_on_homogeneous_orbit", False),
        lambda d: d["decision"].__setitem__("homogeneous_orbit_constant_stabilizer_type", False),
        lambda d: d["boundaries"].__setitem__("ambient_varying_orbit_type_resolved", True),
        lambda d: d["boundaries"].__setitem__("nonlinear_koszul_tate_properness_proved", True),
        lambda d: d["boundaries"].__setitem__("functional_bfv_domain_or_physical_cohomology_constructed", True),
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
