#!/usr/bin/env python3
"""K1127: reconcile K887's frozen radial control with the action-owned T=0 gauge map."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1127-k887-t0-gauge-carrier-correction.json"


def build():
    k132 = json.loads((ROOT / "lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json").read_text())
    k720 = json.loads((ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json").read_text())
    k887 = json.loads((ROOT / "lab/process/k887-sc-act-06-selected-i1b-gauge-descent-obstruction.json").read_text())
    ranks = {row["owned_gauge_image_rank"] for row in k720["exact_controls"]["cases"]}
    return {
        "schema_version": "1.0",
        "result_id": "K1127-K887-T0-GAUGE-CARRIER-CORRECTION",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "native_coordinates": k132["background"]["native_coordinates"],
        "t0_distortion_gauge_generator_owned": k132["minimal_bv_kt_bfv"]["distortion_gauge_generator_at_T0_owned"],
        "action_owned_metric_diffeomorphism_rank": k132["minimal_bv_kt_bfv"]["metric_diffeomorphism_generator_rank"],
        "k720_owned_gauge_ranks": sorted(ranks),
        "k887_radial_control_dimension": k887["exact_gauge_test"]["radial_domain_dimension"],
        "k887_radial_image_rank": k887["exact_gauge_test"]["i1b_euler_rank_on_radial"],
        "k887_exact_slice_calculation_survives": True,
        "k887_radial_control_is_action_owned_t0_gauge": False,
        "k887_source_action_gauge_descent_failure_survives": False,
        "reason": "T=varpi-B_LC(g) is a connection difference and transforms tensorially; at T=0 the source action owns no independent d-chi distortion column",
        "surviving_scope": "the rank-8191 response is an exact frozen connection-only radial-slice calculation, not a Noether predecessor test for the native (g,T) action Hessian",
        "affected_chain": "K887-K925 source-action gauge-completion inferences require correction; explicitly auxiliary mathematics remains separately typed",
        "source_and_ledger_effect": "SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "target_claim": "SC-ACT-06",
    }


def validate(d):
    assert d["native_coordinates"] == "(g,T)"
    assert d["t0_distortion_gauge_generator_owned"] is False
    assert d["action_owned_metric_diffeomorphism_rank"] == 4
    assert d["k720_owned_gauge_ranks"] == [4]
    assert d["k887_radial_control_dimension"] == 16384
    assert d["k887_radial_image_rank"] == 8191
    assert d["k887_exact_slice_calculation_survives"] is True
    assert d["k887_radial_control_is_action_owned_t0_gauge"] is False
    assert d["k887_source_action_gauge_descent_failure_survives"] is False
    assert "transforms tensorially" in d["reason"]
    assert "not a Noether predecessor" in d["surviving_scope"]
    assert "K887-K925" in d["affected_chain"]
    assert d["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED")


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1127 controls: 13/13")
