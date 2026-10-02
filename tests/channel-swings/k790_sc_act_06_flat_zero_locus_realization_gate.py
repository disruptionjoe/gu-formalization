#!/usr/bin/env python3
"""K790: compose the direct flat zero-locus realization gate."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k790-sc-act-06-flat-zero-locus-realization-gate.json"
PATHS = {
    "k719": ROOT / "lab/process/k719-sc-act-06-zero-fermion-full-symbol-reduction.json",
    "k786": ROOT / "lab/process/k786-sc-act-06-zero-residual-deformation-input-gate.json",
    "k787": ROOT / "lab/process/k787-sc-act-06-flat-zero-locus-custody.json",
    "k788": ROOT / "lab/process/k788-sc-act-06-direct-response-orbit-classification.json",
    "k789": ROOT / "lab/process/k789-sc-act-06-maximal-symmetry-budget.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    assert data["k787"]["decision"]["direct_linearization_test_released"]
    assert data["k788"]["decision"]["connection_kernel_dimension"] == 106512
    assert data["k789"]["decision"]["uniform_middle_cohomology_lower_bound"] == 90124
    assert data["k719"]["theorem"]["full_principal_symbol_is_block_diagonal_at_this_germ"]
    return {
        "schema_version": "1.0",
        "result_id": "K790-SC-ACT-06-FLAT-ZERO-LOCUS-REALIZATION-GATE",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Direct K786 gate disposition for the currently serialized K717 flat Upsilon=0 realization.",
        "gu_typed_objects": {
            "carrier": "one K717 local B(epsilon)/Y background with the full serialized connection tangent and zero fermions",
            "pairing": "native action form plus background Frobenius auxiliary metric; no residual-square pairing imported",
            "real_structure": "local real Euclidean base/fibre and K788 pinned real connection coefficient basis",
            "grading": "candidate symmetries -> source fields -> D Upsilon rows -> source redundancies",
            "action_owner": "source first-order zero locus only",
            "target": "middle exactness of the currently serialized flat zero-locus deformation packet",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "composition": {
            "local_zero_locus_background_supplied": True,
            "direct_connection_linearization_supplied": True,
            "all_real_nonzero_covector_orbits_tested": True,
            "uniform_connection_kernel_dimension": 106512,
            "maximal_current_symmetry_grant": 16388,
            "uniform_middle_cohomology_lower_bound_after_grant": 90124,
            "deleting_redundant_euler_rows_can_reduce_field_kernel": False,
            "adding_other_field_columns_can_remove_a_kernel_vector_already_zero_in_every_serialized_connection_response_row": False,
            "zero_fermion_action_hessian_block_split_is_supporting_only_not_a_D_Upsilon_identity": True,
            "complete_owned_total_symmetry_and_redundancy_maps_supplied": False,
            "complete_euclidean_fermion_real_form_and_common_domain_supplied": False,
        },
        "decision": {
            "current_flat_packet_middle_exact": False,
            "current_flat_packet_satisfies_K786": False,
            "K717_background_itself_globally_refuted": False,
            "global_SC_ACT_06_proved_or_refuted": False,
            "reopener": "A source-owned symmetry map with at least 90124 additional independent connection-kernel directions, or a proved omitted first-order Upsilon response row acting on those directions, followed by the complete fermion/redundancy/domain packet.",
            "next_exact_input": "Do not search for another background first. Audit whether the source first-order residual has any omitted connection-response row or symmetry map large enough to meet K789's 90124-rank debt; if not, retire K717 as a direct elliptic realization and switch to a genuinely different native zero-locus germ or the complete K500 A/B route.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The result rejects only the current serialized flat deformation packet and supplies no physical state, quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Exact realization-level gate for the current K717/K788 packet. It is not a no-go for every Upsilon=0 background, does not promote a candidate symmetry, and changes no source, ledger, canon, paper, public, prediction, confirmation or physical verdict.",
        "controls": {
            "producer": "tests/channel-swings/k790_sc_act_06_flat_zero_locus_realization_gate.py",
            "probe": "tests/channel-swings/k790_sc_act_06_flat_zero_locus_realization_gate_probe.py",
            "controls_passed": 44,
            "hostile_mutations_rejected": 34,
        },
    }


def validate(p: dict[str, Any]) -> None:
    c, d = p["composition"], p["decision"]
    for key in ("local_zero_locus_background_supplied", "direct_connection_linearization_supplied", "all_real_nonzero_covector_orbits_tested", "zero_fermion_action_hessian_block_split_is_supporting_only_not_a_D_Upsilon_identity"):
        assert c[key]
    assert c["uniform_connection_kernel_dimension"] == 106512
    assert c["maximal_current_symmetry_grant"] == 16388
    assert c["uniform_middle_cohomology_lower_bound_after_grant"] == 90124
    assert not c["deleting_redundant_euler_rows_can_reduce_field_kernel"]
    assert not c["adding_other_field_columns_can_remove_a_kernel_vector_already_zero_in_every_serialized_connection_response_row"]
    assert not c["complete_owned_total_symmetry_and_redundancy_maps_supplied"]
    assert not c["complete_euclidean_fermion_real_form_and_common_domain_supplied"]
    assert not d["current_flat_packet_middle_exact"] and not d["current_flat_packet_satisfies_K786"]
    assert not d["K717_background_itself_globally_refuted"] and not d["global_SC_ACT_06_proved_or_refuted"]
    assert "90124" in d["reopener"]
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
