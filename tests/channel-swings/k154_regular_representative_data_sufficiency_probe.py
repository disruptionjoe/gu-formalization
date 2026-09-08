#!/usr/bin/env python3
"""Exact and hostile controls for K154 data-sufficiency result."""

from __future__ import annotations

import argparse
import copy
import json
from fractions import Fraction
from pathlib import Path

from k154_regular_representative_certificate import (
    DEMO,
    CertificateError,
    compile_certificate,
    hidden_gap_countermodels,
    regular_form_countermodels,
)


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k154-regular-representative-data-sufficiency-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k154-regular-representative-data-sufficiency-wave-2026-09-08.md"


def rejects(callable_) -> bool:
    try:
        callable_()
    except (CertificateError, KeyError, TypeError, ValueError):
        return True
    return False


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    scope = data.get("fixed_scope", {})
    regular = data.get("regular_data_obstruction", {})
    spectral = data.get("spectral_floor_obstruction", {})
    contract = data.get("positive_certificate_contract", {})
    bounds = data.get("boundaries", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        failures.append("classification")
    if data.get("direction") != "observed_to_native":
        failures.append("direction")
    expected_scope = {
        "input_chain": ["K139", "K151", "K152", "K153"],
        "representative_charges": [[0, 0], [1, 0]],
        "flavor_partner": [0, 1],
        "chart_shift": 256,
        "chart_contraction_upper": "3/8",
        "physical_operator_claimed_nonunique": False,
        "serialized_certificate_data_claimed_insufficient": True,
    }
    if any(scope.get(key) != value for key, value in expected_scope.items()):
        failures.append("fixed scope")
    expected_regular = {
        "bounded_charge_preserving_finite_rank_perturbations_preserve_common_domain": True,
        "bounded_charge_preserving_finite_rank_perturbations_preserve_self_adjointness": True,
        "bounded_charge_preserving_finite_rank_perturbations_preserve_semiboundedness": True,
        "chart_and_charge_data_determine_regular_form_entries": False,
        "chart_and_charge_data_determine_regular_action": False,
        "coefficient_complete_regular_representation_required": True,
        "countermodel_is_change_of_physical_operator": True,
        "countermodel_proves_physical_nonuniqueness": False,
    }
    if any(regular.get(key) != value for key, value in expected_regular.items()):
        failures.append("regular obstruction")
    expected_spectral = {
        "one_seed_form_action_and_residual_determine_next_distinct_spectrum": False,
        "essential_spectrum_edge_is_next_distinct_spectrum_floor": False,
        "discrete_excited_levels_may_lie_below_essential_edge": True,
        "finite_cutoff_second_eigenvalue_is_native_floor": False,
    }
    if any(spectral.get(key) != value for key, value in expected_spectral.items()):
        failures.append("spectral obstruction")
    required_contract = (
        "requires_fixed_operator_ref",
        "requires_conforming_core_ref",
        "requires_regular_form_matrix",
        "requires_positive_hilbert_gram",
        "requires_regular_action_and_total_hilbert_residual_proof",
        "requires_regular_lower_bound_and_positive_transported_coercivity",
        "requires_next_distinct_floor_and_spectral_count_proof",
        "q01_requires_signed_flavor_intertwiner",
        "essential_edge_only_fails_closed",
        "finite_cutoff_only_fails_closed",
        "complete_abstract_positive_control_closes_K152",
    )
    if any(contract.get(key) is not True for key in required_contract):
        failures.append("positive contract")
    if contract.get("native_K139_K153_packet_complete") is not False:
        failures.append("native incompleteness")
    denied = (
        "coefficient_complete_native_R256_serialized",
        "native_dual_residual_closing_bound_serialized",
        "native_next_distinct_spectrum_lower_bound_serialized",
        "native_energy_interval_emitted",
        "complete_native_threshold_or_Gram_margins",
        "native_full_Fock_Mourre_or_scattering",
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
    form_models = regular_form_countermodels("1/3")
    gap_half = hidden_gap_countermodels("1/2")
    gap_small = hidden_gap_countermodels("1/100")
    compiled = compile_certificate(copy.deepcopy(DEMO))
    missing_count = copy.deepcopy(DEMO)
    missing_count.pop("spectral_count_or_exterior_subspace_ref")
    essential_only = copy.deepcopy(DEMO)
    essential_only["essential_edge_used_as_gap"] = True
    cutoff_only = copy.deepcopy(DEMO)
    cutoff_only["finite_cutoff_only"] = True
    bad_gram = copy.deepcopy(DEMO)
    bad_gram["hilbert_gram_matrix"] = [["1", "0"], ["0", "0"]]
    flavor = copy.deepcopy(DEMO)
    flavor["charge_sector"] = [0, 1]
    weak_gap = copy.deepcopy(DEMO)
    weak_gap["next_distinct_spectrum_lower"] = "1/100"
    bad_coercivity = copy.deepcopy(DEMO)
    bad_coercivity["physical_shift"] = "0"
    return [
        ("schema", data.get("schema_version") == "1.0"),
        ("manifest contracts", not manifest_failures(data)),
        ("same chart countermodels", form_models["chart"] == [["1", "0"], ["0", "1"]]),
        ("same domain countermodels", form_models["common_domain"] == "C^2"),
        ("charge preserving rank one", form_models["bounded_charge_preserving_rank_one_perturbation"] is True),
        ("seed form changes", form_models["seed_form_values"] == ["0", "1/3"]),
        ("same seed form across gap models", gap_half["seed_form"] == gap_small["seed_form"] == "0"),
        ("same seed action across gap models", gap_half["seed_action"] == gap_small["seed_action"] == ["0", "0"]),
        ("same zero residual", gap_half["seed_residual"] == gap_small["seed_residual"] == "0"),
        ("same essential edge", gap_half["essential_edge"] == gap_small["essential_edge"] == "4"),
        ("different hidden gap", gap_half["next_distinct_spectrum"] == "1/2" and gap_small["next_distinct_spectrum"] == "1/100"),
        ("essential edge fence", gap_half["essential_edge_alone_is_next_gap"] is False),
        ("compiler schema", compiled["schema_version"] == "1.0"),
        ("compiler exact arithmetic", compiled["arithmetic"] == "exact_rational_outer_bounds"),
        ("compiler rayleigh", compiled["rayleigh"] == "2/101"),
        ("compiler coercivity", compiled["shifted_form_coercivity_floor"] == "3"),
        ("compiler dual residual", compiled["form_dual_residual_sq_upper"] == "1/48"),
        ("compiler gap", compiled["next_distinct_spectrum_lower"] == "2"),
        ("compiler interval ordered", Fraction(compiled["ground_interval"][0]) < Fraction(compiled["ground_interval"][1])),
        ("compiler projection closes", Fraction(compiled["trial_ground_projection_error_upper"]) < 1),
        ("compiler contract complete", compiled["certificate_contract_complete"] is True),
        ("abstract control emits no native interval", compiled["native_energy_interval_emitted"] is False),
        ("missing spectral count rejected", rejects(lambda: compile_certificate(missing_count))),
        ("essential-only gap rejected", rejects(lambda: compile_certificate(essential_only))),
        ("finite cutoff rejected", rejects(lambda: compile_certificate(cutoff_only))),
        ("singular Gram rejected", rejects(lambda: compile_certificate(bad_gram))),
        ("missing flavor proof rejected", rejects(lambda: compile_certificate(flavor))),
        ("unseparated gap rejected", rejects(lambda: compile_certificate(weak_gap))),
        ("nonpositive coercivity rejected", rejects(lambda: compile_certificate(bad_coercivity))),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("rank-one equation", "K_t=t |phi><phi|" in text),
        ("data not physical nonuniqueness", "does not prove physical extension ambiguity" in text),
        ("hidden discrete model", "R_delta e_1=delta e_1" in text),
        ("essential edge distinction", "essential edge >= tau_ess  does not imply" in text),
        ("spectral count requirement", "certified spectral count below `b`" in text),
        ("total residual requirement", "*total Hilbert-space* residual upper bound" in text),
        ("flavor fence", "complete signed flavor intertwiner" in text),
        ("finite cutoff fence", "finite-cutoff second eigenvalue" in text),
        ("positive control fence", "is not native K139 data" in text),
        ("next finite regular formula", "R_(N,256)=U_(N,256)^(-*) H_N U_(N,256)^(-1)" in text),
        ("held-out fence", data.get("held_out") == "delayed-choice entanglement swapping, reserved_unscored"),
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
        print(f"FAIL baseline {len(baseline) - len(failed)}/{len(baseline)}: {failed}")
        return 1
    if not args.selftest:
        print(f"PASS {len(baseline)}/{len(baseline)} controls")
        return 0

    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["fixed_scope"].__setitem__("physical_operator_claimed_nonunique", True),
        lambda d: d["fixed_scope"].__setitem__("chart_shift", 128),
        lambda d: d["regular_data_obstruction"].__setitem__("chart_and_charge_data_determine_regular_form_entries", True),
        lambda d: d["regular_data_obstruction"].__setitem__("chart_and_charge_data_determine_regular_action", True),
        lambda d: d["regular_data_obstruction"].__setitem__("countermodel_is_change_of_physical_operator", False),
        lambda d: d["regular_data_obstruction"].__setitem__("countermodel_proves_physical_nonuniqueness", True),
        lambda d: d["spectral_floor_obstruction"].__setitem__("essential_spectrum_edge_is_next_distinct_spectrum_floor", True),
        lambda d: d["spectral_floor_obstruction"].__setitem__("finite_cutoff_second_eigenvalue_is_native_floor", True),
        lambda d: d["positive_certificate_contract"].__setitem__("requires_regular_form_matrix", False),
        lambda d: d["positive_certificate_contract"].__setitem__("requires_next_distinct_floor_and_spectral_count_proof", False),
        lambda d: d["positive_certificate_contract"].__setitem__("q01_requires_signed_flavor_intertwiner", False),
        lambda d: d["positive_certificate_contract"].__setitem__("native_K139_K153_packet_complete", True),
        lambda d: d["boundaries"].__setitem__("coefficient_complete_native_R256_serialized", True),
        lambda d: d["boundaries"].__setitem__("native_energy_interval_emitted", True),
        lambda d: d["boundaries"].__setitem__("native_full_Fock_Mourre_or_scattering", True),
        lambda d: d["boundaries"].__setitem__("Weinstein_source_or_GU_action_owner", True),
        lambda d: d["boundaries"].__setitem__("prediction_or_confirmation_credit", True),
    ]
    prose_mutations = [
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING", 1),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", "", 1),
        text.replace("```gu-typed-objects", "```text", 1),
        text.replace("K_t=t |phi><phi|", "K_t=0", 1),
        text.replace("does not prove physical extension ambiguity", "proves physical extension ambiguity", 1),
        text.replace("R_delta e_1=delta e_1", "R_delta e_1=tau_ess e_1", 1),
        text.replace("essential edge >= tau_ess  does not imply", "essential edge >= tau_ess implies", 1),
        text.replace("certified spectral count below `b`", "essential edge below `b`", 1),
        text.replace("*total Hilbert-space* residual upper bound", "finite-core residual", 1),
        text.replace("complete signed flavor intertwiner", "verbal equal coupling", 1),
        text.replace("finite-cutoff second eigenvalue", "native second eigenvalue", 1),
        text.replace("is not native K139 data", "is native K139 data", 1),
        text.replace("R_(N,256)=U_(N,256)^(-*) H_N U_(N,256)^(-1)", "R_256=H_N", 1),
    ]
    caught = 0
    missed: list[str] = []
    for index, mutate in enumerate(mutations, start=1):
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
    total = len(mutations) + len(prose_mutations)
    if caught != total:
        print(f"FAIL hostile selftest caught {caught}/{total}; missed {missed}")
        return 1
    print(f"PASS hostile selftest caught {caught}/{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
