#!/usr/bin/env python3
"""K172 continuum n=0/n=1 action blocks and graph-tail discriminator."""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


class CertificateError(ValueError):
    """Raised when a tail certificate is malformed."""


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def load_k170():
    path = Path(__file__).with_name("k170_direct_gram_reference_shape_slice.py")
    spec = importlib.util.spec_from_file_location("k170_solver", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K170 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K170 = load_k170()


def first_block(seed: str, auxiliary_shift: int = 256) -> dict[str, Any]:
    """Return the exact block formula and a rigorous Hilbert-norm enclosure."""
    if seed not in ("vacuum", "one_impurity"):
        raise CertificateError("seed must be vacuum or one_impurity")
    if auxiliary_shift != 256:
        raise CertificateError("K172 evaluates only the fixed K139 chart at 256")
    multiplicity = 1 if seed == "vacuum" else 2
    components = 2 if seed == "vacuum" else 1
    profile_sq = K170.point_profile_norm_sq_interval()
    profile_norm = K170.sqrt_interval(profile_sq[0])[0], K170.sqrt_interval(profile_sq[1])[1]
    correction_sq_upper = Fraction(8, 9 * (auxiliary_shift - 1))
    correction_norm_upper = Fraction(1, 16)
    if not correction_sq_upper < correction_norm_upper**2:
        raise AssertionError("outward D h enclosure did not close")
    per_lower = auxiliary_shift * profile_norm[0] - multiplicity * correction_norm_upper
    per_upper = auxiliary_shift * profile_norm[1] + multiplicity * correction_norm_upper
    if per_lower <= 0:
        raise AssertionError("reverse triangle lower bound is not positive")
    total_lower, total_upper = per_lower, per_upper
    if components == 2:
        root_two = K170.sqrt_interval(Fraction(2))
        total_lower *= root_two[0]
        total_upper *= root_two[1]
    return {
        "seed": seed,
        "charge": [0, 0] if seed == "vacuum" else [1, 0],
        "n0_exact": "W_0 phi=-256 phi",
        "n1_transition_components": components,
        "normal_ordered_self_energy_multiplicity_per_component": multiplicity,
        "profile": "h(p)=(2*pi)^(-1/2)/(sqrt(1+p^2)+256)",
        "g1_per_component": "-h",
        "D_definition": "D_256(e)=int_R e/((omega(k)+256)(omega(k)+256+e)) dk/(2*pi)",
        "W1_g1_per_component": f"(256-{multiplicity}*D_256(omega(p)))*h(p)",
        "D_pointwise_upper": "D_256(e)<=(1/pi)*log(1+e/256)",
        "D_h_norm_sq_upper": qstr(correction_sq_upper),
        "D_h_norm_upper_used": qstr(correction_norm_upper),
        "profile_norm_interval": [qstr(profile_norm[0]), qstr(profile_norm[1])],
        "per_component_W1_g1_norm_interval": [qstr(per_lower), qstr(per_upper)],
        "full_n1_vector_norm_interval": [qstr(total_lower), qstr(total_upper)],
        "continuum_native_first_block": True,
    }


def graph_tail(*, B: Fraction, seed_graph_norm: Fraction, q_D: Fraction,
               q_H: Fraction, resolved_order: int) -> Fraction:
    """Bound the unresolved action column after the left Neumann factor."""
    if B <= 0 or seed_graph_norm <= 0:
        raise CertificateError("positive graph constants are required")
    if not 0 <= q_D < 1 or not 0 <= q_H < 1:
        raise CertificateError("both contraction constants must lie in [0,1)")
    if resolved_order < 0:
        raise CertificateError("resolved order must be nonnegative")
    return B * seed_graph_norm * q_D ** (resolved_order + 1) / ((1 - q_D) * (1 - q_H))


def demo() -> dict[str, Any]:
    vacuum = first_block("vacuum")
    impurity = first_block("one_impurity")
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {"auxiliary_chart_shift": 256, "Hilbert_contraction_upper": "3/8"},
        "native_continuum_blocks": [vacuum, impurity],
        "graph_tail_theorem": {
            "premises": "||G||_(D->D)<=q_D<1, ||W||_(D->H)<=B, ||phi||_D=c, ||G||_(H->H)<=q_H<1",
            "unresolved_after_order_N": "B*c*q_D^(N+1)/((1-q_D)*(1-q_H))",
            "positive_control": qstr(graph_tail(B=Fraction(2), seed_graph_norm=Fraction(1), q_D=Fraction(1, 2), q_H=Fraction(3, 8), resolved_order=1)),
            "native_numeric_B_serialized": False,
            "native_numeric_q_D_serialized": False,
            "native_numeric_tail_emitted": False,
        },
        "Hilbert_only_counterexample": {
            "carrier": "ell2(N_0)",
            "G": "G e_n=q e_(n+1)",
            "W": "W e_n=q^(-n)/(n+1) e_n",
            "word_norm": "||G^n e_0||=q^n",
            "action_block_norm": "||W G^n e_0||=1/(n+1)",
            "action_block_sum_diverges": True,
            "native_continuum_counterexample": False,
        },
        "release_test": {
            "native_n0_vector_serialized": True,
            "native_n1_vector_serialized": True,
            "native_n1_vector_norm_enclosed": True,
            "complete_native_all_order_vector_tail_serialized": False,
            "coefficient_complete_base_R0_action_column_serialized": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "native_left_floor_at_selected_scalar_center_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": {"SC-META-53": "UNCERTAIN_UNCHANGED", "LT-SM8": "NEEDS_UNCHANGED", "RA-F1": "NEEDS_UNCHANGED", "AC-F1": "NEEDS_UNCHANGED"},
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
        "canon_paper_release_or_public_posture_move": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
