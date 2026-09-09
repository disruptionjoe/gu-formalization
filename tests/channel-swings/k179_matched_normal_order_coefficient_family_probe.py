#!/usr/bin/env python3
"""Exact and hostile controls for the K179 coefficient family."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER_PATH = Path(__file__).with_name("k179_matched_normal_order_coefficient_family.py")
MANIFEST = ROOT / "lab/process/k179-matched-normal-order-coefficient-family-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k179-matched-normal-order-coefficient-family-wave-2026-09-09.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k179_solver", SOLVER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_solver()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    family = data.get("coefficient_family", {})
    signs = data.get("sign_theorem", {})
    control = data.get("order_two_direct_CAR_control", {})
    release = data.get("release_test", {})
    ledger = data.get("ledger_effect", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    if family.get("term_count") != 2958 or family.get("unresolved_required_field_instances") != 0:
        failures.append("family_count")
    if family.get("K178_numerical_admission_passes") is not True:
        failures.append("admission")
    if family.get("family_sha256") != "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686":
        failures.append("family_digest")
    if signs.get("K177_structural_record_alone_included_G_sign") is not False:
        failures.append("K177_sign_ceiling")
    if signs.get("W_exchange_sign") != "(-1)^(n+1) times exact global-CAR contraction sign":
        failures.append("W_sign")
    if control.get("terms") != 6 or control.get("all_compiled_coefficients_match_direct_action") is not True:
        failures.append("order_two_control")
    required_true = (
        "K178_required_fields_populated_for_every_contraction",
        "coefficient_complete_exchange_family_through_order_12_serialized",
        "order_2_direct_finite_CAR_control_passed",
    )
    if any(release.get(key) is not True for key in required_true):
        failures.append("release_positive")
    denied = (
        "outward_numerical_prefix_integrals_evaluated",
        "coefficient_complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "scalar_center_left_floor_serialized",
        "native_K152_interval_emitted",
    )
    if any(release.get(key) is not False for key in denied):
        failures.append("release_fence")
    if ledger != {
        "SC-META-53": "UNCERTAIN_UNCHANGED",
        "LT-SM8": "NEEDS_UNCHANGED",
        "RA-F1": "NEEDS_UNCHANGED",
        "AC-F1": "NEEDS_UNCHANGED",
    }:
        failures.append("ledger")
    if any(data.get(key) is not False for key in (
        "physical_or_source_selection",
        "Born_prediction_or_confirmation_credit",
        "canon_paper_release_or_public_posture_move",
    )):
        failures.append("scope")
    return failures


def exact_checks(data: dict, terms: list[dict]) -> list[tuple[str, bool]]:
    order_two = [term for term in terms if term["order"] == 2]
    order_twelve = [term for term in terms if term["order"] == 12]
    direct = [K179.direct_finite_car_coefficient(term) for term in order_two]
    all_failures = [K179.term_failures(term) for term in terms]
    text = ARTIFACT.read_text()
    return [
        ("manifest exact", not manifest_failures(data)),
        ("all 2958 contractions serialized", len(terms) == 2958),
        ("unique contraction identities", len({term["contraction_id"] for term in terms}) == 2958),
        ("zero unresolved K178 fields", len(K179.K178.missing_coefficient_fields(terms)) == 0),
        ("K178 numerical admission accepts family", _admission_passes(terms)),
        ("every term passes structural validation", all(not row for row in all_failures)),
        ("order one exchange remains zero", not any(term["order"] == 1 for term in terms)),
        ("order two has six terms", len(order_two) == 6),
        ("order twelve has 1152 terms", len(order_twelve) == 1152),
        ("all twelve positive orders represented where nonzero", {term["order"] for term in terms} == set(range(2, 13))),
        ("direct order two controls pass", all(row["passes"] for row in direct)),
        ("order two contains both W signs", {term["exact_operator_coefficient"] for term in order_two} == {"-1", "1"}),
        ("Neumann sign carried", all(term["neumann_word_sign"] == (-1 if term["order"] % 2 else 1) for term in terms)),
        ("W minus X sign carried", all(term["W_equals_scalar_minus_X_sign"] == -1 for term in terms)),
        ("raw and W coefficients opposite", all(int(term["raw_C_R_Cstar_older_contraction_coefficient"]) == -int(term["exact_operator_coefficient"]) for term in terms)),
        ("operator monomials typed", all(term["operator_monomial_id"].startswith("W_ex[") for term in terms)),
        ("impurity matrix units typed", all(term["impurity_matrix_unit"].startswith("|") for term in terms)),
        ("creation resolvent is contracted position", all(term["contracted_resolvent_affine_forms"]["creation_resolvent"] == K179.affine_denominator(term["old_position"]) for term in terms)),
        ("outer resolvent is order plus one", all(term["contracted_resolvent_affine_forms"]["outer_exchange_resolvent"] == K179.affine_denominator(term["order"] + 1) for term in terms)),
        ("contracted incidence includes every later denominator", all(len(term["contracted_resolvent_affine_forms"]["all_denominators_containing_contracted_energy"]) == term["order"] - term["old_position"] + 2 for term in terms)),
        ("point prefactor counts both outer factors", all(term["output_kernel_formula"]["normalization_prefactor"] == f"(2*pi)^(-{term['order'] + 2}/2)" for term in terms)),
        ("old variable integrated", all(term["output_kernel_formula"]["integrated_variable"] == f"p_{term['old_position']}" for term in terms)),
        ("new variable retained", all(term["output_kernel_formula"]["new_variable"] == f"p_{term['order'] + 1}" for term in terms)),
        ("exterior projection after contraction", all(term["output_kernel_formula"]["exterior_projection_applied_after_integration"] is True for term in terms)),
        ("normalized exterior convention", all(term["antisymmetrizer_normalization"]["convention"] == "normalized CAR exterior basis" for term in terms)),
        ("wedge Gram determinant fence", all(term["antisymmetrizer_normalization"]["wedge_inner_product_is_specieswise_determinant"] is True for term in terms)),
        ("canonical family digest", K179.family_digest(terms) == data["coefficient_family"]["family_sha256"]),
        ("family digest is sha256", len(data["coefficient_family"]["family_sha256"]) == 64),
        ("coefficient family is emitted by terms CLI", "--terms emits the canonical expansion" in data["coefficient_family"]["encoding"]),
        ("K177 structural theorem preserved", data["sign_theorem"]["K177_structural_car_sign_preserved"] is True),
        ("K177 G-sign ceiling corrected", data["sign_theorem"]["K177_structural_record_alone_included_G_sign"] is False),
        ("normalization statement present", "n path creations" in data["normalization"]["point_factors"]),
        ("quadrature remains open", data["release_test"]["outward_numerical_prefix_integrals_evaluated"] is False),
        ("action column remains open", data["release_test"]["coefficient_complete_base_action_column_evaluated"] is False),
        ("residual remains open", data["release_test"]["complete_R_ref_form_dual_residual_serialized"] is False),
        ("complement remains open", data["release_test"]["positive_complete_M_orthogonal_complement_or_flux_floor_serialized"] is False),
        ("K152 remains open", data["release_test"]["native_K152_interval_emitted"] is False),
        ("source and physics ledger unchanged", all(value.endswith("_UNCHANGED") for value in data["ledger_effect"].values())),
        ("no physical selection", data["physical_or_source_selection"] is False),
        ("no Born credit", data["Born_prediction_or_confirmation_credit"] is False),
        ("no canon public move", data["canon_paper_release_or_public_posture_move"] is False),
        ("routing notice present", "GU-COMPARATOR-ROUTING" in text),
        ("classification present", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects present", "```gu-typed-objects" in text),
        ("finite CAR control documented", "direct finite CAR" in text),
        ("determinant-level next gate documented", "determinant-level" in text),
    ]


def _admission_passes(terms: list[dict]) -> bool:
    try:
        K179.K178.validate_numerical_admission(terms)
    except K179.K178.CertificateError:
        return False
    return True


def hostile_checks(data: dict, terms: list[dict]) -> list[tuple[str, bool]]:
    mutations: list[tuple[str, Any]] = []
    def term_mutation(name: str, field: str, value: Any) -> None:
        broken = copy.deepcopy(terms[0])
        broken[field] = value
        mutations.append((name, bool(K179.term_failures(broken))))

    for field in K179.K178.REQUIRED_COEFFICIENT_FIELDS:
        term_mutation(f"erase_{field}", field, None)
    term_mutation("flip_coefficient", "exact_operator_coefficient", str(-int(terms[0]["exact_operator_coefficient"])))
    term_mutation("erase_monomial_prefix", "operator_monomial_id", "unknown")
    broken = copy.deepcopy(terms[0]); broken["contracted_resolvent_affine_forms"]["outer_exchange_resolvent"] = "256+E_1"; mutations.append(("wrong_outer_resolvent", bool(K179.term_failures(broken))))
    broken = copy.deepcopy(terms[0]); broken["contracted_resolvent_affine_forms"]["all_denominators_containing_contracted_energy"] = []; mutations.append(("erase_incidence", bool(K179.term_failures(broken))))
    broken = copy.deepcopy(terms[0]); broken["output_kernel_formula"]["normalization_prefactor"] = "1"; mutations.append(("erase_point_normalization", bool(K179.term_failures(broken))))
    broken = copy.deepcopy(terms[0]); broken["antisymmetrizer_normalization"]["convention"] = "unnormalized"; mutations.append(("unnormalized_exterior", bool(K179.term_failures(broken))))
    broken = copy.deepcopy(terms[0]); broken["antisymmetrizer_normalization"]["species_factorials"] = {}; mutations.append(("erase_factorials", bool(K179.term_failures(broken))))

    data_updates = (
        ("invent_quadrature", lambda d: d["release_test"].__setitem__("outward_numerical_prefix_integrals_evaluated", True)),
        ("invent_action", lambda d: d["release_test"].__setitem__("coefficient_complete_base_action_column_evaluated", True)),
        ("invent_residual", lambda d: d["release_test"].__setitem__("complete_R_ref_form_dual_residual_serialized", True)),
        ("invent_complement", lambda d: d["release_test"].__setitem__("positive_complete_M_orthogonal_complement_or_flux_floor_serialized", True)),
        ("invent_K152", lambda d: d["release_test"].__setitem__("native_K152_interval_emitted", True)),
        ("erase_direct_control", lambda d: d["order_two_direct_CAR_control"].__setitem__("all_compiled_coefficients_match_direct_action", False)),
        ("invent_K177_G_sign", lambda d: d["sign_theorem"].__setitem__("K177_structural_record_alone_included_G_sign", True)),
        ("move_ledger", lambda d: d["ledger_effect"].__setitem__("SC-META-53", "RESOLVED")),
        ("invent_source_selection", lambda d: d.__setitem__("physical_or_source_selection", True)),
        ("invent_Born", lambda d: d.__setitem__("Born_prediction_or_confirmation_credit", True)),
        ("invent_public_move", lambda d: d.__setitem__("canon_paper_release_or_public_posture_move", True)),
    )
    for name, update in data_updates:
        broken_data = copy.deepcopy(data)
        update(broken_data)
        mutations.append((name, bool(manifest_failures(broken_data))))
    return mutations


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    terms = K179.coefficient_family()
    checks = exact_checks(data, terms)
    failed = [name for name, ok in checks if not ok]
    if failed:
        print(f"FAIL {len(failed)}/{len(checks)}: {', '.join(failed)}")
        return 1
    if args.selftest:
        hostile = hostile_checks(data, terms)
        missed = [name for name, caught in hostile if not caught]
        if missed:
            print(f"HOSTILE FAIL {len(missed)}/{len(hostile)}: {', '.join(missed)}")
            return 1
        print(f"PASS {len(checks)}/{len(checks)}; hostile {len(hostile)}/{len(hostile)} caught")
        return 0
    print(f"PASS {len(checks)}/{len(checks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
