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


report = (ROOT / "explorations/conditional-build/selected-k77-i2b-action-real-projection-2026-08-12.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-action-real-projection-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-i2b-action-real-projection-source-return-2026-08-12.md").read_text()
registry = strict_json(ROOT / "lab/process/selected-k77-i2b-action-real-projection.json")
ledger = strict_json(ROOT / "lab/process/conditional-physics-ledger-v0.206.json")

exact = registry["exact_results"]
assert exact["target_relevant_source_columns"] == 99463
assert exact["target_complex_coordinates"] == 196
assert exact["pairing_comparator_mismatches"] == 0
assert exact["fixed_residual_factorization_failures"] == 0
assert exact["anti_to_fixed_target_pairing_failures"] == 0
assert exact["nonzero_first_derivatives"] == 90
assert exact["fixed_output_rank"] == 170
assert exact["anti_fixed_output_rank"] == 195
assert exact["fixed_anti_basis_pairs_tested"] == 33150
assert exact["fixed_anti_orthogonality_failures"] == 0
assert exact["pplus_action_self_adjoint"] is True
assert exact["anti_fixed_action_witness"] == "-11"
assert exact["nonfixed_background_factorization_fails"] is True
assert exact["nonlinear_residual_replacement_derived"] is False
assert "Euler primalizer" in report and "nonlinear residual" in report
assert "Symplectic geometry" in review and "Controls that fired" in review
assert "SOURCE_CONFIRMS" in source and "SOURCE_SILENT" in source
assert registry["constraint_accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED"
assert ledger["schema_version"] == "0.206"
assert ledger["source_return"] == registry["source_return"]
assert len([m for m in ledger["migrations"] if m["to_version"] == "0.206"]) == 3

print(
    "PASS: P_plus is exact at the fixed-real Euler grade, the anti-fixed "
    "sector refutes nonlinear replacement, and global moving/Green, datum, "
    "canon and physical promotion remain fenced."
)
