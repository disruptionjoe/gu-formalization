#!/usr/bin/env python3
"""Independent controls and hostile mutations for K589."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "lab/process/k589-k77-action-kt-exact-completion.json"


def strict(path):
    return json.loads(path.read_text(), object_pairs_hook=lambda pairs: dict(pairs) if len({k for k, _ in pairs}) == len(pairs) else (_ for _ in ()).throw(ValueError("duplicate key")))


def checks(packet):
    exact = packet["exact_completion"]
    boundary = packet["ownership_boundary"]
    decision = packet["decision"]
    return [
        packet["result_id"] == "K589-K77-ACTION-KT-EXACT-COMPLETION",
        exact["dimensions"] == [21, 91, 70],
        exact["D2_shape"] == [91, 21],
        exact["D2_rank"] == 21,
        exact["D2_nonzero_entries"] == 21,
        exact["D1_shape"] == [70, 91],
        exact["D1_rank"] == 70,
        exact["D1_nonzero_entries"] == 70,
        exact["D1_D2_zero"] is True,
        exact["kernel_D1_dimension"] == 21,
        exact["image_D2_dimension"] == 21,
        exact["kernel_D1_equals_image_D2"] is True,
        exact["homology_dimensions"] == [0, 0, 0],
        exact["euler_characteristic"] == 0,
        exact["higher_linear_reducibility"] == 0,
        boundary["D2_source_owned_by_epsilon_orbit_stabilizer"] is True,
        boundary["D1_action_coupled_through_K588"] is True,
        boundary["finite_homogeneous_orbit_exactness"] is True,
        boundary["nonlinear_functional_KT_properness"] is False,
        boundary["physical_cohomology_constructed"] is False,
        decision["K587_rank21_adjacent_arrow_constructed"] is True,
        decision["K587_base_exact_completion_constructed"] is True,
        decision["selected_source_action_rejected"] is False,
    ]


packet = strict(PACKET)
base = checks(packet)
mutations = [
    ("break nilpotence", lambda p: p["exact_completion"].__setitem__("D1_D2_zero", False)),
    ("break exactness", lambda p: p["exact_completion"].__setitem__("kernel_D1_equals_image_D2", False)),
    ("drop D2 rank", lambda p: p["exact_completion"].__setitem__("D2_rank", 20)),
    ("drop D1 rank", lambda p: p["exact_completion"].__setitem__("D1_rank", 69)),
    ("invent homology", lambda p: p["exact_completion"].__setitem__("homology_dimensions", [0, 1, 0])),
    ("lose source ownership", lambda p: p["ownership_boundary"].__setitem__("D2_source_owned_by_epsilon_orbit_stabilizer", False)),
    ("invent functional properness", lambda p: p["ownership_boundary"].__setitem__("nonlinear_functional_KT_properness", True)),
    ("invent physical cohomology", lambda p: p["ownership_boundary"].__setitem__("physical_cohomology_constructed", True)),
]
rejected = 0
for _, mutate in mutations:
    candidate = copy.deepcopy(packet)
    mutate(candidate)
    if not all(checks(candidate)):
        rejected += 1
print(f"K589 EXACT CONTROLS: {sum(base)}/{len(base)} pass")
print(f"K589 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
if not all(base) or rejected != len(mutations):
    raise SystemExit("K589 probe failed")
