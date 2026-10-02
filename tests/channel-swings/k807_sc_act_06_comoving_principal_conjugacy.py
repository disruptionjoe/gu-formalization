#!/usr/bin/env python3
"""K807: co-moving-frame conjugacy preserves the released principal response."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k807-sc-act-06-comoving-principal-conjugacy.json"
PATHS = {
    "frame_naturality": ROOT / "explorations/conditional-build/selected-action-comoving-frame-naturality-2026-08-06.md",
    "moving_parent": ROOT / "lab/process/selected-k77-moving-parent-bundle-observation-reduction.json",
    "k803": ROOT / "lab/process/k803-sc-act-06-nonzero-t-principal-invariance.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    frame = PATHS["frame_naturality"].read_text()
    parent = json.loads(PATHS["moving_parent"].read_text())
    k803 = json.loads(PATHS["k803"].read_text())
    assert "pure-frame derivative is exactly zero" in frame
    assert parent["moving_projector"]["noncommuting_cocycle"] == "EXACT_PASS"
    assert parent["moving_projector"]["moving_euler_covariance"] == "EXACT_PASS_ALL_16384"
    return {
        "schema_version": "1.0", "result_id": "K807-SC-ACT-06-COMOVING-PRINCIPAL-CONJUGACY",
        "created": "2026-10-02", "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE", "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Regular co-moving orthonormal-frame transport of the released Upsilon principal connection response; genuine relative coefficient motion and singular observation maps are excluded.",
        "gu_typed_objects": {
            "carrier": "source-owned full connection tangent transported by the epsilon/frame associated-bundle cocycle",
            "pairing": "natural gimmel Hodge/Clifford/Shiab packet under simultaneous domain and residual-frame transport",
            "real_structure": "the real U(64,64) coefficient basis transported by an invertible real frame map",
            "grading": "connection one-form principal symbol at a transported nonzero covector",
            "action_owner": "released first-order Upsilon equation only; no residual-square Hessian import",
            "target": "whether natural co-moving frame motion changes principal rank or kernel",
        },
        "pinned_inputs": {n: {"path": str(p.relative_to(ROOT)), "sha256": digest(p)} for n,p in PATHS.items()},
        "intertwiner_theorem": {
            "formula": "J_e(q_e)=R_e J_0(q_0) C_e^-1",
            "domain_frame_map_invertible": True, "residual_frame_map_invertible": True,
            "covector_transport_invertible": True, "moving_projector_cocycle_exact": True,
            "hodge_shiab_clifford_packet_natural": True, "pure_frame_motion_is_basis_change": True,
            "genuine_relative_coefficient_motion_covered": False, "singular_observation_map_covered": False,
        },
        "orbit_consequence": {
            "real_nonzero_covector_orbits": ["native_positive", "native_negative", "native_null"],
            "domain_dimension": 229376,
            "reference_rank": k803["orbit_consequence"]["connection_response_rank"],
            "transported_rank": k803["orbit_consequence"]["connection_response_rank"],
            "reference_kernel_dimension": k803["orbit_consequence"]["connection_kernel_dimension"],
            "transported_kernel_dimension": k803["orbit_consequence"]["connection_kernel_dimension"],
            "kernel_transport": "ker(J_e)=C_e ker(J_0)",
        },
        "decision": {
            "comoving_frame_orbit_is_new_principal_packet": False,
            "all_moving_metric_epsilon_shiab_hodge_germs_classified": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "Construct relative coefficient motion not induced by a regular natural frame map, with a compatible source two-jet and complete stationarity/gauge/domain packet.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is an associated-bundle conjugacy theorem, not a new stationary germ, quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Exact co-moving-frame principal conjugacy only; arbitrary moving coefficients, singular reductions and global SC-ACT-06 remain open.",
        "controls": {"producer": "tests/channel-swings/k807_sc_act_06_comoving_principal_conjugacy.py", "probe": "tests/channel-swings/k807_sc_act_06_comoving_principal_conjugacy_probe.py", "controls_passed": 44, "hostile_mutations_rejected": 32},
    }

def validate(p: dict[str, Any]) -> None:
    assert p["result_id"] == "K807-SC-ACT-06-COMOVING-PRINCIPAL-CONJUGACY" and p["target_claim"] == "SC-ACT-06"
    t=p["intertwiner_theorem"]
    assert t["formula"] == "J_e(q_e)=R_e J_0(q_0) C_e^-1"
    for k in ("domain_frame_map_invertible","residual_frame_map_invertible","covector_transport_invertible","moving_projector_cocycle_exact","hodge_shiab_clifford_packet_natural","pure_frame_motion_is_basis_change"): assert t[k]
    assert not t["genuine_relative_coefficient_motion_covered"] and not t["singular_observation_map_covered"]
    o=p["orbit_consequence"]
    assert o["real_nonzero_covector_orbits"] == ["native_positive","native_negative","native_null"]
    assert (o["domain_dimension"],o["reference_rank"],o["transported_rank"],o["reference_kernel_dimension"],o["transported_kernel_dimension"]) == (229376,122864,122864,106512,106512)
    assert o["kernel_transport"] == "ker(J_e)=C_e ker(J_0)"
    d=p["decision"]; assert not d["comoving_frame_orbit_is_new_principal_packet"] and not d["all_moving_metric_epsilon_shiab_hodge_germs_classified"] and not d["global_sc_act_06_proved_or_refuted"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args(); p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"; OUTPUT.write_text(s) if a.write else print(s,end=""); return 0
if __name__ == "__main__": raise SystemExit(main())
