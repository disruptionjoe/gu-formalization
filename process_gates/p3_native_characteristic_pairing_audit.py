#!/usr/bin/env python3
"""Durability audit for ledger v0.145 native characteristic-pairing kill."""

import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]
CHECKS = 0


def check(label, condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)
    print(f"PASS {label}")


ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.145.json").read_text())
result = json.loads((ROOT / "lab/process/selected-k77-p3-native-characteristic-pairing.json").read_text())
report = (ROOT / "explorations/conditional-build/selected-k77-p3-native-characteristic-pairing-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-p3-native-characteristic-pairing-review.md").read_text()
contract = json.loads((ROOT / "lab/methods/research-evidence-contract-v1.0.json").read_text())

check("ledger version is v0.145", ledger["schema_version"] == "0.145")
check("headline counts freeze", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue freezes at 84", ledger["residue"]["continuous_real"] == 84)
check("five quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("moving Spin native pairing is zero", result["native_pairings"]["moving_spin_killing"] == 0)
check("both half pairings are zero", result["native_pairings"]["u3232_half_1"] == result["native_pairings"]["u3232_half_2"] == 0)
check("full parent pairing is zero", result["native_pairings"]["u6464_full"] == 0)
check("direct horn killed", result["direct_horn"] == "KILLED")
check("nonzero P3 strata have no amplitude", result["p3_native_diagonal"]["n_minus_1"] == result["p3_native_diagonal"]["n_plus_1"] == "NO_REAL_AMPLITUDE")
check("zero P3 stratum leaves all amplitudes", result["p3_native_diagonal"]["n_0"] == "ALL_AMPLITUDES")
check("self-dual control is nonzero", result["self_dual_controls"]["u6464_full_relative"] == 384)
check("self-dual control is not parent invariant", result["self_dual_controls"]["parent_invariant_without_reduction"] is False)
check("report preserves general theorem", "The general theorem survives" in report)
check("report states direct horn killed", "The direct v0.144" in report and "is killed" in report)
check("hostile review rejects chiral trace promotion", "calling" in review and "the parent characteristic class" in review)
check("hostile review retains only reduction revival", "self-dual source-reduction ownership test" in review)
check("current append-only ledger descends to v0.145",
      reaches_historical_snapshot(
          contract, "lab/process/conditional-physics-ledger-v0.145.json"))
check("P1 P2 P3 unchanged", result["p1_p2_p3"] == "UNCHANGED_AND_UNASSIGNED")
check("no canon movement", result["canon_verdict_change"] == "none")

print(f"PASS {CHECKS}/{CHECKS}")
