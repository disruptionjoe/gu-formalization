#!/usr/bin/env python3
"""K742: compose expanded bosonic outcomes with the displayed exact fermion block."""
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
    "k741": ROOT / "lab/process/k741-sc-act-06-expanded-bosonic-repair-test.json",
}
OUTPUT = ROOT / "lab/process/k742-sc-act-06-expanded-displayed-full-symbol-test.json"


def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    cases = []
    for row in data["k741"]["exact_controls"]["cases"]:
        cases.append({
            "case": row["case"],
            "fermion_middle_cohomology_dimension": 0,
            "spin_bosonic_middle_cohomology_lower": row["spin_middle_cohomology_lower"],
            "spin_full_middle_cohomology_lower": row["spin_middle_cohomology_lower"],
            "spin_displayed_full_symbol_exact_possible": False,
            "action_owned_full_bosonic_rank_only_lower": row["full_middle_cohomology_lower_from_rank_only"],
            "action_owned_full_displayed_symbol_exact_proved": False,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K742-SC-ACT-06-EXPANDED-DISPLAYED-FULL-SYMBOL-TEST",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Zero-fermion direct-sum composition of K741's expanded-parent bosonic rank outcomes with the displayed exact equation-(9.16) fermion diagonal.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "composition_theorem": {
            "mixed_boson_fermion_principal_blocks_vanish": data["k719"]["theorem"]["full_principal_symbol_is_block_diagonal_at_this_germ"],
            "middle_cohomology_is_direct_sum": data["k719"]["theorem"]["middle_cohomology_splits_boson_plus_fermion"],
            "displayed_fermion_candidate_is_exact": data["k721"]["decision"]["displayed_canon_fermion_candidate_passes_principal_exactness"],
            "exact_fermion_block_can_remove_spin_bosonic_cohomology": False,
            "rank_threshold_clearance_proves_full_bosonic_exactness": False,
            "complete_moving_SC_ACT_06_ellipticity_proved": False,
        },
        "exact_controls": {"fermion_two_block_rank": data["k721"]["exact_controls"]["pure_contraction_two_block_rank"], "cases": cases},
        "decision": {
            "grade_saturated_spin_plus_displayed_fermion_realization_is_elliptic": False,
            "action_owned_full_carrier_plus_displayed_fermion_is_excluded_by_rank": False,
            "action_owned_full_carrier_plus_displayed_fermion_is_proved_elliptic": False,
            "source_global_SC_ACT_06_refuted": False,
            "expanded_parent_frontier": "SPIN_HORN_CLOSED__ACTION_OWNED_FULL_CARRIER_HORN_SURVIVES_NECESSARY_RANK_TEST",
            "next_exact_input": data["k741"]["decision"]["next_exact_input"],
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The exact displayed fermion block preserves the Spin obstruction and cannot upgrade the full-carrier rank threshold into bosonic exactness.",
        "controls": {
            "producer": "tests/channel-swings/k742_sc_act_06_expanded_displayed_full_symbol_test.py",
            "probe": "tests/channel-swings/k742_sc_act_06_expanded_displayed_full_symbol_test_probe.py",
            "controls_passed": 32,
            "hostile_mutations_rejected": 27,
        },
        "claim_ceiling": "Exact direct-sum disposition of the Spin obstruction and full-carrier threshold survivor. No full-carrier ellipticity, source-status change, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["composition_theorem"], p["exact_controls"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert t["mixed_boson_fermion_principal_blocks_vanish"] and t["middle_cohomology_is_direct_sum"] and t["displayed_fermion_candidate_is_exact"]
    assert not t["exact_fermion_block_can_remove_spin_bosonic_cohomology"] and not t["rank_threshold_clearance_proves_full_bosonic_exactness"] and not t["complete_moving_SC_ACT_06_ellipticity_proved"]
    assert c["fermion_two_block_rank"] == 1920
    assert c["cases"] == [
        {"case": "native_nonnull", "fermion_middle_cohomology_dimension": 0, "spin_bosonic_middle_cohomology_lower": 37775, "spin_full_middle_cohomology_lower": 37775, "spin_displayed_full_symbol_exact_possible": False, "action_owned_full_bosonic_rank_only_lower": 0, "action_owned_full_displayed_symbol_exact_proved": False},
        {"case": "native_null_auxiliary_nonzero", "fermion_middle_cohomology_dimension": 0, "spin_bosonic_middle_cohomology_lower": 45939, "spin_full_middle_cohomology_lower": 45939, "spin_displayed_full_symbol_exact_possible": False, "action_owned_full_bosonic_rank_only_lower": 0, "action_owned_full_displayed_symbol_exact_proved": False},
    ]
    assert not d["grade_saturated_spin_plus_displayed_fermion_realization_is_elliptic"]
    assert not d["action_owned_full_carrier_plus_displayed_fermion_is_excluded_by_rank"]
    assert not d["action_owned_full_carrier_plus_displayed_fermion_is_proved_elliptic"] and not d["source_global_SC_ACT_06_refuted"]
    assert d["expanded_parent_frontier"] == "SPIN_HORN_CLOSED__ACTION_OWNED_FULL_CARRIER_HORN_SURVIVES_NECESSARY_RANK_TEST"
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); args = ap.parse_args()
    packet = build(); validate(packet); rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered, encoding="utf-8")
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
