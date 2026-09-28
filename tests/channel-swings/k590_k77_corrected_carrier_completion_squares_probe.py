#!/usr/bin/env python3
"""Independent controls and hostile mutations for K590."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "lab/process/k590-k77-corrected-carrier-completion-squares.json"


def strict(path):
    return json.loads(path.read_text(), object_pairs_hook=lambda pairs: dict(pairs) if len({k for k, _ in pairs}) == len(pairs) else (_ for _ in ()).throw(ValueError("duplicate key")))


def checks(packet):
    exact = packet["factorized_completion"]
    boundary = packet["ownership_boundary"]
    decision = packet["decision"]
    samples = exact["rational_transport_samples"]
    return [
        packet["result_id"] == "K590-K77-CORRECTED-CARRIER-COMPLETION-SQUARES",
        exact["carrier_rank"] == 512,
        exact["carrier_half_ranks"] == [256, 256],
        exact["degree_dimensions"] == [10752, 46592, 35840],
        exact["lifted_D2_rank"] == 10752,
        exact["lifted_D1_rank"] == 35840,
        exact["middle_kernel_dimension"] == 10752,
        exact["homology_dimensions"] == [0, 0, 0],
        exact["lifted_nilpotence"] is True,
        exact["both_K444_squares_hold_for_all_parallel_projectors"] is True,
        len(samples) == 4,
        all(row["D2_square_defect_rank"] == 0 and row["D1_square_defect_rank"] == 0 for row in samples),
        all(row["projector_idempotent"] and row["transport_orthogonal"] for row in samples),
        exact["all_sample_D2_defects_zero"] is True,
        exact["all_sample_D1_defects_zero"] is True,
        boundary["base_coefficients_from_K589"] is True,
        boundary["carrier_action_is_K441_factorized_identity_transport"] is True,
        boundary["nonfactorized_interacting_carrier_action_constructed"] is False,
        boundary["full_nonlinear_BV_KT_constructed"] is False,
        boundary["physical_boundary_selected"] is False,
        boundary["physical_cohomology_constructed"] is False,
        decision["K587_corrected_carrier_action_identified"] is True,
        decision["K587_both_K444_squares_pass"] is True,
        decision["K587_factorized_completion_endpoint_reached"] is True,
        decision["source_action_rejected"] is False,
    ]


packet = strict(PACKET)
base = checks(packet)
mutations = [
    ("break D2 square", lambda p: p["factorized_completion"].__setitem__("all_sample_D2_defects_zero", False)),
    ("break D1 square", lambda p: p["factorized_completion"].__setitem__("all_sample_D1_defects_zero", False)),
    ("drop D2 rank", lambda p: p["factorized_completion"].__setitem__("lifted_D2_rank", 10751)),
    ("drop D1 rank", lambda p: p["factorized_completion"].__setitem__("lifted_D1_rank", 35839)),
    ("invent homology", lambda p: p["factorized_completion"].__setitem__("homology_dimensions", [0, 1, 0])),
    ("invent nonfactorized action", lambda p: p["ownership_boundary"].__setitem__("nonfactorized_interacting_carrier_action_constructed", True)),
    ("invent full BV", lambda p: p["ownership_boundary"].__setitem__("full_nonlinear_BV_KT_constructed", True)),
    ("invent physical cohomology", lambda p: p["ownership_boundary"].__setitem__("physical_cohomology_constructed", True)),
]
rejected = 0
for _, mutate in mutations:
    candidate = copy.deepcopy(packet)
    mutate(candidate)
    if not all(checks(candidate)):
        rejected += 1
print(f"K590 EXACT CONTROLS: {sum(base)}/{len(base)} pass")
print(f"K590 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
if not all(base) or rejected != len(mutations):
    raise SystemExit("K590 probe failed")
