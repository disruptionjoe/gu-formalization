#!/usr/bin/env python3
"""Exact K166 finite-extension spectral covariance certificates.

K139's scalar finite extension coordinate enters the physical Hamiltonian as
``E I``.  Under the fixed nonunitary chart ``S=U^-1`` this becomes ``E M``
with ``M=S* S``.  Consequently the generalized pencil translates exactly:
``R_E-zM = R_0-(z-E)M``.  Absolute spectral locations require an owned value
of ``E``; matched residual covectors, complements, counts at translated
thresholds, and spectral gaps are coordinate covariant or invariant.

The K155 block below is an exact finite control.  It is not a native K162
continuum anchor and does not select the extension coordinate.
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
    spec = importlib.util.spec_from_file_location(f"k166_{path.stem}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load exact dependency at {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K155 = _load("k155_finite_regular_pullback.py")
K165 = _load("k165_generalized_form_complement_route.py")
K150 = _load("k150_certified_schur_tail_solver.py")


class CertificateError(ValueError):
    """Raised when supplied data do not prove the requested covariance."""


def q(value: Any) -> Fraction:
    try:
        return value if isinstance(value, Fraction) else Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational input: {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def matrix(rows: Sequence[Sequence[Any]]) -> list[list[Fraction]]:
    result = [[q(value) for value in row] for row in rows]
    if not result or any(len(row) != len(result) for row in result):
        raise CertificateError("matrix must be nonempty and square")
    return result


def symmetric(rows: Sequence[Sequence[Any]]) -> list[list[Fraction]]:
    result = matrix(rows)
    if result != K155.transpose(result):
        raise CertificateError("matrix must be exactly symmetric")
    return result


def vector(values: Sequence[Any], size: int) -> list[Fraction]:
    result = [q(value) for value in values]
    if len(result) != size or not any(result):
        raise CertificateError("trial must be nonzero and match the matrix dimension")
    return result


def subtract(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    if len(left) != len(right):
        raise CertificateError("matrix dimensions differ")
    return K155.add(left, K155.scale(Fraction(-1), right))


def bilinear(left: list[Fraction], form: list[list[Fraction]], right: list[Fraction]) -> Fraction:
    return sum(
        (left[i] * form[i][j] * right[j] for i in range(len(form)) for j in range(len(form))),
        Fraction(),
    )


def regular_extension_covariance(
    *, energies: Sequence[Any], couplings: Sequence[Any], charge: tuple[int, int],
    auxiliary_shift: Any, extension_shift: Any,
) -> dict[str, Any]:
    """Verify ``R_E=R_0+E M`` on a complete exact K155 charge block."""
    e = q(extension_shift)
    base = K155.regular_pullback(energies, couplings, charge, auxiliary_shift, 0)
    shifted = K155.regular_pullback(energies, couplings, charge, auxiliary_shift, e)
    if base["U"] != shifted["U"] or base["U_inverse"] != shifted["U_inverse"]:
        raise AssertionError("scalar extension unexpectedly changed the fixed chart")
    inverse = base["U_inverse"]
    metric = K155.matmul(K155.transpose(inverse), inverse)
    predicted = K155.add(base["R"], K155.scale(e, metric))
    if shifted["R"] != predicted:
        raise AssertionError("exact finite pullback violates extension covariance")
    return {
        "dimension": len(metric),
        "extension_shift": qstr(e),
        "physical_metric": metric,
        "chart_independent_of_scalar_extension": True,
        "regular_form_identity": "R_E=R_0+E M",
        "identity_exact": True,
        "finite_control_only": True,
    }


def pencil_covariance(
    *, regular_form: Sequence[Sequence[Any]], metric: Sequence[Sequence[Any]],
    extension_shift: Any, base_parameter: Any,
) -> dict[str, Any]:
    """Compile the exact translated generalized-pencil identity."""
    regular, gram = symmetric(regular_form), symmetric(metric)
    if len(regular) != len(gram):
        raise CertificateError("regular form and metric dimensions differ")
    if K150.inertia(gram) != (0, 0, len(gram)):
        raise CertificateError("metric must be positive definite")
    e, z0 = q(extension_shift), q(base_parameter)
    shifted_regular = K155.add(regular, K155.scale(e, gram))
    left = K155.add(shifted_regular, K155.scale(-(z0 + e), gram))
    right = K155.add(regular, K155.scale(-z0, gram))
    if left != right:
        raise AssertionError("translated pencil identity failed")
    return {
        "base_parameter": qstr(z0),
        "translated_parameter": qstr(z0 + e),
        "identity": "R_E-(z+E)M=R_0-zM",
        "pencil_matrix": [[qstr(value) for value in row] for row in left],
        "inertia": list(K150.inertia(left)),
    }


def trial_covariance(
    *, regular_form: Sequence[Sequence[Any]], metric: Sequence[Sequence[Any]],
    trial: Sequence[Any], extension_shift: Any,
) -> dict[str, Any]:
    """Prove Rayleigh translation and matched residual-covector invariance."""
    regular, gram = symmetric(regular_form), symmetric(metric)
    if len(regular) != len(gram):
        raise CertificateError("regular form and metric dimensions differ")
    if K150.inertia(gram) != (0, 0, len(gram)):
        raise CertificateError("metric must be positive definite")
    u = vector(trial, len(gram))
    norm = bilinear(u, gram, u)
    if norm <= 0:
        raise CertificateError("trial has nonpositive metric norm")
    e = q(extension_shift)
    shifted_regular = K155.add(regular, K155.scale(e, gram))
    rho0 = bilinear(u, regular, u) / norm
    rhoe = bilinear(u, shifted_regular, u) / norm
    residual0 = K155.matmul(K155.add(regular, K155.scale(-rho0, gram)), [[x] for x in u])
    residuale = K155.matmul(K155.add(shifted_regular, K155.scale(-rhoe, gram)), [[x] for x in u])
    if rhoe != rho0 + e or residuale != residual0:
        raise AssertionError("trial translation or residual invariance failed")
    return {
        "metric_norm": qstr(norm),
        "base_rayleigh": qstr(rho0),
        "translated_rayleigh": qstr(rhoe),
        "rayleigh_shift": qstr(e),
        "matched_residual_covector_invariant": True,
        "residual_covector": [qstr(row[0]) for row in residual0],
    }


def complement_covariance(
    *, regular_form: Sequence[Sequence[Any]], metric: Sequence[Sequence[Any]],
    trial: Sequence[Any], base_threshold: Any, extension_shift: Any,
) -> dict[str, Any]:
    """Prove the M-complement and shifted complement form are unchanged."""
    regular, gram = symmetric(regular_form), symmetric(metric)
    if len(regular) != len(gram):
        raise CertificateError("regular form and metric dimensions differ")
    if K150.inertia(gram) != (0, 0, len(gram)):
        raise CertificateError("metric must be positive definite")
    u = vector(trial, len(gram))
    b, e = q(base_threshold), q(extension_shift)
    columns = K165.m_orthogonal_complement(gram, u)
    base_shifted = K155.add(regular, K155.scale(-b, gram))
    translated_regular = K155.add(regular, K155.scale(e, gram))
    translated_shifted = K155.add(translated_regular, K155.scale(-(b + e), gram))
    base_exterior = K165.congruence(base_shifted, columns)
    translated_exterior = K165.congruence(translated_shifted, columns)
    if base_exterior != translated_exterior:
        raise AssertionError("M-orthogonal complement form did not translate covariantly")
    return {
        "complement_kind": "M-orthogonal",
        "complement_dimension": len(columns),
        "translated_threshold": qstr(b + e),
        "complement_form_invariant_at_translated_threshold": True,
        "complement_inertia": list(K150.inertia(base_exterior)),
    }


def absolute_floor_nonidentifiability(*, base_floor: Any, absolute_threshold: Any) -> dict[str, Any]:
    """Give exact scalar extensions placing the same relative floor on either side."""
    floor, threshold = q(base_floor), q(absolute_threshold)
    below_extension = threshold - floor - 1
    above_extension = threshold - floor + 1
    return {
        "base_floor": qstr(floor),
        "absolute_threshold": qstr(threshold),
        "below_extension": qstr(below_extension),
        "below_translated_floor": qstr(floor + below_extension),
        "above_extension": qstr(above_extension),
        "above_translated_floor": qstr(floor + above_extension),
        "absolute_floor_selected_without_extension": False,
        "spectral_gap_is_translation_invariant": True,
    }


def selected_absolute_floor(
    *, base_floor: Any, extension_value: Any | None, extension_selection_ref: str | None,
) -> dict[str, Any]:
    """Fail closed unless the scalar extension value and its owner are supplied."""
    if extension_value is None or not extension_selection_ref:
        raise CertificateError("absolute native floor requires a selected extension value and owner reference")
    return {
        "base_floor": qstr(q(base_floor)),
        "selected_extension": qstr(q(extension_value)),
        "absolute_floor": qstr(q(base_floor) + q(extension_value)),
        "extension_selection_ref": extension_selection_ref,
    }


def k152_coordinate_replay(**refs: str | None) -> dict[str, Any]:
    required_absolute = (
        "full_extension_selection_ref",
        "absolute_anchor_coercivity_ref",
        "absolute_next_distinct_floor_ref",
        "absolute_native_left_floor_ref",
    )
    missing = [name for name in required_absolute if not refs.get(name)]
    return {
        "coordinate_free_form_gram_may_proceed": bool(refs.get("relative_form_and_gram_ref")),
        "matched_form_dual_residual_may_proceed": bool(refs.get("relative_residual_ref")),
        "relative_spectral_gap_may_proceed": bool(refs.get("relative_gap_ref")),
        "missing_absolute_references": missing,
        "native_absolute_packet_complete": not missing,
        "native_K152_absolute_interval_emitted": False,
    }


def demo() -> dict[str, Any]:
    finite = regular_extension_covariance(
        energies=["5/4", "3/2"], couplings=[1, 1], charge=(0, 0),
        auxiliary_shift=256, extension_shift=7,
    )
    regular = [[-2, 1, 1], [1, 6, 0], [1, 0, 5]]
    metric = [[2, 1, 0], [1, 2, 0], [0, 0, 1]]
    pencil = pencil_covariance(
        regular_form=regular, metric=metric, extension_shift=7, base_parameter=0
    )
    trial = trial_covariance(
        regular_form=regular, metric=metric, trial=[1, 0, 0], extension_shift=7
    )
    complement = complement_covariance(
        regular_form=regular, metric=metric, trial=[1, 0, 0],
        base_threshold=0, extension_shift=7,
    )
    replay = k152_coordinate_replay(
        relative_form_and_gram_ref="K162-relative-form",
        relative_residual_ref="K152-relative-residual",
        relative_gap_ref="relative-gap",
        full_extension_selection_ref=None,
        absolute_anchor_coercivity_ref=None,
        absolute_next_distinct_floor_ref=None,
        absolute_native_left_floor_ref=None,
    )
    return {
        "finite_K155_control": {
            "dimension": finite["dimension"],
            "extension_shift": finite["extension_shift"],
            "identity_exact": finite["identity_exact"],
            "finite_control_only": finite["finite_control_only"],
        },
        "translated_pencil": pencil,
        "trial": trial,
        "complement": complement,
        "floor_nonidentifiability": absolute_floor_nonidentifiability(
            base_floor=-4, absolute_threshold=-5
        ),
        "K152_replay": replay,
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if args.demo:
        print(json.dumps(demo(), indent=2, sort_keys=True))
        return 0
    parser.error("use --demo")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
