#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.115."""

from pathlib import Path
import json

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot

ROOT = Path(__file__).resolve().parents[1]
FAILURES = []


def check(label, condition):
    if not condition:
        FAILURES.append(label)


def unique(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8-sig"),
                      object_pairs_hook=unique)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8-sig")


ledger = load("lab/process/conditional-physics-ledger-v0.115.json")
registry = load("lab/process/selected-k77-relative-edge-bitorsor-topology.json")
contract = load("lab/methods/research-evidence-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-relative-edge-bitorsor-topology-2026-08-09.md")
review = read("lab/process/hostile-reviews/2026-08-09-selected-k77-relative-edge-bitorsor-topology-review.md")
source = read("lab/sources/selected-k77-relative-edge-bitorsor-source-reinspection-2026-08-09.md")

check("ledger version", ledger["schema_version"] == "0.115")
check("predecessor", ledger["predecessor"].endswith("v0.114.json"))
check("coverage", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdicts", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 2,
    "conditions_opened": 0, "remaining_named_conditions": 2})
check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("source return", ledger["source_return"] == registry["source_return"]
      and "SOURCE_CONFIRMS" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

top = registry["topology"]
check("one-sided theorem", top["one_sided_nonempty_iff"]
      == "P_H_boundary_is_trivial")
check("negative controls", "c1_equals_1" in top["unitary_negative_control"]
      and "c2_equals_1" in top["spin_negative_control"])
check("relative theorem", top["relative_nonempty_iff"]
      == "P_target_is_isomorphic_to_P_reference"
      and top["reference_copy_identity_section"] is True
      and top["new_independent_characteristic_class"] is False)

desc = registry["relative_descent"]
check("relative patching", desc["noncommuting_triple_overlap"] == "EXACT"
      and desc["trace_pairing_global"] is True
      and desc["dressed_moment_map_global"] is True)
check("gauge laws", desc["target_active_gauge_invariant"] is True
      and desc["reference_active_gauge_adjoint"] is True)
check("local kernel", desc["local_dressed_map_rank"] == 8
      and desc["local_presymplectic_rank"] == 8
      and desc["local_kernel_dimension"] == 4
      and desc["target_gauge_orbit_rank"] == 4
      and desc["kernel_equals_target_gauge_orbit"] is True)
check("old formula scoped", desc["one_sided_formula_recovered_when_reference_trivial"] is True)

check("parents separate", registry["action_parent_fence"]["selected"] is False
      and set(registry["action_parent_fence"]) == {
          "spin_native_selected_carrier", "two_u32_32_halves",
          "full_u64_64", "selected"})
check("analytic open", all(value == "OPEN"
      for value in registry["analytic_fence"].values()))
check("accounting", registry["constraint_fence"]["new_physical_fields"] == 0
      and registry["constraint_fence"]["new_independent_bundle_classes"] == 0
      and registry["constraint_fence"]["new_continuous_coefficients"] == 0
      and registry["constraint_fence"]["P1_P2_P3"] == "UNUSED")
check("controls", registry["controls"]["primary"]
      == "34 exact + 10 planted = 44 PASS"
      and registry["controls"]["independent_sage"]
      == "14 exact + 5 planted = 19 PASS"
      and registry["controls"]["v0102_replay"] == "55/55 PASS"
      and registry["controls"]["v0114_replay"] == "49/49 PASS")

migrated = ["LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6"]
rows = {row["id"]: row for row in ledger["rows"]
        if row.get("row_status") != "SUPERSEDED"}
for row_id in migrated:
    check(f"{row_id} evidence", rows[row_id]["evidence"]
          == "selected-k77-relative-edge-bitorsor-topology-2026-08-09.md")
migrations = [m for m in ledger["migrations"]
              if m["from_version"] == "0.114" and m["to_version"] == "0.115"]
check("six migrations", [m["row_id"] for m in migrations] == migrated)
check("no meaning changes", all(m["meaning_changed"] is False for m in migrations))

check("report layer0", "active target gauge action" in report
      and "passive target transition" in report
      and "topologically" in review)
check("source typing", "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source)
check("review verdict", "CANDIDATE_SURVIVES__RELATIVE_BITORSOR_GLOBALIZES_TOPOLOGY" in review)
for lens in ("Layer-0 semantics", "Prior art", "Differential topology",
             "Symplectic", "Gauge geometry", "Functional analysis",
             "Representation/Clifford", "Complex/path integral", "Source"):
    check(f"review lens {lens}", lens in review)

check("ledger ancestry", reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.115.json"))

if FAILURES:
    raise SystemExit("FAIL selected K77 relative edge bitorsor topology audit: "
                     + "; ".join(FAILURES))
print("PASS selected K77 relative edge bitorsor topology audit")
