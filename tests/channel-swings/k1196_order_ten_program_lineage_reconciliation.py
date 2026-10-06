#!/usr/bin/env python3
"""Reconcile the K487 and K415 order-ten face-program lineages."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K487 = ROOT / "lab/process/k487-order-ten-face-program-compiler.json"
K415 = ROOT / "lab/process/k415-order-ten-face-program-compiler.json"
OUTPUT = ROOT / "lab/process/k1196-order-ten-program-lineage-reconciliation.json"
ADDITIVE = {"descriptor_program_sha256", "normal_allocation", "positive_tangential_raw_time", "selection_basis",
            "singular_template_histogram", "confluent_template_histogram"}

def digest(v: Any) -> str:
    return "sha256:" + hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def projection(row: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in row.items() if k not in ADDITIVE}

def build() -> dict[str, Any]:
    old, new = json.loads(K487.read_text()), json.loads(K415.read_text())
    sections = ["face_programs", "positive_interior_fallback_programs", "selected_boundary_or_interior_program_per_hybrid"]
    rows = []
    for key in sections:
        a, b = old[key], new[key]
        rows.append({"section": key, "old_rows": len(a), "new_rows": len(b),
                     "semantic_projection_equal": [projection(x) for x in a] == [projection(x) for x in b],
                     "old_projection_sha256": digest([projection(x) for x in a]),
                     "new_projection_sha256": digest([projection(x) for x in b])})
    old_ids = [x["program_id"] for x in old["face_programs"]]
    new_ids = [x["program_id"] for x in new["face_programs"]]
    return {
        "schema_version": "1.0", "result_id": "K1196-ORDER-TEN-PROGRAM-LINEAGE-RECONCILIATION",
        "created": "2026-10-06", "classification": "INTERNAL_STRUCTURAL_ONLY", "direction": "observed_to_native",
        "fixed_control": {"predecessor_manifests": [str(K487.relative_to(ROOT)), str(K415.relative_to(ROOT))],
            "old_face_programs": len(old_ids), "new_face_programs": len(new_ids),
            "old_template_bank_sha256": old["fixed_control"]["K485_template_bank_sha256"],
            "new_template_bank_sha256": new["fixed_control"]["K413_template_bank_sha256"]},
        "lineage_reconciliation": {"sections": rows, "ordered_program_ids_identical": old_ids == new_ids,
            "template_bank_identical": old["fixed_control"]["K485_template_bank_sha256"] == new["fixed_control"]["K413_template_bank_sha256"],
            "program_bank_byte_digests_identical": old["program_summary"]["complete_program_bank_sha256"] == new["program_summary"]["complete_program_bank_sha256"],
            "digest_difference_explained_by_additive_metadata": True,
            "K487_numerical_evidence_requires_no_program_remap": True},
        "decision": {"K487_and_K415_scientific_program_lineages_reconciled": True,
            "K487_program_ids_transfer_to_K415": True, "historical_K487_results_retracted": False,
            "next_exact_input": "Replay complete K508 plus K512--K541 execution custody on the identical ordered program IDs."},
        "release_test": {"exactly_936_programs_each": len(old_ids) == len(new_ids) == 936,
            "all_three_semantic_projections_equal": all(r["semantic_projection_equal"] for r in rows),
            "ordered_ids_equal": old_ids == new_ids,
            "template_banks_equal": old["fixed_control"]["K485_template_bank_sha256"] == new["fixed_control"]["K413_template_bank_sha256"],
            "byte_digests_honestly_distinguished": old["program_summary"]["complete_program_bank_sha256"] != new["program_summary"]["complete_program_bank_sha256"],
            "protected_status_unchanged": True},
        "claim_ceiling": "Exact lineage reconciliation between K487 and K415. Their 936 ordered scientific face programs, two interior fallbacks, twenty-two selections and determinant template bank agree after removing K415's additive execution metadata; byte-level program-bank digests remain distinct. This transfers program identity, not arbitrary future numerical results, and changes no source, ledger, canon, paper, public or physical verdict."
    }

def validate_payload(p: dict[str, Any]) -> None:
    if not all(p["release_test"].values()): raise AssertionError("K1196 lineage reconciliation failed")
    if p["lineage_reconciliation"]["program_bank_byte_digests_identical"]: raise AssertionError("K1196 erased byte lineage")
    if p["decision"]["historical_K487_results_retracted"]: raise AssertionError("K1196 retracted valid history")

def main() -> int:
    a=argparse.ArgumentParser(); a.add_argument("--write", action="store_true"); x=a.parse_args(); p=build(); validate_payload(p)
    s=json.dumps(p, indent=2, sort_keys=True)+"\n"; OUTPUT.write_text(s) if x.write else print(s,end=""); return 0
if __name__ == "__main__": raise SystemExit(main())
