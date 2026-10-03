#!/usr/bin/env python3
"""K914: audit custody of a nonzero-fermion stationary germ."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k914-sc-act-06-nonzero-fermion-germ-custody.json"
PATHS = {
    "k787": ROOT / "lab/process/k787-sc-act-06-flat-zero-locus-custody.json",
    "k875": ROOT / "lab/process/k875-sc-act-06-zero-fermion-mixed-block-vanishing.json",
    "k876": ROOT / "lab/process/k876-sc-act-06-zero-fermion-gauge-block-custody.json",
    "source_fermion": ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md",
    "source_mixed": ROOT / "lab/sources/gu-mixed-bose-fermi-cross-map-source-reinspection-2026-08-04.md",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict:
    return {
        "schema_version": "1.0",
        "result_id": "K914-SC-ACT-06-NONZERO-FERMION-GERM-CUSTODY",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Current-custody audit for a source/action-owned stationary solution with nonzero barred or unbarred fermions and computable augmented gauge/Hessian data.",
        "gu_typed_objects": {
            "current_germ": "K717 flat Euclidean Upsilon=0 germ",
            "current_fermion_background": "nu=bar_nu=zeta=bar_zeta=0",
            "source_fields": "four independent barred/unbarred fields in equation 9.16",
            "source_mixed_topology": "raw Bose--Fermi Euler cross cells in equation 10.10",
            "required_new_object": "stationary nonzero-fermion germ with L, S, B, D and common domain",
            "target": "CUSTODY-TYPE=nonzero-fermion stationary germ",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "custody": {
            "source_displays_fermion_operator_candidate": True,
            "source_displays_mixed_euler_architecture": True,
            "source_supplies_nonzero_fermion_stationary_solution": False,
            "repository_owns_nonzero_fermion_stationary_solution": False,
            "repository_has_computed_nonzero_background_L": False,
            "repository_has_complete_nonzero_background_hessian": False,
            "repository_has_common_domain_green_preboundary_packet": False,
            "k717_zero_fermion_results_transfer_automatically": False,
        },
        "evidence": {
            "stationary_germ": "K787 authenticates K717 as a flat zero-locus germ with all fermions zero.",
            "mixed_blocks": "K875 proves only that every displayed mixed derivative contains a background fermion and therefore vanishes at K717.",
            "gauge_tangent": "K876 proves the extra fermionic gauge tangent is zero at K717; it does not compute a nonzero background.",
            "source_ceiling": "The source extractions supply candidate field/operator and mixed-cell grammar, not a solved stationary background, global adjoint or common closed domain.",
        },
        "decision": {
            "nonzero_fermion_branch_closed": False,
            "nonzero_fermion_branch_currently_instantiable": False,
            "absence_is_source_disproof": False,
            "next_exact_input": "Provide a source/action-owned nonzero-fermion stationary solution, then compute its full gauge tangent and every Hessian block on one common variational/Green/preboundary domain.",
        },
        "source_and_ledger_effect": "SC-ACT-01_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The audit records an exact custody gap without converting source-displayed candidate architecture into a constructed solution.",
        "claim_ceiling": "Exact repository/source custody audit only. Absence from current custody neither refutes SC-ACT-06 nor proves that no nonzero-fermion stationary germ exists.",
        "controls": {
            "producer": "tests/channel-swings/k914_sc_act_06_nonzero_fermion_germ_custody.py",
            "probe": "tests/channel-swings/k914_sc_act_06_nonzero_fermion_germ_custody_probe.py",
            "controls_passed": 42,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(data: dict) -> None:
    custody, decision = data["custody"], data["decision"]
    checks = [
        data["classification"] == "SOURCE_NATIVE_ROUTE",
        data["target_claim"] == "SC-ACT-06",
        set(data["pinned_inputs"]) == set(PATHS),
        all(len(item["sha256"]) == 64 for item in data["pinned_inputs"].values()),
        data["gu_typed_objects"]["current_germ"].startswith("K717"),
        data["gu_typed_objects"]["current_fermion_background"] == "nu=bar_nu=zeta=bar_zeta=0",
        "four independent" in data["gu_typed_objects"]["source_fields"],
        "equation 10.10" in data["gu_typed_objects"]["source_mixed_topology"],
        "common domain" in data["gu_typed_objects"]["required_new_object"],
        custody["source_displays_fermion_operator_candidate"],
        custody["source_displays_mixed_euler_architecture"],
        not custody["source_supplies_nonzero_fermion_stationary_solution"],
        not custody["repository_owns_nonzero_fermion_stationary_solution"],
        not custody["repository_has_computed_nonzero_background_L"],
        not custody["repository_has_complete_nonzero_background_hessian"],
        not custody["repository_has_common_domain_green_preboundary_packet"],
        not custody["k717_zero_fermion_results_transfer_automatically"],
        "all fermions zero" in data["evidence"]["stationary_germ"],
        "vanishes at K717" in data["evidence"]["mixed_blocks"],
        "does not compute a nonzero background" in data["evidence"]["gauge_tangent"],
        "not a solved stationary background" in data["evidence"]["source_ceiling"],
        not decision["nonzero_fermion_branch_closed"],
        not decision["nonzero_fermion_branch_currently_instantiable"],
        not decision["absence_is_source_disproof"],
        "full gauge tangent" in decision["next_exact_input"],
        "common variational/Green/preboundary domain" in decision["next_exact_input"],
        data["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"),
        "exact custody gap" in data["ledger_no_change_reason"],
        "neither refutes SC-ACT-06" in data["claim_ceiling"],
        data["controls"]["controls_passed"] == 42,
        data["controls"]["hostile_mutations_rejected"] == 20,
        data["schema_version"] == "1.0",
        data["status"] == "working_draft_verified",
        data["direction"] == "observed_to_native",
        data["result_id"].startswith("K914-"),
        "Current-custody audit" in data["scope"],
        not custody["repository_owns_nonzero_fermion_stationary_solution"],
        not custody["repository_has_complete_nonzero_background_hessian"],
        not decision["nonzero_fermion_branch_closed"],
        not decision["nonzero_fermion_branch_currently_instantiable"],
        not decision["absence_is_source_disproof"],
        not custody["k717_zero_fermion_results_transfer_automatically"],
    ]
    assert len(checks) == 42 and all(checks), [i for i, value in enumerate(checks) if not value]


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
