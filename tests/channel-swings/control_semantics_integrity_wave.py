#!/usr/bin/env python3
"""Exact composite certificate for the 2026-08-24 control-semantics wave."""

from __future__ import annotations

import copy
import hashlib
import json
import pathlib
import subprocess
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
PATHS = {
    "ct": ROOT / "lab/methods/gu-base-categories.md",
    "ct_probe": ROOT / "tests/channel-swings/joe_directed_ct1_base_categories.py",
    "kill": ROOT / "process_gates/kill_target_claim_audit.py",
    "hom": ROOT / "lab/process/homonym-register.yaml",
    "fx3": ROOT / "tests/channel-swings/joe_directed_fx3_homonym_register.py",
    "up": ROOT / "lab/process/upgrade-program-register.yaml",
    "result": ROOT / "explorations/control-semantics-integrity-wave-2026-08-24.md",
    "ledger": ROOT / "lab/process/conditional-physics-ledger-v0.263.json",
    "disp": ROOT / "lab/process/phenomenology-disposition-register-v0.1.json",
}

LEDGER_SHA = "7c75c179c3af512084e50af19043a5d320b38e8c1e53325ee5ec2f97ad9c257b"
DISP_SHA = "759eb1dcad644a7ed28d7b56d1fbbf43e1d2065af7352105cb02ccde0bf2d728"


def load() -> dict[str, str]:
    return {key: path.read_text(encoding="utf-8") for key, path in PATHS.items()}


def checks(blobs: dict[str, str]) -> list[tuple[str, bool]]:
    hom = yaml.safe_load(blobs["hom"])
    upgrades = yaml.safe_load(blobs["up"])
    vpsb = next((e for e in hom["entries"] if e.get("token") == "v_PSB"), {})
    statuses = {row["id"]: row for row in upgrades["items"]}
    ledger_sha = hashlib.sha256(blobs["ledger"].encode()).hexdigest()
    disp_sha = hashlib.sha256(blobs["disp"].encode()).hexdigest()
    affinity_pos = blobs["kill"].find('bears_on = fm.get("bears_on", "")')
    trigger_pos = blobs["kill"].find('head = " ".join')
    result_frontmatter = blobs["result"].split("---", 2)[1]
    return [
        ("CT-1 carries the dated ORDER-SENSITIVE marker",
         "**ORDER-SENSITIVE (typed 2026-08-24).**" in blobs["ct"]),
        ("CT-1 carries the exact AC-A1/AC-F3 witness",
         "discharging `AC-A1` is what kills\n`AC-F3`" in blobs["ct"]),
        ("CT-1 preserves the no-G3/G6-identification ceiling",
         "does not identify G3 with G6" in blobs["ct"]),
        ("CT-1 preserves the no-functor ceiling",
         "construct a functor `L -> G`" in blobs["ct"]),
        ("CT-1 probe pins order sensitivity",
         "P12a Grant discharge is explicitly order-sensitive" in blobs["ct_probe"]),
        ("claim-affinity frontmatter key is implemented",
         'bears_on = fm.get("bears_on", "")' in blobs["kill"]),
        ("claim-affinity unknown IDs are WARN-only",
         'print(f"WARN {f}: {why}")' in blobs["kill"]
         and "warn-only defects" in blobs["kill"]),
        ("claim-affinity runs before kill-language filtering",
         0 <= affinity_pos < trigger_pos),
        ("kill exit status remains driven only by red count",
         "return (1 if len(red) > baseline else 0), hatch_uses" in blobs["kill"]),
        ("affinity selftest includes known claim",
         '"bears_on: SC-TEST-01' in blobs["kill"]),
        ("affinity selftest includes unknown claim",
         '"bears_on: SC-FAKE-99' in blobs["kill"]),
        ("affinity selftest includes untyped affinity",
         '"bears_on: source mechanism' in blobs["kill"]),
        ("affinity selftest requires exactly two WARNs",
         'affinity_text.count("WARN ") == 2' in blobs["kill"]),
        ("v_PSB remains homonym", vpsb.get("kind") == "homonym"),
        ("v_PSB receipt types one-token/two-referent rule",
         "one token with two unrelated referents" in
         vpsb.get("receipt", {}).get("incident", "")),
        ("v_PSB receipt reserves near_collision for two spellings",
         "two spellings one token apart" in
         vpsb.get("receipt", {}).get("incident", "")),
        ("FX-3 pins v_PSB kind", "v_PSB stays homonym" in blobs["fx3"]),
        ("DISCHARGE-ORDER-NONMONOTONE is DONE",
         statuses.get("DISCHARGE-ORDER-NONMONOTONE", {}).get("status") == "DONE"),
        ("SOURCE-MECHANISM convention is DONE",
         statuses.get("SOURCE-MECHANISM-TARGET-CLAIM-CONVENTION", {}).get("status") == "DONE"),
        ("VPSB-HOMONYM-KIND is DONE",
         statuses.get("VPSB-HOMONYM-KIND", {}).get("status") == "DONE"),
        ("result carries routing notice",
         "GU-COMPARATOR-ROUTING" in blobs["result"]),
        ("result declares INTERNAL_STRUCTURAL_ONLY",
         "Classification: `INTERNAL_STRUCTURAL_ONLY`" in blobs["result"]),
        ("result declares no source kill",
         "target_claim: NONE-NOT-A-KILL" in blobs["result"]),
        ("result registers SC-CHI-01 affinity",
         "bears_on: SC-CHI-01" in result_frontmatter),
        ("result carries typed-object declaration",
         "```gu-typed-objects" in blobs["result"]),
        ("ledger v0.263 remains byte-identical", ledger_sha == LEDGER_SHA),
        ("91-row disposition register remains byte-identical", disp_sha == DISP_SHA),
        ("ledger still contains 91 rows",
         len(json.loads(blobs["ledger"])["rows"]) == 91),
        ("result ceiling forbids science movement",
         "changes no scientific object" in " ".join(blobs["result"].split())),
    ]


def run(blobs: dict[str, str], emit: bool = True) -> int:
    rows = checks(blobs)
    failed = [name for name, ok in rows if not ok]
    if emit:
        for name, ok in rows:
            print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        print(f"CERTIFICATE: {len(rows) - len(failed)}/{len(rows)} checks pass")
    return 1 if failed else 0


MUTATIONS = (
    ("remove order marker", "ct", "**ORDER-SENSITIVE (typed 2026-08-24).**", "order note"),
    ("erase AC-F3 witness", "ct",
     "discharging `AC-A1` is what kills\n`AC-F3`",
     "discharging `AC-A1` is what kills\n`AC-FX`"),
    ("erase no-G3/G6 ceiling", "ct", "does not identify G3 with G6", "relates G3 and G6"),
    ("move affinity after trigger", "kill",
     'bears_on = fm.get("bears_on", "")', 'bears_on = fm.get("after_trigger", "")'),
    ("turn WARN into RED label", "kill", 'print(f"WARN {f}: {why}")', 'print(f"RED {f}: {why}")'),
    ("change v_PSB kind", "hom", "  - token: v_PSB\n    kind: homonym",
     "  - token: v_PSB\n    kind: near_collision"),
    ("erase v_PSB taxonomy receipt", "hom", "one token with two unrelated referents",
     "two adjacent spellings"),
    ("requeue discharge packet", "up", "  - id: DISCHARGE-ORDER-NONMONOTONE",
     "  - id: DISCHARGE-ORDER-NONMONOTONE-BROKEN"),
    ("corrupt protected ledger", "ledger", '"schema_version"', '"schema_broken"'),
    ("erase result affinity", "result", "bears_on: SC-CHI-01", "bears_on: UNKNOWN"),
)


def selftest() -> int:
    base = load()
    print("BASELINE — clean certificate before hostile mutations")
    if run(base) != 0:
        print("SELFTEST REFUSED: baseline is red")
        return 1
    caught = 0
    for name, key, old, new in MUTATIONS:
        mutant = copy.deepcopy(base)
        if old not in mutant[key]:
            print(f"[FAIL] mutation fixture missing: {name}")
            continue
        mutant[key] = mutant[key].replace(old, new, 1)
        if run(mutant, emit=False) != 0:
            caught += 1
            print(f"[PASS] caught hostile mutation: {name}")
        else:
            print(f"[FAIL] missed hostile mutation: {name}")
    print(f"SELFTEST: {caught}/{len(MUTATIONS)} hostile mutations caught")
    return 0 if caught == len(MUTATIONS) else 1


def native() -> int:
    commands = [
        [sys.executable, "tests/channel-swings/joe_directed_ct1_base_categories.py"],
        [sys.executable, "process_gates/kill_target_claim_audit.py", "--self-test"],
        [sys.executable, "tests/channel-swings/joe_directed_fx3_homonym_register.py"],
    ]
    for command in commands:
        proc = subprocess.run(command, cwd=ROOT)
        if proc.returncode:
            return proc.returncode
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        raise SystemExit(selftest())
    code = run(load())
    if "--native" in sys.argv and code == 0:
        code = native()
    raise SystemExit(code)
