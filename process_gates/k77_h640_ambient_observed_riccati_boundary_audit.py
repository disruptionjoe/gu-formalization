#!/usr/bin/env python3
"""Process gate for ledger v0.184 H640 ambient/observed boundary."""

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


def check(kind: str, label: str, value) -> None:
    COUNTS[kind] += 1
    ok = bool(value)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


ledger = strict("lab/process/conditional-physics-ledger-v0.184.json")
previous = strict("lab/process/conditional-physics-ledger-v0.183.json")
result = strict("lab/process/selected-k77-h640-ambient-observed-riccati-boundary.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")

check("ledger", "append-only successor identity is exact",
      ledger["schema_version"] == "0.184"
      and ledger["predecessor"].endswith("v0.183.json"))
check("ledger", "headline counts remain unchanged",
      ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"]
      and ledger["progress"]["mapped"] == previous["progress"]["mapped"] == 82)
check("ledger", "residue and quotient count remain unchanged",
      ledger["residue"]["continuous_real"] == previous["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == previous["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier records the prerequisite correction",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 2,
          "conditions_opened": 1, "remaining_named_conditions": 4,
      })
check("ledger", "exactly six current wave rows migrated",
      {item["row_id"] for item in ledger["wave_row_dispositions"]}
      == {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"})
check("ledger", "six append-only v0.184 history records exist",
      sum(item.get("to_version") == "0.184" for item in ledger["migration_history"]) == 6)

boundary = result["ambient_observed_boundary"]
check("result", "exact probe records zero failures over two fields",
      result["checks"] == {"total": 42, "failures": 0, "planted": 2, "two_prime_exact": True})
check("boundary", "observed graph closes while every transverse direction leaks",
      boundary["h640_rank"] == 640
      and boundary["observed_spatial_indices"] == [7, 8, 9]
      and boundary["observed_leakage_rank_each"] == 0
      and boundary["transverse_spatial_count"] == 10
      and boundary["transverse_leakage_rank_each"] == 128)
check("boundary", "ambient hull reaches full carrier and ordinary pullback kills transverse covectors",
      boundary["single_transverse_join_rank"] == 768
      and boundary["all_spatial_hull_ranks"] == [640, 1920]
      and boundary["ambient_hull_rank"] == 1920
      and boundary["ordinary_transverse_covector_pullback_rank_each"] == 0)

pairing = result["pairing"]
check("symplectic", "both pairing horns remain eligible without implying no-leakage",
      pairing["horns"] == 2 and pairing["restriction_rank_each"] == 640
      and pairing["restricted_grassmann_coefficients_alternating_all_fourteen_axes"]
      and not pairing["alternation_implies_no_leakage"])
check("scope", "source and accounting fences remain explicit",
      "SOURCE_SILENT_ON_H640_GRAPH" in result["source_return"]
      and not any(result["accounting"].values()))

standing = contract["standing_ledger"]
check("routing", "operating contract points at v0.184",
      standing["ref"].endswith("v0.184.json")
      and standing["human_ref"].endswith("v0.184.md"))
check("routing", "vertical adapter precedes the sixteen-cell solve",
      contract["current_priority_decision"]["main_sequence"][:2] == [
          "CONSTRUCT_OR_KILL_SOURCE_ACTION_OWNED_VERTICAL_HIGGS_SOLDERING_ADAPTER_ON_H640_WITH_FULL1920_CONTROL",
          "SOLVE_COMPLETE_SIXTEEN_CELL_GRAPH_RICCATI_BARRED_ADJOINT_AND_BV_KT_ONLY_AFTER_ADAPTER_TYPING",
      ])

for relative, needles in {
    "NEXT-STEPS.md": ["ledger v0.184", "Higgs/soldering adapter", "rank 1,920"],
    "RESEARCH-STATUS.md": ["ledger v0.184", "transverse `Y^14`", "rank 128"],
    "lab/process/CURRENT-RESEARCH-CONTEXT.md": ["Current v0.184", "vertical adapter", "P1/P2/P3"],
    "lab/process/hostile-reviews/2026-08-11-selected-k77-h640-ambient-observed-riccati-boundary-review.md": ["SURVIVES_SCOPED", "symplectic/BV-BFV", "ordinary pullback"],
    "lab/sources/selected-k77-h640-ambient-observed-riccati-boundary-source-return-2026-08-11.md": ["SOURCE-SILENT", "not a quotation"],
}.items():
    text = (ROOT / relative).read_text(encoding="utf-8")
    check("surface", f"{relative} carries the required scope",
          all(needle in text for needle in needles))

print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: v0.184 H640 ambient/observed boundary is routed and scope-fenced.")
