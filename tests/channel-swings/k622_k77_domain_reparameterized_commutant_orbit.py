#!/usr/bin/env sage-python
"""K622 domain-reparameterized orbit of the K614 and K617 seeds."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sage.all import block_matrix

from k435_k77_full_h640_observed_map import PRIMES, canonical_digest
from k621_k77_full_action_commutant_seed_adapter_obstruction import build_prime_gate


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k622-k77-domain-reparameterized-commutant-orbit.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def build_prime_orbit(prime: int) -> dict:
    packet = build_prime_gate(prime, keep_matrices=True)
    field = packet["field"]
    projectors = packet["projectors"]
    zero_seed = packet["zero_seed"]
    graph = packet["graph"]

    zero_slow_out = (projectors["slow_outgoing"] * zero_seed).row_space().basis_matrix()
    zero_slow_in = (projectors["slow_incoming"] * zero_seed).row_space().basis_matrix()
    graph_slow_out = (projectors["slow_outgoing"] * graph).row_space().basis_matrix()
    graph_slow_in = (projectors["slow_incoming"] * graph).row_space().basis_matrix()
    zero_slow_pair = block_matrix(field, 2, 1, [[zero_slow_out], [zero_slow_in]], sparse=False)
    graph_slow_pair = block_matrix(field, 2, 1, [[graph_slow_out], [graph_slow_in]], sparse=False)
    domain_map = zero_slow_pair.inverse() * graph_slow_pair

    rows = {}
    for name, projector in projectors.items():
        moved_zero = projector * zero_seed * domain_map
        graph_block = projector * graph
        joined = block_matrix(field, 2, 1, [[moved_zero], [graph_block]], sparse=True)
        rank = int(graph_block.rank())
        joined_rank = int(joined.rank())
        block_dimension = int(projector.rank())
        rows[name] = {
            "eigenspace_rank": block_dimension,
            "moved_zero_seed_block_rank": int(moved_zero.rank()),
            "graph_seed_block_rank": rank,
            "row_space_join_rank_after_domain_map": joined_rank,
            "row_spaces_equal_after_domain_map": joined_rank == rank,
            "invertible_block_transport_exists": joined_rank == rank,
            "block_transport_solution_affine_dimension": block_dimension * (block_dimension - rank),
        }

    checks = {
        "both_slow_pairs_are_direct_decompositions": (
            int(zero_slow_pair.rank()) == int(graph_slow_pair.rank()) == 128
        ),
        "domain_reparameterization_is_invertible": int(domain_map.rank()) == 128,
        "domain_reparameterization_matches_both_slow_rows": (
            zero_slow_pair * domain_map == graph_slow_pair
        ),
        "all_block_row_spaces_match_after_reparameterization": all(
            row["row_spaces_equal_after_domain_map"] for row in rows.values()
        ),
        "invertible_commutant_transport_exists_after_reparameterization": all(
            row["invertible_block_transport_exists"] for row in rows.values()
        ),
    }
    if not all(checks.values()):
        raise AssertionError({"prime": prime, "rows": rows, "checks": checks})
    return {
        "prime": prime,
        "domain_reparameterization_rank": int(domain_map.rank()),
        "domain_reparameterization_sha256": canonical_digest(domain_map),
        "slow_pair_ranks": {"zero_seed": int(zero_slow_pair.rank()), "moving_graph": int(graph_slow_pair.rank())},
        "eigenblock_rows": rows,
        "checks": checks,
    }


def build() -> dict:
    k620 = strict("lab/process/k620-k77-action-functional-calculus-selection-obstruction.json")
    k621 = strict("lab/process/k621-k77-full-action-commutant-seed-adapter-obstruction.json")
    assert not k620["seed_adapter_theorem"]["arbitrary_commutant_or_domain_endomorphism_tested"]
    assert not k621["commutant_theorem"]["fixed_domain_commuting_adapter_exists"]
    packets = [build_prime_orbit(prime) for prime in PRIMES]
    fingerprints = [
        {
            "slow_pair_ranks": packet["slow_pair_ranks"],
            "rows": packet["eigenblock_rows"],
            "checks": packet["checks"],
        }
        for packet in packets
    ]
    assert fingerprints[0] == fingerprints[1]
    rows = packets[0]["eigenblock_rows"]
    return {
        "schema_version": "1.0",
        "result_id": "K622-K77-DOMAIN-REPARAMETERIZED-COMMUTANT-ORBIT",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact orbit test allowing one invertible reparameterization of the Omega0(S)_128 seed domain together with an arbitrary invertible endomorphism in the full K438 action commutant.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "action": "K438 corrected frozen normal symbol A and its complete four-block commutant",
            "domain": "the shared abstract Omega0(S)_128 coordinate domain of K614 J0 and K617 X",
            "domain_adapter": "an arbitrary invertible R in GL(128), not source-selected or action-owned",
            "carrier_adapter": "an arbitrary invertible T in End_A(E), block diagonal on the four action eigenspaces",
            "result": "domain-reparameterized commutant orbit theorem MAP-TYPE=paired-subspace equivalence",
            "target": "existence versus ownership of T J0 R = X",
        },
        "cross_characteristic_packets": packets,
        "eigenblock_fingerprint": rows,
        "orbit_theorem": {
            "zero_seed_slow_row_pair_is_direct_sum": True,
            "moving_seed_slow_row_pair_is_direct_sum": True,
            "one_invertible_domain_reparameterization_matches_both_slow_rows": True,
            "fast_rows_remain_full_after_reparameterization": True,
            "invertible_commutant_and_domain_orbit_equivalence_exists": True,
            "fixed_domain_commutant_adapter_exists": False,
            "block_transport_affine_freedom_for_constructed_domain_map": 24576,
            "orbit_equivalence_selects_unique_adapter": False,
        },
        "ownership_reconciliation": {
            "K621_fixed_domain_obstruction_retracted": False,
            "domain_reparameterization_is_source_selected": False,
            "commutant_transport_is_action_selected": False,
            "orbit_equivalence_identifies_seed_constructions": False,
            "pairing_or_Green_domain_preservation_proved": False,
            "mixed_hessian_or_stationary_background_constructed": False,
        },
        "decision": {
            "K619_common_module_retracted": False,
            "full_abstract_commutant_orbit_is_nonempty": True,
            "actual_K596_K598_packet_released": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "An actual revival now requires an independently action-owned source-domain endomorphism or mixed-Hessian odd adapter on a nonzero stationary moving background, plus proof that the chosen adapter preserves the K441 pairing and common BV/Green domain. Abstract GL(128) by End_A(E) orbit equivalence cannot select those data.",
        },
        "ledger_no_change_reason": "The positive orbit theorem uses arbitrary unowned changes of source coordinates and carrier blocks; it neither constructs nor rejects the source action, a stationary solution, a gauge-reduced class, an observation map, or physical cohomology. SC-ACT-01/02 and SC-CHI-01/51 and every v0.263 ledger row remain unchanged.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "K621's slow-row obstruction might be only a fixed-parameterization artifact; classify the ordered slow subspace pairs before broadening the no-go.",
            "retrieval_collision_result": "No predecessor combines an arbitrary source-domain automorphism with the full K438 commutant for the K614/K617 seed pair.",
            "strongest_alternative": "A pairing-preserving or action-derived adapter is physically stronger but cannot be inferred from abstract orbit equivalence and remains the next owned input.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling existence of arbitrary GL(128) and block-GL transports an action-selected mixed Hessian, a canonical seed identification, or a common analytic domain.",
            "strongest_contrary_construction": "K621 proves no carrier commutant map works while the source coordinates are fixed; the positive result requires changing that domain simultaneously.",
            "weakest_reproducibility_seam": "The constructed reparameterization depends on deterministic row bases over two good characteristics; only existence and rank fingerprints, not a characteristic-zero canonical matrix, are claimed.",
        },
        "claim_ceiling": "Exact cross-characteristic orbit equivalence after adjoining an arbitrary invertible Omega0(S)_128 domain reparameterization: both seeds define ordered complementary rank-64 slow row-space pairs, and one domain map makes every action-eigenblock row space agree, after which invertible block transports exist. The construction is highly nonunique and neither source-selected nor action-owned; it proves no pairing, Green-domain, stationarity, BV/KT, source, ledger, canon, paper, public, novelty, prediction, confirmation, or physical conclusion.",
    }


def validate(payload: dict) -> None:
    theorem = payload["orbit_theorem"]
    ownership = payload["ownership_reconciliation"]
    decision = payload["decision"]
    assert len(payload["cross_characteristic_packets"]) == 2
    assert theorem["one_invertible_domain_reparameterization_matches_both_slow_rows"]
    assert theorem["invertible_commutant_and_domain_orbit_equivalence_exists"]
    assert not theorem["fixed_domain_commutant_adapter_exists"]
    assert theorem["block_transport_affine_freedom_for_constructed_domain_map"] == 24576
    assert not theorem["orbit_equivalence_selects_unique_adapter"]
    assert not ownership["domain_reparameterization_is_source_selected"]
    assert not ownership["pairing_or_Green_domain_preservation_proved"]
    assert decision["full_abstract_commutant_orbit_is_nonempty"]
    assert not decision["actual_K596_K598_packet_released"]


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
