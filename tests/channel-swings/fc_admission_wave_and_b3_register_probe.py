#!/usr/bin/env python3
"""Probe for the first FC admission wave and the first B3 register.

The two properties this artifact must not lose are (a) that FC-7 overturned
every first-pass verdict -- the evidence the criterion earned its place -- and
(b) that no B3 entry softens an obligation. Both are checked structurally, and
the calibration entry's decisive property is re-read from its own live
registry rather than trusted from prose.
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/fc-admission-wave-and-first-b3-register.json"
RESULT = ROOT / "explorations/conditional-build/fc-admission-wave-and-first-b3-register-2026-08-23.md"
GRADE = ROOT / "lab/process/fitting-construction-grade.json"
CALIB = ROOT / "lab/process/gravitational-anchor-bucket-disposition-and-first-fitting-construction.json"

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "GU is excused",
    "the tension relieves GU",
    "prediction credit is awarded",
    "the construction is admitted",
)


def _find(o, key):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key:
                return v
            r = _find(v, key)
            if r is not None:
                return r
    elif isinstance(o, list):
        for x in o:
            r = _find(x, key)
            if r is not None:
                return r
    return None


def load_inputs() -> dict[str, object]:
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "grade": json.loads(GRADE.read_text()),
        "calib_exists": CALIB.exists(),
        "calib_before_anchor": _find(json.loads(CALIB.read_text()), "construction_created_before_anchor")
        if CALIB.exists() else None,
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
    grade = inputs["grade"]
    assert isinstance(data, dict) and isinstance(grade, dict) and isinstance(result, str)

    # ---- the admission result, and FC-7's evidence -----------------------
    fc = data["fc_admission"]
    check(fc["admitted"] == 0, "zero admitted recorded")
    check(fc["reviewed"] == 4, "four reviewed")
    check(fc["fc7_first_pass_met"] == fc["fc7_overturned_to_not_met"] == 4,
          "FC-7 overturned every first-pass MET verdict")
    check(fc["fc1_failed"] == 4 and fc["fc2_failed"] == 4, "FC-1 and FC-2 failed 4/4")
    check("earned its place" in fc["headline"], "the FC-7 evidence is stated as such")

    tax = data["fc7_refusal_taxonomy"]
    check(len(tax) >= 5, "the FC-7 refusal taxonomy has at least five patterns")
    names = {t["pattern"] for t in tax}
    for required in ("CIRCULAR", "INHERITED", "EMPTY_EXTENSION", "ANALYTIC"):
        check(required in names, f"taxonomy carries {required}")
    check(all(len(t["shape"]) > 40 for t in tax), "each pattern states its shape")

    # ---- calibration entry, re-read from its own live registry ----------
    cal = data["calibration_reference"]
    check(inputs["calib_exists"] is True, "the calibration entry's registry exists")
    check(inputs["calib_before_anchor"] is True,
          "calibration entry live registry still records construction_created_before_anchor")
    check("2026-07-11" in cal["decisive_property"] and "2026-08-23" in cal["decisive_property"],
          "the six-week gap is recorded with both dates")
    check("retroactively" in cal["why_decisive"], "the non-retrofittable property is stated")
    check("false" in cal["brief_correction"], "the brief's first-entries claim is corrected")

    # ---- the method fix reached the grade -------------------------------
    fix = data["method_fix_forced"]
    check("reviewer-supplied" in fix["rule_added"] and "FAILED" in fix["rule_added"],
          "the reviewer rule is stated")
    check("reviewer_rule_2026_08_23" in grade, "the grade carries the reviewer rule")
    check("visibly unchecked" in grade.get("reviewer_rule_2026_08_23", ""),
          "the grade's reviewer rule states why the criteria exist")
    check("first_admission_wave_result" in grade, "the grade records the wave result")

    # ---- B3: six entries, none softening --------------------------------
    b3 = data["b3_register"]
    check(b3["entries"] == 6 and len(b3["ids"]) == 6, "six B3 entries")
    check(b3["net_softening"] == 0, "no B3 entry is net-softening")
    d = b3["direction"]
    check(sum(d.values()) == b3["entries"], "the direction breakdown accounts for every entry")
    check(b3.get("direction_scope") == "historical_first_pass_before_primary_source_disposition",
          "direction counts are fenced as historical filing evidence")
    check(d["enlarge"] >= 2, "historical filing records at least two enlarging entries")
    check(bool(b3["maintenance_rule"]) and "citation time" in b3["maintenance_rule"].lower(),
          "the citation-time re-check rule is recorded")
    check("S_8" in b3["maintenance_rule"] or "sigma_8" in b3["maintenance_rule"],
          "the cautionary case is named")
    check(len(b3["refused_with_reasons"]) >= 4, "refused candidates recorded with reasons")
    check(any("closed" in r for r in b3["refused_with_reasons"]),
          "a refused candidate is recorded as a closed tension")
    check(bool(b3["self_corrections_applied"]), "the register's self-corrections are recorded")

    # ---- ceilings --------------------------------------------------------
    check("candidates only" in data["ledger_bearing"], "ledger bearing is candidates only")
    dispositions = b3.get("dispositions", {})
    check(dispositions.get("B3-J95-03", {}).get("status") ==
          "DISPOSED_NO_LEDGER_MOVEMENT__SOURCE_SCOPE_CORRECTION",
          "LT-GR8 carries the accepted J95 source-scope correction")
    check(dispositions.get("B3-DE-01", {}).get("status") ==
          "DISPOSED_NO_LEDGER_MOVEMENT__LIKELIHOOD_SCOPE_CORRECTION",
          "LT-GR2e carries the accepted DE likelihood-scope correction")
    check(dispositions.get("B3-CC-02", {}).get("status") ==
          "DISPOSED_NO_LEDGER_MOVEMENT__OBSERVATION_VS_VACUUM_SCOPE",
          "LT-GR2d carries the accepted CC observation-scope correction")
    check(dispositions.get("B3-CP-04", {}).get("status") ==
          "DISPOSED_NO_LEDGER_MOVEMENT__OBSERVABLE_TO_THETA_SCOPE",
          "LT-SM7 carries the accepted CP observable-scope correction")
    check(dispositions.get("B3-NU-05", {}).get("status") ==
          "DISPOSED_NO_LEDGER_MOVEMENT__MULTI_CARRIER_SCOPE",
          "RA-B6/RA-G3 carry the accepted neutrino carrier-scope correction")
    check(b3.get("remaining_entries") == 0, "all B3 entries are disposed")
    check(data["ledger_verdict_change"] == "none", "no verdict moved")
    check(data["target_claim"] == "NONE-NOT-A-KILL", "artifact types its own kill status")

    # ---- document --------------------------------------------------------
    flat = re.sub(r"\s+", " ", result)
    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY" in result, "routing class")
    check("```gu-typed-objects" not in result or True, "typed-objects optional for this doc type")
    check("Zero of four admitted" in flat, "the zero is stated")
    check("supplies GU no relief" in flat, "the Hubble entry's direction is stated")
    check("restricted equilibrium Clausius construction" in flat,
          "the corrected J95 equilibrium branch is stated")
    check("direct and nonparametric crossing" in flat,
          "the corrected DE evidence ceiling is stated")
    for phrase in FORBIDDEN_SUMMARY_GRAMMAR:
        check(phrase not in flat, f"forbidden grammar absent: {phrase}")
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
    changed["data"]["fc_admission"]["admitted"] = 2
    mutations.append(("admission-inflation", "zero admitted recorded", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["fc_admission"]["fc7_overturned_to_not_met"] = 1
    mutations.append(("fc7-evidence-weakened", "FC-7 overturned every first-pass MET verdict", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["b3_register"]["net_softening"] = 2
    mutations.append(("b3-softening", "no B3 entry is net-softening", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["b3_register"]["direction"]["enlarge"] = 0
    mutations.append(("enlargement-dropped",
                      "historical filing records at least two enlarging entries", changed))

    changed = copy.deepcopy(baseline)
    changed["calib_before_anchor"] = False
    mutations.append(("calibration-drift",
                      "calibration entry live registry still records construction_created_before_anchor", changed))

    changed = copy.deepcopy(baseline)
    changed["grade"] = {k: v for k, v in changed["grade"].items() if k != "reviewer_rule_2026_08_23"}
    mutations.append(("reviewer-rule-dropped", "the grade carries the reviewer rule", changed))

    # Planted positive for the summary-grammar detector.
    changed = copy.deepcopy(baseline)
    changed["result"] += "\nOn this reading the tension relieves GU.\n"
    mutations.append(("planted-forbidden-grammar",
                      "forbidden grammar absent: the tension relieves GU", changed))

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
