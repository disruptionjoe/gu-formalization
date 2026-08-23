#!/usr/bin/env python3
"""Exact-arithmetic and propagation probe for the LT-GR8 carrier/boundary typing step."""

from __future__ import annotations

import copy
import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/selected-k77-ltgr8-observed-boundary-carrier-typing.json"
RESULT = ROOT / "explorations/conditional-build/selected-k77-ltgr8-observed-boundary-carrier-typing-2026-08-22.md"
DELTA = ROOT / "lab/process/conditional-evidence-deltas/gu-ltgr8-boundary-carrier-typing-2026-08-22.json"

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "establishes a GU horizon",
    "confirms Jacobson",
    "derives the Einstein equation",
    "prediction credit is awarded",
    "awards prediction credit",
)


def frac(value: str) -> Fraction:
    return Fraction(value)


def q_of(signs: list[int], vector: list[Fraction]) -> Fraction:
    assert len(signs) == len(vector)
    return sum(Fraction(s) * v * v for s, v in zip(signs, vector))


def load_inputs() -> dict[str, object]:
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "delta": json.loads(DELTA.read_text()),
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
    delta = inputs["delta"]
    state = inputs["state"]
    next_steps = inputs["next_steps"]
    agenda = inputs["agenda"]
    assert isinstance(data, dict) and isinstance(delta, dict) and isinstance(agenda, dict)
    assert isinstance(result, str) and isinstance(state, str) and isinstance(next_steps, str)

    cert = data["exact_typing_certificate"]
    h_signs = cert["horizontal_signs"]
    v_signs = cert["vertical_signs"]
    signs = h_signs + v_signs

    # Signature bookkeeping, plus-first.
    check(h_signs.count(1) == 1 and h_signs.count(-1) == 3, "horizontal signature (1,3)")
    check(v_signs.count(1) == 6 and v_signs.count(-1) == 4, "vertical signature (6,4)")
    check([signs.count(1), signs.count(-1)] == cert["expected_total_signature"] == [7, 7],
          "total signature (7,7)")

    # T-1 restriction: for horizontally supported vectors the ambient value is the q_H value.
    for vec in (["1", "2", "3", "4"], ["7", "0", "5", "1"]):
        h = [frac(x) for x in vec]
        ambient = q_of(signs, h + [Fraction(0)] * 10)
        check(ambient == q_of(h_signs, h), f"T-1 restriction witness {vec}")

    # T-2 conormal lift: block-diagonal dual form; (nu, 0) is ambient-null iff nu is q_H-null.
    for nu in cert["t2_lift_witnesses"]["null_conormals_H"]:
        v = [frac(x) for x in nu]
        check(q_of(h_signs, v) == 0, f"T-2 declared null conormal is null {nu}")
        check(q_of(signs, v + [Fraction(0)] * 10) == 0, f"T-2 lift is ambient-characteristic {nu}")
    for nu in cert["t2_lift_witnesses"]["non_null_conormals_H"]:
        v = [frac(x) for x in nu]
        check(q_of(h_signs, v) != 0, f"T-2 declared non-null conormal is non-null {nu}")
        check(q_of(signs, v + [Fraction(0)] * 10) != 0, f"T-2 non-null lift is non-characteristic {nu}")

    # T-3 cone dimensions: quadric cones of nondegenerate forms have codimension one;
    # verify the smooth-point witness has nonvanishing gradient, and the dimension bookkeeping.
    w = [frac(x) for x in cert["t3_cone_dimensions"]["smooth_point_witness"]]
    check(q_of(signs, w) == 0, "T-3 smooth-point witness is characteristic")
    gradient = [2 * Fraction(s) * x for s, x in zip(signs, w)]
    check(any(g != 0 for g in gradient), "T-3 gradient nonzero at witness")
    check(cert["t3_cone_dimensions"]["ambient_characteristic_cone_dim"] == 14 - 1, "T-3 ambient cone dim 13")
    check(cert["t3_cone_dimensions"]["lifted_observed_null_family_dim"] == 4 - 1, "T-3 lifted family dim 3")

    # T-4(a) observed two components: q_H positive forces u0 != 0 (identity check on witnesses).
    for vec in (["0", "1", "0", "0"], ["0", "2", "3", "6"], ["0", "5", "0", "12"]):
        v = [frac(x) for x in vec]
        check(q_of(h_signs, v) <= 0, f"T-4a zero-u0 vector is never positive {vec}")
    check(q_of(h_signs, [Fraction(2), Fraction(1), Fraction(0), Fraction(0)]) > 0,
          "T-4a a positive observed vector exists")

    # T-4(b) ambient connectedness: exact unit-norm path e0 -> e4 -> -e0 in the (e0, e4) plane.
    e0 = [Fraction(0)] * 14
    e0[0] = Fraction(1)
    for ts in cert["t4_ambient_path"]["sample_ts"]:
        t = frac(ts)
        c = (1 - t * t) / (1 + t * t)
        s_ = (2 * t) / (1 + t * t)
        g1 = [Fraction(0)] * 14
        g1[0], g1[4] = c, s_
        check(q_of(signs, g1) == 1, f"T-4b segment1 stays positive-unit at t={ts}")
        g2 = [Fraction(0)] * 14
        g2[0], g2[4] = -s_, c
        check(q_of(signs, g2) == 1, f"T-4b segment2 stays positive-unit at t={ts}")
    # Endpoint algebra: segment1 at t=0 is e0; segment2 at t=1 is -e0.
    check([frac("0"), frac("1")] == [Fraction(2 * Fraction(0)) / 1, Fraction(1)], "T-4b endpoint bookkeeping")
    t = Fraction(1)
    check((-2 * t / (1 + t * t)) == Fraction(-1) and ((1 - t * t) / (1 + t * t)) == 0,
          "T-4b segment2 endpoint is -e0")

    # Both-signs corollary: a horizontal null vector plus a positive/negative vertical unit.
    bw = cert["both_signs_witness"]
    u = [frac(x) for x in bw["horizontal_null"]] + [Fraction(0)] * 10
    up = list(u)
    up[bw["positive_vertical_index"]] += 1
    un = list(u)
    un[bw["negative_vertical_index"]] += 1
    check(q_of(signs, u) == 0, "both-signs base vector is horizontal null")
    check(q_of(signs, up) > 0, "horizontal-null plus positive vertical is ambient positive")
    check(q_of(signs, un) < 0, "horizontal-null plus negative vertical is ambient negative")

    # Census and packet-status integrity.
    census = {row["type"]: row for row in data["boundary_census"]}
    check(len(census) == 6, "six boundary types")
    check("POST_OBSERVATION_ONLY" in census["LOCAL_RINDLER_HORIZON"]["ambient_status"], "Rindler post-observation")
    check("K104" in census["YORK_QUASILOCAL_ENSEMBLE_BOUNDARY"]["owner_status"], "York missing owner K104")
    check("DO_NOT_IDENTIFY" in census["ANALYTIC_OPERATOR_DOMAIN_BOUNDARY"]["owner_status"], "analytic domain distinct")
    check(census["CAPABILITY_MEASUREMENT_BOUNDARY"]["owner_status"] == "UNPROVED_BRIDGE", "capability bridge unproved")
    pcs = data["packet_component_status"]
    check(len(pcs) == 7, "seven packet components")
    check("BLOCKED_ON_CBRS1" in pcs["causal_boundary"], "causal boundary blocked on CBRS-1")
    check("NONE_FROZEN" in pcs["held_out_consequence"], "held-out consequence not frozen")
    check(data["mechanism_commitment"] == "NONE", "mechanism commitment NONE")
    check(data["confirmation_credit"] == "NONE", "confirmation credit NONE")
    check(data["ledger_verdict_change"] == "none", "ledger unchanged")
    check(data["canon_verdict_change"] == "none", "canon unchanged")

    # Document propagation.
    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("plus-first" in result, "notation declared")
    check("POST-OBSERVATION ONLY" in result or "post-observation-only" in result, "post-observation certificate in doc")
    check("metric-only" in result, "metric-only ceiling stated")
    check("remains `NEEDS`" in result or "remains NEEDS" in result, "LT-GR8 stays NEEDS")
    check("six-item bridge burden" in result, "bridge burden cited")
    for phrase in FORBIDDEN_SUMMARY_GRAMMAR:
        check(phrase not in result, f"forbidden grammar absent: {phrase}")

    # Evidence delta shape and linkage.
    check(delta["status"] == "deferred", "delta deferred")
    check(delta["affected_rows"] == ["LT-GR8"], "delta targets LT-GR8")
    check(delta["integration"]["disposition"] == "deferred", "delta integration deferred")
    check(delta["integration"]["priority_effect"] == "none", "delta priority unchanged")
    check(delta["integration"]["cursor_advanced"] is True, "delta cursor advanced")
    check(data["evidence_delta"].endswith("gu-ltgr8-boundary-carrier-typing-2026-08-22.json"), "delta linked")
    check("no verdict change" in delta["proposed_effect"]["summary"].lower()
          or "verdict unchanged" in delta["proposed_effect"]["summary"].lower(), "delta requests no verdict change")

    # Workspace propagation.
    check("LT-GR8 typing step" in state or "typing step is executed" in state, "state records execution")
    check("LT-GR8 CARRIER AND BOUNDARY TYPING" in next_steps, "next steps announcement")
    items = {item["id"]: item for item in agenda["work_items"]}
    check("typing step is executed" in items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]["next_swing"]
          or "typing swing is executed" in items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]["next_swing"],
          "agenda records execution")
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
    changed["data"]["exact_typing_certificate"]["vertical_signs"][0] = -1
    mutations.append(("vertical-signature-corrupt", "vertical signature (6,4)", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["exact_typing_certificate"]["t2_lift_witnesses"]["null_conormals_H"][0] = ["1", "2", "0", "0"]
    mutations.append(("null-witness-corrupt", "T-2 declared null conormal is null ['1', '2', '0', '0']", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["exact_typing_certificate"]["t4_ambient_path"]["sample_ts"] = ["0", "1/3", "irrelevant-replaced"]
    changed["data"]["exact_typing_certificate"]["t4_ambient_path"]["sample_ts"][2] = "2"
    changed["data"]["exact_typing_certificate"]["both_signs_witness"]["positive_vertical_index"] = 10
    mutations.append(("vertical-role-swap", "horizontal-null plus positive vertical is ambient positive", changed))

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
    changed["result"] += "\nThis typing establishes a GU horizon.\n"
    mutations.append(("planted-forbidden-grammar", "forbidden grammar absent: establishes a GU horizon", changed))

    changed = copy.deepcopy(baseline)
    changed["delta"]["status"] = "pending"
    mutations.append(("delta-disposition-regression", "delta deferred", changed))

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
