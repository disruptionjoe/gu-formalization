#!/usr/bin/env python3
"""Durability audit for ledger v0.159 high-conviction receiver comparison."""

from collections import Counter
import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def unique_json(path):
    def hook(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key: {path}")
        return dict(items)
    return json.loads(path.read_text(), object_pairs_hook=hook)


ledger = unique_json(ROOT / "lab/process/conditional-physics-ledger-v0.159.json")
registry = unique_json(ROOT / "lab/process/selected-k77-high-conviction-receiver-completion.json")
contract = unique_json(ROOT / "lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-high-conviction-receiver-completion-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-high-conviction-receiver-completion-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-high-conviction-receiver-completion-source-return-2026-08-10.md").read_text()
probe = (ROOT / "tests/channel-swings/selected_k77_high_conviction_receiver_completion_probe.py").read_text()

print("A. LEDGER AND ACCOUNTING")
check("ledger", "v0.159 is current and append-only from v0.158",
      ledger["schema_version"] == "0.159" and ledger["predecessor"].endswith("v0.158.json"))
check("ledger", "coverage remains 82 of 82", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("ledger", "verdict counts remain unchanged",
      ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("ledger", "residue and quotients remain 84 and five",
      ledger["residue"]["continuous_real"] == 84 and ledger["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier delta is three closed one opened four remaining",
      ledger["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3,
                                   "conditions_opened": 1, "remaining_named_conditions": 4})
rows = {row["id"]: row for row in ledger["rows"]}
touched = ["RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"]
check("ledger", "all six rows point to the high-conviction result",
      all(rows[row]["evidence"] == "selected-k77-high-conviction-receiver-completion-2026-08-10.md" for row in touched))
check("ledger", "six append-only v0.158 to v0.159 migrations exist",
      sum(1 for migration in ledger["migrations"]
          if migration.get("from_version") == "0.158" and migration.get("to_version") == "0.159") == 6)

print("\nB. EXACT RESULT")
for stratum, expected in {
    "timelike": (128, 256, 0, 256, 0, 128),
    "spacelike": (128, 256, 0, 256, 0, 128),
    "null": (64, 192, 0, 192, 64, 0),
}.items():
    actual = registry["rank_fingerprint_each_pin"][stratum]
    check("result", f"{stratum} southeast and gauge ranks match exact fingerprint",
          (actual["southeast_span"], actual["leak_southeast_join"], actual["leak_southeast_intersection"],
           actual["leak_gauge_join"], actual["leak_gauge_intersection"], actual["symbol_on_gauge"]) == expected)
check("result", "minimal receiver exposes 128 added equations and paired fields",
      registry["minimal_receiver"] == {"old_rank": 128, "new_rank": 256, "added_equations": 128,
                                        "required_paired_left_fields": 128, "source_owned": False})
check("result", "K95 tied coefficient leaves rank-128 residual",
      registry["k95_tied_minus_11_over_12_residual_rank"] == 128)
check("result", "probe passed 29 new checks and replayed predecessor",
      registry["checks"] == {"new": 29, "new_failures": 0,
                              "predecessor_replayed": True, "predecessor_checks": 39})

print("\nC. COUNCIL LEARNING, SOURCE AND HOSTILE REVIEW")
routing = contract["channels"]["VERIFY"]["efficient_specialist_routing"]
synthesis = routing["council_synthesis"]
check("council", "contract preserves convergence and high-confidence outlier rankings",
      synthesis["rankings"] == ["BROAD_CONVERGENCE_ACROSS_DISTANT_DISCIPLINES",
                                "HIGH_CONFIDENCE_SPECIALIST_OUTLIERS"])
check("council", "every registry outlier has an explicit disposition",
      all("disposition" in item for item in registry["council_synthesis"]["high_confidence_outliers"]))
check("council", "deferred outliers carry revival triggers",
      all("revival_trigger" in item for item in registry["council_synthesis"]["high_confidence_outliers"]
          if item["disposition"] == "DEFERRED"))
check("source", "source return is identical in ledger and registry",
      ledger["source_return"] == registry["source_return"])
check("source", "source artifact records confirm correct and silent scopes",
      all(code in source for code in ["SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"]))
check("layer0", "report separates source permission from selected map",
      "source permission for a nonzero southeast block and selection of its map" in report)
check("hostile", "review survives only with scoped verdict", "verdict: SCOPED_SURVIVES" in review)
check("hostile", "all three hostile charges are present",
      all(f"Charge {index}" in review for index in [1, 2, 3]))
for lens in ["Layer-0 semantics", "Prior art", "Differential geometry", "Representation/Clifford",
             "Variational bicomplex", "Symplectic/BV-BFV", "Operator/Krein", "Adversarial scope",
             "High-conviction minority audit"]:
    check("hostile", f"review includes {lens}", lens in review)

print("\nD. PROCESS AND EXECUTABLE FENCES")
check("process", "current append-only ledger descends to v0.159", reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.159.json"
))
check("process", "next gate forbids arbitrary receiver projector",
      "NO_ARBITRARY_RECEIVER_PROJECTOR" in registry["next_gate"])
for path in ["NEXT-STEPS.md", "RESEARCH-STATUS.md", "lab/process/README.md",
             "lab/process/CURRENT-RESEARCH-CONTEXT.md"]:
    check("process", f"{path} names v0.159", "v0.159" in (ROOT / path).read_text())
check("process", "source index lists new return", "selected-k77-high-conviction-receiver-completion-source-return" in (ROOT / "lab/sources/README.md").read_text())
check("process", "test manifest lists exact probe", "selected_k77_high_conviction_receiver_completion_probe.py" in (ROOT / "tests/README.md").read_text())
check("process", "gate manifest lists this audit", "high_conviction_receiver_completion_audit.py" in (ROOT / "process_gates/README.md").read_text())
check("probe", "probe tests southeast and gauge intersections", "leak_southeast_intersection_rank" in probe and "leak_gauge_quotient_intersection_rank" in probe)
check("probe", "probe prices paired receiver ownership", "required_paired_left_fields" in registry["minimal_receiver"] and "paired left field directions" in report)

total = sum(COUNTS.values())
print(f"\nSUMMARY {total-len(FAILURES)}/{total} PASS; counts={dict(COUNTS)}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
