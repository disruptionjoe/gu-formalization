#!/usr/bin/env python3
"""K627 structural nonselection of a positive pairing by K626's full block gauge."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k627-k77-block-gauge-positive-pairing-nonselection.json"
BLOCK_RANKS = (192, 192, 64, 64)


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def build() -> dict:
    k625 = strict("lab/process/k625-k77-canonical-projector-pairing-realization.json")
    k626 = strict("lab/process/k626-k77-ambient-pairing-embedding-gauge.json")
    assert k625["real_pairing_theorem"]["restricted_pairing_is_positive_definite_on_each_block"]
    assert k626["embedding_gauge_theorem"]["gauge_group"] == "GL(192) x GL(192) x GL(64) x GL(64)"
    block_pairing_dimensions = [rank * (rank + 1) // 2 for rank in BLOCK_RANKS]
    return {
        "schema_version": "1.0",
        "result_id": "K627-K77-BLOCK-GAUGE-POSITIVE-PAIRING-NONSELECTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "native_to_observed",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Structural classification of whether K626's full blockwise ambient-embedding gauge can itself select a nonzero symmetric or positive-definite pairing on K438's corrected carrier.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "action": "K438 corrected four-root symbol and its spectral projectors",
            "gauge": "K626 independent block coordinate group GL(192) x GL(192) x GL(64) x GL(64)",
            "pairing_space": "positive-definite symmetric forms on the four real spectral blocks",
            "result": "pairing nonselection theorem MAP-TYPE=homogeneous-space/stabilizer classification",
            "target": "whether abstract K441 data choose one ambient Gram without extra source/action structure",
        },
        "pairing_nonselection_theorem": {
            "block_ranks": list(BLOCK_RANKS),
            "block_positive_pairing_dimensions": block_pairing_dimensions,
            "total_positive_pairing_family_dimension": sum(block_pairing_dimensions),
            "full_block_gauge_has_nonzero_invariant_symmetric_form": False,
            "scalar_witness_argument": "On every positive-rank block, invariance under lambda*I gives lambda^2 H=H. Taking lambda=2 over R forces H=0.",
            "positive_pairing_stabilizer": "O(H_192+) x O(H_192-) x O(H_64+) x O(H_64-)",
            "positive_pairing_family": "GL(192)/O(192) x GL(192)/O(192) x GL(64)/O(64) x GL(64)/O(64)",
            "selecting_a_gram_is_a_gauge_reduction": True,
            "K625_H_Sigma_is_one_projector_induced_point": True,
            "K441_abstract_data_select_a_positive_gram": False,
        },
        "ownership_reconciliation": {
            "K625_canonical_realization_retracted": False,
            "K626_embedding_gauge_retracted": False,
            "full_gauge_nonselection_is_source_or_action_selection": False,
            "orthogonal_reduction_is_supplied_by_K441": False,
            "mixed_hessian_or_stationary_background_constructed": False,
            "common_BV_Green_domain_constructed": False,
        },
        "decision": {
            "abstract_K441_pairing_is_canonical_on_actual_carrier": False,
            "extra_reduction_data_required_to_select_pairing": True,
            "actual_K596_K598_packet_released": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Test K622's serialized domain map against pairing-independent isometry invariants, while keeping the broader K622-family and any source/action-owned Gram separate.",
        },
        "ledger_no_change_reason": "The theorem classifies an unselected coordinate gauge and its positive-form homogeneous space. It supplies no action-owned reduction, stationary solution, physical state, quotient, observation map, or source-native pairing.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "K626's finite shears prove nonuniqueness; the full stabilizer argument decides whether the entire gauge could nevertheless possess one invariant positive form without enumerating embeddings.",
            "retrieval_collision_result": "K625 identifies one canonical projector point and K626 the full gauge, but neither states the no-invariant-form theorem or the dimension of the remaining positive-pairing family.",
            "strongest_alternative": "A source/action-owned Gram could reduce the gauge, but no such selector is serialized and arbitrary reduction is not ownership.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling absence of a gauge-invariant Gram absence of every positive Gram, or treating an arbitrary orthogonal reduction as source/action selected.",
            "strongest_contrary_construction": "K625's H_Sigma is a valid positive projector-induced point and realizes K441 exactly; the theorem denies uniqueness under the full gauge, not existence.",
            "weakest_reproducibility_seam": "The theorem is characteristic-zero structural algebra; its only numerical datum is the transparent symmetric-form dimension count.",
        },
        "claim_ceiling": "Exact structural proof that K626's full GL(192)xGL(192)xGL(64)xGL(64) embedding gauge has no nonzero invariant symmetric form and therefore cannot by itself select an ambient positive Gram. Positive pairings form a 41,216-dimensional blockwise homogeneous space, and choosing one reduces the gauge to its orthogonal stabilizer. K625's H_Sigma remains a valid canonical projector-induced point. No source/action-owned reduction, mixed Hessian, stationary background, common BV/Green domain, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is constructed or settled.",
    }


def validate(payload: dict) -> None:
    theorem = payload["pairing_nonselection_theorem"]
    ownership = payload["ownership_reconciliation"]
    decision = payload["decision"]
    assert theorem["block_ranks"] == [192, 192, 64, 64]
    assert theorem["block_positive_pairing_dimensions"] == [18528, 18528, 2080, 2080]
    assert theorem["total_positive_pairing_family_dimension"] == 41216
    assert not theorem["full_block_gauge_has_nonzero_invariant_symmetric_form"]
    assert theorem["selecting_a_gram_is_a_gauge_reduction"]
    assert not theorem["K441_abstract_data_select_a_positive_gram"]
    assert not ownership["orthogonal_reduction_is_supplied_by_K441"]
    assert decision["extra_reduction_data_required_to_select_pairing"]
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
