#!/usr/bin/env python3
"""K594 selected-I1B third-jet serialization and corrected-carrier type audit."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k594-k77-native-third-jet-carrier-typing.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text())


def build() -> dict:
    k122 = strict("lab/process/selected-k122-native-i1b-cubic-and-preboundary-owner-decomposition.json")
    k124 = strict("lab/process/selected-k124-native-i1b-principal-tt-evaluator-and-cartan-gate.json")
    k441 = strict("lab/process/k441-k77-moving-corrected-boundary-transport.json")
    k589 = strict("lab/process/k589-k77-action-kt-exact-completion.json")
    k590 = strict("lab/process/k590-k77-corrected-carrier-completion-squares.json")
    k592 = strict("lab/process/k592-k77-hessian-carrier-coupling-identifiability.json")

    coefficients = k124["native_coefficients"]
    controls = {
        "D3_t_t_t": str(k122["fixed_metric_full_i1b"]["D3_t_t_t"]),
        "D3_t_v_v_over_native_norm": k122["fixed_metric_full_i1b"]["D3_t_v_v_over_native_norm"],
        "C_t_h_h_principal": coefficients["C_t_h_h_principal"],
        "C_t_h_v_principal": coefficients["C_t_h_v_principal"],
        "K124_C_t_h_v_evaluations": k124["exact_census"]["C_t_h_v_evaluations"],
        "K124_C_t_h_v_failures": k124["exact_census"]["C_t_h_v_failures"],
    }
    assert Fraction(controls["D3_t_t_t"]) == 8736
    assert Fraction(controls["D3_t_v_v_over_native_norm"]) == Fraction(-56, 3)
    assert controls["K124_C_t_h_v_evaluations"] == 120 and controls["K124_C_t_h_v_failures"] == 0

    field_dims = {"t_radial": 1, "h_TT_packet": 20, "v_vertical_normals": 10}
    kt_dims = k589["exact_completion"]["dimensions"]
    carrier_rank = k441["factorized_transport"]["spectral_block_ranks"]
    carrier_rank = sum(carrier_rank)
    lifted_dims = k590["factorized_completion"]["degree_dimensions"]
    assert carrier_rank == 512 and kt_dims == [21, 91, 70]
    assert lifted_dims == [21 * 512, 91 * 512, 70 * 512]

    return {
        "schema_version": "1.0",
        "result_id": "K594-K77-NATIVE-THIRD-JET-CARRIER-TYPING",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The selected first bosonic action's already-owned native third Frechet slots, tested for whether they canonically define the field-dependent endomorphisms required on K441's corrected rank-512 carrier over K589's finite KT degree sectors.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "carrier": "native selected-I1B field tangent in the serialized radial/TT/vertical packet, versus K441's distinct corrected boundary carrier E of rank 512",
            "pairing": "selected action third derivative is a symmetric scalar trilinear form; K441 uses its transported positive boundary pairing",
            "real_structure": "selected real K77 field packet and real rank-512 boundary transport, with no identified intertwiner between them",
            "grading": "native field slots t/h/v versus K589 degree sectors H^21,Q^91,M^70",
            "action_owner": "SC-ACT-01 selected I1B owns the serialized native trilinear slots; it does not thereby own a boundary-carrier representation",
            "result": "third-jet/corrected-carrier typing boundary MAP-TYPE=variational-soldering-audit",
            "target": "field-dependent deformations of K590's D2 tensor I_512 and D1 tensor I_512",
        },
        "selected_action_third_jet": {
            "native_field_packet_dimensions": field_dims,
            "serialized_coefficients": controls,
            "tensor_type": "D3I1B_phi:T_phi F x T_phi F x T_phi F -> R, equivalently delta_phi maps to a symmetric bilinear T_phi F x T_phi F -> R",
            "actual_selected_native_third_action_jet_serialized": True,
            "complete_full_field_third_jet_serialized": False,
            "K592_identifiability_boundary_preserved": not k592["decision"]["actual_selected_third_action_jet_tested"],
        },
        "corrected_carrier_target": {
            "K589_degree_dimensions": kt_dims,
            "K441_carrier_rank": carrier_rank,
            "K590_lifted_degree_dimensions": lifted_dims,
            "required_D2_deformation_type": "delta D2 in Hom(H^21 tensor E,Q^91 tensor E)",
            "required_D1_deformation_type": "delta D1 in Hom(Q^91 tensor E,M^70 tensor E)",
            "required_projector_test": "(I tensor Pi) delta D - delta D (I tensor Pi)=0 on each typed square",
        },
        "type_audit": {
            "native_third_jet_is_scalar_trilinear": True,
            "corrected_coupling_requires_carrier_endomorphism_valued_degree_arrow": True,
            "field_to_carrier_soldering_map_serialized": False,
            "carrier_to_field_injection_serialized": False,
            "degree_sector_to_native_field_map_serialized": False,
            "action_Riesz_map_on_K441_pairing_serialized": False,
            "canonical_composition_exists_from_current_inputs": False,
            "dimension_mismatch_alone_is_not_a_no_go": True,
            "minimum_missing_interface": [
                "a selected field parameter direction delta_phi",
                "typed injections of the K589 degree-sector carrier factors into the native action tangent",
                "the action pairing/Riesz identification returning the varied slot to the target degree sector",
                "compatibility of those maps with K441's transported projector and K589's D2/D1 composition",
            ],
        },
        "decision": {
            "selected_native_third_action_jet_tested": True,
            "selected_third_jet_defines_K441_endomorphism": False,
            "K590_nonfactorized_square_test_released": False,
            "K590_factorized_completion_retracted": False,
            "selected_source_action_rejected": False,
            "route_effect": "K592's request is now split: the selected action's native third jet is partly serialized, but the K441/K589 soldering interface is the exact next input. No 512-by-512 commutator is well typed before that interface exists.",
            "next_exact_input": "Construct one action-owned field-to-boundary soldering packet for a declared native variation and K589 degree arrow, then evaluate both typed projector commutators; otherwise continue a disjoint falsification route without inventing the map.",
        },
        "source_and_ledger_context": {
            "source_claims": ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06", "SC-META-53"],
            "physics_rows": ["LT-SM8", "LT-GR6b", "RA-F1", "AC-F1"],
            "ledger": "lab/process/conditional-physics-ledger-v0.263.json",
            "source_polarity_effect": "none",
            "ledger_effect": "none",
        },
        "preflight_bookend": {
            "route_comparison": "Reuse the selected action's exact native cubic bank before attempting any expanded corrected-carrier matrix; first check whether the variational tensor and target arrow share an owned carrier.",
            "retrieval_collision_result": "K122/K124 already serialize nonzero selected-I1B third derivatives, while K441/K589/K590 serialize a different boundary/KT product. No predecessor supplies their soldering map.",
            "strongest_alternative": "A direct full-field third differentiation remains useful, but cannot by itself turn a scalar action tensor into the required rank-512 carrier endomorphism.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling the missing soldering interface a zero third jet, or treating native t/h/v coefficients as entries of a 512-by-512 action-selected matrix.",
            "strongest_contrary_construction": "A future action-owned injection/Riesz/projection packet could map the nonzero native cubic into either a projector-compatible or projector-obstructing corrected-carrier coupling.",
            "weakest_reproducibility_seam": "The current audit proves a type boundary, not nonexistence of a natural geometric soldering map outside the serialized repository evidence.",
        },
        "claim_ceiling": "Exact selected-action type audit: nonzero native I1B third derivatives are already serialized, including D3_ttt=8736, D3_tvv=-(56/3)<V,*V>, the K124 TT coefficient and 120 zero mixed TT/vertical evaluations. They are scalar native-field trilinears, not owned endomorphisms of K441's corrected rank-512 carrier or deformations of K589's H-Q-M arrows. The missing field/carrier soldering and Riesz packet prevents either K444 square from being evaluated. This does not show the map is absent, retract K590, reject the source action, or move source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusions.",
    }


def validate(payload: dict) -> None:
    jet = payload["selected_action_third_jet"]
    target = payload["corrected_carrier_target"]
    audit = payload["type_audit"]
    decision = payload["decision"]
    assert jet["actual_selected_native_third_action_jet_serialized"] and not jet["complete_full_field_third_jet_serialized"]
    assert jet["serialized_coefficients"]["D3_t_t_t"] == "8736"
    assert jet["serialized_coefficients"]["D3_t_v_v_over_native_norm"] == "-56/3"
    assert target["K589_degree_dimensions"] == [21, 91, 70] and target["K441_carrier_rank"] == 512
    assert target["K590_lifted_degree_dimensions"] == [10752, 46592, 35840]
    assert audit["native_third_jet_is_scalar_trilinear"] and audit["corrected_coupling_requires_carrier_endomorphism_valued_degree_arrow"]
    assert not any(audit[key] for key in ("field_to_carrier_soldering_map_serialized", "carrier_to_field_injection_serialized", "degree_sector_to_native_field_map_serialized", "action_Riesz_map_on_K441_pairing_serialized", "canonical_composition_exists_from_current_inputs"))
    assert decision["selected_native_third_action_jet_tested"] and not decision["selected_third_jet_defines_K441_endomorphism"]
    assert not decision["K590_nonfactorized_square_test_released"] and not decision["K590_factorized_completion_retracted"] and not decision["selected_source_action_rejected"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
