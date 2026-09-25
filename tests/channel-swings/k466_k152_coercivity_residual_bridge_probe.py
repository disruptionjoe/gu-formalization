#!/usr/bin/env python3
"""Independent controls and hostile mutations for K466."""

from __future__ import annotations

import copy
from fractions import Fraction

from k466_k152_coercivity_residual_bridge import bridge, demo


def controls(packet):
    theorem = packet.get("theorem", {})
    exact = packet.get("nonidentity_metric_control", {})
    sharp = packet.get("sharp_control", {})
    native = packet.get("native_status", {})
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K466-K152-COERCIVITY-RESIDUAL-BRIDGE"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("hypothesis", theorem.get("hypothesis") == "R+sM >= cM > 0"),
        ("inverse", theorem.get("inverse_order") == "(R+sM)^(-1) <= c^(-1) M^(-1)"),
        ("quantitative", theorem.get("requires_quantitative_c") is True),
        ("M dual", exact.get("M_dual_square") == "5"),
        ("form dual", exact.get("shifted_form_dual_square") == "17/12"),
        ("ceiling", exact.get("bridge_ceiling") == "5/3"),
        ("bound", exact.get("bound_holds") is True),
        ("sharp", sharp.get("equality_holds") is True),
        ("K463", native.get("K463_formula_can_supply_c") is True),
        ("no native c", native.get("native_quantitative_c_serialized") is False),
        ("no numeric residual", native.get("K152_shifted_residual_numerically_bounded") is False),
    ]


def invalid_rejections() -> int:
    rejected = 0
    for c, shifted in [(Fraction(0), (Fraction(6), Fraction(12))), (Fraction(3), (Fraction(5), Fraction(12)))]:
        try:
            bridge((Fraction(2), Fraction(3)), shifted, (Fraction(2), Fraction(3)), c)
        except ValueError:
            rejected += 1
    return rejected


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K465"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["theorem"].__setitem__("hypothesis", "R+sM >= 0"),
        lambda d: d["theorem"].__setitem__("inverse_order", "M^-1 <= A^-1"),
        lambda d: d["theorem"].__setitem__("requires_quantitative_c", False),
        lambda d: d["nonidentity_metric_control"].__setitem__("M_dual_square", "17/12"),
        lambda d: d["nonidentity_metric_control"].__setitem__("shifted_form_dual_square", "5"),
        lambda d: d["nonidentity_metric_control"].__setitem__("bridge_ceiling", "5"),
        lambda d: d["nonidentity_metric_control"].__setitem__("bound_holds", False),
        lambda d: d["sharp_control"].__setitem__("equality_holds", False),
        lambda d: d["native_status"].__setitem__("K463_formula_can_supply_c", False),
        lambda d: d["native_status"].__setitem__("native_quantitative_c_serialized", True),
        lambda d: d["native_status"].__setitem__("K152_shifted_residual_numerically_bounded", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(ok for _, ok in controls(candidate))
    invalid = invalid_rejections()
    print(f"K466 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K466 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K466 INVALID INPUTS: {invalid}/2 rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) and invalid == 2 else 1


if __name__ == "__main__":
    raise SystemExit(main())
