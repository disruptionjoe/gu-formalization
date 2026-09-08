#!/usr/bin/env python3
"""Exact and hostile controls for the K153 conforming-core compiler."""

from __future__ import annotations

import argparse
import copy
import json
from fractions import Fraction
from pathlib import Path

from k153_neumann_chart_conforming_core_solver import (
    CertificateError,
    DEMO,
    certify_contraction,
    coarse_chart_residual_norm,
    coercive_floor,
    cutoff_inverse_tail,
    finite_cutoff_word_tail,
    gram_spectral_bounds,
    hilbert_to_form_dual_residual_sq,
    k152_ready,
    neumann_tail,
    q,
    signed_point_h2_upper,
    solve,
    validate_native_chart,
)


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k153-neumann-chart-conforming-core-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k153-neumann-chart-conforming-core-wave-2026-09-08.md"


def rejects(callable_) -> bool:
    try:
        callable_()
    except CertificateError:
        return True
    return False


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    fixed = data.get("fixed_control", {})
    core = data.get("conforming_core", {})
    pullback = data.get("pullback_form_and_gram", {})
    residual = data.get("coercivity_and_residual", {})
    transport = data.get("charge_transport", {})
    audit = data.get("native_input_audit", {})
    bounds = data.get("boundaries", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        failures.append("classification")
    if data.get("direction") != "observed_to_native":
        failures.append("direction")
    required_fixed = {
        "coefficient_l1": 4,
        "auxiliary_chart_shift": 256,
        "contraction_upper": "3/8",
        "auxiliary_shift_is_physical_parameter": False,
        "physically_selected": False,
    }
    if any(fixed.get(key) != value for key, value in required_fixed.items()):
        failures.append("fixed control")
    required_core = {
        "native_vectors": "psi_i=U_lambda^-1 phi_i",
        "charge_preserved_by_boundary_map": True,
        "bare_cutoff_vector_is_automatically_conforming": False,
        "neumann_tail": "q^(J+1)/(1-q)||phi||",
        "cutoff_inverse_tail": "delta_N/(1-q)^2||phi||",
        "raw_point_field_norm_required": False,
    }
    if any(core.get(key) != value for key, value in required_core.items()):
        failures.append("conforming core")
    required_pullback = {
        "operator_identity": "H=U_lambda^* R_lambda U_lambda",
        "form_identity": "a(U_lambda^-1 phi_i,U_lambda^-1 phi_j)=r_lambda(phi_i,phi_j)",
        "infinite_form_tail_required_after_pullback": False,
        "fixed_control_gram_interval": ["64/121", "64/25"],
        "form_and_gram_are_the_same_matrix": False,
    }
    if any(pullback.get(key) != value for key, value in required_pullback.items()):
        failures.append("pullback")
    if residual.get("regular_action_data_required") is not True:
        failures.append("regular action")
    if residual.get("next_distinct_spectrum_floor_proved") is not False:
        failures.append("gap fence")
    if residual.get("coarse_residual_automatically_closes_K152") is not False:
        failures.append("residual fence")
    if transport.get("q10_to_q01_requires_signed_flavor_unitary") is not True:
        failures.append("flavor transport")
    if transport.get("verbal_equal_coupling_is_sufficient") is not False or transport.get("particle_hole_complement_is_used") is not False:
        failures.append("transport fence")
    required_true = (
        "q00_conforming_seed_constructed",
        "q10_conforming_seed_constructed",
        "uniform_native_gram_conditioning_proved",
        "native_form_tail_removed_by_exact_pullback",
    )
    required_false = (
        "regular_charge_sector_matrix_and_action_serialized",
        "native_dual_residual_closing_bound_serialized",
        "native_next_distinct_spectrum_lower_bound_serialized",
        "native_energy_interval_emitted",
    )
    if any(audit.get(key) is not True for key in required_true) or any(audit.get(key) is not False for key in required_false):
        failures.append("native audit")
    denied = (
        "numerical_native_residual_energies",
        "complete_charge_sector_point_spectrum",
        "complete_native_threshold_or_Gram_margins",
        "native_full_Fock_Mourre_or_scattering",
        "many_body_asymptotic_completeness",
        "NESS_or_current",
        "physical_parameter_or_state_selection",
        "Weinstein_source_or_GU_action_owner",
        "Born_rule_derived",
        "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if any(bounds.get(key) is not False for key in denied):
        failures.append("boundary")
    if bounds.get("canon_verdict_change") != "none" or bounds.get("paper_release_or_public_posture_change") != "none":
        failures.append("external boundary")
    return failures


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    result = solve(copy.deepcopy(DEMO))
    native = copy.deepcopy(DEMO["native_input"])
    complete = {
        **native,
        "regular_form_action_data_ref": "fixture#regular-action",
        "coercive_shift_proof_ref": "fixture#coercivity",
        "dual_residual_proof_ref": "fixture#residual",
        "next_distinct_spectrum_floor_ref": "fixture#gap",
    }
    h2 = signed_point_h2_upper(256)
    contraction = certify_contraction(256, 4, "3/8")
    return [
        ("schema", data.get("schema_version") == "1.0"),
        ("manifest contracts", not manifest_failures(data)),
        ("fixed two-edge control", data["fixed_control"]["oriented_edges"] == [[0, 1], [0, 2]]),
        ("h2 bound exact", h2 == Fraction(3, 257 * 257) + Fraction(2, 257)),
        ("strict norm square", contraction["boundary_map_norm_sq_upper"] < Fraction(9, 64)),
        ("contraction accepted", contraction["contraction_upper"] == Fraction(3, 8)),
        ("inverse norm", q(result["inverse_norm_upper"]) == Fraction(8, 5)),
        ("Gram spectral bounds", gram_spectral_bounds("3/8") == (Fraction(64, 121), Fraction(64, 25))),
        ("demo Gram bounds", list(map(q, result["orthonormal_core_gram_spectrum"])) == [Fraction(64, 121), Fraction(64, 25)]),
        ("word tail", neumann_tail("3/8", 8) == Fraction(19683, 83886080)),
        ("word tail serialized", q(result["neumann_word_tail_upper"]) == Fraction(19683, 83886080)),
        ("cutoff inverse", cutoff_inverse_tail("3/8", "1/1000") == Fraction(8, 3125)),
        ("combined tail", finite_cutoff_word_tail("3/8", "1/1000", 8) == Fraction(8, 3125) + Fraction(19683, 83886080)),
        ("positive regular coercivity", coercive_floor(2, 0, "3/8") == Fraction(25, 32)),
        ("negative regular coercivity", coercive_floor(-1, 2, "3/8") == Fraction(7, 64)),
        ("dual residual embedding", hilbert_to_form_dual_residual_sq("1/8", "7/64") == Fraction(1, 7)),
        ("demo residual", q(result["form_dual_residual_sq_upper"]) == Fraction(1, 7)),
        ("coarse residual exact", coarse_chart_residual_norm(1, 1, "3/8") == Fraction(119, 40)),
        ("native chart accepted", validate_native_chart(native)),
        ("native chart serialized", result["native_chart_contract_satisfied"] is True),
        ("K152 incomplete", result["k152_native_contract_complete"] is False),
        ("K152 complete fixture", k152_ready(complete)),
        ("no native energy", result["native_energy_interval_emitted"] is False),
        ("no raw point norm", result["raw_point_field_norm_used"] is False),
        ("reject nonpositive chart shift", rejects(lambda: signed_point_h2_upper(0))),
        ("reject underclaimed contraction", rejects(lambda: certify_contraction(256, 4, "1/4"))),
        ("reject closed contraction", rejects(lambda: neumann_tail(1, 2))),
        ("reject negative word order", rejects(lambda: neumann_tail("3/8", -1))),
        ("reject negative cutoff error", rejects(lambda: cutoff_inverse_tail("3/8", -1))),
        ("reject nonpositive coercivity", rejects(lambda: hilbert_to_form_dual_residual_sq(1, 0))),
        ("reject native missing refs", rejects(lambda: validate_native_chart({"claim_native_chart": True, "charge_sector": [0, 0]}))),
        ("reject wrong charge", rejects(lambda: validate_native_chart({**native, "charge_sector": [2, 0]}))),
        ("reject q01 without transport", rejects(lambda: validate_native_chart({**native, "charge_sector": [0, 1]}))),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("chart coordinate fence", "not a physical\nsmall-coupling claim" in text),
        ("explicit native vectors", "psi_i=U_256^-1 phi_i=sum_(j>=0) G_256^j phi_i" in text),
        ("tail formula", "q^(J+1)/(1-q)||phi_i||" in text),
        ("form identity", "a(psi_i,psi_j)=r_256(phi_i,phi_j)" in text),
        ("form-tail correction", "there is no independent infinite\nform-matrix tail to serialize" in text),
        ("Gram interval", "64/121 I <= M <= 64/25 I" in text),
        ("coercivity sign split", "r0<0" in text),
        ("dual residual", "||(H+s)^(-1/2)(H-rho)psi||^2 <= eta^2/c" in text),
        ("native interval absent", "K153 emits no native energy interval" in text),
        ("next regular gate", "Serialize the regular `R_256` form and action" in text),
        ("holdout fence", data.get("held_out") == "delayed-choice entanglement swapping, reserved_unscored"),
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
        print(f"FAIL baseline: {failed}")
        return 1
    if not args.selftest:
        print(f"PASS {len(baseline)}/{len(baseline)} K153 exact controls")
        return 0

    manifest_mutations = [
        lambda d: d["fixed_control"].__setitem__("auxiliary_chart_shift", 1),
        lambda d: d["fixed_control"].__setitem__("contraction_upper", "1"),
        lambda d: d["fixed_control"].__setitem__("auxiliary_shift_is_physical_parameter", True),
        lambda d: d["conforming_core"].__setitem__("bare_cutoff_vector_is_automatically_conforming", True),
        lambda d: d["conforming_core"].__setitem__("raw_point_field_norm_required", True),
        lambda d: d["pullback_form_and_gram"].__setitem__("infinite_form_tail_required_after_pullback", True),
        lambda d: d["pullback_form_and_gram"].__setitem__("form_and_gram_are_the_same_matrix", True),
        lambda d: d["coercivity_and_residual"].__setitem__("regular_action_data_required", False),
        lambda d: d["coercivity_and_residual"].__setitem__("next_distinct_spectrum_floor_proved", True),
        lambda d: d["coercivity_and_residual"].__setitem__("coarse_residual_automatically_closes_K152", True),
        lambda d: d["charge_transport"].__setitem__("verbal_equal_coupling_is_sufficient", True),
        lambda d: d["charge_transport"].__setitem__("particle_hole_complement_is_used", True),
        lambda d: d["native_input_audit"].__setitem__("regular_charge_sector_matrix_and_action_serialized", True),
        lambda d: d["native_input_audit"].__setitem__("native_energy_interval_emitted", True),
        lambda d: d["boundaries"].__setitem__("complete_native_threshold_or_Gram_margins", True),
        lambda d: d["boundaries"].__setitem__("native_full_Fock_Mourre_or_scattering", True),
        lambda d: d["boundaries"].__setitem__("Weinstein_source_or_GU_action_owner", True),
        lambda d: d["boundaries"].__setitem__("Born_rule_derived", True),
    ]
    prose_mutations = [
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING", 1),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", "", 1),
        text.replace("```gu-typed-objects", "```text", 1),
        text.replace("not a physical\nsmall-coupling claim", "a physical small-coupling claim", 1),
        text.replace("psi_i=U_256^-1 phi_i=sum_(j>=0) G_256^j phi_i", "psi_i=phi_i", 1),
        text.replace("q^(J+1)/(1-q)||phi_i||", "0", 1),
        text.replace("a(psi_i,psi_j)=r_256(phi_i,phi_j)", "a=M", 1),
        text.replace("there is no independent infinite\nform-matrix tail to serialize", "sum every form tail", 1),
        text.replace("64/121 I <= M <= 64/25 I", "M=I", 1),
        text.replace("||(H+s)^(-1/2)(H-rho)psi||^2 <= eta^2/c", "residual=0", 1),
        text.replace("K153 emits no native energy interval", "K153 emits a native energy interval", 1),
        text.replace("Serialize the regular `R_256` form and action", "No regular action is needed", 1),
    ]
    caught = 0
    missed: list[str] = []
    for index, mutate in enumerate(manifest_mutations, start=1):
        trial = copy.deepcopy(data)
        mutate(trial)
        if any(not ok for _, ok in checks(trial, text)):
            caught += 1
        else:
            missed.append(f"manifest-{index}")
    for index, trial_text in enumerate(prose_mutations, start=1):
        if any(not ok for _, ok in checks(data, trial_text)):
            caught += 1
        else:
            missed.append(f"prose-{index}")
    total = len(manifest_mutations) + len(prose_mutations)
    if caught != total:
        print(f"FAIL hostile selftest caught {caught}/{total}; missed {missed}")
        return 1
    print(f"PASS hostile selftest caught {caught}/{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
