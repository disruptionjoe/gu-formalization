#!/usr/bin/env python3
"""K1182: extract exact K132-kernel complement ranks of source-owned Upsilon response."""
from __future__ import annotations

import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1182-native-upsilon-k132-complement-ranks.json"
PATHS = {
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
    "k740": ROOT / "lab/process/k740-sc-act-06-expanded-principal-response-rank.json",
    "k743": ROOT / "lab/process/k743-sc-act-06-residual-square-image-cap.json",
    "k745": ROOT / "lab/process/k745-sc-act-06-gauge-redundancy-obstruction.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    k720 = json.loads(PATHS["k720"].read_text()); k743 = json.loads(PATHS["k743"].read_text())
    h_cases = {x["case"]: x for x in k720["exact_controls"]["cases"]}
    stack_cases = {x["case"]: x for x in k743["exact_controls"]["cases"]}
    rows = []
    for name in ("native_nonnull", "native_null_auxiliary_nonzero"):
        h = h_cases[name]; s = stack_cases[name]
        complement = s["total_coupled_image_cap_rank"] - h["action_euler_rank"]
        residual_kernel = h["action_euler_kernel_dimension"] - complement
        rows.append({
            "case": name,
            "field_dimension": k720["exact_controls"]["field_dimension"],
            "hessian_rank": h["action_euler_rank"],
            "hessian_kernel_dimension": h["action_euler_kernel_dimension"],
            "stacked_h_j_rank": s["total_coupled_image_cap_rank"],
            "rank_j_on_ker_h": complement,
            "ker_h_intersect_ker_j_dimension": residual_kernel,
            "owned_gauge_rank": h["owned_gauge_image_rank"],
            "physical_candidate_residual_after_gauge": residual_kernel - h["owned_gauge_image_rank"],
        })
    return {
        "schema_version": "1.0", "result_id": "K1182-NATIVE-UPSILON-K132-COMPLEMENT-RANKS",
        "created": "2026-10-05", "status": "working_draft_verified", "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "map": "J_q=principal D(Upsilon)_q on the action-owned full connection carrier",
        "pinned_inputs": {k: {"path": str(v.relative_to(ROOT)), "sha256": digest(v)} for k,v in PATHS.items()},
        "exact_controls": {"cases": rows},
        "decision": {
            "first_measured_source_owned_k132_carrier_map": True,
            "sufficient_radical_capture": False,
            "protected_verdict_change": "none",
        },
        "claim_ceiling": "exact frozen finite-symbol complement ranks; no global complex, positive quotient, domain, prediction or source-claim verdict",
    }

def validate(packet: dict[str, Any]) -> None:
    assert packet["result_id"] == "K1182-NATIVE-UPSILON-K132-COMPLEMENT-RANKS"
    assert packet["classification"] == "SOURCE_NATIVE_ROUTE" and packet["target_claim"] == "SC-ACT-06"
    rows = {x["case"]: x for x in packet["exact_controls"]["cases"]}
    a, b = rows["native_nonnull"], rows["native_null_auxiliary_nonzero"]
    assert (a["hessian_rank"], b["hessian_rank"]) == (130912, 122748)
    assert (a["stacked_h_j_rank"], b["stacked_h_j_rank"]) == (131074, 131071)
    assert (a["rank_j_on_ker_h"], b["rank_j_on_ker_h"]) == (162, 8323)
    assert (a["physical_candidate_residual_after_gauge"], b["physical_candidate_residual_after_gauge"]) == (98308, 98311)
    for row in rows.values():
        assert row["rank_j_on_ker_h"] == row["stacked_h_j_rank"] - row["hessian_rank"]
        assert row["ker_h_intersect_ker_j_dimension"] == row["hessian_kernel_dimension"] - row["rank_j_on_ker_h"]
    assert packet["decision"]["first_measured_source_owned_k132_carrier_map"]
    assert not packet["decision"]["sufficient_radical_capture"]
    assert packet["decision"]["protected_verdict_change"] == "none"

def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("--write", action="store_true"); a=p.parse_args(); packet=build(); validate(packet)
    rendered=json.dumps(packet, indent=2, sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(rendered)
    else: print(rendered,end="")
    return 0

if __name__ == "__main__": raise SystemExit(main())
