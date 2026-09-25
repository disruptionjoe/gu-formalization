#!/usr/bin/env python3
"""K490 K168 shape form on K489's corrected native tail line."""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k490-k168-native-shape-cross-estimate.json"


def load_k489():
    path = HERE / "k489_native_neumann_word_m_orthogonalization.py"
    spec = importlib.util.spec_from_file_location("k489_for_k490", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K489 = load_k489()


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def interval_for_sector(row: dict[str, Any]) -> dict[str, Any]:
    b_lower, b_upper = map(Fraction, row["B_tail_mass_interval"])
    o_lower = Fraction(row["first_word_norm_sq_interval"][0])
    # The unresolved tail can contain either parity, so O <= B is the sharp
    # available upper relation without inventing higher-word data.
    ratio_lower = o_lower / ((1 + b_upper) * b_upper)
    ratio_upper = Fraction(1, 1 + b_lower)
    cross_sq_lower = 9 * o_lower * o_lower / ((1 + b_upper) ** 2 * b_upper)
    cross_sq_upper = 9 * b_upper / (1 + b_upper) ** 2
    cross_abs_lower = 3 * o_lower / (1 + b_upper)
    cross_abs_upper = 3 * b_upper / (1 + b_upper)
    vacuum_seed = row["charge"] == [0, 0]
    if vacuum_seed:
        theta = [-2 + 3 * ratio_lower, -2 + 3 * ratio_upper]
        sign = "positive"
        formula = "theta_t=-2+3 O/(A B)"
        raw_cross = "DeltaR(phi,t)=+3 O/A"
    else:
        theta = [1 - 3 * ratio_upper, 1 - 3 * ratio_lower]
        sign = "negative"
        formula = "theta_t=1-3 O/(A B)"
        raw_cross = "DeltaR(phi,t)=-3 O/A"
    return {
        "charge": row["charge"],
        "seed": row["seed"],
        "tail_odd_parity_mass_O_bounds": [qstr(o_lower), qstr(b_upper)],
        "corrected_tail_shape_Rayleigh_formula": formula,
        "corrected_tail_shape_Rayleigh_interval": [qstr(theta[0]), qstr(theta[1])],
        "trial_to_corrected_tail_shape_cross_formula": raw_cross,
        "trial_to_corrected_tail_shape_cross_sign": sign,
        "trial_to_corrected_tail_shape_cross_abs_interval": [qstr(cross_abs_lower), qstr(cross_abs_upper)],
        "M_normalized_shape_cross_sq_formula": "9 O^2/(A^2 B)",
        "M_normalized_shape_cross_sq_interval": [qstr(cross_sq_lower), qstr(cross_sq_upper)],
        "combined_base_plus_shape_cross_bounded": False,
    }


def build() -> dict[str, Any]:
    k489 = K489.build()
    sectors = [interval_for_sector(row) for row in k489["native_sectors"]]
    return {
        "schema_version": "1.0",
        "result_id": "K490-K168-NATIVE-SHAPE-CROSS-ESTIMATE",
        "created": "2026-09-25",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "scope": "K168's fixed shape diag(-2,1,1) on K489's actual q00/q10 first corrected M-orthogonal tail line. The base R0 form is deliberately not inferred.",
        "gu_typed_objects": {
            "result": "native K168 corrected-tail cross estimate MAP-TYPE=form-bound",
            "carrier": "K489 q00/q10 two-word cyclic slices inside the K162/K139 positive-Fock carrier",
            "pairing": "physical Gram M=S* S",
            "form": "only DeltaR=S*diag(-2,1,1)S, not the combined R0+DeltaR form",
            "target": "component input and correction for a future K473 combined-form cross estimate",
        },
        "exact_identities": {
            "A": "1+B",
            "B": "sum_(n>=1)||G^n phi||^2",
            "O": "sum over odd n of ||G^n phi||^2",
            "corrected_tail": "t=G phi-(B/A)phi",
            "q00_shape_cross": "+3 O/A",
            "q10_shape_cross": "-3 O/A",
            "normalized_cross_sq": "9 O^2/(A^2 B)",
            "q00_tail_Rayleigh": "-2+3 O/(A B)",
            "q10_tail_Rayleigh": "1-3 O/(A B)",
        },
        "native_sector_bounds": sectors,
        "decision": {
            "actual_K168_component_cross_bounded": True,
            "naive_free_tail_cross_used": False,
            "base_R0_cross_bounded": False,
            "combined_K139_K168_cross_bounded": False,
            "K473_beta_emitted": False,
            "next_exact_input": "Evaluate the same corrected graph under the cancellation-safe base R0 form. Combine its signed cross with K490 before enlarging to the complete complement; do not add separate absolute bounds for auxiliary +256 and -256 pieces.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact native K168 component Rayleigh and cross intervals on K489's corrected q00/q10 M-orthogonal first-tail lines. The sign flips with the seed parity and the naive free-word tail is not used. The cancellation-safe base R0 cross, combined form, complete complement, K473 beta, K152 interval, source, ledger, canon, paper, public and physical conclusions remain open.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    payload = build()
    if args.write:
        OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    if args.demo or not args.write:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
