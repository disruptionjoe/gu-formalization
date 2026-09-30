#!/usr/bin/env python3
"""K658: cofinal complete-space transfer for a Weyl-denominator margin."""

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
OUTPUT = ROOT / "lab/process/k658-k500-cofinal-denominator-margin-transfer.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K657 = load("k657_for_k658", "k657_k500_boundary_weyl_base_floor_certificate.py")


def transfer_row(d_n: Fraction, eta_n: Fraction, complete_coverage: bool = True) -> dict[str, Any]:
    margin = d_n - eta_n
    return {
        "approximant_margin_d_n": str(d_n),
        "complete_operator_error_eta_n": str(eta_n),
        "transferred_margin_d_n_minus_eta_n": str(margin),
        "complete_boundary_coverage": complete_coverage,
        "certificate_accepts": complete_coverage and margin >= 0,
    }


def build() -> dict[str, Any]:
    k657 = K657.build()
    rows = [
        transfer_row(Fraction(3, 4), Fraction(1, 4)),
        transfer_row(Fraction(1, 5), Fraction(1, 5)),
        transfer_row(Fraction(1, 8), Fraction(1, 4)),
        transfer_row(Fraction(9), Fraction(0), complete_coverage=False),
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K658-K500-COFINAL-DENOMINATOR-MARGIN-TRANSFER",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The exact complete-space perturbation transfer needed to turn one cofinal K141 approximation of K159's operator-valued Weyl denominator into K657's nonnegative real-level denominator certificate.",
        "gu_typed_objects": {
            "carrier": "one identified complete spectator-Fock boundary Hilbert space shared by the lifted cofinal approximant and limiting denominator",
            "form": "self-adjoint D_N(-s) and D(-s) in the same extension coordinate, compared in complete-space operator norm",
            "domain": "the full boundary space including every spectator-Fock complement direction",
            "target": "D(-s)>=0, hence K657 r0=-s and K656 b=-s-2",
            "result": "cofinal denominator-margin transfer MAP-TYPE=complete operator-order perturbation",
        },
        "cofinal_margin_theorem": {
            "approximant_hypothesis": "D_N(-s)>=d_N I on the identified complete boundary space",
            "error_hypothesis": "||D_N(-s)-D(-s)||<=eta_N on that same complete boundary space",
            "order_consequence": "D(-s)>=(d_N-eta_N)I",
            "floor_admission": "d_N-eta_N>=0",
            "strict_margin_required": False,
            "same_s_required": True,
            "same_extension_coordinate_required": True,
            "self_adjointness_required": True,
            "complete_boundary_coverage_required": True,
            "finite_impurity_only_sufficient": False,
            "sectorwise_pointwise_convergence_sufficient": False,
            "uncontrolled_complement_sufficient": False,
        },
        "composition": {
            "K657_equivalence_consumed": k657["ordinary_boundary_triple_theorem"]["equivalence"],
            "if_margin_nonnegative": "K657 gives A_W>=-s and r0=-s",
            "K656_consequence": "b=-s-2 on the complete K139/K168 reference form and every reducing bath/parity compression",
            "native_s_or_margin_supplied": False,
        },
        "exact_controls": {
            "rows": rows,
            "accepted_rows": 2,
            "rejected_rows": 2,
            "zero_transferred_margin_accepts": rows[1]["certificate_accepts"],
            "negative_transferred_margin_rejects": not rows[2]["certificate_accepts"],
            "incomplete_coverage_rejects_despite_large_margin": not rows[3]["certificate_accepts"],
            "controls_are_synthetic": True,
        },
        "decision": {
            "K159_missing_cofinal_denominator_separation_retyped": True,
            "K657_real_level_certificate_composed": True,
            "native_cofinal_packet_supplied": False,
            "next_exact_input": "For one proposed s, serialize K139/K141's same-coordinate complete operator-valued D_N(-s), prove a complete-space lower d_N and norm error eta_N with d_N>=eta_N, and verify K657's reference-floor and sign premises.",
        },
        "native_interface_status": {
            "actual_native_s_identified": False,
            "actual_native_d_n_identified": False,
            "actual_native_eta_n_identified": False,
            "actual_complete_boundary_coverage_proved": False,
            "actual_native_denominator_nonnegative": False,
            "actual_native_base_floor_r0_identified": False,
            "actual_native_target_b_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This operator-order transfer is internal to the repository-supplied boundary/Weyl control and supplies no action-owned carrier, physical quotient, observable or positive state-space metric.",
        "preflight_bookend": {
            "route_comparison": "K657 reduces the floor to complete denominator positivity; K159 already asks for cofinal Weyl errors. The sharp norm-margin transfer is the minimal bridge between those two interfaces.",
            "retrieval_collision_result": "K159 controls inverse denominators on a nonreal contour, while K658 requires direct self-adjoint denominator order at one real level. No prior artifact states this complete-space real-level transfer.",
            "strongest_alternative": "A direct analytic proof of D(-s)>=0 can bypass approximants; K652 remains the cancellation-form alternative if the boundary denominator cannot be controlled.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling positive finite impurity blocks a cofinal certificate without bounding the spectator-Fock complement in the same extension coordinate.",
            "strongest_contrary_construction": "A direct-sum complement carrying one negative eigenvalue defeats every finite displayed block while preserving their positive margins.",
            "weakest_reproducibility_seam": "No native same-coordinate D_N(-s), full-space d_N, complete norm error eta_N or selected s is currently serialized.",
        },
        "claim_ceiling": "Exact complete-space cofinal denominator-margin transfer. If a same-coordinate self-adjoint approximation obeys D_N(-s)>=d_N I and ||D_N(-s)-D(-s)||<=eta_N on the entire spectator-Fock boundary space, then D(-s)>=(d_N-eta_N)I. A nonnegative margin composes through K657 to r0=-s and through K656 to b=-s-2. Finite impurity blocks, sampled sectors, pointwise convergence and uncontrolled complements do not suffice. The controls are synthetic. No native s, d_N, eta_N, denominator, r0, b, tail, m, alpha, delta, K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is supplied.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["cofinal_margin_theorem"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["order_consequence"] == "D(-s)>=(d_N-eta_N)I"
    assert controls["accepted_rows"] == 2 and controls["rejected_rows"] == 2
    assert controls["zero_transferred_margin_accepts"]
    assert controls["negative_transferred_margin_rejects"]
    assert controls["incomplete_coverage_rejects_despite_large_margin"]
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
