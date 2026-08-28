#!/usr/bin/env python3
"""Process gate for ledger v0.178 observed Cauchy-domain Layer-0 split."""

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


ledger = strict("lab/process/conditional-physics-ledger-v0.178.json")
previous = strict("lab/process/conditional-physics-ledger-v0.177.json")
result = strict("lab/process/selected-k77-observed-cauchy-domain-layer0.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
v173 = strict("lab/process/selected-k77-wedge-shiab-southeast-completion.json")

check("ledger", "current append-only ledger descends to v0.178",
      reaches_historical_snapshot(contract, "lab/process/conditional-physics-ledger-v0.178.json"))

check("ledger", "append-only successor identity is exact",
      ledger["schema_version"] == "0.178"
      and ledger["predecessor"].endswith("v0.177.json"))
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
      result["checks"] == {"total": 60, "failures": 0, "planted": 4})
check("result", "Majorana graph and Cauchy carrier retain the complete physical rank",
      result["principal_comparator"]["cauchy_data_rank"] == 4
      and "RANK4_TO_PHYSICAL_RANK4" in result["majorana_graph"])
check("result", "spatial incoming half is a distinct rank-two object",
      "INCOMING_NONPOSITIVE_RANK2" in result["spatial_boundary"])
check("result", "local analytic claim is explicitly observed, flat and conditional",
      result["analytic_domain"]
      == "CONDITIONAL_LOCAL_FLAT_OBSERVED_HS_CAUCHY_DOMAIN_BY_STANDARD_SYMMETRIC_HYPERBOLIC_THEOREM")
check("result", "Dirichlet moving-mixed closure is support-scoped",
      result["dirichlet_mixed"].startswith("ALL_MOVING_A_CROSS_TERMS_WITH_DELTA_Q_LEG"))
check("prior_art", "the full carrier has semisimple observed evolution and common symmetrizer",
      v173["fingerprint"]["spatial_jordan_ranks"] == [0, 0, 0]
      and v173["fingerprint"]["common_symmetrizer_rank"] == 1920)
check("scope", "global, spatial-boundary, ambient and null burdens stay open",
      all(word in result["open"] for word in
          ("VARIABLE_COEFFICIENT_GLOBAL_OBSERVED_DOMAIN", "SPATIAL_BOUNDARY_PROJECTOR",
           "AMBIENT_Y14_ULTRAHYPERBOLIC", "NULL_BFV")))
check("scope", "selection remains open",
      result["selection"]
      == "PRINCIPAL_CAUCHY_EXISTENCE_DOES_NOT_SELECT_PAIRING_HORN_OR_CONDITIONAL_P")
check("scope", "P1/P2/P3, verdict, residue, quotient and canon stay still",
      not result["p1_p2_p3_used"] and not result["verdict_change"]
      and not result["booked_residue_change"] and not result["quotient_change"]
      and not result["canon_verdict_change"] and not result["public_posture_change"])

for relative, needles in {
    "lab/process/hostile-reviews/2026-08-11-selected-k77-observed-cauchy-domain-layer0-review.md": ["SURVIVES_WITH_SCOPE_REPAIR", "4/4/2"],
    "lab/sources/selected-k77-observed-cauchy-domain-layer0-source-return-2026-08-11.md": ["SOURCE-SILENT", "spatial"],
}.items():
    text = (ROOT / relative).read_text()
    check("surface", f"{relative} carries the required scope", all(n in text for n in needles))

print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: v0.178 observed Cauchy-domain Layer-0 packet is routed and scope-fenced.")
