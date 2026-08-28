#!/usr/bin/env python3
"""Durability/process audit for ledger v0.163 and the southeast/BV-kernel gate."""

from __future__ import annotations

from collections import Counter
import ast
import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def read(path: str) -> str:
    return (ROOT / path).read_text()


def strict(path: str):
    def reject(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r} in {path}")
            out[key] = value
        return out
    return json.loads(read(path), object_pairs_hook=reject)


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


ledger = strict("lab/process/conditional-physics-ledger-v0.163.json")
prior = strict("lab/process/conditional-physics-ledger-v0.162.json")
result = strict("lab/process/selected-k77-unrestricted-southeast-bv-kernel.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-unrestricted-southeast-bv-kernel-2026-08-11.md")
human_ledger = read("explorations/conditional-build/conditional-physics-ledger-v0.163.md")
source = read("lab/sources/selected-k77-unrestricted-southeast-bv-kernel-source-return-2026-08-11.md")
review = read("lab/process/hostile-reviews/2026-08-11-selected-k77-unrestricted-southeast-bv-kernel-review.md")
probe = read("tests/channel-swings/selected_k77_unrestricted_southeast_bv_kernel_probe.py")

print("A. LEDGER AND ACCOUNTING")
check("ledger", "v0.163 is append-only from v0.162",
      ledger["schema_version"] == "0.163"
      and ledger["predecessor"].endswith("v0.162.json"))
check("ledger", "coverage remains 82 of 82",
      ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("ledger", "verdict counts remain unchanged",
      ledger["progress"]["verdict_counts"] == prior["progress"]["verdict_counts"]
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
for key in ("continuous_real", "function_valued_at_least", "open_discrete_forks", "quotients_ranked"):
    check("ledger", f"residue field {key} remains unchanged",
          ledger["residue"][key] == prior["residue"][key])
check("ledger", "frontier closes two conditions and opens one",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 2,
          "conditions_opened": 1, "remaining_named_conditions": 2})
row_ids = {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}
rows = {row["id"]: row for row in ledger["rows"]}
check("ledger", "all six rows point to this result",
      all(rows[row_id]["evidence"].endswith("selected-k77-unrestricted-southeast-bv-kernel-2026-08-11.md")
          for row_id in row_ids))
check("ledger", "all six rows record the fermion-only principal-BV kill",
      all("FERMION_ONLY_PRINCIPAL_BV_KILLED" in rows[row_id]["mapping_grade"]
          for row_id in row_ids))
new_migrations = [m for m in ledger["migrations"] if m.get("to_version") == "0.163"]
check("ledger", "six append-only v0.162 to v0.163 migrations exist",
      len(new_migrations) == 6 and {m["row_id"] for m in new_migrations} == row_ids)

print("\nB. EXACT SOUTHEAST AND PRINCIPAL-BV RESULT")
check("construction", "the smallest K77 southeast family has two parameters",
      result["parameter_dimension"] == 2
      and "ell_plus" in result["southeast_family"]
      and "ell_minus" in result["southeast_family"])
for causal in ("timelike", "spacelike"):
    row = result["nonnull"][causal]
    check("exact", f"{causal} base and 11/12 comparator are full rank",
          row["base_rank"] == row["k95_11_12_coflip_comparator_rank"] == 1920)
    check("exact", f"{causal} inverse bottom-right block is zero",
          row["inverse_bottom_right_rank"] == 0)
    check("theorem", f"{causal} determinant is southeast-independent",
          row["all_southeast_matrices_determinant_equivalent"] is True)
check("null", "sampled null ranks and nullity are exact",
      result["null"]["zero_southeast_rank"] == 1024
      and result["null"]["k95_11_12_coflip_comparator_rank"] == 1024
      and result["null"]["right_nullity"] == 896)
check("layer0", "null kernel is typed as propagation not gauge",
      result["null"]["typed_as"] == "CHARACTERISTIC_PROPAGATION_NOT_GAUGE_IDENTITY")
check("bv", "fermion-only right generator and left Noether identity are killed",
      result["fermion_only_principal_gauge_generator"].startswith("PROVABLY_ZERO")
      and result["fermion_only_principal_noether_identity"].startswith("PROVABLY_ZERO"))
check("scope", "full-field ordinary-gauge BV remains open and distinct",
      result["full_field_ordinary_gauge_bv"].startswith("OPEN_DISTINCT"))
ast.parse(probe)
for token in ("a_block * b_block", "c_block * b_block", "base * inverse_bottom_columns",
              "bottom_projection * inverse_bottom_columns", "Matrix determinant lemma",
              "nontrivial_fermion_principal_generator = False"):
    check("probe", f"probe retains {token}", token in probe)

print("\nC. SOURCE, HOSTILE REVIEW AND FENCES")
check("source", "source return matches ledger and result",
      ledger["source_return"] == result["source_return"]
      and result["source_return"] in source)
check("source", "return records confirms, no correction and silence",
      "SOURCE-CONFIRMS" in source and "SOURCE-CORRECTS:** none" in source
      and "SOURCE-SILENT:**" in source)
for label in ("Layer-0 semantics", "Prior art", "Exact algebra", "Variational bicomplex",
              "Symplectic/BV--BFV", "Analytic/operator", "Hyperbolic equations",
              "Source criticism", "Adversarial scope"):
    check("hostile", f"review includes {label}", label in review)
check("hostile", "review carries all three hostile charges",
      all(f"Charge {index}" in review for index in (1, 2, 3)))
check("scope", "review preserves source family and K95 scope",
      "source family" in review and "K95 B2C4" in review and "Survives" in review)
check("datum", "external datum cannot create the local Noether identity",
      "external datum cannot supply" in report)

print("\nD. PROCESS POINTERS AND SUCCESSOR")
check("process", "human ledger and result agree on v0.163", "Ledger v0.163" in human_ledger)
check("process", "current append-only ledger descends to v0.163",
      reaches_historical_snapshot(
          contract, "lab/process/conditional-physics-ledger-v0.163.json"
      ))
for path in ("NEXT-STEPS.md", "RESEARCH-STATUS.md", "lab/process/README.md",
             "lab/process/CURRENT-RESEARCH-CONTEXT.md", "lab/process/exploration-absorption-priorities-2026-08-10.md"):
    check("process", f"{path} names v0.163", "v0.163" in read(path))
check("process", "source manifest lists this return",
      "selected-k77-unrestricted-southeast-bv-kernel-source-return" in read("lab/sources/README.md"))
check("process", "test manifest lists this probe",
      "selected_k77_unrestricted_southeast_bv_kernel_probe.py" in read("tests/README.md"))
check("process", "gate manifest lists this audit",
      "unrestricted_southeast_bv_kernel_audit.py" in read("process_gates/README.md"))
check("successor", "result and ledger agree on coupled full-field gauge BV",
      "BUILD_THE_COUPLED_VARPI_PLUS_FOUR_FERMION" in result["next_gate"]
      and "coupled varpi plus four-independent-fermion" in ledger["next_work_queue"][0]["why"])

print(f"\nSUMMARY {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())} PASS; counts={dict(COUNTS)}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
