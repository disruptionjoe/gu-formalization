#!/usr/bin/env python3
"""Strict v0.260 -> v0.261 conditional benchmark integration gate."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OLD_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.260.json"
NEW_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.261.json"
REG_PATH = ROOT / "lab/process/conditional-benchmark-delta-integration.json"
INDEX_PATH = ROOT / "lab/process/conditional-evidence-deltas/index.json"
GR_DELTA = ROOT / "lab/process/conditional-evidence-deltas/gu-ext-gr-bench-widening-2026-08-23.json"
LINK_DELTA = ROOT / "lab/process/conditional-evidence-deltas/gu-ext-sm-cosmo-bench-linking-2026-08-23.json"
GR_REG = ROOT / "lab/process/ext-gr-benchmark-bench-registry.json"
SM_REG = ROOT / "lab/process/ext-sm-cosmo-anchors-acceptance-and-descents.json"
RESULT_PATH = ROOT / "explorations/conditional-build/conditional-benchmark-delta-integration-2026-08-23.md"
SUMMARY_PATH = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.261.md"

NEW_IDS = ["LT-GR9", "LT-GR10", "LT-GR11"]
GR_BENCH_IDS = ["EXT-GR-STRONGFIELD", "EXT-GR-PPN", "EXT-GR-ROTATION"]
ALL_BENCH_IDS = [
    "EXT-J95-SEMI-CLASSICAL-HORIZON",
    *GR_BENCH_IDS,
    "EXT-SM-STRUCTURE",
    "EXT-COSMO-BACKGROUND",
]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def without_context(row):
    return {key: value for key, value in row.items() if key != "context"}


def validate(data: dict, old: dict, *, files: bool = True) -> list[str]:
    defects: list[str] = []
    old_rows = {row["id"]: row for row in old["rows"]}
    rows = {row["id"]: row for row in data.get("rows", [])}
    if data.get("schema_version") != "0.261":
        defects.append("schema version")
    if data.get("predecessor") != "lab/process/conditional-physics-ledger-v0.260.json":
        defects.append("predecessor ref")
    expected_sha = hashlib.sha256(OLD_PATH.read_bytes()).hexdigest()
    if data.get("base_sha256") != expected_sha:
        defects.append("predecessor digest")
    if [row["id"] for row in data.get("rows", []) if row["id"] not in old_rows] != NEW_IDS:
        defects.append("exact appended row order")
    if set(rows) != set(old_rows) | set(NEW_IDS):
        defects.append("row id set")
    for row_id, before in old_rows.items():
        after = rows.get(row_id, {})
        if row_id in {"LT-SM8", "LT-GR2"}:
            if without_context(after) != without_context(before):
                defects.append(f"predecessor content changed {row_id}")
        elif after != before:
            defects.append(f"predecessor row changed {row_id}")
    expected_refs = dict(zip(NEW_IDS, GR_BENCH_IDS))
    for row_id, benchmark_id in expected_refs.items():
        row = rows.get(row_id, {})
        expected = {
            "verdict": "NEEDS",
            "reason_kind": "MISSING_CONSTRUCTION",
            "external_benchmark_ref": benchmark_id,
            "mechanism_commitment": "NONE",
            "confirmation_credit": "NONE",
            "target_claim": "NONE-NOT-A-KILL",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                defects.append(f"{row_id} {key}")
        context = row.get("context")
        if not isinstance(context, dict) or context.get("layer") != "L2" or context.get("grant") != "UNTYPED" or context.get("carrier") != "C2":
            defects.append(f"{row_id} context")
        if not row.get("kill_scope", "").endswith("_ONLY"):
            defects.append(f"{row_id} kill scope")
    sm8 = rows.get("LT-SM8", {}).get("context", {})
    if sm8.get("grant") != ["G5", "G7"] or "OWNER-F" not in sm8.get("note", ""):
        defects.append("LT-SM8 owner/grant context")
    gr2 = rows.get("LT-GR2", {}).get("context", {})
    if gr2.get("layer") != "L2" or gr2.get("carrier") != "C2" or "OWNER-C" not in gr2.get("note", "") or "joint discharge" not in gr2.get("note", ""):
        defects.append("LT-GR2 owner context")
    active = [row for row in data.get("rows", []) if row.get("row_status") != "SUPERSEDED"]
    verdicts = {key: 0 for key in ("SAME", "DIFFERS", "NEEDS", "OVER_DETERMINED")}
    axes = {key: 0 for key in ("REPRESENTATION", "LAGRANGIAN", "ANOMALY_CONSISTENCY")}
    for row in active:
        verdicts[row["verdict"]] += 1
        axes[row["axis"]] += 1
    den = data.get("denominator", {})
    if len(active) != 88 or len(data.get("rows", [])) != 91:
        defects.append("row denominator")
    if den.get("canonical_target_count") != 88 or den.get("row_record_count") != 91 or den.get("source_row_count") != 90:
        defects.append("declared denominator")
    if axes != {"REPRESENTATION": 35, "LAGRANGIAN": 27, "ANOMALY_CONSISTENCY": 26} or den.get("axes") != axes:
        defects.append("axis counts")
    if verdicts != {"SAME": 33, "DIFFERS": 19, "NEEDS": 31, "OVER_DETERMINED": 5}:
        defects.append("verdict counts")
    if data.get("progress", {}).get("verdict_counts") != verdicts:
        defects.append("declared verdict counts")
    benchmarks = data.get("external_benchmarks", [])
    if [item.get("id") for item in benchmarks] != ALL_BENCH_IDS:
        defects.append("external benchmark set/order")
    gr_source = {item["id"]: item for item in load(GR_REG)["benchmarks"]}
    sm_source = {item["id"]: item for item in load(SM_REG)["anchors"]}
    by_benchmark = {item["id"]: item for item in benchmarks}
    for benchmark_id, item in {**gr_source, **sm_source}.items():
        if by_benchmark.get(benchmark_id) != item:
            defects.append(f"benchmark registry drift {benchmark_id}")
    if files:
        registry = load(REG_PATH)
        if registry.get("appended_rows") != NEW_IDS or registry.get("counts", {}).get("external_benchmarks") != 6:
            defects.append("integration registry")
        for path in (GR_DELTA, LINK_DELTA):
            delta = load(path)
            integration = delta.get("integration") or {}
            if delta.get("status") != "integrated" or integration.get("disposition") != "incorporated" or integration.get("canonical_ledger_ref") != "lab/process/conditional-physics-ledger-v0.261.json":
                defects.append(f"delta disposition {path.name}")
        index = load(INDEX_PATH)
        if index.get("integration_cursor") != "GU-LEDGER-KILL-TYPING-2026-08-23":
            defects.append("integration cursor")
        statuses = {item["delta_id"]: item["status"] for item in index.get("deltas", [])}
        if statuses.get("GU-EXT-GR-BENCH-WIDENING-2026-08-23") != "integrated" or statuses.get("GU-EXT-SM-COSMO-BENCH-LINKING-2026-08-23") != "integrated" or statuses.get("GU-LEDGER-KILL-TYPING-2026-08-23") != "integrated":
            defects.append("index statuses")
        prose = (RESULT_PATH.read_text(encoding="utf-8") + SUMMARY_PATH.read_text(encoding="utf-8")).lower()
        for phrase in ("gu-comparator-routing", "reverse-only recovery", "zero predecessor verdict changes", "none-not-a-kill"):
            if phrase not in prose:
                defects.append(f"prose ceiling {phrase}")
    return defects


def main() -> int:
    old = load(OLD_PATH)
    new = load(NEW_PATH)
    defects = validate(new, old)
    if defects:
        for defect in defects:
            print(f"FAIL|conditional_benchmark_delta_integration|{defect}")
        return 1

    mutations = []
    cases = [
        ("dropped-row", lambda d: d["rows"].pop()),
        ("verdict-launder", lambda d: next(row for row in d["rows"] if row["id"] == "LT-GR9").update(verdict="SAME")),
        ("mechanism-import", lambda d: next(row for row in d["rows"] if row["id"] == "LT-GR10").update(mechanism_commitment="JACOBSON")),
        ("confirmation-launder", lambda d: next(row for row in d["rows"] if row["id"] == "LT-GR11").update(confirmation_credit="CONFIRMED")),
        ("benchmark-ref-drift", lambda d: next(row for row in d["rows"] if row["id"] == "LT-GR11").update(external_benchmark_ref="EXT-GR-PPN")),
        ("predecessor-verdict-drift", lambda d: (lambda row: row.update(verdict="SAME" if row["verdict"] != "SAME" else "NEEDS"))(next(row for row in d["rows"] if row["id"] == "LT-GR1"))),
        ("sm-grant-loss", lambda d: next(row for row in d["rows"] if row["id"] == "LT-SM8")["context"].update(grant="G5")),
        ("owner-c-loss", lambda d: next(row for row in d["rows"] if row["id"] == "LT-GR2")["context"].update(note="none")),
        ("target-kill", lambda d: next(row for row in d["rows"] if row["id"] == "LT-GR9").update(target_claim="UNREGISTERED-KILL")),
        ("count-drift", lambda d: d["denominator"].update(canonical_target_count=87)),
        ("duplicate-benchmark", lambda d: d["external_benchmarks"].append(copy.deepcopy(d["external_benchmarks"][-1]))),
        ("base-digest-drift", lambda d: d.update(base_sha256="0" * 64)),
    ]
    for name, mutate in cases:
        candidate = copy.deepcopy(new)
        mutate(candidate)
        if validate(candidate, old, files=False):
            mutations.append(name)
    if len(mutations) != len(cases):
        missing = [name for name, _ in cases if name not in mutations]
        print(f"FAIL|conditional_benchmark_delta_integration|mutation_catches={len(mutations)}/{len(cases)} missing={','.join(missing)}")
        return 1
    print("PASS|conditional_benchmark_delta_integration|checks=ledger+registries+deltas+cursor+ceilings")
    print(f"PASS|conditional_benchmark_delta_integration|mutation_catches={len(mutations)}/{len(cases)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
