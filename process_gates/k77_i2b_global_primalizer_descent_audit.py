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


report = (ROOT / "explorations/conditional-build/selected-k77-i2b-global-primalizer-descent-2026-08-12.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-global-primalizer-descent-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-i2b-global-primalizer-descent-source-return-2026-08-12.md").read_text()
registry = strict_json(ROOT / "lab/process/selected-k77-i2b-global-primalizer-descent.json")
ledger = strict_json(ROOT / "lab/process/conditional-physics-ledger-v0.207.json")

exact = registry["exact_results"]
assert exact["target_complex_coordinates"] == 196
assert exact["target_real_coordinates"] == 392
assert exact["noncommuting_transition_generators"] is True
assert exact["triple_cocycle_failures"] == 0
assert exact["tau_overlap_failures"] == 0
assert exact["pplus_overlap_failures"] == 0
assert exact["pplus_real_rank"] == 196
assert exact["spin_central_sign_cancels_in_adjoint"] is True
assert exact["dot_pplus_rank"] == 56
assert exact["differentiated_idempotency_failures"] == 0
assert exact["off_diagonal_derivative_failures"] == 0
assert exact["moving_naturality_failures"] == 0
assert exact["frozen_projector_firing_basis_vectors"] == 56
assert exact["action_skew_transport_failures"] == 0
assert exact["dot_pplus_action_adjoint_failures"] == 0
assert exact["moving_first_variation_failures"] == 0
assert exact["nontrivial_action_cancellations"] == 2
assert exact["chosen_global_spin_frame_required"] is False
assert exact["source_epsilon_identified"] is False
assert exact["unitary_connection_parent_selected"] is False
assert exact["full_field_euler_preboundary_derived"] is False
assert "full `U(64,64)`" in report and "two `U(32,32)`" in report
assert "Symplectic geometry" in review and "Controls that fired" in review
assert "SOURCE_CONFIRMS" in source and "SOURCE_SILENT" in source
assert registry["constraint_accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED"
assert ledger["schema_version"] == "0.207"
assert ledger["source_return"] == registry["source_return"]
assert len([m for m in ledger["migrations"] if m["to_version"] == "0.207"]) == 3

print(
    "PASS: P_plus descends without a chosen global Spin frame, dot P_plus is "
    "exact and required on the pure-frame orbit, and source epsilon, unitary "
    "parent, full Euler/preboundary, datum, canon and physics remain fenced."
)
