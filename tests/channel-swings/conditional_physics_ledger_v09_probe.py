#!/usr/bin/env python3
"""Append-only, taxonomy, residue and scope checks for ledger v0.9."""

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


v8p = ROOT / "lab/process/conditional-physics-ledger-v0.8.json"
v8vp = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.8.md"
v9p = ROOT / "lab/process/conditional-physics-ledger-v0.9.json"
v9vp = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.9.md"
reportp = ROOT / "explorations/conditional-build/k77-moving-observation-y14-domain-obstruction-2026-08-05.md"
reviewp = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-moving-observation-y14-domain-review.md"
registryp = ROOT / "lab/process/k77-moving-observation-y14-domain-obstruction.json"

v8 = strict(v8p)
v9 = strict(v9p)
registry = strict(registryp)
rows8 = {row["id"]: row for row in v8["rows"]}
rows9 = {row["id"]: row for row in v9["rows"]}
active = {rid: row for rid, row in rows9.items() if row.get("row_status") != "SUPERSEDED"}
view = v9vp.read_text()
report = reportp.read_text()
review = reviewp.read_text()

check("provenance", "v0.8 machine ledger is byte-frozen",
      hashlib.sha256(v8p.read_bytes()).hexdigest()
      == "0ce0687ba11b1789dccb6cfe3f96891ca54504f7912eab221aee47a034b0e9d6")
check("provenance", "v0.8 human view is byte-frozen",
      hashlib.sha256(v8vp.read_bytes()).hexdigest()
      == "6f1105002cc8e9166b94f7136be1dedec85e9a217c92da9b96d8a508a8b4b635")
check("exact", "v0.9 names v0.8 as predecessor",
      v9["schema_version"] == "0.9"
      and v9["predecessor"].endswith("conditional-physics-ledger-v0.8.json"))
check("exact", "row denominator and IDs are unchanged", set(rows8) == set(rows9))
changed = {rid for rid in rows8 if rows8[rid] != rows9[rid]}
check("exact", "only four declared row records changed",
      changed == {"LT-GR2b", "LT-GR2c", "LT-GR5", "LT-GR6"})
check("exact", "the four v0.9 migration edges are explicit",
      {m["row_id"] for m in v9["migrations"] if m.get("to_version") == "0.9"}
      == changed)
check("exact", "82 active targets and 83 provenance rows remain",
      len(active) == 82 and len(rows9) == 83)
check("exact", "axis counts remain 35/21/26",
      Counter(row["axis"] for row in active.values())
      == {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("exact", "verdict counts remain 32/19/25/6",
      Counter(row["verdict"] for row in active.values())
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6})
check("exact", "every active reason kind remains registered",
      all(row["reason_kind"] in v9["taxonomy"]["verdict_kinds"][row["verdict"]]
          for row in active.values()))

check("type", "LT-GR2b keeps partial derivation and moves to observed equation placement",
      rows9["LT-GR2b"]["verdict"] == "SAME"
      and rows9["LT-GR2b"]["reason_kind"] == "DERIVED_PARTIAL"
      and "FIRST_JET_SECTION_GERM" in rows9["LT-GR2b"]["mapping_grade"])
check("type", "LT-GR2c remains NEEDS/MISSING_CONSTRUCTION",
      rows9["LT-GR2c"]["verdict"] == "NEEDS"
      and rows9["LT-GR2c"]["reason_kind"] == "MISSING_CONSTRUCTION")
check("type", "LT-GR2c records no-leakage and the precise ambient-domain horn",
      "FIRST_JET_GERM_NO_LEAKAGE_EXACT" in rows9["LT-GR2c"]["mapping_grade"]
      and "STANDARD_AMBIENT_CAUCHY_HORN_KILLED" in rows9["LT-GR2c"]["mapping_grade"]
      and "PHYSICAL_STRESS_AND_CONSTRAINED_DOMAIN_OPEN" in rows9["LT-GR2c"]["mapping_grade"])
check("type", "LT-GR5 keeps structural difference and names constraint propagation",
      rows9["LT-GR5"]["verdict"] == "DIFFERS"
      and "constraint propagation" in rows9["LT-GR5"]["distance"])
check("type", "LT-GR6 keeps connection current and physical stress separate",
      "up-and-back" in rows9["LT-GR6"]["distance"]
      and "PHYSICAL_UP_AND_BACK_STRESS_OPEN" in rows9["LT-GR6"]["mapping_grade"])

residue = v9["residue"]
check("exact", "global residue is unchanged at 84/19/10/2304",
      residue["continuous_real"] == 84
      and residue["function_valued_at_least"] == 19
      and residue["open_discrete_forks"] == 10
      and residue["open_fork_horn_product"] == 2304)
check("exact", "two prior local/defect quotients remain ranked",
      residue["quotients_ranked"] == 2 and "dimension two" in residue["quotients_ranked_scope"])

observation = registry["observation"]
domain = registry["ambient_domain"]
equations = registry["observed_equations"]
check("exact", "registry records determinant-one first-jet section-germ no-leakage",
      observation["first_jet_determinant"] == 1
      and observation["section_germ_no_leakage"] is True
      and observation["value_only_observation"] == "KILLED")
check("exact", "selected mixed-normal evidence is composed at 85/85/1190",
      observation["selected_mixed_normal_live_directions"] == 85
      and observation["selected_mixed_normal_slice_rank"] == 85
      and observation["selected_full_grade_one_mixed_normal_rank"] == 1190)
check("exact", "finite section jets are not promoted to the global shell",
      registry["global_shell"]["finite_jet_faithful"] is False
      and registry["global_shell"]["bulk_equation_still_independent"] is True)
check("exact", "all three K77 hypersurface inertias are recorded",
      domain["positive_normal_hypersurface_inertia"] == [6, 7, 0]
      and domain["negative_normal_hypersurface_inertia"] == [7, 6, 0]
      and domain["null_normal_hypersurface_inertia"] == [6, 6, 1])
check("type", "only the standard ambient globally-hyperbolic horn is obstructed",
      domain["standard_lorentzian_globally_hyperbolic_route"] == "SHARPLY_OBSTRUCTED"
      and len(domain["revival_horns"]) == 3)
check("type", "observed equation is typed while up-and-back stress stays open",
      "C_S_PLUS_KAPPA1_V" in equations["curvature_distortion_equation"]
      and equations["up_and_back_stress_map"] == "OPEN_SOURCE_DIRECTED")
check("type", "eliminating v is not called Einstein-Hilbert",
      equations["eliminate_v_result"].startswith("CURVATURE_CURRENT_SQUARED"))
check("type", "variable trace is located without a vacuum promotion",
      equations["variable_cosmological_trace_field"] == "LOCATED"
      and equations["nonzero_vacuum_magnitude_screening_wz"] == "OPEN")
check("source", "composed-locus source return is SOURCE-CORRECTS",
      registry["source_return"] == "SOURCE-CORRECTS" and "SOURCE-CORRECTS" in report)
check("hostile", "both mandatory hostile directions and material repairs are present",
      "summary outruns artifact" in review
      and "superseded or mistyped object" in review
      and "section-germ no-leakage" in review
      and "up-and-back" in review)
check("exact", "human and machine meters agree",
      "Ledger v0.9" in view
      and "82/82" in view
      and "84 continuous real before quotient" in view
      and "10 open discrete forks" in view)

dispositions = {row["row_id"]: row for row in v9["wave_row_dispositions"]}
check("exact", "all seven touched rows receive migration or evidence-backed no-change",
      set(dispositions) == {"LT-GR1b", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR5", "LT-GR6", "LT-SM8"}
      and all(dispositions[row]["change"] == "MIGRATED"
              for row in ("LT-GR2b", "LT-GR2c", "LT-GR5", "LT-GR6"))
      and all(dispositions[row]["change"] == "NO_CHANGE"
              for row in ("LT-GR1b", "LT-GR2d", "LT-SM8")))

check("planted", "PLANT the post-Shiab GR1b route remains killed",
      registry["row_dispositions"]["LT-GR1b"].endswith("REMAINS_KILLED"))
check("planted", "PLANT physical positive cohomology remains open",
      registry["row_dispositions"]["LT-SM8"].endswith("POSITIVE_PHYSICAL_COHOMOLOGY_OPEN"))
check("planted", "PLANT no global residue reduction is booked",
      registry["residue"]["global_residue_reduction_booked"] is False)
check("planted", "PLANT P1 P2 P3 remain unused",
      registry["residue"]["P1_P2_P3"] == "UNCHANGED_UNUSED")

print("COUNTS " + " ".join(f"{k}:{v}" for k, v in sorted(counts.items())))
if failures:
    raise SystemExit("FAILURES: " + "; ".join(failures))
print(f"PASS {sum(counts.values())}/{sum(counts.values())}")
