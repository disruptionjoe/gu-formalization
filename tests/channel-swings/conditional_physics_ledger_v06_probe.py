#!/usr/bin/env python3
"""Append-only, taxonomy and scope checks for conditional ledger v0.6."""

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


v5p = ROOT / "lab/process/conditional-physics-ledger-v0.5.json"
v5vp = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.5.md"
v6p = ROOT / "lab/process/conditional-physics-ledger-v0.6.json"
v6vp = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.6.md"
reportp = ROOT / "explorations/conditional-build/k77-epsilon-gravitational-soldering-weld-2026-08-05.md"
reviewp = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-epsilon-gravitational-soldering-weld-review.md"
registryp = ROOT / "lab/process/k77-epsilon-gravitational-soldering-weld.json"

v5 = strict(v5p)
v6 = strict(v6p)
registry = strict(registryp)
rows5 = {row["id"]: row for row in v5["rows"]}
rows6 = {row["id"]: row for row in v6["rows"]}
active = {rid: row for rid, row in rows6.items() if row.get("row_status") != "SUPERSEDED"}
view = v6vp.read_text()
report = reportp.read_text()
review = reviewp.read_text()

check("provenance", "v0.5 machine ledger is byte-frozen",
      hashlib.sha256(v5p.read_bytes()).hexdigest()
      == "3fcdb64a03c7254d54a56b4bb25623fc94052c2ca688c984fa1295f4bad04ac8")
check("provenance", "v0.5 human view is byte-frozen",
      hashlib.sha256(v5vp.read_bytes()).hexdigest()
      == "fb74cf2b8492001494a485bb345ca0049fb8a2c2ef12898de8a1b486cac15244")
check("exact", "v0.6 names v0.5 as predecessor",
      v6["schema_version"] == "0.6"
      and v6["predecessor"].endswith("conditional-physics-ledger-v0.5.json"))
check("exact", "row denominator and IDs are unchanged", set(rows5) == set(rows6))
check("exact", "only LT-GR2c changed", {rid for rid in rows5 if rows5[rid] != rows6[rid]} == {"LT-GR2c"})
check("exact", "the v0.6 migration edge is explicit",
      [m["row_id"] for m in v6["migrations"] if m.get("to_version") == "0.6"] == ["LT-GR2c"])

check("exact", "82 active targets and 83 provenance rows remain",
      len(active) == 82 and len(rows6) == 83)
check("exact", "axis counts remain 35/21/26",
      Counter(row["axis"] for row in active.values())
      == {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("exact", "verdict counts remain 32/19/25/6",
      Counter(row["verdict"] for row in active.values())
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6})
check("exact", "every active reason kind remains registered",
      all(row["reason_kind"] in v6["taxonomy"]["verdict_kinds"][row["verdict"]]
          for row in active.values()))

gr2c = rows6["LT-GR2c"]
check("type", "LT-GR2c remains NEEDS/MISSING_CONSTRUCTION",
      gr2c["verdict"] == "NEEDS" and gr2c["reason_kind"] == "MISSING_CONSTRUCTION")
check("type", "rank-ten sigma and orthogonal same-stratum weld are typed",
      "SIGMA_RANK10" in gr2c["mapping_grade"]
      and "SAME_STRATUM_ORTHOGONAL_WELD_EXACT" in gr2c["mapping_grade"])
check("type", "global reduction, cross-dimensional normalization and analytic closure remain open",
      all(token in gr2c["mapping_grade"] for token in
          ("GLOBAL_FULL_REDUCTION", "BULK_DEFECT_NORMALIZATION", "NONLINEAR_BV", "NULL_DOMAIN_OPEN")))
check("type", "construction scope records the conditional full reduction rather than a fixed slot",
      "GLOBAL_CONDITIONAL_ON_FULL_EPSILON_REDUCTION" in gr2c["construction_scope"])
check("exact", "only one conditional local quotient remains ranked",
      v6["residue"]["quotients_ranked"] == 1
      and "not a global/nonlinear physical quotient" in v6["residue"]["quotients_ranked_scope"])
check("exact", "global residue counts do not move",
      v6["residue"]["continuous_real"] == v5["residue"]["continuous_real"] == 83
      and v6["residue"]["open_discrete_forks"] == v5["residue"]["open_discrete_forks"] == 10)

receiver = registry["receiver"]
projector = registry["projector"]
check("exact", "registry carries rank-ten receiver and rank-ten projector",
      receiver["rank_on_grade1_carrier"] == 10
      and projector["projector_rank"] == 10)
check("exact", "right inverse, isometry, idempotence and self-adjointness are all exact",
      all(projector[key] is True for key in
          ("right_inverse_exact", "isometry_exact", "projector_idempotent", "projector_self_adjoint")))
check("exact", "equivariance is not misreported as uniqueness",
      registry["equivariance_boundary"]["independent_lorentz_equivariant_sym2_bilinear_maps_lower_bound"] == 5
      and registry["equivariance_boundary"]["uniqueness_claim"] == "NOT_MADE")
check("exact", "same-stratum weld passes while bulk/defect support remains open",
      registry["action_weld"]["old_receiver_reconstruction"] == "EXACT"
      and registry["action_weld"]["bulk_defect_support"] == "OPEN")
check("source", "new receiver/weld receives exactly SOURCE-SILENT",
      registry["source_return"] == "SOURCE-SILENT"
      and "Decisive return: `SOURCE-SILENT`" in report)
check("hostile", "both epistemic hostile charges and the support charge are present",
      "summary outruns the artifact" in review
      and "superseded object" in review
      and "action and support hostile review" in review)
check("exact", "human and machine meters agree",
      "Ledger v0.6" in view and "K77 sigma_epsilon: rank 10" in view)

check("planted", "PLANT q is not itself the full receiver",
      "itself is one line" in report and receiver["rank_on_grade1_carrier"] == 10)
check("planted", "PLANT K95 IC1 is not imported into K77",
      "opposite direction" in report and "Cl(9,5)" in report)
check("planted", "PLANT dropping the Krein sign is adverse",
      "anti-isometry" in report and projector["krein_reason"] == "REAL_K77_GRADE1_GENERATORS_ARE_B_SKEW")
check("planted", "PLANT same-stratum algebra is not a bulk/defect theorem",
      registry["action_weld"]["normal_density_or_relative_normalization"] == "OPEN")
check("planted", "PLANT finite Ward is not nonlinear BV",
      registry["ward_bv"]["nonlinear_CME"] == "OPEN")
check("planted", "PLANT P1 P2 P3 remain unused",
      registry["residue"]["P1_P2_P3"] == "UNCHANGED_UNUSED")

print("COUNTS " + " ".join(f"{k}:{v}" for k, v in sorted(counts.items())))
if failures:
    raise SystemExit("FAILURES: " + "; ".join(failures))
print(f"PASS {sum(counts.values())}/{sum(counts.values())}")
