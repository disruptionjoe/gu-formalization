#!/usr/bin/env python3
"""Append-only, target-correction and nonlinear-vacuum checks for ledger v0.11."""

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


v10p = ROOT / "lab/process/conditional-physics-ledger-v0.10.json"
v11p = ROOT / "lab/process/conditional-physics-ledger-v0.11.json"
v10 = strict(v10p)
v11 = strict(v11p)
registry = strict(ROOT / "lab/process/full-norm-pole-split-nonlinear-t-vacuum.json")
rows10 = {row["id"]: row for row in v10["rows"]}
rows11 = {row["id"]: row for row in v11["rows"]}
active = {rid: row for rid, row in rows11.items() if row.get("row_status") != "SUPERSEDED"}
changed = {rid for rid in rows10 if rows10[rid] != rows11[rid]}
migrations = [m for m in v11["migrations"] if m.get("to_version") == "0.11"]

check("provenance", "v0.10 machine ledger is byte-frozen",
      hashlib.sha256(v10p.read_bytes()).hexdigest()
      == "e9fe118810f1ed5915d1cae37d27b0a4ce1cadf69542924f1667584790a29040")
check("exact", "v0.11 names v0.10 as predecessor",
      v11["schema_version"] == "0.11" and v11["predecessor"].endswith("v0.10.json"))
check("exact", "row denominator and IDs are unchanged", set(rows10) == set(rows11))
expected = {"LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR3", "LT-GR5", "LT-GR6"}
check("exact", "exactly seven declared row records changed", changed == expected)
check("exact", "the seven v0.11 migration edges are explicit",
      {m["row_id"] for m in migrations} == expected)
check("exact", "82 active targets and 83 provenance rows remain",
      len(active) == 82 and len(rows11) == 83)
check("exact", "axis counts remain 35/21/26",
      Counter(row["axis"] for row in active.values())
      == {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("exact", "verdict counts remain 32/19/25/6",
      Counter(row["verdict"] for row in active.values())
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6})
check("exact", "every active reason kind remains registered",
      all(row["reason_kind"] in v11["taxonomy"]["verdict_kinds"][row["verdict"]]
          for row in active.values()))

check("type", "LT-GR1 retains P2 as one bit rather than treating the horn as selected",
      rows11["LT-GR1"]["reason_kind"] == "ONE_BIT"
      and "P2_ACTION_SELECTION_OPEN" in rows11["LT-GR1"]["mapping_grade"])
check("type", "LT-GR2c carries the corrected massless-plus-massive target",
      "MASSLESS_PLUS_MASSIVE_SIMPLE_POLES" in rows11["LT-GR2c"]["mapping_grade"]
      and "corrected target" in rows11["LT-GR2c"]["distance"])
check("type", "LT-GR2d records nonlinear saddles but selected K77 remains open",
      "TWO_NONABELIAN_REAL_BRANCHES_BOTH_SADDLES" in rows11["LT-GR2d"]["mapping_grade"]
      and "SELECTED_K77" in rows11["LT-GR2d"]["mapping_grade"])
check("type", "LT-GR3 preserves rather than erases the massive partner",
      "DISTINCT_MASSIVE_POLE" in rows11["LT-GR3"]["mapping_grade"])
check("type", "LT-GR6 keeps source totalization/current open",
      "SOURCE_TOTALIZATION_CURRENT_AND_DOMAIN_OPEN" in rows11["LT-GR6"]["mapping_grade"])

gravity = registry["gravity"]
vacuum = registry["nonlinear_vacuum_control"]
check("exact", "conditional full-norm response has two distinct simple poles",
      gravity["full_norm_conditional_determinant"] == "z*(alpha_II*kappa_1-z)"
      and gravity["pole_count"] == 2 and gravity["pole_multiplicity"] == [1, 1])
check("exact", "massless Einstein pole and plus/cross are retained",
      gravity["massless_residue"] == "1/alpha_II" and gravity["plus_cross_retained"] is True)
check("exact", "no new field or datum was added",
      gravity["new_field_delta"] == 0 and gravity["new_datum_delta"] == 0)
check("exact", "cyclic control has two genuine nonlinear real branches",
      vacuum["real_stationary_branch_count"] == 3
      and vacuum["genuinely_nonlinear_real_branch_count"] == 2)
check("exact", "nonlinear branches are nondegenerate saddles",
      vacuum["hessian_nonzero_resultant"] == -5439488
      and vacuum["stable_minimum_found"] is False)
check("source", "source is silent on P2 and total pole count",
      registry["source_return"] == "SOURCE-SILENT"
      and gravity["p2_action_norm_selection"] == "OPEN_SOURCE_SILENT")
check("type", "selected moving-K77 vacuum remains open",
      vacuum["selected_moving_k77_frechet_adjoint_vacuum"] == "OPEN")

residue = v11["residue"]
check("exact", "global residue remains 84/19/10/2304",
      residue["continuous_real"] == 84
      and residue["function_valued_at_least"] == 19
      and residue["open_discrete_forks"] == 10
      and residue["open_fork_horn_product"] == 2304)
check("exact", "two local/defect quotients remain unbooked globally",
      residue["quotients_ranked"] == 2)

check("planted", "PLANT one Einstein pole does not mean one pole total",
      registry["layer0"]["einstein_recovery"] != registry["layer0"]["orthodox_gr_target"])
check("planted", "PLANT a stationary branch is not called a stable vacuum",
      vacuum["stable_minimum_found"] is False)
check("planted", "PLANT cyclic control is not selected K77",
      registry["layer0"]["cyclic_control_vs_selected_k77"] == "DISTINCT")
check("planted", "PLANT no P1 P2 P3 movement",
      registry["residue"]["P1_P2_P3"] == "UNCHANGED_UNUSED")

print("COUNTS " + " ".join(f"{k}:{v}" for k, v in sorted(counts.items())))
if failures:
    raise SystemExit("FAILURES: " + "; ".join(failures))
print(f"PASS {sum(counts.values())}/{sum(counts.values())}")
