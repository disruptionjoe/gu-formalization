#!/usr/bin/env python3
"""Regression probe for conditional ledger v0.262 verdict/context integration."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "lab/process/conditional-physics-ledger-v0.261.json"
LATEST = ROOT / "lab/process/conditional-physics-ledger-v0.262.json"
DELTA = ROOT / "lab/process/conditional-evidence-deltas/gu-ledger-kill-typing-2026-08-23.json"
INDEX = ROOT / "lab/process/conditional-evidence-deltas/index.json"
REPAIRS = ROOT / "lab/process/mint-context-history-repairs.json"
REGISTRY = ROOT / "lab/process/conditional-ledger-verdict-context-integration.json"

RETYPED = {"AC-F3", "LT-GR1b", "RA-D2"}
REPAIRED = {"AC-B5", "AC-F3", "AC-F4", "LT-GR1b", "LT-GR5", "LT-GR7", "RA-D2", "RA-F3"}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def rows(doc):
    return {row["id"]: row for row in doc["rows"]}


def canonical(row):
    return {key: value for key, value in row.items() if key != "context"}


def row_jsonl_sha(row):
    payload = json.dumps(canonical(row), sort_keys=True, separators=(",", ":")) + "\n"
    return hashlib.sha256(payload.encode()).hexdigest()


def verify(base, latest, delta, index, repairs, registry):
    assert latest["schema_version"] == "0.262"
    assert latest["predecessor"].endswith("v0.261.json")
    assert latest["base_sha256"] == hashlib.sha256(BASE.read_bytes()).hexdigest()
    before, after = rows(base), rows(latest)
    assert set(before) == set(after)

    for rid in RETYPED:
        expected = copy.deepcopy(canonical(before[rid]))
        expected["verdict"] = "DIFFERS"
        expected["reason_kind"] = "ROUTE_KILLED"
        assert canonical(after[rid]) == expected, rid
        assert after[rid]["context"]
    for rid in set(before) - RETYPED:
        assert canonical(after[rid]) == canonical(before[rid]), rid

    active = [row for row in latest["rows"] if row.get("row_status") != "SUPERSEDED"]
    counts = {kind: sum(row["verdict"] == kind for row in active)
              for kind in ("SAME", "DIFFERS", "NEEDS", "OVER_DETERMINED")}
    assert counts == {"SAME": 33, "DIFFERS": 22, "NEEDS": 31, "OVER_DETERMINED": 2}
    assert latest["progress"]["verdict_counts"] == counts
    assert not [row for row in latest["rows"] if row["reason_kind"] == "GENUINE_FALSIFICATION"]

    migrations = [m for m in latest["migration_history"] if m.get("to_version") == "0.262"]
    assert {m["row_id"] for m in migrations} == RETYPED
    assert all(m["new"][:2] == ["DIFFERS", "ROUTE_KILLED"] for m in migrations)
    assert all("no movement toward SAME" in m["scope"] for m in migrations)

    assert delta["status"] == "integrated"
    assert delta["integration"]["canonical_ledger_ref"].endswith("v0.262.json")
    assert index["integration_cursor"] == delta["delta_id"]
    idx = {item["delta_id"]: item["status"] for item in index["deltas"]}
    assert idx[delta["delta_id"]] == "integrated"

    source = load(ROOT / "lab/process/conditional-physics-ledger-v0.260.json")
    source_rows = rows(source)
    assert hashlib.sha256((ROOT / "lab/process/conditional-physics-ledger-v0.260.json").read_bytes()).hexdigest() == "4886eec94f8aaef02c75f844485ac37a26d760fa4ea927832248efa6abeb1a7b"
    repair_rows = repairs["repairs"]
    assert {item["row_id"] for item in repair_rows} == REPAIRED
    assert len(repair_rows) == len(REPAIRED)
    for item in repair_rows:
        rid = item["row_id"]
        assert item["source_ledger_sha256"] == "4886eec94f8aaef02c75f844485ac37a26d760fa4ea927832248efa6abeb1a7b"
        assert item["source_row_jsonl_sha256"] == row_jsonl_sha(source_rows[rid])
        assert item["successor_ledger_ref"].endswith("v0.262.json")
        assert item["context"] == after[rid]["context"]

    assert registry["retyped_rows"] == ["AC-F3", "LT-GR1b", "RA-D2"]
    assert registry["source_claim_killed"] is False
    assert registry["physics_recomputed"] is False


def main():
    docs = [load(path) for path in (BASE, LATEST, DELTA, INDEX, REPAIRS, REGISTRY)]
    verify(*docs)
    sys.path.insert(0, str(ROOT / "process_gates"))
    import mint_context_projection_audit as ct2
    source = load(ROOT / "lab/process/conditional-physics-ledger-v0.260.json")
    source_row = rows(source)["AC-B5"]
    repair = next(
        (item for item in docs[4]["repairs"] if item["row_id"] == "AC-B5"),
        None,
    )
    assert repair is not None
    assert ct2.validate_history_repair(
        ROOT / repair["source_ledger_ref"], repair["source_ledger_ref"],
        source_row, repair) == []
    for key, value in (("source_ledger_sha256", "0" * 64),
                       ("source_row_jsonl_sha256", "0" * 64),
                       ("context", {"layer": "L1", "grant": "G0", "carrier": "C4"})):
        poisoned = copy.deepcopy(repair)
        poisoned[key] = value
        assert ct2.validate_history_repair(
            ROOT / repair["source_ledger_ref"], repair["source_ledger_ref"],
            source_row, poisoned)
    mutations = []

    def plant(label, position, mutate):
        trial = copy.deepcopy(docs)
        mutate(trial[position])
        try:
            verify(*trial)
        except (AssertionError, KeyError, TypeError):
            mutations.append(label)
            return
        raise AssertionError("mutation survived: " + label)

    plant("verdict", 1, lambda d: rows(d)["AC-F3"].update(verdict="OVER_DETERMINED"))
    plant("reason", 1, lambda d: rows(d)["RA-D2"].update(reason_kind="GENUINE_FALSIFICATION"))
    plant("distance", 1, lambda d: rows(d)["LT-GR1b"].update(distance="weakened"))
    plant("unrelated-row", 1, lambda d: rows(d)["RA-F3"].update(verdict="SAME"))
    plant("context", 1, lambda d: rows(d)["AC-F4"]["context"].update(carrier="C1"))
    plant("migration", 1, lambda d: d["migration_history"].pop())
    plant("delta-status", 2, lambda d: d.update(status="pending"))
    plant("cursor", 3, lambda d: d.update(integration_cursor="old"))
    plant("repair-row-hash", 4, lambda d: d["repairs"][0].update(source_row_jsonl_sha256="0" * 64))
    plant("registry-ceiling", 5, lambda d: d.update(source_claim_killed=True))
    print("PASS conditional_ledger_verdict_context_integration_probe")
    print("MUTATIONS %d/10 caught: %s" % (len(mutations), ", ".join(mutations)))
    print("CT2 HISTORY REPAIR 3/3 poisoned pins rejected")


if __name__ == "__main__":
    main()
