#!/usr/bin/env python3
"""K571 compare K466 shifted-coercivity residual bounds with K469."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k571-k152-shifted-coercivity-dominance.json"
ROUTING = (
    "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or "
    "borders a conventional particle-physics comparator. Any result about a "
    "standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` "
    "Majorana mechanism, anomaly selector, VEV-only breaking or familiar "
    "vector-mass route binds only that named model. It is not evidence for or "
    "against Weinstein's source-native mechanism without an explicit typed "
    "bridge. Read `lab/methods/source-native-comparator-routing.md` and follow "
    "its source-native pointers before reusing this result."
)


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict:
    # Sharp two-dimensional control: M=I, A=R+sM=3I, ||u||_M=1.
    a = Fraction(3)
    c = Fraction(3)
    eta_sq = Fraction(5)
    shifted_dual_sq = Fraction(5, 3)
    bridge_energy = a * eta_sq / c
    actual_energy = a * shifted_dual_sq
    return {
        "schema_version": "1.0",
        "result_id": "K571-K152-SHIFTED-COERCIVITY-DOMINANCE",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "gu_comparator_routing": ROUTING,
        "gu_comparator_classification": "INTERNAL_ONLY__NO_SOURCE_NATIVE_OR_CONVENTIONAL_PARTICLE_VERDICT",
        "scope": "The K465/K466 conversion of a complete M-dual trial residual into K152 shifted-form residual energy on the same fixed generalized-M form packet consumed directly by K469.",
        "gu_typed_objects": {
            "result": "shifted-coercivity residual dominance MAP-TYPE=conditional-theorem",
            "carrier": "one fixed complete K162 charge sector",
            "pairing": "positive physical metric M=S* S",
            "form": "A_s=R+sM with A_s>=cM>0",
            "real_structure": "CAR adjoint on the fixed charge sector",
            "grading": "trial line plus complete M-orthogonal complement",
            "action_owner": "repository construction; no source/GU action selects the extension or scalar center",
            "target": "K466/K467 shifted residual energy versus K469 direct M-dual residual square",
        },
        "source_and_ledger_context": {
            "source_claims": ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06", "SC-META-53"],
            "source_polarity_effect": "none",
            "physics_rows": ["LT-SM8", "LT-GR6b", "RA-F1", "AC-F1"],
            "ledger": "lab/process/conditional-physics-ledger-v0.263.json",
            "ledger_effect": "none",
            "inputs": ["K465", "K466", "K467", "K469", "K570"],
        },
        "theorem": {
            "normalization": "<u,Mu>=1 and rho=<u,Ru>",
            "shifted_trial_value": "a=rho+s=<u,(R+sM)u>",
            "coercivity_hypothesis": "R+sM>=cM>0",
            "variational_ceiling": "c<=a",
            "K466_shifted_dual_upper": "ell*(R+sM)^(-1)ell<=eta^2/c, eta^2=ell*M^(-1)ell",
            "K152_residual_energy_upper": "a*ell*(R+sM)^(-1)ell<=a*eta^2/c",
            "dominance": "a/c>=1, so the K466-derived residual-energy upper is never smaller than the direct M-dual upper eta^2 used by K469",
            "shift_can_rescue_coarse_M_dual_upper": False,
            "actual_shifted_dual_may_be_smaller_than_bridge_upper": True,
            "complete_complement_floor_still_required_by_K469": True,
        },
        "sharp_control": {
            "M": "I_2",
            "shifted_form": "3 I_2",
            "trial": "e1",
            "covector": ["1", "2"],
            "a": q(a),
            "c": q(c),
            "M_dual_square": q(eta_sq),
            "shifted_form_dual_square": q(shifted_dual_sq),
            "K466_residual_energy_upper": q(bridge_energy),
            "actual_shifted_residual_energy": q(actual_energy),
            "direct_M_dual_upper": q(eta_sq),
            "all_equal": bridge_energy == actual_energy == eta_sq,
            "control_is_native_K162_packet": False,
        },
        "decision": {
            "quantitative_K466_c_needed_to_improve_residual_accuracy": False,
            "K466_remains_valid_for_shifted_form_typing": True,
            "K469_direct_M_dual_consumer_is_weakly_dominant": True,
            "K570_coarse_upper_not_repaired_by_shift": True,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Pursue a useful reference-specific complete-complement/action-flux floor and a much tighter complete M-dual residual upper; do not chase a large shift as a residual-accuracy repair.",
        },
        "claim_ceiling": "Exact conditional comparison of two certificate routes on the same normalized fixed form. K466 remains a correct metric bridge, but its K152 residual-energy upper carries factor (rho+s)/c>=1 and therefore cannot beat K469's direct M-dual upper. This does not lower the actual native residual, supply a complete complement floor, emit K152, or change source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusions.",
    }


def validate(payload: dict) -> None:
    theorem = payload["theorem"]
    decision = payload["decision"]
    if theorem["variational_ceiling"] != "c<=a" or theorem["shift_can_rescue_coarse_M_dual_upper"]:
        raise AssertionError("K571 variational dominance changed")
    if not payload["sharp_control"]["all_equal"]:
        raise AssertionError("K571 sharp control failed")
    if not decision["K469_direct_M_dual_consumer_is_weakly_dominant"]:
        raise AssertionError("K571 lost route decision")
    if decision["native_K152_interval_emitted"]:
        raise AssertionError("K571 overclaimed native closure")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
