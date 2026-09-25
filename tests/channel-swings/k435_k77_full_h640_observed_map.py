#!/usr/bin/env sage-python
"""K435 exact full-carrier H640/observed map construction.

Run with::

    sage -python tests/channel-swings/k435_k77_full_h640_observed_map.py --demo

The construction is the deterministic full rank-1920 principal fixture used by
the historical H640 probes.  The public serialization is factorized: this
source file, the ordered generator words, the pivot convention, matrix shapes,
nonzero counts and content digests reproduce the actual rank-640 map and its
rank-1920 inverse/lift without embedding hundreds of thousands of scalar
entries in a JSON status artifact.
"""

from __future__ import annotations

import argparse
import hashlib
import json

from sage.all import GF, block_matrix, identity_matrix, matrix, zero_matrix


PRIMES = (1009, 1013)
OBSERVED_SPATIAL = (7, 8, 9)
OBSERVED_SLOTS = (0, 7, 8, 9, 14)
WORD_LABELS = ("1", "E7", "E8", "E9", "E7E8", "E7E9", "E8E9", "E7E8E9")


def tensor_all(field, factors):
    out = matrix(field, [[1]], sparse=True)
    for factor in factors:
        out = out.tensor_product(factor)
    return out


def canonical_digest(value) -> str:
    entries = [
        [int(row), int(column), int(entry)]
        for (row, column), entry in sorted(value.dict().items())
        if entry
    ]
    payload = {
        "shape": [int(value.nrows()), int(value.ncols())],
        "entries": entries,
    }
    raw = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def build_core(prime: int) -> dict:
    field = GF(prime)
    n, nv, spin, total = 7, 14, 128, 1920
    one_dim = nv * spin
    i2 = identity_matrix(field, 2, sparse=True)
    s1 = matrix(field, [[0, 1], [1, 0]], sparse=True)
    s3 = matrix(field, [[1, 0], [0, -1]], sparse=True)
    eps = matrix(field, [[0, 1], [-1, 0]], sparse=True)
    i128 = identity_matrix(field, spin, sparse=True)
    z128 = zero_matrix(field, spin, spin, sparse=True)
    i1920 = identity_matrix(field, total, sparse=True)

    plus, minus = [], []
    for index in range(n):
        plus.append(tensor_all(field, [s3] * index + [s1] + [i2] * (n - 1 - index)))
        minus.append(tensor_all(field, [s3] * index + [eps] + [i2] * (n - 1 - index)))
    gammas = plus + minus
    eta = [1] * 7 + [-1] * 7
    omega = i128
    for gamma in gammas:
        omega *= gamma
    p_plus = (i128 + omega) / field(2)
    p_minus = (i128 - omega) / field(2)

    def block_spin(value):
        return block_matrix(
            field,
            nv,
            nv,
            [[value if row == column else z128 for column in range(nv)] for row in range(nv)],
            sparse=True,
        )

    def wedge(index):
        return block_matrix(
            field,
            nv,
            nv,
            [[field(eta[row]) * gammas[row] * gammas[index] * gammas[column]
              if row != index and column not in (row, index) else z128
              for column in range(nv)] for row in range(nv)],
            sparse=True,
        )

    def k_map(index):
        return block_matrix(
            field,
            nv,
            1,
            [[i128 if row == index else z128] for row in range(nv)],
            sparse=True,
        )

    def codiff(index):
        return block_matrix(
            field,
            1,
            nv,
            [[field(eta[column]) * i128 if column == index else z128 for column in range(nv)]],
            sparse=True,
        )

    weights = p_plus + field(2) * p_minus
    southeast = field(11) / field(24) * p_plus + field(11) / field(12) * p_minus

    def symbol(index):
        return block_matrix(
            field,
            2,
            2,
            [[wedge(index) * block_spin(weights), k_map(index)],
             [-codiff(index), gammas[index] * southeast]],
            sparse=True,
        )

    symbols = [symbol(index) for index in range(14)]
    time = symbols[0]
    evolutions = {index: time.solve_right(symbols[index]) for index in range(1, 14)}

    slot_lift = matrix(field, 15, 5, sparse=True)
    for column, row in enumerate(OBSERVED_SLOTS):
        slot_lift[row, column] = 1
    coordinate_lift = slot_lift.tensor_product(i128)
    observation = coordinate_lift.transpose()

    zero_seed = block_matrix(
        field,
        2,
        1,
        [[zero_matrix(field, one_dim, spin, sparse=True)], [i128]],
        sparse=True,
    )
    e7, e8, e9 = [evolutions[index] for index in OBSERVED_SPATIAL]
    words = [i1920, e7, e8, e9, e7 * e8, e7 * e9, e8 * e9, e7 * e8 * e9]
    span = block_matrix(field, 1, len(words), [[word * zero_seed for word in words]], sparse=True)
    pivot_columns = tuple(int(value) for value in span.pivots())
    h640_basis = span.matrix_from_columns(pivot_columns)
    observed_map = observation * h640_basis
    observed_inverse = observed_map.inverse()
    ambient_lift = h640_basis * observed_inverse
    graph_projector = ambient_lift * observation

    checks = {
        "h640_rank_640": h640_basis.rank() == 640,
        "observed_map_rank_640": observed_map.rank() == 640,
        "observation_lift_identity": observation * ambient_lift == identity_matrix(field, 640, sparse=True),
        "lift_observation_is_h640_projector": graph_projector * ambient_lift == ambient_lift,
        "graph_projector_idempotent": graph_projector * graph_projector == graph_projector,
        "graph_projector_rank_640": graph_projector.rank() == 640,
        "observed_carrier_is_not_coordinate_equal_h640": h640_basis != coordinate_lift,
        "three_observed_evolutions_preserve_h640": all(
            graph_projector * evolutions[index] * ambient_lift == evolutions[index] * ambient_lift
            for index in OBSERVED_SPATIAL
        ),
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    return {
        "prime": prime,
        "field": field,
        "gammas": gammas,
        "eta": eta,
        "symbols": symbols,
        "time": time,
        "evolutions": evolutions,
        "observation": observation,
        "coordinate_lift": coordinate_lift,
        "h640_basis": h640_basis,
        "observed_map": observed_map,
        "observed_inverse": observed_inverse,
        "ambient_lift": ambient_lift,
        "graph_projector": graph_projector,
        "pivot_columns": pivot_columns,
        "checks": checks,
    }


def packet(core: dict) -> dict:
    matrices = {
        "h640_basis": core["h640_basis"],
        "coordinate_observation": core["observation"],
        "restricted_observation_map": core["observed_map"],
        "restricted_observation_inverse": core["observed_inverse"],
        "ambient_inverse_lift": core["ambient_lift"],
        "ambient_graph_projector": core["graph_projector"],
    }
    return {
        "prime": core["prime"],
        "pivot_count": len(core["pivot_columns"]),
        "pivot_sha256": "sha256:" + hashlib.sha256(
            json.dumps(core["pivot_columns"], separators=(",", ":")).encode()
        ).hexdigest(),
        "matrices": {
            name: {
                "shape": [int(value.nrows()), int(value.ncols())],
                "rank": int(value.rank()),
                "nnz": int(len(value.dict())),
                "content_digest": canonical_digest(value),
            }
            for name, value in matrices.items()
        },
        "checks": core["checks"],
    }


def demo() -> dict:
    packets = [packet(build_core(prime)) for prime in PRIMES]
    shape_rank_fingerprint = [
        [name, row["shape"], row["rank"]]
        for name, row in packets[0]["matrices"].items()
    ]
    assert shape_rank_fingerprint == [
        [name, row["shape"], row["rank"]]
        for name, row in packets[1]["matrices"].items()
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K435-K77-FULL-H640-OBSERVED-MAP",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "serialization_contract": {
            "carrier": "conditional selected K77 principal carrier of rank 1920",
            "seed": "the source-owned Omega0 spinor coordinate seed of rank 128",
            "ordered_generators": list(WORD_LABELS),
            "basis_rule": "concatenate each ordered generator word applied to the 128-column zero-form seed, then retain Sage pivot columns in deterministic order",
            "observed_slots": list(OBSERVED_SLOTS),
            "map": "coordinate observation restricted to the deterministic H640 basis",
            "inverse": "H640 basis times the inverse of the restricted observation map",
            "artifact_form": "exact executable factorized serialization plus shapes, nonzero counts and content digests; no lossy rank-only surrogate",
        },
        "cross_characteristic_packets": packets,
        "cross_characteristic_shape_rank_fingerprint": shape_rank_fingerprint,
        "decision": {
            "actual_rank_640_observation_map_constructed": True,
            "actual_rank_1920_ambient_inverse_lift_constructed": True,
            "actual_rank_1920_graph_projector_constructed": True,
            "compressed_rank_two_surrogate_needed": False,
            "full_lower_order_bv_kt_differential_constructed": False,
            "physical_cohomology_constructed": False,
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
