#!/usr/bin/env python3
"""K581 compression of K462 semiboundedness to K500's noncyclic space."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k581-k500-noncyclic-semibound-inheritance.json"


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def diagonal_floor(values: list[Fraction], indices: list[int]) -> Fraction:
    if not indices:
        raise ValueError("nonempty compression required")
    return min(values[index] for index in indices)


def build() -> dict[str, Any]:
    matrix = [Fraction(-4), Fraction(2), Fraction(5)]
    full_floor = diagonal_floor(matrix, [0, 1, 2])
    noncyclic_floor = diagonal_floor(matrix, [1, 2])
    family = []
    for value in (Fraction(-100), Fraction(-3), Fraction(7)):
        diagonal = [Fraction(-1), value, value + 1]
        family.append(
            {
                "parameter": q(value),
                "complete_sector_has_a_finite_lower_bound": True,
                "noncyclic_floor": q(diagonal_floor(diagonal, [1, 2])),
            }
        )
    return {
        "schema_version": "1.0",
        "result_id": "K581-K500-NONCYCLIC-SEMIBOUND-INHERITANCE",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "K500's noncyclic closed subspace N=C^perp_M inside one complete K162 q00 or q10 sector for the fixed K139/K168 center-zero form.",
        "gu_typed_objects": {
            "carrier": "one complete K162 charge sector with cyclic closure C and N=C^perp_M",
            "pairing": "physical positive M=S* S Hilbert pairing",
            "form": "fixed K139/K168 center-zero reference form from K462",
            "result": "noncyclic semibound inheritance MAP-TYPE=form-compression",
            "target": "K500/K494 noncyclic compressed-form floor gamma",
        },
        "native_composition": {
            "complete_sector_input": "K462 proves that there exists a finite regular lower bound r0 for the fixed center-zero form on each complete K162 charge sector.",
            "noncyclic_space_input": "K500 identifies N=C^perp_M as a closed M-orthogonal subspace of that same complete sector.",
            "compression_identity": "for every n in N, <n,R_N n>=<n,R n>",
            "inherited_inequality": "R>=r0 M on H_q implies P_N R P_N>=r0 P_N M P_N on N",
            "existential_native_noncyclic_floor_proved": True,
            "named_quantitative_r0_available": False,
            "named_quantitative_gamma_available": False,
        },
        "exact_controls": {
            "complete_diagonal": [q(value) for value in matrix],
            "complete_floor": q(full_floor),
            "noncyclic_indices": [1, 2],
            "noncyclic_floor": q(noncyclic_floor),
            "inherited_complete_floor_is_valid_on_noncyclic_space": noncyclic_floor >= full_floor,
            "compression_may_improve_the_floor": noncyclic_floor > full_floor,
            "existence_without_numeric_uniformity_family": family,
            "family_noncyclic_floors_are_distinct": len({row["noncyclic_floor"] for row in family}) == len(family),
        },
        "decision": {
            "K500_noncyclic_floor_existence_emitted": True,
            "K462_complete_sector_semibound_reused_without_retraction": True,
            "named_quantitative_noncyclic_floor_emitted": False,
            "K494_target_test_released": False,
            "K473_native_beta_emitted": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Extract a cancellation-safe named lower witness r0 for the combined fixed form or a sharper direct compression bound on N, then compare that quantitative gamma with the cyclic floor and leakage in K494.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "The fixed native K162 noncyclic compression is proved semibounded because it is a closed compression of K462's semibounded complete-sector form. K462 supplies no named numerical lower witness, so this emits no quantitative gamma, K494 target test, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty or physical conclusion.",
    }


def validate(payload: dict[str, Any]) -> None:
    native = payload["native_composition"]
    controls = payload["exact_controls"]
    decision = payload["decision"]
    if not native["existential_native_noncyclic_floor_proved"] or native["named_quantitative_r0_available"] or native["named_quantitative_gamma_available"]:
        raise AssertionError("K581 native inheritance boundary changed")
    if not controls["inherited_complete_floor_is_valid_on_noncyclic_space"] or not controls["compression_may_improve_the_floor"]:
        raise AssertionError("K581 exact compression control failed")
    if len(controls["existence_without_numeric_uniformity_family"]) != 3 or not controls["family_noncyclic_floors_are_distinct"]:
        raise AssertionError("K581 nonuniformity family changed")
    if not decision["K500_noncyclic_floor_existence_emitted"] or not decision["K462_complete_sector_semibound_reused_without_retraction"]:
        raise AssertionError("K581 native decision lost")
    if decision["named_quantitative_noncyclic_floor_emitted"] or decision["K494_target_test_released"] or decision["K473_native_beta_emitted"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K581 overclaimed downstream closure")


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
