#!/usr/bin/env python3
"""Append-only, taxonomy, residue, source and adverse-physics checks for ledger v0.10."""

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


v9p = ROOT / "lab/process/conditional-physics-ledger-v0.9.json"
v10p = ROOT / "lab/process/conditional-physics-ledger-v0.10.json"
v9 = strict(v9p)
v10 = strict(v10p)
registry = strict(ROOT / "lab/process/observed-upback-stress-normal-constraint-vacuum.json")
rows9 = {row["id"]: row for row in v9["rows"]}
rows10 = {row["id"]: row for row in v10["rows"]}
active = {rid: row for rid, row in rows10.items() if row.get("row_status") != "SUPERSEDED"}
changed = {rid for rid in rows9 if rows9[rid] != rows10[rid]}
migrations = [m for m in v10["migrations"] if m.get("to_version") == "0.10"]

check("provenance", "v0.9 machine ledger is byte-frozen",
      hashlib.sha256(v9p.read_bytes()).hexdigest()
      == "0ae17658c90f52895a76cd7bbba4079f3074ed40560a97f8efb682da6c0fdc66")
check("exact", "v0.10 names v0.9 as predecessor",
      v10["schema_version"] == "0.10" and v10["predecessor"].endswith("v0.9.json"))
check("exact", "row denominator and IDs are unchanged", set(rows9) == set(rows10))
check("exact", "exactly five declared row records changed",
      changed == {"LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR5", "LT-GR6"})
check("exact", "the five v0.10 migration edges are explicit",
      {m["row_id"] for m in migrations} == changed)
check("exact", "82 active targets and 83 provenance rows remain",
      len(active) == 82 and len(rows10) == 83)
check("exact", "axis counts remain 35/21/26",
      Counter(row["axis"] for row in active.values())
      == {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("exact", "verdict counts remain 32/19/25/6",
      Counter(row["verdict"] for row in active.values())
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6})
check("exact", "every active reason kind remains registered",
      all(row["reason_kind"] in v10["taxonomy"]["verdict_kinds"][row["verdict"]]
          for row in active.values()))

check("type", "LT-GR2b is a partial located field, not a selected vacuum",
      rows10["LT-GR2b"]["verdict"] == "SAME"
      and rows10["LT-GR2b"]["reason_kind"] == "DERIVED_PARTIAL"
      and "ZERO_INDEFINITE_ONLY" in rows10["LT-GR2b"]["mapping_grade"])
check("type", "LT-GR2c records exact stress and the adverse pole",
      rows10["LT-GR2c"]["reason_kind"] == "MISSING_CONSTRUCTION"
      and "ACTION_HILBERT_STRESS_EXACT" in rows10["LT-GR2c"]["mapping_grade"]
      and "DOUBLE_POLE" in rows10["LT-GR2c"]["mapping_grade"])
lt_gr2d_migration = next((m for m in migrations if m.get("row_id") == "LT-GR2d"), {})
check("type", "LT-GR2d is scope-corrected rather than over-fenced",
      rows10["LT-GR2d"]["reason_kind"] == "MISSING_CONSTRUCTION"
      and lt_gr2d_migration.get("meaning_changed") is True)
check("type", "LT-GR5 retains the generalized propagation partner",
      "GENERALIZED_DOUBLE_POLE_PARTNER_REMAINS" in rows10["LT-GR5"]["mapping_grade"])
check("type", "LT-GR6 separates Hilbert stress, literal VU, current and totalization",
      "RADIAL_TRANSGRESSION_EXACT" in rows10["LT-GR6"]["mapping_grade"]
      and "LITERAL_VU_KILLED" in rows10["LT-GR6"]["mapping_grade"])

check("exact", "stress construction adds no free object",
      registry["stress"]["free_object_delta"] == 0)
check("exact", "observed constraints retain plus/cross dimension two",
      registry["observed_constraints"]["characteristic_kernel_dimension"] == 10
      and registry["observed_constraints"]["constraint_compatible_dimension"] == 6
      and registry["observed_constraints"]["physical_quotient_dimension"] == 2)
check("exact", "repaired metric response is a double pole",
      registry["propagator"]["determinant"] == "-z^2"
      and registry["propagator"]["pole_order"] == 2
      and registry["propagator"]["einstein_single_pole"] is False)
check("exact", "quadratic vacuum is zero and indefinite",
      registry["vacuum"]["unshifted_stationary_solution"] == "V_EQUALS_ZERO_ONLY"
      and registry["vacuum"]["stationary_hessian_inertia"] == [6, 4]
      and registry["vacuum"]["stable_minimum"] is False)
check("type", "full nonlinear vacuum remains open",
      registry["vacuum"]["full_nonlinear_T_cubic"] == "OPEN"
      and registry["vacuum"]["magnitude_wz"] == "OPEN")
check("source", "source return corrects rather than releases a formula",
      registry["source_return"] == "SOURCE-CORRECTS"
      and registry["stress"]["source_totalization_equality"] == "OPEN_SOURCE_BOUNDED_RECONSTRUCTION")

residue = v10["residue"]
check("exact", "global residue remains 84/19/10/2304",
      residue["continuous_real"] == 84
      and residue["function_valued_at_least"] == 19
      and residue["open_discrete_forks"] == 10
      and residue["open_fork_horn_product"] == 2304)
check("exact", "two local/defect quotients remain unbooked globally",
      residue["quotients_ranked"] == 2 and not registry["residue"]["global_residue_reduction_booked"])

check("planted", "PLANT literal VU is not nonlinear stress",
      registry["stress"]["literal_VU_equals_stress"] is False)
check("planted", "PLANT connection current equality remains unclaimed",
      registry["stress"]["connection_current_equality"].startswith("OPEN"))
check("planted", "PLANT a two-mode quotient is not a one-pole theorem",
      registry["observed_constraints"]["physical_quotient_dimension"] == 2
      and registry["propagator"]["pole_order"] != 1)
check("planted", "PLANT tracked shifts are not screening",
      registry["vacuum"]["independent_trace_shift"] == "LINEARLY_TRACKED_NOT_SCREENED")
check("planted", "PLANT P1 P2 P3 remain unused",
      registry["residue"]["P1_P2_P3"] == "UNCHANGED_UNUSED")

print("COUNTS " + " ".join(f"{k}:{v}" for k, v in sorted(counts.items())))
if failures:
    raise SystemExit("FAILURES: " + "; ".join(failures))
print(f"PASS {sum(counts.values())}/{sum(counts.values())}")
