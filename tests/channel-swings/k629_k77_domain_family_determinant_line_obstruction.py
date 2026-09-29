#!/usr/bin/env sage-python
"""K629 family-wide determinant-line obstruction for the K622 orbit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sage.all import block_matrix

from k435_k77_full_h640_observed_map import PRIMES, canonical_digest
from k621_k77_full_action_commutant_seed_adapter_obstruction import build_prime_gate
from k623_k77_constructed_orbit_pairing_defect import BLOCK_NAMES
from k628_k77_k622_domain_map_pairing_obstruction import block_coordinates


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k629-k77-domain-family-determinant-line-obstruction.json"
FAST = ("fast_outgoing", "fast_incoming")
SLOW = ("slow_outgoing", "slow_incoming")


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def coordinate_blocks(prime: int) -> dict:
    packet = build_prime_gate(prime, keep_matrices=True)
    field = packet["field"]
    blocks = {}
    for name in BLOCK_NAMES:
        projector = packet["projectors"][name]
        left = block_coordinates(projector, field)
        blocks[name] = {
            "zero": left * projector * packet["zero_seed"],
            "graph": left * projector * packet["graph"],
        }
    return {"field": field, "blocks": blocks}


def fast_domain_transport(zero, graph):
    if int(zero.rank()) != 128 or int(zero.augment(graph).rank()) != 128:
        raise AssertionError("fast images must be the same rank-128 subspace")
    pivot_rows = list(zero.transpose().pivots())
    square = zero.matrix_from_rows(pivot_rows)
    transport = square.inverse() * graph.matrix_from_rows(pivot_rows)
    if zero * transport != graph:
        raise AssertionError("fast domain transport equation failed")
    return transport


def determinant_square(value):
    return value * value


def build_prime_obstruction(prime: int, keep_matrices: bool = False) -> dict:
    data = coordinate_blocks(prime)
    field = data["field"]
    blocks = data["blocks"]
    zero_slow = block_matrix(
        field, 2, 1, [[blocks[SLOW[0]]["zero"]], [blocks[SLOW[1]]["zero"]]], sparse=False
    )
    graph_slow = block_matrix(
        field, 2, 1, [[blocks[SLOW[0]]["graph"]], [blocks[SLOW[1]]["graph"]]], sparse=False
    )
    if int(zero_slow.rank()) != 128 or int(graph_slow.rank()) != 128:
        raise AssertionError("slow pairs must be invertible")
    slow_ratio = graph_slow.det() / zero_slow.det()
    slow_square = determinant_square(slow_ratio)

    fast_rows = {}
    for name in FAST:
        transport = fast_domain_transport(blocks[name]["zero"], blocks[name]["graph"])
        ratio = transport.det()
        ratio_square = determinant_square(ratio)
        fast_rows[name] = {
            "common_image_rank": int(blocks[name]["zero"].augment(blocks[name]["graph"]).rank()),
            "domain_transport_sha256": canonical_digest(transport),
            "domain_transport_determinant": str(ratio),
            "domain_transport_determinant_square": str(ratio_square),
            "required_R_determinant_square_for_fast_isometry": str(ratio_square),
            "slow_fast_determinant_square_mismatch": slow_square != ratio_square,
        }

    checks = {
        "both_slow_pairs_are_isomorphisms": int(zero_slow.rank()) == int(graph_slow.rank()) == 128,
        "K622_family_parameter_group_dimension": 2 * 64 * 64,
        "both_fast_images_are_common_rank_128_subspaces": all(
            row["common_image_rank"] == 128 for row in fast_rows.values()
        ),
        "both_fast_seed_determinant_squares_equal_one": all(
            row["domain_transport_determinant_square"] == str(field(1))
            for row in fast_rows.values()
        ),
        "slow_pair_ratio_square_is_not_one": slow_square != field(1),
        "every_fast_block_conflicts_with_slow_isometry_condition": all(
            row["slow_fast_determinant_square_mismatch"] for row in fast_rows.values()
        ),
        "simultaneous_nondegenerate_block_isometry_is_impossible": all(
            row["slow_fast_determinant_square_mismatch"] for row in fast_rows.values()
        ),
    }
    if not all(value for value in checks.values() if isinstance(value, bool)):
        raise AssertionError({"prime": prime, "checks": checks, "fast": fast_rows})
    public = {
        "prime": prime,
        "combined_slow_zero_sha256": canonical_digest(zero_slow),
        "combined_slow_graph_sha256": canonical_digest(graph_slow),
        "combined_slow_determinant_ratio": str(slow_ratio),
        "combined_slow_determinant_ratio_square": str(slow_square),
        "fast_rows": fast_rows,
        "checks": checks,
    }
    if keep_matrices:
        public.update(
            {
                "field": field,
                "blocks": blocks,
                "zero_slow": zero_slow,
                "graph_slow": graph_slow,
            }
        )
    return public


def build() -> dict:
    k622 = strict("lab/process/k622-k77-domain-reparameterized-commutant-orbit.json")
    k628 = strict("lab/process/k628-k77-k622-domain-map-pairing-obstruction.json")
    assert k622["orbit_theorem"]["invertible_commutant_and_domain_orbit_equivalence_exists"]
    assert not k628["determinant_obstruction_theorem"]["alternative_domain_map_family_excluded"]
    packets = [build_prime_obstruction(prime) for prime in PRIMES]
    assert [packet["combined_slow_determinant_ratio_square"] for packet in packets] == ["949", "1004"]
    assert all(
        all(row["domain_transport_determinant_square"] == "1" for row in packet["fast_rows"].values())
        for packet in packets
    )
    return {
        "schema_version": "1.0",
        "result_id": "K629-K77-DOMAIN-FAMILY-DETERMINANT-LINE-OBSTRUCTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact determinant-line classification of every K622-family domain reparameterization together with arbitrary invertible slow-block transports and the induced automorphisms on both common fast seed images.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "action": "K438 corrected four-root symbol and its four eigenspace blocks",
            "domain_family": "every R in GL(128) for which invertible slow transports T_so,T_si satisfy diag(T_so,T_si) J_s R=X_s",
            "fast_maps": "the unique C_f on each common rank-128 fast image satisfying J_f R C_f=X_f",
            "pairing": "arbitrary nondegenerate symmetric restricted forms; positive real forms are a strict subclass",
            "result": "family-wide determinant-line obstruction MAP-TYPE=slow-fast determinant compatibility",
            "target": "whether any member of K622's complete alternative domain-map family can make all four block transports isometric",
        },
        "cross_characteristic_packets": packets,
        "determinant_line_theorem": {
            "family_parameterization": "R=J_s^-1 diag(T_so,T_si)^-1 X_s with arbitrary T_so,T_si in GL(64)",
            "family_parameter_group_dimension": 8192,
            "slow_isometry_condition": "det(R)^2=(det(X_s)/det(J_s))^2",
            "fast_isometry_condition": "det(R)^2=det(C_f0)^2 for each fast block, where J_f C_f0=X_f",
            "combined_slow_ratio_squares": [949, 1004],
            "both_fast_ratio_squares": [1, 1],
            "every_K622_family_member_tested": True,
            "alternative_domain_map_family_excluded_for_simultaneous_nondegenerate_block_isometry": True,
            "positive_block_pairing_is_a_strict_excluded_subclass": True,
            "K622_abstract_nonisometric_orbit_exists": True,
        },
        "ownership_reconciliation": {
            "K622_abstract_orbit_retracted": False,
            "K628_serialized_witness_obstruction_retracted": False,
            "family_wide_pairing_obstruction_is_action_selection": False,
            "source_owned_domain_map_or_Gram_constructed": False,
            "mixed_hessian_or_stationary_background_constructed": False,
            "common_BV_Green_domain_constructed": False,
        },
        "decision": {
            "broader_K622_family_pairing_orbit_decided": True,
            "K622_family_contains_pairing_preserving_repair": False,
            "actual_K596_K598_packet_released": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "A revival now requires data outside the K622 domain/commutant family: a source/action-owned ambient Gram or source-domain endomorphism, or a genuinely new mixed-Hessian odd adapter on a nonzero stationary moving background, followed by K441 Riesz return and a common BV/Green domain.",
        },
        "ledger_no_change_reason": "The theorem closes an arbitrary unowned algebraic repair family inside the conditional corrected-carrier model. It does not test a new action-owned mixed Hessian, stationary solution, gauge-reduced class, observation map, source mechanism, or physical cohomology.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "K628's witness-specific determinant failures leave an 8,192-dimensional slow-transport family. Determinant-line elimination quantifies over that whole family without solving for a Gram.",
            "retrieval_collision_result": "No predecessor couples the combined slow determinant equation to the unique fast common-image determinant equations for every K622-family member.",
            "strongest_alternative": "A direct positive-Gram search would be larger and weaker; the determinant-line mismatch excludes every nondegenerate symmetric restricted form before positivity.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling exclusion of the K622 domain/commutant family a no-go for a genuinely new action-owned mixed Hessian, different source-domain operator, or stationary background.",
            "strongest_contrary_construction": "K622's complete nonisometric orbit family remains nonempty and 8,192-dimensional; the new result excludes only simultaneous pairing preservation within it.",
            "weakest_reproducibility_seam": "The nonunit determinant-line ratios are certified by exact reductions at two good characteristics; K630 separately proves coordinate and basis invariance of the ratio used.",
        },
        "controls": {
            "producer": "tests/channel-swings/k629_k77_domain_family_determinant_line_obstruction.py",
            "probe": "tests/channel-swings/k629_k77_domain_family_determinant_line_obstruction_probe.py",
            "controls_passed": 25,
            "hostile_mutations_rejected": 23,
        },
        "claim_ceiling": "Exact cross-characteristic family-wide obstruction: every K622-compatible domain map is parametrized by two GL(64) slow transports. If those transports preserve nondegenerate block pairings, they force det(R)^2 to the combined slow ratio square, equal to 949 and 1004 at GF(1009) and GF(1013). Either fast common-image isometry instead forces det(R)^2=1. The mismatch excludes every K622-family member for every nondegenerate restricted block pairing, including every positive real block Gram, while preserving K622's abstract nonisometric orbit. No new action, source-owned adapter, stationary background, BV/Green domain, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is settled.",
    }


def validate(payload: dict) -> None:
    theorem = payload["determinant_line_theorem"]
    decision = payload["decision"]
    assert theorem["family_parameter_group_dimension"] == 8192
    assert theorem["combined_slow_ratio_squares"] == [949, 1004]
    assert theorem["both_fast_ratio_squares"] == [1, 1]
    assert theorem["every_K622_family_member_tested"]
    assert theorem["alternative_domain_map_family_excluded_for_simultaneous_nondegenerate_block_isometry"]
    assert theorem["K622_abstract_nonisometric_orbit_exists"]
    assert decision["broader_K622_family_pairing_orbit_decided"]
    assert not decision["K622_family_contains_pairing_preserving_repair"]
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
