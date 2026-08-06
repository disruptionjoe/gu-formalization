#!/usr/bin/env python3
"""Fail-closed scope audit for the v0.19 trace-omega Compose migration."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result
    return json.loads(path.read_text(), object_pairs_hook=hook)


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.19.json")
registry = strict(ROOT / "lab/process/trace-omega-higgs-chirality-compose-reconciliation.json")
report = (ROOT / "explorations/conditional-build/trace-omega-higgs-chirality-compose-reconciliation-2026-08-05.md").read_text()
summary = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.19.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-trace-omega-higgs-chirality-compose-review.md").read_text()

assert ledger["schema_version"] == "0.19"
assert registry["source_return"] == "SOURCE-CORRECTS"
assert registry["touched_rows"] == ["RA-D2", "RA-G2", "RA-E3", "RA-E5"]
assert registry["ledger"]["row_changes"] == "FOUR_DISTANCE_MIGRATIONS__ZERO_VERDICT_OR_REASON_KIND_CHANGES"
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["function_valued_at_least"] == 19
assert ledger["residue"]["open_discrete_forks"] == 9
assert ledger["residue"]["quotients_ranked"] == 4
assert "`RA-D2` remains `OVER_DETERMINED/GENUINE_FALSIFICATION`" in report
assert "Build priority one is unchanged" in summary
assert "summary_outruns_artifact" in review
assert "rigor_defends_superseded_or_mistyped_object" in review
assert "symplectic_reduction_veto" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"

print("TRACE_OMEGA_HIGGS_CHIRALITY_COMPOSE_SCOPE_AUDIT_PASS")
