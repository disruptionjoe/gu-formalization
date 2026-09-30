#!/usr/bin/env python3
"""K655: no numerical shifted target follows from current K139/K168 custody."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k655-k500-shifted-target-custody-obstruction.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K653 = load("k653_for_k655", "k653_k500_shifted_schur_target_certificate.py")


def failure_row(target: Fraction) -> dict[str, Any]:
    """Choose an allowed K612 family member whose first shifted diagonal fails."""
    parameter = abs(target) + 3
    base_value = -parameter
    reference_shift = Fraction(-2)
    complete_value = base_value + reference_shift
    shifted_gap = complete_value - target
    return {
        "target_b": str(target),
        "parameter_L": str(parameter),
        "base_regular_value": str(base_value),
        "reference_negative_direction": str(reference_shift),
        "complete_diagonal_value": str(complete_value),
        "shifted_gap": str(shifted_gap),
        "first_K653_hypothesis_fails": shifted_gap < 0,
    }


def build() -> dict[str, Any]:
    k653 = K653.build()
    targets = [Fraction(-100), Fraction(-3), Fraction(-2), Fraction(0), Fraction(5, 4)]
    rows = [failure_row(target) for target in targets]
    return {
        "schema_version": "1.0",
        "result_id": "K655-K500-SHIFTED-TARGET-CUSTODY-OBSTRUCTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Whether the quantitative interface currently serialized by K612 and consumed by K653 can select any finite numerical target b for the fixed K139/K168 reference form.",
        "gu_typed_objects": {
            "carrier": "K612 same-interface two-dimensional controls, not sectors of the fixed native operator",
            "form": "a base regular diagonal plus K168's sharp negative reference direction -2M",
            "domain": "one common finite control domain with M=I",
            "target": "the first shifted-diagonal hypothesis in K653",
            "result": "shifted-target custody obstruction MAP-TYPE=data-sufficiency countermodel",
        },
        "interface_theorem": {
            "statement": "For every finite target b chosen from the currently serialized interface alone, the K612 family contains an allowed member with L=|b|+3 and complete negative-direction value -L-2<b.",
            "first_failure": "the first K653 shifted diagonal has value -L-2-b<0",
            "all_finite_targets_defeated_over_interface_class": True,
            "fixed_native_operator_proved_unbounded_below": False,
            "actual_native_sector_row_identified": False,
            "new_same_domain_estimate_can_reopen": True,
        },
        "exact_controls": {
            "same_interface_not_native": True,
            "rows": rows,
            "all_rows_fail_first_shifted_diagonal": all(row["first_K653_hypothesis_fails"] for row in rows),
            "target_count": len(rows),
        },
        "decision": {
            "K653_consumed": k653["decision"]["direct_target_route_closed_abstractly"],
            "current_custody_selects_numerical_target": False,
            "another_target_guess_before_new_native_evidence_is_decision_grade": False,
            "next_exact_input": "Prove one numerical same-domain base lower R0>=r0 M (or an equivalent complete-form lower) for the fixed K139 operator; K168 then supplies the sharp target b=r0-2.",
        },
        "native_interface_status": {
            "K612_custody_obstruction_sharpened_to_K653": True,
            "actual_native_target_b_identified": False,
            "actual_native_shifted_diagonal_positivity_proved": False,
            "actual_native_shifted_cross_contraction_proved": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a data-sufficiency result for a repository-supplied conditional point-Fock operator interface; the countermodels are not physical states or the fixed native operator.",
        "preflight_bookend": {
            "route_comparison": "K654 asks for a native target, but K612 says the available interface has no quantitative base floor. Composing the two first decides whether target search is meaningful before attempting new sector estimates.",
            "retrieval_collision_result": "K612 proves numerical-floor nonidentifiability and K653 gives the shifted target test; no prior artifact exhibits the exact first K653 failure for every proposed target.",
            "strongest_alternative": "K652's absolute all-order envelopes remain valid but require strictly more native quantitative input than the single base lower isolated here.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling an interface countermodel an actual K139/K168 sector or concluding that the fixed operator has no lower bound.",
            "strongest_contrary_construction": "A newly proved same-domain base lower immediately defeats this nonidentifiability and permits a target; the obstruction is custody-relative, not operator-absolute.",
            "weakest_reproducibility_seam": "The family preserves only the serialized interface fields. It intentionally does not reconstruct every unrecorded property of the fixed native operator.",
        },
        "claim_ceiling": "Exact data-custody obstruction for K653 target selection. For every finite b inferred only from the currently serialized K612/K168 interface, a same-interface control has first shifted diagonal -L-2-b<0, so no numerical target follows from those data. These controls are not sectors of the fixed native K139/K168 operator, do not deny its qualitative semibound, and do not exclude a new same-domain estimate. No native b, tail, m, alpha, delta, K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["interface_theorem"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["all_finite_targets_defeated_over_interface_class"]
    assert not theorem["fixed_native_operator_proved_unbounded_below"]
    assert controls["same_interface_not_native"] and controls["all_rows_fail_first_shifted_diagonal"]
    assert not native["actual_native_target_b_identified"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
