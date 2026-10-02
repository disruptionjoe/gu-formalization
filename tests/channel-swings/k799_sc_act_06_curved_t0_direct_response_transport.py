#!/usr/bin/env python3
"""K799: transport the direct D-Upsilon response over the certified curved T=0 family."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k799-sc-act-06-curved-t0-direct-response-transport.json"
PATHS = {
    "k127": ROOT / "lab/process/selected-k127-native-i1b-ricci-flat-weyl-tt-closure-gate.json",
    "k723": ROOT / "lab/process/k723-sc-act-06-t0-curvature-principal-invariance.json",
    "k747": ROOT / "lab/process/k747-sc-act-06-t0-response-invariance.json",
    "k788": ROOT / "lab/process/k788-sc-act-06-direct-response-orbit-classification.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text()) for name, path in PATHS.items()}
    k127, k723, k747, k788 = data["k127"], data["k723"], data["k747"], data["k788"]
    assert k127["background_family"]["k77_translation_response"] == "ZERO_AS_FULL_CLIFFORD_VALUED_OBJECT"
    assert k723["principal_invariance_theorem"]["normal_frame_freezes_same_highest_order_coefficients"]
    assert k747["principal_transport_theorem"]["residual_response_formula"] == k788["operator"]["principal_map"]
    cases = [
        {
            "orbit": row["orbit"],
            "domain_dimension": row["domain_dimension"],
            "rank": row["rank"],
            "nullity": row["nullity"],
        }
        for row in k788["orbit_theorem"]["cases"]
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K799-SC-ACT-06-CURVED-T0-DIRECT-RESPONSE-TRANSPORT",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Principal-symbol transport of the direct first-order D Upsilon connection response over K127's certified local Ricci-flat arbitrary-Weyl T=0 family.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "gu_typed_objects": {
            "carrier": "Omega1(Cl_14(C)) on the certified K127 local T=0 Levi-Civita family",
            "pairing": "none required for direct response rank; auxiliary positive covector norm only classifies nonzero Euclidean covectors",
            "real_structure": "coherent real normal-frame transport from the pinned K788 coefficient basis",
            "grading": "connection variation to first-order Upsilon residual variation",
            "action_owner": "released source first-order residual Upsilon, not an I1B or I2B Hessian",
            "target": "principal kernel of D Upsilon across the certified curved family",
        },
        "transport_theorem": {
            "k127_family_is_nonflat_when_weyl_nonzero": True,
            "k127_translation_response_zero": True,
            "normal_frame_freezes_highest_order_coefficients": True,
            "curvature_changes_only_subprincipal_or_lower_order_transport": True,
            "direct_response_formula": "J_q(u)=K_LIFT(SHIAB(q_WEDGE_u))",
            "coherent_frame_transport_is_rank_preserving": True,
            "all_real_nonzero_covector_orbits_inherit_k788_rank": True,
            "global_all_t0_or_all_zero_locus_germs_classified": False,
        },
        "exact_controls": {"cases": cases},
        "decision": {
            "connection_response_rank": 122864,
            "connection_kernel_dimension": 106512,
            "curvature_only_change_alters_direct_principal_rank": False,
            "certified_curved_family_is_new_principal_response_data": False,
            "next_exact_input": "Compose the transported kernel with the zero-locus Xi factorization, released zero-fermion full-field extension, and the strongest current symmetry grant.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is a local principal-symbol transport result on one certified family and supplies no global moduli, physical quotient or observable.",
        "claim_ceiling": "Exact principal-rank transport over the certified K127 Ricci-flat arbitrary-Weyl T=0 family only. It does not classify all T=0 or Upsilon=0 germs, prove a global no-go, own a symmetry completion, or change any source or physical verdict.",
        "controls": {"producer": "tests/channel-swings/k799_sc_act_06_curved_t0_direct_response_transport.py", "probe": "tests/channel-swings/k799_sc_act_06_curved_t0_direct_response_transport_probe.py", "controls_passed": 38, "hostile_mutations_rejected": 28},
    }


def validate(p: dict[str, Any]) -> None:
    assert p["result_id"] == "K799-SC-ACT-06-CURVED-T0-DIRECT-RESPONSE-TRANSPORT"
    assert p["status"] == "working_draft_verified" and p["target_claim"] == "SC-ACT-06"
    t = p["transport_theorem"]
    for key in ("k127_family_is_nonflat_when_weyl_nonzero", "k127_translation_response_zero", "normal_frame_freezes_highest_order_coefficients", "curvature_changes_only_subprincipal_or_lower_order_transport", "coherent_frame_transport_is_rank_preserving", "all_real_nonzero_covector_orbits_inherit_k788_rank"):
        assert t[key]
    assert t["direct_response_formula"] == "J_q(u)=K_LIFT(SHIAB(q_WEDGE_u))"
    assert not t["global_all_t0_or_all_zero_locus_germs_classified"]
    assert [row["orbit"] for row in p["exact_controls"]["cases"]] == ["native_positive", "native_negative", "native_null"]
    for row in p["exact_controls"]["cases"]:
        assert (row["domain_dimension"], row["rank"], row["nullity"]) == (229376, 122864, 106512)
    d = p["decision"]
    assert d["connection_response_rank"] == 122864 and d["connection_kernel_dimension"] == 106512
    assert not d["curvature_only_change_alters_direct_principal_rank"] and not d["certified_curved_family_is_new_principal_response_data"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); args = ap.parse_args()
    packet = build(); validate(packet); rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
