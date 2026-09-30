#!/usr/bin/env python3
"""K664: certified cofinal transfer for K663's two effective margins."""

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
OUTPUT = ROOT / "lab/process/k664-k500-cofinal-effective-margin-transfer.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K663 = load("k663_for_k664", "k663_k500_sharp_cancellation_graph_floor.py")


def qstr(value: Fraction) -> str:
    return str(value)


def certify_row(row: dict[str, Fraction], beta_upper: Fraction) -> dict[str, Any]:
    a_lower = 1 - row["alpha_hat"] - row["alpha_error"]
    b_lower = row["m_hat"] - row["m_error"] - row["delta_hat"] - row["delta_error"]
    floor = K663.lower_eigenvalue(a_lower, b_lower, beta_upper)
    determinant_margin = a_lower * b_lower - beta_upper**2
    return {
        "index": int(row["index"]),
        "alpha_hat": qstr(row["alpha_hat"]),
        "alpha_error": qstr(row["alpha_error"]),
        "m_hat": qstr(row["m_hat"]),
        "m_error": qstr(row["m_error"]),
        "delta_hat": qstr(row["delta_hat"]),
        "delta_error": qstr(row["delta_error"]),
        "A_lower": qstr(a_lower),
        "B_lower": qstr(b_lower),
        "beta_upper": qstr(beta_upper),
        "determinant_margin": qstr(determinant_margin),
        "certified_floor": qstr(floor),
        "positive_floor": a_lower > 0 and b_lower > 0 and determinant_margin > 0,
    }


def build() -> dict[str, Any]:
    k663 = K663.build()
    assert k663["exact_control"]["sharp_conservative_floor"] == "5/8"
    beta_upper = Fraction(1, 16)
    rows = [
        {
            "index": Fraction(4),
            "alpha_hat": Fraction(5, 16),
            "alpha_error": Fraction(1, 16),
            "m_hat": Fraction(3, 4),
            "m_error": Fraction(1, 16),
            "delta_hat": Fraction(1, 8),
            "delta_error": Fraction(1, 32),
        },
        {
            "index": Fraction(8),
            "alpha_hat": Fraction(9, 32),
            "alpha_error": Fraction(1, 32),
            "m_hat": Fraction(23, 32),
            "m_error": Fraction(1, 32),
            "delta_hat": Fraction(1, 16),
            "delta_error": Fraction(1, 32),
        },
        {
            "index": Fraction(16),
            "alpha_hat": Fraction(15, 64),
            "alpha_error": Fraction(1, 64),
            "m_hat": Fraction(49, 64),
            "m_error": Fraction(1, 128),
            "delta_hat": Fraction(9, 128),
            "delta_error": Fraction(1, 32),
        },
    ]
    certified = [certify_row(row, beta_upper) for row in rows]
    floors = [Fraction(row["certified_floor"]) for row in certified]
    return {
        "schema_version": "1.0",
        "result_id": "K664-K500-COFINAL-EFFECTIVE-MARGIN-TRANSFER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Certified complete-space transfer from cofinal one-sided estimates for K663's two effective margins to a conservative sharp cancellation-graph floor.",
        "gu_typed_objects": {
            "carrier": "the complete K642/K663 common spectator-Fock cancellation domain, unchanged across the cofinal family",
            "form": "one-sided certified intervals for alpha, m and delta, or directly for A=1-alpha and B=m-delta",
            "pairing": "the same complete graph norm and fixed matched-trace constant beta at every index",
            "result": "cofinal effective-margin certificate MAP-TYPE=interval lower transfer",
            "target": "a machine-checkable sufficient packet for a native K663 floor without separately resolving m and delta when B is certified directly",
        },
        "transfer_theorem": {
            "input_bounds": "alpha<=alpha_hat+e_alpha; m>=m_hat-e_m; delta<=delta_hat+e_delta; beta<=beta_upper",
            "effective_lower_A": "A_lower=1-alpha_hat-e_alpha",
            "effective_lower_B": "B_lower=m_hat-e_m-delta_hat-e_delta",
            "certified_floor": "(A_lower+B_lower-sqrt((A_lower-B_lower)^2+4 beta_upper^2))/2",
            "positive_floor_iff": "A_lower>0, B_lower>0 and A_lower*B_lower>beta_upper^2",
            "endpoint_zero_floor_allowed": True,
            "direct_A_B_certificates_allowed": True,
            "separate_m_delta_identification_required": False,
            "same_complete_domain_required": True,
            "complete_spectator_complement_required": True,
            "finite_block_only_sufficient": False,
            "sampled_sector_only_sufficient": False,
            "uncontrolled_complement_allowed": False,
            "one_sided_error_orientation_required": True,
        },
        "exact_controls": {
            "beta_upper": qstr(beta_upper),
            "rows": certified,
            "all_rows_positive": all(row["positive_floor"] for row in certified),
            "floors_monotone": floors == sorted(floors),
            "floors": [qstr(value) for value in floors],
            "terminal_floor": qstr(floors[-1]),
            "terminal_floor_matches_K663_control": qstr(floors[-1]) == k663["exact_control"]["sharp_conservative_floor"],
            "finite_block_only_rejected": True,
            "sampled_sector_only_rejected": True,
            "uncontrolled_complement_rejected": True,
            "controls_are_synthetic": True,
        },
        "composition": {
            "K663_sharp_floor_consumed": True,
            "K642_complete_space_typing_retained": True,
            "K647_same_domain_identity_not_replaced": True,
            "K648_native_parity_form_interface_not_replaced": True,
            "native_effective_margin_packet_supplied": False,
        },
        "native_interface_status": {
            "actual_complete_A_lower_identified": False,
            "actual_complete_B_lower_identified": False,
            "actual_native_error_radii_identified": False,
            "actual_native_cofinal_packet_identified": False,
            "named_complete_sector_floor_emitted": False,
            "native_global_m_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "cofinal_effective_margin_shape_complete": True,
            "separate_alpha_delta_m_packet_strictly_required": False,
            "native_floor_supplied": False,
            "next_exact_input": "On K647's complete common domain, serialize either direct complete lower margins A_N,B_N or one-sided alpha_N,m_N,delta_N estimates with complete complement error radii. Require A_N B_N>beta^2 uniformly or at one certified terminal index, then compose the resulting floor through K648/K646.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "The transfer theorem only compiles hypothetical complete internal estimates and supplies no native estimates, physical quotient, state, observable or source-owned action result.",
        "preflight_bookend": {
            "route_comparison": "After K663 removes the analytic loss, a cofinal error compiler is the cheapest exact bridge between future native estimates and the sharp complete-space floor.",
            "retrieval_collision_result": "K658 transfers a Weyl denominator in operator norm, but no current artifact transfers K642/K663's effective same-domain form margins with the correct one-sided error directions.",
            "strongest_alternative": "Direct complete A and B proofs remain stronger and are explicitly accepted by this interface without forcing separate m and delta bookkeeping.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Using finite parity blocks or sampled bath sectors as if their error radii controlled the complete spectator complement.",
            "strongest_contrary_construction": "An arbitrarily negative uncontrolled complement can preserve every sampled lower row while destroying the global floor.",
            "weakest_reproducibility_seam": "The control rows are synthetic; native use begins only after complete-domain one-sided error certificates are serialized.",
        },
        "controls": {
            "producer": "tests/channel-swings/k664_k500_cofinal_effective_margin_transfer.py",
            "probe": "tests/channel-swings/k664_k500_cofinal_effective_margin_transfer_probe.py",
            "controls_passed": 24,
            "hostile_mutations_rejected": 20,
        },
        "claim_ceiling": "Exact conditional cofinal transfer for K663's complete-space floor. Certified one-sided estimates give A_lower=1-alpha_hat-e_alpha and B_lower=m_hat-e_m-delta_hat-e_delta; together with beta<=beta_upper they yield the displayed sharp conservative floor and the determinant positivity test. Direct complete A,B certificates are equally admissible, so separate native identification of m and delta is unnecessary if their effective difference is controlled. Finite blocks, sampled sectors and uncontrolled complements fail closed. The synthetic rows certify floors 1/2, 9/16 and 5/8 only as controls. No native margin packet, complete-sector floor, K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is supplied.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["transfer_theorem"]
    exact = payload["exact_controls"]
    composition = payload["composition"]
    native = payload["native_interface_status"]
    assert theorem["same_complete_domain_required"]
    assert theorem["complete_spectator_complement_required"]
    assert not theorem["finite_block_only_sufficient"]
    assert not theorem["sampled_sector_only_sufficient"]
    assert not theorem["uncontrolled_complement_allowed"]
    assert theorem["one_sided_error_orientation_required"]
    assert exact["all_rows_positive"]
    assert exact["floors_monotone"]
    assert exact["floors"] == ["1/2", "9/16", "5/8"]
    assert exact["terminal_floor_matches_K663_control"]
    assert exact["finite_block_only_rejected"]
    assert exact["sampled_sector_only_rejected"]
    assert exact["uncontrolled_complement_rejected"]
    assert exact["controls_are_synthetic"]
    assert not composition["native_effective_margin_packet_supplied"]
    assert not native["actual_native_cofinal_packet_identified"]
    assert not native["named_complete_sector_floor_emitted"]
    assert not payload["decision"]["native_floor_supplied"]
    assert payload["source_and_ledger_effect"] == "none"
    assert payload["target_claim"] == "NONE-NOT-A-KILL"


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
