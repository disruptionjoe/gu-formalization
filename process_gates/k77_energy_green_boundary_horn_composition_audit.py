#!/usr/bin/env python3
"""Process gate for ledger v0.179 energy/Green boundary-horn composition."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]
COUNTS = Counter()
FAILURES = []


def strict(relative):
    path = ROOT / relative

    def reject(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=reject)


def check(kind, label, value):
    COUNTS[kind] += 1
    ok = bool(value)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


ledger = strict("lab/process/conditional-physics-ledger-v0.179.json")
previous = strict("lab/process/conditional-physics-ledger-v0.178.json")
result = strict("lab/process/selected-k77-energy-green-boundary-horn-composition.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")

check("ledger", "current append-only ledger descends to v0.179",
      reaches_historical_snapshot(contract, "lab/process/conditional-physics-ledger-v0.179.json"))

check("ledger", "append-only successor identity is exact",
      ledger["schema_version"] == "0.179"
      and ledger["predecessor"].endswith("v0.178.json"))
check("ledger", "headline counts remain unchanged",
      ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("ledger", "residue and quotient count remain unchanged",
      ledger["residue"]["continuous_real"] == previous["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == previous["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier records two closures and no opening",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 2,
          "conditions_opened": 0, "remaining_named_conditions": 2,
      })
check("ledger", "exactly six current wave rows migrated",
      {item["row_id"] for item in ledger["wave_row_dispositions"]}
      == {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"})

check("result", "new exact probe has zero failures and four plants",
      result["checks"] == {"total": 45, "failures": 0, "planted": 4})
check("result", "full incoming and outgoing halves are exact",
      result["carrier_rank"] == 1920
      and result["incoming_rank"] == result["outgoing_rank"] == 960)
check("result", "one-sided independent-dual obstruction is retained",
      set(result["one_sided_independent_dual_restriction_ranks"].values()) == {960})
check("result", "both doubled Majorana incoming graphs are Green-isotropic",
      set(result["doubled_majorana_green_restriction_ranks"].values()) == {0})
check("result", "two primes reproduce the classification",
      result["exact_primes"] == [1009, 1013])
check("layer0", "registry explicitly records the wrong-object correction",
      "ONE_SIDED_P_DN" in result["layer0_correction"]
      and "DOUBLED_GRAPH_PULLBACK" in result["layer0_correction"])
check("scope", "local compatibility does not become global ownership",
      "VARIABLE_GLOBAL_TRANSPORT_AND_ACTION_OWNERSHIP_OPEN" in result["analytic_status"])
check("scope", "both horns pass without selection",
      result["selection"] == "BOTH_HORNS_PASS__NO_HORN_OR_P_SELECTION")
check("scope", "P1/P2/P3, verdict, residue, quotient and canon stay still",
      not result["p1_p2_p3_used"] and not result["verdict_change"]
      and not result["booked_residue_change"] and not result["quotient_change"]
      and not result["canon_verdict_change"] and not result["public_posture_change"])

for relative, needles in {
    "lab/process/hostile-reviews/2026-08-11-selected-k77-energy-green-boundary-horn-composition-review.md": ["LAYER0_REVERSAL", "rank `960`"],
    "lab/sources/selected-k77-energy-green-boundary-horn-composition-source-return-2026-08-11.md": ["SOURCE-SILENT", "incoming"],
}.items():
    text = (ROOT / relative).read_text()
    check("surface", f"{relative} carries the required scope",
          all(needle in text for needle in needles))

print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: v0.179 energy/Green boundary-horn packet is routed and scope-fenced.")
