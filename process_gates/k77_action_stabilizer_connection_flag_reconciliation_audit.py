#!/usr/bin/env python3
"""Process gate for ledger v0.189 action/stabilizer reconciliation."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


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


ledger = strict("lab/process/conditional-physics-ledger-v0.189.json")
previous = strict("lab/process/conditional-physics-ledger-v0.188.json")
result = strict("lab/process/selected-k77-action-stabilizer-connection-flag-reconciliation.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")

check("ledger", "append-only successor identity is exact",
      ledger["schema_version"] == "0.189"
      and ledger["predecessor"].endswith("v0.188.json"))
check("ledger", "headline counts remain unchanged",
      ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"]
      and ledger["progress"]["mapped"] == previous["progress"]["mapped"] == 82)
check("ledger", "residue and quotient count remain unchanged",
      ledger["residue"]["continuous_real"] == previous["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == previous["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier closes the cocycle and reduced-connection gates",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 2,
          "conditions_opened": 0, "remaining_named_conditions": 2,
      })
expected = {"RA-D4", "RA-E3", "RA-E5", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}
check("ledger", "exactly eight rows migrated",
      {row["row_id"] for row in ledger["wave_row_dispositions"]} == expected)
check("ledger", "both migration stores have exactly eight v0.189 edges",
      sum(row.get("to_version") == "0.189" for row in ledger["migrations"]) == 8
      and sum(row.get("to_version") == "0.189" for row in ledger["migration_history"]) == 8)

construction = result["result"]
check("connection", "three-patch reductive connection theorem closes",
      construction["projector_three_patch_descent"]
      and construction["stabilizer_cocycle"]
      and construction["reduced_connection_affine_descent"]
      and construction["second_fundamental_tensorial_descent"]
      and construction["frame_free_reductive_connection"])
check("prior_art", "global Clifford soldering is retained rather than rebuilt",
      construction["global_gamma_epsilon_retained"])
check("scope", "residual flag and full-unitary compatibility remain open",
      not construction["residual_flag_selected"]
      and construction["full_unitary_varpi_compatibility"] == "OPEN")
check("control", "all four differential plants and residual-flag witness fire",
      all(result["controls"].values()))
check("exact", "two-field 42-check certificate is clean",
      construction["checks"] == 42 and construction["failures"] == 0
      and construction["fields"] == [1009, 1013])
check("accounting", "no parameter, field, fork or quotient is added",
      result["accounting"]["new_continuous_parameters"] == 0
      and result["accounting"]["new_function_slots"] == 0
      and result["accounting"]["new_discrete_forks"] == 0
      and result["accounting"]["new_quotients"] == 0
      and not result["accounting"]["P1_P2_P3_used"])

standing = contract["standing_ledger"]
check("routing", "contract points at v0.189",
      standing["ref"].endswith("v0.189.json")
      and standing["human_ref"].endswith("v0.189.md"))
check("routing", "residual flag concomitant precedes lower-order BV",
      contract["current_priority_decision"]["main_sequence"][:2] == [
          "BUILD_OR_KILL_TARGET_BLIND_ACTION_DERIVED_H_Q_CONCOMITANT_FOR_RESIDUAL_COMPLEX_CARTAN_FLAG_OR_PROVE_REFINEMENT_GAUGE",
          "INSERT_SURVIVING_ZERO_ORDER_HOMEGA_CHAIN_AND_SOLVE_COMPLETE_SIXTEEN_CELL_LOWER_ORDER_RICCATI_BARRED_ADJOINT_BV_KT",
      ])

for relative, needles in {
    "NEXT-STEPS.md": ["v0.189", "A^P", "residual complex-Cartan"],
    "RESEARCH-STATUS.md": ["v0.189", "stabilizer cocycle", "full-unitary"],
    "lab/process/agent-context-pack.md": ["Current v0.189", "gamma_epsilon", "P1/P2/P3"],
    "lab/process/hostile-reviews/2026-08-12-selected-k77-action-stabilizer-connection-flag-reconciliation-review.md": ["SURVIVES_AFTER_SCOPE_REPAIR", "Symplectic", "mistyped"],
    "lab/sources/selected-k77-action-stabilizer-connection-flag-reconciliation-source-return-2026-08-12.md": ["SOURCE_CONFIRMS", "SOURCE_SILENT", "SOURCE_CORRECTS"],
}.items():
    text = (ROOT / relative).read_text(encoding="utf-8")
    check("surface", f"{relative} carries required scope",
          all(needle in text for needle in needles))

print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: v0.189 action/stabilizer connection descent is routed and fenced from the residual flag.")
