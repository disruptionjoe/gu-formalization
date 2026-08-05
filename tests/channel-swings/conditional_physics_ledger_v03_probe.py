#!/usr/bin/env python3
"""Structural, provenance and information-loss checks for ledger v0.3."""

from collections import Counter
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def strict(path):
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key in {path}")
        return dict(items)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


v2_path = ROOT / "lab/process/conditional-physics-ledger-v0.2.json"
view2_path = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.2.md"
v3_path = ROOT / "lab/process/conditional-physics-ledger-v0.3.json"
view3_path = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.3.md"
report_path = ROOT / "explorations/conditional-build/dynamic-cosmological-sector-constraint-rank-2026-08-05.md"

v2 = strict(v2_path)
v3 = strict(v3_path)
rows2 = {row["id"]: row for row in v2["rows"]}
rows3 = {row["id"]: row for row in v3["rows"]}
active = {rid: row for rid, row in rows3.items() if row.get("row_status") != "SUPERSEDED"}
view3 = view3_path.read_text(encoding="utf-8")
report = report_path.read_text(encoding="utf-8")

print("A. IMMUTABLE PREDECESSOR AND APPEND-ONLY SPLIT")
check("provenance", "v0.2 machine ledger retains its pinned digest",
      hashlib.sha256(v2_path.read_bytes()).hexdigest()
      == "f1ba89dbeed6c3e388ce935b8c74a70440c9865bc22488b9bd9b6644b43ea279")
check("provenance", "v0.2 human view retains its pinned digest",
      hashlib.sha256(view2_path.read_bytes()).hexdigest()
      == "2e0efff1e4f68562b74c3fc0fd84b56b464625dbeb11b9514fce87d0d588d8df")
check("exact", "v0.3 names v0.2 as predecessor",
      v3["predecessor"].endswith("conditional-physics-ledger-v0.2.json"))
check("exact", "all predecessor row IDs remain present", set(rows2) < set(rows3))
check("exact", "only LT-GR2 gains lifecycle metadata among predecessor rows",
      {rid for rid in rows2 if rows2[rid] != rows3[rid]} == {"LT-GR2"})
check("exact", "LT-GR2 is historical and names exactly five successors",
      rows3["LT-GR2"]["row_status"] == "SUPERSEDED"
      and rows3["LT-GR2"]["successors"]
      == ["LT-GR2a", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR2e"])
check("exact", "split migration is explicit",
      any(m.get("row_id") == "LT-GR2" and m.get("edge_type") == "split_from"
          and m.get("meaning_changed") is True for m in v3["migrations"]))

print("\nB. ACTIVE DENOMINATOR AND TAXONOMY")
check("exact", "82 active targets and 83 provenance records are present",
      len(active) == v3["denominator"]["canonical_target_count"] == 82
      and len(rows3) == v3["denominator"]["row_record_count"] == 83)
check("exact", "active axis counts are 35/21/26",
      Counter(row["axis"] for row in active.values())
      == {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("exact", "active verdict counts are 32/19/25/6",
      Counter(row["verdict"] for row in active.values())
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6})
check("exact", "machine meter matches the recomputed denominator",
      v3["progress"]["mapped"] == v3["progress"]["total"] == len(active)
      and v3["progress"]["verdict_counts"] == {
          "SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6})
check("exact", "every active row kind is registered under its verdict",
      all(row["reason_kind"] in v3["taxonomy"]["verdict_kinds"][row["verdict"]]
          for row in active.values()))
check("exact", "every active row retains the information-preserving fields",
      all({"id", "axis", "summary", "verdict", "reason_kind", "distance",
           "revival_trigger", "evidence", "mapping_grade"} <= set(row)
          for row in active.values()))

print("\nC. DYNAMIC-COSMOLOGY TYPE SEPARATIONS")
check("type", "literal Lambda g is a structural comparator",
      rows3["LT-GR2a"]["verdict"] == "DIFFERS"
      and rows3["LT-GR2a"]["reason_kind"] == "STRUCTURAL_DIFFERENCE")
check("type", "movable theta is partial rather than complete recovery",
      rows3["LT-GR2b"]["verdict"] == "SAME"
      and rows3["LT-GR2b"]["reason_kind"] == "DERIVED_PARTIAL")
check("type", "curvature covariation is a missing construction",
      rows3["LT-GR2c"]["verdict"] == "NEEDS"
      and "LAYER0_UNCERTAIN" in rows3["LT-GR2c"]["mapping_grade"])
check("type", "magnitude and radiative stability remain open",
      rows3["LT-GR2d"]["verdict"] == "NEEDS"
      and "RADIATIVE_STABILITY_OPEN" in rows3["LT-GR2d"]["mapping_grade"])
check("type", "observable cosmology is not promoted from its proxy",
      rows3["LT-GR2e"]["verdict"] == "NEEDS"
      and "ACTION_OWNERSHIP" in rows3["LT-GR2e"]["mapping_grade"])
check("exact", "the residue meter books no source-only reduction",
      v3["residue"]["continuous_real"] == 83
      and v3["residue"]["quotients_ranked"] == 0
      and "no reduction booked" in v3["residue"]["meter"])

print("\nD. SOURCE, RANK, AND HOSTILE-REVIEW FENCES")
check("source", "the report records exactly SOURCE-CONFIRMS",
      "Source return: `SOURCE-CONFIRMS`" in report
      and "`SOURCE-CORRECTS`" not in report
      and "`SOURCE-SILENT`" not in report)
check("type", "spatial flatness is not collapsed into four-curvature",
      "Spatially\nflat de Sitter" in report and "R=48" in report.replace(" ", "")
      and "G_00=12" in report.replace(" ", ""))
check("type", "the current record-current vacuum collision is named",
      "forces `theta=0`" in report and "curvature-covarying vacuum" in report)
check("type", "Weinberg is classified by horns rather than globally passed or killed",
      "INSIDE_WEINBERG_CLASS" in report and "POSSIBLE_SCOPE_EXIT" in report)
check("hostile", "both named hostile charges were executed",
      "summary outruns artifact" in report.lower()
      and "superseded or mistyped object" in report.lower())
check("exact", "the human meter matches the machine meter",
      "82/82" in view3 and "32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED" in view3)

print("\nE. PLANTED FAILURE MODES")
check("planted", "PLANT superseded LT-GR2 is excluded from active counts",
      len(rows3) != len(active))
check("planted", "PLANT field equality is not booked as residue reduction",
      v3["residue"]["continuous_real"] == v2["residue"]["continuous_real"])
check("planted", "PLANT dynamic does not mean magnitude derived",
      rows3["LT-GR2b"]["mapping_grade"] != "MAGNITUDE_DERIVED")
check("planted", "PLANT proxy w(z) does not count as action-owned prediction",
      rows3["LT-GR2e"]["reason_kind"] == "MISSING_CONSTRUCTION")

print("\nCOUNTS " + " ".join(f"{k}={v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS total={sum(COUNTS.values())}")
