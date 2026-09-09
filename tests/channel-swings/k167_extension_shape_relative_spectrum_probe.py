#!/usr/bin/env python3
"""Probe and hostile checks for K167 extension-shape classification."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k167_extension_shape_relative_spectrum.py")
MANIFEST = ROOT / "lab/process/k167-extension-shape-relative-spectrum-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k167-extension-shape-relative-spectrum-wave-2026-09-09.md"

spec = importlib.util.spec_from_file_location("k167_solver", SOLVER)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def failures(data: dict) -> list[str]:
    out: list[str] = []
    dec = data.get("extension_decomposition", {})
    rel = data.get("relative_spectral_classification", {})
    ctl = data.get("exact_controls", {})
    ref = data.get("K162_reference_contract", {})
    phys = data.get("source_and_physics", {})
    required_true = [
        (dec, "W_equals_E_identity_plus_W0"), (dec, "E_equals_trace_W_over_dimension"),
        (dec, "trace_W0_equals_zero"), (dec, "decomposition_unique"),
        (dec, "scalar_center_pulls_back_as_E_M"),
        (rel, "scalar_center_preserves_matched_residuals"),
        (rel, "scalar_center_preserves_relative_generalized_gaps"),
        (rel, "scalar_center_preserves_complement_forms_at_translated_thresholds"),
        (ref, "declared_complete_non_scalar_extension_required"),
        (ref, "fixed_chart_required"), (ref, "same_complete_form_reference_required"),
        (ref, "physical_selection_requires_supplied_full_rank_response_or_action_owner"),
    ]
    for obj, key in required_true:
        if obj.get(key) is not True: out.append(f"{key} must be true")
    required_false = [
        (rel, "traceless_shape_preserves_matched_residuals_in_general"),
        (rel, "traceless_shape_preserves_relative_generalized_gaps_in_general"),
        (rel, "traceless_shape_preserves_complement_positivity_at_trial_translated_thresholds_in_general"),
        (ref, "conditional_repository_reference_is_physical_selection"),
        (ref, "complete_response_datum_supplied"), (ref, "action_owned_full_extension_supplied"),
        (ctl, "finite_controls_are_native_K162_anchors"),
    ]
    for obj, key in required_false:
        if obj.get(key) is not False: out.append(f"{key} must be false")
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY": out.append("classification")
    if data.get("target_claim") != "NONE-NOT-A-KILL": out.append("target claim")
    if phys.get("SC_META_53_polarity") != "UNCERTAIN": out.append("SC-META-53")
    for key in ("LT_SM8_verdict", "RA_F1_verdict", "AC_F1_verdict"):
        if phys.get(key) != "NEEDS": out.append(key)
    if phys.get("physical_or_source_selection") is not False: out.append("physical selection")
    if phys.get("Born_prediction_or_confirmation_credit") is not False: out.append("credit")
    return out


def run() -> list[str]:
    checks: list[str] = []
    data = json.loads(MANIFEST.read_text())
    assert failures(data) == []; checks.append("manifest contract")
    center, shape = module.decompose_center_shape(module.diagonal([4, 1, -2]))
    assert center == 1 and [shape[i][i] for i in range(3)] == [3, 0, -3]; checks.append("center/shape exact")
    scalar = module.scalar_center_control()
    assert scalar["pullback_identity"] and scalar["residual_invariant"] and scalar["relative_gap_invariant"]; checks.append("scalar covariance")
    assert scalar["rayleigh_translation"] == ["-1", "6"]; checks.append("scalar Rayleigh translation")
    off = module.offdiagonal_shape_control()
    assert off["metric_diagonal"] == ["4", "1", "1"]; checks.append("physical Gram")
    assert off["rayleigh_t0"] == off["rayleigh_t2"] == "-1"; checks.append("fixed Rayleigh control")
    assert off["residual_t0"] == ["0", "0", "0"] and off["residual_t2"] == ["0", "4", "0"]; checks.append("residual shape change")
    assert off["generalized_spectrum_t2"] == ["-2", "3", "5"]; checks.append("shape spectrum exact")
    assert [off["ground_gap_t0"], off["ground_gap_t2"]] == ["3", "5"]; checks.append("relative gap changes")
    comp = module.complement_shape_control()
    assert comp["complement_diagonal_t0"] == ["3", "6"]; checks.append("base complement exact")
    assert comp["complement_diagonal_t2"] == ["-1", "4"]; checks.append("shape complement exact")
    assert comp["complement_positive_t0"] and not comp["complement_positive_t2"]; checks.append("complement route switch")
    assert not comp["translated_threshold_complement_invariant"]; checks.append("translation insufficient")
    contract = module.reference_extension_contract(extension_ref="W0", chart_ref="S", complete_form_ref="R")
    assert contract["conditional_reference_complete"] and not contract["physical_selection_proved"]; checks.append("conditional reference contract")
    try:
        module.reference_extension_contract(extension_ref=None, chart_ref="S", complete_form_ref="R")
    except module.CertificateError: checks.append("missing extension rejected")
    else: raise AssertionError("missing extension accepted")
    try:
        module.reference_extension_contract(extension_ref="W0", chart_ref="S", complete_form_ref="R", claim_physical_selected=True)
    except module.CertificateError: checks.append("false physical selection rejected")
    else: raise AssertionError("false physical selection accepted")
    selected = module.reference_extension_contract(extension_ref="W", chart_ref="S", complete_form_ref="R", claim_physical_selected=True, full_rank_response_ref="K140#datum")
    assert selected["physical_selection_proved"] and selected["absolute_axis_selected"]; checks.append("supplied response route")
    text = ARTIFACT.read_text()
    for needle in ("GU-COMPARATOR-ROUTING", "Classification: INTERNAL_STRUCTURAL_ONLY.", "```gu-typed-objects", "target_claim: NONE-NOT-A-KILL", "not a native K162 anchor", "SC-META-53", "LT-SM8", "RA-F1", "AC-F1"):
        assert needle in text; checks.append(f"artifact {needle}")
    return checks


def hostile() -> int:
    base = json.loads(MANIFEST.read_text())
    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("target_claim", "SC-META-53"),
        lambda d: d["extension_decomposition"].__setitem__("trace_W0_equals_zero", False),
        lambda d: d["extension_decomposition"].__setitem__("scalar_center_pulls_back_as_E_M", False),
        lambda d: d["relative_spectral_classification"].__setitem__("traceless_shape_preserves_matched_residuals_in_general", True),
        lambda d: d["relative_spectral_classification"].__setitem__("traceless_shape_preserves_relative_generalized_gaps_in_general", True),
        lambda d: d["relative_spectral_classification"].__setitem__("traceless_shape_preserves_complement_positivity_at_trial_translated_thresholds_in_general", True),
        lambda d: d["exact_controls"].__setitem__("finite_controls_are_native_K162_anchors", True),
        lambda d: d["K162_reference_contract"].__setitem__("declared_complete_non_scalar_extension_required", False),
        lambda d: d["K162_reference_contract"].__setitem__("conditional_repository_reference_is_physical_selection", True),
        lambda d: d["K162_reference_contract"].__setitem__("complete_response_datum_supplied", True),
        lambda d: d["K162_reference_contract"].__setitem__("action_owned_full_extension_supplied", True),
        lambda d: d["source_and_physics"].__setitem__("SC_META_53_polarity", "ASSERTS"),
        lambda d: d["source_and_physics"].__setitem__("physical_or_source_selection", True),
        lambda d: d["source_and_physics"].__setitem__("Born_prediction_or_confirmation_credit", True),
    ]
    caught = 0
    for mutate in mutations:
        data = copy.deepcopy(base); mutate(data)
        caught += bool(failures(data))
    assert caught == len(mutations)
    print(f"K167 HOSTILE: {caught}/{len(mutations)} planted mutations caught")
    return caught


if __name__ == "__main__":
    checks = run()
    print(f"K167 PASS: {len(checks)}/{len(checks)} checks")
    if "--selftest" in sys.argv: hostile()
