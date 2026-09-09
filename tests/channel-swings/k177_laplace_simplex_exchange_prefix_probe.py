#!/usr/bin/env python3
"""Baseline-first exact and hostile controls for K177."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k177_laplace_simplex_exchange_prefix.py")
MANIFEST = ROOT / "lab/process/k177-laplace-simplex-exchange-prefix-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k177-laplace-simplex-exchange-prefix-wave-2026-09-09.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k177_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K177 = load_solver()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    fixed = data.get("fixed_control", {})
    if fixed.get("maximum_resolved_order") != 12 or fixed.get("auxiliary_chart_shift") != 256:
        failures.append("fixed_control")
    automaton = data.get("boundary_word_automaton", {})
    if automaton.get("order_12_path_counts") != {"Omega": 64, "d_1^*Omega": 64, "d_2^*Omega": 64}:
        failures.append("path_counts")
    if automaton.get("total_path_coordinates_orders_0_through_12") != 633:
        failures.append("path_total")
    contraction = data.get("matched_contraction_compiler", {})
    for key in (
        "adjacent_fresh_mode_removed_as_endpoint",
        "only_older_modes_contracted",
        "exact_CAR_signs_computed_on_distinct_modes",
        "output_charge_checked_for_every_contraction",
        "order_1_exchange_vector_is_zero_for_all_three_seeds",
    ):
        if contraction.get(key) is not True:
            failures.append(key)
    if contraction.get("total_matched_contraction_coordinates_orders_1_through_12") != 2958:
        failures.append("contraction_total")
    simplex = data.get("laplace_simplex", {})
    if simplex.get("orders_1_through_12_compiled") is not True or simplex.get("jacobian") != 1 or simplex.get("all_exponents_telescope") is not True:
        failures.append("simplex")
    gram = data.get("fermionic_gram_reduction", {})
    if gram.get("one_particle_heat_kernel") != "kappa(t)=int_R exp(-t*sqrt(1+p^2)) dp/(2*pi)=K_1(t)/pi":
        failures.append("heat_kernel")
    for key in ("different_species_factorize", "matched_exchange_adds_one_positive_Schwinger_parameter", "all_prefix_scalar_products_reduce_to_finite_ordered_simplex_integrals"):
        if gram.get(key) is not True:
            failures.append(key)
    release = data.get("release_test", {})
    for key in (
        "resolved_prefix_path_coordinates_through_order_12_serialized",
        "matched_exchange_contraction_coordinates_through_order_12_serialized",
        "order_1_exchange_vector_evaluated_as_zero",
        "continuum_scalar_products_reduced_to_heat_kernel_integrals",
    ):
        if release.get(key) is not True:
            failures.append(key)
    for key in (
        "outward_numerical_prefix_integrals_evaluated",
        "coefficient_complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "native_K152_interval_emitted",
    ):
        if release.get(key) is not False:
            failures.append(key)
    return failures


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    result = K177.demo()
    seeds = result["boundary_word_automaton"]["seed_census"]
    contraction = result["matched_contraction_compiler"]
    simplex = result["laplace_simplex"]
    gram = result["fermionic_gram_reduction"]
    release = result["release_test"]
    return [
        ("schema", result["schema_version"] == "1.0"),
        ("manifest", not manifest_failures(data)),
        ("three seeds", [row["charge"] for row in seeds] == [[0, 0], [1, 0], [0, 1]]),
        ("order twelve paths", [row["order_12_path_count"] for row in seeds] == [64, 64, 64]),
        ("vacuum path total", seeds[0]["total_paths_orders_0_through_12"] == 253),
        ("one impurity path totals", [row["total_paths_orders_0_through_12"] for row in seeds[1:]] == [190, 190]),
        ("charge preservation", result["boundary_word_automaton"]["all_words_charge_preserving"] is True),
        ("CAR order", result["boundary_word_automaton"]["global_CAR_order_preserved"] is True),
        ("matched endpoint", contraction["adjacent_fresh_mode_removed_as_endpoint"] is True),
        ("older only", contraction["only_older_modes_contracted"] is True),
        ("exact signs", contraction["exact_CAR_signs_computed_on_distinct_modes"] is True),
        ("charge checked", contraction["output_charge_checked_for_every_contraction"] is True),
        ("order one zero", contraction["order_1_exchange_vector_is_zero_for_all_three_seeds"] is True),
        ("path coordinates", contraction["total_resolved_path_coordinates"] == 633),
        ("contraction coordinates", contraction["total_matched_contraction_coordinates"] == 2958),
        ("vacuum contractions", seeds[0]["total_matched_contractions_orders_1_through_12"] == 1158),
        ("charged contractions", [row["total_matched_contractions_orders_1_through_12"] for row in seeds[1:]] == [900, 900]),
        ("simplex orders", simplex["all_orders_1_through_12_compiled"] is True),
        ("simplex Jacobians", simplex["all_jacobians_one"] is True),
        ("simplex exponents", simplex["all_exponents_telescope"] is True),
        ("order twelve simplex", simplex["order_12"]["simplex"] == "s_1>s_2>...>s_n>0"),
        ("heat kernel normalization", gram["one_particle_heat_kernel"].endswith("K_1(t)/pi")),
        ("determinant", gram["same_species_wedge_inner_product"] == "det[kappa(s_i+r_j)]"),
        ("species factorization", gram["different_species_factorize"] is True),
        ("path pair selection", "equal species occupation" in gram["path_pair_selection"]),
        ("extra Schwinger parameter", gram["matched_exchange_adds_one_positive_Schwinger_parameter"] is True),
        ("finite integrals", gram["all_prefix_scalar_products_reduce_to_finite_ordered_simplex_integrals"] is True),
        ("prefix serialized", release["resolved_prefix_path_coordinates_through_order_12_serialized"] is True),
        ("contractions serialized", release["matched_exchange_contraction_coordinates_through_order_12_serialized"] is True),
        ("numerics open", release["outward_numerical_prefix_integrals_evaluated"] is False),
        ("residual open", release["complete_R_ref_form_dual_residual_serialized"] is False),
        ("K152 open", release["native_K152_interval_emitted"] is False),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("antisymmetry fence", "ordered path is not itself a Fock vector" in text),
        ("Bessel normalization", "K_1(t)/pi" in text),
        ("numerical fence", "does not numerically evaluate" in text),
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
        print(f"PASS {len(baseline)}/{len(baseline)} K177 exact controls")
        return 0

    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["fixed_control"].__setitem__("maximum_resolved_order", 11),
        lambda d: d["boundary_word_automaton"].__setitem__("order_12_path_counts", {"Omega": 32}),
        lambda d: d["boundary_word_automaton"].__setitem__("total_path_coordinates_orders_0_through_12", 632),
        lambda d: d["matched_contraction_compiler"].__setitem__("adjacent_fresh_mode_removed_as_endpoint", False),
        lambda d: d["matched_contraction_compiler"].__setitem__("only_older_modes_contracted", False),
        lambda d: d["matched_contraction_compiler"].__setitem__("exact_CAR_signs_computed_on_distinct_modes", False),
        lambda d: d["matched_contraction_compiler"].__setitem__("output_charge_checked_for_every_contraction", False),
        lambda d: d["matched_contraction_compiler"].__setitem__("order_1_exchange_vector_is_zero_for_all_three_seeds", False),
        lambda d: d["matched_contraction_compiler"].__setitem__("total_matched_contraction_coordinates_orders_1_through_12", 2957),
        lambda d: d["laplace_simplex"].__setitem__("orders_1_through_12_compiled", False),
        lambda d: d["laplace_simplex"].__setitem__("jacobian", 2),
        lambda d: d["laplace_simplex"].__setitem__("all_exponents_telescope", False),
        lambda d: d["fermionic_gram_reduction"].__setitem__("one_particle_heat_kernel", "K_0(t)/pi"),
        lambda d: d["fermionic_gram_reduction"].__setitem__("different_species_factorize", False),
        lambda d: d["fermionic_gram_reduction"].__setitem__("matched_exchange_adds_one_positive_Schwinger_parameter", False),
        lambda d: d["fermionic_gram_reduction"].__setitem__("all_prefix_scalar_products_reduce_to_finite_ordered_simplex_integrals", False),
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
        text.replace("ordered path is not itself a Fock vector", "ordered path is a Fock vector"),
        text.replace("K_1(t)/pi", "K_0(t)/pi"),
        text.replace("does not numerically evaluate", "numerically evaluates"),
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
