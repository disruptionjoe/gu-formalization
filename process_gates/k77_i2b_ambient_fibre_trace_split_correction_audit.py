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


report = (ROOT / "explorations/conditional-build/selected-k77-i2b-ambient-fibre-trace-split-correction-2026-08-12.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-ambient-fibre-trace-split-correction-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-i2b-ambient-fibre-trace-split-correction-source-return-2026-08-12.md").read_text()
registry = strict_json(ROOT / "lab/process/selected-k77-i2b-ambient-fibre-trace-split-correction.json")
ledger = strict_json(ROOT / "lab/process/conditional-physics-ledger-v0.209.json")

exact = registry["exact_results"]
assert exact["ambient_signature"] == [7, 7]
assert exact["base_signature"] == [1, 3]
assert exact["vertical_fibre_signature"] == [6, 4]
assert exact["ambient_so77_dimension"] == 91
assert exact["vertical_so64_dimension"] == 45
assert exact["ambient_trace_orbit_dimension"] == 13
assert exact["vertical_trace_orbit_dimension"] == 9
assert exact["base_fibre_q_mixing_directions"] == 4
assert exact["metric_fibre_total_directions"] == 10
assert exact["vertical_fibre_joint_image_rank"] == 280
assert exact["soldering_joint_image_rank"] == 140
assert exact["ambient_joint_image_rank"] == 392
assert exact["vertical_soldering_image_intersection_rank"] == 28
assert exact["v0208_exact_matrix_identities_preserved"] is True
assert exact["v0208_complete_fibre_orbit_interpretation_preserved"] is False
assert exact["new_external_datum_required"] is False
assert exact["complete_field_euler_preboundary_derived"] is False
assert "9 genuine motions" in report and "4 motions" in report
assert "Symplectic geometry" in review and "Controls that fired" in review
assert "eqs. `(12.18)-(12.19)`" in source
assert "C^(32,32) + C^(32,32)" in source
assert ledger["schema_version"] == "0.209"
assert ledger["predecessor"].endswith("v0.208.json")
assert ledger["source_return"] == registry["source_return"]
assert len([item for item in ledger["migrations"] if item["to_version"] == "0.209"]) == 3
assert len([item for item in ledger["migration_history"] if item["to_version"] == "0.209"]) == 3
assert registry["constraint_accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED"

print(
    "PASS: v0.208 is preserved as an exact ambient theorem and corrected to "
    "nine fibre plus four soldering directions, with the radial tenth metric "
    "direction and full action Euler/preboundary composition left open."
)
