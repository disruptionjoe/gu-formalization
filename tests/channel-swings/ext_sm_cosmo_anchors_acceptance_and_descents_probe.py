#!/usr/bin/env python3
"""Propagation and failure-path probe for the SM/cosmology anchors and owner ledger v2."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/ext-sm-cosmo-anchors-acceptance-and-descents.json"
RESULT = ROOT / "explorations/conditional-build/ext-sm-cosmo-anchors-acceptance-and-descents-2026-08-23.md"
DELTA = ROOT / "lab/process/conditional-evidence-deltas/gu-ext-sm-cosmo-bench-linking-2026-08-23.json"
V1 = ROOT / "lab/process/ext-gr-anchors-reverse-track-descents-r5-to-r3.json"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.260.json"

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "GU derives three generations",
    "the Standard Model is recovered",
    "the expansion history is reproduced",
    "prediction credit is awarded",
)

EXPECTED_ANCHORS = ["EXT-SM-STRUCTURE", "EXT-COSMO-BACKGROUND"]
EXPECTED_OWNERS_V2 = ["OWNER-A", "OWNER-B", "OWNER-C", "OWNER-D", "OWNER-E", "OWNER-F", "OWNER-G"]


def load_inputs() -> dict[str, object]:
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "delta": json.loads(DELTA.read_text()),
        "v1": json.loads(V1.read_text()),
        "ledger": json.loads(LEDGER.read_text()),
        "state": (ROOT / "CURRENT-STATE.yaml").read_text(),
        "next_steps": (ROOT / "NEXT-STEPS.md").read_text(),
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
    v1 = inputs["v1"]
    ledger = inputs["ledger"]
    state = inputs["state"]
    next_steps = inputs["next_steps"]
    assert isinstance(data, dict) and isinstance(delta, dict) and isinstance(v1, dict)
    assert isinstance(ledger, dict) and isinstance(result, str)
    assert isinstance(state, str) and isinstance(next_steps, str)

    anchors = {a["id"]: a for a in data["anchors"]}
    check(list(anchors) == EXPECTED_ANCHORS, "two anchors in order")
    for aid in EXPECTED_ANCHORS:
        a = anchors.get(aid, {})
        check(a.get("status") == "ACCEPTED_AS_SCOPED_REVERSE_SCAFFOLD_TARGET", f"{aid} accepted-as-scoped")
        check(a.get("gu_realization_status") == "PER_LINKED_ROWS_UNCHANGED", f"{aid} rows unchanged")
        check(bool(a.get("claim_ceiling")), f"{aid} claim ceiling")
        check(len(a.get("linked_rows", [])) >= 2, f"{aid} links existing rows")

    # Linked rows must actually exist in the ledger: anchors link, never invent.
    ledger_rows = {r["id"] for r in ledger["rows"] if isinstance(r, dict) and "id" in r}
    for aid in EXPECTED_ANCHORS:
        linked = set(anchors.get(aid, {}).get("linked_rows", []))
        check(linked.issubset(ledger_rows), f"{aid} linked rows exist in ledger")

    sm = anchors["EXT-SM-STRUCTURE"]
    check("not adjudicated here" in sm["statement"], "SM anchor leaves total-theory chirality alone")
    check("controls" in sm["routing_forks_typed"], "SM routing forks typed as controls")
    check("not derivation" in sm["claim_ceiling"], "SM count is accommodation not derivation")
    cos = anchors["EXT-COSMO-BACKGROUND"]
    check("PP1/PP3" in cos["no_duplication"], "cosmology anchor defers to frozen packages")
    check("P-OBS" in cos["statement"], "cosmology confrontation routed to P-OBS")

    descents = data["descents"]
    check(list(descents) == EXPECTED_ANCHORS, "two descents in order")
    for aid in EXPECTED_ANCHORS:
        d = descents.get(aid, {})
        for rung in ("r5_frozen", "r4_frozen", "r3_frozen"):
            check(d.get(rung, {}).get("comparator_driven") is True, f"{aid} {rung} comparator-driven")
        interface = d.get("interface", [])
        check(len(interface) >= 5, f"{aid} interface has at least five demands")
        check(all(item.get("lands_on") for item in interface), f"{aid} demands land on named gaps")
        check(all(item.get("owner") in EXPECTED_OWNERS_V2 for item in interface),
              f"{aid} demands map to v2 owners")

    check("K109 entry gate" in descents["EXT-SM-STRUCTURE"]["r3_frozen"]["quotient"], "SM R3 binds K109 gate")
    check("T-4" in descents["EXT-COSMO-BACKGROUND"]["r4_frozen"]["causal"], "cosmology inherits T-4")
    check("D1 recurs" in descents["EXT-COSMO-BACKGROUND"]["r3_frozen"]["reduction"], "D1 recurrence recorded")

    # Owner ledger v2 must be a superset of v1, with v1's demands preserved.
    v2 = data["consolidated_r1_owner_ledger_v2"]
    v2_owners = [k for k in v2 if k.startswith("OWNER-")]
    check(v2_owners == EXPECTED_OWNERS_V2, "seven owners in order")
    v1_ledger = v1["consolidated_r1_owner_ledger"]
    check(set(v1_ledger).issubset(set(v2_owners)), "v2 covers every v1 owner")
    for owner_id, entry in v1_ledger.items():
        v2_demands = set(v2.get(owner_id, {}).get("demanded_by", []))
        check(set(entry["demanded_by"]).issubset(v2_demands), f"v2 preserves v1 demands for {owner_id}")
    for owner_id in v2_owners:
        check(len(v2[owner_id].get("demanded_by", [])) >= 2, f"{owner_id} triangulated by >=2 demands")

    # Every interface demand in this artifact appears under its owner in v2.
    for aid in EXPECTED_ANCHORS:
        for item in descents[aid]["interface"]:
            owner_id = item["owner"]
            if owner_id in v2:
                check(item["id"] in v2[owner_id].get("demanded_by", []),
                      f"v2 lists {item['id']} under {owner_id}")

    check("discharges or materially narrows" in data["progress_rule"], "progress rule")
    check(data["mechanism_commitment"] == "NONE", "mechanism NONE")
    check(data["confirmation_credit"] == "NONE", "confirmation NONE")
    check("CBRS-blocked" in data["instantiation"], "instantiation blocked")
    check(data["ledger_verdict_change"] == "none", "ledger unchanged")
    check(data["canon_verdict_change"] == "none", "canon unchanged")

    check(delta["status"] == "pending", "delta pending")
    check(delta["integration"] is None, "delta not self-integrated")
    check("Verdict changes: none" in delta["proposed_effect"]["summary"], "delta requests no verdict change")
    check(all("append" in c or "context" in c for c in delta["proposed_effect"]["requested_row_changes"]),
          "delta proposes only appends and context notes")

    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("Demands, not constructions" in result or "DEMANDS, NOT CONSTRUCTIONS" in result, "demand ceiling")
    # Wrapped prose: match on the words, not on their line break.
    check("accommodation" in result and "not\nderivation" in result or "accommodation, not derivation" in result,
          "count typed as accommodation")
    check("non-adjudicating" in result or "controls" in result, "routing controls stated")
    for phrase in FORBIDDEN_SUMMARY_GRAMMAR:
        check(phrase not in result, f"forbidden grammar absent: {phrase}")

    check("EXT-SM-STRUCTURE" in state and "OWNER-G" in state, "state records anchors and v2 owners")
    check("LAST TWO LEGS" in next_steps or "last two legs" in next_steps, "next steps announcement")
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
    changed["data"]["anchors"][0]["statement"] = (
        "The construction must derive three chiral families from the total theory.")
    mutations.append(("chirality-adjudication-smuggle", "SM anchor leaves total-theory chirality alone", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["anchors"][0]["linked_rows"] = ["LT-SM99", "LT-SM98"]
    mutations.append(("invented-rows", "EXT-SM-STRUCTURE linked rows exist in ledger", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["consolidated_r1_owner_ledger_v2"]["OWNER-A"]["demanded_by"] = ["SM-1", "COS-1"]
    mutations.append(("v1-demand-loss", "v2 preserves v1 demands for OWNER-A", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["consolidated_r1_owner_ledger_v2"]["OWNER-F"]["demanded_by"] = ["SM-5"]
    mutations.append(("triangulation-loss", "OWNER-F triangulated by >=2 demands", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["anchors"][1]["no_duplication"] = "this anchor restates the dark-energy kill surfaces"
    mutations.append(("duplication-smuggle", "cosmology anchor defers to frozen packages", changed))

    changed = copy.deepcopy(baseline)
    changed["result"] = changed["result"].replace(
        "GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY",
        "GU-COMPARATOR-ROUTING-CLASSIFICATION: REMOVED",
    )
    mutations.append(("routing-regression", "routing class", changed))

    # Planted positive: the forbidden-grammar detector must fire on an injected claim.
    changed = copy.deepcopy(baseline)
    changed["result"] += "\nWith the anchors benched, GU derives three generations.\n"
    mutations.append(("planted-forbidden-grammar", "forbidden grammar absent: GU derives three generations", changed))

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
