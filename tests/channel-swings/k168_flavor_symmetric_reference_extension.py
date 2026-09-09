#!/usr/bin/env python3
"""K168 exact certificates for one conditional non-scalar C3 extension.

The declared physical impurity extension is ``W_ref=diag(-2,1,1)`` in the
native hard-core basis ``(|0>,|1>,|2>)``.  It is a repository reference
coordinate, not a physical selection.  Pulling it through K139's fixed chart
gives ``Delta R=S* W_ref S`` and therefore the exact form order
``-2 M <= Delta R <= M`` for ``M=S*S``.

Finite K155 matrices below are exact algebraic controls only.  They are not
the missing native K162 limiting-form anchor.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence


HERE = Path(__file__).resolve().parent


def _load(name: str):
    path = HERE / name
    spec = importlib.util.spec_from_file_location(f"k168_{path.stem}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load exact dependency at {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K151 = _load("k151_native_charge_block_assembler.py")
K155 = _load("k155_finite_regular_pullback.py")
K150 = _load("k150_certified_schur_tail_solver.py")


class CertificateError(ValueError):
    """Raised when a purported reference declaration is incomplete."""


def q(value: Any) -> Fraction:
    try:
        return value if isinstance(value, Fraction) else Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational input: {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def reference_extension(values: Sequence[Any] = (-2, 1, 1)) -> dict[str, Any]:
    diagonal = [q(value) for value in values]
    if len(diagonal) != 3:
        raise CertificateError("native hard-core C3 extension must declare exactly three diagonal entries")
    if diagonal[1] != diagonal[2]:
        raise CertificateError("flavor-symmetric extension must give |1> and |2> the same value")
    if sum(diagonal, Fraction()) != 0:
        raise CertificateError("reference shape must have zero scalar center")
    if len(set(diagonal)) == 1:
        raise CertificateError("reference extension must be non-scalar")
    if diagonal != [Fraction(-2), Fraction(1), Fraction(1)]:
        raise CertificateError("K168 fixes the primitive unit-shape normalization diag(-2,1,1)")
    return {
        "basis": ["|0>", "|1>", "|2>"],
        "diagonal": [qstr(value) for value in diagonal],
        "dimension": 3,
        "Hermitian": True,
        "trace": "0",
        "scalar_center": "0",
        "non_scalar": True,
        "flavor_symmetric": True,
        "primitive_integer_normalization": True,
        "physical_selection": False,
    }


def impurity_value(state: int) -> Fraction:
    if K151.occupied(state, 0):
        return Fraction(1)
    if K151.occupied(state, 1):
        return Fraction(1)
    return Fraction(-2)


def extension_block(states: Sequence[int]) -> list[list[Fraction]]:
    values = [impurity_value(state) for state in states]
    return K155.diagonal(values)


def regular_pullback_with_reference(
    energies: Sequence[Any], couplings: Sequence[Any], charge: tuple[int, int], auxiliary_shift: Any
) -> dict[str, Any]:
    """Add W_ref to one complete finite K155 charge block at a fixed chart."""
    base = K155.regular_pullback(energies, couplings, charge, auxiliary_shift, 0)
    physical_extension = extension_block(base["states"])
    inverse = base["U_inverse"]
    metric = K155.matmul(K155.transpose(inverse), inverse)
    delta_regular = K155.matmul(
        K155.transpose(inverse), K155.matmul(physical_extension, inverse)
    )
    regular = K155.add(base["R"], delta_regular)
    lower_slack = K155.add(delta_regular, K155.scale(Fraction(2), metric))
    upper_slack = K155.add(metric, K155.scale(Fraction(-1), delta_regular))
    lower_inertia = K150.inertia(lower_slack)
    upper_inertia = K150.inertia(upper_slack)
    if lower_inertia[0] or upper_inertia[0]:
        raise AssertionError("reference pullback violated -2M <= Delta R <= M")
    direct = K155.add(base["H"], physical_extension)
    if regular != K155.matmul(K155.transpose(inverse), K155.matmul(direct, inverse)):
        raise AssertionError("reference extension pullback identity failed")
    commutator = K155.add(
        K155.matmul(physical_extension, base["G"]),
        K155.scale(Fraction(-1), K155.matmul(base["G"], physical_extension)),
    )
    return {
        "states": base["states"],
        "base_regular": base["R"],
        "reference_regular": regular,
        "metric": metric,
        "delta_regular": delta_regular,
        "lower_slack_inertia": list(lower_inertia),
        "upper_slack_inertia": list(upper_inertia),
        "chart_unchanged_by_extension": True,
        "pullback_identity": "R_ref=R_0+S*W_ref*S",
        "form_order": "-2M<=S*W_ref*S<=M",
        "extension_commutes_with_boundary_map": not any(any(row) for row in commutator),
        "finite_regulator_control_only": True,
    }


def flavor_intertwiner_control(energies: Sequence[Any], couplings: Sequence[Any], auxiliary_shift: Any) -> bool:
    left = regular_pullback_with_reference(energies, couplings, (1, 0), auxiliary_shift)
    right = regular_pullback_with_reference(energies, couplings, (0, 1), auxiliary_shift)
    swap = K151.flavor_swap_matrix(left["states"], right["states"], len(energies))
    return (
        K155.matmul(right["reference_regular"], swap)
        == K155.matmul(swap, left["reference_regular"])
        and K155.matmul(K155.transpose(swap), swap) == K155.identity(len(left["states"]))
    )


def generalized_form_consequences() -> dict[str, Any]:
    """State exact min--max and residual consequences of the form order."""
    return {
        "complete_form_order": "R_0-2M<=R_ref<=R_0+M",
        "every_ordered_generalized_eigenvalue_shift_interval": ["-2", "1"],
        "maximum_absolute_change_of_a_relative_gap": "3",
        "matched_shape_residual_increment_M_dual_norm_upper": "3*||u||_M",
        "complement_margin_survives_if_base_M_margin_strictly_exceeds": "3",
        "base_gap_at_most_three_certifies_positive_reference_gap": False,
        "base_complement_margin_at_most_three_certifies_reference_positivity": False,
        "absolute_axis_selected": False,
    }


def representative_seed_boundary() -> dict[str, Any]:
    control = regular_pullback_with_reference(["5/4"], [1], (0, 0), 256)
    labels = [K151.state_label(state, 1) for state in control["states"]]
    bare = {label: qstr(impurity_value(state)) for label, state in zip(labels, control["states"], strict=True)}
    return {
        "bare_vacuum_extension_value": bare["|0;->"],
        "bare_d1_seed_extension_value": "1",
        "bare_d2_seed_extension_value": "1",
        "dressed_K139_trial_extension_value_equals_bare_seed_value_in_general": False,
        "reason": "W_ref does not commute with the nonunitary boundary map",
        "finite_control_commutator_nonzero": not control["extension_commutes_with_boundary_map"],
        "dressed_extension_rayleigh_interval": ["-2", "1"],
    }


def native_k152_replay(**refs: str | None) -> dict[str, Any]:
    fields = {
        "complete reference extension": refs.get("reference_extension_ref"),
        "fixed K139 chart": refs.get("fixed_chart_ref"),
        "same limiting base form evaluation": refs.get("base_form_ref"),
        "physical Gram evaluation": refs.get("physical_gram_ref"),
        "complete form-dual residual": refs.get("residual_ref"),
        "relative generalized gap": refs.get("gap_ref"),
        "complete M-orthogonal complement floor": refs.get("complement_ref"),
        "native left floor": refs.get("left_floor_ref"),
    }
    missing = [name for name, ref in fields.items() if not ref]
    return {
        "reference_declaration_complete": not any(
            name in missing for name in ("complete reference extension", "fixed K139 chart")
        ),
        "required_native_references": list(fields),
        "missing_native_references": missing,
        "native_same_form_packet_complete": not missing,
        "native_ground_count_emitted": False,
        "native_K152_interval_emitted": False,
    }


def demo() -> dict[str, Any]:
    finite = regular_pullback_with_reference(["5/4", "3/2"], [1, 1], (0, 0), 256)
    replay = native_k152_replay(
        reference_extension_ref="K168#W_ref=diag(-2,1,1)",
        fixed_chart_ref="K139/K153#S=(1-G_256)^-1",
        base_form_ref=None,
        physical_gram_ref=None,
        residual_ref=None,
        gap_ref=None,
        complement_ref=None,
        left_floor_ref=None,
    )
    return {
        "schema_version": "1.0",
        "arithmetic": "exact_rational_finite_controls_plus_analytic_form_order",
        "reference_extension": reference_extension(),
        "native_compatibility": {
            "hard_core_C3_complete": True,
            "preserves_q1_q2_charge_blocks": True,
            "preserves_K162_dyadic_domains": True,
            "bounded_form_perturbation": True,
            "signed_flavor_swap_intertwines": flavor_intertwiner_control(["5/4", "3/2"], [1, 1], 256),
        },
        "fixed_chart_form_consequences": generalized_form_consequences(),
        "representative_seed_boundary": representative_seed_boundary(),
        "finite_K155_control": {
            "dimension": len(finite["states"]),
            "pullback_identity": finite["pullback_identity"],
            "form_order": finite["form_order"],
            "lower_slack_inertia": finite["lower_slack_inertia"],
            "upper_slack_inertia": finite["upper_slack_inertia"],
            "extension_commutes_with_boundary_map": finite["extension_commutes_with_boundary_map"],
            "finite_regulator_control_only": finite["finite_regulator_control_only"],
        },
        "native_K152_replay": replay,
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
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
