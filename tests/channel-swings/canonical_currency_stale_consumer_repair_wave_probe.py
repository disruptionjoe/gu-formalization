#!/usr/bin/env python3
"""Coupled certificate for the CC-11--CC-13 stale-consumer repair wave."""
from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SIDECAR = ROOT / "lab/process/canonical-currency-checks.yaml"
RESULT = ROOT / "lab/process/canonical-currency-stale-consumer-repair-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/canonical-currency-stale-consumer-repair-wave-2026-08-25.md"
AUDIT = ROOT / "process_gates/canonical_currency_audit.py"
WORK_ITEM = "CC1113-REPAIR-2026-08-25"

FILES = {
    "cc11": ROOT / "explorations/twentyfive-lens-what-is-a-generation-2026-08-09.md",
    "cc12a": ROOT / "explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md",
    "cc12b": ROOT / "explorations/source-action-requirements-spec-2026-07-13.md",
    "cc12c": ROOT / "explorations/wave8/H23-source-action-construction-2026-07-11.md",
    "cc13a": ROOT / "explorations/W177-build-connection-curvature-c2-2026-07-14.md",
    "cc13b": ROOT / "lab/active-research/joe-directed/anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md",
    "cc13c": ROOT / "lab/active-research/joe-directed/majorana-126-neutrino/mj2-no-native-126-carrier-2026-08-14.md",
}

IDS = (
    "CC-11-ODD-Q-KREIN-HALF-NULLITY",
    "CC-12-SHIAB-ZERO-INSERTION-SCOPE",
    "CC-13-SG4-IMPORTED-AXIS-CARDINALITY",
    "CC-14-SG4-OBSERVED-EPOCH-BINNING",
    "CC-15-SG4-ONE-WAY-CONSISTENCY-PRICE",
)

REQUIRED = {
    "cc11": (
        "halves are totally null and cross-paired in the odd-`q`",
        "Euclidean `(14,0)` control has definite\n  opposite halves",
    ),
    "cc12a": (
        "This excludes only the bare\n  zero-insertion Hom domain",
        "Odd class-2 insertions can admit nonzero pairing",
    ),
    "cc12b": (
        "bare zero-insertion Majorana scalar",
        "odd class-2 insertions can admit nonzero pairing shapes",
    ),
    "cc12c": (
        "bare\ndegree-zero same-chirality Majorana channel is absent",
        "Odd class-2 insertions\nare outside that Hom computation and remain open",
    ),
    "cc13a": (
        "source-imported two-axis SG4 residual whose survival, not cardinality, was measured",
        "both source-imported axes survive the enumeration",
    ),
    "cc13b": (
        "two source-imported SG4 axes, and the enumeration measures only that neither is eliminated",
    ),
    "cc13c": (
        "two source-imported axes whose survival, not cardinality, was measured",
    ),
}

FORBIDDEN = {
    "cc11": ("`(7,7)` and `(14,0)` alike, with each chirality half **totally null**",),
    "cc12a": ("same-chirality Majorana\n  scalar mass **must** be supplied",),
    "cc12b": ("so same-chirality mass requires an equivariance-breaking spurion",),
    "cc12c": ("same-chirality Majorana channel is\nabsent from the equivariant family",),
    "cc13a": ("measured 2-bit SG4 residual",),
    "cc13b": ("leaves a measured 2-bit SG4 residual",),
    "cc13c": ("a measured 2-bit residual",),
}


def _load_audit():
    spec = importlib.util.spec_from_file_location("canonical_currency_audit", AUDIT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load canonical-currency audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_texts() -> dict[str, str]:
    return {key: path.read_text(encoding="utf-8") for key, path in FILES.items()}


def validate_static(texts: dict[str, str]) -> tuple[list[str], int]:
    failures: list[str] = []
    checks = 0

    for key, phrases in REQUIRED.items():
        for phrase in phrases:
            checks += 1
            if phrase not in texts[key]:
                failures.append(f"{key} missing corrected clause: {phrase}")
    for key, phrases in FORBIDDEN.items():
        for phrase in phrases:
            checks += 1
            if phrase in texts[key]:
                failures.append(f"{key} retains stale clause: {phrase}")

    sidecar = yaml.safe_load(SIDECAR.read_text(encoding="utf-8"))
    repairs = [row for row in sidecar.get("checks", []) if row.get("by") == WORK_ITEM]
    checks += 2
    if len(repairs) != 7:
        failures.append(f"repair sidecar count {len(repairs)} != 7")
    pairs = {(str(row.get("file")), str(row.get("correction_id"))) for row in repairs}
    if len(pairs) != 7 or any(row.get("verdict") != "CLEARED-CONSISTENT" for row in repairs):
        failures.append("repair sidecar does not contain seven unique clearing pairs")

    baseline = (sidecar.get("ratchet") or {}).get("baseline") or {}
    for cid in IDS:
        checks += 1
        if baseline.get(cid) != 0:
            failures.append(f"{cid} current baseline {baseline.get(cid)!r} != 0")

    result = json.loads(RESULT.read_text(encoding="utf-8"))
    checks += 3
    if result.get("historical_stale_count") != 7:
        failures.append("result lost historical stale count 7")
    if result.get("current_stale_count") != 0:
        failures.append("result current stale count is not zero")
    if len(result.get("packets") or []) != 3:
        failures.append("result does not contain three repair packets")

    artifact = ARTIFACT.read_text(encoding="utf-8")
    for phrase in (
        "GU-COMPARATOR-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY",
        "```gu-typed-objects",
        "target_claim: NONE-NOT-A-KILL",
        "stale baselines for CC-11, CC-12 and CC-13 therefore move from `1/3/3` to",
    ):
        checks += 1
        if phrase not in artifact:
            failures.append(f"artifact missing governance/result clause: {phrase}")
    return failures, checks


def validate_dynamic() -> tuple[list[str], int]:
    failures: list[str] = []
    checks = 0
    audit = _load_audit()
    cfg = audit.default_cfg()
    cfg["as_of"] = "2026-08-25"
    result = audit.compute(cfg)
    for cid in IDS:
        row = result["per"][cid]
        checks += 2
        if row["known_stale"]:
            failures.append(f"{cid} still has current known-stale consumers")
        if row["baseline"] != 0:
            failures.append(f"{cid} computed baseline {row['baseline']!r} != 0")
    return failures, checks


def selftest(baseline: dict[str, str]) -> list[str]:
    mutations = (
        ("cc11", "halves are totally null and cross-paired in the odd-`q`"),
        ("cc12a", "Odd class-2 insertions can admit nonzero pairing"),
        ("cc12b", "odd class-2 insertions can admit nonzero pairing shapes"),
        ("cc12c", "Odd class-2 insertions\nare outside that Hom computation and remain open"),
        ("cc13a", "both source-imported axes survive the enumeration"),
        ("cc13b", "two source-imported SG4 axes, and the enumeration measures only that neither is eliminated"),
        ("cc13c", "two source-imported axes whose survival, not cardinality, was measured"),
    )
    escaped: list[str] = []
    for key, phrase in mutations:
        trial = copy.deepcopy(baseline)
        trial[key] = trial[key].replace(phrase, "MUTATED_STALE_SCOPE", 1)
        failures, _ = validate_static(trial)
        if not failures:
            escaped.append(f"mutation escaped: {key}")
    return escaped


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()

    texts = load_texts()
    failures, static_checks = validate_static(texts)
    dynamic_failures, dynamic_checks = validate_dynamic()
    failures.extend(dynamic_failures)
    if failures:
        for failure in failures:
            print(f"[FAIL] {failure}")
        return 1
    print(f"[PASS] {static_checks + dynamic_checks}/{static_checks + dynamic_checks} repair and audit checks pass")
    if args.selftest:
        escaped = selftest(texts)
        if escaped:
            for failure in escaped:
                print(f"[FAIL] {failure}")
            return 1
        print("[PASS] selftest 7/7 stale-scope mutations detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
