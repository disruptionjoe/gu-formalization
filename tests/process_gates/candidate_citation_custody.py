#!/usr/bin/env python3
"""P-M14 three-candidate citation-custody gate with planted regressions."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/candidate-citation-custody-v1.json"

EXPECTED_IDS = [
    "keep-and-grade-loop-cost",
    "generation-number-boundary-odd-primary",
    "observer-value-selection",
]


def validate(data: dict) -> list[str]:
    failures: list[str] = []
    candidates = data.get("candidates", [])
    ids = [item.get("candidate_id") for item in candidates]
    if data.get("status") != "protected_apply_review_required":
        failures.append("manifest must retain protected apply/review status")
    if ids != EXPECTED_IDS:
        failures.append(f"candidate roster/order mismatch: {ids}")
    for item in candidates:
        candidate_id = item.get("candidate_id")
        if candidate_id not in EXPECTED_IDS:
            continue
        sources = item.get("primary_sources", [])
        if len(sources) < 6:
            failures.append(f"{candidate_id}: fewer than six primary identities")
        for source in sources:
            for field in ("key", "identifier", "url"):
                if not source.get(field):
                    failures.append(f"{candidate_id}: source missing {field}")
        protected_paths = item.get("protected_paths", [])
        if len(protected_paths) != 2:
            failures.append(f"{candidate_id}: expected paper and staging protected paths")
        for relpath in protected_paths:
            if not relpath.startswith("papers/") or not (ROOT / relpath).is_file():
                failures.append(f"{candidate_id}: invalid protected path {relpath}")
        if len(item.get("required_corrections", [])) < 3:
            failures.append(f"{candidate_id}: required corrections missing")
        if len(item.get("adverse_findings", [])) < 2:
            failures.append(f"{candidate_id}: adverse findings missing")
    return failures


def selftest(data: dict) -> list[str]:
    mutations = []
    missing_candidate = copy.deepcopy(data)
    missing_candidate["candidates"].pop()
    mutations.append(("missing-candidate", missing_candidate))
    missing_source = copy.deepcopy(data)
    missing_source["candidates"][0]["primary_sources"] = []
    mutations.append(("missing-source-set", missing_source))
    missing_identifier = copy.deepcopy(data)
    missing_identifier["candidates"][1]["primary_sources"][0]["identifier"] = ""
    mutations.append(("missing-identifier", missing_identifier))
    missing_corrections = copy.deepcopy(data)
    missing_corrections["candidates"][2]["required_corrections"] = []
    mutations.append(("missing-required-corrections", missing_corrections))
    uncaught = [name for name, mutant in mutations if not validate(mutant)]
    return uncaught


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures = validate(data)
    if failures:
        for failure in failures:
            print(f"[FAIL] {failure}")
        return 1
    print("[PASS] citation custody baseline: 3/3 candidates")
    if args.selftest:
        uncaught = selftest(data)
        if uncaught:
            for name in uncaught:
                print(f"[FAIL] uncaught mutation: {name}")
            return 1
        print("[PASS] citation custody selftest: 4/4 planted regressions caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
