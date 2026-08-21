#!/usr/bin/env python3
"""Strict gate for the v0.260 Jacobson/K77 reverse-scaffold append."""

from __future__ import annotations

import copy
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD = ROOT / "lab/process/conditional-physics-ledger-v0.259.json"
NEW = ROOT / "lab/process/conditional-physics-ledger-v0.260.json"


def reject_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in pairs:
        if key in out:
            raise AssertionError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def load_strict(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(), object_pairs_hook=reject_duplicates)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def semantic_gate(ledger: dict[str, object]) -> None:
    rows = ledger["rows"]
    row = next(item for item in rows if item["id"] == "LT-GR8")
    benchmark = next(
        item
        for item in ledger["external_benchmarks"]
        if item["id"] == "EXT-J95-SEMI-CLASSICAL-HORIZON"
    )

    require(benchmark["kind"] == "EXTERNAL_CONDITIONAL_BENCHMARK", "benchmark kind drift")
    require(benchmark["mechanism_commitment"] == "NONE", "mechanism imported")
    require(benchmark["gu_realization_status"].startswith("MISSING_TYPED_K77"), "GU realization laundered")
    require(benchmark["confirmation_credit"] == "NONE", "confirmation credit laundered")
    require(benchmark["not_itself_an_empirical_datum"] is True, "conditional theorem called datum")
    require(
        benchmark["council_vote"]
        == {
            "benchmark_without_mechanism_commitment": 8,
            "direct_reverse_premise": 1,
            "later_validation_only": 1,
        },
        "council vote drift",
    )
    require(row["verdict"] == "NEEDS", "target verdict must remain NEEDS")
    require(row["reason_kind"] == "MISSING_CONSTRUCTION", "wrong missingness type")
    require(row["mechanism_commitment"] == "NONE", "row imports mechanism")
    require(row["confirmation_credit"] == "NONE", "row awards confirmation")
    require(row["external_benchmark_ref"] == benchmark["id"], "benchmark reference mismatch")
    require(
        row["context"] == {
            "layer": "L2",
            "grant": "UNTYPED",
            "carrier": "C2",
            "note": row["context"]["note"],
        },
        "context projection must be L2/UNTYPED/C2",
    )
    require("no node" in row["context"]["note"], "UNTYPED rationale missing")
    protocol = ledger["reverse_scaffold_protocol"]
    require("compatibility" in protocol["adjudication"], "reverse-only ceiling missing")
    require("prediction candidate" in protocol["adjudication"], "held-out prediction rule missing")
    require("without selecting" in protocol["forward_track"], "forward independence missing")


def assert_planted_negative(base: dict[str, object], mutate, label: str) -> None:
    trial = copy.deepcopy(base)
    mutate(trial)
    try:
        semantic_gate(trial)
    except AssertionError:
        return
    raise AssertionError(f"planted negative survived: {label}")


def main() -> None:
    old = load_strict(OLD)
    new = load_strict(NEW)
    require(new["schema_version"] == "0.260", "schema version mismatch")
    require(new["predecessor"].endswith("v0.259.json"), "predecessor mismatch")
    require(new["base_sha256"] == hashlib.sha256(OLD.read_bytes()).hexdigest(), "predecessor digest mismatch")

    old_rows = {row["id"]: row for row in old["rows"]}
    new_rows = {row["id"]: row for row in new["rows"]}
    require(len(old_rows) == len(old["rows"]), "duplicate predecessor row id")
    require(len(new_rows) == len(new["rows"]), "duplicate successor row id")
    require(set(new_rows) - set(old_rows) == {"LT-GR8"}, "not exactly one target append")
    require(set(old_rows) <= set(new_rows), "predecessor row removed")
    for row_id, row in old_rows.items():
        require(new_rows[row_id] == row, f"predecessor row changed: {row_id}")

    active_rows = [row for row in new["rows"] if row.get("row_status") != "SUPERSEDED"]
    verdicts = Counter(row["verdict"] for row in active_rows)
    axes = Counter(row["axis"] for row in active_rows)
    require(new["denominator"]["canonical_target_count"] == 85, "canonical count mismatch")
    require(new["denominator"]["row_record_count"] == len(new["rows"]) == 88, "row count mismatch")
    require(new["denominator"]["axes"] == dict(axes), "axis arithmetic mismatch")
    require(new["progress"]["mapped"] == new["progress"]["total"] == 85, "coverage mismatch")
    require(new["progress"]["verdict_counts"] == dict(verdicts), "verdict arithmetic mismatch")
    require(sum(verdicts.values()) == 85, "active verdict denominator mismatch")
    semantic_gate(new)

    files_and_needles = {
        "CURRENT-STATE.yaml": ["LT-GR8", "Reverse-only recovery earns compatibility", "B5 (9,5) is a scoped comparator"],
        "RESEARCH-STATUS.md": ["Jacobson/K77 reverse-scaffold benchmark", "8 for benchmark-without-mechanism"],
        "NEXT-STEPS.md": ["K77 `(7,7)` AS THE PRIMARY GU ROUTE", "Do not treat it as the main"],
        "explorations/W151-gr-and-c-emergence-from-records-2026-07-14.md": ["BOUNDARY IDENTITY", "proposed typed bridge"],
        "explorations/jacobson-b5-entropy-boundary-transfer-council-2026-08-21.md": ["Priority correction", "scoped comparator"],
        "explorations/jacobson-k77-reverse-scaffold-benchmark-council-2026-08-21.md": ["8-1-1", "Reverse-only success"],
        "explorations/conditional-build/conditional-physics-ledger-v0.260.md": ["LT-GR8", "K77 `(7,7)`"],
        "lab/process/README.md": ["conditional-physics-ledger-v0.260.json"],
        "explorations/README.md": ["Jacobson/K77 reverse-scaffold benchmark council"],
        "tests/README.md": ["jacobson_k77_reverse_scaffold_ledger_probe.py"],
    }
    for relative, needles in files_and_needles.items():
        text = (ROOT / relative).read_text()
        for needle in needles:
            require(needle in text, f"missing front-door phrase {needle!r} in {relative}")

    assert_planted_negative(
        new,
        lambda d: d["external_benchmarks"][0].__setitem__("gu_realization_status", "ESTABLISHED"),
        "external benchmark mistaken for GU realization",
    )
    assert_planted_negative(
        new,
        lambda d: d["external_benchmarks"][0].__setitem__("mechanism_commitment", "JACOBSON"),
        "mechanism import",
    )
    assert_planted_negative(
        new,
        lambda d: next(r for r in d["rows"] if r["id"] == "LT-GR8").__setitem__("confirmation_credit", "PREDICTION"),
        "prediction laundering",
    )
    assert_planted_negative(
        new,
        lambda d: next(r for r in d["rows"] if r["id"] == "LT-GR8").__setitem__("context", {"layer": "L2", "grant": "G8", "carrier": "C2", "note": "forced"}),
        "invented grant",
    )

    print("PASS: v0.260 appends only LT-GR8 and preserves benchmark, mechanism, context, and claim ceilings")


if __name__ == "__main__":
    main()
