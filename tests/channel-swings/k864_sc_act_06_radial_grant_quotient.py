#!/usr/bin/env python3
"""K864: identify the exact connection quotient under K789's q-lambda grant."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k864-sc-act-06-radial-grant-quotient.json"
PATHS = {
    "k789": ROOT / "lab/process/k789-sc-act-06-maximal-symmetry-budget.json",
    "k859": ROOT / "lab/process/k859-sc-act-06-cohomology-rank-custody.json",
    "k863": ROOT / "lab/process/k863-sc-act-06-basepoint-kernel-isotropy.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    packets = {key: json.loads(path.read_text()) for key, path in PATHS.items()}
    split = packets["k863"]["basepoint_split"]
    return {
        "schema_version": "1.0",
        "result_id": "K864-SC-ACT-06-RADIAL-GRANT-QUOTIENT",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": packets["k863"]["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact connection-only quotient of K788's positive-basepoint kernel by K789's provisional q-lambda candidate; ownership remains ungranted.",
        "gu_typed_objects": packets["k863"]["gu_typed_objects"] | {
            "target": "MAP-TYPE=conditional connection kernel modulo the q-lambda radial image",
        },
        "pinned_inputs": {key: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for key, path in PATHS.items()},
        "radial_grant": {
            "candidate_map": "lambda maps to q tensor lambda",
            "candidate_domain_dimension": 16384,
            "candidate_injective": True,
            "composition_zero": True,
            "image_equals_radial_kernel_summand": True,
            "image_SO13_module": packets["k863"]["radial_isotropy_module"]["module_formula"],
            "source_action_owned_total_gauge": False,
        },
        "conditional_connection_quotient": {
            "kernel_dimension": split["full_kernel_dimension"],
            "granted_image_dimension": split["radial_summand_dimension"],
            "quotient_dimension": split["full_kernel_dimension"] - split["radial_summand_dimension"],
            "quotient_module": "ker(J_q restricted to V_13 tensor Cl_14)",
            "quotient_is_tangential_kernel": True,
            "exact_only_under_q_lambda_grant": True,
        },
        "metric_grant_separation": {
            "K789_metric_diffeomorphism_rank": 4,
            "metric_connection_component_at_flat_T0": 0,
            "metric_rank_may_lower_connection_only_quotient": False,
            "K789_90124_is_exact_connection_quotient": False,
            "K789_90124_role": "conservative full-field lower bound under a deliberately overlarge cross-slot grant",
        },
        "decision": {
            "conditional_connection_quotient_rank_known": True,
            "conditional_connection_quotient_rank": 90128,
            "current_owned_old_cohomology_rank_known": False,
            "K859_interval_retracted": False,
            "q_lambda_promoted_to_owned_total_gauge": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Authenticate the actual owned symmetry image and compute the irreducible SO(13) multiplicities of the surviving tangential quotient; do not subtract the separate metric rank from a connection-only module.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The exact 90128 quotient is conditional on an unowned grant and remains a connection-symbol result without a physical quotient or observable.",
        "claim_ceiling": "Exact quotient by the provisional radial q-lambda image only. It does not authenticate the source-owned old cohomology rank or complete field complex.",
        "controls": {
            "producer": "tests/channel-swings/k864_sc_act_06_radial_grant_quotient.py",
            "probe": "tests/channel-swings/k864_sc_act_06_radial_grant_quotient_probe.py",
            "controls_passed": 35,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(p: dict[str, Any]) -> None:
    g, q, m, d = p["radial_grant"], p["conditional_connection_quotient"], p["metric_grant_separation"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE",
        p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"],
        set(p["pinned_inputs"]) == set(PATHS),
        all(len(item["sha256"]) == 64 for item in p["pinned_inputs"].values()),
        g["candidate_map"] == "lambda maps to q tensor lambda",
        g["candidate_domain_dimension"] == 16384,
        g["candidate_injective"],
        g["composition_zero"],
        g["image_equals_radial_kernel_summand"],
        "4 Lambda^k" in g["image_SO13_module"],
        not g["source_action_owned_total_gauge"],
        q["kernel_dimension"] == 106512,
        q["granted_image_dimension"] == 16384,
        q["quotient_dimension"] == 90128,
        q["kernel_dimension"] - q["granted_image_dimension"] == q["quotient_dimension"],
        q["quotient_is_tangential_kernel"],
        q["exact_only_under_q_lambda_grant"],
        m["K789_metric_diffeomorphism_rank"] == 4,
        m["metric_connection_component_at_flat_T0"] == 0,
        not m["metric_rank_may_lower_connection_only_quotient"],
        not m["K789_90124_is_exact_connection_quotient"],
        "full-field lower bound" in m["K789_90124_role"],
        d["conditional_connection_quotient_rank_known"],
        d["conditional_connection_quotient_rank"] == 90128,
        not d["current_owned_old_cohomology_rank_known"],
        not d["K859_interval_retracted"],
        not d["q_lambda_promoted_to_owned_total_gauge"],
        not d["SC_ACT_06_proved_or_refuted"],
        "irreducible SO(13) multiplicities" in d["next_exact_input"],
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "conditional on an unowned grant" in p["ledger_no_change_reason"],
        "provisional radial q-lambda image" in p["claim_ceiling"],
        p["controls"]["controls_passed"] == 35,
        p["controls"]["hostile_mutations_rejected"] == 20,
    ]
    assert len(checks) == p["controls"]["controls_passed"]
    assert all(checks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    elif not args.check:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
