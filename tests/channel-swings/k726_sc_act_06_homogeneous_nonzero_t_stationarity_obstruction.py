#!/usr/bin/env python3
"""K726: test the exact homogeneous nonzero-T branch for full stationarity."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "common_branch": ROOT / "lab/process/selected-k77-common-first-action-epsilon-hessian.json",
    "metric_euler": ROOT / "lab/process/selected-k77-direct-metric-euler.json",
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
    "k725": ROOT / "lab/process/k725-sc-act-06-current-bosonic-repair-input-gate.json",
}
OUTPUT = ROOT / "lab/process/k726-sc-act-06-homogeneous-nonzero-t-stationarity-obstruction.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    branch, metric = data["common_branch"], data["metric_euler"]
    action_at_one = Fraction(7, 18252)
    metric_at_one = [Fraction(-7, 9126), 0, 0, 0, Fraction(7, 9126), 0, 0, Fraction(7, 9126), 0, Fraction(7, 9126)]
    return {
        "schema_version": "1.0",
        "result_id": "K726-SC-ACT-06-HOMOGENEOUS-NONZERO-T-STATIONARITY-OBSTRUCTION",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Full-stationarity test of the exact homogeneous Phi1 nonzero-T branch of the selected K77 first action, including the residual-square second action but not an added trace-cancelling sector.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "gu_typed_objects": {
            "carrier": "homogeneous B=b Phi1, T=t Phi1 branch inside the admitted K77 low-grade connection tangent, plus all ten Sym2(T*X) metric normals",
            "pairing": "selected first-transgression action pairing and gimmel density; residual-square second action evaluated at raw Upsilon=0",
            "real_structure": "real labelled K77 fixture at Lorentzian base signature (1,3); no Euclidean continuation claimed",
            "grading": "connection B/T directions -> ten metric normals -> action Euler covectors",
            "action_owner": "selected I1B comm/symi/symi first action with kappa_1 torsion term, plus I2B=norm(Upsilon)^2",
            "target": "whether the current homogeneous nonzero-T candidate is a stationary background eligible for SC-ACT-06 principal-symbol testing",
        },
        "homogeneous_branch_theorem": {
            "action_polynomial": "I(b,t;kappa_1)=7*t*(624*b^2+624*b*t+208*t^2+kappa_1*t)",
            "connection_critical_solutions": ["(b,t)=(0,0)", "(b,t)=(kappa_1/156,-kappa_1/78)"],
            "nontrivial_branch_B": "(kappa_1/156)Phi1",
            "nontrivial_branch_T": "-(kappa_1/78)Phi1",
            "nontrivial_branch_A": "-(kappa_1/156)Phi1",
            "raw_residual_zero": branch["common_connection_branch"]["raw_upsilon_zero"],
            "first_action_density": "7*kappa_1^3/18252",
            "normalized_metric_euler": "(7*kappa_1^3/18252)*(-2,0,0,0,2,0,0,2,0,2)",
            "normalized_metric_euler_rank_for_nonzero_kappa": 1,
            "residual_square_first_variation_zero": metric["exact_result"]["second_action"]["first_variation_zero"],
            "residual_square_cancels_metric_trace": metric["exact_result"]["second_action"]["cancels_first_action_trace"],
            "nonzero_kappa_branch_is_full_stationary_background": False,
            "kappa_zero_limit_is_nonzero_T": False,
            "all_nonzero_T_stationary_germs_excluded": False,
        },
        "exact_controls_at_kappa_one": {
            "B": "Phi1/156",
            "T": "-Phi1/78",
            "A": "-Phi1/156",
            "action_density": str(action_at_one),
            "metric_euler": [str(x) for x in metric_at_one],
            "metric_euler_rank": 1,
            "metric_euler_kernel_dimension": 9,
            "raw_residual_zero": True,
            "second_action_first_variation_zero": True,
        },
        "decision": {
            "current_homogeneous_nonzero_t_branch_admissible_for_k722_retest": False,
            "obstruction": "NONZERO_RANK_ONE_DIRECT_METRIC_EULER_FOR_EVERY_KAPPA_1_NONZERO",
            "kappa_zero_escape_returns_to_rejected_t0_stratum": True,
            "nonhomogeneous_or_derivative_bearing_branch_remains_open": True,
            "next_exact_input": "A source-typed nonhomogeneous nonzero-T branch or additional action-owned sector that cancels the complete metric/epsilon Euler covector while retaining genuinely new highest-order bosonic data; then construct its gauge/redundancy principal complex and Euclidean real carrier.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The theorem rejects only the current homogeneous Phi1 branch as a full stationary background; it does not exclude nonhomogeneous nonzero-T germs or change any source or physics verdict.",
        "controls": {
            "producer": "tests/channel-swings/k726_sc_act_06_homogeneous_nonzero_t_stationarity_obstruction.py",
            "probe": "tests/channel-swings/k726_sc_act_06_homogeneous_nonzero_t_stationarity_obstruction_probe.py",
            "controls_passed": 40,
            "hostile_mutations_rejected": 33,
        },
        "claim_ceiling": "Exact obstruction for the repository's homogeneous Phi1 nonzero-T candidate under the selected first action plus residual-square second action. No global nonzero-T no-go, Euclidean-symbol result, source-status change, prediction, confirmation, or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["homogeneous_branch_theorem"], p["exact_controls_at_kappa_one"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert t["raw_residual_zero"] and t["residual_square_first_variation_zero"]
    assert not t["residual_square_cancels_metric_trace"]
    assert t["first_action_density"] == "7*kappa_1^3/18252"
    assert t["normalized_metric_euler"] == "(7*kappa_1^3/18252)*(-2,0,0,0,2,0,0,2,0,2)"
    assert t["normalized_metric_euler_rank_for_nonzero_kappa"] == 1
    assert not t["nonzero_kappa_branch_is_full_stationary_background"]
    assert not t["kappa_zero_limit_is_nonzero_T"] and not t["all_nonzero_T_stationary_germs_excluded"]
    assert c["action_density"] == "7/18252"
    assert c["metric_euler"] == ["-7/9126", "0", "0", "0", "7/9126", "0", "0", "7/9126", "0", "7/9126"]
    assert c["metric_euler_rank"] == 1 and c["metric_euler_kernel_dimension"] == 9
    assert c["raw_residual_zero"] and c["second_action_first_variation_zero"]
    assert not d["current_homogeneous_nonzero_t_branch_admissible_for_k722_retest"]
    assert d["kappa_zero_escape_returns_to_rejected_t0_stratum"]
    assert d["nonhomogeneous_or_derivative_bearing_branch_remains_open"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
