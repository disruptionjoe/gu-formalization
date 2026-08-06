#!/usr/bin/env python3
"""Append-only and typed-scope checks for conditional physics ledger v0.15."""

from collections import Counter
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
counts = Counter()
failures = []


def strict(path):
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key in {path}")
        return dict(items)
    return json.loads(path.read_text(), object_pairs_hook=pairs)


def check(kind, label, condition):
    counts[kind] += 1
    if not condition:
        failures.append(label)
    print(f"{'PASS' if condition else 'FAIL'} [{kind}] {label}")


v14p = ROOT / "lab/process/conditional-physics-ledger-v0.14.json"
v15p = ROOT / "lab/process/conditional-physics-ledger-v0.15.json"
v14 = strict(v14p)
v15 = strict(v15p)
registry = strict(ROOT / "lab/process/first-interaction-krein-global-zero-mode.json")
rows14 = {row["id"]: row for row in v14["rows"]}
rows15 = {row["id"]: row for row in v15["rows"]}
active = {rid: row for rid, row in rows15.items() if row.get("row_status") != "SUPERSEDED"}
changed = {rid for rid in rows14 if rows14[rid] != rows15[rid]}
migrations = [item for item in v15["migrations"] if item.get("to_version") == "0.15"]
expected = {"LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR3", "LT-GR5", "LT-SM8"}

check("provenance", "v0.14 machine ledger is byte-frozen",
      hashlib.sha256(v14p.read_bytes()).hexdigest()
      == "6bee3c8a18597f29ac7c2a202333bc7b2bfdae18d63ba839d3580ff695d84939")
check("exact", "v0.15 names v0.14 as predecessor",
      v15["schema_version"] == "0.15" and v15["predecessor"].endswith("v0.14.json"))
check("exact", "row denominator and IDs are unchanged", set(rows14) == set(rows15))
check("exact", "exactly six declared row records changed", changed == expected)
check("exact", "the six v0.15 migration edges are explicit",
      {item["row_id"] for item in migrations} == expected and len(migrations) == 6)
check("exact", "82 active targets and 83 provenance rows remain",
      len(active) == 82 and len(rows15) == 83)
check("exact", "axis counts remain 35/21/26",
      Counter(row["axis"] for row in active.values())
      == {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("exact", "verdict counts remain 33/19/24/6",
      Counter(row["verdict"] for row in active.values())
      == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6})
check("exact", "every active reason kind remains registered",
      all(row["reason_kind"] in v15["taxonomy"]["verdict_kinds"][row["verdict"]]
          for row in active.values()))

check("type", "LT-GR2b records free parity failure without killing interacting C",
      "SCALAR_SIGN_EXTENSION_FAILS_FIRST_CUBIC" in rows15["LT-GR2b"]["mapping_grade"]
      and "INTERACTING_C_OPEN" in rows15["LT-GR2b"]["mapping_grade"])
check("type", "LT-GR2c closes the finite local constant-mode class and keeps datum owner open",
      "FINITE_LOCAL_CONSTANT_MODE_COMPLETIONS_NOSCREEN_OR_UNSOLVABLE" in rows15["LT-GR2c"]["mapping_grade"]
      and "DOMAIN_MEASURE_OWNER_OPEN" in rows15["LT-GR2c"]["mapping_grade"])
check("type", "LT-GR2d records exact conditional screening without P2 identification",
      "CONDITIONAL_GLOBAL_Q_SHIFT_SUSCEPTIBILITY_ZERO" in rows15["LT-GR2d"]["mapping_grade"]
      and "OPEN_NOT_P2" in rows15["LT-GR2d"]["mapping_grade"])
check("type", "LT-GR3 sends positivity to interacting C",
      "FIRST_CUBIC_SCALAR_SIGN_EXTENSION_KILLED" in rows15["LT-GR3"]["mapping_grade"]
      and "INTERACTING_C_LOOP_UV_OPEN" in rows15["LT-GR3"]["mapping_grade"])
check("type", "LT-SM8 separates super-IG descent from odd action",
      "SUPER_IG_REBASED_TO_ALGEBRAIC_GLOBAL_DESCENT_NOT_ODD_ACTION" in rows15["LT-SM8"]["mapping_grade"])

check("source", "the decisive source return is SOURCE-CORRECTS",
      registry["source_return"] == "SOURCE-CORRECTS")
check("exact", "the simple free parity extension is killed",
      registry["result"]["free_spectral_parity"].startswith("NO_MULTIPLICATIVE_SCALAR_SIGN_EXTENSION"))
check("type", "the interacting C-operator remains open",
      registry["result"]["interacting_c_operator"] == "OPEN")
check("exact", "the finite local constant-mode dichotomy is registered",
      "K0_NONZERO" in registry["result"]["finite_local_constant_mode"]
      and "K0_ZERO" in registry["result"]["finite_local_constant_mode"])
check("exact", "the conditional global horn requires the normalized functional",
      registry["result"]["global_projector_horn"]
      == "EXACT_CONDITIONAL_ON_NORMALIZED_DOMAIN_MEASURE_FUNCTIONAL")
check("exact", "finite-model constraint surplus leaves zero free weights",
      registry["constraint_surplus"]["remaining_freedom_after_domain_measure_supplied"] == 0)

residue = v15["residue"]
check("exact", "global residue and fork count are unchanged",
      residue["continuous_real"] == 84
      and residue["function_valued_at_least"] == 19
      and residue["open_discrete_forks"] == 9
      and residue["open_fork_horn_product"] == 1152)
check("exact", "one scoped finite zero-mode quotient is newly ranked",
      residue["quotients_ranked"] == 4
      and "zero-mode quotient Q of rank n-1" in residue["quotients_ranked_scope"]
      and "global residue reduction" in residue["quotients_ranked_scope"])
check("type", "external P1/P2/P3 remain unused and P2 is not identified",
      registry["external_datum"] == {
          "P1": "UNUSED", "P2": "UNUSED_NOT_IDENTIFIED", "P3": "UNUSED"
      })

check("planted", "PLANT global screening is conditional, not derived",
      "CONDITIONAL" in registry["result"]["global_projector_horn"])
check("planted", "PLANT free parity failure is not every C-operator failure",
      registry["result"]["interacting_c_operator"] == "OPEN")
check("planted", "PLANT super-IG is not booked as odd BV closure",
      "NOT_ODD_ACTION" in rows15["LT-SM8"]["mapping_grade"])
check("planted", "PLANT fourth quotient does not lower global residue",
      residue["continuous_real"] == v14["residue"]["continuous_real"])

print("COUNTS " + " ".join(f"{kind}:{count}" for kind, count in sorted(counts.items())))
if failures:
    raise SystemExit("FAILURES: " + "; ".join(failures))
print(f"PASS {sum(counts.values())}/{sum(counts.values())}")
