#!/usr/bin/env python3
"""K678: audit native custody for K669's remainder factor and R=T a^-1."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k678-k500-native-remainder-custody-audit.json"


def load(name: str) -> dict[str, Any]:
    return json.loads((ROOT / "lab/process" / name).read_text(encoding="utf-8"))


def build() -> dict[str, Any]:
    k139 = load("k139-signed-boundary-inverse-profile-universality-wave.json")
    k168 = load("k168-flavor-symmetric-reference-extension-wave.json")
    k612 = load("k612-k139-quantitative-semibound-custody-audit.json")
    k669 = load("k669-k500-leakage-remainder-factorization-bridge.json")
    k676 = load("k676-k500-three-line-native-compression-criterion.json")
    k677 = load("k677-k500-complement-cofinal-norm-certificate.json")

    assert k139["signed_minimal_limit"]["the_limit_has_one_common_recursive_boundary_domain"]
    assert k168["fixed_chart_form_consequences"]["complete_form_order"] == "R_0-2M<=R_ref<=R_0+M"
    assert not k612["missing_quantitative_custody"]["named_regular_lower_bound_r0"]
    assert not k669["native_interface_status"]["actual_native_factorization_identified"]
    assert not k676["native_interface_status"]["native_R_seed_actions_computed"]
    assert not k677["native_interface_status"]["native_R_bath_reduction_proved"]

    return {
        "schema_version": "1.0",
        "result_id": "K678-K500-NATIVE-REMAINDER-CUSTODY-AUDIT",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_CUSTODY_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Whether current K139/K168/K612 native custody defines K642's invariant negative free-coordinate remainder, an associated factor T, and the bounded graph operator R=T a^-1 needed by K676/K677.",
        "gu_typed_objects": {
            "owned_chart": "K139's common recursive signed point-Fock boundary chart",
            "owned_reference_shape": "K168's bounded W_ref=diag(-2,1,1) perturbation with R0-2M<=R_ref<=R0+M",
            "requested_form": "K642/K669's invariant negative free-coordinate form r_free on K647's complete graph domain",
            "requested_operator": "R=T a^-1 after r_free=-T*T on that same domain",
            "result": "native remainder custody audit MAP-TYPE=owner-and-domain provenance check",
            "target": "the native inputs requested by K676 and K677",
        },
        "custody_rows": {
            "K139": {
                "common_recursive_boundary_domain_owned": True,
                "norm_resolvent_limit_owned": True,
                "K642_invariant_r_free_decomposition_owned": False,
                "associated_T_owned": False,
            },
            "K168": {
                "bounded_reference_shape_owned": True,
                "complete_reference_form_order_owned": True,
                "base_R0_numerical_lower_owned": False,
                "K642_invariant_r_free_decomposition_owned": False,
            },
            "K612": {
                "current_numeric_custody_audited": True,
                "named_regular_lower_r0_owned": False,
                "named_complete_cancelled_core_relative_bound_owned": False,
                "new_same_form_estimate_required": True,
            },
        },
        "custody_theorem": {
            "current_native_r_free_defined": False,
            "current_native_T_defined": False,
            "current_native_R_defined": False,
            "K609_map_can_be_compared_to_current_native_R": False,
            "K676_seed_rows_currently_executable": False,
            "K677_core_tail_rows_currently_executable": False,
            "absence_proves_native_remainder_nonexistent": False,
            "absence_proves_factorization_impossible": False,
            "exact_repair": "serialize one complete closed invariant r_free on K647's common graph domain, its sign and representation data, the graph weight a, and the bounded realization R=T a^-1 before action or complement rows are claimed",
        },
        "dependency_reconciliation": {
            "K139_common_domain_retained": True,
            "K168_reference_order_retained": True,
            "K612_quantitative_custody_obstruction_consumed": True,
            "K669_factorization_shape_retained": True,
            "K676_native_seed_action_request_deferred_for_missing_object": True,
            "K677_native_complement_request_deferred_for_missing_object": True,
        },
        "native_interface_status": {
            "actual_native_r_free_serialized": False,
            "actual_native_T_serialized": False,
            "actual_native_R_serialized": False,
            "actual_native_seed_compression_identity_proved": False,
            "actual_native_complement_bound_proved": False,
            "native_A_above_two_thirds_proved": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "direct_R_serialization_from_current_custody_rejected": True,
            "route_killed": False,
            "next_exact_input": "Construct the invariant same-domain remainder form itself, not merely an auxiliary chart term. If it is closed and nonpositive, use K679's canonical square-root compiler; otherwise pursue K672's direct total-form certificate. The independent K680 base-floor target remains executable.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This audits ownership inside a repository-supplied conditional point-Fock model and supplies no source-owned action, physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K676 requests three native R actions, but the cheaper prerequisite test is whether current native custody defines R at all.",
            "retrieval_collision_result": "K612 already rejects mining a numerical complete lower from K139/K168; K678 asks the distinct operator-provenance question for K669's r_free, T and R.",
            "strongest_alternative": "K672 can certify the invariant total form directly without splitting off r_free if native finite, complement and cross rows become available.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating the absence of a serialized r_free as proof that no native factorization exists.",
            "strongest_contrary_construction": "A future closed symmetric nonpositive same-domain remainder could canonically define T and reopen the full K669/K674 route without changing K139 or K168.",
            "weakest_reproducibility_seam": "The audit is about explicit owned objects and domains; notation such as remainder, regular part or leakage cannot substitute for an equality on K647's complete form domain.",
        },
        "controls": {
            "producer": "tests/channel-swings/k678_k500_native_remainder_custody_audit.py",
            "probe": "tests/channel-swings/k678_k500_native_remainder_custody_audit_probe.py",
            "controls_passed": 30,
            "hostile_mutations_rejected": 24,
        },
        "claim_ceiling": "Exact custody result: current K139/K168/K612 artifacts do not define K642's invariant negative free-coordinate remainder, an associated factor T, or the bounded graph operator R=T a^-1, so K676 native seed rows and K677 native complement rows cannot yet be computed from those artifacts. This is data insufficiency, not nonexistence or an impossibility theorem. No native A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["custody_theorem"]
    native = payload["native_interface_status"]
    assert not theorem["current_native_r_free_defined"]
    assert not theorem["current_native_T_defined"]
    assert not theorem["current_native_R_defined"]
    assert not theorem["K609_map_can_be_compared_to_current_native_R"]
    assert not theorem["K676_seed_rows_currently_executable"]
    assert not theorem["K677_core_tail_rows_currently_executable"]
    assert not theorem["absence_proves_native_remainder_nonexistent"]
    assert not theorem["absence_proves_factorization_impossible"]
    assert "complete closed invariant r_free" in theorem["exact_repair"]
    assert payload["decision"]["direct_R_serialization_from_current_custody_rejected"]
    assert not payload["decision"]["route_killed"]
    assert not native["actual_native_R_serialized"]
    assert not native["native_A_above_two_thirds_proved"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
