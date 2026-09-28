#!/usr/bin/env python3
"""Independent controls and hostile mutations for K591."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "lab/process/k591-k500-spectral-diameter-leakage-boundary.json"


def strict(path):
    return json.loads(path.read_text(), object_pairs_hook=lambda pairs: dict(pairs) if len({k for k, _ in pairs}) == len(pairs) else (_ for _ in ()).throw(ValueError("duplicate key")))


def checks(packet):
    theorem = packet["theorem"]
    controls = packet["exact_controls"]
    native = packet["native_applicability"]
    decision = packet["decision"]
    return [
        packet["result_id"] == "K591-K500-SPECTRAL-DIAMETER-LEAKAGE-BOUNDARY",
        theorem["sharp"] is True,
        theorem["scalar_shift_invariant"] is True,
        theorem["diagonal_multiplier_required"] is False,
        theorem["exchange_blocks_allowed"] is True,
        controls["row_count"] == 4,
        controls["all_bounds_hold"] is True,
        controls["sharp_endpoint_control_present"] is True,
        controls["off_diagonal_exchange_control_present"] is True,
        controls["reducing_line_zero_present"] is True,
        all(row["bound_holds"] and row["tensor_bound_holds"] for row in controls["rows"]),
        native["K583_all_level_tensor_identity_reused"] is True,
        native["K177_higher_level_exchange_terms_retained"] is True,
        native["K580_level_one_result_preserved"] is True,
        native["native_each_level_spectral_interval_serialized"] is False,
        native["native_uniform_spectral_diameter_serialized"] is False,
        native["finite_orders_through_12_supply_all_level_uniform_bound"] is False,
        native["K168_shape_oscillation_supplies_normal_action_diameter"] is False,
        decision["sharp_coefficient_free_leakage_certificate_emitted"] is True,
        decision["complete_native_K500_uniform_leakage_emitted"] is False,
        decision["native_noncyclic_floor_emitted"] is False,
        decision["K473_beta_emitted"] is False,
        decision["native_K152_interval_emitted"] is False,
    ]


packet = strict(PACKET)
base = checks(packet)
mutations = [
    ("lose sharpness", lambda p: p["theorem"].__setitem__("sharp", False)),
    ("require diagonal", lambda p: p["theorem"].__setitem__("diagonal_multiplier_required", True)),
    ("reject exchange", lambda p: p["theorem"].__setitem__("exchange_blocks_allowed", False)),
    ("lose bound", lambda p: p["exact_controls"].__setitem__("all_bounds_hold", False)),
    ("invent native intervals", lambda p: p["native_applicability"].__setitem__("native_each_level_spectral_interval_serialized", True)),
    ("invent uniform diameter", lambda p: p["native_applicability"].__setitem__("native_uniform_spectral_diameter_serialized", True)),
    ("misuse K168", lambda p: p["native_applicability"].__setitem__("K168_shape_oscillation_supplies_normal_action_diameter", True)),
    ("invent K500 release", lambda p: p["decision"].__setitem__("complete_native_K500_uniform_leakage_emitted", True)),
    ("invent floor", lambda p: p["decision"].__setitem__("native_noncyclic_floor_emitted", True)),
]
rejected = 0
for _, mutate in mutations:
    candidate = copy.deepcopy(packet)
    mutate(candidate)
    if not all(checks(candidate)):
        rejected += 1
print(f"K591 EXACT CONTROLS: {sum(base)}/{len(base)} pass")
print(f"K591 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
if not all(base) or rejected != len(mutations):
    raise SystemExit("K591 probe failed")
