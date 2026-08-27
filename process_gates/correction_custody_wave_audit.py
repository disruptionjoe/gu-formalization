#!/usr/bin/env python3
"""Fail-closed custody audit for the 2026-08-27 correction wave."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "move1": "tests/chase/MOVE-1/move1_octic_sp64_vs_sp1.py",
    "ahat": "tests/chase/MOVE-1/verify/indep_ahat16.py",
    "w114_test": "tests/W114_slot_identity.py",
    "w114_note": "explorations/W114-slot-identity-2026-07-11.md",
    "ncg": "explorations/gu-as-ncg-spectral-triple-swing-2026-07-21.md",
    "prereg": "explorations/prereg-rung2-dynamical-wall-and-selectability-test-2026-07-29.md",
}

def load() -> dict[str, str]:
    return {name: (ROOT / rel).read_text(encoding="utf-8") for name, rel in FILES.items()}

def checks(texts: dict[str, str], records: list[dict[str, str]]) -> list[tuple[str, bool]]:
    by_id = {row["id"]: row for row in records}
    return [
        ("MOVE-1 honest tangent coefficient", "493, 2419200" in texts["move1"]),
        ("MOVE-1 rank-only comparator retained", "13, 2419200" in texts["move1"]),
        ("independent A-hat honest coefficient", "493, 2419200" in texts["ahat"]),
        ("independent A-hat rank-only comparator retained", "13, 2419200" in texts["ahat"]),
        ("W114 executable real commutant", "M(14,R)(x)_R M(64,H) = M(896,H)" in texts["w114_test"]),
        ("W114 note real commutant", "M(14,R)(x)_R M(64,H) = M(896,H)" in texts["w114_note"]),
        ("NCG note real commutant", "M(14,R) (x)_R M(64,H) = M(896,H)" in texts["ncg"]),
        ("complex commutant residue absent", all("M(14,C)" not in texts[k] for k in ("w114_test", "w114_note", "ncg"))),
        ("winding-one null is preregistered", "**|winding| = 1**" in texts["prereg"]),
        ("M-H16 custody executed", by_id.get("M-H16", {}).get("disposition") == "EXECUTED"),
        ("P-L16 compound residue remains live", by_id.get("P-L16", {}).get("disposition") == "VERIFIED_LIVE"),
    ]

def run(texts: dict[str, str], records: list[dict[str, str]]) -> bool:
    results = checks(texts, records)
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"{sum(ok for _, ok in results)}/{len(results)} checks passed")
    return all(ok for _, ok in results)

def selftest(texts: dict[str, str], records: list[dict[str, str]]) -> bool:
    if not run(texts, records):
        print("SELFTEST REFUSED: live baseline is not clean")
        return False
    mutations = [
        ("drop honest MOVE-1 coefficient", "move1", "493, 2419200", "492, 2419200"),
        ("restore complex W114 factor", "w114_test", "M(14,R)", "M(14,C)"),
        ("drop NCG total algebra", "ncg", " = M(896,H)", ""),
        ("erase winding-one null", "prereg", "**|winding| = 1**", "**winding untyped**"),
    ]
    caught = 0
    for label, key, old, new in mutations:
        planted = dict(texts)
        planted[key] = planted[key].replace(old, new, 1)
        if not run(planted, records):
            caught += 1
            print(f"[CAUGHT] {label}")
        else:
            print(f"[MISSED] {label}")
    planted_records = [dict(row) for row in records]
    next(row for row in planted_records if row["id"] == "M-H16")["disposition"] = "VERIFIED_LIVE"
    if not run(texts, planted_records):
        caught += 1
        print("[CAUGHT] reopen M-H16 custody")
    else:
        print("[MISSED] reopen M-H16 custody")
    print(f"selftest: {caught}/5 planted mutations caught")
    return caught == 5

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    texts = load()
    records = json.loads((ROOT / "lab/process/improvement-register-writeback-adjudication-v2.json").read_text(encoding="utf-8"))["records"]
    return 0 if (selftest(texts, records) if args.selftest else run(texts, records)) else 1

if __name__ == "__main__":
    raise SystemExit(main())
