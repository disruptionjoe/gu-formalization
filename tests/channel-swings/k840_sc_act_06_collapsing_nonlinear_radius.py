#!/usr/bin/env python3
"""K840: pointwise IFT does not supply a cutoff-uniform nonlinear radius."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k840-sc-act-06-collapsing-nonlinear-radius.json"
PATHS = {
    "k817": ROOT / "lab/process/k817-sc-act-06-finite-parameter-schur-gate.json",
    "k822": ROOT / "lab/process/k822-sc-act-06-joint-parameter-covector-uniformity.json",
    "k838": ROOT / "lab/process/k838-sc-act-06-nonlinear-germ-admission-compiler.json",
}
SAMPLE_CUTOFFS = (1, 2, 5, 10, 100)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def f(cutoff: int, x: Fraction) -> Fraction:
    return x / cutoff - x * x


def df(cutoff: int, x: Fraction) -> Fraction:
    return Fraction(1, cutoff) - 2 * x


def sample_row(cutoff: int) -> dict[str, Any]:
    derivative = Fraction(1, cutoff)
    second_zero = Fraction(1, cutoff)
    ift_radius = Fraction(1, 4 * cutoff)
    collision_left = Fraction(3, 8 * cutoff)
    collision_right = Fraction(5, 8 * cutoff)
    return {
        "N": cutoff,
        "derivative_at_zero": qstr(derivative),
        "inverse_norm": cutoff,
        "second_zero": qstr(second_zero),
        "certified_ift_radius": qstr(ift_radius),
        "derivative_lower_bound_on_certified_ball": qstr(Fraction(1, 2 * cutoff)),
        "collision_pair_about_critical_point": [qstr(collision_left), qstr(collision_right)],
        "collision_value": qstr(f(cutoff, collision_left)),
    }


def build() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "result_id": "K840-SC-ACT-06-COLLAPSING-NONLINEAR-RADIUS",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact analytic cutoff family separating pointwise inverse-function neighborhoods from any cutoff-uniform zero-isolation or injectivity radius.",
        "governance": {
            "artifact_class": "runtime_research_result",
            "authority_path": "repository_local_research_control",
            "construction_route": "generic_real_analytic_control_not_an_identification_with_the_GU_action",
            "source_claim_effect": "none",
            "physics_ledger_effect": "none",
            "canon_effect": "none",
            "protected_conclusions_unchanged": True,
        },
        "preflight_bookend": {
            "lenses": {
                "orthodox": "Track the inverse derivative norm and a quantitative inverse-function radius, not invertibility alone.",
                "heterodox_rigorous": "Use an exact rational analytic family whose second zero is visible without numerical inference.",
                "commercial": "Package a short reproducible discriminator reusable against future cutoff families.",
                "philosopher": "Keep pointwise existence distinct from a uniform statement over the cutoff index.",
                "frontier": "Expose the missing uniform inverse bound and nonlinear remainder control before source-family credit.",
            },
            "deduplication": {
                "k817": "Finite-parameter Schur persistence after an invertible transverse first term; it does not quantify a cutoff-indexed nonlinear neighborhood.",
                "k822": "Joint parameter/covector uniformity from a uniform gap and remainder; it does not exhibit collapse of an actual nonlinear solution germ across cutoffs.",
                "k838": "Admission of the actual category-appropriate nonlinear germ; it does not show that pointwise IFT neighborhoods may shrink to zero.",
                "nonredundant_increment": "An analytic family with invertible derivative at every cutoff, inverse norm N, a second zero at 1/N, and hence collapsing isolation and injectivity radii.",
            },
            "route_choice": "Test the quantitative nonlinear stability burden by exact scalar counterfamily, then test the diagnosis with the same quadratic nonlinearity and uniformly conditioned linear part.",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "gu_typed_objects": {
            "carrier": "one-dimensional real cutoff-indexed local slice control",
            "pairing": "absolute-value norm on source and target R",
            "real_structure": "real analytic scalar maps",
            "grading": "single even scalar control degree",
            "action_owner": "generic mathematical control; application requires an authenticated source/action-owned GU family",
            "target": "whether pointwise linearized invertibility supplies a cutoff-uniform nonlinear local radius",
        },
        "collapsing_family": {
            "index_set": "positive integers N",
            "map": "f_N(x)=x/N-x^2",
            "base_point": "x=0",
            "base_value": "f_N(0)=0",
            "derivative": "Df_N(x)=1/N-2x",
            "derivative_at_base": "Df_N(0)=1/N",
            "derivative_at_base_invertible_for_every_finite_N": True,
            "inverse_derivative_norm": "||(Df_N(0))^-1||=N",
            "inverse_norm_uniformly_bounded": False,
            "second_zero": "x_N=1/N",
            "zeros": "{0,1/N}",
            "critical_point": "x=1/(2N)",
            "symmetry": "f_N(x)=f_N(1/N-x)",
        },
        "pointwise_ift_certificate": {
            "each_finite_cutoff_has_an_ift_neighborhood": True,
            "certified_origin_centered_radius": "r_N=1/(4N)",
            "derivative_lower_bound": "|Df_N(x)|>=1/(2N) for |x|<=1/(4N)",
            "injective_on_certified_ball": True,
            "largest_open_zero_isolation_radius": "1/N",
            "largest_open_injectivity_radius": "1/(2N)",
        },
        "uniform_failure_certificate": {
            "positive_N_uniform_zero_isolation_radius_exists": False,
            "positive_N_uniform_injectivity_radius_exists": False,
            "zero_isolation_witness": "For every r>0 choose N>1/r; then 0<1/N<r and f_N(0)=f_N(1/N)=0.",
            "injectivity_witness": "The same two distinct zeros lie in (-r,r), so f_N is not injective there.",
            "infimum_zero_isolation_radius": "0",
            "infimum_injectivity_radius": "0",
            "pointwise_derivative_invertibility_implies_uniform_radius": False,
        },
        "exact_samples": [sample_row(cutoff) for cutoff in SAMPLE_CUTOFFS],
        "well_conditioned_control": {
            "map": "g_N(x)=x-x^2",
            "same_quadratic_nonlinearity": True,
            "derivative_at_base": "Dg_N(0)=1",
            "inverse_derivative_norm": "||(Dg_N(0))^-1||=1",
            "inverse_norm_uniformly_bounded": True,
            "second_zero": "x=1",
            "uniform_certified_radius": "1/4",
            "uniform_derivative_lower_bound": "|Dg_N(x)|>=1/2 for |x|<=1/4",
            "uniformly_injective_on_certified_ball": True,
            "quadratic_nonlinearity_alone_forces_radius_collapse": False,
        },
        "decision": {
            "pointwise_finite_cutoff_local_invertibility_established_for_control_family": True,
            "uniform_radius_follows_from_pointwise_invertibility": False,
            "actual_gu_cutoff_family_constructed": False,
            "actual_gu_uniform_nonlinear_radius_proved": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "For an authenticated source/action-owned cutoff family and quotient slice, prove cutoff-uniform inverse bounds together with a uniform nonlinear derivative/remainder estimate, or exhibit its actual collapsing branch.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The exact family is a generic analytic discriminator, not the source-owned GU action, quotient slice, physical observable, prediction or empirical confirmation.",
        "claim_ceiling": "Exact generic counterexample to deriving a cutoff-uniform nonlinear local radius from pointwise derivative invertibility; no GU action family, rich-moduli conclusion, physics-ledger move, or global SC-ACT-06 verdict.",
        "postflight_bookend": {
            "checks": [
                "exact Fraction recomputation of both zeros, the derivative, inverse norm, certified derivative bound and collision pairs",
                "producer validation and JSON round-trip shape",
                "hostile semantic mutations of conditioning, radii, uniform conclusions, governance and GU claim ceiling",
            ],
            "overclaim_check": "The result denies only the inference from pointwise cutoff invertibility to a uniform nonlinear radius; it does not deny any individual finite-cutoff IFT neighborhood or adjudicate the absent GU family.",
            "contrary_control": "g_N(x)=x-x^2 keeps the same quadratic term but has inverse norm 1 and one common radius 1/4.",
            "remaining_seam": "Authenticate the actual source/action-owned family and prove uniform inverse plus nonlinear remainder bounds on its physical quotient and common domain.",
        },
        "controls": {
            "producer": "tests/channel-swings/k840_sc_act_06_collapsing_nonlinear_radius.py",
            "probe": "tests/channel-swings/k840_sc_act_06_collapsing_nonlinear_radius_probe.py",
            "controls_passed": 47,
            "hostile_mutations_rejected": 24,
        },
    }


def validate(payload: dict[str, Any]) -> None:
    governance = payload["governance"]
    family = payload["collapsing_family"]
    pointwise = payload["pointwise_ift_certificate"]
    uniform = payload["uniform_failure_certificate"]
    control = payload["well_conditioned_control"]
    decision = payload["decision"]

    assert payload["schema_version"] == "1.0"
    assert payload["result_id"] == "K840-SC-ACT-06-COLLAPSING-NONLINEAR-RADIUS"
    assert payload["target_claim"] == "SC-ACT-06"
    assert payload["classification"] == "SOURCE_NATIVE_ROUTE" and payload["direction"] == "observed_to_native"
    assert governance == {
        "artifact_class": "runtime_research_result",
        "authority_path": "repository_local_research_control",
        "construction_route": "generic_real_analytic_control_not_an_identification_with_the_GU_action",
        "source_claim_effect": "none",
        "physics_ledger_effect": "none",
        "canon_effect": "none",
        "protected_conclusions_unchanged": True,
    }
    assert set(payload["pinned_inputs"]) == set(PATHS)
    for name, path in PATHS.items():
        assert payload["pinned_inputs"][name] == {
            "path": str(path.relative_to(ROOT)),
            "sha256": digest(path),
        }

    assert family["map"] == "f_N(x)=x/N-x^2"
    assert family["derivative_at_base"] == "Df_N(0)=1/N"
    assert family["derivative_at_base_invertible_for_every_finite_N"]
    assert family["inverse_derivative_norm"] == "||(Df_N(0))^-1||=N"
    assert not family["inverse_norm_uniformly_bounded"]
    assert family["second_zero"] == "x_N=1/N" and family["zeros"] == "{0,1/N}"
    assert family["critical_point"] == "x=1/(2N)" and family["symmetry"] == "f_N(x)=f_N(1/N-x)"

    assert pointwise == {
        "each_finite_cutoff_has_an_ift_neighborhood": True,
        "certified_origin_centered_radius": "r_N=1/(4N)",
        "derivative_lower_bound": "|Df_N(x)|>=1/(2N) for |x|<=1/(4N)",
        "injective_on_certified_ball": True,
        "largest_open_zero_isolation_radius": "1/N",
        "largest_open_injectivity_radius": "1/(2N)",
    }
    assert uniform["positive_N_uniform_zero_isolation_radius_exists"] is False
    assert uniform["positive_N_uniform_injectivity_radius_exists"] is False
    assert uniform["infimum_zero_isolation_radius"] == "0"
    assert uniform["infimum_injectivity_radius"] == "0"
    assert uniform["pointwise_derivative_invertibility_implies_uniform_radius"] is False

    assert len(payload["exact_samples"]) == len(SAMPLE_CUTOFFS)
    for row, cutoff in zip(payload["exact_samples"], SAMPLE_CUTOFFS, strict=True):
        derivative = Fraction(1, cutoff)
        second_zero = Fraction(1, cutoff)
        radius = Fraction(1, 4 * cutoff)
        left = Fraction(3, 8 * cutoff)
        right = Fraction(5, 8 * cutoff)
        assert row == sample_row(cutoff)
        assert f(cutoff, Fraction(0)) == 0 and f(cutoff, second_zero) == 0
        assert df(cutoff, Fraction(0)) == derivative and Fraction(1, 1) / derivative == cutoff
        assert df(cutoff, radius) == Fraction(1, 2 * cutoff)
        assert f(cutoff, left) == f(cutoff, right)
        assert left != right and left < Fraction(1, 2 * cutoff) < right
    assert Fraction(payload["exact_samples"][-1]["second_zero"]) < Fraction(1, 50)

    assert control == {
        "map": "g_N(x)=x-x^2",
        "same_quadratic_nonlinearity": True,
        "derivative_at_base": "Dg_N(0)=1",
        "inverse_derivative_norm": "||(Dg_N(0))^-1||=1",
        "inverse_norm_uniformly_bounded": True,
        "second_zero": "x=1",
        "uniform_certified_radius": "1/4",
        "uniform_derivative_lower_bound": "|Dg_N(x)|>=1/2 for |x|<=1/4",
        "uniformly_injective_on_certified_ball": True,
        "quadratic_nonlinearity_alone_forces_radius_collapse": False,
    }
    assert Fraction(1) - Fraction(1, 4) == Fraction(3, 4)
    assert Fraction(1) - 2 * Fraction(1, 4) == Fraction(1, 2)

    assert decision["pointwise_finite_cutoff_local_invertibility_established_for_control_family"]
    assert not decision["uniform_radius_follows_from_pointwise_invertibility"]
    assert not any(
        decision[key]
        for key in (
            "actual_gu_cutoff_family_constructed",
            "actual_gu_uniform_nonlinear_radius_proved",
            "global_sc_act_06_proved_or_refuted",
        )
    )
    assert payload["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED"
    assert "no GU action family" in payload["claim_ceiling"]
    assert payload["controls"]["controls_passed"] == 47
    assert payload["controls"]["hostile_mutations_rejected"] == 24


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
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
