#!/usr/bin/env python3
"""Independent replay and hostile controls for K300."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k300-order-seven-angular-method-selection.json"


def errors(data: dict) -> list[str]:
    out = []
    fixed = data.get("fixed_control", {})
    if fixed.get("duffy_gap_order") != ["r0", "r1", "r2", "c0", "c1", "c2"]:
        out.append("gap order")
    if fixed.get("tensor_remainder_order") != ["t0", "t1", "t2", "t3", "t4", "y"]:
        out.append("tensor order")
    if fixed.get("y_integrated_after_every_gap_error") is not True:
        out.append("y order")
    transfer = data.get("face_transfer", {})
    if transfer.get("projective_one_gap_faces_replayed") != 6:
        out.append("face count")
    if transfer.get("every_one_gap_native_plus_cauchy_valuation") != [2]:
        out.append("face valuation")
    if transfer.get("left_terminal_gap", {}).get("duffy_face") != "t2=0":
        out.append("left terminal")
    if not str(transfer.get("right_terminal_gap", {}).get("duffy_face", "")).startswith("t4=1"):
        out.append("right terminal")
    endpoint = data.get("endpoint_integrability", {})
    if endpoint.get("worst_endpoint_second_derivative_margin") != 2:
        out.append("endpoint margin")
    if endpoint.get("worst_complete_face_second_derivative_margin") != 1:
        out.append("complete margin")
    if transfer.get("worst_projective_face_second_derivative_margin") != 1:
        out.append("projective margin")
    if endpoint.get("all_second_directional_derivatives_locally_absolutely_integrable") is not True:
        out.append("integrability")
    comparison = data.get("method_comparison", {})
    if comparison.get("selection") != "positive_peano":
        out.append("selection")
    if comparison.get("analytic_subtraction", {}).get("minimum_terminal_sector_models") != 8:
        out.append("sector count")
    decision = data.get("decision", {})
    if decision.get("complete_global_second_directional_norms_computed") is not False or decision.get("k294_low_middle_high_gamma_strata_joined") is not False:
        out.append("claim ceiling")
    return out


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    checks = 14
    assert not errors(data), errors(data)
    mutations = []
    for mutate in (
        lambda d: d["fixed_control"].update(duffy_gap_order=list(reversed(d["fixed_control"]["duffy_gap_order"]))),
        lambda d: d["fixed_control"].update(tensor_remainder_order=["y", "t0", "t1", "t2", "t3", "t4"]),
        lambda d: d["fixed_control"].update(y_integrated_after_every_gap_error=False),
        lambda d: d["face_transfer"].update(projective_one_gap_faces_replayed=5),
        lambda d: d["face_transfer"].update(every_one_gap_native_plus_cauchy_valuation=[1]),
        lambda d: d["face_transfer"]["left_terminal_gap"].update(duffy_face="t2=1"),
        lambda d: d["face_transfer"]["right_terminal_gap"].update(duffy_face="t4=0"),
        lambda d: d["endpoint_integrability"].update(worst_endpoint_second_derivative_margin=0),
        lambda d: d["endpoint_integrability"].update(worst_complete_face_second_derivative_margin=0),
        lambda d: d["endpoint_integrability"].update(all_second_directional_derivatives_locally_absolutely_integrable=False),
        lambda d: d["method_comparison"].update(selection="analytic_subtraction"),
        lambda d: d["method_comparison"]["analytic_subtraction"].update(minimum_terminal_sector_models=4),
        lambda d: d["decision"].update(k294_low_middle_high_gamma_strata_joined=True),
    ):
        changed = copy.deepcopy(data)
        mutate(changed)
        mutations.append(changed)
    rejected = sum(bool(errors(changed)) for changed in mutations)
    assert rejected == len(mutations), (rejected, len(mutations))
    print(f"k300_angular_method_selection_probe: {checks}/{checks} checks pass; hostile {rejected}/{len(mutations)} rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
