#!/usr/bin/env python3
"""Append-only and typed-scope checks for conditional physics ledger v0.14."""

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


v13p = ROOT / "lab/process/conditional-physics-ledger-v0.13.json"
v14p = ROOT / "lab/process/conditional-physics-ledger-v0.14.json"
v13 = strict(v13p)
v14 = strict(v14p)
registry = strict(ROOT / "lab/process/selected-branch-bv-tt-curvature-vev-flrw.json")
rows13 = {row["id"]: row for row in v13["rows"]}
rows14 = {row["id"]: row for row in v14["rows"]}
active = {rid: row for rid, row in rows14.items() if row.get("row_status") != "SUPERSEDED"}
changed = {rid for rid in rows13 if rows13[rid] != rows14[rid]}
migrations = [item for item in v14["migrations"] if item.get("to_version") == "0.14"]
expected = {"LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR2e", "LT-GR3", "LT-GR5", "LT-GR6"}

check("provenance", "v0.13 machine ledger is byte-frozen",
      hashlib.sha256(v13p.read_bytes()).hexdigest()
      == "7e910115077e45d9b0d4e28f8237514bdb9792b65f684f1af4deac0c3af88677")
check("exact", "v0.14 names v0.13 as predecessor",
      v14["schema_version"] == "0.14" and v14["predecessor"].endswith("v0.13.json"))
check("exact", "row denominator and IDs are unchanged", set(rows13) == set(rows14))
check("exact", "exactly eight declared row records changed", changed == expected)
check("exact", "the eight v0.14 migration edges are explicit",
      {item["row_id"] for item in migrations} == expected and len(migrations) == 8)
check("exact", "82 active targets and 83 provenance rows remain",
      len(active) == 82 and len(rows14) == 83)
check("exact", "axis counts remain 35/21/26",
      Counter(row["axis"] for row in active.values())
      == {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("exact", "verdict counts remain 33/19/24/6",
      Counter(row["verdict"] for row in active.values())
      == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6})
check("exact", "every active reason kind remains registered",
      all(row["reason_kind"] in v14["taxonomy"]["verdict_kinds"][row["verdict"]]
          for row in active.values()))

check("type", "LT-GR1 records gauge-rotated LC soldering only modulo gauge",
      "SOLDERING_MOD_GAUGE_EXACT" in rows14["LT-GR1"]["mapping_grade"]
      and "FULL_NONLINEAR_ODD_COHOMOLOGY_OPEN" in rows14["LT-GR1"]["mapping_grade"])
check("type", "LT-GR2b separates finite tree positivity from ultraviolet stability",
      "FINITE_TREE_KREIN_MAJORANT_POSITIVE" in rows14["LT-GR2b"]["mapping_grade"]
      and "ODD_LOOP_UV_STABILITY_OPEN" in rows14["LT-GR2b"]["mapping_grade"])
check("type", "LT-GR2c records local tracking and ambient horn openness",
      "LOCAL_SCALAR_CURVATURE_VEV_TWO_TO_ONE_EXACT" in rows14["LT-GR2c"]["mapping_grade"]
      and "AMBIENT_GLOBAL_HORN_OPEN" in rows14["LT-GR2c"]["mapping_grade"])
check("type", "LT-GR2d records nonzero shift susceptibility",
      "SHIFT_SUSCEPTIBILITY_2_OVER_A_NONSCREENING" in rows14["LT-GR2d"]["mapping_grade"])
check("type", "LT-GR2e fences spatial flatness from four-curvature",
      "SPATIAL_FLATNESS_HOMONYM_FENCED" in rows14["LT-GR2e"]["mapping_grade"]
      and "PERTURBATIONS_AND_WZ_OPEN" in rows14["LT-GR2e"]["mapping_grade"])
check("type", "LT-GR3 records at least two even-BV TT classes and leaves UV open",
      "MASSIVE_EVEN_BV_TT_CLASSES_AT_LEAST_TWO" in rows14["LT-GR3"]["mapping_grade"]
      and "ODD_LOOP_UV_OPEN" in rows14["LT-GR3"]["mapping_grade"])
check("type", "LT-GR6 instantiates only the linear defect soldering chain",
      "DIRECT_PLUS_SOLDERED_CHAIN_INSTANTIATED_LINEAR_DEFECT" in rows14["LT-GR6"]["mapping_grade"]
      and "NONLINEAR_CHIMERIC_ODD_OPEN" in rows14["LT-GR6"]["mapping_grade"])

exact = registry["exact_results"]
check("exact", "metric-to-Levi-Civita symbol rank is ten",
      exact["metric_to_levi_civita_symbol_rank"] == 10)
check("exact", "massive partner has two even-BV TT classes",
      exact["massive_partner_even_bv_tt_classes"] == 2)
check("exact", "finite spectral parity and majorant determinant are exact",
      exact["spectral_parity"] == "I+2L/m_squared"
      and exact["majorant_determinant"] == 1)
check("exact", "local curvature and distortion share one source amplitude",
      exact["constant_curvature"] == "2*rho_vac/a"
      and exact["constant_distortion"] == "-2*beta*rho_vac/(a*kappa)")
check("exact", "local shift susceptibility is nonzero",
      exact["curvature_shift_susceptibility"] == "2/a")
check("source", "the source disposition is narrowly SOURCE-CONFIRMS",
      registry["source_return"] == "SOURCE-CONFIRMS")
check("type", "local screening fails while ambient/global horn remains open",
      registry["boundaries"]["radiative_screening_local_horn"] == "FAILS"
      and registry["boundaries"]["ambient_global_nonlocal_cosmology_horn"] == "OPEN")
check("type", "odd cohomology, full multiplet, loop/RG and w(z) remain open",
      all(registry["boundaries"][key] == "OPEN" for key in (
          "full_odd_super_ig_cohomology", "full_massive_multiplet",
          "loop_rg_majorant", "action_owned_w_of_z")))
check("type", "external P1/P2/P3 remain unused",
      set(registry["external_datum"].values()) == {"UNUSED"})

residue = v14["residue"]
check("exact", "global residue and fork count are unchanged",
      residue["continuous_real"] == 84
      and residue["function_valued_at_least"] == 19
      and residue["open_discrete_forks"] == 9
      and residue["open_fork_horn_product"] == 1152)
check("exact", "only the scoped massive TT quotient is newly ranked",
      residue["quotients_ranked"] == 3
      and "lower bound of two non-exact classes" in residue["quotients_ranked_scope"]
      and "booked as global residue reduction" in residue["quotients_ranked_scope"])

check("planted", "PLANT local tracking is not local screening",
      exact["curvature_shift_susceptibility"] != "0")
check("planted", "PLANT spatially flat does not assert four-curvature zero",
      "SPATIAL_FLATNESS_NOT_R4" in rows14["LT-GR2c"]["mapping_grade"])
check("planted", "PLANT even-BV TT is not full odd cohomology",
      registry["exact_results"]["massive_partner_even_bv_tt_classes"] > 0
      and registry["boundaries"]["full_odd_super_ig_cohomology"] == "OPEN")
check("planted", "PLANT finite tree majorant is not loop/RG closure",
      exact["majorant_determinant"] == 1
      and registry["boundaries"]["loop_rg_majorant"] == "OPEN")

print("COUNTS " + " ".join(f"{kind}:{count}" for kind, count in sorted(counts.items())))
if failures:
    raise SystemExit("FAILURES: " + "; ".join(failures))
print(f"PASS {sum(counts.values())}/{sum(counts.values())}")
