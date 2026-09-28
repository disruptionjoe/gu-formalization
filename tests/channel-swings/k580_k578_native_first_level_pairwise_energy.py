#!/usr/bin/env python3
"""K580 actual q00/q10 first-level pairwise-energy instantiation."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k580-k578-native-first-level-pairwise-energy.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K172 = load("k172_for_k580", "k172_continuum_first_block_graph_tail.py")


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def sector(seed: str) -> dict[str, Any]:
    block = K172.first_block(seed)
    h_lower = Fraction(block["profile_norm_interval"][0])
    multiplicity = int(block["normal_ordered_self_energy_multiplicity_per_component"])
    correction = Fraction(block["D_h_norm_upper_used"])
    d_lower = Fraction(14, 11 * 515 * 517)
    second_moment_upper = correction**2 / h_lower**2
    variance_upper = second_moment_upper - d_lower**2
    if variance_upper <= 0:
        raise AssertionError("K580 strict variance upper left its positive branch")
    pairwise_energy_upper = multiplicity**2 * variance_upper
    k502_square = multiplicity**2 * second_moment_upper
    return {
        "seed": seed,
        "charge": block["charge"],
        "bath_level": 1,
        "components": block["n1_transition_components"],
        "actual_profile_measure": "dmu_h(p)=|h(p)|^2 dp / ||h||^2",
        "actual_multiplier": f"256-{multiplicity}*D_256(omega(p))",
        "pairwise_kernel": f"{multiplicity}^2*(D_256(omega(p))-D_256(omega(q)))^2/2",
        "D_multiplicity": multiplicity,
        "D_pointwise_lower_exact": q(d_lower),
        "D_second_moment_upper_exact": q(second_moment_upper),
        "D_variance_upper_exact": q(variance_upper),
        "normal_leakage_square_upper_exact": q(pairwise_energy_upper),
        "K502_second_moment_square_upper_exact": q(k502_square),
        "strict_improvement_exact": q(k502_square - pairwise_energy_upper),
        "strictly_improves_K502": pairwise_energy_upper < k502_square,
        "uniform_all_level_bound": False,
    }


def build() -> dict[str, Any]:
    rows = [sector("vacuum"), sector("one_impurity")]
    return {
        "schema_version": "1.0",
        "result_id": "K580-K578-NATIVE-FIRST-LEVEL-PAIRWISE-ENERGY",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The actual K172 bath-number-one q00 and q10 cyclic measures and normal-action multipliers in the fixed K139 chart.",
        "gu_typed_objects": {
            "carrier": "K162 q00 or q10 bath-number-one regular-coordinate block",
            "pairing": "normalized positive profile measure induced by h(p)",
            "form": "self-adjoint K172 normal action W_1",
            "result": "native pairwise leakage energy MAP-TYPE=orthogonal-block-norm",
            "target": "the level-one K500 cyclic/noncyclic cross block",
        },
        "pointwise_lower_certificate": {
            "D_definition": "D_256(e)=int_R e/((omega(k)+256)(omega(k)+256+e)) dk/(2*pi)",
            "restriction": "on |k|<=1, omega(k)<=sqrt(2)<3/2; for e=omega(p)>=1 the integrand increases in e",
            "pi_bound": "pi<22/7",
            "result": "D_256(omega(p))>=14/(11*515*517) for every p",
            "strict_positive_mean": True,
        },
        "pairwise_theorem": {
            "K578_specialization": "lambda_1^2=(m^2/2) int int (D(p)-D(q))^2 dmu_h(p)dmu_h(q)=m^2 Var_mu_h(D)",
            "scalar_256_cancels": True,
            "identical_q00_components_cancel_from_normalization": True,
            "strict_upper": "Var(D)=E[D^2]-E[D]^2 <= ||D h||^2/||h||^2-d0^2",
            "K502_relation": "K502 used only Var(D)<=E[D^2]; the positive d0 term is a strict certified improvement on the same actual block.",
        },
        "native_sector_pairwise_energy": rows,
        "decision": {
            "actual_q00_q10_pairwise_measures_instantiated": True,
            "actual_q00_q10_first_level_pairwise_energy_upper_emitted": True,
            "strictly_sharper_than_K502": all(row["strictly_improves_K502"] for row in rows),
            "native_uniform_all_level_variance_emitted": False,
            "complete_K500_uniform_leakage_emitted": False,
            "noncyclic_floor_emitted": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Derive the actual higher-level q00/q10 normal-action pairwise kernels and a bound uniform in bath number; the level-one measure now serves as the exact base case, not as the supremum.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "A rigorous direct K578 pairwise-energy instantiation for the actual q00/q10 bath-number-one blocks, strictly sharper than K502 by a positive mean-square subtraction. It is not an all-level K500 bound, noncyclic floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty or physical conclusion.",
    }


def validate(payload: dict[str, Any]) -> None:
    cert = payload["pointwise_lower_certificate"]
    rows = payload["native_sector_pairwise_energy"]
    if not cert["strict_positive_mean"] or len(rows) != 2:
        raise AssertionError("K580 base certificate changed")
    if [row["charge"] for row in rows] != [[0, 0], [1, 0]] or [row["D_multiplicity"] for row in rows] != [1, 2]:
        raise AssertionError("K580 native sectors changed")
    if any(Fraction(row["normal_leakage_square_upper_exact"]) <= 0 for row in rows):
        raise AssertionError("K580 lost a positive upper")
    if any(Fraction(row["strict_improvement_exact"]) <= 0 or not row["strictly_improves_K502"] for row in rows):
        raise AssertionError("K580 strict improvement failed")
    decision = payload["decision"]
    if not decision["actual_q00_q10_pairwise_measures_instantiated"] or not decision["actual_q00_q10_first_level_pairwise_energy_upper_emitted"]:
        raise AssertionError("K580 native instantiation lost")
    if decision["native_uniform_all_level_variance_emitted"] or decision["complete_K500_uniform_leakage_emitted"] or decision["noncyclic_floor_emitted"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K580 overclaimed downstream closure")


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
