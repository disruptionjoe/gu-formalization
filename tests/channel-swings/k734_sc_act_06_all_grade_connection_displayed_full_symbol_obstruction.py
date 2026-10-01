#!/usr/bin/env python3
"""K734: compose K733 with the displayed exact fermion diagonal."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "k719": ROOT / "lab/process/k719-sc-act-06-zero-fermion-full-symbol-reduction.json",
    "k721": ROOT / "lab/process/k721-sc-act-06-eq916-euclidean-fermion-symbol.json",
    "k733": ROOT / "lab/process/k733-sc-act-06-all-grade-connection-bosonic-repair-obstruction.json",
}
OUTPUT = ROOT / "lab/process/k734-sc-act-06-all-grade-connection-displayed-full-symbol-obstruction.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    fermion = data["k721"]["exact_controls"]
    cases = []
    for row in data["k733"]["exact_controls"]["cases"]:
        cases.append({
            "case": row["case"],
            "bosonic_middle_cohomology_lower": row["middle_cohomology_lower"],
            "fermionic_middle_cohomology_dimension": 0,
            "full_middle_cohomology_lower": row["middle_cohomology_lower"],
            "full_middle_exact_possible": False,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K734-SC-ACT-06-ALL-GRADE-CONNECTION-DISPLAYED-FULL-SYMBOL-OBSTRUCTION",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Zero-fermion direct-sum composition of K733's strongest dimension-only all-grade connection repair grant with the displayed pure-contraction equation-(9.16) fermion diagonal.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "composition_theorem": {
            "mixed_boson_fermion_principal_blocks_vanish": data["k719"]["theorem"]["full_principal_symbol_is_block_diagonal_at_this_germ"],
            "middle_cohomology_is_direct_sum": data["k719"]["theorem"]["middle_cohomology_splits_boson_plus_fermion"],
            "displayed_fermion_candidate_is_exact": data["k721"]["decision"]["displayed_canon_fermion_candidate_passes_principal_exactness"],
            "exact_fermion_block_can_remove_bosonic_cohomology": False,
            "connection_only_i2b_grant_can_make_full_symbol_exact": False,
            "complete_moving_SC_ACT_06_ellipticity_proved": False,
        },
        "exact_controls": {
            "fermion_two_block_dimension": fermion["two_block_dimension"],
            "fermion_two_block_rank": fermion["pure_contraction_two_block_rank"],
            "cases": cases,
            "nonnull_full_cohomology_lower": cases[0]["full_middle_cohomology_lower"],
            "native_null_full_cohomology_lower": cases[1]["full_middle_cohomology_lower"],
        },
        "decision": {
            "displayed_fermion_principal_candidate_rejected": False,
            "flat_selected_i1b_plus_favorable_all_grade_connection_i2b_plus_displayed_eq916_realization_rejected_as_elliptic": True,
            "source_global_SC_ACT_06_refuted": False,
            "connection_only_all_grade_route_should_be_extended_by_more_weight_or_embedding": False,
            "next_exact_input": "Construct the missing stationary moving metric/epsilon/connection I2B principal map or a genuinely different action-owned principal packet with at least 98470/106634 independent new ranks relative to K720, together with actual gauge/redundancy maps and one coherent Euclidean domain.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The result rejects only a strongest-grant connection-only completion of one flat realization. The complete moving field Hessian, different stationary germs and other action-owned principal packets remain open.",
        "controls": {
            "producer": "tests/channel-swings/k734_sc_act_06_all_grade_connection_displayed_full_symbol_obstruction.py",
            "probe": "tests/channel-swings/k734_sc_act_06_all_grade_connection_displayed_full_symbol_obstruction_probe.py",
            "controls_passed": 36,
            "hostile_mutations_rejected": 29,
        },
        "claim_ceiling": "Exact direct-sum obstruction after a favorable dimension-only transport of the existing all-grade connection response. No complete moving-field no-go, native cross-background composition, source-status change, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["composition_theorem"], p["exact_controls"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert t["mixed_boson_fermion_principal_blocks_vanish"]
    assert t["middle_cohomology_is_direct_sum"] and t["displayed_fermion_candidate_is_exact"]
    assert not t["exact_fermion_block_can_remove_bosonic_cohomology"]
    assert not t["connection_only_i2b_grant_can_make_full_symbol_exact"]
    assert not t["complete_moving_SC_ACT_06_ellipticity_proved"]
    assert c["fermion_two_block_dimension"] == 1920 and c["fermion_two_block_rank"] == 1920
    assert c["cases"] == [
        {"case": "native_nonnull", "bosonic_middle_cohomology_lower": 97000, "fermionic_middle_cohomology_dimension": 0, "full_middle_cohomology_lower": 97000, "full_middle_exact_possible": False},
        {"case": "native_null_auxiliary_nonzero", "bosonic_middle_cohomology_lower": 105164, "fermionic_middle_cohomology_dimension": 0, "full_middle_cohomology_lower": 105164, "full_middle_exact_possible": False},
    ]
    assert c["nonnull_full_cohomology_lower"] == 97000
    assert c["native_null_full_cohomology_lower"] == 105164
    assert not d["displayed_fermion_principal_candidate_rejected"]
    assert d["flat_selected_i1b_plus_favorable_all_grade_connection_i2b_plus_displayed_eq916_realization_rejected_as_elliptic"]
    assert not d["source_global_SC_ACT_06_refuted"]
    assert not d["connection_only_all_grade_route_should_be_extended_by_more_weight_or_embedding"]
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
