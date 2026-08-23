#!/usr/bin/env python3
"""Probe for the CBRS-1 owner necessity classification.

Every witness claim is re-verified against the LIVE candidate registry it
cites, not against this artifact's prose: if a recorded field moves, the
classification fails here rather than drifting silently.
"""

from __future__ import annotations

import copy
import glob
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/cbrs1-owner-necessity-theorem.json"
RESULT = ROOT / "explorations/conditional-build/cbrs1-owner-necessity-theorem-2026-08-23.md"
CORPUS_GLOB = "lab/process/selected-k77-cbrs1*.json"

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "sufficiency is established",
    "CBRS-1 is closed",
    "GU is falsified",
    "prediction credit is awarded",
)

EXPECTED_CONDITIONS = ["N1", "N2", "N3", "N4", "N5", "N6"]

# Live-registry facts each witness claim must still exhibit. Keys are probed
# against the flattened JSON text of the cited registry.
WITNESS_FACTS = {
    "CBRS-1M": ["FAIL_CONSTANT_GRADE_METRIC_STATIONARITY", "PASS_COMPLETE_POINT_OWNERS"],
    "CBRS-1P": ["230650", "230610", "EXACTLY_THE_40"],
    "CBRS-1U": ["OBSTRUCTED_BY_NONZERO_PRIMITIVE_MOMENTUM_DIVERGENCE"],
    "CBRS-1I": ["OPEN__CONSTANT_POINTWISE_RECONSTRUCTION", "'target_blind': True"],
    "CBRS-1Y": ["'two_density_universality': False", "'density_fitted_local_solution_exists': True"],
    "CBRS-1AA": ["'overall_coefficient_source_owned': False"],
}


def load_inputs() -> dict[str, object]:
    data = json.loads(REGISTRY.read_text())
    live: dict[str, str] = {}
    for w in data["binding_witnesses"]:
        p = ROOT / w["registry"]
        live[w["witness"]] = str(json.loads(p.read_text())) if p.exists() else ""
    return {
        "data": data,
        "result": RESULT.read_text(),
        "live": live,
        "corpus_count": len(glob.glob(str(ROOT / CORPUS_GLOB))),
        "registries_exist": {w["registry"]: (ROOT / w["registry"]).exists()
                             for w in data["binding_witnesses"]},
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
    live = inputs["live"]
    corpus_count = inputs["corpus_count"]
    registries_exist = inputs["registries_exist"]
    assert isinstance(data, dict) and isinstance(result, str) and isinstance(live, dict)
    assert isinstance(registries_exist, dict)

    # ---- corpus and condition structure ----------------------------------
    check(corpus_count == data["corpus"]["count"] and data["corpus"]["count"] >= 27,
          "live corpus matches the recorded count and has not shrunk")
    conds = [c["id"] for c in data["conditions"]]
    check(conds == EXPECTED_CONDITIONS, "six conditions N1..N6 in order")
    check(all(len(c.get("statement", "")) > 40 for c in data["conditions"]),
          "each condition states a substantive requirement")

    # ---- every condition except N1 is individually witnessed --------------
    witnesses = data["binding_witnesses"]
    witnessed = {w["condition"] for w in witnesses}
    for cid in ("N2", "N3", "N4", "N5", "N6"):
        check(cid in witnessed, f"{cid} has a binding witness")
    check(sum(1 for w in witnesses if w["condition"] == "N6") == 2,
          "N6 carries both its closure and ownership witnesses")
    for w in witnesses:
        check(bool(w.get("isolates")), f"{w['witness']} states what it isolates")
        check(bool(w.get("recorded")), f"{w['witness']} quotes a recorded state")

    # ---- witness claims re-verified against the LIVE registries ----------
    for path, exists in registries_exist.items():
        check(exists, f"cited registry exists: {path}")
    for name, facts in WITNESS_FACTS.items():
        blob = live.get(name, "")
        for fact in facts:
            check(fact in blob, f"{name} live registry still records: {fact}")

    # ---- the tension is recorded as open, not as a result ----------------
    tension = data["n2_n6_tension"]
    check(tension["status"].startswith("OPEN"), "the N2/N6 tension is OPEN")
    check(tension["witness"] == "CBRS-1Y", "the tension witness is CBRS-1Y")
    check("generic" in tension["open_question"], "the open question asks about genericity")
    check(len(tension.get("corroboration", [])) >= 2, "corroborating closes recorded")

    # ---- necessity is not sold as sufficiency ----------------------------
    dne = " ".join(data["does_not_establish"])
    check("SUFFICIENCY" in dne or "sufficiency" in dne, "sufficiency explicitly disclaimed")
    check("cannot supply an owner" in dne, "unsatisfiability explicitly disclaimed")
    check(bool(data.get("scope_caveat")) and "PD-STRUCTURE-TRANSPORT" in data["scope_caveat"],
          "scope caveat cites the transport discipline")

    # ---- the council discriminator is reported honestly ------------------
    out = data["council_discriminator_outcome"]
    check(out["council_item"] == "A2", "reports against council item A2")
    check("PARTIAL" in out["verdict"], "discriminator outcome reported as partial")
    check("NOT_YET_VINDICATED" in out["lens_8_3_terminus"], "terminus lens not prematurely vindicated")
    check("REMAINS_REFUSED" in out["terminal_writeup"], "terminal write-up still refused")
    check("no longer" in out["lane_reposed"], "the lane's question is reposed")

    check(data["target_claim"] == "NONE-NOT-A-KILL", "artifact types its own kill status")
    check(data["ledger_verdict_change"] == "none", "no verdict moved")
    check(data["claim_status_change"] == "none", "no claim status moved")

    # ---- document propagation --------------------------------------------
    result_flat = re.sub(r"\s+", " ", result)
    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("Does not establish" in result, "doc carries the non-establishment section")
    check("necessity is not sufficiency" in result_flat, "doc states necessity is not sufficiency")
    check("prove or refute" in result_flat, "doc states the reposed target")
    for phrase in FORBIDDEN_SUMMARY_GRAMMAR:
        check(phrase not in result_flat, f"forbidden grammar absent: {phrase}")
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
    changed["data"]["binding_witnesses"] = [
        w for w in changed["data"]["binding_witnesses"] if w["condition"] != "N5"]
    mutations.append(("witness-dropped", "N5 has a binding witness", changed))

    changed = copy.deepcopy(baseline)
    changed["live"]["CBRS-1P"] = changed["live"]["CBRS-1P"].replace("230650", "999999")
    mutations.append(("live-registry-drift", "CBRS-1P live registry still records: 230650", changed))

    changed = copy.deepcopy(baseline)
    changed["live"]["CBRS-1Y"] = changed["live"]["CBRS-1Y"].replace(
        "'two_density_universality': False", "'two_density_universality': True")
    mutations.append(("tension-witness-drift", "CBRS-1Y live registry still records: 'two_density_universality': False", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["n2_n6_tension"]["status"] = "PROVED_UNSATISFIABLE"
    mutations.append(("tension-overclaim", "the N2/N6 tension is OPEN", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["does_not_establish"] = ["nothing"]
    mutations.append(("sufficiency-smuggle", "sufficiency explicitly disclaimed", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["council_discriminator_outcome"]["terminal_writeup"] = "NOW_WARRANTED"
    mutations.append(("premature-terminus", "terminal write-up still refused", changed))

    # Planted positive for the summary-grammar detector.
    changed = copy.deepcopy(baseline)
    changed["result"] += "\nWith N1-N6 in hand, sufficiency is established.\n"
    mutations.append(("planted-forbidden-grammar", "forbidden grammar absent: sufficiency is established", changed))

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
