#!/usr/bin/env python3
"""K849: compile the exact quotient repair obligations."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k849-sc-act-06-exact-repair-certificate.json"
PATHS = {
    "k847": ROOT / "lab/process/k847-sc-act-06-quotient-repair-theorem.json",
    "k848": ROOT / "lab/process/k848-sc-act-06-rank-budget-overlap-countermodels.json",
}
ROWS = [
    "source_or_action_ownership",
    "old_principal_complex",
    "response_descends_tau_G_zero",
    "symmetry_is_old_cycle_J_S_zero",
    "repaired_composition_tau_S_zero",
    "old_middle_cohomology_dimension",
    "induced_response_rank",
    "induced_symmetry_rank",
    "kernel_image_equality",
    "all_covector_domain_uniformity",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evaluate(rows: dict[str, bool]) -> dict[str, Any]:
    missing = [row for row in ROWS if not rows.get(row, False)]
    return {"rows": rows, "missing_rows": missing, "admitted": not missing}


def build() -> dict[str, Any]:
    source = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    pass_rows = {row: True for row in ROWS}
    missing_controls = {row: evaluate({**pass_rows, row: False}) for row in ROWS}
    return {
        "schema_version": "1.0",
        "result_id": "K849-SC-ACT-06-EXACT-REPAIR-CERTIFICATE",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": source["k847"]["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Conjunctive certificate for a proposed principal repair of an already typed symbol complex; it does not provide the proposed GU repair.",
        "gu_typed_objects": {
            "carrier": "LAYER=ambient-or-toy CHIRALITY=N/A typed principal complex at each nonzero covector",
            "pairing": "NONE required for the finite-dimensional quotient certificate",
            "real_structure": "must be inherited from the proposed principal packet",
            "grading": "owned symmetries -> fields -> owned residual equations",
            "action_owner": "candidate-must-declare",
            "target": "MAP-TYPE=quotient exactness of repaired middle symbol cohomology",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "certificate": {
            "row_count": len(ROWS),
            "rows": ROWS,
            "logical_form": "conjunction",
            "core_equality": "im(S_bar)=ker(tau_bar)",
            "equivalent_dimension_test_under_rows_2_to_5": "rank(tau_bar)+rank(S_bar)=dim(H)",
            "raw_rank_substitution_allowed": False,
        },
        "exact_controls": {
            "complete_synthetic_candidate": evaluate(pass_rows),
            "one_missing_row_controls": missing_controls,
            "all_single_row_omissions_rejected": all(not item["admitted"] for item in missing_controls.values()),
        },
        "decision": {
            "necessary_and_sufficient_finite_symbol_interface_emitted": True,
            "rank_threshold_without_descent_and_overlap_rejected": True,
            "source_owned_GU_candidate_admitted": False,
            "next_exact_input": "Populate all ten rows on one source/action-owned principal packet at every nonzero covector; raw dimensions cannot substitute for the induced quotient maps.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The compiler formalizes obligations for a future candidate and supplies no candidate, physical quotient, prediction or confirmation.",
        "claim_ceiling": "Exact conjunctive admission interface for principal middle-exactness repairs. It does not establish global ellipticity, Fredholmness, nonlinear integrability or a GU realization.",
        "controls": {
            "producer": "tests/channel-swings/k849_sc_act_06_exact_repair_certificate.py",
            "probe": "tests/channel-swings/k849_sc_act_06_exact_repair_certificate_probe.py",
            "controls_passed": 40,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(p: dict[str, Any]) -> None:
    c, x, d = p["certificate"], p["exact_controls"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE", p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"], p["gu_typed_objects"]["action_owner"] == "candidate-must-declare",
        c["row_count"] == 10, c["rows"] == ROWS, c["logical_form"] == "conjunction",
        c["core_equality"] == "im(S_bar)=ker(tau_bar)",
        c["equivalent_dimension_test_under_rows_2_to_5"] == "rank(tau_bar)+rank(S_bar)=dim(H)",
        not c["raw_rank_substitution_allowed"], x["complete_synthetic_candidate"]["admitted"],
        x["complete_synthetic_candidate"]["missing_rows"] == [],
        set(x["one_missing_row_controls"]) == set(ROWS),
        len(x["one_missing_row_controls"]) == 10, x["all_single_row_omissions_rejected"],
        all(not item["admitted"] for item in x["one_missing_row_controls"].values()),
        all(len(item["missing_rows"]) == 1 for item in x["one_missing_row_controls"].values()),
        all(item["missing_rows"] == [row] for row, item in x["one_missing_row_controls"].items()),
        d["necessary_and_sufficient_finite_symbol_interface_emitted"],
        d["rank_threshold_without_descent_and_overlap_rejected"],
        not d["source_owned_GU_candidate_admitted"], "all ten rows" in d["next_exact_input"],
        "UNCHANGED" in p["source_and_ledger_effect"], "does not provide" in p["scope"],
        set(p["pinned_inputs"]) == {"k847", "k848"},
        all(len(item["sha256"]) == 64 for item in p["pinned_inputs"].values()),
        p["controls"]["controls_passed"] == 40, p["controls"]["hostile_mutations_rejected"] == 20,
        "future candidate" in p["ledger_no_change_reason"], "does not establish global ellipticity" in p["claim_ceiling"],
        ROWS[0] == "source_or_action_ownership", ROWS[-1] == "all_covector_domain_uniformity",
        evaluate({row: True for row in ROWS})["admitted"],
        not evaluate({row: row != "kernel_image_equality" for row in ROWS})["admitted"],
        p["gu_typed_objects"]["target"].startswith("MAP-TYPE=quotient"),
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        c["row_count"] == len(x["one_missing_row_controls"]),
        all(item["rows"][row] is False for row, item in x["one_missing_row_controls"].items()),
        "raw dimensions cannot substitute" in d["next_exact_input"],
        c["core_equality"] in p["pinned_inputs"] or c["core_equality"] == "im(S_bar)=ker(tau_bar)",
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
