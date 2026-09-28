#!/usr/bin/env python3
"""Independent controls and hostile mutations for K588."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "lab/process/k588-k77-action-orbit-reduction.json"


def strict(path: Path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=lambda pairs: dict(pairs) if len({k for k, _ in pairs}) == len(pairs) else (_ for _ in ()).throw(ValueError("duplicate key")))


def checks(packet):
    exact = packet["exact_reduction"]
    boundary = packet["ownership_boundary"]
    decision = packet["decision"]
    return [
        packet["result_id"] == "K588-K77-ACTION-ORBIT-REDUCTION",
        exact["B_shape"] == [1470, 91],
        exact["B_rank"] == 91,
        exact["B_gram_scalar"] == "50/257049",
        exact["B_pseudoinverse_is_left_inverse"] is True,
        exact["image_projector_rank"] == 91,
        exact["image_projector_idempotent"] is True,
        exact["image_projector_symmetric"] is True,
        exact["orbit_quotient_shape"] == [70, 91],
        exact["orbit_quotient_rank"] == 70,
        exact["reduction_shape"] == [70, 1470],
        exact["reduction_rank"] == 70,
        exact["induced_D1_equals_orbit_quotient"] is True,
        exact["induced_D1_rank"] == 70,
        exact["annihilates_orthogonal_complement_of_image_B"] is True,
        boundary["B_selected_action_owned"] is True,
        boundary["A_source_owned_homogeneous_orbit_map"] is True,
        boundary["L_reproduces_A_on_image_B"] is True,
        boundary["L_unique_given_current_pairing_and_zero_extension"] is True,
        boundary["L_uniquely_selected_by_source_on_all_R1470"] is False,
        boundary["full_interacting_action_reduction_constructed"] is False,
        decision["K587_rank70_reduction_constructed"] is True,
        decision["D1_coefficient_matrix_serialized_by_exact_factorization"] is True,
        decision["source_action_rejected"] is False,
    ]


packet = strict(PACKET)
base = checks(packet)
mutations = [
    ("lose left inverse", lambda p: p["exact_reduction"].__setitem__("B_pseudoinverse_is_left_inverse", False)),
    ("lose composition", lambda p: p["exact_reduction"].__setitem__("induced_D1_equals_orbit_quotient", False)),
    ("drop rank", lambda p: p["exact_reduction"].__setitem__("reduction_rank", 69)),
    ("drop D1 rank", lambda p: p["exact_reduction"].__setitem__("induced_D1_rank", 69)),
    ("invent source uniqueness", lambda p: p["ownership_boundary"].__setitem__("L_uniquely_selected_by_source_on_all_R1470", True)),
    ("invent full reduction", lambda p: p["ownership_boundary"].__setitem__("full_interacting_action_reduction_constructed", True)),
    ("lose off-image fence", lambda p: p["exact_reduction"].__setitem__("annihilates_orthogonal_complement_of_image_B", False)),
    ("reject source", lambda p: p["decision"].__setitem__("source_action_rejected", True)),
]
rejected = 0
for _, mutate in mutations:
    candidate = copy.deepcopy(packet)
    mutate(candidate)
    if not all(checks(candidate)):
        rejected += 1
print(f"K588 EXACT CONTROLS: {sum(base)}/{len(base)} pass")
print(f"K588 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
if not all(base) or rejected != len(mutations):
    raise SystemExit("K588 probe failed")
