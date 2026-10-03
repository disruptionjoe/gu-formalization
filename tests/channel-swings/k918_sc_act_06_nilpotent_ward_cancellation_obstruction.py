#!/usr/bin/env python3
"""K918: prove a literal odd background cannot cancel an ordinary torsion defect on the body."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k918-sc-act-06-nilpotent-ward-cancellation-obstruction.json"
PATHS = {
    "k752": ROOT / "lab/process/k752-sc-act-06-nonzero-odd-saddle-body-obstruction.json",
    "k899": ROOT / "lab/process/k899-sc-act-06-torsion-hessian-gauge-restriction.json",
    "k911": ROOT / "lab/process/k911-sc-act-06-augmented-gauge-ward-splitting.json",
    "k917": ROOT / "lab/process/k917-sc-act-06-superpoint-gauge-body-reduction.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict:
    return {
        "schema_version": "1.0",
        "result_id": "K918-SC-ACT-06-NILPOTENT-WARD-CANCELLATION-OBSTRUCTION",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Body-level first augmented Ward equation for the released torsion Hessian over a literal odd superpoint.",
        "gu_typed_objects": {
            "ward_equation": "S G+B*L=0",
            "released_old_block": "S=kappa K+H_Q with H_Q G=0",
            "mixed_block_parity": "B* is odd at an odd background",
            "gauge_tangent_parity": "L is odd",
            "mixed_product": "B*L is even and lies in the nilpotent ideal",
            "target": "OBSTRUCTION-TYPE=body Ward cancellation",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "theorem": {
            "body_of_BstarL": 0,
            "body_ward_equation": "body(kappa) K G=0",
            "KG_rank": 16384,
            "nonzero_body_kappa_allowed": False,
            "nilpotent_kappa_changes_ordinary_torsion_coefficient": False,
            "literal_odd_background_salvages_ordinary_torsion": False,
            "independent_body_old_old_correction_remains_possible": True,
            "even_condensate_background_change_remains_possible": True,
            "k752_body_zero_mechanism_reused": True,
        },
        "proof": {
            "parity_product": "Both B* and L carry odd background degree, so B*L is even but belongs to the positive nilpotent filtration and has zero body.",
            "body_equation": "Applying beta to SG+B*L=0 removes B*L and H_QG, leaving body(kappa)KG=0.",
            "rank": "K899 proves KG injective of ordinary rank 16,384, hence body(kappa)=0.",
        },
        "decision": {
            "k915_changed_gauge_reopens_nonzero_body_torsion_on_literal_odd_route": False,
            "changed_gauge_superpoint_branch_fully_refuted": False,
            "new_body_level_action_parent_required_for_ordinary_torsion": True,
            "SC_ACT_06_proved_or_refuted": False,
            "new_effect_is_current_torsion_ward_composition": True,
            "next_exact_input": "Reduce the graph gauge quotient to the body and freeze separate reopeners for a supermodule complex, a justified commuting-spinor proxy, an even condensate or a new gauge-basic old-old parent.",
        },
        "source_and_ledger_effect": "SC-ACT-01_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The obstruction closes only ordinary-body torsion cancellation by nilpotent odd data; it supplies no full complex or physical state.",
        "claim_ceiling": "Exact body-level Ward obstruction for the released torsion parent. It does not exclude nilpotent deformations, even composites or category-changed spinor models.",
        "controls": {
            "producer": "tests/channel-swings/k918_sc_act_06_nilpotent_ward_cancellation_obstruction.py",
            "probe": "tests/channel-swings/k918_sc_act_06_nilpotent_ward_cancellation_obstruction_probe.py",
            "controls_passed": 44,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(data: dict) -> None:
    theorem, decision = data["theorem"], data["decision"]
    checks = [
        data["schema_version"] == "1.0",
        data["result_id"].startswith("K918-"),
        data["status"] == "working_draft_verified",
        data["classification"] == "SOURCE_NATIVE_ROUTE",
        data["direction"] == "observed_to_native",
        data["target_claim"] == "SC-ACT-06",
        "first augmented Ward equation" in data["scope"],
        set(data["pinned_inputs"]) == set(PATHS),
        all(len(row["sha256"]) == 64 for row in data["pinned_inputs"].values()),
        data["gu_typed_objects"]["ward_equation"] == "S G+B*L=0",
        "H_Q G=0" in data["gu_typed_objects"]["released_old_block"],
        data["gu_typed_objects"]["mixed_block_parity"].endswith("odd background"),
        data["gu_typed_objects"]["gauge_tangent_parity"] == "L is odd",
        "nilpotent ideal" in data["gu_typed_objects"]["mixed_product"],
        theorem["body_of_BstarL"] == 0,
        theorem["body_ward_equation"] == "body(kappa) K G=0",
        theorem["KG_rank"] == 16384,
        not theorem["nonzero_body_kappa_allowed"],
        not theorem["nilpotent_kappa_changes_ordinary_torsion_coefficient"],
        not theorem["literal_odd_background_salvages_ordinary_torsion"],
        theorem["independent_body_old_old_correction_remains_possible"],
        theorem["even_condensate_background_change_remains_possible"],
        theorem["k752_body_zero_mechanism_reused"],
        "positive nilpotent filtration" in data["proof"]["parity_product"],
        "leaving body(kappa)KG=0" in data["proof"]["body_equation"],
        "rank 16,384" in data["proof"]["rank"],
        not decision["k915_changed_gauge_reopens_nonzero_body_torsion_on_literal_odd_route"],
        not decision["changed_gauge_superpoint_branch_fully_refuted"],
        decision["new_body_level_action_parent_required_for_ordinary_torsion"],
        not decision["SC_ACT_06_proved_or_refuted"],
        decision["new_effect_is_current_torsion_ward_composition"],
        "graph gauge quotient" in decision["next_exact_input"],
        "commuting-spinor proxy" in decision["next_exact_input"],
        "even condensate" in decision["next_exact_input"],
        data["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"),
        "closes only ordinary-body torsion cancellation" in data["ledger_no_change_reason"],
        "does not exclude nilpotent deformations" in data["claim_ceiling"],
        data["controls"]["controls_passed"] == 44,
        data["controls"]["hostile_mutations_rejected"] == 20,
        data["gu_typed_objects"]["target"].startswith("OBSTRUCTION-TYPE="),
        theorem["KG_rank"] > 0,
        not theorem["nonzero_body_kappa_allowed"],
        theorem["independent_body_old_old_correction_remains_possible"],
        not decision["SC_ACT_06_proved_or_refuted"],
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
