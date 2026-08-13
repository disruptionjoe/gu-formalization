#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def strict_json(path: Path):
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=unique)


report = (ROOT / "explorations/conditional-build/selected-k77-i2b-full-trace-orbit-derivative-2026-08-12.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-full-trace-orbit-derivative-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-i2b-full-trace-orbit-derivative-source-return-2026-08-12.md").read_text()
registry = strict_json(ROOT / "lab/process/selected-k77-i2b-full-trace-orbit-derivative.json")
ledger = strict_json(ROOT / "lab/process/conditional-physics-ledger-v0.208.json")

exact = registry["exact_results"]
assert exact["so64_generators_tested"] == 91
assert exact["trace_stabilizer_dimension"] == 78
assert exact["trace_orbit_dimension"] == 13
assert exact["target_real_coordinates"] == 392
assert exact["stabilizer_pplus_commutator_failures"] == 0
assert exact["stabilizer_generators_moving_target"] == 12
assert exact["moved_target_fixed_real_failures"] == 0
assert exact["dot_pplus_ranks"] == [56] * 13
assert exact["dot_pplus_joint_image_rank"] == 392
assert exact["differentiated_idempotency_failures"] == 0
assert exact["off_diagonal_derivative_failures"] == 0
assert exact["moving_naturality_failures"] == 0
assert exact["frozen_projector_firing_basis_vectors_per_direction"] == [56] * 13
assert exact["action_skew_generator_failures"] == 0
assert exact["dot_pplus_action_adjoint_failures"] == 0
assert exact["moving_first_variation_failures"] == 0
assert exact["radial_scaling_delta_q_squared"] == -2
assert exact["normalized_trace_orbit_complete"] is True
assert exact["new_external_datum_required"] is False
assert exact["full_u64_64_action_parent_selected"] is False
assert exact["complete_field_euler_preboundary_derived"] is False
assert "C^(32,32) + C^(32,32)" in report
assert "not a source declaration of two independent" in source
assert "Symplectic geometry" in review and "Controls that fired" in review
assert registry["constraint_accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED"
assert ledger["schema_version"] == "0.208"
assert ledger["source_return"] == registry["source_return"]
assert len([m for m in ledger["migrations"] if m["to_version"] == "0.208"]) == 3

print(
    "PASS: all 13 normalized trace-orbit derivatives are exact, rank 56, "
    "jointly span the 392-real target, add no datum, and remain fenced from "
    "arbitrary field Euler/preboundary and unitary-parent selection."
)
