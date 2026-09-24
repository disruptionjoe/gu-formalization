#!/usr/bin/env python3
"""Independent controls and hostile mutations for K424."""

from __future__ import annotations

import copy
import json

from k424_k77_even_bfv_target_cohomology_boundary import demo


def valid(result: dict) -> bool:
    s2 = result["branches"]["Spin2"]
    s3 = result["branches"]["Spin3"]
    complex_ = result["selected_finite_complex"]
    return all(
        [
            s2["source_V_orbit"] == {"trivial": 56, "vector": 7},
            s2["targets"]["gauge_dual"] == {"trivial": 67, "vector": 12},
            s2["targets"]["stabilizer_dual"] == {"trivial": 11, "vector": 5},
            s2["dimensions"] == {"source": 70, "gauge_dual": 91, "stabilizer_dual": 21, "orbit_dual": 70},
            s2["equivariant_hom_real_ranks"] == {"source_to_gauge_dual": 3920, "source_to_stabilizer_dual": 686, "source_to_orbit_dual": 3234},
            s3["source_V_orbit"] == {"trivial": 49, "vector": 7},
            s3["targets"]["gauge_dual"] == {"trivial": 55, "vector": 12},
            s3["targets"]["stabilizer_dual"] == {"trivial": 6, "vector": 5},
            s3["dimensions"] == {"source": 70, "gauge_dual": 91, "stabilizer_dual": 21, "orbit_dual": 70},
            s3["equivariant_hom_real_ranks"] == {"source_to_gauge_dual": 2779, "source_to_stabilizer_dual": 329, "source_to_orbit_dual": 2450},
            complex_["exact"] is True,
            complex_["cohomology_dimensions"] == [0, 0, 0],
            result["decision"]["even_character_targets_remove_k421_character_obstruction"] is True,
            result["decision"]["selected_finite_bfv_complex_supplies_nonzero_cohomology_target"] is False,
        ]
    )


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    for path, value in [
        (("branches", "Spin2", "source_V_orbit", "trivial"), 55),
        (("branches", "Spin2", "targets", "gauge_dual", "vector"), 11),
        (("branches", "Spin2", "equivariant_hom_real_ranks", "source_to_gauge_dual"), 3752),
        (("branches", "Spin2", "dimensions", "gauge_dual"), 90),
        (("branches", "Spin3", "source_V_orbit", "trivial"), 48),
        (("branches", "Spin3", "targets", "stabilizer_dual", "vector"), 4),
        (("branches", "Spin3", "equivariant_hom_real_ranks", "source_to_orbit_dual"), 2401),
        (("selected_finite_complex", "exact"), False),
        (("selected_finite_complex", "cohomology_dimensions"), [0, 1, 0]),
        (("decision", "selected_finite_bfv_complex_supplies_nonzero_cohomology_target"), True),
    ]:
        candidate = copy.deepcopy(result)
        target = candidate
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        mutations.append(candidate)
    rejected = sum(not valid(candidate) for candidate in mutations)
    assert rejected == len(mutations)
    print(json.dumps({"controls_passed": 14, "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
