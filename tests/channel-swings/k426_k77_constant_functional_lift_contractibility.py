#!/usr/bin/env python3
"""K426 constant functional lift of the K419 split exact complex."""

from __future__ import annotations

import argparse
import json


def d0(vector: list[int]) -> list[int]:
    assert len(vector) == 21
    return [0] * 70 + vector


def d1(vector: list[int]) -> list[int]:
    assert len(vector) == 91
    return vector[:70]


def h1(vector: list[int]) -> list[int]:
    assert len(vector) == 91
    return vector[70:]


def h2(vector: list[int]) -> list[int]:
    assert len(vector) == 70
    return vector + [0] * 21


def add(left: list[int], right: list[int]) -> list[int]:
    return [a + b for a, b in zip(left, right, strict=True)]


def basis(dimension: int, index: int) -> list[int]:
    return [int(position == index) for position in range(dimension)]


def verify_contraction() -> dict[str, bool]:
    left_identity = all(h1(d0(basis(21, i))) == basis(21, i) for i in range(21))
    middle_identity = all(
        add(d0(h1(basis(91, i))), h2(d1(basis(91, i)))) == basis(91, i)
        for i in range(91)
    )
    right_identity = all(d1(h2(basis(70, i))) == basis(70, i) for i in range(70))
    complex_identity = all(d1(d0(basis(21, i))) == [0] * 70 for i in range(21))
    return {
        "h1_d0_is_identity": left_identity,
        "d0_h1_plus_h2_d1_is_identity": middle_identity,
        "d1_h2_is_identity": right_identity,
        "d1_d0_is_zero": complex_identity,
    }


def demo() -> dict:
    identities = verify_contraction()
    assert all(identities.values())
    return {
        "schema_version": "1.0",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "native_to_native",
        "finite_fixture": {
            "dimensions": [21, 91, 70],
            "d0": "inject into the final 21 coordinates",
            "d1": "project onto the first 70 coordinates",
            "ranks": [21, 70],
            "cohomology_dimensions": [0, 0, 0],
        },
        "contracting_homotopy": {
            "h1": "project the middle space onto the final 21 coordinates",
            "h2": "inject the final space into the first 70 middle coordinates",
            "identities": identities,
            "euclidean_operator_norms": {"d0": 1, "d1": 1, "h1": 1, "h2": 1},
        },
        "functional_lift": {
            "coefficient_space": "any real vector space or compatible common function domain F",
            "lifted_dimensions": ["F^21", "F^91", "F^70"],
            "same_coordinate_maps": True,
            "contracting_homotopy_tensors_with_identity": True,
            "exact": True,
            "hilbert_ranges_closed": True,
            "bounded_green_contraction_norm": 1,
        },
        "decision": {
            "constant_pointwise_tensor_lift_creates_cohomology": False,
            "boundary_topology_alone_changes_this_split_complex": False,
            "required_escape": "coefficient variation, rank loss, incompatible domain/boundary conditions, or nonclosed range",
            "physical_bfv_cohomology_constructed": False,
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
