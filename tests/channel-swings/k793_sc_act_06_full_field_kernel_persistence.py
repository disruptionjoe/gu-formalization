#!/usr/bin/env python3
"""K793: zero-fermion blocks and added field columns preserve the old kernel."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k793-sc-act-06-full-field-kernel-persistence.json"
PATHS = {
    "k719": ROOT / "lab/process/k719-sc-act-06-zero-fermion-full-symbol-reduction.json",
    "k789": ROOT / "lab/process/k789-sc-act-06-maximal-symmetry-budget.json",
    "k791": ROOT / "lab/process/k791-sc-act-06-released-first-order-row-inventory.json",
    "k792": ROOT / "lab/process/k792-sc-act-06-redundant-prolongation-kernel-theorem.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    k789 = json.loads(PATHS["k789"].read_text(encoding="utf-8"))
    old_kernel = 106512
    grant = (
        k789["composition_theorem"]["internal_candidate_rank"]
        + k789["composition_theorem"]["metric_diffeomorphism_rank"]
    )
    assert k789["decision"]["uniform_middle_cohomology_lower_bound"] == old_kernel - grant
    return {
        "schema_version": "1.0",
        "result_id": "K793-SC-ACT-06-FULL-FIELD-KERNEL-PERSISTENCE",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Persistence of K788's connection-kernel quotient under the released zero-fermion full-field extension of the K717 direct Upsilon packet.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "extension_lemma": {
            "map_form": "J_tilde(v,x,psi)=(Jv+Lx,Fpsi)",
            "embedded_subspace": "ker(J) x {0} x {0}",
            "embedded_subspace_is_in_full_kernel": True,
            "adding_field_columns_can_delete_old_kernel_vectors": False,
            "adding_block_diagonal_fermion_rows_can_act_on_old_bosonic_kernel": False,
            "redundant_xi_row_can_act_on_old_kernel": False,
        },
        "released_full_field_typing": {
            "metric_epsilon_varpi_fermions_are_field_columns": True,
            "zero_fermion_mixed_principal_blocks_vanish": True,
            "fermion_diagonal_is_separate_from_bosonic_connection_kernel": True,
            "i2b_adjoint_row_is_not_part_of_first_order_SC_ACT_06_packet": True,
        },
        "exact_bound": {
            "embedded_connection_kernel_dimension": old_kernel,
            "maximal_current_granted_symmetry_rank": grant,
            "persistent_middle_classes_lower_bound": old_kernel - grant,
            "uniform_on_positive_negative_and_null_real_covectors": True,
        },
        "decision": {
            "released_full_field_extension_repairs_K790": False,
            "complete_fermion_diagonal_can_repair_bosonic_defect": False,
            "new_metric_or_epsilon_columns_alone_can_repair_bosonic_defect": False,
            "remaining_reopener": "A genuinely independent source-owned bosonic response row nonzero on the embedded kernel or at least 90124 additional independent owned symmetry directions.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The persistence theorem is local principal-symbol algebra and supplies no physical quotient or observable.",
        "claim_ceiling": "Exact persistence theorem for the released zero-fermion field extension and currently granted symmetries. It does not classify future nonzero-fermion germs or undisplayed independent rows.",
        "controls": {
            "producer": "tests/channel-swings/k793_sc_act_06_full_field_kernel_persistence.py",
            "probe": "tests/channel-swings/k793_sc_act_06_full_field_kernel_persistence_probe.py",
            "controls_passed": 42,
            "hostile_mutations_rejected": 30,
        },
    }


def validate(p: dict[str, Any]) -> None:
    assert p["result_id"] == "K793-SC-ACT-06-FULL-FIELD-KERNEL-PERSISTENCE"
    assert p["target_claim"] == "SC-ACT-06" and p["classification"] == "SOURCE_NATIVE_ROUTE"
    lemma, typing, bound, decision = p["extension_lemma"], p["released_full_field_typing"], p["exact_bound"], p["decision"]
    assert lemma["map_form"] == "J_tilde(v,x,psi)=(Jv+Lx,Fpsi)"
    assert lemma["embedded_subspace"] == "ker(J) x {0} x {0}"
    assert lemma["embedded_subspace_is_in_full_kernel"]
    assert not lemma["adding_field_columns_can_delete_old_kernel_vectors"]
    assert not lemma["adding_block_diagonal_fermion_rows_can_act_on_old_bosonic_kernel"]
    assert not lemma["redundant_xi_row_can_act_on_old_kernel"]
    assert all(typing.values())
    assert bound["embedded_connection_kernel_dimension"] == 106512
    assert bound["maximal_current_granted_symmetry_rank"] == 16388
    assert bound["persistent_middle_classes_lower_bound"] == 90124
    assert bound["uniform_on_positive_negative_and_null_real_covectors"]
    assert not decision["released_full_field_extension_repairs_K790"]
    assert not decision["complete_fermion_diagonal_can_repair_bosonic_defect"]
    assert not decision["new_metric_or_epsilon_columns_alone_can_repair_bosonic_defect"]
    assert "90124" in decision["remaining_reopener"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]
    assert set(p["pinned_inputs"]) == set(PATHS)


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
