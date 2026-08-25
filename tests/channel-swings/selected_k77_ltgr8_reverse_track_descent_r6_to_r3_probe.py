#!/usr/bin/env python3
"""Propagation and failure-path probe for the LT-GR8 reverse-track descent R6-R3."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/selected-k77-ltgr8-reverse-track-descent-r6-to-r3.json"
RESULT = ROOT / "explorations/conditional-build/selected-k77-ltgr8-reverse-track-descent-r6-to-r3-2026-08-23.md"

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "establishes a GU horizon",
    "confirms Jacobson",
    "derives the Einstein equation",
    "prediction credit is awarded",
    "GU supplies the KMS state",
)

EXPECTED_DEMAND_IDS = [
    "D1_EVEN_SCALAR_CONSTRAINT_AND_LAPSE",
    "D2_PHYSICAL_BOUNDARY_LAW",
    "D3_ONE_SIDED_WEDGE_KMS_STATE_CLASS",
    "D4_STRESS_COMPOSITION_THROUGH_OBSERVATION",
    "D5_ORIENTATION_SELECTION_DATA",
    "D6_HELD_OUT_CONSEQUENCE_RESERVED",
]


def load_inputs() -> dict[str, object]:
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "state": (ROOT / "CURRENT-STATE.yaml").read_text(),
        "next_steps": (ROOT / "NEXT-STEPS.md").read_text(),
        "agenda": json.loads((ROOT / "lab/process/RESEARCH-AGENDA.json").read_text()),
    }


def collect_failures(inputs: dict[str, object]) -> tuple[int, list[str]]:
    failures: list[str] = []
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    data = inputs["data"]
    result = inputs["result"]
    state = inputs["state"]
    next_steps = inputs["next_steps"]
    agenda = inputs["agenda"]
    assert isinstance(data, dict) and isinstance(agenda, dict)
    assert isinstance(result, str) and isinstance(state, str) and isinstance(next_steps, str)

    rungs = data["rung_registry"]
    check(set(rungs) == {"vocabulary_note", "R6", "R5", "R4", "R3", "R2", "R1"}, "rung registry complete")
    check("Layer 0" in rungs["vocabulary_note"] and "L1..L7" in rungs["vocabulary_note"], "homonym guard")
    check(data["execution_order"] == ["R6", "R5", "R4", "R3"], "descent order R6-R3")
    check("FROZEN" in rungs["R6"]["status"], "R6 frozen at council")
    for rung in ("R5", "R4", "R3"):
        check(rungs[rung]["status"] == "FROZEN_HERE", f"{rung} frozen here")
    check("DEMAND_INTERFACE" in rungs["R2"]["status"] and "DEMAND_INTERFACE" in rungs["R1"]["status"],
          "R2/R1 receive the interface")
    check("no longer gates R5-R3" in data["gating_correction"], "CBRS-1 gating correction")

    r5 = data["r5_frozen"]
    check(r5["comparator_driven"] is True, "R5 comparator-driven")
    check("ONE frozen undetermined normalization constant" in r5["entropy_functional"], "eta frozen single constant")
    check("NOT a prediction target" in r5["entropy_functional"], "eta not a prediction target")
    check("Wald-Noether" in r5["entropy_functional"], "Wald-only corrections")
    check("Clausius" in r5["equilibrium_law"] and "frozen before use" in r5["equilibrium_law"],
          "equilibrium law frozen")
    check("Rindler flux" in r5["energy_flux"], "flux definition frozen")

    r4 = data["r4_frozen"]
    check(r4["comparator_driven"] is True, "R4 comparator-driven")
    check("local Rindler wedge family" in r4["boundary_identity"], "boundary identity frozen")
    check("NOT cosmological" in r4["boundary_identity"], "boundary type exclusivity")
    check("post-observation-only" in r4["causal_prerequisites"] and "T-4" in r4["causal_prerequisites"],
          "T-4 certificate cited")
    check(r4["kms_demand_type"] == "ONE_SIDED_PER_STATE__NO_GLOBAL_MODULAR_CONJUGATION_NET_DEMANDED",
          "KMS demand one-sided")
    check("W98" in r4["imported_wall"] and "W109" in r4["imported_wall"], "modular wall imported")

    r3 = data["r3_frozen"]
    check(r3["comparator_driven"] is True, "R3 comparator-driven")
    check("even scalar Hamiltonian constraint" in r3["constraint_structure"], "even scalar constraint demand")
    check(len(r3["method_ports"]) == 2, "both method ports")
    check("K109 entry gate" in r3["reduced_state_space"], "K109 entry gate bound")
    check("K107" in r3["reduced_state_space"], "invariant-linear closure cited")
    check(len(r3["imported_typed_negatives"]) == 3, "three imported negatives")
    check(any("WRONG_TYPE" in item for item in r3["imported_typed_negatives"]), "B5 WRONG_TYPE imported")

    interface = data["r2_r1_demand_interface"]
    check([d["id"] for d in interface] == EXPECTED_DEMAND_IDS, "six demands in order")
    check(all(d.get("lands_on") for d in interface), "every demand lands on a named gap")
    check("not reverse-track progress" in data["progress_rule"], "progress rule")

    check(data["mechanism_commitment"] == "NONE", "mechanism commitment NONE")
    check(data["confirmation_credit"] == "NONE", "confirmation credit NONE")
    check(data["ledger_verdict_change"] == "none", "ledger unchanged")
    check(data["canon_verdict_change"] == "none", "canon unchanged")

    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("R6 -> R5 -> R4 -> R3" in " ".join(result.split())
          or "R6 → R5 → R4 → R3" in " ".join(result.split())
          or "`R6 -> R5 -> R4 -> R3`" in " ".join(result.split()),
          "descent order in doc")
    check("homonym" in result, "homonym guard in doc")
    check("a definition, not a claim" in " ".join(result.split()),
          "temperature is a definition")
    check("WITHOUT demanding a global modular" in " ".join(result.split()),
          "one-sided KMS in doc")
    check("Demands, not constructions" in result or "DEMANDS, NOT CONSTRUCTIONS" in result,
          "demand-grade ceiling")
    check("remains `NEEDS`" in result or "remains NEEDS" in result, "LT-GR8 stays NEEDS")
    for phrase in FORBIDDEN_SUMMARY_GRAMMAR:
        check(phrase not in result, f"forbidden grammar absent: {phrase}")

    check("reverse track" in state and "R6" in state, "state records descent")
    check("LT-GR8 REVERSE TRACK DESCENDS" in " ".join(next_steps.split()),
          "next steps announcement")
    items = {item["id"]: item for item in agenda["work_items"]}
    check("descend" in items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]["next_swing"]
          or "descent" in items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]["next_swing"],
          "agenda records descent order")
    return checks, failures


def main() -> int:
    checks, failures = collect_failures(load_inputs())
    for label in failures:
        print(f"[FAIL] {label}")
    if failures:
        return 1
    print(f"PASS {checks}/{checks}")
    return 0


def selftest() -> int:
    baseline = load_inputs()
    checks, failures = collect_failures(baseline)
    if failures:
        for label in failures:
            print(f"[FAIL] baseline: {label}")
        return 1
    print(f"BASELINE PASS {checks}/{checks}")

    mutations: list[tuple[str, str, dict[str, object]]] = []

    changed = copy.deepcopy(baseline)
    changed["data"]["execution_order"] = ["R1", "R2", "R3"]
    mutations.append(("order-inversion", "descent order R6-R3", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["r5_frozen"]["entropy_functional"] = "S = eta * Area; eta predicted by GU"
    mutations.append(("eta-prediction-smuggle", "eta frozen single constant", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["r4_frozen"]["kms_demand_type"] = "TWO_SIDED_FULL_MODULAR_NET"
    mutations.append(("two-sided-kms-regression", "KMS demand one-sided", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["r2_r1_demand_interface"] = changed["data"]["r2_r1_demand_interface"][:5]
    mutations.append(("demand-drop", "six demands in order", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["mechanism_commitment"] = "JACOBSON_1995"
    mutations.append(("mechanism-smuggle", "mechanism commitment NONE", changed))

    changed = copy.deepcopy(baseline)
    changed["result"] = changed["result"].replace(
        "GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY",
        "GU-COMPARATOR-ROUTING-CLASSIFICATION: REMOVED",
    )
    mutations.append(("routing-regression", "routing class", changed))

    # Planted positive: the forbidden-grammar detector must fire on an injected claim.
    changed = copy.deepcopy(baseline)
    changed["result"] += "\nThe descent confirms Jacobson within GU.\n"
    mutations.append(("planted-forbidden-grammar", "forbidden grammar absent: confirms Jacobson", changed))

    ok = True
    for name, expected, mutated in mutations:
        _, caught = collect_failures(mutated)
        if expected not in caught:
            print(f"[FAIL] mutation {name}: expected failing check {expected!r}, got {caught!r}")
            ok = False
        else:
            print(f"MUTATION CAUGHT {name}: [FAIL] {expected}")
    print("FAILURE-PATH SELFTEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
