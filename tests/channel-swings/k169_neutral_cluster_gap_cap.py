#!/usr/bin/env python3
"""Exact K169 certificates for the neutral-cluster gap cap.

K143's HVZ formula contains every compatible escaping cluster.  In a fixed
``(q1,q2)`` sector, one particle and one hole of the same flavor have net
charge zero and energy infimum ``2*tau``.  A translated two-particle Weyl
sequence is asymptotically orthogonal to every finite trial space, so the
complete physical complement margin above any variational ground trial is at
most ``2*tau``.  The K139 chart carries physical orthogonality to
``M=S* S``-orthogonality without changing this bound.

For the fixed massive control ``tau=5/4``, the cap is ``5/2 < 3``.  Thus
K168's three-unit base-to-reference transfer condition cannot certify the
complete gap.  This does not obstruct a direct certificate for ``R_ref`` at a
smaller positive gap.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent


def _load_k150():
    path = HERE / "k150_certified_schur_tail_solver.py"
    spec = importlib.util.spec_from_file_location("k169_k150", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load exact dependency at {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K150 = _load_k150()
Matrix = list[list[Fraction]]


class CertificateError(ValueError):
    """Raised when inputs do not certify the K169 conclusion."""


def q(value: Any) -> Fraction:
    try:
        return value if isinstance(value, Fraction) else Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational input: {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def transpose(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix, strict=True)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    right_t = transpose(right)
    return [
        [sum((x * y for x, y in zip(row, column, strict=True)), Fraction()) for column in right_t]
        for row in left
    ]


def matvec(matrix: Matrix, vector: list[Fraction]) -> list[Fraction]:
    return [sum((x * y for x, y in zip(row, vector, strict=True)), Fraction()) for row in matrix]


def dot(left: list[Fraction], right: list[Fraction]) -> Fraction:
    return sum((x * y for x, y in zip(left, right, strict=True)), Fraction())


def neutral_cluster_threshold(rest_mass: Any = Fraction(5, 4)) -> dict[str, Any]:
    tau = q(rest_mass)
    if tau <= 0:
        raise CertificateError("particle/hole rest mass must be positive")
    cluster_energy = 2 * tau
    return {
        "particle_charge": [1, 0],
        "hole_charge": [-1, 0],
        "cluster_charge": [0, 0],
        "cluster_particle_number": 2,
        "single_escape_energy_infimum": qstr(tau),
        "neutral_cluster_energy_infimum": qstr(cluster_energy),
        "fixed_total_charge_preserved": True,
        "HVZ_threshold_membership": "E_ref(q)+2*tau belongs to the threshold set",
        "first_threshold_identified": False,
        "local_reference_extension_changes_escape_cost": False,
    }


def finite_trial_complement_cap(rest_mass: Any, trial_rayleigh: Any, ground_energy: Any) -> dict[str, Any]:
    tau, rho, ground = q(rest_mass), q(trial_rayleigh), q(ground_energy)
    if tau <= 0:
        raise CertificateError("rest mass must be positive")
    if rho < ground:
        raise CertificateError("a variational trial Rayleigh value cannot lie below the ground")
    threshold = ground + 2 * tau
    margin_cap = threshold - rho
    return {
        "ground_energy": qstr(ground),
        "trial_rayleigh": qstr(rho),
        "neutral_threshold": qstr(threshold),
        "complete_complement_margin_upper": qstr(margin_cap),
        "universal_margin_upper": qstr(2 * tau),
        "finite_codimension_Weyl_sequence_survives_projection": True,
        "applies_to_every_finite_K162_trial_space": True,
        "identifies_actual_complement_floor": False,
    }


def chart_transport() -> dict[str, Any]:
    return {
        "physical_chart": "S=(1-G_256)^-1",
        "regular_metric": "M=S* S",
        "physical_trial_space": "S P",
        "physical_orthogonal_complement": "(S P)^perp",
        "regular_coordinate_complement": "P^(perp_M)",
        "equivalence": "v in P^(perp_M) iff S v in (S P)^perp",
        "free_Hilbert_complement_substituted": False,
        "gap_cap_preserved_under_chart": True,
    }


def transfer_disposition(rest_mass: Any = Fraction(5, 4), shape_oscillation: Any = 3) -> dict[str, Any]:
    tau, oscillation = q(rest_mass), q(shape_oscillation)
    cap = 2 * tau
    if oscillation <= 0:
        raise CertificateError("shape oscillation must be positive")
    return {
        "rest_mass": qstr(tau),
        "neutral_cluster_gap_cap": qstr(cap),
        "K168_shape_oscillation": qstr(oscillation),
        "strict_transfer_condition": "base complete margin > shape oscillation",
        "strict_transfer_condition_attainable": cap > oscillation,
        "comparison": "2*tau < osc(W_ref)" if cap < oscillation else "2*tau >= osc(W_ref)",
        "direct_base_to_reference_gap_transfer": False if cap <= oscillation else True,
        "direct_reference_specific_K152_route_open": True,
        "base_form_or_Gram_evaluation_would_change_transfer_verdict": False,
    }


def direct_reference_positive_control() -> dict[str, Any]:
    """A nonidentity-metric control with a valid gap below three.

    With ``L=[[1,1,0],[0,1,0],[0,0,1]]``, use
    ``M=L^T L`` and ``R=L^T diag(-1,1,3)L``.  The generalized spectrum is
    ``(-1,1,3)``.  The exact ground vector is ``e1`` and its M-orthogonal
    complement is spanned by ``(-1,1,0)`` and ``e3``.
    """
    metric: Matrix = [
        [Fraction(1), Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(2), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]
    form: Matrix = [
        [Fraction(-1), Fraction(-1), Fraction(0)],
        [Fraction(-1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(3)],
    ]
    trial = [Fraction(1), Fraction(0), Fraction(0)]
    residual = [r + m for r, m in zip(matvec(form, trial), matvec(metric, trial), strict=True)]
    complement = [
        [Fraction(-1), Fraction(0)],
        [Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1)],
    ]
    shifted_complement = matmul(transpose(complement), matmul(form, complement))
    full_inertia = K150.inertia(form)
    complement_inertia = K150.inertia(shifted_complement)
    if residual != [Fraction(), Fraction(), Fraction()]:
        raise AssertionError("positive control trial is not an exact generalized eigenvector")
    if dot(trial, matvec(metric, [row[0] for row in complement])) != 0:
        raise AssertionError("first complement vector is not M-orthogonal")
    if dot(trial, matvec(metric, [row[1] for row in complement])) != 0:
        raise AssertionError("second complement vector is not M-orthogonal")
    return {
        "metric": [[qstr(value) for value in row] for row in metric],
        "form": [[qstr(value) for value in row] for row in form],
        "generalized_spectrum": ["-1", "1", "3"],
        "ground_to_next_gap": "2",
        "gap_exceeds_three": False,
        "trial_generalized_rayleigh": "-1",
        "matched_residual": [qstr(value) for value in residual],
        "threshold": "0",
        "M_orthogonal_complement_inertia": list(complement_inertia),
        "full_pencil_inertia": list(full_inertia),
        "exactly_one_below_threshold": full_inertia == (1, 0, 2),
        "native_K139_data": False,
    }


def native_k152_replay() -> dict[str, Any]:
    return {
        "three_unit_transfer_route": "KILLED_BY_NATIVE_NEUTRAL_CLUSTER_GAP_CAP",
        "direct_reference_route": "OPEN",
        "required_next_references": [
            "same limiting R_ref form evaluation",
            "physical Gram M evaluation",
            "complete R_ref form-dual residual",
            "reference-specific positive M-orthogonal complement or flux certificate",
            "reference-specific next-distinct floor below the neutral-cluster threshold",
            "native left floor at a selected scalar center",
        ],
        "native_reference_form_evaluated": False,
        "native_same_form_packet_complete": False,
        "native_ground_count_emitted": False,
        "native_K152_interval_emitted": False,
    }


def demo() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "arithmetic": "exact_rational_HVZ_charge_and_generalized_congruence_control",
        "neutral_cluster": neutral_cluster_threshold(),
        "finite_trial_complement": finite_trial_complement_cap(Fraction(5, 4), -1, -1),
        "K139_chart_transport": chart_transport(),
        "K168_transfer_disposition": transfer_disposition(),
        "direct_reference_positive_control": direct_reference_positive_control(),
        "native_K152_replay": native_k152_replay(),
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
