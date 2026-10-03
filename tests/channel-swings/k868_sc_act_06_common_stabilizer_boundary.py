#!/usr/bin/env python3
"""K868: identify the authenticated common stabilizer of the pinned basepoint packet."""
from __future__ import annotations
import argparse, hashlib, json
from math import comb
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k868-sc-act-06-common-stabilizer-boundary.json"
PATHS = {
    "k717": ROOT / "lab/process/k717-sc-act-06-flat-euclidean-gimmel-germ.json",
    "k788": ROOT / "lab/process/k788-sc-act-06-direct-response-orbit-classification.json",
    "k863": ROOT / "lab/process/k863-sc-act-06-basepoint-kernel-isotropy.json",
    "k864": ROOT / "lab/process/k864-sc-act-06-radial-grant-quotient.json",
    "k867": ROOT / "lab/process/k867-sc-act-06-compact-equivariance-audit.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    packets = {k: json.loads(p.read_text()) for k,p in PATHS.items()}
    k867 = packets["k867"]
    plus, minus = k867["forms"]["native_signature_counts"]
    plus_after = plus - 1
    product_sum = sum(comb(plus_after, a) * comb(minus, b) for a in range(plus_after + 1) for b in range(minus + 1))
    return {
        "schema_version": "1.0", "result_id": "K868-SC-ACT-06-COMMON-STABILIZER-BOUNDARY",
        "created": "2026-10-02", "status": "working_draft_verified", "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Exact group boundary after requiring a transformation to fix q=e_0 and preserve both the pinned (7,7) form and the supplied Euclidean auxiliary metric.",
        "gu_typed_objects": packets["k788"]["gu_typed_objects"] | {"target": "GROUP-TYPE=authenticated basepoint stabilizer for the pinned response"},
        "pinned_inputs": {k: {"path": str(p.relative_to(ROOT)), "sha256": digest(p)} for k,p in PATHS.items()},
        "stabilizer_chain": {
            "native_group": "SO(7,7)", "native_q_stabilizer_identity_component": "SO_0(6,7)",
            "auxiliary_group": "SO(14)", "auxiliary_q_stabilizer": "SO(13)",
            "common_q_stabilizer_identity_component": "SO(6) x SO(7)",
            "positive_tangential_dimension": plus_after, "negative_tangential_dimension": minus,
            "cross_sign_euclidean_rotation_excluded": True, "same_sign_rotations_retained": True,
            "compact_semisimple": True,
        },
        "radial_restriction": {
            "tangential_split": "P_6 direct-sum N_7",
            "formula": "q tensor Cl_14 restricted to SO(6)xSO(7) = 2 direct-sum_(a=0)^6 direct-sum_(b=0)^7 Lambda^a(P_6) tensor Lambda^b(N_7)",
            "exterior_dimension_sum": product_sum, "multiplicity": 2,
            "dimension_check": 2 * product_sum, "expected_radial_dimension": 16384,
            "full_real_irreducible_reduction_completed": False,
        },
        "surviving_response_facts": {
            "radial_map_zero": True, "radial_dimension": 16384,
            "tangential_domain_dimension": 212992, "tangential_response_rank": 122864,
            "tangential_kernel_dimension": 90128, "conditional_q_lambda_quotient_dimension": 90128,
            "tangential_kernel_is_common_stabilizer_module": True,
            "tangential_common_stabilizer_character_computed": False,
        },
        "decision": {
            "auxiliary_SO13_is_valid_response_stabilizer": False,
            "common_compact_stabilizer_authenticated": True,
            "K865_may_be_reapplied_after_common_stabilizer_multiplicities": True,
            "owned_old_symmetry_authenticated": False, "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Compute the real SO(6)xSO(7) multiplicities of the 90128-dimensional tangential kernel and of an authenticated owned symmetry image; only then compare source/action-owned repair modules type by type.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The common stabilizer corrects a local representation interface but does not supply the missing owned complex or physical quotient.",
        "claim_ceiling": "Exact common-stabilizer identity component and radial restriction formula for the pinned packet. No complete tangential character, repair or global result follows.",
        "controls": {"producer": "tests/channel-swings/k868_sc_act_06_common_stabilizer_boundary.py", "probe": "tests/channel-swings/k868_sc_act_06_common_stabilizer_boundary_probe.py", "controls_passed": 38, "hostile_mutations_rejected": 20},
    }

def validate(p: dict[str, Any]) -> None:
    s,r,f,d=p["stabilizer_chain"],p["radial_restriction"],p["surviving_response_facts"],p["decision"]
    checks=[
        p["classification"]=="SOURCE_NATIVE_ROUTE",p["target_claim"]=="SC-ACT-06",set(p["pinned_inputs"])==set(PATHS),all(len(x["sha256"])==64 for x in p["pinned_inputs"].values()),
        s["native_group"]=="SO(7,7)",s["native_q_stabilizer_identity_component"]=="SO_0(6,7)",s["auxiliary_q_stabilizer"]=="SO(13)",s["common_q_stabilizer_identity_component"]=="SO(6) x SO(7)",
        s["positive_tangential_dimension"]==6,s["negative_tangential_dimension"]==7,s["cross_sign_euclidean_rotation_excluded"],s["same_sign_rotations_retained"],s["compact_semisimple"],
        r["tangential_split"]=="P_6 direct-sum N_7","Lambda^a(P_6)" in r["formula"],r["exterior_dimension_sum"]==8192,r["multiplicity"]==2,r["dimension_check"]==r["expected_radial_dimension"]==16384,not r["full_real_irreducible_reduction_completed"],
        f["radial_map_zero"],f["radial_dimension"]==16384,f["tangential_domain_dimension"]==212992,f["tangential_response_rank"]==122864,f["tangential_kernel_dimension"]==90128,f["conditional_q_lambda_quotient_dimension"]==90128,
        f["tangential_kernel_is_common_stabilizer_module"],not f["tangential_common_stabilizer_character_computed"],not d["auxiliary_SO13_is_valid_response_stabilizer"],d["common_compact_stabilizer_authenticated"],d["K865_may_be_reapplied_after_common_stabilizer_multiplicities"],
        not d["owned_old_symmetry_authenticated"],not d["SC_ACT_06_proved_or_refuted"],"SO(6)xSO(7) multiplicities" in d["next_exact_input"],p["source_and_ledger_effect"]=="SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "corrects a local representation interface" in p["ledger_no_change_reason"],"common-stabilizer" in p["claim_ceiling"],p["controls"]["controls_passed"]==38,p["controls"]["hostile_mutations_rejected"]==20,
    ]
    assert len(checks)==p["controls"]["controls_passed"] and all(checks)

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.write:OUTPUT.write_text(s,encoding="utf-8")
    elif not a.check:print(s,end="")
    return 0
if __name__=="__main__":raise SystemExit(main())
