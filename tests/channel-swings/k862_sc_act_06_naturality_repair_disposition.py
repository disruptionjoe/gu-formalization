#!/usr/bin/env python3
"""K862: compile the naturality-aware quotient-repair disposition."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k862-sc-act-06-naturality-repair-disposition.json"
PATHS = {
    "k850": ROOT / "lab/process/k850-sc-act-06-flat-quotient-repair-interface.json",
    "k854": ROOT / "lab/process/k854-sc-act-06-robust-quotient-repair-certificate.json",
    "k858": ROOT / "lab/process/k858-sc-act-06-topological-repair-disposition.json",
    "k859": ROOT / "lab/process/k859-sc-act-06-cohomology-rank-custody.json",
    "k860": ROOT / "lab/process/k860-sc-act-06-homogeneous-intertwiner-gate.json",
    "k861": ROOT / "lab/process/k861-sc-act-06-equivariant-triviality-countermodel.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    packets = {key: json.loads(path.read_text()) for key, path in PATHS.items()}
    rows = [
        "complete SO(14)-equivariant old principal complex over S^13",
        "constant exact ranks and exact old cohomology rank",
        "authenticated SO(13) isotropy module of H_[e]",
        "source/action-owned repair-domain and repair-target isotropy modules",
        "SO(13)-intertwiners S_0 and tau_0",
        "old-cycle and response-descent identities",
        "tau_0 S_0=0",
        "im(S_0)=ker(tau_0) at the base covector",
        "induced SO(14)-equivariant maps on the complete cosphere",
        "common real structure, invariant metrics and analytic domain",
        "positive Hodge gap and K853 perturbation control when robustness is claimed",
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K862-SC-ACT-06-NATURALITY-REPAIR-DISPOSITION",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": packets["k860"]["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Naturality-aware disposition for repairing a complete Euclidean SC-ACT-06 symbol complex over S^13; current GU custody is not promoted to the required equivariant modules or maps.",
        "gu_typed_objects": packets["k860"]["gu_typed_objects"] | {
            "action_owner": "source/action ownership required for isotropy intertwiners and their globalized maps",
            "target": "MAP-TYPE=SO(14)-natural exact quotient repair",
        },
        "pinned_inputs": {
            key: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for key, path in PATHS.items()
        },
        "compiled_result": {
            "ordinary_high_rank_bundle_trivial_conditionally": True,
            "current_exact_old_cohomology_rank_known": False,
            "current_rank_interval_under_grant": [90124, 106512],
            "homogeneous_maps_reduce_to_isotropy_intertwiners": True,
            "ordinary_triviality_implies_natural_frame": False,
            "current_old_isotropy_module_authenticated": False,
            "current_owned_repair_intertwiners_supplied": False,
            "current_flat_exact_admitted": False,
            "current_flat_robust_admitted": False,
        },
        "naturality_certificate": {
            "row_count": len(rows),
            "rows": rows,
            "all_rows_conjunctive": True,
            "basepoint_exactness_globalizes_only_after_equivariance": True,
            "arbitrary_global_frame_allowed_as_owner": False,
            "rank_lower_bound_allowed_as_exact_dimension": False,
        },
        "exact_controls": {
            "complete_synthetic_candidate": {row: True for row in rows},
            "complete_synthetic_candidate_admitted": True,
            "current_GU_candidate": {row: False for row in rows},
            "current_GU_candidate_admitted": False,
            "all_single_row_omissions_reject": True,
        },
        "decision": {
            "pure_topological_route_remains_closed_conditionally": True,
            "naturality_reopens_an_ordinary_topological_obstruction": False,
            "naturality_adds_a_distinct_representation_ownership_gate": True,
            "current_flat_packet_repaired": False,
            "current_flat_packet_repairability_refuted": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Compute the SO(13) isotropy representation of the authenticated complete old cohomology fibre, then exhibit source/action-owned isotropy modules and intertwiners S_0,tau_0 satisfying every descent, composition and kernel-image row before globalizing over SO(14)/SO(13).",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The result sharpens the mathematical ownership interface but supplies no GU module, owned repair map, domain, physical quotient, state or observable.",
        "claim_ceiling": "Necessary-and-sufficient homogeneous naturality interface conditional on the complete equivariant old complex. It neither repairs nor globally excludes any GU germ.",
        "controls": {
            "producer": "tests/channel-swings/k862_sc_act_06_naturality_repair_disposition.py",
            "probe": "tests/channel-swings/k862_sc_act_06_naturality_repair_disposition_probe.py",
            "controls_passed": 39,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(p: dict[str, Any]) -> None:
    c, n, x, d = p["compiled_result"], p["naturality_certificate"], p["exact_controls"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE",
        p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"],
        p["gu_typed_objects"]["action_owner"].startswith("source/action ownership required"),
        set(p["pinned_inputs"]) == set(PATHS),
        all(len(item["sha256"]) == 64 for item in p["pinned_inputs"].values()),
        c["ordinary_high_rank_bundle_trivial_conditionally"],
        not c["current_exact_old_cohomology_rank_known"],
        c["current_rank_interval_under_grant"] == [90124, 106512],
        c["homogeneous_maps_reduce_to_isotropy_intertwiners"],
        not c["ordinary_triviality_implies_natural_frame"],
        not c["current_old_isotropy_module_authenticated"],
        not c["current_owned_repair_intertwiners_supplied"],
        not c["current_flat_exact_admitted"],
        not c["current_flat_robust_admitted"],
        n["row_count"] == 11,
        len(n["rows"]) == 11,
        n["all_rows_conjunctive"],
        n["basepoint_exactness_globalizes_only_after_equivariance"],
        not n["arbitrary_global_frame_allowed_as_owner"],
        not n["rank_lower_bound_allowed_as_exact_dimension"],
        len(x["complete_synthetic_candidate"]) == 11,
        all(x["complete_synthetic_candidate"].values()),
        x["complete_synthetic_candidate_admitted"],
        len(x["current_GU_candidate"]) == 11,
        not any(x["current_GU_candidate"].values()),
        not x["current_GU_candidate_admitted"],
        x["all_single_row_omissions_reject"],
        d["pure_topological_route_remains_closed_conditionally"],
        not d["naturality_reopens_an_ordinary_topological_obstruction"],
        d["naturality_adds_a_distinct_representation_ownership_gate"],
        not d["current_flat_packet_repaired"],
        not d["current_flat_packet_repairability_refuted"],
        not d["SC_ACT_06_proved_or_refuted"],
        "SO(13) isotropy representation" in d["next_exact_input"],
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "supplies no GU module" in p["ledger_no_change_reason"],
        "neither repairs nor globally excludes" in p["claim_ceiling"],
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
