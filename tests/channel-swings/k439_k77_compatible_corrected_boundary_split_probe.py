#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K439."""

from __future__ import annotations

import copy
import json

from k439_k77_compatible_corrected_boundary_split import demo


EXPECTED = {
    "corrected_carrier": 512,
    "canonical_incoming": 256,
    "canonical_outgoing": 256,
    "old_new_incoming_intersection": 192,
    "new_incoming_outside_old": 64,
    "old_incoming_constraint_leak": 128,
    "new_incoming_constraint_leak": 0,
}


def controls(result: dict) -> list[bool]:
    packets = result["cross_characteristic_packets"]
    decision = result["decision"]
    return [
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        result["direction"] == "native_to_observed",
        [row["prime"] for row in packets] == [1009, 1013],
        result["cross_characteristic_rank_fingerprint"] == EXPECTED,
        all(row["ranks"] == EXPECTED for row in packets),
        all(all(row["checks"].values()) for row in packets),
        result["canonical_functional_calculus"]["sign_polynomial"] == "J=(13823 A-13248 A^3)/575",
        decision["canonical_constraint_compatible_split_constructed"] is True,
        decision["modified_split_uses_fitted_parameter"] is False,
        decision["mutual_constraint_preservation"] is True,
        decision["orientation_reversal_complementarity"] is True,
        decision["physical_boundary_selected"] is False,
        decision["global_calderon_projector_constructed"] is False,
    ]


def valid(result: dict) -> bool:
    return all(controls(result))


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    for path, value in [
        (("classification",), "SUPPORTED"),
        (("direction",), "observed_to_native"),
        (("cross_characteristic_packets", 0, "prime"), 1013),
        (("cross_characteristic_rank_fingerprint", "canonical_incoming"), 320),
        (("cross_characteristic_packets", 0, "ranks", "new_incoming_outside_old"), 0),
        (("cross_characteristic_packets", 0, "checks", "sign_involution_on_corrected_carrier"), False),
        (("canonical_functional_calculus", "sign_polynomial"), "J=A"),
        (("decision", "canonical_constraint_compatible_split_constructed"), False),
        (("decision", "modified_split_uses_fitted_parameter"), True),
        (("decision", "mutual_constraint_preservation"), False),
        (("decision", "orientation_reversal_complementarity"), False),
        (("decision", "physical_boundary_selected"), True),
        (("decision", "global_calderon_projector_constructed"), True),
    ]:
        candidate = copy.deepcopy(result)
        target = candidate
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        mutations.append(candidate)
    rejected = sum(not valid(candidate) for candidate in mutations)
    assert rejected == len(mutations)
    print(json.dumps({"controls_passed": len(controls(result)), "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
