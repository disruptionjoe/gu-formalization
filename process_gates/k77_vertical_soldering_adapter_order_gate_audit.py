#!/usr/bin/env python3
"""Process gate for ledger v0.185 vertical-soldering adapter order result."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]
COUNTS = Counter()
FAILURES: list[str] = []


def strict(relative: str):
    path = ROOT / relative

    def reject(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject)


def check(kind: str, label: str, value) -> None:
    COUNTS[kind] += 1
    ok = bool(value)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


ledger = strict("lab/process/conditional-physics-ledger-v0.185.json")
previous = strict("lab/process/conditional-physics-ledger-v0.184.json")
result = strict("lab/process/selected-k77-vertical-soldering-adapter-order-gate.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")

check("ledger", "current append-only ledger descends to v0.185",
      reaches_historical_snapshot(contract, "lab/process/conditional-physics-ledger-v0.185.json"))

check("ledger", "append-only successor identity is exact",
      ledger["schema_version"] == "0.185"
      and ledger["predecessor"].endswith("v0.184.json"))
check("ledger", "headline counts remain unchanged",
      ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"]
      and ledger["progress"]["mapped"] == previous["progress"]["mapped"] == 82)
check("ledger", "residue and quotient count remain unchanged",
      ledger["residue"]["continuous_real"] == previous["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == previous["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier records two closures and one newly typed successor",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 2,
          "conditions_opened": 1, "remaining_named_conditions": 4,
      })
expected_rows = {"RA-D4", "RA-E3", "RA-E5", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}
check("ledger", "exactly eight current wave rows migrated",
      {item["row_id"] for item in ledger["wave_row_dispositions"]} == expected_rows)
check("ledger", "both migration stores record exactly eight v0.185 edges",
      sum(item.get("to_version") == "0.185" for item in ledger["migrations"]) == 8
      and sum(item.get("to_version") == "0.185" for item in ledger["migration_history"]) == 8)

order = result["order_gate"]
check("result", "exact probe records zero failures over two fields",
      result["checks"] == {"total": 44, "failures": 0, "planted": 2, "two_prime_exact": True})
check("order", "rank-ten algebraic family has zero principal response to ten rank-128 targets",
      order["sigma_epsilon_rank"] == 10
      and order["transverse_principal_residual_count"] == 10
      and order["transverse_principal_residual_rank_each"] == 128
      and order["principal_response_rank_of_algebraic_chain"] == 0)
check("control", "fixed-scale span and first-order firing plant discriminate the classes",
      order["representative_zero_order_adapter_coordinate_rank"] == 10
      and order["principal_target_coordinate_rank"] == 10
      and order["representative_joint_coordinate_rank"] == 20
      and order["representative_targets_in_zero_order_span"] == 0
      and order["first_order_plant_closure_rank"] == 0)
check("control", "H640 and full ambient controls retain their exact ranks",
      order["h640_rank"] == 640 and order["ambient_control_rank"] == 1920)

pairing = result["pairing"]
check("symplectic", "both pairing horns remain eligible without selection",
      pairing == {
          "horns": 2,
          "tested_vertical_basis_terms_per_horn": 10,
          "alternating_terms_per_horn": 10,
          "horn_selected": False,
      })
check("scope", "source and accounting fences remain explicit",
      "SOURCE_SILENT_ON_SIGMA_EPSILON_H640" in result["source_return"]
      and not any(result["accounting"].values()))

for relative, needles in {
    "lab/process/hostile-reviews/2026-08-11-selected-k77-vertical-soldering-adapter-order-gate-review.md": ["SURVIVES_SCOPED", "Symplectic/BV-BFV", "zeroth order"],
    "lab/sources/selected-k77-vertical-soldering-adapter-order-gate-source-return-2026-08-11.md": ["SOURCE-SILENT", "first-order"],
}.items():
    text = (ROOT / relative).read_text(encoding="utf-8")
    check("surface", f"{relative} carries the required scope",
          all(needle in text for needle in needles))

print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: v0.185 differential-order split is routed and scope-fenced.")
