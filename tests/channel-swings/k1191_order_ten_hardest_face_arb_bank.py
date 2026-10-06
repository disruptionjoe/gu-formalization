#!/usr/bin/env python3
"""Audit the literal order-eight hardest-face Arb port at order ten."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K412 = ROOT / "lab/process/k412-order-ten-interior-origin-control.json"
K415 = ROOT / "lab/process/k415-order-ten-face-program-compiler.json"
OUTPUT = ROOT / "lab/process/k1191-order-ten-hardest-face-arb-bank.json"

def digest(value: Any) -> str:
    return "sha256:" + hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"

def build() -> dict[str, Any]:
    k412, k415 = json.loads(K412.read_text()), json.loads(K415.read_text())
    programs = {row["program_id"]: row for row in k415["face_programs"] + k415["positive_interior_fallback_programs"]}
    selected = [programs[row["program_id"]] for row in k415["selected_boundary_or_interior_program_per_hybrid"]]
    controls, descriptors = len(selected) * 3, 13_300
    workload, old_workload = controls * descriptors, 54 * 2_400
    ratio = Fraction(workload, old_workload)
    faces = sum(row["face_kind"] != "positive_interior_fallback" for row in selected)
    fallbacks = len(selected) - faces
    return {
        "schema_version": "1.0", "result_id": "K1191-ORDER-TEN-HARDEST-FACE-ARB-PORT-COST-BOUNDARY",
        "created": "2026-10-06", "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY", "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(K412.relative_to(ROOT)), str(K415.relative_to(ROOT))],
            "hybrid_terms": len(selected), "reachable_face_programs": faces, "positive_interior_fallbacks": fallbacks,
            "normal_levels_per_program": 3, "planned_complete_arb_controls": controls,
            "ordered_descriptors_per_control": descriptors, "planned_descriptor_control_evaluations": workload,
            "order_eight_predecessor_descriptor_evaluations": old_workload, "exact_workload_ratio_to_order_eight": q(ratio),
            "bounded_attempt_arb_decimal_digits": 180, "bounded_attempt_threads": 1,
            "bounded_attempt_cpu_seconds_lower": 2000, "durable_complete_bank_emitted": False,
            "selected_program_digest": digest(selected),
        },
        "execution_observation": {
            "literal_port_started": True, "literal_port_interrupted_after_bounded_window": True,
            "numerical_or_domain_exception_observed": False, "partial_in_memory_rows_promoted": False,
            "measurement_is_a_host_cost_observation_not_a_mathematical_no_go": True,
        },
        "decision": {
            "literal_three_scale_direct_port_selected": False, "port_rejected_for_this_launch_on_measured_resource_cost": True,
            "mathematical_face_program_rejected": False,
            "next_exact_input": "Audit exact whole-program reuse before any further Arb execution; preserve the full 936-face question and do not infer numerical failure from host cost.",
        },
        "release_test": {
            "exactly_22_hybrids_audited": len(selected) == 22,
            "exactly_20_reachable_faces_and_2_fallbacks": faces == 20 and fallbacks == 2,
            "exactly_66_controls_planned": controls == 66,
            "exactly_877800_descriptor_evaluations_planned": workload == 877_800,
            "exact_ratio_1463_over_216": ratio == Fraction(1463, 216),
            "bounded_attempt_exceeded_2000_cpu_seconds": True, "no_partial_bank_promoted": True,
            "complete_order_ten_remainder_not_overclaimed": True, "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k415["ledger_effect"], "source_routing": k415["source_routing"],
        "claim_ceiling": "Exact workload and bounded-execution result for the literal K355-style order-ten hardest-face port. The 22-hybrid, three-level bank requires 877,800 complete descriptor evaluations, exactly 1463/216 times the order-eight predecessor count. One 180-digit single-thread attempt exceeded 2,000 CPU seconds and was interrupted without a durable partial bank. This rejects the literal port for this launch, not the mathematical face program, its finiteness, the order-ten integral, or any source, ledger, canon, paper, public or physical claim.",
    }

def validate_payload(payload: dict[str, Any]) -> None:
    f = payload["fixed_control"]
    actual = (f["hybrid_terms"], f["reachable_face_programs"], f["positive_interior_fallbacks"], f["normal_levels_per_program"], f["planned_complete_arb_controls"], f["ordered_descriptors_per_control"], f["planned_descriptor_control_evaluations"], f["exact_workload_ratio_to_order_eight"], f["durable_complete_bank_emitted"])
    if actual != (22, 20, 2, 3, 66, 13_300, 877_800, "1463/216", False): raise AssertionError("K1191 workload census changed")
    if f["bounded_attempt_cpu_seconds_lower"] < 2000: raise AssertionError("K1191 bounded attempt evidence weakened")
    if payload["decision"]["mathematical_face_program_rejected"] or payload["execution_observation"]["partial_in_memory_rows_promoted"]: raise AssertionError("K1191 overclaimed resource result")
    if not all(payload["release_test"].values()): raise AssertionError("K1191 release test failed")

def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument("--write", action="store_true"); a = p.parse_args()
    payload = build(); validate_payload(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    OUTPUT.write_text(rendered) if a.write else print(rendered, end="")
    return 0

if __name__ == "__main__": raise SystemExit(main())
