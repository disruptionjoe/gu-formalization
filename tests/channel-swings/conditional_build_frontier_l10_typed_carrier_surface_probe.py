#!/usr/bin/env python3
"""Exact propagation probe for the post-LT-GR8 L10 typed-carrier repair."""

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
CAPACITYOS = ROOT.parents[2]
GATE_PATH = ROOT / "process_gates" / "typed_carrier_declaration_audit.py"
ARTIFACT = ROOT / "explorations" / "conditional-build" / "selected-k77-ltgr8-observed-boundary-carrier-typing-2026-08-22.md"
INDEX = ROOT / "lab" / "process" / "conditional-evidence-deltas" / "index.json"
DELTA = ROOT / "lab" / "process" / "conditional-evidence-deltas" / "gu-ltgr8-boundary-carrier-typing-2026-08-22.json"
REGISTRY = ROOT / "lab" / "process" / "conditional-build-frontier-and-l10-typed-carrier-surface.json"

spec = importlib.util.spec_from_file_location("typed_gate", GATE_PATH)
gate = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(gate)

checks = 0


def check(label, condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def run_gate(cwd):
    return subprocess.run(
        [sys.executable, str(GATE_PATH)], cwd=cwd, text=True,
        capture_output=True, check=False)


def main():
    text = ARTIFACT.read_text(encoding="utf-8")
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    delta = json.loads(DELTA.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))

    check("mixed layer names bridge", "LAYER=ambient+observed BRIDGE=section-restriction" in text)
    check("absent action owner uses token", "action_owner: N/A --" in text)
    check("composite target is honestly untyped", "MAP-TYPE=UNTYPED" in text)
    blocks = gate.FENCE_RE.findall(text)
    check("one declaration block", len(blocks) == 1)
    defects, untyped, _ = gate.validate_block(blocks[0])
    check("LT-GR8 declaration validates", defects == [])
    check("composite ambiguity visible", untyped >= 1)

    root_run = run_gate(ROOT)
    aggregate_run = run_gate(CAPACITYOS)
    check("repository invocation bounded red", root_run.returncode == 1)
    check("aggregate invocation bounded red", aggregate_run.returncode == 1)
    check("caller cwd cannot change report", root_run.stdout == aggregate_run.stdout)
    check("no crash in either invocation", not root_run.stderr and not aggregate_run.stderr)
    check("three inherited reds remain", "typed_carrier_declaration_audit: 3 red" in root_run.stdout)
    check("LT-GR8 path no longer red", str(ARTIFACT.relative_to(ROOT)) not in root_run.stdout)

    check("cursor advanced", index["integration_cursor"] == delta["delta_id"])
    check("index disposition deferred", index["deltas"][-1]["status"] == "deferred")
    check("delta disposition deferred", delta["integration"]["disposition"] == "deferred")
    check("priority unchanged", delta["integration"]["priority_effect"] == "none")
    check("verdict ceiling preserved", "NEEDS / MISSING_CONSTRUCTION" in delta["integration"]["reason"])
    check("frontier source delta unchanged", registry["source_to_proof_delta"]["movement"] == "unchanged")
    check("no scientific verdict movement", registry["effect"]["scientific_verdict_change"] == "none")

    print(f"conditional_build_frontier_l10_typed_carrier_surface_probe: {checks}/{checks} checks pass, exit 0")


def selftest():
    original_root = gate.ROOT
    original_cwd = os.getcwd()
    try:
        with tempfile.TemporaryDirectory() as inside, tempfile.TemporaryDirectory() as outside:
            Path(inside, "valid.md").write_text(
                "---\ncreated: 2026-09-01\ndoc_type: construction_result\n---\n"
                "```gu-typed-objects\n" + gate.VALID_BLOCK + "```\n",
                encoding="utf-8")
            Path(outside, "poison.md").write_bytes(b"---\ncreated: 2026-09-01\n\x97")
            gate.ROOT = inside
            os.chdir(outside)
            check("scan is rooted at target not caller", gate.scan_set() == ["valid.md"])
            code, stats = gate.audit()
            check("rooted fixture is green", code == 0 and stats["triggered"] == 1)
        bad = gate.VALID_BLOCK.replace("LAYER=ambient", "LAYER=typing")
        check("old layer token is caught", "CARRIER-BAD-LAYER:typing" in gate.validate_block(bad)[0])
        bad = gate.VALID_BLOCK.replace("action_owner: repository-construction", "action_owner: none")
        check("old owner token is caught", "OWNER-UNTOKENED" in gate.validate_block(bad)[0])
        bad = gate.VALID_BLOCK.replace("MAP-TYPE=restriction", "MAP-TYPE=typing")
        check("old map token is caught", "TARGET-BAD-MAPTYPE:typing" in gate.validate_block(bad)[0])
    finally:
        gate.ROOT = original_root
        os.chdir(original_cwd)
    print(f"SELF-TEST GREEN: {checks}/{checks} controls")


if __name__ == "__main__":
    selftest() if "--selftest" in sys.argv else main()
