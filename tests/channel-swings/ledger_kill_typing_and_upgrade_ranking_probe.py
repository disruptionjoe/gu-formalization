#!/usr/bin/env python3
"""Probe for the ledger kill-typing audit and upgrade ranking.

Re-derives the AC-F3 finding from the live ledger and register rather than
trusting the artifact's prose: the sibling precedent, the self-inconsistent
mapping grade, and the registered claims are all recomputed here.
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/ledger-kill-typing-and-upgrade-ranking.json"
RESULT = ROOT / "explorations/conditional-build/ledger-kill-typing-and-upgrade-ranking-2026-08-23.md"
DELTA = ROOT / "lab/process/conditional-evidence-deltas/gu-ledger-kill-typing-2026-08-23.json"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.260.json"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
GATE = ROOT / "process_gates/kill_target_claim_audit.py"

CITED_CLAIM_IDS = ("SC-GEN-01", "SC-GEN-02", "SC-GEN-04", "SC-CHI-50", "SC-CHI-51")

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "GU is vindicated",
    "the falsifications were wrong",
    "prediction credit is awarded",
    "the ledger has no negative results",
)


def load_inputs() -> dict[str, object]:
    ledger = json.loads(LEDGER.read_text())
    rows = {r["id"]: r for r in ledger["rows"] if isinstance(r, dict) and "id" in r}
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "delta": json.loads(DELTA.read_text()),
        "rows": rows,
        "taxonomy": ledger["taxonomy"]["verdict_kinds"],
        "register": REGISTER.read_text(),
        "gate": GATE.read_text(),
    }


def collect_failures(inputs: dict[str, object]) -> tuple[int, list[str]]:
    failures: list[str] = []
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    data = inputs["data"]
    result = inputs["result"]
    delta = inputs["delta"]
    rows = inputs["rows"]
    taxonomy = inputs["taxonomy"]
    register = inputs["register"]
    gate = inputs["gate"]
    assert isinstance(data, dict) and isinstance(delta, dict) and isinstance(rows, dict)
    assert isinstance(taxonomy, dict) and isinstance(result, str)
    assert isinstance(register, str) and isinstance(gate, str)

    # ---- the finding, recomputed from the live ledger ---------------------
    acf3 = rows.get("AC-F3", {})
    acf4 = rows.get("AC-F4", {})
    check(acf3.get("reason_kind") == "GENUINE_FALSIFICATION", "AC-F3 still typed GENUINE_FALSIFICATION")
    check("ROUTE_KILL" in str(acf3.get("mapping_grade", "")), "AC-F3 mapping grade says ROUTE_KILL")
    check(acf4.get("reason_kind") == "ROUTE_KILLED", "AC-F4 sibling typed ROUTE_KILLED")
    check(acf4.get("verdict") == "DIFFERS", "AC-F4 sibling sits under DIFFERS")
    check(acf3.get("axis") == acf4.get("axis"), "siblings share an axis")
    check("3-primary" in acf3.get("summary", "") and "3-primary" in acf4.get("summary", ""),
          "siblings share the 3-primary target object")
    check("ROUTE_KILLED" in taxonomy.get("DIFFERS", []), "taxonomy carries ROUTE_KILLED under DIFFERS")
    check("GENUINE_FALSIFICATION" in taxonomy.get("OVER_DETERMINED", []),
          "taxonomy carries GENUINE_FALSIFICATION under OVER_DETERMINED")
    check(bool(acf3.get("revival_trigger")), "AC-F3 names a revival trigger (a live alternative)")

    # ---- the registered claims actually exist ----------------------------
    for cid in CITED_CLAIM_IDS:
        check(f"- id: {cid}" in register, f"register carries {cid}")
    chi50 = re.search(r"- id: SC-CHI-50\n(.*?)(?=\n- id: |\Z)", register, re.S)
    check(bool(chi50) and "no chirality for the anomaly to attach to" in " ".join(chi50.group(1).split()),
          "SC-CHI-50 records the no-chirality-for-anomaly stance")
    gen01 = re.search(r"- id: SC-GEN-01\n(.*?)(?=\n- id: |\Z)", register, re.S)
    check(bool(gen01) and "DISAVOWS" in gen01.group(1), "SC-GEN-01 is a DISAVOWS entry")

    # ---- the gate's own record of the cause ------------------------------
    # Docstring prose is wrapped; flatten before phrase checks.
    gate_flat = re.sub(r"\s+", " ", gate)
    check("0 of 84 rows naming any register ID" in gate_flat, "gate records the untyped sweep")
    check("came to target a claim the source never made" in gate_flat, "gate records the consequence")
    # Monotonic: the baseline is a ratchet that may be lowered as rows are
    # typed (it reached 0 on 2026-08-23) but must never be raised.
    m = re.search(r"LEDGER_BASELINE = (\d+)", gate)
    check(bool(m) and int(m.group(1)) <= 8, "gate baseline recorded and never raised")

    # ---- the repaired regression -----------------------------------------
    ltgr8 = rows.get("LT-GR8", {})
    check(ltgr8.get("target_claim") == "NONE-NOT-A-KILL", "LT-GR8 typed with the hatch")
    check("future" in ltgr8.get("target_claim_note", "").lower(), "LT-GR8 note explains the kill_scope field")
    reg_fix = data["gate_regression_repaired"]
    check(reg_fix["row"] == "LT-GR8" and "ok at 8" in reg_fix["after"], "registry records the repair")

    # ---- proposals are proposals, not applications -----------------------
    check(data["ac_f3_finding"]["disposition"] == "PROPOSED_VIA_EVIDENCE_DELTA__NOT_APPLIED",
          "re-typing is proposed, not applied")
    check(data["ledger_verdict_change"] == "none", "no verdict applied")
    check(delta["status"] == "pending", "delta pending")
    check(delta["integration"] is None, "delta not self-integrated")
    check(set(delta["affected_rows"]) == {"AC-F3", "LT-GR1b", "RA-D2"}, "delta targets the three kill rows")
    check("not applied" in delta["proposed_effect"]["summary"], "delta states proposal grade")
    check("no row moves toward SAME" in delta["claim_ceiling"], "delta carries the no-inflation guard")

    # ---- the ranking -----------------------------------------------------
    ranking = data["upgrade_ranking"]
    check([r["rank"] for r in ranking] == [1, 2, 3, 4, 5], "five ranked routes in order")
    check(all(r["competes_with_scheduled_lane"] is False for r in ranking),
          "every ranked route is non-competing")
    check(all(r.get("cost") and r.get("movement") and r.get("level") for r in ranking),
          "each route carries cost, movement and level")
    pred = next(r for r in ranking if "preregister" in r["route"])
    check(len(pred["rows"]) == 9, "the nine PREDICTION rows enumerated")
    live_pred = {rid for rid, r in rows.items() if r.get("reason_kind") == "PREDICTION"}
    check(set(pred["rows"]) == live_pred, "enumerated PREDICTION rows match the live ledger")
    check("MISSING_CONSTRUCTION" in data["explicitly_not_ranked"], "the competing lane is excluded explicitly")

    # ---- document propagation --------------------------------------------
    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("NONE-NOT-A-KILL" in result, "artifact types its own kill status")
    for phrase in FORBIDDEN_SUMMARY_GRAMMAR:
        check(phrase not in result, f"forbidden grammar absent: {phrase}")
    return checks, failures


def main() -> int:
    checks, failures = collect_failures(load_inputs())
    for label in failures:
        print(f"[FAIL] {label}")
    if failures:
        return 1
    print(f"PASS {checks}/{checks}")
    return 0


def selftest() -> int:
    baseline = load_inputs()
    checks, failures = collect_failures(baseline)
    if failures:
        for label in failures:
            print(f"[FAIL] baseline: {label}")
        return 1
    print(f"BASELINE PASS {checks}/{checks}")

    mutations: list[tuple[str, str, dict[str, object]]] = []

    changed = copy.deepcopy(baseline)
    changed["rows"]["AC-F4"]["reason_kind"] = "GENUINE_FALSIFICATION"
    mutations.append(("sibling-precedent-loss", "AC-F4 sibling typed ROUTE_KILLED", changed))

    changed = copy.deepcopy(baseline)
    changed["rows"]["LT-GR8"]["target_claim"] = ""
    mutations.append(("regression-reintroduced", "LT-GR8 typed with the hatch", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["ac_f3_finding"]["disposition"] = "APPLIED"
    mutations.append(("unilateral-application", "re-typing is proposed, not applied", changed))

    changed = copy.deepcopy(baseline)
    changed["delta"]["claim_ceiling"] = changed["delta"]["claim_ceiling"].replace(
        "no row moves toward SAME", "rows may move toward SAME")
    mutations.append(("inflation-guard-drop", "delta carries the no-inflation guard", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["upgrade_ranking"][0]["competes_with_scheduled_lane"] = True
    mutations.append(("competition-smuggle", "every ranked route is non-competing", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["upgrade_ranking"][2]["rows"] = ["RA-A4"]
    mutations.append(("prediction-enumeration-desync", "the nine PREDICTION rows enumerated", changed))

    # Planted positive for the summary-grammar detector.
    changed = copy.deepcopy(baseline)
    changed["result"] += "\nOn this reading GU is vindicated.\n"
    mutations.append(("planted-forbidden-grammar", "forbidden grammar absent: GU is vindicated", changed))

    ok = True
    for name, expected, mutated in mutations:
        _, caught = collect_failures(mutated)
        if expected not in caught:
            print(f"[FAIL] mutation {name}: expected failing check {expected!r}, got {caught!r}")
            ok = False
        else:
            print(f"MUTATION CAUGHT {name}: [FAIL] {expected}")
    print("FAILURE-PATH SELFTEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
