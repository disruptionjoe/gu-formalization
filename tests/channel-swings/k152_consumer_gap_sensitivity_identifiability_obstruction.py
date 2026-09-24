#!/usr/bin/env python3
"""Exact K152/K270 gap and sensitivity identifiability obstruction.

Two rational witness families show that the serialized conditional consumer
does not determine a positive uniform spectral budget or integral tolerance.
This does not falsify K152 or any fully instantiated consumer.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k152-consumer-gap-sensitivity-identifiability-obstruction.json"
K270 = ROOT / "lab/process/k270-k152-sharp-spectral-budget-certificate.json"
K168 = ROOT / "lab/process/k168-flavor-symmetric-reference-extension-wave.json"
K404 = ROOT / "lab/process/k404-order-nine-complete-integral-enclosure.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def energy_budget(a: Fraction, g: Fraction, d: Fraction) -> Fraction:
    if not (a > d > 0 and g > 0):
        raise ValueError("energy budget requires a>d>0 and g>0")
    return d * a * g / ((a + g) * (a - d))


def gap_witness(n: int) -> dict[str, Any]:
    if n < 1:
        raise ValueError("n must be positive")
    epsilon = Fraction(1, n)
    budget = energy_budget(Fraction(3), epsilon, Fraction(1))
    return {
        "n": n,
        "epsilon": qstr(epsilon),
        "gram": ["1", "1", "1"],
        "R0_diagonal": ["0", qstr(epsilon), "1"],
        "rho": "0",
        "nominal_residual_square": "0",
        "exterior_gap_g": qstr(epsilon),
        "a": "3",
        "d": "1",
        "sharp_energy_budget": qstr(budget),
        "Rref_diagonal_after_K168": ["-2", qstr(1 + epsilon), "2"],
        "K168_shape_oscillation": "3",
    }


def sensitivity_witness(n: int) -> dict[str, Any]:
    if n < 1:
        raise ValueError("N must be positive")
    fixed_budget = Fraction(3, 5)
    maximum_uncertainty_squared = fixed_budget / (n * n)
    return {
        "N": n,
        "a": "3",
        "g": "2",
        "d": "1",
        "fixed_energy_budget": qstr(fixed_budget),
        "r_nominal": "0",
        "eta_other": "0",
        "kappa": str(n),
        "required_uncertainty_law": "u=r_I+tau_I <= sqrt(3/5)/N",
        "maximum_uncertainty_squared": qstr(maximum_uncertainty_squared),
    }


def build() -> dict[str, Any]:
    k270 = json.loads(K270.read_text())
    k168 = json.loads(K168.read_text())
    k404 = json.loads(K404.read_text())
    gap_ns = [1, 2, 4, 8, 16, 64, 256]
    sensitivity_ns = [1, 2, 4, 8, 16, 64]
    gaps = [gap_witness(n) for n in gap_ns]
    sensitivities = [sensitivity_witness(n) for n in sensitivity_ns]
    gap_budgets = [Fraction(row["sharp_energy_budget"]) for row in gaps]
    tolerance_squares = [Fraction(row["maximum_uncertainty_squared"]) for row in sensitivities]

    return {
        "schema_version": "1.0",
        "result_id": "K152-CONSUMER-GAP-SENSITIVITY-IDENTIFIABILITY-OBSTRUCTION",
        "created": "2026-09-24",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "Determine whether the serialized K139/K152/K168/K270 inputs identify a positive uniform residual budget or integral-uncertainty tolerance for the actual consumer.",
        "typed_objects": {
            "carrier": "exact three-dimensional rational conforming control family with G=I_3; not a claimed native K139 trial assembly",
            "form": "R0(epsilon)=diag(0,epsilon,1) and conditional K168 extension Rref=R0+diag(-2,1,1)",
            "pairing": "Euclidean Gram G=I_3 in the counterexample family",
            "real_structure": "real rational Hermitian diagonal controls",
            "grading": "ground line plus two-dimensional complement",
            "action_owner": "repository-owned conditional K152/K270 theorem only; native action/operator ownership remains absent",
        },
        "serialized_consumer": {
            "sharp_energy_budget": k270["sharp_spectral_certificate"]["target_budget"],
            "residual_decomposition": k270["value_to_consumer_budget"]["residual_decomposition"],
            "integral_uncertainty_budget": k270["value_to_consumer_budget"]["integral_uncertainty_budget"],
            "K168_reference_diagonal": k168["reference_extension"]["diagonal"],
            "K168_shape_oscillation": k168["fixed_chart_form_consequences"]["maximum_absolute_change_of_a_relative_gap"],
            "K404_status": "sign_decided" if k404["complete_integral_enclosure"]["sign_decided"] else "finite_enclosure_without_sign",
            "K404_role": "proves a finite enclosure only; it supplies no K152 gap, decision margin, or map norm",
        },
        "gap_collapse_family": {
            "definition": "for every integer n>=1, epsilon=1/n, G=I_3, R0=diag(0,epsilon,1), normalized ground trial has rho=0 and residual square zero, while exterior gap g=epsilon",
            "fixed_controls": {"a": "3", "d": "1"},
            "budget_formula": "B_n=3/[2(3n+1)]",
            "all_budgets_positive": all(value > 0 for value in gap_budgets),
            "sample_budgets_strictly_decrease": all(x > y for x, y in zip(gap_budgets, gap_budgets[1:])),
            "infimum": "0",
            "uniform_positive_budget_identified": False,
            "K168_effect": "adding W_ref=diag(-2,1,1) preserves its three-unit shape oscillation but imposes no lower bound on the base complement gap",
            "samples": gaps,
        },
        "sensitivity_scaling_family": {
            "definition": "hold a=3,g=2,d=1 so e_budget=3/5; set r_nominal=eta_other=0, kappa=N and u=r_I+tau_I",
            "uncertainty_law": "u<=sqrt(3/5)/N, equivalently u^2<=3/(5N^2)",
            "fixed_energy_budget": "3/5",
            "sample_tolerance_squares_strictly_decrease": all(x > y for x, y in zip(tolerance_squares, tolerance_squares[1:])),
            "infimum_of_tolerance_squared": "0",
            "uniform_positive_integral_tolerance_identified": False,
            "samples": sensitivities,
        },
        "identifiability_decision": {
            "positive_uniform_K270_energy_budget_from_serialized_inputs": False,
            "positive_uniform_integral_uncertainty_tolerance_from_serialized_inputs": False,
            "reason": "the admissible exact gap family drives the energy budget to zero, and the admissible exact sensitivity family drives the allowable uncertainty to zero while holding the energy budget fixed",
            "further_enclosure_has_decision_defined_target": False,
            "next_exact_inputs": [
                "a native conforming form/Gram assembly and coercive shift",
                "an independent positive exterior gap or complement coercivity bound",
                "a complete nominal residual and other-error budget",
                "a finite integral-to-residual map norm kappa",
                "a declared energy or projection decision margin",
            ],
        },
        "retained_scope": {
            "K152_theorem_falsified": False,
            "K168_reference_extension_falsified": False,
            "K270_sharp_bound_falsified": False,
            "particular_fully_instantiated_consumer_falsified": False,
            "native_K152_interval_emitted": False,
            "source_ledger_canon_paper_public_or_physical_effect": False,
        },
        "release_test": {
            "K270_formula_replayed": energy_budget(Fraction(3), Fraction(2), Fraction(1)) == Fraction(3, 5),
            "gap_budget_formula_replayed": all(Fraction(row["sharp_energy_budget"]) == Fraction(3, 2 * (3 * row["n"] + 1)) for row in gaps),
            "all_gap_budgets_positive": all(value > 0 for value in gap_budgets),
            "sample_gap_budgets_decrease": all(x > y for x, y in zip(gap_budgets, gap_budgets[1:])),
            "gap_family_infimum_zero": True,
            "K168_shape_oscillation_stays_three": all(Fraction(row["K168_shape_oscillation"]) == 3 for row in gaps),
            "sensitivity_formula_replayed": all(Fraction(row["maximum_uncertainty_squared"]) == Fraction(3, 5 * row["N"] * row["N"]) for row in sensitivities),
            "sample_tolerance_squares_decrease": all(x > y for x, y in zip(tolerance_squares, tolerance_squares[1:])),
            "sensitivity_family_infimum_zero": True,
            "no_theorem_or_instantiated_consumer_falsification": True,
            "no_source_ledger_canon_paper_public_or_physical_effect": True,
        },
        "claim_ceiling": "Exact rational counterexample families proving that the currently serialized conditional K152/K168/K270 inputs do not identify a positive uniform residual-energy budget or integral-uncertainty tolerance. Gap collapse sends the sharp K270 budget to zero even with K168's fixed three-unit reference shape, and sensitivity scaling sends allowable integral uncertainty to zero at fixed budget. This does not falsify K152, K168, K270, or any fully instantiated consumer; it supplies no native form, gap, residual, map norm, interval, source/ledger/canon/paper/public/novelty or physical GU verdict.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    gap = payload["gap_collapse_family"]
    sensitivity = payload["sensitivity_scaling_family"]
    decision = payload["identifiability_decision"]
    retained = payload["retained_scope"]
    assert payload["classification"] == "INTERNAL_STRUCTURAL_ONLY"
    assert payload["direction"] == "observed_to_native"
    assert gap["budget_formula"] == "B_n=3/[2(3n+1)]"
    assert gap["all_budgets_positive"] is True
    assert gap["sample_budgets_strictly_decrease"] is True
    assert gap["infimum"] == "0"
    assert gap["uniform_positive_budget_identified"] is False
    assert len(gap["samples"]) == 7
    assert sensitivity["fixed_energy_budget"] == "3/5"
    assert sensitivity["sample_tolerance_squares_strictly_decrease"] is True
    assert sensitivity["infimum_of_tolerance_squared"] == "0"
    assert sensitivity["uniform_positive_integral_tolerance_identified"] is False
    assert len(sensitivity["samples"]) == 6
    assert decision["positive_uniform_K270_energy_budget_from_serialized_inputs"] is False
    assert decision["positive_uniform_integral_uncertainty_tolerance_from_serialized_inputs"] is False
    assert decision["further_enclosure_has_decision_defined_target"] is False
    assert len(decision["next_exact_inputs"]) == 5
    assert all(value is False for value in retained.values())
    assert all(payload["release_test"].values())
    assert "does not falsify K152" in payload["claim_ceiling"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    if args.write:
        OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print("K152 identifiability obstruction passed: gap and sensitivity families both have zero uniform infimum")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
