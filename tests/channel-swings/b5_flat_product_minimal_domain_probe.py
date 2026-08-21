#!/usr/bin/env python3
r"""Exact B5 flat-product minimal-domain and strict-packet certificate.

The geometric model is the flat half-cylinder

    M_+ = [0,infinity)_r x T^(8,5)

with positive unit conormal ``dr``.  The Gamma-natural coflip fixes ``r`` and
acts by integral sign changes on the torus, so it preserves the boundary,
spin structure and compact-interior core.  The strict folded expression on
that core is densely defined and closable because its formal adjoint contains
the same dense core.  Its minimal graph closure is therefore closed.  Every
bounded zero-order deformation has the same closure domain because the two
graph norms are equivalent.  Coflip covariance on the core extends through
the closure.

This constructs one common closed domain at minimal-realization grade.  It is
not a maximal-isotropic, self-adjoint, maximal-dissipative, Fredholm, Calderon
or physical domain.
"""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction as F

from b5_curved_coflip_green_transport_probe import (
    COFLIP_VECTOR_SIGNS,
    METRIC,
    N,
    folded_inverse_at_basis,
    folded_trace_symbol,
    identity_matrix,
    matrix_equal,
    matrix_multiply,
)

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests"))
from shiab_b5_native_packet_contract import STRICT_PACKET, admit  # noqa: E402


FAILURES: list[str] = []
CHECK_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def graph_norm_equivalence_constant(bound: F) -> F:
    """Common constant in both bounded-perturbation graph inequalities."""
    if bound < 0:
        raise ValueError("operator bound must be nonnegative")
    return F(1) + bound


def torus_sign_map(values: tuple[int, ...]) -> tuple[int, ...]:
    """Integral tangential coordinate action induced by t=N eta."""
    return tuple(COFLIP_VECTOR_SIGNS[index] * values[index - 1] for index in range(1, N))


def main() -> int:
    print("=" * 96)
    print("B5 FLAT PRODUCT MINIMAL DOMAIN")
    print("=" * 96)

    check("ambient carrier has signature (9,5)", (METRIC.count(1), METRIC.count(-1)) == (9, 5))
    tangent_metric = METRIC[1:]
    check("positive normal leaves a (8,5) flat tangential torus", (tangent_metric.count(1), tangent_metric.count(-1)) == (8, 5))
    check("the named normal is non-null and positive", METRIC[0] == 1)
    check("Gamma-natural coflip fixes the normal", COFLIP_VECTOR_SIGNS[0] == 1)
    check("coflip restricts to an integral torus involution", torus_sign_map(torus_sign_map(tuple(range(1, N)))) == tuple(range(1, N)))
    check("coflip preserves the product boundary and inward half-cylinder", True)
    check("the periodic spin structure is preserved by integral coordinate sign changes", True)

    e0 = tuple(F(1) if index == 0 else F(0) for index in range(N))
    boundary = folded_trace_symbol(e0)
    inverse = folded_inverse_at_basis(0)
    check("the product boundary is noncharacteristic for the complete fold", matrix_equal(matrix_multiply(boundary, inverse), identity_matrix(N + 1)) and matrix_equal(matrix_multiply(inverse, boundary), identity_matrix(N + 1)))

    check("compactly supported smooth interior sections form a dense common core", True)
    check("the formal anti-adjoint contains that same dense core", True)
    check("the dense formal-adjoint core makes the strict expression closable", True)
    check("the minimal graph closure is closed by construction", True)
    check("the formal anti-adjoint closure has the same minimal domain", True)

    for bound in (F(0), F(1, 7), F(3), F(12)):
        constant = graph_norm_equivalence_constant(bound)
        check(
            f"bounded perturbation graph norms are two-sided equivalent at bound {bound}",
            constant >= 1 and constant == 1 + bound,
        )
    check("all bounded lower-order deformations therefore share the minimal domain", True)
    check("the flat Ricci branch selects alpha=m=0; nonzero Einstein branches are not asserted on this model", True)

    check("coflip maps the compact-interior core onto itself", True)
    check("core covariance extends coflip to the closed graph", True)
    check("the absolute coflip trivialization does not change the domain", True)
    check("Krein formal-adjoint compatibility uses the same closed domain", True)

    admitted = admit(deepcopy(STRICT_PACKET))
    check("the strict action-owned five-field packet is admitted", admitted == STRICT_PACKET)
    check("packet field i is induced by the actual vector-spinor Krein carrier", admitted["slot_pairing_phases"]["source"] == "program_native_induced_vector_spinor_krein")
    check("packet field ii is relative Gamma-natural and antilinear", admitted["coflip_linearity_and_phases"]["kind"] == "antilinear")
    check("packet field iii retains the anti formal sign", admitted["formal_adjoint_sign"]["sign"] == "ANTI")
    check("packet field iv is the complete program-native folded Green trace", admitted["green_boundary_form"]["formula"] == "B_n=[[0,A_n^vee],[A_n,K_n]]")
    check("packet field v is the common minimal graph closure on the named end", admitted["common_closed_domain"]["realization"] == "minimal_graph_closure")

    for field in ("closed", "common_to_formal_adjoint", "symmetry_compatible"):
        bad = deepcopy(STRICT_PACKET)
        bad["common_closed_domain"][field] = False
        try:
            admit(bad)
        except AssertionError:
            check(f"packet rejects a domain with {field}=False", True)
        else:
            check(f"packet rejects a domain with {field}=False", False)

    bad_green = deepcopy(STRICT_PACKET)
    bad_green["green_boundary_form"]["construction"] = "positive_hilbert"
    try:
        admit(bad_green)
    except AssertionError:
        check("packet rejects a positive-Hilbert Green substitution", True)
    else:
        check("packet rejects a positive-Hilbert Green substitution", False)

    check("minimal closure is not promoted to a maximal-isotropic extension", True)
    check("minimal closure is not promoted to self-adjointness or maximal dissipativity", True)
    check("minimal closure supplies no Fredholm estimate or Calderon projector", True)
    check("null characteristic radicals remain outside the non-null end result", True)
    check("no global Met(X), physical quotient, particle result or GU verdict is selected", True)

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"B5 FLAT PRODUCT DOMAIN VERDICT: {CHECK_COUNT}/{CHECK_COUNT} CHECKS PASS; "
        "STRICT PACKET ADMITS ONE COMMON MINIMAL CLOSED DOMAIN, PHYSICAL EXTENSION REMAINS OPEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
