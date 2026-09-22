#!/usr/bin/env python3
"""Decide whether K316's full-boundary pointwise coefficient can exist.

The proposed coefficient would have to cover every value/first/second-y
bordered family on the closed y/split cube.  Two already-proved endpoint facts
prevent that factorization: the terminal (8,8) entry is pointwise unbounded on
the split corner, and the endpoint-paired old-kernel factor has a logarithmically
unbounded second y derivative.  Both singularities are locally integrable only
with the native Peano/split weights retained inside the complete functional.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K300 = ROOT / "lab/process/k300-order-seven-angular-method-selection.json"
K301 = ROOT / "lab/process/k301-order-seven-terminal-split-boundary-correction.json"
K302 = ROOT / "lab/process/k302-order-seven-split-weighted-peano-jet.json"
K315 = ROOT / "lab/process/k315-order-seven-terminal-bordered-adapter.json"
K316 = ROOT / "lab/process/k316-order-seven-complete-y-master.json"
OUTPUT = ROOT / "lab/process/k317-order-seven-boundary-coefficient-discriminator.json"


def build() -> dict[str, Any]:
    k300 = json.loads(K300.read_text())
    k301 = json.loads(K301.read_text())
    k302 = json.loads(K302.read_text())
    k315 = json.loads(K315.read_text())
    k316 = json.loads(K316.read_text())

    families = k315["complete_column_replacement_expansion"]
    family_names = [family["family"] for family in families]
    second_families = [name for name in family_names if name.startswith("second_")]
    if len(families) != 21 or len(second_families) != 15:
        raise AssertionError("K315 bordered family census changed")
    if not k301["decision"]["uniform_pointwise_companion_bank_rejected"]:
        raise AssertionError("K301 pointwise obstruction unavailable")
    if not k302["complete_split_face_transfer"]["terminal_split_face_peano_weighted_integrable"]:
        raise AssertionError("K302 weighted repair unavailable")
    if k300["decision"]["complete_global_second_directional_norms_computed"]:
        raise AssertionError("K300 global norm posture changed")
    if k316["sufficiency_audit"]["global_nonterminal_angular_coefficient_available"]:
        raise AssertionError("K316 coefficient posture changed")

    endpoint_rows = k300["endpoint_integrability"]["rows"]
    worst_margin = min(row["second_derivative_integrability_margin"] for row in endpoint_rows)

    return {
        "schema_version": "1.0",
        "result_id": "K317-ORDER-SEVEN-BOUNDARY-COEFFICIENT-DISCRIMINATOR",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k300-order-seven-angular-method-selection.json",
                "lab/process/k301-order-seven-terminal-split-boundary-correction.json",
                "lab/process/k302-order-seven-split-weighted-peano-jet.json",
                "lab/process/k315-order-seven-terminal-bordered-adapter.json",
                "lab/process/k316-order-seven-complete-y-master.json",
            ],
            "bordered_family_count": len(families),
            "family_names": family_names,
            "second_derivative_family_count": len(second_families),
            "terminal_occurrences": k301["fixed_control"]["occurrences"],
            "terminal_core_slot": k315["fixed_control"]["terminal_core_slot"],
            "scaled_regularizer_degree": k316["fixed_control"]["scaled_regularizer_degree"],
        },
        "pointwise_discriminator": {
            "candidate": "one finite coefficient supremum for the remaining bordered entries on the closed s,y,u,z atlas",
            "terminal_split_path": k301["terminal_split_face"]["admitted_approach"],
            "terminal_argument": k301["terminal_split_face"]["terminal_argument"],
            "terminal_asymptotic": k301["terminal_split_face"]["kernel_asymptotic"],
            "terminal_pointwise_consequence": k301["terminal_split_face"]["pointwise_consequence"],
            "endpoint_paired_old_kernel": "F_x(y)=2*y*K1(x*y), x>0",
            "endpoint_expansion": "F_x(y)=2/x+x*y^2*(log(x*y/2)+EulerGamma-1/2)+O(x^3*y^4*abs(log(y)))",
            "second_y_derivative_expansion": "F_x''(y)=2*x*log(y)+O_x(1) as y->0+",
            "second_y_derivative_pointwise_supremum": "infinite",
            "why_one_counterexample_is_decisive": "the requested coefficient must cover all twenty-one families, including the fifteen second-derivative families; a single required endpoint factor with infinite pointwise supremum invalidates that universal factorization",
            "complete_functional_divergence_claimed": False,
            "coherent_cancellation_ruled_out": False,
        },
        "weighted_integrability": {
            "peano_kernel_near_left_endpoint": "K(y)=y^2/2",
            "leading_log_mass": "integral_0^(1/2) y^2*(-log(y)) dy = log(2)/24+1/72",
            "leading_log_mass_finite": True,
            "K300_worst_second_derivative_integrability_margin": worst_margin,
            "K302_terminal_bounds": k302["universal_weighted_bounds"],
            "pointwise_unboundedness_is_not_integral_divergence": True,
        },
        "replacement_contract": {
            "oracle_type": "weighted complete-chart integral, not a detached compact supremum",
            "required_order": [
                "retain the full K315 column-replacement determinant and coherent signs",
                "retain K299's Peano weight and the native y*(1-y) endpoint factors",
                "integrate the K302 terminal split variables inside the same y chart",
                "apply K314 only on its certified interior/one-gap projective leaves",
                "enclose the remaining K300 endpoint charts with their homogeneous weighted models",
                "take absolute values only after each complete chart/group assembly",
            ],
            "forbidden_shortcut": "multiply K302's marginal B_m by a global pointwise coefficient for the other entries",
            "finite_chart_cover_already_proved_qualitatively": k300["decision"]["positive_rule_face_legal"],
            "numerical_weighted_chart_constants_still_required": True,
        },
        "decision": {
            "full_boundary_pointwise_coefficient_exists": False,
            "K316_proposed_pointwise_factorization_rejected": True,
            "weighted_complete_chart_route_required": True,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_transfer_released": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "implement the K300 finite endpoint cover as determinant-preserving Peano-weighted chart integrals, beginning with the y=0/1 old-kernel charts and composing K302 inside those same integrals; do not seek a global remaining-entry supremum",
        },
        "release_test": {
            "all_twenty_one_families_consumed": len(families) == 21,
            "all_fifteen_second_derivative_families_present": len(second_families) == 15,
            "terminal_pointwise_obstruction_replayed": k301["release_test"]["every_pattern_contains_8_8"],
            "weighted_terminal_repair_replayed": k302["release_test"]["all_three_terminal_jet_orders_bounded"],
            "endpoint_log_obstruction_explicit": True,
            "pointwise_unboundedness_not_misreported_as_divergence": True,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k316["ledger_effect"],
        "source_routing": k316["source_routing"],
        "claim_ceiling": "Exact feasibility discriminator for K316's proposed full-boundary coefficient. The closed y/split atlas has no finite pointwise coefficient of the requested type: K301's terminal split entry is pointwise unbounded, and the endpoint-paired old-kernel factor F_x(y)=2yK1(xy) has F_x''(y)=2x log(y)+O_x(1). K300 and K302 prove these endpoint terms remain locally Peano/split weighted integrable, so this is a factorization obstruction, not divergence of the complete coherent functional. The next valid numerical route is a determinant-preserving weighted finite-chart integral. No complete y-master constant, gap-axis transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim is emitted.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["bordered_family_count"] != 21 or fixed["second_derivative_family_count"] != 15:
        raise AssertionError("bordered family coverage changed")
    discriminator = payload["pointwise_discriminator"]
    if discriminator["second_y_derivative_pointwise_supremum"] != "infinite":
        raise AssertionError("endpoint logarithmic obstruction lost")
    if discriminator["complete_functional_divergence_claimed"] or discriminator["coherent_cancellation_ruled_out"]:
        raise AssertionError("pointwise obstruction overclaimed")
    decision = payload["decision"]
    if decision["full_boundary_pointwise_coefficient_exists"]:
        raise AssertionError("invalid pointwise coefficient restored")
    if not decision["weighted_complete_chart_route_required"]:
        raise AssertionError("weighted replacement route lost")
    if decision["complete_y_master_constant_emitted"] or decision["five_gap_axis_transfer_released"]:
        raise AssertionError("downstream numerical overclaim")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
