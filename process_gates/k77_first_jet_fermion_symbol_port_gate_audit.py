#!/usr/bin/env python3
"""Process gate for ledger v0.186 K77 first-jet fermion-symbol port."""

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


ledger = strict("lab/process/conditional-physics-ledger-v0.186.json")
previous = strict("lab/process/conditional-physics-ledger-v0.185.json")
result = strict("lab/process/selected-k77-first-jet-fermion-symbol-port-gate.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")

check("ledger", "current append-only ledger descends to v0.186",
      reaches_historical_snapshot(contract, "lab/process/conditional-physics-ledger-v0.186.json"))

check("ledger", "append-only successor identity is exact",
      ledger["schema_version"] == "0.186"
      and ledger["predecessor"].endswith("v0.185.json"))
check("ledger", "headline counts remain unchanged",
      ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"]
      and ledger["progress"]["mapped"] == previous["progress"]["mapped"] == 82)
check("ledger", "residue and quotient count remain unchanged",
      ledger["residue"]["continuous_real"] == previous["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == previous["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier records three closures and one canonical successor",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 3,
          "conditions_opened": 1, "remaining_named_conditions": 3,
      })
expected = {"RA-D4", "RA-E3", "RA-E5", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}
check("ledger", "exactly eight rows migrated",
      {row["row_id"] for row in ledger["wave_row_dispositions"]} == expected)
check("ledger", "both migration stores have exactly eight v0.186 edges",
      sum(row.get("to_version") == "0.186" for row in ledger["migrations"]) == 8
      and sum(row.get("to_version") == "0.186" for row in ledger["migration_history"]) == 8)

raw = result["raw_port"]
check("raw", "H640 and ambient controls retain rank",
      raw["h640_rank"] == 640 and raw["ambient_control_rank"] == 1920)
check("raw", "ten transverse rank-128 residuals remain independent",
      raw["transverse_residual_count"] == 10
      and raw["transverse_residual_rank_each"] == 128
      and raw["transverse_residual_coordinate_rank"] == 10)
check("raw", "observation shear is invertible but not K77 orthogonal",
      raw["section_jet_rank"] == 4 and raw["field_shear_rank"] == 14
      and raw["k77_orthogonality_defect_rank"] == 8
      and raw["off_diagonal_rank"] == 4)
check("order", "Levi-Civita is fermion-zero-order",
      raw["levi_civita_fermion_principal_response_rank"] == 0)

spin = result["spin_prolongation"]
check("spin", "boost and rotation satisfy exact Clifford and symbol transport",
      spin["representatives"] == ["opposite_sign_boost", "same_sign_rotation"]
      and spin["vector_orthogonal"] and spin["spin_inverse"]
      and spin["gamma_covariance"] and spin["symbol_covariance"])
check("bundle", "moving graph closes while fixed graph leaks",
      spin["moving_graph_split"]
      and spin["fixed_graph_leak_rank_each"] == 128
      and spin["moving_graph_leak_rank_each"] == 0)
check("symplectic", "both horns are preserved without selection",
      spin["pairing_horns_preserved"] == 2
      and not spin["pairing_horn_selected"])
check("scope", "accounting and source fences remain explicit",
      not any(result["accounting"].values())
      and "SOURCE_SILENT_ON_THE_EPSILON_IG" in result["source_return"])

for relative, needles in {
    "lab/process/hostile-reviews/2026-08-11-selected-k77-first-jet-fermion-symbol-port-gate-review.md": ["SURVIVES_SCOPED", "Symplectic", "mistyped"],
    "lab/sources/selected-k77-first-jet-fermion-symbol-port-gate-source-return-2026-08-11.md": ["SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"],
}.items():
    text = (ROOT / relative).read_text(encoding="utf-8")
    check("surface", f"{relative} carries required scope",
          all(needle in text for needle in needles))

print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: v0.186 raw-port kill and local Spin-prolongation witness are routed and fenced.")
