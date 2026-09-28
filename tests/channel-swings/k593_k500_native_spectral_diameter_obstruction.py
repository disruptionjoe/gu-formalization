#!/usr/bin/env python3
"""K593 native K172 level-one spectral-diameter obstruction."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k593-k500-native-spectral-diameter-obstruction.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K172 = load("k172_for_k593", "k172_continuum_first_block_graph_tail.py")


def lower_bound(e: Fraction) -> float:
    if e <= 257:
        raise ValueError("the explicit logarithmic lower bound requires e>257")
    return math.log(float(e / 257)) / (2 * math.pi)


def build() -> dict:
    k580 = json.loads((ROOT / "lab/process/k580-k578-native-first-level-pairwise-energy.json").read_text())
    samples = []
    previous = -1.0
    for e in (Fraction(514), Fraction(1028), Fraction(2056), Fraction(4112)):
        value = lower_bound(e)
        if value <= previous:
            raise AssertionError("lower-bound samples did not increase")
        previous = value
        samples.append({"e": str(e), "D_lower": f"{value:.15g}"})

    sectors = []
    for seed, multiplicity in (("vacuum", 1), ("one_impurity", 2)):
        native = K172.first_block(seed)
        k580_row = next(row for row in k580["native_sector_pairwise_energy"] if row["seed"] == seed)
        sectors.append({
            "seed": seed,
            "charge": native["charge"],
            "multiplicity": multiplicity,
            "actual_action_on_cyclic_profile": native["W1_g1_per_component"],
            "multiplier_formula": f"w_{multiplicity}(p)=256-{multiplicity}*D_256(omega(p))",
            "multiplication_spectrum": f"(-infinity, 256-{multiplicity}*D_256(1)]",
            "spectral_diameter": "infinity",
            "K580_weighted_leakage_square_upper_exact": k580_row["normal_leakage_square_upper_exact"],
            "weighted_leakage_finite": True,
        })

    return {
        "schema_version": "1.0",
        "result_id": "K593-K500-NATIVE-SPECTRAL-DIAMETER-OBSTRUCTION",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The actual K172 bath-number-one q00 and q10 normal multipliers used by K580, tested against K591's finite spectral-diameter applicability condition.",
        "gu_typed_objects": {
            "carrier": "K162 q00 or q10 bath-number-one regular-coordinate block",
            "pairing": "positive L2(dp) pairing and K580's normalized profile measure",
            "form": "self-adjoint K172 multiplication block W_1",
            "real_structure": "real scalar multiplication in momentum coordinates",
            "grading": "bath number one and fixed charge",
            "action_owner": "repository-supplied K139/K172 conditional operator; no source/GU action selection",
            "result": "native spectral-diameter applicability obstruction MAP-TYPE=multiplication-spectrum",
            "target": "K591 finite-width route to complete K500 leakage",
        },
        "native_kernel": {
            "definition": "D_256(e)=int_R e/((omega(k)+256)(omega(k)+256+e)) dk/(2*pi), omega(k)=sqrt(1+k^2)",
            "strict_monotonicity": "dD_256/de=int_R 1/(omega(k)+256+e)^2 dk/(2*pi)>0",
            "lower_bound": "for e>257, D_256(e)>=(1/(2*pi))*log(e/257)",
            "lower_bound_derivation": "on 0<=k<=e-257, omega(k)+256<=k+257<=e, so e/(a(a+e))>=1/(2a)>=1/(2(k+257)); use evenness",
            "upper_bound_reused": "D_256(e)<=(1/pi)*log(1+e/256) from K172",
            "unbounded": True,
            "continuous": True,
            "sampled_lower_bounds": samples,
        },
        "native_level_one_sectors": sectors,
        "theorem": {
            "essential_range": "because omega(p) covers [1,infinity), D_256 is continuous, strictly increasing and unbounded, w_m(p)=256-mD_256(omega(p)) has essential range (-infinity,256-mD_256(1)]",
            "spectral_consequence": "the self-adjoint multiplication operator W_1 has infinite spectral diameter in both native sectors",
            "K591_applicability": "K591's finite-width sufficient route cannot apply to the actual native family because it already fails at bath level one",
            "weighted_vector_boundary": "infinite operator spectral width does not imply infinite leakage on h: K172 proves ||D_256 h||<=1/16 and K580 gives finite weighted variances",
        },
        "decision": {
            "actual_native_level_one_tested": True,
            "finite_spectral_diameter_route_survives": False,
            "K591_abstract_theorem_retracted": False,
            "K580_finite_weighted_leakage_retracted": False,
            "complete_K500_uniform_leakage_emitted": False,
            "native_noncyclic_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
            "route_effect": "Retire the native finite-spectral-width route. Continue with K583's directly normalized antisymmetrized action vectors or an equivalent weighted pairwise estimate; unbounded off-support spectrum is irrelevant if those vector ratios are uniformly finite.",
            "next_exact_input": "Derive a bath-level-uniform bound on ||W_n v_n tensor v_n-v_n tensor W_n v_n||^2/(2||v_n||^4), retaining K177 exchange terms, and separately serialize the complete-sector/noncyclic numerical floor.",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Test K591 on K172's actual first native multiplier before attempting higher-level spectral enclosures; one infinite-width block kills a uniform finite-width route.",
            "retrieval_collision_result": "K172 records a logarithmic pointwise upper and K580 a finite weighted variance, but neither proves the matching logarithmic lower or identifies the multiplication spectrum.",
            "strongest_alternative": "The K583 vector-specific tensor ratio can remain finite for an unbounded operator and is the required successor rather than a wider spectral search.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling infinite spectral diameter infinite K500 leakage, or treating the conditional operator as source/GU selected.",
            "strongest_contrary_construction": "K580 is the native contrary construction: the same unbounded multiplier has a finite h-weighted variance at level one.",
            "weakest_reproducibility_seam": "The all-level direct vector ratio remains open; K593 kills only finite spectral width and does not extrapolate K580 unchanged through exchange levels.",
        },
        "claim_ceiling": "Exact native applicability obstruction: the K172 level-one multipliers in both q00 and q10 have spectrum unbounded below because D_256(e)>=(2*pi)^-1 log(e/257) for e>257. Their spectral diameter is already infinite, so K591's finite-width sufficient route cannot yield a native uniform K500 bound. K591's abstract theorem and K580's finite profile-weighted variances remain valid; the direct K583 action-vector route and the separate noncyclic floor remain open. No K473/K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict) -> None:
    kernel = payload["native_kernel"]
    sectors = payload["native_level_one_sectors"]
    decision = payload["decision"]
    if not kernel["unbounded"] or not kernel["continuous"] or len(kernel["sampled_lower_bounds"]) != 4:
        raise AssertionError("native kernel conclusion changed")
    values = [float(row["D_lower"]) for row in kernel["sampled_lower_bounds"]]
    if not all(b > a for a, b in zip(values, values[1:])):
        raise AssertionError("logarithmic lower controls failed")
    if [row["multiplicity"] for row in sectors] != [1, 2] or any(row["spectral_diameter"] != "infinity" for row in sectors):
        raise AssertionError("native sector spectrum changed")
    if any(not row["weighted_leakage_finite"] or Fraction(row["K580_weighted_leakage_square_upper_exact"]) <= 0 for row in sectors):
        raise AssertionError("weighted finite boundary changed")
    if not decision["actual_native_level_one_tested"] or decision["finite_spectral_diameter_route_survives"]:
        raise AssertionError("native route decision changed")
    if decision["K591_abstract_theorem_retracted"] or decision["K580_finite_weighted_leakage_retracted"]:
        raise AssertionError("predecessor result was retracted")
    if decision["complete_K500_uniform_leakage_emitted"] or decision["native_noncyclic_floor_emitted"] or decision["K473_released"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K593 overclaimed downstream closure")


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
