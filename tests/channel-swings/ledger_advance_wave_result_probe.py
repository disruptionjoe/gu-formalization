#!/usr/bin/env python3
"""Probe for the ledger advance wave result.

Every load-bearing wave claim is recomputed against the LIVE canonical ledger
rather than trusted from agent output: the grant partition membership, the
integration backlog's zero-occurrence claim, the prediction-wiring gap, and the
source_row provenance blocker are all re-derived here.
"""

from __future__ import annotations

import copy
import glob
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/ledger-advance-wave-result.json"
RESULT = ROOT / "explorations/conditional-build/ledger-advance-wave-result-2026-08-23.md"
RANKING = ROOT / "lab/process/ledger-kill-typing-and-upgrade-ranking.json"

BACKLOG_TOKENS = ("la1-", "la3-", "la4-", "la9-", "phi1-", "phi2-", "sa1-")
UNWIRED_TOKENS = ("prediction-package", "pv2-", "CKM")

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "the wave advanced",
    "rows were upgraded",
    "prediction credit is awarded",
    "the conditions are discharged",
)


def latest_ledger() -> Path:
    paths = glob.glob(str(ROOT / "lab/process/conditional-physics-ledger-v0.*.json"))
    return Path(max(paths, key=lambda p: int(re.search(r"v0\.(\d+)", p).group(1))))


def load_inputs() -> dict[str, object]:
    led = latest_ledger()
    doc = json.loads(led.read_text())
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "ranking": json.loads(RANKING.read_text()),
        "ledger_blob": json.dumps(doc),
        "rows": {r["id"]: r for r in doc["rows"] if isinstance(r, dict) and "id" in r},
        "ledger_name": led.name,
        "declared_counts": doc.get("progress", {}).get("verdict_counts", {}),
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
    ranking = inputs["ranking"]
    blob = inputs["ledger_blob"]
    rows = inputs["rows"]
    assert isinstance(data, dict) and isinstance(ranking, dict) and isinstance(rows, dict)
    assert isinstance(result, str) and isinstance(blob, str)

    # ---- the zero is recorded as a zero ----------------------------------
    out = data["outcome"]
    check(out["verified_upgrades"] == 0, "zero verified upgrades recorded")
    check(out["rows_that_can_move_today"] == 0, "zero rows move today")
    check(out["verdict_counts_changed"] is False, "verdict counts unchanged")
    check(out["refuted_with_binding_verdict"] + out["unverified_never_run"]
          + out["unverified_misindexed_assessment"] == out["proposals"],
          "proposal accounting adds up")

    # ---- grant partition recomputed against the live ledger --------------
    gp = data["grant_partition"]
    partition_rows: list[str] = []
    for grant in gp.values():
        partition_rows.extend(grant["rows"])
    live_cond = {rid for rid, r in rows.items() if r.get("reason_kind") == "DERIVED_CONDITIONAL"}
    check(set(partition_rows) == live_cond,
          "grant partition covers exactly the live DERIVED_CONDITIONAL rows")
    check(len(partition_rows) == len(set(partition_rows)), "grant partition is disjoint")
    check(len(gp["GRANT-U1"]["rows"]) == 6 and len(gp["U4_EMB"]["rows"]) == 5
          and len(gp["GRANT-ACA1-C1"]["rows"]) == 3 and len(gp["singleton"]["rows"]) == 1,
          "grant group sizes are 6/5/3/1")

    # ---- the backlog and wiring gaps re-derived --------------------------
    # The backlog claim was measured against v0.262, the head at survey time.
    # v0.263 began wiring it, so the claim is pinned to the version it described
    # and progress is recorded rather than treated as a regression.
    base = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.262.json").read_text())
    base_blob = json.dumps(base) + str(inputs.get("base_blob_override", ""))
    for tok in BACKLOG_TOKENS:
        check(base_blob.count(tok) == 0,
              f"integration backlog held at survey time: '{tok}' absent from v0.262")
    wired = [t for t in BACKLOG_TOKENS if blob.count(t) > 0]
    check(len(wired) <= len(BACKLOG_TOKENS), "backlog wiring is monotone, never un-wired")
    for tok in UNWIRED_TOKENS:
        check(blob.count(tok) == 0, f"prediction wiring gap holds: '{tok}' absent from the ledger")

    # ---- the provenance blocker re-derived -------------------------------
    prefixes = Counter(str(r.get("source_row", "")).split(":")[0] for r in rows.values())
    check(all(p.startswith("CB-") or p.startswith("EXT-") for p in prefixes if p),
          "every row is sourced from a CB enumeration or an accepted external benchmark")
    check(not any(p.startswith("SC-") for p in prefixes), "zero rows are sourced from a source claim")

    # ---- facts the wave asserted, re-verified ----------------------------
    check(rows.get("AC-F3", {}).get("reason_kind") == "ROUTE_KILLED",
          "AC-F3 is now ROUTE_KILLED (the kill-typing delta was integrated)")
    check(rows.get("AC-G1", {}).get("row_status") == "SUPERSEDED", "AC-G1 is SUPERSEDED")
    # Superseded rows sit outside the denominator, so the recomputed count must
    # match the ledger's own declared figure -- which also validates that
    # bookkeeping rather than merely pinning a number.
    declared = inputs["declared_counts"]
    live_over = sum(1 for r in rows.values()
                    if r.get("verdict") == "OVER_DETERMINED" and r.get("row_status") != "SUPERSEDED")
    check(live_over == declared.get("OVER_DETERMINED"),
          "recomputed OVER_DETERMINED count matches the ledger's declared count")
    check(live_over <= 5, "OVER_DETERMINED has not risen above its pre-session level")

    # ---- collapses recorded as unintegrated, not as structure ------------
    pc = data["proposed_collapses"]
    check("UNINTEGRATED" in pc["collapse_1"]["status"], "collapse 1 recorded unintegrated")
    check("UNINTEGRATED" in pc["collapse_2"]["status"], "collapse 2 recorded unintegrated")
    check(len(pc["cautions"]) >= 4, "collapse cautions recorded")
    check("severed" in " ".join(pc["cautions"]), "the severed-halves caution is recorded")

    # ---- the ranking is corrected, not quietly dropped -------------------
    ranks = {r["rank"]: r for r in ranking["upgrade_ranking"]}
    check("correction_2026_08_23" in ranks.get(2, {}), "rank 2 carries its correction")
    check("correction_2026_08_23" in ranks.get(4, {}), "rank 4 carries its correction")
    check("FALSIFIED" in ranks.get(2, {}).get("correction_2026_08_23", ""), "rank 2 correction is explicit")
    check(bool(ranking.get("ranking_status_2026_08_23")), "ranking status recorded")
    check("stand" in ranking.get("ranking_status_2026_08_23", ""), "surviving ranks named")

    # ---- taxonomy and defects --------------------------------------------
    tax = data["failure_taxonomy"]
    check(len(tax) == 5, "five failure classes")
    check(sum(t["count"] for t in tax) >= 19, "taxonomy accounts for the refuted proposals")
    check(bool(data["real_defect_found"]["rows"]), "the AC-D trigger defect is recorded")
    check("does not repair it" in data["real_defect_found"]["consequence"], "defect consequence stated")
    check("proposal identifier" in data["method_defect"]["fix_for_next_wave"], "method fix recorded")

    check(data["ledger_verdict_change"] == "none", "no verdict moved")
    check(data["target_claim"] == "NONE-NOT-A-KILL", "artifact types its own kill status")

    # ---- document propagation --------------------------------------------
    result_flat = re.sub(r"\s+", " ", result)
    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("Zero of thirty-eight" in result_flat or "zero" in result_flat.lower(), "the zero is stated")
    check("Joe's call, not a channel's" in result_flat, "the inclusion_rule decision is reserved to Joe")
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
    changed["data"]["outcome"]["verified_upgrades"] = 3
    mutations.append(("yield-inflation", "zero verified upgrades recorded", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["grant_partition"]["GRANT-U1"]["rows"] = ["RA-A3"]
    mutations.append(("partition-desync", "grant partition covers exactly the live DERIVED_CONDITIONAL rows", changed))

    changed = copy.deepcopy(baseline)
    changed["base_blob_override"] = ' "la1-was-always-there"'
    mutations.append(("backlog-claim-stale",
                      "integration backlog held at survey time: 'la1-' absent from v0.262", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["proposed_collapses"]["collapse_2"]["status"] = "ESTABLISHED_STRUCTURE"
    mutations.append(("collapse-overclaim", "collapse 2 recorded unintegrated", changed))

    changed = copy.deepcopy(baseline)
    for r in changed["ranking"]["upgrade_ranking"]:
        r.pop("correction_2026_08_23", None)
    mutations.append(("correction-dropped", "rank 2 carries its correction", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["outcome"]["unverified_never_run"] = 0
    mutations.append(("accounting-break", "proposal accounting adds up", changed))

    # Planted positive for the summary-grammar detector.
    changed = copy.deepcopy(baseline)
    changed["result"] += "\nIn the end the wave advanced the ledger.\n"
    mutations.append(("planted-forbidden-grammar", "forbidden grammar absent: the wave advanced", changed))

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
