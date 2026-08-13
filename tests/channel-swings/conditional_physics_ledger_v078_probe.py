#!/usr/bin/env python3
"""Integrity checks for conditional physics ledger v0.78."""

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


old = strict("lab/process/conditional-physics-ledger-v0.77.json")
new = strict("lab/process/conditional-physics-ledger-v0.78.json")
registry = strict("lab/process/selected-k77-action-bundle-observation-overlap.json")

check("schema", "ledger advances once", old["schema_version"] == "0.77" and new["schema_version"] == "0.78")
check("schema", "predecessor is v0.77", new["predecessor"].endswith("v0.77.json"))
check("meter", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("meter", "residue remains frozen",
      new["residue"]["continuous_real"] == old["residue"]["continuous_real"] == 84
      and new["residue"]["function_valued_at_least"] == old["residue"]["function_valued_at_least"]
      and new["residue"]["open_discrete_forks"] == old["residue"]["open_discrete_forks"])
check("meter", "five scoped quotients remain", new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"] == 5)
check("frontier", "frontier delta is 3 closed 1 opened 2 remaining",
      new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3,
                                "conditions_opened": 1, "remaining_named_conditions": 2})
check("source", "source return types confirmation silence and repo derivation",
      all(marker in new["source_return"] for marker in ("SOURCE-CONFIRMS", "SOURCE-SILENT", "REPO-DERIVES")))

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
check("rows", "exactly five named rows migrate",
      {rid for rid in old_rows if old_rows[rid] != new_rows[rid]} == expected)
for rid in sorted(expected):
    check("rows", f"{rid} verdict remains frozen", new_rows[rid]["verdict"] == old_rows[rid]["verdict"])
    check("rows", f"{rid} reason kind remains frozen", new_rows[rid]["reason_kind"] == old_rows[rid]["reason_kind"])
    check("rows", f"{rid} points to v0.78 evidence",
          new_rows[rid]["evidence"] == "selected-k77-action-bundle-observation-overlap-2026-08-08.md")
    check("rows", f"{rid} retains the full pointwise bank result",
          "FULL_U6464_POINTWISE_ACTION_BANK_RANK14_NORMAL10_EXACT" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} records the composed global P_H law",
          "GLOBAL_P_H_ASSOCIATED_BUNDLE_LAW_COMPOSED" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} records action and observation overlap",
          "NONCOMMUTING_THREE_PATCH_ACTION_OVERLAP_EXACT" in new_rows[rid]["mapping_grade"]
          and "COMPLETE_OBSERVATION_DUAL_OVERLAP_EXACT" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} records the separate no-leakage projector",
          "NO_LEAKAGE_PROJECTOR_OVERLAP_EXACT" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} retains the physical-section BFV/domain fence",
          "PHYSICAL_SECTION_INTEGRABILITY_BFV_DOMAIN_OPEN" in new_rows[rid]["mapping_grade"])

migrations = [item for item in new["migrations"]
              if item.get("from_version") == "0.77" and item.get("to_version") == "0.78"]
check("migration", "five append-only migration edges exist",
      len(migrations) == 5 and {item["row_id"] for item in migrations} == expected)
check("registry", "transitions are noncommuting and obey direct overlap",
      registry["exact_results"]["transitions_noncommuting"] is True
      and registry["exact_results"]["direct_sequential_slot_cocycle"] is True
      and registry["exact_results"]["direct_sequential_coefficient_cocycle"] is True)
check("registry", "patch banks are recomputed on seed and held-out families",
      registry["exact_results"]["patchwise_action_banks_recomputed"] is True
      and registry["exact_results"]["seed_direct_action_overlap"] is True
      and registry["exact_results"]["heldout_direct_action_overlap"] is True)
check("registry", "complete observation dual descends",
      registry["exact_results"]["complete_equation_dual_pairwise"] is True
      and registry["exact_results"]["complete_equation_dual_direct"] is True)
check("registry", "no-leakage projector descends separately",
      registry["exact_results"]["no_leakage_projector_pairwise"] is True
      and registry["exact_results"]["no_leakage_projector_direct"] is True)
check("registry", "pairing and endpoint transport descend",
      registry["exact_results"]["coefficient_pairing_descends"] is True
      and registry["exact_results"]["observed_pairing_descends"] is True
      and registry["exact_results"]["endpoint_pairing_preserved"] is True)
check("controls", "frozen receiver and projector plants fire",
      registry["controls"]["frozen_observation_receiver"] == "FIRED"
      and registry["controls"]["frozen_no_leakage_projector"] == "FIRED")
check("controls", "left inverse alone does not imply no leakage",
      registry["controls"]["hidden_covector_under_left_inverse"] == "FIRED")
check("queue", "rank one is physical section then BFV/domain",
      "observation-section" in new["next_work_queue"][0]["why"]
      and "tau_A0/BFV" in new["next_work_queue"][0]["why"]
      and "common Green/Krein domain" in new["next_work_queue"][0]["why"])
check("scope", "no constraint-accounting movement",
      set(registry["constraint_fence"].values()) <= {0, "UNUSED"})
check("scope", "physical section, BFV and common domain remain fenced",
      any("observation-section" in item for item in registry["boundary"])
      and any("BFV" in item for item in registry["boundary"])
      and any("domain" in item for item in registry["boundary"]))

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
