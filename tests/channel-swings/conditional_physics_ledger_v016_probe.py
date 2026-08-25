#!/usr/bin/env python3
"""Append-only migration and scope checks for conditional ledger v0.16."""

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


old_path = ROOT / "lab/process/conditional-physics-ledger-v0.15.json"
old_bytes = old_path.read_bytes()
old = json.loads(old_bytes)
new = load("lab/process/conditional-physics-ledger-v0.16.json")
registry = load("lab/process/first-perturbative-background-c-operator.json")
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.16.md").read_text()
result = (ROOT / "explorations/conditional-build/first-perturbative-background-c-operator-2026-08-05.md").read_text()
source = (ROOT / "lab/sources/first-perturbative-background-c-operator-source-reinspection-2026-08-05.md").read_text()

check("provenance", "v0.15 machine ledger is byte-frozen",
      hashlib.sha256(old_bytes).hexdigest()
      == "dbf7d4bed4b19ff5b330a8a8e3e6458420e3cfd8d507dad4c0e2363aec9ea351")
check("exact", "v0.16 names v0.15 as predecessor",
      new["schema_version"] == "0.16"
      and new["predecessor"].endswith("conditional-physics-ledger-v0.15.json"))

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
changed = {row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]}
expected = {"LT-GR2b", "LT-GR3", "LT-GR5", "LT-SM8"}
check("exact", "row denominator and IDs are unchanged",
      old_rows.keys() == new_rows.keys()
      and new["denominator"] == old["denominator"])
check("exact", "exactly four declared row records changed", changed == expected)

new_edges = [edge for edge in new["migrations"]
             if edge.get("from_version") == "0.15" and edge.get("to_version") == "0.16"]
check("exact", "the four v0.16 migration edges are explicit",
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

check("type", "LT-GR2b books background C without full interacting promotion",
      "FIXED_BACKGROUND_C_EXACT" in new_rows["LT-GR2b"]["mapping_grade"]
      and "FULL_NONLINEAR_FOCK_DOMAIN_OPEN" in new_rows["LT-GR2b"]["mapping_grade"])
check("type", "LT-GR3 retains loop and UV burden",
      "FULL_CUBIC_LOOP_UV_OPEN" in new_rows["LT-GR3"]["mapping_grade"])
check("type", "LT-GR5 retains the complete augmented-torsion domain",
      "FULL_AUGMENTED_TORSION_DOMAIN_OPEN" in new_rows["LT-GR5"]["mapping_grade"])
check("type", "LT-SM8 separates finite TT positivity, full quotient and super-IG",
      "TWO_EVEN_BV_TT_CLASSES" in new_rows["LT-SM8"]["mapping_grade"]
      and "FULL_INTERACTING_QUOTIENT_FOCK_METRIC_OPEN" in new_rows["LT-SM8"]["mapping_grade"]
      and "SUPER_IG_SEPARATE" in new_rows["LT-SM8"]["mapping_grade"])

check("source", "the decisive Eric-lane return is SOURCE-SILENT",
      registry["source_return"] == "SOURCE-SILENT"
      and "Decisive Eric-lane return: `SOURCE-SILENT`" in source)
check("exact", "the registry carries the factored discriminant",
      registry["formulae"]["discriminant"]
      == "(b+u)*(alpha^2*b+(alpha-2)^2*u)")
check("exact", "the first-order C correction has zero residual freedom",
      registry["constraint_surplus"] == {
          "first_order_coefficients": 4,
          "independent_constraint_rank": 4,
          "remaining_freedom": 0,
          "upstream_action_coefficients_and_background": "SUPPLIED_NOT_DERIVED_BY_THIS_COUNT",
      })
check("type", "the D1 192-dimensional record lift remains open",
      registry["d1_toy"].startswith("NOT_FULLY_DISCHARGED")
      and "192-dimensional record-sector lift" in view)
check("exact", "global residue and quotient count are unchanged",
      new["residue"] == old["residue"])
check("type", "external P1/P2/P3 remain unused",
      set(registry["external_datum"].values()) == {"UNUSED"})
check("exact", "the human ledger reports the unchanged meter",
      "82/82" in view and "33 SAME" in view and "84 continuous" in view
      and "Quotients ranked: 4 scoped" in view)
check("type", "the result excludes physical-vacuum and full-QFT promotion",
      "not yet a physical-vacuum theorem" in " ".join(result.split())
      and "quantum Fock-space `C`" in " ".join(result.split()))

check("planted", "PLANT background C is not full interacting C",
      registry["result"]["full_nonlinear_or_qft_c"] == "OPEN")
check("planted", "PLANT zero C freedom does not derive upstream coefficients",
      "SUPPLIED_NOT_DERIVED" in registry["constraint_surplus"]["upstream_action_coefficients_and_background"])
check("planted", "PLANT exceptional walls do not change verdict counts",
      new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("planted", "PLANT this wave does not increment quotient count",
      new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"] == 4)
check("planted", "PLANT D1 is not silently discharged",
      "NOT_FULLY_DISCHARGED" in registry["d1_toy"])
check("planted", "PLANT super-IG is not merged into the C construction",
      "MIXED_SUPER_IG_GLOBAL_DESCENT" in registry["next_gate"])

total = sum(COUNTS.values())
print("COUNTS", " ".join(f"{kind}:{value}" for kind, value in sorted(COUNTS.items())))
if FAILURES:
    print("FAILURES", FAILURES)
    raise SystemExit(1)
print(f"PASS {total}/{total}")
