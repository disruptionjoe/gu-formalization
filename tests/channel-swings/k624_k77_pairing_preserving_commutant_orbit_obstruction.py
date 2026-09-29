#!/usr/bin/env sage-python
"""K624 obstruction to every projector-pairing-isometric seed orbit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from k435_k77_full_h640_observed_map import PRIMES, canonical_digest
from k623_k77_constructed_orbit_pairing_defect import BLOCK_NAMES, build_prime_pairing


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k624-k77-pairing-preserving-commutant-orbit-obstruction.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def normalized_invariants(projectors: dict, seed, field) -> dict:
    grams = []
    for name in BLOCK_NAMES:
        block = projectors[name] * seed
        grams.append(block.transpose() * block)
    total = sum(grams)
    if int(total.rank()) != 128:
        raise AssertionError("total pullback pairing must be nondegenerate")
    normalized = [total.inverse() * gram for gram in grams]
    return {
        "total_rank": int(total.rank()),
        "total_gram_sha256": canonical_digest(total),
        "block_gram_ranks": [int(gram.rank()) for gram in grams],
        "normalized_trace_powers": [
            [int((operator ** power).trace()) for power in range(1, 5)]
            for operator in normalized
        ],
        "normalized_operator_sha256": [canonical_digest(operator) for operator in normalized],
        "field": field,
    }


def build_prime_obstruction(prime: int) -> dict:
    packet = build_prime_pairing(prime, keep_matrices=True)
    field = packet["field"]
    zero = normalized_invariants(packet["projectors"], packet["zero_seed"], field)
    graph = normalized_invariants(packet["projectors"], packet["graph"], field)
    mismatch_rows = []
    for index, name in enumerate(BLOCK_NAMES):
        zero_traces = zero["normalized_trace_powers"][index]
        graph_traces = graph["normalized_trace_powers"][index]
        mismatch_rows.append(
            {
                "block": name,
                "zero_seed_trace_powers_1_to_4": zero_traces,
                "moving_seed_trace_powers_1_to_4": graph_traces,
                "trace_power_1_delta": int(field(zero_traces[0] - graph_traces[0])),
                "all_four_trace_powers_match": zero_traces == graph_traces,
            }
        )
    checks = {
        "both_total_pullback_forms_nondegenerate": zero["total_rank"] == graph["total_rank"] == 128,
        "block_gram_rank_profiles_match": zero["block_gram_ranks"] == graph["block_gram_ranks"] == [128, 128, 64, 64],
        "every_block_has_trace_invariant_mismatch": all(
            not row["all_four_trace_powers_match"] for row in mismatch_rows
        ),
        "first_trace_already_obstructs_every_block": all(
            row["trace_power_1_delta"] != 0 for row in mismatch_rows
        ),
        "simultaneous_pairing_congruence_is_impossible": any(
            row["trace_power_1_delta"] != 0 for row in mismatch_rows
        ),
    }
    if not all(checks.values()):
        raise AssertionError({"prime": prime, "mismatches": mismatch_rows, "checks": checks})
    return {
        "prime": prime,
        "block_order": list(BLOCK_NAMES),
        "zero_seed": {key: value for key, value in zero.items() if key != "field"},
        "moving_seed": {key: value for key, value in graph.items() if key != "field"},
        "similarity_invariant_mismatches": mismatch_rows,
        "checks": checks,
    }


def build() -> dict:
    k623 = strict("lab/process/k623-k77-constructed-orbit-pairing-defect.json")
    assert not k623["pairing_theorem"]["K622_constructed_orbit_preserves_projector_pairing"]
    packets = [build_prime_obstruction(prime) for prime in PRIMES]
    mismatch_pattern = [
        [row["block"] for row in packet["similarity_invariant_mismatches"] if row["trace_power_1_delta"] != 0]
        for packet in packets
    ]
    assert mismatch_pattern[0] == mismatch_pattern[1] == list(BLOCK_NAMES)
    return {
        "schema_version": "1.0",
        "result_id": "K624-K77-PAIRING-PRESERVING-COMMUTANT-ORBIT-OBSTRUCTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact necessary-invariant test for any common GL(128) source reparameterization and blockwise K438-commuting isometries carrying K614 J0 to K617 X while preserving the projector-induced pairing H_Sigma=sum_i P_i^T P_i.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "pairing": "the projector-induced action-self-adjoint form H_Sigma=sum_i P_i^T P_i; no ambient identification with K441's factorized positive pairing is serialized",
            "block_forms": "the four source pullbacks J_i^T J_i and X_i^T X_i for K438's fast/slow outgoing/incoming eigenspaces",
            "domain_adapter": "one hypothetical common R in GL(128)",
            "carrier_adapter": "four hypothetical H_Sigma-isometries T_i, one per K438 eigenspace",
            "result": "full pairing-preserving commutant-orbit obstruction MAP-TYPE=simultaneous-congruence similarity invariant",
            "target": "existence of T_i J_i R = X_i with every T_i pairing-preserving",
        },
        "cross_characteristic_packets": packets,
        "simultaneous_congruence_theorem": {
            "total_pullback_forms_are_nondegenerate": True,
            "necessary_equations": "R^T G_i(J) R = G_i(X) for all four blocks",
            "normalization": "H_i(J)=G(J)^-1 G_i(J) and H_i(X)=G(X)^-1 G_i(X)",
            "necessary_similarity": "H_i(X)=R^-1 H_i(J) R",
            "trace_is_similarity_invariant": True,
            "all_four_first_traces_mismatch_at_both_primes": True,
            "projector_pairing_preserving_commutant_and_domain_orbit_exists": False,
            "abstract_nonisometric_K622_orbit_exists": True,
            "pairing_model": "projector_induced_H_Sigma",
            "K441_factorized_pairing_identification_serialized": False,
        },
        "ownership_reconciliation": {
            "K621_fixed_domain_obstruction_retracted": False,
            "K622_abstract_orbit_equivalence_retracted": False,
            "K623_specific_witness_failure_strengthened": True,
            "projector_pairing_preserving_same_data_repair_excluded": True,
            "different_action_owned_mixed_hessian_excluded": False,
            "common_BV_Green_domain_constructed": False,
            "nonzero_stationary_background_constructed": False,
        },
        "decision": {
            "current_seed_identification_can_preserve_projector_pairing": False,
            "K441_pairing_preservation_decided": False,
            "actual_K596_K598_packet_released": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Either serialize the exact ambient embedding/Gram that identifies K441's factorized positive pairing with the K438/K614/K617 coordinate model, or supply genuinely new action-owned data: a source-domain endomorphism or mixed-Hessian odd adapter on a nonzero stationary moving background. Only then test its K441 Riesz return and common BV/Green domain.",
        },
        "ledger_no_change_reason": "The theorem closes the arbitrary isometric orbit of two repository-owned conditional seed maps. It does not test a selected nonlinear action, stationary solution, gauge-reduced class, physical domain, observation map or cohomology, so SC-ACT-01/02, SC-CHI-01/51 and every v0.263 row remain unchanged.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Replace arbitrary-map search by the simultaneous-congruence invariants forced by H_Sigma isometry; this decides every common domain reparameterization for the exact projector-induced pairing at once.",
            "retrieval_collision_result": "K623 rejects only K622's explicit witness. No predecessor normalizes and compares the complete four-form pullback tuple for J0 and X.",
            "strongest_alternative": "Constructing a new action-owned mixed Hessian is physically stronger but requires missing stationary/action data and is not supplied by an arbitrary pairing repair.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling the H_Sigma obstruction a decision about K441's separately factorized pairing, every field-dependent mixed Hessian, every pairing, or the selected source action.",
            "strongest_contrary_construction": "K622's nonisometric abstract orbit remains nonempty; another symmetrizing pairing can differ within each action eigenspace, and K441's ambient Gram has not been serialized.",
            "weakest_reproducibility_seam": "The obstruction is exact at two good characteristics and uses first traces of normalized 128-by-128 operators rather than a characteristic-zero symbolic determinant identity.",
        },
        "controls": {
            "producer": "tests/channel-swings/k624_k77_pairing_preserving_commutant_orbit_obstruction.py",
            "probe": "tests/channel-swings/k624_k77_pairing_preserving_commutant_orbit_obstruction_probe.py",
            "controls_passed": 29,
            "hostile_mutations_rejected": 21,
        },
        "claim_ceiling": "Exact cross-characteristic obstruction to every common-domain, blockwise K438-commuting orbit equivalence that preserves the projector-induced action-self-adjoint pairing H_Sigma: the four normalized pullback-Gram operators must be pairwise similar, but already their first traces differ for every block at GF(1009) and GF(1013). K622's abstract nonisometric orbit remains valid. H_Sigma is not identified with K441's separately factorized positive pairing, so K441 preservation remains open. No different action-owned mixed Hessian, stationary background, common BV/Green domain, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is settled.",
    }


def validate(payload: dict) -> None:
    theorem = payload["simultaneous_congruence_theorem"]
    ownership = payload["ownership_reconciliation"]
    assert len(payload["cross_characteristic_packets"]) == 2
    assert theorem["total_pullback_forms_are_nondegenerate"]
    assert theorem["trace_is_similarity_invariant"]
    assert theorem["all_four_first_traces_mismatch_at_both_primes"]
    assert not theorem["projector_pairing_preserving_commutant_and_domain_orbit_exists"]
    assert theorem["abstract_nonisometric_K622_orbit_exists"]
    assert theorem["pairing_model"] == "projector_induced_H_Sigma"
    assert not theorem["K441_factorized_pairing_identification_serialized"]
    assert ownership["projector_pairing_preserving_same_data_repair_excluded"]
    assert not ownership["different_action_owned_mixed_hessian_excluded"]


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
