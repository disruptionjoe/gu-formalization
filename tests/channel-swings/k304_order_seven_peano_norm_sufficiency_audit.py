#!/usr/bin/env python3
"""Audit whether the current certificates numerically close the six Peano norms."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K290 = ROOT / "lab/process/k290-order-seven-native-rest-derivative-bank.json"
K300 = ROOT / "lab/process/k300-order-seven-angular-method-selection.json"
K302 = ROOT / "lab/process/k302-order-seven-split-weighted-peano-jet.json"
K303 = ROOT / "lab/process/k303-order-seven-peano-determinant-compiler.json"
OUTPUT = ROOT / "lab/process/k304-order-seven-peano-norm-sufficiency-audit.json"


def route_is_admissible(route: dict[str, Any]) -> bool:
    return bool(
        route["same_measure"]
        and route["global_domain"]
        and route["coherent_before_absolute"]
        and route["split_faces_covered"]
        and not route["uses_superseded_input"]
    )


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k290 = json.loads(K290.read_text())
    k300 = json.loads(K300.read_text())
    k302 = json.loads(K302.read_text())
    k303 = json.loads(K303.read_text())
    patterns = k303["terminal_split_usage"]["pattern_histogram"]
    axes = k303["fixed_control"]["peano_axes"]
    groups = k303["fixed_control"]["coherent_groups"]
    jet_orders = k303["terminal_split_usage"]["required_terminal_jet_orders"]

    routes = {
        "factorized_supremum": {
            "same_measure": True,
            "global_domain": False,
            "coherent_before_absolute": False,
            "split_faces_covered": False,
            "uses_superseded_input": True,
            "status": "rejected",
            "reason": "It would multiply K302's marginal B_m by K290's pointwise multiplier/cofactor ceiling, but K301 supersedes that ceiling on the full split cube and K290 is local to the K284 tube/projective floor.",
        },
        "qualitative_face_transfer": {
            "same_measure": True,
            "global_domain": True,
            "coherent_before_absolute": True,
            "split_faces_covered": True,
            "uses_superseded_input": False,
            "status": "finite_without_number",
            "reason": "K300 plus K302 prove local absolute integrability on a finite boundary cover, but neither supplies outward constants on that cover or their overlap-free composition.",
        },
        "joint_weighted_functionals": {
            "same_measure": True,
            "global_domain": True,
            "coherent_before_absolute": True,
            "split_faces_covered": True,
            "uses_superseded_input": False,
            "status": "selected_next_construction",
            "reason": "Integrate each column-replacement determinant together with its old-kernel, projective, cofactor and split multiplier under the actual axis Peano kernel before absolute group enclosure.",
        },
    }

    template_count = len(patterns) * len(axes) * len(jet_orders)
    instantiated_count = groups * template_count
    y_templates = len(patterns) * len(jet_orders)
    gap_templates = len(patterns) * (len(axes) - 1) * len(jet_orders)
    if template_count != 108 or instantiated_count != 432:
        raise AssertionError("joint functional inventory changed")

    # One complete fixed-(x,q) attempt can be made without K290.  At the
    # simplex barycenter, P=6^-6.  The endpoint-paired old kernels are each
    # <=2/x, the size-four determinant is <=4!*(2/x)^4, and the terminal
    # entry's size-two cofactor is <=2!*(2/x)^2.  Together with pi>3 this
    # leaves C*x^7*q^11*exp(-256*x*(1+q)) before the K302 B_m factor.
    terminal_constant = Fraction(1, 6**9) * Fraction(1, 6**6) * 4 * 384 * 8
    q_factorial = 39916800  # 11!

    return {
        "schema_version": "1.0",
        "result_id": "K304-ORDER-SEVEN-PEANO-NORM-SUFFICIENCY-AUDIT",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k290-order-seven-native-rest-derivative-bank.json",
                "lab/process/k300-order-seven-angular-method-selection.json",
                "lab/process/k302-order-seven-split-weighted-peano-jet.json",
                "lab/process/k303-order-seven-peano-determinant-compiler.json",
            ],
            "peano_axes": axes,
            "companion_patterns": len(patterns),
            "coherent_groups": groups,
            "terminal_jet_orders": jet_orders,
        },
        "concrete_enclosure_attempt": {
            "candidate_inequality": "J_(y,m,terminal)<=B_m(x)*sup|terminal cofactor times undifferentiated old kernels, D4 and native multiplier|",
            "result": "rigorous_at_fixed_x_q_but_radially_nonintegrable",
            "fixed_x_q_bound": {
                "simplex_location": "the y-axis tensor term fixes all five Duffy axes at their means, hence p_i=1/6 and preceding simplex weight 1/120",
                "projective_product": "6^-6",
                "left_and_right_endpoint_safe_values": "each <=2/x",
                "size_four_hadamard": "abs(D4)<=4!*(2/x)^4=384/x^4 because every odd cross sum is at least x",
                "terminal_size_two_cofactor_hadamard": "abs(Cofactor_88)<=2!*(2/x)^2=8/x^2 because deleting row/column 8 leaves cross sums at least x",
                "native_prefactor": "(2*pi)^-9<6^-9",
                "constant_C": fraction_text(terminal_constant),
                "before_Bm": "C*exp(-256*x*(1+q))*x^7*q^11",
                "B0_leaf": "C*exp(-256*x*(1+q))*q^11*x^6",
                "B1_leaf": "C*exp(-256*x*(1+q))*q^11*(x^7/4+2*x^6)",
                "B2_leaf": "C*exp(-256*x*(1+q))*q^11*(3*x^8/8+6*x^6)",
            },
            "exact_q_integration": {
                "identity": "integral_0^infinity q^11*exp(-256*x*q)dq=11!/(256*x)^12",
                "factorial": q_factorial,
                "resulting_x_powers": [-6, -5, -4],
                "radial_origin_integrable": False,
            },
            "exact_failure": "The valid fixed-(x,q) Hadamard enclosure loses the coupled q/x Cauchy--Vandermonde and regularizer structure. Exact q integration creates x^-6, x^-5 and x^-4 radial-origin powers, so this factorization cannot be joined to K294 even for the pure terminal-entry leaf. K290's local/superseded pointwise bank cannot repair that loss.",
            "why_k302_does_not_factor": "B_m integrates only the terminal entry against the y Peano kernel and two terminal split variables. The determinant cofactor, other companion entries and old kernels share y/u/z and may be unbounded on the same faces, so a product of marginal integrals or an unavailable supremum is required; neither follows from K302.",
            "holder_fallback": "not released because no compatible global Lp cofactor/old-kernel moments are serialized under the same Peano measure",
        },
        "route_audit": routes,
        "route_admissibility": {name: route_is_admissible(route) for name, route in routes.items()},
        "minimal_joint_functional_inventory": {
            "definition": "J_(a,m,P,G)=integral K_a(s) |sum of the six signed occurrence column-replacement determinants in coherent group G| times the exact remaining native measure, old kernels and projective weight",
            "axes": len(axes),
            "jet_orders": len(jet_orders),
            "companion_pattern_templates": len(patterns),
            "y_axis_templates": y_templates,
            "five_gap_axis_templates": gap_templates,
            "total_pattern_axis_order_templates": template_count,
            "four_group_instantiations": instantiated_count,
            "compression_rule": "templates may share analytic envelopes only after equality of their cumulative-time supports is proved; the four coherent groups remain signed until the common functional is assembled",
            "k302_supplies_complete_joint_templates": 0,
            "k302_role": "terminal-entry marginal inequalities used inside the 18 y-axis templates, not complete template values",
        },
        "qx_scaling_audit": {
            "native_scalar": "exp(-256*x*(1+q))*x^15*q^11",
            "cauchy_base_scaling": "D4 contributes x^-4, D3 contributes x^-3, and the two endpoint Bessel kernels contribute x^-2, leaving x^6 before regularizer/joint-jet effects",
            "terminal_marginal_scaling": {
                "B0": "x^-1",
                "B1": "x^0 plus x^-1",
                "B2": "x^1 plus x^-1",
            },
            "candidate_terminal_radial_powers": [6, 7, 8],
            "q_boundary": "the raw fixed-(x,q) terminal-leaf majorant keeps only q^11; exact q integration then produces a nonintegrable x^-6 leading power. The size-four Vandermonde q^12 zero and its large-q denominators must remain coupled to x and q inside the joint functional rather than bounded separately",
            "gamma_join_released": False,
            "reason": "The candidate x powers now have a rigorous terminal-leaf coefficient at fixed x,q, but its exact q integral is nonintegrable at x=0. The determinant zeros, denominators and regularizers must be enclosed jointly before a finite gamma coefficient exists.",
        },
        "decision": {
            "all_six_complete_numerical_norms_available": False,
            "positive_peano_route_rejected": False,
            "positive_peano_route_status": "finite_but_not_numerically_closed",
            "k290_pointwise_bank_reinstated": False,
            "k294_gamma_join_released": False,
            "selected_next_exact_input": "construct outward joint weighted column-replacement functionals, beginning with the 18 y-axis pattern/order templates, using K302 inside rather than outside the shared multiplier integral; then extend the same support-aware enclosure to the 90 gap-axis templates",
            "analytic_subtraction_status": k300["method_comparison"]["analytic_subtraction"]["status"],
        },
        "release_test": {
            "factorized_supremum_route_rejected": not route_is_admissible(routes["factorized_supremum"]),
            "joint_weighted_route_admissible": route_is_admissible(routes["joint_weighted_functionals"]),
            "all_missing_functionals_typed": template_count == 108,
            "coherent_groups_not_collapsed": instantiated_count == 432,
            "qualitative_finiteness_preserved": k300["global_legality"]["qualitative_global_remainder_finite"],
            "numerical_norm_overclaim": False,
            "radial_gamma_join_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k302["ledger_effect"],
        "claim_ceiling": "Exact data-sufficiency and closure audit for the K303 six-axis determinant compiler. K302 supplies valid terminal-entry y-Peano marginals but no complete cofactor-weighted norm; K290 cannot provide the missing global multiplier because its pointwise bank is superseded and local. The audit types 108 pattern/axis/order joint-functional templates (432 coherent-group instantiations), preserves K300's qualitative finiteness, and rejects a premature K294 gamma join. It does not reject the positive route, numerically enclose any complete norm, evaluate an exterior action column or residual, emit a native K152 interval, or move source, ledger, canon, paper, public or physical posture.",
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
