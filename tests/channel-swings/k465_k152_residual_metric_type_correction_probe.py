#!/usr/bin/env python3
"""Independent controls and hostile mutations for K465."""

from __future__ import annotations

import copy

from k465_k152_residual_metric_type_correction import demo


def controls(packet):
    identity = packet.get("identity", {})
    exact = packet.get("exact_separation_control", {})
    correction = packet.get("correction", {})
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K465-K152-RESIDUAL-METRIC-TYPE-CORRECTION"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("metric", identity.get("physical_metric") == "M=S^*S"),
        ("M dual", identity.get("serialized_square") == "ell^* M^(-1) ell"),
        ("form dual", identity.get("K152_shifted_form_dual_square") == "ell^* (R+sM)^(-1) ell"),
        ("not identical", identity.get("same_without_additional_bridge") is False),
        ("M control", exact.get("M_dual_square") == "5/6"),
        ("form one", exact.get("shifted_form_one_square") == "5/12"),
        ("form two", exact.get("shifted_form_two_square") == "11/24"),
        ("separation", exact.get("same_M_dual_different_shifted_form_duals") is True),
        ("registry", correction.get("registry_id") == "K457-DUAL-METRIC-20260925"),
        ("payload retained", correction.get("K457_M_dual_payload_retained") is True),
        ("claim retracted", correction.get("K457_shifted_form_dual_serialization_retracted") is True),
        ("no numerics", correction.get("numerical_Gram_evaluation_triggered") is False),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K457"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["identity"].__setitem__("physical_metric", "M=S"),
        lambda d: d["identity"].__setitem__("serialized_square", "ell^*ell"),
        lambda d: d["identity"].__setitem__("K152_shifted_form_dual_square", "ell^*M^-1ell"),
        lambda d: d["identity"].__setitem__("same_without_additional_bridge", True),
        lambda d: d["exact_separation_control"].__setitem__("M_dual_square", "1"),
        lambda d: d["exact_separation_control"].__setitem__("shifted_form_one_square", "5/6"),
        lambda d: d["exact_separation_control"].__setitem__("shifted_form_two_square", "5/12"),
        lambda d: d["exact_separation_control"].__setitem__("same_M_dual_different_shifted_form_duals", False),
        lambda d: d["correction"].__setitem__("registry_id", "NONE"),
        lambda d: d["correction"].__setitem__("K457_M_dual_payload_retained", False),
        lambda d: d["correction"].__setitem__("K457_shifted_form_dual_serialization_retracted", False),
        lambda d: d["correction"].__setitem__("numerical_Gram_evaluation_triggered", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(ok for _, ok in controls(candidate))
    print(f"K465 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K465 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
