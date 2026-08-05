#!/usr/bin/env python3
"""Append-only and selected-K77/P2-norm checks for ledger v0.12."""

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


v11p = ROOT / "lab/process/conditional-physics-ledger-v0.11.json"
v12p = ROOT / "lab/process/conditional-physics-ledger-v0.12.json"
v11 = strict(v11p)
v12 = strict(v12p)
registry = strict(ROOT / "lab/process/selected-moving-k77-vacuum-p2-norm-placement.json")
rows11 = {row["id"]: row for row in v11["rows"]}
rows12 = {row["id"]: row for row in v12["rows"]}
active = {rid: row for rid, row in rows12.items() if row.get("row_status") != "SUPERSEDED"}
changed = {rid for rid in rows11 if rows11[rid] != rows12[rid]}
migrations = [m for m in v12["migrations"] if m.get("to_version") == "0.12"]
expected = {"LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR3", "LT-GR5", "LT-GR6"}

check("provenance", "v0.11 machine ledger is byte-frozen",
      hashlib.sha256(v11p.read_bytes()).hexdigest()
      == "9495e1279ef26dfb4360ad36ce4240ae44b804d91c42312a897be807486ce954")
check("exact", "v0.12 names v0.11 as predecessor",
      v12["schema_version"] == "0.12" and v12["predecessor"].endswith("v0.11.json"))
check("exact", "row denominator and IDs are unchanged", set(rows11) == set(rows12))
check("exact", "exactly seven declared row records changed", changed == expected)
check("exact", "the seven v0.12 migration edges are explicit",
      {m["row_id"] for m in migrations} == expected)
check("exact", "82 active targets and 83 provenance rows remain",
      len(active) == 82 and len(rows12) == 83)
check("exact", "axis counts remain 35/21/26",
      Counter(row["axis"] for row in active.values())
      == {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("exact", "verdict counts move to 33/19/24/6",
      Counter(row["verdict"] for row in active.values())
      == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6})
check("exact", "every active reason kind remains registered",
      all(row["reason_kind"] in v12["taxonomy"]["verdict_kinds"][row["verdict"]]
          for row in active.values()))

check("type", "LT-GR1 moves from one-bit need to a scoped derived match",
      rows11["LT-GR1"]["verdict"] == "NEEDS"
      and rows12["LT-GR1"]["verdict"] == "SAME"
      and rows12["LT-GR1"]["reason_kind"] == "DERIVED_CONDITIONAL"
      and "P2_NORM_FULL_II_DERIVED" in rows12["LT-GR1"]["mapping_grade"])
check("type", "LT-GR2b records selected-action algebraic stationarity only",
      "SELECTED_NONCYCLIC_K77_NONZERO_ALGEBRAIC_STATIONARY_BRANCH_EXACT"
      in rows12["LT-GR2b"]["mapping_grade"]
      and "STABILITY_AND_DOMAIN_OPEN" in rows12["LT-GR2b"]["mapping_grade"])
check("type", "LT-GR2c carries construction-selected full II but open totalization/domain",
      "CANONICAL_GAUSS_FULL_II_NORM_SELECTED" in rows12["LT-GR2c"]["mapping_grade"]
      and "TOTALIZATION_CURRENT_AND_DOMAIN_OPEN" in rows12["LT-GR2c"]["mapping_grade"])
check("type", "LT-GR2d records the radial Hessian without claiming stability",
      "RADIAL_HESSIAN_MINUS_14_KAPPA_1" in rows12["LT-GR2d"]["mapping_grade"]
      and "PHYSICAL_STABILITY" in rows12["LT-GR2d"]["mapping_grade"])
check("type", "LT-GR3 preserves the selected distinct massive partner",
      "SELECTS_DISTINCT_MASSIVE_POLE" in rows12["LT-GR3"]["mapping_grade"])
check("type", "LT-GR6 keeps source totalization/current open",
      "SOURCE_TOTALIZATION_CURRENT_AND_DOMAIN_OPEN" in rows12["LT-GR6"]["mapping_grade"])

gauss = registry["gauss_norm"]
vacuum = registry["selected_vacuum"]
check("exact", "canonical Gauss receiver selects full II rather than trace first",
      gauss["receiver_rank"] == 100
      and gauss["full_ii_quadratic_rank"] == 100
      and gauss["trace_first_quadratic_rank"] == 10
      and gauss["traceless_directions_lost_by_trace"] == 90)
check("exact", "receiver insertion and action projector close exactly",
      gauss["insertion_right_inverse"] is True
      and gauss["projector_rank"] == 100
      and gauss["projector_orthogonal_for_action_pairing"] is True)
check("exact", "P2_norm is derived with zero new free objects",
      gauss["p2_norm_status"] == "DERIVED_FULL_II_ON_CANONICAL_GAUSS_SECTOR"
      and gauss["new_field_delta"] == gauss["new_datum_delta"] == gauss["fitted_coefficient_delta"] == 0)
check("exact", "selected action coefficient and branch include the one-third eddy",
      vacuum["raw_cubic_coefficient"] == 4368
      and vacuum["path_average_cubic_coefficient"] == 1456
      and vacuum["mass_norm"] == 14
      and vacuum["selected_nonzero_branch"] == "t=-kappa_1/312")
check("exact", "full algebraic gradient and moving epsilon orbit vanish",
      vacuum["grade1_translation_derivatives"] == "196/196_ZERO"
      and vacuum["grade13_translation_derivatives"] == "196/196_ZERO"
      and vacuum["moving_epsilon_orbit_derivative"] == "ZERO")
check("exact", "special printed-endpoint coincidence is not a global identity",
      vacuum["printed_endpoint_on_branch"] == "ZERO_SPECIAL_COINCIDENCE_LOCUS"
      and vacuum["printed_endpoint_global_identity"] is False)
check("type", "algebraic stationarity is not promoted to physical stability",
      vacuum["radial_hessian"] == "-14*kappa_1"
      and vacuum["stable_physical_vacuum"] == "OPEN")
check("source", "source supplies ingredients while repo derives the composition",
      registry["source_return"] == "SOURCE-CONFIRMS_INGREDIENTS__REPO_DERIVES_COMPOSITION")
check("type", "P2 datum homonym stays separate and unused",
      registry["layer0"]["p2_datum"] == "EXTERNAL_DATUM_LEDGER_OBJECT__UNCHANGED_UNUSED"
      and registry["residue"]["external_P1_P2_P3"] == "UNCHANGED_UNUSED")

residue = v12["residue"]
check("exact", "one binary fork retires while continuous/functions stay fixed",
      residue["continuous_real"] == 84
      and residue["function_valued_at_least"] == 19
      and residue["open_discrete_forks"] == 9
      and residue["open_fork_horn_product"] == 1152)
check("exact", "two local/defect quotients remain unbooked globally",
      residue["quotients_ranked"] == 2)

check("planted", "PLANT equal target dimension does not identify the two receivers",
      registry["layer0"]["horizontal_gauss_receiver"]
      != registry["layer0"]["vertical_q_receiver"])
check("planted", "PLANT P2_norm closure does not close P2_datum",
      registry["layer0"]["p2_norm"] != registry["layer0"]["p2_datum"])
check("planted", "PLANT algebraic stationary is not physical vacuum",
      registry["layer0"]["algebraic_stationary"]
      != registry["layer0"]["physical_vacuum"])
check("planted", "PLANT branch coincidence does not restore printed Euler globally",
      vacuum["printed_endpoint_global_identity"] is False)
check("planted", "PLANT physical residue is not booked",
      registry["residue"]["global_physical_residue_reduction"] is False)

print("COUNTS " + " ".join(f"{k}:{v}" for k, v in sorted(counts.items())))
if failures:
    raise SystemExit("FAILURES: " + "; ".join(failures))
print(f"PASS {sum(counts.values())}/{sum(counts.values())}")
