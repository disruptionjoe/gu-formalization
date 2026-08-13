#!/usr/bin/env python3
"""Integrity checks for conditional physics ledger v0.79."""

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


old = strict("lab/process/conditional-physics-ledger-v0.78.json")
new = strict("lab/process/conditional-physics-ledger-v0.79.json")
registry = strict("lab/process/selected-k77-physical-section-faithfulness-gate.json")

check("schema", "ledger advances once", old["schema_version"] == "0.78" and new["schema_version"] == "0.79")
check("schema", "predecessor is immutable v0.78", new["predecessor"].endswith("v0.78.json"))
check("meter", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("meter", "residue and forks remain frozen",
      new["residue"]["continuous_real"] == old["residue"]["continuous_real"] == 84
      and new["residue"]["function_valued_at_least"] == old["residue"]["function_valued_at_least"]
      and new["residue"]["open_discrete_forks"] == old["residue"]["open_discrete_forks"])
check("meter", "five scoped quotients remain", new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"] == 5)
check("frontier", "frontier delta remains explicit",
      new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3,
                                "conditions_opened": 1, "remaining_named_conditions": 2})
check("source", "source return records correction confirmation and silence",
      all(marker in new["source_return"] for marker in ("SOURCE-CORRECTS", "SOURCE-CONFIRMS", "SOURCE-SILENT")))

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
check("rows", "exactly five named rows migrate",
      {rid for rid in old_rows if old_rows[rid] != new_rows[rid]} == expected)
for rid in sorted(expected):
    check("rows", f"{rid} verdict remains frozen", new_rows[rid]["verdict"] == old_rows[rid]["verdict"])
    check("rows", f"{rid} reason kind remains frozen", new_rows[rid]["reason_kind"] == old_rows[rid]["reason_kind"])
    check("rows", f"{rid} points to v0.79 evidence",
          new_rows[rid]["evidence"] == "selected-k77-physical-section-faithfulness-gate-2026-08-08.md")
    check("rows", f"{rid} retains the v0.78 overlap theorem",
          "NO_LEAKAGE_PROJECTOR_OVERLAP_EXACT" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} records the arbitrary-X scope kill",
          "ARBITRARY_X_LORENTZ_SECTION_KILLED" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} records local holonomic survival",
          "LOCAL_HOLONOMIC_JET_EXACT" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} records ordinary-pullback action-faithfulness kill",
          "ORDINARY_PULLBACK_ACTION_FAITHFULNESS_KILLED" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} records the surviving construction fork",
          "COMPLETE_4_PLUS_10_OR_BV_CONSTRAINT_FORK_OPEN" in new_rows[rid]["mapping_grade"])

migrations = [item for item in new["migrations"]
              if item.get("from_version") == "0.78" and item.get("to_version") == "0.79"]
check("migration", "five append-only migration edges exist",
      len(migrations) == 5 and {item["row_id"] for item in migrations} == expected)
check("topology", "registry records the spin S4 counterexample",
      registry["topology"]["counterexample"] == "S4"
      and registry["topology"]["spin"] is True
      and registry["topology"]["lorentz_section"] is False)
check("exact", "registry records the universal rank split",
      registry["exact_results"]["ordinary_pullback_rank"] == 4
      and registry["exact_results"]["conormal_kernel_rank"] == 10)
check("exact", "registry records a live action-image collision",
      registry["exact_results"]["action_conormal_witness_nonzero"] is True
      and registry["exact_results"]["action_conormal_witness_pullback_zero"] is True)
check("exact", "complete receiver survives",
      registry["exact_results"]["complete_receiver_rank"] == 14
      and registry["exact_results"]["complete_receiver_detects_witness"] is True)
check("fork", "neither construction horn is promoted", registry["construction_fork"]["selected"] is False)
check("queue", "rank one names both construction horns",
      "4+10" in new["next_work_queue"][0]["why"]
      and "constraint/BV" in new["next_work_queue"][0]["why"])
check("scope", "no constraint-accounting movement",
      set(registry["constraint_fence"].values()) <= {0, "UNUSED"})
check("scope", "P1 P2 P3 remain unused", registry["constraint_fence"]["P1_P2_P3"] == "UNUSED")

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
