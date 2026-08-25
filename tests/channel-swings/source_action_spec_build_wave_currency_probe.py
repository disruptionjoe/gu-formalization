#!/usr/bin/env python3
"""Probe for the requirements-spec build-wave currency restoration.

Verifies the three restored rows, recomputes the spec tallies independently
from the companion test's own table, and checks every cited source and test
path actually exists -- the defect class that shipped a wrong W203 path in
draft.
"""

from __future__ import annotations

import copy
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/source-action-spec-build-wave-currency.json"
RESULT = ROOT / "explorations/conditional-build/source-action-spec-build-wave-currency-2026-08-23.md"
SPEC = ROOT / "explorations/source-action-requirements-spec-2026-07-13.md"
SPEC_TEST = ROOT / "tests/spec-consistency/source_action_requirements_consistency.py"

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "H41 is built",
    "the source action is complete",
    "prediction credit is awarded",
    "the coefficients are fitted",
)

ROW_RE = re.compile(r'\("(SA-[A-Za-z0-9]+)",\s*"([A-Z]+)"\)')
EXPECTED_NEW = ["SA-G11", "SA-G12", "SA-G13"]


def load_inputs() -> dict[str, object]:
    data = json.loads(REGISTRY.read_text())
    cited: dict[str, bool] = {}
    for row in data["rows_added"]:
        for key in ("source", "test"):
            cited[row[key]] = (ROOT / row[key]).exists()
    return {
        "data": data,
        "result": RESULT.read_text(),
        "spec": SPEC.read_text(),
        "spec_test": SPEC_TEST.read_text(),
        "cited_exist": cited,
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
    spec = inputs["spec"]
    spec_test = inputs["spec_test"]
    cited_exist = inputs["cited_exist"]
    assert isinstance(data, dict) and isinstance(cited_exist, dict)
    assert all(isinstance(s, str) for s in (result, spec, spec_test))
    check(bool(cited_exist), "cited provenance set nonempty")

    # ---- the three rows are present and correctly classed ----------------
    added = {r["id"]: r for r in data["rows_added"]}
    check(list(added) == EXPECTED_NEW, "three rows added in order")
    for rid in EXPECTED_NEW:
        check(f"| {rid} |" in spec, f"{rid} present in spec")
        check(added[rid]["data_fitted"] is False, f"{rid} recorded as not data-fitted")
        check(bool(added[rid]["qualifier"]), f"{rid} carries a typing qualifier")
        check("branch-3" in added[rid]["qualifier"] or "axiom" in added[rid]["qualifier"],
              f"{rid} typed conditional or reduced")
    check(added["SA-G11"]["class"] == "FIT" and added["SA-G12"]["class"] == "FIT", "kappa and Z_U are FIT")
    check(added["SA-G13"]["class"] == "DECLARATION", "the posit is a DECLARATION")
    check("sign forced" in added["SA-G11"]["qualifier"], "kappa sign forced recorded")
    check("14-dimensional" in added["SA-G13"]["qualifier"], "W230 current-space dimension recorded")

    # ---- tallies recomputed independently from the companion test table --
    rows = ROW_RE.findall(spec_test)
    counts = Counter(cls for _, cls in rows)
    after = data["tallies"]["after"]
    before = data["tallies"]["before"]
    check(len(rows) == 31, "spec test table has 31 rows")
    check(counts["FORCED"] == 8, "recomputed FORCED tally = 8")
    check(counts["DECLARATION"] == 10, "recomputed DECLARATION tally = 10")
    check(counts["FIT"] == 13, "recomputed FIT tally = 13")
    check(after["rows"] == len(rows), "registry rows agree with recomputed table")
    check(after["DECLARATION"] == counts["DECLARATION"] and after["FIT"] == counts["FIT"],
          "registry class tallies agree with recomputed table")
    check(before["rows"] + len(EXPECTED_NEW) == after["rows"], "tally arithmetic: rows")
    check(before["FORCED"] == after["FORCED"], "tally arithmetic: FORCED unchanged")
    check(before["DECLARATION"] + 1 == after["DECLARATION"], "tally arithmetic: one DECLARATION")
    check(before["FIT"] + 2 == after["FIT"], "tally arithmetic: two FITs")
    check("31 requirement rows: 8 FORCED, 10 DECLARATION, 13 FIT"
          in " ".join(spec.split()), "spec tallies updated")
    check("31 rows" in spec, "spec inline row count updated")
    check("len(TABLE) == 31" in spec_test, "spec test row assertion updated")

    # ---- provenance: every cited path exists -----------------------------
    for path, exists in cited_exist.items():
        check(exists, f"cited path exists: {path}")

    # ---- the lapse is read from history, and H41 status is preserved -----
    hist = data["maintenance_history"]
    check(hist["lapse_after"].startswith("2026-07-14"), "lapse boundary dated")
    check(set(hist["wave_that_continued"]) >= {"W203", "W229", "W230", "W236"}, "wave enumerated")
    check(len(hist["observed_updates"]) == 2, "observed maintenance updates recorded")
    h41 = data["h41_status_checked"]
    check(h41["claim"] == "H41 remains unbuilt", "H41 status preserved")
    check("refuted" in h41["refuted_hypothesis"] or bool(h41["evidence"]), "H41 hypothesis checked with evidence")
    check("unbuilt" in data["does_not_loosen_the_object"] or "zero data-fitted" in data["does_not_loosen_the_object"],
          "tightness accounting recorded")
    check("depends_on" in data["distinct_from_earlier_audit"]["earlier"], "distinct cause from earlier audit")

    check(data["ledger_verdict_change"] == "none", "ledger unchanged")
    check(data["claim_status_change"] == "none", "claim status unchanged")
    check(data["canon_verdict_change"] == "none", "canon unchanged")

    # ---- document propagation -------------------------------------------
    result_flat = re.sub(r"\s+", " ", result)
    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("H41 remains unbuilt" in result_flat, "doc preserves H41 status")
    check("zero data-fitted coefficients" in result_flat, "doc states the tightness accounting")
    check("branch-3 / W154-conditional" in result_flat or "branch-conditional" in result_flat,
          "doc types the conditionality")
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
    changed["spec_test"] = changed["spec_test"].replace('("SA-G13", "DECLARATION"),', "")
    mutations.append(("row-desync", "spec test table has 31 rows", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["tallies"]["after"]["FIT"] = 12
    mutations.append(("tally-arithmetic-break", "tally arithmetic: two FITs", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["rows_added"][0]["data_fitted"] = True
    mutations.append(("data-fitting-smuggle", "SA-G11 recorded as not data-fitted", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["rows_added"][2]["class"] = "FIT"
    mutations.append(("posit-misclass", "the posit is a DECLARATION", changed))

    changed = copy.deepcopy(baseline)
    changed["cited_exist"] = dict(changed["cited_exist"])
    first = next(iter(changed["cited_exist"]), None)
    if first is None:
        mutations.append(("empty-provenance", "cited provenance set nonempty", changed))
    else:
        changed["cited_exist"][first] = False
        mutations.append(("broken-provenance", f"cited path exists: {first}", changed))

    changed = copy.deepcopy(baseline)
    changed["cited_exist"] = {}
    mutations.append(("missing-provenance-set", "cited provenance set nonempty", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["h41_status_checked"]["claim"] = "H41 is built"
    mutations.append(("h41-status-flip", "H41 status preserved", changed))

    # Planted positive for the summary-grammar detector.
    changed = copy.deepcopy(baseline)
    changed["result"] += "\nAfter this wave H41 is built.\n"
    mutations.append(("planted-forbidden-grammar", "forbidden grammar absent: H41 is built", changed))

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
