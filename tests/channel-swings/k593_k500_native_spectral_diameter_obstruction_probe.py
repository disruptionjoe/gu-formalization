#!/usr/bin/env python3
"""Independent controls and hostile mutations for K593."""

from __future__ import annotations

import copy
import json
from fractions import Fraction

from k593_k500_native_spectral_diameter_obstruction import build


def controls(payload: dict) -> list[bool]:
    kernel = payload["native_kernel"]
    sectors = payload["native_level_one_sectors"]
    theorem = payload["theorem"]
    decision = payload["decision"]
    lowers = [float(row["D_lower"]) for row in kernel["sampled_lower_bounds"]]
    return [
        payload["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        payload["direction"] == "observed_to_native",
        "1/(omega(k)+256+e)^2" in kernel["strict_monotonicity"],
        "log(e/257)" in kernel["lower_bound"],
        kernel["unbounded"] is True,
        kernel["continuous"] is True,
        len(lowers) == 4,
        all(b > a for a, b in zip(lowers, lowers[1:])),
        [row["seed"] for row in sectors] == ["vacuum", "one_impurity"],
        [row["multiplicity"] for row in sectors] == [1, 2],
        all(row["spectral_diameter"] == "infinity" for row in sectors),
        all(row["weighted_leakage_finite"] is True for row in sectors),
        all(Fraction(row["K580_weighted_leakage_square_upper_exact"]) > 0 for row in sectors),
        "infinite spectral diameter" in theorem["spectral_consequence"],
        "does not imply infinite leakage" in theorem["weighted_vector_boundary"],
        decision["actual_native_level_one_tested"] is True,
        decision["finite_spectral_diameter_route_survives"] is False,
        decision["K591_abstract_theorem_retracted"] is False,
        decision["K580_finite_weighted_leakage_retracted"] is False,
        decision["complete_K500_uniform_leakage_emitted"] is False,
        decision["native_noncyclic_floor_emitted"] is False,
        decision["K473_released"] is False,
        decision["native_K152_interval_emitted"] is False,
        payload["source_and_ledger_effect"] == "none",
        payload["target_claim"] == "NONE-NOT-A-KILL",
    ]


def valid(payload: dict) -> bool:
    return all(controls(payload))


def set_path(payload: dict, path: tuple[object, ...], value: object) -> None:
    target = payload
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value


def main() -> int:
    payload = build()
    assert valid(payload)
    mutations = [
        (("classification",), "SUPPORTED"),
        (("direction",), "native_to_observed"),
        (("native_kernel", "strict_monotonicity"), "unknown"),
        (("native_kernel", "lower_bound"), "bounded"),
        (("native_kernel", "unbounded"), False),
        (("native_kernel", "continuous"), False),
        (("native_kernel", "sampled_lower_bounds"), []),
        (("native_level_one_sectors", 0, "seed"), "other"),
        (("native_level_one_sectors", 0, "multiplicity"), 2),
        (("native_level_one_sectors", 1, "spectral_diameter"), "finite"),
        (("native_level_one_sectors", 0, "weighted_leakage_finite"), False),
        (("native_level_one_sectors", 0, "K580_weighted_leakage_square_upper_exact"), "0"),
        (("theorem", "spectral_consequence"), "finite width"),
        (("theorem", "weighted_vector_boundary"), "infinite spectral width implies infinite leakage"),
        (("decision", "actual_native_level_one_tested"), False),
        (("decision", "finite_spectral_diameter_route_survives"), True),
        (("decision", "K591_abstract_theorem_retracted"), True),
        (("decision", "K580_finite_weighted_leakage_retracted"), True),
        (("decision", "complete_K500_uniform_leakage_emitted"), True),
        (("decision", "native_noncyclic_floor_emitted"), True),
        (("decision", "K473_released"), True),
        (("decision", "native_K152_interval_emitted"), True),
        (("source_and_ledger_effect",), "moved"),
        (("target_claim",), "SC-META-53"),
    ]
    rejected = 0
    for path, value in mutations:
        candidate = copy.deepcopy(payload)
        set_path(candidate, path, value)
        rejected += int(not valid(candidate))
    assert rejected == len(mutations)
    print(json.dumps({"controls_passed": len(controls(payload)), "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
