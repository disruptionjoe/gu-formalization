#!/usr/bin/env sage-python
"""K626 blockwise ambient-embedding gauge of K441's factorized model."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sage.all import identity_matrix, zero_matrix

from k435_k77_full_h640_observed_map import PRIMES, canonical_digest
from k623_k77_constructed_orbit_pairing_defect import BLOCK_NAMES, build_prime_pairing


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k626-k77-ambient-pairing-embedding-gauge.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def normalized_traces(pairing, seed, projectors: dict) -> dict[str, str]:
    grams = {}
    for name in BLOCK_NAMES:
        block = projectors[name] * seed
        grams[name] = block.transpose() * pairing * block
    total = sum(list(grams.values())[1:], list(grams.values())[0])
    if not total.is_invertible():
        raise AssertionError("total pullback pairing must be invertible")
    inverse = total.inverse()
    return {name: str((inverse * grams[name]).trace()) for name in BLOCK_NAMES}


def coordinate_left_inverse(basis, field):
    rank = basis.ncols()
    pivot_rows = list(basis.transpose().pivots())
    square = basis.matrix_from_rows(pivot_rows)
    inverse = square.inverse()
    left = zero_matrix(field, rank, basis.nrows(), sparse=True)
    for column_index, ambient_row in enumerate(pivot_rows):
        for row_index in range(rank):
            value = inverse[row_index, column_index]
            if value:
                left[row_index, ambient_row] = value
    if left * basis != identity_matrix(field, rank):
        raise AssertionError("coordinate left inverse failed")
    return left


def build_prime_gauge(prime: int) -> dict:
    packet = build_prime_pairing(prime, keep_matrices=True)
    field = packet["field"]
    action = packet["action"]
    projectors = packet["projectors"]
    corrected = sum(list(projectors.values())[1:], list(projectors.values())[0])
    pairing = packet["projector_pairing"]
    zero_seed = packet["zero_seed"]
    graph = packet["graph"]
    identity = identity_matrix(field, 640, sparse=True)
    base_zero = normalized_traces(pairing, zero_seed, projectors)
    base_graph = normalized_traces(pairing, graph, projectors)

    shear_rows = {}
    for name in BLOCK_NAMES:
        projector = projectors[name]
        basis = projector.column_space().basis_matrix().transpose()
        rank = basis.ncols()
        left = coordinate_left_inverse(basis, field)
        elementary = zero_matrix(field, rank, rank, sparse=True)
        elementary[0, 1] = field(1)
        nilpotent = basis * elementary * left * projector
        shear = identity + nilpotent
        inverse_shear = identity - nilpotent
        changed_pairing = shear.transpose() * pairing * shear
        changed_zero = normalized_traces(changed_pairing, zero_seed, projectors)
        changed_graph = normalized_traces(changed_pairing, graph, projectors)
        checks = {
            "rank_one_block_shear": int(nilpotent.rank()) == 1,
            "nilpotent_square_zero": (nilpotent * nilpotent).is_zero(),
            "explicit_inverse": shear * inverse_shear == identity and inverse_shear * shear == identity,
            "commutes_with_action": shear * action == action * shear,
            "commutes_with_all_projectors": all(
                shear * other == other * shear for other in projectors.values()
            ),
            "changed_pairing_rank_512": int(changed_pairing.rank()) == 512,
            "action_self_adjoint_for_changed_pairing": action.transpose() * changed_pairing == changed_pairing * action,
            "all_projectors_self_adjoint_for_changed_pairing": all(
                other.transpose() * changed_pairing == changed_pairing * other
                for other in projectors.values()
            ),
            "zero_seed_normalized_traces_change": changed_zero != base_zero,
            "graph_seed_normalized_traces_change": changed_graph != base_graph,
            "corrected_carrier_preserved": shear * corrected == corrected * shear,
        }
        if not all(checks.values()):
            raise AssertionError({"prime": prime, "block": name, "checks": checks})
        shear_rows[name] = {
            "eigenspace_rank": rank,
            "nilpotent_rank": int(nilpotent.rank()),
            "nilpotent_sha256": canonical_digest(nilpotent),
            "changed_pairing_sha256": canonical_digest(changed_pairing),
            "base_zero_seed_normalized_traces": base_zero,
            "changed_zero_seed_normalized_traces": changed_zero,
            "base_graph_seed_normalized_traces": base_graph,
            "changed_graph_seed_normalized_traces": changed_graph,
            "checks": checks,
        }
    return {"prime": prime, "shear_rows": shear_rows}


def build() -> dict:
    k624 = strict("lab/process/k624-k77-pairing-preserving-commutant-orbit-obstruction.json")
    k625 = strict("lab/process/k625-k77-canonical-projector-pairing-realization.json")
    assert "H_Sigma" in k624["claim_ceiling"]
    assert k625["real_pairing_theorem"]["isometric_factorized_coordinate_map_exists"]
    packets = [build_prime_gauge(prime) for prime in PRIMES]
    boolean_fingerprints = [
        {
            name: row["checks"]
            for name, row in packet["shear_rows"].items()
        }
        for packet in packets
    ]
    assert boolean_fingerprints[0] == boolean_fingerprints[1]
    return {
        "schema_version": "1.0",
        "result_id": "K626-K77-AMBIENT-PAIRING-EMBEDDING-GAUGE",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "native_to_observed",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact classification of the blockwise ambient-coordinate gauge left unselected by K441's abstract factorized Euclidean model, with actual-carrier rank-one shears testing whether K624's normalized pullback-Gram fingerprints are invariant under that gauge.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "abstract_model": "K441 four spectral blocks with Euclidean pairing, rational pair rotation and closed-domain Green conjugation",
            "ambient_realization": "an isomorphism F from the actual corrected carrier to the abstract factorized blocks, pulling Euclidean pairing back to H_F=F^T F",
            "embedding_gauge": "independent invertible block changes C_i in GL(192), GL(192), GL(64), GL(64), with F replaced by C F and the abstract transport conjugated accordingly",
            "actual_probe": "rank-one square-zero shears S_i=I+N_i inside each K438 eigenspace, with H_i=S_i^T H_Sigma S_i",
            "result": "ambient pairing nonidentifiability MAP-TYPE=blockwise congruence gauge",
            "target": "whether K624's H_Sigma orbit obstruction is intrinsic to K441's abstract factorized data",
        },
        "cross_characteristic_packets": packets,
        "embedding_gauge_theorem": {
            "gauge_group": "GL(192) x GL(192) x GL(64) x GL(64)",
            "all_blockwise_changes_preserve_four_root_action_up_to_factorized_coordinates": True,
            "pulled_back_pairing_family": "H_C=F^T C^T C F, positive definite on the real corrected carrier for every invertible real C",
            "moving_transport_family": "U_C=F^-1 C^-1 U C F; its projector parallelism, isometry, closed-domain and Green-conjugation laws are coordinate conjugates of K441",
            "K441_serializes_one_ambient_embedding": False,
            "H_Sigma_is_a_canonical_projector_point_in_the_family": True,
            "K624_normalized_trace_fingerprints_are_embedding_gauge_invariant": False,
            "actual_carrier_shears_tested": 8,
            "every_tested_shear_changes_both_seed_fingerprints": True,
        },
        "ownership_reconciliation": {
            "K625_canonical_realization_retracted": False,
            "K624_H_Sigma_obstruction_retracted": False,
            "K624_universalized_to_every_K441_embedding": False,
            "K441_abstract_transport_selects_an_ambient_Gram": False,
            "embedding_gauge_is_source_or_action_selection": False,
            "pairing_gauge_constructs_mixed_hessian_or_stationary_background": False,
        },
        "decision": {
            "canonical_projector_realization_classified": True,
            "abstract_K441_pairing_alone_decides_K622_orbit": False,
            "source_or_action_owned_embedding_required_for_broader_verdict": True,
            "actual_K596_K598_packet_released": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Supply a source/action-owned ambient embedding or Gram for the corrected carrier, or a genuinely new action-owned source-domain endomorphism or mixed-Hessian odd adapter on a nonzero stationary moving background. Then test its K441 Riesz return, pairing and common BV/Green domain. K624 remains decisive for the canonical H_Sigma realization only.",
        },
        "ledger_no_change_reason": "The result exposes coordinate/metric freedom in a conditional boundary transport and narrows an internal orbit obstruction. It selects no embedding from the source action and constructs no stationary solution, mixed Hessian, gauge-reduced class, observation map or physical cohomology.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "After K625 constructs one canonical realization, test the entire missing coordinate-choice seam by exact within-eigenspace congruences rather than treating H_Sigma as silently unique.",
            "retrieval_collision_result": "K623/K624 mention another symmetrizing pairing but do not classify K441's embedding gauge or test their invariants under actual-carrier block shears.",
            "strongest_alternative": "Finding one source/action-owned Gram would collapse the gauge physically, but no such selector is serialized.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling gauge dependence proof that some alternative positive pairing makes the K622 orbit isometric, or calling arbitrary C source/action selected.",
            "strongest_contrary_construction": "The canonical H_Sigma point is exact and K624 remains a complete obstruction there; gauge variation changes its necessary fingerprints but does not itself produce a successful orbit.",
            "weakest_reproducibility_seam": "The actual-carrier shear fingerprints are certified over both good characteristics; positivity of H_C over the real carrier follows by congruence from H_Sigma and is not a finite-field order claim.",
        },
        "claim_ceiling": "Exact cross-characteristic proof that K441's abstract factorized transport leaves a full blockwise ambient-embedding gauge and that K624's normalized pullback-Gram trace fingerprints are not invariant under it. Eight actual-carrier rank-one square-zero shears preserve the four-root action, all spectral projectors, nondegeneracy and self-adjointness while changing both seed fingerprints. K624 remains decisive for K625's canonical H_Sigma realization but cannot be universalized to every unselected K441 embedding. No alternative pairing-preserving orbit, source/action-owned Gram, mixed Hessian, stationary background, common BV/Green domain, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is constructed or settled.",
    }


def validate(payload: dict) -> None:
    theorem = payload["embedding_gauge_theorem"]
    ownership = payload["ownership_reconciliation"]
    decision = payload["decision"]
    assert len(payload["cross_characteristic_packets"]) == 2
    assert theorem["actual_carrier_shears_tested"] == 8
    assert theorem["every_tested_shear_changes_both_seed_fingerprints"]
    assert not theorem["K441_serializes_one_ambient_embedding"]
    assert not theorem["K624_normalized_trace_fingerprints_are_embedding_gauge_invariant"]
    assert ownership["K624_H_Sigma_obstruction_retracted"] is False
    assert ownership["K624_universalized_to_every_K441_embedding"] is False
    assert decision["source_or_action_owned_embedding_required_for_broader_verdict"]
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
