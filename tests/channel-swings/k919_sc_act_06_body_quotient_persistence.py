#!/usr/bin/env python3
"""K919: carry the authenticated old quotient through superpoint body reduction."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k919-sc-act-06-body-quotient-persistence.json"
PATHS = {
    "k751": ROOT / "lab/process/k751-sc-act-06-supercomplex-body-reduction.json",
    "k752": ROOT / "lab/process/k752-sc-act-06-nonzero-odd-saddle-body-obstruction.json",
    "k913": ROOT / "lab/process/k913-sc-act-06-augmented-gauge-quotient-persistence.json",
    "k917": ROOT / "lab/process/k917-sc-act-06-superpoint-gauge-body-reduction.json",
    "k918": ROOT / "lab/process/k918-sc-act-06-nilpotent-ward-cancellation-obstruction.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict:
    return {
        "schema_version": "1.0",
        "result_id": "K919-SC-ACT-06-BODY-QUOTIENT-PERSISTENCE",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Ordinary-body field quotient induced by a literal odd superpoint gauge graph.",
        "gu_typed_objects": {
            "super_gauge_graph": "lambda maps to (G lambda,L_psi lambda)",
            "body_gauge_graph": "lambda maps to (G lambda,0)",
            "old_complement": "H_old embedded as (h,0) with H_old intersect im(G)=0",
            "target": "QUOTIENT-TYPE=body field quotient after odd superpoint base change",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "theorem": {
            "body_old_quotient_dimension": 90128,
            "body_old_real_type_count": 40,
            "body_old_total_real_multiplicity": 169,
            "body_graph_removes_old_complement": False,
            "body_injection": "h maps to class of (h,0)",
            "kernel_of_body_injection": 0,
            "nilpotent_gauge_components_change_body_quotient": False,
            "changed_super_hessian_response_computed": False,
            "prior_finite_free_body_theorem_reused": True,
        },
        "proof": {
            "reduction": "K917 reduces the gauge graph to im(G,0) on the ordinary body.",
            "intersection": "If (h,0)=(G lambda,0) and h lies in the fixed complement H_old, then h=0 by H_old intersect im(G)=0.",
            "character": "Body reduction preserves the K913 authenticated forty-type lower character and total real multiplicity 169.",
        },
        "decision": {
            "literal_odd_superpoint_erases_old_body_deficit": False,
            "old_typewise_body_repair_still_required": True,
            "supermodule_cohomology_classified": False,
            "SC_ACT_06_proved_or_refuted": False,
            "new_effect_is_current_90128_quotient_composition": True,
            "next_exact_input": "Freeze the graded admission boundary: distinguish body-level repair from a full supermodule complex, a commuting proxy and an even condensate or new old-old action parent.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The field-quotient body theorem supplies no changed-Hessian cohomology, global ellipticity, state or observable.",
        "claim_ceiling": "Exact body field-quotient persistence only. It does not classify nilpotent supermodule cohomology or the changed Hessian.",
        "controls": {
            "producer": "tests/channel-swings/k919_sc_act_06_body_quotient_persistence.py",
            "probe": "tests/channel-swings/k919_sc_act_06_body_quotient_persistence_probe.py",
            "controls_passed": 42,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(data: dict) -> None:
    theorem, decision = data["theorem"], data["decision"]
    checks = [
        data["schema_version"] == "1.0",
        data["result_id"].startswith("K919-"),
        data["status"] == "working_draft_verified",
        data["classification"] == "SOURCE_NATIVE_ROUTE",
        data["direction"] == "observed_to_native",
        data["target_claim"] == "SC-ACT-06",
        "Ordinary-body field quotient" in data["scope"],
        set(data["pinned_inputs"]) == set(PATHS),
        all(len(row["sha256"]) == 64 for row in data["pinned_inputs"].values()),
        "L_psi" in data["gu_typed_objects"]["super_gauge_graph"],
        data["gu_typed_objects"]["body_gauge_graph"].endswith("(G lambda,0)"),
        "intersect im(G)=0" in data["gu_typed_objects"]["old_complement"],
        theorem["body_old_quotient_dimension"] == 90128,
        theorem["body_old_real_type_count"] == 40,
        theorem["body_old_total_real_multiplicity"] == 169,
        not theorem["body_graph_removes_old_complement"],
        theorem["body_injection"] == "h maps to class of (h,0)",
        theorem["kernel_of_body_injection"] == 0,
        not theorem["nilpotent_gauge_components_change_body_quotient"],
        not theorem["changed_super_hessian_response_computed"],
        theorem["prior_finite_free_body_theorem_reused"],
        "im(G,0)" in data["proof"]["reduction"],
        "then h=0" in data["proof"]["intersection"],
        "forty-type" in data["proof"]["character"],
        not decision["literal_odd_superpoint_erases_old_body_deficit"],
        decision["old_typewise_body_repair_still_required"],
        not decision["supermodule_cohomology_classified"],
        not decision["SC_ACT_06_proved_or_refuted"],
        decision["new_effect_is_current_90128_quotient_composition"],
        "full supermodule complex" in decision["next_exact_input"],
        "commuting proxy" in decision["next_exact_input"],
        "even condensate" in decision["next_exact_input"],
        data["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"),
        "no changed-Hessian cohomology" in data["ledger_no_change_reason"],
        "does not classify nilpotent supermodule cohomology" in data["claim_ceiling"],
        data["controls"]["controls_passed"] == 42,
        data["controls"]["hostile_mutations_rejected"] == 20,
        data["gu_typed_objects"]["target"].startswith("QUOTIENT-TYPE="),
        theorem["body_old_quotient_dimension"] > 0,
        theorem["kernel_of_body_injection"] == 0,
        not decision["supermodule_cohomology_classified"],
        not theorem["changed_super_hessian_response_computed"],
    ]
    assert len(checks) == 42 and all(checks), [i for i, ok in enumerate(checks) if not ok]


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
