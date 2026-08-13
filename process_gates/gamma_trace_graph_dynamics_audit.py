#!/usr/bin/env python3
"""Durability audit for ledger v0.158 graph-dynamics gate."""

from collections import Counter
import json
from pathlib import Path


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


ledger = unique_json(ROOT / "lab/process/conditional-physics-ledger-v0.158.json")
registry = unique_json(ROOT / "lab/process/selected-k77-gamma-trace-graph-dynamics-gate.json")
contract = unique_json(ROOT / "lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-gamma-trace-graph-dynamics-gate-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-gamma-trace-graph-dynamics-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-gamma-trace-graph-dynamics-source-return-2026-08-10.md").read_text()
probe = (ROOT / "tests/channel-swings/selected_k77_gamma_trace_graph_dynamics_probe.py").read_text()

print("A. LEDGER AND ACCOUNTING")
check("ledger", "v0.158 is current and append-only from v0.157",
      ledger["schema_version"] == "0.158" and ledger["predecessor"].endswith("v0.157.json"))
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
check("ledger", "all six rows point to the graph-dynamics result",
      all(rows[row]["evidence"] == "selected-k77-gamma-trace-graph-dynamics-gate-2026-08-10.md" for row in touched))
check("ledger", "six append-only v0.157 to v0.158 migrations exist",
      sum(1 for migration in ledger["migrations"]
          if migration.get("from_version") == "0.157" and migration.get("to_version") == "0.158") == 6)

print("\nB. EXACT RESULT")
for candidate in registry["candidates"].values():
    check("result", "left/right/Krein ranks are 128/128/1920",
          candidate["right_kernel_rank"] == candidate["left_kernel_rank"] == 128
          and candidate["krein_pairing_rank"] == 1920)
    check("result", "all three causal representatives have rank-128 Green and receiver leak",
          all(candidate[name] == {"green_rank": 128, "raw_rank": 128, "receiver_leak_rank": 128}
              for name in ["timelike", "spacelike", "null"]))
    check("result", "all fourteen diagonal currents are full rank and radial current vanishes",
          candidate["diagonal_current_ranks"] == [128] * 14 and candidate["radial_current_rank"] == 0)
check("result", "action and current live while finite BV is deferred",
      registry["horns"] == {"GRAPH_ACTION_LIVE": True, "FERMION_CURRENT_LIVE": True,
                             "FINITE_BV_ADMITTED": False, "BV_DEFERRED": True})

print("\nC. SOURCE, LAYER 0 AND HOSTILE REVIEW")
check("source", "all source return codes are explicit",
      all(code in source for code in ["SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"]))
check("layer0", "report separates restricted action from full-Euler closure",
      "restricted action" in report and "full Euler" in report)
check("layer0", "report keeps the local Krein pairing nonpositive and nonglobal",
      "It is not a" in report and "positive Hilbert Riesz map" in report
      and "source-selected global reality/domain" in report)
check("hostile", "all three hostile charges are present",
      all(f"Charge {index}" in review for index in [1, 2, 3]))
for lens in ["Layer-0 semantics", "Prior art", "Analytic/operator", "Symplectic/BV-BFV",
             "Representation/Clifford", "Source-critical", "Adversarial scope"]:
    check("hostile", f"review includes {lens}", lens in review)

print("\nD. PROCESS AND EXECUTABLE FENCES")
check("process", "contract points to v0.158", contract["standing_ledger"]["ref"].endswith("v0.158.json"))
check("process", "next gate owns the rank-128 receiver completion", "RANK128_EQUATION_RECEIVER" in registry["next_gate"])
check("process", "parent and rival scopes remain separate", "TWO_U32_32_HALVES_REMAIN_DISTINCT" in registry["parent_scope"])
for path in ["lab/process/RESEARCH-AGENDA.json", "NEXT-STEPS.md", "RESEARCH-STATUS.md", "lab/process/README.md", "lab/process/CURRENT-RESEARCH-CONTEXT.md"]:
    check("process", f"{path} names v0.158", "v0.158" in (ROOT / path).read_text())
check("process", "source index lists the new return", "selected-k77-gamma-trace-graph-dynamics-source-return" in (ROOT / "lab/sources/README.md").read_text())
check("process", "test manifest lists the exact probe", "selected_k77_gamma_trace_graph_dynamics_probe.py" in (ROOT / "tests/README.md").read_text())
check("process", "gate manifest lists this audit", "gamma_trace_graph_dynamics_audit.py" in (ROOT / "process_gates/README.md").read_text())
check("probe", "probe keeps barred fields independent and composes Krein pairing",
      "left_kernel" in probe and "Krein-dual barred carrier" in probe)
check("probe", "probe tests receiver leak and current cancellation",
      "receiver_leak_rank" in probe and "radial tautological current cancels" in probe)
check("probe", "probe stops BV on nonclosure", "BV_DEFERRED_PENDING_SOURCE_OWNED_RECEIVER" in probe)

total = sum(COUNTS.values())
print(f"\nSUMMARY {total-len(FAILURES)}/{total} PASS; counts={dict(COUNTS)}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
