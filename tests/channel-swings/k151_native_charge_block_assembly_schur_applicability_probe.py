#!/usr/bin/env python3
"""Exact and hostile controls for K151 charge-block assembly."""

from __future__ import annotations

import argparse
import copy
import json
from fractions import Fraction
from pathlib import Path

from k150_certified_schur_tail_solver import inertia
from k151_native_charge_block_assembler import (
    apply_car,
    basis,
    charge_block,
    charges,
    flavor_intertwines,
    flavor_swap,
    flavor_swap_matrix,
    is_hard_core,
    matmul,
    particle_hole_complement_preserves_native,
    point_tail_norm_sq,
    resolvent_dressed_tail_norm_sq,
    transpose,
)


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k151-native-charge-block-assembly-schur-applicability-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k151-native-charge-block-assembly-schur-applicability-wave-2026-09-08.md"


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    assembly = data.get("exact_charge_block_assembly", {})
    symmetry = data.get("charge_symmetry", {})
    schur = data.get("schur_applicability", {})
    finite = data.get("finite_control", {})
    bounds = data.get("boundaries", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        failures.append("classification")
    if data.get("direction") != "observed_to_native":
        failures.append("direction")
    required_assembly = {
        "native_impurity_carrier": "span{|0>,|1>,|2>}",
        "hard_core_condition": "n1*n2=0",
        "fermionic_signs": "canonical exterior-algebra inversion parity",
        "matrix_arithmetic": "exact_rational_for_rational_mode_data",
        "matrix_is_exactly_symmetric": True,
        "interaction_preserves_each_charge_block": True,
        "auxiliary_finite_U_available_by_restoring_double_occupancy": True,
        "native_hard_core_matrix_is_the_auxiliary_principal_compression": True,
        "finite_regulator_matrix_is_native_continuum_spectrum": False,
    }
    if any(assembly.get(key) != value for key, value in required_assembly.items()):
        failures.append("assembly")
    required_symmetry = {
        "flavor_swap_is_signed_exterior_basis_permutation": True,
        "flavor_swap_maps_sector_q1_q2_to_q2_q1": True,
        "equal_flavor_data_give_exact_matrix_intertwiner": True,
        "intertwining_equation": "H_(q2,q1) S_q = S_q H_(q1,q2)",
        "unitarity_equation": "S_q^* S_q=I",
        "two_flavor_particle_hole_complement_preserves_native_C3": False,
        "verbal_equal_coupling_is_sufficient_symmetry_certificate": False,
    }
    if any(symmetry.get(key) != value for key, value in required_symmetry.items()):
        failures.append("symmetry")
    if symmetry.get("selected_charge_orbit_representatives_for_form_computation") != [[0, 0], [1, 0]]:
        failures.append("orbit representatives")
    required_schur = {
        "bare_point_form_factor_is_L2": False,
        "constant_point_coefficients_give_cutoff_uniform_bound": False,
        "bare_low_tail_off_diagonal_block_is_bounded_in_native_Hilbert_norm": False,
        "K139_resolvent_dressed_boundary_coefficient_is_L2": True,
        "resolvent_dressed_boundary_inverse_is_bounded": True,
        "resolvent_dressed_boundary_bound_implies_raw_Hilbert_block_bound": False,
        "K139_transformed_regular_terms_are_free_graph_relative": True,
        "K150_raw_bounded_Schur_hypothesis_certified": False,
        "K150_finite_cutoff_norm_may_be_used_as_continuum_bound": False,
        "required_lower_certificate_route": "form_level_Lehmann--Goerisch_or_certified_penalty_form_bound",
    }
    if any(schur.get(key) != value for key, value in required_schur.items()):
        failures.append("schur applicability")
    expected_finite = {
        "q00_dimension": 8,
        "q10_dimension": 7,
        "q01_dimension": 7,
        "q11_dimension": 5,
        "q00_exact_inertia": [1, 0, 7],
        "q10_exact_inertia": [1, 0, 6],
        "q01_exact_inertia": [1, 0, 6],
        "q11_exact_inertia": [0, 0, 5],
    }
    if any(finite.get(key) != value for key, value in expected_finite.items()):
        failures.append("finite control")
    denied = (
        "native_conforming_transformed_Ritz_matrix_serialized",
        "continuum_complement_floor_proved",
        "continuum_coupling_norm_proved",
        "numerical_native_residual_energies",
        "complete_charge_sector_point_spectrum",
        "complete_native_threshold_or_Gram_margins",
        "native_full_Fock_Mourre_or_scattering",
        "NESS_or_current",
        "Weinstein_source_or_GU_action_owner",
        "Born_rule_derived",
        "prediction_or_confirmation_credit",
    )
    if any(bounds.get(key) is not False for key in denied):
        failures.append("boundary")
    if bounds.get("canon_verdict_change") != "none" or bounds.get("paper_release_or_public_posture_change") != "none":
        failures.append("external boundary")
    return failures


def hard_core_is_principal_compression(charge: tuple[int, int]) -> bool:
    native_states, native = charge_block(["5/4"], [1], charge)
    exterior_states, exterior = charge_block(["5/4"], [1], charge, hard_core=False, penalty=7)
    exterior_index = {state: i for i, state in enumerate(exterior_states)}
    selected = [exterior_index[state] for state in native_states]
    compressed = [[exterior[i][j] for j in selected] for i in selected]
    return compressed == native


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    energies = ["5/4"]
    couplings = [1]
    blocks = {charge: charge_block(energies, couplings, charge) for charge in ((0, 0), (1, 0), (0, 1), (1, 1))}
    dimensions = {charge: len(value[0]) for charge, value in blocks.items()}
    inertias = {charge: inertia(value[1]) for charge, value in blocks.items()}
    source, _ = blocks[(1, 0)]
    target, _ = blocks[(0, 1)]
    swap = flavor_swap_matrix(source, target, 1)
    signed_entries = [entry for row in swap for entry in row if entry]
    identity = [[Fraction(i == j) for j in range(len(source))] for i in range(len(source))]
    state = (1 << 0) | (1 << 3)
    twice = apply_car(state, 3, False)
    anti_left = apply_car(twice[0], 0, False) if twice else None
    anti_right_first = apply_car(state, 0, False)
    anti_right = apply_car(anti_right_first[0], 3, False) if anti_right_first else None
    anti_sum = (
        twice[1] * anti_left[1] + anti_right_first[1] * anti_right[1]
        if twice and anti_left and anti_right_first and anti_right
        else 99
    )
    raw_growth = [point_tail_norm_sq([1] * count) for count in (1, 2, 4, 8, 16)]
    dressed_8 = resolvent_dressed_tail_norm_sq(
        [Fraction(abs(k), 1) + Fraction(5, 4) for k in range(-8, 9)], [1] * 17, 1
    )
    dressed_16 = resolvent_dressed_tail_norm_sq(
        [Fraction(abs(k), 1) + Fraction(5, 4) for k in range(-16, 17)], [1] * 33, 1
    )
    return [
        ("schema", data.get("schema_version") == "1.0"),
        ("manifest contracts", not manifest_failures(data)),
        ("hard-core basis excludes double", all(is_hard_core(state) for state in basis(1, (0, 0)))),
        ("q00 basis charge", all(charges(state, 1) == (0, 0) for state in blocks[(0, 0)][0])),
        ("q10 basis charge", all(charges(state, 1) == (1, 0) for state in blocks[(1, 0)][0])),
        ("CAR anticommutes", anti_sum == 0),
        ("dimensions", dimensions == {(0, 0): 8, (1, 0): 7, (0, 1): 7, (1, 1): 5}),
        ("inertias", inertias == {(0, 0): (1, 0, 7), (1, 0): (1, 0, 6), (0, 1): (1, 0, 6), (1, 1): (0, 0, 5)}),
        ("native compression q00", hard_core_is_principal_compression((0, 0))),
        ("native compression q10", hard_core_is_principal_compression((1, 0))),
        ("flavor intertwiner q00", flavor_intertwines(["5/4"], [1], (0, 0))),
        ("flavor intertwiner q10", flavor_intertwines(["5/4"], [1], (1, 0))),
        ("swap unitary", matmul(transpose(swap), swap) == identity),
        ("swap has fermionic signs", -1 in signed_entries and 1 in signed_entries),
        ("swap charge target", all(charges(flavor_swap(state, 1)[0], 1) == (0, 1) for state in source)),
        ("particle-hole vacuum exits native", particle_hole_complement_preserves_native(0) is False),
        ("raw tail exact growth", raw_growth == [1, 2, 4, 8, 16]),
        ("raw tail unbounded witness", all(raw_growth[i + 1] > raw_growth[i] for i in range(4))),
        ("dressed tail finite", dressed_16 > dressed_8 > 0),
        ("dressed increments shrink", dressed_16 - dressed_8 < Fraction(1, 4)),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("interaction formula", "d_i* a_(i,+,j)" in text),
        ("charge formula", "q_i=n_i+N_(i,+)-N_(i,-)" in text),
        ("signed symmetry", "H_(M,(q_2,q_1)) S_q = S_q H_(M,(q_1,q_2))" in text),
        ("particle-hole fence", "excluded double state `|12>`" in text),
        ("bare tail formula", "sum_(k omitted) |g_k|^2" in text),
        ("K150 refusal", "Feeding a finite `beta_M` to K150 would" in text),
        ("form switch", "Lehmann--Goerisch" in text),
        ("finite control fence", "It is not a table of native" in text),
        ("next form gate", "Construct a form-level lower-enclosure kernel" in text),
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
        print(f"PASS {len(baseline)}/{len(baseline)} K151 exact controls")
        return 0

    mutations = [
        lambda d: d["exact_charge_block_assembly"].__setitem__("matrix_is_exactly_symmetric", False),
        lambda d: d["exact_charge_block_assembly"].__setitem__("interaction_preserves_each_charge_block", False),
        lambda d: d["exact_charge_block_assembly"].__setitem__("finite_regulator_matrix_is_native_continuum_spectrum", True),
        lambda d: d["charge_symmetry"].__setitem__("equal_flavor_data_give_exact_matrix_intertwiner", False),
        lambda d: d["charge_symmetry"].__setitem__("two_flavor_particle_hole_complement_preserves_native_C3", True),
        lambda d: d["charge_symmetry"].__setitem__("verbal_equal_coupling_is_sufficient_symmetry_certificate", True),
        lambda d: d["schur_applicability"].__setitem__("bare_point_form_factor_is_L2", True),
        lambda d: d["schur_applicability"].__setitem__("constant_point_coefficients_give_cutoff_uniform_bound", True),
        lambda d: d["schur_applicability"].__setitem__("bare_low_tail_off_diagonal_block_is_bounded_in_native_Hilbert_norm", True),
        lambda d: d["schur_applicability"].__setitem__("resolvent_dressed_boundary_bound_implies_raw_Hilbert_block_bound", True),
        lambda d: d["schur_applicability"].__setitem__("K150_raw_bounded_Schur_hypothesis_certified", True),
        lambda d: d["schur_applicability"].__setitem__("K150_finite_cutoff_norm_may_be_used_as_continuum_bound", True),
        lambda d: d["finite_control"].__setitem__("q00_dimension", 7),
        lambda d: d["finite_control"].__setitem__("q11_exact_inertia", [1, 0, 4]),
        lambda d: d["boundaries"].__setitem__("native_conforming_transformed_Ritz_matrix_serialized", True),
        lambda d: d["boundaries"].__setitem__("continuum_coupling_norm_proved", True),
        lambda d: d["boundaries"].__setitem__("numerical_native_residual_energies", True),
        lambda d: d["boundaries"].__setitem__("native_full_Fock_Mourre_or_scattering", True),
        lambda d: d["boundaries"].__setitem__("Weinstein_source_or_GU_action_owner", True),
        lambda d: d["boundaries"].__setitem__("prediction_or_confirmation_credit", True),
    ]
    prose_mutations = [
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING", 1),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", "", 1),
        text.replace("```gu-typed-objects", "```text", 1),
        text.replace("d_i* a_(i,+,j)", "d_i a_(i,+,j)", 1),
        text.replace("q_i=n_i+N_(i,+)-N_(i,-)", "q_i=n_i+N_(i,+)+N_(i,-)"),
        text.replace("H_(M,(q_2,q_1)) S_q = S_q H_(M,(q_1,q_2))", "symmetry assumed", 1),
        text.replace("excluded double state `|12>`", "native state `|12>`", 1),
        text.replace("sum_(k omitted) |g_k|^2", "bounded", 1),
        text.replace("Feeding a finite `beta_M` to K150 would", "Using beta_M will", 1),
        text.replace("Lehmann--Goerisch", "raw Schur"),
        text.replace("It is not a table of native", "It is a table of native", 1),
        text.replace("Construct a form-level lower-enclosure kernel", "Diagonalize another cutoff", 1),
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
