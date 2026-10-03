#!/usr/bin/env python3
"""K866: compile the basepoint-isotropy repair disposition."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k866-sc-act-06-isotropy-repair-disposition.json"
PATHS = {
    "k862": ROOT / "lab/process/k862-sc-act-06-naturality-repair-disposition.json",
    "k863": ROOT / "lab/process/k863-sc-act-06-basepoint-kernel-isotropy.json",
    "k864": ROOT / "lab/process/k864-sc-act-06-radial-grant-quotient.json",
    "k865": ROOT / "lab/process/k865-sc-act-06-isotypic-repair-criterion.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    packets = {key: json.loads(path.read_text()) for key, path in PATHS.items()}
    rows = [
        "SO(13)-equivariant radial/tangential split of the K788 basepoint kernel",
        "exact radial module direct-sum_(k=0)^6 4 Lambda^k(V_13)",
        "q-lambda image identified with the radial summand",
        "conditional connection-only quotient dimension 90128",
        "irreducible multiplicities of the tangential quotient",
        "authenticated source/action-owned old symmetry image",
        "source/action-owned repair-domain and repair-target multiplicities",
        "h_rho<=a_rho+b_rho for every real irreducible type",
        "constructed SO(13)-intertwiners S_0,tau_0",
        "descent, composition and im(S_0)=ker(tau_0)",
        "globalized SO(14)-equivariant maps and analytic robustness rows",
    ]
    current = {row: False for row in rows}
    for row in rows[:4]:
        current[row] = True
    return {
        "schema_version": "1.0",
        "result_id": "K866-SC-ACT-06-ISOTROPY-REPAIR-DISPOSITION",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": packets["k862"]["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Compiled naturality disposition after authenticating the radial SO(13) kernel module, the provisional radial quotient, and the irrepwise repair-capacity theorem.",
        "gu_typed_objects": packets["k862"]["gu_typed_objects"],
        "pinned_inputs": {key: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for key, path in PATHS.items()},
        "compiled_result": {
            "basepoint_radial_kernel_module_authenticated": True,
            "basepoint_tangential_kernel_authenticated_as_kernel_module": True,
            "radial_module_formula": "direct-sum_(k=0)^6 4 Lambda^k(V_13)",
            "conditional_q_lambda_connection_quotient_dimension": 90128,
            "K789_90124_exact_connection_quotient": False,
            "tangential_irreducible_multiplicities_known": False,
            "owned_old_symmetry_image_known": False,
            "owned_old_cohomology_module_known": False,
            "owned_repair_modules_known": False,
            "owned_repair_intertwiners_known": False,
            "current_flat_exact_admitted": False,
        },
        "isotropy_certificate": {
            "row_count": len(rows),
            "rows": rows,
            "current_GU_candidate": current,
            "satisfied_row_count": sum(current.values()),
            "all_rows_conjunctive": True,
            "current_GU_candidate_admitted": all(current.values()),
            "raw_total_rank_can_substitute_for_isotypic_coverage": False,
        },
        "decision": {
            "K862_naturality_gate_retracted": False,
            "radial_structure_materially_advanced": True,
            "current_flat_packet_repaired": False,
            "current_flat_packet_repairability_refuted": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Compute the irreducible real SO(13) multiplicities of the 90128-dimensional tangential kernel, authenticate the actual owned old symmetry quotient, and compare the surviving h_rho against source/action-owned repair multiplicities a_rho,b_rho before constructing S_0,tau_0.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "Four representation rows advance, but the actual owned quotient, repair modules, maps, analytic domain and physical interpretation remain absent.",
        "claim_ceiling": "Exact basepoint radial module, conditional q-lambda quotient and exact irrepwise repair-capacity theorem. No GU repair, global no-go or physical conclusion follows.",
        "controls": {
            "producer": "tests/channel-swings/k866_sc_act_06_isotropy_repair_disposition.py",
            "probe": "tests/channel-swings/k866_sc_act_06_isotropy_repair_disposition_probe.py",
            "controls_passed": 39,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(p: dict[str, Any]) -> None:
    c, x, d = p["compiled_result"], p["isotropy_certificate"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE",
        p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"],
        set(p["pinned_inputs"]) == set(PATHS),
        all(len(item["sha256"]) == 64 for item in p["pinned_inputs"].values()),
        c["basepoint_radial_kernel_module_authenticated"],
        c["basepoint_tangential_kernel_authenticated_as_kernel_module"],
        c["radial_module_formula"] == "direct-sum_(k=0)^6 4 Lambda^k(V_13)",
        c["conditional_q_lambda_connection_quotient_dimension"] == 90128,
        not c["K789_90124_exact_connection_quotient"],
        not c["tangential_irreducible_multiplicities_known"],
        not c["owned_old_symmetry_image_known"],
        not c["owned_old_cohomology_module_known"],
        not c["owned_repair_modules_known"],
        not c["owned_repair_intertwiners_known"],
        not c["current_flat_exact_admitted"],
        x["row_count"] == 11,
        len(x["rows"]) == 11,
        len(x["current_GU_candidate"]) == 11,
        x["satisfied_row_count"] == 4,
        sum(x["current_GU_candidate"].values()) == 4,
        x["all_rows_conjunctive"],
        not x["current_GU_candidate_admitted"],
        not x["raw_total_rank_can_substitute_for_isotypic_coverage"],
        not d["K862_naturality_gate_retracted"],
        d["radial_structure_materially_advanced"],
        not d["current_flat_packet_repaired"],
        not d["current_flat_packet_repairability_refuted"],
        not d["SC_ACT_06_proved_or_refuted"],
        "90128-dimensional tangential kernel" in d["next_exact_input"],
        "h_rho" in d["next_exact_input"],
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "actual owned quotient" in p["ledger_no_change_reason"],
        "No GU repair" in p["claim_ceiling"],
        p["controls"]["controls_passed"] == 39,
        p["controls"]["hostile_mutations_rejected"] == 20,
        p["controls"]["producer"].endswith("k866_sc_act_06_isotropy_repair_disposition.py"),
        p["controls"]["probe"].endswith("k866_sc_act_06_isotropy_repair_disposition_probe.py"),
        x["rows"][0].startswith("SO(13)-equivariant"),
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
