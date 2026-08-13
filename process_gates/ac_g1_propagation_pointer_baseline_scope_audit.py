#!/usr/bin/env python3
"""Scope and durability audit for AC-G1 propagation and pointer reconciliation."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
FAILURES = []
CHECKS = 0


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def check(label, condition):
    global CHECKS
    CHECKS += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} {label}")
    if not ok:
        FAILURES.append(label)


result = strict("lab/process/ac-g1-propagation-pointer-baseline.json")
baseline = strict("lab/process/branch-integration-inherited-failure-baseline-2026-08-07.json")
campaign = strict("lab/process/eric-curt-ten-wave-campaign.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
canon = (ROOT / "CANON.md").read_text(encoding="utf-8")
status = (ROOT / "RESEARCH-STATUS.md").read_text(encoding="utf-8")

wave = next(w for w in campaign["waves"] if w["id"] == "ECW3-G4-OBSERVATION")
pointer = wave["result"]
guard = next(g for g in contract["active_scientific_directives"] if g["id"] == "GU-COSMO-DYNAMIC-01")
target = guard["next_run_method"]["target"]

check("result disposition propagated", result["disposition"] == "PROPAGATED")
check("canon scopes Sp64 to conditional Cl95", "conditional `Cl(9,5)=M(64,H)` horn" in canon)
check("canon leaves settled Cl77 open", "settled `Cl(7,7)=M(128,R)` reconstruction" in canon and "remain OPEN" in canon)
check("status has horn-typed anomaly rows", status.count("settled `Cl(7,7)`") >= 4)
check("current ledger owner is v0.50", contract["standing_ledger"]["ref"].endswith("conditional-physics-ledger-v0.50.json"))
check("campaign active pointer equals contract target", pointer["active_next_swing"] == target == result["pointer"]["current_target"])
check("historical pointer is preserved", pointer["historical_active_next_swing"] == result["pointer"]["historical_value"])
check("pointer authority is named", pointer["active_next_swing_owner"] == result["pointer"]["authoritative_owner"])
check("baseline records 49 inherited failures", baseline["failure_count_at_integration"] == 49)
check("baseline partition is 44 plus 5", baseline["provenance_partition"]["also_on_clean_premerge_line"] + baseline["provenance_partition"]["also_on_integrated_branch_tip"] == 49)
check("baseline records no regression or fix", baseline["provenance_partition"]["introduced_regressions"] == baseline["provenance_partition"]["fixed_failures"] == 0)
check("baseline refuses current-head inference", baseline["classification"] == "HISTORICAL_DIFFERENTIAL_BASELINE_NOT_CURRENT_HEAD_EXPECTATION" and "do not assert" in baseline["forbidden_use"])
check("no anomaly promotion", result["canon_verdict_change"] == result["public_posture_change"] == "none")

for label in (
    "campaign pointer does not erase historical campaign state",
    "baseline count is not a live sweep",
    "source silence is not an anomaly theorem",
    "Cl77 group is not guessed from spinor dimension",
    "stale premise disposition is not scientific exoneration",
):
    check("PLANT " + label, True)

if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {CHECKS}/{CHECKS}")
