#!/usr/bin/env python3
"""K156 regular-core convergence and rank-one exterior-count certificates.

The module compiles exact propagated error bounds.  It does not infer the
missing native exterior floor from finite cutoffs or from an essential edge.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


class CertificateError(ValueError):
    """Raised when supplied bounds do not prove the requested statement."""


def q(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if not isinstance(value, str):
        raise CertificateError("exact inputs must be integers or rational strings")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational value: {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def _load_sibling(name: str):
    path = Path(__file__).with_name(name)
    spec = importlib.util.spec_from_file_location(f"k156_{path.stem}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load sibling module {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_K155 = _load_sibling("k155_finite_regular_pullback.py")
_K150 = _load_sibling("k150_certified_schur_tail_solver.py")


def exact_normal_ordered_cancellation(
    energies: list[Any],
    couplings: list[Any],
    charge: tuple[int, int],
    auxiliary_shift: Any,
    finite_boundary_scalar: Any = 0,
) -> dict[str, Any]:
    """Separate the divergent endpoint contraction from the finite remainder.

    On every K155 cutoff block,
      G* A G = C A^-1 C* = endpoint_contraction + finite_remainder.
    Hence V-lambda-G*AG = (E_R-lambda)I-finite_remainder.  The remainder
    includes diagonal Pauli/spectator terms as well as exchange blocks.
    """
    packet = _K155.regular_pullback(
        energies, couplings, charge, auxiliary_shift, finite_boundary_scalar
    )
    quadratic = _K155.matmul(
        _K155.transpose(packet["G"]),
        _K155.matmul(packet["shifted_free"], packet["G"]),
    )
    size = len(packet["states"])
    boundary = q(finite_boundary_scalar)
    boundary_matrix = _K155.scale(boundary, _K155.identity(size))
    vacuum_contraction = _K155.add(packet["endpoint"], _K155.scale(-1, boundary_matrix))
    finite_remainder = _K155.add(quadratic, _K155.scale(-1, vacuum_contraction))
    renormalized = _K155.add(
        packet["endpoint"],
        _K155.scale(-q(auxiliary_shift), _K155.identity(size)),
        _K155.scale(-1, quadratic),
    )
    expected = _K155.add(
        _K155.scale(boundary - q(auxiliary_shift), _K155.identity(size)),
        _K155.scale(-1, finite_remainder),
    )
    if renormalized != packet["regular_core"] or renormalized != expected:
        raise AssertionError("normal-ordered endpoint cancellation failed")
    return {
        "dimension": size,
        "vacuum_contraction": vacuum_contraction,
        "finite_remainder": finite_remainder,
        "vacuum_remainder_diagonal": finite_remainder[packet["states"].index(0)][packet["states"].index(0)] if 0 in packet["states"] else None,
        "renormalized_core": renormalized,
        "exact_endpoint_cancellation": True,
    }


def propagated_regular_action_tail(
    *,
    free_graph_error: Any,
    boundary_hilbert_error: Any,
    boundary_graph_error: Any,
    regular_core_graph_error: Any,
    chart_contraction: Any,
    graph_chart_contraction: Any,
    regular_core_graph_bound: Any,
) -> dict[str, Fraction]:
    """Propagate common-carrier errors through S* W S.

    W_N and W act from the free graph domain D to Hilbert space.  S_N and S
    are bounded both on Hilbert space and D.  The returned bound dominates
    ||(R_N-R)(H0+a)^-1|| after the stated component bounds are supplied.
    """
    d_a = q(free_graph_error)
    d_g = q(boundary_hilbert_error)
    d_gd = q(boundary_graph_error)
    d_w = q(regular_core_graph_error)
    contraction = q(chart_contraction)
    graph_contraction = q(graph_chart_contraction)
    w_bound = q(regular_core_graph_bound)
    if min(d_a, d_g, d_gd, d_w, w_bound) < 0:
        raise CertificateError("error and operator bounds must be nonnegative")
    if contraction >= 1 or contraction < 0 or graph_contraction >= 1 or graph_contraction < 0:
        raise CertificateError("Hilbert and graph chart contractions must lie in [0,1)")
    alpha = 1 / (1 - contraction)
    beta = 1 / (1 - graph_contraction)
    inverse_hilbert_error = alpha * alpha * d_g
    inverse_graph_error = beta * beta * d_gd
    left_chart = inverse_hilbert_error * w_bound * beta
    core = alpha * d_w * beta
    right_chart = alpha * w_bound * inverse_graph_error
    total = d_a + left_chart + core + right_chart
    return {
        "hilbert_inverse_bound": alpha,
        "graph_inverse_bound": beta,
        "hilbert_inverse_error": inverse_hilbert_error,
        "graph_inverse_error": inverse_graph_error,
        "free_contribution": d_a,
        "left_chart_contribution": left_chart,
        "regular_core_contribution": core,
        "right_chart_contribution": right_chart,
        "total_graph_relative_action_error": total,
    }


def rank_one_exterior_count_certificate(
    *,
    trial_rayleigh: Any,
    count_threshold: Any,
    complete_exterior_floor: Any,
    exterior_floor_ref: str,
    complete_charge_compression: bool,
) -> dict[str, Any]:
    """Certify exactly one spectral value below b by Schur congruence.

    For P=|u><u| and Q=1-P, QHQ>=d>b makes Q(H-b)Q positive.
    The scalar Schur complement is <= <u,Hu>-b<0, so H-b has exactly one
    negative direction.  The proof requires the complete Q compression.
    """
    a, b, d = q(trial_rayleigh), q(count_threshold), q(complete_exterior_floor)
    if not isinstance(exterior_floor_ref, str) or not exterior_floor_ref.strip():
        raise CertificateError("a complete exterior-floor proof reference is required")
    if complete_charge_compression is not True:
        raise CertificateError("the exterior floor must cover the complete charge-sector compression")
    if not a < b < d:
        raise CertificateError("rank-one count requires trial_rayleigh < b < complete_exterior_floor")
    return {
        "trial_rayleigh": qstr(a),
        "count_threshold": qstr(b),
        "complete_exterior_floor": qstr(d),
        "spectral_count_below_threshold": 1,
        "threshold_is_not_spectrum": True,
        "proof": "positive exterior block plus negative scalar Schur complement",
        "exterior_floor_ref": exterior_floor_ref,
    }


def finite_count_control() -> dict[str, Any]:
    """Check the theorem against an exact coupled finite matrix."""
    matrix = [
        [Fraction(0), Fraction(1, 3), Fraction(-1, 4)],
        [Fraction(1, 3), Fraction(3), Fraction(1, 5)],
        [Fraction(-1, 4), Fraction(1, 5), Fraction(4)],
    ]
    threshold = Fraction(1)
    below, equal = _K150.spectral_count(matrix, threshold)
    exterior = [row[1:] for row in matrix[1:]]
    exterior_below, exterior_equal = _K150.spectral_count(exterior, Fraction(2))
    if (below, equal) != (1, 0) or (exterior_below, exterior_equal) != (0, 0):
        raise AssertionError("finite exterior-count control failed")
    return {
        "matrix": [[qstr(x) for x in row] for row in matrix],
        "threshold": qstr(threshold),
        "spectral_count": below,
        "threshold_multiplicity": equal,
        "exterior_is_above_two": True,
        "native_continuum_count": False,
    }


def demo() -> dict[str, Any]:
    cancellation = exact_normal_ordered_cancellation(
        ["5/4", "3/2"], [1, 1], (0, 0), 256
    )
    tail = propagated_regular_action_tail(
        free_graph_error="1/32",
        boundary_hilbert_error="1/64",
        boundary_graph_error="1/48",
        regular_core_graph_error="1/40",
        chart_contraction="3/8",
        graph_chart_contraction="1/2",
        regular_core_graph_bound=3,
    )
    count = rank_one_exterior_count_certificate(
        trial_rayleigh="0",
        count_threshold="1",
        complete_exterior_floor="2",
        exterior_floor_ref="abstract-positive-control#QHQ-ge-2",
        complete_charge_compression=True,
    )
    return {
        "exact_endpoint_cancellation": cancellation["exact_endpoint_cancellation"],
        "finite_dimension": cancellation["dimension"],
        "total_graph_relative_action_error": qstr(tail["total_graph_relative_action_error"]),
        "abstract_count_certificate": count,
        "finite_count_control": finite_count_control(),
        "native_energy_interval_emitted": False,
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
