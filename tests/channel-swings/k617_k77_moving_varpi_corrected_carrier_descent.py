#!/usr/bin/env sage-python
"""K617 descent of the historical moving-varpi graph to the corrected carrier."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sage.all import block_matrix, identity_matrix, zero_matrix

from k435_k77_full_h640_observed_map import PRIMES
from k436_k77_full_action_boundary_projector import build_boundary_packet
from k438_k77_constraint_compressed_boundary_symbol import (
    OBSERVED_ONE_FORM_INDICES,
    build_compressed_packet,
)
from k439_k77_compatible_corrected_boundary_split import build_split_packet


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k617-k77-moving-varpi-corrected-carrier-descent.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def observed_graphs(prime: int, compressed: dict) -> dict:
    core = build_boundary_packet(prime, keep_core=True)["core"]
    field = core["field"]
    gammas = core["gammas"]
    eta = core["eta"]
    q = gammas[7]
    identity = identity_matrix(field, 128, sparse=True)
    row_blocks = [
        -field(eta[index]) / field(12) * gammas[index] * q
        for index in OBSERVED_ONE_FORM_INDICES
    ]
    column_blocks = [
        field(-1 if index == 7 else 1)
        * q
        * field(eta[index])
        / field(12)
        * gammas[index]
        for index in OBSERVED_ONE_FORM_INDICES
    ]
    return {
        "row_pin": block_matrix(
            field, 5, 1, [[block] for block in row_blocks] + [[identity]], sparse=True
        ),
        "column_pin": block_matrix(
            field,
            5,
            1,
            [[block] for block in column_blocks] + [[identity]],
            sparse=True,
        ),
    }


def build_prime_packet(prime: int, keep_matrices: bool = False) -> dict:
    compressed = build_compressed_packet(prime, keep_matrices=True)
    split = build_split_packet(prime, keep_matrices=True)
    field = compressed["field"]
    graphs = observed_graphs(prime, compressed)
    zero_seed = block_matrix(
        field,
        2,
        1,
        [
            [zero_matrix(field, 512, 128, sparse=True)],
            [identity_matrix(field, 128, sparse=True)],
        ],
        sparse=True,
    )
    rows = {}
    corrected_graphs = {}
    for name, graph in graphs.items():
        corrected_graph = compressed["corrected"] * graph
        corrected_graphs[name] = corrected_graph
        joined_zero = block_matrix(
            field, 1, 2, [[corrected_graph, zero_seed]], sparse=True
        )
        rows[name] = {
            "observed_graph_rank": int(graph.rank()),
            "observed_clifford_trace_rank": int(
                (compressed["gamma_full"] * graph).rank()
            ),
            "removed_trace_rank": int((graph - corrected_graph).rank()),
            "corrected_graph_rank": int(corrected_graph.rank()),
            "corrected_zero_seed_join_rank": int(joined_zero.rank()),
            "corrected_zero_seed_intersection_rank": int(256 - joined_zero.rank()),
            "corrected_zero_seed_difference_rank": int(
                (corrected_graph - zero_seed).rank()
            ),
            "incoming_rank": int((split["incoming"] * corrected_graph).rank()),
            "outgoing_rank": int((split["outgoing"] * corrected_graph).rank()),
            "fast_rank": int((compressed["fast"] * corrected_graph).rank()),
            "slow_rank": int((compressed["slow"] * corrected_graph).rank()),
            "fast_incoming_rank": int(
                (compressed["fast"] * split["incoming"] * corrected_graph).rank()
            ),
            "fast_outgoing_rank": int(
                (compressed["fast"] * split["outgoing"] * corrected_graph).rank()
            ),
            "slow_incoming_rank": int(
                (compressed["slow"] * split["incoming"] * corrected_graph).rank()
            ),
            "slow_outgoing_rank": int(
                (compressed["slow"] * split["outgoing"] * corrected_graph).rank()
            ),
            "frozen_action_residual_rank": int(
                (compressed["compressed"] * corrected_graph).rank()
            ),
        }
    common = corrected_graphs["row_pin"]
    checks = {
        "both_graphs_descend_injectively": all(
            row["corrected_graph_rank"] == 128 for row in rows.values()
        ),
        "correction_removes_nonzero_trace": all(
            row["removed_trace_rank"] == 128 for row in rows.values()
        ),
        "pin_candidates_collapse_after_correction": common
        == corrected_graphs["column_pin"],
        "corrected_graph_differs_from_zero_seed": all(
            row["corrected_zero_seed_intersection_rank"] == 0
            and row["corrected_zero_seed_join_rank"] == 256
            for row in rows.values()
        ),
        "all_four_spectral_sign_blocks_are_met": all(
            row[key] > 0
            for row in rows.values()
            for key in (
                "fast_incoming_rank",
                "fast_outgoing_rank",
                "slow_incoming_rank",
                "slow_outgoing_rank",
            )
        ),
        "frozen_action_does_not_annihilate_graph": all(
            row["frozen_action_residual_rank"] == 128 for row in rows.values()
        ),
    }
    if not all(checks.values()):
        raise AssertionError({"prime": prime, "checks": checks, "rows": rows})
    packet = {"prime": prime, "rows": rows, "checks": checks}
    if keep_matrices:
        packet.update(
            {
                "field": field,
                "compressed": compressed,
                "split": split,
                "corrected_graph": common,
                "zero_seed": zero_seed,
            }
        )
    return packet


def public_packet(packet: dict) -> dict:
    return {key: value for key, value in packet.items() if key not in {
        "field", "compressed", "split", "corrected_graph", "zero_seed"
    }}


def build() -> dict:
    historical = strict("lab/process/selected-k77-moving-varpi-stationary-intersection.json")
    unrestricted = strict("lab/process/selected-k77-unrestricted-four-field-euler-image.json")
    k616 = strict("lab/process/k616-k77-unsplit-rank-one-transport-obstruction.json")
    assert historical["candidates"]["row_pin"]["nullity"] == 128
    assert historical["candidates"]["column_pin"]["nullity"] == 128
    assert historical["tautological_family"]["both_nonzero"] is True
    assert unrestricted["bounded_route_action_owned"] is False
    assert k616["transport_theorem"]["moving_nonlinear_action_coupling_covered"] is False
    packets = [public_packet(build_prime_packet(prime)) for prime in PRIMES]
    assert packets[0]["rows"] == packets[1]["rows"]
    rows = packets[0]["rows"]
    return {
        "schema_version": "1.0",
        "result_id": "K617-K77-MOVING-VARPI-CORRECTED-CARRIER-DESCENT",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact descent of the historical displayed-southeast-zero moving-varpi Omega0-to-gamma-trace stationary graph through the current observed slots and K438 corrected carrier, compared with K614's zero-form seed and K438/K439 frozen spectral split.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "historical_input": "repository-constructed displayed-southeast-zero moving-varpi algebraic kernel graph on both certified nonzero bosonic stationary branches",
            "observation": "K435 coordinate observation to slots 0,7,8,9 and Omega0",
            "constraint": "K438 corrected Clifford projector on the observed H640 carrier",
            "frozen_action": "K438 compressed normal symbol A, which is not the historical moving-varpi algebraic operator",
            "result": "moving-varpi corrected-carrier descent MAP-TYPE=historical-kernel-to-current-carrier comparison",
            "target": "a genuinely action-owned moving nonlinear corrected-carrier background and mixed-Hessian/Riesz packet",
        },
        "cross_characteristic_packets": packets,
        "cross_characteristic_rows": rows,
        "descent_theorem": {
            "historical_graph_nullity": 128,
            "both_nonzero_bosonic_branches_covered_historically": True,
            "both_pin_candidates_descend_injectively": True,
            "pin_candidates_become_identical_after_correction": True,
            "corrected_graph_rank": 128,
            "corrected_graph_equals_K614_zero_seed": False,
            "corrected_graph_intersection_K614_zero_seed_rank": 0,
            "corrected_graph_join_K614_zero_seed_rank": 256,
            "all_four_frozen_spectral_sign_blocks_met": True,
            "frozen_action_residual_rank": 128,
            "stationary_for_frozen_K438_action": False,
        },
        "ownership_reconciliation": {
            "historical_graph_is_source_selected": False,
            "historical_graph_is_repository_constructed": True,
            "bounded_graph_route_action_owned_by_unrestricted_four_field_action": False,
            "corrected_descent_reverses_prior_action_ownership_kill": False,
            "moving_differential_BV_Green_domain_constructed": False,
            "mixed_hessian_Riesz_packet_constructed": False,
        },
        "decision": {
            "K615_frozen_stationarity_obstruction_retracted": False,
            "K616_unsplit_packet_obstruction_retracted": False,
            "moving_graph_has_nontrivial_corrected_descent": True,
            "moving_graph_revives_bounded_action_owned_route": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Classify the K438 polynomial action hull of the descended graph and its blockwise complement. Treat the action-derived vector split separately from ownership of a mixed-Hessian bilinear coupling, and preserve the earlier unrestricted-Euler route kill.",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Reuse the exact historical moving-varpi graph before inventing a new nonlinear background, but compose it with the current corrected carrier and prior action-ownership kill.",
            "retrieval_collision_result": "The August graph predates K438/K439; later work killed it as an action-owned bounded subsystem but did not test its corrected-carrier image.",
            "strongest_alternative": "Construct the unrestricted four-field southeast rival and full BV complex; that remains larger because the current test can first decide whether the old graph supplies any corrected input at all.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling nontrivial corrected descent a source-selected stationary solution or a revival of the already-killed bounded graph action.",
            "strongest_contrary_construction": "The two historical Pin graphs collapse to one corrected rank-128 image, but K438 acts injectively on it and the unrestricted action still owns the full nonnull Euler image.",
            "weakest_reproducibility_seam": "The descent is exact at both current good characteristics; its historical stationary premise remains tied to the separately certified displayed-southeast-zero algebraic operator.",
        },
        "claim_ceiling": "Exact cross-characteristic descent of the historical moving-varpi algebraic graph into the current corrected carrier. Both Pin candidates collapse to the same rank-128 corrected image, disjoint from K614's zero-form image, and meet every K438/K439 spectral-sign block. K438's frozen action has rank-128 residual on that image, so the graph is not stationary for the frozen model. The newer carrier does not reverse the prior unrestricted-action ownership kill or construct a moving differential BV/Green domain or mixed-Hessian/Riesz packet. No source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion moves.",
    }


def validate(payload: dict) -> None:
    d = payload["descent_theorem"]
    o = payload["ownership_reconciliation"]
    q = payload["decision"]
    assert len(payload["cross_characteristic_packets"]) == 2
    assert d["both_pin_candidates_descend_injectively"]
    assert d["pin_candidates_become_identical_after_correction"]
    assert d["corrected_graph_rank"] == 128
    assert d["corrected_graph_intersection_K614_zero_seed_rank"] == 0
    assert d["corrected_graph_join_K614_zero_seed_rank"] == 256
    assert d["frozen_action_residual_rank"] == 128
    assert not d["stationary_for_frozen_K438_action"]
    assert not o["bounded_graph_route_action_owned_by_unrestricted_four_field_action"]
    assert not o["corrected_descent_reverses_prior_action_ownership_kill"]
    assert not o["mixed_hessian_Riesz_packet_constructed"]
    assert q["moving_graph_has_nontrivial_corrected_descent"]
    assert not q["moving_graph_revives_bounded_action_owned_route"]
    assert not q["selected_source_action_rejected"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
