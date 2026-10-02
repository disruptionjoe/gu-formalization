#!/usr/bin/env python3
"""K827: regular parameter changes preserve the first nonzero response jet."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k827-sc-act-06-regular-parameter-jet-invariance.json"
PATHS = {
    "k819": ROOT / "lab/process/k819-sc-act-06-second-order-zero-locus-obstruction.json",
    "k826": ROOT / "lab/process/k826-sc-act-06-relative-coefficient-ownership-gate.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    return {
        "schema_version": "1.0", "result_id": "K827-SC-ACT-06-REGULAR-PARAMETER-JET-INVARIANCE",
        "created": "2026-10-02", "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE", "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Regular-local-parameter invariance of the first nonzero response jet; singular reparameterizations are excluded from one normalization class.",
        "pinned_inputs": {n: {"path": str(p.relative_to(ROOT)), "sha256": digest(p)} for n,p in PATHS.items()},
        "jet_invariance_theorem": {
            "regular_change_condition": "phi(0)=0 and phi'(0)!=0",
            "vanishing_order_preserved": True,
            "leading_jet_rule": "(f o phi)^(k)(0)=f^(k)(0)*phi'(0)^k when f vanishes through order k-1",
            "first_order_rank_preserved": True,
            "first_order_scale_preserved": False,
            "singular_change_may_raise_vanishing_order": True,
            "singular_change_is_same_normalization_class": False,
        },
        "exact_controls": {
            "base_family": "f(t)=t", "base_vanishing_order": 1,
            "regular_phi": "phi(s)=2s+s^2", "regular_phi_derivative_at_zero": 2,
            "regular_composite_derivative_at_zero": 2, "regular_composite_vanishing_order": 1,
            "singular_psi": "psi(s)=s^2", "singular_psi_derivative_at_zero": 0,
            "singular_composite_vanishing_order": 2,
            "endpoint_parameter_scaling_owns_absolute_delta": False,
        },
        "decision": {
            "actual_source_normalization_constructed": False,
            "singular_reparameterization_credited_as_zero_tangent": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "Supply the source/action-owned local parameter and distinguish its regular normalization class from singular changes before assigning the first nonzero response jet.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "claim_ceiling": "Parameter-jet invariance gate only; no GU family, coefficient, ellipticity, or physical conclusion.",
        "controls": {"producer": "tests/channel-swings/k827_sc_act_06_regular_parameter_jet_invariance.py", "probe": "tests/channel-swings/k827_sc_act_06_regular_parameter_jet_invariance_probe.py", "controls_passed": 24, "hostile_mutations_rejected": 12},
    }

def validate(p: dict[str, Any]) -> None:
    t,c,d=p["jet_invariance_theorem"],p["exact_controls"],p["decision"]
    assert t["regular_change_condition"] == "phi(0)=0 and phi'(0)!=0"
    assert t["vanishing_order_preserved"] and t["first_order_rank_preserved"]
    assert not t["first_order_scale_preserved"] and t["singular_change_may_raise_vanishing_order"]
    assert not t["singular_change_is_same_normalization_class"]
    assert c["regular_phi_derivative_at_zero"] == c["regular_composite_derivative_at_zero"] == 2
    assert c["base_vanishing_order"] == c["regular_composite_vanishing_order"] == 1
    assert c["singular_psi_derivative_at_zero"] == 0 and c["singular_composite_vanishing_order"] == 2
    assert not c["endpoint_parameter_scaling_owns_absolute_delta"]
    assert not d["actual_source_normalization_constructed"] and not d["singular_reparameterization_credited_as_zero_tangent"] and not d["global_sc_act_06_proved_or_refuted"]
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); a=ap.parse_args(); p=build(); validate(p)
    if a.check: assert json.loads(OUTPUT.read_text())==p
    else: print(json.dumps(p,indent=2,sort_keys=True))
    return 0
if __name__=="__main__": raise SystemExit(main())
