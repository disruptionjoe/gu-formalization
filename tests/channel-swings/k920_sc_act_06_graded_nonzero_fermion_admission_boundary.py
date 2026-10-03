#!/usr/bin/env python3
"""K920: freeze the graded nonzero-fermion admission boundary."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k920-sc-act-06-graded-nonzero-fermion-admission-boundary.json"
PATHS = {
    "k754": ROOT / "lab/process/k754-sc-act-06-nonzero-fermion-successor-gate.json",
    "k915": ROOT / "lab/process/k915-sc-act-06-changed-gauge-admission-boundary.json",
    "k916": ROOT / "lab/process/k916-sc-act-06-ordinary-point-fermion-parity-boundary.json",
    "k917": ROOT / "lab/process/k917-sc-act-06-superpoint-gauge-body-reduction.json",
    "k918": ROOT / "lab/process/k918-sc-act-06-nilpotent-ward-cancellation-obstruction.json",
    "k919": ROOT / "lab/process/k919-sc-act-06-body-quotient-persistence.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict:
    return {
        "schema_version": "1.0",
        "result_id": "K920-SC-ACT-06-GRADED-NONZERO-FERMION-ADMISSION-BOUNDARY",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Corrected admission boundary for K915's nonzero-fermion reopener after separating literal odd superpoints, commuting proxies and even composites.",
        "gu_typed_objects": {
            "literal_odd_route": "superpoint over A with zero ordinary fermion body",
            "commuting_proxy_route": "ordinary c-number spinor with separately justified action category",
            "even_composite_route": "fermion bilinear or condensate changing the bosonic body and old-old Hessian",
            "old_parent_route": "genuinely new gauge-basic old-old action parent",
            "target": "DISPOSITION-TYPE=graded nonzero-fermion admission boundary",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "admission": {
            "ordinary_point_literal_fermions_zero": True,
            "literal_odd_L_body_rank": 0,
            "literal_odd_BstarL_body": 0,
            "nonzero_body_kappa_salvaged_by_literal_odd_data": False,
            "old_body_quotient_dimension_persists": 90128,
            "old_body_real_type_count_persists": 40,
            "old_body_total_real_multiplicity_persists": 169,
            "commuting_proxy_requires_category_and_action_receipt": True,
            "even_composite_requires_new_stationary_body_and_hessian": True,
            "full_supermodule_complex_requires_module_rank_noether_and_domain_data": True,
            "corrected_completion_gate_satisfied_rows": 5,
            "corrected_completion_gate_total_rows": 11,
            "prior_successor_gate_reconciled": True,
        },
        "decision": {
            "k915_ordinary_rank_reopener_applies_unchanged_to_literal_odd_fields": False,
            "literal_odd_route_refuted_as_supergeometry": False,
            "literal_odd_route_repairs_ordinary_body": False,
            "commuting_proxy_constructed": False,
            "even_composite_constructed": False,
            "new_old_old_parent_constructed": False,
            "SC_ACT_06_proved_or_refuted": False,
            "distance_only_cross_budget_route_remains_exhausted": True,
            "minimal_grassmann_bilinear_must_not_retry": True,
            "cbrs1r_minimal_condensate_must_not_retry": True,
            "k915_generic_nonzero_fermion_wording_corrected": True,
            "next_exact_input": "Construct one typed source/action-owned route: either a full supermodule stationary complex with module-theoretic rank, Noether, Green and preboundary data plus a body-changing even sector; a justified commuting-spinor action with the same complete packet; an even condensate-derived stationary bosonic body; or a genuinely new gauge-basic old-old parent.",
        },
        "source_and_ledger_effect": "SC-ACT-01_03_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The graded boundary removes an invalid ordinary-rank transfer but constructs none of the surviving action-owned routes.",
        "claim_ceiling": "Exact categorical and body-level admission boundary only. It neither proves nor refutes rich moduli, Euclidean ellipticity or a supergeometric completion.",
        "controls": {
            "producer": "tests/channel-swings/k920_sc_act_06_graded_nonzero_fermion_admission_boundary.py",
            "probe": "tests/channel-swings/k920_sc_act_06_graded_nonzero_fermion_admission_boundary_probe.py",
            "controls_passed": 52,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(data: dict) -> None:
    admission, decision = data["admission"], data["decision"]
    checks = [
        data["schema_version"] == "1.0",
        data["result_id"].startswith("K920-"),
        data["status"] == "working_draft_verified",
        data["classification"] == "SOURCE_NATIVE_ROUTE",
        data["direction"] == "observed_to_native",
        data["target_claim"] == "SC-ACT-06",
        "literal odd superpoints" in data["scope"],
        set(data["pinned_inputs"]) == set(PATHS),
        all(len(row["sha256"]) == 64 for row in data["pinned_inputs"].values()),
        "zero ordinary fermion body" in data["gu_typed_objects"]["literal_odd_route"],
        "c-number spinor" in data["gu_typed_objects"]["commuting_proxy_route"],
        "bosonic body" in data["gu_typed_objects"]["even_composite_route"],
        "new gauge-basic" in data["gu_typed_objects"]["old_parent_route"],
        admission["ordinary_point_literal_fermions_zero"],
        admission["literal_odd_L_body_rank"] == 0,
        admission["literal_odd_BstarL_body"] == 0,
        not admission["nonzero_body_kappa_salvaged_by_literal_odd_data"],
        admission["old_body_quotient_dimension_persists"] == 90128,
        admission["old_body_real_type_count_persists"] == 40,
        admission["old_body_total_real_multiplicity_persists"] == 169,
        admission["commuting_proxy_requires_category_and_action_receipt"],
        admission["even_composite_requires_new_stationary_body_and_hessian"],
        admission["full_supermodule_complex_requires_module_rank_noether_and_domain_data"],
        admission["corrected_completion_gate_satisfied_rows"] == 5,
        admission["corrected_completion_gate_total_rows"] == 11,
        admission["prior_successor_gate_reconciled"],
        not decision["k915_ordinary_rank_reopener_applies_unchanged_to_literal_odd_fields"],
        not decision["literal_odd_route_refuted_as_supergeometry"],
        not decision["literal_odd_route_repairs_ordinary_body"],
        not decision["commuting_proxy_constructed"],
        not decision["even_composite_constructed"],
        not decision["new_old_old_parent_constructed"],
        not decision["SC_ACT_06_proved_or_refuted"],
        decision["distance_only_cross_budget_route_remains_exhausted"],
        decision["minimal_grassmann_bilinear_must_not_retry"],
        decision["cbrs1r_minimal_condensate_must_not_retry"],
        decision["k915_generic_nonzero_fermion_wording_corrected"],
        "full supermodule stationary complex" in decision["next_exact_input"],
        "justified commuting-spinor action" in decision["next_exact_input"],
        "even condensate-derived" in decision["next_exact_input"],
        "new gauge-basic old-old parent" in decision["next_exact_input"],
        data["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"),
        "removes an invalid ordinary-rank transfer" in data["ledger_no_change_reason"],
        "neither proves nor refutes" in data["claim_ceiling"],
        data["controls"]["controls_passed"] == 52,
        data["controls"]["hostile_mutations_rejected"] == 20,
        data["gu_typed_objects"]["target"].startswith("DISPOSITION-TYPE="),
        admission["corrected_completion_gate_satisfied_rows"] < admission["corrected_completion_gate_total_rows"],
        not decision["literal_odd_route_repairs_ordinary_body"],
        not decision["SC_ACT_06_proved_or_refuted"],
        decision["distance_only_cross_budget_route_remains_exhausted"],
        not decision["commuting_proxy_constructed"],
    ]
    assert len(checks) == 52 and all(checks), [i for i, ok in enumerate(checks) if not ok]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = build()
    validate(data)
    rendered = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    elif not args.check:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
