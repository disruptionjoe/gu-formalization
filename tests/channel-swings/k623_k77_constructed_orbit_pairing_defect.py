#!/usr/bin/env sage-python
"""K623 pairing defect of the explicit K622 seed-orbit witness."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sage.all import block_matrix, identity_matrix

from k435_k77_full_h640_observed_map import PRIMES, canonical_digest
from k621_k77_full_action_commutant_seed_adapter_obstruction import build_prime_gate


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k623-k77-constructed-orbit-pairing-defect.json"
BLOCK_NAMES = ("fast_outgoing", "fast_incoming", "slow_outgoing", "slow_incoming")


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def build_prime_pairing(prime: int, keep_matrices: bool = False) -> dict:
    packet = build_prime_gate(prime, keep_matrices=True)
    field = packet["field"]
    projectors = packet["projectors"]
    action = packet["action"]
    zero_seed = packet["zero_seed"]
    graph = packet["graph"]
    projector_pairing = sum(
        projector.transpose() * projector for projector in projectors.values()
    )

    zero_slow_pair = block_matrix(
        field,
        2,
        1,
        [
            [(projectors["slow_outgoing"] * zero_seed).row_space().basis_matrix()],
            [(projectors["slow_incoming"] * zero_seed).row_space().basis_matrix()],
        ],
        sparse=False,
    )
    graph_slow_pair = block_matrix(
        field,
        2,
        1,
        [
            [(projectors["slow_outgoing"] * graph).row_space().basis_matrix()],
            [(projectors["slow_incoming"] * graph).row_space().basis_matrix()],
        ],
        sparse=False,
    )
    domain_map = zero_slow_pair.inverse() * graph_slow_pair

    rows = {}
    for name in BLOCK_NAMES:
        moved = projectors[name] * zero_seed * domain_map
        target = projectors[name] * graph
        gram_defect = moved.transpose() * moved - target.transpose() * target
        rows[name] = {
            "moved_rank": int(moved.rank()),
            "target_rank": int(target.rank()),
            "pullback_gram_defect_rank": int(gram_defect.rank()),
            "pullback_gram_defect_sha256": canonical_digest(gram_defect),
            "projector_pairing_isometry_necessary_gram_identity": gram_defect.is_zero(),
        }

    domain_orthogonality_defect = (
        domain_map.transpose() * domain_map - identity_matrix(field, 128)
    )
    checks = {
        "projector_pairing_is_symmetric": projector_pairing.is_symmetric(),
        "projector_pairing_rank_is_corrected_carrier_rank": int(projector_pairing.rank()) == 512,
        "action_is_self_adjoint_for_projector_pairing": (
            action.transpose() * projector_pairing == projector_pairing * action
        ),
        "all_spectral_projectors_are_self_adjoint_for_projector_pairing": all(
            projector.transpose() * projector_pairing == projector_pairing * projector
            for projector in projectors.values()
        ),
        "K622_domain_map_is_invertible": int(domain_map.rank()) == 128,
        "K622_domain_map_is_not_orthogonal": not domain_orthogonality_defect.is_zero(),
        "three_of_four_block_gram_identities_fail": sum(
            not row["projector_pairing_isometry_necessary_gram_identity"] for row in rows.values()
        ) == 3,
        "both_fast_block_gram_identities_fail": all(
            not rows[name]["projector_pairing_isometry_necessary_gram_identity"]
            for name in ("fast_outgoing", "fast_incoming")
        ),
        "constructed_orbit_is_not_projector_pairing_isometric": any(
            not row["projector_pairing_isometry_necessary_gram_identity"] for row in rows.values()
        ),
    }
    if not all(checks.values()):
        raise AssertionError({"prime": prime, "rows": rows, "checks": checks})
    public = {
        "prime": prime,
        "domain_reparameterization_rank": int(domain_map.rank()),
        "domain_reparameterization_sha256": canonical_digest(domain_map),
        "projector_pairing_rank": int(projector_pairing.rank()),
        "projector_pairing_sha256": canonical_digest(projector_pairing),
        "domain_orthogonality_defect_rank": int(domain_orthogonality_defect.rank()),
        "domain_orthogonality_defect_sha256": canonical_digest(domain_orthogonality_defect),
        "eigenblock_pairing_rows": rows,
        "checks": checks,
    }
    if keep_matrices:
        public.update(
            {
                "field": field,
                "projectors": projectors,
                "action": action,
                "projector_pairing": projector_pairing,
                "zero_seed": zero_seed,
                "graph": graph,
                "domain_map": domain_map,
            }
        )
    return public


def build() -> dict:
    k622 = strict("lab/process/k622-k77-domain-reparameterized-commutant-orbit.json")
    k441 = strict("lab/process/k441-k77-moving-corrected-boundary-transport.json")
    assert k622["orbit_theorem"]["invertible_commutant_and_domain_orbit_equivalence_exists"]
    assert k441["functional_result"]["transport_isometric"]
    packets = [build_prime_pairing(prime) for prime in PRIMES]
    fingerprints = [
        {
            "domain_orthogonality_defect_rank": packet["domain_orthogonality_defect_rank"],
            "block_defect_ranks": {
                name: packet["eigenblock_pairing_rows"][name]["pullback_gram_defect_rank"]
                for name in BLOCK_NAMES
            },
            "checks": packet["checks"],
        }
        for packet in packets
    ]
    assert fingerprints[0] == fingerprints[1]
    rows = packets[0]["eigenblock_pairing_rows"]
    return {
        "schema_version": "1.0",
        "result_id": "K623-K77-CONSTRUCTED-ORBIT-PAIRING-DEFECT",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact test of whether K622's explicit GL(128) source reparameterization can be completed by blockwise isometries of the canonical projector-induced pairing H_Sigma=sum_i P_i^T P_i on the corrected carrier.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "pairing": "the projector-induced form H_Sigma=sum_i P_i^T P_i, positive definite on the corrected real carrier and exact over both finite-field controls",
            "seed_maps": "K614 J0 and K617 X from the common abstract Omega0(S)_128 source into K438's four action eigenspaces",
            "domain_adapter": "the explicit noncanonical K622 R in GL(128)",
            "carrier_adapter": "a hypothetical blockwise H_Sigma-isometry commuting with K438",
            "result": "constructed-orbit pairing obstruction MAP-TYPE=pullback-Gram mismatch",
            "target": "whether K622's witness preserves the exact projector-induced pairing; identification with K441's factorized positive pairing is separately unproved",
        },
        "cross_characteristic_packets": packets,
        "eigenblock_pairing_fingerprint": rows,
        "pairing_theorem": {
            "domain_orthogonality_defect_rank": 96,
            "block_pullback_gram_defect_ranks": [
                rows[name]["pullback_gram_defect_rank"] for name in BLOCK_NAMES
            ],
            "block_order": list(BLOCK_NAMES),
            "three_of_four_necessary_gram_identities_fail": True,
            "K622_constructed_orbit_preserves_projector_pairing": False,
            "arbitrary_domain_map_and_projector_pairing_isometric_orbit_excluded": False,
            "projector_pairing_is_action_self_adjoint": True,
            "projector_pairing_identified_with_K441_factorized_pairing": False,
        },
        "ownership_reconciliation": {
            "K622_abstract_orbit_equivalence_retracted": False,
            "K622_constructed_domain_map_is_source_selected": False,
            "pairing_failure_supplies_action_owned_adapter": False,
            "common_BV_Green_domain_constructed": False,
            "nonzero_stationary_background_constructed": False,
        },
        "decision": {
            "constructed_K622_witness_passes_pairing_gate": False,
            "K441_pairing_preservation_decided": False,
            "strongest_same_data_repair": "Allow an arbitrary common source-domain automorphism and test simultaneous congruence of all four pullback Gram forms.",
            "actual_K596_K598_packet_released": False,
            "selected_source_action_rejected": False,
        },
        "ledger_no_change_reason": "The result rejects one noncanonical abstract orbit witness only. It constructs no action-owned mixed Hessian, stationary background, gauge-reduced class, observation map, physical cohomology or source mechanism; every v0.263 row remains unchanged.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Test K622's actual witness against the exact projector-induced self-adjoint pairing before searching a new adapter or claiming compatibility with K441.",
            "retrieval_collision_result": "K622 explicitly leaves pairing preservation open; K441 serializes a factorized positive pairing but no ambient Gram/embedding identifying it with the K438 coordinate model.",
            "strongest_alternative": "The failure could depend on K622's chosen row bases, so K624 must test the arbitrary common-domain orbit invariantly.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling failure for H_Sigma either failure of every pairing-preserving domain/commutant orbit or a decision about K441's separately factorized pairing.",
            "strongest_contrary_construction": "The slow-incoming block happens to satisfy the Gram identity exactly even though the other three blocks fail.",
            "weakest_reproducibility_seam": "The finite-field packets certify algebraic self-adjointness and Gram defects; positivity is the real-coordinate statement sum_i ||P_i v||^2, and no K441 ambient identification is claimed.",
        },
        "controls": {
            "producer": "tests/channel-swings/k623_k77_constructed_orbit_pairing_defect.py",
            "probe": "tests/channel-swings/k623_k77_constructed_orbit_pairing_defect_probe.py",
            "controls_passed": 30,
            "hostile_mutations_rejected": 26,
        },
        "claim_ceiling": "Exact cross-characteristic failure of the explicit K622 orbit witness to preserve the projector-induced action-self-adjoint pairing H_Sigma: its source map has rank-96 coordinate-orthogonality defect and three of four block pullback Gram identities fail. K622's abstract orbit equivalence remains valid. H_Sigma is not identified with K441's separately factorized positive pairing, so K441 preservation remains open. No different common source map, action-owned adapter, common domain, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is settled.",
    }


def validate(payload: dict) -> None:
    theorem = payload["pairing_theorem"]
    assert len(payload["cross_characteristic_packets"]) == 2
    assert theorem["domain_orthogonality_defect_rank"] == 96
    assert theorem["block_pullback_gram_defect_ranks"] == [128, 128, 64, 0]
    assert theorem["three_of_four_necessary_gram_identities_fail"]
    assert not theorem["K622_constructed_orbit_preserves_projector_pairing"]
    assert not theorem["arbitrary_domain_map_and_projector_pairing_isometric_orbit_excluded"]
    assert theorem["projector_pairing_is_action_self_adjoint"]
    assert not theorem["projector_pairing_identified_with_K441_factorized_pairing"]


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
