#!/usr/bin/env python3
"""Deterministic replay and hostile controls for K338."""

from __future__ import annotations

import copy
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k338_order_seven_complete_gap_axis_peano_bank.py")
MANIFEST = ROOT / "lab/process/k338-order-seven-complete-gap-axis-peano-bank.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k338_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K338 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    producer = load_producer()
    stored = json.loads(MANIFEST.read_text())
    replay = producer.build()
    producer.validate_payload(replay)
    if json.dumps(replay, sort_keys=True) != json.dumps(stored, sort_keys=True):
        raise AssertionError("deterministic K338 replay differs from stored manifest")

    axes = stored["gap_axis_constants"]
    masses = [Fraction(row["K299_peano_mass"]) for row in axes]
    expected = [Fraction(1, 504), Fraction(1, 300), Fraction(1, 160), Fraction(1, 72), Fraction(1, 24)]
    if masses != expected:
        raise AssertionError("K299 Peano mass order changed")
    if len(stored["complete_cover"]["finite_rows"]) != 516:
        raise AssertionError("stored K334 leaf coverage changed")
    if any(len(row["axes"]) != 5 for row in stored["complete_cover"]["finite_rows"]):
        raise AssertionError("a finite leaf lost a gap axis")
    if len(stored["complete_cover"]["analytic_tail_rows"]) != 3:
        raise AssertionError("analytic tail partition changed")
    if not all(
        float(row["peano_weighted_second_directional_constant"]) > 0
        and float(row["complete_value_first_second_abs_uppers"][2]) > 0
        for row in axes
    ):
        raise AssertionError("a K338 constant is nonpositive")

    mutations = [
        lambda p: p["fixed_control"].__setitem__("accepted_subdivision_checksum", "sha256:bad"),
        lambda p: p["fixed_control"].__setitem__("finite_leaf_count", 515),
        lambda p: p["fixed_control"].__setitem__("gap_class_count", 64),
        lambda p: p["fixed_control"].__setitem__("tail_powers_value_first_second", [34, 35, 36]),
        lambda p: p["complete_cover"].__setitem__("origin_uses_degree_27_zero_safe_scaled_envelopes", False),
        lambda p: p["complete_cover"].__setitem__("projective_preconditioning_precedes_interval_substitution", False),
        lambda p: p["complete_cover"].__setitem__("tail_finiteness_is_analytic_not_sampled", False),
        lambda p: p["complete_cover"].__setitem__("literal_B5_border_zeros_retained", False),
        lambda p: p["complete_cover"].__setitem__("shared_entry_substitution_precedes_complete_determinant_enclosure", False),
        lambda p: p["gap_axis_constants"][0].__setitem__("K299_peano_mass", "1/24"),
        lambda p: p["decision"].__setitem__("complete_six_axis_peano_norm_emitted", False),
        lambda p: p["decision"].__setitem__("complete_base_action_column_evaluated", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        payload = copy.deepcopy(stored)
        mutate(payload)
        try:
            producer.validate_payload(payload)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"K338 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K338 complete gap-axis probe passed 10/10 controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
