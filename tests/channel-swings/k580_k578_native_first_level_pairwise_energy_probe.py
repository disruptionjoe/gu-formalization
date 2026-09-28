#!/usr/bin/env python3
"""Independent controls and hostile mutations for K580."""

from __future__ import annotations

import copy
import importlib.util
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k580_probe_target", HERE / "k580_k578_native_first_level_pairwise_energy.py")
K580 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(K580)


def checks(payload: dict) -> list[bool]:
    rows = payload["native_sector_pairwise_energy"]
    decision = payload["decision"]
    return [
        payload["result_id"] == "K580-K578-NATIVE-FIRST-LEVEL-PAIRWISE-ENERGY",
        payload["pointwise_lower_certificate"]["strict_positive_mean"] is True,
        [row["charge"] for row in rows] == [[0, 0], [1, 0]],
        [row["components"] for row in rows] == [2, 1],
        [row["D_multiplicity"] for row in rows] == [1, 2],
        all(row["bath_level"] == 1 for row in rows),
        all(Fraction(row["D_pointwise_lower_exact"]) == Fraction(14, 11 * 515 * 517) for row in rows),
        all(Fraction(row["strict_improvement_exact"]) > 0 for row in rows),
        all(row["strictly_improves_K502"] for row in rows),
        payload["pairwise_theorem"]["scalar_256_cancels"] is True,
        payload["pairwise_theorem"]["identical_q00_components_cancel_from_normalization"] is True,
        decision["actual_q00_q10_pairwise_measures_instantiated"] is True,
        decision["actual_q00_q10_first_level_pairwise_energy_upper_emitted"] is True,
        decision["strictly_sharper_than_K502"] is True,
        decision["native_uniform_all_level_variance_emitted"] is False,
        decision["complete_K500_uniform_leakage_emitted"] is False,
        decision["noncyclic_floor_emitted"] is False,
        decision["native_K152_interval_emitted"] is False,
        payload["source_and_ledger_effect"] == "none",
    ]


def main() -> int:
    payload = K580.build()
    controls = checks(payload)
    mutations = [
        lambda p: p["pointwise_lower_certificate"].__setitem__("strict_positive_mean", False),
        lambda p: p["native_sector_pairwise_energy"].pop(),
        lambda p: p["native_sector_pairwise_energy"][0].__setitem__("charge", [9, 9]),
        lambda p: p["native_sector_pairwise_energy"][0].__setitem__("normal_leakage_square_upper_exact", "0"),
        lambda p: p["native_sector_pairwise_energy"][0].__setitem__("strict_improvement_exact", "0"),
        lambda p: p["native_sector_pairwise_energy"][0].__setitem__("strictly_improves_K502", False),
        lambda p: p["decision"].__setitem__("actual_q00_q10_pairwise_measures_instantiated", False),
        lambda p: p["decision"].__setitem__("native_uniform_all_level_variance_emitted", True),
        lambda p: p["decision"].__setitem__("complete_K500_uniform_leakage_emitted", True),
        lambda p: p["decision"].__setitem__("noncyclic_floor_emitted", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        hostile = copy.deepcopy(payload)
        mutate(hostile)
        try:
            K580.validate(hostile)
        except AssertionError:
            rejected += 1
    print(f"K580 controls: {sum(controls)}/{len(controls)}; hostile: {rejected}/{len(mutations)}")
    return 0 if all(controls) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
