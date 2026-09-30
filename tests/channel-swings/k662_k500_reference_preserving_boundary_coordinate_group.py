#!/usr/bin/env python3
"""K662: full bounded reference-preserving ordinary-boundary coordinate group."""

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
OUTPUT = ROOT / "lab/process/k662-k500-reference-preserving-boundary-coordinate-group.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K661 = load("k661_for_k662", "k661_k500_friedrichs_reference_nonidentifiability.py")


def add(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(a + b for a, b in zip(left, right, strict=True))


def subtract(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(a - b for a, b in zip(left, right, strict=True))


def congruence_diagonal(values: tuple[Fraction, ...], u: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(value / scale**2 for value, scale in zip(values, u, strict=True))


def strings(values: tuple[Fraction, ...]) -> list[str]:
    return [str(value) for value in values]


def build() -> dict[str, Any]:
    k661 = K661.build()
    u = (Fraction(2), Fraction(1, 2))
    m = (Fraction(-1), Fraction(2))
    w = (Fraction(1, 2), Fraction(3))
    c = (Fraction(3, 2), Fraction(-2, 3))
    d = subtract(w, m)
    m_prime = congruence_diagonal(add(m, c), u)
    w_prime = congruence_diagonal(add(w, c), u)
    d_prime = subtract(w_prime, m_prime)
    error = (Fraction(1, 20), Fraction(-1, 50))
    d_n = add(d, error)
    error_prime = congruence_diagonal(error, u)
    d_n_prime = congruence_diagonal(d_n, u)
    norm_u = Fraction(2)
    norm_u_inverse = Fraction(2)
    d_floor = min(d)
    d_n_floor = min(d_n)
    eta = max(abs(x) for x in error)
    transformed_floor = min(d_prime)
    transformed_d_n_floor = min(d_n_prime)
    transformed_eta = max(abs(x) for x in error_prime)
    return {
        "schema_version": "1.0",
        "result_id": "K662-K500-REFERENCE-PRESERVING-BOUNDARY-COORDINATE-GROUP",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The complete bounded invertible ordinary-boundary coordinate class that preserves one already authenticated reference extension, and its exact congruence transport of K657--K658's complete denominator packet.",
        "gu_typed_objects": {
            "carrier": "one complete spectator-Fock boundary Hilbert space with boundedly invertible coordinate map U",
            "form": "Gamma_0'=U Gamma_0 and Gamma_1'=U^{-*}(Gamma_1+C Gamma_0), with bounded self-adjoint C",
            "domain": "the unchanged reference extension ker(Gamma_0')=ker(Gamma_0) and the same target extension in transformed coordinates",
            "target": "the complete denominator order and cofinal approximation packet under every bounded reference-preserving coordinate change",
            "result": "reference-preserving boundary-coordinate covariance MAP-TYPE=bounded congruence equivalence",
        },
        "coordinate_group_theorem": {
            "hypotheses": "U boundedly invertible on the complete boundary Hilbert space; C bounded self-adjoint",
            "boundary_maps": "Gamma_0'=U Gamma_0; Gamma_1'=U^{-*}(Gamma_1+C Gamma_0)",
            "green_identity_preserved": True,
            "reference_kernel_identity": "ker(Gamma_0')=ker(Gamma_0)",
            "reference_extension_unchanged": True,
            "friedrichs_status_preserved_if_previously_proved": True,
            "friedrichs_status_created": False,
            "weyl_transform": "M'(z)=U^{-*}(M(z)+C)U^{-1}",
            "extension_transform": "W'=U^{-*}(W+C)U^{-1}",
            "denominator_transform": "D'(z)=U^{-*}D(z)U^{-1}",
            "complete_denominator_nonnegativity_equivalent": True,
            "strict_positivity_equivalent": True,
            "numerical_floor_invariant_for_unitary_U": True,
            "numerical_floor_invariant_for_general_U": False,
            "K661_symplectic_swap_covered": False,
        },
        "quantitative_transport": {
            "floor_hypothesis": "d>=0 and d_N>=0",
            "if_D_ge_nonnegative_d_then": "D'>=d/||U||^2",
            "if_error_le_eta_then": "||D_N'-D'||<=||U^{-1}||^2 eta",
            "if_DN_ge_nonnegative_dN_then": "D_N'>=d_N/||U||^2",
            "conservative_transferred_margin": "d_N/||U||^2-||U^{-1}||^2 eta_N",
            "unitary_case_recovers_K660_exact_margin_invariance": True,
            "condition_number_cost_is_coordinate_not_operator_physics": True,
        },
        "exact_controls": {
            "U_diagonal": strings(u),
            "U_inverse_diagonal": strings(tuple(1 / x for x in u)),
            "norm_U": str(norm_u),
            "norm_U_inverse": str(norm_u_inverse),
            "M_diagonal": strings(m),
            "W_diagonal": strings(w),
            "C_diagonal": strings(c),
            "denominator_diagonal": strings(d),
            "transformed_M_diagonal": strings(m_prime),
            "transformed_W_diagonal": strings(w_prime),
            "transformed_denominator_diagonal": strings(d_prime),
            "congruence_identity": d_prime == congruence_diagonal(d, u),
            "original_denominator_floor": str(d_floor),
            "transformed_denominator_floor": str(transformed_floor),
            "floor_lower_bound": str(d_floor / norm_u**2),
            "floor_bound_holds": transformed_floor >= d_floor / norm_u**2,
            "cofinal_error_diagonal": strings(error),
            "transformed_cofinal_error_diagonal": strings(error_prime),
            "cofinal_approximant_diagonal": strings(d_n),
            "transformed_cofinal_approximant_diagonal": strings(d_n_prime),
            "approximant_congruence_identity": d_n_prime == congruence_diagonal(d_n, u),
            "operator_norm_error": str(eta),
            "transformed_operator_norm_error": str(transformed_eta),
            "error_upper_bound": str(norm_u_inverse**2 * eta),
            "error_bound_holds": transformed_eta <= norm_u_inverse**2 * eta,
            "original_approximant_floor": str(d_n_floor),
            "transformed_approximant_floor": str(transformed_d_n_floor),
            "approximant_floor_lower_bound": str(d_n_floor / norm_u**2),
            "approximant_floor_bound_holds": transformed_d_n_floor >= d_n_floor / norm_u**2,
            "conservative_margin": str(d_n_floor / norm_u**2 - norm_u_inverse**2 * eta),
            "conservative_margin_nonnegative": d_n_floor / norm_u**2 >= norm_u_inverse**2 * eta,
            "unitary_swap_denominator_diagonal": strings(tuple(reversed(d))),
            "unitary_swap_floor_invariant": min(tuple(reversed(d))) == d_floor,
            "unitary_swap_error_norm_invariant": max(abs(x) for x in reversed(error)) == eta,
            "controls_are_synthetic": True,
        },
        "composition": {
            "K661_current_interface_does_not_select_friedrichs": k661["decision"]["current_interface_rejected_as_friedrichs_proof"],
            "K660_translation_subgroup": "U=I",
            "K657_order_test_coordinate_independent_within_group": True,
            "K658_packet_transports_with_condition_number_bounds": True,
            "K139_regulator_coordinates_already_authenticated_in_group": False,
        },
        "decision": {
            "maximal_bounded_reference_preserving_affine_coordinate_shape_serialized": True,
            "general_boundary_symplectic_changes_rejected_as_reference_safe": True,
            "native_coordinate_law_authenticated": False,
            "native_floor_supplied": False,
            "next_exact_input": "Construct K139's complete Gamma_0 and Gamma_1, prove ker(Gamma_0) is the Friedrichs extension from the closed minimal form, and represent every regulator/counterterm coordinate change by boundedly invertible U and bounded self-adjoint C on the complete boundary space. Then serialize D_N(-s), d_N and eta_N in one coordinate and apply the exact condition-number transport if needed.",
        },
        "native_interface_status": {
            "actual_native_minimal_operator_serialized": False,
            "actual_native_friedrichs_form_serialized": False,
            "actual_native_boundary_triple_serialized": False,
            "actual_native_reference_proved_friedrichs": False,
            "actual_native_coordinate_group_law_proved": False,
            "actual_native_s_identified": False,
            "actual_native_denominator_serialized": False,
            "actual_native_d_n_identified": False,
            "actual_native_eta_n_identified": False,
            "actual_native_base_floor_r0_identified": False,
            "actual_native_target_b_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "The theorem classifies internal boundary coordinates for the repository-supplied point-Fock control; it supplies no source-selected action, physical quotient, state or observable.",
        "preflight_bookend": {
            "route_comparison": "K661 proves that unrestricted ordinary-boundary reparameterization can change the reference; the useful follow-through is to characterize exactly the bounded coordinate changes that cannot.",
            "retrieval_collision_result": "K660 covers translations with U=I but not complete boundary-space basis changes or their quantitative condition-number cost.",
            "strongest_alternative": "A direct complete-form proof under K652 bypasses all boundary-coordinate transport.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling a nonunitary coordinate change margin-invariant, or treating an arbitrary symplectic boundary-map change as reference-preserving.",
            "strongest_contrary_construction": "The exact U=diag(2,1/2) control preserves positivity by congruence but moves the denominator floor from 1 to 3/8 and the cofinal error norm from 1/20 to 2/25.",
            "weakest_reproducibility_seam": "K139 does not serialize U, C or complete trace maps, so membership of its regulator coordinates in this group remains unproved.",
        },
        "claim_ceiling": "Exact complete-boundary coordinate theorem. Every bounded reference-preserving affine ordinary-boundary change of the displayed form Gamma_0'=U Gamma_0 and Gamma_1'=U^{-*}(Gamma_1+C Gamma_0), with U boundedly invertible and C bounded self-adjoint, retains ker(Gamma_0), transports M and W jointly, and sends D to U^{-*}DU^{-1}. Denominator nonnegativity and strict positivity are equivalent; exact numerical floors and cofinal-error norms are invariant only for unitary U, while general U incurs explicit condition-number bounds for the nonnegative K657--K658 margins. This preserves but cannot create a Friedrichs proof and does not authenticate K139's regulator coordinates. No native s, denominator, d_N, eta_N, r0, b, tail, m, alpha, delta, K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is supplied.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["coordinate_group_theorem"]
    exact = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["reference_extension_unchanged"]
    assert theorem["complete_denominator_nonnegativity_equivalent"]
    assert not theorem["friedrichs_status_created"]
    assert not theorem["numerical_floor_invariant_for_general_U"]
    assert not theorem["K661_symplectic_swap_covered"]
    assert exact["congruence_identity"]
    assert exact["floor_bound_holds"]
    assert exact["approximant_congruence_identity"]
    assert exact["error_bound_holds"]
    assert exact["approximant_floor_bound_holds"]
    assert exact["conservative_margin_nonnegative"]
    assert exact["unitary_swap_floor_invariant"]
    assert exact["unitary_swap_error_norm_invariant"]
    assert not native["actual_native_coordinate_group_law_proved"]


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
