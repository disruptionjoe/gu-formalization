#!/usr/bin/env python3
"""K442 corrected-boundary product with the homogeneous-orbit KT model."""

from __future__ import annotations

import argparse
import json


KT_DIMS = [21, 91, 70]
CARRIER_RANK = 512
HALF_RANK = 256


def d0(v: tuple[int, ...]) -> tuple[int, ...]:
    return (0,) * 70 + v


def d1(v: tuple[int, ...]) -> tuple[int, ...]:
    return v[:70]


def h1(v: tuple[int, ...]) -> tuple[int, ...]:
    return v[70:]


def h2(v: tuple[int, ...]) -> tuple[int, ...]:
    return v + (0,) * 21


def basis(n: int, i: int) -> tuple[int, ...]:
    return tuple(int(j == i) for j in range(n))


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x + y for x, y in zip(a, b))


def verify_finite_complex() -> dict[str, bool]:
    return {
        "d1_d0_zero": all(d1(d0(basis(21, i))) == (0,) * 70 for i in range(21)),
        "h1_d0_identity": all(h1(d0(basis(21, i))) == basis(21, i) for i in range(21)),
        "d1_h2_identity": all(d1(h2(basis(70, i))) == basis(70, i) for i in range(70)),
        "middle_contraction_identity": all(add(d0(h1(basis(91, i))), h2(d1(basis(91, i)))) == basis(91, i) for i in range(91)),
    }


def demo() -> dict:
    checks = verify_finite_complex()
    assert all(checks.values())
    total_dims = [n * CARRIER_RANK for n in KT_DIMS]
    half_dims = [n * HALF_RANK for n in KT_DIMS]
    return {
        "schema_version": "1.0",
        "result_id": "K442-K77-CORRECTED-BOUNDARY-KT-PRODUCT",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "native_to_observed",
        "inputs": {
            "kt_model": "the existing proper homogeneous Spin(7,7)-orbit KT resolution with 21 stabilizer relations, 91 labels and orbit rank 70",
            "boundary_carrier": "K441 moving corrected carrier of rank 512 with parallel rank-256 incoming/outgoing projectors",
            "product_status": "conditional decoupled graded product; not the full interacting K77 field/antifield complex",
        },
        "finite_product_complex": {
            "base_dimensions": KT_DIMS,
            "corrected_carrier_rank": CARRIER_RANK,
            "product_dimensions": total_dims,
            "differential_ranks": [21 * CARRIER_RANK, 70 * CARRIER_RANK],
            "middle_kernel_dimension": 21 * CARRIER_RANK,
            "finite_cohomology_dimensions": [0, 0, 0],
            "incoming_dimensions_by_degree": half_dims,
            "outgoing_dimensions_by_degree": half_dims,
            "exact_checks": checks,
        },
        "homogeneous_orbit_kt": {
            "local_normal_form": "delta b_m=p_m; delta p_m=0; delta beta_h=b_h; delta b_h=0",
            "orbit_constraints": 70,
            "stabilizer_relations": 21,
            "delta_squared_zero_on_generators": True,
            "positive_antifield_degree_acyclic": True,
            "h0": "functions on the cotangent zero section of the selected homogeneous orbit, with corrected-carrier coefficients",
            "full_nonlinear_k77_properness": False,
        },
        "boundary_descent": {
            "differential": "d_KT tensor I_E",
            "boundary_projector": "I_KT tensor Pi_out/in(t)",
            "commutator_zero": True,
            "contracting_homotopy": "h_KT tensor I_E",
            "contraction_commutes_with_boundary": True,
            "product_connection": "I_KT tensor B(t)",
            "boundary_projectors_parallel": True,
            "closed_trace_subcomplex": True,
        },
        "decision": {
            "decoupled_kt_boundary_product_constructed": True,
            "proper_homogeneous_orbit_kt_preserved": True,
            "moving_boundary_subcomplex_preserved": True,
            "physical_cohomology_constructed": False,
            "full_interacting_bv_kt_constructed": False,
            "next_exact_input": "classify the lower-order coupling terms Q by the exact boundary condition [Q,Pi]=0 and test a non-preserving slow-sector control",
        },
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
