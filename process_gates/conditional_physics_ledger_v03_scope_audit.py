#!/usr/bin/env python3
"""Fail-closed historical snapshot audit for the v0.3 cosmological split.

This module also owns the reusable v0.3--v0.17 ancestry predicate. Historical
certificates prove their immutable snapshot and require the live append-only
ledger to descend to it; they never require an old pointer to remain current.
"""

from copy import deepcopy
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


def reaches_historical_snapshot(contract, target_relative, overrides=None):
    """Return true only for an exact, finite predecessor walk to the target."""
    if contract.get("standing_ledger", {}).get("append_only") is not True:
        return False
    target = (ROOT / target_relative).resolve()
    cursor_relative = contract["standing_ledger"].get("ref")
    seen = set()
    overrides = overrides or {}
    while cursor_relative:
        cursor = (ROOT / cursor_relative).resolve()
        if cursor == target:
            return cursor.is_file()
        if cursor_relative in seen:
            return False
        seen.add(cursor_relative)
        if cursor_relative in overrides:
            payload = overrides[cursor_relative]
        elif cursor.is_file():
            payload = strict(cursor_relative)
        else:
            return False
        cursor_relative = payload.get("predecessor")
    return False


def main():
    target_relative = "lab/process/conditional-physics-ledger-v0.3.json"
    ledger = strict(target_relative)
    contract = strict("lab/methods/research-evidence-contract-v1.0.json")
    view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.3.md").read_text(encoding="utf-8")
    source = (ROOT / "lab/sources/keating-interview-2025-06-12-source-record.md").read_text(encoding="utf-8")
    media = (ROOT / "lab/sources/media-index.md").read_text(encoding="utf-8")
    report = (ROOT / "explorations/conditional-build/dynamic-cosmological-sector-constraint-rank-2026-08-05.md").read_text(encoding="utf-8")
    report_flat = " ".join(report.split())

    rows = {row["id"]: row for row in ledger["rows"]}
    active = [row for row in ledger["rows"] if row.get("row_status") != "SUPERSEDED"]

    assert ledger["schema_version"] == "0.3"
    assert ledger["predecessor"].endswith("conditional-physics-ledger-v0.2.json")
    assert len(active) == 82
    assert rows["LT-GR2"]["row_status"] == "SUPERSEDED"
    assert set(rows["LT-GR2"]["successors"]) == {
        "LT-GR2a", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR2e"
    }
    assert reaches_historical_snapshot(contract, target_relative)

    no_append = deepcopy(contract)
    no_append["standing_ledger"]["append_only"] = False
    assert not reaches_historical_snapshot(no_append, target_relative)
    skipped = {"lab/process/conditional-physics-ledger-v0.4.json": {
        "predecessor": "lab/process/conditional-physics-ledger-v0.2.json"
    }}
    assert not reaches_historical_snapshot(contract, target_relative, skipped)
    cycle = {"lab/process/conditional-physics-ledger-v0.4.json": {
        "predecessor": "lab/process/conditional-physics-ledger-v0.5.json"
    }}
    assert not reaches_historical_snapshot(contract, target_relative, cycle)
    missing = {"lab/process/conditional-physics-ledger-v0.4.json": {
        "predecessor": "lab/process/conditional-physics-ledger-v0.missing.json"
    }}
    assert not reaches_historical_snapshot(contract, target_relative, missing)

    assert "00:44:13" in source and "00:45:52" in source
    assert "SOURCE-CONFIRMS" in source
    assert "official Portal Group transcript" in media
    assert "spatial-flatness versus four-curvature" in media
    assert "Spatially flat de Sitter" in report_flat
    assert "action-parameter reduction remains" not in report
    assert "No reduction is booked" in report
    assert "83 continuous real" in view and "Quotients ranked: 0" in view
    assert "P1/P2/P3" in report

    print("PASS: historical v0.3 snapshot is immutable and reachable from the current append-only ledger; 4/4 hostile ancestry controls fire")


if __name__ == "__main__":
    main()
