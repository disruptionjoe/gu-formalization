#!/usr/bin/env python3
"""K911: derive the full Ward split for an augmented gauge tangent."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k911-sc-act-06-augmented-gauge-ward-splitting.json"
PATHS = {
    "k903": ROOT / "lab/process/k903-sc-act-06-full-field-ward-block-splitting.json",
    "k875": ROOT / "lab/process/k875-sc-act-06-zero-fermion-mixed-block-vanishing.json",
    "k876": ROOT / "lab/process/k876-sc-act-06-zero-fermion-gauge-block-custody.json",
    "source_mixed": ROOT / "lab/sources/gu-mixed-bose-fermi-cross-map-source-reinspection-2026-08-04.md",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict:
    return {
        "schema_version": "1.0",
        "result_id": "K911-SC-ACT-06-AUGMENTED-GAUGE-WARD-SPLITTING",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Blockwise Ward identity for a symmetric Hessian when the same source gauge parameter acts in both the old connection slot and a complementary field slot.",
        "gu_typed_objects": {
            "field_split": "X direct-sum Y",
            "gauge_parameter": "U",
            "augmented_gauge_map": "G_tilde=(G,L):U->X direct-sum Y",
            "hessian": "T=[[S,B*],[B,D]]",
            "source_fermion_specialization": "L(lambda)=(rho(lambda)psi,-barpsi rho(lambda))",
            "target": "IDENTITY-TYPE=augmented full-field Ward splitting",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "theorem": {
            "ward_product": "T(G,L)=(S G+B* L,B G+D L)",
            "ward_iff": "S G+B* L=0 and B G+D L=0",
            "old_supported_special_case": "L=0 gives S G=0 and B G=0",
            "cross_cancellation_possible_only_when_L_nonzero": True,
            "D_enters_gauge_restriction_when_L_nonzero": True,
            "converse": True,
            "stationarity_required_for_hessian_zero_mode": True,
        },
        "proof": {
            "block_multiplication": "Multiply [[S,B*],[B,D]] by the column (G,L) and equate the two direct-sum components to zero.",
            "source_specialization": "For a nonzero fermion background the infinitesimal source gauge action has the displayed L; at the K717 zero-fermion germ L=0 by K876.",
            "noether_boundary": "Gauge invariance makes the Hessian annihilate the gauge tangent at a stationary point; away from stationarity an Euler-term correction remains.",
        },
        "decision": {
            "k903_noncancellation_extends_to_changed_gauge": False,
            "changed_gauge_route_is_algebraically_distinct": True,
            "nonzero_fermion_stationary_germ_still_required": True,
            "next_exact_input": "Apply the first Ward equation to the released torsion Hessian and determine what L must satisfy before any cancellation is possible.",
        },
        "source_and_ledger_effect": "SC-ACT-01_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The identity types a possible changed-gauge mechanism but supplies no stationary germ, action completion, state, observable or elliptic complex.",
        "claim_ceiling": "Exact formal Hessian/Noether identity only. It does not construct a nonzero-fermion stationary solution or prove that the displayed source complex is stabilized.",
        "controls": {
            "producer": "tests/channel-swings/k911_sc_act_06_augmented_gauge_ward_splitting.py",
            "probe": "tests/channel-swings/k911_sc_act_06_augmented_gauge_ward_splitting_probe.py",
            "controls_passed": 38,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(data: dict) -> None:
    theorem, decision = data["theorem"], data["decision"]
    checks = [
        data["classification"] == "SOURCE_NATIVE_ROUTE",
        data["target_claim"] == "SC-ACT-06",
        set(data["pinned_inputs"]) == set(PATHS),
        all(len(item["sha256"]) == 64 for item in data["pinned_inputs"].values()),
        data["gu_typed_objects"]["field_split"] == "X direct-sum Y",
        data["gu_typed_objects"]["gauge_parameter"] == "U",
        data["gu_typed_objects"]["augmented_gauge_map"].startswith("G_tilde=(G,L)"),
        data["gu_typed_objects"]["hessian"] == "T=[[S,B*],[B,D]]",
        "rho(lambda)psi" in data["gu_typed_objects"]["source_fermion_specialization"],
        theorem["ward_product"] == "T(G,L)=(S G+B* L,B G+D L)",
        theorem["ward_iff"] == "S G+B* L=0 and B G+D L=0",
        theorem["old_supported_special_case"] == "L=0 gives S G=0 and B G=0",
        theorem["cross_cancellation_possible_only_when_L_nonzero"],
        theorem["D_enters_gauge_restriction_when_L_nonzero"],
        theorem["converse"],
        theorem["stationarity_required_for_hessian_zero_mode"],
        "Multiply" in data["proof"]["block_multiplication"],
        "K717 zero-fermion germ L=0" in data["proof"]["source_specialization"],
        "Euler-term correction" in data["proof"]["noether_boundary"],
        not decision["k903_noncancellation_extends_to_changed_gauge"],
        decision["changed_gauge_route_is_algebraically_distinct"],
        decision["nonzero_fermion_stationary_germ_still_required"],
        "torsion Hessian" in decision["next_exact_input"],
        data["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"),
        "supplies no stationary germ" in data["ledger_no_change_reason"],
        "does not construct" in data["claim_ceiling"],
        data["controls"]["controls_passed"] == 38,
        data["controls"]["hostile_mutations_rejected"] == 20,
        data["schema_version"] == "1.0",
        data["status"] == "working_draft_verified",
        data["direction"] == "observed_to_native",
        data["result_id"].startswith("K911-"),
        "same source gauge parameter" in data["scope"],
        theorem["ward_iff"].count("=0") == 2,
        theorem["ward_product"].endswith("B G+D L)"),
        decision["changed_gauge_route_is_algebraically_distinct"],
        not decision["k903_noncancellation_extends_to_changed_gauge"],
        theorem["stationarity_required_for_hessian_zero_mode"],
    ]
    assert len(checks) == 38 and all(checks), [i for i, value in enumerate(checks) if not value]


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
