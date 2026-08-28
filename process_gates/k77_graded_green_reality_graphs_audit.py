#!/usr/bin/env python3
"""Process gate for ledger v0.177 graded Green/reality graphs."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def strict(relative: str):
    path = ROOT / relative

    def reject(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result

    return json.loads(path.read_text(), object_pairs_hook=reject)


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


ledger = strict("lab/process/conditional-physics-ledger-v0.177.json")
previous = strict("lab/process/conditional-physics-ledger-v0.176.json")
result = strict("lab/process/selected-k77-graded-green-reality-graphs.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
v174 = strict("lab/process/selected-k77-action-adjoint-weight-classification.json")

check("ledger", "current append-only ledger descends to v0.177",
      reaches_historical_snapshot(contract, "lab/process/conditional-physics-ledger-v0.177.json"))

check("ledger", "append-only successor identity is exact",
      ledger["schema_version"] == "0.177"
      and ledger["predecessor"].endswith("v0.176.json"))
check("ledger", "headline counts remain unchanged",
      ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("ledger", "residue and quotient count remain unchanged",
      ledger["residue"]["continuous_real"] == previous["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == previous["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier records three closures and one opening",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 3,
          "conditions_opened": 1, "remaining_named_conditions": 2,
      })
check("ledger", "exactly six current wave rows migrated",
      {item["row_id"] for item in ledger["wave_row_dispositions"]}
      == {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"})

check("result", "new exact probe has zero failures and four plants",
      result["checks"] == {"total": 70, "failures": 0, "planted": 4})
check("result", "both complete action-pairing horns survive",
      set(result["action_pairing_horns"].values())
      == {"NONCHARACTERISTIC_GRADED_LAGRANGIAN_REALITY_GRAPH"})
check("result", "full-carrier prior art is the exact two-horn classification",
      v174["pairing_ranks"] == [1920, 1920]
      and v174["directions_checked_each_prime"] == 14
      and v174["checks"]["failures"] == 0)
check("scope", "selection remains open",
      result["selection"] == "TWO_HORNS_PLUS_CONDITIONAL_P_REMAIN_UNSELECTED")
check("scope", "null, mixed and analytic domains remain open",
      result["full_moving_mixed_preboundary"] == "OPEN"
      and result["analytic_domain"].startswith("OPEN__NULL_CHARACTERISTIC"))
check("scope", "P1/P2/P3, verdict, residue, quotient and canon stay still",
      not result["p1_p2_p3_used"] and not result["verdict_change"]
      and not result["booked_residue_change"] and not result["quotient_change"]
      and not result["canon_verdict_change"] and not result["public_posture_change"])

for relative, needles in {
    "lab/process/hostile-reviews/2026-08-11-selected-k77-graded-green-reality-graphs-review.md": ["SURVIVES_WITH_SCOPE_REPAIR", "graded-even"],
    "lab/sources/selected-k77-graded-green-reality-graphs-source-return-2026-08-11.md": ["SOURCE-SILENT", "four independent"],
}.items():
    text = (ROOT / relative).read_text()
    check("surface", f"{relative} carries the required scope", all(n in text for n in needles))

print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: v0.177 graded Green/reality-graph packet is routed and scope-fenced.")
