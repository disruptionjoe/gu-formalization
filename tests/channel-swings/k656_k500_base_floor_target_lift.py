#!/usr/bin/env python3
"""K656: lift one base-form lower through K168 to a sharp target."""

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
OUTPUT = ROOT / "lab/process/k656-k500-base-floor-target-lift.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K655 = load("k655_for_k656", "k655_k500_shifted_target_custody_obstruction.py")


def lift_row(base_floor: Fraction) -> dict[str, Any]:
    target = base_floor - 2
    reference_eigenvalues = [Fraction(-2), Fraction(1), Fraction(1)]
    complete_values = [base_floor + value for value in reference_eigenvalues]
    shifted_gaps = [value - target for value in complete_values]
    return {
        "base_floor_r0": str(base_floor),
        "target_b": str(target),
        "reference_eigenvalues": [str(value) for value in reference_eigenvalues],
        "complete_values_on_sharp_control": [str(value) for value in complete_values],
        "shifted_gaps": [str(value) for value in shifted_gaps],
        "all_shifted_gaps_nonnegative": all(value >= 0 for value in shifted_gaps),
        "negative_reference_direction_saturates": shifted_gaps[0] == 0,
    }


def build() -> dict[str, Any]:
    k655 = K655.build()
    rows = [lift_row(value) for value in (Fraction(-7), Fraction(0), Fraction(3), Fraction(11, 4))]
    return {
        "schema_version": "1.0",
        "result_id": "K656-K500-BASE-FLOOR-TARGET-LIFT",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The sharp lower-target consequence of one separately proved same-domain numerical lower R0>=r0 M for K139's fixed base regular form under K168's reference extension.",
        "gu_typed_objects": {
            "carrier": "the complete K139 common form domain and all of its K643/K648 reducing compressions",
            "form": "R_ref=R0+S*W_ref*S with M=S*S and W_ref=diag(-2,1,1)",
            "domain": "the single K647 common graph form domain",
            "target": "a native K653/K654 candidate b derived from a separately proved base lower r0",
            "result": "base-floor target lift MAP-TYPE=sharp form-order transfer",
        },
        "base_floor_lift_theorem": {
            "new_input": "R0>=r0 M on the complete common form domain",
            "existing_native_order": "-2M<=Delta R<=M from K168",
            "composition": "R_ref=R0+Delta R>=(r0-2)M",
            "selected_target": "b=r0-2",
            "compression_consequence": "every bath-number and total-parity compression has floor at least b",
            "K653_sector_search_required_after_global_base_lower": False,
            "two_unit_loss_sharp_over_declared_reference_class": True,
            "sharpness_witness": "R0=r0 M on a vector in W_ref's -2 eigenspace",
            "same_domain_required": True,
        },
        "exact_controls": {
            "conditional_not_native_number": True,
            "rows": rows,
            "all_rows_pass": all(row["all_shifted_gaps_nonnegative"] for row in rows),
            "all_rows_sharp": all(row["negative_reference_direction_saturates"] for row in rows),
            "row_count": len(rows),
        },
        "decision": {
            "K655_custody_obstruction_consumed": k655["interface_theorem"]["all_finite_targets_defeated_over_interface_class"],
            "minimal_numerical_repair_identified": True,
            "native_base_floor_r0_supplied": False,
            "native_target_floor_emitted": False,
            "next_exact_input": "Derive one numerical complete same-domain base lower r0 for the fixed K139 regular form. Then set b=r0-2, compose through every K643/K648 compression, and separately prove the K642 remainder constants alpha,delta.",
        },
        "native_interface_status": {
            "K168_order_consumed": True,
            "conditional_target_formula_complete": True,
            "actual_native_base_floor_r0_identified": False,
            "actual_native_target_b_identified": False,
            "actual_uniform_parity_tails_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This conditional form-order transfer remains inside the repository-supplied K139/K168 mathematical control and supplies no action-owned state, observable, quotient or physical positivity result.",
        "preflight_bookend": {
            "route_comparison": "After K655, guessing b is unproductive. K168 already makes one complete base lower sufficient, so isolating r0 is cheaper and stronger than independent per-sector target tests.",
            "retrieval_collision_result": "K168 states the order interval and K612 states the missing base lower, but no prior artifact composes them into the sharp native target formula and all-compression consequence.",
            "strongest_alternative": "K652's all-order A_s,D_s,K_s envelopes remain useful if a global base lower is unavailable; they require more sectorwise information but may succeed on a correlated domain.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Substituting an invented or finite-control r0 into b=r0-2 and reporting the result as native m or physical positivity.",
            "strongest_contrary_construction": "K655's family shows that without a proved r0 the formula selects no number; the conditional lift cannot repair absent custody by itself.",
            "weakest_reproducibility_seam": "The transfer is exact and sharp, but the only new numerical input r0 remains entirely unserialized for the fixed operator.",
        },
        "claim_ceiling": "Exact conditional target lift for the fixed K139/K168 common form. A separately proved complete base lower R0>=r0 M combines with K168's sharp order R_ref>=R0-2M to give b=r0-2 on the complete form and every bath/parity compression. The two-unit loss is sharp over the declared reference-shape class. No numerical r0 or b, native tail, m, alpha, delta, K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is supplied.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["base_floor_lift_theorem"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["selected_target"] == "b=r0-2"
    assert theorem["two_unit_loss_sharp_over_declared_reference_class"]
    assert controls["all_rows_pass"] and controls["all_rows_sharp"]
    assert not native["actual_native_base_floor_r0_identified"]


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
