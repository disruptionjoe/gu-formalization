#!/usr/bin/env python3
"""Append-only, taxonomy and scope checks for conditional ledger v0.5."""

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


v4p = ROOT / "lab/process/conditional-physics-ledger-v0.4.json"
v4vp = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.4.md"
v5p = ROOT / "lab/process/conditional-physics-ledger-v0.5.json"
v5vp = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.5.md"
reportp = ROOT / "explorations/conditional-build/pre-shiab-gauss-defect-action-bv-symbol-2026-08-05.md"
reviewp = ROOT / "lab/process/hostile-reviews/2026-08-05-pre-shiab-gauss-defect-action-bv-symbol-review.md"
registryp = ROOT / "lab/process/pre-shiab-gauss-defect-action-bv-symbol.json"

v4 = strict(v4p)
v5 = strict(v5p)
registry = strict(registryp)
rows4 = {row["id"]: row for row in v4["rows"]}
rows5 = {row["id"]: row for row in v5["rows"]}
active = {rid: row for rid, row in rows5.items() if row.get("row_status") != "SUPERSEDED"}
view = v5vp.read_text()
report = reportp.read_text()
review = reviewp.read_text()

check("provenance", "v0.4 machine ledger is byte-frozen",
      hashlib.sha256(v4p.read_bytes()).hexdigest()
      == "bccb428d969d8d1416e244524a934dd960bad525a534464372a3eab03c474f54")
check("provenance", "v0.4 human view is byte-frozen",
      hashlib.sha256(v4vp.read_bytes()).hexdigest()
      == "e3150ba16bf09c81701a38e221008f845fc1ebf82a301de1f318e87d4c721959")
check("exact", "v0.5 names v0.4 as predecessor",
      v5["schema_version"] == "0.5"
      and v5["predecessor"].endswith("conditional-physics-ledger-v0.4.json"))
check("exact", "row denominator and IDs are unchanged", set(rows4) == set(rows5))
check("exact", "only LT-GR2c changed", {rid for rid in rows4 if rows4[rid] != rows5[rid]} == {"LT-GR2c"})
check("exact", "the v0.5 migration edge is explicit",
      [m["row_id"] for m in v5["migrations"] if m.get("to_version") == "0.5"] == ["LT-GR2c"])

check("exact", "82 active targets and 83 provenance rows remain",
      len(active) == 82 and len(rows5) == 83)
check("exact", "axis counts remain 35/21/26",
      Counter(row["axis"] for row in active.values())
      == {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("exact", "verdict counts remain 32/19/25/6",
      Counter(row["verdict"] for row in active.values())
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6})
check("exact", "every active reason kind remains registered",
      all(row["reason_kind"] in v5["taxonomy"]["verdict_kinds"][row["verdict"]]
          for row in active.values()))

gr2c = rows5["LT-GR2c"]
check("type", "LT-GR2c remains NEEDS/MISSING_CONSTRUCTION",
      gr2c["verdict"] == "NEEDS" and gr2c["reason_kind"] == "MISSING_CONSTRUCTION")
check("type", "current-I1B kill and repaired local quotient are both typed",
      "CURRENT_I1B_T0_OWNER_KILLED" in gr2c["mapping_grade"]
      and "BV_QUOTIENT_RANK16_EXACT" in gr2c["mapping_grade"])
check("type", "global soldering weld and null domain remain open",
      all(token in gr2c["mapping_grade"] for token in ("GLOBAL_SOLDERING", "WELD", "NULL_DOMAIN_OPEN")))
check("type", "construction scope stays local and non-null",
      gr2c["construction_scope"] == "FIXED_GRAVITATIONAL_SLOT__FLAT_BACKGROUND__LINEARIZED_NONNULL_EVEN_BV_SYMBOL")
check("exact", "only one conditional local quotient is ranked",
      v5["residue"]["quotients_ranked"] == 1
      and "not a global/nonlinear physical quotient" in v5["residue"]["quotients_ranked_scope"])
check("exact", "global residue counts do not move",
      v5["residue"]["continuous_real"] == v4["residue"]["continuous_real"] == 83
      and v5["residue"]["open_discrete_forks"] == v4["residue"]["open_discrete_forks"] == 10
      and "NO_NEW_INDEPENDENT_FORK" in registry["repaired_action"]["discrete_residue_booking"])

exact = registry["exact_results"]
check("exact", "registry carries trace reversal and non-null quotient ranks",
      exact["trace_reversed_frobenius_inertia"] == [6, 4]
      and exact["nonnull_repaired_hessian_rank_nonzero_gain"] == 16
      and exact["nonnull_BV_quotient_dimension"] == 16)
check("exact", "zero-gain and null controls remain adverse",
      exact["zero_gain_hessian_rank"] == 12
      and exact["null_non_gauge_characteristic_kernel_dimension"] == 6)
check("source", "new repaired action receives exactly SOURCE-SILENT",
      registry["source_return"] == "SOURCE-SILENT"
      and "Source return: `SOURCE-SILENT`" in report)
check("hostile", "both two-sided hostile charges are present",
      "summary outruns the artifact" in review and "superseded or mistyped object" in review)
check("exact", "human and machine meters agree",
      "Ledger v0.5" in view and "Quotients ranked: 1 conditional/local" in view)

check("planted", "PLANT fixed-slot v is not raw adjoint-valued v_T",
      "not an ordinary symmetric tensor" in report and "sigma_epsilon" in report)
check("planted", "PLANT rank 16 is not a physical degree count",
      "six graviton polarizations" in report and exact["nonnull_BV_quotient_dimension"] == 16)
check("planted", "PLANT null exactness is not promoted",
      registry["exact_complex"]["null_disposition"] == "CHARACTERISTIC_NOT_EXACT_AFTER_GAUGE")
check("planted", "PLANT repaired action is not attributed to the source",
      registry["boundaries"]["source_attribution"] == "REPAIRED_TERM_AND_BV_COMPLEX_NOT_PRINTED")
check("planted", "PLANT P1 P2 P3 remain unused",
      registry["boundaries"]["data"] == "P1_P2_P3_UNCHANGED_UNUSED")

print("COUNTS " + " ".join(f"{k}:{v}" for k, v in sorted(counts.items())))
if failures:
    raise SystemExit("FAILURES: " + "; ".join(failures))
print(f"PASS {sum(counts.values())}/{sum(counts.values())}")
