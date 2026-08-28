#!/usr/bin/env python3
"""Process gate for ledger v0.188 finite K77 graph projector/descent."""

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


def check(kind: str, label: str, condition) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


ledger = strict("lab/process/conditional-physics-ledger-v0.188.json")
previous = strict("lab/process/conditional-physics-ledger-v0.187.json")
result = strict("lab/process/selected-k77-finite-section-projector-atlas-descent.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")

check("ledger", "current append-only ledger descends to v0.188",
      reaches_historical_snapshot(contract, "lab/process/conditional-physics-ledger-v0.188.json"))

check("ledger", "append-only successor identity is exact",
      ledger["schema_version"] == "0.188"
      and ledger["predecessor"].endswith("v0.187.json"))
check("ledger", "headline counts remain unchanged",
      ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"]
      and ledger["progress"]["mapped"] == previous["progress"]["mapped"] == 82)
check("ledger", "residue and quotient count remain unchanged",
      ledger["residue"]["continuous_real"] == previous["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == previous["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier records finite closure and action-owned successor",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 3,
          "conditions_opened": 1, "remaining_named_conditions": 3,
      })
expected = {"RA-D4", "RA-E3", "RA-E5", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}
check("ledger", "exactly eight rows migrated",
      {row["row_id"] for row in ledger["wave_row_dispositions"]} == expected)
check("ledger", "both migration stores have exactly eight v0.188 edges",
      sum(row.get("to_version") == "0.188" for row in ledger["migrations"]) == 8
      and sum(row.get("to_version") == "0.188" for row in ledger["migration_history"]) == 8)

finite = result["finite_reduction"]
check("projector", "finite graph projector is exact and parameter-free",
      finite["graph_dimension"] == 4 and finite["parameter_dimension"] == 40
      and finite["idempotent"] and finite["eta_self_adjoint"]
      and finite["owns_graph"] and not finite["new_parameter_or_datum"])
check("analytic", "actual graph has Lorentzian inertia",
      finite["actual_graph_inertia"] == [1, 3])

atlas = result["atlas"]
check("atlas", "block and mixed fractional atlas descent are exact",
      atlas["block_stabilizer_descent"] and atlas["mixed_fractional_descent"]
      and atlas["projector_naturality"] == "P_J'=g*P_J*g^-1")
check("analytic", "null Gram boundary is explicit",
      atlas["null_gram_boundary_explicit"])

lift = result["lift"]
check("layer0", "projector and normalized O/Spin lift remain distinct",
      lift["normalized_O77_representative"] == "LOCAL_MOD_BLOCK_STABILIZER"
      and lift["spin_lift"] == "LOCAL_MOD_STABILIZER_AND_DOUBLE_COVER_SIGN"
      and lift["first_derivative_matches_v0187"]
      and not lift["global_preferred_frame_owned"])
check("scope", "full epsilon_IG remains open",
      lift["full_epsilon_IG_flag"] == "OPEN" and not any(result["accounting"].values()))
check("control", "all four planted shortcuts fire",
      all(result["plants"].values()))
check("exact", "two-field 39-check certificate is clean",
      result["checks"]["total"] == 39 and result["checks"]["failures"] == 0
      and result["checks"]["fields"] == [1009, 1013]
      and result["checks"]["all_forty_tangent_directions"])

for relative, needles in {
    "lab/process/hostile-reviews/2026-08-12-selected-k77-finite-section-projector-atlas-descent-review.md": ["SURVIVES_SCOPED", "Symplectic", "mistyped"],
    "lab/sources/selected-k77-finite-section-projector-atlas-descent-source-return-2026-08-12.md": ["SOURCE_CONFIRMS", "SOURCE_SILENT", "SOURCE_CORRECTS"],
}.items():
    text = (ROOT / relative).read_text(encoding="utf-8")
    check("surface", f"{relative} carries required scope",
          all(needle in text for needle in needles))

print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: v0.188 finite K77 graph projector/descent is routed and fenced.")
