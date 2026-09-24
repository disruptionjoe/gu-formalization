#!/usr/bin/env python3
"""K424 even-character BFV target branching and cohomology boundary."""

from __future__ import annotations

import argparse
import json


def hom_rank(source: dict[str, int], target: dict[str, int], end_dimension: int) -> int:
    return source["trivial"] * target["trivial"] + end_dimension * source["vector"] * target["vector"]


def branch(overlap: int) -> dict:
    ambient_trivial = 14 - overlap
    plane_trivial = 7 - overlap
    gauge = {
        "trivial": ambient_trivial * (ambient_trivial - 1) // 2 + (1 if overlap == 2 else 0),
        "vector": ambient_trivial + (1 if overlap == 3 else 0),
    }
    stabilizer = {
        "trivial": plane_trivial * (plane_trivial - 1) // 2 + (1 if overlap == 2 else 0),
        "vector": plane_trivial + (1 if overlap == 3 else 0),
    }
    orbit = {
        "trivial": gauge["trivial"] - stabilizer["trivial"],
        "vector": gauge["vector"] - stabilizer["vector"],
    }
    vector_dimension = overlap
    end_dimension = 2 if overlap == 2 else 1
    dimension = lambda module: module["trivial"] + vector_dimension * module["vector"]
    return {
        "group": f"Spin({overlap})",
        "vector_real_dimension": vector_dimension,
        "vector_endomorphism_real_dimension": end_dimension,
        "source_V_orbit": orbit,
        "targets": {"gauge_dual": gauge, "stabilizer_dual": stabilizer, "orbit_dual": orbit},
        "dimensions": {
            "source": dimension(orbit),
            "gauge_dual": dimension(gauge),
            "stabilizer_dual": dimension(stabilizer),
            "orbit_dual": dimension(orbit),
        },
        "equivariant_hom_real_ranks": {
            "source_to_gauge_dual": hom_rank(orbit, gauge, end_dimension),
            "source_to_stabilizer_dual": hom_rank(orbit, stabilizer, end_dimension),
            "source_to_orbit_dual": hom_rank(orbit, orbit, end_dimension),
        },
        "central_character": {"source": 1, "all_three_targets": 1},
    }


def demo() -> dict:
    branches = {"Spin2": branch(2), "Spin3": branch(3)}
    return {
        "schema_version": "1.0",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "branches": branches,
        "selected_finite_complex": {
            "primal_ranks": [21, 70],
            "dual_ranks": [70, 21],
            "dimensions": [21, 91, 70],
            "exact": True,
            "cohomology_dimensions": [0, 0, 0],
            "physical_functional_cohomology_computed": False,
        },
        "decision": {
            "even_character_targets_remove_k421_character_obstruction": True,
            "nonzero_equivariant_map_spaces_exist": True,
            "selected_finite_bfv_complex_supplies_nonzero_cohomology_target": False,
            "physical_quotient_or_domain_constructed": False,
            "next_exact_input": "An action-selected non-exact target summand or a functional completion whose closed cohomology survives, together with the actual Green domain and observation map.",
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
