#!/usr/bin/env python3
"""K587: derive the minimal typed interface for an action-owned KT completion."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k587-k77-action-kt-completion-interface.json"


def strict(relative: str) -> dict[str, Any]:
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def build() -> dict[str, Any]:
    typed = strict("lab/process/k585-k77-action-boundary-coupling-typing.json")
    obstruction = strict("lab/process/k586-k77-hessian-adjoint-nilpotence-obstruction.json")
    kt = strict("lab/process/k442-k77-corrected-boundary-kt-product.json")
    square = strict("lab/process/k444-k77-degree-changing-boundary-squares.json")
    base = kt["finite_product_complex"]["base_dimensions"]
    carrier = kt["finite_product_complex"]["corrected_carrier_rank"]
    h_dim, q_dim, m_dim = base
    payload = {
        "schema_version": "1.0",
        "result_id": "K587-K77-ACTION-KT-COMPLETION-INTERFACE",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "scope": "Necessary-and-sufficient finite-dimensional rank/kernel interface for completing K585's injective action block into K442's 21-to-91-to-70 base complex, followed by the exact factorized rank-512 lift already specified by K442/K444. It specifies obligations but supplies no missing action coefficients.",
        "gu_typed_objects": {
            "observed_block": "B: Q^91 -> R^1470, rank 91",
            "required_reduction": "L: R^1470 -> M^70, owned by the selected action; D1 = L B",
            "required_adjacent_arrow": "D2: H^21 -> Q^91, independently owned by the selected action or its authenticated gauge/BV completion",
            "base_complex": "0 -> H^21 --D2--> Q^91 --D1--> M^70 -> 0",
            "factorized_lift": "tensor both base arrows with identity on the corrected rank-512 carrier",
            "MAP-TYPE": "minimal exact-completion interface",
            "LAYER": "source-action tangent/BV boundary",
            "CHIRALITY": "N/A",
        },
        "source_and_ledger_context": {
            "source_claims": ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06", "SC-META-53"],
            "source_polarity_effect": "none",
            "physics_rows": ["LT-SM8", "LT-GR6b", "RA-F1", "AC-F1"],
            "ledger": "lab/process/conditional-physics-ledger-v0.263.json",
            "ledger_effect": "none",
            "typed_input": "lab/process/k585-k77-action-boundary-coupling-typing.json",
            "obstruction_input": "lab/process/k586-k77-hessian-adjoint-nilpotence-obstruction.json",
            "kt_input": "lab/process/k442-k77-corrected-boundary-kt-product.json",
            "typed_square_input": "lab/process/k444-k77-degree-changing-boundary-squares.json",
        },
        "preflight_bookend": {
            "route_comparison": "After rejecting direct and adjoint identifications, derive the smallest coefficient-level obligations that would actually instantiate the accepted abstract KT carrier.",
            "retrieval_collision_result": "K442/K444 supply target dimensions and square obligations; K475 supplies abstract rank fingerprints; none supplies L or D2 for the selected action.",
            "strongest_alternative": "A hand-chosen coordinate projection realizes the dimensions but has no source authority and is retained only as a logical control.",
        },
        "base_completion_interface": {
            "dimensions": {"H": h_dim, "Q": q_dim, "M": m_dim, "R": 1470},
            "observed_B_rank": typed["actual_action_block"]["rank"],
            "required_L_shape": [m_dim, 1470],
            "derived_D1_shape": [m_dim, q_dim],
            "required_D1_rank": m_dim,
            "required_D2_shape": [q_dim, h_dim],
            "required_D2_rank": h_dim,
            "required_nilpotence_equation": "(L B) D2 = 0",
            "required_kernel_dimension_if_D1_surjective": q_dim - m_dim,
            "exactness_equivalence": "rank(LB)=70, rank(D2)=21, and (LB)D2=0; then im(D2)=ker(LB) because both have dimension 21",
            "B_injective_is_sufficient_to_select_L": False,
            "euclidean_adjoint_supplies_D2": False,
            "coefficient_bearing_inputs_present": False,
        },
        "logical_control": {
            "decomposition": "Q^91 = H^21 direct-sum M^70",
            "D2_control": "canonical inclusion of H into Q",
            "D1_control": "canonical projection of Q onto M",
            "D1_D2_zero": True,
            "rank_D2": h_dim,
            "rank_D1": m_dim,
            "control_proves_interface_consistent": True,
            "control_is_action_derived": False,
        },
        "corrected_carrier_lift": {
            "carrier_rank": carrier,
            "degree_dimensions": [h_dim * carrier, q_dim * carrier, m_dim * carrier],
            "required_product_D2_rank": h_dim * carrier,
            "required_product_D1_rank": m_dim * carrier,
            "factorized_nilpotence_follows_from_base": True,
            "factorized_exactness_follows_from_base": True,
            "commutes_with_degreewise_identical_projectors": True,
            "nonfactorized_action_requires_K444_typed_square_checks": True,
            "K444_square_count": sum(
                key.startswith("degree_") for key in square["actual_arrow_counts"]
            ),
        },
        "decision": {
            "minimal_completion_interface_derived": True,
            "selected_action_completion_constructed": False,
            "canonical_adjoint_obstruction_respected": obstruction["decision"]["canonical_adjoint_completion_rejected"],
            "source_action_rejected": False,
            "next_exact_input": "Derive an action-owned L with rank(LB)=70 and an independent action-owned D2 of rank 21 satisfying (LB)D2=0; then identify the boundary-carrier action and run both K444 typed square checks.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating the logical direct-sum control as coefficients selected by Weinstein's action.",
            "strongest_contrary_construction": "Many reductions L can make LB surjective; B's full column rank alone singles out none of them and supplies no D2.",
            "weakest_reproducibility_seam": "The interface is finite-dimensional linear algebra; the open seam is source authentication of L, D2 and the carrier action, not arithmetic.",
        },
        "controls": {
            "producer": "tests/channel-swings/k587_k77_action_kt_completion_interface.py",
            "probe": "tests/channel-swings/k587_k77_action_kt_completion_interface_probe.py",
        },
        "claim_ceiling": "For the current 21-to-91-to-70 base dimensions, an action-owned exact completion requires a rank-70 D1=LB and a rank-21 D2 with (LB)D2=0; these conditions are sufficient for base exactness, and their identity-512 lift has the K442 ranks. The artifact does not supply L or D2, authenticate factorization, construct the selected action's BV/KT complex, or move source, ledger, canon, paper, public posture, novelty, prediction, confirmation or a physical GU verdict.",
    }
    validate(payload)
    return payload


def validate(payload: dict[str, Any]) -> None:
    base = payload["base_completion_interface"]
    lift = payload["corrected_carrier_lift"]
    control = payload["logical_control"]
    decision = payload["decision"]
    if base["dimensions"] != {"H": 21, "Q": 91, "M": 70, "R": 1470}:
        raise AssertionError("base dimensions changed")
    if base["observed_B_rank"] != 91 or base["required_D1_rank"] != 70 or base["required_D2_rank"] != 21:
        raise AssertionError("base rank interface changed")
    if base["required_kernel_dimension_if_D1_surjective"] != 21:
        raise AssertionError("kernel dimension changed")
    if base["B_injective_is_sufficient_to_select_L"] or base["euclidean_adjoint_supplies_D2"] or base["coefficient_bearing_inputs_present"]:
        raise AssertionError("invented completion data")
    if not control["D1_D2_zero"] or control["control_is_action_derived"]:
        raise AssertionError("logical control boundary changed")
    if lift["degree_dimensions"] != [10752, 46592, 35840] or lift["required_product_D2_rank"] != 10752 or lift["required_product_D1_rank"] != 35840:
        raise AssertionError("corrected-carrier lift changed")
    if not decision["minimal_completion_interface_derived"] or decision["selected_action_completion_constructed"] or decision["source_action_rejected"]:
        raise AssertionError("K587 decision changed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
