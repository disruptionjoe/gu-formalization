#!/usr/bin/env python3
"""Fail closed if GU reverse search collapses into action-first selection.

The gate checks the owner-native two-graph contract, every active steering
front door, and a small selection simulation.  ``--selftest`` first requires a
green repository baseline, then plants independent control regressions and
requires every one to be detected.
"""

from __future__ import annotations

import argparse
import copy
import json
import shutil
import tempfile
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
REVERSE = [
    "empirical_benchmark_descent",
    "operational_constraint_extraction",
    "state_observable_interface",
    "causal_dynamical_demand",
    "candidate_action_requirements",
]
FORWARD = [
    "action_causal_closure",
    "physical_state_space",
    "observable_export",
    "held_out_confrontation",
]
ANCHORS = {
    "EXT-QM-MASSIVE-MATTER-INTERFERENCE",
    "EXT-QM-SPACELIKE-BELL-NOSIGNAL",
}
FILES = {
    "contract": Path("lab/process/reverse-scaffold-method-contract.json"),
    "passport": Path("lab/specifications/theory-passport/gu-geometry-first-v0.1.yaml"),
    "agenda": Path("lab/process/RESEARCH-AGENDA.json"),
    "current": Path("CURRENT-STATE.yaml"),
    "program": Path("RESEARCH-PROGRAM.md"),
    "posture": Path("RESEARCH-POSTURE.md"),
    "next": Path("NEXT-STEPS.md"),
    "contributing": Path("CONTRIBUTING.md"),
    "readme": Path("README.md"),
    "protocol": Path("lab/process/construction-space-exploration-protocol.md"),
}


def load_json(root: Path, key: str) -> dict:
    return json.loads((root / FILES[key]).read_text(encoding="utf-8"))


def load_text(root: Path, key: str) -> str:
    return (root / FILES[key]).read_text(encoding="utf-8")


def item(agenda: dict) -> dict:
    for candidate in agenda.get("work_items", []):
        if candidate.get("id") == "CONDITIONAL-BUILD-REVERSE-SCAFFOLD":
            return candidate
    return {}


def stage_ids(graph: dict, field: str) -> list[str]:
    stages = graph.get(field, [])
    return [stage.get("id") if isinstance(stage, dict) else stage for stage in stages]


def compact(text: str) -> str:
    return " ".join(text.replace(">", " ").split())


def select_reverse_wave(action_root_empty: bool, arcs: list[dict]) -> list[str]:
    """Model the contract's work selector, not its certification checker."""
    eligible = [
        arc
        for arc in arcs
        if arc.get("direction") == "observed_to_native"
        and arc.get("ready") is True
        and not arc.get("collision")
        and not (arc.get("stage") == "candidate_action_requirements" and not arc.get("demand_lineage"))
    ]
    # An empty action root intentionally has no effect on stages before R1.
    if action_root_empty:
        eligible = [arc for arc in eligible if arc.get("stage") != "candidate_action_requirements"]
    eligible.sort(key=lambda arc: (-int(arc.get("information_gain", 0)), arc["id"]))
    return [arc["id"] for arc in eligible]


def audit(root: Path) -> list[str]:
    errors: list[str] = []
    contract = load_json(root, "contract")
    passport = load_json(root, "passport")
    agenda = load_json(root, "agenda")
    current = load_text(root, "current")
    program = load_text(root, "program")
    posture = load_text(root, "posture")
    next_steps = load_text(root, "next")
    contributing = load_text(root, "contributing")
    readme = load_text(root, "readme")
    protocol = load_text(root, "protocol")

    posture_control = contract.get("work_posture", {})
    if posture_control.get("default_scale") != "big_wave":
        errors.append("contract default scale is not big_wave")
    if posture_control.get("direction_violation") != "reroute_within_same_big_wave":
        errors.append("contract direction violation does not reroute the same Big Wave")
    if posture_control.get("zero_work_authority") != "none":
        errors.append("contract grants zero-work authority")
    if posture_control.get("maintenance_substitution") != "forbidden_when_any_reverse_search_arc_is_executable":
        errors.append("contract permits maintenance substitution")

    graphs = contract.get("method_graphs", {})
    reverse = graphs.get("reverse_scaffold_search", {})
    forward = graphs.get("forward_certification", {})
    if reverse.get("direction") != "observed_to_native":
        errors.append("contract reverse direction changed")
    if stage_ids(reverse, "stages") != REVERSE:
        errors.append("contract reverse stages changed")
    if reverse.get("action_required_to_open") is not False:
        errors.append("contract makes action a reverse-search prerequisite")
    if forward.get("direction") != "native_to_observed":
        errors.append("contract forward direction changed")
    if stage_ids(forward, "stages") != FORWARD:
        errors.append("contract forward certification stages changed")

    anchors = contract.get("quantum_calibration_anchors", [])
    if {anchor.get("id") for anchor in anchors} != ANCHORS:
        errors.append("contract quantum calibration anchor set changed")
    for anchor in anchors:
        if anchor.get("confirmation_credit") != "none":
            errors.append(f"calibration anchor {anchor.get('id')} receives confirmation credit")

    if "critical_path" in passport:
        errors.append("passport restored a single critical_path")
    passport_graphs = passport.get("method_graphs", {})
    p_reverse = passport_graphs.get("reverse_scaffold_search", {})
    p_forward = passport_graphs.get("forward_certification", {})
    if p_reverse.get("direction") != "observed_to_native" or p_reverse.get("stage_ids") != REVERSE:
        errors.append("passport reverse graph disagrees with contract")
    if p_reverse.get("action_required_to_open") is not False:
        errors.append("passport blocks reverse search on action")
    if stage_ids(p_forward, "stages") != FORWARD:
        errors.append("passport forward graph disagrees with contract")
    invariants = passport.get("selection_invariants", {})
    required_invariants = {
        "certification_order_is_not_work_selection_order",
        "blocked_action_does_not_block_reverse_search",
        "action_candidates_require_backward_demand_lineage",
        "source_authentication_is_separate_from_candidate_construction",
        "calibration_cannot_receive_prediction_credit",
        "wrong_direction_reroutes_same_big_wave",
        "wrong_direction_never_authorizes_zero_work_or_scale_down",
    }
    for invariant in required_invariants:
        if invariants.get(invariant) is not True:
            errors.append(f"passport invariant false or missing: {invariant}")

    active = item(agenda)
    if not active:
        errors.append("active reverse-scaffold agenda item missing")
    else:
        if "critical_path" in active:
            errors.append("agenda restored a single critical_path")
        search = active.get("reverse_scaffold_search_path", {})
        certification = active.get("forward_certification_path", {})
        if search.get("ordered_stages") != REVERSE or search.get("action_required_to_open") is not False:
            errors.append("agenda reverse path blocks or disagrees")
        if certification.get("ordered_burdens") != FORWARD:
            errors.append("agenda forward path disagrees")
        priorities = active.get("priority_sequence", [])
        if not priorities or not priorities[0].startswith("R6 calibration"):
            errors.append("agenda does not begin with empirical calibration descent")
        swing = active.get("next_swing", "")
        for phrase in ("Big Wave", "quantum calibration anchors", "same Big Wave"):
            if phrase not in swing:
                errors.append(f"agenda next_swing lacks {phrase!r}")

    current_required = (
        "direction: observed_to_native",
        "action_required_to_open: false",
        "direction_violation: reroute_within_same_big_wave",
        "zero_work_authority: none",
        "EXT-QM-MASSIVE-MATTER-INTERFERENCE",
        "EXT-QM-SPACELIKE-BELL-NOSIGNAL",
        "Execute one largest honest compatible Big Wave",
        "never authorizes zero work",
        "Conditional physical-state interface research is open now",
    )
    for phrase in current_required:
        if compact(phrase) not in compact(current):
            errors.append(f"CURRENT-STATE lacks active control {phrase!r}")

    prose_required = {
        "program": ("Certification order is not work-selection order", "largest honest compatible Big Wave"),
        "posture": ("Certification order is not the work queue", "never licenses no work"),
        "next": ("not a forward dependency queue", "cannot stop work, reduce scale"),
        "contributing": ("observed-to-native reverse search governs contribution", "not a reason to stop"),
        "readme": ("does not block conditional reverse-scaffold research",),
        "protocol": ("direction defect reroutes that Wave", "never authorizes no work"),
    }
    prose = {
        "program": program,
        "posture": posture,
        "next": next_steps,
        "contributing": contributing,
        "readme": readme,
        "protocol": protocol,
    }
    for key, phrases in prose_required.items():
        for phrase in phrases:
            if compact(phrase) not in compact(prose[key]):
                errors.append(f"{FILES[key]} lacks {phrase!r}")

    fixture = [
        {"id": "R6-matter", "direction": "observed_to_native", "stage": REVERSE[0], "ready": True, "information_gain": 9},
        {"id": "R5-bell", "direction": "observed_to_native", "stage": REVERSE[1], "ready": True, "information_gain": 8},
        {"id": "R4-common-state", "direction": "observed_to_native", "stage": REVERSE[2], "ready": True, "information_gain": 7},
        {"id": "R1-action", "direction": "observed_to_native", "stage": REVERSE[4], "ready": True, "demand_lineage": False, "information_gain": 10},
        {"id": "source-action-retrieval", "direction": "native_to_observed", "stage": FORWARD[0], "ready": True, "information_gain": 99},
    ]
    selected = select_reverse_wave(action_root_empty=True, arcs=fixture)
    if selected != ["R6-matter", "R5-bell", "R4-common-state"]:
        errors.append(f"empty-action selector failed Big-Wave reverse reroute: {selected}")

    return errors


def set_json(root: Path, key: str, mutation: Callable[[dict], None]) -> None:
    path = root / FILES[key]
    data = json.loads(path.read_text(encoding="utf-8"))
    mutation(data)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def replace_text(root: Path, key: str, old: str, new: str) -> None:
    path = root / FILES[key]
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"selftest plant source missing: {old}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def selftest() -> int:
    baseline = audit(ROOT)
    if baseline:
        print("[FAIL] clean baseline is not green")
        for error in baseline:
            print(f"  - {error}")
        return 1

    plants: list[tuple[str, Callable[[Path], None]]] = [
        (
            "action becomes reverse prerequisite",
            lambda root: set_json(root, "contract", lambda data: data["method_graphs"]["reverse_scaffold_search"].__setitem__("action_required_to_open", True)),
        ),
        (
            "passport drops blocked-action invariant",
            lambda root: set_json(root, "passport", lambda data: data["selection_invariants"].__setitem__("blocked_action_does_not_block_reverse_search", False)),
        ),
        (
            "agenda returns to source-action priority",
            lambda root: set_json(root, "agenda", lambda data: item(data).__setitem__("priority_sequence", ["Reopen source action first"])),
        ),
        (
            "current state converts reroute to stop",
            lambda root: replace_text(root, "current", "direction_violation: reroute_within_same_big_wave", "direction_violation: stop"),
        ),
        (
            "contract silently scales down",
            lambda root: set_json(root, "contract", lambda data: data["work_posture"].__setitem__("default_scale", "small")),
        ),
        (
            "calibration is promoted to confirmation",
            lambda root: set_json(root, "contract", lambda data: data["quantum_calibration_anchors"][0].__setitem__("confirmation_credit", "positive")),
        ),
        (
            "contributor front door loses no-stop rule",
            lambda root: replace_text(root, "contributing", "not a reason to stop", "a reason to stop"),
        ),
    ]

    caught = 0
    for label, plant in plants:
        with tempfile.TemporaryDirectory(prefix="gu_reverse_scaffold_") as temp:
            fixture = Path(temp)
            for rel in FILES.values():
                (fixture / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / rel, fixture / rel)
            plant(fixture)
            errors = audit(fixture)
            if errors:
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
    print("[PASS] reverse-scaffold direction, Big-Wave liveness, and quantum calibration controls agree")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
