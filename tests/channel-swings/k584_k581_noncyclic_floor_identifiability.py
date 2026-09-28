#!/usr/bin/env python3
"""K584 identifiability limit for K581's numerical noncyclic floor."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k584-k581-noncyclic-floor-identifiability.json"


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def family_row(t: Fraction, alpha: Fraction = Fraction(5), mu: Fraction = Fraction(1), shared_floor: Fraction = Fraction(-11)) -> dict[str, Any]:
    # C=span(e0), N=span(e1,e2), R_t=[[alpha,mu,0],[mu,t,0],[0,0,t+1]].
    shifted_cyclic = alpha - shared_floor
    shifted_noncyclic_1 = t - shared_floor
    shifted_noncyclic_2 = t + 1 - shared_floor
    shifted_two_by_two_det = shifted_cyclic * shifted_noncyclic_1 - mu**2
    shared_floor_valid = all(value > 0 for value in (shifted_cyclic, shifted_noncyclic_1, shifted_noncyclic_2, shifted_two_by_two_det))
    return {
        "parameter_t": q(t),
        "matrix": [[q(alpha), q(mu), "0"], [q(mu), q(t), "0"], ["0", "0", q(t + 1)]],
        "cyclic_compression_floor_alpha": q(alpha),
        "cyclic_noncyclic_cross_norm_mu": q(abs(mu)),
        "noncyclic_compression_floor_gamma": q(t),
        "shared_complete_sector_floor_control": q(shared_floor),
        "shared_floor_shifted_leading_minor_1": q(shifted_cyclic),
        "shared_floor_shifted_leading_minor_2": q(shifted_two_by_two_det),
        "shared_floor_shifted_third_diagonal": q(shifted_noncyclic_2),
        "shared_complete_sector_floor_valid": shared_floor_valid,
        "zero_target_positive_by_Schur_test": alpha > 0 and alpha * t - mu**2 > 0 and t + 1 > 0,
        "K473_beta_formula": f"(5+({q(t)})-sqrt((5-({q(t)}))^2+4))/2",
    }


def build() -> dict[str, Any]:
    parameters = [Fraction(-10), Fraction(0), Fraction(2), Fraction(20)]
    rows = [family_row(value) for value in parameters]
    return {
        "schema_version": "1.0",
        "result_id": "K584-K581-NONCYCLIC-FLOOR-IDENTIFIABILITY",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The logical information supplied to K494/K473 by a fixed cyclic floor, fixed cyclic/noncyclic cross norm and qualitative complete-sector semiboundedness, compared with the missing numerical floor of K581's noncyclic compression.",
        "gu_typed_objects": {
            "carrier": "one complete K162 charge sector split as C direct-sum N in the M-Hilbert coordinate",
            "pairing": "identity control for the transported positive M pairing",
            "form": "self-adjoint block form with fixed cyclic compression and fixed cross norm",
            "result": "noncyclic-floor identifiability obstruction MAP-TYPE=logical-independence",
            "target": "K500/K494 quantitative noncyclic floor gamma",
        },
        "theorem": {
            "family": "R_t=[[alpha,mu,0],[mu,t,0],[0,0,t+1]] on C=span(e0), N=span(e1,e2)",
            "fixed_data": "alpha=5 and ||P_C R_t P_N||=mu=1 for every t",
            "qualitative_semiboundedness": "every finite-dimensional R_t is semibounded, while gamma_t=inf spec(P_N R_t P_N)=t varies",
            "identifiability_conclusion": "cyclic floor alpha, cross norm mu and existence of some complete-sector lower bound do not determine any named numerical gamma",
            "sufficient_missing_input": "one named complete-sector lower witness r0 is already a valid conservative noncyclic gamma by K581; alternatively prove a sharper direct lower bound on N",
            "not_an_absence_theorem": "the actual native gamma exists by K581; only its numerical value is absent from the serialized premises",
        },
        "exact_controls": {
            "alpha": "5",
            "mu": "1",
            "parameters": [q(value) for value in parameters],
            "family_rows": rows,
            "all_rows_share_cyclic_floor": len({row["cyclic_compression_floor_alpha"] for row in rows}) == 1,
            "all_rows_share_cross_norm": len({row["cyclic_noncyclic_cross_norm_mu"] for row in rows}) == 1,
            "all_rows_semibounded": all(row["shared_complete_sector_floor_valid"] for row in rows),
            "one_explicit_shared_floor_control": "-11",
            "noncyclic_floors_are_distinct": len({row["noncyclic_compression_floor_gamma"] for row in rows}) == len(rows),
            "zero_target_outcomes_differ": len({row["zero_target_positive_by_Schur_test"] for row in rows}) > 1,
        },
        "decision": {
            "K581_existential_floor_preserved": True,
            "K498_cyclic_floor_plus_K500_cross_determine_gamma": False,
            "named_complete_sector_r0_would_supply_conservative_gamma": True,
            "current_native_named_r0_serialized": False,
            "current_native_named_gamma_emitted": False,
            "K494_target_test_released": False,
            "K473_native_beta_emitted": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Extract a named cancellation-safe complete-sector lower witness r0 from the fixed K139/K168 form and inherit it through K581, or prove a sharper direct noncyclic compression bound; cyclic alpha and leakage mu cannot replace that input.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "An exact identifiability theorem: a fixed cyclic floor, fixed cyclic/noncyclic cross norm and qualitative semiboundedness do not determine K581's numerical noncyclic floor. Any named complete-sector lower witness would nevertheless descend as a conservative gamma. The actual native floor is not disproved, and no K494 target, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["theorem"]
    controls = payload["exact_controls"]
    decision = payload["decision"]
    if len(controls["family_rows"]) != 4:
        raise AssertionError("K584 control family changed")
    if not controls["all_rows_share_cyclic_floor"] or not controls["all_rows_share_cross_norm"] or not controls["all_rows_semibounded"]:
        raise AssertionError("K584 fixed-data family failed")
    if not controls["noncyclic_floors_are_distinct"] or not controls["zero_target_outcomes_differ"]:
        raise AssertionError("K584 family does not establish numerical independence")
    if "do not determine" not in theorem["identifiability_conclusion"] or "exists" not in theorem["not_an_absence_theorem"]:
        raise AssertionError("K584 theorem boundary changed")
    if not decision["K581_existential_floor_preserved"] or decision["K498_cyclic_floor_plus_K500_cross_determine_gamma"]:
        raise AssertionError("K584 decision changed")
    if not decision["named_complete_sector_r0_would_supply_conservative_gamma"] or decision["current_native_named_r0_serialized"]:
        raise AssertionError("K584 missing-input boundary changed")
    if decision["current_native_named_gamma_emitted"] or decision["K494_target_test_released"] or decision["K473_native_beta_emitted"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K584 overclaimed downstream closure")


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
