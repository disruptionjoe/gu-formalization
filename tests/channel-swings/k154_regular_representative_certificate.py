#!/usr/bin/env python3
"""Fail-closed K154 bridge from regular-representative data to K152.

The compiler is deliberately strict.  K139 chart/domain facts and an HVZ
essential edge are not substitutes for coefficient-complete form/action data
or a proof that all spectrum outside the ground eigenspace lies above a stated
floor.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from k152_form_dual_residual_enclosure_solver import (
    CertificateError,
    dual_temple_ground_enclosure,
    form_pencil,
    q,
    qstr,
    rayleigh_quotient,
)
from k153_neumann_chart_conforming_core_solver import (
    coercive_floor,
    hilbert_to_form_dual_residual_sq,
)


def _proof_ref(packet: dict[str, Any], key: str) -> str:
    value = packet.get(key)
    if not isinstance(value, str) or not value.strip():
        raise CertificateError(f"missing proof reference: {key}")
    return value


def validate_packet(packet: Any) -> dict[str, Any]:
    if not isinstance(packet, dict):
        raise CertificateError("regular-representative packet must be an object")
    packet_kind = packet.get("packet_kind")
    if packet_kind not in ("abstract_positive_control", "native_K139_fixed_operator"):
        raise CertificateError("packet kind must distinguish abstract control from native data")
    claims_native = packet.get("claim_native_regular_packet")
    if claims_native is not (packet_kind == "native_K139_fixed_operator"):
        raise CertificateError("native claim does not match packet provenance kind")
    charge = packet.get("charge_sector")
    if charge not in ([0, 0], [1, 0], [0, 1]):
        raise CertificateError("charge sector is not a representative or flavor partner")
    for key in (
        "fixed_operator_ref",
        "k139_chart_ref",
        "conforming_core_ref",
        "regular_form_ref",
        "regular_action_ref",
        "hilbert_residual_proof_ref",
        "regular_lower_bound_ref",
        "next_distinct_spectrum_floor_ref",
        "spectral_count_or_exterior_subspace_ref",
    ):
        _proof_ref(packet, key)
    if charge == [0, 1]:
        _proof_ref(packet, "signed_flavor_intertwiner_ref")
    if packet.get("finite_cutoff_only") is not False:
        raise CertificateError("finite-cutoff-only data are not native regular data")
    if packet.get("essential_edge_used_as_gap") is not False:
        raise CertificateError("an essential edge cannot stand in for the next-distinct floor")
    form, gram = form_pencil(packet.get("regular_form_matrix"), packet.get("hilbert_gram_matrix"))
    coefficients = packet.get("trial_coefficients")
    if not isinstance(coefficients, list) or len(coefficients) != len(form):
        raise CertificateError("trial coefficients do not match the form pencil")
    return {
        "charge": charge,
        "packet_kind": packet_kind,
        "form": form,
        "gram": gram,
        "coefficients": coefficients,
    }


def compile_certificate(packet: Any) -> dict[str, Any]:
    checked = validate_packet(packet)
    contraction = q(packet.get("chart_contraction_upper"))
    regular_lower = q(packet.get("regular_lower_bound"))
    shift = q(packet.get("physical_shift"))
    residual = q(packet.get("hilbert_residual_norm_upper"))
    if residual < 0:
        raise CertificateError("Hilbert residual norm bound must be nonnegative")
    coercivity = coercive_floor(regular_lower, shift, contraction)
    if coercivity <= 0:
        raise CertificateError("transported shifted-form coercivity is not positive")
    rho = rayleigh_quotient(
        packet["regular_form_matrix"],
        packet["hilbert_gram_matrix"],
        checked["coefficients"],
    )
    eps_sq = hilbert_to_form_dual_residual_sq(residual, coercivity)
    lower, upper, correction, projection = dual_temple_ground_enclosure(
        rho,
        eps_sq,
        shift,
        coercivity,
        packet.get("next_distinct_spectrum_lower"),
    )
    return {
        "schema_version": "1.0",
        "arithmetic": "exact_rational_outer_bounds",
        "charge_sector": checked["charge"],
        "rayleigh": qstr(rho),
        "shifted_form_coercivity_floor": qstr(coercivity),
        "form_dual_residual_sq_upper": qstr(eps_sq),
        "next_distinct_spectrum_lower": qstr(q(packet["next_distinct_spectrum_lower"])),
        "ground_interval": [qstr(lower), qstr(upper)],
        "correction_upper": qstr(correction),
        "trial_ground_projection_error_upper": qstr(projection),
        "certificate_contract_complete": True,
        "native_energy_interval_emitted": checked["packet_kind"] == "native_K139_fixed_operator",
        "essential_edge_used_as_gap": False,
    }


def regular_form_countermodels(seed_shift: Any) -> dict[str, Any]:
    """Same identity chart/domain/charge data, different seed form/action."""
    shift = q(seed_shift)
    base = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(2)]]
    perturbed = [[shift, Fraction(0)], [Fraction(0), Fraction(2)]]
    return {
        "chart": [["1", "0"], ["0", "1"]],
        "common_domain": "C^2",
        "charge_projection": [["1", "0"], ["0", "1"]],
        "base_form": [[qstr(x) for x in row] for row in base],
        "perturbed_form": [[qstr(x) for x in row] for row in perturbed],
        "seed_form_values": [qstr(base[0][0]), qstr(perturbed[0][0])],
        "bounded_charge_preserving_rank_one_perturbation": True,
    }


def hidden_gap_countermodels(hidden_level: Any, essential_edge: Any = 4) -> dict[str, Any]:
    """Same seed form/action and essential edge, arbitrarily different gap."""
    level = q(hidden_level)
    edge = q(essential_edge)
    if not 0 < level < edge:
        raise CertificateError("hidden level must lie strictly between ground and essential edge")
    return {
        "seed_form": "0",
        "seed_action": ["0", "0"],
        "seed_residual": "0",
        "essential_edge": qstr(edge),
        "next_distinct_spectrum": qstr(level),
        "model_prefix": [["0", "0", "0"], ["0", qstr(level), "0"], ["0", "0", qstr(edge)]],
        "essential_edge_alone_is_next_gap": False,
    }


DEMO = {
    "packet_kind": "abstract_positive_control",
    "claim_native_regular_packet": False,
    "charge_sector": [0, 0],
    "fixed_operator_ref": "abstract-positive-control#H",
    "k139_chart_ref": "abstract-positive-control#identity-chart",
    "conforming_core_ref": "abstract-positive-control#two-vector-core",
    "regular_form_ref": "abstract-positive-control#exact-form",
    "regular_action_ref": "abstract-positive-control#exact-action",
    "hilbert_residual_proof_ref": "abstract-positive-control#residual-quarter",
    "regular_lower_bound_ref": "abstract-positive-control#R-nonnegative",
    "next_distinct_spectrum_floor_ref": "abstract-positive-control#second-eigenvalue-two",
    "spectral_count_or_exterior_subspace_ref": "abstract-positive-control#one-ground-state",
    "regular_form_matrix": [["0", "0"], ["0", "2"]],
    "hilbert_gram_matrix": [["1", "0"], ["0", "1"]],
    "trial_coefficients": ["1", "1/10"],
    "chart_contraction_upper": "3/8",
    "regular_lower_bound": "0",
    "physical_shift": "3",
    "hilbert_residual_norm_upper": "1/4",
    "next_distinct_spectrum_lower": "2",
    "finite_cutoff_only": False,
    "essential_edge_used_as_gap": False,
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path)
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    try:
        packet = DEMO if args.demo or args.input is None else json.loads(args.input.read_text())
        print(json.dumps(compile_certificate(packet), indent=2, sort_keys=True))
    except (CertificateError, KeyError, TypeError, ValueError, json.JSONDecodeError, OSError) as exc:
        print(json.dumps({"certified": False, "error": str(exc)}, sort_keys=True))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
