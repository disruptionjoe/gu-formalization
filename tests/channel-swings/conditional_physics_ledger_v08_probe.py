#!/usr/bin/env python3
"""Append-only, taxonomy, residue and scope checks for ledger v0.8."""

from collections import Counter
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
counts = Counter()
failures: list[str] = []


def strict(path: Path):
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key in {path}")
        return dict(items)
    return json.loads(path.read_text(), object_pairs_hook=pairs)


def check(kind: str, label: str, condition: bool) -> None:
    counts[kind] += 1
    if not condition:
        failures.append(label)
    print(f"{'PASS' if condition else 'FAIL'} [{kind}] {label}")


v7p = ROOT / "lab/process/conditional-physics-ledger-v0.7.json"
v7vp = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.7.md"
v8p = ROOT / "lab/process/conditional-physics-ledger-v0.8.json"
v8vp = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.8.md"
reportp = ROOT / "explorations/conditional-build/k77-global-even-bv-null-green-domain-2026-08-05.md"
reviewp = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-global-even-bv-null-green-review.md"
registryp = ROOT / "lab/process/k77-global-even-bv-null-green-domain.json"

v7 = strict(v7p)
v8 = strict(v8p)
registry = strict(registryp)
rows7 = {row["id"]: row for row in v7["rows"]}
rows8 = {row["id"]: row for row in v8["rows"]}
active = {rid: row for rid, row in rows8.items() if row.get("row_status") != "SUPERSEDED"}
view = v8vp.read_text()
report = reportp.read_text()
review = reviewp.read_text()

check("provenance", "v0.7 machine ledger is byte-frozen",
      hashlib.sha256(v7p.read_bytes()).hexdigest()
      == "962fe592b131d52fe382a7298cf217ed2b6c0aa480b0cd17a87f62739c3c6b5a")
check("provenance", "v0.7 human view is byte-frozen",
      hashlib.sha256(v7vp.read_bytes()).hexdigest()
      == "bf6b365cf68ad0406cdfd80ac0bc7f73cf8b5c52fa82cd3ee4b15e46b860ab41")
check("exact", "v0.8 names v0.7 as predecessor",
      v8["schema_version"] == "0.8"
      and v8["predecessor"].endswith("conditional-physics-ledger-v0.7.json"))
check("exact", "row denominator and IDs are unchanged", set(rows7) == set(rows8))
check("exact", "only LT-GR2c changed", {rid for rid in rows7 if rows7[rid] != rows8[rid]} == {"LT-GR2c"})
check("exact", "the v0.8 migration edge is explicit",
      [m["row_id"] for m in v8["migrations"] if m.get("to_version") == "0.8"] == ["LT-GR2c"])
check("exact", "82 active targets and 83 provenance rows remain",
      len(active) == 82 and len(rows8) == 83)
check("exact", "axis counts remain 35/21/26",
      Counter(row["axis"] for row in active.values())
      == {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("exact", "verdict counts remain 32/19/25/6",
      Counter(row["verdict"] for row in active.values())
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6})
check("exact", "every active reason kind remains registered",
      all(row["reason_kind"] in v8["taxonomy"]["verdict_kinds"][row["verdict"]]
          for row in active.values()))

gr2c = rows8["LT-GR2c"]
check("type", "LT-GR2c remains NEEDS/MISSING_CONSTRUCTION",
      gr2c["verdict"] == "NEEDS" and gr2c["reason_kind"] == "MISSING_CONSTRUCTION")
check("type", "formal even owner, null quotient and conditional Green grade are explicit",
      all(token in gr2c["mapping_grade"] for token in
          ("FORMAL_MINIMAL_CME_COMPOSED", "NULL_4_CONSTRAINT_4_GAUGE_2_PHYSICAL_EXACT",
           "DEFECT_GREEN_DOMAIN_CONDITIONAL", "GLOBAL_Y14_DOMAIN_OBSERVATION_PHYSICS_OPEN")))
check("type", "distance now targets observation and global coupled Y14 domain",
      "observation" in gr2c["distance"] and "Y14" in gr2c["distance"])

residue = v8["residue"]
check("exact", "lambda_def is charged as the 84th prequotient real",
      residue["continuous_real"] == 84
      and "lambda_def" in residue["continuous_real_note"])
check("exact", "retiring the alias returns discrete forks and horn product to 10/2304",
      residue["open_discrete_forks"] == 10
      and residue["open_fork_horn_product"] == 2304
      and "LAMBDA_DEF_ALIAS_RETIRED" in residue["retired_fork"])
check("exact", "two local/defect quotients are ranked without global residue reduction",
      residue["quotients_ranked"] == 2
      and "dimension two" in residue["quotients_ranked_scope"])

null = registry["null_split"]
check("exact", "registry records the exact null 10-to-6-to-2 filtration",
      null["characteristic_kernel_dimension"] == 10
      and null["harmonic_constraint_rank_on_kernel"] == 4
      and null["constraint_compatible_kernel_dimension"] == 6
      and null["residual_gauge_rank"] == 4
      and null["physical_quotient_dimension"] == 2)
check("exact", "plus and cross are explicit and all six are not removed",
      null["explicit_representatives"] == ["PLUS", "CROSS"]
      and null["all_six_removed"] is False)
check("type", "formal CME is scoped to the homogeneous even gauge algebra",
      registry["formal_minimal_even_bv"]["classical_master_equation"].startswith("PASS_FORMAL")
      and registry["formal_minimal_even_bv"]["odd_super_ig_closure"] == "OPEN"
      and registry["formal_minimal_even_bv"]["positive_physical_cohomology"] == "OPEN")
check("type", "Green domain is flat-defect/conditional and leaves Y14 open",
      "FLAT_DEFECT" in registry["green_domain"]["scope"]
      and registry["green_domain"]["curved_lower_order_completion"] == "OPEN"
      and registry["green_domain"]["global_coupled_noncompact_y14_domain"] == "OPEN")
check("source", "composed-locus source return is SOURCE-SILENT",
      registry["source_return"] == "SOURCE-SILENT" and "SOURCE-SILENT" in report)
check("hostile", "both mandatory hostile charges and three material repairs are present",
      "summary outruns the artifact" in review
      and "superseded or mistyped object" in review
      and "dimension filtration" in review
      and "flat observation background" in review
      and "84 is a prequotient" in review)
check("exact", "human and machine meters agree",
      "Ledger v0.8" in view and "84 continuous real before quotient" in view
      and "10 open discrete forks" in view)

dispositions = {row["row_id"]: row for row in v8["wave_row_dispositions"]}
check("exact", "all five declared rows receive migration or evidence-backed no-change",
      set(dispositions) == {"LT-GR1b", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-SM8"}
      and dispositions["LT-GR2c"]["change"] == "MIGRATED"
      and all(dispositions[row]["change"] == "NO_CHANGE"
              for row in ("LT-GR1b", "LT-GR2b", "LT-GR2d", "LT-SM8")))

check("planted", "PLANT formal homogeneous CME is not positive SM BV",
      registry["row_dispositions"]["LT-SM8"].endswith("POSITIVE_PHYSICAL_COHOMOLOGY_OPEN"))
check("planted", "PLANT the selected Shiab horn does not revive LT-GR1b",
      registry["row_dispositions"]["LT-GR1b"].endswith("REMAINS_KILLED"))
check("planted", "PLANT normalization quotient remains unranked",
      registry["normalization"]["normalization_quotient_ranked"] is False)
check("planted", "PLANT no global residue reduction is booked",
      registry["residue"]["global_residue_reduction_booked"] is False)
check("planted", "PLANT P1 P2 P3 remain unused",
      registry["residue"]["P1_P2_P3"] == "UNCHANGED_UNUSED")

print("COUNTS " + " ".join(f"{k}:{v}" for k, v in sorted(counts.items())))
if failures:
    raise SystemExit("FAILURES: " + "; ".join(failures))
print(f"PASS {sum(counts.values())}/{sum(counts.values())}")
