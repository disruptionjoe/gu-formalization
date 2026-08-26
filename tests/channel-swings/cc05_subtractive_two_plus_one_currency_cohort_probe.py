#!/usr/bin/env python3
"""Coupled certificate for the complete aged CC-05 subtractive-2+1 cohort."""
from __future__ import annotations

import argparse
import copy
import importlib.util
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SIDECAR = ROOT / "lab/process/canonical-currency-checks.yaml"
AUDIT = ROOT / "process_gates/canonical_currency_audit.py"
CORRECTION = "CC-05-SUBTRACTIVE-TWO-PLUS-ONE"
WAVE = "CC05-WAVE-2026-08-26"
REPAIR = "CC05-REPAIR-2026-08-26"

EXPECTED = {
    "canon/exhaustiveness-by-type-RESULTS.md",
    "canon/final-verdict-generation-count-and-the-open-bridge.md",
    "canon/forcing-slot-toy-rs-RESULTS.md",
    "canon/single-decider-integer-index-RESULTS.md",
    "canon/six-axis-escape-hatch-map-RESULTS.md",
    "canon/three-generations-locate-not-force-CRT-RESULTS.md",
    "explorations/63-perspective-steelman-narratives-2026-07-20.md",
    "explorations/W221-falsify-generation-count-structure-2026-07-14.md",
    "explorations/ac-e1-daifreed-shadow-recomputation-2026-08-12.md",
    "explorations/boyle-turok-foil-class-relative-typing-2026-08-03.md",
    "explorations/conditional-build/selected-k77-coupled-euler-complex-scope-2026-08-08.md",
    "explorations/cptt-triality-native-action-gate-2026-07-15.md",
    "explorations/cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22.md",
    "explorations/external-datum-ledger-and-the-2plus1-product-rule-2026-07-29.md",
    "explorations/frontier-design-packets-index-2026-08-11.md",
    "explorations/generation-sector/n5-generation-count-synthesis-2026-06-23.md",
    "explorations/generation-sector/oq3a-gu-variational-k3-selection-2026-06-23.md",
    "explorations/generation-sector/oq3a-k3-variational-selection-2026-06-23.md",
    "explorations/generation-sector/oq3c-index-additivity-2026-06-23.md",
    "explorations/layer0-pass-on-the-2plus1-count-claim-2026-07-29.md",
    "explorations/n4-two-z3s-2026-07-20.md",
    "explorations/old-vs-eric-ten-specialist-gap-opportunity-council-2026-07-31.md",
    "explorations/path5-branchC-three-generations-firewall-2026-07-11.md",
    "explorations/perspective-and-dialectic/4d-reduction-62-perspective-steelman-hegelian-2026-06-22.md",
    "explorations/portfolio-correction-wave-2026-08-12.md",
    "explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md",
    "explorations/shiab-operator/sc1-oq2c-null-mode-interpretation-2026-06-23.md",
    "explorations/source-action-term-by-term-against-the-spec-2026-07-29.md",
    "explorations/three-seam-prongB-no-fourth-generation-2026-07-21.md",
    "explorations/two-track-perspective-sweep-2026-07-11/A-orthodox-rigor.md",
    "explorations/type-ii1-spectral/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md",
    "explorations/z3-receptacle-design-packet-2026-08-11.md",
    "lab/deep-research/dr1-identification-boundary-eta-2026-06-28.md",
    "lab/deep-research/hardening-report-batch-2026-06-28.md",
    "lab/process/CURRENT-RESEARCH-CONTEXT.md",
    "lab/process/hinge-panel-synthesis-2026-08-03.md",
    "lab/process/improvement-register-2026-08-03.md",
    "lab/sources/claim-mining-toe-weinstein-2026-07-20.md",
    "lab/sources/secondary-summary-boyle-turok-circulating-claims-2026-08-05.md",
}

REPAIRED = {
    "explorations/W221-falsify-generation-count-structure-2026-07-14.md",
    "explorations/cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22.md",
    "explorations/generation-sector/n5-generation-count-synthesis-2026-06-23.md",
    "explorations/generation-sector/oq3a-gu-variational-k3-selection-2026-06-23.md",
    "explorations/generation-sector/oq3a-k3-variational-selection-2026-06-23.md",
    "explorations/generation-sector/oq3c-index-additivity-2026-06-23.md",
    "explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md",
    "explorations/shiab-operator/sc1-oq2c-null-mode-interpretation-2026-06-23.md",
    "explorations/two-track-perspective-sweep-2026-07-11/A-orthodox-rigor.md",
}

BANNER_TOKENS = (
    "Canonical subtractive-2+1 correction (2026-08-26)",
    "not an additive",
    "n_g -> n_g - 1",
    "distinguished",
    "multiplicity",
)


def load_audit():
    spec = importlib.util.spec_from_file_location("canonical_currency_audit", AUDIT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load canonical-currency audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expected_record_keys() -> set[tuple[str, str, str]]:
    keys = {
        (path, "CLEARED-CONSISTENT", REPAIR if path in REPAIRED else WAVE)
        for path in EXPECTED
    }
    keys.update((path, "STALE-FOUND", WAVE) for path in REPAIRED)
    return keys


def validate_records(records: list[dict]) -> list[str]:
    failures: list[str] = []
    selected = [row for row in records if row.get("by") in {WAVE, REPAIR}]
    actual = [
        (str(row.get("file")), str(row.get("verdict")), str(row.get("by")))
        for row in selected
    ]
    if set(actual) != expected_record_keys():
        failures.append("cohort record membership differs from the reviewed 30+9 custody set")
    if len(actual) != len(set(actual)):
        failures.append("cohort contains a duplicate file/verdict/author record")
    for row in selected:
        if row.get("correction_id") != CORRECTION:
            failures.append(f"wrong correction for {row.get('file')}")
        if not str(row.get("note", "")).strip():
            failures.append(f"missing semantic-scope note for {row.get('file')}")
        if row.get("verdict") == "STALE-FOUND" and not str(row.get("pointer", "")).strip():
            failures.append(f"missing stale-finding pointer for {row.get('file')}")
        if not (ROOT / str(row.get("file"))).is_file():
            failures.append(f"missing reviewed file {row.get('file')}")
    return failures


def validate_banners(overrides: dict[str, str] | None = None) -> list[str]:
    failures: list[str] = []
    overrides = overrides or {}
    for path in REPAIRED:
        text = overrides.get(path, (ROOT / path).read_text(encoding="utf-8"))
        for token in BANNER_TOKENS:
            if token not in text:
                failures.append(f"repair fence missing {token!r} in {path}")
    return failures


def validate_dynamic() -> list[str]:
    failures: list[str] = []
    audit = load_audit()
    cfg = audit.default_cfg()
    cfg["as_of"] = "2026-08-26"
    result = audit.compute(cfg)
    row = result["per"][CORRECTION]
    if row["dirty"] != 0 or row["unchecked"] or row["known_stale"]:
        failures.append("CC-05 remains dirty")
    if not EXPECTED.issubset(set(row["cleared"]) | set(row["repaired"])):
        failures.append("CC-05 did not clear every reviewed candidate")
    if len(row["repaired"]) != 10:
        failures.append(f"CC-05 repaired count is {len(row['repaired'])}, expected 10")
    live_dirty = sum(item["dirty"] for item in result["per"].values())
    if live_dirty != 70:
        failures.append(f"live dirty queue is {live_dirty}, expected 70")
    return failures


def selftest(records: list[dict]) -> list[str]:
    escaped: list[str] = []
    selected_indexes = [
        index for index, row in enumerate(records) if row.get("by") in {WAVE, REPAIR}
    ]
    for index in selected_indexes:
        trial = copy.deepcopy(records)
        trial.pop(index)
        if not validate_records(trial):
            escaped.append(f"missing-record mutation {index} escaped")
    trial = copy.deepcopy(records)
    trial.append(copy.deepcopy(records[selected_indexes[0]]))
    if not validate_records(trial):
        escaped.append("duplicate-record mutation escaped")
    trial = copy.deepcopy(records)
    trial[selected_indexes[0]]["verdict"] = "FENCED-COMPARATOR"
    if not validate_records(trial):
        escaped.append("wrong-verdict mutation escaped")
    trial = copy.deepcopy(records)
    trial[selected_indexes[-1]]["correction_id"] = "CC-10-UCSD-EDITED-DERIVATIVE"
    if not validate_records(trial):
        escaped.append("wrong-correction mutation escaped")
    for path in REPAIRED:
        text = (ROOT / path).read_text(encoding="utf-8")
        trial_text = text.replace(BANNER_TOKENS[0], "missing correction heading", 1)
        if not validate_banners({path: trial_text}):
            escaped.append(f"missing-banner mutation escaped for {path}")
    return escaped


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    sidecar = yaml.safe_load(SIDECAR.read_text(encoding="utf-8"))
    records = sidecar.get("checks", [])
    failures = validate_records(records)
    failures.extend(validate_banners())
    failures.extend(validate_dynamic())
    if failures:
        for failure in failures:
            print(f"[FAIL] {failure}")
        return 1
    print("[PASS] complete CC-05 cohort clears with exact scope and repair custody")
    if args.selftest:
        escaped = selftest(records)
        if escaped:
            for failure in escaped:
                print(f"[FAIL] {failure}")
            return 1
        print("[PASS] selftest catches 60/60 record and repair-fence mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
