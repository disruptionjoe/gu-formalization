#!/usr/bin/env python3
"""K158 generalized-pencil and complete-contour budget certificates.

The compiler keeps the singular Hamiltonian ``H`` distinct from its regular
representative ``R = U^(-*) H U^(-1)``.  It emits a native Riesz count only
when regular-action, chart/Gram, and complete reference-resolvent bounds are
all supplied and the resulting outward error is below the K157 threshold.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


class CertificateError(ValueError):
    """Raised when supplied data do not prove the requested certificate."""


def _load(name: str):
    path = Path(__file__).with_name(name)
    spec = importlib.util.spec_from_file_location(f"k158_{path.stem}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K150 = _load("k150_certified_schur_tail_solver.py")
K152 = _load("k152_form_dual_residual_enclosure_solver.py")
K155 = _load("k155_finite_regular_pullback.py")


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


def ceil_q(value: Fraction) -> int:
    return (value.numerator + value.denominator - 1) // value.denominator


def matrix_equal(left, right) -> bool:
    return left == right


def generalized_pencil_identity(charge: tuple[int, int], spectral_parameter: Any = 0) -> dict[str, Any]:
    """Check the exact finite identity underlying the native contour bridge.

    With ``S=U^-1`` and ``M=S* S``, one has
      T(z)=R-zM=U^(-*) (H-z) U^-1,
      T(z)^-1=U (H-z)^-1 U*,
      (H-z)^-1=S T(z)^-1 S*.
    This is a pencil identity, not an isospectrality claim for ``H`` and ``R``.
    """
    z = q(spectral_parameter)
    packet = K155.regular_pullback(["5/4", "3/2"], [1, 1], charge, 256)
    size = len(packet["H"])
    unit = K155.identity(size)
    shifted_h = K155.add(packet["H"], K155.scale(-z, unit))
    s = packet["U_inverse"]
    metric = K155.matmul(K155.transpose(s), s)
    pencil = K155.add(packet["R"], K155.scale(-z, metric))
    congruent = K155.matmul(K155.transpose(s), K155.matmul(shifted_h, s))
    if not matrix_equal(pencil, congruent):
        raise AssertionError("generalized-pencil congruence identity failed")
    if K155.matmul(packet["U"], s) != unit or K155.matmul(s, packet["U"]) != unit:
        raise AssertionError("chart inverse identity failed")
    return {
        "charge": list(charge),
        "dimension": size,
        "spectral_parameter": qstr(z),
        "pencil_identity_exact": True,
        "singular_resolvent_reconstruction_exact": True,
        "H_and_R_called_isospectral": False,
    }


def rectangle_reference_bound(charge: tuple[int, int]) -> dict[str, Any]:
    """Certify a uniform finite-reference resolvent bound on K157's rectangle.

    The horizontal edges are distance 1/2 from every real spectrum.  On the
    right edge x=-1, exact inertia proves an empty rational guard interval:
    [-3/2,-1/2] for q=00 and [-5/4,-3/4] for q=10.  K157's Gershgorin lower
    bounds place the whole finite spectrum to the right of -4, so the left
    edge x=-5 has distance greater than one.
    """
    packet = K155.regular_pullback(["5/4", "3/2"], [1, 1], charge, 256)
    matrix = packet["H"]
    if charge == (0, 0):
        guard = (Fraction(-3, 2), Fraction(-1, 2))
        uniform = Fraction(2)
    elif charge == (1, 0):
        guard = (Fraction(-5, 4), Fraction(-3, 4))
        uniform = Fraction(4)
    else:
        raise CertificateError("K158 reference rectangle covers only representative charges")
    left_count = K150.spectral_count(matrix, guard[0])
    right_count = K150.spectral_count(matrix, guard[1])
    if left_count != (1, 0) or right_count != (1, 0):
        raise AssertionError("right-edge guard interval is not spectrally empty")
    gershgorin = min(
        matrix[i][i]
        - sum((abs(matrix[i][j]) for j in range(len(matrix)) if j != i), Fraction())
        for i in range(len(matrix))
    )
    if not gershgorin > -4:
        raise AssertionError("left-edge unit gap did not close")
    h0_shift_max = max(packet["free"][i][i] + 256 for i in range(len(matrix)))
    finite_graph = h0_shift_max * uniform
    free_tail_graph = Fraction(257, 2)
    complete_graph = max(finite_graph, free_tail_graph)
    chart_upper = Fraction(127, 125)
    for chart in (packet["U"], packet["U_inverse"]):
        if not (
            K155.induced_one_norm(chart) < chart_upper
            and K155.induced_infinity_norm(chart) < chart_upper
        ):
            raise AssertionError("finite chart norm did not fit 127/125")
    pencil_inverse = ceil_q(chart_upper * chart_upper * uniform)
    pencil_graph = ceil_q(h0_shift_max * chart_upper * chart_upper * uniform)
    return {
        "charge": list(charge),
        "right_edge_empty_guard": [qstr(guard[0]), qstr(guard[1])],
        "left_edge_gershgorin_lower": qstr(gershgorin),
        "uniform_reference_resolvent_upper": qstr(uniform),
        "finite_H0_plus_256_upper": qstr(h0_shift_max),
        "free_tail_graph_resolvent_upper": qstr(free_tail_graph),
        "complete_graph_resolvent_upper": qstr(complete_graph),
        "finite_chart_and_inverse_upper": qstr(chart_upper),
        "reference_pencil_inverse_integer_upper": pencil_inverse,
        "reference_pencil_graph_integer_upper": pencil_graph,
    }


def pencil_resolvent_budget(
    *,
    reference_chart_inverse_upper: Any,
    hilbert_chart_error: Any,
    regular_action_error: Any,
    reference_pencil_inverse_upper: Any,
    reference_pencil_graph_upper: Any,
    free_shift: Any = 256,
    contour_modulus_upper: Any = "201/40",
    require_rank_transfer: bool = False,
) -> dict[str, Any]:
    """Propagate regular/pencil data to a singular resolvent error.

    ``regular_action_error`` bounds ``(R-R_N)(H0+a)^-1``.  The chart error
    controls both outer inverse factors and the pencil metric
    ``M=S* S``.  ``reference_graph_resolvent_upper`` bounds
    ``(H0+a)(H_N-z)^-1`` on the complete contour reference.
    """
    s0 = q(reference_chart_inverse_upper)
    dg, tau = q(hilbert_chart_error), q(regular_action_error)
    pencil_inverse_upper = q(reference_pencil_inverse_upper)
    graph_amplification = q(reference_pencil_graph_upper)
    shift, zmax = q(free_shift), q(contour_modulus_upper)
    if min(s0, dg, tau, pencil_inverse_upper, graph_amplification, shift, zmax) < 0 or shift == 0:
        raise CertificateError("errors and bounds must be nonnegative and the shift positive")
    if s0 * dg >= 1:
        raise CertificateError("reference inverse chart cannot bootstrap the native chart")
    native_chart_upper = s0 / (1 - s0 * dg)
    inverse_chart_error = s0 * s0 * dg / (1 - s0 * dg)
    metric_relative_error = (
        (native_chart_upper + s0) * inverse_chart_error / shift
    )
    neumann_parameter = graph_amplification * (
        tau + zmax * metric_relative_error
    )
    if neumann_parameter >= 1:
        if require_rank_transfer:
            raise CertificateError("generalized-pencil Neumann condition does not close")
        return {
            "neumann_parameter": qstr(neumann_parameter),
            "complete_resolvent_error_upper": None,
            "rank_transfer_certified": False,
            "failure": "generalized-pencil Neumann condition does not close",
        }
    eta = pencil_inverse_upper * (
        (native_chart_upper + s0) * inverse_chart_error
        + s0 * native_chart_upper * neumann_parameter
    ) / (1 - neumann_parameter)
    closes = 10 * eta < 6
    if require_rank_transfer and not closes:
        raise CertificateError("complete perimeter-ten resolvent error is not below 3/5")
    return {
        "reference_inverse_chart_upper": qstr(s0),
        "native_inverse_chart_upper": qstr(native_chart_upper),
        "inverse_chart_error_upper": qstr(inverse_chart_error),
        "metric_relative_error_upper": qstr(metric_relative_error),
        "reference_pencil_inverse_upper": qstr(pencil_inverse_upper),
        "graph_amplification_upper": qstr(graph_amplification),
        "neumann_parameter": qstr(neumann_parameter),
        "complete_resolvent_error_upper": qstr(eta),
        "rank_transfer_certified": closes,
    }


def free_graph_boundary_obstruction(auxiliary_shift: Any = 256) -> dict[str, Any]:
    """Prove that a sharp point-boundary tail is not in the free graph norm.

    For ``h(p)=(2*pi)^-1/2 (omega(p)+lambda)^-1``, whenever
    ``omega(p)>=lambda`` one has ``omega/(omega+lambda)>=1/2``.  Therefore
    ``|omega h|^2>=1/(8*pi)`` on an infinite-measure tail.  Removing any
    finite momentum window leaves the same divergence.  Thus the K156
    ``d_GD`` cannot be a finite ``Dom(H0)->Dom(H0)`` norm for this point map.
    """
    shift = q(auxiliary_shift)
    if shift <= 0:
        raise CertificateError("auxiliary shift must be positive")
    return {
        "auxiliary_shift": qstr(shift),
        "point_vector_h_is_L2": True,
        "omega_times_h_is_L2": False,
        "tail_lower_density_when_omega_ge_lambda": "1/(8*pi)",
        "every_finite_cutoff_free_graph_tail_is_infinite": True,
        "G_maps_free_operator_domain_to_itself": False,
        "K156_free_graph_d_GD_is_finite": False,
        "particle_number_graph_bound_substitutes_for_free_graph_bound": False,
    }


def k157_partial_ledger(index: int = 4096) -> dict[str, Any]:
    if index <= 0:
        raise CertificateError("cofinal index must be positive")
    cutoff_tail_sq = Fraction(1, 3 * index)
    cell_error_sq = Fraction(1, 768 * index * index)
    complete_hilbert = 4 * K152.sqrt_upper(cutoff_tail_sq + cell_error_sq, bits=40)
    return {
        "index": index,
        "delta": qstr(Fraction(1, index)),
        "mode_radius": index * index,
        "K157_high_momentum_Hilbert_tail_sq_upper_per_channel": qstr(cutoff_tail_sq),
        "cell_Hilbert_error_sq_upper_per_channel": qstr(cell_error_sq),
        "complete_d_G_upper": qstr(complete_hilbert),
        "complete_d_GD_upper": "infinite_in_the_free_operator_graph_topology",
        "graph_chart_contraction_q_D": None,
        "uniform_regular_core_graph_bound_B": None,
        "complete_d_W_upper": None,
        "complete_tau_upper": None,
        "contour_budget_attempted": False,
        "failure": "K156 free-graph d_GD and q_D premises are false for the sharp point boundary map",
        "native_rank_transfer_certified": False,
    }


def demo() -> dict[str, Any]:
    references = [rectangle_reference_bound((0, 0)), rectangle_reference_bound((1, 0))]
    abstract = []
    for reference in references:
        abstract.append(
            pencil_resolvent_budget(
                reference_chart_inverse_upper=reference["finite_chart_and_inverse_upper"],
                hilbert_chart_error="1/1600",
                regular_action_error="1/1000000",
                reference_pencil_inverse_upper=reference["reference_pencil_inverse_integer_upper"],
                reference_pencil_graph_upper=reference["reference_pencil_graph_integer_upper"],
                require_rank_transfer=True,
            )
        )
    return {
        "schema_version": "1.0",
        "pencil_identities": [generalized_pencil_identity((0, 0)), generalized_pencil_identity((1, 0))],
        "reference_rectangles": references,
        "free_graph_boundary_obstruction": free_graph_boundary_obstruction(),
        "K157_partial_ledger_n4096": k157_partial_ledger(4096),
        "abstract_positive_controls": abstract,
        "native_count_emitted": False,
        "native_energy_interval_emitted": False,
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
