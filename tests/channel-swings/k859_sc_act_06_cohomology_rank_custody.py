#!/usr/bin/env python3
"""K859: exact current cohomology-rank custody under the maximal grant."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k859-sc-act-06-cohomology-rank-custody.json"
K789 = ROOT / "lab/process/k789-sc-act-06-maximal-symmetry-budget.json"
K858 = ROOT / "lab/process/k858-sc-act-06-topological-repair-disposition.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    k789 = json.loads(K789.read_text())
    k858 = json.loads(K858.read_text())
    cases = k789["exact_controls"]["cases"]
    kernel = cases[0]["connection_kernel_dimension"]
    ceiling = cases[0]["maximal_granted_symmetry_budget"]
    lower = kernel - ceiling
    attainable = [kernel - rank for rank in range(ceiling + 1)]
    return {
        "schema_version": "1.0",
        "result_id": "K859-SC-ACT-06-COHOMOLOGY-RANK-CUSTODY",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": k858["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Rank custody for the current K788/K789 flat connection kernel under the deliberately overlarge symmetry grant; no complete cosphere bundle or owned symmetry map is inferred.",
        "gu_typed_objects": k858["gu_typed_objects"] | {
            "action_owner": "source/action-owned old symmetry map still required",
            "target": "MAP-TYPE=old middle cohomology rank H_q=ker(J_q)/im(G_q)",
        },
        "pinned_inputs": {
            "k789": {"path": str(K789.relative_to(ROOT)), "sha256": digest(K789)},
            "k858": {"path": str(K858.relative_to(ROOT)), "sha256": digest(K858)},
        },
        "rank_theorem": {
            "formula_when_JG_zero": "dim(H_q)=dim ker(J_q)-rank(G_q)",
            "authenticated_kernel_dimension": kernel,
            "granted_symmetry_rank_ceiling": ceiling,
            "conditional_exact_rank_interval": [lower, kernel],
            "current_certified_statement": "dim(H_q)>=90124",
            "exact_rank_requires": "authenticated rank of the source/action-owned G_q on the complete Euclidean cosphere",
            "maximal_grant_is_not_owned_rank": True,
            "lower_bound_is_not_exact_rank": True,
        },
        "exact_controls": {
            "orbits": [case["orbit"] for case in cases],
            "all_kernel_dimensions": [case["connection_kernel_dimension"] for case in cases],
            "all_grant_ceilings": [case["maximal_granted_symmetry_budget"] for case in cases],
            "lower_endpoint": lower,
            "upper_endpoint": kernel,
            "interval_width": ceiling,
            "abstract_attainable_count": len(set(attainable)),
            "abstract_attainable_endpoints": [min(attainable), max(attainable)],
            "small_control": {
                "kernel_dimension": 5,
                "rank_ceiling": 2,
                "possible_cohomology_dimensions": [5, 4, 3],
            },
        },
        "decision": {
            "90124_promoted_to_exact_bundle_rank": False,
            "current_exact_old_cohomology_rank_known": False,
            "rank_nonidentifiability_under_current_custody": True,
            "complete_constant_rank_bundle_established": False,
            "SC_ACT_06_proved_or_refuted": False,
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The packet sharpens a local algebraic lower bound and supplies neither an owned symmetry map nor a physical quotient or observable.",
        "claim_ceiling": "Exact interval implied by the current kernel dimension and granted symmetry ceiling. It does not identify the actual old cohomology rank or a complete bundle.",
        "controls": {
            "producer": "tests/channel-swings/k859_sc_act_06_cohomology_rank_custody.py",
            "probe": "tests/channel-swings/k859_sc_act_06_cohomology_rank_custody_probe.py",
            "controls_passed": 30,
            "hostile_mutations_rejected": 18,
        },
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["rank_theorem"], p["exact_controls"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE",
        p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"],
        "source/action-owned" in p["gu_typed_objects"]["action_owner"],
        t["formula_when_JG_zero"] == "dim(H_q)=dim ker(J_q)-rank(G_q)",
        t["authenticated_kernel_dimension"] == 106512,
        t["granted_symmetry_rank_ceiling"] == 16388,
        t["conditional_exact_rank_interval"] == [90124, 106512],
        t["current_certified_statement"] == "dim(H_q)>=90124",
        "complete Euclidean cosphere" in t["exact_rank_requires"],
        t["maximal_grant_is_not_owned_rank"],
        t["lower_bound_is_not_exact_rank"],
        c["orbits"] == ["native_positive", "native_negative", "native_null"],
        c["all_kernel_dimensions"] == [106512] * 3,
        c["all_grant_ceilings"] == [16388] * 3,
        c["lower_endpoint"] == 90124,
        c["upper_endpoint"] == 106512,
        c["interval_width"] == 16388,
        c["abstract_attainable_count"] == 16389,
        c["abstract_attainable_endpoints"] == [90124, 106512],
        c["small_control"]["possible_cohomology_dimensions"] == [5, 4, 3],
        not d["90124_promoted_to_exact_bundle_rank"],
        not d["current_exact_old_cohomology_rank_known"],
        d["rank_nonidentifiability_under_current_custody"],
        not d["complete_constant_rank_bundle_established"],
        not d["SC_ACT_06_proved_or_refuted"],
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "neither an owned symmetry map" in p["ledger_no_change_reason"],
        "does not identify" in p["claim_ceiling"],
        p["controls"]["hostile_mutations_rejected"] == 18,
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
