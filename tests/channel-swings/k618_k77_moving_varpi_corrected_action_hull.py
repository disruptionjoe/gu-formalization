#!/usr/bin/env sage-python
"""K618 action-polynomial hull and bounded-route revival gate for K617."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sage.all import block_matrix

from k435_k77_full_h640_observed_map import PRIMES
from k617_k77_moving_varpi_corrected_carrier_descent import build_prime_packet


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k618-k77-moving-varpi-corrected-action-hull.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def joined_rank(field, columns) -> int:
    return int(block_matrix(field, 1, len(columns), [columns], sparse=True).rank())


def build_prime_hull(prime: int) -> dict:
    packet = build_prime_packet(prime, keep_matrices=True)
    field = packet["field"]
    compressed = packet["compressed"]
    split = packet["split"]
    graph = packet["corrected_graph"]
    action = compressed["compressed"]
    powers = []
    current = graph
    krylov_ranks = []
    for exponent in range(5):
        powers.append(current)
        krylov_ranks.append(joined_rank(field, powers))
        current = action * current

    blocks = {
        "fast_outgoing": compressed["fast"] * split["outgoing"] * graph,
        "fast_incoming": compressed["fast"] * split["incoming"] * graph,
        "slow_outgoing": compressed["slow"] * split["outgoing"] * graph,
        "slow_incoming": compressed["slow"] * split["incoming"] * graph,
    }
    block_ranks = {name: int(value.rank()) for name, value in blocks.items()}
    spectral_hull_rank = joined_rank(field, list(blocks.values()))
    fast_outgoing_total = int((compressed["fast"] * split["outgoing"]).rank())
    fast_incoming_total = int((compressed["fast"] * split["incoming"]).rank())
    slow_outgoing_total = int((compressed["slow"] * split["outgoing"]).rank())
    slow_incoming_total = int((compressed["slow"] * split["incoming"]).rank())
    totals = {
        "fast_outgoing": fast_outgoing_total,
        "fast_incoming": fast_incoming_total,
        "slow_outgoing": slow_outgoing_total,
        "slow_incoming": slow_incoming_total,
    }
    missing = {name: totals[name] - block_ranks[name] for name in totals}
    checks = {
        "krylov_stabilizes_at_384": krylov_ranks == [128, 256, 384, 384, 384],
        "spectral_and_krylov_hulls_agree": spectral_hull_rank == krylov_ranks[-1] == 384,
        "slow_blocks_are_exhausted": missing["slow_outgoing"] == missing["slow_incoming"] == 0,
        "fast_blocks_each_miss_64": missing["fast_outgoing"] == missing["fast_incoming"] == 64,
        "corrected_carrier_not_exhausted": 512 - spectral_hull_rank == 128,
        "graph_not_action_invariant": krylov_ranks[1] > krylov_ranks[0],
    }
    if not all(checks.values()):
        raise AssertionError({
            "prime": prime,
            "checks": checks,
            "krylov_ranks": krylov_ranks,
            "block_ranks": block_ranks,
            "totals": totals,
            "missing": missing,
        })
    return {
        "prime": prime,
        "krylov_ranks_A0_through_A4": krylov_ranks,
        "block_ranks": block_ranks,
        "block_total_ranks": totals,
        "missing_block_ranks": missing,
        "spectral_hull_rank": spectral_hull_rank,
        "corrected_carrier_rank": 512,
        "corrected_complement_rank": 128,
        "checks": checks,
    }


def build() -> dict:
    k617 = strict("lab/process/k617-k77-moving-varpi-corrected-carrier-descent.json")
    old_hull = strict("lab/process/selected-k77-fixed-common-receiver-hull.json")
    unrestricted = strict("lab/process/selected-k77-unrestricted-four-field-euler-image.json")
    k439 = strict("lab/process/k439-k77-compatible-corrected-boundary-split.json")
    k616 = strict("lab/process/k616-k77-unsplit-rank-one-transport-obstruction.json")
    assert k617["decision"]["moving_graph_has_nontrivial_corrected_descent"] is True
    assert old_hull["pin_join_rank"] == 384
    assert unrestricted["bounded_route_action_owned"] is False
    assert "13823 A-13248 A^3" in k439["gu_typed_objects"]["sign_involution"]
    assert k616["matching_half_repair"]["conditional_K596_packet_remains_live"] is True
    packets = [build_prime_hull(prime) for prime in PRIMES]
    fingerprints = [
        {
            "krylov": row["krylov_ranks_A0_through_A4"],
            "blocks": row["block_ranks"],
            "totals": row["block_total_ranks"],
            "missing": row["missing_block_ranks"],
            "hull": row["spectral_hull_rank"],
        }
        for row in packets
    ]
    assert fingerprints[0] == fingerprints[1]
    return {
        "schema_version": "1.0",
        "result_id": "K618-K77-MOVING-VARPI-CORRECTED-ACTION-HULL",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact K438 polynomial-action hull generated by K617's common corrected moving-varpi graph, including the four K438/K439 spectral-sign components, complement ranks, and reconciliation with the historical rank-384 receiver hull and unrestricted four-field Euler-image route kill.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "seed": "K617 common rank-128 corrected image of both historical moving-varpi Pin graphs",
            "action": "K438 compressed frozen normal symbol A with roots plus/minus 1 and plus/minus 1/24",
            "projectors": "K438 fast/slow and K439 incoming/outgoing projectors, all polynomial in A on the corrected carrier",
            "hull": "span{X,AX,A^2X,A^3X}, equal to the direct sum of the four action-polynomial spectral images of X",
            "historical_comparator": "v0.161 fixed common fermion equation receiver hull inside the ambient 1920-dimensional four-field equation space",
            "result": "corrected graph action-module and revival gate MAP-TYPE=polynomial-module closure",
        },
        "cross_characteristic_packets": packets,
        "cross_characteristic_fingerprint": fingerprints[0],
        "action_hull_theorem": {
            "krylov_ranks_A0_through_A4": [128, 256, 384, 384, 384],
            "minimal_action_hull_rank": 384,
            "action_hull_is_full_corrected_carrier": False,
            "corrected_carrier_complement_rank": 128,
            "fast_outgoing_image_rank": 128,
            "fast_incoming_image_rank": 128,
            "slow_outgoing_image_rank": 64,
            "slow_incoming_image_rank": 64,
            "fast_outgoing_missing_rank": 64,
            "fast_incoming_missing_rank": 64,
            "slow_outgoing_missing_rank": 0,
            "slow_incoming_missing_rank": 0,
            "K617_graph_is_A_invariant": False,
        },
        "ownership_and_typing": {
            "spectral_vector_components_are_action_derived": True,
            "reason": "K439's sign projector and K438's fast/slow projectors are exact polynomials in the action symbol A.",
            "action_derived_vector_split_owns_mixed_hessian_coupling": False,
            "matching_half_bilinear_packet_constructed": False,
            "historical_receiver_hull_rank": 384,
            "current_corrected_action_hull_rank": 384,
            "equal_rank_identifies_historical_and_current_hulls": False,
            "historical_and_current_ambient_types": "ambient four-field equation receiver rank 1920 versus corrected observed boundary carrier rank 512",
            "unrestricted_four_field_Euler_image_rank_nonnull": 1920,
            "bounded_route_action_owned": False,
        },
        "revival_gate": {
            "corrected_carrier_supplies_nontrivial_diagnostic_module": True,
            "corrected_carrier_revives_historical_bounded_graph_as_action_subsystem": False,
            "K616_vector_projection_ownership_narrowed": True,
            "K616_core_unsplit_packet_obstruction_retracted": False,
            "remaining_exact_missing_input": "An action mixed Hessian or higher odd derivative that owns a matching-half bilinear coupling on a nonzero stationary moving background, together with the moving differential BV/Green domain.",
        },
        "decision": {
            "K617_nontrivial_descent_retracted": False,
            "K615_frozen_zero_form_obstruction_retracted": False,
            "prior_unrestricted_Euler_route_kill_retracted": False,
            "rank384_coincidence_promoted_to_identity": False,
            "actual_K596_K598_packet_released": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Return to the unrestricted four-field operator or construct an independently action-owned mixed-Hessian odd coupling and moving BV/Green domain. Do not use the rank-384 coincidence, action-polynomial vector split, or post-variation projection to revive the bounded graph route.",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Compute the cheapest exact action-module closure after K617 before attempting a moving differential domain or mistaking equal ranks for an adapter.",
            "retrieval_collision_result": "v0.161 owns a rank-384 ambient equation receiver; K617 creates a new corrected-boundary seed, but no predecessor compares their typing or computes its K438 Krylov hull.",
            "strongest_alternative": "The unrestricted four-field southeast rival remains the native successor if the corrected module does not establish pre-variation action ownership.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Identifying two rank-384 hulls in different ambient spaces or treating action-derived spectral vectors as an action-owned mixed-Hessian coupling.",
            "strongest_contrary_construction": "The K438 polynomial orbit is a genuine rank-384 corrected module and exhausts both slow blocks, but misses rank 64 in each fast sign and remains a post-composition diagnostic rather than the unrestricted action's selected subsystem.",
            "weakest_reproducibility_seam": "The module ranks are certified at two current good characteristics; no explicit characteristic-zero isomorphism to the historical GF(1000033) receiver is claimed or needed.",
        },
        "claim_ceiling": "Exact cross-characteristic classification of the K438 polynomial module generated by K617's descended graph. Its Krylov ranks are 128,256,384,384,384; it exhausts both slow sign blocks, occupies rank 128 of each rank-192 fast sign block, and leaves a rank-128 corrected complement. The spectral vector decomposition is action-derived because the projectors are polynomials in A, but this does not own a mixed-Hessian bilinear coupling. The rank-384 module is not identified with the historical rank-384 ambient receiver, and the prior unrestricted-action route kill remains in force. No actual K596/K598 packet, moving BV/Green domain, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion moves.",
    }


def validate(payload: dict) -> None:
    h = payload["action_hull_theorem"]
    o = payload["ownership_and_typing"]
    r = payload["revival_gate"]
    d = payload["decision"]
    assert h["krylov_ranks_A0_through_A4"] == [128, 256, 384, 384, 384]
    assert h["minimal_action_hull_rank"] == 384
    assert not h["action_hull_is_full_corrected_carrier"]
    assert h["corrected_carrier_complement_rank"] == 128
    assert [h[key] for key in ("fast_outgoing_missing_rank", "fast_incoming_missing_rank", "slow_outgoing_missing_rank", "slow_incoming_missing_rank")] == [64, 64, 0, 0]
    assert o["spectral_vector_components_are_action_derived"]
    assert not o["action_derived_vector_split_owns_mixed_hessian_coupling"]
    assert not o["equal_rank_identifies_historical_and_current_hulls"]
    assert not o["bounded_route_action_owned"]
    assert r["corrected_carrier_supplies_nontrivial_diagnostic_module"]
    assert not r["corrected_carrier_revives_historical_bounded_graph_as_action_subsystem"]
    assert not r["K616_core_unsplit_packet_obstruction_retracted"]
    assert not d["prior_unrestricted_Euler_route_kill_retracted"]
    assert not d["actual_K596_K598_packet_released"]
    assert not d["selected_source_action_rejected"]


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
