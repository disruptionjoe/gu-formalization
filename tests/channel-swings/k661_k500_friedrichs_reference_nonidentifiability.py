#!/usr/bin/env python3
"""K661: ordinary boundary data and resolvent convergence do not select Friedrichs."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k661-k500-friedrichs-reference-nonidentifiability.json"


def trim(poly: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def derivative(poly: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    if len(poly) == 1:
        return (Fraction(0),)
    return trim(tuple(Fraction(i) * poly[i] for i in range(1, len(poly))))


def multiply(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(tuple(out))


def integral_01(poly: tuple[Fraction, ...]) -> Fraction:
    return sum(value / Fraction(i + 1) for i, value in enumerate(poly))


def evaluate(poly: tuple[Fraction, ...], x: Fraction) -> Fraction:
    return sum(value * x**i for i, value in enumerate(poly))


def gamma0(poly: tuple[Fraction, ...]) -> tuple[Fraction, Fraction]:
    return evaluate(poly, Fraction(0)), evaluate(poly, Fraction(1))


def gamma1(poly: tuple[Fraction, ...]) -> tuple[Fraction, Fraction]:
    prime = derivative(poly)
    return evaluate(prime, Fraction(0)), -evaluate(prime, Fraction(1))


def dot(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> Fraction:
    return sum(a * b for a, b in zip(left, right, strict=True))


def green_pairing(
    f: tuple[Fraction, ...], g: tuple[Fraction, ...]
) -> tuple[Fraction, Fraction, Fraction]:
    minus_f2 = tuple(-value for value in derivative(derivative(f)))
    minus_g2 = tuple(-value for value in derivative(derivative(g)))
    bulk = integral_01(multiply(minus_f2, g)) - integral_01(multiply(f, minus_g2))
    boundary = dot(gamma1(f), gamma0(g)) - dot(gamma0(f), gamma1(g))
    swapped = dot(tuple(-x for x in gamma0(f)), gamma1(g)) - dot(
        gamma1(f), tuple(-x for x in gamma0(g))
    )
    return bulk, boundary, swapped


def vector(values: tuple[Fraction, ...]) -> list[str]:
    return [str(value) for value in values]


def build() -> dict[str, Any]:
    polynomials = {
        "one": (Fraction(1),),
        "x": (Fraction(0), Fraction(1)),
        "x_one_minus_x": (Fraction(0), Fraction(1), Fraction(-1)),
        "x2_one_minus_x": (Fraction(0), Fraction(0), Fraction(1), Fraction(-1)),
    }
    pairs = [("one", "x"), ("x", "x_one_minus_x"), ("x_one_minus_x", "x2_one_minus_x")]
    green_rows = []
    for left, right in pairs:
        bulk, boundary, swapped = green_pairing(polynomials[left], polynomials[right])
        green_rows.append(
            {
                "left": left,
                "right": right,
                "bulk_pairing": str(bulk),
                "dirichlet_coordinate_pairing": str(boundary),
                "swapped_coordinate_pairing": str(swapped),
                "both_green_identities_hold": bulk == boundary == swapped,
            }
        )
    constant = polynomials["one"]
    dirichlet_witness = polynomials["x_one_minus_x"]
    return {
        "schema_version": "1.0",
        "result_id": "K661-K500-FRIEDRICHS-REFERENCE-NONIDENTIFIABILITY",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A custody-relative obstruction to inferring K657's Friedrichs reference from ordinary-boundary-triple validity, semiboundedness, recursive-domain existence, or norm-resolvent convergence without the native minimal form and boundary maps.",
        "gu_typed_objects": {
            "carrier": "one complete boundary Hilbert space; the exact control is the two-endpoint trace space for the minimal interval Laplacian",
            "form": "the closed minimal semibounded operator and its Friedrichs form closure, which are not serialized by K139/K159",
            "domain": "the reference extension ker(Gamma_0), distinguished from a different self-adjoint reference obtained by a valid symplectic boundary-map swap",
            "target": "the native proof that K139's chosen ker(Gamma_0) is the Friedrichs extension",
            "result": "Friedrichs-reference custody obstruction MAP-TYPE=nonidentifiability",
        },
        "interval_control": {
            "minimal_operator": "-d^2/dx^2 on C_c^infinity(0,1), closed to the minimal semibounded symmetric operator",
            "boundary_maps": "Gamma_0 f=(f(0),f(1)); Gamma_1 f=(f'(0),-f'(1))",
            "green_identity_exact_on_polynomial_controls": all(row["both_green_identities_hold"] for row in green_rows),
            "dirichlet_reference": "ker(Gamma_0)",
            "dirichlet_is_friedrichs": True,
            "swapped_maps": "Gamma_0'=Gamma_1; Gamma_1'=-Gamma_0",
            "swapped_green_identity_valid": all(row["both_green_identities_hold"] for row in green_rows),
            "swapped_reference": "ker(Gamma_1), the Neumann extension",
            "swapped_reference_is_friedrichs": False,
            "same_minimal_operator": True,
            "both_references_self_adjoint_and_semibounded": True,
        },
        "exact_controls": {
            "green_rows": green_rows,
            "constant_trace": vector(gamma0(constant)),
            "constant_normal_trace": vector(gamma1(constant)),
            "constant_is_neumann_not_dirichlet": gamma1(constant) == (0, 0) and gamma0(constant) != (0, 0),
            "dirichlet_witness_trace": vector(gamma0(dirichlet_witness)),
            "dirichlet_witness_normal_trace": vector(gamma1(dirichlet_witness)),
            "dirichlet_witness_is_dirichlet_not_neumann": gamma0(dirichlet_witness) == (0, 0) and gamma1(dirichlet_witness) != (0, 0),
            "constant_dirichlet_approximant_resolvent_errors": ["0", "0", "0"],
            "constant_neumann_approximant_resolvent_errors": ["0", "0", "0"],
            "both_constant_families_norm_resolvent_converge": True,
            "convergence_selects_friedrichs": False,
            "controls_are_synthetic": True,
        },
        "custody_theorem": {
            "ordinary_boundary_triple_alone_selects_friedrichs": False,
            "semibounded_reference_alone_selects_friedrichs": False,
            "norm_resolvent_convergence_alone_selects_friedrichs": False,
            "profile_universality_alone_selects_friedrichs": False,
            "required_native_evidence": [
                "the densely defined closed semibounded minimal symmetric restriction",
                "its closable minimal quadratic form and closed Friedrichs form",
                "complete ordinary boundary maps on Dom(S*)",
                "proof that ker(Gamma_0) is the operator associated with that closed Friedrichs form",
            ],
            "fixed_native_reference_is_not_friedrichs": False,
        },
        "composition": {
            "K139_norm_resolvent_universality_retained": True,
            "K159_complete_boundary_space_typing_retained": True,
            "K657_friedrichs_premise_discharged": False,
            "K660_translations_preserve_a_previously_proved_reference": True,
            "general_symplectic_swap_is_not_a_K660_translation": True,
        },
        "decision": {
            "current_interface_rejected_as_friedrichs_proof": True,
            "native_friedrichs_reference_denied": False,
            "next_exact_input": "Serialize K139's minimal semibounded restriction, closed minimal form and complete trace maps; prove that the operator associated with the closed minimal form is exactly ker(Gamma_0). K662 then gives the maximal bounded coordinate class that preserves that proof.",
        },
        "native_interface_status": {
            "actual_native_minimal_operator_serialized": False,
            "actual_native_friedrichs_form_serialized": False,
            "actual_native_boundary_triple_serialized": False,
            "actual_native_reference_proved_friedrichs": False,
            "actual_native_s_identified": False,
            "actual_native_denominator_serialized": False,
            "actual_native_base_floor_r0_identified": False,
            "actual_native_target_b_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "The interval pair is a synthetic custody control, not a sector of the repository-supplied point-Fock model, and no source-selected extension or physical state is identified.",
        "preflight_bookend": {
            "route_comparison": "K657 cannot consume a real-level denominator before the reference extension is authenticated as Friedrichs; K660 proves only that a known status survives a restricted translation.",
            "retrieval_collision_result": "K139/K159 serialize convergence, a recursive domain and operator-valued boundary typing but not the minimal form closure or complete ordinary boundary maps.",
            "strongest_alternative": "K652's direct cancelled-form route bypasses the Friedrichs-reference obligation.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling a semibounded norm-resolvent limit Friedrichs merely because it is represented by an ordinary boundary triple.",
            "strongest_contrary_construction": "One minimal interval Laplacian admits a Dirichlet Friedrichs reference and, after a valid symplectic swap, a distinct Neumann non-Friedrichs reference; constant operator families converge in norm resolvent to either.",
            "weakest_reproducibility_seam": "The exact control proves data insufficiency, not the identity of K139's actual unrecorded trace maps.",
        },
        "claim_ceiling": "Exact custody-relative nonidentifiability theorem. For one semibounded minimal interval Laplacian, exact polynomial Green identities support both the Dirichlet ordinary boundary triple, whose Gamma_0 reference is Friedrichs, and its symplectically swapped Neumann reference, which is not Friedrichs. Constant approximant families converge in norm resolvent to either. Thus ordinary-triple validity, semiboundedness, recursive-domain existence, norm-resolvent convergence and profile universality do not by themselves identify the Friedrichs reference. The controls are not K139 sectors and do not deny that a correct native Friedrichs reference exists. No native s, denominator, d_N, eta_N, r0, b, tail, m, alpha, delta, K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is supplied.",
    }


def validate(payload: dict[str, Any]) -> None:
    control = payload["interval_control"]
    exact = payload["exact_controls"]
    custody = payload["custody_theorem"]
    assert control["green_identity_exact_on_polynomial_controls"]
    assert control["swapped_green_identity_valid"]
    assert control["dirichlet_is_friedrichs"]
    assert not control["swapped_reference_is_friedrichs"]
    assert exact["constant_is_neumann_not_dirichlet"]
    assert exact["dirichlet_witness_is_dirichlet_not_neumann"]
    assert exact["both_constant_families_norm_resolvent_converge"]
    assert not custody["norm_resolvent_convergence_alone_selects_friedrichs"]
    assert not custody["fixed_native_reference_is_not_friedrichs"]


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
