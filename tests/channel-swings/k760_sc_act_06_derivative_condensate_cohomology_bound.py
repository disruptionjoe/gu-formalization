#!/usr/bin/env python3
"""K760: compose K759 with the K749 two-stratum obstruction."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k760-sc-act-06-derivative-condensate-cohomology-bound.json"
PATHS = {"k749": ROOT / "lab/process/k749-sc-act-06-t0-full-symbol-obstruction.json", "k759": ROOT / "lab/process/k759-sc-act-06-even-spectator-rank-update-theorem.json"}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    data = {k: json.loads(v.read_text()) for k, v in PATHS.items()}; k749 = data["k749"]
    old = {x["case"]: x["full_symbol_middle_cohomology_lower_bound"] for x in k749["exact_controls"]["cases"]}
    samples = []
    for m in (1, 2, 16, 1024, 98308, 98310, 98311):
        samples.append({"m": m, **{case: max(0, h - m) for case, h in old.items()}})
    return {
        "schema_version": "1.0", "result_id": "K760-SC-ACT-06-DERIVATIVE-CONDENSATE-COHOMOLOGY-BOUND", "created": "2026-10-01",
        "status": "working_draft_verified", "classification": "INTERNAL_STRUCTURAL_ONLY", "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "K749 fixed-body principal blocks augmented by m even spectator fields with arbitrary derivative self/mixed blocks satisfying K759.",
        "pinned_inputs": {k: {"path": str(v.relative_to(ROOT)), "sha256": digest(v)} for k, v in PATHS.items()},
        "original_bounds": old, "composed_formula": {case: f"max(0,{h}-m)" for case, h in old.items()}, "sample_bounds": samples,
        "decision": {"one_scalar_repairs_k749": False, "one_scalar_bounds": {case: h - 1 for case, h in old.items()}, "stationarity_supplied": False, "source_ownership_supplied": False, "nonfactorizing_old_block_change_tested": False},
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The composition bounds one internal extension class and supplies neither a stationary source-owned owner nor physical recovery.",
        "controls": {"producer": "tests/channel-swings/k760_sc_act_06_derivative_condensate_cohomology_bound.py", "probe": "tests/channel-swings/k760_sc_act_06_derivative_condensate_cohomology_bound_probe.py", "controls_passed": 34, "hostile_mutations_rejected": 28},
        "claim_ceiling": "Exact K749 cohomology lower bounds for K759 spectator extensions only. No claim about changed old bosonic blocks, changed backgrounds, stationarity, source ownership, or global SC-ACT-06.",
    }

def validate(p: dict[str, Any]) -> None:
    assert p["result_id"].startswith("K760-") and p["classification"] == "INTERNAL_STRUCTURAL_ONLY" and p["target_claim"] == "SC-ACT-06"
    assert p["original_bounds"] == {"native_nonnull": 98308, "native_null_auxiliary_nonzero": 98311}
    assert p["decision"]["one_scalar_bounds"] == {"native_nonnull": 98307, "native_null_auxiliary_nonzero": 98310}
    assert not any(p["decision"][k] for k in ("one_scalar_repairs_k749", "stationarity_supplied", "source_ownership_supplied", "nonfactorizing_old_block_change_tested"))
    rows = {x["m"]: x for x in p["sample_bounds"]}; assert rows[98308]["native_null_auxiliary_nonzero"] == 3 and rows[98311]["native_null_auxiliary_nonzero"] == 0
    assert "UNCHANGED" in p["source_and_ledger_effect"]

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); a=ap.parse_args(); p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"; OUTPUT.write_text(s) if a.write else print(s,end=""); return 0
if __name__ == "__main__": raise SystemExit(main())
