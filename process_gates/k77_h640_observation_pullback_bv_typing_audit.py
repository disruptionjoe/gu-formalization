#!/usr/bin/env python3
"""Process gate for ledger v0.183 H640 observation graph / BV typing."""

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


ledger = strict("lab/process/conditional-physics-ledger-v0.183.json")
previous = strict("lab/process/conditional-physics-ledger-v0.182.json")
result = strict("lab/process/selected-k77-h640-observation-pullback-bv-typing.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")

check("ledger", "current append-only ledger descends to v0.183",
      reaches_historical_snapshot(contract, "lab/process/conditional-physics-ledger-v0.183.json"))

check("ledger", "append-only successor identity is exact",
      ledger["schema_version"] == "0.183"
      and ledger["predecessor"].endswith("v0.182.json"))
check("ledger", "headline counts remain unchanged",
      ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"]
      and ledger["progress"]["mapped"] == previous["progress"]["mapped"] == 82)
check("ledger", "residue and quotient count remain unchanged",
      ledger["residue"]["continuous_real"] == previous["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == previous["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier records four closed conditions and three named successors",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 4,
          "conditions_opened": 1, "remaining_named_conditions": 3,
      })
check("ledger", "exactly six current wave rows migrated",
      {item["row_id"] for item in ledger["wave_row_dispositions"]}
      == {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"})
check("ledger", "six append-only v0.183 history records exist",
      sum(item.get("to_version") == "0.183" for item in ledger["migration_history"]) == 6)

check("result", "probe has zero failures and exact/two-prime coverage",
      result["checks"] == {
          "total": 58, "failures": 0, "planted": 3,
          "characteristic_zero_graph": True, "two_prime_transport": True,
      })
graph = result["characteristic_zero"]
check("graph", "equal rank does not mean equal carrier",
      graph["h640_rank"] == graph["coordinate_observation_rank"] == 640
      and not graph["coordinate_subspaces_equal"]
      and graph["intersection_rank"] == 512 and graph["join_rank"] == 768)
check("graph", "observation derives a rank-128 principal no-leakage graph",
      graph["graph_correction_rank"] == 128
      and graph["observation_restricts_isomorphically"]
      and graph["principal_graph_no_leakage"])

transport = result["transport"]
check("transport", "complete coordinate frame classes and moving chain rule are recorded",
      transport["coordinate_stabilizer_generators"] == 51
      and transport["coordinate_mixed_generators"] == 40
      and transport["mixed_fixed_leakage_rank_each"] == 128
      and transport["moving_projector_chain_rule_all"]
      and transport["pure_frame_only"])

lower = result["lower_order"]
check("lower", "individual lower-order witnesses leak while graph compression remains exact",
      {lower[key] for key in (
          "internal_witness_graph_leakage_rank",
          "observed_port_graph_leakage_rank",
          "transverse_port_graph_leakage_rank",
          "generic_port_graph_leakage_rank",
      )} == {128}
      and lower["mixed_gauge_frame_graph_leakage_rank"] == 256
      and lower["graph_compression_exact"]
      and not lower["complete_sixteen_cell_graph_riccati_built"])

bv = result["bv_typing"]
check("bv", "barred/unbarred, antifield and pairing ranks are typed without cohomology",
      bv["barred_unbarred_graph_field_rank"] == 1280
      and bv["formal_non_ghost_field_antifield_rank"] == 2560
      and bv["restricted_k77_pairing_rank"] == 640
      and not bv["complete_bv_koszul_tate_built"]
      and not bv["physical_cohomology_built"])

check("scope", "source silence and public-accounting fences remain explicit",
      "SOURCE_SILENT_ON_THE_ACTION_DERIVED_GRAPH_LIFT" in result["source_return"]
      and not result["accounting"]["P1_P2_P3_used"]
      and not result["accounting"]["verdict_change"]
      and not result["accounting"]["booked_residue_change"]
      and not result["accounting"]["quotient_change"]
      and not result["accounting"]["canon_verdict_change"]
      and not result["accounting"]["public_posture_change"])

for relative, needles in {
    "lab/process/hostile-reviews/2026-08-11-selected-k77-h640-observation-pullback-bv-typing-review.md": ["SURVIVES_SCOPED", "symplectic/BV-BFV", "intersection rank 512"],
    "lab/sources/selected-k77-h640-observation-pullback-bv-typing-source-return-2026-08-11.md": ["SOURCE-SILENT", "repository construction"],
}.items():
    text = (ROOT / relative).read_text(encoding="utf-8")
    check("surface", f"{relative} carries the required scope",
          all(needle in text for needle in needles))

print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: v0.183 H640 observation graph / BV typing is routed and scope-fenced.")
