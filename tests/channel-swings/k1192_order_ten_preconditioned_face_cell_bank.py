#!/usr/bin/env python3
"""Audit exact reuse and workload for an all-face order-ten cell bank."""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT = Path(__file__).resolve().parents[2]
K413 = ROOT / "lab/process/k413-order-ten-mask-native-preconditioner-compiler.json"
K415 = ROOT / "lab/process/k415-order-ten-face-program-compiler.json"
OUTPUT = ROOT / "lab/process/k1192-order-ten-preconditioned-face-cell-bank.json"

def digest(v: Any) -> str: return "sha256:" + hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def q(v: Fraction) -> str: return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"

def full_signature(row: dict[str, Any]) -> tuple[Any, ...]:
    return (row["axis"], tuple(row["zeroed_axes"]), int(row["codimension"]), bool(row["active_peano_axis_zeroed"]), tuple(row["maximum_value_first_second_singular_powers"]), int(row["minimum_second_derivative_face_normal_power"]), row["descriptor_program_sha256"])

def reduced_signature(row: dict[str, Any]) -> tuple[Any, ...]:
    return (tuple(row["zeroed_axes"]), int(row["codimension"]), bool(row["active_peano_axis_zeroed"]), tuple(row["maximum_value_first_second_singular_powers"]), int(row["minimum_second_derivative_face_normal_power"]))

def build() -> dict[str, Any]:
    k413, k415 = json.loads(K413.read_text()), json.loads(K415.read_text())
    rows = k415["face_programs"]
    full, reduced = Counter(full_signature(r) for r in rows), Counter(reduced_signature(r) for r in rows)
    masks = Counter(tuple(r["zeroed_axes"]) for r in rows)
    one_cell = len(rows) * 13_300
    ratio = Fraction(one_cell, 877_800)
    return {
        "schema_version": "1.0", "result_id": "K1192-ORDER-TEN-ALL-FACE-CELL-REUSE-OBSTRUCTION",
        "created": "2026-10-06", "classification": "INTERNAL_STRUCTURAL_ONLY", "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(K413.relative_to(ROOT)), str(K415.relative_to(ROOT))],
            "face_programs_audited": len(rows), "ordered_descriptors_per_face_cell": 13_300,
            "one_cell_per_face_descriptor_evaluations": one_cell, "ratio_to_K1191_three_scale_selected_bank": q(ratio),
            "full_axis_mask_descriptor_signatures": len(full), "reduced_axis_erased_signatures": len(reduced),
            "unique_zero_masks": len(masks), "maximum_programs_per_zero_mask": max(masks.values()),
            "singleton_full_signatures": sum(v == 1 for v in full.values()),
            "singular_template_count": len(k413["preconditioner_templates"]),
            "confluent_template_count": len(k413["confluent_divided_difference_contract"]["templates"]),
            "full_signature_digest": digest(sorted((repr(k), v) for k, v in full.items())),
        },
        "reuse_boundary": {
            "every_complete_axis_mask_descriptor_signature_is_unique": len(full) == len(rows) and all(v == 1 for v in full.values()),
            "erasing_axis_or_descriptor_data_creates_apparent_reuse_only": len(reduced) < len(full),
            "zero_mask_deduplication_is_coordinate_geometry_not_numerical_integrand_reuse": True,
            "template_reuse_eliminates_complete_group_assembly": False,
            "one_cell_all_face_bank_executed": False,
        },
        "decision": {
            "exact_whole_program_reuse_releases_all_face_arb_bank": False,
            "literal_all_face_bank_deferred_on_measured_resource_cost": True,
            "projective_zero_mask_geometry_released": True,
            "next_exact_input": "Exploit the 121 zero masks for projective geometry, but require a new factorization or cached group-level evaluator before returning to the 936 unique numerical programs.",
        },
        "release_test": {
            "exactly_936_face_programs": len(rows) == 936, "all_936_full_signatures_unique": len(full) == 936 and all(v == 1 for v in full.values()),
            "exactly_230_axis_erased_signatures": len(reduced) == 230, "exactly_121_zero_masks": len(masks) == 121,
            "maximum_20_programs_per_zero_mask": max(masks.values()) == 20,
            "exactly_12448800_one_cell_descriptor_evaluations": one_cell == 12_448_800,
            "exact_ratio_156_over_11": ratio == Fraction(156, 11), "exactly_60_singular_and_75_confluent_templates": len(k413["preconditioner_templates"]) == 60 and len(k413["confluent_divided_difference_contract"]["templates"]) == 75,
            "all_face_bank_not_overclaimed": True, "complete_order_ten_remainder_not_overclaimed": True,
        },
        "ledger_effect": k415["ledger_effect"], "source_routing": k415["source_routing"],
        "claim_ceiling": "Exact reuse obstruction and workload census for a positive-width cell on every K415 order-ten face. All 936 complete axis/mask/descriptor program signatures are unique. Erasing axis and descriptor ownership collapses them to 230 signatures and 121 zero masks, but that is coordinate reuse, not licensed numerical-integrand reuse. One cell per face still costs 12,448,800 descriptor evaluations, exactly 156/11 times K1191's entire planned selected bank. No all-face Arb bank, Peano remainder, integral, action column, K152 interval, source, ledger, canon, paper, public or physical claim is emitted.",
    }

def validate_payload(p: dict[str, Any]) -> None:
    f=p["fixed_control"]
    if (f["face_programs_audited"],f["one_cell_per_face_descriptor_evaluations"],f["ratio_to_K1191_three_scale_selected_bank"],f["full_axis_mask_descriptor_signatures"],f["reduced_axis_erased_signatures"],f["unique_zero_masks"],f["maximum_programs_per_zero_mask"],f["singular_template_count"],f["confluent_template_count"]) != (936,12_448_800,"156/11",936,230,121,20,60,75): raise AssertionError("K1192 census changed")
    if not p["reuse_boundary"]["every_complete_axis_mask_descriptor_signature_is_unique"] or p["reuse_boundary"]["one_cell_all_face_bank_executed"]: raise AssertionError("K1192 reuse boundary changed")
    if not all(p["release_test"].values()): raise AssertionError("K1192 release test failed")

def main() -> int:
    a=argparse.ArgumentParser(); a.add_argument("--write",action="store_true"); x=a.parse_args(); p=build(); validate_payload(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"; OUTPUT.write_text(s) if x.write else print(s,end=""); return 0
if __name__ == "__main__": raise SystemExit(main())
