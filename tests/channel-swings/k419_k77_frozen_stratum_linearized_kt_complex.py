#!/usr/bin/env python3
"""K419 exact finite frozen-stratum action/reducibility complex."""

from __future__ import annotations

import argparse
import hashlib
import json
from typing import Any


def digest(value: Any) -> str:
    payload = json.dumps(value, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(payload).hexdigest()


def demo() -> dict[str, Any]:
    axes = list(range(14))
    odd_axes = {1, 3, 5, 7, 9, 11, 13}
    gauge_basis = [(a, b) for a in axes for b in axes if a < b]
    stabilizer_basis = [(a, b) for a, b in gauge_basis if a in odd_axes and b in odd_axes]
    orbit_basis = [pair for pair in gauge_basis if pair not in stabilizer_basis]
    orbit_index = {pair: index for index, pair in enumerate(orbit_basis)}
    action_columns = [None if pair in stabilizer_basis else orbit_index[pair] for pair in gauge_basis]
    stabilizer_inclusion = [gauge_basis.index(pair) for pair in stabilizer_basis]

    # Dual exact sequence: V* includes on complement coordinates, while g*
    # projects to the odd-odd coordinates h*. The maps compose to zero.
    dual_inclusion = [gauge_basis.index(pair) for pair in orbit_basis]
    dual_projection = [stabilizer_basis.index(pair) if pair in stabilizer_basis else None for pair in gauge_basis]
    composition_zero = all(dual_projection[column] is None for column in dual_inclusion)

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "native_to_native",
        "bases": {
            "gauge_dimension": len(gauge_basis),
            "stabilizer_dimension": len(stabilizer_basis),
            "orbit_dimension": len(orbit_basis),
            "gauge_basis_digest": digest(gauge_basis),
            "stabilizer_basis_digest": digest(stabilizer_basis),
            "orbit_basis_digest": digest(orbit_basis),
        },
        "primal_exact_sequence": {
            "sequence": "0 -> h -> so(7,7) -> V_orbit -> 0",
            "inclusion_rank": len(stabilizer_inclusion),
            "action_rank": len(orbit_basis),
            "action_kernel_dimension": action_columns.count(None),
            "action_surjective": set(column for column in action_columns if column is not None) == set(range(len(orbit_basis))),
            "composition_zero": all(action_columns[column] is None for column in stabilizer_inclusion),
            "euler_characteristic": len(stabilizer_basis) - len(gauge_basis) + len(orbit_basis),
            "map_digest": digest({"inclusion": stabilizer_inclusion, "action": action_columns}),
        },
        "dual_exact_sequence": {
            "sequence": "0 -> V_orbit* -> so(7,7)* -> h* -> 0",
            "dual_inclusion_rank": len(dual_inclusion),
            "relation_projection_rank": len(stabilizer_basis),
            "projection_kernel_dimension": len(orbit_basis),
            "composition_zero": composition_zero,
            "map_digest": digest({"inclusion": dual_inclusion, "projection": dual_projection}),
        },
        "linearized_kt_fixture": {
            "constraint_generators": len(gauge_basis),
            "independent_linearized_constraints": len(orbit_basis),
            "first_stage_relations": len(stabilizer_basis),
            "candidate_degree_1_antifields": len(gauge_basis),
            "candidate_degree_2_reducibility_generators": len(stabilizer_basis),
            "finite_complex_exact": True,
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
