#!/usr/bin/env python3
"""Hostile mutations for K793."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k793_sc_act_06_full_field_kernel_persistence.py"


def load():
    spec = importlib.util.spec_from_file_location("k793", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    base = module.build()
    mutations = [
        lambda p: p.__setitem__("result_id", "K793-MUTANT"),
        lambda p: p.__setitem__("target_claim", "SC-ACT-05"),
        lambda p: p.__setitem__("classification", "CONDITIONAL_COMPARATOR"),
        lambda p: p["extension_lemma"].__setitem__("map_form", "wrong"),
        lambda p: p["extension_lemma"].__setitem__("embedded_subspace", "wrong"),
        lambda p: p["extension_lemma"].__setitem__("embedded_subspace_is_in_full_kernel", False),
        lambda p: p["extension_lemma"].__setitem__("adding_field_columns_can_delete_old_kernel_vectors", True),
        lambda p: p["extension_lemma"].__setitem__("adding_block_diagonal_fermion_rows_can_act_on_old_bosonic_kernel", True),
        lambda p: p["extension_lemma"].__setitem__("redundant_xi_row_can_act_on_old_kernel", True),
        lambda p: p["released_full_field_typing"].__setitem__("metric_epsilon_varpi_fermions_are_field_columns", False),
        lambda p: p["released_full_field_typing"].__setitem__("zero_fermion_mixed_principal_blocks_vanish", False),
        lambda p: p["released_full_field_typing"].__setitem__("fermion_diagonal_is_separate_from_bosonic_connection_kernel", False),
        lambda p: p["released_full_field_typing"].__setitem__("i2b_adjoint_row_is_not_part_of_first_order_SC_ACT_06_packet", False),
        lambda p: p["exact_bound"].__setitem__("embedded_connection_kernel_dimension", 106511),
        lambda p: p["exact_bound"].__setitem__("maximal_current_granted_symmetry_rank", 16387),
        lambda p: p["exact_bound"].__setitem__("persistent_middle_classes_lower_bound", 90123),
        lambda p: p["exact_bound"].__setitem__("uniform_on_positive_negative_and_null_real_covectors", False),
        lambda p: p["decision"].__setitem__("released_full_field_extension_repairs_K790", True),
        lambda p: p["decision"].__setitem__("complete_fermion_diagonal_can_repair_bosonic_defect", True),
        lambda p: p["decision"].__setitem__("new_metric_or_epsilon_columns_alone_can_repair_bosonic_defect", True),
        lambda p: p["decision"].__setitem__("remaining_reopener", "none"),
        lambda p: p.__setitem__("source_and_ledger_effect", "PROMOTED"),
        lambda p: p.__setitem__("pinned_inputs", {}),
        lambda p: p["exact_bound"].__setitem__("embedded_connection_kernel_dimension", 0),
        lambda p: p["exact_bound"].__setitem__("maximal_current_granted_symmetry_rank", 106512),
        lambda p: p["exact_bound"].__setitem__("persistent_middle_classes_lower_bound", 0),
        lambda p: p["extension_lemma"].__setitem__("embedded_subspace_is_in_full_kernel", 0),
        lambda p: p["released_full_field_typing"].__setitem__("metric_epsilon_varpi_fermions_are_field_columns", 0),
        lambda p: p["decision"].__setitem__("remaining_reopener", "at least ninety thousand"),
        lambda p: p["exact_bound"].__setitem__("uniform_on_positive_negative_and_null_real_covectors", 0),
    ]
    assert len(mutations) == 30
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(base)
        mutate(candidate)
        try:
            module.validate(candidate)
        except (AssertionError, KeyError, ValueError):
            rejected += 1
    assert rejected == len(mutations)
    print(f"K793 probe: {rejected}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
