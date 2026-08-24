#!/usr/bin/env python3
"""Composite certificate for the 2026-08-24 SG4/source/parity integrity wave."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import os
from pathlib import Path
import subprocess
import sys

import yaml


ROOT = Path(__file__).resolve().parents[2]
MUT = os.environ.get("SG4_SOURCE_PARITY_MUTATE", "")
MUTATIONS = (
    "missing_fork",
    "unpin_fork",
    "review_bypass",
    "source_grade",
    "source_polarity",
    "source_adherence",
    "parity_evidence",
    "parity_receipt",
    "upgrade_status",
    "input_digest",
)
CHECKS: list[tuple[str, bool, object]] = []

FORK_REGISTRY = ROOT / "lab/process/layer0-fork-registry.yaml"
FORK_GATE = ROOT / "process_gates/fork_depth_audit.py"
SOURCE_REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
PATH_YAML = ROOT / "lab/process/path-dependencies.yaml"
PATH_MD = ROOT / "lab/process/path-dependencies.md"
PATH_GATE = ROOT / "process_gates/path_dependency_audit.py"
UPGRADES = ROOT / "lab/process/upgrade-program-register.yaml"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
DISPOSITIONS = ROOT / "lab/process/phenomenology-disposition-register-v0.1.json"

FROZEN_INPUTS = {
    ROOT / "lab/active-research/joe-directed/lens-digs/ldd-sg4-bit2-selector-governance-2026-08-17.md":
        "f9af4b664b7bf97cef9a1857e17ba9c273364e546a4326ed8bebac3da147d6b4",
    ROOT / "lab/active-research/joe-directed/source-chain/sca-right-chain-2026-08-15.md":
        "c6fabae2ce4ba664a88642d8b589a94327dac5d217336e4851ec5096a16f1629",
    ROOT / "lab/active-research/joe-directed/parity-crosscheck/pcx1-signature-parity-clause-does-not-fire-2026-08-17.md":
        "69ec4f71e087bcb515929c7d54e4dfb12edaf37faf35f8a21e354ed615e054b2",
}


def check(name: str, ok: bool, detail: object = None) -> None:
    CHECKS.append((name, bool(ok), detail))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_inputs() -> None:
    for path, expected in FROZEN_INPUTS.items():
        actual = sha256(path)
        if MUT == "input_digest" and "source-chain" in path.as_posix():
            actual = "0" * 64
        check(f"frozen input: {path.name}", actual == expected, actual)


def verify_fork_packet() -> None:
    data = yaml.safe_load(FORK_REGISTRY.read_text(encoding="utf-8"))
    rows = [row for row in data["forks"] if row.get("id") == "SG4-BIT-2-PHASE"]
    if MUT == "missing_fork":
        rows = []
    check("SG4 fork appears exactly once", len(rows) == 1, len(rows))
    if not rows:
        return
    row = copy.deepcopy(rows[0])
    if MUT == "review_bypass":
        row["independent_review_required"] = False
    check("SG4 fork remains open", row.get("status") == "open", row.get("status"))
    check("SG4 fork has two typed phase horns", len(row.get("horns", [])) == 2, row.get("horns"))
    check("SG4 settlement requires independent review", row.get("independent_review_required") is True)
    check("SG4 review covers result and wording", row.get("independent_review_scope") == "result_and_wording")

    gate = load_module("fork_depth_for_wave", FORK_GATE)
    pinned = "SG4-BIT-2-PHASE" in gate.REQUIRED_FORK_IDS
    if MUT == "unpin_fork":
        pinned = False
    check("SG4 fork is pinned against deletion", pinned)
    check("open SG4 row is schema-valid", gate.entry_errors(row) == [], gate.entry_errors(row))

    settled = {
        **row,
        "status": "settled",
        "settled_side": row["horns"][0],
        "settled_how": "a future action-owned construction selected the phase exactly",
        "settled_at": __import__("datetime").date(2026, 8, 24),
        "settled_by": ["lab/active-research/joe-directed/source-chain/sca-right-chain-2026-08-15.md"],
    }
    missing_review = gate.entry_errors(settled)
    check("settlement without IV receipt fails", any("independent_reviewed_by" in e for e in missing_review), missing_review)
    same = {**settled, "independent_reviewed_by": list(settled["settled_by"])}
    same_errors = gate.entry_errors(same)
    check("self-review path fails independence", any("distinct" in e for e in same_errors), same_errors)
    distinct = {
        **settled,
        "independent_reviewed_by": ["lab/active-research/joe-directed/parity-crosscheck/pcx1-signature-parity-clause-does-not-fire-2026-08-17.md"],
    }
    check("distinct result-and-wording IV receipt passes", gate.entry_errors(distinct) == [], gate.entry_errors(distinct))


def verify_source_packet() -> None:
    data = yaml.safe_load(SOURCE_REGISTER.read_text(encoding="utf-8"))
    rows = [row for row in data["claims"] if row.get("id") == "SC-GRP-50"]
    check("SC-GRP-50 appears exactly once", len(rows) == 1, len(rows))
    if not rows:
        return
    row = copy.deepcopy(rows[0])
    if MUT == "source_grade":
        row["grade"] = "transcript-verified"
    if MUT == "source_polarity":
        row["polarity"] = "UNCERTAIN"
    if MUT == "source_adherence":
        row["adherence"]["adherence"] = "ADHERED"
    check("SC-GRP-50 preserves ASSERTS polarity", row.get("polarity") == "ASSERTS", row.get("polarity"))
    check("SC-GRP-50 remains transcript-uncertain", row.get("grade") == "transcript-uncertain", row.get("grade"))
    check("SC-GRP-50 remains PARTIAL", row["adherence"].get("adherence") == "PARTIAL", row["adherence"])
    check("permanent no-audio posture is explicit", "will not be checked" in row.get("provenance_caveat", ""))
    check("both disputed-token outcomes are preserved", "Either outcome" in row.get("provenance_caveat", ""))
    check("SC-A certificate is the pinned owner evidence", row["adherence"].get("pinned_at") == "c0634255460f6db2182c29c8e6b861a0eec21bd6")

    claims = data["claims"]
    adherence = {key: sum(c["adherence"]["adherence"] == key for c in claims) for key in ("ADHERED", "PARTIAL", "UNTYPED")}
    cores = {key: sum(c["core"] == key for c in claims) for key in ("hard-core", "auxiliary", "disavowed-by-source")}
    headline = data["register"]["adjudication_headline"]
    check("source-register population is unique 111", len(claims) == len({c["id"] for c in claims}) == 111, len(claims))
    check("source-register adherence counts are current", adherence == {"ADHERED": 82, "PARTIAL": 20, "UNTYPED": 9}, adherence)
    check("source-register core counts are current", cores == {"hard-core": 49, "auxiliary": 51, "disavowed-by-source": 11}, cores)
    check("headline prints new PARTIAL and hard-core counts", "PARTIAL 20" in headline and "hard-core 49" in headline)


def verify_parity_packet() -> None:
    data = yaml.safe_load(PATH_YAML.read_text(encoding="utf-8"))
    chain = next(row for row in data["chains"] if row["id"] == "PD-SIGNATURE-PARITY")
    steps = copy.deepcopy(chain["chain"])
    if MUT == "parity_evidence":
        steps[-1]["evidence"] = "CONDITIONAL"
    if MUT == "parity_receipt":
        steps[-1]["receipt"] = "tests/no-such-probe.py"
    check("parity chain has eight ordered steps", len(steps) == 8, len(steps))
    check("original row remains the single CONDITIONAL step", sum(s["evidence"] == "CONDITIONAL" for s in steps) == 1)
    check("new parity cross-check is additive EXACT", steps[-1]["evidence"] == "EXACT", steps[-1])
    check("new parity receipt is PCX-1", steps[-1]["receipt"] == "tests/channel-swings/joe_directed_pcx1_signature_parity_clause_does_not_fire.py", steps[-1]["receipt"])
    check("armed firing condition names SG4 bit 2", "SG4-bit-2 effective half" in steps[-1]["fact"])
    path_gate = load_module("path_dependency_for_wave", PATH_GATE)
    check("generated dependency view is current", PATH_MD.read_text(encoding="utf-8") == path_gate.render(data))


def verify_integration_and_floors() -> None:
    data = yaml.safe_load(UPGRADES.read_text(encoding="utf-8"))
    rows = {row["id"]: row for row in data["items"]}
    ids = ("SG4-BIT2-FORK-ENTRY", "SC-GRP-50-REGISTRATION", "PD-CHAIN-STEP-ADDITION")
    if MUT == "upgrade_status":
        rows[ids[0]] = {**rows[ids[0]], "status": "QUEUED"}
    for identifier in ids:
        check(f"upgrade closed: {identifier}", rows[identifier]["status"] == "DONE", rows[identifier]["status"])
        check(f"upgrade has integrity-wave receipt: {identifier}", "sg4-source-parity-integrity-wave-2026-08-24.md" in str(rows[identifier]["activation"]))
    check("ledger v0.263 remains byte-identical", sha256(LEDGER) == "7c75c179c3af512084e50af19043a5d320b38e8c1e53325ee5ec2f97ad9c257b")
    check("91-row disposition register remains byte-identical", sha256(DISPOSITIONS) == "759eb1dcad644a7ed28d7b56d1fbbf43e1d2065af7352105cb02ccde0bf2d728")


def selftest() -> int:
    print("SELFTEST: verifying clean baseline before mutations")
    clean = dict(os.environ)
    clean.pop("SG4_SOURCE_PARITY_MUTATE", None)
    baseline = subprocess.run([sys.executable, str(Path(__file__).resolve())], env=clean, capture_output=True, text=True)
    if baseline.returncode != 0:
        print("FAIL baseline")
        print(baseline.stdout)
        return 1
    caught = 0
    for mutation in MUTATIONS:
        env = dict(os.environ, SG4_SOURCE_PARITY_MUTATE=mutation)
        result = subprocess.run([sys.executable, str(Path(__file__).resolve())], env=env, capture_output=True, text=True)
        genuine = result.returncode == 1 and "[FAIL]" in result.stdout
        print(f"mutation {mutation:18s}: {'CAUGHT' if genuine else 'MISSED'}")
        caught += int(genuine)
    print(f"SELFTEST: {caught}/{len(MUTATIONS)} mutations caught")
    return 0 if caught == len(MUTATIONS) else 1


def main() -> int:
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        return selftest()
    verify_inputs()
    verify_fork_packet()
    verify_source_packet()
    verify_parity_packet()
    verify_integration_and_floors()
    passed = sum(ok for _, ok, _ in CHECKS)
    for name, ok, detail in CHECKS:
        print(f"[{'ok' if ok else 'FAIL'}] {name}" + ("" if ok else f": {detail}"))
    print(f"SG4-SOURCE-PARITY-INTEGRITY: {passed}/{len(CHECKS)} checks pass")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
