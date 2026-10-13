#!/usr/bin/env python3
"""Hostile scope and mistyping mutations for the K1744 certificate."""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1744-interval-finite-channel-boundary.json").read_text())


def valid(d):
    e = d.get("exact_rational_interval_certificate", {})
    f = d.get("finite_strength_interval_boundary", {})
    z = d.get("decision", {})
    return all([
        d.get("claim_id") == "K1744",
        d.get("proof_partition", {}).get("interval_proof") == "dependency-free rational outward intervals",
        "not finite-strength" in d.get("proof_partition", {}).get("exact_algebra", ""),
        "not interval" in d.get("proof_partition", {}).get("ordinary_floating_regression", ""),
        e.get("q") == "1/1024",
        float(e.get("jacobian", [0, 0])[0]) > 97048,
        float(e.get("k1728_q5_excess", [0, 0])[0]) > 0,
        0 < float(e.get("singular_vertical_gap", [0, 0])[0]) < float(e.get("face_gaps", {}).get("p=1", [0, 0])[0]),
        f.get("full_fisher_interval_status") == "not_proved",
        "python-flint==0.9.0" in f.get("missing_dependency", ""),
        not z.get("finite_strength_fisher_ordering_interval_proved", True),
        z.get("axis_frozen_singular_boundary_discriminator_proved", False),
        not z.get("global_two_radius_optimizer_proved", True),
        not z.get("all_seed_optimizer_proved", True),
        not z.get("source_or_physical_status_change", True),
        "axis-frozen" in d.get("scope_guard", ""),
        "Euclidean" in d.get("scope_guard", ""),
    ])


assert valid(DATA)
mutations = [
    lambda d: d.__setitem__("claim_id", "K1738"),
    lambda d: d["proof_partition"].__setitem__("interval_proof", "ordinary float"),
    lambda d: d["proof_partition"].__setitem__("exact_algebra", "finite-strength proof"),
    lambda d: d["proof_partition"].__setitem__("ordinary_floating_regression", "interval certified"),
    lambda d: d["exact_rational_interval_certificate"].__setitem__("q", "1/1000"),
    lambda d: d["exact_rational_interval_certificate"].__setitem__("jacobian", ["0", "0"]),
    lambda d: d["exact_rational_interval_certificate"].__setitem__("k1728_q5_excess", ["0", "0"]),
    lambda d: d["exact_rational_interval_certificate"].__setitem__("singular_vertical_gap", ["0.2", "0.3"]),
    lambda d: d["finite_strength_interval_boundary"].__setitem__("full_fisher_interval_status", "proved"),
    lambda d: d["finite_strength_interval_boundary"].__setitem__("missing_dependency", "none"),
    lambda d: d["decision"].__setitem__("finite_strength_fisher_ordering_interval_proved", True),
    lambda d: d["decision"].__setitem__("axis_frozen_singular_boundary_discriminator_proved", False),
    lambda d: d["decision"].__setitem__("global_two_radius_optimizer_proved", True),
    lambda d: d["decision"].__setitem__("all_seed_optimizer_proved", True),
    lambda d: d["decision"].__setitem__("source_or_physical_status_change", True),
    lambda d: d.__setitem__("scope_guard", "global boundary theorem"),
]
for index, mutation in enumerate(mutations, 1):
    altered = copy.deepcopy(DATA)
    mutation(altered)
    assert not valid(altered), index
    print(f"PASS {index:02d}: rejected hostile mutation")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
