#!/usr/bin/env python3
"""Exact K109 current-candidate positivity/domain owner census."""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
K108_PROBE = ROOT / "tests/channel-swings/selected_k108_rsap_physical_split_positivity_owner_gate_probe.py"
REGISTRY = ROOT / "lab/process/selected-k109-rsap-concrete-positivity-domain-owner-census.json"
RESULT = ROOT / "explorations/conditional-build/selected-k109-rsap-concrete-positivity-domain-owner-census-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k109-rsap-concrete-positivity-domain-owner-census-review.md"
CURRENT = ROOT / "CURRENT-STATE.yaml"
NEXT = ROOT / "NEXT-STEPS.md"
CONTEXT = ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md"
K107 = ROOT / "lab/process/selected-k107-rsap-phase-space-compatible-complex-positivity.json"
K108 = ROOT / "lab/process/selected-k108-rsap-physical-split-positivity-owner-gate.json"
VRS1 = ROOT / "lab/process/superposition-vrs1-internal-complex-source-census.json"
C_OPERATOR = ROOT / "lab/process/first-perturbative-background-c-operator.json"
GREEN_RESULT = ROOT / "explorations/conditional-build/selected-branch-linearized-totalization-current-green-domain-2026-08-05.md"
NONLOCAL_RESULT = ROOT / "explorations/conditional-build/selected-k77-nonlocal-ultrahyperbolic-polarization-gate-2026-08-11.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


print("A. PREDECESSOR AND DURABLE FILES")
k108_output = io.StringIO()
k108_code = None
with contextlib.redirect_stdout(k108_output):
    try:
        runpy.run_path(str(K108_PROBE), run_name="__main__")
    except SystemExit as error:
        k108_code = error.code
check("predecessor", "K108 physical-split certificate replays cleanly",
      k108_code == 0 and '"failures": []' in k108_output.getvalue())
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. SOURCE EVIDENCE FOR THE THREE STRONGEST PARTIALS")
k107 = load(K107)
k108 = load(K108)
vrs1 = load(VRS1)
c_operator = load(C_OPERATOR)
green_text = GREEN_RESULT.read_text(encoding="utf-8")
nonlocal_text = NONLOCAL_RESULT.read_text(encoding="utf-8")
check("carrier", "K107 retains the conditional 98D phase tangent",
      k107["carrier"]["phase_dimension"] == 98)
check("pairing", "K107 phase pairing remains indefinite",
      k107["compatible_complex_classification"]["g_J_signature"] == "48_50_OR_50_48"
      and k107["compatible_complex_classification"]["positive_compatible_invariant_complex_structure_exists"] is False)
check("physical", "K108 physical split is a distinct 80D conditional carrier",
      k108["physical_split"]["cotangent_reduction_dimension"] == 80)
check("physical", "K108 physical split remains indefinite",
      k108["physical_split"]["invariant_form_signature"] == [18, 22])
check("positive", "the TT C-operator is exactly positive on its fixed block",
      c_operator["result"]["background_c"] == "EXACT_UNIQUE_POSITIVE_ON_REAL_COMPONENT_CONNECTED_TO_FREE_POINT")
check("positive", "the TT C-operator leaves the full nonlinear or QFT C open",
      c_operator["result"]["full_nonlinear_or_qft_c"] == "OPEN")
check("domain", "the observed defect construction has a common Green core",
      "common **defect** Krein/Green domain" in green_text
      and "common core" in green_text)
check("domain", "the observed defect domain explicitly does not prove positivity",
      "does not prove positive energy" in green_text)
check("domain", "the ultrahyperbolic restriction is explicitly not a physical closed domain",
      "not a physical\nclosed domain" in nonlocal_text)
moving_j_rows = [row for row in vrs1["candidate_families"] if row["id"] == "CS-MOVE"]
check("moving_j", "moving J10 remains fibrewise-only",
      len(moving_j_rows) == 1
      and moving_j_rows[0]["status"] == "NOT_YET_FALSIFIED_PARTIAL_CONSTRUCTION")
i2_rows = [row for row in vrs1["candidate_families"] if row["id"] == "CS-I2"]
check("i2", "I2 is typed as a differential owner rather than standalone J",
      len(i2_rows) == 1
      and i2_rows[0]["status"] == "RETYPED_AS_DIFFERENTIAL_OWNER__KILLED_AS_STANDALONE_J")
check("composite", "the surviving composite is named but not constructed",
      vrs1["surviving_composite"]["status"] == "NOT_YET_FALSIFIED__NOT_CONSTRUCTED")


print("\nC. CENSUS MATRIX")
registry = load(REGISTRY)
candidates = registry["candidates"]
check("registry", "the census contains exactly nine unique rows",
      len(candidates) == 9 and len({row["id"] for row in candidates}) == 9)
check("registry", "every row cites existing evidence",
      all((ROOT / row["evidence"]).exists() for row in candidates))
check("eligibility", "no current row meets the full entry criterion",
      not any(row["eligible"] for row in candidates))
check("eligibility", "the eligible count is exactly zero",
      sum(bool(row["eligible"]) for row in candidates) == 0)
carrier_yes = sum(row["carrier"] == "YES_CONDITIONAL_98D" for row in candidates)
pairing_yes = sum(row["positive_pairing"].startswith("YES_") for row in candidates)
domain_yes = sum(row["closed_domain"].startswith("YES_") for row in candidates)
check("count", "exactly two rows own the conditional 98D carrier", carrier_yes == 2)
check("count", "exactly one row owns an exact positive pairing", pairing_yes == 1)
check("count", "exactly one row owns a conditional common closed domain", domain_yes == 1)
check("count", "serialized counts match recomputation",
      registry["counts"] == {
          "candidate_rows": 9,
          "conditional_98d_carrier_yes": carrier_yes,
          "exact_positive_pairing_yes": pairing_yes,
          "conditional_common_closed_domain_yes": domain_yes,
          "full_entry_criterion_yes": 0,
      })
check("composition", "partial owners are explicitly not silently composed",
      registry["strongest_partial_results"]["composition"].startswith("TYPE_MISSING"))


print("\nD. CLAIM CEILING AND REVERSE SCAFFOLD")
ceiling = registry["claim_ceiling"]
check("ceiling", "the current named inventory is exhausted", ceiling["current_named_inventory_exhausted"] is True)
check("ceiling", "future action-admissible candidates remain open", ceiling["all_future_action_admissible_candidates_exhausted"] is False)
check("ceiling", "no universal positivity no-go is claimed", ceiling["universal_positivity_no_go_proved"] is False)
check("ceiling", "H-Q* is narrowed but not killed", ceiling["H_Q_star"] == "NARROWED_UNCONSTRUCTED_NOT_KILLED")
check("ceiling", "H0 is strengthened but not proved", ceiling["H0"] == "STRENGTHENED_NOT_PROVED")
check("reverse", "the conditional classical 98D RSAP is retained",
      ceiling["conditional_classical_98d_rsap"] == "RETAINED")
check("reverse", "the reverse scaffold preserves R0 and classical BFV",
      "CONDITIONAL_BALANCED_SEED_R0" in registry["reverse_scaffold"]["retain"]
      and "EXACT_FINITE_CLASSICAL_BFV_CHARGE" in registry["reverse_scaffold"]["retain"])
check("park", "only the current positivity inventory lane is parked",
      registry["disposition"]["current_positivity_inventory_lane"] == "PARKED_PENDING_NEW_OWNER")
check("routing", "the result remains source-native and changes no ledger",
      registry["comparator_routing_classification"] == "SOURCE_NATIVE_ROUTE"
      and registry["disposition"]["ledger_change"] == "none")


print("\nE. ROADMAP AND SUCCESSOR")
current_text = CURRENT.read_text(encoding="utf-8")
next_text = NEXT.read_text(encoding="utf-8")
context_text = CONTEXT.read_text(encoding="utf-8")
k108_result = (ROOT / "explorations/conditional-build/selected-k108-rsap-physical-split-positivity-owner-gate-2026-08-15.md").read_text(encoding="utf-8")
check("roadmap", "CURRENT records K109 and the zero-of-nine result",
      "K109" in current_text
      and "zero of nine" in " ".join(current_text.lower().split()))
check("roadmap", "NEXT parks the current inventory rather than all future routes",
      "K109" in next_text and "current inventory" in next_text)
check("roadmap", "context pack names the new-owner intake packet",
      "K109" in context_text and "typed owner packet" in context_text)
check("successor", "K108 records the K109 successor closure",
      "Successor closure (K109)" in k108_result)


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES,
           "by_kind": dict(COUNTS)}
print("\n" + json.dumps(summary, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
