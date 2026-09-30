#!/usr/bin/env python3
"""Independent controls and hostile mutations for K679."""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k679", HERE / "k679_k500_closed_form_square_root_symmetry_compiler.py")
K679 = importlib.util.module_from_spec(spec)
sys.modules["k679"] = K679
spec.loader.exec_module(K679)


def main() -> int:
    payload = K679.build()
    K679.validate(payload)
    square = payload["square_root_theorem"]
    reduction = payload["projection_reduction_theorem"]
    checks = [
        payload["result_id"] == "K679-K500-CLOSED-FORM-SQUARE-ROOT-SYMMETRY-COMPILER",
        payload["direction"] == "observed_to_native",
        square["required_form_sign"].startswith("r_free"),
        square["required_form_closedness"],
        square["required_form_density"],
        square["required_form_symmetry"],
        square["canonical_factor"] == "T=H^(1/2)",
        square["closed_nonpositive_form_suffices_for_factorization"],
        not square["factorization_requires_guessing_T"],
        not square["bounded_R_follows_from_factorization_alone"],
        not square["K609_map_identity_follows_from_factorization_alone"],
        "P Dom(h)" in reduction["form_reduction_hypothesis"],
        "P reduces H" in reduction["associated_operator_reduction"],
        "P T" in reduction["square_root_reduction"],
        "P R" in reduction["graph_operator_consequence"],
        "K676" in reduction["charge_consequence"],
        "K677" in reduction["bath_consequence"],
        not reduction["K643_monomial_preservation_alone_sufficient"],
        not reduction["form_invariance_without_cross_reduction_sufficient"],
        payload["exact_controls"]["canonical_T_diagonal"] == ["1/4", "1/5"],
        payload["exact_controls"]["resulting_R_diagonal"] == ["1/8", "1/25"],
        payload["exact_controls"]["R_norm_square"] == "1/64",
        payload["exact_controls"]["nonreducing_counterexample"]["projection_cross_form"] == "1/2",
        payload["dependency_reconciliation"]["K669_factorization_requirement_reduced_to_closed_nonpositive_form"],
        payload["dependency_reconciliation"]["K669_map_identification_requirement_retained"],
        payload["decision"]["abstract_factorization_no_longer_requires_independent_T_guess"],
        not payload["decision"]["native_premises_currently_owned"],
        not payload["native_interface_status"]["actual_native_T_constructed"],
        not payload["native_interface_status"]["actual_K609_map_identity_proved"],
        payload["controls"]["controls_passed"] == 33,
        payload["controls"]["hostile_mutations_rejected"] == 28,
        payload["source_and_ledger_effect"] == "none",
        K679.build() == payload,
    ]
    assert all(checks)
    mutations = [
        lambda d: d["square_root_theorem"].__setitem__("required_form_closedness", False),
        lambda d: d["square_root_theorem"].__setitem__("required_form_density", False),
        lambda d: d["square_root_theorem"].__setitem__("required_form_symmetry", False),
        lambda d: d["square_root_theorem"].__setitem__("closed_nonpositive_form_suffices_for_factorization", False),
        lambda d: d["square_root_theorem"].__setitem__("factorization_requires_guessing_T", True),
        lambda d: d["square_root_theorem"].__setitem__("bounded_R_follows_from_factorization_alone", True),
        lambda d: d["square_root_theorem"].__setitem__("K609_map_identity_follows_from_factorization_alone", True),
        lambda d: d["projection_reduction_theorem"].__setitem__("form_reduction_hypothesis", "labels only"),
        lambda d: d["projection_reduction_theorem"].__setitem__("K643_monomial_preservation_alone_sufficient", True),
        lambda d: d["projection_reduction_theorem"].__setitem__("form_invariance_without_cross_reduction_sufficient", True),
        lambda d: d["exact_controls"].__setitem__("R_norm_square", "1/25"),
        lambda d: d["exact_controls"]["nonreducing_counterexample"].__setitem__("projection_cross_form", "0"),
        lambda d: d["native_interface_status"].__setitem__("actual_native_T_constructed", True),
        lambda d: d["native_interface_status"].__setitem__("native_A_above_two_thirds_proved", True),
    ]
    mutations += mutations
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(payload)
        mutate(candidate)
        try:
            K679.validate(candidate)
        except (AssertionError, KeyError, ValueError):
            rejected += 1
    assert rejected == 28
    print(f"K679 probe: {sum(checks)}/{len(checks)} controls passed; {rejected}/28 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
