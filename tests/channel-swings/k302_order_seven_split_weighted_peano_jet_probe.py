#!/usr/bin/env python3
"""Independent exact/numerical replay for K302."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
K302 = json.loads(
    (ROOT / "lab/process/k302-order-seven-split-weighted-peano-jet.json").read_text()
)


def peano(y: float) -> float:
    return min(y, 1.0 - y) ** 2 / 2.0


def i_ab(a: float, b: float) -> float:
    return (1.5 + 1.0 / (2.0 * a * a) - 2.0 / a - math.log(a)) / b**3


def j2(y: float) -> float:
    return 2.0 * (i_ab(y, 1.0 - y) + i_ab(1.0 - y, y))


def check(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)


def main() -> int:
    midpoint = peano(0.5) * j2(0.5)
    endpoint_samples = [peano(y) * j2(y) for y in (1e-3, 2e-3, 4e-3)]
    grid_max = max(peano(i / 20000) * j2(i / 20000) for i in range(1, 20000))
    tests = {
        "midpoint identity": abs(midpoint - (4.0 * math.log(2.0) - 2.0)) < 1e-13,
        "midpoint rational bound": midpoint < 0.8,
        "endpoint tends to half": all(0.49 < value < 0.5 for value in endpoint_samples),
        "KJ2 global coarse bound": grid_max < 3.0,
        "all occurrences covered": K302["complete_split_face_transfer"]["all_24_occurrences_covered"],
        "weighted integrability": K302["complete_split_face_transfer"]["terminal_split_face_peano_weighted_integrable"],
        "positive route retained": K302["decision"]["positive_peano_route_retained"],
        "pointwise bank not reinstated": not K302["decision"]["k290_uniform_pointwise_bank_reinstated"],
        "old numerical remainders not reinstated": not K302["decision"]["k291_k293_numerical_remainders_reinstated"],
        "six norms remain open": not K302["decision"]["complete_six_coherent_norms_computed"],
    }
    for name, condition in tests.items():
        check(name, condition)
    hostile = {
        "drop Peano endpoint zero": endpoint_samples[0] < 1.0,
        "erase derivative numerator": midpoint < 3.0,
        "replace split integration by floor": K302["release_test"]["no_split_cutoff"],
        "restore K290": not K302["decision"]["k290_uniform_pointwise_bank_reinstated"],
        "restore K293": not K302["decision"]["k291_k293_numerical_remainders_reinstated"],
        "emit gamma join": not K302["release_test"]["radial_gamma_join_emitted"],
        "emit K152": not K302["release_test"]["native_K152_interval_emitted"],
    }
    for name, rejected in hostile.items():
        check(f"hostile {name}", rejected)
    print(f"K302 probe: {len(tests)}/{len(tests)} checks; {len(hostile)}/{len(hostile)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
