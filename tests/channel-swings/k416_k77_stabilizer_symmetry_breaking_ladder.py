#!/usr/bin/env python3
"""K416 exact K77 stabilizer/subquotient/symmetry-breaking ladder."""

from __future__ import annotations

import argparse
import json
from typing import Any


def hom_rank(source: dict[str, int], target: dict[str, int]) -> int:
    return sum(source.get(irrep, 0) * multiplicity for irrep, multiplicity in target.items())


def dimension(decomposition: dict[str, int], dimensions: dict[str, int]) -> int:
    return sum(multiplicity * dimensions[irrep] for irrep, multiplicity in decomposition.items())


def demo() -> dict[str, Any]:
    b3_dims = {"1": 1, "7v": 7, "8s": 8}
    b3_source = {"1": 21, "7v": 7}
    b3_target = {"8s": 16}

    compact_dims = {"(1,1,1)": 1, "(3,1,1)": 3, "(1,2,2)": 4,
                    "(2,2,1)": 4, "(2,1,2)": 4}
    compact_source = {"(1,1,1)": 21, "(3,1,1)": 7, "(1,2,2)": 7}
    compact_target = {"(2,2,1)": 16, "(2,1,2)": 16}

    diagonal_dims = {"1": 1, "3": 3}
    # 7 -> 3 + (2 tensor 2) = 1 + 3 + 3.
    diagonal_source = {"1": 21 + 7, "3": 2 * 7}
    # 8 -> (2 tensor 2) + (2 tensor 2) = 2*1 + 2*3.
    diagonal_target = {"1": 2 * 16, "3": 2 * 16}

    return {
        "schema_version": "1.0",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "tested_trace_realization": "full real K77 spinor; tested and not source-selected",
        "full_stabilizer": {
            "group": "Spin(3,4)",
            "complexified_type": "B3",
            "source_decomposition": b3_source,
            "target_decomposition": b3_target,
            "source_dimension": dimension(b3_source, b3_dims),
            "target_dimension": dimension(b3_target, b3_dims),
            "equivariant_hom_rank": hom_rank(b3_source, b3_target),
            "invariant_subquotient_statement": (
                "Every finite-dimensional invariant subquotient has only trivial and "
                "vector composition factors, so its Hom into a spinor-isotypic target is zero."
            ),
            "all_invariant_subquotients_obstructed": True,
        },
        "maximal_compact": {
            "group": "Spin(3)xSpin(4)=SU(2)_A x SU(2)_B x SU(2)_C",
            "vector_branching": "7 -> (3,1,1) + (1,2,2)",
            "spinor_branching": "8 -> (2,2,1) + (2,1,2)",
            "source_decomposition": compact_source,
            "target_decomposition": compact_target,
            "source_dimension": dimension(compact_source, compact_dims),
            "target_dimension": dimension(compact_target, compact_dims),
            "equivariant_hom_rank": hom_rank(compact_source, compact_target),
            "repair_reopens": False,
        },
        "declared_diagonal_breaking": {
            "group": "diagonal SU(2) in SU(2)_A x SU(2)_B x SU(2)_C",
            "vector_branching": "7 -> 1 + 3 + 3",
            "spinor_branching": "8 -> 2*1 + 2*3",
            "source_decomposition": diagonal_source,
            "target_decomposition": diagonal_target,
            "source_dimension": dimension(diagonal_source, diagonal_dims),
            "target_dimension": dimension(diagonal_target, diagonal_dims),
            "equivariant_hom_rank": hom_rank(diagonal_source, diagonal_target),
            "repair_reopens": True,
            "interpretation": (
                "Representation-level intertwiners become available only after this declared "
                "symmetry reduction; no action-owned map, quotient descent or Green domain follows."
            ),
        },
        "decision": {
            "smaller_full_stabilizer_invariant_image_repairs_route": False,
            "maximal_compact_restriction_repairs_route": False,
            "declared_diagonal_breaking_permits_representation_maps": True,
            "first_open_hom_rank_in_tested_ladder": 1344,
            "source_owned_symmetry_breaking_selected": False,
            "quotient_descent_solved": False,
            "green_domain_solved": False,
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
