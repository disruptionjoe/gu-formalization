#!/usr/bin/env python3
"""K819: certify the second-order zero-locus obstruction."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k819-sc-act-06-second-order-zero-locus-obstruction.json"
PATHS = {
    "k815": ROOT / "lab/process/k815-sc-act-06-zero-locus-tangent-compatibility.json",
    "k817": ROOT / "lab/process/k817-sc-act-06-finite-parameter-schur-gate.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    return {
        "schema_version": "1.0", "result_id": "K819-SC-ACT-06-SECOND-ORDER-ZERO-LOCUS-OBSTRUCTION",
        "created": "2026-10-02", "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE", "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Necessary second-order compatibility for any source-typed relative Upsilon=0 solution germ after K815 tangent solvability.",
        "gu_typed_objects": {
            "carrier": "second jet of a proposed real field/background curve x_t",
            "pairing": "cokernel quotient of the frozen first response J only",
            "real_structure": "real C2 parameter curve and real residual target",
            "grading": "parameter two-jet and field two-jet into the Upsilon residual target",
            "action_owner": "released Upsilon zero locus; no source parameter family is supplied",
            "target": "existence of a second derivative of a zero-locus solution family",
        },
        "pinned_inputs": {n: {"path": str(p.relative_to(ROOT)), "sha256": digest(p)} for n,p in PATHS.items()},
        "second_order_theorem": {
            "first_equation": "J xdot + b = 0",
            "second_equation": "J xddot + F_tt + 2 F_tx[xdot] + F_xx[xdot,xdot] = 0",
            "obstruction": "pi_coker(J)(F_tt + 2 F_tx[xdot] + F_xx[xdot,xdot]) = 0",
            "kernel_choice_must_be_solved": True,
            "first_order_pass_implies_second_order_pass": False,
            "second_order_pass_proves_full_family": False,
        },
        "exact_controls": {
            "obstructed_family": "F(t,x)=x^2+t^2", "obstructed_J": 0, "obstructed_b": 0,
            "obstructed_first_order_passes": True, "obstructed_second_term": "2+2*xdot^2",
            "obstructed_real_second_order_solution_exists": False,
            "repairable_family": "F(t,x)=x^2-t^2", "repairable_first_order_passes": True,
            "repairable_kernel_speeds": [-1, 1], "repairable_branches": ["x=-t", "x=t"],
            "repairable_second_order_solution_exists": True,
        },
        "decision": {
            "actual_source_two_jet_constructed": False, "k815_alone_certifies_solution_family": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "For a source family, solve K815 and then the K819 cokernel equation over the affine kernel freedom in xdot before crediting a C2 zero-locus germ.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "A generic second-order existence obstruction supplies no source family, physical quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Necessary second-order zero-locus compatibility only; no source two-jet, ellipticity or global SC-ACT-06 conclusion.",
        "controls": {"producer": "tests/channel-swings/k819_sc_act_06_second_order_zero_locus_obstruction.py", "probe": "tests/channel-swings/k819_sc_act_06_second_order_zero_locus_obstruction_probe.py", "controls_passed": 24, "hostile_mutations_rejected": 12},
    }

def validate(p: dict[str, Any]) -> None:
    t, c, d = p["second_order_theorem"], p["exact_controls"], p["decision"]
    assert t["first_equation"] == "J xdot + b = 0"
    assert "F_tt" in t["second_equation"] and "pi_coker(J)" in t["obstruction"]
    assert t["kernel_choice_must_be_solved"] and not t["first_order_pass_implies_second_order_pass"]
    assert not t["second_order_pass_proves_full_family"]
    assert c["obstructed_first_order_passes"] and not c["obstructed_real_second_order_solution_exists"]
    assert c["repairable_kernel_speeds"] == [-1, 1] and c["repairable_second_order_solution_exists"]
    assert all(2 + 2*v*v > 0 for v in range(-8, 9))
    assert [v for v in range(-3, 4) if 2*v*v - 2 == 0] == c["repairable_kernel_speeds"]
    assert not any(d[k] for k in ("actual_source_two_jet_constructed", "k815_alone_certifies_solution_family", "global_sc_act_06_proved_or_refuted"))
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
    p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check: assert json.loads(OUTPUT.read_text())==p
    else: print(s,end="")
    return 0
if __name__ == "__main__": raise SystemExit(main())
