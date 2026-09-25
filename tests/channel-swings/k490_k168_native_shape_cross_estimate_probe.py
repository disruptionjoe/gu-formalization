#!/usr/bin/env python3
"""Independent controls and hostile mutations for K490."""

from __future__ import annotations

import argparse
import copy
import json
from fractions import Fraction
from pathlib import Path

from k490_k168_native_shape_cross_estimate import build


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k490-k168-native-shape-cross-estimate.json"


def q(value: str) -> Fraction:
    return Fraction(value)


def checks(payload: dict) -> list[tuple[str, bool]]:
    rows = payload["native_sector_bounds"]
    q00, q10 = rows
    amplitudes = [Fraction(1), Fraction(1, 2), Fraction(1, 4)]
    weights = [value * value for value in amplitudes]
    a = sum(weights, Fraction())
    b = sum(weights[1:], Fraction())
    odd = weights[1]
    coefficient = b / a
    physical_trial = amplitudes
    physical_tail = [-coefficient * amplitudes[0]] + [
        (1 - coefficient) * value for value in amplitudes[1:]
    ]
    direct_q00 = sum(
        left * sign * right
        for left, sign, right in zip(physical_trial, [-2, 1, -2], physical_tail, strict=True)
    )
    direct_q10 = sum(
        left * sign * right
        for left, sign, right in zip(physical_trial, [1, -2, 1], physical_tail, strict=True)
    )
    tail_norm = b / a
    direct_normalized_sq = direct_q00 * direct_q00 / (a * tail_norm)
    return [
        ("result id", payload["result_id"] == "K490-K168-NATIVE-SHAPE-CROSS-ESTIMATE"),
        ("two native sectors", [row["charge"] for row in rows] == [[0, 0], [1, 0]]),
        ("opposite cross signs", [row["trial_to_corrected_tail_shape_cross_sign"] for row in rows] == ["positive", "negative"]),
        ("q00 formula", q00["corrected_tail_shape_Rayleigh_formula"] == "theta_t=-2+3 O/(A B)"),
        ("q10 formula", q10["corrected_tail_shape_Rayleigh_formula"] == "theta_t=1-3 O/(A B)"),
        ("cross square formula", all(row["M_normalized_shape_cross_sq_formula"] == "9 O^2/(A^2 B)" for row in rows)),
        ("positive cross lower", all(q(row["trial_to_corrected_tail_shape_cross_abs_interval"][0]) > 0 for row in rows)),
        ("ordered cross intervals", all(q(row["trial_to_corrected_tail_shape_cross_abs_interval"][0]) <= q(row["trial_to_corrected_tail_shape_cross_abs_interval"][1]) for row in rows)),
        ("ordered normalized intervals", all(q(row["M_normalized_shape_cross_sq_interval"][0]) <= q(row["M_normalized_shape_cross_sq_interval"][1]) for row in rows)),
        ("q00 shape range", -2 < q(q00["corrected_tail_shape_Rayleigh_interval"][0]) <= q(q00["corrected_tail_shape_Rayleigh_interval"][1]) < 1),
        ("q10 shape range", -2 < q(q10["corrected_tail_shape_Rayleigh_interval"][0]) <= q(q10["corrected_tail_shape_Rayleigh_interval"][1]) < 1),
        ("component released", payload["decision"]["actual_K168_component_cross_bounded"] is True),
        ("base withheld", payload["decision"]["base_R0_cross_bounded"] is False),
        ("combined withheld", payload["decision"]["combined_K139_K168_cross_bounded"] is False),
        ("K473 withheld", payload["decision"]["K473_beta_emitted"] is False),
        ("finite q00 direct cross", direct_q00 == 3 * odd / a),
        ("finite q10 direct cross", direct_q10 == -3 * odd / a),
        ("finite normalized square", direct_normalized_sq == 9 * odd * odd / (a * a * b)),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    stored = json.loads(MANIFEST.read_text())
    rebuilt = build()
    results = checks(stored)
    results.append(("deterministic rebuild", stored == rebuilt))
    if not all(ok for _, ok in results):
        raise AssertionError([name for name, ok in results if not ok])
    mutations = [
        lambda p: p["native_sector_bounds"][0].__setitem__("trial_to_corrected_tail_shape_cross_sign", "negative"),
        lambda p: p["native_sector_bounds"][1].__setitem__("trial_to_corrected_tail_shape_cross_sign", "positive"),
        lambda p: p["native_sector_bounds"][0].__setitem__("M_normalized_shape_cross_sq_formula", "9 O/A"),
        lambda p: p["native_sector_bounds"].pop(),
        lambda p: p["decision"].__setitem__("base_R0_cross_bounded", True),
        lambda p: p["decision"].__setitem__("combined_K139_K168_cross_bounded", True),
        lambda p: p["decision"].__setitem__("K473_beta_emitted", True),
        lambda p: p["native_sector_bounds"][0].__setitem__("trial_to_corrected_tail_shape_cross_abs_interval", ["0", "0"]),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            survived = all(ok for _, ok in checks(candidate))
        except (KeyError, IndexError, ValueError, ZeroDivisionError):
            survived = False
        if not survived:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError("hostile mutation survived")
    print(f"K490 CONTROL: {len(results)}/{len(results)} pass; hostile {rejected}/{len(mutations)} rejected")
    if args.selftest:
        print("K490 SELFTEST: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
