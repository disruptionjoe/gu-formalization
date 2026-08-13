#!/usr/bin/env python3
"""Durability audit for ledger v0.160 source-owned-hull interface."""

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


ledger = unique_json(ROOT / "lab/process/conditional-physics-ledger-v0.160.json")
registry = unique_json(ROOT / "lab/process/selected-k77-source-owned-hull-interface.json")
predecessor = unique_json(ROOT / "lab/process/selected-k77-high-conviction-receiver-completion.json")
contract = unique_json(ROOT / "lab/methods/research-evidence-contract-v1.0.json")
contract_md = (ROOT / "lab/methods/research-evidence-contract-v1.0.md").read_text()
report = (ROOT / "explorations/conditional-build/selected-k77-source-owned-hull-interface-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-source-owned-hull-interface-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-source-owned-hull-interface-source-return-2026-08-10.md").read_text()
probe = (ROOT / "tests/channel-swings/selected_k77_source_owned_hull_interface_probe.py").read_text()

print("A. LEDGER AND ACCOUNTING")
check("ledger", "v0.160 is append-only from v0.159",
      ledger["schema_version"] == "0.160" and ledger["predecessor"].endswith("v0.159.json"))
check("ledger", "coverage remains 82 of 82",
      ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("ledger", "verdict counts remain unchanged",
      ledger["progress"]["verdict_counts"] == {
          "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("ledger", "residue and quotients remain 84 and five",
      ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier closes field-type debit and opens fixed reduction one for one",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 1,
          "conditions_opened": 1, "remaining_named_conditions": 4})
rows = {row["id"]: row for row in ledger["rows"]}
touched = ["RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"]
check("ledger", "all six rows point to the interface result",
      all(rows[row]["evidence"] == "selected-k77-source-owned-hull-interface-2026-08-10.md"
          for row in touched))
check("ledger", "all six rows name the fixed reduction or source-typed ambient correction",
      all("SOURCE_TYPED" in rows[row]["mapping_grade"]
          or "AMBIENT_FIELDS_SOURCE_TYPED" in rows[row]["mapping_grade"] for row in touched))
check("ledger", "six append-only v0.159 to v0.160 migrations exist",
      sum(1 for migration in ledger["migrations"]
          if migration.get("from_version") == "0.159"
          and migration.get("to_version") == "0.160") == 6)

print("\nB. INPUT CERTIFICATE AND LAYER-0 CORRECTION")
check("input", "predecessor exact certificate remains 29 checks green",
      predecessor["checks"]["new"] == 29 and predecessor["checks"]["new_failures"] == 0)
check("input", "predecessor minimal receiver cost is unchanged",
      predecessor["minimal_receiver"] == {
          "old_rank": 128, "new_rank": 256, "added_equations": 128,
          "required_paired_left_fields": 128, "source_owned": False})
check("result", "registry keeps the common fixed-hull rank untested",
      registry["exact_input"]["fixed_common_hull_rank"] == "UNTESTED")
check("result", "registry corrects only ambient field-type ownership",
      registry["layer0_correction"] ==
      "SOURCE_OWNS_AMBIENT_BARRED_AND_UNBARRED_FIELD_TYPES__SOURCE_DOES_NOT_YET_SELECT_THE_FINITE_REDUCTION")
check("result", "early stop rejects fitted or unrestricted selectors",
      "FITTED_PROJECTOR" in registry["early_stop_rule"]
      and "UNRESTRICTED_FUNCTION_VALUED_MAP" in registry["early_stop_rule"])
check("result", "H1 through H7 remain ordered",
      registry["acceptance_gates"] == [
          "H1_SOURCE_TYPED_FIXED_REDUCTION", "H2_FULL_EULER_CLOSURE",
          "H3_VARIATIONAL_NOETHER_OWNERSHIP", "H4_BV_AND_COMMON_DOMAIN",
          "H5_OBSERVATION_CHIRALITY_MIRROR", "H6_DATUM_INDEX_COUNT",
          "H7_RENDEZVOUS"])

print("\nC. SOURCE, HOSTILE REVIEW AND FENCES")
check("source", "source return is identical in ledger and registry",
      ledger["source_return"] == registry["source_return"])
check("source", "source artifact records confirm correct and silent scopes",
      all(code in source for code in ["SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"]))
check("layer0", "report states ambient ownership is not finite selection",
      "source ownership of an ambient carrier is not source selection" in report)
check("layer0", "report forbids equal-rank subspace identification",
      "Equal dimensions do not show that the receiver subspaces are equal" in report)
check("hostile", "review survives only with scoped verdict",
      "verdict: SCOPED_SURVIVES" in review)
check("hostile", "all three hostile charges are present",
      all(f"Charge {index}" in review for index in [1, 2, 3]))
for lens in ["Layer-0 semantics", "Prior art", "Analytic/operator",
             "Symplectic/variational", "BV", "Representation/anomaly/cosmology",
             "Adversarial summary audit"]:
    check("hostile", f"review includes {lens}", lens in review)
check("datum", "external datum remains downstream and cannot manufacture closure",
      "datum manufactures a local receiver" in report)
check("scope", "canon public posture and P1/P2/P3 do not move",
      registry["canon_verdict_change"] == registry["public_posture_change"] == "NONE"
      and registry["p1_p2_p3"] == "UNCHANGED_UNUSED_FOR_LOCAL_CLOSURE")

print("\nD. PROCESS AND EXECUTABLE FENCES")
check("process", "machine contract points to v0.160 in both forms",
      contract["standing_ledger"]["ref"].endswith("v0.160.json")
      and contract["standing_ledger"]["human_ref"].endswith("v0.160.md"))
check("process", "machine contract carries the source-owned-hull directive",
      "source_owned_hull_interface_directive" in contract["standing_ledger"])
check("process", "human contract names the v0.160 correction and fixed reduction",
      "conditional-physics-ledger-v0.160.json" in contract_md
      and "P_epsilon u=u" in contract_md)
for path in ["lab/process/RESEARCH-AGENDA.json", "NEXT-STEPS.md", "RESEARCH-STATUS.md",
             "lab/process/README.md", "lab/process/CURRENT-RESEARCH-CONTEXT.md"]:
    check("process", f"{path} names v0.160", "v0.160" in (ROOT / path).read_text())
check("process", "priority surface names the action-owned moving reduction",
      "P_epsilon u=u" in (ROOT / "lab/process/exploration-absorption-priorities-2026-08-10.md").read_text())
check("process", "source index lists the new return",
      "selected-k77-source-owned-hull-interface-source-return" in
      (ROOT / "lab/sources/README.md").read_text())
check("process", "test manifest lists the composition probe",
      "selected_k77_source_owned_hull_interface_probe.py" in
      (ROOT / "tests/README.md").read_text())
check("process", "gate manifest lists this audit",
      "source_owned_hull_interface_audit.py" in
      (ROOT / "process_gates/README.md").read_text())
check("probe", "probe consumes predecessor registry instead of recomputing its matrices",
      "selected-k77-high-conviction-receiver-completion.json" in probe)
check("probe", "probe carries planted equal-rank and ambient-permission controls",
      probe.count("PLANT") >= 2)
check("probe", "probe preserves H1 through H7 and early stop",
      "H1_SOURCE_TYPED_FIXED_REDUCTION" in probe
      and "H7_RENDEZVOUS" in probe
      and "fitted receiver projector" in probe)

total = sum(COUNTS.values())
print(f"\nSUMMARY {total-len(FAILURES)}/{total} PASS; counts={dict(COUNTS)}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
