#!/usr/bin/env python3
"""Fail-closed audit for CURRENT-STATE live-versus-historical frontier custody."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CURRENT = ROOT / "CURRENT-STATE.yaml"
REGISTRY = ROOT / "lab/process/current-frontier-semantic-currency.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_inputs() -> dict:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    basis = registry["basis"]
    return {
        "current": yaml.safe_load(CURRENT.read_text(encoding="utf-8")),
        "registry": registry,
        "agenda": json.loads((ROOT / basis["research_agenda"]["path"]).read_text()),
        "dispositions": json.loads(
            (ROOT / basis["phenomenology_disposition_register"]["path"]).read_text()
        ),
        "b2": json.loads((ROOT / basis["b2_frontier"]["path"]).read_text()),
        "qualification": json.loads(
            (ROOT / basis["w154_w229_qualification"]["path"]).read_text()
        ),
        "b5_artifact": (ROOT / registry["b5_agenda_currency"]["result_ref"]).read_text(),
    }


def audit(data: dict, check_digests: bool = True) -> list[str]:
    failures: list[str] = []
    current = data["current"]
    registry = data["registry"]
    surface = registry["surface_contract"]
    live = current.get(surface["live_key"])
    history = current.get(surface["history_key"])

    def check(ok: bool, message: str) -> None:
        if not ok:
            failures.append(message)

    check(isinstance(live, str) and bool(live.strip()), "live next_condition missing")
    check(isinstance(history, str) and bool(history.strip()), "prior_conditions history missing")
    if isinstance(live, str):
        check(len(live) < 2400, "live next_condition is not bounded")
        check("strongest disjoint non-B2 gate" in live, "live selection route missing")
        check("current named B2 action-root set is empty" in live, "empty B2 root missing")
        check("91 terminal" in live and "ledger v0.263" in live, "protected live facts missing")
        for marker in surface["stale_live_markers_forbidden"]:
            check(marker not in live, f"stale marker remains live: {marker}")
    if isinstance(history, str):
        check("25 terminal rows and 66 open rows" in history, "historical 25/66 condition lost")
        check("b2_selectable=false" in history, "historical B2 gate condition lost")
    summary = current.get("current_result", {}).get("summary", "")
    check("91 terminal and 0 open rows" in summary, "current exhaustion result lost")

    question = current.get("current_question", "")
    check(
        registry["live_frontier"]["current_question_contains"] in question,
        "current_question disagrees with live frontier",
    )

    disposition = data["dispositions"]["exhaustion_evaluation"]
    expected = registry["basis"]["phenomenology_disposition_register"]
    for key in ("terminal_rows", "open_rows", "exhausted", "b2_selectable"):
        check(disposition.get(key) == expected[key], f"disposition mismatch: {key}")

    root = data["qualification"]["root_candidate_rebuild"]
    qual = data["qualification"]["admission_result"]
    check(root.get("current_named_root_candidate_set") == [], "named B2 root is not empty")
    check(
        root.get("state") == registry["basis"]["w154_w229_qualification"]["root_candidate_state"],
        "root-candidate state mismatch",
    )
    check(qual.get("candidate_admitted") is False, "W154/W229 unexpectedly admitted")

    agenda_item = next(
        item for item in data["agenda"]["work_items"]
        if item["id"] == "CONDITIONAL-BUILD-REVERSE-SCAFFOLD"
    )
    check("current named root-candidate set is empty" in agenda_item["current_authority"],
          "agenda root authority is not current")
    check("W154/W229 is nonadmitted" in agenda_item["latest_result"],
          "agenda latest result is not current")
    check("strongest disjoint non-B2 native gate" in agenda_item["next_swing"],
          "agenda next swing is not the live route")

    b5 = next(
        item for item in data["agenda"]["work_items"]
        if item["id"] == registry["b5_agenda_currency"]["work_item"]
    )
    b5_contract = registry["b5_agenda_currency"]
    check(b5["state"] == b5_contract["state"], "B5 agenda state is stale")
    check("RB6 recertification and the full-20 Gram-adjoint wave completed" in b5["latest_result"],
          "B5 latest result does not retire RB6/Wave One")
    check("EXTERNAL-VIA-GRAM" in b5["latest_result"],
          "B5 graph-mixing branch ceiling lost")
    check(b5_contract["live_reopener"] in b5["next_swing"],
          "B5 live reopener missing")
    check("Do not repeat RB6 recertification" in b5["next_swing"],
          "B5 completed work is not forbidden as a repeat")
    check("odd rank-128 spinor" in b5["current_authority"],
          "B5 boundary multiplier typing lost")
    check("source-native `B5-MIDDLE-DIFFERENTIAL` row remains" in data["b5_artifact"],
          "B5 source-native/independent boundary lost")
    check("## Hostile review and ceiling" in data["b5_artifact"],
          "B5 currency hostile review missing")

    check(data["b2"]["basis"]["terminal_rows"] == 91, "B2 basis terminal count moved")
    check(data["b2"]["basis"]["b2_selectable"] is True, "B2 selectability history moved")
    check(all(value is False for value in registry["protected_effects"].values()),
          "protected movement field changed")

    if check_digests:
        for name, entry in registry["basis"].items():
            if "path" in entry:
                check(digest(ROOT / entry["path"]) == entry["sha256"],
                      f"basis digest mismatch: {name}")
    return failures


def selftest(base: dict) -> tuple[int, int]:
    mutations = []

    def add(name: str, fn) -> None:
        case = copy.deepcopy(base)
        fn(case)
        mutations.append((name, case))

    add("live-key-missing", lambda d: d["current"].pop("next_condition"))
    add("history-key-missing", lambda d: d["current"].pop("prior_conditions"))
    add("stale-25-66-live", lambda d: d["current"].__setitem__(
        "next_condition", d["current"]["next_condition"] + " 25 terminal and 66 open"))
    add("root-fabricated", lambda d: d["qualification"]["root_candidate_rebuild"].__setitem__(
        "current_named_root_candidate_set", ["SYNTHETIC-CBRS-1AC"]))
    add("terminal-count-moved", lambda d: d["dispositions"]["exhaustion_evaluation"].__setitem__(
        "terminal_rows", 90))
    add("b2-gate-reversed", lambda d: d["b2"]["basis"].__setitem__("b2_selectable", False))
    add("agenda-stale", lambda d: d["agenda"]["work_items"][2].__setitem__(
        "next_swing", "Qualify the only named materially distinct candidate"))
    add("agenda-latest-stale", lambda d: d["agenda"]["work_items"][2].__setitem__(
        "latest_result", "The hourly invariant-gapping campaign is complete"))
    add("b5-rb6-repeat", lambda d: next(
        item for item in d["agenda"]["work_items"]
        if item["id"] == "B5-INDEPENDENT-RECONSTRUCTION"
    ).__setitem__("next_swing", "Step 0: recertify the remaining RB6 null with exact derivatives."))
    add("protected-effect-moved", lambda d: d["registry"]["protected_effects"].__setitem__(
        "ledger_verdict_change", True))

    caught = 0
    for name, case in mutations:
        failures = audit(case, check_digests=False)
        if failures:
            caught += 1
        else:
            print(f"RED selftest mutation escaped: {name}")
    return caught, len(mutations)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = load_inputs()
    failures = audit(data)
    if failures:
        for failure in failures:
            print(f"RED current_frontier_semantic_currency: {failure}")
        return 1
    print("PASS current_frontier_semantic_currency: live/history/owner facts")
    if args.selftest:
        caught, total = selftest(data)
        print(f"PASS hostile mutations caught: {caught}/{total}")
        return 0 if caught == total else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
