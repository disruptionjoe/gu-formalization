#!/usr/bin/env python3
"""Append-only and selected-branch/domain checks for ledger v0.13."""

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


v12p = ROOT / "lab/process/conditional-physics-ledger-v0.12.json"
v13p = ROOT / "lab/process/conditional-physics-ledger-v0.13.json"
v12 = strict(v12p)
v13 = strict(v13p)
registry = strict(ROOT / "lab/process/selected-branch-linearized-totalization-current-green-domain.json")
rows12 = {row["id"]: row for row in v12["rows"]}
rows13 = {row["id"]: row for row in v13["rows"]}
active = {rid: row for rid, row in rows13.items() if row.get("row_status") != "SUPERSEDED"}
changed = {rid for rid in rows12 if rows12[rid] != rows13[rid]}
migrations = [item for item in v13["migrations"] if item.get("to_version") == "0.13"]
expected = {"LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR3", "LT-GR5", "LT-GR6"}

check("provenance", "v0.12 machine ledger is byte-frozen",
      hashlib.sha256(v12p.read_bytes()).hexdigest()
      == "5c21f4785415f94ce67c47b4570f4c5028124418c6083b414531194eea8ab7a3")
check("exact", "v0.13 names v0.12 as predecessor",
      v13["schema_version"] == "0.13" and v13["predecessor"].endswith("v0.12.json"))
check("exact", "row denominator and IDs are unchanged", set(rows12) == set(rows13))
check("exact", "exactly seven declared row records changed", changed == expected)
check("exact", "the seven v0.13 migration edges are explicit",
      {item["row_id"] for item in migrations} == expected)
check("exact", "82 active targets and 83 provenance rows remain",
      len(active) == 82 and len(rows13) == 83)
check("exact", "axis counts remain 35/21/26",
      Counter(row["axis"] for row in active.values())
      == {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("exact", "verdict counts remain 33/19/24/6",
      Counter(row["verdict"] for row in active.values())
      == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6})
check("exact", "every active reason kind remains registered",
      all(row["reason_kind"] in v13["taxonomy"]["verdict_kinds"][row["verdict"]]
          for row in active.values()))

check("type", "LT-GR1 retains the massless pole on the common defect domain",
      "MASSLESS_POLE_ON_COMMON_DEFECT_KREIN_GREEN_DOMAIN" in rows13["LT-GR1"]["mapping_grade"])
check("type", "LT-GR2b separates the Gauss Hessian from radial stability",
      "GAUSS_TRACE_AND_TRACELESS_HESSIANS_EXACT" in rows13["LT-GR2b"]["mapping_grade"]
      and "PHYSICAL_STABILITY_OPEN" in rows13["LT-GR2b"]["mapping_grade"])
check("type", "LT-GR2c records the common domain but keeps two-field identification open",
      "COMMON_DEFECT_KREIN_GREEN_DOMAIN" in rows13["LT-GR2c"]["mapping_grade"]
      and "TWO_FIELD_IDENTIFICATION" in rows13["LT-GR2c"]["mapping_grade"])
check("type", "LT-GR2d keeps direct susceptibility distinct from the two-field test",
      "DIRECT_SOURCE_SUSCEPTIBILITY" in rows13["LT-GR2d"]["mapping_grade"]
      and "TWO_FIELD_CURVATURE_VEV" in rows13["LT-GR2d"]["mapping_grade"])
check("type", "LT-GR3 records exact mass and opposite residues",
      "MASS_SQUARED_124_ALPHA_KAPPA_OVER_117" in rows13["LT-GR3"]["mapping_grade"]
      and "OPPOSITE_RESIDUES_EXACT" in rows13["LT-GR3"]["mapping_grade"])
check("type", "LT-GR6 records the direct-plus-soldered chain and source correction",
      "DIRECT_PLUS_SOLDERED_CURRENT_CHAIN_TYPED" in rows13["LT-GR6"]["mapping_grade"]
      and "SOURCE_CORRECTS_LITERAL_UPBACK_EQUALITY" in rows13["LT-GR6"]["mapping_grade"])

exact = registry["exact_results"]
check("exact", "selected branch Gauss coefficients are exact",
      exact["gauss_trace_coefficient"] == "100/117*kappa_1"
      and exact["gauss_traceless_coefficient"] == "124/117*kappa_1")
check("exact", "partner mass and residues are recorded exactly",
      exact["tt_mass_squared"] == "124/117*alpha_II*kappa_1"
      and exact["tt_residues"] == ["1/alpha_II", "-1/alpha_II"])
check("exact", "common defect domain is closed without ambient promotion",
      registry["domain"]["closed_grade"]
      == "coupled normally-hyperbolic observed defect Krein/Green complex"
      and registry["domain"]["ambient_y14_domain"] == "OPEN")
check("source", "the composed source disposition is SOURCE-CORRECTS",
      registry["source_return"] == "SOURCE-CORRECTS")
check("type", "physical cohomology remains open",
      registry["domain"]["positive_physical_cohomology"] == "OPEN")
check("type", "external P1/P2/P3 remain unused",
      set(registry["external_datum"].values()) == {"UNUSED"})

residue = v13["residue"]
check("exact", "residue and fork count are unchanged",
      residue["continuous_real"] == 84
      and residue["function_valued_at_least"] == 19
      and residue["open_discrete_forks"] == 9
      and residue["open_fork_horn_product"] == 1152)
check("exact", "no global physical quotient is silently booked",
      residue["quotients_ranked"] == 2)

check("planted", "PLANT radial and Gauss coefficients are not conflated",
      exact["cl1_sector_coefficients"][0] != exact["gauss_traceless_coefficient"].split("*")[0])
check("planted", "PLANT common Green domain is not positive physical cohomology",
      registry["domain"]["closed_grade"] != registry["domain"]["positive_physical_cohomology"])
check("planted", "PLANT direct susceptibility does not close two-field cosmology",
      "TWO_FIELD" in registry["next_gate"])

print("COUNTS " + " ".join(f"{kind}:{count}" for kind, count in sorted(counts.items())))
if failures:
    raise SystemExit("FAILURES: " + "; ".join(failures))
print(f"PASS {sum(counts.values())}/{sum(counts.values())}")
