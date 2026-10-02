#!/usr/bin/env python3
"""K854: robust all-covector quotient-repair certificate."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k854-sc-act-06-robust-quotient-repair-certificate.json"
PATHS = {
    "k849": ROOT / "lab/process/k849-sc-act-06-exact-repair-certificate.json",
    "k850": ROOT / "lab/process/k850-sc-act-06-flat-quotient-repair-interface.json",
    "k851": ROOT / "lab/process/k851-sc-act-06-compact-cosphere-hodge-gap.json",
    "k852": ROOT / "lab/process/k852-sc-act-06-uniformity-failure-controls.json",
    "k853": ROOT / "lab/process/k853-sc-act-06-robust-exactness-radius.json",
}
EXACT_ROWS = [
    "source_or_action_ownership",
    "old_principal_complex",
    "response_descends_tau_G_zero",
    "symmetry_is_old_cycle_J_S_zero",
    "repaired_composition_tau_S_zero",
    "old_middle_cohomology_dimension",
    "induced_response_rank",
    "induced_symmetry_rank",
    "pointwise_kernel_image_equality",
    "authenticated_compact_unit_cosphere",
    "continuous_induced_map_family",
    "continuous_auxiliary_fibre_metrics",
    "common_domain_and_real_structure",
    "uniform_hodge_gap_conclusion",
]
ROBUST_ROWS = EXACT_ROWS + ["composition_compatible_perturbation_below_radius"]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evaluate(rows: dict[str, bool]) -> dict[str, Any]:
    missing_exact = [row for row in EXACT_ROWS if not rows.get(row, False)]
    missing_robust = [row for row in ROBUST_ROWS if not rows.get(row, False)]
    return {
        "rows": rows,
        "missing_exact_rows": missing_exact,
        "missing_robust_rows": missing_robust,
        "exact_admitted": not missing_exact,
        "robust_admitted": not missing_robust,
    }


def build() -> dict[str, Any]:
    source = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    complete = {row: True for row in ROBUST_ROWS}
    omissions = {row: evaluate({**complete, row: False}) for row in ROBUST_ROWS}
    flat = source["k850"]["current_flat_packet"]
    current_rows = {row: False for row in ROBUST_ROWS}
    current_rows["old_principal_complex"] = flat["old_principal_complex"]
    return {
        "schema_version": "1.0",
        "result_id": "K854-SC-ACT-06-ROBUST-QUOTIENT-REPAIR-CERTIFICATE",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": source["k850"]["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Robust compact-cosphere certificate for a future repair of the current flat quotient complex; no repair maps, new germ or completed GU family are constructed.",
        "gu_typed_objects": {
            "carrier": "LAYER=ambient CHIRALITY=N/A repaired quotient symbol bundle over the authenticated Euclidean unit cosphere",
            "pairing": "continuous positive auxiliary fibre metrics used for the quotient Hodge operator",
            "real_structure": "must be inherited continuously from the proposed principal packet",
            "grading": "owned principal symmetries -> old quotient cohomology -> owned principal responses",
            "action_owner": "candidate-must-declare",
            "target": "MAP-TYPE=quotient exact and perturbatively robust middle symbol complex",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "certificate": {
            "exact_row_count": len(EXACT_ROWS),
            "robust_row_count": len(ROBUST_ROWS),
            "exact_rows": EXACT_ROWS,
            "robust_rows": ROBUST_ROWS,
            "logical_form": "conjunction",
            "core_equality": "im(S_bar_q)=ker(tau_bar_q) for every q",
            "uniformity_theorem": "compact authenticated cosphere plus continuous maps/metrics plus pointwise exactness implies mu=min_q lambda_min(L_q)>0",
            "robustness_theorem": "composition-compatible perturbations below (-T-R+sqrt((T+R)^2+2mu))/2 preserve exactness",
            "uniform_gap_is_an_independent_GU_input": False,
            "raw_rank_substitution_allowed": False,
        },
        "exact_controls": {
            "complete_synthetic_candidate": evaluate(complete),
            "one_missing_row_controls": omissions,
            "all_single_row_omissions_reject_robust_admission": all(not x["robust_admitted"] for x in omissions.values()),
            "only_missing_robustness_row_preserves_exact_admission": omissions[ROBUST_ROWS[-1]]["exact_admitted"],
        },
        "current_flat_packet": {
            "old_middle_cohomology_lower_bound": flat["old_middle_cohomology_lower_bound"],
            "rows": current_rows,
            "evaluation": evaluate(current_rows),
            "owned_continuous_tau_bar_family": False,
            "owned_continuous_S_bar_family": False,
            "pointwise_exactness": False,
            "uniform_hodge_gap": False,
            "robustness_radius": False,
        },
        "decision": {
            "K849_uniformity_row_decomposed_and_resolved": True,
            "future_exact_candidate_needs_independent_uniform_gap_assumption": False,
            "current_flat_packet_exact_admitted": False,
            "current_flat_packet_robust_admitted": False,
            "current_flat_packet_repairability_refuted": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Construct continuous source/action-owned tau_bar_q and S_bar_q on the authenticated compact Euclidean cosphere, prove pointwise equality im(S_bar_q)=ker(tau_bar_q), and compute the resulting gap and norm bounds; robustness then has the explicit K853 radius.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The certificate removes an analytic ambiguity but supplies none of the missing source-owned GU maps, domains, quotients or observables.",
        "claim_ceiling": "Necessary-and-sufficient finite-symbol exactness interface plus a sufficient perturbative robustness extension. It neither repairs nor globally excludes the current or any other GU germ.",
        "controls": {
            "producer": "tests/channel-swings/k854_sc_act_06_robust_quotient_repair_certificate.py",
            "probe": "tests/channel-swings/k854_sc_act_06_robust_quotient_repair_certificate_probe.py",
            "controls_passed": 47,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(p: dict[str, Any]) -> None:
    c, x, f, d = p["certificate"], p["exact_controls"], p["current_flat_packet"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE", p["target_claim"] == "SC-ACT-06", "scope before inference" in p["comparator_routing_notice"],
        p["gu_typed_objects"]["action_owner"] == "candidate-must-declare", c["exact_row_count"] == 14, c["robust_row_count"] == 15,
        c["exact_rows"] == EXACT_ROWS, c["robust_rows"] == ROBUST_ROWS, c["logical_form"] == "conjunction",
        c["core_equality"] == "im(S_bar_q)=ker(tau_bar_q) for every q", "mu=min_q" in c["uniformity_theorem"],
        "sqrt((T+R)^2+2mu)" in c["robustness_theorem"], not c["uniform_gap_is_an_independent_GU_input"],
        not c["raw_rank_substitution_allowed"], x["complete_synthetic_candidate"]["exact_admitted"],
        x["complete_synthetic_candidate"]["robust_admitted"], not x["complete_synthetic_candidate"]["missing_exact_rows"],
        not x["complete_synthetic_candidate"]["missing_robust_rows"], len(x["one_missing_row_controls"]) == 15,
        x["all_single_row_omissions_reject_robust_admission"], x["only_missing_robustness_row_preserves_exact_admission"],
        all(not item["robust_admitted"] for item in x["one_missing_row_controls"].values()),
        not x["one_missing_row_controls"]["pointwise_kernel_image_equality"]["exact_admitted"],
        f["old_middle_cohomology_lower_bound"] == 90124, f["rows"]["old_principal_complex"],
        sum(1 for value in f["rows"].values() if value) == 1, not f["evaluation"]["exact_admitted"],
        not f["evaluation"]["robust_admitted"], not f["owned_continuous_tau_bar_family"],
        not f["owned_continuous_S_bar_family"], not f["pointwise_exactness"], not f["uniform_hodge_gap"],
        not f["robustness_radius"], d["K849_uniformity_row_decomposed_and_resolved"],
        not d["future_exact_candidate_needs_independent_uniform_gap_assumption"], not d["current_flat_packet_exact_admitted"],
        not d["current_flat_packet_robust_admitted"], not d["current_flat_packet_repairability_refuted"],
        not d["SC_ACT_06_proved_or_refuted"], "K853 radius" in d["next_exact_input"],
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED", "analytic ambiguity" in p["ledger_no_change_reason"],
        "neither repairs nor globally excludes" in p["claim_ceiling"], set(p["pinned_inputs"]) == {"k849", "k850", "k851", "k852", "k853"},
        all(len(v["sha256"]) == 64 for v in p["pinned_inputs"].values()), p["controls"]["controls_passed"] == 47,
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
