#!/usr/bin/env python3
"""Fail closed if the 2026-11-09 program_focus steering decays.

Checks that research priority stays where agents read it first, that the
constraint matrix, action class and discovery bets stay well formed, that the
retired follow-through chain does not grow back in NEXT-STEPS, and that new
conditional-build results name the matrix cell, intersection or bet they
target.  This is a process gate; it evaluates no scientific claim.
``--selftest`` requires a green baseline, then plants regressions and requires
every one to be caught.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import tempfile
from pathlib import Path
from typing import Callable

import yaml

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "current": Path("CURRENT-STATE.yaml"),
    "agents": Path("AGENTS.md"),
    "verification": Path("VERIFICATION.md"),
    "next": Path("NEXT-STEPS.md"),
    "status": Path("RESEARCH-STATUS.md"),
    "matrix": Path("lab/process/action-constraint-matrix.json"),
    "action_class": Path("lab/process/action-class.json"),
    "bets": Path("lab/process/discovery-bets.json"),
    "metrics": Path("lab/process/weekly-metrics.json"),
    "reader": Path("scripts/research_context.py"),
}
REVERSE = [
    "empirical_benchmark_descent",
    "operational_constraint_extraction",
    "state_observable_interface",
    "causal_dynamical_demand",
    "candidate_action_requirements",
]
SM_ANCHORS = {"EXT-SM-WEAK-CHIRALITY", "EXT-SM-THREE-CHIRAL-GENERATIONS"}
CELL_STATUS = {"open", "constrained", "decided_for_C", "gated", "empty"}
LANES = {"LB-MATRIX", "LB-CLASS", "LB-LADDER"}
FOCUS_KEYS = {
    "version", "authority", "read_first", "goal", "files", "split", "run_selection",
    "preflight_required", "postflight_required", "zero_delta_reroute", "review_tiers", "forbidden",
    "structure_not_specifics",
}
RESET_DATE = "2026-11-09"
KITEM_DIR = Path("explorations/conditional-build")
KITEM_FIELDS = ("program_target:", "tier:", "expected_delta:", "actual_delta:")


def text(root: Path, key: str) -> str:
    return (root / FILES[key]).read_text(encoding="utf-8")


def load_json(root: Path, key: str) -> dict:
    return json.loads(text(root, key))


def audit(root: Path) -> list[str]:
    errors: list[str] = []

    raw = text(root, "current")
    state = yaml.safe_load(raw)
    keys = list(state) if isinstance(state, dict) else []
    focus = state.get("program_focus") if isinstance(state, dict) else None
    if not isinstance(focus, dict):
        errors.append("CURRENT-STATE.yaml lacks a program_focus mapping")
        focus = {}
    elif "program_focus" not in keys[:6]:
        errors.append("program_focus is not among the first keys of CURRENT-STATE.yaml")
    missing = FOCUS_KEYS - set(focus)
    if missing:
        errors.append(f"program_focus lacks {sorted(missing)}")
    if raw.find("program_focus:") > 200 * 80:
        errors.append("program_focus starts too deep in CURRENT-STATE.yaml for a top-down reader")
    forbidden = " ".join(str(item) for item in focus.get("forbidden", []))
    if "external review" not in forbidden:
        errors.append("program_focus.forbidden no longer excludes external review")
    if "specific action" not in forbidden or "gated cell" not in forbidden or "guessed action variants" not in forbidden:
        errors.append("program_focus.forbidden no longer blocks specific-action search, gate-object building, or unbounded lane-C guessing")
    if "every action in class C" not in str(focus.get("structure_not_specifics", "")):
        errors.append("program_focus lost the structure-not-specifics rule")
    if "never zero work" not in str(focus.get("zero_delta_reroute", "")):
        errors.append("program_focus reroute rule no longer excludes zero work")
    for field, needle in (("current_question", "class C"), ("next_condition", "program_focus")):
        lead = str(state.get(field, "")).strip().splitlines()[:1]
        if not lead or needle not in lead[0]:
            errors.append(f"{field} lead line no longer points at program_focus ({needle!r})")

    reader = text(root, "reader")
    if '"program_focus": state.get("program_focus")' not in reader:
        errors.append("entry view (scripts/research_context.py) no longer prints program_focus")

    agents = text(root, "agents")
    step0 = agents.split("1. Read", 1)[0]
    if "program_focus" not in step0 or "External" not in step0 or "not a pathway" not in step0:
        errors.append("AGENTS.md step 0 no longer routes to program_focus and excludes external review")

    verification = text(root, "verification")
    first = re.search(r"(?m)^## (.+)$", verification)
    if not first or "program_focus" not in first.group(1):
        errors.append("VERIFICATION.md first section is no longer the program_focus standard")

    next_steps = text(root, "next")
    live = next_steps.split("## Archived steering history", 1)[0]
    if re.search(r"(?m)^## Current follow-through|^> \*\*Historical predecessor", live):
        errors.append("NEXT-STEPS.md regrew a 'Current follow-through' section")
    head = next_steps.split("# Next Steps For Contributors", 1)[0]
    if "program_focus" not in head:
        errors.append("NEXT-STEPS.md lost its pinned program_focus section")
    status_head = text(root, "status")[:4000]
    if "program_focus" not in status_head:
        errors.append("RESEARCH-STATUS.md lost its pinned program_focus section")

    action_class = load_json(root, "action_class")
    wording = action_class.get("verdict_wording", {})
    if "not a global GU verdict" not in wording.get("empty_intersection", ""):
        errors.append("action class empty-intersection wording lost its scope")
    if wording.get("forbidden_for_matrix_kills") != "a narrower route failed":
        errors.append("action class no longer forbids 'a narrower route failed'")
    if not isinstance(action_class.get("degeneration_log"), list) or "widening_policy" not in action_class:
        errors.append("action class lost its widening policy or degeneration log")
    if {"inclusion_witness", "exclusion_witness"} - set(action_class.get("width_test", {})):
        errors.append("action class lost a width-test witness")

    matrix = load_json(root, "matrix")
    rows = {row.get("id"): row for row in matrix.get("rows", [])}
    columns = {col.get("id") for col in matrix.get("columns", [])}
    if not {"P1", "P2", "P3"} <= set(rows):
        errors.append("constraint matrix lost a P-row")
    for rid, row in rows.items():
        if row.get("anchor") not in SM_ANCHORS:
            errors.append(f"matrix row {rid} has no SM anchor")
        lineage = row.get("lineage", [])
        if [str(step).split(":", 1)[0] for step in lineage] != REVERSE:
            errors.append(f"matrix row {rid} lineage does not descend all five reverse stages")
    for cell in matrix.get("cells", []):
        where = f"{cell.get('row')}x{cell.get('column')}"
        if cell.get("row") not in rows or cell.get("column") not in columns:
            errors.append(f"matrix cell {where} names an unknown row or column")
        if cell.get("status") not in CELL_STATUS:
            errors.append(f"matrix cell {where} has unknown status {cell.get('status')!r}")
        if cell.get("status") in {"constrained", "decided_for_C", "empty", "gated"} and not cell.get("evidence"):
            errors.append(f"matrix cell {where} moved without evidence")
        for ref in cell.get("evidence", []):
            path = str(ref).split(" ", 1)[0]
            if "/" in path and not (root / path).exists():
                errors.append(f"matrix cell {where} cites missing evidence {path}")
    for cell in matrix.get("cells", []):
        if cell.get("status") == "gated" and not cell.get("structural_route"):
            errors.append(f"gated matrix cell {cell.get('row')}x{cell.get('column')} has no structural_route")
    if "structure level" not in matrix.get("working_rule", ""):
        errors.append("constraint matrix lost its structure-level working rule")
    for item in matrix.get("cells", []) + matrix.get("intersections", []):
        packet = item.get("packet")
        if packet and not (root / packet).is_file():
            errors.append(f"matrix item {item.get('id') or item.get('row')} names a missing packet {packet}")
    if set(matrix.get("lane_state", {})) != LANES:
        errors.append("constraint matrix lane_state lost a lane-B sub-lane counter")
    counter = matrix.get("program_run_counter", {})
    if not isinstance(counter.get("count"), int) or counter.get("since") != RESET_DATE:
        errors.append("constraint matrix program_run_counter is missing or malformed")
    if "narrower route failed" in json.dumps(matrix.get("shrinkage_log", [])):
        errors.append("matrix shrinkage log uses forbidden kill wording")

    bets = load_json(root, "bets")
    rules = bets.get("lane_rules", {})
    if "At most 3" not in rules.get("guess_budget", ""):
        errors.append("discovery-bets lost the per-run guess budget")
    if rules.get("time_box_runs") != 24 or "re-derivation" not in rules.get("speculative_actions", ""):
        errors.append("discovery-bets lane rules lost the 24-run box or the re-derivation rule")
    for bet in bets.get("bets", []):
        for field in ("id", "question", "target_row", "kill_criterion", "status", "runs_used", "zero_delta_streak"):
            if field not in bet:
                errors.append(f"bet {bet.get('id')} lacks {field}")
        if isinstance(bet.get("runs_used"), int) and bet["runs_used"] > rules.get("time_box_runs", 24) and bet.get("status") == "active":
            errors.append(f"bet {bet.get('id')} is still active past its time box")

    metrics = load_json(root, "metrics")
    if "entry_schema" not in metrics or not isinstance(metrics.get("entries"), list):
        errors.append("weekly metrics file lost its schema or entries list")

    kdir = root / KITEM_DIR
    if kdir.is_dir():
        for path in sorted(kdir.glob("*.md")):
            match = re.search(r"(\d{4}-\d{2}-\d{2})\.md$", path.name)
            if not match or match.group(1) < RESET_DATE:
                continue
            body = path.read_text(encoding="utf-8")
            front = body.split("\n---", 2)[1] if body.startswith("---") else ""
            absent = [field for field in KITEM_FIELDS if field not in front]
            if absent:
                errors.append(f"{KITEM_DIR / path.name} lacks program_focus frontmatter {absent}")

    return errors


def set_json(root: Path, key: str, mutation: Callable[[dict], None]) -> None:
    path = root / FILES[key]
    data = json.loads(path.read_text(encoding="utf-8"))
    mutation(data)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def replace_text(root: Path, key: str, old: str, new: str) -> None:
    path = root / FILES[key]
    body = path.read_text(encoding="utf-8")
    if old not in body:
        raise RuntimeError(f"selftest plant source missing: {old}")
    path.write_text(body.replace(old, new, 1), encoding="utf-8")


def copy_fixture(fixture: Path) -> None:
    for rel in FILES.values():
        (fixture / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / rel, fixture / rel)
    matrix = json.loads((ROOT / FILES["matrix"]).read_text(encoding="utf-8"))
    for item in matrix.get("cells", []) + matrix.get("intersections", []):
        packet = item.get("packet")
        if packet and (ROOT / packet).exists():
            (fixture / packet).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / packet, fixture / packet)
    for cell in matrix.get("cells", []) + matrix.get("intersections", []):
        for ref in cell.get("evidence", []):
            path = str(ref).split(" ", 1)[0]
            if "/" in path and (ROOT / path).exists():
                (fixture / path).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / path, fixture / path)


def plant_kitem(root: Path) -> None:
    path = root / KITEM_DIR / "k9999-untargeted-2026-11-10.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\ntitle: untargeted\n---\n\nBody.\n", encoding="utf-8")


def selftest() -> int:
    baseline = audit(ROOT)
    if baseline:
        print("[FAIL] clean baseline is not green")
        for error in baseline:
            print(f"  - {error}")
        return 1
    with tempfile.TemporaryDirectory(prefix="gu_program_focus_") as temp:
        fixture = Path(temp)
        copy_fixture(fixture)
        clean = audit(fixture)
        if clean:
            print("[FAIL] unmutated fixture is not green; selftest would be vacuous")
            for error in clean:
                print(f"  - {error}")
            return 1

    plants: list[tuple[str, Callable[[Path], None]]] = [
        ("program_focus renamed", lambda r: replace_text(r, "current", "program_focus:\n", "retired_focus:\n")),
        ("external-review ban removed", lambda r: replace_text(r, "current", "proposing, planning for, or waiting on external review", "skipping review")),
        ("entry view stops printing program_focus", lambda r: replace_text(r, "reader", '"program_focus": state.get("program_focus"),', "")),
        ("NEXT-STEPS regrows follow-through chain", lambda r: replace_text(r, "next", "# Next Steps For Contributors", "## Current follow-through — 2026-11-10\n\nReuse K9999.\n\n# Next Steps For Contributors")),
        ("matrix cell moves without evidence", lambda r: set_json(r, "matrix", lambda d: d["cells"][0].__setitem__("evidence", []))),
        ("matrix row loses SM anchor", lambda r: set_json(r, "matrix", lambda d: d["rows"][0].__setitem__("anchor", "EXT-QM-SPACELIKE-BELL-NOSIGNAL"))),
        ("kill wording loses scope", lambda r: set_json(r, "action_class", lambda d: d["verdict_wording"].__setitem__("empty_intersection", "GU is falsified."))),
        ("structure-not-specifics rule removed", lambda r: replace_text(r, "current", "every action in class C, or for a subfamily", "some action, or for a subfamily")),
        ("gated cell loses its structural route", lambda r: set_json(r, "matrix", lambda d: [c.pop("structural_route", None) for c in d["cells"] if c.get("status") == "gated"])),
        ("lane-C guess budget removed", lambda r: set_json(r, "bets", lambda d: d["lane_rules"].pop("guess_budget"))),
        ("matrix points at a missing packet", lambda r: set_json(r, "matrix", lambda d: d["intersections"][0].__setitem__("packet", "lab/process/work-packets/missing.md"))),
        ("bet runs past its time box", lambda r: set_json(r, "bets", lambda d: d["bets"][0].__setitem__("runs_used", 30))),
        ("new K-item without a target", plant_kitem),
        ("VERIFICATION first section reverts to a K-item", lambda r: replace_text(r, "verification", "## Verification standard under program_focus (pinned 2026-11-09)", "## K9999: stopping corrector")),
    ]
    caught = 0
    for label, plant in plants:
        with tempfile.TemporaryDirectory(prefix="gu_program_focus_") as temp:
            fixture = Path(temp)
            copy_fixture(fixture)
            plant(fixture)
            if audit(fixture):
                caught += 1
                print(f"[PASS] caught hostile mutation: {label}")
            else:
                print(f"[FAIL] hostile mutation escaped: {label}")
    print(f"selftest: baseline green; {caught}/{len(plants)} hostile mutations caught")
    return 0 if caught == len(plants) else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    errors = audit(ROOT)
    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1
    print("[PASS] program_focus steering, matrix, bets and front doors agree")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
