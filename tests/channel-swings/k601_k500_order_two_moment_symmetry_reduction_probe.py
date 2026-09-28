#!/usr/bin/env python3
"""Probe and hostile mutations for K601."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "k601_k500_order_two_moment_symmetry_reduction.py"
spec = importlib.util.spec_from_file_location("k601_probe_source", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


payload = module.build()
module.validate(payload)
replay = payload["K179_replay"]
decision = payload["decision"]
checks = [
    payload["result_id"] == "K601-K500-ORDER-TWO-MOMENT-SYMMETRY-REDUCTION",
    replay["complete_order_two_term_count"] == 6,
    replay["terms_per_seed"] == {"0": 2, "1": 2, "2": 2},
    replay["cyclic_overlap_allowed_per_seed"] == {"0": 2, "1": 1, "2": 1},
    replay["common_normalization_prefactor"],
    replay["common_three_resolvent_denominators"],
    replay["common_output_variable_provenance"],
    replay["vacuum_coefficients"] == ["1", "1"],
    replay["one_impurity_coefficients"] == ["-1", "-1"],
    replay["charge_conjugate_coefficients"] == ["-1", "-1"],
    payload["symmetry_reduction"]["q00_leakage_square"] == "b/n-a^2/n^2",
    payload["symmetry_reduction"]["q10_q01_leakage_square"] == "b/n-a^2/(4*n^2)",
    payload["exact_controls"]["cauchy_condition"],
    payload["exact_controls"]["difference_identity_passes"],
    payload["exact_controls"]["q10_lower_passes"],
    decision["first_nonzero_exchange_family_reduced"],
    decision["six_terms_require_six_independent_quadratures"] is False,
    decision["minimum_order_two_scalar_integrals"] == ["n", "a", "b"],
    decision["q10_q01_order_two_leakage_strictly_positive"],
    payload["source_and_ledger_effect"] == "none",
]
assert all(checks)


mutations = [
    ("term count", lambda p: p["K179_replay"].__setitem__("complete_order_two_term_count", 5)),
    ("seed counts", lambda p: p["K179_replay"].__setitem__("terms_per_seed", {"0": 2, "1": 2, "2": 1})),
    ("overlap counts", lambda p: p["K179_replay"].__setitem__("cyclic_overlap_allowed_per_seed", {"0": 2, "1": 2, "2": 2})),
    ("prefactor", lambda p: p["K179_replay"].__setitem__("common_normalization_prefactor", False)),
    ("denominators", lambda p: p["K179_replay"].__setitem__("common_three_resolvent_denominators", False)),
    ("provenance", lambda p: p["K179_replay"].__setitem__("common_output_variable_provenance", False)),
    ("vacuum signs", lambda p: p["K179_replay"].__setitem__("vacuum_coefficients", ["1", "-1"])),
    ("q10 signs", lambda p: p["K179_replay"].__setitem__("one_impurity_coefficients", ["1", "1"])),
    ("q01 signs", lambda p: p["K179_replay"].__setitem__("charge_conjugate_coefficients", ["1", "1"])),
    ("q00 formula", lambda p: p["symmetry_reduction"].__setitem__("q00_leakage_square", "b/n")),
    ("q10 formula", lambda p: p["symmetry_reduction"].__setitem__("q10_q01_leakage_square", "b/n")),
    ("Cauchy", lambda p: p["exact_controls"].__setitem__("cauchy_condition", False)),
    ("difference", lambda p: p["exact_controls"].__setitem__("difference_identity_passes", False)),
    ("lower", lambda p: p["exact_controls"].__setitem__("q10_lower_passes", False)),
    ("erase reduction", lambda p: p["decision"].__setitem__("first_nonzero_exchange_family_reduced", False)),
    ("require six", lambda p: p["decision"].__setitem__("six_terms_require_six_independent_quadratures", True)),
    ("four scalars", lambda p: p["decision"].__setitem__("minimum_order_two_scalar_integrals", ["n", "a", "b", "c"])),
    ("erase positive", lambda p: p["decision"].__setitem__("q10_q01_order_two_leakage_strictly_positive", False)),
    ("invent numerical", lambda p: p["decision"].__setitem__("numerical_order_two_moments_emitted", True)),
    ("invent complete", lambda p: p["decision"].__setitem__("complete_finite_K456_moments_emitted", True)),
    ("invent uniform", lambda p: p["decision"].__setitem__("complete_K500_uniform_leakage_emitted", True)),
    ("invent floor", lambda p: p["decision"].__setitem__("native_noncyclic_floor_emitted", True)),
    ("release K473", lambda p: p["decision"].__setitem__("K473_released", True)),
    ("release K152", lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True)),
]
rejected = 0
for _name, mutate in mutations:
    changed = copy.deepcopy(payload)
    mutate(changed)
    try:
        module.validate(changed)
    except AssertionError:
        rejected += 1
assert rejected == len(mutations)
print(f"{len(checks)}/{len(checks)} exact checks passed; {rejected}/{len(mutations)} hostile mutations rejected")
