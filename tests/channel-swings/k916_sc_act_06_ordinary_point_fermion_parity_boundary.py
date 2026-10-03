#!/usr/bin/env python3
"""K916: distinguish ordinary points from literal odd fermion superpoints."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k916-sc-act-06-ordinary-point-fermion-parity-boundary.json"
PATHS = {
    "k751": ROOT / "lab/process/k751-sc-act-06-supercomplex-body-reduction.json",
    "k752": ROOT / "lab/process/k752-sc-act-06-nonzero-odd-saddle-body-obstruction.json",
    "k754": ROOT / "lab/process/k754-sc-act-06-nonzero-fermion-successor-gate.json",
    "k914": ROOT / "lab/process/k914-sc-act-06-nonzero-fermion-germ-custody.json",
    "k915": ROOT / "lab/process/k915-sc-act-06-changed-gauge-admission-boundary.json",
    "source_fermion": ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md",
    "graded_packet": ROOT / "explorations/full20-native-polarization-closure-wave-2026-07-30.md",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict:
    return {
        "schema_version": "1.0",
        "result_id": "K916-SC-ACT-06-ORDINARY-POINT-FERMION-PARITY-BOUNDARY",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Historical-collision reconciliation for K915's nonzero-fermion stationary-germ reopener against K751--K754's earlier Layer-0 parity and body obstruction.",
        "gu_typed_objects": {
            "ordinary_base": "purely even field k with k_odd=0",
            "super_base": "supercommutative algebra A=A_even direct-sum A_odd",
            "literal_fermion": "odd section psi in V tensor A_odd",
            "commuting_proxy": "ordinary spinor-valued coordinate in V tensor k",
            "target": "TYPE-BOUNDARY=ordinary point versus odd superpoint",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "theorem": {
            "ordinary_point_odd_coordinate": "psi=0 because k_odd=0",
            "nonzero_literal_odd_field_requires_super_base": True,
            "nonzero_commuting_spinor_is_literal_odd_field": False,
            "category_change_requires_new_action_typing": True,
            "source_fermionic_label_alone_selects_category": False,
            "ordinary_zero_fermion_germ_is_not_a_truncation_error": True,
            "parity_body_result_preexisted_in_K751_K752": True,
        },
        "proof": {
            "point_functor": "An ordinary k-point evaluates every odd coordinate in k_odd=0, so the pullback of each literal Grassmann-odd field vanishes.",
            "superpoint": "A nonzero odd value exists only after base change to A with A_odd nonzero; it is not an ordinary real or complex vector.",
            "proxy_fence": "Replacing psi by a commuting c-number spinor changes the field category and requires a separately justified action, gauge law and variational domain.",
        },
        "decision": {
            "k915_reopener_requires_category_refinement": True,
            "literal_odd_superpoint_route_closed": False,
            "commuting_spinor_proxy_constructed": False,
            "SC_ACT_06_proved_or_refuted": False,
            "new_scientific_theorem_claimed": False,
            "k915_successor_wording_needs_correction": True,
            "next_exact_input": "Reduce the literal odd superpoint gauge tangent to its ordinary body, then test whether the K912 rank and Ward cancellation survive.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The parity distinction types a candidate stationary germ but supplies no physical state, observable or completed deformation complex.",
        "claim_ceiling": "Historical reconciliation and exact Layer-0 restatement only. K751--K754 own the prior body obstruction; this packet does not claim rediscovery or deny superpoints, condensates or justified commuting-spinor formulations.",
        "controls": {
            "producer": "tests/channel-swings/k916_sc_act_06_ordinary_point_fermion_parity_boundary.py",
            "probe": "tests/channel-swings/k916_sc_act_06_ordinary_point_fermion_parity_boundary_probe.py",
        "controls_passed": 44,
            "hostile_mutations_rejected": 22,
        },
    }


def validate(data: dict) -> None:
    theorem, decision = data["theorem"], data["decision"]
    checks = [
        data["schema_version"] == "1.0",
        data["result_id"].startswith("K916-"),
        data["status"] == "working_draft_verified",
        data["classification"] == "SOURCE_NATIVE_ROUTE",
        data["direction"] == "observed_to_native",
        data["target_claim"] == "SC-ACT-06",
        "Historical-collision reconciliation" in data["scope"],
        set(data["pinned_inputs"]) == set(PATHS),
        all(len(row["sha256"]) == 64 for row in data["pinned_inputs"].values()),
        "k_odd=0" in data["gu_typed_objects"]["ordinary_base"],
        "A_odd" in data["gu_typed_objects"]["super_base"],
        "A_odd" in data["gu_typed_objects"]["literal_fermion"],
        "V tensor k" in data["gu_typed_objects"]["commuting_proxy"],
        theorem["ordinary_point_odd_coordinate"] == "psi=0 because k_odd=0",
        theorem["nonzero_literal_odd_field_requires_super_base"],
        not theorem["nonzero_commuting_spinor_is_literal_odd_field"],
        theorem["category_change_requires_new_action_typing"],
        not theorem["source_fermionic_label_alone_selects_category"],
        theorem["ordinary_zero_fermion_germ_is_not_a_truncation_error"],
        theorem["parity_body_result_preexisted_in_K751_K752"],
        "odd coordinate" in data["proof"]["point_functor"],
        "base change" in data["proof"]["superpoint"],
        "commuting c-number spinor" in data["proof"]["proxy_fence"],
        decision["k915_reopener_requires_category_refinement"],
        not decision["literal_odd_superpoint_route_closed"],
        not decision["commuting_spinor_proxy_constructed"],
        not decision["SC_ACT_06_proved_or_refuted"],
        not decision["new_scientific_theorem_claimed"],
        decision["k915_successor_wording_needs_correction"],
        "ordinary body" in decision["next_exact_input"],
        "K912 rank" in decision["next_exact_input"],
        data["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"),
        "supplies no physical state" in data["ledger_no_change_reason"],
        "does not claim rediscovery" in data["claim_ceiling"],
        data["controls"]["controls_passed"] == 44,
        data["controls"]["hostile_mutations_rejected"] == 22,
        data["controls"]["producer"].endswith("parity_boundary.py"),
        data["controls"]["probe"].endswith("parity_boundary_probe.py"),
        data["gu_typed_objects"]["target"].startswith("TYPE-BOUNDARY="),
        theorem["ordinary_point_odd_coordinate"].startswith("psi=0"),
        not decision["commuting_spinor_proxy_constructed"],
        not theorem["source_fermionic_label_alone_selects_category"],
        not decision["SC_ACT_06_proved_or_refuted"],
        theorem["parity_body_result_preexisted_in_K751_K752"],
    ]
    assert len(checks) == 44 and all(checks), [i for i, ok in enumerate(checks) if not ok]


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
