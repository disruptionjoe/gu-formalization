#!/usr/bin/env python3
"""Durability audit for ledger v0.157 moving-varpi intersection."""

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


ledger = unique_json(ROOT / "lab/process/conditional-physics-ledger-v0.157.json")
registry = unique_json(ROOT / "lab/process/selected-k77-moving-varpi-stationary-intersection.json")
contract = unique_json(ROOT / "lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-moving-varpi-stationary-intersection-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-moving-varpi-stationary-intersection-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-moving-varpi-stationary-intersection-source-return-2026-08-10.md").read_text()
probe = (ROOT / "tests/channel-swings/selected_k77_moving_varpi_stationary_intersection_probe.py").read_text()

print("A. LEDGER AND ACCOUNTING")
check("ledger", "v0.157 is current and append-only from v0.156",
      ledger["schema_version"] == "0.157" and ledger["predecessor"].endswith("v0.156.json"))
check("ledger", "coverage remains 82 of 82", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("ledger", "verdict counts remain unchanged",
      ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("ledger", "residue remains 84", ledger["residue"]["continuous_real"] == 84)
check("ledger", "five quotients remain booked", ledger["residue"]["quotients_ranked"] == 5)
check("ledger", "P1/P2/P3 remain unchanged", "P1/P2/P3 are unchanged" in ledger["residue"]["meter"])
check("ledger", "frontier delta is 3 closed 1 opened 3 remaining",
      ledger["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3,
                                   "conditions_opened": 1, "remaining_named_conditions": 3})

rows = {row["id"]: row for row in ledger["rows"]}
touched = ["RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"]
check("ledger", "all six declared rows exist", all(row in rows for row in touched))
check("ledger", "all six point to the moving-varpi result",
      all(rows[row]["evidence"] == "selected-k77-moving-varpi-stationary-intersection-2026-08-10.md" for row in touched))
check("ledger", "all six migrations are append-only from v0.156",
      sum(1 for migration in ledger["migrations"]
          if migration.get("from_version") == "0.156" and migration.get("to_version") == "0.157") == 6)

print("\nB. EXACT RESULT REGISTRY")
check("result", "both exact branch amplitudes are recorded nonzero",
      registry["tautological_family"]["both_nonzero"] and registry["tautological_family"]["branch_numerator_norm"] == 6)
check("result", "both canonical candidates have rank/nullity 1792/128",
      all(row["rank"] == 1792 and row["nullity"] == 128 for row in registry["candidates"].values()))
check("result", "both candidates retain rank-128 ports and lower rows",
      all(row["port_rank"] == row["lower_rank"] == 128 for row in registry["candidates"].values()))
check("result", "characteristic-zero nullity is exact",
      registry["characteristic_zero_certificate"] == {
          "upper_left_good_prime_invertible": True,
          "explicit_qq_i_kernel_graph_rank": 128,
          "exact_nullity": 128,
      })
check("result", "kernel is Omega0 to gamma-trace Omega1",
      registry["kernel_typing"]["graph"] == "OMEGA0_TO_GAMMA_TRACE_OMEGA1")
check("result", "kernel projects to zero under RS, W and mirror",
      all(registry["kernel_typing"][key] == 0
          for key in ["pi_rs_projection", "w_projection", "mirror_projection"]))
check("result", "physical BV/domain and index/count remain open",
      registry["kernel_typing"]["physical_bv_domain"] == "OPEN"
      and registry["kernel_typing"]["index_count"] == "OPEN")
check("result", "southeast-zero scope is explicit", "SOUTHEAST_ZERO" in registry["operator_scope"])
check("result", "two-half port is not claimed", "NO_TWO_HALF_PORT_CLAIM" in registry["parent_scope"])

print("\nC. LAYER 0, SOURCE AND HOSTILE FENCES")
check("layer0", "report distinguishes fixed and tautological connections",
      "a_i P" in report and "s gamma_i" in report)
check("layer0", "report separates algebraic and differential modes",
      "zero-order algebraic block" in report and "full differential operator" in report)
check("layer0", "report places the graph outside W and mirror",
      "common annihilator" not in report or ("W graph_1" in report and "Mirror graph_1" in report))
check("source", "source return has all three dispositions",
      all(code in source for code in ["SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"]))
check("source", "source-admitted southeast rival stays open", "southeast-nonzero" in source)
check("hostile", "summary overrun charge is present", "Charge 1" in review and "128 fermions" in review)
check("hostile", "superseded-object charge is present", "Charge 2" in review and "Layer-0 homonym" in review)
check("hostile", "downstream disposition charge is present", "Charge 3" in review and "needs-recheck" in review)
for lens in ["Layer-0 semantics", "Prior art", "Differential geometry", "Representation/Clifford",
             "Variational bicomplex", "Symplectic/BV-BFV", "Operator/Krein/analytic", "Adversarial scope"]:
    check("hostile", f"hostile review includes {lens}", lens in review)

print("\nD. PROCESS POINTERS AND SUCCESSOR")
check("process", "current append-only ledger descends to v0.157", reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.157.json"
))
check("process", "successor couples current and differential domain", "DIFFERENTIAL_BV_GREEN_DOMAIN" in registry["next_gate"])
check("process", "successor forbids count inference", "NO_COUNT_INFERENCE" in registry["next_gate"])
for path in ["NEXT-STEPS.md", "RESEARCH-STATUS.md", "lab/process/README.md", "lab/process/CURRENT-RESEARCH-CONTEXT.md"]:
    check("process", f"{path} names v0.157", "v0.157" in (ROOT / path).read_text())
check("process", "source index lists the return", "selected-k77-moving-varpi-stationary-intersection-source-return" in (ROOT / "lab/sources/README.md").read_text())
check("process", "test manifest lists the exact probe", "selected_k77_moving_varpi_stationary_intersection_probe.py" in (ROOT / "tests/README.md").read_text())
check("process", "process-gate manifest lists this audit", "moving_varpi_stationary_intersection_audit.py" in (ROOT / "process_gates/README.md").read_text())

print("\nE. EXECUTABLE PROBE FENCES")
check("probe", "probe uses the componentwise operator", "def contracted_one_form_operator" in probe)
check("probe", "probe replays the immutable predecessor", "load_predecessor" in probe)
check("probe", "probe has a nondecomposable plant", "nondecomposable component plant" in probe)
check("probe", "probe builds explicit QQ(i) graphs", "QQ(i)" in probe and "tautological_kernel_graphs" in probe)
check("probe", "probe checks RS, W and mirror projections",
      all(token in probe for token in ['active_structures["rs"]', 'active_structures["W"]', 'active_structures["M"]']))
check("probe", "probe carries variational, analytic and symplectic fences",
      all(f'("{kind}"' in probe for kind in ["variational", "analytic", "symplectic"]))

total = sum(COUNTS.values())
print(f"\nSUMMARY {total-len(FAILURES)}/{total} PASS; counts={dict(COUNTS)}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
