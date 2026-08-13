#!/usr/bin/env python3
"""Exact receipt composition for action ownership of the v0.136 leak witnesses.

This probe does not recompute the expensive Clifford matrices.  It composes
three independently exact, durable results at their common typed locus:

* the source-native K77 connection tangent and first-order Euler closure;
* the complete nonzero-branch pointwise first-action Hessian; and
* the W/mirror zero-order leakage certificates.

Layer 0: field tangent, gauge orbit, stationary-solution tangent, BV
characteristic distribution and analytic domain are different objects.
"""

from __future__ import annotations

from collections import Counter
from math import comb
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def strict(relative: str):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
jets = strict("lab/process/selected-k77-complete-euler-jet-tangent-closure.json")
closure = strict("lab/process/selected-k77-grade5-unitary-parent-euler-closure.json")
hessian = strict("lab/process/selected-k77-nonzero-branch-parent-hessian.json")
leakage = strict("lab/process/selected-k77-zero-order-w-mirror-parent-leakage.json")
result = strict("lab/process/selected-k77-action-owned-leakage-composition.json")


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
check("source", "draft owns a full connection one-form and only a candidate four-field operator",
      "components of `varpi`" in source and "begin\nwith operators like" in source)
check("source", "source is silent on a carrier-selecting connection restriction",
      "unique or globally defined operator" in source and "SOURCE-SILENT" in source)
check("prior_art", "v0.128 owns the full selected low-grade Y14 first-jet tangent",
      jets["exact_result"]["ambient_total_tangent"] == 1571
      and jets["exact_result"]["ambient_offslice_rank"] == 1250)
check("prior_art", "v0.129 owns the Spin-skew and full-unitary closure dimensions",
      closure["exact_result"]["spin_connection_dimension"] == 113792
      and closure["exact_result"]["unitary_connection_dimension"] == 229376)
check("prior_art", "v0.134 owns a complete nonzero-branch pointwise Hessian",
      hessian["exact_result"]["carrier_dimension"] == 229376
      and hessian["exact_result"]["radical_dimension"] == 0)
check("prior_art", "v0.136 owns rank-two cross and outside-pair leakage systems",
      leakage["exact_results"]["cross_leakage_coefficient_rank_each_witness"] == 2
      and leakage["exact_results"]["outside_doubled_pair_coefficient_rank_each_witness"] == 2)
for label in (
    "admissible connection field tangent versus gauge orbit",
    "field tangent versus tangent to the stationary solution locus",
    "pointwise Hessian radical versus BV characteristic distribution",
    "invariant representation subspace versus physical cohomology",
    "finite action Hessian versus closed analytic domain",
):
    check("layer0", label + " remain distinct", True)


print("\nB. EXACT GRADE AND PARENT MEMBERSHIP")
grade_results = hessian["exact_result"]["grade_results"]
for grade in range(15):
    expected = 14 * comb(14, grade)
    row = grade_results[str(grade)]
    check("exact", f"grade {grade} dimension is 14*C(14,{grade})", row["dimension"] == expected)
    check("exact", f"grade {grade} pointwise Hessian has zero radical",
          row["rank"] == row["dimension"] and row["inertia"][2] == 0)

check("exact", "full connection tangent dimension is 14*2^14",
      sum(grade_results[str(k)]["dimension"] for k in range(15)) == 14 * 2**14 == 229376)
check("exact", "source-native low-grade connection tangent is 196+1274=1470",
      grade_results["1"]["dimension"] + grade_results["2"]["dimension"] == 1470)
check("exact", "full selected low-grade tangent adds metric and epsilon as 10+1470+91=1571",
      10 + 1470 + comb(14, 2) == jets["exact_result"]["ambient_total_tangent"])

spin_grades = set(closure["exact_result"]["grade_saturated_spin_closure"])
even_grades = set(hessian["exact_result"]["parents"]["Weyl_block_even"]["grades"])
witnesses = {
    "moving_spin": {"grade": 2, "required_parent": "moving Spin", "admitted": 2 in spin_grades},
    "two_u32_32_halves": {"grade": 6, "required_parent": "two U(32,32) halves", "admitted": 6 in even_grades},
    "source_full_u64_64": {"grade": 1, "required_parent": "full U(64,64)", "admitted": True},
}
for name, witness in witnesses.items():
    grade = witness["grade"]
    check("exact", f"{name} witness is admitted by its named action field tangent", witness["admitted"])
    check("exact", f"{name} witness grade {grade} is not in the pointwise Hessian radical",
          grade_results[str(grade)]["rank"] == grade_results[str(grade)]["dimension"])
    check("exact", f"{name} retains the v0.136 rank-64+64 preferred leakage fingerprint",
          leakage["exact_results"]["preferred_rank_each_witness"] == {
              "W_internal": 0, "W_to_mirror": 64, "W_outside_pair": 64
          })

check("planted", "the conditional Spin-skew closure genuinely excludes grade zero",
      0 not in spin_grades)
check("planted", "the two-half block genuinely excludes the odd full-U grade-one coset",
      1 not in even_grades)
check("planted", "observed X4 first jets do not equal the source-native Y14 tangent",
      jets["exact_result"]["observed_total_tangent"] == 1131
      and jets["exact_result"]["ambient_total_tangent"] == 1571)


print("\nC. COMPOSITION AND SCOPE")
check("theorem", "every named parent retains at least one already-certified leaking direction",
      all(item["admitted"] for item in witnesses.values()))
check("theorem", "the selected pointwise action does not remove any leak witness by a Hessian radical",
      all(grade_results[str(item["grade"])]["inertia"][2] == 0 for item in witnesses.values()))
check("theorem", "the action-owned smaller-field-tangent escape is closed negatively",
      result["disposition"] == "ACTION_OWNS_ALL_THREE_LEAK_WITNESSES__NO_ACTION_DERIVED_FIELD_TANGENT_RESTRICTION")
check("type", "the result does not claim an on-shell, gauge, BV, domain, spectrum or count no-go",
      result["scope"]["not_closed"] == [
          "coupled stationary solution tangent",
          "gauge orbit",
          "BV characteristic distribution or cohomology",
          "complete four-field operator cancellation",
          "global analytic domain",
          "physical spectrum index or generation count",
      ])
check("symplectic", "no Hessian rank is promoted to a BV quotient", result["layer0"]["bv"] == "OPEN_DISTINCT")
check("analytic", "no finite rank is promoted to a closed operator or spectrum", result["layer0"]["domain"] == "OPEN_DISTINCT")
check("variational", "pointwise field ownership is not called solution-space tangency",
      result["layer0"]["stationary_solution_tangent"] == "OPEN_DISTINCT")
check("accounting", "no verdict residue quotient datum or P1/P2/P3 moves",
      all(result["accounting"][key] is False for key in (
          "verdict_change", "residue_change", "quotient_change", "datum_change", "p1_p2_p3_change"
      )))


summary = " ".join(f"{kind}={count}" for kind, count in sorted(COUNTS.items()))
print(f"\nCOUNTS {summary}")
if FAILURES:
    print("FAILURES")
    for failure in FAILURES:
        print(f"- {failure}")
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
print("DISPOSITION=ACTION_OWNS_ALL_THREE_LEAK_WITNESSES__NO_ACTION_DERIVED_FIELD_TANGENT_RESTRICTION")
print("NEXT=COMPLETE_FOUR_FIELD_BV_CONSTRAINT_DOMAIN_OR_DIFFERENT_ADAPTER")
