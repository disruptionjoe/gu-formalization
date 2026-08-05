#!/usr/bin/env python3
"""Append-only, taxonomy and scope checks for conditional ledger v0.7."""

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


v6p = ROOT / "lab/process/conditional-physics-ledger-v0.6.json"
v6vp = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.6.md"
v7p = ROOT / "lab/process/conditional-physics-ledger-v0.7.json"
v7vp = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.7.md"
reportp = ROOT / "explorations/conditional-build/k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md"
reviewp = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-global-chimeric-spin-reduction-review.md"
registryp = ROOT / "lab/process/k77-global-chimeric-spin-reduction-and-support-normalization.json"

v6 = strict(v6p)
v7 = strict(v7p)
registry = strict(registryp)
rows6 = {row["id"]: row for row in v6["rows"]}
rows7 = {row["id"]: row for row in v7["rows"]}
active = {rid: row for rid, row in rows7.items() if row.get("row_status") != "SUPERSEDED"}
view = v7vp.read_text()
report = reportp.read_text()
review = reviewp.read_text()

check("provenance", "v0.6 machine ledger is byte-frozen",
      hashlib.sha256(v6p.read_bytes()).hexdigest()
      == "c7facf3e7e94f00d813530061bc93b5cd05b2fec49778d656fb4f8ec575628f1")
check("provenance", "v0.6 human view is byte-frozen",
      hashlib.sha256(v6vp.read_bytes()).hexdigest()
      == "518ab97900d2983465c15faeccb4e017a68db2df0c1a1ce4730b7100cb10aea8")
check("exact", "v0.7 names v0.6 as predecessor",
      v7["schema_version"] == "0.7"
      and v7["predecessor"].endswith("conditional-physics-ledger-v0.6.json"))
check("exact", "row denominator and IDs are unchanged", set(rows6) == set(rows7))
check("exact", "only LT-GR2c changed", {rid for rid in rows6 if rows6[rid] != rows7[rid]} == {"LT-GR2c"})
check("exact", "the v0.7 migration edge is explicit",
      [m["row_id"] for m in v7["migrations"] if m.get("to_version") == "0.7"] == ["LT-GR2c"])

check("exact", "82 active targets and 83 provenance rows remain",
      len(active) == 82 and len(rows7) == 83)
check("exact", "axis counts remain 35/21/26",
      Counter(row["axis"] for row in active.values())
      == {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("exact", "verdict counts remain 32/19/25/6",
      Counter(row["verdict"] for row in active.values())
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6})
check("exact", "every active reason kind remains registered",
      all(row["reason_kind"] in v7["taxonomy"]["verdict_kinds"][row["verdict"]]
          for row in active.values()))

gr2c = rows7["LT-GR2c"]
check("type", "LT-GR2c remains NEEDS/MISSING_CONSTRUCTION",
      gr2c["verdict"] == "NEEDS" and gr2c["reason_kind"] == "MISSING_CONSTRUCTION")
check("type", "global gamma_epsilon and rank-ten receiver are exact",
      "GLOBAL_GAMMA_EPSILON_EXACT" in gr2c["mapping_grade"]
      and "SIGMA_RANK10_AND_ORTHOGONAL_PROJECTOR_EXACT" in gr2c["mapping_grade"])
check("type", "primary support has no profile while alias, BV and null domain remain open",
      all(token in gr2c["mapping_grade"] for token in
          ("PRIMARY_SUPPORT_WITHOUT_PROFILE_SELECTED", "LAMBDA_DEF_ALIAS", "NONLINEAR_BV", "NULL_DOMAIN_OPEN")))
check("type", "construction scope records the global K77 full reduction and independent-X horn",
      "K77_GLOBAL_FULL_CHIMERIC_CLIFFORD_REDUCTION" in gr2c["construction_scope"]
      and "INDEPENDENT_X_SUPPORT_HORN" in gr2c["construction_scope"])
check("exact", "only one conditional local quotient remains ranked",
      v7["residue"]["quotients_ranked"] == 1
      and "not a global/nonlinear physical quotient" in v7["residue"]["quotients_ranked_scope"])
check("exact", "continuous residue is a typed 83-to-84 alias range",
      v7["residue"]["continuous_real"] == 83
      and v7["residue"]["continuous_real_upper_if_lambda_def_independent"] == 84)
check("exact", "the alias creates one open fork without changing P1/P2/P3",
      v7["residue"]["open_discrete_forks"] == v6["residue"]["open_discrete_forks"] + 1 == 11
      and v7["residue"]["open_fork_horn_product"] == 4608)

global_reduction = registry["global_full_reduction"]
support = registry["support_horns"]["primary"]
check("exact", "registry constructs a global full labelled rank-fourteen frame",
      global_reduction["global"] is True
      and global_reduction["labelled_rank"] == 14
      and global_reduction["Clifford_relations_preserved"] is True)
check("exact", "the construction adds neither a field nor discrete datum",
      global_reduction["new_field_count"] == 0
      and global_reduction["new_discrete_datum_count"] == 0)
check("exact", "the rank-ten receiver condition is discharged globally on the admitted branch",
      registry["receiver_inheritance"]["receiver_rank"] == 10
      and registry["receiver_inheritance"]["global_reduction_condition"].startswith("DISCHARGED"))
check("exact", "primary support uses current pushforward without a transverse profile",
      support["id"] == "BULK_PLUS_INDEPENDENT_X"
      and support["support_map"] == "CANONICAL_CURRENT_PUSHFORWARD_s_BANG"
      and support["transverse_profile_required"] is False)
check("type", "lambda_def is an alias fork rather than a booked parameter",
      registry["normalization"]["new_continuous_parameter_added"] == "NOT_BOOKED_PENDING_ALIAS_ADJUDICATION"
      and "ALIAS_FORK" in registry["normalization"]["residue_owner"])
check("source", "global ownership reinspection returns SOURCE-CORRECTS",
      registry["source_return"] == "SOURCE-CORRECTS"
      and "SOURCE-CORRECTS" in report)
check("hostile", "both epistemic hostile charges and lambda alias repair are present",
      "summary outruns the artifact" in review
      and "superseded or mistyped object" in review
      and "alias" in review.lower())
check("exact", "human and machine meters agree",
      "Ledger v0.7" in view and "global full gamma_epsilon" in view)

check("planted", "PLANT spin-C existence is not absolute uniqueness",
      registry["induced_spin_lift"]["absolute_uniqueness_of_all_C_spin_structures"] is False)
check("planted", "PLANT source epsilon is not gamma_epsilon",
      registry["layer0"]["source_epsilon_vs_gamma_epsilon"] == "DISTINCT_DEPENDENT_CONSTRUCTION")
check("planted", "PLANT full frame is not merely an unframed plane",
      registry["layer0"]["full_frame_vs_unframed_plane"] == "FULL_LABELLED_FRAME")
check("planted", "PLANT chosen horn is not claimed unique",
      support["uniqueness_claimed"] is False)
check("planted", "PLANT support choice does not fix dark-energy magnitude",
      registry["normalization"]["dark_energy_magnitude_fixed"] is False)
check("planted", "PLANT nonlinear BV and null Green domain stay open",
      "FULL_PRIMITIVE_NONLINEAR_EVEN_WARD_BV_LEDGER" in registry["held_open"]
      and "TRACE_COMPATIBLE_CLOSED_KREIN_GREEN_BFV_DOMAIN" in registry["held_open"])
check("planted", "PLANT P1 P2 P3 remain unused",
      registry["residue"]["P1_P2_P3"] == "UNCHANGED_UNUSED")

print("COUNTS " + " ".join(f"{k}:{v}" for k, v in sorted(counts.items())))
if failures:
    raise SystemExit("FAILURES: " + "; ".join(failures))
print(f"PASS {sum(counts.values())}/{sum(counts.values())}")
