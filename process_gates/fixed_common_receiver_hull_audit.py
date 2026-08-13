#!/usr/bin/env python3
"""Durability audit for ledger v0.161 fixed common receiver hull."""

from collections import Counter
import ast
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


ledger = unique_json(ROOT / "lab/process/conditional-physics-ledger-v0.161.json")
result = unique_json(ROOT / "lab/process/selected-k77-fixed-common-receiver-hull.json")
predecessor = unique_json(ROOT / "lab/process/conditional-physics-ledger-v0.160.json")
contract = unique_json(ROOT / "lab/process/functional-channel-operating-contract-v1.0.json")
contract_md = (ROOT / "lab/process/functional-channel-operating-contract-v1.0.md").read_text()
report = (ROOT / "explorations/conditional-build/selected-k77-fixed-common-receiver-hull-2026-08-11.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-11-selected-k77-fixed-common-receiver-hull-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-fixed-common-receiver-hull-source-return-2026-08-11.md").read_text()
probe_path = ROOT / "tests/channel-swings/selected_k77_fixed_common_receiver_hull_probe.py"
probe = probe_path.read_text()

print("A. LEDGER AND ACCOUNTING")
check("ledger", "v0.161 is append-only from v0.160",
      ledger["schema_version"] == "0.161"
      and ledger["predecessor"].endswith("v0.160.json"))
check("ledger", "coverage remains 82 of 82",
      ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("ledger", "verdict counts remain unchanged",
      ledger["progress"]["verdict_counts"] == {
          "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("ledger", "residue, forks and quotients remain unchanged",
      ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier closes two conditions and opens one",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 2,
          "conditions_opened": 1, "remaining_named_conditions": 3})
rows = {row["id"]: row for row in ledger["rows"]}
touched = ["RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"]
check("ledger", "all six rows point to the common-hull result",
      all(rows[row]["evidence"] ==
          "selected-k77-fixed-common-receiver-hull-2026-08-11.md"
          for row in touched))
check("ledger", "six append-only v0.160 to v0.161 migrations exist",
      sum(1 for migration in ledger["migrations"]
          if migration.get("from_version") == "0.160"
          and migration.get("to_version") == "0.161") == 6)
check("ledger", "predecessor headline accounting is identical",
      ledger["progress"]["verdict_counts"] == predecessor["progress"]["verdict_counts"]
      and ledger["residue"] == predecessor["residue"])

print("\nB. EXACT HULL RESULT")
for pin in ["column_pin", "row_pin"]:
    pin_result = result["pin_candidates"][pin]
    check("exact", f"{pin} original receiver rank is 128",
          pin_result["receiver_rank"] == 128)
    check("exact", f"{pin} all causal minimal receivers have rank 256",
          set(pin_result["per_stratum_minimal_rank"].values()) == {256})
    check("exact", f"{pin} pairwise intersection and join are 128 and 384",
          pin_result["pairwise_intersection_rank"] == 128
          and pin_result["pairwise_join_rank"] == 384)
    check("exact", f"{pin} common equation and action hulls have rank 384",
          pin_result["fixed_common_hull_rank"] == 384
          and pin_result["fixed_common_paired_left_rank"] == 384)
    check("exact", f"{pin} adds 256 equation and paired-left directions",
          pin_result["fixed_common_added_equations"] == 256
          and pin_result["fixed_common_paired_left_added"] == 256)
check("exact", "row and column Pin common hulls coincide as subspaces",
      result["pin_join_rank"] == result["pin_intersection_rank"] == 384)
check("exact", "fixed rank-256 reading is explicitly killed",
      result["rank_256_fixed_hull_survives"] is False)
check("probe", "probe parses and carries exact common-hull controls",
      not ast.parse(probe) is None
      and probe.count('check("planted"') >= 2
      and '"intersection_rank"' in probe)

print("\nC. LAYER 0, SOURCE AND HOSTILE REVIEW")
check("layer0", "bosonic parent constraints are not direct fermion selectors",
      result["layer0"].startswith("P_EPSILON_AND_D_VARPI_CHI_ARE_BOSONIC_PARENT_CONSTRAINTS"))
check("source", "source return matches ledger",
      result["source_return"] == ledger["source_return"])
check("source", "source artifact records confirms and silence",
      "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source)
check("hostile", "review survives only in scoped form",
      "verdict: SCOPED_SURVIVES" in review)
check("hostile", "review carries all three hostile charges",
      all(f"Charge {index}" in review for index in [1, 2, 3]))
for lens in ["Layer-0 semantics", "Prior art", "Differential geometry",
             "Variational bicomplex", "Symplectic/BV-BFV",
             "Operator/Krein/analytic", "Adversarial scope"]:
    check("hostile", f"review includes {lens}", lens in review)
check("scope", "report limits rank 384 to the tested causal bank",
      "smallest tested covector-independent" in report
      and "global nonlinear bundle wholesale" not in report)
check("scope", "unrestricted source operator survives",
      "does not kill the unrestricted source" in report
      or "work returns to the unrestricted source operator" in report)
check("scope", "canon, posture and datum do not move",
      result["disposition"].startswith("PER_STRATUM_RANK256")
      and "No verdict, residue, quotient, P1/P2/P3 assignment" in report)

print("\nD. PROCESS POINTERS AND SUCCESSOR")
check("process", "contract points to v0.161 in both forms",
      contract["standing_ledger"]["ref"].endswith("v0.161.json")
      and contract["standing_ledger"]["human_ref"].endswith("v0.161.md"))
check("process", "machine contract carries the rank-384 directive",
      "RANK384" in contract["standing_ledger"]["source_owned_hull_interface_directive"])
check("process", "human contract carries rank-384 and unrestricted successor",
      "rank-384" in contract_md and "unrestricted four-field Euler" in contract_md)
for path in ["LANES.yaml", "NEXT-STEPS.md", "RESEARCH-STATUS.md",
             "lab/process/README.md", "lab/process/agent-context-pack.md",
             "lab/process/exploration-absorption-priorities-2026-08-10.md"]:
    check("process", f"{path} names v0.161", "v0.161" in (ROOT / path).read_text())
check("process", "source manifest lists this return",
      "selected-k77-fixed-common-receiver-hull-source-return" in
      (ROOT / "lab/sources/README.md").read_text())
check("process", "test manifest lists this probe",
      "selected_k77_fixed_common_receiver_hull_probe.py" in
      (ROOT / "tests/README.md").read_text())
check("process", "gate manifest lists this audit",
      "fixed_common_receiver_hull_audit.py" in
      (ROOT / "process_gates/README.md").read_text())
check("successor", "result and ledger agree on four-field action-dual gate",
      result["next_gate"] ==
      "COMPARE_THE_EXACT_COMMON_HULL_WITH_THE_UNRESTRICTED_FOUR_FIELD_EULER_IMAGE_AND_ACTION_DUAL__ONLY_AN_INDUCED_FERMION_INTERTWINER_MAY_THEN_RUN_GRAPH_MIRROR_RANDOM192_640_832_CONTROLS"
      and "FOUR_FIELD_ACTION_DUAL" in ledger["migrations"][-1]["new"][2])

total = sum(COUNTS.values())
print(f"\nSUMMARY {total-len(FAILURES)}/{total} PASS; counts={dict(COUNTS)}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
