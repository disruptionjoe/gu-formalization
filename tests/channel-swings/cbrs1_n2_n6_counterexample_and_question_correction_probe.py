#!/usr/bin/env python3
"""Exact regression probe for the CBRS-1 N2/N6 question correction."""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/cbrs1-n2-n6-counterexample-and-question-correction.json"
RESULT = ROOT / "explorations/conditional-build/cbrs1-n2-n6-counterexample-and-question-correction-2026-08-23.md"
I_REGISTRY = ROOT / "lab/process/selected-k77-cbrs1i-chiral-null-point-class.json"
J_REGISTRY = ROOT / "lab/process/selected-k77-cbrs1j-complete-tangent.json"
NECESSITY = ROOT / "lab/process/cbrs1-owner-necessity-theorem.json"
NECESSITY_RESULT = ROOT / "explorations/conditional-build/cbrs1-owner-necessity-theorem-2026-08-23.md"
CURRENT = ROOT / "CURRENT-STATE.yaml"
NEXT = ROOT / "NEXT-STEPS.md"
AGENDA = ROOT / "lab/process/RESEARCH-AGENDA.json"


def load_inputs() -> dict[str, object]:
    return {
        "registry": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "i": json.loads(I_REGISTRY.read_text()),
        "j": json.loads(J_REGISTRY.read_text()),
        "necessity": json.loads(NECESSITY.read_text()),
        "necessity_result": NECESSITY_RESULT.read_text(),
        "current": CURRENT.read_text(),
        "next": NEXT.read_text(),
        "agenda": json.loads(AGENDA.read_text()),
    }


def collect_failures(inputs: dict[str, object]) -> tuple[int, list[str]]:
    failures: list[str] = []
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    r = inputs["registry"]
    text = inputs["result"]
    i = inputs["i"]
    j = inputs["j"]
    necessity = inputs["necessity"]
    necessity_text = inputs["necessity_result"]
    current = inputs["current"]
    next_steps = inputs["next"]
    agenda = inputs["agenda"]
    assert isinstance(r, dict) and isinstance(i, dict) and isinstance(j, dict)
    assert isinstance(necessity, dict) and isinstance(agenda, dict)
    assert all(isinstance(x, str) for x in (text, necessity_text, current, next_steps))

    # Live CBRS-1I counterexample, not copied prose.
    check(i["frozen_class"]["target_blind"] is True, "CBRS-1I remains target-blind")
    check(len(i["branches"]) == 2, "CBRS-1I retains both nonzero branches")
    for sign in ("minus", "plus"):
        row = i["branches"][sign]["intrinsic_metric_row"]
        check(len(row) == 10 and set(row) == {"0"}, f"CBRS-1I {sign} intrinsic metric row is exactly zero")
        check(i["branches"][sign]["translation_support"] == 0, f"CBRS-1I {sign} translation support is zero")
        check(i["branches"][sign]["spin_grade_two_support"] == 0, f"CBRS-1I {sign} Spin owner support is zero")
    check("INTRINSIC_METRIC_STATIONARITY_PASS" in i["point_class_status"], "CBRS-1I point system includes N2")
    check(i["global_vacuum_status"].startswith("OPEN"), "CBRS-1I global ceiling remains open")

    # Live CBRS-1J downstream N3 obstruction.
    check(j["frozen_class"]["target_blind"] is True, "CBRS-1J same class remains target-blind")
    check(j["frozen_class"]["pointwise_metric_stationary"] is True, "CBRS-1J same class remains metric-stationary")
    h = j["complete_hessian"]
    check(h["dimension"] == 230650 and h["dimension_coverage"] == 230650, "CBRS-1J covers the complete tangent")
    check(h["minus_sign_rank"] == h["dimension"] and h["minus_sign_nullity"] == 0, "CBRS-1J minus Hessian is full rank")
    check(h["plus_sign_rank"] == h["dimension"] and h["plus_sign_nullity"] == 0, "CBRS-1J plus Hessian is full rank")
    p = j["primitive_and_symbol"]
    check(p["complete_field_kernel_dimension"] == 0, "CBRS-1J complete field kernel is zero")
    check(p["primitive_quotient_dimension"] == 0, "CBRS-1J primitive quotient is zero")
    check(p["first_symbol_domain_dimension"] == 0, "CBRS-1J first-symbol domain is zero")

    # Logical result and honest genericity boundary.
    check(r["logical_result"]["verdict"] == "REFUTED_BY_EXISTING_COUNTEREXAMPLE", "universal N2/N6 incompatibility is refuted")
    check(r["logical_result"]["counterexample"] == "CBRS-1I", "counterexample identity is pinned")
    check(r["genericity_audit"]["universal_reading"] == "REFUTED", "universal reading stays refuted")
    check(r["genericity_audit"]["open_dense_or_measure_one_reading"] == "UNDEFINED", "mathematical genericity stays undefined")
    check(len(r["genericity_audit"]["missing_structures"]) >= 4, "missing genericity structures are explicit")
    check(r["corrected_target"]["minimum_surviving_conjunction"] == ["N2", "N3", "N6"], "minimum surviving conjunction is N2-N3-N6")
    check(r["corrected_target"]["full_packet"] == ["N1", "N2", "N3", "N4", "N5", "N6"], "full necessity packet is preserved")
    check("FC-1-through-FC-7" in r["corrected_target"]["method_boundary"] and "B1-B4" in r["corrected_target"]["method_boundary"], "corrected target obeys the fitting-construction method")
    check(r["corrected_target"]["necessity_not_sufficiency"] is True, "necessity is not sufficiency")
    check(r["target_claim"] == "NONE-NOT-A-KILL", "internal correction is not a source kill")
    check(all(r[k] == "none" for k in ("ledger_verdict_change", "claim_status_change", "source_ownership_change", "canon_verdict_change", "public_posture_change")), "no scientific status boundary moves")

    # Correction propagation.
    tension = necessity["n2_n6_tension"]
    check(tension["status"].startswith("UNIVERSAL_INCOMPATIBILITY_REFUTED"), "necessity registry carries the correction")
    check(tension["counterexample"] == "CBRS-1I", "necessity registry names the counterexample")
    check(necessity["corrected_open_question"]["minimum_conjunction"] == ["N2", "N3", "N6"], "necessity registry carries corrected target")
    combined = re.sub(r"\s+", " ", "\n".join((text, necessity_text, current, next_steps)))
    check("universal N2/N6 incompatibility is refuted" in combined, "public owner surfaces state the logical correction")
    check("N2 AND N3 AND N6" in combined or "N2 ∧ N3 ∧ N6" in combined, "owner surfaces state the corrected conjunction")
    check("GU-COMPARATOR-ROUTING" in text and "GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY" in text, "new artifact carries comparator routing")
    check("```gu-typed-objects" in text, "new artifact carries typed objects")

    # A missing work item must fail these checks, not crash the harness
    # (probe_authorship_lint L1).
    item = next((x for x in agenda["work_items"]
                 if x["id"] == "CONDITIONAL-BUILD-REVERSE-SCAFFOLD"), {})
    check("decide N2 AND N3 AND N6" in item.get("priority_sequence", [""])[0]
          and "FC-1-through-FC-7" in item.get("priority_sequence", [""])[0],
          "agenda priority is corrected and method-bounded")
    check("CBRS-1I" in item.get("latest_result", "") and "CBRS-1J" in item.get("latest_result", ""),
          "agenda latest result binds both witnesses")

    # Claim-form detector: quoted/rejected uses are allowed, live directives are not.
    forbidden_live = (
        "the lane's live target is to prove or refute that N2 and N6 are generically incompatible",
        "The next construction target remains the CBRS-1 N2/N6 generic-incompatibility question",
        "It is: prove or refute that `N2 ∧ N6` is generically unsatisfiable.",
    )
    for phrase in forbidden_live:
        check(phrase not in "\n".join((necessity_text, current, next_steps)), f"superseded live directive absent: {phrase}")
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
    changed["i"]["frozen_class"]["target_blind"] = False
    mutations.append(("counterexample-owner", "CBRS-1I remains target-blind", changed))

    changed = copy.deepcopy(baseline)
    changed["i"]["branches"]["minus"]["intrinsic_metric_row"][3] = "1"
    mutations.append(("counterexample-metric", "CBRS-1I minus intrinsic metric row is exactly zero", changed))

    changed = copy.deepcopy(baseline)
    changed["j"]["complete_hessian"]["plus_sign_nullity"] = 1
    mutations.append(("n3-obstruction", "CBRS-1J plus Hessian is full rank", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["genericity_audit"]["open_dense_or_measure_one_reading"] = "PROVED"
    mutations.append(("genericity-smuggle", "mathematical genericity stays undefined", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["corrected_target"]["minimum_surviving_conjunction"] = ["N2", "N6"]
    mutations.append(("old-target-restored", "minimum surviving conjunction is N2-N3-N6", changed))

    changed = copy.deepcopy(baseline)
    changed["necessity"]["n2_n6_tension"]["status"] = "OPEN__NOT_ANSWERED_BY_THE_CORPUS"
    mutations.append(("necessity-drift", "necessity registry carries the correction", changed))

    changed = copy.deepcopy(baseline)
    changed["next"] += "\nThe next construction target remains the CBRS-1 N2/N6 generic-incompatibility question\n"
    mutations.append(("planted-stale-directive", "superseded live directive absent: The next construction target remains the CBRS-1 N2/N6 generic-incompatibility question", changed))

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
