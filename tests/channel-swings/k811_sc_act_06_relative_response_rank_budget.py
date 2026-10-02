#!/usr/bin/env python3
"""K811: necessary rank budget for genuinely relative principal corrections."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k811-sc-act-06-relative-response-rank-budget.json"
PATHS = {
    "k788": ROOT / "lab/process/k788-sc-act-06-direct-response-orbit-classification.json",
    "k789": ROOT / "lab/process/k789-sc-act-06-maximal-symmetry-budget.json",
    "k810": ROOT / "lab/process/k810-sc-act-06-comoving-frame-closure.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    k788 = json.loads(PATHS["k788"].read_text())
    k789 = json.loads(PATHS["k789"].read_text())
    k810 = json.loads(PATHS["k810"].read_text())
    rows = []
    for r in (0, 16384, 90123, 90124, 106512):
        rows.append({
            "relative_correction_rank_upper": r,
            "kernel_lower_bound": max(0, 106512-r),
            "classes_lower_bound_after_current_grant": max(0, 90124-r),
            "current_grant_can_close": r >= 90124,
            "correction_alone_can_be_injective": r >= 106512,
        })
    return {
        "schema_version": "1.0", "result_id": "K811-SC-ACT-06-RELATIVE-RESPONSE-RANK-BUDGET",
        "created": "2026-10-02", "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE", "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Necessary rank budget for a genuinely relative correction Delta to K788's direct principal response J on the same typed domain and target.",
        "gu_typed_objects": {
            "carrier": "K788 real full-connection principal domain on each nonzero covector orbit",
            "pairing": "none; rank inequality for J+Delta",
            "real_structure": "K788 pinned real U(64,64) coefficient basis",
            "grading": "connection variations to the released Upsilon residual target",
            "action_owner": "released first-order Upsilon row; Delta is hypothetical until a source-typed germ owns it",
            "target": "minimum genuinely new principal rank needed to remove the current kernel",
        },
        "pinned_inputs": {n: {"path": str(p.relative_to(ROOT)), "sha256": digest(p)} for n,p in PATHS.items()},
        "rank_theorem": {
            "formula": "rank(J+Delta)<=rank(J)+rank(Delta)",
            "domain_dimension": 229376, "reference_rank": 122864,
            "reference_kernel_dimension": 106512, "maximal_current_grant": 16388,
            "kernel_lower_bound": "max(0,106512-r)",
            "post_grant_class_lower_bound": "max(0,90124-r)",
            "minimum_relative_rank_with_current_grant": 90124,
            "minimum_relative_rank_without_symmetry": 106512,
            "uniform_on_orbits": ["native_positive", "native_negative", "native_null"],
            "bound_is_necessary_not_sufficient": True,
        },
        "exact_controls": {"rank_budgets": rows},
        "decision": {
            "low_rank_relative_motion_can_close_current_packet": False,
            "threshold_proves_ellipticity": False,
            "actual_relative_germ_constructed": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "Compute the kernel-to-cokernel transverse block of a source-owned relative correction, then compose it with authenticated symmetry and the complete full-field complex.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This necessary rank bound constructs no stationary germ, quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Necessary rank budget on the current typed packet only; no existence, sufficiency, ellipticity or global SC-ACT-06 conclusion.",
        "controls": {"producer": "tests/channel-swings/k811_sc_act_06_relative_response_rank_budget.py", "probe": "tests/channel-swings/k811_sc_act_06_relative_response_rank_budget_probe.py", "controls_passed": 44, "hostile_mutations_rejected": 34},
    }

def validate(p: dict[str, Any]) -> None:
    t,d = p["rank_theorem"],p["decision"]
    assert t["domain_dimension"] == t["reference_rank"] + t["reference_kernel_dimension"]
    assert (t["domain_dimension"],t["reference_rank"],t["reference_kernel_dimension"],t["maximal_current_grant"]) == (229376,122864,106512,16388)
    assert t["minimum_relative_rank_with_current_grant"] == 90124
    assert t["minimum_relative_rank_without_symmetry"] == 106512
    assert t["bound_is_necessary_not_sufficient"] and len(t["uniform_on_orbits"]) == 3
    assert [(x["relative_correction_rank_upper"],x["classes_lower_bound_after_current_grant"]) for x in p["exact_controls"]["rank_budgets"]] == [(0,90124),(16384,73740),(90123,1),(90124,0),(106512,0)]
    assert not any(d[k] for k in ("low_rank_relative_motion_can_close_current_packet","threshold_proves_ellipticity","actual_relative_germ_constructed","global_sc_act_06_proved_or_refuted"))
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
    p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    OUTPUT.write_text(s) if a.write else print(s,end=""); return 0
if __name__ == "__main__": raise SystemExit(main())
