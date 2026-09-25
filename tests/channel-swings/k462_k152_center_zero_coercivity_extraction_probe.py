#!/usr/bin/env python3
"""Independent controls and hostile mutations for K462."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction

from k462_k152_center_zero_coercivity_extraction import (
    CertificateError,
    chart_transport,
    compose_existential,
    demo,
)


def rejects(thunk) -> bool:
    try:
        thunk()
    except CertificateError:
        return True
    return False


def controls(packet):
    composition = packet.get("continuum_composition", {})
    refs = composition.get("required_references", {})
    constants = packet.get("exact_chart_constants", {})
    control = packet.get("exact_positive_control", {})
    covariance = packet.get("coordinate_covariance", {})
    decision = packet.get("decision", {})
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K462-K152-CENTER-ZERO-COERCIVITY-EXTRACTION"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("K139 semibound", refs.get("K139_uniform_semibound") is True),
        ("K141 continuum", refs.get("K141_fixed_W_continuum_limit") is True),
        ("K168 center zero", refs.get("K168_reference_at_scalar_center_zero") is True),
        ("K153 chart", refs.get("K153_exact_chart") is True),
        ("K156 K162 carrier", refs.get("K156_K162_continuum_carrier") is True),
        ("reducing charge sector", refs.get("complete_charge_sector_reducing") is True),
        ("no missing theorem refs", composition.get("missing_references") == []),
        ("fixed W ref", composition.get("fixed_extension") == "K168 W_ref=diag(-2,1,1)"),
        ("zero coordinate", composition.get("scalar_extension_coordinate") == "0"),
        ("existential semibound", composition.get("existential_center_zero_semiboundedness") is True),
        ("complete sector", composition.get("complete_K162_charge_sector_covered") is True),
        ("no native numeric bound", composition.get("quantitative_regular_lower_bound_serialized") is False),
        ("no quantitative release", composition.get("quantitative_center_zero_coercivity_released") is False),
        ("no Gram evaluation release", composition.get("K457_numerical_evaluation_released") is False),
        ("q", constants.get("q_upper") == "3/8"),
        ("lower chart factor", constants.get("one_minus_q_squared") == "25/64"),
        ("upper chart factor", constants.get("one_plus_q_squared") == "121/64"),
        ("Gram interval", constants.get("gram_interval") == ["64/121", "64/25"]),
        ("control r0", control.get("regular_lower_bound") == "-4"),
        ("control shift", control.get("physical_shift") == "137/16"),
        ("control floor", control.get("physical_coercivity_floor") == "1"),
        ("zero not selected", covariance.get("center_zero_is_physical_selection") is False),
        ("shift covariance", covariance.get("translated_shift") == "s_E=s0-E"),
        ("relative transport", covariance.get("relative_coercivity_family_transports") is True),
        ("no absolute placement", covariance.get("absolute_physical_placement_released") is False),
        ("existential decision", decision.get("existential_center_zero_coercivity_proved") is True),
        ("missing witness retained", decision.get("named_native_lower_bound_witness_present") is False),
        ("no quantitative ref", decision.get("quantitative_center_zero_coercivity_ref_released") is False),
        ("no rank one", decision.get("rank_one_below_b_certificate_present") is False),
        ("no interval", decision.get("native_K152_interval_emitted") is False),
    ]


def hostile_mutations(packet):
    return [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K461"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["continuum_composition"]["required_references"].__setitem__("K139_uniform_semibound", False),
        lambda d: d["continuum_composition"]["required_references"].__setitem__("K141_fixed_W_continuum_limit", False),
        lambda d: d["continuum_composition"]["required_references"].__setitem__("K168_reference_at_scalar_center_zero", False),
        lambda d: d["continuum_composition"]["required_references"].__setitem__("K153_exact_chart", False),
        lambda d: d["continuum_composition"]["required_references"].__setitem__("K156_K162_continuum_carrier", False),
        lambda d: d["continuum_composition"]["required_references"].__setitem__("complete_charge_sector_reducing", False),
        lambda d: d["continuum_composition"].__setitem__("missing_references", ["K141"]),
        lambda d: d["continuum_composition"].__setitem__("fixed_extension", "untyped W"),
        lambda d: d["continuum_composition"].__setitem__("scalar_extension_coordinate", "1"),
        lambda d: d["continuum_composition"].__setitem__("existential_center_zero_semiboundedness", False),
        lambda d: d["continuum_composition"].__setitem__("complete_K162_charge_sector_covered", False),
        lambda d: d["continuum_composition"].__setitem__("quantitative_regular_lower_bound_serialized", True),
        lambda d: d["continuum_composition"].__setitem__("quantitative_center_zero_coercivity_released", True),
        lambda d: d["continuum_composition"].__setitem__("K457_numerical_evaluation_released", True),
        lambda d: d["exact_chart_constants"].__setitem__("q_upper", "1/2"),
        lambda d: d["exact_chart_constants"].__setitem__("one_minus_q_squared", "1/4"),
        lambda d: d["exact_chart_constants"].__setitem__("one_plus_q_squared", "2"),
        lambda d: d["exact_chart_constants"].__setitem__("gram_interval", ["1", "1"]),
        lambda d: d["exact_positive_control"].__setitem__("regular_lower_bound", "-3"),
        lambda d: d["exact_positive_control"].__setitem__("physical_shift", "8"),
        lambda d: d["exact_positive_control"].__setitem__("physical_coercivity_floor", "0"),
        lambda d: d["coordinate_covariance"].__setitem__("center_zero_is_physical_selection", True),
        lambda d: d["coordinate_covariance"].__setitem__("translated_shift", "s_E=s0+E"),
        lambda d: d["coordinate_covariance"].__setitem__("relative_coercivity_family_transports", False),
        lambda d: d["coordinate_covariance"].__setitem__("absolute_physical_placement_released", True),
        lambda d: d["decision"].__setitem__("existential_center_zero_coercivity_proved", False),
        lambda d: d["decision"].__setitem__("named_native_lower_bound_witness_present", True),
        lambda d: d["decision"].__setitem__("quantitative_center_zero_coercivity_ref_released", True),
        lambda d: d["decision"].__setitem__("rank_one_below_b_certificate_present", True),
        lambda d: d["decision"].__setitem__("native_K152_interval_emitted", True),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    packet = demo()
    base = controls(packet)
    print(f"K462 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    if not all(ok for _, ok in base):
        for name, ok in base:
            if not ok:
                print(f"[FAIL] {name}")
        return 1
    if not args.selftest:
        return 0

    mutations = hostile_mutations(packet)
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        if not all(ok for _, ok in controls(candidate)):
            rejected += 1

    analytic_rejections = [
        rejects(lambda: chart_transport(regular_lower_bound=-4, physical_shift=7, contraction_upper=Fraction(3, 8))),
        rejects(lambda: chart_transport(regular_lower_bound=-1, physical_shift=2, contraction_upper=1)),
        rejects(lambda: compose_existential(
            k139_uniform_semibound=False,
            k141_fixed_w_continuum_limit=True,
            k168_reference_at_center_zero=True,
            k153_exact_chart=True,
            k156_k162_continuum_carrier=True,
            complete_charge_sector_reducing=True,
            quantitative_regular_lower_bound=-4,
            quantitative_physical_shift=None,
        )),
    ]
    print(f"K462 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K462 ANALYTIC REJECTIONS: {sum(analytic_rejections)}/{len(analytic_rejections)} rejected")
    return 0 if rejected == len(mutations) and all(analytic_rejections) else 1


if __name__ == "__main__":
    raise SystemExit(main())
