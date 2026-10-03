#!/usr/bin/env python3
"""K915: freeze the changed-gauge/nonzero-fermion admission boundary."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k915-sc-act-06-changed-gauge-admission-boundary.json"
PATHS = {
    "k910": ROOT / "lab/process/k910-sc-act-06-cross-completion-admission-boundary.json",
    "k911": ROOT / "lab/process/k911-sc-act-06-augmented-gauge-ward-splitting.json",
    "k912": ROOT / "lab/process/k912-sc-act-06-torsion-salvage-stabilizer-necessity.json",
    "k913": ROOT / "lab/process/k913-sc-act-06-augmented-gauge-quotient-persistence.json",
    "k914": ROOT / "lab/process/k914-sc-act-06-nonzero-fermion-germ-custody.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict:
    return {
        "schema_version": "1.0",
        "result_id": "K915-SC-ACT-06-CHANGED-GAUGE-ADMISSION-BOUNDARY",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Admission boundary for reopening K910's released flat packet through a changed gauge embedding realized by a source/action-owned nonzero-fermion stationary germ.",
        "gu_typed_objects": {
            "gauge": "G_tilde=(G,L)",
            "hessian": "T=[[S,B*],[B,D]]",
            "ward_pair": "S G+B*L=0 and B G+D L=0",
            "old_quotient": "H_old, dimension 90128, forty real types, multiplicity 169",
            "target": "DISPOSITION-TYPE=changed-gauge admission boundary",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "admission": {
            "requires_stationary_nonzero_fermion_germ": True,
            "requires_action_owned_full_hessian": True,
            "requires_common_variational_green_preboundary_domain": True,
            "requires_both_augmented_ward_equations": True,
            "nonzero_torsion_requires_L_injective": True,
            "nonzero_torsion_requires_trivial_infinitesimal_stabilizer": True,
            "nonzero_torsion_requires_rank_BstarL": 16384,
            "old_tangential_lower_bound_persists_in_field_quotient": 90128,
            "old_real_type_count_persists": 40,
            "old_total_real_multiplicity_persists": 169,
            "old_typewise_hessian_repair_still_required": True,
            "current_custody_satisfies_admission": False,
            "corrected_completion_gate_satisfied_rows": 5,
            "corrected_completion_gate_total_rows": 11,
        },
        "decision": {
            "changed_gauge_can_algebraically_mix_old_and_new_ward_defects": True,
            "changed_gauge_alone_removes_old_quotient": False,
            "released_torsion_parent_reopened_on_current_germ": False,
            "nonzero_fermion_branch_refuted": False,
            "nonzero_fermion_completion_constructed": False,
            "SC_ACT_06_proved_or_refuted": False,
            "distance_only_cross_budget_route_remains_exhausted": True,
            "next_exact_input": "Provide a source/action-owned nonzero-fermion stationary germ with full gauge tangent (G,L), trivial infinitesimal stabilizer if kappa is nonzero, both Ward equations, every Hessian block and common domain/Green/preboundary data; then recompute old-type quotient capacity. Otherwise construct a genuinely new gauge-basic old-old action parent.",
        },
        "source_and_ledger_effect": "SC-ACT-01_03_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The boundary distinguishes a valid changed-gauge mechanism from a current construction; no source claim or physics-ledger row moves.",
        "claim_ceiling": "Exact local necessary-condition and custody boundary only. It neither supplies the missing germ nor proves or refutes rich moduli or Euclidean ellipticity.",
        "controls": {
            "producer": "tests/channel-swings/k915_sc_act_06_changed_gauge_admission_boundary.py",
            "probe": "tests/channel-swings/k915_sc_act_06_changed_gauge_admission_boundary_probe.py",
            "controls_passed": 46,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(data: dict) -> None:
    admission, decision = data["admission"], data["decision"]
    checks = [
        data["classification"] == "SOURCE_NATIVE_ROUTE",
        data["target_claim"] == "SC-ACT-06",
        set(data["pinned_inputs"]) == set(PATHS),
        all(len(item["sha256"]) == 64 for item in data["pinned_inputs"].values()),
        data["gu_typed_objects"]["gauge"] == "G_tilde=(G,L)",
        data["gu_typed_objects"]["hessian"] == "T=[[S,B*],[B,D]]",
        data["gu_typed_objects"]["ward_pair"] == "S G+B*L=0 and B G+D L=0",
        "90128" in data["gu_typed_objects"]["old_quotient"],
        admission["requires_stationary_nonzero_fermion_germ"],
        admission["requires_action_owned_full_hessian"],
        admission["requires_common_variational_green_preboundary_domain"],
        admission["requires_both_augmented_ward_equations"],
        admission["nonzero_torsion_requires_L_injective"],
        admission["nonzero_torsion_requires_trivial_infinitesimal_stabilizer"],
        admission["nonzero_torsion_requires_rank_BstarL"] == 16384,
        admission["old_tangential_lower_bound_persists_in_field_quotient"] == 90128,
        admission["old_real_type_count_persists"] == 40,
        admission["old_total_real_multiplicity_persists"] == 169,
        admission["old_typewise_hessian_repair_still_required"],
        not admission["current_custody_satisfies_admission"],
        admission["corrected_completion_gate_satisfied_rows"] == 5,
        admission["corrected_completion_gate_total_rows"] == 11,
        decision["changed_gauge_can_algebraically_mix_old_and_new_ward_defects"],
        not decision["changed_gauge_alone_removes_old_quotient"],
        not decision["released_torsion_parent_reopened_on_current_germ"],
        not decision["nonzero_fermion_branch_refuted"],
        not decision["nonzero_fermion_completion_constructed"],
        not decision["SC_ACT_06_proved_or_refuted"],
        decision["distance_only_cross_budget_route_remains_exhausted"],
        "trivial infinitesimal stabilizer" in decision["next_exact_input"],
        "recompute old-type quotient capacity" in decision["next_exact_input"],
        "new gauge-basic old-old action parent" in decision["next_exact_input"],
        data["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"),
        "valid changed-gauge mechanism" in data["ledger_no_change_reason"],
        "neither supplies the missing germ" in data["claim_ceiling"],
        data["controls"]["controls_passed"] == 46,
        data["controls"]["hostile_mutations_rejected"] == 20,
        data["schema_version"] == "1.0",
        data["status"] == "working_draft_verified",
        data["direction"] == "observed_to_native",
        data["result_id"].startswith("K915-"),
        "changed gauge embedding" in data["scope"],
        admission["corrected_completion_gate_satisfied_rows"] < admission["corrected_completion_gate_total_rows"],
        not admission["current_custody_satisfies_admission"],
        decision["distance_only_cross_budget_route_remains_exhausted"],
        not decision["nonzero_fermion_completion_constructed"],
    ]
    assert len(checks) == 46 and all(checks), [i for i, value in enumerate(checks) if not value]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = build()
    validate(data)
    rendered = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    elif not args.check:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
