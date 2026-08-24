#!/usr/bin/env python3
"""Executable gate for the row-complete phenomenology disposition register."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
REGISTER = ROOT / "lab/process/phenomenology-disposition-register-v0.1.json"
METHOD_REG = ROOT / "lab/process/phenomenology-disposition-and-exhaustion-rule.json"
ANCHOR_REG = ROOT / "lab/process/gravitational-anchor-bucket-disposition-and-first-fitting-construction.json"
CHIRAL16_REG = ROOT / "lab/process/chiral16-same-row-disposition-wave.json"
CARRIER_GRAVITY_REG = ROOT / "lab/process/carrier-gravity-row-disposition-wave.json"
B3_REG = ROOT / "lab/process/fc-admission-wave-and-first-b3-register.json"

TERMINAL_OUTCOMES = {
    "FITTING_CONSTRUCTION",
    "PRECISE_IMPOSSIBILITY",
    "B2_NAMED_REQUIREMENT",
}


def load_inputs() -> dict[str, object]:
    ledger_bytes = LEDGER.read_bytes()
    return {
        "ledger": json.loads(ledger_bytes),
        "ledger_sha256": hashlib.sha256(ledger_bytes).hexdigest(),
        "register": json.loads(REGISTER.read_text()),
        "method": json.loads(METHOD_REG.read_text()),
        "anchors": json.loads(ANCHOR_REG.read_text()),
        "chiral16": json.loads(CHIRAL16_REG.read_text()),
        "carrier_gravity": json.loads(CARRIER_GRAVITY_REG.read_text()),
        "b3": json.loads(B3_REG.read_text()),
    }


def collect_failures(inputs: dict[str, object]) -> tuple[int, list[str]]:
    failures: list[str] = []
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    ledger = inputs["ledger"]
    register = inputs["register"]
    method = inputs["method"]
    anchors = inputs["anchors"]
    chiral16 = inputs["chiral16"]
    carrier_gravity = inputs["carrier_gravity"]
    b3 = inputs["b3"]
    assert all(isinstance(value, dict)
               for value in (ledger, register, method, anchors, chiral16, carrier_gravity, b3))

    ledger_ids = [row.get("id") for row in ledger.get("rows", [])]
    denominator_groups = register.get("row_denominator_by_ledger_verdict", {})
    denominator_ids = [row_id for group in denominator_groups.values() for row_id in group]
    check(len(denominator_ids) == len(set(denominator_ids)), "denominator has no duplicate rows")
    check(set(denominator_ids) == set(ledger_ids), "denominator exactly covers current ledger rows")
    currency_current = register.get("ledger_basis", {}).get("sha256") == inputs["ledger_sha256"]
    coverage_current = (len(denominator_ids) == len(set(denominator_ids))
                        and set(denominator_ids) == set(ledger_ids))
    check(currency_current, "ledger digest is current")
    check(register.get("ledger_basis", {}).get("schema_version") == ledger.get("schema_version"),
          "ledger schema version is current")

    terminal_rows = register.get("terminal_row_dispositions", [])
    terminal_ids = [row.get("row_id") for row in terminal_rows]
    check(len(terminal_ids) == len(set(terminal_ids)), "terminal rows are unique")
    check(set(terminal_ids).issubset(set(ledger_ids)), "terminal rows belong to denominator")
    check(all(row.get("terminal_outcome") in TERMINAL_OUTCOMES for row in terminal_rows),
          "terminal rows use closed outcome vocabulary")
    check(all(row.get("evidence_ref") for row in terminal_rows),
          "every terminal row has evidence")
    check(all(row.get("named_requirements") for row in terminal_rows
              if row.get("terminal_outcome") == "B2_NAMED_REQUIREMENT"),
          "terminal B2 rows name requirements")
    check(all(row.get("construction_id") for row in terminal_rows
              if row.get("terminal_outcome") == "FITTING_CONSTRUCTION"),
          "terminal B1 rows name fitting constructions")

    anchor_rows = {row.get("row_id"): row for row in anchors.get("dispositions", [])}
    anchor_fc = {row.get("row_id"): row for row in anchors.get("fitting_constructions", [])}
    chiral_rows = {row.get("row_id"): row for row in chiral16.get("terminal_rows", [])}
    carrier_gravity_rows = {
        row.get("row_id"): row for row in carrier_gravity.get("terminal_rows", [])
    }
    carrier_gravity_fc = {
        row_id: row
        for construction in carrier_gravity.get("fitting_constructions", [])
        for row_id in construction.get("rows", [])
        for row in [construction]
    }
    for row in terminal_rows:
        row_id = row.get("row_id")
        evidence_row = (anchor_rows.get(row_id) or chiral_rows.get(row_id)
                        or carrier_gravity_rows.get(row_id, {}))
        check(bool(evidence_row), f"terminal row evidence resolves: {row_id}")
        check(row.get("bucket") == evidence_row.get("bucket"),
              f"terminal bucket matches evidence: {row_id}")
        if row.get("terminal_outcome") == "FITTING_CONSTRUCTION":
            evidence_fc = anchor_fc.get(row_id) or carrier_gravity_fc.get(row_id, {})
            check(row.get("construction_id") == evidence_fc.get("id"),
                  f"fitting construction matches evidence: {row_id}")
        if row_id in chiral_rows:
            check(row.get("terminal_outcome") == evidence_row.get("terminal_outcome"),
                  f"chiral-16 terminal outcome matches evidence: {row_id}")
            check(row.get("named_requirements") == evidence_row.get("named_requirements"),
                  f"chiral-16 requirements match evidence: {row_id}")
        if row_id in carrier_gravity_rows:
            check(row.get("terminal_outcome") == evidence_row.get("terminal_outcome"),
                  f"carrier/gravity terminal outcome matches evidence: {row_id}")
            for field in ("construction_id", "named_requirements", "impossibility_id"):
                if field in evidence_row:
                    check(row.get(field) == evidence_row.get(field),
                          f"carrier/gravity {field} matches evidence: {row_id}")

    sub = register.get("b3_subdispositions", {})
    completed = sub.get("completed", [])
    pending = sub.get("pending", [])
    pending_ids = {row.get("id") for row in pending}
    completed_ids = {row.get("id") for row in completed}
    b3_data = b3.get("b3_register", {})
    filed_ids = set(b3_data.get("ids", []))
    disposed_ids = set(b3_data.get("dispositions", {}))
    check(completed_ids == disposed_ids, "completed B3 units match source register")
    check(pending_ids == filed_ids - disposed_ids, "pending B3 units are derived")
    check(all(row.get("parent_row") in ledger_ids for row in completed),
          "completed B3 units retain parent rows")
    pending_parentage_complete = all(row.get("parent_row") in ledger_ids for row in pending)
    check(all(row.get("scope_effect") == "SUBDISPOSITION_ONLY__PARENT_ROW_REMAINS_OPEN"
              for row in completed), "B3 subdispositions do not launder row terminals")
    check(all(row.get("parent_row") not in terminal_ids for row in completed),
          "completed B3 parent rows remain nonterminal")

    open_ids = set(ledger_ids) - set(terminal_ids)
    open_cohort_ids = {
        row_id
        for cohort in register.get("open_row_cohorts", [])
        for row_id in cohort.get("row_ids", [])
    }
    check(open_cohort_ids == open_ids, "open cohorts exactly cover nonterminal rows")

    evaluation = register.get("exhaustion_evaluation", {})
    all_rows_terminal = not open_ids
    all_split_units_terminal = not pending
    derived_exhausted = (
        all_rows_terminal
        and all_split_units_terminal
        and pending_parentage_complete
        and currency_current
        and coverage_current
    )
    check(evaluation.get("ledger_currency") is currency_current, "currency predicate is derived")
    check(evaluation.get("exact_row_coverage") is coverage_current, "coverage predicate is derived")
    check(evaluation.get("split_unit_parentage") is pending_parentage_complete,
          "split parentage predicate is derived")
    check(evaluation.get("denominator_rows") == len(ledger_ids), "denominator count is derived")
    check(evaluation.get("terminal_rows") == len(terminal_ids), "terminal count is derived")
    check(evaluation.get("open_rows") == len(open_ids), "open count is derived")
    check(evaluation.get("completed_b3_subdispositions") == len(completed),
          "completed B3 count is derived")
    check(evaluation.get("pending_b3_subdispositions") == len(pending_ids),
          "pending B3 count is derived")
    check(evaluation.get("all_rows_terminal") is all_rows_terminal,
          "row terminality predicate is derived")
    check(evaluation.get("all_required_split_units_terminal") is all_split_units_terminal,
          "split terminality predicate is derived")
    check(evaluation.get("exhausted") is derived_exhausted, "exhaustion state is derived")
    check(evaluation.get("b2_selectable") is derived_exhausted, "B2 eligibility follows exhaustion")

    live_ref = method.get("live_disposition_register")
    check(live_ref == str(REGISTER.relative_to(ROOT)), "method points to live register")
    rule = method.get("exhaustion_rule", {})
    check(set(rule.get("terminal_outcomes", [])) == TERMINAL_OUTCOMES,
          "method and register share terminal vocabulary")
    check("stale" in rule.get("fail_closed_rule", "")
          and "b2_selectable false" in rule.get("fail_closed_rule", ""),
          "method fails closed on stale or incomplete state")
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
    first_group = changed["register"]["row_denominator_by_ledger_verdict"]["SAME"]
    first_group.pop()
    mutations.append(("row-omitted", "denominator exactly covers current ledger rows", changed))

    changed = copy.deepcopy(baseline)
    first_group = changed["register"]["row_denominator_by_ledger_verdict"]["SAME"]
    first_group.append(first_group[0])
    mutations.append(("row-duplicated", "denominator has no duplicate rows", changed))

    changed = copy.deepcopy(baseline)
    changed["register"]["ledger_basis"]["sha256"] = "stale"
    mutations.append(("ledger-stale", "ledger digest is current", changed))

    changed = copy.deepcopy(baseline)
    changed["register"]["exhaustion_evaluation"]["exhausted"] = True
    mutations.append(("false-exhaustion", "exhaustion state is derived", changed))

    changed = copy.deepcopy(baseline)
    changed["register"]["b3_subdispositions"]["completed"][0]["scope_effect"] = "ROW_TERMINAL"
    mutations.append(("b3-row-laundering", "B3 subdispositions do not launder row terminals", changed))

    changed = copy.deepcopy(baseline)
    for row in changed["register"]["terminal_row_dispositions"]:
        if row.get("terminal_outcome") == "B2_NAMED_REQUIREMENT":
            row["named_requirements"] = []
            break
    mutations.append(("unnamed-b2", "terminal B2 rows name requirements", changed))

    changed = copy.deepcopy(baseline)
    changed["register"]["terminal_row_dispositions"][0]["evidence_ref"] = ""
    mutations.append(("terminal-without-evidence", "every terminal row has evidence", changed))

    ok = True
    for name, expected, mutated in mutations:
        _, caught = collect_failures(mutated)
        if expected not in caught:
            print(f"[FAIL] mutation {name}: expected {expected!r}, got {caught!r}")
            ok = False
        else:
            print(f"MUTATION CAUGHT {name}: [FAIL] {expected}")
    print("FAILURE-PATH SELFTEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
