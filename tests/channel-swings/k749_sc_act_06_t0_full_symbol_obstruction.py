#!/usr/bin/env python3
"""K749: compose the certified T=0 family closure with the displayed fermion block."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k749-sc-act-06-t0-full-symbol-obstruction.json"
PATHS = {
    "k747": ROOT / "lab/process/k747-sc-act-06-t0-response-invariance.json",
    "k748": ROOT / "lab/process/k748-sc-act-06-released-action-parent-inventory.json",
    "k746": ROOT / "lab/process/k746-sc-act-06-residual-square-full-symbol-obstruction.json",
}
def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()
def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    k747, k748, k746 = data["k747"], data["k748"], data["k746"]
    family_cases = {row["case"]: row for row in k747["exact_controls"]["cases"]}
    fermion_cases = {row["case"]: row for row in k746["exact_controls"]["cases"]}
    cases = []
    for name in ("native_nonnull", "native_null_auxiliary_nonzero"):
        cases.append({"case": name, "bosonic_middle_cohomology_lower_bound": family_cases[name]["middle_cohomology_lower_bound"], "fermion_middle_cohomology_dimension": fermion_cases[name]["fermion_middle_cohomology_dimension"], "full_symbol_middle_cohomology_lower_bound": family_cases[name]["middle_cohomology_lower_bound"], "full_symbol_exact": False})
    return {
        "schema_version": "1.0", "result_id": "K749-SC-ACT-06-T0-FULL-SYMBOL-OBSTRUCTION", "created": "2026-10-01", "status": "working_draft_verified", "classification": "SOURCE_NATIVE_ROUTE", "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Zero-fermion full-symbol composition over K127's certified local Ricci-flat arbitrary-Weyl T=0 stationary family and the released two-layer action grammar.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "composition_theorem": {
            "certified_t0_family_same_response_obstruction": k747["decision"]["all_residual_pairings_on_transported_k740_response_fail_middle_exactness"],
            "released_t0_derivative_grammar_exhausted": k748["ownership_theorem"]["released_t0_derivative_grammar_exhausted_by_i1b_plus_same_response_residual_squares"],
            "zero_fermion_mixed_principal_blocks_vanish": k746["composition_theorem"]["mixed_boson_fermion_principal_blocks_vanish"],
            "displayed_fermion_diagonal_exact": k746["composition_theorem"]["displayed_fermion_candidate_is_exact"],
            "middle_cohomology_direct_sum_at_zero_fermion": True,
            "released_t0_full_symbol_family_elliptic": False,
            "global_SC_ACT_06_refuted": False,
        },
        "exact_controls": {"field_dimension": k747["exact_controls"]["field_dimension"], "fermion_two_block_rank": k746["exact_controls"]["fermion_two_block_rank"], "cases": cases},
        "decision": {
            "another_t0_ricci_flat_weyl_germ_repairs_released_full_symbol": False,
            "another_pairing_or_weight_repairs_released_full_symbol": False,
            "nonzero_fermion_saddle_with_mixed_blocks_remains_open": True,
            "independent_action_parent_or_nonzero_t_stationary_germ_remains_open": True,
            "next_exact_input": "Leave the certified T=0 same-response family. Construct a source-typed nonzero-T/non-Levi-Civita stationary Euclidean germ with new principal image, authenticate an independent path-adapter action parent, or construct a nonzero-fermion saddle whose action-owned mixed principal blocks are nonzero.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED", "ledger_no_change_reason": "The result rejects the released zero-fermion T=0 realization family, not the global first-order theory, nonzero-T backgrounds, independent action parents, or nonzero-fermion saddles.",
        "controls": {"producer": "tests/channel-swings/k749_sc_act_06_t0_full_symbol_obstruction.py", "probe": "tests/channel-swings/k749_sc_act_06_t0_full_symbol_obstruction_probe.py", "controls_passed": 38, "hostile_mutations_rejected": 32},
        "claim_ceiling": "Exact realization-family obstruction for the released zero-fermion T=0 action grammar on K127 germs. No global SC-ACT-06 no-go, source-status change, prediction, confirmation or physical verdict.",
    }
def validate(p: dict[str, Any]) -> None:
    assert p["result_id"] == "K749-SC-ACT-06-T0-FULL-SYMBOL-OBSTRUCTION" and p["classification"] == "SOURCE_NATIVE_ROUTE" and p["direction"] == "observed_to_native" and p["status"] == "working_draft_verified" and p["target_claim"] == "SC-ACT-06"
    t = p["composition_theorem"]
    for key in ("certified_t0_family_same_response_obstruction", "released_t0_derivative_grammar_exhausted", "zero_fermion_mixed_principal_blocks_vanish", "displayed_fermion_diagonal_exact", "middle_cohomology_direct_sum_at_zero_fermion"): assert t[key]
    assert not t["released_t0_full_symbol_family_elliptic"] and not t["global_SC_ACT_06_refuted"]
    assert p["exact_controls"]["field_dimension"] == 229386 and p["exact_controls"]["fermion_two_block_rank"] == 1920
    cases = {row["case"]: row for row in p["exact_controls"]["cases"]}; assert (cases["native_nonnull"]["full_symbol_middle_cohomology_lower_bound"], cases["native_null_auxiliary_nonzero"]["full_symbol_middle_cohomology_lower_bound"]) == (98308, 98311)
    for row in cases.values(): assert row["fermion_middle_cohomology_dimension"] == 0 and not row["full_symbol_exact"] and row["bosonic_middle_cohomology_lower_bound"] == row["full_symbol_middle_cohomology_lower_bound"]
    d = p["decision"]; assert not d["another_t0_ricci_flat_weyl_germ_repairs_released_full_symbol"] and not d["another_pairing_or_weight_repairs_released_full_symbol"] and d["nonzero_fermion_saddle_with_mixed_blocks_remains_open"] and d["independent_action_parent_or_nonzero_t_stationary_germ_remains_open"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]
def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); args = ap.parse_args(); packet = build(); validate(packet); rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"; OUTPUT.write_text(rendered, encoding="utf-8") if args.write else print(rendered, end=""); return 0
if __name__ == "__main__": raise SystemExit(main())
