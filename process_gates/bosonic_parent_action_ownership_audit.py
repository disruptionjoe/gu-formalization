#!/usr/bin/env python3
"""Governance audit for ledger v0.133 bosonic parent action ownership."""

from __future__ import annotations

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
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


ledger = strict("lab/process/conditional-physics-ledger-v0.133.json")
result = strict("lab/process/selected-k77-bosonic-parent-action-ownership.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
rows = {row["id"]: row for row in ledger["rows"]}
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-bosonic-parent-action-ownership-review.md").read_text()
report = (ROOT / "explorations/conditional-build/selected-k77-bosonic-parent-action-ownership-2026-08-10.md").read_text()
canon = (ROOT / "canon/generation-carrier-identification-scope-correction-2026-08-10.md").read_text()

check("ledger", "v0.133 appends to v0.132",
      ledger["schema_version"] == "0.133"
      and ledger["predecessor"].endswith("v0.132.json"))
check("ledger", "coverage and verdict counts remain unchanged",
      ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
      and ledger["progress"]["verdict_counts"]
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("ledger", "residue forks and quotients remain unchanged",
      ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["function_valued_at_least"] == 19
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("result", "both intersecting decompositions are exact",
      result["exact_inputs"]["b_adjoint_split"] == [8128, 8256]
      and result["exact_inputs"]["weyl_block_coset_split"] == [8192, 8192]
      and list(result["exact_inputs"]["cross_cells"].values()) == [4096, 4032, 4096, 4160])
check("result", "zero-branch complement is dynamical rather than constrained",
      result["result"]["zero_branch"].startswith("FULL_QUADRATIC_NORM_HAS_NONZERO_COMPLEMENT_HESSIAN")
      and result["result"]["hard_reduction"] == "NOT_GENERATED_BY_WRITTEN_ACTION_AT_ZERO_BRANCH")
check("result", "nonzero-branch Hessian fails closed as open",
      result["result"]["nonzero_branch_normal_hessian"] == "OPEN")
check("result", "Weyl compatibility is distinct and costs the known branch",
      result["layer0"]["b_adjoint_parity"] == "NOT_WEYL_CHIRALITY"
      and result["result"]["known_nonzero_branch"].startswith("ODD_PHI1"))
check("rows", "all nine rows carry v0.133 evidence",
      all("selected-k77-bosonic-parent-action-ownership" in rows[row_id]["evidence"]
          for row_id in ("RA-D2", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1", "LT-GR1", "LT-GR2b", "LT-GR3")))
check("rows", "fermion rows keep the nonzero bosonic parent gate first",
      all("nonzero" in rows[row_id]["distance"].lower()
          for row_id in ("RA-D2", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1")))
check("rows", "gravity rows require the actual nonzero normal Hessian",
      all("nonzero" in rows[row_id]["distance"].lower()
          and "hessian" in rows[row_id]["distance"].lower()
          for row_id in ("LT-GR1", "LT-GR2b", "LT-GR3")))
check("review", "hostile review keeps the zero-branch scope",
      "CANDIDATE_SURVIVES_WITH_ZERO_BRANCH_SCOPE" in review
      and "NONZERO_BRANCH_NORMAL_HESSIAN_REQUIRED" in review)
check("review", "symplectic and analytic fences are explicit",
      "Symplectic geometry" in review and "Variational/analytic" in review)
check("report", "report names all three closed conditions and the open Hessian",
      "conditions_closed: 3" in report and "conditions_opened: 1" in report
      and "NONZERO_BRANCH_NORMAL_HESSIAN_OPEN" in report)
check("canon", "canon carries only the scope/dependency correction",
      "scope/dependency" in canon and "correction only" in canon
      and "changes no canon verdict" in canon)
check("ledger", "current append-only ledger descends to v0.133",
      reaches_historical_snapshot(
          contract, "lab/process/conditional-physics-ledger-v0.133.json"))
check("accounting", "P1 P2 P3 and all status postures are unchanged",
      result["accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED"
      and all(result[key] == "none" for key in
              ("claim_status_change", "canon_verdict_change", "public_posture_change")))

total = sum(COUNTS.values())
print("CHECKS=" + " ".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"PASS {total-len(FAILURES)}/{total}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
