#!/usr/bin/env sage-python
"""K436 full rank-1920 action boundary projector on the observed x7 face."""

from __future__ import annotations

import argparse
import json

from sage.all import block_matrix, identity_matrix, zero_matrix

from k435_k77_full_h640_observed_map import PRIMES, build_core, canonical_digest


NORMAL_INDEX = 7


def build_boundary_packet(prime: int, keep_core: bool = False) -> dict:
    core = build_core(prime)
    field = core["field"]
    identity1920 = identity_matrix(field, 1920, sparse=True)
    time = core["time"]
    normal = core["symbols"][NORMAL_INDEX]
    reduced = time.solve_right(normal)
    incoming = (identity1920 - reduced) / field(2)
    outgoing = (identity1920 + reduced) / field(2)
    lift = core["ambient_lift"]
    observation = core["observation"]
    h640_projector = core["graph_projector"]
    observed_reduced = observation * reduced * lift
    observed_incoming = observation * incoming * lift
    observed_outgoing = observation * outgoing * lift
    h640_incoming_lift = incoming * lift

    h640_invariance_residual = (identity1920 - h640_projector) * reduced * lift
    checks = {
        "time_symbol_invertible": time.rank() == 1920,
        "normal_symbol_invertible": normal.rank() == 1920,
        "reduced_symbol_involution": reduced * reduced == identity1920,
        "incoming_projector_idempotent": incoming * incoming == incoming,
        "outgoing_projector_idempotent": outgoing * outgoing == outgoing,
        "incoming_outgoing_complementary": incoming + outgoing == identity1920,
        "incoming_outgoing_disjoint": incoming * outgoing == zero_matrix(field, 1920, 1920, sparse=True),
        "incoming_rank_960": incoming.rank() == 960,
        "h640_preserved_by_boundary_symbol": h640_invariance_residual.is_zero(),
        "observed_reduced_symbol_involution": observed_reduced * observed_reduced == identity_matrix(field, 640, sparse=True),
        "observed_incoming_idempotent": observed_incoming * observed_incoming == observed_incoming,
        "observed_outgoing_idempotent": observed_outgoing * observed_outgoing == observed_outgoing,
        "observed_orientation_reversal_complement": observed_incoming + observed_outgoing == identity_matrix(field, 640, sparse=True),
        "observation_intertwines_incoming": observation * incoming * lift == observed_incoming,
        "lift_intertwines_incoming": incoming * lift == lift * observed_incoming,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    matrix_rows = {
        "time_symbol": time,
        "normal_symbol_plus_dx7": normal,
        "reduced_normal_symbol": reduced,
        "ambient_incoming_projector": incoming,
        "observed_reduced_normal_symbol": observed_reduced,
        "observed_incoming_projector": observed_incoming,
        "h640_incoming_lift": h640_incoming_lift,
    }
    row = {
        "prime": prime,
        "ambient_ranks": {
            "carrier": 1920,
            "incoming": int(incoming.rank()),
            "outgoing": int(outgoing.rank()),
        },
        "h640_ranks": {
            "carrier": 640,
            "incoming": int(observed_incoming.rank()),
            "outgoing": int(observed_outgoing.rank()),
        },
        "matrices": {
            name: {
                "shape": [int(value.nrows()), int(value.ncols())],
                "rank": int(value.rank()),
                "nnz": int(len(value.dict())),
                "content_digest": canonical_digest(value),
            }
            for name, value in matrix_rows.items()
        },
        "checks": checks,
    }
    if keep_core:
        row["core"] = core
        row["reduced"] = reduced
        row["incoming"] = incoming
        row["outgoing"] = outgoing
        row["observed_reduced"] = observed_reduced
        row["observed_incoming"] = observed_incoming
        row["observed_outgoing"] = observed_outgoing
    return row


def public_packet(row: dict) -> dict:
    return {key: value for key, value in row.items() if key not in {
        "core", "reduced", "incoming", "outgoing", "observed_reduced",
        "observed_incoming", "observed_outgoing",
    }}


def demo() -> dict:
    packets = [public_packet(build_boundary_packet(prime)) for prime in PRIMES]
    assert [row["h640_ranks"] for row in packets] == [
        {"carrier": 640, "incoming": 320, "outgoing": 320},
        {"carrier": 640, "incoming": 320, "outgoing": 320},
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K436-K77-FULL-ACTION-BOUNDARY-PROJECTOR",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "native_to_observed",
        "boundary": {
            "observed_hypersurface": "x7=0 in the selected flat observed 1+3 chart",
            "outward_conormal": "+dx7",
            "normal_index": NORMAL_INDEX,
            "orientation_reversal": "-dx7 exchanges Pi_in and Pi_out",
            "selection_ceiling": "the oriented face is a declared conditional test boundary, not a source-selected physical boundary",
        },
        "full_symbol_contract": {
            "time_symbol": "D_t=D_0 from the selected K77 sixteen-cell principal operator",
            "normal_symbol": "D_n=D_7 on outward conormal +dx7",
            "reduced_symbol": "S_7=D_t^-1 D_7",
            "incoming_projector": "Pi_in=(I-S_7)/2",
            "outgoing_projector": "Pi_out=(I+S_7)/2",
        },
        "cross_characteristic_packets": packets,
        "decision": {
            "actual_rank_1920_time_and_normal_symbols_constructed": True,
            "actual_rank_960_ambient_incoming_projector_constructed": True,
            "h640_preserved": True,
            "actual_rank_320_h640_incoming_projector_constructed": True,
            "orientation_load_bearing": True,
            "global_closed_domain_constructed": False,
            "physical_boundary_selected": False,
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
