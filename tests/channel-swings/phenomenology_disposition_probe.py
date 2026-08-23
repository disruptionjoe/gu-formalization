#!/usr/bin/env python3
"""Probe for the FITTING_CONSTRUCTION grade and the phenomenology disposition rule.

These two methods exist to stop the program discarding legitimate conditional
work and to stop it returning to the source action early. The checks therefore
enforce the two properties that make them non-laundering: the grade is barred
from ledger movement and prediction credit, and the deferred bucket cannot be
selected while workable buckets remain.
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GRADE_REG = ROOT / "lab/process/fitting-construction-grade.json"
GRADE_DOC = ROOT / "lab/methods/fitting-construction-grade.md"
DISP_REG = ROOT / "lab/process/phenomenology-disposition-and-exhaustion-rule.json"
DISP_DOC = ROOT / "lab/methods/phenomenology-disposition-and-exhaustion-rule.md"
POSTURE = ROOT / "RESEARCH-POSTURE.md"

EXPECTED_FC = ["FC-1", "FC-2", "FC-3", "FC-4", "FC-5", "FC-6"]
EXPECTED_BUCKETS = ["B1", "B2", "B3", "B4"]

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "this counts as a derivation",
    "GU is confirmed",
    "prediction credit is awarded",
    "compatibility establishes",
)


def load_inputs() -> dict[str, object]:
    return {
        "grade": json.loads(GRADE_REG.read_text()),
        "grade_doc": GRADE_DOC.read_text(),
        "disp": json.loads(DISP_REG.read_text()),
        "disp_doc": DISP_DOC.read_text(),
        "posture": POSTURE.read_text(),
    }


def collect_failures(inputs: dict[str, object]) -> tuple[int, list[str]]:
    failures: list[str] = []
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    grade = inputs["grade"]
    grade_doc = inputs["grade_doc"]
    disp = inputs["disp"]
    disp_doc = inputs["disp_doc"]
    posture = inputs["posture"]
    assert isinstance(grade, dict) and isinstance(disp, dict)
    assert all(isinstance(s, str) for s in (grade_doc, disp_doc, posture))

    gd_flat = re.sub(r"\s+", " ", grade_doc)
    dd_flat = re.sub(r"\s+", " ", disp_doc)

    # ---- the grade sits where it claims to sit ---------------------------
    g = grade["grade"]
    check(g["token"] == "FITTING_CONSTRUCTION", "grade token")
    check(g["sits_below"] == "conditional" and g["sits_above"] == "speculative",
          "grade is placed between conditional and speculative")
    check("a derivation" in g["is_not"] and "a prediction" in g["is_not"],
          "grade disclaims derivation and prediction")

    # ---- all six admission criteria, each with a requirement -------------
    crit = {c["id"]: c for c in grade["admission_criteria"]}
    check(list(crit) == EXPECTED_FC, "six admission criteria in order")
    for cid in EXPECTED_FC:
        check(len(crit.get(cid, {}).get("requirement", "")) > 60,
              f"{cid} states a substantive requirement")
    check("fingerprint" in crit.get("FC-1", {}).get("requirement", ""), "FC-1 demands the structure fingerprint")
    check("NAMED" in crit.get("FC-3", {}).get("requirement", "") or "named" in crit.get("FC-3", {}).get("requirement", ""),
          "FC-3 demands a named search")
    check("polarity" in crit.get("FC-4", {}).get("requirement", ""), "FC-4 respects claim polarity")
    check("not a pathway" in crit.get("FC-5", {}).get("requirement", ""),
          "FC-5 forbids the degenerate source-action pathway")
    check("demotion" in crit.get("FC-6", {}).get("requirement", "") or "drops to" in crit.get("FC-6", {}).get("requirement", ""),
          "FC-6 makes the grade revocable")

    # ---- the anti-laundering bars are present and specific ---------------
    bars = " ".join(grade["explicitly_not_licensed"])
    check("compatibility as derivation" in bars, "compatibility-as-derivation barred")
    check("prediction or confirmation credit" in bars, "prediction credit barred")
    check("toward SAME" in bars, "ledger movement toward SAME barred")
    check("target fitting" in bars.lower(), "target fitting barred")
    check(len(grade["anti_laundering_features"]) >= 4, "anti-laundering features enumerated")

    # The posture's forbidden move must still stand unrelaxed.
    check("compatibility_as_derivation" in posture, "posture still forbids compatibility as derivation")
    check("compatibility as derivation, which RESEARCH-POSTURE.md lists among the forbidden moves"
          in " ".join(grade["explicitly_not_licensed"]),
          "grade explicitly defers to the posture's forbidden move")

    # ---- the four buckets and the exhaustion rule ------------------------
    buckets = {b["id"]: b for b in disp["buckets"]}
    check(list(buckets) == EXPECTED_BUCKETS, "four buckets in order")
    check(buckets.get("B2", {}).get("deferred") is True, "B2 is the deferred bucket")
    check(all(buckets.get(b, {}).get("deferred") is False for b in ("B1", "B3", "B4")),
          "B1, B3 and B4 are workable now")
    rule = disp["exhaustion_rule"]
    check("may not select" in rule["statement"] or "Do not return" in rule["statement"],
          "the exhaustion rule is stated as a prohibition")
    check("B1" in rule["statement"] and "B3" in rule["statement"] and "B4" in rule["statement"],
          "the rule names the buckets that must be exhausted first")
    check(len(rule.get("reasons", [])) >= 2, "the ordering is justified, not asserted")
    check("exhausted" in rule.get("definition_of_exhausted", "").lower()
          or "attempted" in rule.get("definition_of_exhausted", ""),
          "exhausted is defined")

    # ---- disposition discipline prevents each bucket becoming an excuse --
    disc = {d["bucket"]: d for d in disp["disposition_discipline"]}
    check("named requirement" in disc.get("B2", {}).get("requires", ""), "B2 requires a named requirement")
    check("citation" in disc.get("B3", {}).get("requires", "") or "cite" in disc.get("B3", {}).get("requires", ""),
          "B3 requires an external citation")
    check("SC-" in disc.get("B4", {}).get("requires", "") or "source locus" in disc.get("B4", {}).get("requires", ""),
          "B4 requires the source locus")
    check(disp["revisable"] is True, "dispositions are revisable")

    # ---- neither method claims to score the program well -----------------
    check("earns no prediction credit" in dd_flat or "moves no ledger row" in dd_flat,
          "disposition doc disclaims scoring")
    check("does not excuse GU" in dd_flat, "B3 does not excuse GU")
    check("not a way to score the program well" in dd_flat, "the scheme disclaims being a scoreboard")

    # ---- doc/registry agreement ------------------------------------------
    for cid in EXPECTED_FC:
        check(f"**{cid}" in grade_doc, f"{cid} appears in the method doc")
    for bid in EXPECTED_BUCKETS:
        check(f"**{bid} " in disp_doc, f"{bid} appears in the method doc")
    check("FITTING_CONSTRUCTION" in dd_flat, "disposition doc names the grade it banks into")
    check("fitting-construction-grade.md" in dd_flat, "disposition doc links the grade method")

    check(grade["ledger_verdict_change"] == "none", "grade moves no verdict")
    check(disp["ledger_verdict_change"] == "none", "disposition moves no verdict")

    for phrase in FORBIDDEN_SUMMARY_GRAMMAR:
        check(phrase not in gd_flat, f"grade doc: forbidden grammar absent: {phrase}")
        check(phrase not in dd_flat, f"disposition doc: forbidden grammar absent: {phrase}")
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
    changed["grade"]["explicitly_not_licensed"] = ["nothing in particular"]
    mutations.append(("bars-removed", "compatibility-as-derivation barred", changed))

    changed = copy.deepcopy(baseline)
    changed["grade"]["grade"]["sits_below"] = "repository-derived"
    mutations.append(("grade-inflation", "grade is placed between conditional and speculative", changed))

    changed = copy.deepcopy(baseline)
    changed["grade"]["admission_criteria"] = [
        c for c in changed["grade"]["admission_criteria"] if c["id"] != "FC-5"]
    mutations.append(("pathway-criterion-dropped", "six admission criteria in order", changed))

    changed = copy.deepcopy(baseline)
    for c in changed["grade"]["admission_criteria"]:
        if c["id"] == "FC-6":
            c["requirement"] = "the construction is permanent once admitted"
    mutations.append(("irrevocable-grade", "FC-6 makes the grade revocable", changed))

    changed = copy.deepcopy(baseline)
    for b in changed["disp"]["buckets"]:
        if b["id"] == "B2":
            b["deferred"] = False
    mutations.append(("deferral-lifted", "B2 is the deferred bucket", changed))

    changed = copy.deepcopy(baseline)
    changed["disp"]["disposition_discipline"] = [
        {**d, "requires": "nothing"} for d in changed["disp"]["disposition_discipline"]]
    mutations.append(("discipline-gutted", "B2 requires a named requirement", changed))

    # Planted positive for the summary-grammar detector.
    changed = copy.deepcopy(baseline)
    changed["grade_doc"] += "\nOnce admitted, this counts as a derivation.\n"
    mutations.append(("planted-forbidden-grammar",
                      "grade doc: forbidden grammar absent: this counts as a derivation", changed))

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
