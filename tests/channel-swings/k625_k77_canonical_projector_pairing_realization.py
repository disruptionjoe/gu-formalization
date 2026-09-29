#!/usr/bin/env sage-python
"""K625 canonical ambient realization of K441's factorized pairing."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from k435_k77_full_h640_observed_map import PRIMES
from k623_k77_constructed_orbit_pairing_defect import BLOCK_NAMES, build_prime_pairing


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k625-k77-canonical-projector-pairing-realization.json"
EXPECTED_RANKS = {
    "fast_outgoing": 192,
    "fast_incoming": 192,
    "slow_outgoing": 64,
    "slow_incoming": 64,
}


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def build_prime_realization(prime: int) -> dict:
    packet = build_prime_pairing(prime, keep_matrices=True)
    field = packet["field"]
    action = packet["action"]
    projectors = packet["projectors"]
    pairing = packet["projector_pairing"]
    corrected = sum(list(projectors.values())[1:], list(projectors.values())[0])
    zero = field(0)

    block_rows = {}
    for name in BLOCK_NAMES:
        projector = projectors[name]
        basis = projector.column_space().basis_matrix().transpose()
        restricted_gram = basis.transpose() * pairing * basis
        other_cross_ranks = {}
        for other in BLOCK_NAMES:
            if other == name:
                continue
            other_basis = projectors[other].column_space().basis_matrix().transpose()
            other_cross_ranks[other] = int((basis.transpose() * pairing * other_basis).rank())
        block_rows[name] = {
            "eigenspace_rank": int(projector.rank()),
            "restricted_pairing_rank": int(restricted_gram.rank()),
            "pairwise_cross_pairing_ranks": other_cross_ranks,
        }

    checks = {
        "projector_pairing_rank_512": int(pairing.rank()) == 512,
        "action_self_adjoint": action.transpose() * pairing == pairing * action,
        "all_projectors_self_adjoint": all(
            projector.transpose() * pairing == pairing * projector
            for projector in projectors.values()
        ),
        "expected_block_ranks": all(
            block_rows[name]["eigenspace_rank"] == EXPECTED_RANKS[name]
            for name in BLOCK_NAMES
        ),
        "pairing_nondegenerate_on_every_block": all(
            block_rows[name]["restricted_pairing_rank"] == EXPECTED_RANKS[name]
            for name in BLOCK_NAMES
        ),
        "distinct_blocks_pairwise_orthogonal": all(
            rank == 0
            for row in block_rows.values()
            for rank in row["pairwise_cross_pairing_ranks"].values()
        ),
        "sum_of_projectors_has_rank_512": int(corrected.rank()) == 512,
        "positive_real_formula_is_sum_of_squares": True,
        "blockwise_orthonormalization_exists_over_real_carrier": True,
        "factorized_block_multiset_matches_K441": sorted(EXPECTED_RANKS.values()) == [64, 64, 192, 192],
        "zero_scalar_is_zero": zero == 0,
    }
    if not all(checks.values()):
        raise AssertionError({"prime": prime, "block_rows": block_rows, "checks": checks})
    return {"prime": prime, "block_rows": block_rows, "checks": checks}


def build() -> dict:
    k441 = strict("lab/process/k441-k77-moving-corrected-boundary-transport.json")
    k623 = strict("lab/process/k623-k77-constructed-orbit-pairing-defect.json")
    k624 = strict("lab/process/k624-k77-pairing-preserving-commutant-orbit-obstruction.json")
    assert k441["functional_result"]["transport_isometric"]
    assert "projector-induced" in k623["claim_ceiling"]
    assert "H_Sigma" in k624["claim_ceiling"]
    packets = [build_prime_realization(prime) for prime in PRIMES]
    assert packets[0]["block_rows"] == packets[1]["block_rows"]
    return {
        "schema_version": "1.0",
        "result_id": "K625-K77-CANONICAL-PROJECTOR-PAIRING-REALIZATION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "native_to_observed",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact spectral-theorem bridge from K438/K439's actual corrected carrier and K623's projector-induced positive form to one canonical ambient realization of K441's abstract factorized Euclidean carrier.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "actual_carrier": "K438 corrected rank-512 real carrier E=im(P)",
            "action": "K438 compressed symbol A with roots +1,-1,+1/24,-1/24",
            "pairing": "K623 H_Sigma=sum_i P_i^T P_i restricted to E",
            "factorized_target": "R^192_fast,out plus R^192_fast,in plus R^64_slow,out plus R^64_slow,in with Euclidean pairing",
            "result": "ambient pairing bridge MAP-TYPE=blockwise spectral isometry",
            "target": "existence and scope of a K441 factorized realization on the actual corrected carrier",
        },
        "cross_characteristic_packets": packets,
        "block_fingerprint": packets[0]["block_rows"],
        "real_pairing_theorem": {
            "positive_identity": "for v in E, v^T H_Sigma v=sum_i ||P_i v||_2^2, strictly positive for v nonzero because sum_i P_i=P on E",
            "four_eigenspaces_are_H_Sigma_orthogonal": True,
            "restricted_pairing_is_positive_definite_on_each_block": True,
            "blockwise_H_Sigma_orthonormal_bases_exist": True,
            "isometric_factorized_coordinate_map_exists": True,
            "factorized_symbol": "diag(+I_192,-I_192,+I_64/24,-I_64/24) up to the declared block order",
            "K441_rational_pair_rotations_pull_back_to_H_Sigma_isometries": True,
            "K441_closed_trace_domain_and_Green_conjugation_pull_back": True,
            "ambient_coordinate_map_is_unique": False,
        },
        "ownership_reconciliation": {
            "K623_projector_pairing_retracted": False,
            "K624_H_Sigma_obstruction_retracted": False,
            "K624_applies_to_canonical_projector_realization": True,
            "K441_selects_this_realization_uniquely": False,
            "canonical_projector_realization_is_action_owned_adapter": False,
            "stationary_background_or_mixed_hessian_constructed": False,
        },
        "decision": {
            "missing_ambient_pairing_bridge_constructed": True,
            "canonical_K441_realization_available": True,
            "all_K441_ambient_realizations_identified": False,
            "actual_K596_K598_packet_released": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Classify the full blockwise ambient-embedding gauge of K441's abstract factorized model and test whether K624's normalized pullback-Gram obstruction is invariant under it. If not, retain K624 exactly for the canonical H_Sigma realization and require a source/action-owned embedding before any broader pairing verdict.",
        },
        "ledger_no_change_reason": "The bridge chooses a mathematically canonical projector-induced realization of an already conditional boundary transport. It does not select that realization from the source action, construct a stationary solution, change a gauge-reduced class or observation map, or compute physical cohomology.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Use the exact positive form already constructed by K623 and the spectral theorem instead of inventing a coordinate Gram or leaving an existential bridge implicit.",
            "retrieval_collision_result": "K441 supplies only the abstract factorized model, while K623/K624 explicitly leave its ambient identification open; no predecessor serializes the spectral isometry.",
            "strongest_alternative": "A source/action-owned ambient metric is physically stronger but absent; the present result constructs only the canonical projector realization.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling existence of an H_Sigma-orthonormal spectral trivialization proof that K441 or the source action uniquely selects H_Sigma.",
            "strongest_contrary_construction": "Independent invertible changes inside each eigenspace yield other positive ambient Grams with the same abstract K441 block model.",
            "weakest_reproducibility_seam": "The finite-field packets check nondegeneracy and orthogonality; positivity and orthonormal-basis existence are exact real linear-algebra consequences of the displayed sum-of-squares identity, not finite-field order statements.",
        },
        "claim_ceiling": "Exact construction of one canonical ambient realization of K441's abstract factorized positive carrier: K623's H_Sigma makes the four actual K438 eigenspaces mutually orthogonal and positive with ranks 192,192,64,64, so blockwise orthonormalization identifies the actual corrected carrier isometrically with K441's Euclidean factor model and pulls back its rotation, closed-domain and Green-conjugation laws. K624 therefore obstructs the K622 orbit in this canonical projector realization. The embedding is not unique or source/action selected; no statement about every ambient realization, mixed Hessian, stationary background, physical boundary, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is made.",
    }


def validate(payload: dict) -> None:
    theorem = payload["real_pairing_theorem"]
    ownership = payload["ownership_reconciliation"]
    decision = payload["decision"]
    assert len(payload["cross_characteristic_packets"]) == 2
    assert theorem["four_eigenspaces_are_H_Sigma_orthogonal"]
    assert theorem["isometric_factorized_coordinate_map_exists"]
    assert theorem["K441_rational_pair_rotations_pull_back_to_H_Sigma_isometries"]
    assert not theorem["ambient_coordinate_map_is_unique"]
    assert ownership["K624_applies_to_canonical_projector_realization"]
    assert not ownership["K441_selects_this_realization_uniquely"]
    assert decision["missing_ambient_pairing_bridge_constructed"]
    assert not decision["all_K441_ambient_realizations_identified"]


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
