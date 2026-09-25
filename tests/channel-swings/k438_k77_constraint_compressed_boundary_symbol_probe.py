#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K438."""

from __future__ import annotations

import copy
import json

from k438_k77_constraint_compressed_boundary_symbol import demo


EXPECTED = {
    "observed_carrier": 640,
    "corrected_carrier": 512,
    "compressed_symbol": 512,
    "fast_abs_one_block": 384,
    "slow_abs_one_over_24_block": 128,
    "uncompressed_involution_defect": 128,
    "original_constraint_leak": 128,
}


def controls(result: dict) -> list[bool]:
    packets = result["cross_characteristic_packets"]
    decision = result["decision"]
    return [
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        result["direction"] == "observed_to_native",
        [row["prime"] for row in packets] == [1009, 1013],
        result["cross_characteristic_rank_fingerprint"] == EXPECTED,
        all(row["ranks"] == EXPECTED for row in packets),
        all(all(row["checks"].values()) for row in packets),
        result["construction"]["exact_identity"] == "576 A^4 - 577 A^2 + P = 0",
        decision["constraint_compressed_symbol_constructed"] is True,
        decision["zero_characteristic_root_present"] is False,
        decision["compressed_symbol_is_involution"] is False,
        decision["slow_characteristic_block_rank"] == 128,
        decision["action_and_constraint_determine_spectral_blocks"] is True,
        decision["physical_boundary_selected"] is False,
        decision["nonlinear_bv_kt_compatibility_proved"] is False,
    ]


def valid(result: dict) -> bool:
    return all(controls(result))


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    for path, value in [
        (("classification",), "SUPPORTED"),
        (("direction",), "native_to_observed"),
        (("cross_characteristic_packets", 0, "prime"), 1013),
        (("cross_characteristic_rank_fingerprint", "slow_abs_one_over_24_block"), 0),
        (("cross_characteristic_packets", 0, "ranks", "original_constraint_leak"), 0),
        (("cross_characteristic_packets", 0, "checks", "quartic_identity"), False),
        (("construction", "exact_identity"), "A^2=P"),
        (("decision", "constraint_compressed_symbol_constructed"), False),
        (("decision", "zero_characteristic_root_present"), True),
        (("decision", "compressed_symbol_is_involution"), True),
        (("decision", "slow_characteristic_block_rank"), 0),
        (("decision", "action_and_constraint_determine_spectral_blocks"), False),
        (("decision", "physical_boundary_selected"), True),
        (("decision", "nonlinear_bv_kt_compatibility_proved"), True),
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
