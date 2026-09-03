#!/usr/bin/env python3
"""Coupled certificate for the 2026-08-25 canonical-currency stewardship wave.

This verifies repository process truth only: registry enrollment, exact
signature-candidate adjudication, recorded verdicts, ratchet baselines, B2
steering currency, and the unchanged CT-5 certificate. It does not verify the
underlying mathematical or source-level corrections.
"""
from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/correction-registry.yaml"
SIDECAR = ROOT / "lab/process/canonical-currency-checks.yaml"
AGENDA = ROOT / "lab/process/RESEARCH-AGENDA.json"
UPGRADES = ROOT / "lab/process/upgrade-program-register.yaml"
CURRENT = ROOT / "CURRENT-STATE.yaml"
EVIDENCE = ROOT / "explorations/canonical-currency-and-steering-reconciliation-2026-08-25.md"
CT5 = ROOT / "tests/channel-swings/joe_directed_ct5_canonical_corrections_as_dirty_bits.py"
AUDIT = ROOT / "process_gates/canonical_currency_audit.py"

WORK_ITEM = "GU-FORMALIZATION-STEWARDSHIP-2026-08-25"
IDS = (
    "CC-11-ODD-Q-KREIN-HALF-NULLITY",
    "CC-12-SHIAB-ZERO-INSERTION-SCOPE",
    "CC-13-SG4-IMPORTED-AXIS-CARDINALITY",
    "CC-14-SG4-OBSERVED-EPOCH-BINNING",
    "CC-15-SG4-ONE-WAY-CONSISTENCY-PRICE",
)
EXPECTED_COUNTS = dict(zip(IDS, (10, 29, 4, 6, 3)))
EXPECTED_CURRENT_COUNTS = dict(zip(IDS, (9, 29, 1, 6, 3)))
EXPECTED_BASELINES = dict(zip(IDS, (0, 0, 0, 0, 0)))
EXPECTED_HISTORICAL_STALE = {
    IDS[0]: {"explorations/twentyfive-lens-what-is-a-generation-2026-08-09.md"},
    IDS[1]: {
        "explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md",
        "explorations/source-action-requirements-spec-2026-07-13.md",
        "explorations/wave8/H23-source-action-construction-2026-07-11.md",
    },
    IDS[2]: {
        "explorations/W177-build-connection-curvature-c2-2026-07-14.md",
        "lab/active-research/joe-directed/anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md",
        "lab/active-research/joe-directed/majorana-126-neutrino/mj2-no-native-126-carrier-2026-08-14.md",
    },
    IDS[3]: set(),
    IDS[4]: set(),
}
EXPECTED_CURRENT_STALE = {cid: set() for cid in IDS}


def _load_audit():
    spec = importlib.util.spec_from_file_location("canonical_currency_audit", AUDIT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load canonical-currency audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_state() -> dict:
    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    sidecar = yaml.safe_load(SIDECAR.read_text(encoding="utf-8"))
    agenda = json.loads(AGENDA.read_text(encoding="utf-8"))
    upgrades = yaml.safe_load(UPGRADES.read_text(encoding="utf-8"))
    current = yaml.safe_load(CURRENT.read_text(encoding="utf-8"))
    evidence = EVIDENCE.read_text(encoding="utf-8")
    return {
        "registry": registry,
        "sidecar": sidecar,
        "agenda": agenda,
        "upgrades": upgrades,
        "current": current,
        "evidence": evidence,
    }


def validate_static(state: dict) -> list[str]:
    failures: list[str] = []
    entries = {e.get("id"): e for e in state["registry"].get("canonical_source_corrections", [])}
    for cid in IDS:
        entry = entries.get(cid)
        if entry is None:
            failures.append(f"registry missing {cid}")
            continue
        if str(entry.get("canonical_since")) != "2026-08-24":
            failures.append(f"{cid} canonical_since moved")
        signature = entry.get("signature") or {}
        if signature.get("match") != "all_families" or len(signature.get("token_families") or []) < 2:
            failures.append(f"{cid} signature contract weakened")

    stewardship = [c for c in state["sidecar"].get("checks", []) if c.get("by") == WORK_ITEM]
    pairs = {(str(c.get("file")), str(c.get("correction_id"))) for c in stewardship}
    if len(stewardship) != 52 or len(pairs) != 52:
        failures.append(f"stewardship sidecar is not 52 unique pairs ({len(stewardship)}/{len(pairs)})")
    for cid in IDS:
        selected = [c for c in stewardship if c.get("correction_id") == cid]
        if len(selected) != EXPECTED_COUNTS[cid]:
            failures.append(f"{cid} sidecar count {len(selected)} != {EXPECTED_COUNTS[cid]}")
        stale = {str(c.get("file")) for c in selected if c.get("verdict") == "STALE-FOUND"}
        if stale != EXPECTED_HISTORICAL_STALE[cid]:
            failures.append(f"{cid} historical stale partition changed")
        for c in selected:
            if c.get("verdict") == "STALE-FOUND" and c.get("pointer") != EVIDENCE.relative_to(ROOT).as_posix():
                failures.append(f"{cid} stale pointer missing for {c.get('file')}")

    baseline = (state["sidecar"].get("ratchet") or {}).get("baseline") or {}
    for cid, expected in EXPECTED_BASELINES.items():
        if baseline.get(cid) != expected:
            failures.append(f"{cid} baseline {baseline.get(cid)!r} != {expected}")
    if (state["sidecar"].get("ratchet") or {}).get("extension_measured_on") != "2026-08-25":
        failures.append("ratchet extension date moved")

    agenda_items = [
        row
        for row in state["agenda"].get("work_items", [])
        if isinstance(row, dict)
        and row.get("id") == "CONDITIONAL-BUILD-REVERSE-SCAFFOLD"
    ]
    if len(agenda_items) != 1:
        failures.append("agenda lacks one durable reverse-scaffold authority item")
        authority = ""
    else:
        authority = str(agenda_items[0].get("current_authority", ""))
    agenda_terms = (
        "observed phenomena backward",
        "named B2/action-root candidate set is empty",
        "Scheduled Progress selects the largest honest compatible Big Wave",
        "CBRS-1AB and W154/W229 remain valid candidate-local boundaries",
        "do not authorize source-action-first selection, zero work, scale reduction or maintenance substitution",
    )
    if any(term not in authority for term in agenda_terms):
        failures.append("agenda durable authority does not express the reverse-scaffold/B2 contract")

    rows = {r.get("id"): r for r in state["upgrades"].get("items", []) if isinstance(r, dict)}
    rs = rows.get("RS-WAVE-SERIES") or {}
    if rs.get("status") != "ACTIVE" or str(rs.get("next_check")) != "2026-08-31":
        failures.append("RS-WAVE-SERIES status/next_check moved")
    activation = str(rs.get("activation", ""))
    if "candidate set empty" not in activation or "new activation decision" not in activation:
        failures.append("RS-WAVE-SERIES activation lost the empty-root/reopen contract")

    summary = str((state["current"].get("current_result") or {}).get("summary", ""))
    if "52 exact pre-correction signature hits" not in summary or "current stale baselines are 0/0/0/0/0" not in summary:
        failures.append("CURRENT-STATE lacks the reconciliation summary")
    evidence = state["evidence"]
    for term in ("**52**", "**45**", "**7**", "RS-WAVE-SERIES remains ACTIVE only as a current steering guard"):
        if term not in evidence:
            failures.append(f"evidence missing {term}")
    return failures


def validate_dynamic(state: dict) -> list[str]:
    failures: list[str] = []
    audit = _load_audit()
    cfg = audit.default_cfg()
    cfg["as_of"] = "2026-08-25"
    result = audit.compute(cfg)
    recorded = {
        (str(c.get("file")), str(c.get("correction_id")))
        for c in state["sidecar"].get("checks", [])
        if c.get("by") == WORK_ITEM
    }
    for cid in IDS:
        row = result["per"][cid]
        candidates = set(row["unchecked"] + row["known_stale"] + row["cleared"] + row["fenced"] + row["repaired"])
        if len(candidates) != EXPECTED_CURRENT_COUNTS[cid] or row["unchecked"]:
            failures.append(f"{cid} current candidate census/unadjudicated set changed")
        if set(row["known_stale"]) != EXPECTED_CURRENT_STALE[cid]:
            failures.append(f"{cid} current audit stale set changed")
        if row["baseline"] != EXPECTED_BASELINES[cid]:
            failures.append(f"{cid} computed baseline changed")
    # The original 52-pair sidecar remains historical custody. Repairs may
    # remove stale language from the signature's current hit set, so current
    # measured pairs are intentionally not required to equal that old census.

    run = subprocess.run([sys.executable, str(CT5)], cwd=ROOT, text=True, capture_output=True)
    reported = re.search(
        r"^CERTIFICATE:\s+(\d+)/(\d+) checks pass;",
        run.stdout,
        re.MULTILINE,
    )
    if (
        run.returncode != 0
        or reported is None
        or int(reported.group(1)) <= 0
        or reported.group(1) != reported.group(2)
    ):
        failures.append("subordinate CT-5 certificate did not self-report all checks passing")
    return failures


def _single(items, predicate, label: str):
    matches = [item for item in items if predicate(item)]
    if not matches or matches[1:]:
        raise AssertionError(f"selftest fixture is not unique: {label}")
    return matches[0]


def selftest(baseline: dict) -> list[str]:
    mutations = []

    def drop_registry(s):
        s["registry"]["canonical_source_corrections"] = [e for e in s["registry"]["canonical_source_corrections"] if e.get("id") != IDS[0]]
    mutations.append(("registry-entry", drop_registry))

    def flip_stale(s):
        target = _single(s["sidecar"]["checks"], lambda c: c.get("by") == WORK_ITEM and c.get("file") == "explorations/twentyfive-lens-what-is-a-generation-2026-08-09.md", "stale verdict")
        target["verdict"] = "CLEARED-CONSISTENT"
    mutations.append(("stale-verdict", flip_stale))

    mutations.append(("ratchet-baseline", lambda s: s["sidecar"]["ratchet"]["baseline"].__setitem__(IDS[1], 4)))
    def erase_agenda_authority(s):
        target = _single(
            s["agenda"].get("work_items", []),
            lambda row: row.get("id") == "CONDITIONAL-BUILD-REVERSE-SCAFFOLD",
            "reverse-scaffold authority",
        )
        target["current_authority"] = "historical priority remains"
    mutations.append(("agenda-authority", erase_agenda_authority))

    def close_guard(s):
        target = _single(s["upgrades"].get("items", []), lambda r: isinstance(r, dict) and r.get("id") == "RS-WAVE-SERIES", "RS-WAVE-SERIES")
        target["status"] = "DONE"
    mutations.append(("upgrade-status", close_guard))

    mutations.append(("current-state", lambda s: s["current"]["current_result"].__setitem__("summary", "stale")))
    mutations.append(("evidence-count", lambda s: s.__setitem__("evidence", s["evidence"].replace("**52**", "**51**"))))

    def remove_pair(s):
        checks = s["sidecar"]["checks"]
        target = _single(checks, lambda c: c.get("by") == WORK_ITEM and c.get("file") == "explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md", "sidecar pair")
        checks.remove(target)
    mutations.append(("sidecar-pair", remove_pair))

    failures: list[str] = []
    for name, mutate in mutations:
        trial = copy.deepcopy(baseline)
        mutate(trial)
        if not validate_static(trial):
            failures.append(f"mutation escaped: {name}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    state = load_state()
    failures = validate_static(state) + validate_dynamic(state)
    if failures:
        for failure in failures:
            print(f"[FAIL] {failure}")
        return 1
    print("[PASS] canonical-currency census 52/52; historical 45/7 partition preserved")
    print("[PASS] durable reverse-scaffold/B2 authority and current 0/0/0/0/0 stale baselines reconciled")
    print("[PASS] subordinate CT-5 certificate self-reports all checks passing")
    if args.selftest:
        escaped = selftest(state)
        if escaped:
            for failure in escaped:
                print(f"[FAIL] {failure}")
            return 1
        print("[PASS] selftest 8/8 hostile coupled-surface mutations detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
