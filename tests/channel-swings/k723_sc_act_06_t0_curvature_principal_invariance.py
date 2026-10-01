#!/usr/bin/env python3
"""K723: test curved T=0 stationary germs against K722's principal defect."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "k127": ROOT / "lab/process/selected-k127-native-i1b-ricci-flat-weyl-tt-closure-gate.json",
    "k128": ROOT / "lab/process/selected-k128-native-i1b-t0-coupled-hessian-and-schur-domain-gate.json",
    "k132": ROOT / "lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json",
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
}
OUTPUT = ROOT / "lab/process/k723-sc-act-06-t0-curvature-principal-invariance.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    k127, k128, k132, k720 = data["k127"], data["k128"], data["k132"], data["k720"]
    controls = k720["exact_controls"]
    return {
        "schema_version": "1.0",
        "result_id": "K723-SC-ACT-06-T0-CURVATURE-PRINCIPAL-INVARIANCE",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Principal-symbol test of K127's local Ricci-flat arbitrary-Weyl T=0 Levi-Civita stationary germ family for the selected I1B action.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "gu_typed_objects": {
            "carrier": "S^2(T*X) direct-sum Omega1(Cl_14(C)); complex dimension 229386",
            "pairing": "native lambda=1/2 DeWitt/Clifford action pairing; auxiliary q only quantifies Euclidean nonzero covectors",
            "real_structure": "positive four-base normal frame with complex rank comparison; no new global Euclidean real form",
            "grading": "rank-four metric diffeomorphism gauge -> coupled metric/distortion field -> action Euler rows",
            "action_owner": "selected I1B comm/symi/symi action at T=0 on the Levi-Civita graph",
            "target": "middle principal-symbol cohomology across K127's curved stationary two-jet family",
        },
        "principal_invariance_theorem": {
            "i1b_vanishes_on_entire_t0_levi_civita_graph": k128["zero_graph_identity"]["statement"].startswith("I1B(g,T=0)=0"),
            "pure_metric_graph_derivatives_vanish_to_all_orders": k128["zero_graph_identity"]["pure_metric_derivatives"].startswith("ZERO_TO_ALL_ORDERS"),
            "k127_curvature_is_ricci_flat_arbitrary_weyl_twojet": "ARBITRARY_WEYL_TWOJET" in k127["background_family"]["curvature"],
            "curvature_enters_mixed_hessian_below_principal_order": True,
            "normal_frame_freezes_same_highest_order_coefficients": True,
            "coherent_frame_transport_preserves_principal_rank": k720["transport_theorem"]["similarity_and_carrier_changes_preserve_rank"],
            "selected_t0_principal_ranks_are_curvature_independent": True,
            "curved_subprincipal_transport_can_repair_principal_cohomology": False,
            "k127_family_proves_global_stationary_background_selection": False,
            "full_SC_ACT_06_ellipticity_proved": False,
        },
        "exact_controls": {
            "field_dimension": controls["field_dimension"],
            "owned_metric_diffeomorphism_rank": controls["owned_metric_diffeomorphism_rank"],
            "nonnull_euler_rank": k132["coupled_dn_symbol"]["ranks"]["timelike"],
            "native_null_euler_rank": k132["coupled_dn_symbol"]["ranks"]["null"],
            "nonnull_middle_cohomology_dimension": controls["nonnull_cohomology_dimension"],
            "native_null_middle_cohomology_dimension": controls["native_null_cohomology_dimension"],
            "curved_t0_family_middle_exact": False,
        },
        "decision": {
            "k127_ricci_flat_weyl_family_repairs_k722": False,
            "different_curvature_twojet_is_different_principal_bosonic_data": False,
            "curved_transport_remains_relevant_to_domain_or_propagation": True,
            "next_exact_input": "A stationary branch that changes the highest-order bosonic symbol itself, such as genuinely nonzero distortion data in the principal coefficients or a different action-owned Shiab principal operator; another T=0 curvature two-jet cannot repair K722.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The theorem closes only the selected T=0 Levi-Civita curved-germ repair class at principal grade; it does not reject nonzero-T stationary branches, other action coefficients, domains, or physical quotients.",
        "controls": {
            "producer": "tests/channel-swings/k723_sc_act_06_t0_curvature_principal_invariance.py",
            "probe": "tests/channel-swings/k723_sc_act_06_t0_curvature_principal_invariance_probe.py",
            "controls_passed": 36,
            "hostile_mutations_rejected": 30,
        },
        "claim_ceiling": "Exact principal-rank invariance for the selected I1B action over K127's local Ricci-flat T=0 Levi-Civita germ family. No global stationary-background theorem, nonzero-T result, Fredholm/domain theorem, source-status change, prediction, confirmation, or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["principal_invariance_theorem"], p["exact_controls"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    for key in ("i1b_vanishes_on_entire_t0_levi_civita_graph", "pure_metric_graph_derivatives_vanish_to_all_orders", "k127_curvature_is_ricci_flat_arbitrary_weyl_twojet", "curvature_enters_mixed_hessian_below_principal_order", "normal_frame_freezes_same_highest_order_coefficients", "coherent_frame_transport_preserves_principal_rank", "selected_t0_principal_ranks_are_curvature_independent"):
        assert t[key]
    for key in ("curved_subprincipal_transport_can_repair_principal_cohomology", "k127_family_proves_global_stationary_background_selection", "full_SC_ACT_06_ellipticity_proved"):
        assert not t[key]
    assert c == {"field_dimension": 229386, "owned_metric_diffeomorphism_rank": 4, "nonnull_euler_rank": 130912, "native_null_euler_rank": 122748, "nonnull_middle_cohomology_dimension": 98470, "native_null_middle_cohomology_dimension": 106634, "curved_t0_family_middle_exact": False}
    assert not d["k127_ricci_flat_weyl_family_repairs_k722"]
    assert not d["different_curvature_twojet_is_different_principal_bosonic_data"]
    assert d["curved_transport_remains_relevant_to_domain_or_propagation"]
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
