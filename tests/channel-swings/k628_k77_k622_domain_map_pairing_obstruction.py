#!/usr/bin/env sage-python
"""K628 pairing-independent determinant obstruction for K622's exact domain map."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sage.all import block_matrix

from k435_k77_full_h640_observed_map import PRIMES, canonical_digest
from k621_k77_full_action_commutant_seed_adapter_obstruction import build_prime_gate
from k623_k77_constructed_orbit_pairing_defect import BLOCK_NAMES
from k626_k77_ambient_pairing_embedding_gauge import coordinate_left_inverse


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k628-k77-k622-domain-map-pairing-obstruction.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def block_coordinates(projector, field):
    basis = projector.column_space().basis_matrix().transpose()
    return coordinate_left_inverse(basis, field)


def build_prime_obstruction(prime: int) -> dict:
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
    for name in BLOCK_NAMES:
        projector = projectors[name]
        left = block_coordinates(projector, field)
        moved_zero = left * projector * zero_seed * domain_map
        moving = left * projector * graph
        block_rank = int(projector.rank())
        seed_rank = int(moved_zero.rank())
        join_rank = int(moved_zero.augment(moving).rank())
        if seed_rank == 128:
            pivot_rows = list(moved_zero.transpose().pivots())
            square_zero = moved_zero.matrix_from_rows(pivot_rows)
            square_graph = moving.matrix_from_rows(pivot_rows)
            transport = square_zero.inverse() * square_graph
            transport_kind = "common-image induced automorphism"
            verified = moved_zero * transport == moving
        elif seed_rank == block_rank:
            pivot_columns = list(moved_zero.pivots())
            square_zero = moved_zero.matrix_from_columns(pivot_columns)
            square_graph = moving.matrix_from_columns(pivot_columns)
            transport = square_graph * square_zero.inverse()
            transport_kind = "full-block left transport"
            verified = transport * moved_zero == moving
        else:
            raise AssertionError({"prime": prime, "block": name, "rank": seed_rank})
        determinant = transport.det()
        determinant_square = determinant * determinant
        rows[name] = {
            "eigenspace_rank": block_rank,
            "seed_rank": seed_rank,
            "joined_image_rank": join_rank,
            "transport_kind": transport_kind,
            "transport_sha256": canonical_digest(transport),
            "transport_determinant": str(determinant),
            "transport_determinant_square": str(determinant_square),
            "determinant_is_plus_or_minus_one": determinant in (field(1), field(-1)),
            "nondegenerate_restricted_pairing_isometry_obstructed": determinant_square != field(1),
            "transport_equation_verified": bool(verified),
        }
    checks = {
        "domain_map_matches_K622_algorithm": canonical_digest(domain_map),
        "all_transport_equations_verified": all(row["transport_equation_verified"] for row in rows.values()),
        "both_fast_seed_images_coincide": all(
            rows[name]["joined_image_rank"] == 128 for name in ("fast_outgoing", "fast_incoming")
        ),
        "both_fast_blocks_obstruct_every_nondegenerate_restricted_pairing": all(
            rows[name]["nondegenerate_restricted_pairing_isometry_obstructed"]
            for name in ("fast_outgoing", "fast_incoming")
        ),
        "slow_outgoing_obstructs_every_nondegenerate_block_pairing": rows["slow_outgoing"]["nondegenerate_restricted_pairing_isometry_obstructed"],
        "slow_incoming_identity_transport_survives": not rows["slow_incoming"]["nondegenerate_restricted_pairing_isometry_obstructed"],
        "at_least_three_blocks_obstruct": sum(
            row["nondegenerate_restricted_pairing_isometry_obstructed"] for row in rows.values()
        ) >= 3,
    }
    if not all(value for key, value in checks.items() if key != "domain_map_matches_K622_algorithm"):
        raise AssertionError({"prime": prime, "rows": rows, "checks": checks})
    return {"prime": prime, "domain_map_rank": int(domain_map.rank()), "eigenblock_rows": rows, "checks": checks}


def build() -> dict:
    k622 = strict("lab/process/k622-k77-domain-reparameterized-commutant-orbit.json")
    k627 = strict("lab/process/k627-k77-block-gauge-positive-pairing-nonselection.json")
    assert k622["orbit_theorem"]["invertible_commutant_and_domain_orbit_equivalence_exists"]
    assert not k627["pairing_nonselection_theorem"]["K441_abstract_data_select_a_positive_gram"]
    packets = [build_prime_obstruction(prime) for prime in PRIMES]
    obstruction_fingerprints = [
        {
            name: {
                "eigenspace_rank": row["eigenspace_rank"],
                "seed_rank": row["seed_rank"],
                "joined_image_rank": row["joined_image_rank"],
                "determinant_is_plus_or_minus_one": row["determinant_is_plus_or_minus_one"],
                "nondegenerate_restricted_pairing_isometry_obstructed": row["nondegenerate_restricted_pairing_isometry_obstructed"],
            }
            for name, row in packet["eigenblock_rows"].items()
        }
        for packet in packets
    ]
    assert obstruction_fingerprints[0] == obstruction_fingerprints[1]
    return {
        "schema_version": "1.0",
        "result_id": "K628-K77-K622-DOMAIN-MAP-PAIRING-OBSTRUCTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact good-reduction determinant test of whether K622's serialized row-basis domain reparameterization can be implemented by block transports preserving any nondegenerate restricted symmetric pairing.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "action": "K438 corrected four-root symbol and its exact eigenspace projectors",
            "domain_map": "K622's deterministic row-basis R in GL(128) matching the ordered slow row-space decompositions",
            "block_transports": "the induced automorphisms on the common fast seed images and the unique transports on the full slow eigenspaces",
            "pairing": "an arbitrary nondegenerate symmetric restricted form; positive real forms are a strict subclass",
            "result": "serialized-map all-pairing obstruction MAP-TYPE=determinant isometry invariant",
            "target": "whether K622's exact stored orbit witness can preserve some alternative K441 ambient Gram",
        },
        "cross_characteristic_packets": packets,
        "determinant_obstruction_theorem": {
            "isometry_determinant_condition": "C^T H C=H with det(H) nonzero implies det(C)^2=1",
            "tested_good_characteristics": list(PRIMES),
            "obstructed_blocks": ["fast_outgoing", "fast_incoming", "slow_outgoing"],
            "unobstructed_blocks": ["slow_incoming"],
            "K622_serialized_domain_map_preserves_some_nondegenerate_block_pairing": False,
            "K622_abstract_nonisometric_orbit_exists": True,
            "every_K622_family_member_tested": False,
            "alternative_domain_map_family_excluded": False,
        },
        "ownership_reconciliation": {
            "K622_abstract_orbit_retracted": False,
            "K624_H_Sigma_obstruction_retracted": False,
            "K627_gauge_nonselection_retracted": False,
            "serialized_map_all_pairing_obstruction_is_action_selection": False,
            "source_owned_domain_map_or_Gram_constructed": False,
            "mixed_hessian_or_stationary_background_constructed": False,
            "common_BV_Green_domain_constructed": False,
        },
        "decision": {
            "K622_serialized_witness_can_be_repaired_by_only_changing_positive_Gram": False,
            "broader_K622_family_pairing_orbit_decided": False,
            "actual_K596_K598_packet_released": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Either solve the separate simultaneous isometry problem over K622's unselected domain-map family, or supply a source/action-owned ambient Gram or genuinely new mixed-Hessian adapter on a nonzero stationary background before any K596/K598 or physical-domain claim.",
        },
        "ledger_no_change_reason": "The determinant obstruction closes one arbitrary stored orbit witness and selects no replacement, action-owned domain endomorphism, stationary solution, physical quotient, observation map, or source-native pairing.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "K627 proves the gauge cannot select a Gram, but K626 leaves open whether K622's exact witness accidentally preserves some alternative one. Determinants test every nondegenerate restricted form without searching a 41,216-dimensional family.",
            "retrieval_collision_result": "K624 tests only H_Sigma and K626 only changes normalized fingerprints; no predecessor applies the determinant isometry invariant to K622's exact domain map.",
            "strongest_alternative": "Another member of K622's large domain-map family may have different induced determinants and remains a distinct nonlinear simultaneous-isometry problem.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Universalizing failure of K622's deterministic row-basis witness to every possible domain reparameterization or to a source/action-owned mixed Hessian.",
            "strongest_contrary_construction": "The slow-incoming transport is the identity at both primes and is unobstructed; the theorem needs only one obstructed block, while three are found.",
            "weakest_reproducibility_seam": "The conclusion uses exact reductions at two certified good characteristics. It excludes a characteristic-zero determinant of plus or minus one for these induced rational transports, but does not solve positivity or existence for a different domain-map family member.",
        },
        "claim_ceiling": "Exact cross-characteristic determinant obstruction for K622's serialized row-basis domain map. At GF(1009) and GF(1013), the induced fast-image transports and slow-outgoing full-block transport have determinant square unequal to one, so none can preserve any nondegenerate restricted symmetric pairing; changing only the ambient positive Gram cannot repair this stored witness. The slow-incoming identity transport survives. The result does not test every K622-family domain map and constructs no source/action-owned Gram, mixed Hessian, stationary background, common BV/Green domain, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }


def validate(payload: dict) -> None:
    theorem = payload["determinant_obstruction_theorem"]
    ownership = payload["ownership_reconciliation"]
    decision = payload["decision"]
    assert len(payload["cross_characteristic_packets"]) == 2
    assert theorem["obstructed_blocks"] == ["fast_outgoing", "fast_incoming", "slow_outgoing"]
    assert theorem["unobstructed_blocks"] == ["slow_incoming"]
    assert not theorem["K622_serialized_domain_map_preserves_some_nondegenerate_block_pairing"]
    assert theorem["K622_abstract_nonisometric_orbit_exists"]
    assert not theorem["every_K622_family_member_tested"]
    assert not ownership["K622_abstract_orbit_retracted"]
    assert not decision["broader_K622_family_pairing_orbit_decided"]
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
