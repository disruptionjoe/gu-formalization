#!/usr/bin/env python3
"""Exact type and propagation probe for LT-GR8 D4 stress composition."""

from __future__ import annotations

import copy
import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/selected-k77-ltgr8-observed-stress-composition-typing.json"
RESULT = ROOT / "explorations/conditional-build/selected-k77-ltgr8-observed-stress-composition-typing-2026-08-23.md"
DELTA = ROOT / "lab/process/conditional-evidence-deltas/gu-ltgr8-observed-stress-composition-typing-2026-08-23.json"

FORBIDDEN_SUMMARY_GRAMMAR = (
    "establishes a physical horizon",
    "confirms Jacobson",
    "derives the Einstein equation",
    "constructs the Rindler flux",
    "awards confirmation credit",
)


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def rank(a: list[list[Fraction]]) -> int:
    m = [row[:] for row in a]
    rows = len(m)
    cols = len(m[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if m[r][col] != 0), None)
        if pivot is None:
            continue
        m[pivot_row], m[pivot] = m[pivot], m[pivot_row]
        scale = m[pivot_row][col]
        m[pivot_row] = [x / scale for x in m[pivot_row]]
        for r in range(rows):
            if r != pivot_row and m[r][col] != 0:
                factor = m[r][col]
                m[r] = [x - factor * y for x, y in zip(m[r], m[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def sym_coords(a: list[list[Fraction]]) -> list[Fraction]:
    return [a[i][j] for i in range(len(a)) for j in range(i, len(a))]


def pullback(d: list[list[Fraction]], t: list[list[Fraction]]) -> list[list[Fraction]]:
    return matmul(matmul(transpose(d), t), d)


def load_inputs() -> dict[str, object]:
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "delta": json.loads(DELTA.read_text()),
        "index": json.loads((ROOT / "lab/process/conditional-evidence-deltas/index.json").read_text()),
        "boundary": json.loads((ROOT / "lab/process/selected-k77-ltgr8-observed-boundary-carrier-typing.json").read_text()),
        "reverse": json.loads((ROOT / "lab/process/selected-k77-ltgr8-reverse-track-descent-r6-to-r3.json").read_text()),
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
    index = inputs["index"]
    boundary = inputs["boundary"]
    reverse = inputs["reverse"]
    state = inputs["state"]
    next_steps = inputs["next_steps"]
    agenda = inputs["agenda"]
    assert all(isinstance(x, dict) for x in (data, delta, index, boundary, reverse, agenda))
    assert all(isinstance(x, str) for x in (result, state, next_steps))

    d = [[Fraction(x) for x in row] for row in data["exact_certificate"]["section_jet"]]
    check(len(d) == 14 and all(len(row) == 4 for row in d), "section derivative is 14x4")
    check(d[:4] == [[Fraction(int(i == j)) for j in range(4)] for i in range(4)], "D begins with I4")
    check(rank(d) == 4, "section derivative rank four")

    # Existing T_H already lands in the observed metric Euler dual; re-pullback is ill-typed.
    existing = data["existing_stress"]
    check("B_X^!" in existing["formula"], "existing T_H codomain is observed B_X dual")
    check(existing["ambient_input_to_s_star"] is False, "existing T_H is not an ambient s-star input")
    check(existing["repullback_status"] == "ILL_TYPED_ALREADY_OBSERVED", "re-pullback is ill-typed")
    check("OWNED" in existing["density_pairing"], "existing observed density pairing preserved")
    check("WARD_EXACT" in existing["conservation"], "existing observed Ward theorem preserved")

    # Build the hypothetical linear map Sym^2(R^14)^* -> Sym^2(R^4)^* exactly.
    images: list[list[Fraction]] = []
    for i in range(14):
        for j in range(i, 14):
            basis = [[Fraction(0) for _ in range(14)] for _ in range(14)]
            basis[i][j] = 1
            basis[j][i] = 1
            images.append(sym_coords(pullback(d, basis)))
    linear_map = transpose(images)
    computed_rank = rank(linear_map)
    check(len(images) == 105, "ambient symmetric-tensor dimension 105")
    check(len(linear_map) == 10, "observed symmetric-tensor dimension 10")
    hypothetical = data["type_split"]["hypothetical_ambient_algebraic_symmetric_tensor_pullback"]
    check(computed_rank == hypothetical["rank"] == 10,
          "pullback rank 10")
    check(105 - computed_rank == hypothetical["kernel_dimension"] == 95,
          "pullback kernel dimension 95")
    check("INPUT_UNOWNED" in hypothetical["status"], "ambient Hilbert input unowned")

    # Symmetry and contraction-not-projection witness: a vertical T_44 contributes J_0 tensor J_0.
    vertical = [[Fraction(0) for _ in range(14)] for _ in range(14)]
    vertical[4][4] = 1
    observed = pullback(d, vertical)
    check(observed == transpose(observed), "pullback preserves symmetry")
    check(any(x != 0 for row in observed for x in row), "vertical block contributes through contraction")
    check(all(vertical[i][j] == 0 for i in range(4) for j in range(4)), "horizontal projection witness is zero")
    check(observed != [[Fraction(0) for _ in range(4)] for _ in range(4)], "contraction differs from projection")

    # Explicit nonzero kernel tensor n tensor n with D^T n = 0.
    n = [Fraction(-1), Fraction(-2), Fraction(0), Fraction(0), Fraction(1)] + [Fraction(0)] * 9
    check(matmul(transpose(d), [[x] for x in n]) == [[Fraction(0)] for _ in range(4)], "normal covector kills section tangent")
    kernel_t = [[x * y for y in n] for x in n]
    check(any(x != 0 for row in kernel_t for x in row), "kernel tensor is nonzero")
    check(pullback(d, kernel_t) == [[Fraction(0) for _ in range(4)] for _ in range(4)], "nonzero tensor pulls back to zero")

    # Density mismatch is a type check, not a numerical determinant substitute.
    cert = data["exact_certificate"]
    check(cert["density_source_dimension"] == 14 and cert["density_target_dimension"] == 4,
          "density dimensions differ 14 to 4")
    check(len(d) != len(d[0]), "D is rectangular and has no determinant")
    check(data["type_split"]["hypothetical_ambient_to_observed_stress_density"]["status"] == "MISSING_OWNER",
          "four-density owner missing")

    # Total variation counterexample: A(g,s)=g*s and s(g)=g at g=1.
    chain = cert["section_chain_control"]
    g = Fraction(chain["at_g"])
    direct = g
    total = 2 * g
    check(direct == chain["direct_derivative"] == 1, "direct fixed-section derivative is one")
    check(total == chain["total_derivative"] == 2, "total section-dependent derivative is two")
    check(direct != total, "section chain term is nonzero")

    # Conservation counterexample on s(x)=(x,x^2), T=diag(0,1), evaluated at x=1.
    x = Fraction(cert["conservation_counterexample"]["at_x"])
    metric = 1 + 4 * x * x
    gamma = 4 * x / metric
    pulled_t = 4 * x * x
    covariant = 8 * x - 2 * gamma * pulled_t
    raised = covariant / metric
    check(metric == 5, "counterexample induced metric five")
    check(covariant == Fraction(8, 5), "pullback covariant derivative 8/5")
    check(raised == Fraction(8, 25), "pullback raised divergence 8/25")
    check(data["type_split"]["hypothetical_pullback_conservation"]["status"] == "NOT_INHERITED",
          "conservation not inherited")

    # Claim ceiling and D4 disposition.
    check(data["observation_map"]["classification"] == "CONTRACTION_NOT_PROJECTION", "contraction classification")
    check("TYPING_COMPLETE" in data["d4_disposition"], "D4 typing complete")
    check("EXISTING_T_H_ALREADY_OBSERVED" in data["d4_disposition"], "existing stress already observed")
    check("CAUSAL_FLUX_MISSING" in data["d4_disposition"], "causal flux remains missing")
    check(data["mechanism_commitment"] == "NONE", "mechanism commitment NONE")
    check(data["confirmation_credit"] == "NONE", "confirmation credit NONE")
    check(data["ledger_verdict_change"] == "none", "ledger verdict unchanged")
    check(data["canon_verdict_change"] == "none", "canon unchanged")
    for phrase in FORBIDDEN_SUMMARY_GRAMMAR:
        check(phrase not in result, f"forbidden grammar absent: {phrase}")

    # Evidence delta and propagation.
    check(delta["status"] == "deferred", "delta deferred")
    check(delta["affected_rows"] == ["LT-GR8"], "delta targets LT-GR8")
    check(delta["integration"]["disposition"] == "deferred", "delta disposition deferred")
    check(index["integration_cursor"] == delta["delta_id"], "delta cursor advanced")
    check(any(item["delta_id"] == delta["delta_id"] and item["status"] == "deferred" for item in index["deltas"]),
          "delta indexed deferred")
    check("ALREADY_OBSERVED" in boundary["packet_component_status"]["stress_energy_flux"],
          "boundary packet refined")
    d4 = next(item for item in reverse["r2_r1_demand_interface"] if item["id"].startswith("D4_"))
    check("TYPING_COMPLETE" in d4["status"], "reverse D4 status complete")
    check("D6" in reverse["next_demand"], "reverse packet selects D6 next")
    check("D4" in state and "already lands in the observed" in state, "current state records D4 split")
    check("LT-GR8 D4" in next_steps, "next steps records D4")
    items = {item["id"]: item for item in agenda["work_items"]}
    check("D6" in items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]["next_swing"], "agenda selects D6 next")
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
    changed["data"]["existing_stress"]["ambient_input_to_s_star"] = True
    mutations.append(("repullback-smuggle", "existing T_H is not an ambient s-star input", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["exact_certificate"]["section_jet"][4] = [0, 0, 0, 0]
    mutations.append(("projection-smuggle", "vertical block contributes through contraction", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["type_split"]["hypothetical_ambient_algebraic_symmetric_tensor_pullback"]["kernel_dimension"] = 0
    mutations.append(("injectivity-smuggle", "pullback kernel dimension 95", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["type_split"]["hypothetical_ambient_to_observed_stress_density"]["status"] = "EXACT_AVAILABLE"
    mutations.append(("density-smuggle", "four-density owner missing", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["exact_certificate"]["section_chain_control"]["total_derivative"] = 1
    mutations.append(("chain-drop", "total section-dependent derivative is two", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["exact_certificate"]["conservation_counterexample"]["raised_divergence"] = "0"
    # The numerical registry field is claim evidence; make its status lie too so the probe must catch it.
    changed["data"]["type_split"]["hypothetical_pullback_conservation"]["status"] = "AUTOMATIC"
    mutations.append(("conservation-smuggle", "conservation not inherited", changed))

    changed = copy.deepcopy(baseline)
    changed["result"] += "\nThis contraction confirms Jacobson.\n"
    mutations.append(("confirmation-smuggle", "forbidden grammar absent: confirms Jacobson", changed))

    ok = True
    for name, expected, mutated in mutations:
        _, caught = collect_failures(mutated)
        if expected not in caught:
            print(f"[FAIL] mutation {name}: expected {expected!r}, got {caught!r}")
            ok = False
        else:
            print(f"MUTATION CAUGHT {name}: [FAIL] {expected}")
    print("FAILURE-PATH SELFTEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
