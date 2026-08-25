#!/usr/bin/env python3
"""Fail-closed currency audit for the SC-GEN-53 prediction seed."""

from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import subprocess
import sys

import yaml


ROOT = Path(__file__).resolve().parents[2]
AGENDA = ROOT / "lab/process/RESEARCH-AGENDA.json"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
EVIDENCE = ROOT / "lab/methods/research-evidence-contract-v1.0.md"
HE1 = ROOT / "lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md"
RESULT = ROOT / "explorations/sc-gen53-prediction-seed-currency-reconciliation-2026-08-25.md"
MUTATE = os.environ.get("SCGEN53_CURRENCY_MUTATE", "")
MUTATIONS = (
    "repeat_task",
    "erase_he1",
    "rename_partner",
    "promote_packet",
    "drop_scale_gate",
    "drop_real_caveat",
    "promote_adherence",
    "drop_routing",
)


def load() -> dict:
    agenda = json.loads(AGENDA.read_text(encoding="utf-8"))
    work = {row["id"]: row for row in agenda["work_items"]}
    register = yaml.safe_load(REGISTER.read_text(encoding="utf-8"))
    claims = {row["id"]: row for row in register["claims"]}
    return {
        "agenda": agenda,
        "seed": work["PRED-CANDIDATE-PACKETS"],
        "claim": claims["SC-GEN-53"],
        "evidence": EVIDENCE.read_text(encoding="utf-8"),
        "he1": HE1.read_text(encoding="utf-8"),
        "result": RESULT.read_text(encoding="utf-8"),
    }


def evaluate(data: dict) -> list[tuple[str, bool]]:
    seed = data["seed"]
    claim = data["claim"]
    combined = "\n".join((seed["assessment_summary"], seed["next_swing"], data["evidence"], data["result"]))
    return [
        ("HE-1 remains the named completed owner", "he1-imposter-separation-invariant-2026-08-14.md" in seed["assessment_source"]),
        ("agenda retires the restriction rerun", "Do not rerun the completed `16`/`144` restriction" in seed["next_swing"]),
        ("agenda separates partner from imposter", "distinct WG-P03 `144` partner" in seed["assessment_summary"]),
        ("agenda preserves the exact invariant witnesses", "Dynkin index `2` versus `34`" in seed["assessment_summary"] and "mass-channel ladder `0 -> 2 -> 11`" in seed["assessment_summary"]),
        ("remaining numerical scale is explicit", "numerical energy scale" in combined),
        ("remaining physical observable map is explicit", "physical observable map" in combined),
        ("remaining predeclared threshold is explicit", "predeclared threshold" in combined),
        ("complex-to-real caveat remains explicit", "Spin(6,4)" in combined and "real-form" in combined),
        ("prediction packet remains blocked", seed["state"] == "BLOCKED_SOURCE_GAP" and "No prediction packet graduates" in data["result"]),
        ("source polarity remains ASSERTS", claim["polarity"] == "ASSERTS"),
        ("source adherence remains PARTIAL", claim["adherence"]["adherence"] == "PARTIAL"),
        ("source evidence includes HE-1", any("he1-imposter-separation-invariant-2026-08-14.md" in item for item in claim["adherence"]["evidence"])),
        ("source note no longer calls the invariant missing", "representation invariant is supplied" in claim["adherence"]["note"]),
        ("HE-1 original certificate shape remains", "62/62 checks" in data["he1"] and "FENCE 1" in data["he1"] and "FENCE 4" in data["he1"]),
        ("result carries exact routing classification", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in data["result"] and "GU-COMPARATOR-ROUTING" in data["result"]),
        ("result carries typed objects", "```gu-typed-objects" in data["result"] and "target: SC-GEN-53" in data["result"]),
    ]


def mutate(data: dict, name: str) -> None:
    if name == "repeat_task":
        data["seed"]["next_swing"] = "First restrict the true-family and imposter modules."
    elif name == "erase_he1":
        data["seed"]["assessment_source"] = data["seed"]["assessment_source"].replace("; lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md", "")
    elif name == "rename_partner":
        data["seed"]["assessment_summary"] = data["seed"]["assessment_summary"].replace("distinct WG-P03 `144` partner", "imposter `144`")
    elif name == "promote_packet":
        data["seed"]["state"] = "READY"
    elif name == "drop_scale_gate":
        for key in ("assessment_summary", "next_swing"):
            data["seed"][key] = data["seed"][key].replace("numerical energy scale", "energy input")
        data["evidence"] = data["evidence"].replace("numerical energy scale", "energy input")
        data["result"] = data["result"].replace("numerical energy scale", "energy input")
    elif name == "drop_real_caveat":
        data["seed"]["assessment_summary"] = data["seed"]["assessment_summary"].replace("Spin(6,4)", "physical")
        data["seed"]["next_swing"] = data["seed"]["next_swing"].replace("Spin(6,4)", "physical")
        data["evidence"] = data["evidence"].replace("Spin(6,4)", "physical")
        data["result"] = data["result"].replace("Spin(6,4)", "physical")
    elif name == "promote_adherence":
        data["claim"]["adherence"]["adherence"] = "ADHERED"
    elif name == "drop_routing":
        data["result"] = data["result"].replace("Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`", "Classification omitted")


def run() -> int:
    data = load()
    if MUTATE:
        data = copy.deepcopy(data)
        mutate(data, MUTATE)
    checks = evaluate(data)
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"SCGEN53-PREDICTION-SEED-CURRENCY: {sum(ok for _, ok in checks)}/{len(checks)} checks pass")
    return 0 if all(ok for _, ok in checks) else 1


def selftest() -> int:
    clean = dict(os.environ)
    clean.pop("SCGEN53_CURRENCY_MUTATE", None)
    baseline = subprocess.run([sys.executable, str(Path(__file__).resolve())], env=clean, capture_output=True, text=True)
    if baseline.returncode != 0:
        print("SELFTEST: baseline failed")
        print(baseline.stdout)
        return 1
    caught = 0
    for name in MUTATIONS:
        env = dict(clean, SCGEN53_CURRENCY_MUTATE=name)
        result = subprocess.run([sys.executable, str(Path(__file__).resolve())], env=env, capture_output=True, text=True)
        genuine = result.returncode == 1 and "[FAIL]" in result.stdout
        print(f"mutation {name:18s}: {'CAUGHT' if genuine else 'MISSED'}")
        caught += int(genuine)
    print(f"SELFTEST: {caught}/{len(MUTATIONS)} mutations caught")
    return 0 if caught == len(MUTATIONS) else 1


if __name__ == "__main__":
    raise SystemExit(selftest() if "--selftest" in sys.argv or "--self-test" in sys.argv else run())
