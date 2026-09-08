#!/usr/bin/env python3
"""Exact and hostile controls for the K152 form-dual certificate."""

from __future__ import annotations

import argparse
import copy
import json
from fractions import Fraction
from pathlib import Path

from k152_form_dual_residual_enclosure_solver import (
    CertificateError,
    DEMO,
    DEMO_FORM,
    DEMO_GRAM,
    DEMO_RESIDUAL_SQ,
    DEMO_SHIFT,
    DEMO_VECTOR,
    add,
    congruence,
    dual_temple_ground_enclosure,
    finite_form_dual_residual_sq,
    form_intertwines,
    form_pencil,
    isolate_generalized_eigenvalue,
    matmul,
    q,
    rayleigh_quotient,
    solve,
    transpose,
    validate_native_contract,
)


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k152-form-dual-residual-lower-enclosure-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k152-form-dual-residual-lower-enclosure-wave-2026-09-08.md"


def rejects(callable_) -> bool:
    try:
        callable_()
    except CertificateError:
        return True
    return False


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    pencil = data.get("generalized_form_pencil", {})
    dual = data.get("shifted_dual_residual_certificate", {})
    charge = data.get("charge_transport", {})
    native = data.get("native_input_audit", {})
    bounds = data.get("boundaries", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        failures.append("classification")
    if data.get("direction") != "observed_to_native":
        failures.append("direction")
    required_pencil = {
        "gram_requirement": "M positive definite",
        "arithmetic": "exact rational or outward-certified rational input",
        "spectral_count": "inertia(A-xM)",
        "ordered_ritz_isolation": "exact rational bisection",
        "basis_covariant_under": "(A,M)->(T*AT,T*MT) for invertible T",
        "bare_finite_cutoff_basis_is_automatically_native_conforming": False,
        "floating_point_eigensigns_are_certificate_inputs": False,
    }
    if any(pencil.get(key) != value for key, value in required_pencil.items()):
        failures.append("pencil")
    required_dual = {
        "coercivity_requirement": "H+s>=c>0",
        "dual_residual_square": "epsilon2=||(H+s)^(-1/2)(H-rho)u||^2",
        "gap": "g=b-rho",
        "energy_parameter": "E=(rho+s)epsilon2",
        "correction": "Delta=(E+sqrt(E^2+4g^2E))/(2g)",
        "ground_interval": "[rho-Delta,rho]",
        "projection_error": "eta_P<=sqrt(epsilon2*(b+s)/(b-rho)^2)",
        "square_root_rounding": "outward dyadic upper",
        "raw_Hilbert_point_coupling_norm_required": False,
        "finite_core_dual_residual_alone_is_native_residual": False,
        "unproved_exterior_gap_is_accepted": False,
    }
    if any(dual.get(key) != value for key, value in required_dual.items()):
        failures.append("dual")
    required_charge = (
        "requires_signed_unitary",
        "requires_Hilbert_pairing_intertwining",
        "requires_form_intertwining",
        "requires_trial_space_transport",
        "requires_dual_residual_transport",
        "requires_exterior_gap_transport",
    )
    if any(charge.get(key) is not True for key in required_charge):
        failures.append("charge")
    if charge.get("verbal_equal_coupling_is_sufficient") is not False or charge.get("particle_hole_complement_is_used") is not False:
        failures.append("charge fence")
    required_native_true = (
        "K139_proves_transformed_common_domain_and_norm_resolvent_limit",
        "K151_proves_finite_regulator_charge_blocks_and_signed_flavor_intertwiner",
    )
    required_native_false = (
        "q00_transformed_native_form_gram_serialized",
        "q10_transformed_native_form_gram_serialized",
        "native_dual_residual_bound_serialized",
        "native_next_distinct_spectrum_lower_bound_serialized",
        "native_interval_emitted",
    )
    if any(native.get(key) is not True for key in required_native_true) or any(native.get(key) is not False for key in required_native_false):
        failures.append("native audit")
    denied = (
        "native_q00_or_q10_form_matrix_emitted",
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
    lower, upper = map(q, result["ground_interval"])
    projection = q(result["ground_eigenspace_projection_error_upper"])
    correction = q(result["dual_temple_correction_upper"])
    transform = [[Fraction(1), Fraction(1)], [Fraction(0), Fraction(1)]]
    inverse = [[Fraction(1), Fraction(-1)], [Fraction(0), Fraction(1)]]
    form = [[Fraction(-1), Fraction(0)], [Fraction(0), Fraction(2)]]
    gram = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    changed_form = congruence(form, transform)
    changed_gram = congruence(gram, transform)
    changed_vector = [Fraction(3, 4), Fraction(1, 4)]
    original_ritz = isolate_generalized_eigenvalue(form, gram, 1, -2, 0)
    changed_ritz = isolate_generalized_eigenvalue(changed_form, changed_gram, 1, -2, 0)
    actual_line_error_sq = Fraction(1, 17)
    native_fixture = {
        "claim_native": True,
        "charge_sector": [1, 0],
        "transformed_common_domain_proof_ref": "fixture#domain",
        "form_gram_serialization_ref": "fixture#pencil",
        "coercive_shift_proof_ref": "fixture#shift",
        "dual_residual_proof_ref": "fixture#residual",
        "exterior_gap_proof_ref": "fixture#gap"
    }
    return [
        ("schema", data.get("schema_version") == "1.0"),
        ("manifest contracts", not manifest_failures(data)),
        ("fixed two-edge control", data["fixed_control"]["oriented_edges"] == [[0, 1], [0, 2]]),
        ("positive Gram accepted", form_pencil(DEMO_FORM, DEMO_GRAM)[1] == gram),
        ("exact generalized ground", original_ritz == (Fraction(-1), Fraction(-1))),
        ("nonorthogonal generalized ground", changed_ritz == original_ritz),
        ("basis form congruence", changed_form == [[Fraction(-1), Fraction(-1)], [Fraction(-1), Fraction(1)]]),
        ("basis Gram congruence", changed_gram == [[Fraction(1), Fraction(1)], [Fraction(1), Fraction(2)]]),
        ("inverse change exact", matmul(transform, inverse) == gram),
        ("form intertwiner exact", form_intertwines(form, gram, changed_form, changed_gram, inverse)),
        ("Rayleigh exact", rayleigh_quotient(form, gram, DEMO_VECTOR) == Fraction(-14, 17)),
        ("Rayleigh basis invariant", rayleigh_quotient(changed_form, changed_gram, changed_vector) == Fraction(-14, 17)),
        ("dual residual exact", DEMO_RESIDUAL_SQ == "720/4913"),
        ("dual residual basis invariant", finite_form_dual_residual_sq(changed_form, changed_gram, changed_vector, DEMO_SHIFT) == Fraction(720, 4913)),
        ("ground interval contains exact", lower <= -1 <= upper),
        ("Ritz upper exact", upper == -1),
        ("correction positive", correction > 0),
        ("projection bound closes", 0 < projection < 1),
        ("projection bound contains exact line error", projection * projection >= actual_line_error_sq),
        ("raw coupling not used", result["uses_raw_hilbert_coupling_norm"] is False),
        ("demo not native", result["native_input_contract_satisfied"] is False),
        ("solver does not assemble native", result["native_ibc_inputs_assembled_by_solver"] is False),
        ("native contract shape accepted", validate_native_contract(native_fixture)),
        ("zero residual exact interval", dual_temple_ground_enclosure(-1, 0, 2, 1, 2)[:2] == (Fraction(-1), Fraction(-1))),
        ("reject asymmetric form", rejects(lambda: form_pencil([[1, 2], [0, 1]], gram))),
        ("reject indefinite Gram", rejects(lambda: form_pencil(form, [[1, 0], [0, -1]]))),
        ("reject singular Gram", rejects(lambda: form_pencil(form, [[1, 0], [0, 0]]))),
        ("reject nonexact float", rejects(lambda: form_pencil([[1.0]], [[1]]))),
        ("reject unbracketed Ritz", rejects(lambda: isolate_generalized_eigenvalue(form, gram, 1, 0, 3))),
        ("reject bad Ritz index", rejects(lambda: isolate_generalized_eigenvalue(form, gram, 3, -2, 3))),
        ("reject nonpositive coercivity", rejects(lambda: dual_temple_ground_enclosure(-1, 0, 2, 0, 2))),
        ("reject coercivity conflict", rejects(lambda: dual_temple_ground_enclosure(-1, 0, 2, 2, 2))),
        ("reject negative residual", rejects(lambda: dual_temple_ground_enclosure(-1, -1, 2, 1, 2))),
        ("reject closed exterior gap", rejects(lambda: dual_temple_ground_enclosure(-1, 0, 2, 1, -1))),
        ("reject open projection", rejects(lambda: dual_temple_ground_enclosure(-1, 10, 2, 1, 2))),
        ("reject native missing refs", rejects(lambda: validate_native_contract({"claim_native": True, "charge_sector": [0, 0]}))),
        ("reject unselected charge", rejects(lambda: validate_native_contract({**native_fixture, "charge_sector": [2, 0]}))),
        ("reject q01 without signed transport", rejects(lambda: validate_native_contract({**native_fixture, "charge_sector": [0, 1]}))),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("conforming-domain fence", "not because a bare cutoff has finitely many modes" in text),
        ("pencil count", "n_-(A-xM)=#{j: rho_j<x}" in text),
        ("dual norm", "epsilon^2=||(H+s)^(-1/2)(H-rho)u||^2" in text),
        ("lower formula", "Delta=[E+sqrt(E^2+4g^2 E)]/(2g)" in text),
        ("raw-tail avoidance", "No raw point-field Hilbert norm occurs" in text),
        ("projection formula", "1-p <= epsilon^2 (b+s)/(b-rho)^2" in text),
        ("degenerate fence", "one vector does not recover the complete cluster projector" in text),
        ("five-part charge certificate", "charge-orbit transport is a five-part certificate" in text),
        ("native input absent", "K152 emits no native numerical interval" in text),
        ("next native gate", "Construct explicit conforming vectors `psi_i=U_s^-1 phi_i`" in text),
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
        print(f"PASS {len(baseline)}/{len(baseline)} K152 exact controls")
        return 0

    manifest_mutations = [
        lambda d: d["generalized_form_pencil"].__setitem__("gram_requirement", "optional"),
        lambda d: d["generalized_form_pencil"].__setitem__("spectral_count", "floating eigensolver"),
        lambda d: d["generalized_form_pencil"].__setitem__("bare_finite_cutoff_basis_is_automatically_native_conforming", True),
        lambda d: d["shifted_dual_residual_certificate"].__setitem__("coercivity_requirement", "assumed"),
        lambda d: d["shifted_dual_residual_certificate"].__setitem__("correction", "rho"),
        lambda d: d["shifted_dual_residual_certificate"].__setitem__("raw_Hilbert_point_coupling_norm_required", True),
        lambda d: d["shifted_dual_residual_certificate"].__setitem__("finite_core_dual_residual_alone_is_native_residual", True),
        lambda d: d["shifted_dual_residual_certificate"].__setitem__("unproved_exterior_gap_is_accepted", True),
        lambda d: d["charge_transport"].__setitem__("requires_signed_unitary", False),
        lambda d: d["charge_transport"].__setitem__("requires_dual_residual_transport", False),
        lambda d: d["charge_transport"].__setitem__("verbal_equal_coupling_is_sufficient", True),
        lambda d: d["charge_transport"].__setitem__("particle_hole_complement_is_used", True),
        lambda d: d["native_input_audit"].__setitem__("q00_transformed_native_form_gram_serialized", True),
        lambda d: d["native_input_audit"].__setitem__("native_interval_emitted", True),
        lambda d: d["boundaries"].__setitem__("numerical_native_residual_energies", True),
        lambda d: d["boundaries"].__setitem__("complete_native_threshold_or_Gram_margins", True),
        lambda d: d["boundaries"].__setitem__("native_full_Fock_Mourre_or_scattering", True),
        lambda d: d["boundaries"].__setitem__("Weinstein_source_or_GU_action_owner", True),
        lambda d: d["boundaries"].__setitem__("Born_rule_derived", True),
        lambda d: d["boundaries"].__setitem__("prediction_or_confirmation_credit", True),
    ]
    prose_mutations = [
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING", 1),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", "", 1),
        text.replace("```gu-typed-objects", "```text", 1),
        text.replace("not because a bare cutoff has finitely many modes", "because a bare cutoff is finite", 1),
        text.replace("n_-(A-xM)=#{j: rho_j<x}", "eigenvalues from floating point", 1),
        text.replace("epsilon^2=||(H+s)^(-1/2)(H-rho)u||^2", "epsilon=0", 1),
        text.replace("Delta=[E+sqrt(E^2+4g^2 E)]/(2g)", "Delta=0", 1),
        text.replace("No raw point-field Hilbert norm occurs", "Use the raw point norm", 1),
        text.replace("1-p <= epsilon^2 (b+s)/(b-rho)^2", "1-p=0", 1),
        text.replace("one vector does not recover the complete cluster projector", "one vector recovers every cluster", 1),
        text.replace("charge-orbit transport is a five-part certificate", "charge transport is verbal", 1),
        text.replace("K152 emits no native numerical interval", "K152 emits native values", 1),
        text.replace("Construct explicit conforming vectors `psi_i=U_s^-1 phi_i`", "Diagonalize another bare cutoff", 1),
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
