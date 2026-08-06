#!/usr/bin/env python3
"""Append-only migration and scope checks for conditional ledger v0.17."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def load(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


old_path = ROOT / "lab/process/conditional-physics-ledger-v0.16.json"
old_bytes = old_path.read_bytes()
old = json.loads(old_bytes)
new = load("lab/process/conditional-physics-ledger-v0.17.json")
registry = load("lab/process/selected-cubic-qft-threshold-and-numerator-gate.json")
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.17.md").read_text()
result = (ROOT / "explorations/conditional-build/selected-cubic-qft-threshold-and-numerator-gate-2026-08-05.md").read_text()
source = (ROOT / "lab/sources/selected-cubic-qft-threshold-and-numerator-gate-source-reinspection-2026-08-05.md").read_text()

check("provenance", "v0.16 machine ledger is byte-frozen",
      hashlib.sha256(old_bytes).hexdigest()
      == "a1242d9e4ad1157f55afecf77691253cafcad86c5dbfa169ec36f48fc46ddc03")
check("exact", "v0.17 names v0.16 as predecessor",
      new["schema_version"] == "0.17"
      and new["predecessor"].endswith("conditional-physics-ledger-v0.16.json"))

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
changed = {row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]}
expected = {"LT-GR2b", "LT-GR3", "LT-GR5", "LT-SM8"}
check("exact", "row denominator and IDs are unchanged",
      old_rows.keys() == new_rows.keys() and new["denominator"] == old["denominator"])
check("exact", "exactly four declared row records changed", changed == expected)

new_edges = [edge for edge in new["migrations"]
             if edge.get("from_version") == "0.16" and edge.get("to_version") == "0.17"]
check("exact", "the four v0.17 migration edges are explicit",
      {edge["row_id"] for edge in new_edges} == expected and len(new_edges) == 4)
check("exact", "82 active targets and 83 provenance rows remain",
      new["progress"]["mapped"] == new["progress"]["total"] == 82
      and len(new["rows"]) == 83)
check("exact", "axis counts remain 35/21/26",
      new["denominator"]["axes"]
      == {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("exact", "verdict counts remain 33/19/24/6",
      new["progress"]["verdict_counts"]
      == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6})

check("type", "LT-GR2b retains background C and exposes the on-shell numerator",
      "FIXED_BACKGROUND_C_EXACT" in new_rows["LT-GR2b"]["mapping_grade"]
      and "ONSHELL_NUMERATOR_OPEN" in new_rows["LT-GR2b"]["mapping_grade"])
check("type", "LT-GR3 retains loop and UV burden after the exact shell",
      "ODD_CONTINUUM_SHELL" in new_rows["LT-GR3"]["mapping_grade"]
      and "LOOP_UV_OPEN" in new_rows["LT-GR3"]["mapping_grade"])
check("type", "LT-GR5 retains augmented-torsion numerator and domain",
      "AUGMENTED_TORSION_NUMERATOR_AND_DOMAIN_OPEN" in new_rows["LT-GR5"]["mapping_grade"])
check("type", "LT-SM8 separates kinematics, numerator, Fock metric and super-IG",
      "NO_SCALAR_SIGN_CLEARS_ODD_CONTINUUM_SHELL" in new_rows["LT-SM8"]["mapping_grade"]
      and "ONSHELL_NUMERATOR_FULL_FOCK_METRIC_OPEN" in new_rows["LT-SM8"]["mapping_grade"]
      and "SUPER_IG_SEPARATE" in new_rows["LT-SM8"]["mapping_grade"])

check("source", "the decisive Eric-lane return is SOURCE-SILENT",
      registry["source_return"] == "SOURCE-SILENT"
      and "Decisive Eric-lane return: `SOURCE-SILENT`" in source)
check("exact", "the registry carries the two selected mass formulae",
      registry["formulae"]["massive_tt_mass_squared"] == "124*alpha_II*kappa_1/117"
      and registry["formulae"]["scalar_mass_squared_stable_branch"] == "a*kappa/(3*beta^2)")
check("exact", "the registry books shells but not a Q1 pole",
      "REAL_SHELL" in registry["result"]["even_theta_odd_channel"]
      and "REAL_TWO_MASSLESS_SHELL" in registry["result"]["odd_theta_odd_channel"]
      and registry["result"]["q1_pole"].startswith("CONDITIONAL"))
check("type", "the scalar-enlarged zero-field Hessian is retired as mistyped",
      "Scalar-enlarged vacuum Hessian: no new block" in view
      and "complete Hessian" in result and "vanishes at the zero-field point" in result)
check("exact", "global residue and quotient count are unchanged", new["residue"] == old["residue"])
check("type", "external P1/P2/P3 remain unused", set(registry["external_datum"].values()) == {"UNUSED"})
check("exact", "the human ledger reports the unchanged meter",
      "82/82" in view and "33 SAME" in view and "84 continuous" in view
      and "Quotients ranked: 4 scoped" in view)
check("type", "the result excludes pole and full-QFT promotion",
      "No interacting `C`, Q1 pole" in result and "on-shell numerator" in result)

check("planted", "PLANT a real shell is not a booked pole",
      registry["result"]["q1_pole"] != "PROVED_POLE")
check("planted", "PLANT scalar fluctuation does not increment quotient count",
      new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"] == 4)
check("planted", "PLANT the wave does not change verdict counts",
      new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("planted", "PLANT the native Y14 state space is not silently identified",
      "complete native" in view and "`Y^14` quantum state space" in view)
check("planted", "PLANT super-IG is not merged into the C construction",
      "SUPER_IG_DESCENT" in registry["next_gate"])
check("planted", "PLANT the normalized observer functional remains separate",
      "NORMALIZED_OBSERVER_FUNCTIONAL" in registry["next_gate"])

total = sum(COUNTS.values())
print("COUNTS", " ".join(f"{kind}:{value}" for kind, value in sorted(COUNTS.items())))
if FAILURES:
    print("FAILURES", FAILURES)
    raise SystemExit(1)
print(f"PASS {total}/{total}")
