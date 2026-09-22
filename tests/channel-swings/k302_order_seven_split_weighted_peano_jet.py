#!/usr/bin/env python3
"""Build Peano-weighted terminal split Bessel jet bounds through order two."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K299 = ROOT / "lab/process/k299-order-seven-positive-peano-simplex-rule.json"
K301 = ROOT / "lab/process/k301-order-seven-terminal-split-boundary-correction.json"
OUTPUT = ROOT / "lab/process/k302-order-seven-split-weighted-peano-jet.json"


def build() -> dict[str, Any]:
    k299 = json.loads(K299.read_text())
    k301 = json.loads(K301.read_text())
    if not k301["companion_census"]["all_24_contain_terminal_8_8_entry"]:
        raise AssertionError("K301 terminal census changed")
    if k299["one_dimensional_factors"][-1]["axis"] != "y":
        raise AssertionError("K299 y Peano factor changed")
    return {
        "schema_version": "1.0",
        "result_id": "K302-ORDER-SEVEN-SPLIT-WEIGHTED-PEANO-JET",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k299-order-seven-positive-peano-simplex-rule.json",
                "lab/process/k301-order-seven-terminal-split-boundary-correction.json",
            ],
            "terminal_argument": "w=x*z with z=y*a+(1-y)*b, a=1-u3, b=1-z3",
            "native_domain": "x>0; y,a,b in [0,1]",
            "peano_kernel": "K(y)=y^2/2 for y<=1/2 and (1-y)^2/2 for y>=1/2",
            "maximum_y_derivative_order": 2,
        },
        "bessel_jet_inequalities": {
            "order_0": "2*K1(w)<=2/w",
            "order_1_recurrence": "abs((2*K1)'(w))=K0(w)+K2(w)<=1/w+2/w^2",
            "order_2_recurrence": "(2*K1)''(w)=(3*K1(w)+K3(w))/2<=3/(2*w)+4/w^3",
            "inputs": [
                "K0(w)<=K1(w)",
                "w^nu*K_nu(w)<=2^(nu-1)*(nu-1)! for integer nu>=1",
                "all absolute derivative signs follow complete monotonicity of K1",
            ],
        },
        "exact_split_integrals": {
            "I0": "integral_[0,1]^2 da db/(y*a+(1-y)*b)=-log(y)/(1-y)-log(1-y)/y",
            "J2": "integral_[0,1]^2 2*(a-b)^2/(y*a+(1-y)*b)^3 da db=2*(I(y,1-y)+I(1-y,y))",
            "I(A,B)": "[3/2+1/(2*A^2)-2/A-log(A)]/B^3 for A+B=1",
            "endpoint_behavior": "K(y)*I0(y)->0 and K(y)*J2(y)->1/2 as y->0 or 1",
            "midpoint_control": "K(1/2)*J2(1/2)=4*log(2)-2<4/5",
        },
        "universal_weighted_bounds": {
            "definition": "B_m(x)=integral_0^1 K(y) integral_[0,1]^2 abs(d_y^m[2*K1(x*(y*a+(1-y)*b))]) da db dy",
            "B0": {"upper": "1/x", "strict": True},
            "B1": {"upper": "1/4+2/x", "strict": True},
            "B2": {"upper": "3*x/8+6/x", "strict": True},
            "proof_partition": {
                "K_over_z": "with m=min(y,1-y), z>=m*(a+b) and K=m^2/2, K/z<=1/[4*(a+b)]",
                "first_derivative_terms": "K*abs(a-b)/z<=1/4 and K*abs(a-b)/z^2<=1/[2*(a+b)]",
                "second_derivative_linear_term": "K*(a-b)^2/z<=m*(a+b)/2<= (a+b)/4",
                "second_derivative_cubic_term": "K*J2<=3 by symmetry and the y<=1/2 split: y^2*I(y,1-y)<=1 and y^2*I(1-y,y)<=2",
                "elementary_integral": "integral_[0,1]^2 da db/(a+b)=2*log(2)<2",
            },
        },
        "complete_split_face_transfer": {
            "worst_entry": "the (8,8) companion entry; every other companion entry adds nonnegative cumulative-time support",
            "monotonicity": "K1 and its alternating absolute derivatives decrease when nonnegative support is added",
            "all_24_occurrences_covered": True,
            "pointwise_uniform_bound_required": False,
            "terminal_split_face_peano_weighted_integrable": True,
            "k300_projective_face_result_composed": True,
        },
        "decision": {
            "k301_pointwise_defect_repaired_for_y_peano_jet": True,
            "k290_uniform_pointwise_bank_reinstated": False,
            "k291_k293_numerical_remainders_reinstated": False,
            "positive_peano_route_retained": True,
            "complete_six_coherent_norms_computed": False,
            "next_exact_input": "compose B0/B1/B2 with the complete companion determinant cofactors, old kernels, common size-four determinant, native density and q/x integration for the y Peano term; then enclose the five Duffy-gap terms with the K296 face factors",
        },
        "release_test": {
            "no_split_cutoff": True,
            "all_three_terminal_jet_orders_bounded": True,
            "pointwise_unboundedness_not_misreported_as_divergence": True,
            "complete_exterior_integrand_bound_emitted": False,
            "radial_gamma_join_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k301["ledger_effect"],
        "claim_ceiling": "Exact Peano-kernel-weighted split-integrated bounds through y-derivative order two for the worst terminal (8,8) companion Bessel entry in every K288 occurrence: B0<1/x, B1<1/4+2/x and B2<3x/8+6/x. This repairs K301's pointwise split-boundary defect for the K299 y-axis method without reinstating K290's uniform pointwise bank or K291/K293's numerical remainders. Determinant/coherent composition, the other five Peano norms, q/x integration, K294 gamma join, exterior action-column value, residual, K152 interval, source/ledger move, canon, paper, public and physical claims remain open.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build(), indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
