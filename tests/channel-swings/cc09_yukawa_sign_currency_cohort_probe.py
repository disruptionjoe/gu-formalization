#!/usr/bin/env python3
"""Coupled certificate for the complete aged CC-09 Yukawa-sign cohort."""
from __future__ import annotations

import argparse
import copy
import importlib.util
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SIDECAR = ROOT / "lab/process/canonical-currency-checks.yaml"
AUDIT = ROOT / "process_gates/canonical_currency_audit.py"
CORRECTION = "CC-09-YUKAWA-REPULSIVE-SIGN"
WAVE = "CC09-WAVE-2026-08-26"
REPAIR = "CC09-REPAIR-2026-08-26"

EXPECTED = {
    "explorations/W122-spin0-gauge-vs-physical-auxfield-2026-07-13.md",
    "explorations/W123-native-r2-running-sign-convention-audit-2026-07-13.md",
    "explorations/W141-steelman-sweep-observational-2026-07-14.md",
    "explorations/W155-ten-divergent-perspectives-tachyon-2026-07-14.md",
    "explorations/W176-build-reduction-x4-effective-2026-07-14.md",
    "explorations/W239-track-b-distinctive-prediction-scan-2026-07-15.md",
    "explorations/conditional-build/selected-second-layer-massive-so3-closure-identifiability-2026-08-07.md",
    "explorations/geometry-curvature-emergence/pc5-higgs-emergence-spec-2026-06-23.md",
    "explorations/path2-branchC-fakeon-2026-07-11.md",
    "explorations/path2-wave5-stageC-tensor-numerators-2026-07-14.md",
    "explorations/path4-branchA-eos-gravity-correlation-2026-07-11.md",
    "explorations/path4-branchE-adversary-arguments-2026-07-11.md",
    "explorations/path4-wave2-alphaW-parameter-free-2026-07-11.md",
    "explorations/resolver-wave-d-native-126-connection-placement-2026-08-03.md",
    "explorations/run-six-move-workflow-results-2026-08-09.md",
    "explorations/source-action-requirements-spec-2026-07-13.md",
    "explorations/track2-conditional-numbers-2026-07-13.md",
    "explorations/type-ii1-spectral/type-ii1-sm-checklist-tightening-2026-06-23.md",
    "explorations/wave22/H10-ppn-weak-field-2026-07-11.md",
    "explorations/wave28/H49-bach-weyl-sector-2026-07-11.md",
    "explorations/wave30/H50-mudw-de-scale-prediction-2026-07-11.md",
    "explorations/wave31/H51-dewitt-coefficient-cL-2026-07-11.md",
    "explorations/wave32/H53-falsifiability-audit-2026-07-11.md",
    "explorations/wave42/renormalization-landscape-scan-2026-07-11.md",
    "explorations/wave5/H16-stelle-viability-2026-07-11.md",
    "lab/active-research/joe-directed/majorana-126-neutrino/src1-source-steelman-of-the-vev-2026-08-14.md",
    "lab/active-research/joe-directed/massless-vector-cosmology/mv1-the-surviving-massless-vectors-meet-the-data-2026-08-14.md",
    "lab/process/exploration-absorption-priorities-2026-08-10.md",
}

REPAIRED = {
    "explorations/W239-track-b-distinctive-prediction-scan-2026-07-15.md",
    "explorations/path4-branchE-adversary-arguments-2026-07-11.md",
    "explorations/path4-wave2-alphaW-parameter-free-2026-07-11.md",
    "explorations/source-action-requirements-spec-2026-07-13.md",
    "explorations/wave28/H49-bach-weyl-sector-2026-07-11.md",
    "explorations/wave30/H50-mudw-de-scale-prediction-2026-07-11.md",
    "explorations/wave31/H51-dewitt-coefficient-cL-2026-07-11.md",
    "explorations/wave32/H53-falsifiability-audit-2026-07-11.md",
    "lab/active-research/joe-directed/massless-vector-cosmology/mv1-the-surviving-massless-vectors-meet-the-data-2026-08-14.md",
}

BANNER_TOKENS = (
    "Canonical Yukawa-sign correction (2026-08-26)",
    "-4/3",
    "repulsive",
    "+1/3",
    "scalaron",
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
        failures.append("cohort record membership differs from the reviewed 28+9 custody set")
    if len(actual) != len(set(actual)):
        failures.append("cohort contains a duplicate file/verdict/author record")
    for row in selected:
        if row.get("correction_id") != CORRECTION:
            failures.append(f"wrong correction for {row.get('file')}")
        if not str(row.get("note", "")).strip():
            failures.append(f"missing semantic-scope note for {row.get('file')}")
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
        failures.append("CC-09 remains dirty")
    if set(row["cleared"]) & EXPECTED != EXPECTED - REPAIRED:
        failures.append("CC-09 consistent set differs from its reviewed cohort")
    if set(row["repaired"]) != REPAIRED:
        failures.append("CC-09 repaired set differs from its exact repair custody")
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
    print("[PASS] complete CC-09 cohort clears with exact scope and repair custody")
    if args.selftest:
        escaped = selftest(records)
        if escaped:
            for failure in escaped:
                print(f"[FAIL] {failure}")
            return 1
        print("[PASS] selftest catches 49/49 record and repair-fence mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
