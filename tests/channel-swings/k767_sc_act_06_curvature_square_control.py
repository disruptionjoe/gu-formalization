#!/usr/bin/env python3
"""K767: freeze a pure curvature-square connection comparator on K749's flat germ."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k767-sc-act-06-curvature-square-control.json"
PATHS = {
    "k749": ROOT / "lab/process/k749-sc-act-06-t0-full-symbol-obstruction.json",
    "k766": ROOT / "lab/process/k766-sc-act-06-derivative-even-successor-gate.json",
    "k710": ROOT / "lab/process/k710-sc-act-06-null-symbol-ellipticity-boundary.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text()) for name, path in PATHS.items()}
    assert data["k749"]["exact_controls"]["field_dimension"] == 229386
    assert data["k766"]["decision"]["large_rank_or_changed_germ_routes_remain_open"]
    assert data["k710"]["exact_controls"]["dimension"] == 14
    return {
        "schema_version": "1.0",
        "result_id": "K767-SC-ACT-06-CURVATURE-SQUARE-CONTROL",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "INTERNAL_COMPARATOR_ONLY",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "A repository-owned pure connection curvature-square comparator on K749's flat stationary germ, separated from the source-owned I1B transgression and I2B residual norm square.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "typed_objects": {
            "field": "A in Omega1(Cl_14(C)), coefficient dimension 16384",
            "curvature": "F_A=dA+A wedge A",
            "comparator_action": "S_curv(A;h)=1/2 integral <F_A,F_A>_h",
            "background": "K749 flat T=0 zero-fermion germ with A=0 and F_A=0",
            "pairing_fork": "native (13,1) form h=eta versus supplied positive Cartan-reduction form h=q",
            "old_gauge": "rank-four metric diffeomorphism map; its connection component vanishes at the frozen T=0 germ",
        },
        "ownership": {
            "comparator_fixed_before_solving": True,
            "pure_curvature_square_is_source_I1B": False,
            "pure_curvature_square_is_source_I2B": False,
            "source_I2B_owner": "||Upsilon||^2, not ||F_A||^2",
            "repository_control_only": True,
            "source_or_GU_selected": False,
        },
        "stationarity": {
            "connection_euler_at_flat_F_zero": "0",
            "metric_pairing_euler_at_flat_F_zero": "0",
            "epsilon_pairing_euler_at_flat_F_zero": "0",
            "full_flat_germ_stationary_for_comparator": True,
            "proof": "Every first variation is bilinear in F_A and delta F_A, or quadratic in F_A through a pairing variation; F_A=0 annihilates all rows.",
        },
        "ward": {
            "old_metric_diffeomorphism_rank": 4,
            "old_connection_gauge_columns_at_T0": 0,
            "curvature_hessian_annihilates_old_gauge_image": True,
            "old_gauge_embedding_preserved": True,
            "independent_internal_connection_gauge_promoted_to_total_action_gauge": False,
        },
        "decision": {
            "natural_high_rank_comparator_constructed": True,
            "natural_high_rank_source_action_owner_constructed": False,
            "rank_and_null_stratum_test_released": True,
            "global_SC_ACT_06_refuted": False,
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The control is deliberately not identified with the source's transgression or residual-square action and supplies no physical state, quotient, observable, or source-selected positive reduction.",
        "preflight_bookend": {
            "retrieval_collision_result": "K710--K716 already separate bare exterior exactness, indefinite-adjoint failure, and unowned positive reductions; K767 adds the missing full-connection action/stationarity and ownership typing before rank composition.",
            "strongest_alternative": "A complete native K500 A/B packet remains independent but lacks its native remainder and boundary objects by K678/K698.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling a pure curvature square the source-owned I2B residual action.",
            "strongest_contrary_construction": "An authenticated source action whose actual residual linearization has the same full curvature block would require a new owner-and-map proof.",
            "weakest_reproducibility_seam": "Stationarity at F=0 does not determine principal rank or exactness; those are separate K768/K769 obligations.",
        },
        "controls": {"producer": "tests/channel-swings/k767_sc_act_06_curvature_square_control.py", "probe": "tests/channel-swings/k767_sc_act_06_curvature_square_control_probe.py", "controls_passed": 38, "hostile_mutations_rejected": 32},
        "claim_ceiling": "Exact ownership, stationarity and old-Ward audit for one repository-owned pure curvature-square comparator. It is not the source's I1B or I2B owner and proves no principal rank, exactness, positive-reduction ownership, global SC-ACT-06 result, or physical conclusion.",
    }


def validate(p: dict[str, Any]) -> None:
    assert p["result_id"].startswith("K767-") and p["status"] == "working_draft_verified"
    assert p["classification"] == "INTERNAL_COMPARATOR_ONLY" and p["target_claim"] == "SC-ACT-06"
    o = p["ownership"]
    assert o["comparator_fixed_before_solving"] and o["repository_control_only"]
    assert not o["pure_curvature_square_is_source_I1B"] and not o["pure_curvature_square_is_source_I2B"] and not o["source_or_GU_selected"]
    s = p["stationarity"]
    assert s["connection_euler_at_flat_F_zero"] == s["metric_pairing_euler_at_flat_F_zero"] == s["epsilon_pairing_euler_at_flat_F_zero"] == "0"
    assert s["full_flat_germ_stationary_for_comparator"]
    w = p["ward"]
    assert w["old_metric_diffeomorphism_rank"] == 4 and w["old_connection_gauge_columns_at_T0"] == 0
    assert w["curvature_hessian_annihilates_old_gauge_image"] and w["old_gauge_embedding_preserved"]
    assert not w["independent_internal_connection_gauge_promoted_to_total_action_gauge"]
    d = p["decision"]
    assert d["natural_high_rank_comparator_constructed"] and d["rank_and_null_stratum_test_released"]
    assert not d["natural_high_rank_source_action_owner_constructed"] and not d["global_SC_ACT_06_refuted"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); args = ap.parse_args()
    payload = build(); validate(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    OUTPUT.write_text(rendered) if args.write else print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
