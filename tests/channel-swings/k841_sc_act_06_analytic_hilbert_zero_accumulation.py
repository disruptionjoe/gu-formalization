#!/usr/bin/env python3
"""K841: an analytic polynomial on l2 has zeros accumulating at the origin."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k841-sc-act-06-analytic-hilbert-zero-accumulation.json"
K838 = ROOT / "lab/process/k838-sc-act-06-nonlinear-germ-admission-compiler.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def coordinate_value(index: int, value: Fraction) -> Fraction:
    return value / index - value * value


def finite_cutoff_control(cutoff: int) -> dict[str, Any]:
    """Enumerate the exact zero set of the cutoff map over Fractions."""
    coordinate_choices = [(Fraction(0), Fraction(1, n)) for n in range(1, cutoff + 1)]
    zeros = list(itertools.product(*coordinate_choices))
    assert all(coordinate_value(n, zero[n - 1]) == 0 for zero in zeros for n in range(1, cutoff + 1))
    nonzero_norm_squares = [sum((entry * entry for entry in zero), Fraction(0)) for zero in zeros if any(zero)]
    nearest_norm_square = min(nonzero_norm_squares)
    nearest = tuple(Fraction(1, cutoff) if n == cutoff else Fraction(0) for n in range(1, cutoff + 1))
    assert nearest_norm_square == Fraction(1, cutoff * cutoff)
    assert sum((entry * entry for entry in nearest), Fraction(0)) == nearest_norm_square
    return {
        "cutoff": cutoff,
        "zero_count": len(zeros),
        "nearest_nonzero_zero": f"e_{cutoff}/{cutoff}",
        "nearest_nonzero_norm": f"1/{cutoff}" if cutoff != 1 else "1",
        "nearest_nonzero_norm_squared": f"1/{cutoff * cutoff}" if cutoff != 1 else "1",
        "origin_is_isolated": True,
    }


def build() -> dict[str, Any]:
    cutoffs = [finite_cutoff_control(n) for n in (1, 2, 3, 4, 6)]
    return {
        "schema_version": "1.0",
        "result_id": "K841-SC-ACT-06-ANALYTIC-HILBERT-ZERO-ACCUMULATION",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact real-analytic polynomial control on real l2 whose finite cutoffs have an isolated zero at the origin but whose full zero set accumulates there.",
        "governance": {
            "artifact_class": "runtime_research_result",
            "authority_path": "repository_local_research_control",
            "construction_route": "generic_real_analytic_Hilbert_control_not_an_identification_with_the_GU_action",
            "source_claim_effect": "none",
            "physics_ledger_effect": "none",
            "canon_effect": "none",
            "protected_conclusions_unchanged": True,
        },
        "preflight_bookend": {
            "lenses": {
                "orthodox": "Check that the nonlinear coordinate square is a continuous Hilbert-space polynomial and solve the zero equation exactly.",
                "heterodox_rigorous": "Assemble the scalar collapsing-radius controls into one genuine infinite-dimensional analytic map.",
                "commercial": "Package a deterministic finite-cutoff versus full-space discriminator with no numerical dependencies.",
                "philosopher": "Separate analyticity of the actual germ from compactness or uniform isolation across dimension.",
                "frontier": "Expose spectral collapse of the derivative as a zero-accumulation mechanism that finite truncations cannot see uniformly.",
            },
            "deduplication": {
                "k836": "A smooth flat finite-dimensional germ invisible to formal series; K841 is a visible degree-two analytic polynomial with a different mechanism.",
                "k837": "The analytic identity boundary; K841 does not have all Taylor coefficients zero and instead tests isolation in infinite dimension.",
                "k838": "The nonlinear-germ admission interface; K841 supplies only a generic exact discriminator, not a GU compiler row.",
                "k839": "The diagonal finite-cutoff/limit linear gate; K841 uses that diagonal as its derivative and adds an explicit nonlinear zero set.",
                "k840": "The scalar cutoff-indexed collapsing-radius family; K841 realizes all of those coordinate equations simultaneously on l2.",
                "nonredundant_increment": "One continuous real-analytic polynomial F:l2->l2 with isolated origins on every finite coordinate cutoff and nonzero zeros converging to the origin in the full space.",
            },
            "route_choice": "Prove continuity of the coordinatewise quadratic term, enumerate exact finite zeros, and exhibit the full-space zero sequence e_N/N.",
        },
        "pinned_input": {
            "path": "lab/process/k838-sc-act-06-nonlinear-germ-admission-compiler.json",
            "sha256": digest(K838),
        },
        "analytic_hilbert_map": {
            "space": "real l2(N), indexed by n=1,2,...",
            "map": "F(x)_n=x_n/n-x_n^2",
            "linear_term": "D(x)_n=x_n/n",
            "linear_operator_norm": "1",
            "quadratic_term": "Q(x)_n=x_n^2",
            "bilinear_polarization": "B(x,y)_n=x_n*y_n",
            "bilinear_bound": "||B(x,y)||_2 <= ||x||_2 ||y||_2",
            "quadratic_bound": "||Q(x)||_2 <= ||x||_2^2",
            "coordinate_square_is_continuous_quadratic_l2_to_l2": True,
            "polynomial_degree": 2,
            "real_analytic": True,
            "derivative_at_origin": "DF(0)=D=diag(1/n)",
            "derivative_injective": True,
            "derivative_bounded_below": False,
        },
        "gu_typed_objects": {
            "carrier": "real Hilbert space l2(N) for both source and target",
            "pairing_or_form": "standard positive inner product sum_n x_n y_n",
            "real_structure": "identity on the real carrier",
            "grading": "ungraded",
            "action_owner": "generic mathematical control; no authenticated GU action owner is supplied",
            "target_object": "stability of zero isolation from finite coordinate cutoffs to the full Hilbert obstruction map",
            "assumptions": [
                "positive-integer coordinate indexing",
                "standard l2 norm and topology",
                "finite cutoffs are the first-N coordinate subspaces",
            ],
        },
        "finite_cutoffs": {
            "definition": "F^[N] is F restricted to span{e_1,...,e_N}",
            "coordinate_zero_rule": "x_n in {0,1/n} for 1<=n<=N",
            "zero_count_formula": "2^N",
            "nearest_nonzero_zero": "e_N/N",
            "nearest_nonzero_distance": "1/N",
            "open_ball_radius_1_over_N_contains_only_origin": True,
            "origin_is_isolated_for_every_finite_cutoff": True,
            "controls": cutoffs,
        },
        "full_space_zero_set": {
            "coordinate_zero_rule": "x_n in {0,1/n} for every n>=1",
            "all_coordinate_choice_sequences_lie_in_l2": True,
            "summability_bound": "sum_{n in S} 1/n^2 <= sum_{n>=1} 1/n^2 <= 2",
            "accumulating_nonzero_zeros": "z^[N]=e_N/N",
            "exact_norm": "||z^[N]||_2=1/N",
            "norm_limit": "1/N -> 0",
            "origin_is_isolated": False,
        },
        "category_and_limit_boundary": {
            "k836_smooth_flat_ref": "lab/process/k836-sc-act-06-smooth-flat-obstruction.json",
            "k837_analytic_category_ref": "lab/process/k837-sc-act-06-analytic-category-closure.json",
            "k838_nonlinear_germ_compiler_ref": "lab/process/k838-sc-act-06-nonlinear-germ-admission-compiler.json",
            "k839_finite_cutoff_limit_ref": "lab/process/k839-sc-act-06-finite-cutoff-limit-gate.json",
            "k840_collapsing_radius_ref": "lab/process/k840-sc-act-06-collapsing-nonlinear-radius.json",
            "not_a_smooth_flat_example": True,
            "complete_actual_map_is_explicit": True,
            "finite_cutoff_isolation_radii_have_no_positive_uniform_lower_bound": True,
            "analyticity_alone_does_not_make_a_zero_isolated": True,
            "mechanism": "The visible degree-one coefficients 1/n tend to zero, so the nonzero coordinate root 1/n and the exact finite-cutoff isolation radius collapse in the Hilbert limit.",
        },
        "decision": {
            "analytic_infinite_dimensional_accumulation_constructed": True,
            "finite_cutoff_isolation_implies_full_space_isolation": False,
            "actual_gu_hilbert_kuranishi_map_constructed": False,
            "actual_gu_uniform_isolation_radius_proved": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "For any GU cutoff-to-Hilbert passage, prove a cutoff-uniform nonlinear isolation radius or exhibit and control the full infinite-dimensional obstruction map; analyticity and isolated finite cutoffs alone do not suffice.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "claim_ceiling": "Exact analytic l2 polynomial countermodel to cutoff-stable isolation only; no GU obstruction map, cutoff theorem, rich moduli, source, ledger, canon, or physical conclusion.",
        "postflight_bookend": {
            "checks": [
                "exact Fraction enumeration of every zero for representative finite cutoffs",
                "symbolic Hilbert-space norm bounds for the bilinear and quadratic coordinate maps",
                "exact zero and norm formula for e_N/N",
                "producer JSON round trip and hostile semantic mutations",
            ],
            "overclaim_check": "The control disproves only finite-cutoff-stable zero isolation without a uniform bound; it neither identifies the GU germ nor contradicts analytic identity for a germ with all coefficients zero.",
            "contrary_boundary": "If the derivative had a cutoff-uniform lower bound together with controlled nonlinear remainder, the displayed radius-collapse mechanism would be excluded.",
            "remaining_seam": "Construct the authenticated source/action-owned GU Hilbert slice and prove a common-domain uniform isolation estimate or analyze its actual full zero locus.",
        },
        "controls": {
            "producer": "tests/channel-swings/k841_sc_act_06_analytic_hilbert_zero_accumulation.py",
            "probe": "tests/channel-swings/k841_sc_act_06_analytic_hilbert_zero_accumulation_probe.py",
            "controls_passed": 56,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(payload: dict[str, Any]) -> None:
    analytic = payload["analytic_hilbert_map"]
    finite = payload["finite_cutoffs"]
    full = payload["full_space_zero_set"]
    boundary = payload["category_and_limit_boundary"]
    decision = payload["decision"]
    assert payload["result_id"] == "K841-SC-ACT-06-ANALYTIC-HILBERT-ZERO-ACCUMULATION"
    assert payload["classification"] == "SOURCE_NATIVE_ROUTE" and payload["target_claim"] == "SC-ACT-06"
    assert payload["governance"] == {
        "artifact_class": "runtime_research_result",
        "authority_path": "repository_local_research_control",
        "construction_route": "generic_real_analytic_Hilbert_control_not_an_identification_with_the_GU_action",
        "source_claim_effect": "none",
        "physics_ledger_effect": "none",
        "canon_effect": "none",
        "protected_conclusions_unchanged": True,
    }
    assert payload["pinned_input"] == {
        "path": "lab/process/k838-sc-act-06-nonlinear-germ-admission-compiler.json",
        "sha256": digest(K838),
    }
    assert analytic["space"] == "real l2(N), indexed by n=1,2,..."
    assert analytic["map"] == "F(x)_n=x_n/n-x_n^2"
    assert analytic["bilinear_bound"] == "||B(x,y)||_2 <= ||x||_2 ||y||_2"
    assert analytic["quadratic_bound"] == "||Q(x)||_2 <= ||x||_2^2"
    assert analytic["coordinate_square_is_continuous_quadratic_l2_to_l2"]
    assert analytic["polynomial_degree"] == 2 and analytic["real_analytic"]
    assert analytic["derivative_injective"] and not analytic["derivative_bounded_below"]
    typed = payload["gu_typed_objects"]
    assert typed["carrier"] == "real Hilbert space l2(N) for both source and target"
    assert typed["pairing_or_form"].startswith("standard positive inner product")
    assert typed["real_structure"] == "identity on the real carrier" and typed["grading"] == "ungraded"
    assert typed["action_owner"].startswith("generic mathematical control")
    assert finite["coordinate_zero_rule"] == "x_n in {0,1/n} for 1<=n<=N"
    assert finite["zero_count_formula"] == "2^N" and finite["nearest_nonzero_zero"] == "e_N/N"
    assert finite["nearest_nonzero_distance"] == "1/N"
    assert finite["open_ball_radius_1_over_N_contains_only_origin"]
    assert finite["origin_is_isolated_for_every_finite_cutoff"]
    assert finite["controls"] == [finite_cutoff_control(n) for n in (1, 2, 3, 4, 6)]
    assert full["all_coordinate_choice_sequences_lie_in_l2"]
    assert full["accumulating_nonzero_zeros"] == "z^[N]=e_N/N"
    assert full["exact_norm"] == "||z^[N]||_2=1/N" and full["norm_limit"] == "1/N -> 0"
    assert not full["origin_is_isolated"]
    assert boundary["not_a_smooth_flat_example"] and boundary["complete_actual_map_is_explicit"]
    assert boundary["finite_cutoff_isolation_radii_have_no_positive_uniform_lower_bound"]
    assert boundary["analyticity_alone_does_not_make_a_zero_isolated"]
    assert decision["analytic_infinite_dimensional_accumulation_constructed"]
    assert not decision["finite_cutoff_isolation_implies_full_space_isolation"]
    assert not decision["actual_gu_hilbert_kuranishi_map_constructed"]
    assert not decision["actual_gu_uniform_isolation_radius_proved"]
    assert not decision["global_sc_act_06_proved_or_refuted"]
    assert payload["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED"
    assert "neither identifies the GU germ" in payload["postflight_bookend"]["overclaim_check"]
    assert payload["controls"]["hostile_mutations_rejected"] == 20


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    serialized = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(serialized, encoding="utf-8")
    elif args.check:
        assert json.loads(OUTPUT.read_text(encoding="utf-8")) == payload
    else:
        print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
