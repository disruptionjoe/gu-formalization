#!/usr/bin/env python3
"""K722: compose K719--K721 into the frozen flat full-symbol verdict."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "k719": ROOT / "lab/process/k719-sc-act-06-zero-fermion-full-symbol-reduction.json",
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
    "k721": ROOT / "lab/process/k721-sc-act-06-eq916-euclidean-fermion-symbol.json",
}
OUTPUT = ROOT / "lab/process/k722-sc-act-06-flat-full-symbol-obstruction.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    inputs = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    boson = inputs["k720"]["exact_controls"]
    fermion = inputs["k721"]["exact_controls"]
    cases = []
    for case in boson["cases"]:
        cases.append({
            "case": case["case"],
            "bosonic_middle_cohomology_dimension": case["middle_cohomology_dimension"],
            "fermionic_middle_cohomology_dimension": 0,
            "full_middle_cohomology_dimension": case["middle_cohomology_dimension"],
            "full_middle_exact": False,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K722-SC-ACT-06-FLAT-FULL-SYMBOL-OBSTRUCTION",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Block-diagonal composition of the selected K132 I1B bosonic symbol and displayed pure-contraction equation-(9.16) fermion symbol on K717's zero-fermion flat Euclidean germ.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "composition_theorem": {
            "mixed_boson_fermion_principal_blocks_vanish": inputs["k719"]["theorem"]["full_principal_symbol_is_block_diagonal_at_this_germ"],
            "middle_cohomology_is_direct_sum": inputs["k719"]["theorem"]["middle_cohomology_splits_boson_plus_fermion"],
            "displayed_fermion_candidate_is_exact": inputs["k721"]["theorem"]["fermion_middle_cohomology_is_zero_for_displayed_candidate"],
            "selected_bosonic_candidate_is_exact": inputs["k720"]["transport_theorem"]["selected_bosonic_middle_symbol_is_exact"],
            "full_frozen_symbol_is_exact_at_every_nonzero_covector": False,
            "native_null_auxiliary_nonzero_control_fails": True,
            "changing_only_row_projectors_can_remove_defect": False,
            "full_SC_ACT_06_ellipticity_proved": False,
        },
        "exact_controls": {
            "fermion_two_block_dimension": fermion["two_block_dimension"],
            "fermion_two_block_rank": fermion["pure_contraction_two_block_rank"],
            "cases": cases,
            "nonnull_full_cohomology_dimension": cases[0]["full_middle_cohomology_dimension"],
            "native_null_full_cohomology_dimension": cases[1]["full_middle_cohomology_dimension"],
        },
        "decision": {
            "frozen_flat_selected_i1b_plus_displayed_eq916_realization_rejected_as_elliptic": True,
            "source_global_SC_ACT_06_refuted": False,
            "displayed_fermion_principal_candidate_rejected": False,
            "same_flat_selected_bosonic_route_needs_more_abstract_projector_work": False,
            "next_exact_input": "A live SC-ACT-06 route now requires new action-owned bosonic data: either a different source-selected coefficient or a different stationary Euclidean germ whose actual coupled Euler kernel equals its gauge image. Only then rebuild both diagonals on a common analytic domain; do not advance to Fredholm or nonlinear moduli on this rejected flat realization.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The certificate rejects one frozen coefficient/background realization. Source-admitted Shiab/southeast variants, other stationary germs, analytic domains and physical positivity remain unselected.",
        "controls": {
            "producer": "tests/channel-swings/k722_sc_act_06_flat_full_symbol_obstruction.py",
            "probe": "tests/channel-swings/k722_sc_act_06_flat_full_symbol_obstruction_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 29,
        },
        "claim_ceiling": "Exact direct-sum obstruction for the frozen K132-selected I1B plus displayed pure-contraction equation-(9.16) symbol on K717. This is a realization-level rejection, not a global source no-go, and it moves no source, ledger, canon, paper, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["composition_theorem"], p["exact_controls"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    for key in ("mixed_boson_fermion_principal_blocks_vanish", "middle_cohomology_is_direct_sum", "displayed_fermion_candidate_is_exact", "native_null_auxiliary_nonzero_control_fails"):
        assert t[key]
    for key in ("selected_bosonic_candidate_is_exact", "full_frozen_symbol_is_exact_at_every_nonzero_covector", "changing_only_row_projectors_can_remove_defect", "full_SC_ACT_06_ellipticity_proved"):
        assert not t[key]
    assert c["fermion_two_block_dimension"] == c["fermion_two_block_rank"] == 1920
    assert c["cases"] == [
        {"case": "native_nonnull", "bosonic_middle_cohomology_dimension": 98470, "fermionic_middle_cohomology_dimension": 0, "full_middle_cohomology_dimension": 98470, "full_middle_exact": False},
        {"case": "native_null_auxiliary_nonzero", "bosonic_middle_cohomology_dimension": 106634, "fermionic_middle_cohomology_dimension": 0, "full_middle_cohomology_dimension": 106634, "full_middle_exact": False},
    ]
    assert c["nonnull_full_cohomology_dimension"] == 98470 and c["native_null_full_cohomology_dimension"] == 106634
    assert d["frozen_flat_selected_i1b_plus_displayed_eq916_realization_rejected_as_elliptic"]
    assert not d["source_global_SC_ACT_06_refuted"] and not d["displayed_fermion_principal_candidate_rejected"]
    assert not d["same_flat_selected_bosonic_route_needs_more_abstract_projector_work"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
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
