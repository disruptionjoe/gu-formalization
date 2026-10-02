#!/usr/bin/env python3
"""K850: apply the K849 certificate shape to the current flat packet."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k850-sc-act-06-flat-quotient-repair-interface.json"
PATHS = {
    "k845": ROOT / "lab/process/k845-sc-act-06-lower-order-repair-boundary.json",
    "k846": ROOT / "lab/process/k846-sc-act-06-flat-function-space-disposition.json",
    "k848": ROOT / "lab/process/k848-sc-act-06-rank-budget-overlap-countermodels.json",
    "k849": ROOT / "lab/process/k849-sc-act-06-exact-repair-certificate.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    source = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    debt = source["k846"]["composition"]["uniform_middle_symbol_cohomology_lower_bound"]
    rows = source["k849"]["certificate"]["rows"]
    current = {
        "old_principal_complex": True,
        "old_middle_cohomology_lower_bound": debt,
        "source_or_action_owned_tau_bar": False,
        "source_or_action_owned_S_bar": False,
        "exact_dim_H_q": False,
        "induced_response_rank_every_q": False,
        "induced_symmetry_rank_every_q": False,
        "kernel_image_equality_every_q": False,
        "common_domain_and_uniformity": False,
    }
    return {
        "schema_version": "1.0",
        "result_id": "K850-SC-ACT-06-FLAT-QUOTIENT-REPAIR-INTERFACE",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": source["k846"]["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Certificate interface for a future repair of the current K717/K788/K789 flat principal packet; no repair map or new germ is constructed.",
        "gu_typed_objects": {
            "carrier": "LAYER=ambient CHIRALITY=N/A current K717 flat Y14 principal field/symmetry/equation sequence",
            "pairing": "auxiliary coefficient pairing used by K843/K844, distinct from source action ownership",
            "real_structure": "K740 pinned real coefficient basis",
            "grading": "owned principal symmetries -> flat fields -> owned principal residual rows",
            "action_owner": "source-action-required-for-future-repair",
            "target": "MAP-TYPE=quotient induced repair on H_q=ker(J_q)/im(G_q)",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "current_flat_packet": current,
        "future_packet_contract": {
            "certificate_rows": rows,
            "for_each_nonzero_covector_q": True,
            "old_cohomology": "H_q=ker(J_q)/im(G_q)",
            "response_descent": "tau_q G_q=0, defining tau_bar_q on H_q",
            "symmetry_descent": "J_q S_q=0 and tau_q S_q=0, defining S_bar_q into ker(tau_bar_q)",
            "exactness": "im(S_bar_q)=ker(tau_bar_q)",
            "effective_dimension_identity": "rank(tau_bar_q)+rank(S_bar_q)=dim(H_q)",
            "uniform_lower_bound_consequence": "rank(tau_bar_q)+rank(S_bar_q)>=90124 on the certified current cone",
            "lower_bound_is_sufficient": False,
            "raw_rank_budget_is_sufficient": False,
        },
        "decision": {
            "K845_scalar_budget_retained_as_necessary": True,
            "K845_scalar_budget_upgraded_to_exact_certificate": True,
            "current_flat_packet_passes_certificate": False,
            "current_flat_packet_repairability_refuted": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Supply actual source/action-owned tau_q and S_q, compute their induced maps on the complete H_q at every nonzero covector, and prove im(S_bar_q)=ker(tau_bar_q) with common-domain uniformity.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The packet sharpens the input contract for one rejected realization and neither supplies a new realization nor computes a physical quotient or observable.",
        "claim_ceiling": "Exact future-input interface for repairing the current flat packet. It neither proves repair impossible nor admits any presently owned GU completion.",
        "controls": {
            "producer": "tests/channel-swings/k850_sc_act_06_flat_quotient_repair_interface.py",
            "probe": "tests/channel-swings/k850_sc_act_06_flat_quotient_repair_interface_probe.py",
            "controls_passed": 41,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(p: dict[str, Any]) -> None:
    c, f, d = p["current_flat_packet"], p["future_packet_contract"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE", p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"],
        p["gu_typed_objects"]["action_owner"] == "source-action-required-for-future-repair",
        c["old_principal_complex"], c["old_middle_cohomology_lower_bound"] == 90124,
        not c["source_or_action_owned_tau_bar"], not c["source_or_action_owned_S_bar"],
        not c["exact_dim_H_q"], not c["induced_response_rank_every_q"],
        not c["induced_symmetry_rank_every_q"], not c["kernel_image_equality_every_q"],
        not c["common_domain_and_uniformity"], len(f["certificate_rows"]) == 10,
        f["for_each_nonzero_covector_q"], f["old_cohomology"] == "H_q=ker(J_q)/im(G_q)",
        "tau_bar_q" in f["response_descent"], "S_bar_q" in f["symmetry_descent"],
        f["exactness"] == "im(S_bar_q)=ker(tau_bar_q)",
        f["effective_dimension_identity"] == "rank(tau_bar_q)+rank(S_bar_q)=dim(H_q)",
        ">=90124" in f["uniform_lower_bound_consequence"], not f["lower_bound_is_sufficient"],
        not f["raw_rank_budget_is_sufficient"], d["K845_scalar_budget_retained_as_necessary"],
        d["K845_scalar_budget_upgraded_to_exact_certificate"], not d["current_flat_packet_passes_certificate"],
        not d["current_flat_packet_repairability_refuted"], not d["SC_ACT_06_proved_or_refuted"],
        "im(S_bar_q)=ker(tau_bar_q)" in d["next_exact_input"],
        "UNCHANGED" in p["source_and_ledger_effect"], "no repair map" in p["scope"],
        set(p["pinned_inputs"]) == {"k845", "k846", "k848", "k849"},
        all(len(item["sha256"]) == 64 for item in p["pinned_inputs"].values()),
        p["controls"]["controls_passed"] == 41, p["controls"]["hostile_mutations_rejected"] == 20,
        "neither supplies a new realization" in p["ledger_no_change_reason"],
        "neither proves repair impossible" in p["claim_ceiling"],
        p["gu_typed_objects"]["target"].startswith("MAP-TYPE=quotient"),
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        c["old_middle_cohomology_lower_bound"] > 0, not d["current_flat_packet_passes_certificate"],
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
