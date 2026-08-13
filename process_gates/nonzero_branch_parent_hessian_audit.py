#!/usr/bin/env python3
"""Process/durability audit for ledger v0.134's parent-Hessian result."""

from collections import Counter
from pathlib import Path
import json


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


ledger = strict("lab/process/conditional-physics-ledger-v0.134.json")
result = strict("lab/process/selected-k77-nonzero-branch-parent-hessian.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-nonzero-branch-parent-hessian-2026-08-10.md").read_text()
report_flat = " ".join(report.replace("**", "").split())
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-nonzero-branch-parent-hessian-review.md").read_text()
priorities = (ROOT / "lab/process/exploration-absorption-priorities-2026-08-10.md").read_text()
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
next_steps = (ROOT / "NEXT-STEPS.md").read_text()
status = (ROOT / "RESEARCH-STATUS.md").read_text()

check("ledger", "v0.134 is append-only from v0.133",
      ledger["predecessor"].endswith("conditional-physics-ledger-v0.133.json")
      and ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_134")
check("ledger", "headline counts and denominator remain unchanged",
      ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
      and ledger["progress"]["verdict_counts"]
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("ledger", "frontier closes one condition without opening another",
      ledger["frontier_delta"]
      == {"headline_delta": "NONE", "conditions_closed": 1,
          "conditions_opened": 0, "remaining_named_conditions": 1})
check("ledger", "source return preserves full group two halves and source silence",
      "FULL_U6464" in ledger["source_return"]
      and "TWO_C32_32" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

parents = result["exact_result"]["parents"]
check("exact", "complete pointwise carrier has rank 229376 and zero radical",
      parents["complete"]["dimension"] == parents["complete"]["rank"] == 229376
      and parents["complete"]["inertia"] == [114659, 114717, 0])
check("exact", "B-adjoint split is complete and nondegenerate",
      parents["B_skew"]["rank"] == 113792
      and parents["B_self_complement"]["rank"] == 115584
      and parents["B_skew"]["inertia"][2] == parents["B_self_complement"]["inertia"][2] == 0)
check("exact", "Weyl block and coset are complete and nondegenerate",
      parents["Weyl_block_even"]["rank"] == 114688
      and parents["Weyl_coset_odd"]["rank"] == 114688
      and parents["Weyl_block_even"]["inertia"][2] == parents["Weyl_coset_odd"]["inertia"][2] == 0)
check("exact", "all fifteen grade banks are full rank",
      len(result["exact_result"]["grade_results"]) == 15
      and all(row["dimension"] == row["rank"] and row["inertia"][2] == 0
              for row in result["exact_result"]["grade_results"].values()))
check("exact", "radial checksum and nonzero-kappa scope are retained",
      result["exact_result"]["radial_hessian"] == "-14*kappa_1"
      and result["branch"]["assumption"] == "kappa_1 != 0")

check("type", "result says no action-derived reduction rather than selecting full U",
      result["disposition"]["preregistered_horn"] == "NONZERO_HESSIAN_OWNS_BOTH"
      and "can also host it" in result["disposition"]["conditional_parent_statement"])
check("type", "report keeps pointwise functional and physical objects separate",
      "pointwise first-transgression connection" in report_flat
      and "not the raw residual" in report_flat.lower()
      and "does not establish a positive physical phase space" in report_flat)
check("type", "two halves remain a reduction inside full source parent",
      "two split Weyl spaces" in report_flat and "moving block reduction" in report_flat
      and "does not lie in the two-half" in report_flat)
check("type", "hostile review preserves reduced-domain dissent",
      "declared moving-Spin connection is a" in review
      and "not as a refutation of all" in review)
check("symplectic", "hostile review contains mandatory symplectic lens and no quotient inflation",
      "Symplectic geometry" in review
      and "no candidate characteristic distribution" in review
      and "says nothing about the coupled" in review)
check("analytic", "finite inertia is fenced from positivity and closed domains",
      "Krein/operator theory" in review and "fundamental-symmetry" in review
      and "functional derivative and boundary domain" in result["layer0"]["not_computed"])

changed = {"LT-GR1", "LT-GR2b", "LT-GR3", "RA-D2", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}
rows = {row["id"]: row for row in ledger["rows"]}
check("ledger", "exactly nine wave dispositions name the intended rows",
      {row["row_id"] for row in ledger["wave_row_dispositions"]} == changed)
check("ledger", "all nine rows cite the new evidence and induced operator successor",
      all(rows[row_id]["evidence"] == "selected-k77-nonzero-branch-parent-hessian-2026-08-10.md"
          and "induced" in rows[row_id]["distance"].lower()
          for row_id in changed))
check("ledger", "nine append-only v0.133 to v0.134 migrations exist",
      sum(edge.get("from_version") == "0.133" and edge.get("to_version") == "0.134"
          for edge in ledger["migrations"]) == 9)
check("ledger", "P1 P2 P3 residue forks and quotients remain unchanged",
      ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5
      and "P1/P2/P3 remain unchanged/unused" in ledger["residue"]["meter"])

check("routing", "contract points to ledger v0.134",
      contract["standing_ledger"]["ref"].endswith("v0.134.json")
      and contract["standing_ledger"]["human_ref"].endswith("v0.134.md"))
check("routing", "contract and context route to the induced source-full operator",
      "RANK229376" in contract["standing_ledger"]["carrier_selection_directive"]
      and "induced source-full K77 Dirac/RS operator" in context)
check("routing", "priority surface promotes induced operator to Build A",
      "Build A — induced fermion selector" in priorities
      and "Build B — coupled functional completion" in priorities)
check("routing", "roadmap and status carry v0.134 headline",
      "v0.134" in next_steps and "229,376" in next_steps
      and "v0.134" in status and "229,376" in status)

check("planted", "PLANT dropping the complement cannot reproduce the total rank",
      parents["B_skew"]["rank"] != parents["complete"]["rank"])
check("planted", "PLANT two-half block alone cannot host odd Phi1 branch",
      "odd Phi1 branch" in result["disposition"]["conditional_parent_statement"]
      and "two-half" in result["disposition"]["conditional_parent_statement"])
check("planted", "PLANT balanced even inertia does not imply the odd coset vanishes",
      parents["Weyl_block_even"]["inertia"][0] == parents["Weyl_block_even"]["inertia"][1]
      and parents["Weyl_coset_odd"]["rank"] > 0)
check("planted", "PLANT no canon verdict or public posture change is booked",
      result["accounting"]["canon_verdict_change"] == "none"
      and result["accounting"]["public_posture_change"] == "none")

print("COUNTS " + " ".join(f"{kind}={count}" for kind, count in sorted(COUNTS.items())))
print(f"PASS {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
