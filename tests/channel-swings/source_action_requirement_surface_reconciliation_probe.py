#!/usr/bin/env python3
"""Probe for the source-action requirement-surface reconciliation.

Includes planted-positive controls for the alias detector, because Finding A
is an absence result: corrupting a detector cannot flip an absence, so the
detector's power is demonstrated on synthetic positives and negatives
(VERIFICATION.md probe discipline, rule 4).
"""

from __future__ import annotations

import copy
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/source-action-requirement-surface-reconciliation.json"
RESULT = ROOT / "explorations/conditional-build/source-action-requirement-surface-reconciliation-2026-08-23.md"
SPEC = ROOT / "explorations/source-action-requirements-spec-2026-07-13.md"
MAP = ROOT / "explorations/source-action-constraint-intersection-2026-07-11.md"
SPEC_TEST = ROOT / "tests/spec-consistency/source_action_requirements_consistency.py"
OWNER_LEDGER = ROOT / "lab/process/ext-sm-cosmo-anchors-acceptance-and-descents.json"

ALIASES = ("alpha_W", "c_W", "R^Y", "OQ2", "Willmore")

CITED_ARTIFACTS = (
    "explorations/path4-wave2-alphaW-parameter-free-2026-07-11.md",
    "explorations/W236-gravity-theta-sector-residual-built-action-2026-07-15.md",
    "explorations/W225-gravity-projected-shadow-schwarzschild-cheap-read-2026-07-15.md",
)

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "the map is discredited",
    "GU is falsified",
    "prediction credit is awarded",
    "the over-determination never existed",
)

ROW_RE = re.compile(r'\("(SA-[A-Za-z0-9]+)",\s*"([A-Z]+)"\)')


def alias_hits(text: str) -> set[str]:
    """The detector under test: which coefficient aliases appear."""
    return {a for a in ALIASES if a in text}


def load_inputs() -> dict[str, object]:
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "spec": SPEC.read_text(),
        "map": MAP.read_text(),
        "spec_test": SPEC_TEST.read_text(),
        "owner_ledger": json.loads(OWNER_LEDGER.read_text()),
        "cited_exist": {p: (ROOT / p).exists() for p in CITED_ARTIFACTS},
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
    map_text = inputs["map"]
    spec_test = inputs["spec_test"]
    owner_ledger = inputs["owner_ledger"]
    cited_exist = inputs["cited_exist"]
    assert isinstance(data, dict) and isinstance(owner_ledger, dict) and isinstance(cited_exist, dict)
    assert all(isinstance(s, str) for s in (result, spec, map_text, spec_test))

    # ---- detector power: planted positive and clean negative -------------
    check(alias_hits("a document about spinor bundles and nothing else") == set(),
          "alias detector: clean negative finds nothing")
    check("alpha_W" in alias_hits("the coefficient alpha_W appears here"),
          "alias detector: planted positive fires")
    check("OQ2" in alias_hits("this mentions OQ2-A only"),
          "alias detector: planted alias variant fires")

    # ---- Finding A: the gap is closed -----------------------------------
    check(bool(alias_hits(spec)), "spec now carries the coefficient")
    check("| SA-G10 |" in spec, "SA-G10 row present")
    check("FIT (gated)" in spec, "SA-G10 classed FIT (gated)")
    # Monotonic, not pinned: later swings may legitimately add rows. This probe
    # owns SA-G10 and asserts its repair has not regressed, nothing more.
    inline = re.search(r"(\d+) rows \(SA-G10", spec)
    check(bool(inline) and int(inline.group(1)) >= 28, "spec inline row count at or above the repair")
    title = re.search(r"(\d+) requirement rows: (\d+) FORCED, (\d+) DECLARATION, (\d+) FIT", spec)
    check(bool(title) and int(title.group(1)) >= 28 and int(title.group(4)) >= 11,
          "spec tallies at or above the repair")
    check("ADDENDUM 2026-08-23" in spec, "spec records why the row was missing")

    # Independent recomputation of the tallies from the companion test's own
    # table, cross-checked against the spec's stated numbers.
    rows = ROW_RE.findall(spec_test)
    counts = Counter(cls for _, cls in rows)
    check(len(rows) >= 28, "spec test table at or above the repair")
    check(("SA-G10", "FIT") in rows, "spec test table includes SA-G10 as FIT")
    check(counts["FORCED"] >= 8, "recomputed FORCED tally at or above 8")
    check(counts["DECLARATION"] >= 9, "recomputed DECLARATION tally at or above 9")
    check(counts["FIT"] >= 11, "recomputed FIT tally at or above 11")
    m = re.search(r"len\(TABLE\) == (\d+)", spec_test)
    check(bool(m) and int(m.group(1)) >= 28, "spec test row assertion at or above the repair")
    mf = re.search(r'counts\.get\("FIT"\) == (\d+)', spec_test)
    check(bool(mf) and int(mf.group(1)) >= 11, "spec test FIT assertion at or above the repair")

    fa = data["finding_a_coverage_gap"]
    before, after = fa["repair"]["tally_before"], fa["repair"]["tally_after"]
    check(before["rows"] + 1 == after["rows"], "registry tally arithmetic: rows")
    check(before["FIT"] + 1 == after["FIT"], "registry tally arithmetic: FIT")
    check(before["FORCED"] == after["FORCED"] and before["DECLARATION"] == after["DECLARATION"],
          "registry tally arithmetic: other classes unchanged")
    check(len(rows) >= after["rows"] and counts["FIT"] >= after["FIT"],
          "live table has not regressed below the recorded repair")
    check(fa["repair"]["creates_new_freedom"] is False, "no new freedom claimed")
    check(set(fa["aliases_swept"]) == set(ALIASES), "swept alias set pinned")

    # ---- Finding B: the stale pointer is annotated ------------------------
    map_flat = re.sub(r"\s+", " ", map_text.replace(">", " "))
    check("STALE TARGETING NOTICE" in map_text, "map carries the staleness notice")
    check("[!CAUTION]" in map_text, "notice uses the repository CAUTION pattern")
    check("path4-wave2-alphaW-parameter-free-2026-07-11.md" in map_text, "notice names the sibling result")
    check("W236-gravity-theta-sector-residual-built-action-2026-07-15.md" in map_text,
          "notice names the later result")
    check("co-presence, not a shared number" in map_flat, "notice states the co-presence typing")
    check("W154" in map_flat and "conservative IG branch" in map_flat
          and "imported exact Schwarzschild" in map_flat,
          "notice carries W236's conditions")
    check("gauge-sector over-determination in this map is untouched" in map_flat,
          "notice bounds itself to the theta sector")
    check("Nothing here is a claim that the map was wrong" in map_flat, "notice makes no misconduct claim")
    fb = data["finding_b_stale_target"]
    check(len(fb["bearing_results"]) == 2, "two bearing results registered")
    check(any(r["relation"] == "SAME_DAY_SIBLING" for r in fb["bearing_results"]), "sibling typed")
    check(any(r["relation"] == "LATER_RESULT" for r in fb["bearing_results"]), "later result typed")
    check(len(fb["reopening_conditions"]) >= 2, "reopening conditions recorded")
    check("dissolved" in fb["consequence"], "consequence stated exactly")

    # ---- Finding C: the self-correction ----------------------------------
    owner_c = owner_ledger["consolidated_r1_owner_ledger_v2"]["OWNER-C"]
    check("triangulation_caveat_2026_08_23" in owner_c, "OWNER-C caveat present")
    # A dropped caveat must fail its own check, not crash the harness.
    check("does NOT assert" in owner_c.get("triangulation_caveat_2026_08_23", ""),
          "caveat refuses joint discharge")
    check("SA-G10" in owner_c.get("spec_rows", []), "OWNER-C linked to SA-G10")

    # ---- provenance and ceilings -----------------------------------------
    for path, exists in cited_exist.items():
        check(exists, f"cited artifact exists: {path}")
    check(data["ledger_verdict_change"] == "none", "ledger unchanged")
    check(data["claim_status_change"] == "none", "claim status unchanged")
    check(data["canon_verdict_change"] == "none", "canon unchanged")
    check(data["descent_yield_accounting"]["new_physics_constraint"] == 0,
          "descent yield honestly accounted")

    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("mostly re-description" in result, "honest yield stated in doc")
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
    changed["spec"] = changed["spec"].replace("| SA-G10 |", "| SA-REMOVED |")
    mutations.append(("row-removal", "SA-G10 row present", changed))

    changed = copy.deepcopy(baseline)
    changed["spec_test"] = changed["spec_test"].replace('("SA-G10", "FIT"),', "")
    mutations.append(("test-table-desync", "spec test table includes SA-G10 as FIT", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["finding_a_coverage_gap"]["repair"]["tally_after"]["FIT"] = 10
    mutations.append(("tally-arithmetic-break", "registry tally arithmetic: FIT", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["finding_a_coverage_gap"]["repair"]["creates_new_freedom"] = True
    mutations.append(("freedom-inflation", "no new freedom claimed", changed))

    changed = copy.deepcopy(baseline)
    changed["map"] = changed["map"].replace(
        "gauge-sector over-determination in this map is untouched", "everything in this map falls")
    mutations.append(("notice-overreach", "notice bounds itself to the theta sector", changed))

    changed = copy.deepcopy(baseline)
    changed["map"] = changed["map"].replace("conservative IG", "any")
    mutations.append(("condition-stripping", "notice carries W236's conditions", changed))

    changed = copy.deepcopy(baseline)
    changed["owner_ledger"]["consolidated_r1_owner_ledger_v2"]["OWNER-C"].pop(
        "triangulation_caveat_2026_08_23")
    mutations.append(("self-correction-drop", "OWNER-C caveat present", changed))

    # Planted positive for the absence detector's own failure path.
    changed = copy.deepcopy(baseline)
    changed["result"] += "\nOn reflection the map is discredited.\n"
    mutations.append(("planted-forbidden-grammar", "forbidden grammar absent: the map is discredited", changed))

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
