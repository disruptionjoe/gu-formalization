#!/usr/bin/env python3
"""Durability audit for ledger v0.162 unrestricted four-field Euler image."""

from collections import Counter
import ast
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


ledger = unique_json(ROOT / "lab/process/conditional-physics-ledger-v0.162.json")
result = unique_json(ROOT / "lab/process/selected-k77-unrestricted-four-field-euler-image.json")
predecessor = unique_json(ROOT / "lab/process/conditional-physics-ledger-v0.161.json")
contract = unique_json(ROOT / "lab/methods/research-evidence-contract-v1.0.json")
contract_md = (ROOT / "lab/methods/research-evidence-contract-v1.0.md").read_text()
report = (ROOT / "explorations/conditional-build/selected-k77-unrestricted-four-field-euler-image-2026-08-11.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-11-selected-k77-unrestricted-four-field-euler-image-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-unrestricted-four-field-euler-image-source-return-2026-08-11.md").read_text()
probe_path = ROOT / "tests/channel-swings/selected_k77_unrestricted_four_field_euler_image_probe.py"
probe = probe_path.read_text()

print("A. LEDGER AND ACCOUNTING")
check("ledger", "v0.162 is append-only from v0.161",
      ledger["schema_version"] == "0.162"
      and ledger["predecessor"].endswith("v0.161.json"))
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
          "conditions_opened": 1, "remaining_named_conditions": 2})
rows = {row["id"]: row for row in ledger["rows"]}
touched = ["RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"]
check("ledger", "all six rows point to the unrestricted-image result",
      all(rows[row]["evidence"] ==
          "selected-k77-unrestricted-four-field-euler-image-2026-08-11.md"
          for row in touched))
check("ledger", "all six rows record the bounded-route kill",
      all("BOUNDED_GRAPH_ROUTE_KILLED" in rows[row]["mapping_grade"]
          for row in touched))
check("ledger", "six append-only v0.161 to v0.162 migrations exist",
      sum(1 for migration in ledger["migrations"]
          if migration.get("from_version") == "0.161"
          and migration.get("to_version") == "0.162") == 6)
check("ledger", "predecessor headline accounting is identical",
      ledger["progress"]["verdict_counts"] == predecessor["progress"]["verdict_counts"]
      and ledger["residue"]["continuous_real"] == predecessor["residue"]["continuous_real"]
      and ledger["residue"]["quotients_ranked"] == predecessor["residue"]["quotients_ranked"])

print("\nB. EXACT FOUR-FIELD IMAGE AND ACTION DUAL")
check("exact", "nonnull principal symbols are full rank 1920",
      result["symbol_ranks"]["timelike"] == 1920
      and result["symbol_ranks"]["spacelike"] == 1920)
check("exact", "null representative has finite-field rank 1024",
      result["symbol_ranks"]["null"] == 1024)
check("exact", "tested Euler image and action dual both have rank 1920",
      result["tested_unrestricted_euler_image_rank"] == 1920
      and result["tested_unrestricted_action_dual_rank"] == 1920)
for pin in ["column_pin", "row_pin"]:
    row = result["candidates"][pin]
    check("exact", f"{pin} rank-384 hull is contained properly",
          row["common_hull_rank"] == 384
          and row["common_in_unrestricted_intersection_rank"] == 384
          and row["common_unrestricted_join_rank"] == 1920
          and row["proper_codimension"] == 1536
          and row["common_equals_unrestricted"] is False)
    check("action", f"{pin} paired rank-384 hull is proper in action dual",
          row["paired_common_rank"] == 384
          and row["paired_common_action_dual_intersection_rank"] == 384
          and row["paired_common_action_dual_join_rank"] == 1920
          and row["paired_common_equals_unrestricted_dual"] is False)
    check("scope", f"{pin} null intersection remains separately recorded",
          row["common_null_intersection_rank"] == 192)
check("exact", "both Pin fingerprints agree exactly",
      result["candidates"]["column_pin"] == result["candidates"]["row_pin"])
check("horn", "bounded route is not action owned",
      result["bounded_route_action_owned"] is False)
check("horn", "disposition returns to unrestricted source operator",
      "RETURN_TO_UNRESTRICTED_SOURCE_OPERATOR" in result["disposition"])
check("probe", "probe parses and retains full symbol, pairing and planted controls",
      ast.parse(probe) is not None
      and "rolled_symbol" in probe
      and "pairing.transpose().solve_right" in probe
      and probe.count('check("planted"') >= 3)

print("\nC. SOURCE, LAYER 0 AND HOSTILE REVIEW")
check("source", "source return matches ledger and result",
      ledger["source_return"] == result["source_return"])
check("source", "source artifact records confirms, no correction and silence",
      all(code in source for code in ["SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"]))
check("layer0", "report separates equation image, action dual, BV and datum",
      all(term in report for term in ["unrestricted Euler image", "action dual", "BV constraint", "external datum"]))
check("hostile", "review survives only as a scoped bounded-route kill",
      "verdict: SCOPED_SURVIVES__BOUNDED_GRAPH_ROUTE_KILLED" in review)
check("hostile", "review carries all three hostile charges",
      all(f"Charge {index}" in review for index in [1, 2, 3]))
for lens in ["Layer-0 semantics", "Prior art", "Exact algebra",
             "Variational bicomplex", "Symplectic/BV--BFV",
             "Analytic/operator", "Source criticism", "Adversarial scope"]:
    check("hostile", f"review includes {lens}", lens in review)
check("scope", "source-family and southeast rival survive",
      "southeast-nonzero rival" in report
      and "program does not" in review)
check("datum", "external datum cannot manufacture local closure",
      "cannot manufacture local Euler closure" in report)

print("\nD. PROCESS POINTERS AND SUCCESSOR")
check("process", "current append-only ledger descends to v0.162",
      reaches_historical_snapshot(
          contract, "lab/process/conditional-physics-ledger-v0.162.json"
      ))
check("process", "human contract names the unrestricted source/BV successor",
      "unrestricted four-field" in contract_md and "off-shell constraint/BV" in contract_md)
for path in ["NEXT-STEPS.md", "RESEARCH-STATUS.md",
             "lab/process/README.md", "lab/process/CURRENT-RESEARCH-CONTEXT.md",
             "lab/process/exploration-absorption-priorities-2026-08-10.md"]:
    check("process", f"{path} names v0.162", "v0.162" in (ROOT / path).read_text())
check("process", "source manifest lists this return",
      "selected-k77-unrestricted-four-field-euler-image-source-return" in
      (ROOT / "lab/sources/README.md").read_text())
check("process", "test manifest lists this probe",
      "selected_k77_unrestricted_four_field_euler_image_probe.py" in
      (ROOT / "tests/README.md").read_text())
check("process", "gate manifest lists this audit",
      "unrestricted_four_field_euler_image_audit.py" in
      (ROOT / "process_gates/README.md").read_text())
check("successor", "result and ledger agree on unrestricted source/BV gate",
      result["next_gate"] ==
      "BUILD_THE_UNRESTRICTED_FOUR_FIELD_SOURCE_OPERATOR_WITH_THE_SOURCE_ADMITTED_SOUTHEAST_RIVAL_AND_DERIVE_ITS_OFFSHELL_BV_CONSTRAINT_COMPLEX__NO_POST_VARIATION_RANK384_PROJECTOR"
      and "UNRESTRICTED_SOURCE_BV" in ledger["migrations"][-1]["new"][2])

total = sum(COUNTS.values())
print(f"\nSUMMARY {total-len(FAILURES)}/{total} PASS; counts={dict(COUNTS)}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
