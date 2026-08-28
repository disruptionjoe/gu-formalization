#!/usr/bin/env python3
"""Durability/process audit for ledger v0.164 and coupled gauge Noether/BV."""

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


ledger = strict("lab/process/conditional-physics-ledger-v0.164.json")
prior = strict("lab/process/conditional-physics-ledger-v0.163.json")
result = strict("lab/process/selected-k77-coupled-gauge-noether-bv.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-coupled-gauge-noether-bv-2026-08-11.md")
human_ledger = read("explorations/conditional-build/conditional-physics-ledger-v0.164.md")
source = read("lab/sources/selected-k77-coupled-gauge-noether-bv-source-return-2026-08-11.md")
review = read("lab/process/hostile-reviews/2026-08-11-selected-k77-coupled-gauge-noether-bv-review.md")
probe = read("tests/channel-swings/selected_k77_coupled_gauge_noether_bv_probe.py")

print("A. LEDGER AND ACCOUNTING")
check("ledger", "v0.164 is append-only from v0.163",
      ledger["schema_version"] == "0.164"
      and ledger["predecessor"].endswith("v0.163.json"))
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
      all(rows[row_id]["evidence"].endswith("selected-k77-coupled-gauge-noether-bv-2026-08-11.md")
          for row_id in row_ids))
check("ledger", "all six rows record local gauge BV closure",
      all("LOCAL_FULL_FIELD_GAUGE_BV_EXACT" in rows[row_id]["mapping_grade"]
          for row_id in row_ids))
new_migrations = [migration for migration in ledger["migrations"]
                  if migration.get("to_version") == "0.164"]
check("ledger", "six append-only v0.163 to v0.164 migrations exist",
      len(new_migrations) == 6 and {migration["row_id"] for migration in new_migrations} == row_ids)

print("\nB. EXACT GAUGE NOETHER/BV RESULT")
brst = result["minimal_brst"]
check("bv", "minimal differential is nilpotent on every declared field",
      brst["nilpotent_on_every_declared_field"] is True)
check("bv", "nonabelian ghost bracket is nontrivial",
      brst["ghost_bracket_nonzero_control"] is True)
check("gauge", "fermion residuals transform covariantly",
      brst["fermion_residuals_transform_covariantly"] is True)
check("gauge", "independent-dual density is invariant off shell",
      brst["independent_dual_fermion_density_brst_invariant_off_shell"] is True)
check("bv", "ghost-antifield term is required",
      brst["ghost_antifield_term_required"] is True)
check("checks", "the exact probe records 37 passes and zero failures",
      result["checks"]["total"] == 37 and result["checks"]["failures"] == 0)
ast.parse(probe)
for token in ("sA = esub(ecomm(c, A), dc)", "sc = emul(c, c)",
              "szeta = emul(c, zeta)", "sbar_zeta = eneg(emul(bar_zeta, c))",
              "minimal BRST is nilpotent on the connection",
              "fermion density is BRST invariant off shell"):
    check("probe", f"probe retains {token}", token in probe)

print("\nC. MULTIPLICITY-COMMUTANT NO-SELECTION THEOREM")
selection = result["carrier_selection_theorem"]
check("representation", "pointwise carrier is fifteen form slots times spinors",
      "F^15 tensor S" in selection["pointwise_carrier"])
check("representation", "ordinary gauge action is identity on multiplicity",
      selection["gauge_action"] == "I_15 tensor rho")
check("theorem", "rank-384 carriers arise from rank-three multiplicity planes",
      selection["spin_rank"] == 128 and selection["multiplicity_rank"] == 3
      and selection["target_rank"] == 384)
check("theorem", "the invariant family is Gr(3,15) with 36-coordinate chart",
      selection["invariant_family"] == "Gr(3,15)"
      and selection["graph_chart_dimension"] == 36)
check("theorem", "two distinct exact equal-rank witnesses exist",
      selection["distinct_equal_rank_exact_witnesses"] == 2)
check("scope", "ordinary gauge symmetry preserves but does not select",
      "PRESERVES_ANY_SUPPLIED" in selection["conclusion"]
      and "SELECTS_NONE" in selection["conclusion"])
check("scope", "full U and two U-halves leave the multiplicity commutant",
      selection["two_u32_32_halves"].startswith("DOES_NOT_REMOVE")
      and selection["full_u64_64_comparator"].startswith("DOES_NOT_REMOVE"))
check("scope", "the prior rank-384 common hull is neither revived nor refuted",
      selection["v0.161_common_hull"].startswith("NEITHER_REVIVED_NOR_REFUTED"))

print("\nD. SOURCE, HOSTILE REVIEW AND FENCES")
check("source", "source return matches ledger and result",
      ledger["source_return"] == result["source_return"]
      and result["source_return"] in source)
check("source", "return records confirmation, no correction and silence",
      "SOURCE-CONFIRMS" in source and "SOURCE-CORRECTS" in source
      and "None in this Run" in source and "SOURCE-SILENT" in source)
for label in ("Layer-0 semantics", "Prior art", "Exact algebra", "Gauge theory",
              "Representation theory", "Variational bicomplex", "Symplectic/BV--BFV",
              "Analytic/operator", "Source criticism", "Adversarial scope"):
    check("hostile", f"review includes {label}", label in review)
check("hostile", "review carries all three hostile charges",
      all(f"Charge {index}" in review for index in (1, 2, 3)))
check("scope", "report separates local BRST from global BV/BFV",
      "Local BRST nilpotence is not a global BV master action" in report)
check("datum", "P1/P2/P3 remain unused",
      result["p1_p2_p3_change"] == "none" and "P1/P2/P3 remain unused" in report)

print("\nE. PROCESS POINTERS AND SUCCESSOR")
check("process", "human ledger names v0.164", "Ledger v0.164" in human_ledger)
check("process", "current append-only ledger descends to v0.164",
      reaches_historical_snapshot(
          contract, "lab/process/conditional-physics-ledger-v0.164.json"
      ))
for path in ("NEXT-STEPS.md", "RESEARCH-STATUS.md", "lab/process/README.md",
             "lab/process/CURRENT-RESEARCH-CONTEXT.md",
             "lab/process/exploration-absorption-priorities-2026-08-10.md"):
    check("process", f"{path} names v0.164", "v0.164" in read(path))
check("process", "source manifest lists this return",
      "selected-k77-coupled-gauge-noether-bv-source-return" in read("lab/sources/README.md"))
check("process", "test manifest lists this probe",
      "selected_k77_coupled_gauge_noether_bv_probe.py" in read("tests/README.md"))
check("process", "gate manifest lists this audit",
      "coupled_gauge_noether_bv_audit.py" in read("process_gates/README.md"))
check("successor", "result and ledger agree on coupled Green/domain work",
      "SYMMETRIZED_GREEN_PREBOUNDARY" in result["next_gate"]
      and "symmetrized Green/preboundary" in ledger["next_work_queue"][0]["why"])

print(f"\nSUMMARY {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())} PASS; counts={dict(COUNTS)}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
