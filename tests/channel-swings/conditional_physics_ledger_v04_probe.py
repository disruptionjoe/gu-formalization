#!/usr/bin/env python3
"""Append-only, taxonomy and scope checks for conditional ledger v0.4."""

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


v3p = ROOT / "lab/process/conditional-physics-ledger-v0.3.json"
v3vp = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.3.md"
v4p = ROOT / "lab/process/conditional-physics-ledger-v0.4.json"
v4vp = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.4.md"
reportp = ROOT / "explorations/conditional-build/source-native-curvature-vev-euler-rank-2026-08-05.md"
reviewp = ROOT / "lab/process/hostile-reviews/2026-08-05-source-native-curvature-vev-euler-rank-review.md"

v3 = strict(v3p)
v4 = strict(v4p)
rows3 = {row["id"]: row for row in v3["rows"]}
rows4 = {row["id"]: row for row in v4["rows"]}
active = {rid: row for rid, row in rows4.items() if row.get("row_status") != "SUPERSEDED"}
view = v4vp.read_text()
report = reportp.read_text()
review = reviewp.read_text()

check("provenance", "v0.3 machine ledger is byte-frozen",
      hashlib.sha256(v3p.read_bytes()).hexdigest()
      == "8fa8fcc66a165a9e48c1d566ec95457a9f878e3470d7bcb8859b1adf7a3045c1")
check("provenance", "v0.3 human view is byte-frozen",
      hashlib.sha256(v3vp.read_bytes()).hexdigest()
      == "7d94bde8c9774e93f06d66dc95998f3e47af9d4084098a391b1d8bbcc297283b")
check("exact", "v0.4 names v0.3 as predecessor",
      v4["predecessor"].endswith("conditional-physics-ledger-v0.3.json"))
check("exact", "row denominator and IDs are unchanged", set(rows3) == set(rows4))
check("exact", "only LT-GR2b/c/d rows changed", {rid for rid in rows3 if rows3[rid] != rows4[rid]}
      == {"LT-GR2b", "LT-GR2c", "LT-GR2d"})
check("exact", "three v0.4 migration edges are explicit",
      {m["row_id"] for m in v4["migrations"] if m.get("to_version") == "0.4"}
      == {"LT-GR2b", "LT-GR2c", "LT-GR2d"})

check("exact", "82 active targets and 83 provenance rows remain",
      len(active) == 82 and len(rows4) == 83)
check("exact", "axis counts remain 35/21/26",
      Counter(row["axis"] for row in active.values())
      == {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("exact", "verdict counts remain 32/19/25/6",
      Counter(row["verdict"] for row in active.values())
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6})
check("exact", "every active reason kind is registered",
      all(row["reason_kind"] in v4["taxonomy"]["verdict_kinds"][row["verdict"]]
          for row in active.values()))
check("exact", "every row retains distance and revival trigger",
      all(row.get("distance") and row.get("revival_trigger") for row in active.values()))

check("type", "variable theta/T earns partial ambient action ownership",
      rows4["LT-GR2b"]["verdict"] == "SAME"
      and "AMBIENT_ACTION_EULER_EXACT" in rows4["LT-GR2b"]["mapping_grade"])
check("type", "curvature covariation remains NEEDS at the observed/BV locus",
      rows4["LT-GR2c"]["verdict"] == "NEEDS"
      and "RANK_105_EXACT" in rows4["LT-GR2c"]["mapping_grade"]
      and "BV_UNDEFINED" in rows4["LT-GR2c"]["mapping_grade"])
check("type", "current-action inability is not collapsed with an ordinary missing construction",
      rows4["LT-GR2d"]["reason_kind"] == "PROVEN_UNABLE_BY_CURRENT_ACTION")
check("type", "observable cosmology is unchanged and unpromoted", rows4["LT-GR2e"] == rows3["LT-GR2e"])
check("exact", "residue and quotient counts remain unchanged",
      v4["residue"]["continuous_real"] == v3["residue"]["continuous_real"] == 83
      and v4["residue"]["quotients_ranked"] == 0)

check("source", "report records exactly SOURCE-CONFIRMS",
      "Source return: `SOURCE-CONFIRMS`" in report
      and "Source return: `SOURCE-CORRECTS`" not in report
      and "Source return: `SOURCE-SILENT`" not in report)
check("exact", "report states ranks 105 and 196 separately",
      "rank **105**" in report and "rank **196**" in report and "91" in report)
check("type", "ambient and observed receivers remain distinct",
      "contraction before restriction" in report and "rank-10 observed Einstein sector" in report)
check("type", "circular old-receiver kill is explicitly forbidden",
      "circular to demand" in report and "negative evidence against" in report)
check("type", "BV rank is undefined rather than booked zero",
      "BV quotient rank is undefined" in report and v4["residue"]["quotients_ranked"] == 0)
check("type", "vacuum shift is tracked rather than screened",
      "tracks the shift but does not screen it" in report)
check("hostile", "both two-sided hostile charges are present",
      "summary outruns the artifact" in review and "superseded or mistyped object" in review)
check("exact", "human and machine meters agree",
      "82/82" in view and "32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED" in view)

check("planted", "PLANT total rank is not curvature rank",
      "105" in rows4["LT-GR2c"]["mapping_grade"] and "196" in rows4["LT-GR2c"]["mapping_grade"])
check("planted", "PLANT no quotient reduction is manufactured",
      v4["residue"]["quotients_ranked"] == v3["residue"]["quotients_ranked"])
check("planted", "PLANT fixed Lambda is not blamed for the rank-10 loss",
      "Lambda g` spans only the one-dimensional" in report)
check("planted", "PLANT P1 P2 P3 are absent from the repair queue",
      all(not any(token in item["why"] for token in ("P1", "P2", "P3"))
          for item in v4["next_work_queue"]))

print("COUNTS " + " ".join(f"{k}:{v}" for k, v in sorted(counts.items())))
if failures:
    raise SystemExit("FAILURES: " + "; ".join(failures))
print(f"PASS {sum(counts.values())}/{sum(counts.values())}")
