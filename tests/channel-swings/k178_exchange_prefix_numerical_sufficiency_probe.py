#!/usr/bin/env python3
"""Baseline-first exact and hostile controls for K178."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k178_exchange_prefix_numerical_sufficiency.py")
MANIFEST = ROOT / "lab/process/k178-exchange-prefix-numerical-sufficiency-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k178-exchange-prefix-numerical-sufficiency-wave-2026-09-09.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k178_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K178 = load_solver()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    fixed = data.get("fixed_control", {})
    if fixed.get("maximum_resolved_order") != 12 or fixed.get("auxiliary_chart_shift") != 256:
        failures.append("fixed_control")
    compiler = data.get("structural_compiler", {})
    expected = {
        "path_records": 633,
        "path_signature_blocks": 198,
        "contraction_records": 2958,
        "contraction_signature_blocks": 201,
        "ambiguous_multi_record_contraction_signature_blocks": 173,
        "order_2_contraction_records": 6,
        "order_2_contraction_signature_blocks": 6,
        "unresolved_coefficient_fields_per_contraction": 5,
        "unresolved_coefficient_field_instances": 14790,
    }
    if any(compiler.get(key) != value for key, value in expected.items()):
        failures.append("compiler_census")
    admission = data.get("numerical_admission_contract", {})
    if admission.get("required_coefficient_fields") != list(K178.REQUIRED_COEFFICIENT_FIELDS):
        failures.append("required_fields")
    for key in ("current_k177_family_rejected", "positive_complete_control_accepted"):
        if admission.get(key) is not True:
            failures.append(key)
    for key in ("census_or_generic_formula_is_sufficient", "occupation_signature_alone_is_a_cancellation_group"):
        if admission.get(key) is not False:
            failures.append(key)
    control = data.get("nonidentifiability_control", {})
    if control.get("quadratic_values") != ["1", "4"] or control.get("values_differ") is not True:
        failures.append("nonidentifiability")
    if control.get("native_coefficient_selected") is not False:
        failures.append("native_selection_fence")
    release = data.get("release_test", {})
    for key in ("k177_representation_class_preserved", "complete_structural_skeleton_compiled"):
        if release.get(key) is not True:
            failures.append(key)
    for key in (
        "coefficient_complete_integral_family_serialized",
        "outward_numerical_prefix_integrals_evaluated",
        "coefficient_complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "scalar_center_left_floor_serialized",
        "native_K152_interval_emitted",
    ):
        if release.get(key) is not False:
            failures.append(key)
    return failures


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    result = K178.demo()
    compiler = result["structural_compiler"]
    admission = result["numerical_admission_contract"]
    control = result["nonidentifiability_control"]
    release = result["release_test"]
    order_two = compiler["by_order"][2]
    order_twelve = compiler["by_order"][12]
    incomplete = K178.contraction_records()
    missing = K178.missing_coefficient_fields(incomplete)
    rejected = False
    try:
        K178.validate_numerical_admission(incomplete)
    except K178.CertificateError:
        rejected = True
    positive = K178.positive_control_term()
    accepted = True
    try:
        K178.validate_numerical_admission([positive])
    except K178.CertificateError:
        accepted = False
    return [
        ("schema", result["schema_version"] == "1.0"),
        ("manifest", not manifest_failures(data)),
        ("path records", compiler["path_records"] == 633),
        ("path blocks", compiler["path_signature_blocks"] == 198),
        ("contraction records", compiler["contraction_records"] == 2958),
        ("contraction blocks", compiler["contraction_signature_blocks"] == 201),
        ("ambiguous blocks", compiler["ambiguous_multi_record_contraction_signature_blocks"] == 173),
        ("order two records", order_two["contraction_records"] == 6),
        ("order two blocks", order_two["contraction_signature_blocks"] == 6),
        ("order twelve records", order_twelve["contraction_records"] == 1152),
        ("order twelve blocks", order_twelve["contraction_signature_blocks"] == 33),
        ("five required fields", len(K178.REQUIRED_COEFFICIENT_FIELDS) == 5),
        ("missing field instances", len(missing) == 14790),
        ("current rejected direct", rejected),
        ("current rejected demo", admission["current_k177_family_rejected"] is True),
        ("positive accepted direct", accepted),
        ("positive accepted demo", admission["positive_complete_control_accepted"] is True),
        ("census insufficient", admission["census_or_generic_formula_is_sufficient"] is False),
        ("signature insufficient", admission["occupation_signature_alone_is_a_cancellation_group"] is False),
        ("same skeleton", control["shared_structural_skeleton"] is True),
        ("same generic Gram", control["shared_generic_heat_kernel_gram"] is True),
        ("different values", control["quadratic_values"] == ["1", "4"] and control["values_differ"] is True),
        ("control not native", control["native_coefficient_selected"] is False),
        ("K177 preserved", release["k177_representation_class_preserved"] is True),
        ("skeleton complete", release["complete_structural_skeleton_compiled"] is True),
        ("family incomplete", release["coefficient_complete_integral_family_serialized"] is False),
        ("numerics open", release["outward_numerical_prefix_integrals_evaluated"] is False),
        ("action open", release["coefficient_complete_base_action_column_evaluated"] is False),
        ("residual open", release["complete_R_ref_form_dual_residual_serialized"] is False),
        ("complement open", release["positive_complete_M_orthogonal_complement_or_flux_floor_serialized"] is False),
        ("center open", release["scalar_center_left_floor_serialized"] is False),
        ("K152 open", release["native_K152_interval_emitted"] is False),
        ("owner named", result["next_exact_input"]["owner"] == "K156 matched finite-cutoff normal ordering"),
        ("quadrature ordered", result["next_exact_input"]["must_precede"] == "determinant-aware outward quadrature"),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("correction preserved", "K177's representation theorem remains exact" in text),
        ("coefficient fence", "does not serialize a coefficient-complete integral family" in text),
        ("ledger fence", all(value.endswith("_UNCHANGED") for value in result["ledger_effect"].values())),
        ("no source selection", result["physical_or_source_selection"] is False),
        ("no export credit", result["Born_prediction_or_confirmation_credit"] is False),
        ("no posture move", result["canon_paper_release_or_public_posture_move"] is False),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text()
    baseline = checks(data, text)
    failed = [name for name, ok in baseline if not ok]
    if failed:
        print(f"FAIL baseline {len(baseline)-len(failed)}/{len(baseline)}: {failed}")
        return 1
    if not args.selftest:
        print(f"PASS {len(baseline)}/{len(baseline)} K178 exact controls")
        return 0

    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["fixed_control"].__setitem__("maximum_resolved_order", 11),
        lambda d: d["structural_compiler"].__setitem__("path_records", 632),
        lambda d: d["structural_compiler"].__setitem__("path_signature_blocks", 197),
        lambda d: d["structural_compiler"].__setitem__("contraction_records", 2957),
        lambda d: d["structural_compiler"].__setitem__("contraction_signature_blocks", 200),
        lambda d: d["structural_compiler"].__setitem__("ambiguous_multi_record_contraction_signature_blocks", 172),
        lambda d: d["structural_compiler"].__setitem__("order_2_contraction_records", 5),
        lambda d: d["structural_compiler"].__setitem__("unresolved_coefficient_fields_per_contraction", 4),
        lambda d: d["structural_compiler"].__setitem__("unresolved_coefficient_field_instances", 14789),
        lambda d: d["numerical_admission_contract"].__setitem__("required_coefficient_fields", []),
        lambda d: d["numerical_admission_contract"].__setitem__("current_k177_family_rejected", False),
        lambda d: d["numerical_admission_contract"].__setitem__("positive_complete_control_accepted", False),
        lambda d: d["numerical_admission_contract"].__setitem__("census_or_generic_formula_is_sufficient", True),
        lambda d: d["numerical_admission_contract"].__setitem__("occupation_signature_alone_is_a_cancellation_group", True),
        lambda d: d["nonidentifiability_control"].__setitem__("quadratic_values", ["1", "1"]),
        lambda d: d["nonidentifiability_control"].__setitem__("native_coefficient_selected", True),
        lambda d: d["release_test"].__setitem__("k177_representation_class_preserved", False),
        lambda d: d["release_test"].__setitem__("coefficient_complete_integral_family_serialized", True),
        lambda d: d["release_test"].__setitem__("outward_numerical_prefix_integrals_evaluated", True),
        lambda d: d["release_test"].__setitem__("coefficient_complete_base_action_column_evaluated", True),
        lambda d: d["release_test"].__setitem__("complete_R_ref_form_dual_residual_serialized", True),
        lambda d: d["release_test"].__setitem__("native_K152_interval_emitted", True),
    ]
    caught = 0
    for mutate in mutations:
        mutant = copy.deepcopy(data)
        mutate(mutant)
        if manifest_failures(mutant):
            caught += 1
    prose_mutants = [
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING"),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", ""),
        text.replace("```gu-typed-objects", "```text"),
        text.replace("K177's representation theorem remains exact", "K177 is rejected"),
        text.replace("does not serialize a coefficient-complete integral family", "serializes a coefficient-complete integral family"),
    ]
    for mutant in prose_mutants:
        if any(not ok for _, ok in checks(data, mutant)):
            caught += 1
    expected = len(mutations) + len(prose_mutants)
    if caught != expected:
        print(f"FAIL hostile {caught}/{expected}")
        return 1
    print(f"PASS hostile {caught}/{expected} mutations caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
