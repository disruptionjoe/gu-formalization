#!/usr/bin/env python3
"""Process gate for ledger v0.187 canonical section-jet Cartan/Spin lift."""

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


ledger = strict("lab/process/conditional-physics-ledger-v0.187.json")
previous = strict("lab/process/conditional-physics-ledger-v0.186.json")
result = strict("lab/process/selected-k77-canonical-section-jet-cartan-spin-prolongation.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")

check("ledger", "current append-only ledger descends to v0.187",
      reaches_historical_snapshot(contract, "lab/process/conditional-physics-ledger-v0.187.json"))

check("ledger", "append-only successor identity is exact",
      ledger["schema_version"] == "0.187"
      and ledger["predecessor"].endswith("v0.186.json"))
check("ledger", "headline counts remain unchanged",
      ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"]
      and ledger["progress"]["mapped"] == previous["progress"]["mapped"] == 82)
check("ledger", "residue and quotient count remain unchanged",
      ledger["residue"]["continuous_real"] == previous["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == previous["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier records local closure and nonlinear successor",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 3,
          "conditions_opened": 1, "remaining_named_conditions": 3,
      })
expected = {"RA-D4", "RA-E3", "RA-E5", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}
check("ledger", "exactly eight rows migrated",
      {row["row_id"] for row in ledger["wave_row_dispositions"]} == expected)
check("ledger", "both migration stores have exactly eight v0.187 edges",
      sum(row.get("to_version") == "0.187" for row in ledger["migrations"]) == 8
      and sum(row.get("to_version") == "0.187" for row in ledger["migration_history"]) == 8)

cartan = result["cartan_lift"]
check("cartan", "forty-dimensional lift and signature classes are exact",
      cartan["domain_dimension"] == 40
      and cartan["rotation_directions"] == 18
      and cartan["boost_directions"] == 22)
check("cartan", "actual receiver maps without fitting",
      cartan["actual_section_jet_rank"] == 4
      and cartan["actual_lift_rank"] == 8
      and cartan["graph_block_exact"] and cartan["k77_orthogonal"]
      and not cartan["residual_fit_used"])
check("control", "plants reject blind skew and missing reciprocal block",
      cartan["blind_skew_projection_factor"] == "1/2"
      and cartan["missing_reciprocal_defect_rank"] == 8)

spin = result["spin_and_operator"]
check("spin", "all-forty Clifford and chirality identities pass",
      spin["gamma_covariance_all_40"] and spin["chirality_preserved_all_40"])
check("bundle", "full carrier/H640 controls remain nonvacuous",
      spin["ambient_control_rank"] == 1920 and spin["h640_rank"] == 640
      and spin["inherited_symbol_covariance"]
      and spin["inherited_fixed_graph_leak_rank"] == 128
      and spin["inherited_moving_graph_leak_rank"] == 0)
check("symplectic", "both horns are preserved without selection",
      spin["pairing_block_types_preserved_all_40"] == 2
      and not spin["pairing_horn_selected"])

gimmel = result["moving_gimmel"]
check("layer0", "moving-gimmel and fixed-Cartan maps remain distinct",
      gimmel["metric_basis_directions"] == 10 and gimmel["compensation_exact"]
      and not gimmel["fixed_metric_cartan_element"]
      and not gimmel["identified_with_q_J"])
check("scope", "nonlinear flag and BV remain open",
      result["scope"]["finite_nonlinear_normalization"] == "OPEN"
      and result["scope"]["full_epsilon_IG_complex_cartan_flag"] == "OPEN"
      and result["scope"]["lower_order_bv_kt"] == "OPEN"
      and not any(result["accounting"].values()))

for relative, needles in {
    "lab/process/hostile-reviews/2026-08-12-selected-k77-canonical-section-jet-cartan-spin-prolongation-review.md": ["SURVIVES_SCOPED", "Symplectic", "mistyped"],
    "lab/sources/selected-k77-canonical-section-jet-cartan-spin-prolongation-source-return-2026-08-12.md": ["SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"],
}.items():
    text = (ROOT / relative).read_text(encoding="utf-8")
    check("surface", f"{relative} carries required scope",
          all(needle in text for needle in needles))

print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: v0.187 canonical local section-jet Cartan/Spin lift is routed and fenced.")
