#!/usr/bin/env python3
"""Coupled certificate for the 2026-08-25 semantic-integrity custody wave."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "lab/process/semantic-integrity-typed-object-custody-wave.json"
TYPED = ROOT / "process_gates/typed_carrier_declaration_audit.py"
KILL = ROOT / "process_gates/kill_target_claim_audit.py"
FRONTIER = ROOT / "tests/channel-swings/current_frontier_semantic_currency_audit.py"

FAILURES: list[str] = []
CHECKS = 0


def check(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if condition:
        print(f"[PASS] {label}")
    else:
        FAILURES.append(label)
        print(f"[FAIL] {label}")


data = json.loads(CERT.read_text(encoding="utf-8"))
typed = runpy.run_path(str(TYPED))
kill = runpy.run_path(str(KILL))
frontier = runpy.run_path(str(FRONTIER))

previous_cwd = Path.cwd()
os.chdir(ROOT)
try:
    typed_code, typed_stats = typed["audit"]()
    kill_code, _ = kill["audit"]()
    ledger_code = kill["audit_ledger"]()
finally:
    os.chdir(previous_cwd)

frontier_data = frontier["load_inputs"]()
frontier_failures = frontier["audit"](frontier_data)

check(data["schema_version"] == "1.0" and data["status"] == "PASS",
      "certificate schema and status")
check(data["typed_object_custody"]["before_red"] == 46,
      "entering typed-object red count frozen")
check(typed_code == 0 and typed_stats["red"] == 0,
      "typed-object audit closes at zero reds")
check(typed_stats["blocks"] == data["typed_object_custody"]["after_blocks"] == 181,
      "typed-object block inventory closes")
check(len(data["typed_object_custody"]["paths"]) == 15,
      "fifteen typed-object paths recorded")
check(all((ROOT / path).is_file() for path in data["typed_object_custody"]["paths"]),
      "every typed-object path resolves")
check(data["typed_object_custody"]["repaired_existing_blocks"] == 12 and
      data["typed_object_custody"]["added_blocks"] == 3,
      "twelve repairs plus three declarations recorded")

check(data["kill_target_custody"]["before_red"] == 3,
      "entering kill-target red count frozen")
check(kill_code == 0 and ledger_code == 0 and kill["SCOPE_BASELINE"] == 0,
      "kill-target scope and ledger close at zero")
check(len(data["kill_target_custody"]["paths"]) == 3,
      "three kill-target paths recorded")
check(all("target_claim: NONE-NOT-A-KILL" in (ROOT / path).read_text(encoding="utf-8")
          for path in data["kill_target_custody"]["paths"]),
      "three negative-result targets are explicit")

agenda = ROOT / "lab/process/RESEARCH-AGENDA.json"
agenda_digest = hashlib.sha256(agenda.read_bytes()).hexdigest()
check(not frontier_failures, "current-frontier semantic currency passes")
check(agenda_digest == data["frontier_currency"]["agenda_sha256"],
      "agenda digest matches coupled certificate")
check(data["frontier_currency"]["probe_authorship_state"] == "107/983",
      "live authorship state is current")

valid_block = """result: fixture
carrier: object LAYER=toy CHIRALITY=N/A
pairing: form ON=object
real_structure: real
grading: degree zero
action_owner: repository-construction
target: object MAP-TYPE=evaluation
"""
mutations = {
    "bad-layer": valid_block.replace("LAYER=toy", "LAYER=process"),
    "bad-map": valid_block.replace("MAP-TYPE=evaluation", "MAP-TYPE=diagnosis"),
    "bad-owner": valid_block.replace("repository-construction", "none"),
    "missing-pairing-owner": valid_block.replace("form ON=object", "form"),
}
for name, block in mutations.items():
    defects, _, _ = typed["validate_block"](block)
    check(bool(defects), f"hostile typed-object mutation caught: {name}")

untyped_negative = {"title": "internal route killed", "created": "2026-08-25"}
check(bool(kill["TRIGGER"].search(untyped_negative["title"])) and
      not kill["CLAIM_ID"].search(json.dumps(untyped_negative)) and
      kill["HATCH"] not in json.dumps(untyped_negative),
      "hostile untyped negative target is detectable")

stale = copy.deepcopy(frontier_data)
stale["registry"]["basis"]["research_agenda"]["sha256"] = "0" * 64
check(any("research_agenda" in failure for failure in frontier["audit"](stale)),
      "hostile stale agenda digest is caught")
check(data["hostile_controls"]["caught"] == data["hostile_controls"]["count"] == 7,
      "seven hostile controls close")
check(all(value == "none" for value in data["effect"].values()),
      "protected scientific effects remain none")

if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{CHECKS}: {FAILURES}")
print(f"PASS {CHECKS}/{CHECKS}")
