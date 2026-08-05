#!/usr/bin/env python3
"""Fail-closed wiring audit for the v0.3 cosmological-sector split."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def strict(relative):
    path = ROOT / relative

    def pairs(items):
        keys = [key for key, _ in items]
        assert len(keys) == len(set(keys)), f"duplicate key in {path}"
        return dict(items)

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs)


ledger = strict("lab/process/conditional-physics-ledger-v0.3.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
lanes = (ROOT / "LANES.yaml").read_text(encoding="utf-8")
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.3.md").read_text(encoding="utf-8")
source = (ROOT / "lab/sources/keating-interview-2025-06-12-source-record.md").read_text(encoding="utf-8")
media = (ROOT / "lab/sources/media-index.md").read_text(encoding="utf-8")
report = (ROOT / "explorations/conditional-build/dynamic-cosmological-sector-constraint-rank-2026-08-05.md").read_text(encoding="utf-8")
report_flat = " ".join(report.split())

rows = {row["id"]: row for row in ledger["rows"]}
active = [row for row in ledger["rows"] if row.get("row_status") != "SUPERSEDED"]
directive = contract["active_scientific_directives"][0]

assert ledger["schema_version"] == "0.3"
assert ledger["predecessor"].endswith("conditional-physics-ledger-v0.2.json")
assert len(active) == 82
assert rows["LT-GR2"]["row_status"] == "SUPERSEDED"
assert set(rows["LT-GR2"]["successors"]) == {
    "LT-GR2a", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR2e"
}
assert contract["standing_ledger"]["ref"].endswith("v0.3.json")
assert contract["standing_ledger"]["human_ref"].endswith("v0.3.md")
assert "conditional-physics-ledger-v0.3.json" in lanes
assert "conditional-physics-ledger-v0.2.json" not in lanes

assert directive["id"] == "GU-COSMO-DYNAMIC-01"
assert directive["status"] == "LAYER0_SPLIT_COMPLETED__BUILD_GATES_OPEN"
assert directive["source_return"] == "SOURCE-CONFIRMS"
assert directive["release_condition_met"] is True
assert directive["primary_row_on_hold"] is None
assert set(directive["successor_rows"]) == set(rows["LT-GR2"]["successors"])
assert "CURVATURE_VEV_EULER_COUPLING" in directive["next_gate"]

assert "00:44:13" in source and "00:45:52" in source
assert "SOURCE-CONFIRMS" in source
assert "official Portal Group transcript" in media
assert "spatial-flatness versus four-curvature" in media
assert "Spatially flat de Sitter" in report_flat
assert "action-parameter reduction remains" not in report  # prose uses explicit native burden, not a false pass
assert "No reduction is booked" in report
assert "83 continuous real" in view and "Quotients ranked: 0" in view
assert "P1/P2/P3" in report

print("PASS: v0.3 splits the dynamic cosmological sector append-only, releases the Layer-0 hold, wires the confirmed source and preserves action/rank/magnitude fences")
